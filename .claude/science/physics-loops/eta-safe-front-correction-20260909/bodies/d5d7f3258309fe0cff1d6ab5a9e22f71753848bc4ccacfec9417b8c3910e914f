#!/usr/bin/env python3
"""Block 78: full sourced linear ADM cadence on the incidence carrier.

The runner extends Block 77's staggered Einstein operator through the positive
Block 53 depth-two canonical update.  It derives the unique source-kick
placement in the supplied kick-first order, propagates all four Einstein
constraints, and decodes Block 67's literal Q -> O_s hop as the incoming
source segment.  Physical Record typing, coupling/debit, boundary data,
nonlinear completion, selection, and retention remain outside the result.
"""

from __future__ import annotations

from itertools import product
import os
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.linalg import block_diag, null_space


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_"
    "CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
BLOCK53_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_"
    "UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK67_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_"
    "SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
BLOCK77_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_"
    "CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11 as block53  # noqa: E402
import admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13 as block67  # noqa: E402
import admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14 as block77  # noqa: E402


BASIS = block53.SYMMETRIC_BASIS
IDENTITY6 = np.eye(6)
ZERO6 = np.zeros((6, 6))
TOL = 1.0e-10
CURRENT_AXIOM_COMMIT = "b02f50a9cfb8ca57c2dbe7026d06487947d22331"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
AXIOM_REPO_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"


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


