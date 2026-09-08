#!/usr/bin/env python3
"""Block 83: component-staggered signed-link action and local-Ward boundary.

One oriented nearest-neighbour phase-space link action produces the exact
Block-78 lapse, shift, and spatial-stress source cadence from its geometry
derivatives.  The same scalar supplies genuine matter--geometry mixed
Hessians and the flat null-link equations.  The construction is signed and
component-staggered: it is not yet positive matter or a certified pointwise
inverse metric.  A localized total Ward identity still requires a bounded-
local equivariant pullback/deposition map and a site-mixing generator.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
PARENT_NOTE = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_LOCAL_SHADOW_ENERGY_FLUX_LAPSE_TRANSLATION_JOINT_ACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
BLOCK78_NOTE = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
NOETHER_NOTE = ROOT / "docs" / (
    "AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_"
    "2026-06-05.md"
)

RUNNER_RELATIVE = (
    "scripts/admissibility_component_staggered_signed_link_action_local_"
    "ward_boundary_2026_08_14.py"
)
PARENT_RUNNER = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/scripts/admissibility_local_shadow_energy_flux_lapse_translation_joint_action_boundary_2026_08_14.py'
)
BLOCK78_RUNNER = (
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_"
    "record_cadence_boundary_2026_08_14.py"
)
AUDIT_INPUT_PATHS = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_LOCAL_SHADOW_ENERGY_FLUX_LAPSE_TRANSLATION_JOINT_ACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_SECOND_ORDER_WARD_PSEUDOCONSTRAINT_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    'scripts/admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14.py',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/scripts/admissibility_local_shadow_energy_flux_lapse_translation_joint_action_boundary_2026_08_14.py',
    'scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py',
)

CURRENT_AXIOM_COMMIT = "44b6a6a1423f59cb4a24160d24117bd2283d2d9e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
PARENT_COMMIT = "6d4ceb046de25664ae65836a1127348fc4a9c81c"
PARENT_NOTE_BLOB = "6970cdf9344f26555100aacc662fe2ee18ce3a2e"
PARENT_RUNNER_BLOB = "e9c79c6e8437ff00784bd144750515b65082d25a"

DELTA = 0.5
COUPLING = 1.0
TOL = 1.0e-10
ETA = np.diag((-1.0, 1.0, 1.0, 1.0))


def symmetric_basis() -> tuple[np.ndarray, ...]:
    basis: list[np.ndarray] = []
    for axis in range(3):
        value = np.zeros((3, 3))
        value[axis, axis] = 1.0
        basis.append(value)
    for left, right in ((0, 1), (0, 2), (1, 2)):
        value = np.zeros((3, 3))
        value[left, right] = value[right, left] = 1.0 / np.sqrt(2.0)
        basis.append(value)
    return tuple(basis)


BASIS = symmetric_basis()


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return int(self.failed != 0)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def git_commit_path_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def git_worktree_path_blob(path: str) -> str:
    return subprocess.run(
        ("git", "hash-object", "--", path),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def authority_certificate(mutation: str) -> dict[str, object]:
    origin_main = subprocess.run(
        ("git", "rev-parse", "origin/main"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    frozen = tuple(
        path
        for path in AUDIT_INPUT_PATHS
        if path not in (NOTE_PATH.relative_to(ROOT).as_posix(), RUNNER_RELATIVE)
    )
    mismatches = tuple(
        path
        for path in frozen
        if git_worktree_path_blob(path) != git_commit_path_blob(PARENT_COMMIT, path)
    )
    loaded: set[str] = set()
    for module in tuple(sys.modules.values()):
        file_name = getattr(module, "__file__", None)
        if not file_name:
            continue
        path = Path(file_name).resolve()
        try:
            relative = path.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if relative.startswith("scripts/") and relative.endswith(".py"):
            loaded.add(relative)
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    return {
        "origin_main": origin_main,
        "axiom_blob": git_worktree_path_blob("docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "expected_axiom": expected_axiom,
        "parent_note": git_worktree_path_blob(PARENT_NOTE.relative_to(ROOT).as_posix()),
        "parent_runner": git_worktree_path_blob(PARENT_RUNNER),
        "mismatches": mismatches,
        "missing_inputs": tuple(path for path in AUDIT_INPUT_PATHS if not (ROOT / path).exists()),
        "loaded": loaded,
    }


def tensor_coordinates(tensor: np.ndarray) -> np.ndarray:
    return np.asarray([np.sum(item * tensor) for item in BASIS], dtype=complex)


def coordinate_tensor(coordinates: np.ndarray) -> np.ndarray:
    return sum(
        (coordinates[index] * item for index, item in enumerate(BASIS)),
        start=np.zeros((3, 3), dtype=np.asarray(coordinates).dtype),
    )


def source_mode_data(
    size: int,
    axis: int,
    sign: int,
    neutral_step: int,
    along: int,
    transverse: int,
    remaining: int,
) -> tuple[np.ndarray, complex, complex, np.ndarray, np.ndarray, np.ndarray, int]:
    neutral_axis = (axis + neutral_step) % 3
    remaining_axis = (axis + (3 - neutral_step)) % 3
    integers = np.zeros(3, dtype=int)
    integers[axis] = along
    integers[neutral_axis] = transverse
    integers[remaining_axis] = remaining
    momentum = 2.0 * np.pi * integers / size
    density = 1.0 - np.exp(-1.0j * momentum[neutral_axis])
    density_next = np.exp(-1.0j * sign * momentum[axis]) * density
    incoming = np.zeros(3, dtype=complex)
    outgoing = np.zeros(3, dtype=complex)
    incoming[axis] = sign * np.exp(0.5j * sign * momentum[axis]) * density
    outgoing[axis] = sign * np.exp(-0.5j * sign * momentum[axis]) * density
    stress = np.zeros((3, 3), dtype=complex)
    stress[axis, axis] = density
    return momentum, density, density_next, incoming, outgoing, stress, neutral_axis


def signed_pair_fourier(
    momentum: np.ndarray,
    axis: int,
    sign: int,
    neutral_axis: int,
    mutation: str,
) -> tuple[complex, complex, np.ndarray, np.ndarray, complex]:
    direction = np.zeros(3)
    direction[axis] = sign
    second = np.zeros(3)
    second[neutral_axis] = -1.0 if mutation == "wrong_pair_phase" else 1.0
    legs = ((1.0, np.zeros(3)), (-1.0, second))
    if mutation == "positive_only":
        legs = legs[:1]
    rho0 = 0.0j
    rho1 = 0.0j
    current = np.zeros(3, dtype=complex)
    stress = np.zeros((3, 3), dtype=complex)
    zero_mode = 0.0j
    for weight, tail in legs:
        tail_phase = np.exp(-1.0j * momentum @ tail)
        head_phase = np.exp(-1.0j * momentum @ (tail + direction))
        midpoint_phase = np.exp(-1.0j * momentum @ (tail + direction / 2.0))
        rho0 += weight * tail_phase
        rho1 += 0.5 * weight * (tail_phase + head_phase)
        current += weight * direction * midpoint_phase
        stress += weight * np.outer(direction, direction) * tail_phase
        zero_mode += weight
    return rho0, rho1, current, stress, zero_mode


def signed_source_certificate(mutation: str) -> dict[str, object]:
    modes = 0
    error = 0.0
    zero_mode_error = 0.0
    null_error = 0.0
    velocity_error = 0.0
    response_error = 0.0
    negative_legs = 0
    for size in range(3, 9):
        for axis in range(3):
            for sign in (-1, 1):
                for neutral_step in (1, 2):
                    for along in range(size):
                        for transverse in range(1, size):
                            for remaining in range(size):
                                data = source_mode_data(
                                    size,
                                    axis,
                                    sign,
                                    neutral_step,
                                    along,
                                    transverse,
                                    remaining,
                                )
                                k, rho, rho_next, _jin, jout, tau, neutral_axis = data
                                observed = signed_pair_fourier(
                                    k, axis, sign, neutral_axis, mutation
                                )
                                midpoint = 0.5 * (rho + rho_next)
                                error = max(
                                    error,
                                    abs(observed[0] - rho),
                                    abs(observed[1] - midpoint),
                                    float(np.max(np.abs(observed[2] - jout))),
                                    float(np.max(np.abs(observed[3] - tau))),
                                )
                                zero_mode_error = max(zero_mode_error, abs(observed[4]))
                                direction = np.zeros(3)
                                direction[axis] = sign
                                for weight in (1.0, -1.0):
                                    if mutation == "positive_only" and weight < 0.0:
                                        continue
                                    covector = np.concatenate(((-weight,), weight * direction))
                                    einbein = 1.0 / weight
                                    displacement = np.concatenate(((1.0,), direction))
                                    null_error = max(
                                        null_error, abs(float(covector @ ETA @ covector))
                                    )
                                    velocity_error = max(
                                        velocity_error,
                                        float(np.max(np.abs(displacement - einbein * ETA @ covector))),
                                    )
                                    rho_leg = einbein * covector[0] ** 2
                                    current_leg = -einbein * covector[0] * covector[1:]
                                    stress_leg = einbein * np.outer(covector[1:], covector[1:])
                                    response_error = max(
                                        response_error,
                                        abs(rho_leg - weight),
                                        float(np.max(np.abs(current_leg - weight * direction))),
                                        float(np.max(np.abs(stress_leg - weight * np.outer(direction, direction)))),
                                    )
                                    negative_legs += int(weight < 0.0)
                                modes += 1
    return {
        "modes": modes,
        "error": error,
        "zero_mode_error": zero_mode_error,
        "null_error": null_error,
        "velocity_error": velocity_error,
        "response_error": response_error,
        "negative_legs": negative_legs,
    }


def unpack_geometry(values: np.ndarray) -> tuple[float, float, float, np.ndarray, np.ndarray, np.ndarray]:
    q = np.asarray(values, dtype=float)
    return q[0], q[1], q[2], q[3:6], q[6:9], coordinate_tensor(q[9:15]).real


def integrated_gamma(values: np.ndarray, mutation: str = "") -> np.ndarray:
    n0, n1_tail, n1_head, beta0, beta1, h0 = unpack_geometry(values)
    gamma = ETA.copy()
    lapse_factor = 1.0 if mutation != "wrong_lapse_weight" else 0.5
    shift_factor = 2.0 if mutation != "wrong_shift_weight" else 1.0
    stress_factor = 4.0 if mutation != "wrong_stress_weight" else 2.0
    gamma[0, 0] += 2.0 * DELTA * COUPLING * lapse_factor * (
        n0 + 0.5 * (n1_tail + n1_head)
    )
    gamma[0, 1:] += shift_factor * DELTA * COUPLING * (beta0 + beta1)
    gamma[1:, 0] = gamma[0, 1:]
    gamma[1:, 1:] -= stress_factor * DELTA * COUPLING * h0
    return gamma


def link_action(
    geometry: np.ndarray,
    covector: np.ndarray,
    einbein: float,
    displacement: np.ndarray,
    mass: float = 0.0,
    mutation: str = "",
) -> float:
    gamma = integrated_gamma(geometry, mutation)
    p = np.asarray(covector, dtype=float)
    return float(p @ displacement - 0.5 * einbein * (p @ gamma @ p + mass**2))


def central_gradient(function, value: np.ndarray, step: float = 1.0) -> np.ndarray:
    point = np.asarray(value, dtype=float)
    result = np.zeros_like(point)
    for index in np.ndindex(point.shape):
        direction = np.zeros_like(point)
        direction[index] = step
        result[index] = (function(point + direction) - function(point - direction)) / (2.0 * step)
    return result


def expected_geometry_gradient(covector: np.ndarray, einbein: float) -> np.ndarray:
    p = np.asarray(covector, dtype=float)
    rho = einbein * p[0] ** 2
    current = -einbein * p[0] * p[1:]
    stress = einbein * np.outer(p[1:], p[1:])
    return np.concatenate(
        (
            (-DELTA * COUPLING * rho,),
            (-0.5 * DELTA * COUPLING * rho,) * 2,
            2.0 * DELTA * COUPLING * current,
            2.0 * DELTA * COUPLING * current,
            2.0 * DELTA * COUPLING * tensor_coordinates(stress).real,
        )
    )


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations: list[np.ndarray] = []
    for perm in permutations(range(3)):
        permutation = np.eye(3)[list(perm)]
        for signs in product((-1.0, 1.0), repeat=3):
            rotation = np.diag(signs) @ permutation
            if round(np.linalg.det(rotation)) == 1:
                rotations.append(rotation)
    return tuple(rotations)


def rotate_geometry(values: np.ndarray, rotation: np.ndarray) -> np.ndarray:
    n0, n1_tail, n1_head, beta0, beta1, h0 = unpack_geometry(values)
    return np.concatenate(
        (
            (n0, n1_tail, n1_head),
            rotation @ beta0,
            rotation @ beta1,
            tensor_coordinates(rotation @ h0 @ rotation.T).real,
        )
    )


def action_gradient_certificate(mutation: str) -> dict[str, object]:
    geometry = np.asarray(
        (0.12, -0.08, 0.17, 0.05, -0.11, 0.07, -0.03, 0.09, 0.04,
         0.16, -0.06, 0.13, 0.08, -0.05, 0.11)
    )
    covectors = tuple(
        np.concatenate(((-weight,), weight * np.asarray(direction, dtype=float)))
        for direction in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
        for weight in (1.0, -1.0)
    )
    gradient_error = 0.0
    interaction_error = 0.0
    symmetry_error = 0.0
    for covector in covectors:
        einbein = -1.0 / covector[0]
        displacement = einbein * ETA @ covector
        observed = central_gradient(
            lambda value: link_action(value, covector, einbein, displacement, mutation=mutation),
            geometry,
        )
        expected = expected_geometry_gradient(covector, einbein)
        gradient_error = max(gradient_error, float(np.max(np.abs(observed - expected))))
        flat_action = link_action(np.zeros(15), covector, einbein, displacement)
        actual_action = link_action(geometry, covector, einbein, displacement, mutation=mutation)
        interaction_error = max(
            interaction_error,
            abs((actual_action - flat_action) - float(expected @ geometry)),
        )
        symmetry_error = max(
            symmetry_error,
            float(np.max(np.abs(integrated_gamma(geometry, mutation) - integrated_gamma(geometry, mutation).T))),
        )

    covariance_error = 0.0
    covector = np.asarray((-0.73, 0.42, -0.31, 0.54))
    displacement = np.asarray((1.0, 0.23, -0.17, 0.41))
    einbein = 0.91
    base = link_action(geometry, covector, einbein, displacement, mutation=mutation)
    for rotation in proper_cubic_rotations():
        lift = np.zeros((4, 4))
        lift[0, 0] = 1.0
        lift[1:, 1:] = rotation
        transformed = link_action(
            rotate_geometry(geometry, rotation),
            lift @ covector,
            einbein,
            lift @ displacement,
            mutation=mutation,
        )
        covariance_error = max(covariance_error, abs(transformed - base))
    return {
        "links": len(covectors),
        "gradient_error": gradient_error,
        "interaction_error": interaction_error,
        "symmetry_error": symmetry_error,
        "frames": len(proper_cubic_rotations()),
        "covariance_error": covariance_error,
    }


def mixed_hessian_certificate(mutation: str) -> dict[str, object]:
    geometry = np.asarray(
        (0.07, -0.02, 0.11, 0.03, 0.08, -0.04, -0.05, 0.06, 0.09,
         0.12, -0.09, 0.04, 0.03, 0.02, -0.07)
    )
    covector = np.asarray((-0.83, 0.47, -0.36, 0.59))
    einbein = 1.17
    displacement = np.asarray((1.0, 0.31, -0.22, 0.44))

    dq_dp = np.column_stack(
        tuple(
            (
                expected_geometry_gradient(covector + np.eye(4)[index], einbein)
                - expected_geometry_gradient(covector - np.eye(4)[index], einbein)
            ) / 2.0
            for index in range(4)
        )
    )
    dp_dq = np.column_stack(
        tuple(
            (
                displacement - einbein * integrated_gamma(geometry + np.eye(15)[index]) @ covector
                - (displacement - einbein * integrated_gamma(geometry - np.eye(15)[index]) @ covector)
            ) / 2.0
            for index in range(15)
        )
    ).T
    dq_de = (
        expected_geometry_gradient(covector, einbein + 1.0)
        - expected_geometry_gradient(covector, einbein - 1.0)
    ) / 2.0
    de_dq = central_gradient(
        lambda q: -0.5 * float(covector @ integrated_gamma(q) @ covector),
        geometry,
    )
    if mutation == "break_mixed_hessian":
        dp_dq = dp_dq.copy()
        dp_dq[0, 0] += 0.25

    flat_error = 0.0
    mass_error = 0.0
    glue_error = 0.0
    for direction in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        for weight in (1.0, -1.0):
            p = np.concatenate(((-weight,), weight * np.asarray(direction, dtype=float)))
            e = 1.0 / weight
            dx = np.concatenate(((1.0,), np.asarray(direction, dtype=float)))
            used_mass = 1.0 if mutation == "skip_mass_shell" else 0.0
            flat_error = max(flat_error, float(np.max(np.abs(dx - e * ETA @ p))))
            mass_error = max(mass_error, abs(float(p @ ETA @ p + used_mass**2)))
            x0 = np.zeros(3)
            x_mid = np.asarray(direction, dtype=float)
            x1 = 2.0 * x_mid
            left = p[1:].copy()
            right = p[1:].copy()

            def free_chain(varied_midpoint: np.ndarray) -> float:
                return float(
                    p[0]
                    + left @ (varied_midpoint - x0)
                    + p[0]
                    + right @ (x1 - varied_midpoint)
                )

            observed_glue = central_gradient(free_chain, x_mid)
            expected_glue = left - right
            glue_error = max(
                glue_error,
                float(np.max(np.abs(observed_glue - expected_glue))),
                float(np.max(np.abs(observed_glue))),
            )
    return {
        "p_hessian_error": float(np.max(np.abs(dq_dp - dp_dq))),
        "e_hessian_error": float(np.max(np.abs(dq_de - de_dq))),
        "flat_error": flat_error,
        "mass_error": mass_error,
        "glue_error": glue_error,
        "matter_coordinates": 5,
        "geometry_coordinates": 15,
    }


def smooth_geometry(x0: np.ndarray, x1: np.ndarray, shift: np.ndarray, amplitude: float) -> np.ndarray:
    tail = np.asarray(x0) - shift
    head = np.asarray(x1) - shift
    midpoint = 0.5 * (tail + head)
    n0 = amplitude * 0.17 * np.sin(np.asarray((0.4, 0.7, -0.3)) @ tail)
    n1_tail = amplitude * -0.13 * np.cos(np.asarray((0.2, -0.5, 0.6)) @ tail)
    n1_head = amplitude * -0.13 * np.cos(np.asarray((0.2, -0.5, 0.6)) @ head)
    beta0 = amplitude * np.asarray((0.05, -0.08, 0.11)) * np.sin(np.asarray((0.3, 0.4, 0.2)) @ midpoint)
    beta1 = amplitude * np.asarray((-0.06, 0.09, 0.04)) * np.cos(np.asarray((0.5, -0.2, 0.3)) @ midpoint)
    h = np.zeros(6)
    h[0] = amplitude * 0.31 * np.sin(np.asarray((0.6, 0.8, -0.4)) @ tail)
    h[1:] = amplitude * np.asarray((-0.04, 0.07, 0.03, -0.05, 0.02))
    return np.concatenate(((n0, n1_tail, n1_head), beta0, beta1, h))


def smooth_action(
    x0: np.ndarray,
    x1: np.ndarray,
    field_shift: np.ndarray,
    amplitude: float,
    coupling: float,
) -> float:
    geometry = smooth_geometry(x0, x1, field_shift, amplitude)
    covector = np.asarray((-1.0, 1.0, 0.0, 0.0))
    displacement = np.concatenate(((1.0,), x1 - x0))
    gamma = integrated_gamma(geometry)
    interaction = gamma - ETA
    return float(covector @ displacement - 0.5 * (covector @ ETA @ covector) - 0.5 * coupling * (covector @ interaction @ covector))


def smooth_recoil_certificate(mutation: str) -> dict[str, object]:
    x0 = np.asarray((0.23, -0.17, 0.31))
    x1 = x0 + np.asarray((1.0, 0.0, 0.0))
    zero = np.zeros(3)
    translation = np.asarray((0.19, -0.11, 0.07))
    base = smooth_action(x0, x1, zero, 1.0, 1.0)
    moved = smooth_action(x0 + translation, x1 + translation, translation, 1.0, 1.0)
    translation_error = abs(base - moved)
    force0 = -central_gradient(
        lambda value: smooth_action(value, x1, zero, 1.0, 1.0), x0, step=1.0e-5
    )
    force1 = -central_gradient(
        lambda value: smooth_action(x0, value, zero, 1.0, 1.0), x1, step=1.0e-5
    )
    if mutation == "freeze_smooth_recoil":
        force0[:] = 0.0
        force1[:] = 0.0
    transverse = max(abs(force0[1]), abs(force0[2]), abs(force1[1]), abs(force1[2]))

    def transverse_force(coupling: float) -> float:
        amplitude = coupling
        observed = -central_gradient(
            lambda value: smooth_action(value, x1, zero, amplitude, coupling),
            x0,
            step=1.0e-5,
        )
        # The flat canonical term contributes only along the link direction;
        # transverse components are entirely interaction recoil.
        return float(np.linalg.norm(observed[1:]))

    low = transverse_force(0.2)
    high = transverse_force(0.4)
    scale_error = abs(high / low - 4.0)
    return {
        "translation_error": translation_error,
        "transverse": transverse,
        "force_norm": float(np.linalg.norm(force0) + np.linalg.norm(force1)),
        "scale_error": scale_error,
    }


def stage_rank_certificate(mutation: str) -> dict[str, object]:
    _k, rho, rho_next, _incoming, current, stress, _neutral = source_mode_data(
        3, 0, -1, 1, 0, 1, 0
    )
    midpoint = 0.5 * (rho + rho_next)
    stage_one = rho * stress[0, 0] - current[0] ** 2
    stage_two = midpoint * 0.0 - current[0] ** 2
    note = flat(NOTE_PATH)
    acknowledged = "same-event point-worldline interpretation fails" in note
    if mutation == "claim_stage_local":
        acknowledged = False
    return {
        "rho": rho,
        "midpoint": midpoint,
        "current": current[0],
        "stage_one": stage_one,
        "stage_two_magnitude": abs(stage_two),
        "stage_two_squared": abs(stage_two) ** 2,
        "acknowledged": acknowledged,
        "macro_escape": "macro-link construction evades" in note,
    }


def spatial_operators(momentum: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    p = 2.0 * np.sin(np.asarray(momentum, dtype=float) / 2.0)
    kappa_squared = float(p @ p)
    identity = np.eye(3)
    kinetic = np.column_stack(
        tuple(tensor_coordinates(item - 0.5 * identity * np.trace(item)) for item in BASIS)
    )
    potential = np.column_stack(
        tuple(
            tensor_coordinates(
                kappa_squared * item
                + np.outer(p, p) * np.trace(item)
                - np.outer(p, p @ item)
                - np.outer(item @ p, p)
                - identity * (kappa_squared * np.trace(item) - p @ item @ p)
            )
            for item in BASIS
        )
    )
    hamiltonian = np.asarray(
        [np.sum((kappa_squared * identity - np.outer(p, p)) * item) for item in BASIS],
        dtype=complex,
    )[None, :]
    momentum_constraint = np.column_stack(tuple(-2.0j * (item @ p) for item in BASIS))
    return kinetic, potential, hamiltonian, momentum_constraint


@lru_cache(maxsize=None)
def cached_operators(momentum_key: tuple[float, float, float]) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    return spatial_operators(np.asarray(momentum_key))


def schedule_residual(data, weights: tuple[float, float]) -> float:
    momentum, rho, rho_next, incoming, outgoing, stress, _neutral = data
    key = tuple(float(value) for value in momentum)
    kinetic, potential, hamiltonian, momentum_constraint = cached_operators(key)
    h = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray((rho,))
    pi = np.linalg.pinv(momentum_constraint, rcond=1.0e-12) @ (2.0 * incoming)
    stress_coordinates = tensor_coordinates(stress)
    pi1 = pi + DELTA * (-potential @ h + weights[0] * stress_coordinates)
    h1 = h + DELTA * (kinetic @ pi1)
    pi2 = pi1 + DELTA * (-potential @ h1 + weights[1] * stress_coordinates)
    h2 = h1 + DELTA * (kinetic @ pi2)
    midpoint = 0.5 * (rho + rho_next)
    return float(
        max(
            np.max(np.abs(momentum_constraint @ pi1 - 2.0 * outgoing)),
            np.max(np.abs(momentum_constraint @ pi2 - 2.0 * outgoing)),
            abs((hamiltonian @ h1)[0] - midpoint),
            abs((hamiltonian @ h2)[0] - rho_next),
        )
    )


def time_adjoint_certificate(mutation: str) -> dict[str, object]:
    modes = 0
    front_failures = 0
    equal_failures = 0
    front_error = 0.0
    equal_error = 0.0
    for size in range(3, 9):
        for axis in range(3):
            for sign in (-1, 1):
                for neutral_step in (1, 2):
                    for along in range(size):
                        for transverse in range(1, size):
                            for remaining in range(size):
                                data = source_mode_data(size, axis, sign, neutral_step, along, transverse, remaining)
                                front = schedule_residual(data, (2.0, 0.0))
                                equal = schedule_residual(data, (1.0, 1.0))
                                front_failures += int(front > TOL)
                                equal_failures += int(equal > TOL)
                                front_error = max(front_error, front)
                                equal_error = max(equal_error, equal)
                                modes += 1
    covector = np.asarray((-1.0, 1.0, 0.0, 0.0))
    displacement = np.asarray((1.0, 1.0, 0.0, 0.0))
    forward_geometry = np.zeros(15)
    forward_geometry[9] = 1.0
    adjoint_geometry = np.zeros(15)
    flat_action = link_action(np.zeros(15), covector, 1.0, displacement)
    forward_interaction = link_action(
        forward_geometry, covector, 1.0, displacement
    ) - flat_action
    adjoint_interaction = link_action(
        adjoint_geometry, covector, 1.0, displacement
    ) - flat_action
    reversal_residual = abs(forward_interaction - adjoint_interaction)
    note = flat(NOTE_PATH)
    scoped = "not time-self-adjoint" in note and "equal stress split" in note
    if mutation == "claim_time_symmetric":
        scoped = False
    return {
        "modes": modes,
        "front_failures": front_failures,
        "front_error": front_error,
        "equal_failures": equal_failures,
        "equal_error": equal_error,
        "reversal_residual": reversal_residual,
        "scoped": scoped,
    }


def raw_potential_stencil(size: int = 7) -> dict[tuple[int, int, int], np.ndarray]:
    symbols = np.zeros((size, size, size, 6, 6), dtype=complex)
    for index in np.ndindex((size,) * 3):
        momentum = 2.0 * np.pi * np.asarray(index, dtype=float) / size
        _kinetic, potential, _hamiltonian, _momentum = spatial_operators(momentum)
        phases = np.asarray(
            (
                1.0,
                1.0,
                1.0,
                np.exp(0.5j * (momentum[0] + momentum[1])),
                np.exp(0.5j * (momentum[0] + momentum[2])),
                np.exp(0.5j * (momentum[1] + momentum[2])),
            )
        )
        placement = np.diag(phases)
        symbols[index] = placement @ potential @ placement.conj().T
    kernel = np.fft.fftn(symbols, axes=(0, 1, 2)) / size**3
    maxima = np.max(np.abs(kernel), axis=(3, 4))
    result: dict[tuple[int, int, int], np.ndarray] = {}
    for index in np.argwhere(maxima > 1.0e-10):
        shift = tuple(int(value if value <= size // 2 else value - size) for value in index)
        result[shift] = kernel[tuple(index)]
    return result


def ward_boundary_certificate(mutation: str) -> dict[str, object]:
    support_profiles = (
        np.asarray((0.5, 0.0, 0.5)),
        np.asarray((0.0, 1.0, 0.0)),
        np.asarray((1.0, 0.0, 0.0)),
    )
    center = np.asarray((0.5, 0.5, 0.0))
    radius = max(float(np.max(np.abs(profile - center))) for profile in support_profiles)
    lower_bound = 0.5 * float(np.max(np.abs(support_profiles[1] - support_profiles[2])))

    stencil = raw_potential_stencil()
    nonzero = tuple(shift for shift in stencil if shift != (0, 0, 0))
    axial = tuple(shift for shift in nonzero if sum(abs(value) for value in shift) == 1)
    diagonal = tuple(shift for shift in nonzero if sum(abs(value) for value in shift) == 2)
    first_path = ((1, 0, 0), (0, 1, 0))
    second_path = ((0, 1, 0), (1, 0, 0))
    axis_swap = np.asarray(((0, 1, 0), (1, 0, 0), (0, 0, -1)))
    displacement = np.asarray((1, 1, 0))
    transformed = tuple(tuple(int(value) for value in axis_swap @ np.asarray(step)) for step in first_path)
    route_fixed = transformed == first_path

    counts = []
    for size in (5, 7, 9):
        frequencies = 2.0 * np.pi * np.fft.fftfreq(size)
        x = 0.37
        weights = np.asarray(
            [np.mean(np.exp(1.0j * frequencies * (x - site))) for site in range(size)]
        )
        counts.append(int(np.count_nonzero(np.abs(weights) > 1.0e-12)))
    epsilon = 1.0e-6

    def hat(value: float) -> float:
        return max(1.0 - abs(value), 0.0)

    left_derivative = (hat(0.0) - hat(-epsilon)) / epsilon
    right_derivative = (hat(epsilon) - hat(0.0)) / epsilon
    hat_jump = abs(left_derivative - right_derivative)

    note = flat(NOTE_PATH)
    noether = flat(NOETHER_NOTE)
    scoped = all(
        phrase in note
        for phrase in (
            "candidate component-staggered integrated inverse-metric coupling",
            "bounded-local component/stage pullback",
            "localized total ward identity is not executed",
            "18-edge graph current",
        )
    )
    if mutation in ("claim_point_metric", "claim_local_interpolation", "claim_total_ward"):
        scoped = False
    return {
        "quadrature_radius": radius,
        "quadrature_lower": lower_bound,
        "support": len(stencil),
        "axial": len(axial),
        "diagonal": len(diagonal),
        "swap_fixes_displacement": bool(np.array_equal(axis_swap @ displacement, displacement)),
        "swap_exchanges_paths": transformed == second_path,
        "route_fixed": route_fixed,
        "spectral_counts": counts,
        "hat_jump": hat_jump,
        "site_mixing_open": "site-mixing generators are out of scope" in noether,
        "scoped": scoped,
    }


def scope_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    axiom = (ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md").read_text(encoding="utf-8")
    valid = all(
        phrase in note
        for phrase in (
            "signed diagnostic pair",
            "negative einbein",
            "positive isolated matter is not established",
            "smooth recoil comparator is conditional",
            "full dynamic lattice matter is not established",
            "gravity does not fail",
            "no axiom is amended",
            "no toe percentage moves",
            "fail — partial-narrowing",
            "n1 — alternative route enumeration",
            "n8 — cross-cycle echo",
            "state is a configuration of records",
        )
    )
    if mutation in (
        "claim_positive_matter",
        "claim_dynamic_complete",
        "claim_gravity_no_go",
        "claim_axiom_update",
        "claim_toe_progress",
    ):
        valid = False
    return {
        "valid": valid,
        "axiom_state": "A state is a configuration of records." in axiom,
        "permanent": "records are permanent" in axiom,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "wrong_pair_phase",
            "positive_only",
            "wrong_lapse_weight",
            "wrong_shift_weight",
            "wrong_stress_weight",
            "break_mixed_hessian",
            "skip_mass_shell",
            "freeze_smooth_recoil",
            "claim_stage_local",
            "claim_time_symmetric",
            "claim_point_metric",
            "claim_local_interpolation",
            "claim_total_ward",
            "claim_positive_matter",
            "claim_dynamic_complete",
            "claim_gravity_no_go",
            "claim_axiom_update",
            "claim_toe_progress",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority-parent-and-runtime-closure",
        "current axioms, Block82, Block78, and every declared comparison input are content-bound",
        authority["origin_main"] == CURRENT_AXIOM_COMMIT
        and authority["axiom_blob"] == authority["expected_axiom"]
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and not authority["mismatches"]
        and not authority["missing_inputs"]
        and authority["loaded"] == {RUNNER_RELATIVE},
        f"loaded scripts={len(authority['loaded'])}; frozen mismatches={len(authority['mismatches'])}",
    )

    source = signed_source_certificate(mutation)
    checks.check(
        "B-signed-two-link-source-and-flat-null-root",
        "two parallel links of weights +1 and -1 exactly generate every Block78 source component",
        source["modes"] == 13056
        and source["error"] < TOL
        and source["zero_mode_error"] < TOL
        and source["null_error"] < TOL
        and source["velocity_error"] < TOL
        and source["response_error"] < TOL
        and source["negative_legs"] == 13056,
        f"modes={source['modes']}; source/null/velocity={source['error']:.2e}/{source['null_error']:.1e}/{source['velocity_error']:.1e}; negative legs={source['negative_legs']}",
    )

    action = action_gradient_certificate(mutation)
    checks.check(
        "C-one-scalar-component-staggered-geometry-response",
        "one symmetric macro-link coefficient yields the required lapse, shift, and front-loaded stress gradients",
        action["links"] == 12
        and action["gradient_error"] < TOL
        and action["interaction_error"] < TOL
        and action["symmetry_error"] < TOL
        and action["frames"] == 24
        and action["covariance_error"] < TOL,
        f"links/frames={action['links']}/{action['frames']}; gradient/scalar/cubic={action['gradient_error']:.2e}/{action['interaction_error']:.2e}/{action['covariance_error']:.2e}",
    )

    mixed = mixed_hessian_certificate(mutation)
    checks.check(
        "D-matter-geometry-mixed-hessians-and-flat-equations",
        "the P and e cross derivatives commute and the signed flat links solve velocity and mass shell",
        mixed["p_hessian_error"] < TOL
        and mixed["e_hessian_error"] < TOL
        and mixed["flat_error"] < TOL
        and mixed["mass_error"] < TOL
        and mixed["glue_error"] < TOL
        and mixed["matter_coordinates"] == 5
        and mixed["geometry_coordinates"] == 15,
        f"mixed P/e={mixed['p_hessian_error']:.2e}/{mixed['e_hessian_error']:.2e}; flat/mass={mixed['flat_error']:.1e}/{mixed['mass_error']:.1e}",
    )

    recoil = smooth_recoil_certificate(mutation)
    checks.check(
        "E-conditional-smooth-recoil-and-global-translation-comparator",
        "a smooth-field extension gives nonzero transverse reciprocal force and exact joint global translation",
        recoil["translation_error"] < TOL
        and recoil["transverse"] > 1.0e-3
        and recoil["force_norm"] > 1.0e-3
        and recoil["scale_error"] < 1.0e-8,
        f"translation={recoil['translation_error']:.1e}; transverse/force={recoil['transverse']:.4f}/{recoil['force_norm']:.4f}; g2 scale={recoil['scale_error']:.1e}",
    )

    stage = stage_rank_certificate(mutation)
    checks.check(
        "F-same-event-stage-rank-obstruction-and-macro-link-escape",
        "the second stage violates the point-worldline rank-one minor while the aggregate macro link survives",
        abs(stage["rho"] - stage["midpoint"]) < TOL
        and abs(stage["current"] + stage["rho"]) < TOL
        and abs(stage["stage_one"]) < TOL
        and abs(stage["stage_two_magnitude"] - 3.0) < TOL
        and abs(stage["stage_two_squared"] - 9.0) < TOL
        and stage["acknowledged"]
        and stage["macro_escape"],
        f"stage-one minor={abs(stage['stage_one']):.1e}; stage-two magnitude/squared={stage['stage_two_magnitude']:.1f}/{stage['stage_two_squared']:.1f}",
    )

    adjoint = time_adjoint_certificate(mutation)
    checks.check(
        "G-front-loaded-cadence-versus-time-adjoint-boundary",
        "the exact front-loaded schedule is not self-adjoint and its equal-weight symmetrization breaks constraints",
        adjoint["modes"] == 13056
        and adjoint["front_failures"] == 0
        and adjoint["front_error"] < 5.0e-12
        and adjoint["equal_failures"] == 11064
        and abs(adjoint["equal_error"] - 4.0) < TOL
        and abs(adjoint["reversal_residual"] - 1.0) < TOL
        and adjoint["scoped"],
        f"front/equal failures={adjoint['front_failures']}/{adjoint['equal_failures']}; maxima={adjoint['front_error']:.2e}/{adjoint['equal_error']:.1f}; reversal={adjoint['reversal_residual']:.1f}",
    )

    ward = ward_boundary_certificate(mutation)
    checks.check(
        "H-component-quadrature-and-graph-current-boundary",
        "no common point quadrature exists and diagonal graph edges have no unique cubic-equivariant axis route",
        abs(ward["quadrature_radius"] - 0.5) < TOL
        and abs(ward["quadrature_lower"] - 0.5) < TOL
        and ward["support"] == 19
        and ward["axial"] == 6
        and ward["diagonal"] == 12
        and ward["swap_fixes_displacement"]
        and ward["swap_exchanges_paths"]
        and not ward["route_fixed"],
        f"quadrature min sup={ward['quadrature_radius']:.1f}; support axial/diagonal={ward['axial']}/{ward['diagonal']}; invariant single route={ward['route_fixed']}",
    )

    checks.check(
        "I-bounded-local-pullback-and-localized-Ward-gate",
        "spectral recoil is global, hat interpolation is nonsmooth, and the required site-mixing theorem remains open",
        ward["spectral_counts"] == [5, 7, 9]
        and abs(ward["hat_jump"] - 2.0) < TOL
        and ward["site_mixing_open"]
        and ward["scoped"],
        f"spectral support={ward['spectral_counts']}; hat derivative jump={ward['hat_jump']:.1f}; site-mixing open={ward['site_mixing_open']}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "J-no-go-axiom-Record-retention-and-TOE-scope",
        "the positive link action and narrow boundaries do not establish positive matter, gravity failure, or TOE movement",
        all(scope.values()),
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} minimal-axiom blob={CURRENT_AXIOM_BLOB}; Block82 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: checked — one 4x4 symmetric macro-link coefficient, 15 geometry coordinates, four momenta, and one einbein have exact source gradients and mixed Hessians"
    )
    print(
        "per_site: checked and bounded — integer tail/head/midpoint deposition is nearest-link local; differentiable varied-position interpolation is not supplied"
    )
    print(
        "per_mode: checked — all 13,056 L=3..8 signed neutral source modes are generated by the two-link Fourier transform"
    )
    print(
        "per_block: checked — flat matter equations, source cadence, proper-cubic scalar covariance, rank-one hostile control, and time-adjoint hostile control are separate"
    )
    print(
        "lattice_wide: checked and not executed — no bounded-local component pullback, site-mixing gauge identity, localized total Ward tensor, positive compact matter, Record compiler, or retained chain"
    )
    print(
        "RESULT: a genuine component-staggered signed-link action closes source gradients and P/e mixed Hessians; the first remaining gravity object is the equivariant local pullback/deposition map"
    )
    print(
        "PORTFOLIO: freeze further coefficient/Hessian work after this block unless the pullback-chain identity is constructed; redirect to state/Record/Born, physical lineage, and retention"
    )
    print(
        "SCOPE: positive partial joint-action progress; no localized total Ward closure, axiom update, obligation retirement, audit verdict, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
