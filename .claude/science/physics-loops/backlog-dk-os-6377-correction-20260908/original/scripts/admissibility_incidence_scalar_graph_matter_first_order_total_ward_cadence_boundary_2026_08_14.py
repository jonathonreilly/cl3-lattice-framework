#!/usr/bin/env python3
"""Block 95: local incidence scalar, total Ward cochain, and ADM cadence.

A nearest-neighbour Lorentzian lattice half-density scalar on the actual
Block77 staggered tensor/vector carrier has a finite raw stress vertex and a
finite link-centred site-mixing generator.  Their off-shell first-order
matter--geometry cochain is exact.  The same Hermitian scalar action supplies
the geometry source, reciprocal matter recoil, and commuting mixed Hessians.
On exact massless-shell transfers its source satisfies the covariant Ward identity and
propagates all four Block78 constraints under the required front-loaded
stress cadence.  Positive compact zero-mode support, nonlinear Ward closure,
the common stage/work map, Record compilation, selection, and retention stay
open.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_"
    "CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
RUNNER_RELATIVE = (
    "scripts/admissibility_incidence_scalar_graph_matter_first_order_total_"
    "ward_cadence_boundary_2026_08_14.py"
)
BLOCK77_NOTE = (
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_"
    "TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK77_RUNNER = (
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_"
    "tensor_cadence_boundary_2026_08_14.py"
)
BLOCK78_NOTE = (
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_"
    "CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK78_RUNNER = (
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_"
    "cadence_boundary_2026_08_14.py"
)
BLOCK83_NOTE = (
    "docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK83_RUNNER = (
    "scripts/admissibility_component_staggered_signed_link_action_local_"
    "ward_boundary_2026_08_14.py"
)
BLOCK93_NOTE = (
    "docs/ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK93_RUNNER = (
    "scripts/admissibility_raw_graph_ward_compact_pullback_translation_"
    "generator_boundary_2026_08_14.py"
)
BLOCK53_NOTE = (
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_"
    "UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK53_RUNNER = (
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_"
    "update_lstar_boundary_2026_08_11.py"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14.py",
    "scripts/admissibility_raw_graph_ward_compact_pullback_translation_generator_boundary_2026_08_14.py",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
)

CURRENT_AXIOM_COMMIT = "eee6ab5874e2fc207db5526dc82d9f71ae550c7c"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
PARENT_COMMIT = "ccaeed85fb2cfc9354973e55ac3b5c627618fee5"
BLOCK77_NOTE_BLOB = "05b2d0fe7a6ff79243c8ba7c5ae87c2a0c13ca02"
BLOCK77_RUNNER_BLOB = "fd23e8f7caf5cff5d76c8bec3864554e5f280708"
BLOCK78_NOTE_BLOB = "f9cbc29ddf57cb3385b65e97e6cad497b7b66d1d"
BLOCK78_RUNNER_BLOB = "2066434b8b96240774fc7f4c7cd9b2adcdd78a94"
BLOCK83_NOTE_BLOB = "e78006cf55101576993cd39941163e922583b473"
BLOCK83_RUNNER_BLOB = "86bae02240012cc935f1b3df644892a5487f5a90"
BLOCK93_NOTE_BLOB = "98a551203819af056fd2d3e2a66a393f8caf29d0"
BLOCK93_RUNNER_BLOB = "35a988db4a29aa3a7cd42387db18a7b4018bf022"

TOL = 2.0e-10
MASS = 0.0
MASSIVE_SPECTATOR = 0.37

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14 as block77  # noqa: E402


ETA = block77.ETA
BASIS3 = block77.block53.SYMMETRIC_BASIS
IDENTITY6 = np.eye(6)
LaurentKey = tuple[int, ...]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 160 else detail[:157] + "..."
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
    current = {NOTE_PATH.relative_to(ROOT).as_posix(), RUNNER_RELATIVE}
    frozen = tuple(item for item in AUDIT_INPUT_PATHS if item not in current)
    mismatches = tuple(
        item
        for item in frozen
        if git_worktree_path_blob(item) != git_commit_path_blob(PARENT_COMMIT, item)
    )
    loaded: set[str] = set()
    for module in tuple(sys.modules.values()):
        file_name = getattr(module, "__file__", None)
        if not file_name:
            continue
        module_path = Path(file_name).resolve()
        try:
            relative = module_path.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if relative.startswith("scripts/") and relative.endswith(".py"):
            loaded.add(relative)
    declared = {item for item in AUDIT_INPUT_PATHS if item.startswith("scripts/")}
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    return {
        "origin_main": origin_main,
        "axiom": git_worktree_path_blob("docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "expected_axiom": expected_axiom,
        "mismatches": mismatches,
        "missing": tuple(item for item in AUDIT_INPUT_PATHS if not (ROOT / item).exists()),
        "loaded_missing": tuple(sorted(loaded - declared)),
        "block77": (
            git_worktree_path_blob(BLOCK77_NOTE),
            git_worktree_path_blob(BLOCK77_RUNNER),
        ),
        "block78": (
            git_worktree_path_blob(BLOCK78_NOTE),
            git_worktree_path_blob(BLOCK78_RUNNER),
        ),
        "block83": (
            git_worktree_path_blob(BLOCK83_NOTE),
            git_worktree_path_blob(BLOCK83_RUNNER),
        ),
        "block93": (
            git_worktree_path_blob(BLOCK93_NOTE),
            git_worktree_path_blob(BLOCK93_RUNNER),
        ),
    }


def scalar_symbol(momentum: np.ndarray, mass: float = MASS) -> float:
    p = block77.lattice_vector(momentum)
    return float(p @ ETA @ p + mass**2)


def average_derivative(incoming: np.ndarray, transfer: np.ndarray) -> np.ndarray:
    return ETA @ np.sin(np.asarray(incoming, dtype=float) + 0.5 * np.asarray(transfer, dtype=float))


def tensor_coordinates(tensor: np.ndarray) -> np.ndarray:
    return np.asarray(
        [np.sum(basis * tensor) for basis in block77.BASIS],
        dtype=complex,
    )


def centered_stress(incoming: np.ndarray, transfer: np.ndarray) -> np.ndarray:
    derivative = average_derivative(incoming, transfer)
    return np.outer(derivative, derivative)


def raw_stress(incoming: np.ndarray, transfer: np.ndarray) -> np.ndarray:
    return block77.placement_matrix(transfer) @ tensor_coordinates(
        centered_stress(incoming, transfer)
    )


def raw_generator(incoming: np.ndarray, transfer: np.ndarray) -> np.ndarray:
    return 1.0j * block77.vector_placement(transfer) @ average_derivative(
        incoming, transfer
    )


def add_laurent(
    coefficients: dict[LaurentKey, np.ndarray],
    matter_shift: np.ndarray,
    geometry_shift: np.ndarray,
    component: int,
    value: complex,
    dimension: int,
) -> None:
    key = tuple(int(item) for item in np.concatenate((matter_shift, geometry_shift)))
    coefficients.setdefault(key, np.zeros(dimension, dtype=complex))[component] += value


def scalar_laurent_coefficients() -> dict[LaurentKey, np.ndarray]:
    result: dict[LaurentKey, np.ndarray] = {}
    zero = np.zeros(4, dtype=int)
    key = tuple(int(item) for item in np.concatenate((zero, zero)))
    result[key] = np.asarray((MASS**2 + 2.0 * float(np.trace(ETA)),), dtype=complex)
    for axis in range(4):
        for sign in (-1, 1):
            matter = np.zeros(4, dtype=int)
            matter[axis] = sign
            key = tuple(int(item) for item in np.concatenate((matter, zero)))
            result[key] = np.asarray((-ETA[axis, axis],), dtype=complex)
    return result


def generator_laurent_coefficients() -> dict[LaurentKey, np.ndarray]:
    result: dict[LaurentKey, np.ndarray] = {}
    for axis in range(4):
        matter = np.zeros(4, dtype=int)
        geometry = np.zeros(4, dtype=int)
        matter[axis] = 1
        geometry[axis] = 1
        add_laurent(result, matter, geometry, axis, 0.5 * ETA[axis, axis], 4)
        matter = np.zeros(4, dtype=int)
        matter[axis] = -1
        add_laurent(result, matter, np.zeros(4, dtype=int), axis, -0.5 * ETA[axis, axis], 4)
    return result


def stress_laurent_coefficients() -> dict[LaurentKey, np.ndarray]:
    result: dict[LaurentKey, np.ndarray] = {}
    for slot, (left, right) in enumerate(block77.PAIRS):
        if left == right:
            matter = np.zeros(4, dtype=int)
            geometry = np.zeros(4, dtype=int)
            matter[left] = 2
            geometry[left] = 1
            add_laurent(result, matter, geometry, slot, -0.25, 10)
            add_laurent(
                result,
                np.zeros(4, dtype=int),
                np.zeros(4, dtype=int),
                slot,
                0.5,
                10,
            )
            add_laurent(result, -matter, -geometry, slot, -0.25, 10)
            continue
        factor = np.sqrt(2.0) * ETA[left, left] * ETA[right, right] / 4.0
        terms = (
            ((1, 1), (1, 1), -factor),
            ((1, -1), (1, 0), factor),
            ((-1, 1), (0, 1), factor),
            ((-1, -1), (0, 0), -factor),
        )
        for matter_signs, geometry_signs, value in terms:
            matter = np.zeros(4, dtype=int)
            geometry = np.zeros(4, dtype=int)
            matter[left], matter[right] = matter_signs
            geometry[left], geometry[right] = geometry_signs
            add_laurent(result, matter, geometry, slot, value, 10)
    return result


def evaluate_laurent(
    coefficients: dict[LaurentKey, np.ndarray],
    incoming: np.ndarray,
    transfer: np.ndarray,
) -> np.ndarray:
    result = np.zeros_like(next(iter(coefficients.values())))
    point = np.concatenate((incoming, transfer))
    for shift, value in coefficients.items():
        result += value * np.exp(1.0j * np.asarray(shift) @ point)
    return result


def support_shape(coefficients: dict[LaurentKey, np.ndarray]) -> tuple[int, int, int, int, int, int]:
    support = np.asarray(tuple(coefficients), dtype=int)
    matter = support[:, :4]
    geometry = support[:, 4:]
    return (
        len(support),
        int(np.max(np.abs(matter))),
        int(np.max(np.sum(np.abs(matter), axis=1))),
        int(np.max(np.abs(geometry))),
        int(np.max(np.sum(np.abs(geometry), axis=1))),
        int(np.max(np.sum(np.abs(support), axis=1))),
    )


def locality_certificate(mutation: str) -> dict[str, object]:
    scalar = scalar_laurent_coefficients()
    generator = generator_laurent_coefficients()
    stress = stress_laurent_coefficients()
    scalar_error = 0.0
    generator_error = 0.0
    stress_error = 0.0
    rng = np.random.default_rng(9501)
    for _ in range(64):
        incoming = rng.uniform(-np.pi, np.pi, 4)
        transfer = rng.uniform(-np.pi, np.pi, 4)
        scalar_error = max(
            scalar_error,
            abs(evaluate_laurent(scalar, incoming, transfer)[0] - scalar_symbol(incoming)),
        )
        generator_error = max(
            generator_error,
            float(np.max(np.abs(evaluate_laurent(generator, incoming, transfer) - raw_generator(incoming, transfer)))),
        )
        stress_error = max(
            stress_error,
            float(np.max(np.abs(evaluate_laurent(stress, incoming, transfer) - raw_stress(incoming, transfer)))),
        )
    proof_valid = mutation != "fake_locality"
    return {
        "scalar_shape": support_shape(scalar),
        "generator_shape": support_shape(generator),
        "stress_shape": support_shape(stress),
        "scalar_terms": sum(np.count_nonzero(np.abs(value) > TOL) for value in scalar.values()),
        "generator_terms": sum(np.count_nonzero(np.abs(value) > TOL) for value in generator.values()),
        "stress_terms": sum(np.count_nonzero(np.abs(value) > TOL) for value in stress.values()),
        "scalar_error": scalar_error,
        "generator_error": generator_error,
        "stress_error": stress_error,
        "proof_valid": proof_valid,
    }


def vertex_certificate(mutation: str) -> dict[str, object]:
    rng = np.random.default_rng(9502)
    hermiticity = 0.0
    antihermiticity = 0.0
    periodicity = 0.0
    probes = 0
    position_generator_error = 0.0
    action_pairing_error = 0.0
    for _ in range(96):
        incoming = rng.uniform(-np.pi, np.pi, 4)
        transfer = rng.uniform(-np.pi, np.pi, 4)
        stress = raw_stress(incoming, transfer)
        generator = raw_generator(incoming, transfer)
        hermiticity = max(
            hermiticity,
            float(np.max(np.abs(raw_stress(incoming + transfer, -transfer) - stress.conj()))),
        )
        antihermiticity = max(
            antihermiticity,
            float(np.max(np.abs(raw_generator(incoming + transfer, -transfer) + generator.conj()))),
        )
        for axis in range(4):
            period = 2.0 * np.pi * np.eye(4)[axis]
            periodicity = max(
                periodicity,
                float(np.max(np.abs(raw_stress(incoming, transfer + period) - stress))),
                float(np.max(np.abs(raw_stress(incoming + period, transfer) - stress))),
                float(np.max(np.abs(raw_generator(incoming, transfer + period) - generator))),
                float(np.max(np.abs(raw_generator(incoming + period, transfer) - generator))),
            )
        probes += 1
    size = 7
    sites = np.arange(size, dtype=float)
    for axis in range(4):
        incoming_angle = 2.0 * np.pi * (axis + 1) / size
        transfer_angle = 2.0 * np.pi * (axis + 2) / size
        local = 0.5 * ETA[axis, axis] * (
            np.exp(-1.0j * transfer_angle * (sites - 0.5))
            * np.exp(-1.0j * incoming_angle * (sites - 1.0))
            - np.exp(-1.0j * transfer_angle * (sites + 0.5))
            * np.exp(-1.0j * incoming_angle * (sites + 1.0))
        )
        expected = (
            1.0j
            * ETA[axis, axis]
            * np.sin(incoming_angle + 0.5 * transfer_angle)
            * np.exp(-1.0j * (incoming_angle + transfer_angle) * sites)
        )
        position_generator_error = max(
            position_generator_error,
            float(np.max(np.abs(local - expected))),
        )
        action_pairing_error = max(
            action_pairing_error,
            float(
                np.max(
                    np.abs(
                        np.exp(-1.0j * transfer_angle * sites)
                        * np.exp(1.0j * (incoming_angle + transfer_angle) * sites)
                        * np.exp(-1.0j * incoming_angle * sites)
                        - 1.0
                    )
                )
            ),
        )
    if mutation == "break_hermiticity":
        hermiticity = max(hermiticity, 0.25)
    constant = raw_generator(np.asarray((0.31, -0.47, 0.28, 0.63)), np.zeros(4))
    return {
        "probes": probes,
        "hermiticity": hermiticity,
        "antihermiticity": antihermiticity,
        "periodicity": periodicity,
        "constant_norm": float(np.linalg.norm(constant)),
        "position_generator_error": position_generator_error,
        "action_pairing_error": action_pairing_error,
    }


def ward_covariance_certificate(mutation: str) -> dict[str, object]:
    rng = np.random.default_rng(9503)
    difference_error = 0.0
    cochain_error = 0.0
    rotation_error = 0.0
    generator_rotation_error = 0.0
    reflection_error = 0.0
    generator_reflection_error = 0.0
    level_set_error = 0.0
    massive_spectator_error = 0.0
    probes = 0
    for probe in range(96):
        incoming = rng.uniform(-np.pi, np.pi, 4)
        transfer = rng.uniform(-np.pi, np.pi, 4)
        derivative = average_derivative(incoming, transfer)
        difference = scalar_symbol(incoming + transfer) - scalar_symbol(incoming)
        massive_difference = scalar_symbol(
            incoming + transfer, MASSIVE_SPECTATOR
        ) - scalar_symbol(incoming, MASSIVE_SPECTATOR)
        stress = raw_stress(incoming, transfer)
        generator = raw_generator(incoming, transfer)
        difference_error = max(
            difference_error,
            abs(difference - 2.0 * block77.lattice_vector(transfer) @ derivative),
        )
        massive_spectator_error = max(
            massive_spectator_error,
            abs(massive_difference - difference),
        )
        cochain_error = max(
            cochain_error,
            float(np.max(np.abs(block77.raw_gauge(-transfer).T @ stress + difference * generator))),
        )
        if probe < 12:
            for spatial in block77.ROTATIONS:
                transform = np.eye(4)
                transform[:3, :3] = spatial
                transformed_transfer = transform @ transfer
                raw_tensor = (
                    block77.placement_matrix(transformed_transfer)
                    @ block77.tensor_representation(transform)
                    @ block77.placement_matrix(transfer).conj().T
                )
                raw_vector = (
                    block77.vector_placement(transformed_transfer)
                    @ transform
                    @ block77.vector_placement(transfer).conj().T
                )
                rotation_error = max(
                    rotation_error,
                    float(np.max(np.abs(raw_stress(transform @ incoming, transformed_transfer) - raw_tensor @ stress))),
                )
                generator_rotation_error = max(
                    generator_rotation_error,
                    float(np.max(np.abs(raw_generator(transform @ incoming, transformed_transfer) - raw_vector @ generator))),
                )
            reflection = np.diag((1.0, 1.0, 1.0, -1.0))
            reflected_transfer = reflection @ transfer
            raw_reflection = (
                block77.placement_matrix(reflected_transfer)
                @ block77.tensor_representation(reflection)
                @ block77.placement_matrix(transfer).conj().T
            )
            raw_vector_reflection = (
                block77.vector_placement(reflected_transfer)
                @ reflection
                @ block77.vector_placement(transfer).conj().T
            )
            reflection_error = max(
                reflection_error,
                float(np.max(np.abs(raw_stress(reflection @ incoming, reflected_transfer) - raw_reflection @ stress))),
            )
            generator_reflection_error = max(
                generator_reflection_error,
                float(np.max(np.abs(raw_generator(reflection @ incoming, reflected_transfer) - raw_vector_reflection @ generator))),
            )
        probes += 1

    for spatial in block77.ROTATIONS:
        transform = np.eye(4)
        transform[:3, :3] = spatial
        incoming = np.asarray((0.37, -0.51, 0.83, 0.29))
        outgoing = transform @ incoming
        transfer = outgoing - incoming
        stress = raw_stress(incoming, transfer)
        level_set_error = max(
            level_set_error,
            abs(scalar_symbol(outgoing) - scalar_symbol(incoming)),
            float(np.max(np.abs(block77.raw_gauge(-transfer).T @ stress))),
        )
    if mutation == "break_cochain":
        cochain_error = max(cochain_error, 0.125)
    return {
        "probes": probes,
        "difference_error": difference_error,
        "cochain_error": cochain_error,
        "rotation_error": rotation_error,
        "generator_rotation_error": generator_rotation_error,
        "reflection_error": reflection_error,
        "generator_reflection_error": generator_reflection_error,
        "level_set_error": level_set_error,
        "massive_spectator_error": massive_spectator_error,
        "frames": len(block77.ROTATIONS),
    }


def joint_action_certificate(mutation: str) -> dict[str, object]:
    size = 3
    mode_count = size**4
    rng = np.random.default_rng(9504)
    h_position = rng.normal(size=(size, size, size, size, 10))
    xi_position = rng.normal(size=(size, size, size, size, 4))
    h_modes = np.fft.fftn(h_position, axes=(0, 1, 2, 3)) / size**4
    xi_modes = np.fft.fftn(xi_position, axes=(0, 1, 2, 3)) / size**4
    hamiltonian = np.zeros((mode_count, mode_count), dtype=complex)
    generator_matrix = np.zeros_like(hamiltonian)
    varied_hamiltonian = np.zeros_like(hamiltonian)
    symbols = np.zeros(mode_count)
    mode_indices = tuple(np.ndindex((size,) * 4))
    momenta = {
        index: 2.0 * np.pi * np.asarray(index, dtype=float) / size
        for index in mode_indices
    }
    for incoming_index in mode_indices:
        incoming_flat = np.ravel_multi_index(incoming_index, (size,) * 4)
        incoming = momenta[incoming_index]
        symbols[incoming_flat] = scalar_symbol(incoming)
        for transfer_index in mode_indices:
            transfer_array = np.asarray(transfer_index, dtype=int)
            outgoing_index = tuple((np.asarray(incoming_index) + transfer_array) % size)
            outgoing_flat = np.ravel_multi_index(outgoing_index, (size,) * 4)
            negative_transfer = tuple((-transfer_array) % size)
            transfer = momenta[transfer_index]
            stress = raw_stress(incoming, transfer)
            generator = raw_generator(incoming, transfer)
            h_minus = h_modes[negative_transfer]
            xi_minus = xi_modes[negative_transfer]
            hamiltonian[outgoing_flat, incoming_flat] += h_minus @ stress
            generator_matrix[outgoing_flat, incoming_flat] += xi_minus @ generator
            varied_hamiltonian[outgoing_flat, incoming_flat] += (
                block77.raw_gauge(-transfer) @ xi_minus
            ) @ stress
    flat_operator = np.diag(symbols)
    ward_matrix = varied_hamiltonian + flat_operator @ generator_matrix - generator_matrix @ flat_operator
    field = rng.normal(size=mode_count) + 1.0j * rng.normal(size=mode_count)
    action_variation = abs(np.vdot(field, ward_matrix @ field))
    recoil = hamiltonian @ field

    selected_transfer_index = (1, 0, 1, 1)
    selected_transfer = momenta[selected_transfer_index]
    left = np.zeros((mode_count, 10), dtype=complex)
    right = np.zeros_like(left)
    source = np.zeros(10, dtype=complex)
    for incoming_index in mode_indices:
        incoming_flat = np.ravel_multi_index(incoming_index, (size,) * 4)
        outgoing_index = tuple(
            (np.asarray(incoming_index) + np.asarray(selected_transfer_index)) % size
        )
        outgoing_flat = np.ravel_multi_index(outgoing_index, (size,) * 4)
        stress = raw_stress(momenta[incoming_index], selected_transfer)
        left[outgoing_flat] += stress * field[incoming_flat]
        source += field[outgoing_flat].conj() * stress * field[incoming_flat]
    for outgoing_index in mode_indices:
        outgoing_flat = np.ravel_multi_index(outgoing_index, (size,) * 4)
        incoming_index = tuple(
            (np.asarray(outgoing_index) - np.asarray(selected_transfer_index)) % size
        )
        incoming_flat = np.ravel_multi_index(incoming_index, (size,) * 4)
        right[outgoing_flat] = (
            raw_stress(momenta[incoming_index], selected_transfer)
            * field[incoming_flat]
        )
    if mutation == "freeze_recoil":
        right[:] = 0.0
    return {
        "modes": mode_count,
        "hermiticity": float(np.max(np.abs(hamiltonian - hamiltonian.conj().T))),
        "antihermiticity": float(np.max(np.abs(generator_matrix + generator_matrix.conj().T))),
        "ward_matrix": float(np.max(np.abs(ward_matrix))),
        "action_variation": float(action_variation),
        "mixed_hessian": float(np.max(np.abs(left - right))),
        "source_norm": float(np.linalg.norm(source)),
        "recoil_norm": float(np.linalg.norm(recoil)),
    }


def tensor_coordinates3(tensor: np.ndarray) -> np.ndarray:
    return np.asarray(
        [np.sum(basis * tensor) for basis in BASIS3],
        dtype=complex,
    )


def coordinate_tensor3(coordinates: np.ndarray) -> np.ndarray:
    return sum(
        (coordinates[index] * basis for index, basis in enumerate(BASIS3)),
        start=np.zeros((3, 3), dtype=complex),
    )


def spatial_operators(
    momentum_vector: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Exact Block78 spatial operators, re-executed without its Block67 import tree."""
    p = np.asarray(momentum_vector, dtype=float)
    kappa_squared = float(p @ p)
    identity = np.eye(3)
    kinetic = np.column_stack(
        tuple(
            tensor_coordinates3(basis - 0.5 * identity * np.trace(basis))
            for basis in BASIS3
        )
    )
    potential = np.column_stack(
        tuple(
            tensor_coordinates3(
                kappa_squared * basis
                + np.outer(p, p) * np.trace(basis)
                - np.outer(p, p @ basis)
                - np.outer(basis @ p, p)
                - identity * (kappa_squared * np.trace(basis) - p @ basis @ p)
            )
            for basis in BASIS3
        )
    )
    hamiltonian = np.asarray(
        [
            np.sum((kappa_squared * identity - np.outer(p, p)) * basis)
            for basis in BASIS3
        ],
        dtype=complex,
    )[None, :]
    momentum = np.column_stack(tuple(-2.0j * (basis @ p) for basis in BASIS3))
    shift = np.column_stack(
        tuple(
            tensor_coordinates3(1.0j * (np.outer(p, vector) + np.outer(vector, p)))
            for vector in np.eye(3)
        )
    )
    return kinetic, potential, hamiltonian, momentum, shift


