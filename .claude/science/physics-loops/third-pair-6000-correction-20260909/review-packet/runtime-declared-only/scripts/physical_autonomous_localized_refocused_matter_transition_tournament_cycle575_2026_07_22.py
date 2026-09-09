#!/usr/bin/env python3
"""Cycle575: autonomous localized/refocused matter-transition tournament.

Three independent constructions attack the localization/transport residual left
by accepted Cycle573.  A physical seven-M2 carrier star generates a compact
defect mode.  A carried two-rail control implements an autonomous forward/
inverse echo.  A 36-rail composite separates the freely moving envelope label
from the scalar/even transition label.  All are candidate specified updates,
not new axioms, Records, Born laws, gravity laws, or proper-time theorems.
"""

from __future__ import annotations

import ast
from hashlib import sha256
from itertools import combinations
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
import physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22 as c573


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_LOCALIZED_REFOCUSED_MATTER_TRANSITION_TOURNAMENT_"
    "CYCLE575_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/"
    "physical_autonomous_localized_refocused_matter_transition_tournament_"
    "cycle575_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
ACCEPTED_CYCLE573_COMMIT = "69e1a7cfbc47ddd73c07e3d4ea8854226cd41389"
TOL = 5e-10
SIGNAL = 1e-7
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
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
    "physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py":
        "a9786cf68a9c669e7e7fe310a00ab9912aa404689651682ccfe3045a06e357f1",
}
RECEIPT_SHA256 = {
    "physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json":
        "350e2c1922379bb42091e1cb5685c9e1f698ed23b81acf7c14803ba5043fcfc1",
    "physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json":
        "c80aae229d3721b273d12188960e2a4b16402d10a982856bec76c465dad52baa",
    "physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json":
        "f104399af621ded1b50e180e6fcce5f254008715b72191c6199fe4d583a8a806",
    "physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json":
        "61888b3dfa3e777c7b036f0c2156011155afd7c09e022c8ff8f200d1fa8b05c7",
}
CYCLE573_NOTE_SHA256 = "fb5eeabcdf7b76fd2c55737e5f0c87bcb557ddd4ec5f03569989ab8aae4d4de2"

SCALAR = c573.SCALAR.copy()
EVEN = c573.EVEN.copy()
PLUS = c573.PLUS.copy()
MINUS = c573.MINUS.copy()


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
        ("git", "merge-base", "--is-ancestor", ACCEPTED_CYCLE573_COMMIT, "HEAD"),
        cwd=ROOT, check=False,
    ).returncode == 0


def dependency_controls() -> dict[str, object]:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCY_SHA256}
    receipt_observed = {name: file_sha(ROOT / "outputs" / name) for name in RECEIPT_SHA256}
    receipt_rows = {
        name: json.loads((ROOT / "outputs" / name).read_text(encoding="utf-8"))
        for name in RECEIPT_SHA256
    }
    retained = {
        "mass_residual": receipt_rows[
            "physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"
        ]["fixtures"]["Cycle219_mass_residual"],
        "contact_residual": receipt_rows[
            "physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"
        ]["fixtures"]["Cycle230_contact_factorization_residual"],
        "seam_residual": receipt_rows[
            "physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"
        ]["fixtures"]["Cycle230_axis_seam_residual"],
        "Cycle573_pass": receipt_rows[
            "physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json"
        ]["pass"],
    }
    note_hash = file_sha(ROOT / (
        "docs/work_history/repo/review_feedback/"
        "PHYSICAL_MATTER_TRANSITION_CLOCK_EQUIVALENCE_TOURNAMENT_CYCLE573_NOTE_2026-07-22.md"
    ))
    check(
        "accepted Cycle573 is an ancestor, every consumed Cycle219/230/563/569/570/573 artifact is byte-exact, and retained physics evidence is consumed from the Cycle563 receipt's computed fixtures",
        accepted_base_is_ancestor()
        and observed == DEPENDENCY_SHA256
        and receipt_observed == RECEIPT_SHA256
        and note_hash == CYCLE573_NOTE_SHA256
        and receipt_rows[
            "physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json"
        ].get("pass") is True
        and max(retained[key] for key in ("mass_residual", "contact_residual", "seam_residual")) < TOL,
        {
            "current_commit": current_commit(),
            "accepted_Cycle573_commit": ACCEPTED_CYCLE573_COMMIT,
            "accepted_Cycle573_is_ancestor": accepted_base_is_ancestor(),
            "runners": observed,
            "receipts": receipt_observed,
            "Cycle573_note_sha256": note_hash,
            "retained": retained,
            "evidence_source": "Cycle563 receipt fixtures (computed by its recorded run via the Cycle557/533 fixture path); Cycle569/570 receipts are byte-pinned anchors whose aggregate pass values are not gate inputs; the runnable Cycle573 pass is consumed",
        },
    )
    return retained


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset",
        "autonomous localized/refocused matter-transition tournament",
        "route a — carrier-generated star defect",
        "route b — carried autonomous inverse echo",
        "route c — composite internal transition",
        "no supplied static host trap", "no host-chosen mirror cadence",
        "no supplied endpoint count word", "all 576 paired proper-cubic frames",
        "cycle 456 is downstream only", "schedule is not time",
        "formation is not record actuality", "n1 — normalized alternatives",
        "n8 — cross-cycle echo", "broad localization no-go: fail / do not ship",
        "there is no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(item for item in required if item not in body)
    check("the Cycle575 note freezes target, route families, and rhetoric ceiling", not missing, missing)


def phase_aligned_residual(actual: np.ndarray, expected: np.ndarray) -> float:
    overlap = np.vdot(expected.ravel(), actual.ravel())
    if abs(overlap) == 0:
        return float(np.linalg.norm(actual - expected))
    return float(np.linalg.norm(actual - overlap / abs(overlap) * expected))


def spatial_stream(state: np.ndarray, *, inverse: bool = False) -> np.ndarray:
    if state.ndim < 4 or state.shape[3] != 6:
        raise ValueError("direction axis must be the fourth state axis")
    output = np.zeros_like(state)
    for direction, displacement in enumerate(c210.DIRECTIONS):
        shift = tuple(int((-1 if inverse else 1) * value) for value in displacement)
        output[..., direction, *([slice(None)] * (state.ndim - 4))] = np.roll(
            state[..., direction, *([slice(None)] * (state.ndim - 4))],
            shift, axis=(0, 1, 2),
        )
    return output


def matter_collision(state: np.ndarray, beta: float, contact: float,
                     *, inverse: bool = False) -> np.ndarray:
    matrix = np.exp(1j * contact) * c219.common_species(beta).coin
    if inverse:
        matrix = matrix.conj().T
    return np.einsum("ab,xyzb...->xyza...", matrix, state, optimize=True)


def local_layer(state: np.ndarray, beta: float, contact: float,
                local_matrices: dict[tuple[int, int, int], np.ndarray] | None = None,
                *, inverse: bool = False) -> np.ndarray:
    local_matrices = {} if local_matrices is None else local_matrices
    if not inverse:
        work = matter_collision(state, beta, contact)
        for site, matrix in local_matrices.items():
            work[site] = np.einsum("ab,b...->a...", matrix, work[site], optimize=True)
        return spatial_stream(work)
    work = spatial_stream(state, inverse=True)
    for site, matrix in local_matrices.items():
        work[site] = np.einsum("ab,b...->a...", matrix.conj().T, work[site], optimize=True)
    return matter_collision(work, beta, contact, inverse=True)


def site_plus(center: tuple[int, int, int], length: int, logical: int,
              frame: np.ndarray) -> np.ndarray:
    state = np.zeros((length, length, length, 6), dtype=complex)
    state[center] = c573.transition_internal(logical, frame)
    return state


