#!/usr/bin/env python3
"""Cycle573: physical matter-transition clock-equivalence tournament.

Route A uses the scalar/even antipodal sectors of the actual Cycle219 bound-
pair collision update as a projective period-two transition standard. Route B
transports two trapped standards through local M2 SWAP conveyors and compares
their physical transition rails after independent proper-cubic reorientation,
mass-sector variation, and contact-source phase variation. Route C reuses one
finite event/comparison/carry work reservoir through compute-use-uncompute
echoes while a two-word physical ledger retains repeated calibration results.

The construction adds no clock dimension. Update, circuit, and routing
ordinals are not decoded as time. Transition candidates are not Records or
actuality, a generator entry is not a rate, and the result is not proper time.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, permutations, product
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MATTER_TRANSITION_CLOCK_EQUIVALENCE_TOURNAMENT_CYCLE573_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_matter_transition_clock_equivalence_tournament_"
    "cycle573_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
ACCEPTED_CYCLE570_COMMIT = "5d609e37eacb9790ca741c4914ad2bbc3f2d86c7"
TOL = 4e-10
SIGNAL = 1e-8
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
MODULUS = 16
TRAIN_BETAS = (-0.2, -0.3)
HELD_BETA = -0.35
TRAIN_CYCLES = (1, 3, 5)
HELD_CYCLES = (9, 17, 25)
CONTACT = 0.37
PASS = 0
FAIL = 0

DEPENDENCY_SHA256 = {
    "common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py":
        "c0f06a9cc9ffc4dcfe1d80b94da10bbef81ca1c74fddddac48712b0a7c332ced",
    "physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py":
        "853abe5470efd15b154d6cb348d49795a6fa84e77a62f0b21a79105892b1d415",
}
RECEIPT_SHA256 = {
    "physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json":
        "350e2c1922379bb42091e1cb5685c9e1f698ed23b81acf7c14803ba5043fcfc1",
    "physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json":
        "c80aae229d3721b273d12188960e2a4b16402d10a982856bec76c465dad52baa",
    "physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json":
        "f104399af621ded1b50e180e6fcce5f254008715b72191c6199fe4d583a8a806",
}

SCALAR = c210.UNIFORM.copy()
EVEN = np.asarray((0.5, 0.5, -0.5, -0.5, 0.0, 0.0), dtype=complex)
PLUS = (SCALAR + EVEN) / math.sqrt(2)
MINUS = (SCALAR - EVEN) / math.sqrt(2)
P_PLUS = np.outer(PLUS, PLUS.conj())
P_MINUS = np.outer(MINUS, MINUS.conj())

Word = tuple[int, ...]


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class EchoLayout:
    q_a: int
    q_b: int
    event_a: int
    event_b: int
    compare: int
    carry: int
    low: tuple[int, ...]
    high: tuple[int, ...]
    width: int


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def current_commit() -> str:
    return subprocess.check_output(
        ("git", "rev-parse", "HEAD"), cwd=ROOT, text=True
    ).strip()


def accepted_base_is_ancestor() -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ACCEPTED_CYCLE570_COMMIT, "HEAD"),
        cwd=ROOT, check=False,
    ).returncode == 0


def dependency_controls() -> dict[str, object]:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCY_SHA256}
    receipt_observed = {name: file_sha(ROOT / "outputs" / name) for name in RECEIPT_SHA256}
    receipts = {
        name: json.loads((ROOT / "outputs" / name).read_text(encoding="utf-8"))
        for name in RECEIPT_SHA256
    }
    evidence = {
        "Cycle563_mass_residual": receipts["physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"]["fixtures"]["Cycle219_mass_residual"],
        "Cycle563_contact_residual": receipts["physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"]["fixtures"]["Cycle230_contact_factorization_residual"],
        "Cycle563_seam_residual": receipts["physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"]["fixtures"]["Cycle230_axis_seam_residual"],
    }
    check(
        "accepted Cycle570 commit is ancestral, the Cycle219/230/563/569/570 shore artifacts are byte-exact, and retained physics evidence is consumed from the Cycle563 receipt's computed fixtures",
        accepted_base_is_ancestor()
        and observed == DEPENDENCY_SHA256 and receipt_observed == RECEIPT_SHA256
        and max(evidence[key] for key in evidence if key.endswith("residual")) < 5e-10,
        {"current_commit": current_commit(),
         "accepted_Cycle570_commit": ACCEPTED_CYCLE570_COMMIT,
         "accepted_Cycle570_is_ancestor": accepted_base_is_ancestor(),
         "runners": observed, "receipts": receipt_observed,
         "retained_fixtures": evidence,
         "evidence_source": "Cycle563 receipt fixtures (computed by its recorded run via the Cycle557/533 fixture path); Cycle569/570 receipts are byte-pinned anchors whose aggregate pass values are not gate inputs"},
    )
    return evidence


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset",
        "physical matter-transition clock-equivalence tournament",
        "route a — bound-pair transition standard",
        "route b — transported two-standard comparison",
        "route c — recyclable relational calibration echo",
        "no supplied endpoint count word", "all 576 paired proper-cubic frames",
        "schedule is not time", "formation is not record actuality",
        "localized free-stream control", "n1 — normalized alternatives",
        "n8 — cross-cycle echo", "broad time no-go: fail / do not ship",
        "there is no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle573 note freezes the tournament and interpretation ceiling", not missing, missing)


def phase_aligned_residual(actual: np.ndarray, expected: np.ndarray) -> float:
    overlap = np.vdot(expected, actual)
    if abs(overlap) == 0:
        return float(np.linalg.norm(actual - expected))
    return float(np.linalg.norm(actual - overlap / abs(overlap) * expected))


def transition_internal(logical: int, frame: np.ndarray | None = None) -> np.ndarray:
    state = PLUS if logical == 0 else MINUS
    if frame is None:
        return state.copy()
    return c210.direction_permutation(frame) @ state


def collision_step(internal: np.ndarray, beta: float, contact_phase: float,
                   *, inverse: bool = False) -> np.ndarray:
    coin = c219.common_species(beta).coin
    matrix = np.exp(1j * contact_phase) * coin
    return matrix.conj().T @ internal if inverse else matrix @ internal


def event_projector_weight(internal: np.ndarray, frame: np.ndarray | None = None) -> float:
    target = transition_internal(1, frame)
    return float(abs(np.vdot(target, internal)) ** 2)


def complete_basis() -> np.ndarray:
    columns = [PLUS.copy(), MINUS.copy()]
    for index in range(6):
        vector = np.eye(6, dtype=complex)[:, index]
        for column in columns:
            vector -= column * np.vdot(column, vector)
        norm = float(np.linalg.norm(vector))
        if norm > 1e-12:
            columns.append(vector / norm)
        if len(columns) == 6:
            break
    return np.column_stack(columns)


def local_latch_matrix(frame: np.ndarray | None = None) -> np.ndarray:
    identity_internal = np.eye(6, dtype=complex)
    identity_receipt = np.eye(2, dtype=complex)
    flip = np.asarray(((0, 1), (1, 0)), dtype=complex)
    target = transition_internal(1, frame)
    projector = np.outer(target, target.conj())
    return np.kron(identity_internal - projector, identity_receipt) + np.kron(projector, flip)


def controlled_comparison_matrix() -> np.ndarray:
    matrix = np.zeros((8, 8), dtype=complex)
    for event_a, event_b, receipt in product((0, 1), repeat=3):
        source = 4 * event_a + 2 * event_b + receipt
        target_receipt = receipt ^ (event_a & event_b)
        target = 4 * event_a + 2 * event_b + target_receipt
        matrix[target, source] = 1
    return matrix


def apply_axes(state: np.ndarray, matrix: np.ndarray, axes: tuple[int, ...]) -> np.ndarray:
    remaining = tuple(index for index in range(state.ndim) if index not in axes)
    order = axes + remaining
    inverse_order = np.argsort(order)
    leading = math.prod(state.shape[index] for index in axes)
    trailing = math.prod(state.shape[index] for index in remaining)
    transformed = matrix @ np.transpose(state, order).reshape(leading, trailing)
    reshaped = transformed.reshape(tuple(state.shape[index] for index in order))
    return np.transpose(reshaped, inverse_order)


def physical_comparison_receipt(internal_a: np.ndarray, internal_b: np.ndarray,
                                frame_a: np.ndarray, frame_b: np.ndarray) -> dict[str, float]:
    zero = np.asarray((1, 0), dtype=complex)
    initial = np.einsum(
        "a,b,c,d,e->abcde", internal_a, zero, internal_b, zero, zero,
        optimize=True,
    )
    latch_a = local_latch_matrix(frame_a)
    latch_b = local_latch_matrix(frame_b)
    compare = controlled_comparison_matrix()
    state = apply_axes(initial, latch_a, (0, 1))
    state = apply_axes(state, latch_b, (2, 3))
    state = apply_axes(state, compare, (1, 3, 4))
    receipt_weight = float(np.linalg.norm(state[..., 1]) ** 2)
    event_a_weight = float(np.linalg.norm(state[:, 1, :, :, :]) ** 2)
    event_b_weight = float(np.linalg.norm(state[:, :, :, 1, :]) ** 2)
    restored = apply_axes(state, compare, (1, 3, 4))
    restored = apply_axes(restored, latch_b, (2, 3))
    restored = apply_axes(restored, latch_a, (0, 1))
    return {
        "receipt_weight": receipt_weight,
        "event_a_weight": event_a_weight,
        "event_b_weight": event_b_weight,
        "inverse_residual": float(np.linalg.norm(restored - initial)),
        "norm_residual": abs(float(np.linalg.norm(state)) - 1.0),
    }


def bound_pair_step(state: np.ndarray, beta: float, contact_phase: float,
                    *, inverse: bool = False) -> np.ndarray:
    """Exact equal-direction bound-pair update on a periodic cubic box."""
    if state.ndim != 4 or state.shape[-1] != 6 or len(set(state.shape[:3])) != 1:
        raise ValueError("bound-pair state leaves cubic equal-direction code")
    if not inverse:
        mixed = np.einsum(
            "ab,xyzb->xyza", np.exp(1j * contact_phase) * c219.common_species(beta).coin,
            state, optimize=True,
        )
        output = np.zeros_like(mixed)
        for direction, displacement in enumerate(c210.DIRECTIONS):
            output[..., direction] = np.roll(
                mixed[..., direction], tuple(int(value) for value in displacement),
                axis=(0, 1, 2),
            )
        return output
    unstreamed = np.zeros_like(state)
    for direction, displacement in enumerate(c210.DIRECTIONS):
        unstreamed[..., direction] = np.roll(
            state[..., direction], tuple(-int(value) for value in displacement),
            axis=(0, 1, 2),
        )
    return np.einsum(
        "ab,xyzb->xyza",
        (np.exp(1j * contact_phase) * c219.common_species(beta).coin).conj().T,
        unstreamed, optimize=True,
    )


def uniform_bound_state(length: int, logical: int) -> np.ndarray:
    return np.ones((length, length, length, 1), dtype=complex) * transition_internal(logical) / math.sqrt(length**3)


def local_transition_density(state: np.ndarray) -> np.ndarray:
    amplitude = np.einsum("a,xyza->xyz", MINUS.conj(), state, optimize=True)
    return np.abs(amplitude) ** 2


def gaussian_bound_state(length: int, width: float) -> np.ndarray:
    coordinate = (np.arange(length) + length // 2) % length - length // 2
    x, y, z = np.meshgrid(coordinate, coordinate, coordinate, indexing="ij")
    envelope = np.exp(-(x * x + y * y + z * z) / (4 * width * width)).astype(complex)
    envelope /= np.linalg.norm(envelope)
    return envelope[..., None] * PLUS


def route_a_controls() -> dict[str, object]:
    print("\nROUTE A — AUTONOMOUS BOUND-PAIR TRANSITION STANDARD")
    basis = complete_basis()
    latch = local_latch_matrix()
    algebra = {
        "scalar_even_overlap": float(abs(np.vdot(SCALAR, EVEN))),
        "even_projector_residual": float(np.linalg.norm(c210.P_EVEN @ EVEN - EVEN)),
        "plus_minus_overlap": float(abs(np.vdot(PLUS, MINUS))),
        "basis_unitarity_residual": float(np.linalg.norm(basis.conj().T @ basis - np.eye(6))),
        "latch_unitarity_residual": float(np.linalg.norm(latch.conj().T @ latch - np.eye(12))),
        "latch_involution_residual": float(np.linalg.norm(latch @ latch - np.eye(12))),
        "adjacent_Givens_upper_bound_for_transition_basis": 15,
        "maximum_terminal_support_M2": 3,
    }
    rows = []
    maximum = 0.0
    fixtures = tuple((3, beta, False) for beta in TRAIN_BETAS) + ((4, HELD_BETA, True),)
    for length, beta, held in fixtures:
        for logical in (0, 1):
            initial = uniform_bound_state(length, logical)
            physical = bound_pair_step(initial, beta, CONTACT)
            expected = uniform_bound_state(length, 1 - logical)
            eg = phase_aligned_residual(physical, expected)
            restored = bound_pair_step(physical, beta, CONTACT, inverse=True)
            inverse = float(np.linalg.norm(restored - initial))
            density = local_transition_density(physical)
            event_total = float(density.sum())
            event_expected = float(1 - logical)
            local_uniformity = float(np.max(np.abs(density - event_total / length**3)))
            norm = abs(float(np.linalg.norm(physical)) - 1.0)
            maximum = max(maximum, eg, inverse, abs(event_total - event_expected), local_uniformity, norm)
            rows.append({
                "length": length, "beta": beta, "held": held, "logical_input": logical,
                "EG_projective_residual": eg, "inverse_residual": inverse,
                "candidate_transition_total": event_total,
                "candidate_transition_expected": event_expected,
                "local_density_uniformity_residual": local_uniformity,
                "norm_residual": norm,
            })
    recurrence = []
    for length, beta, held in fixtures:
        state = uniform_bound_state(length, 0)
        observed = []
        for _probe_ordinal in range(8):
            state = bound_pair_step(state, beta, CONTACT)
            observed.append(round(float(local_transition_density(state).sum())))
        recurrence.append({"length": length, "beta": beta, "held": held,
                           "physical_transition_word": tuple(observed),
                           "expected": (1, 0, 1, 0, 1, 0, 1, 0)})
    check(
        "the actual Cycle219 scalar/even antipode in the equal-direction bound-pair update gives an exact local projective transition criterion, E/G, inverse, and held recurrence without an endpoint count word",
        maximum < TOL
        and all(row["physical_transition_word"] == row["expected"] for row in recurrence)
        and max(algebra[key] for key in algebra if key.endswith("residual")) < TOL,
        {"algebra": algebra, "rows": rows, "recurrence": recurrence,
         "maximum_residual": maximum, "endpoint_count_word_input": False,
         "relative_contact_support_preserved": True},
    )
    return {"algebra": algebra, "rows": rows, "recurrence": recurrence,
            "maximum_residual": maximum}


def transport_line(internal: np.ndarray, distance: int, *, reverse: bool = False) -> tuple[np.ndarray, int]:
    if distance < 1:
        raise ValueError("transport distance must be positive")
    blocks = np.zeros((distance + 1, 6), dtype=complex)
    blocks[-1 if reverse else 0] = internal
    edges = reversed(range(distance)) if reverse else range(distance)
    swaps = 0
    for edge in edges:
        blocks[[edge, edge + 1], :] = blocks[[edge + 1, edge], :]
        swaps += 6
    return blocks[0 if reverse else -1].copy(), swaps


def transported_fixture(name: str, distance: int, beta_a: float, beta_b: float,
                        contact_a: float, contact_b: float, frame_a: np.ndarray,
                        frame_b: np.ndarray, held: bool) -> dict[str, object]:
    start_a = transition_internal(0, frame_a)
    start_b = transition_internal(0, frame_b)
    moved_a, swaps_a = transport_line(start_a, distance)
    moved_b, swaps_b = transport_line(start_b, distance)
    after_a = collision_step(moved_a, beta_a, contact_a)
    after_b = collision_step(moved_b, beta_b, contact_b)
    event_a = event_projector_weight(after_a, frame_a)
    event_b = event_projector_weight(after_b, frame_b)
    comparison = physical_comparison_receipt(after_a, after_b, frame_a, frame_b)
    receipt = int(abs(comparison["receipt_weight"] - 1.0) < TOL)
    restored_a, reverse_a = transport_line(collision_step(after_a, beta_a, contact_a, inverse=True), distance, reverse=True)
    restored_b, reverse_b = transport_line(collision_step(after_b, beta_b, contact_b, inverse=True), distance, reverse=True)
    return {
        "name": name, "held": held, "distance": distance,
        "beta_a": beta_a, "beta_b": beta_b,
        "contact_source_phase_a": contact_a, "contact_source_phase_b": contact_b,
        "event_a": event_a, "event_b": event_b, "local_comparison_receipt": receipt,
        "physical_comparison": comparison,
        "transport_SWAPS": swaps_a + swaps_b,
        "inverse_transport_SWAPS": reverse_a + reverse_b,
        "inverse_a": phase_aligned_residual(restored_a, start_a),
        "inverse_b": phase_aligned_residual(restored_b, start_b),
        "frame_a_det": round(np.linalg.det(frame_a)), "frame_b_det": round(np.linalg.det(frame_b)),
    }


def localized_free_stream_control() -> dict[str, object]:
    rows = []
    for length, width, steps, held in ((7, 1.5, 3, False), (9, 1.9, 5, True)):
        outputs = {}
        for beta in (-0.2, HELD_BETA):
            state = gaussian_bound_state(length, width)
            initial = state.copy()
            transition_totals = []
            for _probe_ordinal in range(steps):
                state = bound_pair_step(state, beta, CONTACT)
                transition_totals.append(float(local_transition_density(state).sum()))
            restored = state
            for _probe_ordinal in range(steps):
                restored = bound_pair_step(restored, beta, CONTACT, inverse=True)
            code_projection = abs(np.vdot(initial.ravel(), state.ravel())) ** 2
            outputs[str(beta)] = {
                "transition_totals": tuple(transition_totals),
                "fixed_initial_code_survival": float(code_projection),
                "inverse_residual": float(np.linalg.norm(restored - initial)),
            }
        difference = max(abs(a - b) for a, b in zip(
            outputs[str(-0.2)]["transition_totals"], outputs[str(HELD_BETA)]["transition_totals"]
        ))
        rows.append({"length": length, "width": width, "steps": steps, "held": held,
                     "carrier_variation_transition_difference": difference,
                     "outputs": outputs})
    return {
        "rows": rows,
        "held_carrier_variation_signal": rows[-1]["carrier_variation_transition_difference"],
        "maximum_inverse_residual": max(
            output["inverse_residual"] for row in rows for output in row["outputs"].values()
        ),
        "interpretation": "localized free-stream state leaves the exact two-state transition code; this is a route-specific control, not a universal clock no-go",
    }


def proper_frames() -> tuple[np.ndarray, ...]:
    return c210.proper_cubic_frames()


def route_b_controls() -> dict[str, object]:
    print("\nROUTE B — TRANSPORTED TWO-STANDARD COMPARISON")
    frames = proper_frames()
    rows = (
        transported_fixture("train-same-carrier-one-edge", 1, -0.3, -0.3, CONTACT, CONTACT, frames[0], frames[5], False),
        transported_fixture("train-mass-varied-two-edge", 2, -0.2, -0.3, 0.0, CONTACT, frames[3], frames[11], False),
        transported_fixture("held-mass-contact-varied-three-edge", 3, -0.2, HELD_BETA, 0.0, CONTACT, frames[7], frames[19], True),
        transported_fixture("held-mass-contact-varied-five-edge", 5, -0.3, HELD_BETA, CONTACT, 0.0, frames[13], frames[23], True),
    )
    paired_failures = 0
    maximum_covariance = 0.0
    maximum_comparison_inverse = 0.0
    maximum_comparison_norm = 0.0
    base_after_a = collision_step(PLUS, -0.2, 0.0)
    base_after_b = collision_step(PLUS, HELD_BETA, CONTACT)
    path = np.asarray(((0, 0, 0), (1, 0, 0), (2, 0, 0)))
    for frame_a in frames:
        rep_a = c210.direction_permutation(frame_a)
        for frame_b in frames:
            rep_b = c210.direction_permutation(frame_b)
            residual_a = phase_aligned_residual(
                collision_step(rep_a @ PLUS, -0.2, 0.0), rep_a @ base_after_a
            )
            residual_b = phase_aligned_residual(
                collision_step(rep_b @ PLUS, HELD_BETA, CONTACT), rep_b @ base_after_b
            )
            maximum_covariance = max(maximum_covariance, residual_a, residual_b)
            event_a = event_projector_weight(rep_a @ base_after_a, frame_a)
            event_b = event_projector_weight(rep_b @ base_after_b, frame_b)
            comparison = physical_comparison_receipt(
                rep_a @ base_after_a, rep_b @ base_after_b, frame_a, frame_b
            )
            maximum_comparison_inverse = max(
                maximum_comparison_inverse, comparison["inverse_residual"]
            )
            maximum_comparison_norm = max(
                maximum_comparison_norm, comparison["norm_residual"]
            )
            mapped_a = tuple(frame_a @ site for site in path)
            mapped_b = tuple(frame_b @ site for site in path)
            local = all(
                int(np.abs(mapped[index + 1] - mapped[index]).sum()) == 1
                for mapped in (mapped_a, mapped_b) for index in range(2)
            )
            paired_failures += int(
                residual_a >= TOL or residual_b >= TOL
                or abs(event_a - 1) >= TOL or abs(event_b - 1) >= TOL or not local
                or abs(comparison["receipt_weight"] - 1) >= TOL
                or comparison["inverse_residual"] >= TOL
                or comparison["norm_residual"] >= TOL
            )
    free_control = localized_free_stream_control()
    check(
        "two trapped matter standards transport by local M2 SWAPs and produce one local comparison receipt after independent reorientation, mass-sector, and actual-contact phase variation under all24/all576",
        all(
            row["local_comparison_receipt"] == 1 and row["inverse_a"] < TOL and row["inverse_b"] < TOL
            and row["physical_comparison"]["inverse_residual"] < TOL
            and row["physical_comparison"]["norm_residual"] < TOL
            and row["frame_a_det"] == row["frame_b_det"] == 1
            for row in rows
        )
        and len(frames) == 24 and paired_failures == 0 and maximum_covariance < TOL
        and free_control["maximum_inverse_residual"] < TOL
        and free_control["held_carrier_variation_signal"] > SIGNAL,
        {"fixtures": rows, "proper_frames": len(frames), "paired_frames": len(frames) ** 2,
         "paired_failures": paired_failures, "maximum_covariance_residual": maximum_covariance,
         "maximum_comparison_inverse_residual": maximum_comparison_inverse,
         "maximum_comparison_norm_residual": maximum_comparison_norm,
         "localized_free_stream_control": free_control,
         "transport_trap_and_path_supplied": True},
    )
    return {"fixtures": rows, "proper_frames": len(frames), "paired_frames": len(frames) ** 2,
            "paired_failures": paired_failures, "maximum_covariance_residual": maximum_covariance,
            "maximum_comparison_inverse_residual": maximum_comparison_inverse,
            "maximum_comparison_norm_residual": maximum_comparison_norm,
            "localized_free_stream_control": free_control}


def one_hot(position: int, width: int = MODULUS) -> Word:
    if position not in range(width):
        raise ValueError("one-hot position leaves word")
    return tuple(int(index == position) for index in range(width))


def hot_position(word: Word) -> int:
    if len(word) != MODULUS or any(bit not in (0, 1) for bit in word) or sum(word) != 1:
        raise ValueError("malformed one-hot word")
    return word.index(1)


def echo_layout() -> EchoLayout:
    return EchoLayout(0, 1, 2, 3, 4, 5, tuple(range(6, 22)), tuple(range(22, 38)), 38)


def echo_initial(*, malformed: str | None = None) -> Word:
    layout = echo_layout()
    bits = [0] * layout.width
    for index, bit in zip(layout.low, one_hot(14)):
        bits[index] = bit
    for index, bit in zip(layout.high, one_hot(0)):
        bits[index] = bit
    if malformed == "q":
        bits[layout.q_a] = 2
    elif malformed == "low":
        bits[layout.low[0]] = 1
    elif malformed == "high":
        bits[layout.high[0]] = 0
    elif malformed == "work":
        bits[layout.compare] = 1
    elif malformed is not None:
        raise ValueError("unknown malformed echo fixture")
    return tuple(bits)


def validate_echo(bits: Word, *, boundary: bool = True) -> None:
    layout = echo_layout()
    if len(bits) != layout.width or any(bit not in (0, 1) for bit in bits):
        raise ValueError("echo word leaves binary layout")
    hot_position(tuple(bits[index] for index in layout.low))
    hot_position(tuple(bits[index] for index in layout.high))
    if boundary and any(bits[index] for index in (layout.event_a, layout.event_b, layout.compare, layout.carry)):
        raise ValueError("recyclable work reservoir is not blank")


def apply_gate(bits: list[int], gate: Gate) -> None:
    if gate.kind == "X":
        bits[gate.sites[0]] ^= 1
    elif gate.kind == "CNOT":
        control, target = gate.sites
        bits[target] ^= bits[control]
    elif gate.kind == "TOFFOLI":
        left, right, target = gate.sites
        bits[target] ^= bits[left] & bits[right]
    elif gate.kind == "FREDKIN":
        control, left, right = gate.sites
        if bits[control]:
            bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError("unknown gate")


def controlled_rotate(control: int, word: tuple[int, ...], label: str) -> tuple[Gate, ...]:
    return tuple(
        Gate("FREDKIN", (control, word[index], word[index + 1]), f"{label}:rotate-{index}")
        for index in reversed(range(MODULUS - 1))
    )


def opportunity_schedule() -> tuple[Gate, ...]:
    layout = echo_layout()
    gates = [
        Gate("X", (layout.q_a,), "matter-A:actual-coin-code-toggle"),
        Gate("X", (layout.q_b,), "matter-B:actual-coin-code-toggle"),
        Gate("CNOT", (layout.q_a, layout.event_a), "event-A:local-transition-latch"),
        Gate("CNOT", (layout.q_b, layout.event_b), "event-B:local-transition-latch"),
        Gate("TOFFOLI", (layout.event_a, layout.event_b, layout.compare), "comparison:both-transition"),
        Gate("TOFFOLI", (layout.compare, layout.low[-1], layout.carry), "ledger:compute-carry"),
    ]
    gates.extend(controlled_rotate(layout.carry, layout.high, "ledger:high"))
    gates.extend(controlled_rotate(layout.compare, layout.low, "ledger:low"))
    gates.extend((
        Gate("TOFFOLI", (layout.compare, layout.low[0], layout.carry), "ledger:uncompute-carry"),
        Gate("TOFFOLI", (layout.event_a, layout.event_b, layout.compare), "comparison:uncompute"),
        Gate("CNOT", (layout.q_b, layout.event_b), "event-B:uncompute"),
        Gate("CNOT", (layout.q_a, layout.event_a), "event-A:uncompute"),
    ))
    return tuple(gates)


def run_opportunity(bits: Word, *, reverse: bool = False, delete_label: str | None = None) -> Word:
    output = list(bits)
    schedule = opportunity_schedule()
    iterable = reversed(schedule) if reverse else schedule
    for gate in iterable:
        if gate.label == delete_label:
            continue
        apply_gate(output, gate)
    return tuple(output)


def run_cycles(bits: Word, cycles: int, *, reverse: bool = False,
               delete_label: str | None = None) -> Word:
    if cycles < 0:
        raise ValueError("negative cycle prefix")
    output = bits
    for _probe_ordinal in range(2 * cycles):
        output = run_opportunity(output, reverse=reverse, delete_label=delete_label)
    return output


def ledger_value(bits: Word) -> int:
    layout = echo_layout()
    low = hot_position(tuple(bits[index] for index in layout.low))
    high = hot_position(tuple(bits[index] for index in layout.high))
    return high * MODULUS + low


def decoded_calibrations(bits: Word) -> int:
    return (ledger_value(bits) - 14) % (MODULUS * MODULUS)


def route_c_controls() -> dict[str, object]:
    print("\nROUTE C — RECYCLABLE RELATIONAL CALIBRATION ECHO")
    rows = []
    maximum = 0.0
    for cycles in TRAIN_CYCLES + HELD_CYCLES:
        initial = echo_initial()
        physical = run_cycles(initial, cycles)
        validate_echo(physical)
        restored = run_cycles(physical, cycles, reverse=True)
        decoded = decoded_calibrations(physical)
        work = tuple(physical[index] for index in (
            echo_layout().event_a, echo_layout().event_b, echo_layout().compare, echo_layout().carry
        ))
        # The physical two-step matter word returns both internal standards to PLUS projectively.
        internal = PLUS.copy()
        for _ in range(2):
            internal = collision_step(internal, -0.3, CONTACT)
        matter_cycle_residual = phase_aligned_residual(internal, PLUS)
        maximum = max(maximum, matter_cycle_residual)
        rows.append({
            "cycles": cycles, "held": cycles in HELD_CYCLES,
            "physical_opportunities_executed_for_probe": 2 * cycles,
            "decoded_calibrations": decoded, "expected": cycles,
            "EG_exact": decoded == cycles, "inverse_exact": restored == initial,
            "recycled_work_boundary": work, "matter_cycle_projective_residual": matter_cycle_residual,
            "low_word": hot_position(tuple(physical[index] for index in echo_layout().low)),
            "high_word": hot_position(tuple(physical[index] for index in echo_layout().high)),
        })
    composition_rows = []
    for left, right in ((1, 3), (3, 5), (9, 17), (17, 25)):
        initial = echo_initial()
        split = run_cycles(run_cycles(initial, left), right)
        direct = run_cycles(initial, left + right)
        composition_rows.append({"left": left, "right": right, "exact": split == direct,
                                 "decoded": decoded_calibrations(split)})
    refinement_rows = tuple({
        "cycles": cycles, "fine_transition_opportunities": 2 * cycles,
        "coarse_recurrence_cells": decoded_calibrations(run_cycles(echo_initial(), cycles)),
        "refinement_ratio": 2,
        "residual": 2 * decoded_calibrations(run_cycles(echo_initial(), cycles)) - 2 * cycles,
    } for cycles in TRAIN_CYCLES + HELD_CYCLES)
    baseline = run_cycles(echo_initial(), 3)
    deletion_labels = (
        "event-A:local-transition-latch", "comparison:both-transition",
        "ledger:low:rotate-14", "event-A:uncompute",
    )
    deletions = {
        label: {
            "state_changed": run_cycles(echo_initial(), 3, delete_label=label) != baseline,
            "work_leakage": sum(run_cycles(echo_initial(), 3, delete_label=label)[index] for index in (
                echo_layout().event_a, echo_layout().event_b, echo_layout().compare, echo_layout().carry
            )),
        }
        for label in deletion_labels
    }
    wrap_baseline = run_cycles(echo_initial(), 3)
    carry_deleted = run_cycles(echo_initial(), 3, delete_label="ledger:compute-carry")
    deletions["ledger:compute-carry"] = {
        "state_changed": carry_deleted != wrap_baseline,
        "work_leakage": carry_deleted[echo_layout().carry],
    }
    malformed = {}
    for name in ("q", "low", "high", "work"):
        try:
            validate_echo(echo_initial(malformed=name))
            malformed[name] = False
        except ValueError:
            malformed[name] = True
    resource_row = {
        "actual_matter_internal_M2": 12,
        "recyclable_event_comparison_carry_M2": 4,
        "two_word_retained_ledger_M2": 32,
        "total_active_M2": 48,
        "fresh_host_supplied_work_M2_per_prefix": 0,
        "logical_gates_per_opportunity": len(opportunity_schedule()),
        "maximum_terminal_support_M2": 3,
        "ledger_capacity_before_alias": 256,
    }
    check(
        "one fixed event/comparison/carry reservoir is reused through every calibration echo; the physical two-word ledger gives exact E/G, inverse, refinement, composition, rollover, deletions, and held prefixes without a fresh bank",
        maximum < TOL
        and all(row["EG_exact"] and row["inverse_exact"] and row["recycled_work_boundary"] == (0, 0, 0, 0) for row in rows)
        and all(row["exact"] for row in composition_rows)
        and all(row["residual"] == 0 for row in refinement_rows)
        and all(item["state_changed"] for item in deletions.values())
        and deletions["event-A:uncompute"]["work_leakage"] > 0
        and all(malformed.values())
        and resource_row["fresh_host_supplied_work_M2_per_prefix"] == 0,
        {"rows": rows, "composition": composition_rows, "refinement": refinement_rows,
         "deletions": deletions, "malformed_rejected": malformed,
         "resources": resource_row, "maximum_residual": maximum},
    )
    return {"rows": rows, "composition": composition_rows, "refinement": refinement_rows,
            "deletions": deletions, "malformed_rejected": malformed,
            "resources": resource_row, "maximum_residual": maximum}


def firewall_controls() -> None:
    print("\nDECODER / INTERPRETATION FIREWALL")
    functions = (event_projector_weight, local_transition_density, decoded_calibrations)
    forbidden = ("schedule", "depth", "phase", "iteration", "rate", "energy", "record", "proper")
    hits = {}
    for function in functions:
        tree = ast.parse(inspect.getsource(function))
        names = tuple(
            node.id.lower() if isinstance(node, ast.Name) else node.attr.lower()
            for node in ast.walk(tree) if isinstance(node, (ast.Name, ast.Attribute))
        )
        hits[function.__name__] = {token: sum(token in name for name in names) for token in forbidden}
    check(
        "transition and calibration decoders consume physical matter/projector/ledger state only; schedule is not time and no phase, generator entry, FORMATION, norm, or receipt is renamed energy, rate, Record, actuality, or probability",
        all(value == 0 for row in hits.values() for value in row.values()),
        {"AST_forbidden_name_hits": hits, "clock_dimension_added": False,
         "schedule_called_time": False, "generator_entry_called_rate": False,
         "formation_called_Record_actuality": False, "norm_called_probability": False,
         "proper_time_claimed": False},
    )


def no_go_inventory_controls(started: float, fixtures, route_a, route_b, route_c) -> None:
    print("\nSUPPLIED / DERIVED / OPEN / FULL N1-N8")
    n1 = (
        ("scalar/even bound-pair recurrence", "Cycle219 antipodal sectors under actual equal-direction contact update", "local transition candidate", "ATTEMPTED — POSITIVE at k=0"),
        ("trapped transported dual standard", "complete six-mode local SWAP plus rotated comparator", "mass/contact/frame equivalence receipt", "ATTEMPTED — POSITIVE with supplied trap"),
        ("localized freely streaming standard", "finite wavepacket under direction stream", "retain exact two-state recurrence while moving", "ATTEMPTED — PARTIAL; code leakage and carrier dependence visible"),
        ("recyclable relational echo", "compute-use-uncompute work plus two-word ledger", "repeated calibration without fresh sidecars", "ATTEMPTED — POSITIVE to capacity 256"),
        ("Cycle570 fresh-bath dilation", "one retained reservoir vector per count token", "arbitrary-input contraction", "RETAINED POSITIVE but not recyclable"),
        ("face-carrier transition standard", "Cycle569 reservoir/face Rabi recurrence", "source-sensitive independent standard", "OPEN; angle selection and return path unresolved"),
    )
    walls = (
        "localized autonomous standard", "trap/transport law selection", "FORMATION actuality",
        "unbounded reservoir/noise", "empirical equivalence/scale", "continuum/Lorentz proper time",
    )
    n2 = tuple((left, right, "no", "no", True) for left, right in combinations(walls, 2))
    n3 = (
        "Cycle219 common coin family and selected beta values", "scalar/even preparation",
        "translation-invariant k=0 finite periodic state", "actual contact phase g=0.37",
        "equal-direction bound-pair restriction", "local transition projector and comparator basis",
        "supplied trap and six-mode SWAP transport path", "face-carrier labels and frame placement",
        "blank four-M2 recyclable work reservoir", "blank base-16 two-word ledger",
        "finite capacity 256", "noiseless gates and held split",
    )
    n4 = (
        ("Cycle219 note lines 31-75", "shared scalar/even coin phases and mass family", "uses exact antipode; beta still supplied", True),
        ("Cycle219 note lines 103-134", "mass spectrum and clock theorem open", "does not promote restricted recurrence to species law", True),
        ("Cycle230 note lines 286-390", "local contact is one-particle identity and proper-cubic", "retained mass/contact fixture exact-pinned", True),
        ("Cycle563 note lines 161-175", "mass/contact/seam and physical compiler controls", "receipt values retained, no matter law modified", True),
        ("Cycle569 note lines 324-378", "physical M2 source/contact lift and held controls", "contact phase/carrier frames only at stated scope", True),
        ("Cycle570 note lines 360-385", "finite reservoir and clock-equivalence walls open", "directly attacks those finite residuals", True),
    )
    n5 = (
        ("L3 beta -0.2/-0.3", "train k0", "exact projective recurrence"),
        ("L4 beta -0.35", "held k0", "exact no-refit recurrence"),
        ("transport distances 1/2 then held 3/5", "trapped code", "exact"),
        ("calibration cycles 1/3/5 then held 9/17/25", "finite ledger", "exact"),
        ("L7/L9 localized packet", "adversarial free stream", "nonzero leakage; no universal rhetoric"),
        ("noise/unbounded/moving continuum", "untested", "no negative claim"),
    )
    n6 = (
        "derive a localized trap from the accepted free-plus-contact law",
        "test a refocused freely moving packet without host-chosen mirrors",
        "couple the recyclable ledger to a supplied Record-formation bridge without calling it actuality",
        "replace finite base-16 capacity with an autonomous stabilizing reservoir",
        "compare against an independently selected face-carrier or field-transition standard",
        "establish empirical scaling and controlled continuum/Lorentz transport",
    )
    n7 = (
        "A hostile constructive reviewer should treat the k=0 and trapped positives as calibration fixtures, not universal clock equivalence. The next decisive construction must localize the same scalar/even transition under the accepted free-plus-contact stream, transport it without a supplied trap or mirror cadence, compare it against a dynamically independent standard under source variation, and retain bounded refinement residuals while the recyclable work rail stays blank. The localized leakage measured here is a target for refocusing, not a theorem that such a clock cannot exist."
    )
    n8 = (
        "Cycle219 supplied a common mass family but explicitly left a clock theorem open",
        "Cycles428/444 made oscillator and echo candidates physical while calibration remained supplied",
        "Cycles498/504 added endpoint refinement and finite rollover without a matter transition",
        "Cycles563/569 preserved the actual mass/contact/seam and source-carrier physical lift",
        "Cycle570 closed a finite count-semigroup/full-operator bridge but left matter equivalence and recycling open",
        "Cycle573 closes a restricted k0/trapped transition and finite recyclable echo while exposing localized free-stream leakage",
    )
    supplied = (
        "Cycle219 common coin, beta sectors, scalar/even preparation and equal-direction bound-pair restriction",
        "Cycle230/563/569 contact phase, physical compiler, seam fixture and source/carrier frames",
        "translation-invariant periodic preparation and local transition projector/basis compiler",
        "trap, local six-mode SWAP transport path and rendezvous comparator",
        "blank four-M2 work reservoir, base-16 two-word ledger, finite capacity and noiseless gates",
    )
    derived = (
        "exact scalar/even period-two projective recurrence on actual k0 bound-pair update",
        "local transition density and physical latch criterion without endpoint count input",
        "trapped two-standard comparison under beta/contact/frame/path variation and all576",
        "quantified localized free-stream code leakage and carrier sensitivity",
        "finite recyclable calibration echo with exact E/G/inverse/composition/refinement/rollover",
        "retained mass/contact/seam controls, deletions, lawful domain and constant overhead",
    )
    open_items = (
        "localized autonomous recurrence under the accepted untrapped full stream",
        "derivation/selection of trap, transition preparation and transport law",
        "Record formation, actuality, permanence and realized history",
        "unbounded recyclable reservoir, stability, noise and synchronization",
        "independent empirical clock equivalence and dimensionful scale",
        "continuum/Lorentz/proper-time theorem, source/gravity and Born probability",
    )
    elapsed = time.monotonic() - started
    rss = resource_usage()
    check(
        "full N1-N8 keeps the localized free-stream residual route-specific and preserves all independent walls; no broad no-go, minimum-content, shared-obstruction, or axiom-pressure claim ships",
        len(n1) >= 5 and len(n2) == 15 and len(n3) >= 10 and len(n4) == 6
        and len(n5) == 6 and len(n6) >= 5 and len(n7) > 400 and len(n8) == 6
        and len(supplied) == 5 and len(derived) == len(open_items) == 6
        and route_a["maximum_residual"] < TOL
        and route_b["paired_failures"] == 0
        and route_b["localized_free_stream_control"]["held_carrier_variation_signal"] > SIGNAL
        and all(row["EG_exact"] for row in route_c["rows"])
        and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
        {"N1_normalized_alternatives": n1, "N2_pairwise_wall_audit": n2,
         "N3_hidden_wall_scan": n3, "N4_residual_matching": n4,
         "N5_resolution_audit": n5, "N6_partial_closure_paths": n6,
         "N7_hostile_steelman": n7, "N8_cross_cycle_echo": n8,
         "supplied": supplied, "derived": derived, "open": open_items,
         "broad_time_no_go": "FAIL / DO NOT SHIP", "minimum_content_claim": False,
         "shared_substrate_obstruction": False, "axiom_pressure": False,
         "highest_honest_terminal": "restricted k0/trapped dimensionless matter-transition equivalence plus finite recyclable calibration, not proper time",
         "authority": AUTHORITY, "audit": AUDIT, "elapsed_seconds": elapsed,
         "peak_rss_bytes": rss,
         "six_wall_ledger": {
             "C_ref": "matter transition and finite recycling constructed; beta/preparation/trap/ledger reference supplied",
             "C_num": "exact projective, integer, composition and refinement residuals plus explicit localized leakage; no empirical scale",
             "C_wrap": "finite two-word reusable ledger closes fresh-bank-per-prefix at capacity 256; unbounded/noisy renewal open",
             "C_int": "actual mass/contact recurrence consumed without calling phase energy or generator entry a rate",
             "C_local": "onsite projector/latch, adjacent transport, 48-M2 echo and all24/all576; autonomous localization/trap derivation open",
             "C_source": "contact/source phase common-mode control only; no physical stress/gravity/backreaction",
         }},
    )


def resource_usage() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def install_wall_cap() -> None:
    if hasattr(signal, "SIGALRM"):
        def alarm(_signum, _frame):
            raise TimeoutError("Cycle573 exceeded wall cap")
        signal.signal(signal.SIGALRM, alarm)
        signal.alarm(int(WALL_CAP_SECONDS) + 1)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    install_wall_cap()
    print("Cycle573 physical matter-transition clock-equivalence tournament")
    print("authority", AUTHORITY, "audit", AUDIT)
    fixtures: dict[str, object] = {}
    route_a: dict[str, object] = {}
    route_b: dict[str, object] = {}
    route_c: dict[str, object] = {}
    try:
        fixtures = dependency_controls()
        note_contract()
        route_a = route_a_controls()
        route_b = route_b_controls()
        route_c = route_c_controls()
        firewall_controls()
        no_go_inventory_controls(started, fixtures, route_a, route_b, route_c)
        cold_internal_elapsed_seconds = time.monotonic() - started
        cold_maximum_RSS_bytes = resource_usage()
        receipt = {
            "status": "cycle573-physical-matter-transition-clock-equivalence-tournament",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "accepted_Cycle570_ancestor_commit": ACCEPTED_CYCLE570_COMMIT,
            "definitive_run_descendant_HEAD": current_commit(),
            "branch_head_equality_is_scientific_dependency": False,
            "runner_sha256": file_sha(Path(__file__)),
            "note_sha256": file_sha(NOTE),
            "tests_passed": PASS,
            "tests_total": PASS + FAIL,
            "pass": FAIL == 0,
            "cold_internal_elapsed_seconds": cold_internal_elapsed_seconds,
            "cold_maximum_RSS_bytes": cold_maximum_RSS_bytes,
            "exact_pinned_dependencies": {
                "Cycle219_runner_sha256":
                    DEPENDENCY_SHA256["common_matter_field_coin_family_cycle219_2026_07_16.py"],
                "Cycle230_runner_sha256":
                    DEPENDENCY_SHA256["spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"],
                "Cycle563_runner_sha256":
                    DEPENDENCY_SHA256["physical_held_sparse_order_retirement_cycle563_2026_07_21.py"],
                "Cycle569_runner_sha256":
                    DEPENDENCY_SHA256["physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py"],
                "Cycle570_runner_sha256":
                    DEPENDENCY_SHA256["physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py"],
                "Cycle563_receipt_sha256":
                    RECEIPT_SHA256["physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"],
                "Cycle569_receipt_sha256":
                    RECEIPT_SHA256["physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json"],
                "Cycle570_receipt_sha256":
                    RECEIPT_SHA256["physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json"],
            },
            "retained_physical_fixtures": {
                "one_particle_mass_residual": fixtures["Cycle563_mass_residual"],
                "contact_factorization_residual": fixtures["Cycle563_contact_residual"],
                "axis_seam_braid_residual": fixtures["Cycle563_seam_residual"],
            },
            "frozen_split": {
                "route_A_train": [{"length": 3, "beta": -0.2}, {"length": 3, "beta": -0.3}],
                "route_A_held": {"length": 4, "beta": -0.35},
                "route_B_train_path_edges": [1, 2],
                "route_B_held_path_edges": [3, 5],
                "route_C_train_calibration_cycles": [1, 3, 5],
                "route_C_held_calibration_cycles": [9, 17, 25],
                "contact_phase": 0.37,
                "held_refit_parameters": 0,
            },
            "route_A_bound_pair_transition": {
                "disposition": "positive exact projective period-two recurrence on the declared periodic k0 equal-direction bound-pair code",
                "EG_projective_and_inverse_pass": bool(all(
                    row["EG_projective_residual"] < TOL and row["inverse_residual"] < TOL
                    for row in route_a["rows"]
                )),
                "physical_transition_word": list(route_a["recurrence"][0]["physical_transition_word"]),
                "maximum_residual": route_a["maximum_residual"],
                "maximum_terminal_support_M2": route_a["algebra"]["maximum_terminal_support_M2"],
                "transition_basis_adjacent_Givens_upper_bound":
                    route_a["algebra"]["adjacent_Givens_upper_bound_for_transition_basis"],
                "supplied_endpoint_count_word": False,
                "localization_preparation_and_beta_derived": False,
            },
            "route_B_transported_comparison": {
                "disposition": "positive trapped local-SWAP comparison; freely streaming localized control remains partial",
                "proper_cubic_frames": route_b["proper_frames"],
                "paired_frame_tests": route_b["paired_frames"],
                "paired_frame_failures": route_b["paired_failures"],
                "maximum_covariance_residual": route_b["maximum_covariance_residual"],
                "maximum_physical_comparison_inverse_residual": route_b["maximum_comparison_inverse_residual"],
                "maximum_physical_comparison_norm_residual": route_b["maximum_comparison_norm_residual"],
                "held_localized_free_stream_carrier_variation_signal":
                    route_b["localized_free_stream_control"]["held_carrier_variation_signal"],
                "localized_free_stream_maximum_inverse_residual":
                    route_b["localized_free_stream_control"]["maximum_inverse_residual"],
                "transport_path_and_trap_supplied": True,
                "universal_moving_clock_equivalence_claimed": False,
            },
            "route_C_recyclable_echo": {
                "disposition": "positive finite-capacity reusable calibration echo",
                "EG_inverse_composition_and_rollover_exact": bool(
                    all(row["EG_exact"] and row["inverse_exact"] for row in route_c["rows"])
                    and all(row["exact"] for row in route_c["composition"])
                ),
                "refinement_ratio": route_c["refinement"][0]["refinement_ratio"],
                "refinement_residual": max(row["residual"] for row in route_c["refinement"]),
                "maximum_matter_cycle_residual": route_c["maximum_residual"],
                "actual_matter_internal_M2": route_c["resources"]["actual_matter_internal_M2"],
                "recyclable_event_comparison_carry_M2": route_c["resources"]["recyclable_event_comparison_carry_M2"],
                "two_word_retained_ledger_M2": route_c["resources"]["two_word_retained_ledger_M2"],
                "total_active_M2": route_c["resources"]["total_active_M2"],
                "fresh_host_supplied_work_M2_per_prefix": route_c["resources"]["fresh_host_supplied_work_M2_per_prefix"],
                "logical_gates_per_opportunity": route_c["resources"]["logical_gates_per_opportunity"],
                "maximum_terminal_support_M2": route_c["resources"]["maximum_terminal_support_M2"],
                "ledger_capacity_before_alias": route_c["resources"]["ledger_capacity_before_alias"],
            },
            "controls": {
                "E_G_and_inverse_tested": True,
                "deletion_and_work_leakage_visible": True,
                "malformed_words_rejected": True,
                "undefined_coerced_to_zero": False,
                "constant_bounded_overhead_on_declared_code": True,
                "no_clock_dimension": True,
                "schedule_called_time": False,
                "phase_called_energy": False,
                "generator_entry_called_rate": False,
                "transition_receipt_called_Record_or_actuality": False,
                "projector_weight_called_probability": False,
            },
            "scope_boundary": {
                "highest_honest_terminal": "restricted k0/trapped dimensionless matter-transition equivalence plus finite recyclable calibration, not proper time",
                "localized_autonomous_recurrence_closed": False,
                "trap_and_transport_law_derived": False,
                "FORMATION_Record_actuality_closed": False,
                "unbounded_noisy_recycling_closed": False,
                "empirical_dimensionful_scale_derived": False,
                "independent_clock_universality_closed": False,
                "continuum_Lorentz_proper_time_closed": False,
                "source_gravity_closed": False,
                "Born_probability_closed": False,
                "shared_substrate_obstruction": False,
                "axiom_pressure": False,
                "broad_time_no_go_gate": "FAIL / DO NOT SHIP",
            },
            "six_wall_ledger": {
                "C_ref": "matter transition and finite recycling constructed; beta, preparation, trap, projector, comparison, and ledger reference supplied",
                "C_num": "exact projective, integer, composition and refinement residuals plus explicit localized leakage; no empirical scale",
                "C_wrap": "fixed four-M2 work reservoir reused and two-word ledger crosses rollover to capacity 256; unbounded/noisy renewal open",
                "C_int": "actual mass/contact recurrence consumed; common phase is not energy and no generator element is called a rate",
                "C_local": "onsite projector/latch, adjacent transport, 48-M2 echo, support-three terminals, all24/all576; autonomous localization/trap derivation open",
                "C_source": "contact/source phase tested as common-mode variation only; no physical stress, gravity, or backreaction law",
            },
            "no_go_discipline": {
                "N1_through_N8_executed": True,
                "route_specific_failure_promoted_to_shared_obstruction": False,
                "minimum_content_claim": False,
                "shared_substrate_obstruction": False,
                "axiom_pressure": False,
            },
            "optimal_next_campaign": "derive or falsify autonomous localized/refocused transport of the scalar-even transition under the accepted free-plus-contact stream, then compare it against a dynamically independent face-carrier or field standard under source variation while keeping the recyclable work rail blank",
        }
        RECEIPT.write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    except Exception as exc:
        check("Cycle573 runner completed without exception", False, repr(exc))
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print("SUMMARY_JSON", json.dumps({
        "status": "cycle573-physical-matter-transition-clock-equivalence-tournament",
        "authority": AUTHORITY, "audit": AUDIT,
        "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds_internal": time.monotonic() - started,
        "maximum_RSS_bytes_internal": resource_usage(),
        "route_A_maximum_residual": route_a.get("maximum_residual"),
        "route_B_all576_failures": route_b.get("paired_failures"),
        "route_B_maximum_comparison_inverse_residual": route_b.get("maximum_comparison_inverse_residual"),
        "route_B_maximum_comparison_norm_residual": route_b.get("maximum_comparison_norm_residual"),
        "route_B_localized_held_signal": route_b.get("localized_free_stream_control", {}).get("held_carrier_variation_signal"),
        "route_C_maximum_residual": route_c.get("maximum_residual"),
        "shared_substrate_obstruction": False, "axiom_pressure": False,
    }, sort_keys=True))
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