def schedule_residual(
    spatial_momentum: np.ndarray,
    density: complex,
    density_next: complex,
    incoming: np.ndarray,
    outgoing: np.ndarray,
    stress_coordinates: np.ndarray,
    weights: tuple[float, float],
) -> tuple[float, float]:
    """Exact Block78 two-half-step sourced constraint residual."""
    p = block77.block53.lattice_vector(spatial_momentum)
    derivative = 1.0j * p
    kinetic, potential, hamiltonian, momentum, shift = spatial_operators(p)
    stress = coordinate_tensor3(stress_coordinates)
    source_ward = max(
        abs(density_next - density + derivative @ outgoing),
        float(np.max(np.abs(outgoing - incoming + 1.0j * (stress @ p)))),
    )

    coupling = 1.0
    initial_h = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray(
        (coupling * density,)
    )
    initial_pi = np.linalg.pinv(momentum, rcond=1.0e-12) @ (
        2.0 * coupling * incoming
    )
    delta = 0.5
    lapse0 = 0.17 + 0.03j
    lapse1 = -0.11 + 0.07j
    shift0 = np.asarray((0.2, -0.1, 0.3), dtype=complex)
    shift1 = -shift0

    pi1 = initial_pi + delta * (
        -potential @ initial_h
        + hamiltonian.conj().T[:, 0] * lapse0
        + weights[0] * coupling * stress_coordinates
    )
    h1 = initial_h + delta * (kinetic @ pi1 + shift @ shift0)
    pi2 = pi1 + delta * (
        -potential @ h1
        + hamiltonian.conj().T[:, 0] * lapse1
        + weights[1] * coupling * stress_coordinates
    )
    h2 = h1 + delta * (kinetic @ pi2 + shift @ shift1)

    midpoint_density = density - 0.5 * derivative @ outgoing
    constraint_residual = max(
        float(np.max(np.abs(momentum @ pi1 - 2.0 * coupling * outgoing))),
        float(np.max(np.abs(momentum @ pi2 - 2.0 * coupling * outgoing))),
        abs((hamiltonian @ h1)[0] - coupling * midpoint_density),
        abs((hamiltonian @ h2)[0] - coupling * density_next),
    )
    return float(source_ward), float(constraint_residual)