def git_blob_flat(blob: str) -> str:
    result = subprocess.run(
        ("git", "cat-file", "blob", blob),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return " ".join(result.stdout.lower().split())


def git_commit_path_blob(commit: str, path: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def tensor_coordinates(tensor: np.ndarray) -> np.ndarray:
    return np.asarray([np.sum(basis * tensor) for basis in BASIS], dtype=complex)


def coordinate_tensor(coordinates: np.ndarray) -> np.ndarray:
    return sum(
        (coordinates[index] * basis for index, basis in enumerate(BASIS)),
        start=np.zeros((3, 3), dtype=complex),
    )


def spatial_operators(
    momentum_vector: np.ndarray,
    mutation: str = "",
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    p = np.asarray(momentum_vector, dtype=float)
    kappa_squared = float(p @ p)
    identity = np.eye(3)

    kinetic = np.column_stack(
        tuple(
            tensor_coordinates(basis - 0.5 * identity * np.trace(basis))
            for basis in BASIS
        )
    )
    potential = np.column_stack(
        tuple(
            tensor_coordinates(
                kappa_squared * basis
                + np.outer(p, p) * np.trace(basis)
                - np.outer(p, p @ basis)
                - np.outer(basis @ p, p)
                - identity
                * (kappa_squared * np.trace(basis) - p @ basis @ p)
            )
            for basis in BASIS
        )
    )
    if mutation == "wrong_potential":
        potential = kappa_squared * np.eye(6)

    hamiltonian = np.asarray(
        [
            np.sum((kappa_squared * identity - np.outer(p, p)) * basis)
            for basis in BASIS
        ],
        dtype=complex,
    )[None, :]
    momentum = np.column_stack(tuple(-2.0j * (basis @ p) for basis in BASIS))
    shift = np.column_stack(
        tuple(
            tensor_coordinates(
                1.0j * (np.outer(p, vector) + np.outer(vector, p))
            )
            for vector in np.eye(3)
        )
    )
    return kinetic, potential, hamiltonian, momentum, shift


def tensor_rotation(rotation: np.ndarray) -> np.ndarray:
    return np.column_stack(
        tuple(
            tensor_coordinates(rotation @ basis @ rotation.T) for basis in BASIS
        )
    ).real


def operator_identity_certificate(
    mutation: str,
) -> tuple[int, float, float, set[int], set[int], set[int]]:
    modes = 0
    identity_error = 0.0
    covariance_error = 0.0
    hamiltonian_ranks: set[int] = set()
    momentum_ranks: set[int] = set()
    tt_ranks: set[int] = set()
    for size in range(3, 13):
        for integer_mode in np.ndindex((size,) * 3):
            centered = np.asarray(integer_mode, dtype=int)
            if np.all(centered == 0):
                continue
            k = 2.0 * np.pi * centered / size
            p = block53.lattice_vector(k)
            kinetic, potential, hamiltonian, momentum, shift = spatial_operators(
                p, mutation
            )
            derivative = 1.0j * p
            residuals = (
                potential @ shift,
                momentum @ potential,
                hamiltonian @ shift,
                momentum @ hamiltonian.conj().T,
                hamiltonian @ kinetic
                + 0.5 * (derivative[None, :] @ momentum),
                potential - potential.T,
                kinetic - kinetic.T,
            )
            identity_error = max(
                identity_error,
                max(float(np.max(np.abs(residual))) for residual in residuals),
            )
            hamiltonian_ranks.add(int(np.linalg.matrix_rank(hamiltonian, TOL)))
            momentum_ranks.add(int(np.linalg.matrix_rank(momentum, TOL)))
            tt_ranks.add(int(np.linalg.matrix_rank(block53.tt_constraint(k), TOL)))
            modes += 1

    probes = (
        np.asarray((0.31, -0.77, 1.12)),
        np.asarray((np.pi, -0.43, np.pi)),
    )
    for rotation in block53.proper_cubic_rotations():
        representation = tensor_rotation(rotation)
        for k in probes:
            p = block53.lattice_vector(k)
            rotated_p = rotation @ p
            g0, p0, c0, m0, s0 = spatial_operators(p)
            g1, p1, c1, m1, s1 = spatial_operators(rotated_p)
            covariance_error = max(
                covariance_error,
                float(np.max(np.abs(p1 - representation @ p0 @ representation.T))),
                float(np.max(np.abs(g1 - representation @ g0 @ representation.T))),
                float(np.max(np.abs(c1 @ representation - c0))),
                float(np.max(np.abs(m1 @ representation - rotation @ m0))),
                float(np.max(np.abs(s1 @ rotation - representation @ s0))),
            )
    return (
        modes,
        identity_error,
        covariance_error,
        hamiltonian_ranks,
        momentum_ranks,
        tt_ranks,
    )


def block77_adm_bridge_certificate(
    mutation: str,
) -> tuple[int, float, np.ndarray]:
    """Bind the canonical variables to Block 77's actual 10x10 symbol."""
    cases = 0
    error = 0.0
    canonical_scale_numerator = 0.0j
    canonical_scale_denominator = 0.0
    momentum_scale_numerator = 0.0j
    momentum_scale_denominator = 0.0
    spatial_slots = list(block77.SPATIAL_SLOTS)
    shift_slots = list(block77.SHIFT_SLOTS)
    temporal_angles = (0.37, np.pi)
    for size in range(3, 13):
        for integer_mode in np.ndindex((size,) * 3):
            if all(value == 0 for value in integer_mode):
                continue
            k = 2.0 * np.pi * np.asarray(integer_mode, dtype=float) / size
            p = block53.lattice_vector(k)
            kinetic, potential, hamiltonian, momentum, shift = spatial_operators(p)
            inverse_kinetic = np.linalg.inv(kinetic)
            for temporal_angle in temporal_angles:
                temporal_momentum = float(2.0 * np.sin(temporal_angle / 2.0))
                symbol = block77.centered_operator(
                    np.concatenate((p, (temporal_momentum,)))
                )
                if mutation == "break_block77_bridge":
                    symbol = 2.0 * symbol
                canonical_target = (
                    potential - temporal_momentum**2 * inverse_kinetic
                )
                canonical_scale_numerator += np.vdot(
                    canonical_target,
                    symbol[np.ix_(spatial_slots, spatial_slots)],
                )
                canonical_scale_denominator += float(
                    np.vdot(canonical_target, canonical_target).real
                )
                canonical_scale_numerator += np.vdot(
                    hamiltonian[0], symbol[0, spatial_slots]
                )
                canonical_scale_denominator += float(
                    np.vdot(hamiltonian[0], hamiltonian[0]).real
                )
                momentum_target = (
                    momentum
                    @ inverse_kinetic
                    @ (1.0j * temporal_momentum * IDENTITY6)
                )
                momentum_scale_numerator += np.vdot(
                    momentum_target,
                    symbol[np.ix_(shift_slots, spatial_slots)],
                )
                momentum_scale_denominator += float(
                    np.vdot(momentum_target, momentum_target).real
                )
                residuals = (
                    symbol[np.ix_(spatial_slots, spatial_slots)]
                    - 0.5
                    * canonical_target,
                    symbol[0, spatial_slots] - 0.5 * hamiltonian[0],
                    symbol[spatial_slots, 0]
                    - 0.5 * hamiltonian.conj().T[:, 0],
                    2.0
                    * np.sqrt(2.0)
                    * symbol[np.ix_(spatial_slots, shift_slots)]
                    + 1.0j
                    * temporal_momentum
                    * inverse_kinetic
                    @ shift,
                    symbol[np.ix_(shift_slots, spatial_slots)]
                    - momentum_target / (2.0 * np.sqrt(2.0)),
                    symbol[np.ix_(shift_slots, shift_slots)]
                    + momentum @ inverse_kinetic @ shift / 4.0,
                    symbol[shift_slots, 0],
                )
                error = max(
                    error,
                    max(float(np.max(np.abs(residual))) for residual in residuals),
                )
                cases += 1

    unit_shift_source = np.zeros((4, 4), dtype=float)
    unit_shift_source[0, 3] = 1.0
    unit_shift_source[3, 0] = 1.0
    shift_coordinate_scale = float(
        np.sum(block77.BASIS[block77.SHIFT_SLOTS[0]] * unit_shift_source)
    )
    canonical_scale = float(
        (canonical_scale_numerator / canonical_scale_denominator).real
    )
    momentum_output_scale = float(
        (momentum_scale_numerator / momentum_scale_denominator).real
    )
    covariant_source_coefficient_over_g = canonical_scale
    constraint_factor = covariant_source_coefficient_over_g / canonical_scale
    momentum_factor = (
        covariant_source_coefficient_over_g
        * shift_coordinate_scale
        / momentum_output_scale
    )
    total_stress_impulse = covariant_source_coefficient_over_g / canonical_scale
    kick_coefficient = total_stress_impulse / 0.5
    normalizations = np.asarray(
        (
            constraint_factor,
            momentum_factor,
            kick_coefficient,
            total_stress_impulse,
        )
    )
    return cases, error, normalizations


def placement(momentum: np.ndarray, co_locate: bool = False) -> np.ndarray:
    if co_locate:
        return np.eye(6, dtype=complex)
    k = np.asarray(momentum, dtype=float)
    return np.diag(
        (
            1.0,
            1.0,
            1.0,
            np.exp(0.5j * (k[0] + k[1])),
            np.exp(0.5j * (k[0] + k[2])),
            np.exp(0.5j * (k[1] + k[2])),
        )
    )


def homogeneous_macro(
    kinetic: np.ndarray,
    potential: np.ndarray,
    depth: int = 2,
) -> np.ndarray:
    delta = 1.0 / depth
    kick = np.block([[IDENTITY6, ZERO6], [-delta * potential, IDENTITY6]])
    drift = np.block([[IDENTITY6, delta * kinetic], [ZERO6, IDENTITY6]])
    return np.linalg.matrix_power(drift @ kick, depth)


def support_shape(symbols: np.ndarray) -> tuple[int, int, int]:
    size = symbols.shape[0]
    kernel = np.fft.fftn(symbols, axes=(0, 1, 2)) / size**3
    maximum = np.max(np.abs(kernel), axis=(-2, -1))
    support = np.argwhere(maximum > 1.0e-10)
    shifts = tuple(
        np.where(index <= size // 2, index, index - size) for index in support
    )
    return (
        len(support),
        max(int(np.max(np.abs(shift))) for shift in shifts),
        max(int(np.sum(np.abs(shift))) for shift in shifts),
    )


def locality_certificate(
    mutation: str,
) -> tuple[tuple[int, int, int], tuple[int, int, int], float, float, float]:
    size = 7
    potential_symbols = np.zeros((size, size, size, 6, 6), dtype=complex)
    macro_symbols = np.zeros((size, size, size, 12, 12), dtype=complex)
    for integer_mode in np.ndindex((size,) * 3):
        k = 2.0 * np.pi * np.asarray(integer_mode) / size
        p = block53.lattice_vector(k)
        kinetic, potential, _, _, _ = spatial_operators(p)
        field_placement = placement(k)
        potential_symbols[integer_mode] = (
            field_placement @ potential @ field_placement.conj().T
        )
        macro_placement = placement(k, mutation == "co_locate_macro")
        state_placement = block_diag(macro_placement, macro_placement)
        macro_symbols[integer_mode] = (
            state_placement
            @ homogeneous_macro(kinetic, potential)
            @ state_placement.conj().T
        )

    probe = np.asarray((0.31, -0.47, 0.82))
    p = block53.lattice_vector(probe)
    kinetic, potential, _, _, _ = spatial_operators(p)
    base_u = placement(probe)
    base_potential = base_u @ potential @ base_u.conj().T
    base_state_u = block_diag(base_u, base_u)
    base_macro = (
        base_state_u
        @ homogeneous_macro(kinetic, potential)
        @ base_state_u.conj().T
    )
    periodicity = 0.0
    for axis in range(3):
        shifted = probe.copy()
        shifted[axis] += 2.0 * np.pi
        shifted_p = block53.lattice_vector(shifted)
        shifted_g, shifted_v, _, _, _ = spatial_operators(shifted_p)
        shifted_u = placement(shifted)
        shifted_state_u = block_diag(shifted_u, shifted_u)
        periodicity = max(
            periodicity,
            float(
                np.max(
                    np.abs(
                        shifted_u @ shifted_v @ shifted_u.conj().T
                        - base_potential
                    )
                )
            ),
            float(
                np.max(
                    np.abs(
                        shifted_state_u
                        @ homogeneous_macro(shifted_g, shifted_v)
                        @ shifted_state_u.conj().T
                        - base_macro
                    )
                )
            ),
        )
    hermiticity = float(np.max(np.abs(base_potential - base_potential.conj().T)))
    raw_covariance = 0.0
    covariance_probes = (
        probe,
        np.asarray((np.pi, -0.43, 0.71)),
    )
    for rotation in block53.proper_cubic_rotations():
        representation = tensor_rotation(rotation)
        state_representation = block_diag(representation, representation)
        for k in covariance_probes:
            rotated_k = rotation @ k
            p0 = block53.lattice_vector(k)
            p1 = block53.lattice_vector(rotated_k)
            g0, v0, _, _, _ = spatial_operators(p0)
            g1, v1, _, _, _ = spatial_operators(p1)

            u0 = placement(k)
            u1 = placement(rotated_k)
            raw_tensor = u1 @ representation @ u0.conj().T
            if mutation == "break_raw_covariance":
                raw_tensor = representation.astype(complex)
            raw_v0 = u0 @ v0 @ u0.conj().T
            raw_v1 = u1 @ v1 @ u1.conj().T
            raw_covariance = max(
                raw_covariance,
                float(
                    np.max(
                        np.abs(raw_v1 - raw_tensor @ raw_v0 @ raw_tensor.conj().T)
                    )
                ),
            )

            macro_co_located = mutation == "co_locate_macro"
            um0 = placement(k, macro_co_located)
            um1 = placement(rotated_k, macro_co_located)
            state_u0 = block_diag(um0, um0)
            state_u1 = block_diag(um1, um1)
            raw_state_tensor = (
                state_u1 @ state_representation @ state_u0.conj().T
            )
            raw_macro0 = (
                state_u0
                @ homogeneous_macro(g0, v0)
                @ state_u0.conj().T
            )
            raw_macro1 = (
                state_u1
                @ homogeneous_macro(g1, v1)
                @ state_u1.conj().T
            )
            raw_covariance = max(
                raw_covariance,
                float(
                    np.max(
                        np.abs(
                            raw_macro1
                            - raw_state_tensor
                            @ raw_macro0
                            @ raw_state_tensor.conj().T
                        )
                    )
                ),
            )
    return (
        support_shape(potential_symbols),
        support_shape(macro_symbols),
        periodicity,
        hermiticity,
        raw_covariance,
    )


def tt_stability_certificate(mutation: str) -> tuple[int, float, float, int, float, float]:
    modes = 0
    tt_error = 0.0
    symplectic_error = 0.0
    stable = 0
    minimum_shadow = np.inf
    modulus_error = 0.0
    symplectic_form = np.block([[ZERO6, IDENTITY6], [-IDENTITY6, ZERO6]])
    depth = 1 if mutation == "depth_one" else 2
    for size in range(3, 13):
        for integer_mode in np.ndindex((size,) * 3):
            centered = np.asarray(integer_mode, dtype=int)
            if np.all(centered == 0):
                continue
            k = 2.0 * np.pi * centered / size
            p = block53.lattice_vector(k)
            kappa_squared = float(p @ p)
            kinetic, potential, _, _, _ = spatial_operators(p)
            tt = null_space(block53.tt_constraint(k), rcond=1.0e-11)
            tt_error = max(
                tt_error,
                float(
                    np.max(
                        np.abs(tt.T @ potential @ tt - kappa_squared * np.eye(2))
                    )
                ),
                float(np.max(np.abs(tt.T @ kinetic @ tt - np.eye(2)))),
            )
            macro = homogeneous_macro(kinetic, potential, depth)
            symplectic_error = max(
                symplectic_error,
                float(
                    np.max(
                        np.abs(macro.T @ symplectic_form @ macro - symplectic_form)
                    )
                ),
            )
            state_tt = block_diag(tt, tt)
            physical_macro = state_tt.T @ macro @ state_tt
            eigenvalues = np.linalg.eigvals(physical_macro)
            current_modulus = float(np.max(np.abs(np.abs(eigenvalues) - 1.0)))
            modulus_error = max(modulus_error, current_modulus)
            _, _, shadow, _, _ = block53.split_substep(kappa_squared, depth)
            current_shadow = float(np.min(np.linalg.eigvalsh(shadow)))
            minimum_shadow = min(minimum_shadow, current_shadow)
            stable += int(current_modulus < TOL and current_shadow > TOL)
            modes += 1
    return modes, tt_error, symplectic_error, stable, minimum_shadow, modulus_error


def source_mode_data(
    size: int,
    axis: int,
    sign: int,
    neutral_step: int,
    along: int,
    transverse: int,
    remaining: int,
) -> tuple[np.ndarray, complex, complex, np.ndarray, np.ndarray, np.ndarray]:
    neutral_axis = (axis + neutral_step) % 3
    remaining_axis = (axis + (3 - neutral_step)) % 3
    integers = np.zeros(3, dtype=int)
    integers[axis] = along
    integers[neutral_axis] = transverse
    integers[remaining_axis] = remaining
    k = 2.0 * np.pi * integers / size
    density = 1.0 - np.exp(-1.0j * k[neutral_axis])
    density_next = np.exp(-1.0j * sign * k[axis]) * density
    incoming = np.zeros(3, dtype=complex)
    outgoing = np.zeros(3, dtype=complex)
    incoming[axis] = sign * np.exp(0.5j * sign * k[axis]) * density
    outgoing[axis] = sign * np.exp(-0.5j * sign * k[axis]) * density
    stress = np.zeros((3, 3), dtype=complex)
    stress[axis, axis] = density
    return k, density, density_next, incoming, outgoing, tensor_coordinates(stress)


def schedule_residual(
    k: np.ndarray,
    density: complex,
    density_next: complex,
    incoming: np.ndarray,
    outgoing: np.ndarray,
    stress_coordinates: np.ndarray,
    weights: tuple[float, float],
    omit_stress: bool = False,
    wrong_momentum_factor: bool = False,
) -> tuple[float, float]:
    p = block53.lattice_vector(k)
    derivative = 1.0j * p
    kinetic, potential, hamiltonian, momentum, shift = spatial_operators(p)
    stress = coordinate_tensor(stress_coordinates)
    source_ward = max(
        abs(density_next - density + derivative @ outgoing),
        float(
            np.max(
                np.abs(outgoing - incoming + 1.0j * (stress @ p))
            )
        ),
    )

    coupling = 1.0
    initial_h = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray(
        (coupling * density,)
    )
    momentum_factor = 1.0 if wrong_momentum_factor else 2.0
    initial_pi = np.linalg.pinv(momentum, rcond=1.0e-12) @ (
        momentum_factor * coupling * incoming
    )
    used_stress = np.zeros(6, dtype=complex) if omit_stress else stress_coordinates
    delta = 0.5
    lapse0 = 0.17 + 0.03j
    lapse1 = -0.11 + 0.07j
    shift0 = np.asarray((0.2, -0.1, 0.3), dtype=complex)
    shift1 = -shift0

    pi1 = initial_pi + delta * (
        -potential @ initial_h
        + hamiltonian.conj().T[:, 0] * lapse0
        + weights[0] * coupling * used_stress
    )
    h1 = initial_h + delta * (kinetic @ pi1 + shift @ shift0)
    pi2 = pi1 + delta * (
        -potential @ h1
        + hamiltonian.conj().T[:, 0] * lapse1
        + weights[1] * coupling * used_stress
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


def source_schedule_certificate(mutation: str) -> tuple[int, float, int, float, int, float, int, float]:
    modes = 0
    source_ward_error = 0.0
    baseline_failures = 0
    baseline_error = 0.0
    equal_failures = 0
    equal_error = 0.0
    late_failures = 0
    late_error = 0.0
    baseline_weights = (2.0, 0.0)
    if mutation == "equal_source_split":
        baseline_weights = (1.0, 1.0)
    elif mutation == "late_source":
        baseline_weights = (0.0, 2.0)
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
                                ward, residual = schedule_residual(
                                    *data,
                                    baseline_weights,
                                    omit_stress=mutation == "omit_spatial_stress",
                                    wrong_momentum_factor=mutation == "wrong_momentum_factor",
                                )
                                _, equal = schedule_residual(*data, (1.0, 1.0))
                                _, late = schedule_residual(*data, (0.0, 2.0))
                                source_ward_error = max(source_ward_error, ward)
                                baseline_error = max(baseline_error, residual)
                                equal_error = max(equal_error, equal)
                                late_error = max(late_error, late)
                                baseline_failures += int(residual > TOL)
                                equal_failures += int(equal > TOL)
                                late_failures += int(late > TOL)
                                modes += 1
    if mutation == "accept_equal_split":
        equal_failures = 0
    return (
        modes,
        source_ward_error,
        baseline_failures,
        baseline_error,
        equal_failures,
        equal_error,
        late_failures,
        late_error,
    )


def add_complex_equation(
    rows: list[list[float]],
    targets: list[float],
    coefficients: tuple[complex, complex],
    target: complex,
) -> None:
    if max(abs(value) for value in coefficients) < 1.0e-12:
        return
    rows.append([float(value.real) for value in coefficients])
    targets.append(float(target.real))
    rows.append([float(value.imag) for value in coefficients])
    targets.append(float(target.imag))


def weight_uniqueness_certificate(mutation: str) -> tuple[int, int, np.ndarray, float]:
    rows: list[list[float]] = []
    targets: list[float] = []
    delta = 0.5
    samples = 0
    for size in (3, 4):
        for axis in range(3):
            for sign in (-1, 1):
                for neutral_step in (1, 2):
                    for along in range(size):
                        for transverse in range(1, size):
                            data = source_mode_data(
                                size, axis, sign, neutral_step, along, transverse, 0
                            )
                            k, _, _, incoming, outgoing, stress_coordinates = data
                            p = block53.lattice_vector(k)
                            derivative = 1.0j * p
                            _, _, _, momentum, _ = spatial_operators(p)
                            stress_momentum = momentum @ stress_coordinates
                            difference = outgoing - incoming
                            if mutation != "drop_midpoint_constraint":
                                add_complex_equation(
                                    rows,
                                    targets,
                                    (
                                        0.5
                                        * delta**2
                                        * (derivative @ stress_momentum),
                                        0.0j,
                                    ),
                                    delta * (derivative @ difference),
                                )
                            for component in range(3):
                                add_complex_equation(
                                    rows,
                                    targets,
                                    (
                                        delta * stress_momentum[component],
                                        delta * stress_momentum[component],
                                    ),
                                    2.0 * difference[component],
                                )
                            samples += 1
    matrix = np.asarray(rows, dtype=float)
    target = np.asarray(targets, dtype=float)
    weights, _, rank, _ = np.linalg.lstsq(matrix, target, rcond=1.0e-12)
    residual = float(np.max(np.abs(matrix @ weights - target)))
    return samples, int(rank), weights, residual


def cycle713_incoming_certificate(mutation: str) -> tuple[int, int, int, set[tuple[int, int, int]]]:
    cases = 0
    failures = 0
    induction_checks = 0
    directions: set[tuple[int, int, int]] = set()
    for rotation in block67.b64.ROTATIONS:
        for outcome, sign in block67.nonzero_menu0_pairs(rotation):
            branch = block67.signed_branch(rotation, outcome, sign)
            decoded = block67.decode_signed_source(branch.records)
            if decoded is None:
                failures += 1
                continue
            direction = np.asarray(decoded.direction, dtype=int)
            head = np.asarray(decoded.head_site, dtype=int)
            new_source = np.asarray(decoded.new_source, dtype=int)
            old_source = np.asarray(decoded.old_source, dtype=int)
            context = block67.b64.decode_context(branch.records[branch.head_site])
            offset = new_source - head
            if mutation == "co_locate_source_at_head":
                offset = np.zeros(3, dtype=int)
            y0 = head + offset
            y_minus_one = y0 - direction
            if mutation == "drop_incoming_segment":
                y_minus_one = y0
            local_ok = (
                context is not None
                and np.array_equal(offset, -np.asarray(context.transverse))
                and np.array_equal(y0, new_source)
                and np.array_equal(y_minus_one, old_source)
                and int(np.sum(np.abs(offset))) == 1
                and int(offset @ direction) == 0
            )
            failures += int(not local_ok)
            previous = y_minus_one
            for index in range(6):
                head_n = head + index * direction
                source_n = head_n + offset
                failures += int(not np.array_equal(source_n - previous, direction))
                previous = source_n
                induction_checks += 1
            directions.add(tuple(int(value) for value in direction))
            cases += 1
    return cases, failures, induction_checks, directions


def isolated_boundary_certificate(mutation: str, note: str) -> tuple[int, float, bool]:
    _, _, hamiltonian_zero, _, _ = spatial_operators(np.zeros(3))
    density_before = 0.0
    density_after = 1.0
    incoming_flux_divergence = 0.0
    boundary_defect = density_after - density_before + incoming_flux_divergence
    best_zero_mode_field = np.linalg.pinv(
        hamiltonian_zero, rcond=1.0e-12
    ) @ np.asarray((boundary_defect,))
    isolated_birth_residual = float(
        np.linalg.norm(
            hamiltonian_zero @ best_zero_mode_field
            - np.asarray((boundary_defect,))
        )
    )
    acknowledged = (
        "actually isolated source" in note
        and "incoming boundary flux or a reservoir/recoil tensor" in note
        and "compact zero mode" in note
    )
    if mutation == "claim_isolated_birth":
        acknowledged = False
    return int(np.linalg.matrix_rank(hamiltonian_zero, TOL)), isolated_birth_residual, acknowledged


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = flat(NOTE_PATH)
    stacked_axioms = flat(AXIOM_PATH)
    authority_axioms = git_blob_flat(CURRENT_AXIOM_BLOB)
    resolved_authority_blob = git_commit_path_blob(
        CURRENT_AXIOM_COMMIT, AXIOM_REPO_PATH
    )
    kinetic_note = flat(KINETIC_PATH)
    block53_note = flat(BLOCK53_PATH)
    block67_note = flat(BLOCK67_PATH)
    block77_note = flat(BLOCK77_PATH)

    checks.check(
        "A-authority-and-parent-bindings",
        "the content-addressed current foundation and Blocks 53, 67, and 77 are bound without importing a selected gravity law",
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and mutation != "stale_axiom_authority"
        and resolved_authority_blob == CURRENT_AXIOM_BLOB
        and all(
            phrase in authority_axioms and phrase in stacked_axioms
            for phrase in (
                "admissibility is not a dynamics axiom",
                "a state is a configuration of records",
                "records are permanent",
            )
        )
        and "a site with no record cannot be read" in authority_axioms
        and "finite additivity" in authority_axioms
        and "are not record axiom content" in authority_axioms
        and "c_t = c_s" in kinetic_note
        and "positive shadow energy" in block53_note
        and "keep the physical source at `o_s`" in block67_note
        and "full constraint/source half-step schedule" in block77_note,
    )

    operator = operator_identity_certificate(mutation)
    block77_bridge = block77_adm_bridge_certificate(mutation)
    checks.check(
        "B-full-linear-adm-polynomial-identities-and-cubic-covariance",
        "the ADM complex closes exactly and is the canonical decomposition of Block 77's ten-component symbol",
        operator[0] == 6065
        and operator[1] < 5.0e-13
        and operator[2] < 5.0e-13
        and operator[3:] == ({1}, {3}, {4})
        and block77_bridge[0] == 12130
        and block77_bridge[1] < 5.0e-13
        and np.max(
            np.abs(block77_bridge[2] - np.asarray((1.0, 2.0, 2.0, 1.0)))
        )
        < 5.0e-13,
        f"modes={operator[0]}; identity/covariance={operator[1]:.3e}/{operator[2]:.3e}; ranks H/M/TT={operator[3]}/{operator[4]}/{operator[5]}; Block77 bridge cases/error={block77_bridge[0]}/{block77_bridge[1]:.3e}; normalization C/M/kick/impulse={block77_bridge[2]}",
    )

    locality = locality_certificate(mutation)
    checks.check(
        "C-raw-finite-range-potential-and-depth-two-macro",
        "the staggered spatial potential and complete homogeneous macro transfer are integer-Laurent finite-range laws",
        locality[0] == (19, 1, 2)
        and locality[1] == (57, 2, 3)
        and locality[2] < 3.0e-13
        and locality[3] < 3.0e-13
        and locality[4] < 3.0e-13,
        f"potential/macro support={locality[0]}/{locality[1]}; periodicity/Hermiticity/raw covariance={locality[2]:.3e}/{locality[3]:.3e}/{locality[4]:.3e}",
    )

    stability = tt_stability_certificate(mutation)
    checks.check(
        "D-two-tt-symplectic-full-zone-positive-depth-two-transfer",
        "all nonzero L=3 through L=12 modes have two TT pairs, exact symplecticity, unit-circle transfer, and positive shadow form",
        stability[0] == 6065
        and stability[1] < 5.0e-13
        and stability[2] < 5.0e-13
        and stability[3] == 6065
        and stability[4] > 0.23
        and stability[5] < 5.0e-13,
        f"modes/stable={stability[0]}/{stability[3]}; TT/symplectic/modulus={stability[1]:.3e}/{stability[2]:.3e}/{stability[5]:.3e}; min shadow={stability[4]:.6f}",
    )

    schedule = source_schedule_certificate(mutation)
    checks.check(
        "E-front-loaded-source-propagates-all-four-einstein-constraints",
        "the (2,0) kick placement carries energy and momentum constraints across every signed neutral source mode",
        schedule[0] == 13056
        and schedule[1] < 5.0e-13
        and schedule[2] == 0
        and schedule[3] < 5.0e-12,
        f"modes={schedule[0]}; source Ward={schedule[1]:.3e}; failures={schedule[2]}; max constraint={schedule[3]:.3e}",
    )

    checks.check(
        "F-equal-and-late-source-placement-hostile-controls",
        "equal and late stress splitting fail the generic sourced Hamiltonian midpoint while the front-loaded schedule passes",
        schedule[4] == 11064
        and schedule[5] > 3.9
        and schedule[6] == 11064
        and schedule[7] > 7.9,
        f"equal failures/max={schedule[4]}/{schedule[5]:.6f}; late failures/max={schedule[6]}/{schedule[7]:.6f}",
    )

    weights = weight_uniqueness_certificate(mutation)
    checks.check(
        "G-source-weight-uniqueness-in-supplied-kick-first-order",
        "midpoint and endpoint constraint equations derive the unique real weights (2,0) without fitting a response prefactor",
        weights[0] == 216
        and weights[1] == 2
        and np.max(np.abs(weights[2] - np.asarray((2.0, 0.0)))) < 5.0e-13
        and weights[3] < 5.0e-13,
        f"samples={weights[0]}; rank={weights[1]}; weights={weights[2]}; residual={weights[3]:.3e}",
    )

    incoming = cycle713_incoming_certificate(mutation)
    checks.check(
        "H-cycle713-offset-decoder-supplies-the-incoming-source-segment",
        "the content/frame-defined transverse offset maps Q to O_s and every later head finalization into one conserved source line",
        incoming[0] == 96
        and incoming[1] == 0
        and incoming[2] == 576
        and incoming[3] == set(block67.b64.DIRECTIONS),
        f"branches={incoming[0]}; failures={incoming[1]}; induction checks={incoming[2]}; directions={len(incoming[3])}",
    )

    boundary = isolated_boundary_certificate(mutation, note)
    checks.check(
        "I-cycle713-no-birth-repair-and-isolated-zero-mode-boundary",
        "Cycle713 uses its literal incoming hop, while genuinely isolated positive compact creation keeps an explicit boundary/reservoir wall",
        boundary[0] == 0 and boundary[1] == 1.0 and boundary[2],
        f"rank C(0)={boundary[0]}; isolated birth residual={boundary[1]:.1f}; boundary acknowledged={boundary[2]}",
    )

    scope_ok = all(
        phrase in note
        for phrase in (
            "configuration of records",
            "physical same-m2 source typing",
            "zero toe percentage movement",
            "no-go discipline gate status: fail",
            "partial-narrowing",
            "n1 -- alternative route enumeration",
            "n8 -- cross-cycle echo",
        )
    )
    if mutation in ("claim_record_native", "claim_complete"):
        scope_ok = False
    checks.check(
        "J-record-cadence-ontology-selection-and-no-go-scope",
        "the linear cadence result is separated from physical Record compilation, coupling/debit, nonlinear law, retention, and TOE promotion",
        scope_ok,
    )

    print(
        f"AXIOM_AUTHORITY: origin/main construction commit={CURRENT_AXIOM_COMMIT} immutable minimal-axiom blob={CURRENT_AXIOM_BLOB}; no removed scalar-I/additivity premise is imported"
    )
    print(
        "N5_CERTIFICATE: 6065 nonzero L=3..12 modes, 12130 Block77 canonical bridge cases, 24 cubic frames, 13056 signed two-transverse-axis neutral source modes, 96 Cycle713 event branches, four Einstein constraints, and both internal half steps are resolved"
    )
    print(
        "per_element: every spatial field and momentum coordinate, lapse row, three shift rows, and source-weight coefficient is checked; the physical source census injects diagonal ray stress only"
    )
    print(
        "per_site: translation-representative vertex stress, face momentum flux, radius-one Q-to-O_s source hop, transverse head offset, and six-step continuation are checked on local carriers"
    )
    print(
        "per_mode: all 6065 nonzero L=3 through L=12 spatial modes and all 13056 declared L=3 through L=8 two-transverse-axis neutral signed-source modes include even pi corners"
    )
    print(
        "per_block: current-axiom binding, Block77 canonical decomposition, ADM identities, raw locality/covariance, TT stability, source conservation, constraints, coefficient uniqueness, and Cycle713 decoding are checked separately"
    )
    print(
        "lattice_wide: checked and not executed — no physical same-M2 source compiler, gravity-state Record encoder, positive-mean boundary, exchange/debit law, or nonlinear selected gravity law is supplied"
    )
    print(
        "SCHEDULE: the derived kick-first weights are (2,0); all 13056 source modes propagate four constraints, while equal and late placement fail 11064 modes"
    )
    print(
        f"BLOCK77_BRIDGE: cases={block77_bridge[0]} residual={block77_bridge[1]:.3e}; derived normalization Ch/Mpi/first-kick/total-impulse={block77_bridge[2]}"
    )
    print(
        "CYCLE713: Y_n=H_n+u_s keeps the physical source at O_s; Q->O_s is the incoming segment, so no birth impulse is needed on this conditional single front"
    )
    print(
        "SCOPE: partial-positive linear cadence and source-decoder construction; no physical Record typing, coupling/debit, boundary selection, nonlinear completion, retention, obligation retirement, or TOE movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
