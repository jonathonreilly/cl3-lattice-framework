#!/usr/bin/env python3
"""Block 82: local shadow energy, Ward discriminators, and action boundary.

The Block79 shadow Hamiltonian is localized on the raw staggered spatial
carrier.  Its nineteen-shift potential admits an exact pointwise energy
balance.  The simplest raw-index flux representative has only a cyclic C3
stabilizer; an eight-coset Reynolds average of the whole density/source/flux
triplet restores covariance under all 24 proper-cubic frames while preserving
continuity and global work.  Two independent tests then prevent a physical
overclaim: the field-only energy changes under a sourced lapse displacement,
and its declared centered-nearest-neighbor field charge does not equal
Block81's matched-direction recoil on any of 13,056 minimum-norm source
representatives.

An exact type-I discrete action reproduces both Block78 substeps when the
source is prescribed.  The remaining positive target is one dynamic matter
action whose lapse, shift, and metric derivatives produce rho, j, and tau and
whose matter Euler--Lagrange equation supplies the opposite recoil.  No broad
gravity no-go, axiom amendment, or TOE movement follows from this boundary.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_LOCAL_SHADOW_ENERGY_FLUX_LAPSE_TRANSLATION_JOINT_ACTION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_MATCHED_TENSOR_SHADOW_EXCHANGE_RECORD_RAIL_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_LOCAL_SHADOW_ENERGY_FLUX_LAPSE_TRANSLATION_JOINT_ACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_MATCHED_TENSOR_SHADOW_EXCHANGE_RECORD_RAIL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_TOTAL_CUBIC_RECORD_GROWTH_GRAVITY_DEBIT_WARD_STATE_AXIOM_DECISION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_SECOND_ORDER_WARD_PSEUDOCONSTRAINT_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md",
    "docs/AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md",
    "docs/PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md",
    "docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_local_shadow_energy_flux_lapse_translation_joint_action_boundary_2026_08_14.py",
    "scripts/admissibility_matched_tensor_shadow_exchange_record_rail_boundary_2026_08_14.py",
    "scripts/admissibility_total_cubic_record_growth_gravity_debit_ward_state_axiom_decision_2026_08_14.py",
    "scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py",
    "scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/admissibility_canonical_two_tt_positive_transfer_record_source_continuity_lstar_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_endpoint_record_attachment_intertwiner_boundary_2026_08_12.py",
    "scripts/admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12.py",
    "scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py",
    "scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_matched_tensor_shadow_exchange_record_rail_boundary_2026_08_14 as block81  # noqa: E402


block80 = block81.block80
block79 = block81.block79
block78 = block81.block78
b64 = block81.b64
b53 = block81.b53

Checks = block81.Checks
TOL = 3.0e-10
DELTA = 0.5
COUPLING = 1.0
CURRENT_AXIOM_COMMIT = "621bc7521a1a314df700a2d8d09988beee1c4ad7"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK81_COMMIT = "5d2bc91220dfb1249fcc18da9f1f6048c430694f"
BLOCK81_NOTE_BLOB = "e249e3684d746f31bb77b7e7b1224349bc52ab19"
BLOCK81_RUNNER_BLOB = "8579dfb573e2dc28bac09946282b0c87753f2784"
RUNNER_RELATIVE = (
    "scripts/admissibility_local_shadow_energy_flux_lapse_translation_"
    "joint_action_boundary_2026_08_14.py"
)

Shift = tuple[int, int, int]
PathSteps = tuple[Shift, ...]


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
    declared = {path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")}
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
    frozen_paths = tuple(
        path
        for path in AUDIT_INPUT_PATHS
        if path not in (RUNNER_RELATIVE, NOTE_PATH.relative_to(ROOT).as_posix())
    )
    mismatches = tuple(
        path
        for path in frozen_paths
        if git_worktree_path_blob(path) != git_commit_path_blob(BLOCK81_COMMIT, path)
    )
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    return {
        "origin_main": origin_main,
        "axiom_blob": git_worktree_path_blob("docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "expected_axiom": expected_axiom,
        "parent_note": git_worktree_path_blob(PARENT_NOTE.relative_to(ROOT).as_posix()),
        "parent_runner": git_worktree_path_blob(
            "scripts/admissibility_matched_tensor_shadow_exchange_record_rail_boundary_2026_08_14.py"
        ),
        "mismatches": mismatches,
        "missing": tuple(sorted(loaded - declared)),
        "extra": tuple(sorted(declared - loaded)),
        "declared": len(declared),
        "loaded": len(loaded),
    }


def spatial_placement(momentum: np.ndarray, co_located: bool = False) -> np.ndarray:
    k = np.asarray(momentum, dtype=float)
    phases = (
        1.0,
        1.0,
        1.0,
        np.exp(0.5j * (k[0] + k[1])),
        np.exp(0.5j * (k[0] + k[2])),
        np.exp(0.5j * (k[1] + k[2])),
    )
    if co_located:
        phases = (1.0,) * 6
    return np.diag(phases)


def raw_spatial_operators(
    momentum: np.ndarray,
    co_located: bool = False,
) -> tuple[np.ndarray, np.ndarray]:
    p = b53.lattice_vector(momentum)
    kinetic, potential, _constraint, _momentum, _shift = block78.spatial_operators(p)
    placement = spatial_placement(momentum, co_located)
    return kinetic, placement @ potential @ placement.conj().T


def potential_stencil(
    size: int,
    co_located: bool = False,
) -> dict[Shift, np.ndarray]:
    symbols = np.zeros((size, size, size, 6, 6), dtype=complex)
    for integer_mode in np.ndindex((size,) * 3):
        momentum = 2.0 * np.pi * np.asarray(integer_mode, dtype=float) / size
        symbols[integer_mode] = raw_spatial_operators(momentum, co_located)[1]
    kernel = np.fft.fftn(symbols, axes=(0, 1, 2)) / size**3
    maxima = np.max(np.abs(kernel), axis=(3, 4))
    result: dict[Shift, np.ndarray] = {}
    for index in np.argwhere(maxima > 1.0e-10):
        shift = tuple(
            int(value if value <= size // 2 else value - size) for value in index
        )
        result[shift] = kernel[tuple(index)]
    return result


def shifted(field: np.ndarray, displacement: Shift) -> np.ndarray:
    return np.roll(
        field,
        shift=tuple(-value for value in displacement),
        axis=(0, 1, 2),
    )


def apply_stencil(
    field: np.ndarray,
    stencil: dict[Shift, np.ndarray],
) -> np.ndarray:
    result = np.zeros_like(field, dtype=complex)
    for displacement, coefficient in stencil.items():
        result += np.einsum(
            "ij,...j->...i", coefficient, shifted(field, displacement)
        )
    return result


def site_energy(
    h: np.ndarray,
    pi: np.ndarray,
    kinetic: np.ndarray,
    stencil: dict[Shift, np.ndarray],
    include_cross: bool = True,
) -> np.ndarray:
    ph = apply_stencil(h, stencil)
    momentum_term = pi if not include_cross else pi - DELTA * ph
    g_momentum = np.einsum("ij,...j->...i", kinetic, momentum_term)
    return 0.5 * np.real(
        np.einsum("...i,...i->...", pi.conj(), g_momentum)
        + np.einsum("...i,...i->...", h.conj(), ph)
    )


def fourier_shadow_energy(h: np.ndarray, pi: np.ndarray) -> float:
    size = h.shape[0]
    volume = size**3
    hh = np.fft.fftn(h, axes=(0, 1, 2))
    pp = np.fft.fftn(pi, axes=(0, 1, 2))
    energy = 0.0
    frequencies = np.fft.fftfreq(size)
    for index in np.ndindex((size,) * 3):
        momentum = 2.0 * np.pi * np.asarray(
            [frequencies[index[axis]] for axis in range(3)]
        )
        kinetic, potential = raw_spatial_operators(momentum)
        h_mode = hh[index]
        pi_mode = pp[index]
        energy += 0.5 / volume * float(
            np.real(
                np.vdot(h_mode, potential @ h_mode)
                + np.vdot(pi_mode, kinetic @ pi_mode)
                - DELTA * np.vdot(h_mode, potential @ kinetic @ pi_mode)
            )
        )
    return energy


def local_energy_certificate(mutation: str) -> dict[str, object]:
    size = 7
    co_located = mutation == "co_located_stencil"
    stencil = potential_stencil(size, co_located)
    kinetic = block78.spatial_operators(np.zeros(3))[0]
    rng = np.random.default_rng(8201)
    h = rng.normal(size=(size, size, size, 6))
    pi = rng.normal(size=(size, size, size, 6))
    ph = apply_stencil(h, stencil)
    hh = np.fft.fftn(h, axes=(0, 1, 2))
    direct_modes = np.zeros_like(hh)
    frequencies = np.fft.fftfreq(size)
    for index in np.ndindex((size,) * 3):
        momentum = 2.0 * np.pi * np.asarray(
            [frequencies[index[axis]] for axis in range(3)]
        )
        direct_modes[index] = raw_spatial_operators(momentum, co_located)[1] @ hh[index]
    direct = np.fft.ifftn(direct_modes, axes=(0, 1, 2))
    conjugacy = 0.0
    for displacement, coefficient in stencil.items():
        opposite = tuple(-value for value in displacement)
        conjugacy = max(
            conjugacy,
            float(np.max(np.abs(stencil[opposite] - coefficient.conj().T))),
        )
    density = site_energy(
        h,
        pi,
        kinetic,
        stencil,
        include_cross=mutation != "wrong_shadow_cross",
    )
    shadow = fourier_shadow_energy(h, pi)
    return {
        "support": len(stencil),
        "coordinate_radius": max(max(abs(value) for value in key) for key in stencil),
        "manhattan_radius": max(sum(abs(value) for value in key) for key in stencil),
        "conjugacy": conjugacy,
        "application": float(np.max(np.abs(ph - direct))),
        "imaginary": float(np.max(np.abs(np.imag(ph)))),
        "sum_error": abs(float(np.sum(density)) - shadow),
        "site_sum": float(np.sum(density)),
        "fourier_sum": shadow,
    }


def shortest_paths(displacement: Shift, single: bool = False) -> tuple[PathSteps, ...]:
    steps: list[Shift] = []
    for axis, value in enumerate(displacement):
        unit = [0, 0, 0]
        unit[axis] = 1 if value > 0 else -1
        steps.extend(tuple(unit) for _ in range(abs(value)))
    paths = tuple(sorted(set(permutations(steps))))
    return paths[:1] if single else paths


def path_distribution(
    displacement: Shift,
    single: bool = False,
) -> dict[PathSteps, Fraction]:
    paths = shortest_paths(displacement, single)
    weight = Fraction(1, len(paths))
    return dict(Counter({path: weight for path in paths}))


def rotate_shift(rotation: np.ndarray, displacement: Shift) -> Shift:
    return tuple(int(value) for value in rotation @ np.asarray(displacement))


def path_covariance_certificate(single: bool) -> tuple[int, int]:
    stencil = potential_stencil(7)
    cases = failures = 0
    for displacement in stencil:
        if displacement == (0, 0, 0):
            continue
        distribution = path_distribution(displacement, single)
        for rotation in b64.ROTATIONS:
            rotated = {
                tuple(rotate_shift(rotation, step) for step in path): weight
                for path, weight in distribution.items()
            }
            target = path_distribution(rotate_shift(rotation, displacement), single)
            failures += int(rotated != target)
            cases += 1
    return cases, failures


def rotate_raw_tensor_field(field: np.ndarray, rotation: np.ndarray) -> np.ndarray:
    """Active raw staggered tensor action in NumPy's Fourier convention."""
    size = field.shape[0]
    modes = np.fft.fftn(field, axes=(0, 1, 2))
    rotated_modes = np.zeros_like(modes)
    representation = block78.tensor_rotation(rotation)
    for index in np.ndindex((size,) * 3):
        integer = np.asarray(
            [value if value <= size // 2 else value - size for value in index],
            dtype=int,
        )
        momentum = 2.0 * np.pi * integer / size
        rotated_integer = rotation @ integer
        rotated_momentum = rotation @ momentum
        action = (
            spatial_placement(rotated_momentum)
            @ representation
            @ spatial_placement(momentum).conj().T
        )
        destination = tuple(int(value % size) for value in rotated_integer)
        rotated_modes[destination] = action @ modes[index]
    return np.fft.ifftn(rotated_modes, axes=(0, 1, 2))


def rotate_site_scalar(field: np.ndarray, rotation: np.ndarray) -> np.ndarray:
    """Active scalar action: input x is deposited at R x."""
    size = field.shape[0]
    result = np.zeros_like(field)
    for site in np.ndindex((size,) * 3):
        destination = tuple(
            int(value % size) for value in rotation @ np.asarray(site)
        )
        result[destination] = field[site]
    return result


def rotate_bond_current(current: np.ndarray, rotation: np.ndarray) -> np.ndarray:
    """Rotate oriented positive-axis bonds, including negative-axis anchors."""
    size = current.shape[1]
    result = np.zeros_like(current)
    identity = np.eye(3, dtype=int)
    for source_axis in range(3):
        image = rotation @ identity[:, source_axis]
        target_axis = int(np.argmax(np.abs(image)))
        sign = int(image[target_axis])
        for site in np.ndindex((size,) * 3):
            anchor = rotation @ np.asarray(site)
            if sign < 0:
                anchor[target_axis] -= 1
            destination = tuple(int(value % size) for value in anchor)
            result[(target_axis,) + destination] += sign * current[
                (source_axis,) + site
            ]
    return result


def rotation_action_certificate() -> dict[str, object]:
    momentum = np.asarray((0.7, -1.1, 1.3))
    kinetic, potential = raw_spatial_operators(momentum)
    operator_error = composition_error = 0.0
    composition_cases = 0
    rotations = tuple(np.asarray(rotation, dtype=int) for rotation in b64.ROTATIONS)
    for rotation in rotations:
        representation = block78.tensor_rotation(rotation)
        rotated_momentum = rotation @ momentum
        action = (
            spatial_placement(rotated_momentum)
            @ representation
            @ spatial_placement(momentum).conj().T
        )
        rotated_kinetic, rotated_potential = raw_spatial_operators(rotated_momentum)
        operator_error = max(
            operator_error,
            float(
                np.max(
                    np.abs(rotated_potential - action @ potential @ action.conj().T)
                )
            ),
            float(
                np.max(
                    np.abs(rotated_kinetic - action @ kinetic @ action.conj().T)
                )
            ),
        )
        for second in rotations:
            second_representation = block78.tensor_rotation(second)
            second_momentum = second @ momentum
            second_action = (
                spatial_placement(second_momentum)
                @ second_representation
                @ spatial_placement(momentum).conj().T
            )
            first_after_second = (
                spatial_placement(rotation @ second_momentum)
                @ representation
                @ spatial_placement(second_momentum).conj().T
            )
            product = rotation @ second
            product_action = (
                spatial_placement(product @ momentum)
                @ block78.tensor_rotation(product)
                @ spatial_placement(momentum).conj().T
            )
            composition_error = max(
                composition_error,
                float(
                    np.max(
                        np.abs(first_after_second @ second_action - product_action)
                    )
                ),
            )
            composition_cases += 1

    size = 7
    support_union: set[Shift] = set()
    monomial_failures = 0
    for rotation in rotations:
        representation = block78.tensor_rotation(rotation)
        symbols = np.zeros((size, size, size, 6, 6), dtype=complex)
        for index in np.ndindex((size,) * 3):
            integer = np.asarray(
                [
                    value if value <= size // 2 else value - size
                    for value in index
                ]
            )
            k = 2.0 * np.pi * integer / size
            symbols[index] = (
                spatial_placement(rotation @ k)
                @ representation
                @ spatial_placement(k).conj().T
            )
        kernel = np.fft.fftn(symbols, axes=(0, 1, 2)) / size**3
        maxima = np.max(np.abs(kernel), axis=(3, 4))
        for index in np.argwhere(maxima > 1.0e-10):
            support_union.add(
                tuple(
                    int(value if value <= size // 2 else value - size)
                    for value in index
                )
            )
        for output in range(6):
            entries = int(np.count_nonzero(np.abs(kernel[..., output, :]) > 1.0e-10))
            monomial_failures += int(entries != 1)
    return {
        "frames": len(rotations),
        "operator_error": operator_error,
        "composition_cases": composition_cases,
        "composition_error": composition_error,
        "action_shifts": len(support_union),
        "coordinate_radius": max(
            max(abs(value) for value in shift) for shift in support_union
        ),
        "manhattan_radius": max(
            sum(abs(value) for value in shift) for shift in support_union
        ),
        "monomial_failures": monomial_failures,
    }


def reynolds_rotations() -> tuple[np.ndarray, ...]:
    """One representative of each H R coset of the base C3 stabilizer."""
    cycle = np.asarray(((0, 0, 1), (1, 0, 0), (0, 1, 0)), dtype=int)
    stabilizer = (np.eye(3, dtype=int), cycle, cycle @ cycle)

    def key(matrix: np.ndarray) -> tuple[int, ...]:
        return tuple(int(value) for value in matrix.reshape(-1))

    seen: set[tuple[int, ...]] = set()
    representatives: list[np.ndarray] = []
    for raw_rotation in b64.ROTATIONS:
        rotation = np.asarray(raw_rotation, dtype=int)
        coset = {key(element @ rotation) for element in stabilizer}
        if coset.isdisjoint(seen):
            representatives.append(rotation)
            seen.update(coset)
    return tuple(representatives)


def route_flux(
    phi: np.ndarray,
    displacement: Shift,
    single: bool,
) -> np.ndarray:
    current = np.zeros((3,) + phi.shape, dtype=float)
    paths = shortest_paths(displacement, single)
    for path in paths:
        location = [0, 0, 0]
        weight = 0.5 / len(paths)
        for step in path:
            axis = next(index for index, value in enumerate(step) if value)
            if step[axis] > 0:
                bond = tuple(location)
                sign = 1.0
            else:
                location[axis] -= 1
                bond = tuple(location)
                sign = -1.0
            current[axis] += sign * weight * np.roll(
                phi,
                shift=bond,
                axis=(0, 1, 2),
            )
            if step[axis] > 0:
                location[axis] += 1
    return current


def backward_divergence(vector: np.ndarray) -> np.ndarray:
    result = np.zeros(vector.shape[1:], dtype=float)
    for axis in range(3):
        result += vector[axis] - np.roll(vector[axis], shift=1, axis=axis)
    return result


def base_flux_triplet(
    h: np.ndarray,
    pi: np.ndarray,
    force: np.ndarray,
    stencil: dict[Shift, np.ndarray],
    kinetic: np.ndarray,
    *,
    endpoint_work: bool = False,
    single_path: bool = False,
) -> dict[str, np.ndarray | float]:
    size = h.shape[0]
    ph = apply_stencil(h, stencil)
    pi1 = pi + DELTA * (-ph + force)
    acceleration = np.einsum("ij,...j->...i", kinetic, pi1)
    h1 = h + DELTA * acceleration
    e0 = site_energy(h, pi, kinetic, stencil)
    e1 = site_energy(h1, pi1, kinetic, stencil)
    midpoint = pi1 if endpoint_work else (pi + pi1) / 2.0
    q0 = DELTA * np.real(
        np.einsum(
            "...i,...i->...",
            force.conj(),
            np.einsum("ij,...j->...i", kinetic, midpoint),
        )
    )
    pa = apply_stencil(acceleration, stencil)
    boundary = np.real(
        np.einsum("...i,...i->...", h.conj(), pa)
        - np.einsum("...i,...i->...", acceleration.conj(), ph)
    )
    current = np.zeros((3, size, size, size), dtype=float)
    green = np.zeros((size, size, size), dtype=float)
    for displacement, coefficient in stencil.items():
        if displacement == (0, 0, 0):
            continue
        phi = np.real(
            np.einsum(
                "...i,...i->...",
                h.conj(),
                np.einsum(
                    "ij,...j->...i",
                    coefficient,
                    shifted(acceleration, displacement),
                ),
            )
            - np.einsum(
                "...i,...i->...",
                acceleration.conj(),
                np.einsum(
                    "ij,...j->...i",
                    coefficient,
                    shifted(h, displacement),
                ),
            )
        )
        green += 0.5 * (phi - shifted(phi, tuple(-v for v in displacement)))
        current += route_flux(phi, displacement, single_path)
    divergence = backward_divergence(current)
    tensor_flux = -DELTA / 2.0 * current
    continuity = e1 - e0 + backward_divergence(tensor_flux) - q0
    return {
        "e0": e0,
        "e1": e1,
        "q0": q0,
        "tensor_flux": tensor_flux,
        "point_identity": float(
            np.max(np.abs(e1 - e0 - q0 - DELTA / 2.0 * boundary))
        ),
        "green_identity": float(np.max(np.abs(boundary - green))),
        "flux_identity": float(np.max(np.abs(green - divergence))),
        "continuity": float(np.max(np.abs(continuity))),
        "global_balance": abs(float(np.sum(e1 - e0 - q0))),
    }


def reynolds_flux_triplet(
    h: np.ndarray,
    pi: np.ndarray,
    force: np.ndarray,
    stencil: dict[Shift, np.ndarray],
    kinetic: np.ndarray,
    *,
    endpoint_work: bool = False,
    single_path: bool = False,
    rotations: tuple[np.ndarray, ...] | None = None,
) -> dict[str, np.ndarray]:
    accumulated: dict[str, np.ndarray] = {}
    selected = reynolds_rotations() if rotations is None else rotations
    for rotation in selected:
        rotated = base_flux_triplet(
            rotate_raw_tensor_field(h, rotation),
            rotate_raw_tensor_field(pi, rotation),
            rotate_raw_tensor_field(force, rotation),
            stencil,
            kinetic,
            endpoint_work=endpoint_work,
            single_path=single_path,
        )
        pulled = {
            "e0": rotate_site_scalar(np.asarray(rotated["e0"]), rotation.T),
            "e1": rotate_site_scalar(np.asarray(rotated["e1"]), rotation.T),
            "q0": rotate_site_scalar(np.asarray(rotated["q0"]), rotation.T),
            "tensor_flux": rotate_bond_current(
                np.asarray(rotated["tensor_flux"]), rotation.T
            ),
        }
        for key, value in pulled.items():
            if key not in accumulated:
                accumulated[key] = value.copy()
            else:
                accumulated[key] += value
    return {key: value / len(selected) for key, value in accumulated.items()}


def local_flux_certificate(mutation: str) -> dict[str, object]:
    size = 7
    kinetic = block78.spatial_operators(np.zeros(3))[0]
    stencil = potential_stencil(size)
    rng = np.random.default_rng(8202)
    h = rng.normal(size=(size, size, size, 6)).astype(complex)
    pi = rng.normal(size=(size, size, size, 6)).astype(complex)
    force = np.zeros_like(h)
    force[1, 2, 3, 0] = 0.73
    force[4, 0, 2, 2] = -0.21
    single = False
    base = base_flux_triplet(
        h,
        pi,
        force,
        stencil,
        kinetic,
        endpoint_work=mutation == "endpoint_work",
        single_path=single,
    )
    cases, covariance_failures = path_covariance_certificate(single)

    covariance_size = 5
    covariance_stencil = potential_stencil(covariance_size)
    covariance_rng = np.random.default_rng(8203)
    covariance_h = covariance_rng.normal(
        size=(covariance_size, covariance_size, covariance_size, 6)
    ) + 1.0j * covariance_rng.normal(
        size=(covariance_size, covariance_size, covariance_size, 6)
    )
    covariance_pi = covariance_rng.normal(size=covariance_h.shape) + 1.0j * (
        covariance_rng.normal(size=covariance_h.shape)
    )
    covariance_force = np.zeros_like(covariance_h)
    covariance_force[1, 2, 3, 0] = 0.73 + 0.19j
    covariance_force[4, 0, 2, 2] = -0.21 + 0.11j
    base_covariance = base_flux_triplet(
        covariance_h,
        covariance_pi,
        covariance_force,
        covariance_stencil,
        kinetic,
    )
    selected_rotations = reynolds_rotations()
    if mutation == "drop_reynolds_coset":
        selected_rotations = selected_rotations[:-1]
    averaged = reynolds_flux_triplet(
        covariance_h,
        covariance_pi,
        covariance_force,
        covariance_stencil,
        kinetic,
        endpoint_work=mutation == "endpoint_work",
        single_path=single,
        rotations=selected_rotations,
    )
    full_average = reynolds_flux_triplet(
        covariance_h,
        covariance_pi,
        covariance_force,
        covariance_stencil,
        kinetic,
        endpoint_work=mutation == "endpoint_work",
        single_path=single,
        rotations=tuple(np.asarray(rotation, dtype=int) for rotation in b64.ROTATIONS),
    )
    if mutation == "unaveraged_cubic_flux":
        averaged = {
            key: np.asarray(base_covariance[key])
            for key in ("e0", "e1", "q0", "tensor_flux")
        }
    full_covariance_error = 0.0
    full_covariance_failures = 0
    base_covariance_failures = 0
    for raw_rotation in b64.ROTATIONS:
        rotation = np.asarray(raw_rotation, dtype=int)
        rotated_inputs = (
            rotate_raw_tensor_field(covariance_h, rotation),
            rotate_raw_tensor_field(covariance_pi, rotation),
            rotate_raw_tensor_field(covariance_force, rotation),
        )
        rotated_base = base_flux_triplet(
            *rotated_inputs,
            covariance_stencil,
            kinetic,
        )
        base_error = max(
            float(
                np.max(
                    np.abs(
                        np.asarray(rotated_base[key])
                        - rotate_site_scalar(
                            np.asarray(base_covariance[key]), rotation
                        )
                    )
                )
            )
            for key in ("e0", "e1", "q0")
        )
        base_error = max(
            base_error,
            float(
                np.max(
                    np.abs(
                        np.asarray(rotated_base["tensor_flux"])
                        - rotate_bond_current(
                            np.asarray(base_covariance["tensor_flux"]), rotation
                        )
                    )
                )
            ),
        )
        base_covariance_failures += int(base_error > 1.0e-9)
        if mutation == "unaveraged_cubic_flux":
            rotated_average = {
                key: np.asarray(rotated_base[key])
                for key in ("e0", "e1", "q0", "tensor_flux")
            }
        else:
            rotated_average = reynolds_flux_triplet(
                *rotated_inputs,
                covariance_stencil,
                kinetic,
                endpoint_work=mutation == "endpoint_work",
                single_path=single,
                rotations=selected_rotations,
            )
        errors = (
            float(
                np.max(
                    np.abs(
                        rotated_average["e0"]
                        - rotate_site_scalar(averaged["e0"], rotation)
                    )
                )
            ),
            float(
                np.max(
                    np.abs(
                        rotated_average["e1"]
                        - rotate_site_scalar(averaged["e1"], rotation)
                    )
                )
            ),
            float(
                np.max(
                    np.abs(
                        rotated_average["q0"]
                        - rotate_site_scalar(averaged["q0"], rotation)
                    )
                )
            ),
            float(
                np.max(
                    np.abs(
                        rotated_average["tensor_flux"]
                        - rotate_bond_current(averaged["tensor_flux"], rotation)
                    )
                )
            ),
        )
        frame_error = max(errors)
        full_covariance_error = max(full_covariance_error, frame_error)
        full_covariance_failures += int(frame_error > 1.0e-9)
    averaged_continuity = averaged["e1"] - averaged["e0"] + backward_divergence(
        averaged["tensor_flux"]
    ) - averaged["q0"]
    action = rotation_action_certificate()
    return {
        "point_identity": base["point_identity"],
        "green_identity": base["green_identity"],
        "flux_identity": base["flux_identity"],
        "continuity": base["continuity"],
        "global_balance": base["global_balance"],
        "path_cases": cases,
        "covariance_failures": covariance_failures,
        "base_covariance_failures": base_covariance_failures,
        "full_covariance_failures": full_covariance_failures,
        "full_covariance_error": full_covariance_error,
        "averaged_continuity": float(np.max(np.abs(averaged_continuity))),
        "averaged_sum_error": abs(
            float(np.sum(averaged["e0"]))
            - float(np.sum(np.asarray(base_covariance["e0"])))
        ),
        "reynolds_cosets": len(selected_rotations),
        "coset_compression_error": max(
            float(np.max(np.abs(averaged[key] - full_average[key])))
            for key in ("e0", "e1", "q0", "tensor_flux")
        ),
        "action": action,
    }


def mode_shadow_energy(
    h: np.ndarray,
    pi: np.ndarray,
    kinetic: np.ndarray,
    potential: np.ndarray,
) -> float:
    return (
        0.5
        * float(np.real(np.vdot(h, potential @ h) + np.vdot(pi, kinetic @ pi)))
        - DELTA
        / 2.0
        * float(np.real(np.vdot(h, potential @ kinetic @ pi)))
    )


def lapse_shift_certificate(mutation: str) -> dict[str, object]:
    cgc_error = pgc_error = ps_error = cgdm_error = 0.0
    identity_modes = 0
    for size in range(3, 13):
        for index in np.ndindex((size,) * 3):
            if index == (0, 0, 0):
                continue
            k_identity = 2.0 * np.pi * np.asarray(index, dtype=float) / size
            p_identity = b53.lattice_vector(k_identity)
            (
                kinetic_identity,
                potential_identity,
                hamiltonian_identity,
                momentum_identity,
                shift_identity,
            ) = block78.spatial_operators(p_identity)
            lapse_direction = hamiltonian_identity.conj().T
            derivative = 1.0j * p_identity
            cgc_error = max(
                cgc_error,
                float(
                    np.max(
                        np.abs(
                            hamiltonian_identity
                            @ kinetic_identity
                            @ lapse_direction
                        )
                    )
                ),
            )
            pgc_error = max(
                pgc_error,
                float(
                    np.max(
                        np.abs(
                            potential_identity
                            @ kinetic_identity
                            @ lapse_direction
                        )
                    )
                ),
            )
            ps_error = max(
                ps_error,
                float(np.max(np.abs(potential_identity @ shift_identity))),
            )
            cgdm_error = max(
                cgdm_error,
                float(
                    np.max(
                        np.abs(
                            hamiltonian_identity @ kinetic_identity
                            + 0.5 * derivative @ momentum_identity
                        )
                    )
                ),
            )
            identity_modes += 1

    data = block78.source_mode_data(5, 0, 1, 1, 1, 2, 1)
    k, density, _density_next, incoming, _outgoing, stress = data
    p = b53.lattice_vector(k)
    kinetic, potential, hamiltonian, momentum, shift = block78.spatial_operators(p)
    h = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray((density,))
    pi = np.linalg.pinv(momentum, rcond=1.0e-12) @ (2.0 * incoming)
    chi = 0.37 - 0.12j
    displaced = pi + hamiltonian.conj().T[:, 0] * chi
    observed = mode_shadow_energy(h, displaced, kinetic, potential) - mode_shadow_energy(
        h, pi, kinetic, potential
    )
    analytic = float(np.real(np.conj(chi) * (hamiltonian @ kinetic @ pi)[0]))
    source_sign = 1.0 if mutation == "wrong_source_sign" else -1.0
    source_form = source_sign * float(
        np.real(np.conj(chi) * (1.0j * p @ incoming))
    )
    if mutation == "ignore_lapse":
        observed = 0.0

    tt = null_space(b53.tt_constraint(k), rcond=1.0e-11)
    vacuum_h = tt[:, 1]
    vacuum_pi = tt[:, 0]
    vacuum_displaced = vacuum_pi + hamiltonian.conj().T[:, 0] * chi
    vacuum_variation = mode_shadow_energy(
        vacuum_h, vacuum_displaced, kinetic, potential
    ) - mode_shadow_energy(vacuum_h, vacuum_pi, kinetic, potential)
    xi = np.asarray((0.23 - 0.11j, -0.07 + 0.19j, 0.31 + 0.04j))
    shifted_h = h + shift @ xi
    shift_variation = mode_shadow_energy(
        shifted_h, pi, kinetic, potential
    ) - mode_shadow_energy(h, pi, kinetic, potential)

    force = 2.0 * stress
    works = []
    for lapse in (0.0, 1.0):
        pi1 = pi + DELTA * (
            -potential @ h + hamiltonian.conj().T[:, 0] * lapse + force
        )
        works.append(
            DELTA
            * float(
                np.real(np.vdot(force, kinetic @ ((pi + pi1) / 2.0)))
            )
        )
    return {
        "identity_modes": identity_modes,
        "cgc_error": cgc_error,
        "pgc_error": pgc_error,
        "ps_error": ps_error,
        "cgdm_error": cgdm_error,
        "observed": observed,
        "analytic": analytic,
        "source_form": source_form,
        "identity_error": max(abs(observed - analytic), abs(analytic - source_form)),
        "vacuum_variation": abs(vacuum_variation),
        "shift_variation": abs(shift_variation),
        "source_constraint": float(np.max(np.abs(momentum @ pi - 2.0 * incoming))),
        "source_work_zero": works[0],
        "source_work_one": works[1],
        "source_work_difference": works[1] - works[0],
    }


def translation_recoil_certificate(mutation: str) -> dict[str, object]:
    modes = matches = 0
    minimum = np.inf
    maximum = 0.0
    commutator = 0.0
    fixture: dict[str, object] = {}
    for size in range(3, 9):
        for axis in range(3):
            for sign in (-1, 1):
                for neutral_step in (1, 2):
                    for along in range(size):
                        for transverse in range(1, size):
                            for remaining in range(size):
                                data = block78.source_mode_data(
                                    size,
                                    axis,
                                    sign,
                                    neutral_step,
                                    along,
                                    transverse,
                                    remaining,
                                )
                                k, density, _next, incoming, _outgoing, stress = data
                                p = b53.lattice_vector(k)
                                kinetic, potential, hamiltonian, momentum, _shift = (
                                    block78.spatial_operators(p)
                                )
                                h = np.linalg.pinv(
                                    hamiltonian, rcond=1.0e-12
                                ) @ np.asarray((density,))
                                pi = np.linalg.pinv(momentum, rcond=1.0e-12) @ (
                                    2.0 * incoming
                                )
                                force = 2.0 * stress
                                pi1 = pi + DELTA * (-potential @ h + force)
                                work = DELTA * float(
                                    np.real(
                                        np.vdot(
                                            force,
                                            kinetic @ ((pi + pi1) / 2.0),
                                        )
                                    )
                                )
                                charge = np.asarray(
                                    [
                                        DELTA
                                        * float(
                                            np.real(
                                                np.vdot(
                                                    force,
                                                    (1.0j * np.sin(k[direction])) * h,
                                                )
                                            )
                                        )
                                        for direction in range(3)
                                    ]
                                )
                                matched = np.zeros(3)
                                matched[axis] = sign * work
                                if mutation == "force_q_equals_dW":
                                    charge = matched.copy()
                                residual = float(np.linalg.norm(charge - matched))
                                minimum = min(minimum, residual)
                                maximum = max(maximum, residual)
                                matches += int(residual < 1.0e-10)
                                for direction in range(3):
                                    generator = 1.0j * np.sin(k[direction]) * np.eye(6)
                                    commutator = max(
                                        commutator,
                                        float(
                                            np.max(
                                                np.abs(generator @ kinetic - kinetic @ generator)
                                            )
                                        ),
                                        float(
                                            np.max(
                                                np.abs(generator @ potential - potential @ generator)
                                            )
                                        ),
                                    )
                                if (
                                    size,
                                    axis,
                                    sign,
                                    neutral_step,
                                    along,
                                    transverse,
                                    remaining,
                                ) == (3, 0, -1, 1, 0, 1, 0):
                                    fixture = {
                                        "momentum": k,
                                        "work": work,
                                        "charge": charge,
                                        "matched": matched,
                                    }
                                modes += 1
    return {
        "modes": modes,
        "matches": matches,
        "minimum": minimum,
        "maximum": maximum,
        "commutator": commutator,
        "fixture": fixture,
    }


def discrete_source_action(
    h0: np.ndarray,
    h1: np.ndarray,
    lapse: complex,
    shift_parameter: np.ndarray,
    density: complex,
    current: np.ndarray,
    force: np.ndarray,
    kinetic: np.ndarray,
    potential: np.ndarray,
    hamiltonian: np.ndarray,
    shift: np.ndarray,
    mutation: str = "",
) -> float:
    inverse_kinetic = np.linalg.inv(kinetic)
    velocity = (h1 - h0) / DELTA - shift @ shift_parameter
    potential_sign = 1.0 if mutation == "wrong_action_sign" else -1.0
    return (
        DELTA
        / 2.0
        * float(np.real(np.vdot(velocity, inverse_kinetic @ velocity)))
        + potential_sign
        * DELTA
        / 2.0
        * float(np.real(np.vdot(h0, potential @ h0)))
        + DELTA
        * float(
            np.real(np.conj(lapse) * ((hamiltonian @ h0)[0] - COUPLING * density))
        )
        + DELTA * float(np.real(np.vdot(h0, force)))
        + 2.0
        * DELTA
        * COUPLING
        * float(np.real(np.vdot(shift_parameter, current)))
    )


def real_gradient(function, value: np.ndarray) -> np.ndarray:
    point = np.asarray(value, dtype=complex)
    result = np.zeros_like(point)
    for index in np.ndindex(point.shape):
        direction = np.zeros_like(point)
        direction[index] = 1.0
        real_part = (function(point + direction) - function(point - direction)) / 2.0
        direction[index] = 1.0j
        imaginary_part = (
            function(point + direction) - function(point - direction)
        ) / 2.0
        result[index] = real_part + 1.0j * imaginary_part
    return result


def external_action_certificate(mutation: str) -> dict[str, object]:
    data = block78.source_mode_data(5, 0, 1, 1, 1, 2, 1)
    k, density, density_next, incoming, outgoing, stress = data
    p = b53.lattice_vector(k)
    derivative = 1.0j * p
    kinetic, potential, hamiltonian, momentum, shift = block78.spatial_operators(p)
    h0 = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray((density,))
    pi0 = np.linalg.pinv(momentum, rcond=1.0e-12) @ (2.0 * incoming)
    density_midpoint = density - 0.5 * derivative @ outgoing
    lapses = (0.17 + 0.03j, -0.11 + 0.07j)
    shifts = (
        np.asarray((0.2, -0.1, 0.3), dtype=complex),
        np.asarray((-0.2, 0.1, -0.3), dtype=complex),
    )
    forces = (2.0 * stress, np.zeros(6, dtype=complex))
    densities = (density, density_midpoint)
    fields = [h0]
    momenta = [pi0]
    for stage in range(2):
        pi1 = momenta[-1] + DELTA * (
            -potential @ fields[-1]
            + hamiltonian.conj().T[:, 0] * lapses[stage]
            + forces[stage]
        )
        h1 = fields[-1] + DELTA * (kinetic @ pi1 + shift @ shifts[stage])
        momenta.append(pi1)
        fields.append(h1)

    d2_error = legendre_error = lapse_error = shift_error = 0.0
    constraint_error = 0.0
    stage_gradients: list[tuple[np.ndarray, np.ndarray]] = []
    for stage in range(2):
        h_start = fields[stage]
        h_end = fields[stage + 1]
        lapse = lapses[stage]
        beta = shifts[stage]
        rho = densities[stage]
        current = outgoing
        force = forces[stage]

        def action(a, b, n, bet):
            return discrete_source_action(
                a,
                b,
                n,
                bet,
                rho,
                current,
                force,
                kinetic,
                potential,
                hamiltonian,
                shift,
                mutation,
            )

        grad_end = real_gradient(lambda value: action(h_start, value, lapse, beta), h_end)
        grad_start = real_gradient(lambda value: action(value, h_end, lapse, beta), h_start)
        grad_lapse = real_gradient(
            lambda value: action(h_start, h_end, value.item(), beta),
            np.asarray(lapse),
        )
        grad_shift = real_gradient(
            lambda value: action(h_start, h_end, lapse, value), beta
        )
        expected_pi_end = momenta[stage + 1]
        expected_pi_start = momenta[stage]
        expected_lapse = DELTA * (
            (hamiltonian @ h_start)[0] - COUPLING * rho
        )
        expected_shift = -DELTA * (
            momentum @ expected_pi_end - 2.0 * COUPLING * current
        )
        d2_error = max(d2_error, float(np.max(np.abs(grad_end - expected_pi_end))))
        legendre_error = max(
            legendre_error,
            float(np.max(np.abs(grad_start + expected_pi_start))),
        )
        lapse_error = max(lapse_error, abs(grad_lapse.item() - expected_lapse))
        shift_error = max(
            shift_error, float(np.max(np.abs(grad_shift - expected_shift)))
        )
        constraint_error = max(
            constraint_error,
            abs(expected_lapse),
            float(np.max(np.abs(expected_shift))),
        )
        stage_gradients.append((grad_start, grad_end))
    glue_error = float(np.max(np.abs(stage_gradients[0][1] + stage_gradients[1][0])))
    schedule_error = max(
        abs((hamiltonian @ fields[0])[0] - density),
        abs((hamiltonian @ fields[1])[0] - density_midpoint),
        abs((hamiltonian @ fields[2])[0] - density_next),
        float(np.max(np.abs(momentum @ momenta[1] - 2.0 * outgoing))),
        float(np.max(np.abs(momentum @ momenta[2] - 2.0 * outgoing))),
    )
    operator_error = max(
        float(np.max(np.abs(shift.conj().T @ momenta[1] - momentum @ momenta[1]))),
        float(np.max(np.abs(potential @ shift))),
    )
    return {
        "stages": 2,
        "d2_error": d2_error,
        "legendre_error": legendre_error,
        "lapse_error": lapse_error,
        "shift_error": shift_error,
        "constraint_error": constraint_error,
        "glue_error": glue_error,
        "schedule_error": schedule_error,
        "operator_error": operator_error,
    }


def matter_source_term(
    h: np.ndarray,
    lapse: complex,
    shift_parameter: np.ndarray,
    density: complex,
    current: np.ndarray,
    force: np.ndarray,
) -> float:
    return DELTA * float(
        np.real(
            -COUPLING * np.conj(lapse) * density
            + 2.0 * COUPLING * np.vdot(shift_parameter, current)
            + np.vdot(h, force)
        )
    )


def joint_action_contract_certificate(mutation: str) -> dict[str, object]:
    data = block78.source_mode_data(5, 0, 1, 1, 1, 2, 1)
    _k, density, _next, _incoming, current, force_half = data
    h = np.asarray((0.2, -0.1, 0.3, 0.07, -0.12, 0.05), dtype=complex)
    lapse = 0.17 + 0.03j
    beta = np.asarray((0.2, -0.1, 0.3), dtype=complex)
    force = 2.0 * force_half
    used_force = np.zeros_like(force) if mutation == "omit_metric_variation" else force
    gradient_h = real_gradient(
        lambda value: matter_source_term(
            value, lapse, beta, density, current, used_force
        ),
        h,
    )
    gradient_lapse = real_gradient(
        lambda value: matter_source_term(
            h, value.item(), beta, density, current, used_force
        ),
        np.asarray(lapse),
    )
    gradient_shift = real_gradient(
        lambda value: matter_source_term(
            h, lapse, value, density, current, used_force
        ),
        beta,
    )
    gradient_error = max(
        float(np.max(np.abs(gradient_h - DELTA * force))),
        abs(gradient_lapse.item() + DELTA * COUPLING * density),
        float(
            np.max(
                np.abs(gradient_shift - 2.0 * DELTA * COUPLING * current)
            )
        ),
    )

    metric = np.diag((-1.0, 1.0, 1.0, 1.0))
    symmetric_basis: list[np.ndarray] = []
    for left in range(4):
        for right in range(left, 4):
            basis = np.zeros((4, 4))
            value = 1.0 if left == right else 1.0 / np.sqrt(2.0)
            basis[left, right] = value
            basis[right, left] = value
            symmetric_basis.append(basis)
    mass_shell_error = metric_derivative_error = stress_error = 0.0
    for direction in block81.DIRECTIONS:
        amplitude = 0.73
        null_vector = np.asarray((1.0,) + direction)
        momentum = amplitude * null_vector
        einbein = 1.0 / amplitude
        mass_shell_error = max(
            mass_shell_error, abs(float(momentum @ metric @ momentum))
        )
        expected_stress = einbein * np.outer(momentum, momentum)

        def metric_term(inverse_metric: np.ndarray) -> float:
            return -einbein / 2.0 * float(momentum @ inverse_metric @ momentum)

        for basis in symmetric_basis:
            derivative = (metric_term(metric + basis) - metric_term(metric - basis)) / 2.0
            expected_derivative = -einbein / 2.0 * float(
                momentum @ basis @ momentum
            )
            metric_derivative_error = max(
                metric_derivative_error, abs(derivative - expected_derivative)
            )
            hilbert_coordinate = -2.0 * derivative
            expected_coordinate = float(np.sum(basis * expected_stress))
            stress_error = max(
                stress_error, abs(hilbert_coordinate - expected_coordinate)
            )
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").split())
    requires_recoil = mutation != "freeze_matter_recoil"
    return {
        "gradient_error": gradient_error,
        "mass_shell_error": mass_shell_error,
        "metric_derivative_error": metric_derivative_error,
        "stress_error": stress_error,
        "directions": len(block81.DIRECTIONS),
        "external_not_dynamic": "prescribed external source" in note,
        "requires_recoil": requires_recoil and "matter Euler--Lagrange" in note,
        "one_lm": "one `L_m[chi;h,n,beta]`" in note,
        "metric_derivative": "metric derivative" in note,
        "integrability_open": "mixed-Hessian integrability is not tested" in note,
    }


def no_double_counting_certificate(mutation: str) -> dict[str, object]:
    data = block78.source_mode_data(3, 0, -1, 1, 0, 1, 0)
    k, density, _next, incoming, _outgoing, stress = data
    p = b53.lattice_vector(k)
    kinetic, potential, hamiltonian, momentum, _shift = block78.spatial_operators(p)
    h = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray((density,))
    pi = np.linalg.pinv(momentum, rcond=1.0e-12) @ (2.0 * incoming)
    force = 2.0 * stress
    pi1 = pi + DELTA * (-potential @ h + force)
    work = DELTA * float(
        np.real(np.vdot(force, kinetic @ ((pi + pi1) / 2.0)))
    )
    field_change = work
    matter_change = -work
    independent_f_change = work
    accepted_independent = mutation == "add_independent_F_energy"
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").split())
    return {
        "work": work,
        "two_sector_balance": abs(field_change + matter_change),
        "three_sector_surplus": field_change + matter_change + independent_f_change,
        "reject_independent": not accepted_independent
        and "not a third independent energy reservoir" in note,
        "encode_same_current": "copy or encode the same field current" in note,
    }


def route_census_certificate(mutation: str) -> dict[str, object]:
    paths = {
        "block77": ROOT
        / "docs"
        / "ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
        "weak_field": ROOT / "docs" / "GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md",
        "noether": ROOT
        / "docs"
        / "AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md",
        "coframe": ROOT
        / "docs"
        / "PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md",
        "cycle576": ROOT
        / "docs"
        / "work_history"
        / "repo"
        / "review_feedback"
        / "PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md",
    }
    text = {name: path.read_text(encoding="utf-8").lower() for name, path in paths.items()}
    note = NOTE_PATH.read_text(encoding="utf-8")
    return {
        "routes": len(paths),
        "block77_external": "source-birth boundary" in text["block77"]
        and "remain open" in text["block77"],
        "weak_field_supplied": "inputs remain supplied" in text["weak_field"],
        "noether_scope": "site-mixing generators" in text["noether"]
        and "out of scope" in text["noether"],
        "coframe_bridge": "physical identification remains" in text["coframe"],
        "cycle576_not_stress": "not physical stress" in text["cycle576"]
        and "remains open" in text["cycle576"],
        "declared_census": "named-route census" in note,
        "not_exhaustive": "not a universal absence theorem" in note,
        "no_false_completion": mutation != "claim_existing_action_complete",
    }


def scope_certificate(mutation: str) -> dict[str, object]:
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").split())
    axiom = (ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md").read_text(
        encoding="utf-8"
    )
    return {
        "energy_column_only": "energy-column partial closure" in note,
        "not_full_stress": "does not prove a full physical stress tensor" in note,
        "matched_killed_narrowly": "rejects only that declared field-charge identification"
        in note
        and "centered-nearest-neighbor" in note
        and "minimum-norm" in note
        and "gravity does not fail" in note.lower(),
        "external_boundary": "external-source action" in note
        and "not dynamic matter" in note,
        "partial_narrowing": "FAIL — partial-narrowing" in note,
        "n1_n8": all(f"N{index}" in note for index in range(1, 9)),
        "state_sentence": "A state is a configuration of records." in axiom,
        "no_axiom": mutation != "claim_axiom_update" and "No axiom is amended" in note,
        "no_toe": mutation != "claim_toe_progress" and "No TOE percentage moves" in note,
        "no_physical_closure": mutation != "claim_physical_closure"
        and "No physical gravity closure is claimed" in note,
        "no_broad_no_go": mutation != "claim_gravity_no_go"
        and "not a gravity no-go" in note,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "wrong_shadow_cross",
            "co_located_stencil",
            "endpoint_work",
            "unaveraged_cubic_flux",
            "drop_reynolds_coset",
            "ignore_lapse",
            "wrong_source_sign",
            "force_q_equals_dW",
            "wrong_action_sign",
            "freeze_matter_recoil",
            "omit_metric_variation",
            "add_independent_F_energy",
            "claim_existing_action_complete",
            "claim_axiom_update",
            "claim_toe_progress",
            "claim_physical_closure",
            "claim_gravity_no_go",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority-parent-and-runtime-closure",
        "current axioms, Block81, comparators, and the loaded helper closure are content-bound",
        authority["origin_main"] == CURRENT_AXIOM_COMMIT
        and authority["axiom_blob"] == authority["expected_axiom"]
        and authority["parent_note"] == BLOCK81_NOTE_BLOB
        and authority["parent_runner"] == BLOCK81_RUNNER_BLOB
        and not authority["mismatches"]
        and not authority["missing"]
        and not authority["extra"],
        f"scripts declared/loaded={authority['declared']}/{authority['loaded']}; frozen mismatches={len(authority['mismatches'])}",
    )

    energy = local_energy_certificate(mutation)
    checks.check(
        "B-raw-staggered-local-shadow-energy",
        "the Block79 shadow Hamiltonian is a nineteen-shift bounded-local energy column",
        energy["support"] == 19
        and energy["coordinate_radius"] == 1
        and energy["manhattan_radius"] == 2
        and energy["conjugacy"] < TOL
        and energy["application"] < 1.0e-10
        and energy["imaginary"] < 1.0e-10
        and energy["sum_error"] < 1.0e-10,
        f"support/radii={energy['support']}/{energy['coordinate_radius']}/{energy['manhattan_radius']}; local/Fourier error={energy['sum_error']:.2e}",
    )

    flux = local_flux_certificate(mutation)
    checks.check(
        "C-pointwise-energy-flux-and-cubic-path-orbit",
        "a finite Reynolds average makes the exact local continuity triplet proper-cubic covariant",
        flux["point_identity"] < 1.0e-10
        and flux["green_identity"] < 1.0e-10
        and flux["flux_identity"] < 1.0e-10
        and flux["continuity"] < 1.0e-10
        and flux["global_balance"] < 1.0e-10
        and flux["path_cases"] == 432
        and flux["covariance_failures"] == 0
        and flux["base_covariance_failures"] == 21
        and flux["full_covariance_failures"] == 0
        and flux["full_covariance_error"] < 1.0e-10
        and flux["averaged_continuity"] < 1.0e-10
        and flux["averaged_sum_error"] < 1.0e-10
        and flux["reynolds_cosets"] == 8
        and flux["coset_compression_error"] < 1.0e-10
        and flux["action"]["frames"] == 24
        and flux["action"]["operator_error"] < TOL
        and flux["action"]["composition_cases"] == 576
        and flux["action"]["composition_error"] < TOL
        and flux["action"]["action_shifts"] == 7
        and flux["action"]["coordinate_radius"] == 1
        and flux["action"]["manhattan_radius"] == 2
        and flux["action"]["monomial_failures"] == 0,
        f"continuity/base-bad/averaged-bad={flux['averaged_continuity']:.2e}/{flux['base_covariance_failures']}/{flux['full_covariance_failures']}; cosets/compression={flux['reynolds_cosets']}/{flux['coset_compression_error']:.2e}",
    )

    lapse = lapse_shift_certificate(mutation)
    checks.check(
        "D-sourced-lapse-and-shift-discriminator",
        "field-only shadow energy is shift invariant and vacuum-lapse invariant but changes on a sourced lapse orbit",
        lapse["identity_error"] < TOL
        and lapse["identity_modes"] == sum(size**3 - 1 for size in range(3, 13))
        and lapse["cgc_error"] < TOL
        and lapse["pgc_error"] < TOL
        and lapse["ps_error"] < TOL
        and lapse["cgdm_error"] < TOL
        and abs(lapse["observed"]) > 0.8
        and lapse["vacuum_variation"] < TOL
        and lapse["shift_variation"] < TOL
        and lapse["source_constraint"] < TOL
        and abs(lapse["source_work_difference"] + 0.625) < TOL,
        f"operator CGC/PGC/PS/CG+DM={lapse['cgc_error']:.1e}/{lapse['pgc_error']:.1e}/{lapse['ps_error']:.1e}/{lapse['cgdm_error']:.1e}; lapse={lapse['observed']:.6f}; work shift={lapse['source_work_difference']:.3f}",
    )

    recoil = translation_recoil_certificate(mutation)
    fixture = recoil["fixture"]
    checks.check(
        "E-declared-centered-field-charge-versus-matched-recoil",
        "the declared centered field charge disagrees with the Block81 matched recoil on the minimum-norm source census",
        recoil["modes"] == 13056
        and recoil["matches"] == 0
        and recoil["minimum"] > 0.003
        and abs(recoil["maximum"] - 1.0) < TOL
        and recoil["commutator"] < TOL
        and abs(fixture["work"] - 0.75) < TOL
        and float(np.linalg.norm(fixture["charge"])) < TOL
        and float(np.linalg.norm(fixture["matched"] - np.asarray((-0.75, 0.0, 0.0)))) < TOL,
        f"modes/matches={recoil['modes']}/{recoil['matches']}; residual={recoil['minimum']:.6f}..{recoil['maximum']:.6f}; fixture W={fixture['work']:.2f}",
    )

    action = external_action_certificate(mutation)
    checks.check(
        "F-two-stage-type-I-external-source-action",
        "one discrete type-I action exactly reproduces both Block78 forced substeps and constraints",
        action["stages"] == 2
        and action["d2_error"] < 1.0e-10
        and action["legendre_error"] < 1.0e-10
        and action["lapse_error"] < 1.0e-10
        and action["shift_error"] < 1.0e-10
        and action["constraint_error"] < 1.0e-10
        and action["glue_error"] < 1.0e-10
        and action["schedule_error"] < 1.0e-10
        and action["operator_error"] < 1.0e-10,
        f"D2/Legendre/glue={action['d2_error']:.2e}/{action['legendre_error']:.2e}/{action['glue_error']:.2e}; schedule={action['schedule_error']:.2e}",
    )

    contract = joint_action_contract_certificate(mutation)
    checks.check(
        "G-prescribed-source-gradients-and-dynamic-target",
        "the comparator fixes source-gradient signs while dynamic integrability and recoil remain open",
        contract["gradient_error"] < 1.0e-10
        and contract["mass_shell_error"] < TOL
        and contract["metric_derivative_error"] < TOL
        and contract["stress_error"] < TOL
        and contract["directions"] == 6
        and contract["external_not_dynamic"]
        and contract["requires_recoil"]
        and contract["one_lm"]
        and contract["metric_derivative"]
        and contract["integrability_open"],
        f"source-gradient/metric-derivative/Hilbert-stress={contract['gradient_error']:.2e}/{contract['metric_derivative_error']:.2e}/{contract['stress_error']:.2e}; directions={contract['directions']}",
    )

    counting = no_double_counting_certificate(mutation)
    checks.check(
        "H-no-independent-F-energy-double-counting",
        "Block81 F may encode the field current but cannot add a third independent positive energy share",
        abs(counting["work"] - 0.75) < TOL
        and counting["two_sector_balance"] < TOL
        and abs(counting["three_sector_surplus"] - counting["work"]) < TOL
        and counting["reject_independent"]
        and counting["encode_same_current"],
        f"W/two-sector residual/three-sector surplus={counting['work']:.2f}/{counting['two_sector_balance']:.1e}/{counting['three_sector_surplus']:.2f}",
    )

    census = route_census_certificate(mutation)
    checks.check(
        "I-named-current-action-route-census",
        "five named repository routes each leave at least one joint-action ingredient open",
        census["routes"] == 5
        and all(value for key, value in census.items() if key != "routes"),
        f"routes={census['routes']}; external/supplied/translation/coframe/Regge={census['block77_external']}/{census['weak_field_supplied']}/{census['noether_scope']}/{census['coframe_bridge']}/{census['cycle576_not_stress']}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "J-no-go-axiom-and-TOE-scope",
        "the energy-column closure and two narrow kills do not imply gravity failure, axiom adoption, or TOE movement",
        all(scope.values()),
        f"energy/stress/narrow/N1-N8/axiom/TOE={scope['energy_column_only']}/{scope['not_full_stress']}/{scope['matched_killed_narrowly']}/{scope['n1_n8']}/{scope['no_axiom']}/{scope['no_toe']}",
    )

    print(
        "AXIOM_AUTHORITY: origin/main="
        + str(authority["origin_main"])
        + " minimal-axiom blob="
        + CURRENT_AXIOM_BLOB
        + "; Block81 parent="
        + BLOCK81_COMMIT
    )
    print(
        "per_element: checked — the local shadow density, source gradients, lapse identity, centered field generator, and worldline metric response are derived rather than fitted"
    )
    print(
        "per_site: checked — the base 19-shift density and unit-cell bond flux satisfy continuity; the eight-coset Reynolds triplet is bounded-local and all-24-frame covariant"
    )
    print(
        "per_mode: checked — 13,056 minimum-norm source representatives reject identification of the declared centered field-charge increment with dW"
    )
    print(
        "per_block: checked and not executed — the external-source action closes, but no dynamic L_m, mixed-Hessian integrability test, matter recoil, or localized total Ward identity is supplied"
    )
    print(
        "lattice_wide: checked and not executed — no common dynamic action, total physical stress, nonlinear/global positive compact source, physical readout, axiom adoption, or retained audit chain"
    )
    print(
        "RESULT: an exact bounded-local energy column, covariant Reynolds continuity triplet, and external-source variational bridge survive; the declared centered field charge is not Block81's matched recoil"
    )
    print(
        "NEXT: construct the smallest dynamic matter/worldline action whose metric derivatives yield rho,j,tau and whose matter equation supplies recoil, then derive the total Ward tensor"
    )
    print(
        "SCOPE: positive energy-column partial closure plus narrow sourced-lapse and matched-recoil discrimination; no axiom update, obligation retirement, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