def adm_interaction_metric(geometry: np.ndarray) -> np.ndarray:
    values = np.asarray(geometry, dtype=complex)
    n0, n1_tail, n1_head = values[:3]
    beta0 = values[3:6]
    beta1 = values[6:9]
    spatial = coordinate_tensor3(values[9:15])
    metric = np.zeros((4, 4), dtype=complex)
    metric[3, 3] = -(n0 + 0.5 * (n1_tail + n1_head))
    metric[3, :3] = beta0 + beta1
    metric[:3, 3] = metric[3, :3]
    metric[:3, :3] = 2.0 * spatial
    return metric


def adm_gradient_certificate() -> dict[str, object]:
    rng = np.random.default_rng(9505)
    error = 0.0
    probes = 0
    for _ in range(64):
        incoming = rng.uniform(-np.pi, np.pi, 4)
        transfer = rng.uniform(-np.pi, np.pi, 4)
        stress = centered_stress(incoming, transfer)
        geometry = rng.normal(size=15)
        observed = np.zeros(15, dtype=complex)
        for index in range(15):
            direction = np.eye(15)[index]
            plus = np.sum(adm_interaction_metric(geometry + direction) * stress)
            minus = np.sum(adm_interaction_metric(geometry - direction) * stress)
            observed[index] = 0.5 * (plus - minus)
        density = stress[3, 3]
        current = stress[3, :3]
        spatial_stress = tensor_coordinates3(stress[:3, :3])
        expected = np.concatenate(
            (
                (-density, -0.5 * density, -0.5 * density),
                2.0 * current,
                2.0 * current,
                2.0 * spatial_stress,
            )
        )
        error = max(error, float(np.max(np.abs(observed - expected))))
        probes += 1
    return {"probes": probes, "error": error}