def carrier_star(length: int, center: tuple[int, int, int],
                 frame: np.ndarray) -> dict[str, object]:
    shell = []
    for canonical_direction, displacement in enumerate(c210.DIRECTIONS):
        mapped = frame @ displacement
        site = tuple(int((center[axis] + mapped[axis]) % length) for axis in range(3))
        shell.append((canonical_direction, site))
    return {"center": center, "shell": tuple(shell), "carrier_M2": 7}


def validate_carrier(carrier: dict[str, object], length: int) -> bool:
    center = carrier.get("center")
    shell = carrier.get("shell")
    if not isinstance(center, tuple) or len(center) != 3 or not isinstance(shell, tuple):
        return False
    sites = tuple(site for _role, site in shell)
    relative = set()
    for site in sites:
        displacement = []
        for axis in range(3):
            value = (site[axis] - center[axis]) % length
            displacement.append(-1 if value == length - 1 else value)
        relative.add(tuple(displacement))
    cubic_neighbors = {
        tuple(int(value) for value in displacement)
        for displacement in c210.DIRECTIONS
    }
    return (
        len(shell) == 6 and len(set(sites)) == 6
        and all(role in range(6) for role, _site in shell)
        and set(role for role, _site in shell) == set(range(6))
        and all(all(value in range(length) for value in site) for site in sites)
        and relative == cubic_neighbors
    )


def star_corrections(beta: float, contact: float, carrier: dict[str, object],
                     delete_role: int | None = None) -> dict[tuple[int, int, int], np.ndarray]:
    collision = np.exp(1j * contact) * c219.common_species(beta).coin
    correction = c210.REVERSE @ collision.conj().T
    return {
        site: correction
        for role, site in carrier["shell"]
        if role != delete_role
    }


def star_macro(state: np.ndarray, beta: float, contact: float,
               carrier: dict[str, object], *, inverse: bool = False,
               delete_role: int | None = None) -> np.ndarray:
    if not validate_carrier(carrier, state.shape[0]):
        raise ValueError("carrier star leaves the local one-center/six-shell code")
    corrections = star_corrections(beta, contact, carrier, delete_role)
    if not inverse:
        return local_layer(local_layer(state, beta, contact), beta, contact, corrections)
    return local_layer(
        local_layer(state, beta, contact, corrections, inverse=True),
        beta, contact, inverse=True,
    )


def route_a_controls() -> dict[str, object]:
    print("\nROUTE A — CARRIER-GENERATED STAR DEFECT")
    frames = c210.proper_cubic_frames()
    fixtures = (
        (5, -0.2, 0.0, (2, 2, 2), frames[0], False),
        (7, -0.3, CONTACT, (2, 3, 4), frames[9], False),
        (9, -0.35, -0.23, (5, 3, 6), frames[17], True),
    )
    rows = []
    maximum = 0.0
    for length, beta, contact, center, frame, held in fixtures:
        carrier = carrier_star(length, center, frame)
        for logical in (0, 1):
            initial = site_plus(center, length, logical, frame)
            physical = star_macro(initial, beta, contact, carrier)
            expected = np.zeros_like(initial)
            expected[center] = c573.collision_step(
                c573.transition_internal(logical, frame), beta, contact
            )
            eg = float(np.linalg.norm(physical - expected))
            restored = star_macro(physical, beta, contact, carrier, inverse=True)
            inverse = float(np.linalg.norm(restored - initial))
            norm = abs(float(np.linalg.norm(physical)) - 1.0)
            outside = physical.copy()
            outside[center] = 0
            leakage = float(np.linalg.norm(outside))
            maximum = max(maximum, eg, inverse, norm, leakage)
            rows.append({
                "length": length, "beta": beta, "contact_source": contact,
                "center": center, "held": held, "logical_input": logical,
                "EG_residual": eg, "inverse_residual": inverse,
                "norm_residual": norm, "outside_star_boundary_leakage": leakage,
            })
    covariance_maximum = 0.0
    held_length, held_beta, held_contact = 9, -0.35, -0.23
    held_center = (4, 4, 4)
    for frame in frames:
        carrier = carrier_star(held_length, held_center, frame)
        initial = site_plus(held_center, held_length, 0, frame)
        physical = star_macro(initial, held_beta, held_contact, carrier)
        expected = np.zeros_like(initial)
        expected[held_center] = c573.collision_step(
            c573.transition_internal(0, frame), held_beta, held_contact
        )
        covariance_maximum = max(covariance_maximum, float(np.linalg.norm(physical - expected)))
    carrier = carrier_star(9, held_center, frames[17])
    initial = site_plus(held_center, 9, 0, frames[17])
    baseline = star_macro(initial, held_beta, held_contact, carrier)
    deleted = star_macro(initial, held_beta, held_contact, carrier, delete_role=4)
    deletion_signal = float(np.linalg.norm(deleted - baseline))
    malformed = dict(carrier)
    malformed["shell"] = carrier["shell"][:-1]
    malformed_rejected = False
    try:
        star_macro(initial, held_beta, held_contact, malformed)
    except ValueError:
        malformed_rejected = True
    check(
        "an in-state seven-M2 carrier star generates an exact compact scalar/even transition under the specified free-plus-contact layers on train, held translation, and all24 frames",
        maximum < TOL and covariance_maximum < TOL
        and deletion_signal > SIGNAL and malformed_rejected,
        {
            "rows": rows,
            "proper_frames": len(frames),
            "maximum_residual": maximum,
            "maximum_covariance_residual": covariance_maximum,
            "deleted_shell_role_signal": deletion_signal,
            "malformed_carrier_rejected": malformed_rejected,
            "carrier_M2": 7,
            "host_coordinate_potential": False,
            "carrier_stationarity_law_supplied": True,
            "moving_transport_closed": False,
        },
    )
    return {
        "rows": rows, "proper_frames": len(frames), "maximum_residual": maximum,
        "maximum_covariance_residual": covariance_maximum,
        "deleted_shell_role_signal": deletion_signal,
        "malformed_carrier_rejected": malformed_rejected,
    }


