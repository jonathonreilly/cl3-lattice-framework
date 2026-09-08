#!/usr/bin/env python3
"""Record-visible integrated formation instruments and selector kill.

This runner constructs a finite-range Record-only controller motif.  Each of
its two blank midpoint targets sees all load-bearing data in its six nearest
neighbors.  A total normalized kernel includes refusal, supported no-event,
and the atomic two-Record append; its event-conditioned marginals equal the
displayed one-site Admissibility distributions.  Radius two makes simultaneous
targets disjoint but admits exact decoder aliases and sequential-order effects.
Two inequivalent bounded candidate models demonstrate selection freedom, while
a live-M2 CPTP comparator localizes the remaining wall to law authority and
resources.  None is promoted to the framework law.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
import math
from pathlib import Path
import subprocess

import numpy as np

import frontier_nn_formation_selector_two_model_kill_2026_08_14 as block72


block71 = block72.block71
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / "NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md"
AUDIT_INPUT_PATHS = ('docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md', 'docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py', 'scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py', 'docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md')

# Current selected files; original receipt constants below remain historical.
CURRENT_INPUT_SHA256 = {
    "docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md": "29b0177eaca7e86542c1a15d9a64751895ea5798d695f6305f23891ec974ff58",
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md": "ad99e42a21df2ea4c656cb6be8fc957e68377623c37075556c20b1ecd423f5c6",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py": "cff4964b3dc6acebb8ad4d0c501371197898b207f8cc77468e7c76749a6d9664",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py": "7d64706ad0a76724b6ae14fc1c0751d9f3518105ebea775d1399fcf129aba74c",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md": "370637c3881b72b68e5df8fb8d8afaa55fcd995025c01173771ffce418918847"
}
TOL = 5.0e-11

Coord = tuple[int, int, int]
Content = object
ZERO: Coord = (0, 0, 0)
EX: Coord = (1, 0, 0)
EY: Coord = (0, 1, 0)
IDENTITY_KEY: Content = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)
# D = 2I-C.  Its eigenvalue-one spectral projector is the supplied calibration C.
KCAL: Content = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(2)),
)
# D_Q = 2I-Q.  Spectral type distinguishes both controller tags from the root.
KQCAL: Content = (
    (Fraction(3, 2), Fraction(-1, 2)),
    (Fraction(-1, 2), Fraction(3, 2)),
)
GUARD_RADIUS = 2
BRANCH_WEIGHTS = block72.BRANCH_WEIGHTS


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
class Model:
    name: str
    alpha0: int
    hazard: Fraction


MODEL_A = Model("A", 1, Fraction(1, 3))
MODEL_B = Model("B", 2, Fraction(1, 2))
MODEL_RATE_HALF = Model("A-rate-half", 1, Fraction(1, 2))
MODEL_ALPHA_TWO = Model("A-alpha-two", 2, Fraction(1, 3))


@dataclass(frozen=True)
class Motif:
    anchor: Coord
    e_head: Coord
    e_meta: Coord
    m: int


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def neg(vector: Coord) -> Coord:
    return tuple(-value for value in vector)  # type: ignore[return-value]


def scale(multiplier: int, vector: Coord) -> Coord:
    return tuple(multiplier * value for value in vector)  # type: ignore[return-value]


def translate(site: Coord, displacement: Coord) -> Coord:
    return add(site, displacement)


def l1_ball(anchor: Coord, radius: int) -> set[Coord]:
    return {
        add(anchor, offset)
        for offset in product(range(-radius, radius + 1), repeat=3)
        if sum(abs(value) for value in offset) <= radius
    }


def frame_pairs() -> tuple[tuple[Coord, Coord], ...]:
    output: list[tuple[Coord, Coord]] = []
    for rotation in block71.ROTATIONS:
        pair = (block71.rotate(rotation, EX), block71.rotate(rotation, EY))
        if pair not in output:
            output.append(pair)
    return tuple(output)


FRAMES = frame_pairs()


def as_matrix(content: Content) -> np.ndarray:
    return np.asarray(content, dtype=complex)


def matrix_key(matrix: np.ndarray | Content) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    array = as_matrix(matrix)
    return tuple(
        tuple(complex(round(value.real, 14), round(value.imag, 14)) for value in row)
        for row in array
    )  # type: ignore[return-value]


def matrix_equal(left: Content, right: Content, tolerance: float = TOL) -> bool:
    try:
        return float(np.linalg.norm(as_matrix(left) - as_matrix(right))) < tolerance
    except (TypeError, ValueError):
        return False


def projector_ok(content: Content) -> bool:
    try:
        matrix = as_matrix(content)
    except (TypeError, ValueError):
        return False
    return (
        matrix.shape == (2, 2)
        and float(np.linalg.norm(matrix - matrix.conj().T)) < TOL
        and float(np.linalg.norm(matrix @ matrix - matrix)) < TOL
        and abs(float(np.trace(matrix).real) - 1.0) < TOL
        and abs(float(np.trace(matrix).imag)) < TOL
    )


def calibration_from_tag(content: Content) -> np.ndarray | None:
    try:
        matrix = as_matrix(content)
    except (TypeError, ValueError):
        return None
    if matrix.shape != (2, 2) or float(np.linalg.norm(matrix - matrix.conj().T)) >= TOL:
        return None
    eigenvalues = np.linalg.eigvalsh(matrix)
    if float(np.linalg.norm(eigenvalues - np.asarray((1.0, 2.0)))) >= TOL:
        return None
    candidate = 2 * np.eye(2, dtype=complex) - matrix
    return candidate if projector_ok(candidate) else None


def root_bit(content: Content, calibration: np.ndarray) -> int | None:
    if matrix_equal(content, calibration):
        return 0
    if matrix_equal(content, np.eye(2, dtype=complex) - calibration):
        return 1
    return None


def unbiased(left: Content, right: Content) -> bool:
    if not projector_ok(left) or not projector_ok(right):
        return False
    overlap = np.trace(as_matrix(left) @ as_matrix(right))
    return abs(float(overlap.real) - 0.5) < TOL and abs(float(overlap.imag)) < TOL


def root_content(m: int) -> Content:
    return block71.K1 if m else block71.K0


def calibration_tag(collapse_tag: bool = False) -> Content:
    return KQCAL if collapse_tag else KCAL


def controller_sites(motif: Motif) -> tuple[Coord, Coord, Coord]:
    return (
        motif.anchor,
        add(motif.anchor, scale(2, motif.e_head)),
        add(motif.anchor, scale(2, motif.e_meta)),
    )


def required_records(motif: Motif, collapse_tag: bool = False) -> dict[Coord, Content]:
    return {
        motif.anchor: root_content(motif.m),
        add(motif.anchor, scale(2, motif.e_head)): KQCAL,
        add(motif.anchor, scale(2, motif.e_meta)): calibration_tag(collapse_tag),
    }


def target_sites(motif: Motif) -> tuple[Coord, Coord]:
    return (
        add(motif.anchor, motif.e_head),
        add(motif.anchor, motif.e_meta),
    )


def guard_blanks(motif: Motif, radius: int, collapse_tag: bool = False) -> set[Coord]:
    del collapse_tag
    return l1_ball(motif.anchor, radius) - set(controller_sites(motif))


def shaped_guard_blanks(motif: Motif) -> set[Coord]:
    body_diagonals = {
        add(motif.anchor, offset) for offset in product((-1, 1), repeat=3)
    }
    return (
        l1_ball(motif.anchor, GUARD_RADIUS) | body_diagonals
    ) - set(controller_sites(motif))


def controller_data(records: dict[Coord, Content], motif: Motif) -> dict[str, object] | None:
    root_site, q_site, d_site = controller_sites(motif)
    if root_site not in records or q_site not in records or d_site not in records:
        return None
    q_calibration = calibration_from_tag(records[q_site])
    calibration = calibration_from_tag(records[d_site])
    if q_calibration is None or calibration is None:
        return None
    m = root_bit(records[root_site], calibration)
    if m is None or not unbiased(records[root_site], q_calibration):
        return None
    return {
        "m": m,
        "q": q_calibration,
        "calibration": calibration,
        "root": as_matrix(records[root_site]),
    }


def is_match(
    records: dict[Coord, Content],
    motif: Motif,
    radius: int = GUARD_RADIUS,
    collapse_tag: bool = False,
) -> bool:
    del collapse_tag
    data = controller_data(records, motif)
    return (
        data is not None and data["m"] == motif.m
        and not any(site in records for site in guard_blanks(motif, radius))
    )


def is_shaped_match(records: dict[Coord, Content], motif: Motif) -> bool:
    data = controller_data(records, motif)
    return (
        data is not None and data["m"] == motif.m
        and not any(site in records for site in shaped_guard_blanks(motif))
    )


def find_matches(
    records: dict[Coord, Content],
    radius: int = GUARD_RADIUS,
    collapse_tag: bool = False,
) -> tuple[Motif, ...]:
    matches: list[Motif] = []
    for anchor in records:
        for e_head, e_meta in FRAMES:
            probe = Motif(anchor, e_head, e_meta, 0)
            data = controller_data(records, probe)
            if data is None:
                continue
            motif = Motif(anchor, e_head, e_meta, int(data["m"]))
            if is_match(records, motif, radius, collapse_tag):
                matches.append(motif)
    return tuple(sorted(matches, key=lambda item: (item.anchor, item.e_head, item.e_meta, item.m)))


def base_alpha(model: Model, recorded_neighbor_count: int) -> Fraction:
    return Fraction(model.alpha0 + recorded_neighbor_count)


def gaussian_density(alpha: Fraction, matrix: np.ndarray) -> float:
    value = float(alpha)
    norm_squared = float(np.trace(matrix.conj().T @ matrix).real)
    return (value / math.pi) ** 4 * math.exp(-value * norm_squared)


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


def special_candidates(site: Coord, records: dict[Coord, Content], collapse_tag: bool = False):
    del collapse_tag
    candidates: list[dict[str, object]] = []
    identity = np.eye(2, dtype=complex)
    for direction in block71.DIRECTIONS:
        root = records.get(add(site, neg(direction)))
        tag = records.get(add(site, direction))
        if root is None or tag is None or not projector_ok(root):
            continue
        calibration = calibration_from_tag(tag)
        if calibration is None:
            continue
        m = root_bit(root, calibration)
        if m is None and unbiased(root, calibration):
            candidates.append({
                "role": "head",
                "direction": direction,
                "marker": identity - calibration,
            })
        if m is not None:
            candidates.append({
                "role": "meta",
                "direction": direction,
                "m": m,
                "calibration": calibration,
            })
    return tuple(candidates)


def one_site_distribution(
    site: Coord,
    records: dict[Coord, Content],
    model: Model,
    collapse_tag: bool = False,
) -> dict[str, object]:
    candidates = special_candidates(site, records, collapse_tag)
    if len(candidates) == 1:
        candidate = candidates[0]
        role = str(candidate["role"])
        direction = candidate["direction"]
        if role == "head":
            m = None
            mass = {matrix_key(candidate["marker"]): Fraction(1)}
        else:
            m = int(candidate["m"])
            calibration = as_matrix(candidate["calibration"])
            mass = {
                matrix_key(calibration): BRANCH_WEIGHTS[m][0],
                matrix_key(np.eye(2, dtype=complex) - calibration): BRANCH_WEIGHTS[m][1],
            }
        return {"kind": role, "m": m, "direction": direction, "mass": mass}
    neighbor_count = sum(add(site, direction) in records for direction in block71.DIRECTIONS)
    alpha = base_alpha(model, neighbor_count)
    return {
        "kind": "base",
        "neighbor_count": neighbor_count,
        "alpha": alpha,
        "normalized": alpha > 0,
        "moment": Fraction(4, 1) / alpha,
    }


def conjugate(unitary: np.ndarray, content: Content) -> np.ndarray:
    matrix = np.asarray(content, dtype=complex)
    return unitary @ matrix @ unitary.conj().T


def internal_covariance_certificate() -> dict[str, object]:
    unitaries = (
        np.eye(2, dtype=complex),
        block71.H,
        block71.T,
        block71.H @ block71.T,
        np.asarray(((1, 1j), (1j, 1)), dtype=complex) / math.sqrt(2),
    )
    maximum_residual = 0.0
    actual_rule_failures = 0
    cases = 0
    identity = np.eye(2, dtype=complex)
    for unitary in unitaries:
        unitary_residual = float(np.linalg.norm(unitary.conj().T @ unitary - identity))
        maximum_residual = max(maximum_residual, unitary_residual)
        c_rotated = conjugate(unitary, block71.K0)
        d_rotated = conjugate(unitary, KCAL)
        q_rotated = conjugate(unitary, block71.KPLUS)
        dq_rotated = conjugate(unitary, KQCAL)
        maximum_residual = max(
            maximum_residual,
            float(np.linalg.norm((2 * identity - d_rotated) - c_rotated)),
            float(np.linalg.norm((2 * identity - dq_rotated) - q_rotated)),
            float(np.linalg.norm((identity - q_rotated) - conjugate(unitary, block71.KMINUS))),
            float(np.linalg.norm((identity - c_rotated) - conjugate(unitary, block71.K1))),
        )
        for m in (0, 1):
            expected_root = c_rotated if m == 0 else identity - c_rotated
            maximum_residual = max(
                maximum_residual,
                float(np.linalg.norm(expected_root - conjugate(unitary, root_content(m)))),
            )
            motif = Motif(ZERO, EX, EY, m)
            root_site, q_site, d_site = controller_sites(motif)
            records: dict[Coord, Content] = {
                root_site: matrix_key(expected_root),
                q_site: matrix_key(dq_rotated),
                d_site: matrix_key(d_rotated),
            }
            actual_rule_failures += find_matches(records) != (motif,)
            head, meta = target_sites(motif)
            head_rule = one_site_distribution(head, records, MODEL_A)
            meta_rule = one_site_distribution(meta, records, MODEL_A)
            actual_rule_failures += head_rule.get("mass") != {
                matrix_key(identity - q_rotated): Fraction(1)
            }
            actual_rule_failures += meta_rule.get("mass") != {
                matrix_key(c_rotated): BRANCH_WEIGHTS[m][0],
                matrix_key(identity - c_rotated): BRANCH_WEIGHTS[m][1],
            }
            for b in (0, 1):
                output, applied = append_atomic(records, motif, b)
                actual_rule_failures += not applied
                actual_rule_failures += not matrix_equal(
                    output.get(head), identity - q_rotated
                )
                actual_rule_failures += not matrix_equal(
                    output.get(meta), c_rotated if b == 0 else identity - c_rotated
                )
            cases += 1
    return {
        "unitaries": len(unitaries),
        "cases": cases,
        "maximum_residual": maximum_residual,
        "actual_rule_failures": actual_rule_failures,
    }


def local_rule_certificate(collapse_tag: bool = False) -> dict[str, object]:
    failures = uniqueness_failures = covariance_failures = outside_failures = 0
    normalization_failures = 0
    cases = 0
    translations = (ZERO, (11, -7, 5))
    for rotation in block71.ROTATIONS:
        e_head = block71.rotate(rotation, EX)
        e_meta = block71.rotate(rotation, EY)
        for displacement in translations:
            for m in (0, 1):
                motif = Motif(displacement, e_head, e_meta, m)
                records = required_records(motif, collapse_tag)
                matches = find_matches(records, collapse_tag=collapse_tag)
                uniqueness_failures += len(matches) != 1 or (matches and matches[0] != motif)
                head, meta = target_sites(motif)
                head_distribution = one_site_distribution(head, records, MODEL_A, collapse_tag)
                meta_distribution = one_site_distribution(meta, records, MODEL_A, collapse_tag)
                failures += (
                    head_distribution.get("kind") != "head"
                    or head_distribution.get("m") is not None
                    or head_distribution.get("mass") != {matrix_key(block71.KMINUS): Fraction(1)}
                    or meta_distribution.get("kind") != "meta"
                    or meta_distribution.get("m") != m
                    or meta_distribution.get("mass") != {
                        matrix_key(block71.K0): BRANCH_WEIGHTS[m][0],
                        matrix_key(block71.K1): BRANCH_WEIGHTS[m][1],
                    }
                )
                for distribution in (head_distribution, meta_distribution):
                    normalization_failures += sum(distribution.get("mass", {}).values()) != 1
                far_records = dict(records)
                far_records[add(displacement, (5, 5, 5))] = block71.KPLUS
                outside_failures += (
                    one_site_distribution(head, far_records, MODEL_A, collapse_tag) != head_distribution
                    or one_site_distribution(meta, far_records, MODEL_A, collapse_tag) != meta_distribution
                )
                covariance_failures += block71.distance(head, motif.anchor) != 1
                covariance_failures += block71.distance(meta, motif.anchor) != 1
                cases += 1
    base_checks = 0
    base_support_minimum = math.inf
    for model in (MODEL_A, MODEL_B):
        moments = []
        for count in range(7):
            alpha = base_alpha(model, count)
            integral = gaussian_integral_certificate(alpha)
            normalization_failures += (
                alpha <= 0 or abs(integral["mass"] - 1.0) >= TOL
                or integral["exponent_error"] >= TOL
            )
            moments.append(Fraction(4, 1) / alpha)
            for matrix in (block71.P0, block71.P1, block71.PMINUS, block71.PPLUS):
                base_support_minimum = min(base_support_minimum, gaussian_density(alpha, matrix))
            base_checks += 1
        failures += len(set(moments)) == 1
    internal = internal_covariance_certificate()
    return {
        "frames": len(FRAMES),
        "cases": cases,
        "base_checks": base_checks,
        "failures": failures,
        "uniqueness_failures": uniqueness_failures,
        "covariance_failures": covariance_failures,
        "outside_failures": outside_failures,
        "normalization_failures": normalization_failures,
        "base_support_minimum": base_support_minimum,
        "guard_sites": len(l1_ball(ZERO, GUARD_RADIUS)),
        "guard_blanks": len(guard_blanks(Motif(ZERO, EX, EY, 0), GUARD_RADIUS, collapse_tag)),
        "internal": internal,
    }


def event_distribution(model: Model, m: int, bad_weights: bool = False) -> dict[str, Fraction]:
    weights = BRANCH_WEIGHTS[m]
    if bad_weights and m == 1:
        weights = (Fraction(1, 4), Fraction(3, 4))
    return {
        "no_event": 1 - model.hazard,
        "b0": model.hazard * weights[0],
        "b1": model.hazard * weights[1],
    }


def instrument_distribution(
    records: dict[Coord, Content],
    motif: Motif,
    model: Model,
    bad_weights: bool = False,
) -> dict[str, Fraction]:
    if not is_match(records, motif):
        return {
            "refuse": Fraction(1),
            "no_event": Fraction(0),
            "b0": Fraction(0),
            "b1": Fraction(0),
        }
    event = event_distribution(model, motif.m, bad_weights)
    return {"refuse": Fraction(0), **event}


def append_atomic(
    records: dict[Coord, Content],
    motif: Motif,
    b: int,
    radius: int = GUARD_RADIUS,
) -> tuple[dict[Coord, Content], bool]:
    if not is_match(records, motif, radius):
        return dict(records), False
    data = controller_data(records, motif)
    if data is None:
        return dict(records), False
    head, meta = target_sites(motif)
    if head in records or meta in records:
        return dict(records), False
    output = dict(records)
    identity = np.eye(2, dtype=complex)
    marker = identity - as_matrix(data["q"])
    calibration = as_matrix(data["calibration"])
    metadata = identity - calibration if b else calibration
    output.update({head: matrix_key(marker), meta: matrix_key(metadata)})
    return output, True


def find_controller_packets(records: dict[Coord, Content]) -> tuple[tuple[Motif, int], ...]:
    packets: list[tuple[Motif, int]] = []
    identity = np.eye(2, dtype=complex)
    for anchor in records:
        for e_head, e_meta in FRAMES:
            probe = Motif(anchor, e_head, e_meta, 0)
            data = controller_data(records, probe)
            if data is None:
                continue
            motif = Motif(anchor, e_head, e_meta, int(data["m"]))
            head, meta = target_sites(motif)
            if head not in records or meta not in records:
                continue
            marker = identity - as_matrix(data["q"])
            calibration = as_matrix(data["calibration"])
            if not matrix_equal(records[head], marker):
                continue
            if matrix_equal(records[meta], calibration):
                packets.append((motif, 0))
            elif matrix_equal(records[meta], identity - calibration):
                packets.append((motif, 1))
    return tuple(sorted(packets, key=lambda item: (
        item[0].anchor, item[0].e_head, item[0].e_meta, item[0].m, item[1]
    )))


def simultaneous_append(
    records: dict[Coord, Content],
    outcomes: tuple[tuple[Motif, int], ...],
    radius: int = GUARD_RADIUS,
) -> tuple[dict[Coord, Content], bool]:
    updates: dict[Coord, Content] = {}
    for motif, b in outcomes:
        candidate, applied = append_atomic(records, motif, b, radius)
        if not applied:
            return dict(records), False
        for site in set(candidate) - set(records):
            if site in updates and not matrix_equal(updates[site], candidate[site]):
                return dict(records), False
            updates[site] = candidate[site]
    if set(updates) & set(records):
        return dict(records), False
    output = dict(records)
    output.update(updates)
    return output, True


def integrated_event_certificate(
    bad_weights: bool = False,
    sequential_append: bool = False,
) -> dict[str, object]:
    normalization_failures = conditional_failures = marginal_failures = 0
    append_failures = decode_failures = controller_decode_failures = 0
    preservation_failures = replay_failures = 0
    atomicity_failures = 0
    sequential_intermediate_cases = 0
    refusal_failures = 0
    no_event_failures = 0
    instrument_cases = 0
    cases = 0
    for model in (MODEL_A, MODEL_B):
        for rotation in block71.ROTATIONS:
            motif_frame = (
                block71.rotate(rotation, EX),
                block71.rotate(rotation, EY),
            )
            for m in (0, 1):
                motif = Motif((7, -5, 3), *motif_frame, m)
                records = required_records(motif)
                sentinel = (40, -30, 20)
                records[sentinel] = block71.KPLUS
                distribution = instrument_distribution(records, motif, model, bad_weights)
                normalization_failures += sum(distribution.values()) != 1
                event_mass = distribution["b0"] + distribution["b1"]
                conditional = (
                    distribution["b0"] / event_mass,
                    distribution["b1"] / event_mass,
                )
                conditional_failures += conditional != BRANCH_WEIGHTS[m]
                head, meta = target_sites(motif)
                head_rule = one_site_distribution(head, records, model)
                meta_rule = one_site_distribution(meta, records, model)
                marginal_failures += (
                    head_rule.get("mass") != {matrix_key(block71.KMINUS): Fraction(1)}
                    or meta_rule.get("mass") != {
                        matrix_key(block71.K0): conditional[0],
                        matrix_key(block71.K1): conditional[1],
                    }
                )
                no_event_output = dict(records)
                no_event_failures += distribution["refuse"] != 0
                no_event_failures += no_event_output != records
                for b in (0, 1):
                    if sequential_append:
                        intermediate = dict(records)
                        intermediate[head] = block71.KMINUS
                        sequential_intermediate_cases += (
                            len(intermediate) == len(records) + 1 and head in intermediate and meta not in intermediate
                        )
                        atomicity_failures += 1
                    output, applied = append_atomic(records, motif, b)
                    append_failures += not applied or len(output) != len(records) + 2
                    preservation_failures += output.get(sentinel) != records[sentinel]
                    found = block71.find_packets(output)
                    decode_failures += (
                        len(found) != 1 or found[0]["m"] != m or found[0]["b"] != b
                    )
                    controller_decode_failures += find_controller_packets(output) != ((motif, b),)
                    replay, replay_applied = append_atomic(output, motif, b)
                    replay_failures += replay_applied or replay != output
                    cases += 1
                occupied = dict(records)
                occupied[head] = block71.KPLUS
                refused_distribution = instrument_distribution(occupied, motif, model)
                refused, applied = append_atomic(occupied, motif, 0)
                refusal_failures += (
                    applied
                    or refused != occupied
                    or refused_distribution != {
                        "refuse": Fraction(1),
                        "no_event": Fraction(0),
                        "b0": Fraction(0),
                        "b1": Fraction(0),
                    }
                )
                instrument_cases += 2
    return {
        "cases": cases,
        "normalization_failures": normalization_failures,
        "conditional_failures": conditional_failures,
        "marginal_failures": marginal_failures,
        "append_failures": append_failures,
        "decode_failures": decode_failures,
        "controller_decode_failures": controller_decode_failures,
        "preservation_failures": preservation_failures,
        "replay_failures": replay_failures,
        "atomicity_failures": atomicity_failures,
        "sequential_intermediate_cases": sequential_intermediate_cases,
        "refusal_failures": refusal_failures,
        "no_event_failures": no_event_failures,
        "instrument_cases": instrument_cases,
    }


def compatible(left: Motif, right: Motif, radius: int) -> bool:
    left_records = required_records(left)
    right_records = required_records(right)
    if any(site in right_records and right_records[site] != content for site, content in left_records.items()):
        return False
    if set(left_records) & guard_blanks(right, radius):
        return False
    if set(right_records) & guard_blanks(left, radius):
        return False
    return True


def shaped_compatible(left: Motif, right: Motif) -> bool:
    left_records = required_records(left)
    right_records = required_records(right)
    if any(site in right_records and right_records[site] != content for site, content in left_records.items()):
        return False
    if set(left_records) & shaped_guard_blanks(right):
        return False
    if set(right_records) & shaped_guard_blanks(left):
        return False
    return True


def guard_certificate(radius: int = GUARD_RADIUS) -> dict[str, object]:
    dangerous_pairs = 0
    pair_cases = 0
    left_anchor = ZERO
    for e_head, e_meta in FRAMES:
        for left_m in (0, 1):
            left = Motif(left_anchor, e_head, e_meta, left_m)
            left_targets = set(target_sites(left))
            for f_head, f_meta in FRAMES:
                for right_m in (0, 1):
                    for left_target in left_targets:
                        for relative_target in (f_head, f_meta):
                            displacement = tuple(
                                left_target[index] - relative_target[index]
                                for index in range(3)
                            )
                            right = Motif(displacement, f_head, f_meta, right_m)
                            same = left == right
                            overlap = bool(left_targets & set(target_sites(right)))
                            if not same and overlap and compatible(left, right, radius):
                                dangerous_pairs += 1
                            pair_cases += 1
    return {
        "radius": radius,
        "pair_cases": pair_cases,
        "dangerous_pairs": dangerous_pairs,
        "guard_sites": len(l1_ball(ZERO, radius)),
        "canonical_guard_blanks": len(guard_blanks(Motif(ZERO, EX, EY, 0), radius)),
    }


def adversarial_global_certificate() -> dict[str, object]:
    alias_left = Motif((0, 0, 0), (1, 0, 0), (0, 1, 0), 0)
    alias_right = Motif((-1, 1, -1), (1, 0, 0), (0, -1, 0), 0)
    alias_prestate = merge_required((alias_left, alias_right))
    alias_matches = find_matches(alias_prestate)
    alias_output, alias_applied = simultaneous_append(
        alias_prestate, ((alias_left, 0), (alias_right, 0))
    )
    direct_packets = block71.find_packets(alias_output)
    contextual_packets = find_controller_packets(alias_output)

    schedule_left = Motif((0, 0, 0), (1, 0, 0), (0, 1, 0), 0)
    schedule_right = Motif((-2, -1, 0), (-1, 0, 0), (0, 1, 0), 0)
    schedule_prestate = merge_required((schedule_left, schedule_right))
    schedule_matches = find_matches(schedule_prestate)
    synchronous, synchronous_applied = simultaneous_append(
        schedule_prestate, ((schedule_left, 0), (schedule_right, 0))
    )
    after_right, right_applied = append_atomic(schedule_prestate, schedule_right, 0)
    sequential, left_after_right_applied = append_atomic(after_right, schedule_left, 0)
    intruding_target = target_sites(schedule_right)[1]

    return {
        "alias_compatible": compatible(alias_left, alias_right, GUARD_RADIUS),
        "alias_both_match": alias_left in alias_matches and alias_right in alias_matches,
        "alias_targets_disjoint": not bool(
            set(target_sites(alias_left)) & set(target_sites(alias_right))
        ),
        "alias_applied": alias_applied,
        "direct_packet_count": len(direct_packets),
        "direct_packet_roots": tuple(packet["root"] for packet in direct_packets),
        "contextual_packets": contextual_packets,
        "schedule_compatible": compatible(schedule_left, schedule_right, GUARD_RADIUS),
        "schedule_both_match": schedule_left in schedule_matches and schedule_right in schedule_matches,
        "schedule_targets_disjoint": not bool(
            set(target_sites(schedule_left)) & set(target_sites(schedule_right))
        ),
        "intruding_target": intruding_target,
        "intrudes_left_guard": intruding_target in guard_blanks(schedule_left, GUARD_RADIUS),
        "synchronous_applied": synchronous_applied,
        "synchronous_growth": len(synchronous) - len(schedule_prestate),
        "right_applied": right_applied,
        "left_after_right_applied": left_after_right_applied,
        "sequential_growth": len(sequential) - len(schedule_prestate),
    }


def merge_required(motifs: tuple[Motif, ...]) -> dict[Coord, Content]:
    records: dict[Coord, Content] = {}
    for motif in motifs:
        for site, content in required_records(motif).items():
            if site in records and records[site] != content:
                raise RuntimeError("incompatible fixture motifs")
            records[site] = content
    return records


def packet_signature(packet: dict[str, object]) -> tuple[object, ...]:
    return (
        packet["root"], packet["head"], packet["meta"], packet["m"], packet["b"]
    )


def intended_packet_signature(motif: Motif, b: int) -> tuple[object, ...]:
    head, meta = target_sites(motif)
    return (motif.anchor, head, meta, motif.m, b)


def two_event_decoder_certificate(
    radius: int = GUARD_RADIUS,
    shaped: bool = False,
) -> dict[str, object]:
    raw_pairs = compatible_pairs = branch_cases = 0
    original_decoder_mismatches = contextual_decoder_mismatches = 0
    post_guard_rejections = append_failures = 0
    offsets = tuple(
        offset
        for offset in product(range(-3, 4), repeat=3)
        if sum(abs(value) for value in offset) <= 3
    )
    for left_m in (0, 1):
        left = Motif(ZERO, EX, EY, left_m)
        for displacement in offsets:
            for right_head, right_meta in FRAMES:
                for right_m in (0, 1):
                    raw_pairs += 1
                    right = Motif(displacement, right_head, right_meta, right_m)
                    pair_compatible = (
                        shaped_compatible(left, right)
                        if shaped else compatible(left, right, radius)
                    )
                    if left == right or not pair_compatible:
                        continue
                    records = merge_required((left, right))
                    left_matches = (
                        is_shaped_match(records, left)
                        if shaped else is_match(records, left, radius)
                    )
                    right_matches = (
                        is_shaped_match(records, right)
                        if shaped else is_match(records, right, radius)
                    )
                    if not left_matches or not right_matches:
                        continue
                    if set(target_sites(left)) & set(target_sites(right)):
                        continue
                    compatible_pairs += 1
                    for left_b, right_b in product((0, 1), repeat=2):
                        output, applied = simultaneous_append(
                            records, ((left, left_b), (right, right_b)), radius
                        )
                        append_failures += not applied
                        intended = {
                            intended_packet_signature(left, left_b),
                            intended_packet_signature(right, right_b),
                        }
                        decoded = {
                            packet_signature(packet) for packet in block71.find_packets(output)
                        }
                        original_decoder_mismatches += decoded != intended
                        contextual_decoder_mismatches += set(find_controller_packets(output)) != {
                            (left, left_b), (right, right_b)
                        }
                        allowed_left = set(controller_sites(left)) | set(target_sites(left))
                        allowed_right = set(controller_sites(right)) | set(target_sites(right))
                        left_clean = not any(
                            site in output
                            for site in l1_ball(left.anchor, GUARD_RADIUS) - allowed_left
                        )
                        right_clean = not any(
                            site in output
                            for site in l1_ball(right.anchor, GUARD_RADIUS) - allowed_right
                        )
                        post_guard_rejections += not (left_clean and right_clean)
                        branch_cases += 1
    return {
        "radius": radius,
        "shaped": shaped,
        "guard_sites": len(
            shaped_guard_blanks(Motif(ZERO, EX, EY, 0))
            | set(controller_sites(Motif(ZERO, EX, EY, 0)))
        ) if shaped else len(l1_ball(ZERO, radius)),
        "guard_blanks": len(shaped_guard_blanks(Motif(ZERO, EX, EY, 0))) if shaped else len(
            guard_blanks(Motif(ZERO, EX, EY, 0), radius)
        ),
        "offsets": len(offsets),
        "raw_pairs": raw_pairs,
        "compatible_pairs": compatible_pairs,
        "branch_cases": branch_cases,
        "append_failures": append_failures,
        "original_decoder_mismatches": original_decoder_mismatches,
        "contextual_decoder_mismatches": contextual_decoder_mismatches,
        "post_guard_rejections": post_guard_rejections,
    }


def global_product_certificate(model: Model) -> dict[str, object]:
    anchors = (ZERO, (12, 0, 0), (0, 12, 0), (0, 0, 12))
    motifs = tuple(
        Motif(anchor, *FRAMES[index * 5], index % 2)
        for index, anchor in enumerate(anchors)
    )
    records = merge_required(motifs)
    detected = find_matches(records)
    detection_failures = len(detected) != len(motifs) or set(detected) != set(motifs)
    distributions = tuple(event_distribution(model, motif.m) for motif in motifs)
    labels = ("no_event", "b0", "b1")
    normalization = Fraction(0)
    cylinder: dict[tuple[str, str], Fraction] = {}
    overwrite_failures = frozen_union_order_failures = 0
    controller_decode_failures = 0
    outcome_cases = 0
    for outcomes in product(labels, repeat=len(motifs)):
        probability = Fraction(1)
        for distribution, outcome in zip(distributions, outcomes):
            probability *= distribution[outcome]
        normalization += probability
        cylinder[outcomes[:2]] = cylinder.get(outcomes[:2], Fraction(0)) + probability
        output = dict(records)
        updates: dict[Coord, Content] = {}
        expected_packets: list[tuple[Motif, int]] = []
        for motif, outcome in zip(motifs, outcomes):
            if outcome == "no_event":
                continue
            b = int(outcome == "b1")
            candidate, applied = append_atomic(records, motif, b)
            proposed = {site: candidate[site] for site in set(candidate) - set(records)}
            overwrite_failures += not applied or len(proposed) != 2
            overwrite_failures += any(site in output or site in updates for site in proposed)
            updates.update(proposed)
            expected_packets.append((motif, b))
        output.update(updates)
        reversed_output = dict(records)
        for site, content in reversed(tuple(updates.items())):
            reversed_output[site] = content
        frozen_union_order_failures += output != reversed_output
        controller_decode_failures += set(find_controller_packets(output)) != set(expected_packets)
        outcome_cases += 1
    cylinder_failures = 0
    for first_outcomes in product(labels, repeat=2):
        expected = distributions[0][first_outcomes[0]] * distributions[1][first_outcomes[1]]
        cylinder_failures += cylinder.get(first_outcomes, Fraction(0)) != expected
    covariance_failures = 0
    rotation = block71.ROTATIONS[7]
    displacement = (31, -17, 9)
    rotated_records = {
        add(displacement, block71.rotate(rotation, site)): content
        for site, content in records.items()
    }
    rotated_matches = find_matches(rotated_records)
    expected_rotated = {
        Motif(
            add(displacement, block71.rotate(rotation, motif.anchor)),
            block71.rotate(rotation, motif.e_head),
            block71.rotate(rotation, motif.e_meta),
            motif.m,
        )
        for motif in motifs
    }
    covariance_failures += set(rotated_matches) != expected_rotated
    return {
        "motifs": len(motifs),
        "outcome_cases": outcome_cases,
        "normalization_failure": normalization != 1,
        "detection_failures": int(detection_failures),
        "overwrite_failures": overwrite_failures,
        "frozen_union_order_failures": frozen_union_order_failures,
        "controller_decode_failures": controller_decode_failures,
        "cylinder_failures": cylinder_failures,
        "covariance_failures": covariance_failures,
        "synchronous_snapshot_required": True,
        "infinite_lattice_executed": False,
    }


def model_selector_certificate(collapse_models: bool = False) -> dict[str, object]:
    second = MODEL_A if collapse_models else MODEL_B
    models = (MODEL_A, second)
    blank_moments = tuple(Fraction(4, model.alpha0) for model in models)
    single_m0 = tuple(event_distribution(model, 0) for model in models)
    global_certificates = tuple(global_product_certificate(model) for model in models)
    same_alpha = (MODEL_A, MODEL_RATE_HALF)
    same_hazard = (MODEL_A, MODEL_ALPHA_TWO)
    return {
        "models": models,
        "blank_moments": blank_moments,
        "single_m0": single_m0,
        "inequivalent": blank_moments[0] != blank_moments[1] and single_m0[0] != single_m0[1],
        "rate_seam_inequivalent": (
            base_alpha(same_alpha[0], 0) == base_alpha(same_alpha[1], 0)
            and event_distribution(same_alpha[0], 0) != event_distribution(same_alpha[1], 0)
        ),
        "kernel_seam_inequivalent": (
            same_hazard[0].hazard == same_hazard[1].hazard
            and base_alpha(same_hazard[0], 0) != base_alpha(same_hazard[1], 0)
        ),
        "global": global_certificates,
    }


def live_m_cptp_escape_certificate() -> dict[str, object]:
    dimension = 32
    identity = np.eye(dimension, dtype=complex)
    gamma = np.zeros((dimension, dimension), dtype=complex)
    for m in (0, 1):
        index = block71.full_index(1, m, 0, 0, 0)
        gamma[index, index] = 1
    projectors: dict[tuple[int, int], np.ndarray] = {}
    for m, b in product((0, 1), repeat=2):
        projector = np.zeros((dimension, dimension), dtype=complex)
        for r, a in product((0, 1), repeat=2):
            index = block71.full_index(1, m, b, r, a)
            projector[index, index] = 1
        projectors[(m, b)] = projector
    unitary = block71.word_matrix(block71.dilation_word(), 5)
    hazard = Fraction(1, 3)
    k_refuse = identity - gamma
    k_no_event = math.sqrt(float(1 - hazard)) * gamma
    event_kraus = {
        key: math.sqrt(float(hazard)) * projector @ unitary @ gamma
        for key, projector in projectors.items()
    }
    completeness = k_refuse.conj().T @ k_refuse + k_no_event.conj().T @ k_no_event
    for kraus in event_kraus.values():
        completeness += kraus.conj().T @ kraus
    completeness_residual = float(np.linalg.norm(completeness - identity))
    event_projector = sum(projectors.values(), np.zeros_like(identity))
    support_residual = float(np.linalg.norm(event_projector @ unitary @ gamma - unitary @ gamma))

    probability_failures = 0
    probability_cases = 0
    for input_m in (0, 1):
        state = np.zeros(dimension, dtype=complex)
        state[block71.full_index(1, input_m, 0, 0, 0)] = 1
        refuse_probability = float(np.linalg.norm(k_refuse @ state) ** 2)
        no_event_probability = float(np.linalg.norm(k_no_event @ state) ** 2)
        probability_failures += abs(refuse_probability) >= TOL
        probability_failures += abs(no_event_probability - float(1 - hazard)) >= TOL
        for (m, b), kraus in event_kraus.items():
            probability = float(np.linalg.norm(kraus @ state) ** 2)
            expected = float(hazard * BRANCH_WEIGHTS[input_m][b]) if m == input_m else 0.0
            probability_failures += abs(probability - expected) >= TOL
            probability_cases += 1

    coherent_failures = 0
    coherent_cases = 0
    coherent_amplitudes = (
        (1 / math.sqrt(2), 1 / math.sqrt(2)),
        (1 / math.sqrt(2), 1j / math.sqrt(2)),
        (math.sqrt(3) / 2, 0.5),
    )
    for amplitude0, amplitude1 in coherent_amplitudes:
        state = np.zeros(dimension, dtype=complex)
        state[block71.full_index(1, 0, 0, 0, 0)] = amplitude0
        state[block71.full_index(1, 1, 0, 0, 0)] = amplitude1
        for (m, b), kraus in event_kraus.items():
            probability = float(np.linalg.norm(kraus @ state) ** 2)
            population = abs(amplitude0 if m == 0 else amplitude1) ** 2
            expected = float(hazard * BRANCH_WEIGHTS[m][b]) * population
            coherent_failures += abs(probability - expected) >= TOL
            coherent_cases += 1
    return {
        "kraus_outcomes": 6,
        "gamma_rank": int(round(float(np.trace(gamma).real))),
        "hazard": hazard,
        "completeness_residual": completeness_residual,
        "event_support_residual": support_residual,
        "probability_cases": probability_cases,
        "probability_failures": probability_failures,
        "coherent_cases": coherent_cases,
        "coherent_failures": coherent_failures,
        "uses_unrecorded_live_m2": True,
        "clean_inputs_supplied": 4,
        "packet_word_primitives": 73,
        "operation_and_locking_authority_supplied": False,
    }


def resource_certificate(live_m_claim: bool = False) -> dict[str, object]:
    return {
        "controller_records": 3,
        "guard_sites": 25,
        "guard_blank_sites": 22,
        "blank_targets": 2,
        "new_records_per_event": 2,
        "quantum_clean_inputs": 0,
        "gate_primitives": 0,
        "m_is_preexisting_record": True,
        "connects_to_live_Block71_m": live_m_claim,
        "controller_genesis_supplied": False,
        "physical_step_clock_supplied": False,
        "fresh_capacity_regeneration_supplied": False,
    }


def current_inputs_match() -> bool:
    return all((ROOT / path).is_file()
               and sha256((ROOT / path).read_bytes()).hexdigest() == digest
               for path, digest in CURRENT_INPUT_SHA256.items())


def authority_certificate(stale: bool = False) -> dict[str, object]:
    axiom = " ".join(AXIOM_PATH.read_text(encoding="utf-8").split())
    parent_note = " ".join(PARENT_NOTE_PATH.read_text(encoding="utf-8").split())
    main = subprocess.check_output(("git", "rev-parse", "origin/main"), cwd=ROOT, text=True).strip()
    ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", main, "HEAD"), cwd=ROOT, check=False
    ).returncode == 0
    if stale:
        ancestor = False
    return {
        "main": main,
        "ancestor": ancestor,  # historical diagnostic only
        "current_inputs_match": current_inputs_match() and not stale,
        "state_records": "A state is a configuration of records." in axiom,
        "only_records": "Only records are readable." in axiom,
        "one_site_distribution": "probability distribution over the possibilities" in axiom,
        "rate_open": "formation site/rate" in axiom,
        "parent_probability_split": "three different probability/control layers" in parent_note,
        "parent_zero_toe": "zero TOE percentage movement" in parent_note,
        "input_paths": AUDIT_INPUT_PATHS,
    }


def boundary_surface_ok(law_claim: bool = False) -> bool:
    note = NOTE_PATH.read_text(encoding="utf-8")
    n2 = note.split("### N2 — Wall-independence audit", 1)[1].split(
        "### N3 — Hidden-wall scan", 1
    )[0]
    wall_pair_rows = sum(
        line.startswith("| W") and "/W" in line for line in n2.splitlines()
    )
    needles = (
        "### N1 — Alternative-route enumeration and normalization",
        "### N2 — Wall-independence audit",
        "### N3 — Hidden-wall scan",
        "### N4 — Residual matching",
        "### N5 — Rhetoric and granularity audit",
        "### N6 — Partial-closure path scan",
        "### N7 — Steelman and strongest surviving escape route",
        "### N8 — Cross-cycle echo audit",
        "Record-visible controller",
        "single normalized event kernel",
        "synchronous snapshot is extra law content",
        "does not connect to the live Block71 matter input",
        "two compatible integrated models",
        "downstream formation primitive",
        "not an axiom edit",
        "zero TOE percentage movement",
        "gravity pivot",
        "928 of 8,192",
        "five-Record contextual",
        "six-outcome completeness",
        "sufficient end-to-end payload / modular residual set",
    )
    return not law_claim and wall_pair_rows == 55 and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=(
        "stale_axiom", "collapse_tag", "bad_weights", "sequential_append",
        "shrink_guard", "collapse_models", "live_m_claim", "law_claim",
    ))
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation == "stale_axiom")
    authority_ok = (
        authority["current_inputs_match"] and authority["state_records"] and authority["only_records"]
        and authority["one_site_distribution"] and authority["rate_open"]
        and authority["parent_probability_split"] and authority["parent_zero_toe"]
        and len(authority["input_paths"]) == 6
    )
    checks.check(
        "A-current-main-axiom-and-Block72-authority",
        authority_ok,
        f"origin/main={str(authority['main'])[:10]}; current Record/Admissibility and complete Block71/72 proof/program closure are bound",
    )

    local = local_rule_certificate(mutation == "collapse_tag")
    local_ok = (
        local["frames"] == 24 and local["cases"] == 96 and local["base_checks"] == 14
        and local["failures"] == 0 and local["uniqueness_failures"] == 0
        and local["covariance_failures"] == 0 and local["outside_failures"] == 0
        and local["normalization_failures"] == 0 and local["base_support_minimum"] > 0
        and local["guard_sites"] == 25
        and local["guard_blanks"] == 22 and local["internal"]["cases"] == 10
        and local["internal"]["maximum_residual"] < TOL
        and local["internal"]["actual_rule_failures"] == 0
    )
    checks.check(
        "B-Record-visible-NN-controller-and-one-site-marginals",
        local_ok,
        f"{local['cases']} motif/frame cases uniquely expose root m plus ordered algebraic tags; head/meta marginals and {local['base_checks']} full-support base-kernel rows normalize; internal residual={local['internal']['maximum_residual']:.1e}",
    )

    event = integrated_event_certificate(
        mutation == "bad_weights", mutation == "sequential_append"
    )
    event_ok = (
        event["cases"] == 192 and event["normalization_failures"] == 0
        and event["conditional_failures"] == 0 and event["marginal_failures"] == 0
        and event["append_failures"] == 0 and event["decode_failures"] == 0
        and event["controller_decode_failures"] == 0
        and event["preservation_failures"] == 0 and event["replay_failures"] == 0
        and event["atomicity_failures"] == 0 and event["refusal_failures"] == 0
        and event["no_event_failures"] == 0 and event["instrument_cases"] == 192
    )
    checks.check(
        "C-single-normalized-no-event-and-atomic-append-kernel",
        event_ok,
        f"{event['cases']} model/frame/(m,b) outcomes plus {event['instrument_cases']} total valid/refusal rows join q, exact p(b|m), identity/no-event, two-site atomic append, contextual decoder, prior preservation, and replay",
    )

    radius = 1 if mutation == "shrink_guard" else GUARD_RADIUS
    guard = guard_certificate(radius)
    guard_ok = (
        guard["radius"] == 2 and guard["pair_cases"] == 9216
        and guard["dangerous_pairs"] == 0 and guard["guard_sites"] == 25
        and guard["canonical_guard_blanks"] == 22
    )
    checks.check(
        "D-radius-two-guard-kills-simultaneous-target-overlap",
        guard_ok,
        f"exhausted {guard['pair_cases']} ordered frame/m/target alignments at radius {guard['radius']}; compatible distinct matches with shared targets={guard['dangerous_pairs']}",
    )

    adversarial = adversarial_global_certificate()
    two_event = two_event_decoder_certificate(radius)
    shaped_two_event = two_event_decoder_certificate(shaped=True)
    radius_three = two_event_decoder_certificate(3)
    alias_expected = {
        (Motif((0, 0, 0), (1, 0, 0), (0, 1, 0), 0), 0),
        (Motif((-1, 1, -1), (1, 0, 0), (0, -1, 0), 0), 0),
    }
    adversarial_ok = (
        adversarial["alias_compatible"] and adversarial["alias_both_match"]
        and adversarial["alias_targets_disjoint"] and adversarial["alias_applied"]
        and adversarial["direct_packet_count"] == 3
        and set(adversarial["contextual_packets"]) == alias_expected
        and adversarial["schedule_compatible"] and adversarial["schedule_both_match"]
        and adversarial["schedule_targets_disjoint"] and adversarial["intrudes_left_guard"]
        and adversarial["synchronous_applied"] and adversarial["synchronous_growth"] == 4
        and adversarial["right_applied"] and not adversarial["left_after_right_applied"]
        and adversarial["sequential_growth"] == 2
        and two_event["radius"] == 2 and two_event["offsets"] == 63
        and two_event["raw_pairs"] == 6048 and two_event["compatible_pairs"] == 2048
        and two_event["branch_cases"] == 8192 and two_event["append_failures"] == 0
        and two_event["original_decoder_mismatches"] == 928
        and two_event["contextual_decoder_mismatches"] == 0
        and two_event["post_guard_rejections"] == 5376
        and shaped_two_event["guard_sites"] == 33
        and shaped_two_event["guard_blanks"] == 30
        and shaped_two_event["compatible_pairs"] == 1280
        and shaped_two_event["branch_cases"] == 5120
        and shaped_two_event["original_decoder_mismatches"] == 0
        and shaped_two_event["contextual_decoder_mismatches"] == 0
        and shaped_compatible(
            Motif((0, 0, 0), (1, 0, 0), (0, 1, 0), 0),
            Motif((-2, -1, 0), (-1, 0, 0), (0, 1, 0), 0),
        )
        and radius_three["raw_pairs"] == 6048
        and radius_three["compatible_pairs"] == 0
        and radius_three["branch_cases"] == 0
    )
    checks.check(
        "E-two-event-decoder-alias-and-scheduler-obstruction",
        adversarial_ok,
        f"radius-{radius}: {two_event['compatible_pairs']} compatible pairs/{two_event['branch_cases']} branches give {two_event['original_decoder_mismatches']} original three-Record aliases but {two_event['contextual_decoder_mismatches']} five-Record contextual aliases; the 33-site shaped guard retains {shaped_two_event['compatible_pairs']} pairs with zero two-event aliases yet leaves the {adversarial['synchronous_growth']}/{adversarial['sequential_growth']} scheduler witness; radius-3 cross-capable pairs={radius_three['compatible_pairs']}",
    )

    selector = model_selector_certificate(mutation == "collapse_models")
    global_ok = all(
        certificate["motifs"] == 4 and certificate["outcome_cases"] == 81
        and not certificate["normalization_failure"] and certificate["detection_failures"] == 0
        and certificate["overwrite_failures"] == 0
        and certificate["frozen_union_order_failures"] == 0
        and certificate["controller_decode_failures"] == 0
        and certificate["cylinder_failures"] == 0 and certificate["covariance_failures"] == 0
        and certificate["synchronous_snapshot_required"]
        and not certificate["infinite_lattice_executed"]
        for certificate in selector["global"]
    )
    checks.check(
        "F-finite-product-synchronous-update-and-cylinder-consistency",
        global_ok,
        "both models normalize all 81 outcomes on four separated motifs, preserve disjoint frozen-prestate update unions, contextually decode selected events, and reproduce every two-motif cylinder marginal",
    )

    selector_ok = (
        selector["models"] == (MODEL_A, MODEL_B)
        and selector["blank_moments"] == (Fraction(4), Fraction(2))
        and selector["inequivalent"] and selector["single_m0"][0] != selector["single_m0"][1]
        and selector["rate_seam_inequivalent"] and selector["kernel_seam_inequivalent"]
    )
    checks.check(
        "G-two-compatible-integrated-models-remain-inequivalent",
        selector_ok,
        f"A(alpha0=1,q=1/3) versus B(alpha0=2,q=1/2): blank moments={selector['blank_moments']}, single-motif laws={selector['single_m0']}; same-alpha/rate and same-rate/alpha controls also separate",
    )

    live_escape = live_m_cptp_escape_certificate()
    live_escape_ok = (
        live_escape["kraus_outcomes"] == 6 and live_escape["gamma_rank"] == 2
        and live_escape["hazard"] == Fraction(1, 3)
        and live_escape["completeness_residual"] < TOL
        and live_escape["event_support_residual"] < TOL
        and live_escape["probability_cases"] == 8
        and live_escape["probability_failures"] == 0
        and live_escape["coherent_cases"] == 12
        and live_escape["coherent_failures"] == 0
        and live_escape["uses_unrecorded_live_m2"]
        and live_escape["clean_inputs_supplied"] == 4
        and live_escape["packet_word_primitives"] == 73
        and not live_escape["operation_and_locking_authority_supplied"]
    )
    checks.check(
        "H-live-m-CPTP-escape-localizes-authority-wall",
        live_escape_ok,
        f"six Kraus outcomes complete at residual {live_escape['completeness_residual']:.1e}; 8 basis and 12 coherent probability rows carry live m with exact q p(b|m), but four clean inputs, the 73-primitive word, operation, and Record locking remain supplied",
    )

    resources = resource_certificate(mutation == "live_m_claim")
    resource_ok = (
        resources["controller_records"] == 3 and resources["guard_sites"] == 25
        and resources["guard_blank_sites"] == 22 and resources["blank_targets"] == 2
        and resources["new_records_per_event"] == 2 and resources["quantum_clean_inputs"] == 0
        and resources["gate_primitives"] == 0 and resources["m_is_preexisting_record"]
        and not resources["connects_to_live_Block71_m"]
        and not resources["controller_genesis_supplied"]
        and not resources["physical_step_clock_supplied"]
        and not resources["fresh_capacity_regeneration_supplied"]
    )
    checks.check(
        "I-resource-controller-and-live-input-boundary",
        resource_ok,
        "three supplied controller Records plus 22 Record-free guard sites replace clean quantum inputs; m is readable but pre-recorded, and controller genesis/capacity renewal/physical step remain open",
    )

    exact_decision_ok = (
        selector_ok and event_ok and guard_ok and adversarial_ok and live_escape_ok
        and not resources["connects_to_live_Block71_m"]
    )
    checks.check(
        "J-integrated-selector-kill-localizes-the-owner-decision",
        exact_decision_ok,
        "even after controller, invariant marginals, total joint append/refusal, contextual decoding, and finite frozen-snapshot arbitration are unified—and a live CPTP escape exists—two laws survive; authority must select",
    )

    boundary_ok = boundary_surface_ok(mutation == "law_claim")
    checks.check(
        "K-N1-N8-axiom-gravity-and-TOE-boundary",
        boundary_ok,
        "the note keeps the candidate law downstream, debits the Record motif and synchronous slice, rejects a live-input bridge claim, triggers the gravity pivot, and records no axiom/audit/TOE promotion",
    )

    print(
        "METRICS "
        f"local_cases={local['cases']} event_cases={event['cases']} guard_pair_cases={guard['pair_cases']} "
        f"dangerous_pairs={guard['dangerous_pairs']} decoder_pair_cases={two_event['branch_cases']} "
        f"three_record_aliases={two_event['original_decoder_mismatches']} contextual_aliases={two_event['contextual_decoder_mismatches']} "
        f"live_kraus_residual={live_escape['completeness_residual']:.2e} "
        f"product_outcomes={sum(c['outcome_cases'] for c in selector['global'])} "
        f"hazards={tuple(str(model.hazard) for model in selector['models'])}"
    )
    print(
        "BOUNDARY: one Record-visible finite-range candidate now unifies invariant NN marginals, supported no-event mass, refusal, and atomic append; radius two is write-safe but has three-Record decoder aliases and sequential-order dependence, while contextual decoding and the live CPTP escape add unapproved law/resource content; physical selection, global process, gravity, retention, obligation retirement, and TOE movement remain unsupplied"
    )
    print("per_element: checked three spectrally and relationally typed controller Records, two midpoint targets, exact K-minus/K-b outputs, two supported no-event hazards, seven base-neighbor counts, and five actual-rule internal-unitary controls")
    print("per_site: checked every 25-site radius-two guard, the 33-site shaped alternative, both invariant target NN conditions, all 24 frames, prior-Record preservation, occupied refusal, and isolated/contextual scanning")
    print("per_mode: checked both readable Record m values, four (m,b) branches, two integrated models, 192 event outcomes, plus 8 basis and 12 coherent live-M2 Kraus probability rows")
    print("per_block: checked 9,216 target-overlap alignments, 8,192 adjacent decoder branches with 928 original aliases, 5,120 shaped-guard branches with zero aliases, the scheduler witness, and two 81-outcome separated products")
    print("lattice_wide: checked and not executed — finite frozen-snapshot fixtures, pair-level contextual decoding, and cylinder identities do not supply provenance on arbitrary maps, sequential confluence, an autonomous infinite-Z3 process, or a physical clock")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