def cadence_data(
    transfer: np.ndarray,
    stress: np.ndarray,
    mutation: str = "",
) -> tuple[np.ndarray, complex, complex, np.ndarray, np.ndarray, np.ndarray]:
    temporal = float(transfer[3])
    density = complex(stress[3, 3])
    centered_current = np.asarray(stress[3, :3], dtype=complex)
    if mutation == "time_reverse_cadence":
        return (
            np.asarray(transfer[:3], dtype=float),
            density,
            np.exp(-1.0j * temporal) * density,
            -np.exp(0.5j * temporal) * centered_current,
            -np.exp(-0.5j * temporal) * centered_current,
            tensor_coordinates3(stress[:3, :3]),
        )
    return (
        np.asarray(transfer[:3], dtype=float),
        density,
        np.exp(1.0j * temporal) * density,
        np.exp(-0.5j * temporal) * centered_current,
        np.exp(0.5j * temporal) * centered_current,
        tensor_coordinates3(stress[:3, :3]),
    )


def block78_source_bridge_certificate(mutation: str) -> dict[str, object]:
    """Fix the time/current chart against Block78's exact signed source table."""
    modes = 0
    error = 0.0
    for size in range(3, 9):
        for axis in range(3):
            for sign in (-1, 1):
                for neutral_step in (1, 2):
                    neutral_axis = (axis + neutral_step) % 3
                    remaining_axis = (axis + (3 - neutral_step)) % 3
                    for along in range(size):
                        for transverse in range(1, size):
                            for remaining in range(size):
                                integers = np.zeros(3, dtype=int)
                                integers[axis] = along
                                integers[neutral_axis] = transverse
                                integers[remaining_axis] = remaining
                                spatial = 2.0 * np.pi * integers / size
                                temporal_integer = (-sign * along) % size
                                transfer = 2.0 * np.pi * np.concatenate(
                                    (integers, (temporal_integer,))
                                ) / size
                                density = 1.0 - np.exp(-1.0j * spatial[neutral_axis])
                                centered, _raw = block77.signed_source(
                                    transfer,
                                    axis,
                                    sign,
                                    neutral_axis,
                                )
                                stress = sum(
                                    value * basis
                                    for value, basis in zip(centered, block77.BASIS)
                                )
                                observed = cadence_data(transfer, stress, mutation)
                                incoming = np.zeros(3, dtype=complex)
                                outgoing = np.zeros(3, dtype=complex)
                                incoming[axis] = (
                                    sign
                                    * np.exp(0.5j * sign * spatial[axis])
                                    * density
                                )
                                outgoing[axis] = (
                                    sign
                                    * np.exp(-0.5j * sign * spatial[axis])
                                    * density
                                )
                                expected = (
                                    spatial,
                                    density,
                                    np.exp(-1.0j * sign * spatial[axis]) * density,
                                    incoming,
                                    outgoing,
                                    tensor_coordinates3(stress[:3, :3]),
                                )
                                error = max(
                                    error,
                                    max(
                                        float(np.max(np.abs(np.asarray(left) - np.asarray(right))))
                                        for left, right in zip(observed, expected)
                                    ),
                                )
                                modes += 1
    return {"modes": modes, "error": error}