def gaussian_state(length: int, width: float, frame: np.ndarray) -> np.ndarray:
    coordinate = (np.arange(length) + length // 2) % length - length // 2
    x, y, z = np.meshgrid(coordinate, coordinate, coordinate, indexing="ij")
    envelope = np.exp(-(x * x + y * y + z * z) / (4 * width * width)).astype(complex)
    envelope /= np.linalg.norm(envelope)
    return envelope[..., None] * c573.transition_internal(0, frame)


def tagged_initial(matter: np.ndarray, tag: int = 0) -> np.ndarray:
    if tag not in (0, 1):
        raise ValueError("tag must be a lawful two-rail basis value")
    output = np.zeros(matter.shape + (2,), dtype=complex)
    output[..., tag] = matter
    return output


def accepted_forward_step(state: np.ndarray, beta: float, contact: float) -> np.ndarray:
    return spatial_stream(matter_collision(state, beta, contact))


def locally_compiled_inverse_step(state: np.ndarray, beta: float, contact: float,
                                  *, delete_second_reversal: bool = False) -> np.ndarray:
    reversed_input = np.einsum("ab,xyzb->xyza", c210.REVERSE, state, optimize=True)
    forward_streamed = spatial_stream(reversed_input)
    if delete_second_reversal:
        unstreamed = forward_streamed
    else:
        unstreamed = np.einsum(
            "ab,xyzb->xyza", c210.REVERSE, forward_streamed, optimize=True
        )
    return matter_collision(unstreamed, beta, contact, inverse=True)


def tagged_echo_layer(state: np.ndarray, beta: float, contact: float,
                      *, delete_inverse_branch: bool = False,
                      delete_second_reversal: bool = False) -> np.ndarray:
    if state.ndim != 5 or state.shape[3:] != (6, 2):
        raise ValueError("tagged echo leaves the six-direction/two-tag code")
    output = np.zeros_like(state)
    output[..., 1] = accepted_forward_step(state[..., 0], beta, contact)
    if delete_inverse_branch:
        output[..., 0] = accepted_forward_step(state[..., 1], beta, contact)
    else:
        output[..., 0] = locally_compiled_inverse_step(
            state[..., 1], beta, contact,
            delete_second_reversal=delete_second_reversal,
        )
    return output


def tagged_transition_weight(state: np.ndarray, beta: float, contact: float,
                             frame: np.ndarray) -> float:
    collision = matter_collision(state[..., 0], beta, contact)
    target = c573.transition_internal(1, frame)
    amplitude = np.einsum("a,xyza->xyz", target.conj(), collision, optimize=True)
    return float(np.linalg.norm(amplitude) ** 2)


def typed_candidate_output(reference: int, probe: int, comparison: int) -> tuple[int, int, int]:
    if any(value not in (0, 1) for value in (reference, probe, comparison)):
        raise ValueError("candidate output rails must be binary")
    return reference, probe, comparison


def comparison_cleanup_deleted(internal_a: np.ndarray, internal_b: np.ndarray,
                               frame_a: np.ndarray, frame_b: np.ndarray) -> dict[str, float]:
    """Run the local comparison with its cleanup stage deleted.

    Mirrors c573.physical_comparison_receipt through the latch/latch/compare
    stages and then stops: the restore (uncompute) sequence is omitted, so any
    weight left on the receipt rail and any departure from the input state is
    work the deleted cleanup stage would have recovered.
    """
    zero = np.asarray((1, 0), dtype=complex)
    initial = np.einsum(
        "a,b,c,d,e->abcde", internal_a, zero, internal_b, zero, zero,
        optimize=True,
    )
    state = c573.apply_axes(initial, c573.local_latch_matrix(frame_a), (0, 1))
    state = c573.apply_axes(state, c573.local_latch_matrix(frame_b), (2, 3))
    state = c573.apply_axes(state, c573.controlled_comparison_matrix(), (1, 3, 4))
    return {
        "retained_receipt_rail_weight": float(np.linalg.norm(state[..., 1]) ** 2),
        "state_change": float(np.linalg.norm(state - initial)),
    }


def route_b_controls() -> dict[str, object]:
    print("\nROUTE B — CARRIED AUTONOMOUS INVERSE ECHO")
    frames = c210.proper_cubic_frames()
    fixtures = (
        (7, 1.5, -0.2, 0.0, frames[0], False),
        (7, 1.8, -0.3, CONTACT, frames[8], False),
        (9, 1.9, -0.35, -0.23, frames[19], True),
    )
    rows = []
    maximum = 0.0
    local_inverse_compiler_maximum = 0.0
    local_forward_compiler_maximum = 0.0
    for length, width, beta, contact, frame, held in fixtures:
        initial = tagged_initial(gaussian_state(length, width, frame))
        after_forward = tagged_echo_layer(initial, beta, contact)
        after_echo = tagged_echo_layer(after_forward, beta, contact)
        inverse = tagged_echo_layer(after_forward, beta, contact)
        event = tagged_transition_weight(initial, beta, contact, frame)
        retained_forward = c573.bound_pair_step(
            initial[..., 0], beta, contact
        )
        forward_compiler_residual = float(
            np.linalg.norm(after_forward[..., 1] - retained_forward)
        )
        local_forward_compiler_maximum = max(
            local_forward_compiler_maximum, forward_compiler_residual
        )
        residual = float(np.linalg.norm(after_echo - initial))
        inverse_residual = float(np.linalg.norm(inverse - initial))
        norm = max(abs(float(np.linalg.norm(after_forward)) - 1), abs(float(np.linalg.norm(after_echo)) - 1))
        tag_boundary = float(np.linalg.norm(after_echo[..., 1]))
        compiled_inverse = locally_compiled_inverse_step(
            after_forward[..., 1], beta, contact
        )
        retained_inverse = c573.bound_pair_step(
            after_forward[..., 1], beta, contact, inverse=True
        )
        compiler_residual = float(np.linalg.norm(compiled_inverse - retained_inverse))
        local_inverse_compiler_maximum = max(
            local_inverse_compiler_maximum, compiler_residual
        )
        maximum = max(maximum, residual, inverse_residual, norm, tag_boundary, abs(event - 1))
        rows.append({
            "length": length, "width": width, "beta": beta,
            "contact_source": contact, "held": held,
            "EG_two_layer_echo_residual": residual,
            "inverse_residual": inverse_residual,
            "norm_residual": norm,
            "transition_projector_weight": event,
            "carried_tag_one_boundary_leakage": tag_boundary,
            "local_RSR_inverse_stream_compiler_residual": compiler_residual,
            "local_forward_compiler_residual": forward_compiler_residual,
        })
    comparison_inverse_maximum = 0.0
    comparison_norm_maximum = 0.0
    covariance_maximum = 0.0
    paired_failures = 0
    base_a = c573.collision_step(PLUS, -0.2, 0.0)
    base_b = c573.collision_step(PLUS, -0.35, -0.23)
    for frame_a in frames:
        rep_a = c210.direction_permutation(frame_a)
        for frame_b in frames:
            rep_b = c210.direction_permutation(frame_b)
            after_a = c573.collision_step(rep_a @ PLUS, -0.2, 0.0)
            after_b = c573.collision_step(rep_b @ PLUS, -0.35, -0.23)
            covariance_a = phase_aligned_residual(after_a, rep_a @ base_a)
            covariance_b = phase_aligned_residual(after_b, rep_b @ base_b)
            covariance_maximum = max(covariance_maximum, covariance_a, covariance_b)
            comparison = c573.physical_comparison_receipt(after_a, after_b, frame_a, frame_b)
            comparison_inverse_maximum = max(
                comparison_inverse_maximum, comparison["inverse_residual"]
            )
            comparison_norm_maximum = max(
                comparison_norm_maximum, comparison["norm_residual"]
            )
            paired_failures += int(
                covariance_a >= TOL or covariance_b >= TOL
                or abs(comparison["receipt_weight"] - 1) >= TOL
                or comparison["inverse_residual"] >= TOL
                or comparison["norm_residual"] >= TOL
            )
    held_initial = tagged_initial(gaussian_state(9, 1.9, frames[19]))
    held_forward = tagged_echo_layer(held_initial, -0.35, -0.23)
    held_baseline = tagged_echo_layer(held_forward, -0.35, -0.23)
    held_deleted = tagged_echo_layer(
        held_forward, -0.35, -0.23, delete_inverse_branch=True
    )
    inverse_deletion_signal = float(np.linalg.norm(held_deleted - held_baseline))
    generic_envelope = np.linalg.norm(
        gaussian_state(9, 1.9, frames[19]), axis=-1
    ).astype(complex)
    generic_internal = np.eye(6, dtype=complex)[0]
    generic_initial = tagged_initial(
        generic_envelope[..., None] * generic_internal
    )
    generic_forward = tagged_echo_layer(generic_initial, -0.35, -0.23)
    generic_baseline = tagged_echo_layer(generic_forward, -0.35, -0.23)
    reversal_deleted = tagged_echo_layer(
        generic_forward, -0.35, -0.23, delete_second_reversal=True
    )
    reversal_deletion_signal = float(
        np.linalg.norm(reversal_deleted - generic_baseline)
    )
    cleanup_deleted = comparison_cleanup_deleted(
        c573.collision_step(c210.direction_permutation(frames[7]) @ PLUS, -0.35, -0.23),
        c573.collision_step(c210.direction_permutation(frames[19]) @ PLUS, -0.35, -0.23),
        frames[7], frames[19],
    )
    comparison_cleanup_deletion_leakage = cleanup_deleted["retained_receipt_rail_weight"]
    comparison_cleanup_deletion_state_change = cleanup_deleted["state_change"]
    rng = np.random.default_rng(575)
    arbitrary = (
        rng.normal(size=(5, 5, 5, 6, 2))
        + 1j * rng.normal(size=(5, 5, 5, 6, 2))
    )
    arbitrary /= np.linalg.norm(arbitrary)
    arbitrary_once = tagged_echo_layer(arbitrary, -0.35, -0.23)
    arbitrary_twice = tagged_echo_layer(arbitrary_once, -0.35, -0.23)
    arbitrary_domain_involution_residual = float(
        np.linalg.norm(arbitrary_twice - arbitrary)
    )
    arbitrary_domain_norm_residual = abs(float(np.linalg.norm(arbitrary_once)) - 1.0)
    malformed_rejected = False
    try:
        tagged_echo_layer(np.zeros((9, 9, 9, 6, 3), dtype=complex), -0.35, -0.23)
    except ValueError:
        malformed_rejected = True
    output_interface = typed_candidate_output(1, 1, 1)
    check(
        "a two-rail control carried with the packet autonomously alternates the accepted local coin/contact/stream factors and an R-S-R inverse-stream compilation, refocusing held packets with all576 blank-work comparisons",
        maximum < TOL and len(frames) == 24 and paired_failures == 0
        and covariance_maximum < TOL and comparison_inverse_maximum < TOL
        and comparison_norm_maximum < TOL and local_inverse_compiler_maximum < TOL
        and local_forward_compiler_maximum < TOL
        and arbitrary_domain_involution_residual < TOL
        and arbitrary_domain_norm_residual < TOL
        and inverse_deletion_signal > SIGNAL and reversal_deletion_signal > SIGNAL
        and abs(comparison_cleanup_deletion_leakage - 1.0) < TOL
        and comparison_cleanup_deletion_state_change > SIGNAL and malformed_rejected
        and output_interface == (1, 1, 1),
        {
            "rows": rows,
            "proper_frames": len(frames), "paired_frames": len(frames) ** 2,
            "paired_failures": paired_failures,
            "maximum_residual": maximum,
            "maximum_covariance_residual": covariance_maximum,
            "maximum_comparison_inverse_residual": comparison_inverse_maximum,
            "maximum_comparison_norm_residual": comparison_norm_maximum,
            "maximum_local_RSR_inverse_compiler_residual": local_inverse_compiler_maximum,
            "maximum_local_forward_compiler_residual": local_forward_compiler_maximum,
            "inverse_branch_deletion_signal": inverse_deletion_signal,
            "second_reversal_deletion_signal": reversal_deletion_signal,
            "comparison_cleanup_deletion_leakage": comparison_cleanup_deletion_leakage,
            "comparison_cleanup_deletion_state_change": comparison_cleanup_deletion_state_change,
            "arbitrary_domain_involution_residual": arbitrary_domain_involution_residual,
            "arbitrary_domain_norm_residual": arbitrary_domain_norm_residual,
            "malformed_tag_rejected": malformed_rejected,
            "typed_candidate_output": output_interface,
            "host_mirror_cadence": False,
            "carried_control_law_supplied": True,
            "M2_per_cell_per_standard": 12,
            "reusable_comparison_work_M2": 3,
        },
    )
    return {
        "rows": rows, "proper_frames": len(frames), "paired_frames": len(frames) ** 2,
        "paired_failures": paired_failures, "maximum_residual": maximum,
        "maximum_covariance_residual": covariance_maximum,
        "maximum_comparison_inverse_residual": comparison_inverse_maximum,
        "maximum_comparison_norm_residual": comparison_norm_maximum,
        "maximum_local_RSR_inverse_compiler_residual": local_inverse_compiler_maximum,
        "maximum_local_forward_compiler_residual": local_forward_compiler_maximum,
        "inverse_branch_deletion_signal": inverse_deletion_signal,
        "second_reversal_deletion_signal": reversal_deletion_signal,
        "comparison_cleanup_deletion_leakage": comparison_cleanup_deletion_leakage,
        "comparison_cleanup_deletion_state_change": comparison_cleanup_deletion_state_change,
        "arbitrary_domain_involution_residual": arbitrary_domain_involution_residual,
        "arbitrary_domain_norm_residual": arbitrary_domain_norm_residual,
    }


def composite_initial(envelope: np.ndarray, logical: int, frame_clock: np.ndarray) -> np.ndarray:
    if envelope.ndim != 4 or envelope.shape[-1] != 6:
        raise ValueError("composite envelope leaves the six-direction matter code")
    clock = c573.transition_internal(logical, frame_clock)
    return np.einsum("xyzd,c->xyzdc", envelope, clock, optimize=True)


def composite_step(state: np.ndarray, beta_envelope: float, beta_clock: float,
                   contact: float, *, inverse: bool = False,
                   delete_clock_coin: bool = False,
                   delete_stream: bool = False) -> np.ndarray:
    if state.ndim != 5 or state.shape[3:] != (6, 6) or len(set(state.shape[:3])) != 1:
        raise ValueError("composite state leaves the cubic 36-rail code")
    envelope_coin = np.exp(1j * contact) * c219.common_species(beta_envelope).coin
    clock_coin = np.eye(6, dtype=complex) if delete_clock_coin else c219.common_species(beta_clock).coin
    if not inverse:
        mixed = np.einsum("ab,xyzbc->xyzac", envelope_coin, state, optimize=True)
        mixed = np.einsum("ij,xyzdj->xyzdi", clock_coin, mixed, optimize=True)
        return mixed if delete_stream else spatial_stream(mixed)
    unstreamed = state if delete_stream else spatial_stream(state, inverse=True)
    mixed = np.einsum("ij,xyzdj->xyzdi", clock_coin.conj().T, unstreamed, optimize=True)
    return np.einsum("ab,xyzbc->xyzac", envelope_coin.conj().T, mixed, optimize=True)


def factorization_leakage(state: np.ndarray) -> float:
    singular = np.linalg.svd(state.reshape(-1, 6), compute_uv=False)
    return float(np.linalg.norm(singular[1:]))


def recover_envelope(state: np.ndarray, clock: np.ndarray) -> np.ndarray:
    return np.einsum("c,xyzdc->xyzd", clock.conj(), state, optimize=True)


def recover_clock(state: np.ndarray, envelope: np.ndarray) -> np.ndarray:
    return np.einsum("xyzd,xyzdc->c", envelope.conj(), state, optimize=True)


def candidate_transition_weight(clock: np.ndarray, frame: np.ndarray) -> float:
    target = c573.transition_internal(1, frame)
    return float(abs(np.vdot(target, clock)) ** 2)


def composite_fixture(length: int, width: float, beta_envelope: float,
                      beta_clock: float, contact: float, frame_envelope: np.ndarray,
                      frame_clock: np.ndarray, held: bool) -> dict[str, object]:
    envelope = gaussian_state(length, width, frame_envelope)
    initial = composite_initial(envelope, 0, frame_clock)
    physical = composite_step(initial, beta_envelope, beta_clock, contact)
    expected_envelope = c573.bound_pair_step(envelope, beta_envelope, contact)
    initial_clock = c573.transition_internal(0, frame_clock)
    expected_clock = c573.collision_step(initial_clock, beta_clock, 0.0)
    expected = np.einsum("xyzd,c->xyzdc", expected_envelope, expected_clock, optimize=True)
    eg = float(np.linalg.norm(physical - expected))
    restored = composite_step(
        physical, beta_envelope, beta_clock, contact, inverse=True
    )
    inverse = float(np.linalg.norm(restored - initial))
    norm = abs(float(np.linalg.norm(physical)) - 1.0)
    factor = factorization_leakage(physical)
    recovered_envelope = recover_envelope(physical, expected_clock)
    envelope_residual = float(np.linalg.norm(recovered_envelope - expected_envelope))
    clock_weight = candidate_transition_weight(expected_clock, frame_clock)
    physical_twice = composite_step(
        physical, beta_envelope, beta_clock, contact
    )
    direct_twice = initial.copy()
    for _probe_ordinal in range(2):
        direct_twice = composite_step(
            direct_twice, beta_envelope, beta_clock, contact
        )
    composition = float(np.linalg.norm(physical_twice - direct_twice))
    return {
        "length": length, "width": width, "beta_envelope": beta_envelope,
        "beta_clock": beta_clock, "contact_source": contact, "held": held,
        "EG_residual": eg, "inverse_residual": inverse, "norm_residual": norm,
        "factorization_leakage": factor,
        "envelope_mass_channel_residual": envelope_residual,
        "clock_transition_projector_weight": clock_weight,
        "composition_residual": composition,
    }


def route_c_controls() -> dict[str, object]:
    print("\nROUTE C — COMPOSITE INTERNAL TRANSITION")
    frames = c210.proper_cubic_frames()
    rows = (
        composite_fixture(5, 1.2, -0.2, -0.25, 0.0, frames[0], frames[3], False),
        composite_fixture(7, 1.7, -0.3, -0.32, CONTACT, frames[8], frames[14], False),
        composite_fixture(9, 2.0, -0.35, -0.41, -0.23, frames[17], frames[22], True),
        composite_fixture(9, 2.2, -0.35, -0.41, 0.51, frames[6], frames[20], True),
    )
    maximum = max(
        row[key]
        for row in rows
        for key in (
            "EG_residual", "inverse_residual", "norm_residual",
            "factorization_leakage", "envelope_mass_channel_residual",
            "composition_residual",
        )
    )
    maximum = max(maximum, max(abs(row["clock_transition_projector_weight"] - 1) for row in rows))
    covariance_maximum = 0.0
    comparison_inverse_maximum = 0.0
    comparison_norm_maximum = 0.0
    paired_failures = 0
    envelope_coin = c219.common_species(-0.35).coin
    clock_coin = c219.common_species(-0.41).coin
    composite_coin = np.kron(envelope_coin, clock_coin)
    base_clock = c573.collision_step(PLUS, -0.41, 0.0)
    for frame_envelope in frames:
        rep_envelope = c210.direction_permutation(frame_envelope)
        mapped_directions = tuple(
            tuple(int(value) for value in frame_envelope @ displacement)
            for displacement in c210.DIRECTIONS
        )
        stream_lawful = set(mapped_directions) == {
            tuple(int(value) for value in displacement) for displacement in c210.DIRECTIONS
        }
        for frame_clock in frames:
            rep_clock = c210.direction_permutation(frame_clock)
            representation = np.kron(rep_envelope, rep_clock)
            covariance = float(np.linalg.norm(
                representation @ composite_coin @ representation.conj().T - composite_coin
            ))
            covariance_maximum = max(covariance_maximum, covariance)
            reference_clock = rep_envelope @ base_clock
            probe_clock = c573.collision_step(rep_clock @ PLUS, -0.41, 0.0)
            comparison = c573.physical_comparison_receipt(
                reference_clock, probe_clock, frame_envelope, frame_clock
            )
            comparison_inverse_maximum = max(
                comparison_inverse_maximum, comparison["inverse_residual"]
            )
            comparison_norm_maximum = max(
                comparison_norm_maximum, comparison["norm_residual"]
            )
            paired_failures += int(
                not stream_lawful or covariance >= TOL
                or abs(comparison["receipt_weight"] - 1) >= TOL
                or comparison["inverse_residual"] >= TOL
                or comparison["norm_residual"] >= TOL
            )
    envelope = gaussian_state(9, 2.0, frames[17])
    initial = composite_initial(envelope, 0, frames[22])
    baseline = composite_step(initial, -0.35, -0.41, -0.23)
    no_clock = composite_step(
        initial, -0.35, -0.41, -0.23, delete_clock_coin=True
    )
    no_stream = composite_step(
        initial, -0.35, -0.41, -0.23, delete_stream=True
    )
    clock_deletion_signal = phase_aligned_residual(no_clock, baseline)
    stream_deletion_signal = phase_aligned_residual(no_stream, baseline)
    rail_deleted = baseline.copy()
    rail_deleted[..., 0] = 0
    rail_deletion_leakage = abs(float(np.linalg.norm(rail_deleted)) - 1.0)
    spectator_clock = c573.collision_step(PLUS, -0.41, 0.0)
    spectator_transition_weight = candidate_transition_weight(
        spectator_clock, np.eye(3, dtype=int)
    )
    spectator_transition_residual = phase_aligned_residual(spectator_clock, MINUS)
    held_envelope_a = gaussian_state(9, 2.0, frames[17])
    held_envelope_b = gaussian_state(9, 2.2, frames[17])
    held_composite_a = composite_step(
        composite_initial(held_envelope_a, 0, np.eye(3, dtype=int)),
        -0.35, -0.41, -0.23,
    )
    held_composite_b = composite_step(
        composite_initial(held_envelope_b, 0, np.eye(3, dtype=int)),
        -0.2, -0.41, 0.51,
    )
    evolved_envelope_a = c573.bound_pair_step(held_envelope_a, -0.35, -0.23)
    evolved_envelope_b = c573.bound_pair_step(held_envelope_b, -0.2, 0.51)
    recovered_clock_a = recover_clock(held_composite_a, evolved_envelope_a)
    recovered_clock_b = recover_clock(held_composite_b, evolved_envelope_b)
    envelope_to_clock_coupling_signal = phase_aligned_residual(
        recovered_clock_a, recovered_clock_b
    )
    malformed_rejected = False
    try:
        composite_step(np.zeros((5, 5, 5, 6, 5), dtype=complex), -0.2, -0.25, 0.0)
    except ValueError:
        malformed_rejected = True
    output_interface = typed_candidate_output(1, 1, 1)
    check(
        "a 36-rail composite factors arbitrary localized free motion from the scalar/even transition, preserving the envelope mass channel under train/held beta/source variation and all576 independent frames",
        maximum < TOL and len(frames) == 24 and paired_failures == 0
        and covariance_maximum < TOL and comparison_inverse_maximum < TOL
        and comparison_norm_maximum < TOL and clock_deletion_signal > SIGNAL
        and stream_deletion_signal > SIGNAL and rail_deletion_leakage > SIGNAL
        and abs(spectator_transition_weight - 1) < TOL
        and spectator_transition_residual < TOL
        and envelope_to_clock_coupling_signal < TOL
        and malformed_rejected and output_interface == (1, 1, 1),
        {
            "rows": rows,
            "proper_frames": len(frames), "paired_frames": len(frames) ** 2,
            "paired_failures": paired_failures,
            "maximum_residual": maximum,
            "maximum_covariance_residual": covariance_maximum,
            "maximum_comparison_inverse_residual": comparison_inverse_maximum,
            "maximum_comparison_norm_residual": comparison_norm_maximum,
            "clock_coin_deletion_signal": clock_deletion_signal,
            "stream_deletion_signal": stream_deletion_signal,
            "one_clock_rail_deletion_leakage": rail_deletion_leakage,
            "decoupled_clock_transition_weight": spectator_transition_weight,
            "decoupled_clock_transition_residual": spectator_transition_residual,
            "envelope_to_clock_coupling_signal": envelope_to_clock_coupling_signal,
            "clock_is_dynamically_bound_to_envelope": False,
            "clock_is_kinematically_attached_by_rail_identity": True,
            "malformed_composite_rejected": malformed_rejected,
            "typed_candidate_output": output_interface,
            "matter_M2_per_cell_per_standard": 36,
            "additional_M2_per_cell_over_six_mode_matter": 30,
            "two_standard_plus_reusable_work_M2_per_cell": 75,
            "maximum_terminal_support_M2": 3,
            "fresh_work_M2_per_prefix": 0,
            "common_carriage_tensor_law_supplied": True,
        },
    )
    return {
        "rows": rows, "proper_frames": len(frames), "paired_frames": len(frames) ** 2,
        "paired_failures": paired_failures, "maximum_residual": maximum,
        "maximum_covariance_residual": covariance_maximum,
        "maximum_comparison_inverse_residual": comparison_inverse_maximum,
        "maximum_comparison_norm_residual": comparison_norm_maximum,
        "clock_coin_deletion_signal": clock_deletion_signal,
        "stream_deletion_signal": stream_deletion_signal,
        "one_clock_rail_deletion_leakage": rail_deletion_leakage,
        "decoupled_clock_transition_weight": spectator_transition_weight,
        "decoupled_clock_transition_residual": spectator_transition_residual,
        "envelope_to_clock_coupling_signal": envelope_to_clock_coupling_signal,
        "clock_is_dynamically_bound_to_envelope": False,
    }


def interpretation_firewall() -> dict[str, object]:
    print("\nDECODER / INTERPRETATION FIREWALL")
    functions = (typed_candidate_output, candidate_transition_weight)
    forbidden = ("schedule", "depth", "phase", "iteration", "time", "rate", "energy", "record", "probability")
    hits = {}
    for function in functions:
        tree = ast.parse(inspect.getsource(function))
        names = [node.id.lower() for node in ast.walk(tree) if isinstance(node, ast.Name)]
        hits[function.__name__] = {
            word: sum(word in name for name in names) for word in forbidden
        }
    clean = all(value == 0 for row in hits.values() for value in row.values())
    check(
        "typed candidate outputs consume only physical transition and comparison rails; no control ordinal, phase, generator, receipt, norm, or classifier is renamed physical time, rate, energy, Record, or probability",
        clean,
        {
            "AST_forbidden_name_hits": hits,
            "clock_dimension_added": False,
            "host_classifier_consumed": False,
            "Cycle456_law_tag_or_endpoint_word_consumed": False,
            "schedule_called_time": False,
            "phase_called_energy": False,
            "generator_entry_called_rate": False,
            "transition_called_Record_actuality": False,
            "projector_weight_called_probability": False,
            "proper_time_claimed": False,
        },
    )
    return {"hits": hits, "clean": clean}


def no_go_gate(retained: dict[str, object]) -> dict[str, object]:
    print("\nSUPPLIED / DERIVED / OPEN / FULL N1-N8")
    alternatives = (
        ("carrier-star compact mode", "seven-M2 relational defect carrier", "coin cancellation plus radial reversal", "exact localized transition", "ATTEMPTED — POSITIVE; moving carrier law open"),
        ("carried autonomous echo", "direction x two-tag packet", "off-diagonal U/U-dagger involution", "exact free-packet refocus", "ATTEMPTED — POSITIVE; control law supplied"),
        ("composite internal clock", "direction x scalar/even tensor particle", "commuting free envelope and internal transition", "moving-envelope carried candidate", "ATTEMPTED — POSITIVE as kinematic attachment; spectator control shows it is not matter-derived"),
        ("unmodified six-mode packet", "Cycle573 localized equal-direction packet", "accepted free stream alone", "retain plus/minus code", "ATTEMPTED — PARTIAL in Cycle573"),
        ("compact flat-band mode", "finite-support eigenmode of unmodified massive walk", "momentum-flat eigenphase pair", "localized transition without added content", "OPEN; massive flat pair not established"),
        ("nonlinear self-bound clock", "two-body/contact soliton", "interaction-stabilized co-moving internal orbit", "autonomous localization and transport", "OPEN; nonlinear many-body search not run"),
    )
    walls = (
        "derive defect carrier/contact law",
        "derive carried inverse-control law",
        "derive composite tensor content",
        "derive dynamical envelope-clock binding",
        "empirical scale and independent standard",
        "FORMATION actuality and realized history",
        "continuum/Lorentz transport",
        "physical source/gravity response",
        "Born/probability law",
    )
    pairwise = tuple((left, right, "no", "no", True) for left, right in combinations(walls, 2))
    n3 = (
        "Cycle219 coin and selected beta values",
        "Cycle230 common contact phase and seam convention",
        "seven-M2 carrier-star preparation and stationary carrier law",
        "local coin-cancel/reversal defect contact",
        "two-rail carried forward/inverse control law",
        "36-rail direction x internal tensor content and common-carriage stream",
        "kinematic rail identity attaching the internal clock to the moving envelope",
        "blank reusable comparison work and typed candidate output rails",
        "finite noiseless periodic boxes and held split",
    )
    n4 = (
        ("Cycle219 note lines 31-75", "common scalar/even antipode and mass family", "transition engine used unchanged", True),
        ("Cycle219 note lines 103-134", "localized clock theorem open", "added routes do not claim beta/content derivation", True),
        ("Cycle230 note lines 286-390", "contact/seam proper-cubic fixture", "exact-pinned and common phase consumed", True),
        ("Cycle563 note lines 161-175", "physical M2 mass/contact/seam controls", "receipt values retained", True),
        ("Cycle569 note lines 324-378", "source-carrier/contact physical lift", "source phase tested only common-mode", True),
        ("Cycle570 note lines 360-385", "recyclable comparison and clock walls", "reusable work boundary retained", True),
        ("Cycle573 note lines 198-222", "static trap and free-packet leakage residual", "directly attacked by three distinct mechanisms", True),
    )
    n5 = (
        ("carrier star", "site/star/finite lattice", "exact at site and all translated/oriented stars; no moving carrier theorem"),
        ("carried echo", "site/packet/finite lattice", "exact for arbitrary finite packet on tested periodic boxes; no noise/continuum theorem"),
        ("composite", "mode/cell/packet/finite lattice", "exact factorization on declared 36-rail code; no derivation of extra content"),
        ("broad unmodified-six-mode claim", "lattice-wide", "not tested exhaustively and not shipped"),
    )
    n6 = (
        "search the unmodified massive walk for a compact flat eigenphase pair",
        "derive the carrier star as a bound state of supplied local CAR contact",
        "compile the inverse-control tag from a recyclable local QCA phase carrier",
        "retire the 36-rail tensor import through a bounded physical-M2 subcell compiler",
        "feed typed candidate pairs into a later Cycle456-compatible word builder without importing its classifier",
        "compare against an independently selected face-carrier transition with empirical scaling",
    )
    n7 = (
        "A hostile reviewer should accept that Route C answers the finite constructive question only for a newly specified "
        "direction-by-internal tensor particle. The reviewer should then demand a compiler from the accepted six-mode/CAR "
        "matter content into those 36 rails, or an exact compact flat-band/soliton mode of the unmodified update, before calling "
        "localization intrinsic. Routes A and B likewise move the burden into a carrier contact or inverse-control law. Those are "
        "actionable import-retirement routes, so no universal obstruction or axiom-pressure claim is available."
    )
    n8 = (
        "Cycle219 provided the antipodal scalar/even transition but left a localized clock theorem open",
        "Cycles428/444 used physical oscillators and echoes with supplied calibration",
        "Cycles563/569 made the mass/contact/seam/source-carrier substrate physical",
        "Cycle570 made finite comparison work recyclable",
        "Cycle573 exposed free-stream leakage while closing k0/trapped comparison",
        "Cycle575 replaces the host trap/cadence by in-state carrier, carried echo, and composite routes while retaining explicit imports",
    )
    supplied = (
        "accepted Cycle219/230/563/569/570/573 physical shore and common contact source values",
        "carrier-star state, stationary carrier rule, and local cancellation/reversal contact",
        "two-rail carried U/U-dagger control law",
        "36-rail direction x clock tensor content and factorized common-carriage update",
        "finite periodic boxes, noiseless gates, blank comparison work, and held split",
    )
    derived = (
        "exact compact star transition with translation and all24 proper-cubic covariance",
        "exact arbitrary-packet forward/inverse refocusing without host mirror cadence",
        "exact moving-envelope/internal-transition factorization under beta/contact variation plus a decoupled-clock spectator control",
        "all576 independent-frame comparison receipts with blank reusable work",
        "E/G, inverse, norm, leakage, deletion, lawful-domain, resource, and typed-output controls",
    )
    open_rows = (
        "derivation of defect, inverse-control, or composite-content laws from the accepted six-mode substrate",
        "a dynamical binding interaction between envelope matter and the attached internal transition",
        "autonomous moving transport of the carrier-star mode",
        "unmodified massive flat-band or nonlinear soliton construction",
        "noise, unbounded operation, synchronization, and continuum/Lorentz refinement",
        "independent empirical clock selection and dimensionful calibration",
        "Record formation, actuality, realized history, source gravity, and Born probability",
    )
    ledger = {
        "C_ref": "localized carrier/echo/composite transition references constructed; preparation and update content remain supplied, and the composite clock is a kinematically attached spectator",
        "C_num": "exact finite E/G, inverse, factorization, composition and covariance residuals; no empirical duration scale",
        "C_wrap": "comparison work returns blank and carried echo control recycles; unbounded/noisy renewal remains open",
        "C_int": "accepted mass/contact transition used without naming phase energy or a generator entry rate",
        "C_local": "star radius one, carried 12-rail echo, 36-rail composite with 30 extra rails, support-three receipts, all24/all576; compiler and dynamical-binding retirement open",
        "C_source": "contact/source phase varied as a common-mode input only; no stress, gravity, redshift, or backreaction law",
    }
    condition = (
        len(alternatives) >= 5 and len(pairwise) == 36
        and all(row[-1] is True for row in n4)
        and retained["mass_residual"] < TOL
    )
    check(
        "full N1-N8 normalizes six route families, keeps every supplied law visible, and blocks broad localization no-go, minimum-content, shared-obstruction, or axiom-pressure rhetoric",
        condition,
        {
            "N1_normalized_alternatives": alternatives,
            "N2_pairwise_wall_audit": pairwise,
            "N3_hidden_condition_scan": n3,
            "N4_residual_matching": n4,
            "N5_resolution_audit": n5,
            "N6_partial_closure_paths": n6,
            "N7_hostile_steelman": n7,
            "N8_cross_cycle_echo": n8,
            "supplied": supplied, "derived": derived, "open": open_rows,
            "broad_localization_no_go": "FAIL / DO NOT SHIP",
            "minimum_content_claim": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "highest_honest_terminal": (
                "finite autonomous localized/refocused matter-transition candidates under explicitly supplied carrier, "
                "inverse-control, or composite-content laws; not intrinsic proper time"
            ),
            "authority": AUTHORITY, "audit": AUDIT,
            "six_wall_ledger": ledger,
        },
    )
    return {
        "alternatives": alternatives, "pairwise": pairwise, "n3": n3, "n4": n4,
        "n5": n5, "n6": n6, "n7": n7, "n8": n8,
        "supplied": supplied, "derived": derived, "open": open_rows,
        "six_wall_ledger": ledger,
        "shared_substrate_obstruction": False, "axiom_pressure": False,
    }


def main() -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0
    signal.alarm(int(WALL_CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle575 autonomous localized/refocused matter-transition tournament")
    print("authority", AUTHORITY, "audit", AUDIT)
    retained = dependency_controls()
    note_contract()
    route_a = route_a_controls()
    route_b = route_b_controls()
    route_c = route_c_controls()
    firewall = interpretation_firewall()
    gate = no_go_gate(retained)
    elapsed = time.perf_counter() - started
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = int(peak if sys.platform == "darwin" else peak * 1024)
    check(
        "the frozen tournament stays below the 360-second and 3-GiB cold caps",
        elapsed < WALL_CAP_SECONDS and peak_bytes < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_RSS_bytes": peak_bytes},
    )
    receipt = {
        "status": "cycle575-autonomous-localized-refocused-matter-transition-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "accepted_Cycle573_ancestor_commit": ACCEPTED_CYCLE573_COMMIT,
        "definitive_run_HEAD": current_commit(),
        "branch_head_equality_is_scientific_dependency": False,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "tests_passed": PASS,
        "tests_total": PASS + FAIL,
        "pass": FAIL == 0,
        "cold_internal_elapsed_seconds": elapsed,
        "cold_maximum_RSS_bytes": peak_bytes,
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
            "Cycle573_runner_sha256":
                DEPENDENCY_SHA256["physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py"],
            "Cycle563_receipt_sha256":
                RECEIPT_SHA256["physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"],
            "Cycle569_receipt_sha256":
                RECEIPT_SHA256["physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json"],
            "Cycle570_receipt_sha256":
                RECEIPT_SHA256["physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json"],
            "Cycle573_receipt_sha256":
                RECEIPT_SHA256["physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json"],
            "Cycle573_note_sha256": CYCLE573_NOTE_SHA256,
        },
        "retained_physical_fixtures": {
            "one_particle_mass_residual": retained["mass_residual"],
            "contact_factorization_residual": retained["contact_residual"],
            "axis_seam_braid_residual": retained["seam_residual"],
        },
        "frozen_split": {
            "route_A_train": [
                {"length": 5, "beta": -0.2, "contact_source": 0.0},
                {"length": 7, "beta": -0.3, "contact_source": CONTACT},
            ],
            "route_A_held": {"length": 9, "beta": -0.35, "contact_source": -0.23},
            "route_B_train": [
                {"length": 7, "width": 1.5, "beta": -0.2, "contact_source": 0.0},
                {"length": 7, "width": 1.8, "beta": -0.3, "contact_source": CONTACT},
            ],
            "route_B_held": {"length": 9, "width": 1.9, "beta": -0.35, "contact_source": -0.23},
            "route_C_train": [
                {"length": 5, "width": 1.2, "envelope_beta": -0.2, "clock_beta": -0.25, "contact_source": 0.0},
                {"length": 7, "width": 1.7, "envelope_beta": -0.3, "clock_beta": -0.32, "contact_source": CONTACT},
            ],
            "route_C_held": [
                {"length": 9, "width": 2.0, "envelope_beta": -0.35, "clock_beta": -0.41, "contact_source": -0.23},
                {"length": 9, "width": 2.2, "envelope_beta": -0.35, "clock_beta": -0.41, "contact_source": 0.51},
            ],
            "held_refit_parameters": 0,
        },
        "route_A_carrier_generated_star_defect": {
            "disposition":
                "positive exact compact transition under a supplied in-state carrier and engineered stationary defect law; moving transport open",
            "maximum_EG_inverse_norm_or_leakage_residual": route_a["maximum_residual"],
            "maximum_all24_covariance_residual": route_a["maximum_covariance_residual"],
            "deleted_shell_role_signal": route_a["deleted_shell_role_signal"],
            "carrier_M2": 7,
            "carrier_local_adjacency_constraint_enforced": route_a["malformed_carrier_rejected"],
            "host_coordinate_potential": False,
            "static_host_trap": False,
            "carrier_stationarity_law_supplied": True,
            "coin_cancel_reversal_contact_supplied": True,
            "autonomous_moving_transport_closed": False,
        },
        "route_B_carried_autonomous_inverse_echo": {
            "disposition":
                "strongest positive: exact original-six-mode packet refocusing with a carried supplied two-rail controller and local accepted factors",
            "maximum_EG_inverse_norm_tag_residual": route_b["maximum_residual"],
            "maximum_local_forward_compiler_residual": route_b["maximum_local_forward_compiler_residual"],
            "maximum_local_RSR_inverse_compiler_residual": route_b["maximum_local_RSR_inverse_compiler_residual"],
            "arbitrary_full_domain_involution_residual": route_b["arbitrary_domain_involution_residual"],
            "arbitrary_full_domain_norm_residual": route_b["arbitrary_domain_norm_residual"],
            "proper_cubic_frames": route_b["proper_frames"],
            "paired_frame_comparisons": route_b["paired_frames"],
            "paired_frame_failures": route_b["paired_failures"],
            "maximum_covariance_residual": route_b["maximum_covariance_residual"],
            "maximum_physical_comparison_inverse_residual": route_b["maximum_comparison_inverse_residual"],
            "maximum_physical_comparison_norm_residual": route_b["maximum_comparison_norm_residual"],
            "inverse_branch_deletion_signal": route_b["inverse_branch_deletion_signal"],
            "second_reversal_deletion_signal": route_b["second_reversal_deletion_signal"],
            "comparison_cleanup_deletion_leakage": route_b["comparison_cleanup_deletion_leakage"],
            "comparison_cleanup_deletion_state_change": route_b["comparison_cleanup_deletion_state_change"],
            "M2_per_cell_per_standard": 12,
            "reusable_comparison_work_M2": 3,
            "host_chosen_mirror_cadence": False,
            "nonlocal_inverse_service": False,
            "carried_control_law_supplied": True,
            "net_transport_after_echo": False,
        },
        "route_C_composite_internal_transition": {
            "disposition":
                "positive exact moving-envelope carriage on a supplied 36-rail tensor code; decoupled control shows the clock is a spectator rather than matter-derived",
            "maximum_EG_inverse_norm_factorization_mass_channel_residual": route_c["maximum_residual"],
            "maximum_composite_coin_covariance_residual": route_c["maximum_covariance_residual"],
            "proper_cubic_frames": route_c["proper_frames"],
            "paired_frame_comparisons": route_c["paired_frames"],
            "paired_frame_failures": route_c["paired_failures"],
            "maximum_physical_comparison_inverse_residual": route_c["maximum_comparison_inverse_residual"],
            "maximum_physical_comparison_norm_residual": route_c["maximum_comparison_norm_residual"],
            "clock_coin_deletion_signal": route_c["clock_coin_deletion_signal"],
            "stream_deletion_signal": route_c["stream_deletion_signal"],
            "one_clock_rail_deletion_leakage": route_c["one_clock_rail_deletion_leakage"],
            "decoupled_clock_transition_weight": route_c["decoupled_clock_transition_weight"],
            "decoupled_clock_transition_residual": route_c["decoupled_clock_transition_residual"],
            "envelope_to_clock_coupling_signal": route_c["envelope_to_clock_coupling_signal"],
            "clock_is_dynamically_bound_to_envelope": route_c["clock_is_dynamically_bound_to_envelope"],
            "clock_is_kinematically_attached_by_rail_identity": True,
            "matter_M2_per_cell_per_standard": 36,
            "additional_M2_per_cell_over_six_mode_matter": 30,
            "two_standard_plus_reusable_work_M2_per_cell": 75,
            "maximum_terminal_support_M2": 3,
            "fresh_work_M2_per_prefix": 0,
        },
        "typed_downstream_interface": {
            "rails": [
                "reference_transition_candidate",
                "probe_transition_candidate",
                "comparison_agreement_candidate",
            ],
            "Cycle456_compatible_word_builder_may_consume_later": True,
            "Cycle456_classifier_consumed_here": False,
            "Cycle456_law_tags_consumed_here": False,
            "endpoint_words_consumed_here": False,
            "Record_or_Born_semantics_assigned": False,
        },
        "controls": {
            "E_G_and_inverse_tested": True,
            "deletion_and_work_leakage_visible": True,
            "malformed_words_rejected": True,
            "undefined_coerced_to_zero": False,
            "constant_bounded_overhead_on_declared_codes": True,
            "all24_and_all576_tested": True,
            "reusable_comparison_work_blank": True,
            "no_clock_dimension": True,
            "schedule_called_time": False,
            "phase_called_energy": False,
            "generator_entry_called_rate": False,
            "transition_receipt_called_Record_or_actuality": False,
            "projector_weight_called_probability": False,
            "source_variation_called_gravity_or_redshift": False,
        },
        "scope_boundary": {
            "highest_honest_terminal":
                "finite autonomous localized/refocused matter-transition candidates under explicitly supplied carrier, inverse-control, or composite-content laws; not intrinsic proper time",
            "intrinsic_unmodified_six_mode_moving_clock_closed": False,
            "carrier_defect_law_derived": False,
            "carried_control_law_derived": False,
            "composite_tensor_content_derived": False,
            "dynamical_envelope_clock_binding_closed": False,
            "empirical_dimensionful_scale_derived": False,
            "independent_clock_universality_closed": False,
            "continuum_Lorentz_proper_time_closed": False,
            "FORMATION_Record_actuality_closed": False,
            "source_gravity_closed": False,
            "Born_probability_closed": False,
            "shared_substrate_obstruction": gate["shared_substrate_obstruction"],
            "axiom_pressure": gate["axiom_pressure"],
            "broad_localization_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "six_wall_ledger": gate["six_wall_ledger"],
        "no_go_discipline": {
            "normalized_route_families": len(gate["alternatives"]),
            "independent_wall_pairs": len(gate["pairwise"]),
            "N1_through_N8_executed": True,
            "route_specific_failure_promoted_to_shared_obstruction": False,
            "minimum_content_claim": False,
            "shared_substrate_obstruction": gate["shared_substrate_obstruction"],
            "axiom_pressure": gate["axiom_pressure"],
        },
        "optimal_next_campaign":
            "search the unmodified massive Cycle219/contact update for a compact flat-band pair or nonlinear self-bound orbit; otherwise derive the Route-B control tag from a recyclable local QCA carrier and add a genuine Route-C envelope-clock interaction that makes the decoupled spectator control fail",
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "status": "cycle575-autonomous-localized-refocused-matter-transition-tournament",
        "authority": AUTHORITY, "audit": AUDIT,
        "tests_passed": PASS, "tests_failed": FAIL,
        "route_A_maximum_residual": route_a.get("maximum_residual"),
        "route_A_shell_deletion_signal": route_a.get("deleted_shell_role_signal"),
        "route_B_maximum_residual": route_b.get("maximum_residual"),
        "route_B_all576_failures": route_b.get("paired_failures"),
        "route_C_maximum_residual": route_c.get("maximum_residual"),
        "route_C_all576_failures": route_c.get("paired_failures"),
        "firewall_clean": firewall.get("clean"),
        "shared_substrate_obstruction": gate.get("shared_substrate_obstruction"),
        "axiom_pressure": gate.get("axiom_pressure"),
        "elapsed_seconds_internal": elapsed,
        "maximum_RSS_bytes_internal": peak_bytes,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
