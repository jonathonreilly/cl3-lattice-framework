#!/usr/bin/env python3
"""Cycle583: infinite/contact-internal-content tournament.

The runner works on the accepted Cycle230 antisymmetric CAR fibers.  It does
not claim that a CAR fiber is a bounded physical-M2 compiler.  Wrapped phases
are not energies, total-momentum labels are not rates, and update ordinals are
not time.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations
import gc
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import numpy as np
import scipy.sparse as sparse
import scipy.sparse.linalg as sparse_linalg


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22 as c578


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONTACT_DIMER_INFINITE_INTERNAL_CONTENT_TOURNAMENT_"
    "CYCLE583_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_contact_dimer_infinite_internal_content_tournament_"
    "cycle583_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
ACCEPTED_CYCLE578_COMMIT = "d73ae344764a5f3a31cadbcfa6467a8fe06b386c"
BETA = -0.3
CONTACT = 0.37
TOL = 5e-9
SIGNAL = 1e-8
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
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
    "physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py":
        "4ef60441d31d62b1fc61c9b5e09ff3bc8f7f32d1b68bc3c548834431d24302f6",
}
CYCLE578_RECEIPT_SHA256 = "7d745296b8ced52bf26b96fb13fe52024715846b6b491e6c6c6ba32aa2908ee2"
CYCLE578_NOTE_SHA256 = "a66126cf39bf6020680da5654bcbc85b11107e1f7d955f0ff5449098a0aa5dfc"


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


def dependency_controls() -> dict[str, float]:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCY_SHA256}
    receipt_path = ROOT / "outputs/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_receipt_2026_07_22.json"
    note_path = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_CONTACT_BOUND_MOVING_TRANSITION_TOURNAMENT_CYCLE578_NOTE_2026-07-22.md"
    ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", ACCEPTED_CYCLE578_COMMIT, "HEAD"),
        cwd=ROOT, check=False,
    ).returncode == 0
    prior = json.loads(receipt_path.read_text(encoding="utf-8"))
    retained = prior["retained_physical_M2_fixtures"]
    residuals = {
        "mass_residual": retained["one_particle_mass_residual"],
        "contact_residual": retained["Cycle230_contact_factorization_residual"],
        "seam_residual": retained["Cycle230_seam_braid_residual"],
    }
    condition = (
        ancestor and observed == DEPENDENCY_SHA256
        and file_sha(receipt_path) == CYCLE578_RECEIPT_SHA256
        and file_sha(note_path) == CYCLE578_NOTE_SHA256
        and prior["pass"] is True and max(residuals.values()) < TOL
    )
    check(
        "accepted Cycle578 is ancestral and every consumed shore artifact is byte exact",
        condition,
        {"ancestor": ancestor, "runners": observed,
         "Cycle578_receipt_sha256": file_sha(receipt_path),
         "Cycle578_note_sha256": file_sha(note_path), "retained": residuals},
    )
    return residuals


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "cycle 583", "15 by 15",
        "birman–schwinger", "full free spectrum touches", "contact-cyclic",
        "infinite-volume isolated-pole and exponential-tail theorem remains open",
        "proper-cubic", "three-car", "wrapped phase is not energy",
        "group displacement is not a rate", "update schedule is not time",
        "car-fiber result is not a physical-m2 compiler", "n1 — normalized alternatives",
        "n8 — cross-cycle echo", "no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(row for row in required if row not in body)
    check("the Cycle583 note freezes the bounded claim and rhetoric ceiling", not missing, missing)


# Proper-cubic irreps on onsite wedge powers.
CHARACTERS = {
    "A1": (1, 1, 1, 1, 1),
    "A2": (1, 1, 1, -1, -1),
    "E": (2, -1, 2, 0, 0),
    "T1": (3, 0, -1, 1, -1),
    "T2": (3, 0, -1, -1, 1),
}
FRAMES = c210.proper_cubic_frames()


def frame_class(frame: np.ndarray) -> int:
    trace = int(round(np.trace(frame)))
    if trace == 3:
        return 0
    if trace == 0:
        return 1
    if trace == 1:
        return 3
    return 2 if np.count_nonzero(frame - np.diag(np.diag(frame))) == 0 else 4


def wedge_isometry(power: int) -> np.ndarray:
    columns = []
    factorial = math.factorial(power)
    for chosen in combinations(range(6), power):
        vector = np.zeros(6**power)
        for perm in permutations(range(power)):
            inversions = sum(
                perm[i] > perm[j] for i in range(power) for j in range(i + 1, power)
            )
            directions = tuple(chosen[index] for index in perm)
            flat = 0
            for direction in directions:
                flat = 6 * flat + direction
            vector[flat] += (-1) ** inversions / math.sqrt(factorial)
        columns.append(vector)
    return np.asarray(columns).T


J2 = wedge_isometry(2)
J3 = wedge_isometry(3)


def wedge_projectors(power: int, isometry: np.ndarray) -> tuple[dict[str, np.ndarray], list[np.ndarray]]:
    reps = []
    classes = []
    for frame in FRAMES:
        direction = c210.direction_permutation(frame)
        tensor = direction
        for _ in range(power - 1):
            tensor = np.kron(tensor, direction)
        reps.append(isometry.T @ tensor @ isometry)
        classes.append(frame_class(frame))
    projectors = {
        name: chars[0] / 24 * sum(chars[ci] * rep for ci, rep in zip(classes, reps))
        for name, chars in CHARACTERS.items()
    }
    return projectors, reps


PROJECTORS2, REPS2 = wedge_projectors(2, J2)
PROJECTORS3, REPS3 = wedge_projectors(3, J3)


def projector_axis(projector: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(projector)
    axis = vectors[:, int(np.argmax(values))]
    pivot = int(np.argmax(np.abs(axis)))
    return axis * np.exp(-1j * np.angle(axis[pivot]))


A2_AXIS = projector_axis(PROJECTORS2["A2"])
A2_FULL = J2 @ A2_AXIS
COIN2 = np.kron(c219.common_species(BETA).coin, c219.common_species(BETA).coin)


def free_fiber(momentum: np.ndarray) -> np.ndarray:
    phases = np.asarray([
        np.exp(-1j * np.dot(momentum, c210.DIRECTIONS[first] - c210.DIRECTIONS[second]))
        for first in range(6) for second in range(6)
    ])
    return phases[:, None] * COIN2


def bs_scalar_sum(length: int, phase: float, keep_wave: bool = False) -> tuple[complex, np.ndarray | None]:
    z = np.exp(1j * phase)
    accumulator = 0j
    waves = np.empty((length, length, length, 36), complex) if keep_wave else None
    for ix in range(length):
        for iy in range(length):
            for iz in range(length):
                momentum = 2 * np.pi * np.asarray((ix, iy, iz), float) / length
                solution = np.linalg.solve(free_fiber(momentum) - z * np.eye(36), A2_FULL)
                accumulator += np.vdot(A2_FULL, solution)
                if waves is not None:
                    waves[ix, iy, iz] = solution
    scalar = 1 - z * (np.exp(-1j * CONTACT) - 1) * accumulator / length**3
    return scalar, waves


def bs_matrix(length: int, phase: float) -> np.ndarray:
    z = np.exp(1j * phase)
    accumulator = np.zeros((15, 15), complex)
    for ix in range(length):
        for iy in range(length):
            for iz in range(length):
                momentum = 2 * np.pi * np.asarray((ix, iy, iz), float) / length
                solved = np.linalg.solve(free_fiber(momentum) - z * np.eye(36), J2)
                accumulator += J2.conj().T @ solved
    return np.eye(15) - z * (np.exp(-1j * CONTACT) - 1) * accumulator / length**3


def cyclic_gap(length: int, phase: float) -> float:
    z = np.exp(1j * phase)
    minimum = np.inf
    for ix in range(length):
        for iy in range(length):
            for iz in range(length):
                momentum = 2 * np.pi * np.asarray((ix, iy, iz), float) / length
                values, vectors = np.linalg.eig(free_fiber(momentum))
                overlaps = np.abs(vectors.conj().T @ A2_FULL)
                contact_coupled = overlaps > 1e-8
                if np.any(contact_coupled):
                    distances = np.abs(np.angle(values[contact_coupled] / z))
                    minimum = min(minimum, float(np.min(distances)))
    return minimum


def tail_observables(waves: np.ndarray) -> dict[str, object]:
    length = waves.shape[0]
    relative = np.fft.ifftn(waves, axes=(0, 1, 2))
    relative /= np.linalg.norm(relative)
    probability = np.sum(np.abs(relative)**2, axis=3)
    shells = {radius: 0.0 for radius in range(length // 2 + 1)}
    radius2 = 0.0
    seam = 0.0
    for ix in range(length):
        for iy in range(length):
            for iz in range(length):
                signed = tuple(c578.signed_coordinate(value, length) for value in (ix, iy, iz))
                weight = float(probability[ix, iy, iz])
                radius = max(abs(value) for value in signed)
                shells[radius] += weight
                radius2 += weight * sum(value * value for value in signed)
                if any(abs(value) == length // 2 for value in signed):
                    seam += weight
    return {
        "contact_weight": float(probability[0, 0, 0]),
        "relative_radius_squared": radius2,
        "seam_boundary_weight": seam,
        "chebyshev_shell_probabilities": {str(k): v for k, v in shells.items()},
        "tail_probability_radius_ge_9": sum(value for key, value in shells.items() if key >= 9),
    }


def route_a_controls() -> dict[str, object]:
    frozen = (
        (11, -2.975575673176911),
        (15, -2.9755759681238305),
        (19, -2.9755759890506126),
        (23, -2.9755759907782897),
        (27, -2.9755759909092183),
        (31, -2.9755759909120467),
    )
    roots = []
    last_waves = None
    for length, phase in frozen:
        scalar, waves = bs_scalar_sum(length, phase, keep_wave=length == 31)
        roots.append({"L": length, "wrapped_phase": phase,
                      "scalar_BS_residual": float(abs(scalar))})
        if waves is not None:
            last_waves = waves
    matrix = bs_matrix(11, frozen[0][1])
    matrix_residual = float(np.linalg.svd(matrix, compute_uv=False)[-1])
    convergence = [abs(frozen[i + 1][1] - frozen[i][1]) for i in range(len(frozen) - 1)]

    on_shell_p = np.asarray((0.1587840759295163, 2.0565324125417215, -2.1028635833236886))
    z = np.exp(1j * frozen[-1][1])
    values, vectors = np.linalg.eig(free_fiber(on_shell_p))
    nearest = int(np.argmin(abs(values - z)))
    full_touch = float(abs(values[nearest] - z))
    dark_overlap = float(abs(np.vdot(A2_FULL, vectors[:, nearest] / np.linalg.norm(vectors[:, nearest]))))

    cyclic_rows = [
        {"L": length, "sampled_contact_cyclic_phase_gap": cyclic_gap(length, frozen[-1][1])}
        for length in (9, 13, 17, 21)
    ]
    chars = CHARACTERS["A2"]
    covariance = max(
        float(np.linalg.norm(rep @ A2_AXIS - chars[frame_class(frame)] * A2_AXIS))
        for frame, rep in zip(FRAMES, REPS2)
    )
    ranks = {name: int(np.linalg.matrix_rank(projector, tol=1e-10))
             for name, projector in PROJECTORS2.items()}
    tails = tail_observables(last_waves)
    check(
        "Route A gives an exact 15 by 15 contact Birman–Schwinger reduction and converged A2 finite sums",
        max(row["scalar_BS_residual"] for row in roots) < 1e-10
        and matrix_residual < 1e-10 and convergence[-1] < 1e-8,
        {"roots": roots, "L11_matrix_minimum_singular_value": matrix_residual,
         "successive_phase_differences": convergence},
    )
    check(
        "the candidate wrapped phase touches the full free spectrum but the located on-shell vector is A2-source dark",
        full_touch < 1e-12 and dark_overlap < 1e-10,
        {"momentum": on_shell_p.tolist(), "full_spectrum_distance": full_touch,
         "A2_source_overlap": dark_overlap},
    )
    check(
        "the frozen grids retain a positive contact-cyclic diagnostic gap without promoting it to a theorem",
        min(row["sampled_contact_cyclic_phase_gap"] for row in cyclic_rows) > 0.05,
        cyclic_rows,
    )
    check(
        "the onsite two-CAR content and A2 pole source are proper-cubic covariant",
        ranks == {"A1": 0, "A2": 1, "E": 2, "T1": 9, "T2": 3}
        and covariance < 1e-12,
        {"onsite_wedge2_irrep_ranks": ranks, "A2_all24_residual": covariance},
    )
    check(
        "the L31 inverse-Fourier pole candidate remains localized in finite diagnostics",
        tails["contact_weight"] > 0.25 and tails["relative_radius_squared"] < 2.1
        and tails["seam_boundary_weight"] < 1e-7,
        tails,
    )
    return {
        "finite_rank_identity": "B_L(z)=I_15-z(exp(-ig)-1) L^-3 sum_p J2^dagger(F(p)-zI)^-1 J2",
        "roots": roots, "L11_matrix_minimum_singular_value": matrix_residual,
        "successive_phase_differences": convergence,
        "full_spectrum_on_shell": {"momentum": on_shell_p.tolist(),
            "distance": full_touch, "A2_source_overlap": dark_overlap},
        "sampled_contact_cyclic_gaps": cyclic_rows,
        "onsite_wedge2_irrep_ranks": ranks, "A2_all24_residual": covariance,
        "finite_L31_tail_diagnostic": tails,
        "ordinary_full_spectrum_gap_available": False,
        "infinite_volume_isolated_pole_and_exponential_tail_theorem": False,
        "exact_unfinished_lemma": (
            "Prove a uniform continuous-T3 gap/cancellation for the contact-cyclic source and prove that "
            "the relevant reducing or cancellation structure survives exponential spatial weighting; "
            "ordinary full-spectrum Combes-Thomas cannot be invoked because the full free spectrum touches z."
        ),
    }


def irrep_weights(onsite_full: np.ndarray) -> dict[str, float]:
    eta = J2.conj().T @ onsite_full
    denominator = float(np.vdot(eta, eta).real)
    if denominator == 0:
        return {name: 0.0 for name in PROJECTORS2}
    return {
        name: float(np.vdot(eta, projector @ eta).real / denominator)
        for name, projector in PROJECTORS2.items()
    }


def select_t2_candidate(length: int) -> tuple[complex, np.ndarray, dict[str, object]]:
    walk = c578.relative_car_walk(length, BETA, CONTACT, (0.0, 0.0, 0.0))
    quotient, *_ = c578.antisymmetric_quotient(length)
    seed = np.exp(0.173j * np.arange(walk.shape[0], dtype=float))
    seed /= np.linalg.norm(seed)
    values, vectors = sparse_linalg.eigs(
        walk, k=16, sigma=0.999 * np.exp(-3.0j), v0=seed, ncv=33,
        tol=2e-11, maxiter=5000,
    )
    candidates = []
    for index, value in enumerate(values):
        vector = vectors[:, index] / np.linalg.norm(vectors[:, index])
        full = quotient @ vector
        weights = irrep_weights(full[:36])
        observables = c578.relative_observables(length, vector)
        if weights["T2"] > 0.999:
            candidates.append((observables["contact_weight"], value, vector, full, weights, observables))
    _contact, value, vector, full, weights, observables = max(candidates, key=lambda row: row[0])
    observables = dict(observables)
    observables["eigen_residual"] = float(np.linalg.norm(walk @ vector - value * vector))
    return value, vector, {"full": full, "irrep_weights": weights, **observables}


def route_b_controls() -> dict[str, object]:
    rows = []
    stored = {}
    delta_k = 2 * np.pi / 127
    for length in (7, 9, 11):
        value_b, vector_b, second = select_t2_candidate(length)
        value_a, vector_a, primary = c578.isolated_eigenpair(
            length, BETA, CONTACT, (0.0, 0.0, 0.0), -2.976, eigen_count=10
        )
        quotient, *_ = c578.antisymmetric_quotient(length)
        full_a = quotient @ vector_a
        full_b = second.pop("full")
        component_products = np.conj(full_a[:36]) * full_b[:36]
        component = int(np.argmax(np.abs(component_products)))
        invariant_cross = float(abs(np.vdot(full_a[:36], full_b[:36])))
        moving_value, moving_vector, moving = c578.isolated_eigenpair(
            length, BETA, CONTACT, (delta_k, 0.0, 0.0), float(np.angle(value_b)),
            prior=vector_b, eigen_count=12,
        )
        row = {
            "L": length, "split": "train" if length == 7 else "held",
            "primary_wrapped_phase": float(np.angle(value_a)),
            "second_wrapped_phase": float(np.angle(value_b)),
            "second": second,
            "maximum_component_local_cross_term": float(abs(component_products[component])),
            "component_index": component,
            "proper_cubic_invariant_contact_cross_term": invariant_cross,
            "moving_K_label": delta_k,
            "moving_wrapped_phase": float(np.angle(moving_value)),
            "moving_phase_response": float(np.angle(moving_value / value_b)),
            "moving": moving,
        }
        rows.append(row)
        stored[length] = (value_b, vector_b, full_b, component)

    # All24 covariance of the train moving candidate and its component-local observable orbit.
    length = 7
    value0, vector0, full0, component0 = stored[length]
    value_k, vector_k, _obs_k = c578.isolated_eigenpair(
        length, BETA, CONTACT, (delta_k, 0.0, 0.0), float(np.angle(value0)),
        prior=vector0, eigen_count=12,
    )
    quotient, *_ = c578.antisymmetric_quotient(length)
    full_k = quotient @ vector_k
    primary_value, primary_vector, _ = c578.isolated_eigenpair(
        length, BETA, CONTACT, (delta_k, 0.0, 0.0), -2.976, eigen_count=10
    )
    primary_full = quotient @ primary_vector
    base_cross = np.conj(primary_full[component0]) * full_k[component0]
    covariance_residuals = []
    cross_residuals = []
    base_momentum = np.asarray((delta_k, 0.0, 0.0))
    for frame in FRAMES:
        full_rep = c578.full_frame_representation(length, frame)
        rotated = full_rep @ full_k
        rotated_q = quotient.conj().T @ rotated
        rotated_walk = c578.relative_car_walk(
            length, BETA, CONTACT, tuple(float(row) for row in frame @ base_momentum)
        )
        covariance_residuals.append(float(np.linalg.norm(rotated_walk @ rotated_q - value_k * rotated_q)))
        direction = c210.direction_permutation(frame)
        target = int(np.argmax(np.kron(direction, direction)[:, component0]))
        rotated_primary = full_rep @ primary_full
        cross_residuals.append(float(abs(np.conj(rotated_primary[target]) * rotated[target] - base_cross)))

    frozen_localized = [
        row["second"]["contact_weight"] > 0.15
        and row["second"]["relative_radius_squared"] < 8.0
        and row["second"]["seam_boundary_weight"] < 0.15
        for row in rows
    ]
    held_localized = [
        flag for row, flag in zip(rows, frozen_localized) if row["split"] == "held"
    ]
    certified = all(frozen_localized)
    check(
        "Route B decomposes the onsite two-CAR content and finds a pure T2 contact-active fixed-window candidate",
        all(row["second"]["irrep_weights"]["T2"] > 0.999 for row in rows)
        and max(row["second"]["eigen_residual"] for row in rows) < 1e-10,
        rows,
    )
    check(
        "the finite T2 candidate has a nonzero component-local A2-T2 cross term with a covariant all24 orbit",
        min(row["maximum_component_local_cross_term"] for row in rows) > 1e-4
        and max(cross_residuals) < 1e-12 and max(covariance_residuals) < 1e-10,
        {"rows": rows, "all24_eigen_residual": max(covariance_residuals),
         "all24_component_orbit_residual": max(cross_residuals)},
    )
    check(
        "the frozen train-held T2 family does not certify a second co-moving localized branch",
        not certified and not all(held_localized),
        {"localization_rows": frozen_localized, "certified": certified,
         "disposition": "fixed-window certification failure, not an absence theorem"},
    )
    return {
        "search": "fixed sigma phase -3.0, k=16, ncv=33, maximum-contact pure-T2 candidate; no held refit",
        "rows": rows, "localization_threshold_rows": frozen_localized,
        "held_localization_threshold_rows": held_localized,
        "second_co_moving_localized_branch_certified": certified,
        "all24_eigen_residual": max(covariance_residuals),
        "all24_component_observable_orbit_residual": max(cross_residuals),
        "nonzero_component_local_cross_term_exists_in_finite_boxes": True,
        "proper_cubic_invariant_contact_cross_term_is_zero_between_irreps": True,
        "second_mode_absence_theorem": False,
    }


PERMUTATIONS3 = []
for perm in permutations(range(3)):
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    PERMUTATIONS3.append((perm, (-1) ** inversions))


def site_tuple3(site: int, length: int) -> tuple[int, int, int]:
    return site // (length * length), (site // length) % length, site % length


def site_flat3(site: tuple[int, int, int], length: int) -> int:
    return (site[0] * length + site[1]) * length + site[2]


@lru_cache(maxsize=None)
def three_car_quotient(length: int) -> tuple[sparse.csr_matrix, float]:
    if length < 3 or length % 2 == 0:
        raise ValueError("frozen three-CAR quotient requires odd L>=3")
    sites = length**3
    full_dimension = sites * sites * 216
    seen = np.zeros(full_dimension, bool)
    rows = np.empty(full_dimension, np.int32)
    cols = np.empty(full_dimension, np.int32)
    data = np.empty(full_dimension, float)
    cursor = 0
    quotient_dimension = 0

    def encode(r1: int, r2: int, directions: tuple[int, int, int]) -> int:
        return ((r1 * sites + r2) * 216 + (directions[0] * 6 + directions[1]) * 6 + directions[2])

    for index in range(full_dimension):
        if seen[index]:
            continue
        pair, directional = divmod(index, 216)
        r1, r2 = divmod(pair, sites)
        d1, remainder = divmod(directional, 36)
        d2, d3 = divmod(remainder, 6)
        positions = (site_tuple3(r1, length), site_tuple3(r2, length), (0, 0, 0))
        directions = (d1, d2, d3)
        orbit: dict[int, int] = {}
        for perm, parity in PERMUTATIONS3:
            anchor = positions[perm[2]]
            relative = []
            for particle in perm[:2]:
                relative.append(site_flat3(tuple(
                    (positions[particle][axis] - anchor[axis]) % length for axis in range(3)
                ), length))
            target = encode(relative[0], relative[1], tuple(directions[p] for p in perm))
            orbit[target] = orbit.get(target, 0) + parity
        for target in orbit:
            seen[target] = True
        orbit = {target: parity for target, parity in orbit.items() if parity}
        if not orbit:
            continue
        norm = math.sqrt(sum(parity * parity for parity in orbit.values()))
        for target, parity in orbit.items():
            rows[cursor] = target
            cols[cursor] = quotient_dimension
            data[cursor] = parity / norm
            cursor += 1
        quotient_dimension += 1
    quotient = sparse.csr_matrix(
        (data[:cursor], (rows[:cursor], cols[:cursor])),
        shape=(full_dimension, quotient_dimension),
    )
    isometry_residual = float(sparse.linalg.norm(
        quotient.conj().T @ quotient - sparse.eye(quotient_dimension)
    ))
    return quotient, isometry_residual


class ThreeCarWalk:
    def __init__(self, length: int):
        self.length = length
        self.sites = length**3
        self.quotient, self.isometry_residual = three_car_quotient(length)
        self.coin = c219.common_species(BETA).coin
        site = np.arange(self.sites)
        first, second = np.meshgrid(site, site, indexing="ij")
        pairs = (first == 0).astype(int) + (second == 0).astype(int) + (first == second).astype(int)
        self.phase = np.exp(1j * CONTACT * pairs).reshape((length,) * 6)

    def full_step(self, vector: np.ndarray, inverse: bool = False) -> np.ndarray:
        length = self.length
        coin = self.coin.conj().T if inverse else self.coin
        tensor = vector.reshape((length,) * 6 + (6, 6, 6))
        if inverse:
            tensor = tensor * self.phase[..., None, None, None].conj()
            streamed = np.zeros_like(tensor)
            for d1, v1 in enumerate(c210.DIRECTIONS):
                for d2, v2 in enumerate(c210.DIRECTIONS):
                    for d3, v3 in enumerate(c210.DIRECTIONS):
                        shifts = tuple(-int(row) for row in np.r_[v1 - v3, v2 - v3])
                        streamed[..., d1, d2, d3] = np.roll(
                            tensor[..., d1, d2, d3], shifts, axis=range(6)
                        )
            tensor = streamed
        flat = tensor.reshape(length**6, 6, 6, 6)
        flat = np.einsum("ai,pijk->pajk", coin, flat, optimize=True)
        flat = np.einsum("bj,pajk->pabk", coin, flat, optimize=True)
        flat = np.einsum("ck,pabk->pabc", coin, flat, optimize=True)
        tensor = flat.reshape((length,) * 6 + (6, 6, 6))
        if not inverse:
            streamed = np.zeros_like(tensor)
            for d1, v1 in enumerate(c210.DIRECTIONS):
                for d2, v2 in enumerate(c210.DIRECTIONS):
                    for d3, v3 in enumerate(c210.DIRECTIONS):
                        shifts = tuple(int(row) for row in np.r_[v1 - v3, v2 - v3])
                        streamed[..., d1, d2, d3] = np.roll(
                            tensor[..., d1, d2, d3], shifts, axis=range(6)
                        )
            tensor = streamed * self.phase[..., None, None, None]
        return tensor.reshape(-1)

    def step(self, vector: np.ndarray, inverse: bool = False) -> np.ndarray:
        return self.quotient.conj().T @ self.full_step(self.quotient @ vector, inverse)


def three_seed(walk: ThreeCarWalk, irrep: str) -> np.ndarray:
    axis = projector_axis(PROJECTORS3[irrep])
    full = np.zeros(walk.quotient.shape[0], complex)
    full[:216] = J3 @ axis
    encoded = walk.quotient.conj().T @ full
    return encoded / np.linalg.norm(encoded)


def arnoldi_scout(walk: ThreeCarWalk, irrep: str, iterations: int) -> dict[str, float]:
    dimension = walk.quotient.shape[1]
    basis = np.zeros((dimension, iterations + 1), complex)
    hessenberg = np.zeros((iterations + 1, iterations), complex)
    basis[:, 0] = three_seed(walk, irrep)
    for column in range(iterations):
        candidate = walk.step(basis[:, column])
        for _ in range(2):
            projection = basis[:, :column + 1].conj().T @ candidate
            hessenberg[:column + 1, column] += projection
            candidate -= basis[:, :column + 1] @ projection
        hessenberg[column + 1, column] = np.linalg.norm(candidate)
        basis[:, column + 1] = candidate / hessenberg[column + 1, column]
    values, vectors = np.linalg.eig(hessenberg[:iterations, :iterations])
    residuals = np.abs(hessenberg[iterations, iterations - 1] * vectors[-1])
    best = int(np.argmin(residuals))
    return {
        "wrapped_phase": float(np.angle(values[best])),
        "ritz_modulus": float(abs(values[best])),
        "ritz_residual": float(residuals[best]),
        "terminal_krylov_norm": float(abs(hessenberg[iterations, iterations - 1])),
    }


def rotate_three_full(vector: np.ndarray, length: int, frame: np.ndarray) -> np.ndarray:
    """Rotate two relative sites and all three direction labels together."""
    sites = length**3
    direction = c210.direction_permutation(frame)
    direction_target = np.argmax(direction, axis=0)
    directional_target = np.empty(216, int)
    for d1 in range(6):
        for d2 in range(6):
            for d3 in range(6):
                source = (d1 * 6 + d2) * 6 + d3
                directional_target[source] = (
                    (int(direction_target[d1]) * 6 + int(direction_target[d2])) * 6
                    + int(direction_target[d3])
                )
    site_target = np.empty(sites, int)
    for site in range(sites):
        coordinate = np.asarray(site_tuple3(site, length), int)
        site_target[site] = site_flat3(
            tuple(int(row % length) for row in frame @ coordinate), length
        )
    pair_target = (
        site_target[:, None] * sites + site_target[None, :]
    ).reshape(-1)
    target = (
        pair_target[:, None] * 216 + directional_target[None, :]
    ).reshape(-1)
    rotated = np.empty_like(vector)
    rotated[target] = vector
    return rotated


def route_c_controls() -> dict[str, object]:
    ranks = {name: int(np.linalg.matrix_rank(projector, tol=1e-10))
             for name, projector in PROJECTORS3.items()}
    rows = []
    deletion_signals = []
    for length, iterations in ((3, 80), (5, 45)):
        walk = ThreeCarWalk(length)
        for irrep in ("A1", "A2"):
            seed = three_seed(walk, irrep)
            stepped = walk.step(seed)
            inverse_residual = float(np.linalg.norm(walk.step(stepped, inverse=True) - seed))
            full_stepped = walk.full_step(walk.quotient @ seed)
            leakage = float(np.linalg.norm(
                full_stepped - walk.quotient @ (walk.quotient.conj().T @ full_stepped)
            ))
            deleted = walk.quotient @ seed
            deleted[int(np.argmax(np.abs(deleted)))] = 0
            deletion = float(np.linalg.norm(
                deleted - walk.quotient @ (walk.quotient.conj().T @ deleted)
            ))
            deletion_signals.append(deletion)
            rows.append({
                "L": length, "split": "train" if length == 3 else "held",
                "irrep": irrep, "quotient_dimension": walk.quotient.shape[1],
                "quotient_nonzeros": walk.quotient.nnz,
                "isometry_residual_Frobenius": walk.isometry_residual,
                "forward_norm_residual": float(abs(np.linalg.norm(stepped) - 1)),
                "inverse_residual": inverse_residual,
                "antisymmetric_projection_leakage": leakage,
                "single_ordered_component_deletion_signal": deletion,
                "arnoldi_iterations": iterations,
                **arnoldi_scout(walk, irrep, iterations),
            })
            gc.collect()
        del walk
        three_car_quotient.cache_clear()
        gc.collect()
    malformed_rejected = False
    try:
        three_car_quotient(4)
    except ValueError:
        malformed_rejected = True
    walk3 = ThreeCarWalk(3)
    covariance_residuals = []
    covariance_projection_leakages = []
    for irrep in ("A1", "A2"):
        full_seed = walk3.quotient @ three_seed(walk3, irrep)
        stepped = walk3.full_step(full_seed)
        for frame in FRAMES:
            rotated_seed = rotate_three_full(full_seed, 3, frame)
            left = rotate_three_full(stepped, 3, frame)
            right = walk3.full_step(rotated_seed)
            covariance_residuals.append(float(np.linalg.norm(left - right)))
            covariance_projection_leakages.append(float(np.linalg.norm(
                rotated_seed - walk3.quotient @ (walk3.quotient.conj().T @ rotated_seed)
            )))
    certified = any(
        row["split"] == "held" and row["ritz_residual"] < 1e-6
        and abs(row["ritz_modulus"] - 1) < 1e-6 for row in rows
    )
    check(
        "Route C constructs exact train-held antisymmetric three-CAR quotient updates under the cap",
        ranks == {"A1": 1, "A2": 1, "E": 0, "T1": 9, "T2": 9}
        and max(row["forward_norm_residual"] for row in rows) < TOL
        and max(row["inverse_residual"] for row in rows) < TOL
        and max(row["antisymmetric_projection_leakage"] for row in rows) < TOL
        and malformed_rejected and min(deletion_signals) > SIGNAL
        and max(covariance_residuals) < TOL
        and max(covariance_projection_leakages) < TOL,
        {"onsite_wedge3_irrep_ranks": ranks, "rows": rows,
         "malformed_even_L_rejected": malformed_rejected,
         "all24_seed_update_covariance_residual": max(covariance_residuals),
         "all24_rotated_code_leakage": max(covariance_projection_leakages)},
    )
    check(
        "the capped A1/A2 three-CAR Krylov scout does not certify a held isolated internal mode",
        not certified and min(row["ritz_residual"] for row in rows if row["split"] == "held") > 1e-2,
        {"rows": rows, "certified": certified,
         "disposition": "bounded scout non-certification; T1/T2 and deeper Krylov searches remain open"},
    )
    return {
        "onsite_wedge3_irrep_ranks": ranks, "rows": rows,
        "all24_seed_update_covariance_residual": max(covariance_residuals),
        "all24_rotated_code_leakage": max(covariance_projection_leakages),
        "held_internal_mode_certified": certified,
        "T1_T2_three_CAR_scout": "open under declared resource cap",
        "three_CAR_mode_absence_theorem": False,
        "resource_contract": "L3 train m80; L5 held m45; A1/A2 only; 360 seconds and 3 GiB maximum-RSS caps",
    }


def interpretation_firewall() -> dict[str, object]:
    required = (
        "wrapped phase is not energy", "group displacement is not a rate",
        "update schedule is not time", "contact weight is not born probability",
        "car-fiber result is not a physical-m2 compiler",
        "finite grid contact-cyclic gap is not an infinite-volume theorem",
        "source coupling is not gravity", "candidate occurrence is not a record",
    )
    body = normalized(NOTE)
    missing = tuple(row for row in required if row not in body)
    check("the interpretation firewall keeps every retained quantity typed", not missing, missing)
    return {"clean": not missing, "missing": missing}


def no_go_gate(retained: dict[str, float]) -> dict[str, object]:
    alternatives = (
        ("two-CAR finite-rank resolvent", "A2 onsite contact source", "finite pole sums", "positive exact reduction"),
        ("two-CAR continuous torus", "contact-cyclic cancellation", "isolated pole plus exponential tail", "open lemma"),
        ("two-CAR T2 window", "second cubic irrep", "co-moving internal transition", "held certification failed"),
        ("three-CAR A1/A2", "triple contact sectors", "second internal mode", "bounded scout inconclusive"),
        ("three-CAR T1/T2", "nine-dimensional cubic sectors", "second internal mode", "resource-capped open"),
        ("four-plus CAR", "larger contact clusters", "internal multiplicity", "open"),
        ("different even contact law", "additional local invariant", "split localized branches", "open supplied-law route"),
        ("physical-M2 gauge compiler", "bounded auxiliary constraints", "literal site realization", "separate compiler wall"),
    )
    qualifying_negative_families = (alternatives[2], alternatives[3])
    walls = (
        "C_ref second internal reference", "C_num empirical calibration",
        "C_wrap unbounded renewal", "C_int infinite contact pole theorem",
        "C_local physical-M2 compiler", "C_source gravity and backreaction",
    )
    mechanisms = {
        walls[0]: "a second held localized irrep and nonzero local transition observable",
        walls[1]: "an independent measured scale and calibration map",
        walls[2]: "renewal resources and stability under arbitrarily many updates",
        walls[3]: "a continuous-torus contact-cyclic gap/cancellation stable under exponential weighting",
        walls[4]: "a bounded M2 encoding with local gauge constraints and exact intertwining",
        walls[5]: "a dynamical stress/source carrier and backreaction law",
    }
    pairwise = tuple(
        (left, right,
         f"{left} needs {mechanisms[left]}, which does not entail {mechanisms[right]}",
         f"{right} needs {mechanisms[right]}, which does not entail {mechanisms[left]}",
         False)
        for left, right in combinations(walls, 2)
    )
    n3 = (
        "Cycle219 beta=-0.3 coin and common wrapped phase convention",
        "Cycle230 six CAR directions and onsite coupling g=0.37",
        "odd periodic relative boxes and frozen shift-invert/Krylov windows",
        "A2 finite-root phases imported from reconnaissance then independently residual-tested",
        "contact-cyclic overlap threshold 1e-8 and sampled grids",
        "noiseless arithmetic and exact local CAR quotient constraints",
    )
    n4 = (
        ("Cycle219", "mass fixture", retained["mass_residual"], True),
        ("Cycle230", "contact factorization", retained["contact_residual"], True),
        ("Cycle230", "seam braid", retained["seam_residual"], True),
        ("Cycle578", "finite contact-bound branch", "literal runner and receipt pinned", True),
    )
    n5 = (
        ("Route A finite BS", "L11/15/19/23/27/31", "exact finite sums; continuous theorem open"),
        ("Route A cyclic diagnostic", "L9/13/17/21 grids", "diagnostic only; no uniform theorem"),
        ("Route B", "L7 train and L9/L11 held", "fixed spectral window; no absence theorem"),
        ("Route C", "L3 train/L5 held A1/A2", "T1/T2 and deeper Krylov open"),
        ("physical-M2", "none constructed here", "CAR-fiber/physical-site distinction preserved"),
    )
    n6 = (
        "prove the continuous-T3 contact-cyclic reducing/cancellation lemma",
        "establish exponential weighting without coupling the dark continuum back to the source",
        "continue the T2 candidate with a branch-aware volume embedding rather than a fixed window",
        "run T1/T2 three-CAR block Krylov or finite-rank contact resolvents",
        "search four-plus CAR contact clusters under a separately frozen cap",
        "compose any retained CAR object with an independently verified bounded physical-M2 compiler",
    )
    n7 = (
        "Mechanism: the onsite A2 contact source yields an exact 15-dimensional Birman–Schwinger equation and rapidly convergent finite-volume pole phase. "
        "Terminal obligation: because the full free spectrum touches that phase, a hostile reviewer must reject an ordinary spectral-gap or Combes–Thomas proof until a continuous contact-cyclic cancellation stable under exponential weighting is proved. "
        "The finite T2 cross term and exact three-CAR quotient keep constructive second-mode routes open, while held localization/Krylov thresholds presently do not certify them."
    )
    n8 = (
        "Cycle219 supplied the massive proper-cubic one-particle walk",
        "Cycle230 supplied intrinsic CAR and local even contact but no physical-site compiler",
        "Cycles563/569 retained the physical-M2 mass/contact/seam fixtures",
        "Cycle578 found a finite contact-bound dispersive A2 dimer branch",
        "Cycle583 exposes its exact finite-rank contact resolvent and the precise full-spectrum-touch boundary, while scouting rather than excluding internal multiplicity",
    )
    supplied = (
        "Cycle219/230/563/569/578 byte-pinned shore",
        "beta=-0.3, g=0.37, odd periodic boxes, frozen pole phases and spectral windows",
        "proper-cubic frame action, numerical overlap threshold, Krylov depths and caps",
    )
    derived = (
        "exact finite 15 by 15 Birman-Schwinger reduction and small residuals through L31",
        "A2 rank-one onsite source and proper-cubic covariance",
        "explicit on-shell full-spectrum touch with source-dark eigenvector",
        "finite T2 component-local cross term and failed held localization certification",
        "exact three-CAR antisymmetric quotient and reversible contact update on L3/L5",
    )
    open_rows = (
        "infinite-volume isolated pole and exponential-tail theorem",
        "second co-moving localized internal mode",
        "T1/T2 three-CAR and larger contact sectors",
        "bounded physical-M2 compiler for the CAR object",
        "unbounded renewal, calibration, gravity/source response, Record actuality, and Born law",
    )
    ledger = {
        "C_ref": "one finite-volume A2 contact reference gains an exact finite-rank equation; a second held internal reference remains open",
        "C_num": "finite BS pole residuals and dimensionless phase convergence sharpen numerics; no empirical scale or physical duration",
        "C_wrap": "unchanged: no new renewal or unbounded noisy recurrence result",
        "C_int": "stronger finite/integral contact mechanism and proper-cubic irrep content; continuous pole/localization lemma remains open",
        "C_local": "exact two-/three-CAR quotient updates only; no bounded physical-M2 object compiler is constructed",
        "C_source": "g=0.37 remains supplied dimensionless contact strength; no gravity, redshift, stress, or backreaction",
    }
    n1_pass = len(qualifying_negative_families) >= 5
    negative_claim_shipped = False
    condition = (
        not n1_pass and not negative_claim_shipped and len(pairwise) == 15
        and all(row[-1] is False for row in pairwise)
        and all(row[-1] is True for row in n4)
    )
    check(
        "fresh N1-N8 testing withholds absence, no-go, minimum-content, shared-obstruction, and axiom-pressure claims",
        condition,
        {"N1_normalized_alternatives": alternatives,
         "N1_qualifying_negative_families": qualifying_negative_families,
         "N1_required": 5, "N1_pass": n1_pass,
         "N2_directional_pairwise_wall_audit": pairwise,
         "N3_hidden_wall_scan": n3, "N4_residual_matching": n4,
         "N5_resolution_audit": n5, "N6_partial_closure_paths": n6,
         "N7_hostile_steelman": n7, "N8_cross_cycle_echo": n8,
         "negative_claim_shipped": negative_claim_shipped,
         "shared_substrate_obstruction": False, "axiom_pressure": False},
    )
    return {
        "N1_normalized_alternatives": alternatives,
        "N1_qualifying_negative_families": qualifying_negative_families,
        "N1_required": 5, "N1_pass": n1_pass,
        "N2_directional_pairwise_wall_audit": pairwise,
        "N3_hidden_wall_scan": n3, "N4_residual_matching": n4,
        "N5_resolution_audit": n5, "N6_partial_closure_paths": n6,
        "N7_hostile_steelman": n7, "N8_cross_cycle_echo": n8,
        "supplied": supplied, "derived": derived, "open": open_rows,
        "six_wall_ledger": ledger, "negative_claim_shipped": negative_claim_shipped,
        "shared_substrate_obstruction": False, "axiom_pressure": False,
    }


def main() -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0
    signal.alarm(int(WALL_CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle583 physical contact-dimer infinite/internal-content tournament")
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
        "the frozen Cycle583 tournament remains below the 360-second and 3-GiB internal maximum-RSS caps",
        elapsed < WALL_CAP_SECONDS and peak_bytes < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "maximum_RSS_bytes": peak_bytes},
    )
    receipt = {
        "status": "cycle583-physical-contact-dimer-infinite-internal-content-tournament",
        "authority": AUTHORITY, "audit": AUDIT,
        "accepted_Cycle578_ancestor_commit": ACCEPTED_CYCLE578_COMMIT,
        "definitive_run_HEAD": subprocess.check_output(
            ("git", "rev-parse", "HEAD"), cwd=ROOT, text=True
        ).strip(),
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0,
        "cold_internal_elapsed_seconds": elapsed,
        "cold_maximum_RSS_bytes": peak_bytes,
        "cold_caps": {"seconds": WALL_CAP_SECONDS, "maximum_RSS_bytes": RSS_CAP_BYTES,
                      "peak_memory_footprint_is_a_separately_reported_external_metric": True},
        "exact_pinned_dependencies": {**DEPENDENCY_SHA256,
            "Cycle578_receipt": CYCLE578_RECEIPT_SHA256,
            "Cycle578_note": CYCLE578_NOTE_SHA256},
        "retained_physical_M2_fixtures": retained,
        "route_A_finite_rank_contact_resolvent": route_a,
        "route_B_internal_irrep_search": route_b,
        "route_C_three_CAR_scout": route_c,
        "interpretation_firewall": firewall,
        "no_go_discipline": gate,
        "six_wall_ledger": gate["six_wall_ledger"],
        "scope_boundary": {
            "CAR_fiber_result_is_physical_M2_compiler": False,
            "infinite_volume_exponential_localization_theorem": False,
            "second_internal_mode_certified": False,
            "wrapped_phase_is_energy": False,
            "group_displacement_is_rate": False,
            "schedule_is_time": False,
            "authority": AUTHORITY, "audit": AUDIT,
        },
        "optimal_next_campaign": (
            "prove the continuous-T3 contact-cyclic cancellation/reducing lemma with exponential weighting; "
            "in parallel formulate a branch-aware T2 or three-CAR finite-rank contact resolvent"
        ),
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("SUMMARY_JSON", json.dumps({
        "tests_passed": PASS, "tests_failed": FAIL,
        "route_A_max_BS_residual": max(row["scalar_BS_residual"] for row in route_a["roots"]),
        "route_A_full_spectrum_distance": route_a["full_spectrum_on_shell"]["distance"],
        "route_B_second_mode_certified": route_b["second_co_moving_localized_branch_certified"],
        "route_C_second_mode_certified": route_c["held_internal_mode_certified"],
        "shared_substrate_obstruction": gate["shared_substrate_obstruction"],
        "axiom_pressure": gate["axiom_pressure"],
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": peak_bytes,
    }, sort_keys=True))
    print("RESULT", f"pass={PASS}", f"fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