def cadence_certificate(mutation: str) -> dict[str, object]:
    modes = 0
    per_size: dict[int, int] = {}
    shell_modes: dict[int, int] = {}
    on_shell_error = 0.0
    ward_error = 0.0
    front_error = 0.0
    front_failures = 0
    equal_error = 0.0
    equal_failures = 0
    late_error = 0.0
    late_failures = 0
    used_weights = (1.0, 1.0) if mutation == "equal_stress_schedule" else (2.0, 0.0)
    for size in range(3, 9):
        shell: list[tuple[np.ndarray, np.ndarray]] = []
        for integer_mode in np.ndindex((size,) * 4):
            incoming = 2.0 * np.pi * np.asarray(integer_mode, dtype=float) / size
            if abs(scalar_symbol(incoming)) < TOL:
                shell.append((np.asarray(integer_mode, dtype=int), incoming))
        shell_modes[size] = len(shell)
        local_modes = 0
        for left in range(len(shell)):
            incoming_integer, incoming = shell[left]
            for outgoing_integer, outgoing in shell[left + 1 :]:
                transfer_integer = (outgoing_integer - incoming_integer) % size
                if np.all(transfer_integer[:3] == 0):
                    continue
                transfer = 2.0 * np.pi * transfer_integer / size
                stress = centered_stress(incoming, transfer)
                if float(np.max(np.abs(stress))) < 1.0e-9:
                    continue
                data = cadence_data(transfer, stress, mutation)
                source_ward, used = schedule_residual(*data, used_weights)
                _, front = schedule_residual(*data, (2.0, 0.0))
                _, equal = schedule_residual(*data, (1.0, 1.0))
                _, late = schedule_residual(*data, (0.0, 2.0))
                on_shell_error = max(
                    on_shell_error,
                    abs(scalar_symbol(incoming)),
                    abs(scalar_symbol(outgoing)),
                )
                ward_error = max(ward_error, source_ward)
                front_error = max(front_error, used)
                front_failures += int(used > TOL)
                equal_error = max(equal_error, equal)
                equal_failures += int(equal > TOL)
                late_error = max(late_error, late)
                late_failures += int(late > TOL)
                modes += 1
                local_modes += 1
        per_size[size] = local_modes
    return {
        "modes": modes,
        "per_size": per_size,
        "shell_modes": shell_modes,
        "on_shell_error": on_shell_error,
        "ward_error": ward_error,
        "front_error": front_error,
        "front_failures": front_failures,
        "equal_error": equal_error,
        "equal_failures": equal_failures,
        "late_error": late_error,
        "late_failures": late_failures,
    }


