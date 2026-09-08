#!/usr/bin/env python3
"""Block 79: Cycle713 Record-head to sourced ADM work/archive boundary.

This runner makes the strongest current-ancestry vertical composition that is
actually executable.  It inserts the already-present Cycle713 endpoint's
derived same-M2 content as a candidate Record conditional on support and
formation, proves that the unchanged Block64 front continues, uses the
unique frontier-role transfer between adjacent permanent head Records as a
candidate moving point source for Block78, and derives the exact shadow-work
ledger.  It then separates three missing
interfaces: the next endpoint cannot yet be locked without blocking the
front, an identical Record packet cannot supply a field-dependent opposite
debit or encode the gravity output, and a dense arbitrary-horizon 3+1 history
cannot be materialized as fresh bounded-local permanent Records on Z3.

The result is a conditional positive compiler plus narrow countergates.  It is
not a selected physical law, a broad gravity/Record no-go, an axiom adoption,
or TOE obligation retirement.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import os
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK67_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_"
    "SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
BLOCK78_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_"
    "CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/admissibility_canonical_two_tt_positive_transfer_record_source_continuity_lstar_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_endpoint_record_attachment_intertwiner_boundary_2026_08_12.py",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
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
import admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13 as block67  # noqa: E402
import admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14 as block78  # noqa: E402


b64 = block67.b64
b65 = block67.b65
b63 = block67.b63
b53 = block78.block53

TOL = 1.0e-10
DELTA = 0.5
IDENTITY6 = np.eye(6, dtype=complex)
ZERO6 = np.zeros((6, 6), dtype=complex)
CURRENT_AXIOM_COMMIT = "b02f50a9cfb8ca57c2dbe7026d06487947d22331"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK78_COMMIT = "f978fccc8c"
PINNED_BLOBS = {
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md": "8511a1b04c74241f310186860fa0040142204964",
    "scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py": "8692942aad43ca3ac661bf0d1998f6cab6dd68c0",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "f9cbc29ddf57cb3385b65e97e6cad497b7b66d1d",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py": "2066434b8b96240774fc7f4c7cd9b2adcdd78a94",
}


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 152 else detail[:149] + "..."
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


def git_worktree_path_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", "--", path),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def coord_add(left: b64.Coord, right: b64.Coord) -> b64.Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def coord_sub(left: b64.Coord, right: b64.Coord) -> b64.Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def correct_endpoint_content(branch: block67.SignedBranch) -> b64.Carrier:
    """The old endpoint's physical projector, derived from the head frame.

    The successor frame already includes Block67's signed reflection.  Thus
    R_s(P1) is R(P1) on the positive chart and R(P0) on the negative chart.
    No program label or fitted tag is introduced.
    """

    context = b64.decode_context(branch.records[branch.head_site])
    if context is None:
        raise RuntimeError("signed branch has no decodable head")
    return b63.rotate_hermitian(context.rotation, b65.P1)


def endpoint_record_certificate(mutation: str) -> dict[str, object]:
    cases = equality_failures = parser_aliases = covariance_failures = 0
    geometry_failures = missing_records = 0
    base_packets: dict[tuple[int, int], b64.Records] = {}
    for outcome, sign in block67.nonzero_menu0_pairs(b64.IDENTITY_ROTATION):
        branch = block67.signed_branch(b64.IDENTITY_ROTATION, outcome, sign)
        packet = dict(branch.records)
        packet[branch.old_source] = correct_endpoint_content(branch)
        base_packets[(outcome, sign)] = packet

    for rotation in b64.ROTATIONS:
        for outcome, sign in block67.nonzero_menu0_pairs(rotation):
            branch = block67.signed_branch(rotation, outcome, sign)
            correct = correct_endpoint_content(branch)
            actual = correct
            if mutation == "wrong_endpoint_projector":
                context = b64.decode_context(branch.records[branch.head_site])
                assert context is not None
                actual = b63.rotate_hermitian(context.rotation, b65.P0)
            elif mutation == "freeze_endpoint_frame":
                actual = b65.P1

            packet = dict(branch.records)
            if mutation != "omit_endpoint_record":
                packet[branch.old_source] = actual
            missing_records += branch.old_source not in packet

            expected_chart = b63.rotate_hermitian(
                rotation, b65.P1 if sign == 1 else b65.P0
            )
            equality_failures += actual != correct or correct != expected_chart
            parser_aliases += int(b64.decode_context(actual) is not None)
            parser_aliases += int(b64.outcome_decode(actual) is not None)
            geometry_failures += not (
                block67.manhattan(branch.old_source, branch.new_source) == 1
                and coord_sub(branch.new_source, branch.old_source)
                == branch.direction
            )

            base = base_packets[(outcome, sign)]
            transformed = b65.transformed_records(base, rotation, b64.ORIGIN)
            covariance_failures += packet != transformed
            cases += 1
    return {
        "cases": cases,
        "equality_failures": equality_failures,
        "parser_aliases": parser_aliases,
        "covariance_failures": covariance_failures,
        "geometry_failures": geometry_failures,
        "missing_records": missing_records,
    }


def endpoint_continuation_certificate(mutation: str) -> dict[str, object]:
    innovations = tuple(
        Fraction(value, 31)
        for value in (1, 5, 9, 13, 17, 21, 25, 29, 3, 7, 11, 15, 19, 23, 27)
    )
    short_failures = long_failures = permanence_failures = 0
    next_target_failures = lock_next_not_blocked = overwrite_failures = 0
    short_cases = long_cases = active_checks = 0

    for rotation in b64.ROTATIONS:
        for outcome, sign in block67.nonzero_menu0_pairs(rotation):
            branch = block67.signed_branch(rotation, outcome, sign)
            endpoint = correct_endpoint_content(branch)
            packet = dict(branch.records)
            packet[branch.old_source] = endpoint
            run = b65.continue_block64(packet, 4, innovations)
            short_failures += not (run.ok and len(run.records) == 15)
            permanence_failures += any(
                run.records.get(site) != carrier for site, carrier in packet.items()
            )
            active_checks += run.active_checks
            short_cases += 1

            first = b65.continue_block64(packet, 1, innovations)
            profile = block67.decoded_head_profile(first.records)
            if not first.ok or len(profile.frontiers) != 1:
                next_target_failures += 1
                continue
            offset = coord_sub(branch.new_source, branch.head_site)
            next_source = coord_add(profile.frontiers[0], offset)
            active = b64.active_sites(first.records)
            target_ok = (
                len(active) == 1
                and next_source in active
                and active[next_source].kind == "relay"
            )
            next_target_failures += not target_ok
            if next_source in first.records:
                overwrite_failures += 1
                continue
            locked = dict(first.records)
            locked[next_source] = endpoint
            blocked = len(b64.active_sites(locked)) == 0
            lock_next_not_blocked += not blocked

    for outcome, sign in block67.nonzero_menu0_pairs(b64.IDENTITY_ROTATION):
        branch = block67.signed_branch(b64.IDENTITY_ROTATION, outcome, sign)
        endpoint = correct_endpoint_content(branch)
        packet = dict(branch.records)
        packet[branch.old_source] = endpoint
        run = b65.continue_block64(packet, 32, innovations)
        long_failures += not (run.ok and len(run.records) == 99)
        permanence_failures += any(
            run.records.get(site) != carrier for site, carrier in packet.items()
        )
        active_checks += run.active_checks
        long_cases += 1

    if mutation == "claim_next_endpoint_locked":
        lock_next_not_blocked = 96
    elif mutation == "overwrite_endpoint":
        overwrite_failures = 96
    return {
        "short_cases": short_cases,
        "short_failures": short_failures,
        "long_cases": long_cases,
        "long_failures": long_failures,
        "permanence_failures": permanence_failures,
        "next_target_failures": next_target_failures,
        "lock_next_not_blocked": lock_next_not_blocked,
        "overwrite_failures": overwrite_failures,
        "active_checks": active_checks,
    }


def record_head_cadence_certificate(mutation: str) -> dict[str, object]:
    innovations = (Fraction(1, 7), Fraction(3, 7), Fraction(5, 7))
    cases = failures = incoming_failures = 0
    directions: set[b64.Coord] = set()
    record_edges = 0
    for rotation in b64.ROTATIONS:
        for outcome, sign in block67.nonzero_menu0_pairs(rotation):
            branch = block67.signed_branch(rotation, outcome, sign)
            packet = dict(branch.records)
            packet[branch.old_source] = correct_endpoint_content(branch)
            incoming_old = branch.old_source
            if mutation == "drop_incoming_segment":
                incoming_old = branch.new_source
            incoming_failures += coord_sub(branch.new_source, incoming_old) != branch.direction

            horizon = 0 if mutation == "skip_finalization" else 1
            run = b65.continue_block64(packet, horizon, innovations)
            profile0 = block67.decoded_head_profile(packet)
            profile1 = block67.decoded_head_profile(run.records)
            ok = (
                run.ok
                and len(profile0.frontiers) == 1
                and len(profile1.frontiers) == 1
                and profile0.frontiers[0] in packet
                and profile1.frontiers[0] in run.records
                and coord_sub(profile1.frontiers[0], profile0.frontiers[0])
                == branch.direction
                and run.records[profile0.frontiers[0]]
                == packet[profile0.frontiers[0]]
            )
            failures += not ok
            if ok:
                directions.add(branch.direction)
                record_edges += 1
            cases += 1
    return {
        "cases": cases,
        "failures": failures,
        "incoming_failures": incoming_failures,
        "record_edges": record_edges,
        "directions": directions,
    }


def point_source_data(
    k: np.ndarray,
    site: b64.Coord,
    direction: b64.Coord,
    flip_outgoing_phase: bool = False,
) -> tuple[np.ndarray, complex, complex, np.ndarray, np.ndarray, np.ndarray]:
    axis = int(np.flatnonzero(np.abs(np.asarray(direction)) > 0)[0])
    sign = int(direction[axis])
    density = np.exp(-1.0j * float(k @ np.asarray(site, dtype=float)))
    density_next = np.exp(-1.0j * sign * k[axis]) * density
    incoming = np.zeros(3, dtype=complex)
    outgoing = np.zeros(3, dtype=complex)
    incoming[axis] = sign * np.exp(0.5j * sign * k[axis]) * density
    phase_sign = 1.0 if flip_outgoing_phase else -1.0
    outgoing[axis] = sign * np.exp(
        phase_sign * 0.5j * sign * k[axis]
    ) * density
    stress = np.zeros((3, 3), dtype=complex)
    stress[axis, axis] = density
    return k, density, density_next, incoming, outgoing, block78.tensor_coordinates(stress)


def point_source_adm_certificate(mutation: str) -> dict[str, object]:
    modes = failures = 0
    ward_error = constraint_error = 0.0
    weights = (1.0, 1.0) if mutation == "equal_source_split" else (2.0, 0.0)
    for rotation in b64.ROTATIONS:
        for outcome, sign in block67.nonzero_menu0_pairs(rotation):
            branch = block67.signed_branch(rotation, outcome, sign)
            for size in range(3, 6):
                for integer_mode in np.ndindex((size,) * 3):
                    if integer_mode == (0, 0, 0):
                        continue
                    k = 2.0 * np.pi * np.asarray(integer_mode, dtype=float) / size
                    data = point_source_data(
                        k,
                        branch.head_site,
                        branch.direction,
                        flip_outgoing_phase=mutation == "flip_outgoing_phase",
                    )
                    ward, residual = block78.schedule_residual(*data, weights)
                    ward_error = max(ward_error, ward)
                    constraint_error = max(constraint_error, residual)
                    failures += int(max(ward, residual) > TOL)
                    modes += 1

    _, _, hamiltonian_zero, _, _ = block78.spatial_operators(np.zeros(3))
    zero_rank = int(np.linalg.matrix_rank(hamiltonian_zero, TOL))
    zero_residual = float(
        np.linalg.norm(
            hamiltonian_zero
            @ (np.linalg.pinv(hamiltonian_zero, rcond=1.0e-12) @ np.ones(1))
            - np.ones(1)
        )
    )
    if mutation == "claim_zero_mode":
        zero_residual = 0.0
    return {
        "modes": modes,
        "failures": failures,
        "ward_error": ward_error,
        "constraint_error": constraint_error,
        "zero_rank": zero_rank,
        "zero_residual": zero_residual,
    }


def shadow_form(kinetic: np.ndarray, potential: np.ndarray, mutation: str = "") -> np.ndarray:
    cross = 0.0 if mutation == "wrong_shadow_cross_term" else -DELTA / 2.0
    return np.block(
        [
            [potential, cross * potential @ kinetic],
            [cross * kinetic @ potential, kinetic],
        ]
    )


def shadow_energy(form: np.ndarray, state: np.ndarray) -> float:
    return 0.5 * float(np.real(state.conj() @ form @ state))


def shadow_work_certificate(mutation: str) -> dict[str, object]:
    modes = stable = 0
    form_error = work_error = unforced_error = constraint_error = 0.0
    tt_error = 0.0
    minimum_shadow = np.inf
    minimum_zero_field_work = np.inf
    maximum_zero_field_work = -np.inf
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
                                k, density, _density_next, incoming, _outgoing, stress = data
                                p = b53.lattice_vector(k)
                                kinetic, potential, hamiltonian, momentum, _shift = (
                                    block78.spatial_operators(p)
                                )
                                h0 = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray((density,))
                                pi0 = np.linalg.pinv(momentum, rcond=1.0e-12) @ (2.0 * incoming)
                                force = 2.0 * stress
                                form = shadow_form(kinetic, potential, mutation)
                                kick = np.block(
                                    [[IDENTITY6, ZERO6], [-DELTA * potential, IDENTITY6]]
                                )
                                drift = np.block(
                                    [[IDENTITY6, DELTA * kinetic], [ZERO6, IDENTITY6]]
                                )
                                homogeneous = drift @ kick
                                form_error = max(
                                    form_error,
                                    float(
                                        np.max(
                                            np.abs(
                                                homogeneous.conj().T @ form @ homogeneous
                                                - form
                                            )
                                        )
                                    ),
                                )

                                pi1 = pi0 + DELTA * (-potential @ h0 + force)
                                h1 = h0 + DELTA * kinetic @ pi1
                                pi2 = pi1 - DELTA * potential @ h1
                                h2 = h1 + DELTA * kinetic @ pi2
                                z0 = np.concatenate((h0, pi0))
                                z1 = np.concatenate((h1, pi1))
                                z2 = np.concatenate((h2, pi2))
                                average = pi1 if mutation == "endpoint_work" else (pi0 + pi1) / 2.0
                                work = DELTA * float(np.real(force.conj() @ kinetic @ average))
                                work_error = max(
                                    work_error,
                                    abs(shadow_energy(form, z1) - shadow_energy(form, z0) - work),
                                )
                                unforced_error = max(
                                    unforced_error,
                                    abs(shadow_energy(form, z2) - shadow_energy(form, z1)),
                                )
                                _, residual = block78.schedule_residual(*data, (2.0, 0.0))
                                constraint_error = max(constraint_error, residual)

                                tt = null_space(b53.tt_constraint(k), rcond=1.0e-11)
                                tt_kinetic = tt.conj().T @ kinetic @ tt
                                tt_potential = tt.conj().T @ potential @ tt
                                tt_form = np.block(
                                    [
                                        [tt_potential, -DELTA * tt_potential @ tt_kinetic / 2.0],
                                        [-DELTA * tt_kinetic @ tt_potential / 2.0, tt_kinetic],
                                    ]
                                )
                                current_minimum = float(np.linalg.eigvalsh(tt_form).min())
                                minimum_shadow = min(minimum_shadow, current_minimum)
                                tt_error = max(
                                    tt_error,
                                    float(np.max(np.abs(tt_kinetic - np.eye(2)))),
                                    float(
                                        np.max(
                                            np.abs(
                                                tt_potential - float(p @ p) * np.eye(2)
                                            )
                                        )
                                    ),
                                )
                                projected = tt @ (tt.conj().T @ stress)
                                projected_force = 2.0 * projected
                                zero_field_work = (
                                    DELTA**2
                                    * float(
                                        np.real(
                                            projected_force.conj()
                                            @ kinetic
                                            @ projected_force
                                        )
                                    )
                                    / 2.0
                                )
                                minimum_zero_field_work = min(
                                    minimum_zero_field_work, zero_field_work
                                )
                                maximum_zero_field_work = max(
                                    maximum_zero_field_work, zero_field_work
                                )
                                stable += int(current_minimum > TOL)
                                modes += 1
    return {
        "modes": modes,
        "stable": stable,
        "form_error": form_error,
        "work_error": work_error,
        "unforced_error": unforced_error,
        "constraint_error": constraint_error,
        "tt_error": tt_error,
        "minimum_shadow": minimum_shadow,
        "minimum_zero_field_work": minimum_zero_field_work,
        "maximum_zero_field_work": maximum_zero_field_work,
    }


def forced_macro(
    kinetic: np.ndarray,
    potential: np.ndarray,
    stress: np.ndarray,
    h0: np.ndarray,
    pi0: np.ndarray,
) -> tuple[np.ndarray, float]:
    force = 2.0 * stress
    pi1 = pi0 + DELTA * (-potential @ h0 + force)
    h1 = h0 + DELTA * kinetic @ pi1
    pi2 = pi1 - DELTA * potential @ h1
    h2 = h1 + DELTA * kinetic @ pi2
    work = DELTA * float(np.real(force.conj() @ kinetic @ ((pi0 + pi1) / 2.0)))
    return np.concatenate((h2, pi2)), work


def debit_and_output_counterexample(mutation: str) -> dict[str, object]:
    k = 2.0 * np.pi * np.asarray((1, 2, 1), dtype=float) / 5.0
    data = point_source_data(k, b64.ORIGIN, (1, 0, 0))
    _, density, _density_next, incoming, _outgoing, stress = data
    p = b53.lattice_vector(k)
    kinetic, potential, hamiltonian, momentum, _shift = block78.spatial_operators(p)
    h0 = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray((density,))
    pi0 = np.linalg.pinv(momentum, rcond=1.0e-12) @ (2.0 * incoming)
    tt = null_space(b53.tt_constraint(k), rcond=1.0e-11)
    projected = tt @ (tt.conj().T @ stress)
    delta_pi = projected / np.linalg.norm(projected)
    output0, work0 = forced_macro(kinetic, potential, stress, h0, pi0)
    output1, work1 = forced_macro(kinetic, potential, stress, h0, pi0 + delta_pi)

    branch = block67.signed_branch(b64.IDENTITY_ROTATION, 1, 1)
    packet = dict(branch.records)
    packet[branch.old_source] = correct_endpoint_content(branch)
    run = b65.continue_block64(packet, 1, (Fraction(1, 3),))
    packet0 = run.records
    packet1 = dict(run.records)
    packets_identical = packet0 == packet1

    difference = output1 - output0
    output_constraint_error = max(
        float(np.max(np.abs(hamiltonian @ difference[:6]))),
        float(np.max(np.abs(momentum @ difference[6:]))),
    )
    work_difference = abs(work1 - work0)
    best_fixed_cost_residual = work_difference / 2.0
    if mutation == "fixed_record_cost":
        best_fixed_cost_residual = 0.0

    form = shadow_form(kinetic, potential)
    initial0 = np.concatenate((h0, pi0))
    formal_debit = -work0
    if mutation == "omit_debit":
        formal_debit = 0.0
    combined_residual = abs(
        shadow_energy(form, output0)
        - shadow_energy(form, initial0)
        + formal_debit
    )
    omitted_debit_residual = abs(
        shadow_energy(form, output0) - shadow_energy(form, initial0)
    )

    # Any fixed finite-dimensional battery Hamiltonian is bounded.  For the
    # normalized TT ray pi(lambda)=pi0+lambda*delta_pi, work is affine with a
    # nonzero slope, and so exceeds every fixed two-norm battery bound.
    slope = work_difference
    battery_norm = 1.0
    overflow_lambda = int(np.ceil((2.0 * battery_norm + abs(work0)) / slope)) + 1
    _, overflow_work = forced_macro(
        kinetic, potential, stress, h0, pi0 + overflow_lambda * delta_pi
    )
    battery_overflow = abs(overflow_work) > 2.0 * battery_norm
    return {
        "packets_identical": packets_identical,
        "work0": work0,
        "work1": work1,
        "work_difference": work_difference,
        "best_fixed_cost_residual": best_fixed_cost_residual,
        "output_difference": float(np.linalg.norm(difference)),
        "output_constraint_error": output_constraint_error,
        "combined_residual": combined_residual,
        "omitted_debit_residual": omitted_debit_residual,
        "slope": slope,
        "overflow_lambda": overflow_lambda,
        "overflow_work": overflow_work,
        "battery_overflow": battery_overflow,
    }


def encode_two_m2(values: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if values.shape != (16,):
        raise ValueError("the raw ADM payload has sixteen real coordinates")
    matrices = []
    for start in (0, 8):
        matrix = np.zeros((2, 2), dtype=complex)
        for entry in range(4):
            matrix.flat[entry] = values[start + 2 * entry] + 1.0j * values[start + 2 * entry + 1]
        matrices.append(matrix)
    return matrices[0], matrices[1]


def decode_two_m2(matrices: tuple[np.ndarray, np.ndarray]) -> np.ndarray:
    values: list[float] = []
    for matrix in matrices:
        for entry in matrix.flat:
            values.extend((float(entry.real), float(entry.imag)))
    return np.asarray(values)


def payload_certificate(mutation: str) -> dict[str, object]:
    columns = []
    basis_error = hostile_error = 0.0
    for index in range(16):
        vector = np.zeros(16)
        vector[index] = 1.0
        encoded = encode_two_m2(vector)
        if mutation == "drop_second_m2":
            encoded = (encoded[0], np.zeros((2, 2), dtype=complex))
        decoded = decode_two_m2(encoded)
        columns.append(decoded)
        basis_error = max(basis_error, float(np.max(np.abs(decoded - vector))))
    map_matrix = np.column_stack(columns)
    hostile = np.asarray([Fraction(index - 7, 3) for index in range(16)], dtype=float)
    encoded_hostile = encode_two_m2(hostile)
    if mutation == "drop_second_m2":
        encoded_hostile = (encoded_hostile[0], np.zeros((2, 2), dtype=complex))
    hostile_error = float(np.max(np.abs(decode_two_m2(encoded_hostile) - hostile)))
    return {
        "rank": int(np.linalg.matrix_rank(map_matrix, TOL)),
        "basis_error": basis_error,
        "hostile_error": hostile_error,
    }


def finite_box_archive_certificate(mutation: str) -> dict[str, object]:
    failures = collisions = 0
    cases = 0
    maximum_spatial_dilation = 0
    maximum_role_dilation = 0
    minimum_time_dilation = 10**9
    maximum_time_dilation = 0
    for length in range(2, 9):
        sites: dict[tuple[int, int, int], tuple[int, int, int, int, int]] = {}
        for tick, i, j, k, role in product(
            range(17), range(length), range(length), range(length), range(2)
        ):
            x = i if mutation == "reuse_record" else tick * (length + 1) + i
            site = (x, j, 2 * k + role)
            collisions += site in sites
            sites[site] = (tick, i, j, k, role)
            cases += 1
        expected = 17 * 2 * length**3
        failures += len(sites) != expected
        maximum_spatial_dilation = max(maximum_spatial_dilation, 2)
        maximum_role_dilation = max(maximum_role_dilation, 1)
        time_dilation = 0 if mutation == "reuse_record" else length + 1
        minimum_time_dilation = min(minimum_time_dilation, time_dilation)
        maximum_time_dilation = max(maximum_time_dilation, time_dilation)
    return {
        "cases": cases,
        "failures": failures,
        "collisions": collisions,
        "maximum_spatial_dilation": maximum_spatial_dilation,
        "maximum_role_dilation": maximum_role_dilation,
        "minimum_time_dilation": minimum_time_dilation,
        "maximum_time_dilation": maximum_time_dilation,
    }


def ball3(radius: int) -> int:
    return (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3


def diamond4(depth: int) -> int:
    return (depth + 1) * (depth**3 + 3 * depth**2 + 5 * depth + 3) // 3


def first_capacity_failure(q: int, radius: int, slack: int, mutation: str = "") -> int:
    for depth in range(1, 1001):
        demand = ball3(depth) if mutation == "drop_time_axis" else q * diamond4(depth)
        effective_radius = depth if mutation == "growing_radius_as_fixed" else radius
        supply = ball3(effective_radius * depth + slack)
        if demand > supply:
            return depth
    return -1


def archive_capacity_certificate(mutation: str) -> dict[str, object]:
    thresholds = (
        first_capacity_failure(1, 3, 0, mutation),
        first_capacity_failure(2, 3, 0, mutation),
        first_capacity_failure(2, 3, 1, mutation),
        first_capacity_failure(2, 3, 3, mutation),
    )
    checkpoints = {
        "q1_last": (diamond4(104), ball3(3 * 104)),
        "q1_fail": (diamond4(105), ball3(3 * 105)),
        "q2s1_last": (2 * diamond4(51), ball3(3 * 51 + 1)),
        "q2s1_fail": (2 * diamond4(52), ball3(3 * 52 + 1)),
    }
    overlap_sites = 0
    full_image_failures = 0
    for size in range(3, 13):
        torus = set(product(range(size), repeat=3))
        offset0 = (0, 0, 0)
        offset1 = (1 % size, 2 % size, 1 % size)
        image0 = {
            tuple((site[index] + offset0[index]) % size for index in range(3))
            for site in torus
        }
        image1 = {
            tuple((site[index] + offset1[index]) % size for index in range(3))
            for site in torus
        }
        full_image_failures += image0 != torus or image1 != torus
        overlap_sites += len(image0 & image1)
    if mutation == "allow_slice_overlap":
        overlap_sites = 0
    return {
        "thresholds": thresholds,
        "checkpoints": checkpoints,
        "overlap_sites": overlap_sites,
        "full_image_failures": full_image_failures,
    }


def nonperiodic_clock_certificate() -> dict[str, object]:
    half = Fraction(1, 2)
    step = (
        (half, half),
        (Fraction(-1), Fraction(1)),
    )
    macro = tuple(
        tuple(
            sum((step[row][inner] * step[inner][column] for inner in range(2)), Fraction(0))
            for column in range(2)
        )
        for row in range(2)
    )
    determinant = macro[0][0] * macro[1][1] - macro[0][1] * macro[1][0]
    trace = macro[0][0] + macro[1][1]
    characteristic = (4, -1, 4)
    rational_trace_is_noninteger = trace.denominator != 1
    return {
        "macro": macro,
        "determinant": determinant,
        "trace": trace,
        "characteristic": characteristic,
        "rational_trace_is_noninteger": rational_trace_is_noninteger,
    }


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = flat(NOTE_PATH)
    stacked_axioms = flat(AXIOM_PATH)
    authority_axioms = git_blob_flat(CURRENT_AXIOM_BLOB)
    pinned_paths_ok = all(
        git_commit_path_blob(BLOCK78_COMMIT, path) == blob
        and git_worktree_path_blob(path) == blob
        for path, blob in PINNED_BLOBS.items()
    )
    parent_script_paths = tuple(
        path
        for path in AUDIT_INPUT_PATHS
        if path.startswith("scripts/")
        and path
        != "scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py"
    )
    helper_closure_pinned = all(
        git_worktree_path_blob(path) == git_commit_path_blob(BLOCK78_COMMIT, path)
        for path in parent_script_paths
    )
    checks.check(
        "A-authority-and-parent-content-bindings",
        "current axioms and the exact Block67/78 source and cadence parents are content-pinned",
        mutation != "stale_axiom_authority"
        and all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and git_commit_path_blob(
            CURRENT_AXIOM_COMMIT, "docs/MINIMAL_AXIOMS_2026-06-29.md"
        )
        == CURRENT_AXIOM_BLOB
        and git_worktree_path_blob("docs/MINIMAL_AXIOMS_2026-06-29.md")
        == CURRENT_AXIOM_BLOB
        and pinned_paths_ok
        and helper_closure_pinned
        and all(
            phrase in authority_axioms and phrase in stacked_axioms
            for phrase in (
                "the full one-site possibility domain has algebraic presentation `m_2(c)`",
                "records are permanent",
                "a state is a configuration of records",
            )
        )
        and "a site never carries more than one record" in authority_axioms
        and "only records are readable" in authority_axioms,
    )

    endpoint = endpoint_record_certificate(mutation)
    checks.check(
        "B-derived-same-m2-old-endpoint-candidate-content-and-covariance",
        "conditional insertion of the derived co-rotated endpoint projector needs no tag and creates no parser alias",
        endpoint["cases"] == 96
        and endpoint["equality_failures"] == 0
        and endpoint["parser_aliases"] == 0
        and endpoint["covariance_failures"] == 0
        and endpoint["geometry_failures"] == 0
        and endpoint["missing_records"] == 0,
        f"branches={endpoint['cases']}; equality/parser/covariance/geometry/missing={endpoint['equality_failures']}/{endpoint['parser_aliases']}/{endpoint['covariance_failures']}/{endpoint['geometry_failures']}/{endpoint['missing_records']}",
    )

    continuation = endpoint_continuation_certificate(mutation)
    checks.check(
        "C-endpoint-permanence-continuation-and-live-next-slot-boundary",
        "the conditionally inserted old candidate is inert through the front, while inserting at the next live slot blocks it",
        continuation["short_cases"] == 96
        and continuation["short_failures"] == 0
        and continuation["long_cases"] == 4
        and continuation["long_failures"] == 0
        and continuation["permanence_failures"] == 0
        and continuation["next_target_failures"] == 0
        and continuation["lock_next_not_blocked"] == 0
        and continuation["overwrite_failures"] == 0,
        f"N4/N32={continuation['short_cases']}/{continuation['long_cases']}; failures={continuation['short_failures']}/{continuation['long_failures']}; active checks={continuation['active_checks']}; next-slot nonblocks={continuation['lock_next_not_blocked']}",
    )

    cadence = record_head_cadence_certificate(mutation)
    checks.check(
        "D-literal-record-head-cadence",
        "each finalization appends the next head Record one signed edge ahead and transfers the unique frontier role",
        cadence["cases"] == 96
        and cadence["failures"] == 0
        and cadence["incoming_failures"] == 0
        and cadence["record_edges"] == 96
        and cadence["directions"] == set(b64.DIRECTIONS),
        f"branches/Record edges={cadence['cases']}/{cadence['record_edges']}; failures/incoming={cadence['failures']}/{cadence['incoming_failures']}; directions={len(cadence['directions'])}",
    )

    point_source = point_source_adm_certificate(mutation)
    checks.check(
        "E-record-head-point-source-propagates-four-adm-constraints",
        "the decoded frontier transfer obeys a conserved point-stress candidate map into the derived (2,0) ADM macro",
        point_source["modes"] == 20448
        and point_source["failures"] == 0
        and point_source["ward_error"] < 5.0e-13
        and point_source["constraint_error"] < 5.0e-12
        and point_source["zero_rank"] == 0
        and point_source["zero_residual"] == 1.0,
        f"nonzero modes={point_source['modes']}; failures={point_source['failures']}; Ward/constraints={point_source['ward_error']:.3e}/{point_source['constraint_error']:.3e}; zero rank/residual={point_source['zero_rank']}/{point_source['zero_residual']:.1f}",
    )

    work = shadow_work_certificate(mutation)
    checks.check(
        "F-exact-positive-tt-shadow-work-identity",
        "the forced first kick has an exact midpoint work law and the unforced second step preserves shadow energy",
        work["modes"] == 13056
        and work["stable"] == 13056
        and work["form_error"] < 5.0e-13
        and work["work_error"] < 5.0e-13
        and work["unforced_error"] < 5.0e-13
        and work["constraint_error"] < 5.0e-12
        and work["tt_error"] < 5.0e-13
        and work["minimum_shadow"] > 0.23
        and work["minimum_zero_field_work"] > 0.002,
        f"modes/stable={work['modes']}/{work['stable']}; form/work/free/constraint={work['form_error']:.3e}/{work['work_error']:.3e}/{work['unforced_error']:.3e}/{work['constraint_error']:.3e}; min shadow/work={work['minimum_shadow']:.6f}/{work['minimum_zero_field_work']:.6f}",
    )

    counterexample = debit_and_output_counterexample(mutation)
    checks.check(
        "G-formal-opposite-debit-and-fixed-record-battery-countergate",
        "a formal -W ledger conserves exactly, but identical packets need different debits and fixed bounded batteries overflow",
        counterexample["packets_identical"]
        and counterexample["work_difference"] > 0.5
        and counterexample["best_fixed_cost_residual"] > 0.25
        and counterexample["combined_residual"] < 5.0e-13
        and counterexample["omitted_debit_residual"] > 0.05
        and counterexample["slope"] > 0.5
        and counterexample["battery_overflow"],
        f"work={counterexample['work0']:.6f}/{counterexample['work1']:.6f}; delta/best fixed residual={counterexample['work_difference']:.6f}/{counterexample['best_fixed_cost_residual']:.6f}; formal/omitted={counterexample['combined_residual']:.3e}/{counterexample['omitted_debit_residual']:.3e}; overflow lambda/work={counterexample['overflow_lambda']}/{counterexample['overflow_work']:.6f}",
    )

    output_scope = mutation != "claim_head_encodes_gravity"
    checks.check(
        "H-identical-record-history-does-not-encode-gravity-output",
        "two constrained TT inputs give identical Record histories but distinct gravity outputs",
        output_scope
        and counterexample["packets_identical"]
        and counterexample["output_difference"] > 0.6
        and counterexample["output_constraint_error"] < 5.0e-13,
        f"output separation={counterexample['output_difference']:.9f}; homogeneous output-constraint residual={counterexample['output_constraint_error']:.3e}",
    )

    payload = payload_certificate(mutation)
    checks.check(
        "I-two-m2-raw-adm-payload-codec",
        "two algebraic M2 contents linearly pack all 16 raw h, pi, lapse, and shift coordinates",
        payload["rank"] == 16
        and payload["basis_error"] < 1.0e-15
        and payload["hostile_error"] < 1.0e-15,
        f"real codec rank={payload['rank']}; basis/hostile recovery={payload['basis_error']:.1e}/{payload['hostile_error']:.1e}",
    )

    finite = finite_box_archive_certificate(mutation)
    finite_scope = mutation != "promote_finite_tube"
    checks.check(
        "J-finite-box-append-only-positive-control",
        "finite boxes admit an exact two-Record archive, with the explicit cost that time dilation grows with box size",
        finite_scope
        and finite["cases"] == 44030
        and finite["failures"] == 0
        and finite["collisions"] == 0
        and finite["maximum_spatial_dilation"] == 2
        and finite["maximum_role_dilation"] == 1
        and finite["minimum_time_dilation"] == 3
        and finite["maximum_time_dilation"] == 9,
        f"packets={finite['cases']}; failures/collisions={finite['failures']}/{finite['collisions']}; spatial/role/time={finite['maximum_spatial_dilation']}/{finite['maximum_role_dilation']}/{finite['minimum_time_dilation']}..{finite['maximum_time_dilation']}",
    )

    archive = archive_capacity_certificate(mutation)
    cp = archive["checkpoints"]
    checks.check(
        "K-uniform-local-full-slice-permanent-record-capacity-boundary",
        "a fixed-dilation injective 3+1 archive outgrows its Z3 host, and exact unit-translation slices overlap",
        archive["thresholds"] == (105, 51, 52, 54)
        and cp["q1_last"][0] <= cp["q1_last"][1]
        and cp["q1_fail"][0] > cp["q1_fail"][1]
        and cp["q2s1_last"][0] <= cp["q2s1_last"][1]
        and cp["q2s1_fail"][0] > cp["q2s1_fail"][1]
        and archive["full_image_failures"] == 0
        and archive["overlap_sites"] == 6075,
        f"first failures q1s0/q2s0/q2s1/q2s3={archive['thresholds']}; q2s1 N51={cp['q2s1_last']}, N52={cp['q2s1_fail']}; torus overlaps={archive['overlap_sites']}",
    )

    clock = nonperiodic_clock_certificate()
    scope_ok = all(
        phrase in note
        for phrase in (
            "no-go discipline gate status: fail",
            "partial-narrowing",
            "n1 -- alternative route enumeration",
            "n8 -- cross-cycle echo",
            "zero toe percentage movement",
            "not a gravity no-go",
            "not an axiom-necessity theorem",
            "formal debit is not a physical reservoir",
            "record-head is not a gravity-state record compiler",
            "live mutable carrier",
        )
    )
    if mutation in (
        "live_m2_is_current",
        "claim_axiom_required",
        "claim_complete",
        "host_clock",
        "promote_trajectory_digits",
    ):
        scope_ok = False
    checks.check(
        "L-clock-ontology-no-go-and-toe-scope",
        "the nonperiodic live-state and N1-N8 escapes keep the result bounded, unretained, and non-axiomatic",
        clock["macro"]
        == (
            (Fraction(-1, 4), Fraction(3, 4)),
            (Fraction(-3, 2), Fraction(1, 2)),
        )
        and clock["determinant"] == 1
        and clock["trace"] == Fraction(1, 4)
        and clock["characteristic"] == (4, -1, 4)
        and clock["rational_trace_is_noninteger"]
        and scope_ok,
        f"macro={clock['macro']}; det/trace={clock['determinant']}/{clock['trace']}; polynomial={clock['characteristic']}; bounded scope={scope_ok}",
    )

    print(
        f"AXIOM_AUTHORITY: construction commit={CURRENT_AXIOM_COMMIT} immutable minimal-axiom blob={CURRENT_AXIOM_BLOB}; Block78 parent={BLOCK78_COMMIT}"
    )
    print(
        "N5_CERTIFICATE: 96 signed Cycle713 branches, 4/32-event continuations, 20448 literal point-source modes, 13056 work-law modes, 16 payload coordinates, finite boxes L=2..8, and exact archive thresholds are resolved"
    )
    print(
        "per_element: endpoint projectors, every h/pi coordinate, lapse, three shifts, stress components, shadow-form blocks, two M2 payloads, and opposite-debit terms are checked"
    )
    print(
        "per_site: Q/O_s/H_0/H_1 geometry, every appended front Record, next-relay collision, finite-box archive packet, and bounded-dilation host ball are checked"
    )
    print(
        "per_mode: all 20448 nonzero L=3..5 branch-modes propagate four constraints and all 13056 Block78 L=3..8 source modes satisfy the shadow-work identity"
    )
    print(
        "per_block: authority, endpoint typing, continuation, cadence, ADM source, work, debit, output, payload, finite control, archive capacity, clock, and scope are checked separately"
    )
    print(
        "lattice_wide: checked and not executed — a live gravity carrier, physical opposite-debit reservoir, selected endpoint disposition, global scheduler, boundary data, nonlinear law, and retained audit chain remain absent"
    )
    print(
        "VERTICAL: the old endpoint has derived parser-compatible same-M2 candidate content conditional on support/formation; each newly appended adjacent head transfers the frontier role and, under the candidate source map, drives one exact nonzero-mode ADM tick"
    )
    print(
        "WORK: the exact midpoint shadow work has a formal -W ledger, but no current Record packet, fixed bounded qubit battery, or selected source recoil supplies that physical debit"
    )
    print(
        "ARCHIVE: two M2 contents have enough raw payload capacity, while a uniform bounded-local fresh-Record full-slice history fails geometrically; live-state and nonlocal/clocked encodings remain escapes"
    )
    print(
        "SCOPE: partial-positive vertical compiler plus partial-narrowing countergates; no selected L_phys, axiom adoption, positive audit retention, obligation retirement, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