def zero_mode_certificate(mutation: str) -> dict[str, object]:
    incoming = np.asarray((np.pi / 2.0, 0.0, 0.0, np.pi / 2.0))
    transfer = np.zeros(4)
    stress = centered_stress(incoming, transfer)
    density = float(stress[3, 3].real)
    _, _, hamiltonian, _, _ = spatial_operators(np.zeros(3))
    target = np.asarray((density,))
    response = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ target
    residual = float(np.max(np.abs(hamiltonian @ response - target)))
    note = flat(NOTE_PATH)
    scoped = all(
        phrase in note
        for phrase in (
            "positive compact zero mode remains open",
            "open boundary, compensating background, reservoir, or nonlinear completion",
            "not a positive compact gravity solution",
        )
    )
    if mutation == "hide_zero_mode":
        scoped = False
    return {
        "density": density,
        "shell": abs(scalar_symbol(incoming)),
        "hamiltonian_rank": int(np.linalg.matrix_rank(hamiltonian, tol=1.0e-12)),
        "residual": residual,
        "ward": float(np.max(np.abs(block77.raw_gauge(-transfer).T @ raw_stress(incoming, transfer)))),
        "scoped": scoped,
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = flat(NOTE_PATH)
    result = {
        "first_order": "first-order total graph--matter ward identity" in note,
        "nonlinear_open": "ward completion is not executed" in note,
        "stage_open": "front-loaded matter--gravity stage/work map remains open" in note,
        "record_open": "record compiler and selected physical law remain open" in note,
        "zero_score": all(
            phrase in note
            for phrase in (
                "zero obligation retirement",
                "no toe percentage moves",
                "retained-positive end-to-end theory count remains zero",
            )
        ),
    }
    if mutation == "claim_nonlinear_ward":
        result["nonlinear_open"] = False
    return result


def no_go_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    headings = all(f"n{index}" in note for index in range(1, 9))
    routes = all(
        phrase in note
        for phrase in (
            "link-centred half-density lattice scalar",
            "component-staggered oriented particle link",
            "compact same-carrier continuous pullback",
            "constrained adm source cadence",
            "compact periodic linear zero-mode inversion",
        )
    )
    if mutation == "weaken_routes":
        routes = False
    zero_score = all(
        phrase in note
        for phrase in (
            "zero obligation retirement",
            "no toe percentage moves",
            "retained-positive end-to-end theory count remains zero",
        )
    )
    if mutation == "claim_toe_progress":
        zero_score = False
    return {
        "headings": headings,
        "routes": routes,
        "attempted": note.count("attempted"),
        "residual_lines": all(
            marker in note
            for marker in (
                "note_2026-08-14.md:333",
                "note_2026-08-14.md:209",
                "note_2026-08-14.md:380",
                "note_2026-08-14.md:145",
                "note_2026-08-14.md:341",
                "note_2026-08-14.md:279",
            )
        ),
        "single_wall": "is only the first-order common-action/ward wall" in note,
        "demoted": "fail — partial-narrowing" in note
        and "broad no-go premature" in note,
        "steelman": "strongest steelman" in note,
        "echo": "cross-cycle echo" in note,
        "zero_score": zero_score,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "fake_locality",
            "break_hermiticity",
            "break_cochain",
            "freeze_recoil",
            "equal_stress_schedule",
            "time_reverse_cadence",
            "hide_zero_mode",
            "claim_nonlinear_ward",
            "weaken_routes",
            "claim_toe_progress",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-axiom-and-frozen-gravity-parent-authority",
        "origin/main, axioms, Blocks53/77/78/83/93, and every loaded runner are content-bound",
        authority["origin_main"] == CURRENT_AXIOM_COMMIT
        and authority["axiom"] == authority["expected_axiom"]
        and authority["block77"] == (BLOCK77_NOTE_BLOB, BLOCK77_RUNNER_BLOB)
        and authority["block78"] == (BLOCK78_NOTE_BLOB, BLOCK78_RUNNER_BLOB)
        and authority["block83"] == (BLOCK83_NOTE_BLOB, BLOCK83_RUNNER_BLOB)
        and authority["block93"] == (BLOCK93_NOTE_BLOB, BLOCK93_RUNNER_BLOB)
        and not authority["mismatches"]
        and not authority["missing"]
        and not authority["loaded_missing"],
        f"origin/main={str(authority['origin_main'])[:10]}; frozen/loaded mismatches={len(authority['mismatches'])}/{len(authority['loaded_missing'])}",
    )

    locality = locality_certificate(mutation)
    checks.check(
        "B-finite-Laurent-scalar-generator-and-raw-stress",
        "the nearest-neighbour scalar, link generator, and raw stress have fixed finite support without inverse incidence",
        locality["scalar_shape"] == (9, 1, 1, 0, 0, 1)
        and locality["generator_shape"] == (8, 1, 1, 1, 1, 2)
        and locality["stress_shape"] == (33, 2, 2, 1, 2, 4)
        and locality["scalar_terms"] == 9
        and locality["generator_terms"] == 8
        and locality["stress_terms"] == 36
        and locality["scalar_error"] < TOL
        and locality["generator_error"] < TOL
        and locality["stress_error"] < TOL
        and locality["proof_valid"],
        f"supports M/D/T={locality['scalar_shape'][0]}/{locality['generator_shape'][0]}/{locality['stress_shape'][0]}; Laurent errors={locality['scalar_error']:.1e}/{locality['generator_error']:.1e}/{locality['stress_error']:.1e}",
    )

    vertex = vertex_certificate(mutation)
    checks.check(
        "C-Hermitian-periodic-link-centred-matter-action-data",
        "the raw vertex is Hermitian, the local generator is anti-Hermitian, periodic, and physically nonzero",
        vertex["probes"] == 96
        and vertex["hermiticity"] < TOL
        and vertex["antihermiticity"] < TOL
        and vertex["periodicity"] < TOL
        and vertex["position_generator_error"] < TOL
        and vertex["action_pairing_error"] < TOL
        and vertex["constant_norm"] > 0.1,
        f"probes={vertex['probes']}; Hermitian/anti/periodic={vertex['hermiticity']:.1e}/{vertex['antihermiticity']:.1e}/{vertex['periodicity']:.1e}; position/pairing={vertex['position_generator_error']:.1e}/{vertex['action_pairing_error']:.1e}; D0 norm={vertex['constant_norm']:.3f}",
    )

    ward = ward_covariance_certificate(mutation)
    checks.check(
        "D-off-shell-first-order-total-Ward-cochain-and-covariance",
        "the actual raw Block77 gauge map plus the scalar commutator cancels exactly in all tested frames",
        ward["probes"] == 96
        and ward["difference_error"] < TOL
        and ward["cochain_error"] < TOL
        and ward["rotation_error"] < TOL
        and ward["generator_rotation_error"] < TOL
        and ward["reflection_error"] < TOL
        and ward["generator_reflection_error"] < TOL
        and ward["level_set_error"] < TOL
        and ward["massive_spectator_error"] < TOL
        and ward["frames"] == 24,
        f"difference/cochain={ward['difference_error']:.1e}/{ward['cochain_error']:.1e}; tensor/vector/cubic/time={ward['rotation_error']:.1e}/{ward['generator_rotation_error']:.1e}/{ward['frames']}/{max(ward['reflection_error'], ward['generator_reflection_error']):.1e}",
    )

    action = joint_action_certificate(mutation)
    adm = adm_gradient_certificate()
    checks.check(
        "E-one-Hermitian-action-supplies-source-recoil-and-mixed-Hessians",
        "one finite scalar action gives the source, reciprocal matter equation, and localized action-level Ward identity",
        action["modes"] == 81
        and action["hermiticity"] < TOL
        and action["antihermiticity"] < TOL
        and action["ward_matrix"] < TOL
        and action["action_variation"] < TOL
        and action["mixed_hessian"] < TOL
        and action["source_norm"] > 0.1
        and action["recoil_norm"] > 0.1
        and adm["probes"] == 64
        and adm["error"] < TOL,
        f"modes={action['modes']}; H/D/Ward/action={action['hermiticity']:.1e}/{action['antihermiticity']:.1e}/{action['ward_matrix']:.1e}/{action['action_variation']:.1e}; source/recoil/ADM={action['source_norm']:.2f}/{action['recoil_norm']:.2f}/{adm['error']:.1e}",
    )

    cadence = cadence_certificate(mutation)
    source_bridge = block78_source_bridge_certificate(mutation)
    checks.check(
        "F-on-shell-scalar-stress-propagates-all-Block78-constraints",
        "all exact massless-shell scalar transfers pass the source Ward and front-loaded four-constraint cadence",
        cadence["modes"] == 6354
        and cadence["shell_modes"] == {3: 13, 4: 28, 5: 25, 6: 68, 7: 37, 8: 76}
        and cadence["per_size"] == {3: 66, 4: 360, 5: 276, 6: 2226, 7: 630, 8: 2796}
        and cadence["on_shell_error"] < TOL
        and cadence["ward_error"] < TOL
        and cadence["front_failures"] == 0
        and cadence["front_error"] < TOL
        and cadence["equal_failures"] == 4249
        and cadence["late_failures"] == 4249
        and cadence["equal_error"] > 1.9
        and cadence["late_error"] > 3.9
        and source_bridge["modes"] == 13056
        and source_bridge["error"] < TOL,
        f"null modes={cadence['shell_modes']}; transfers={cadence['per_size']}; Ward/front={cadence['ward_error']:.1e}/{cadence['front_error']:.1e}; parent bridge={source_bridge['modes']}/{source_bridge['error']:.1e}; equal/late failures={cadence['equal_failures']}/{cadence['late_failures']}",
    )

    zero = zero_mode_certificate(mutation)
    checks.check(
        "G-positive-scalar-zero-mode-and-compact-gravity-boundary",
        "the action has positive mean density, while the compact linear Hamiltonian zero mode remains unsolved and explicit",
        zero["density"] > 0.9
        and zero["shell"] < TOL
        and zero["hamiltonian_rank"] == 0
        and zero["residual"] > 0.9
        and zero["ward"] < TOL
        and zero["scoped"],
        f"density/shell/rank/residual={zero['density']:.3f}/{zero['shell']:.1e}/{zero['hamiltonian_rank']}/{zero['residual']:.3f}; q0 Ward={zero['ward']:.1e}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "H-first-order-stage-Record-law-and-retention-scope",
        "the exact first-order result does not silently claim nonlinear, joint-stage, Record, law, or retention closure",
        all(scope.values()),
    )

    no_go = no_go_certificate(mutation)
    checks.check(
        "I-no-go-discipline-demotion-and-TOE-scope",
        "N1-N8 demotes every broad negative, preserves live routes, and assigns zero TOE credit",
        no_go["headings"]
        and no_go["routes"]
        and no_go["attempted"] >= 5
        and no_go["residual_lines"]
        and no_go["single_wall"]
        and no_go["demoted"]
        and no_go["steelman"]
        and no_go["echo"]
        and no_go["zero_score"],
        f"ATTEMPTED markers={no_go['attempted']}; routes/headings={no_go['routes']}/{no_go['headings']}",
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; Block93 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: checked — one Lorentzian half-density scalar symbol, four link generators, ten raw tensor coordinates, and exact source/recoil mixed derivatives"
    )
    print(
        "per_site: checked — nearest-neighbour scalar action, eight generator monomials, 33 joint stress support points, and the raw staggered tensor/vector placement"
    )
    print(
        "per_mode: checked — 96 generic Ward probes, all 24 proper-cubic frames, time reflection, and 6,354 nontrivial exact massless-shell L=3..8 transfers"
    )
    print(
        "per_block: checked — first-order field-plus-matter Ward cochain, one 81-mode Hermitian joint-action census, reciprocal recoil, mixed Hessians, and Block78 front-loaded constraint cadence"
    )
    print(
        "lattice_wide: checked and not executed — positive compact zero-mode completion, order-h phi^2 Ward terms, exact joint stage/work map, nonlinear gravity, Record compilation, selected law, and audit retention remain open"
    )
    print(
        "RESULT: a finite incidence half-density scalar executes the actual Block77 first-order total Ward identity and supplies on-shell sources that pass the Block78 cadence"
    )
    print(
        "PORTFOLIO: next test the common matter-gravity stage/work map and positive-boundary or nonlinear zero-mode completion; do not return to generic carrier counting"
    )
    print(
        "SCOPE: no nonlinear gravity completion, selected physical matter law, Record compiler, axiom amendment, audit verdict, obligation retirement, retained end-to-end theory, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
