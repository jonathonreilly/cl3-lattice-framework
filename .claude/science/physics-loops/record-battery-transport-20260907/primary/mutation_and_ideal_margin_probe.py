#!/usr/bin/env python3
"""Scratch-only sensitivity and ideal-margin probe for the battery primary."""

from __future__ import annotations

import hashlib
import importlib.util
import math
import os
import sys
from pathlib import Path

for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import numpy as np


ROOT = Path.cwd()
PRIMARY_PATH = ROOT / "scripts/native_edge_record_shared_battery_transport_2026_09_07.py"
SPEC = importlib.util.spec_from_file_location("battery_primary", PRIMARY_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load primary")
primary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = primary
SPEC.loader.exec_module(primary)


def load_fixture() -> dict[str, object]:
    basis, hops, currents, numbers = primary.build_sector()
    full_mask = (1 << len(primary.EDGES)) - 1
    masks = [full_mask]
    for edge in primary.EDGE_ORDER:
        masks.append(masks[-1] & ~(1 << edge))
    hamiltonians = [primary.hamiltonian(hops, mask) for mask in masks]
    spectra = [primary.spectral_groups(matrix) for matrix in hamiltonians]
    groups = [item[0] for item in spectra]
    eigenvalues = [item[1] for item in spectra]
    eigenvectors = [item[2] for item in spectra]
    ground_values, ground_vectors = primary.eigh(hamiltonians[0])
    state = ground_vectors[:, int(np.argmin(ground_values))]
    pulse = np.array(
        [
            np.exp(
                -1j
                * primary.BOOST_PHASE
                * (((bits >> 0) & 1) - ((bits >> 1) & 1))
            )
            for bits in basis
        ],
        dtype=np.complex128,
    )
    state = pulse * state
    state /= np.linalg.norm(state)
    return {
        "basis": basis,
        "currents": currents,
        "numbers": numbers,
        "masks": masks,
        "hamiltonians": hamiltonians,
        "groups": groups,
        "eigenvalues": eigenvalues,
        "eigenvectors": eigenvectors,
        "initial": state,
    }


def baseline_prefixes(fixture: dict[str, object]) -> list[dict[str, object]]:
    groups = fixture["groups"]
    eigenvalues = fixture["eigenvalues"]
    eigenvectors = fixture["eigenvectors"]
    initial = fixture["initial"]
    components = {
        (number, number): group.projector @ initial
        for number, group in enumerate(groups[0])
    }
    propagator = np.eye(len(initial), dtype=np.complex128)
    result: list[dict[str, object]] = []
    for step, dwell in enumerate(primary.DWELLS, start=1):
        dwell_unitary = primary.unitary_from_eigensystem(
            eigenvalues[step - 1], eigenvectors[step - 1], dwell
        )
        propagator = dwell_unitary @ propagator
        minus_components = {
            key: np.exp(-1j * dwell * groups[step - 1][key[1]].energy) * vector
            for key, vector in components.items()
        }
        minus_surface = primary.surface_from_components(
            minus_components, groups[0], groups[step - 1]
        )
        next_components: dict[tuple[int, int], np.ndarray] = {}
        for initial_number in range(len(groups[0])):
            total = sum(
                (
                    vector
                    for (candidate, _), vector in minus_components.items()
                    if candidate == initial_number
                ),
                np.zeros(len(initial), dtype=np.complex128),
            )
            for output_number, output_group in enumerate(groups[step]):
                next_components[(initial_number, output_number)] = output_group.projector @ total
        plus_surface = primary.surface_from_components(next_components, groups[0], groups[step])
        result.append(
            {
                "propagator": propagator.copy(),
                "minus_components": minus_components,
                "plus_components": next_components,
                "minus": minus_surface,
                "plus": plus_surface,
            }
        )
        components = next_components
    return result


def general_shared_density(
    initial_eigen_density: np.ndarray,
    propagator: np.ndarray,
    initial_values: np.ndarray,
    initial_vectors: np.ndarray,
    output_values: np.ndarray,
    output_vectors: np.ndarray,
    *,
    overlap_one: bool = False,
) -> np.ndarray:
    transition = output_vectors.conj().T @ propagator @ initial_vectors
    dimension = len(initial_values)
    output_eigen_density = np.zeros((dimension, dimension), dtype=np.complex128)
    for left_output in range(dimension):
        left_shifts = initial_values - output_values[left_output]
        for right_output in range(dimension):
            right_shifts = initial_values - output_values[right_output]
            if overlap_one:
                kernel = np.ones((dimension, dimension), dtype=float)
            else:
                kernel = primary.sine_overlap(
                    left_shifts[:, np.newaxis] - right_shifts[np.newaxis, :]
                )
            output_eigen_density[left_output, right_output] = np.sum(
                transition[left_output, :, np.newaxis]
                * initial_eigen_density
                * transition[right_output, np.newaxis, :].conj()
                * kernel
            )
    return output_vectors @ output_eigen_density @ output_vectors.conj().T


def reset_event_channel(
    density: np.ndarray,
    input_values: np.ndarray,
    input_vectors: np.ndarray,
    output_values: np.ndarray,
    output_vectors: np.ndarray,
) -> np.ndarray:
    input_density = input_vectors.conj().T @ density @ input_vectors
    change_basis = output_vectors.conj().T @ input_vectors
    dimension = len(input_values)
    output_density = np.zeros((dimension, dimension), dtype=np.complex128)
    for left_output in range(dimension):
        left_shifts = input_values - output_values[left_output]
        for right_output in range(dimension):
            right_shifts = input_values - output_values[right_output]
            kernel = primary.sine_overlap(
                left_shifts[:, np.newaxis] - right_shifts[np.newaxis, :]
            )
            output_density[left_output, right_output] = np.sum(
                change_basis[left_output, :, np.newaxis]
                * input_density
                * change_basis[right_output, np.newaxis, :].conj()
                * kernel
            )
    return output_vectors @ output_density @ output_vectors.conj().T


def reverse_moment_energy(
    components: dict[tuple[int, int], np.ndarray],
    initial_groups: list[primary.SpectralGroup],
    surface_groups: list[primary.SpectralGroup],
) -> float:
    entries = []
    for (initial_number, surface_number), vector in components.items():
        if np.linalg.norm(vector) <= 2.0e-14:
            continue
        shift = initial_groups[initial_number].energy - surface_groups[surface_number].energy
        entries.append((shift, vector))
    result = 0.0 + 0.0j
    for ket_shift, ket_vector in entries:
        for bra_shift, bra_vector in entries:
            wrong_moment = (
                primary.PACKET_MEAN - 0.5 * (ket_shift + bra_shift)
            ) * primary.sine_overlap_scalar(ket_shift - bra_shift)
            result += wrong_moment * np.vdot(bra_vector, ket_vector)
    return float(result.real)


def surface_measure(
    fixture: dict[str, object], density: np.ndarray, step: int, before_event: bool
) -> dict[str, object]:
    index = step - 1 if before_event else step
    return primary.measure(
        density,
        fixture["hamiltonians"][index],
        fixture["masks"][index],
        fixture["currents"],
        fixture["numbers"],
    )


def fourth_largest(values: dict[int, float]) -> float:
    ordered = sorted((abs(value) for value in values.values()), reverse=True)
    return ordered[3]


def mutation_family_checks(
    fixture: dict[str, object], prefixes: list[dict[str, object]]
) -> list[str]:
    lines: list[str] = []

    direct_overlap, _ = primary.direct_packet_integrals(0.2, -0.3)
    x = 0.5 / primary.PACKET_WIDTH
    wrong_overlap = (1.0 - x) * math.cos(math.pi * x)
    b0_residual = abs(direct_overlap - wrong_overlap)
    lines.append(f"MUTATION B0 caught={b0_residual > 2e-11} omit_sine_term_residual={b0_residual:.6e}")

    group = fixture["groups"][0][0]
    wrong_energy = group.energy + 0.125
    b1_residual = primary.max_abs(
        fixture["hamiltonians"][0] @ group.projector - wrong_energy * group.projector
    )
    lines.append(f"MUTATION B1 caught={b1_residual > primary.NUM_TOL} spectral_energy_shift_residual={b1_residual:.6e}")

    wrong_order = (1,) + primary.EDGE_ORDER[1:]
    b2_caught = wrong_order != primary.local_front_order()
    lines.append(f"MUTATION B2 caught={b2_caught} wrong_order={wrong_order}")

    groups = fixture["groups"]
    initial = fixture["initial"]
    wrong_minus = {
        (number, number): np.exp(+1j * primary.DWELLS[0] * group.energy)
        * group.projector
        @ initial
        for number, group in enumerate(groups[0])
    }
    wrong_plus: dict[tuple[int, int], np.ndarray] = {}
    for initial_number in range(len(groups[0])):
        source = wrong_minus[(initial_number, initial_number)]
        for output_number, output_group in enumerate(groups[1]):
            wrong_plus[(initial_number, output_number)] = output_group.projector @ source
    correct_endpoint = primary.endpoint_components(
        initial,
        prefixes[0]["propagator"],
        groups[0],
        groups[1],
    )
    b3_residual = max(
        primary.max_abs(wrong_plus[key] - correct_endpoint[key]) for key in correct_endpoint
    )
    lines.append(f"MUTATION B3 caught={b3_residual > primary.NUM_TOL} reverse_dwell_phase_residual={b3_residual:.6e}")

    output_values = fixture["eigenvalues"][-1].copy()
    output_values[0] += 0.125
    initial_density_eigen = (
        fixture["eigenvectors"][0].conj().T
        @ np.outer(initial, initial.conj())
        @ fixture["eigenvectors"][0]
    )
    wrong_degenerate_density = general_shared_density(
        initial_density_eigen,
        prefixes[-1]["propagator"],
        fixture["eigenvalues"][0],
        fixture["eigenvectors"][0],
        output_values,
        fixture["eigenvectors"][-1],
    )
    b4_residual = np.linalg.norm(wrong_degenerate_density - prefixes[-1]["plus"].density)
    lines.append(f"MUTATION B4 caught={b4_residual > 8e-9} split_degenerate_energy_distance={b4_residual:.6e}")

    initial_energy = float(
        np.vdot(initial, fixture["hamiltonians"][0] @ initial).real
    )
    conserved_total = initial_energy + primary.PACKET_MEAN
    reverse_drifts = []
    for step, prefix in enumerate(prefixes, start=1):
        wrong_battery = reverse_moment_energy(
            prefix["plus_components"], groups[0], groups[step]
        )
        system_energy = float(
            np.trace(prefix["plus"].density @ fixture["hamiltonians"][step]).real
        )
        reverse_drifts.append(abs(system_energy + wrong_battery - conserved_total))
    b5_residual = max(reverse_drifts)
    lines.append(f"MUTATION B5 caught={b5_residual > 1e-8} reverse_shift_ledger_drift={b5_residual:.6e}")

    first_dwell = primary.unitary_from_eigensystem(
        fixture["eigenvalues"][0], fixture["eigenvectors"][0], primary.DWELLS[0]
    )
    initial_density = np.outer(initial, initial.conj())
    wrong_control = first_dwell.conj().T @ initial_density @ first_dwell
    b6_residual = primary.max_abs(prefixes[0]["minus"].density - wrong_control)
    lines.append(f"MUTATION B6 caught={b6_residual > primary.NUM_TOL} anti_dwell_control_residual={b6_residual:.6e}")

    wrong_elapsed = primary.AUDIT_TIMEOUT_SEC + 1.0
    b7_caught = not (
        wrong_elapsed <= primary.AUDIT_TIMEOUT_SEC and 0.0 < primary.RSS_LIMIT_MIB
    )
    lines.append(f"MUTATION B7 caught={b7_caught} synthetic_elapsed={wrong_elapsed:.0f}s scope=predicate_only")

    doubled_density = 2.0 * prefixes[0]["plus"].density
    mutated_density = surface_measure(fixture, doubled_density, 1, before_event=False)
    mutated_densities = mutated_density["densities"]
    p2_caught = not (
        min(mutated_densities) >= primary.DENSITY_LOW
        and max(mutated_densities) <= primary.DENSITY_HIGH
    )
    lines.append(f"MUTATION P2 caught={p2_caught} double_norm_density_range=[{min(mutated_densities):.6f},{max(mutated_densities):.6f}]")

    baseline_post_energies = [
        float(np.trace(prefix["plus"].density @ fixture["hamiltonians"][step]).real)
        for step, prefix in enumerate(prefixes, start=1)
    ]
    offset_energies = [value + 6.0 for value in baseline_post_energies]
    p3_caught = not (max(offset_energies) < -primary.NUM_TOL)
    lines.append(f"MUTATION P3 caught={p3_caught} fixed_plus6_max={max(offset_energies):+.6f} target_remains_Elt0")
    return lines


def physical_variant_lines(
    fixture: dict[str, object], prefixes: list[dict[str, object]]
) -> list[str]:
    initial = fixture["initial"]
    initial_density = np.outer(initial, initial.conj())
    initial_eigen_density = (
        fixture["eigenvectors"][0].conj().T
        @ initial_density
        @ fixture["eigenvectors"][0]
    )
    stationary_eigen_density = np.diag(np.diag(initial_eigen_density))
    stationary_distances = []
    stationary_supports = []
    ideal_distances = []
    ideal_minus_supports = []
    ideal_plus_supports = []
    for step, prefix in enumerate(prefixes, start=1):
        stationary = general_shared_density(
            stationary_eigen_density,
            prefix["propagator"],
            fixture["eigenvalues"][0],
            fixture["eigenvectors"][0],
            fixture["eigenvalues"][step],
            fixture["eigenvectors"][step],
        )
        stationary_distances.append(np.linalg.norm(stationary - prefix["plus"].density))
        stationary_supports.append(
            int(surface_measure(fixture, stationary, step, before_event=False)["support"])
        )
        ideal_plus = general_shared_density(
            initial_eigen_density,
            prefix["propagator"],
            fixture["eigenvalues"][0],
            fixture["eigenvectors"][0],
            fixture["eigenvalues"][step],
            fixture["eigenvectors"][step],
            overlap_one=True,
        )
        ideal_distances.append(np.linalg.norm(ideal_plus - prefix["plus"].density))
        ideal_plus_supports.append(
            int(surface_measure(fixture, ideal_plus, step, before_event=False)["support"])
        )

        previous_output = 0 if step == 1 else step - 1
        before_propagator = prefix["propagator"]
        ideal_minus = general_shared_density(
            initial_eigen_density,
            before_propagator,
            fixture["eigenvalues"][0],
            fixture["eigenvectors"][0],
            fixture["eigenvalues"][previous_output],
            fixture["eigenvectors"][previous_output],
            overlap_one=True,
        )
        ideal_minus_supports.append(
            int(surface_measure(fixture, ideal_minus, step, before_event=True)["support"])
        )

    reset_density = initial_density.copy()
    reset_distances = []
    reset_minus_supports = []
    reset_plus_supports = []
    for step, dwell in enumerate(primary.DWELLS, start=1):
        dwell_unitary = primary.unitary_from_eigensystem(
            fixture["eigenvalues"][step - 1],
            fixture["eigenvectors"][step - 1],
            dwell,
        )
        reset_minus = dwell_unitary @ reset_density @ dwell_unitary.conj().T
        reset_minus_supports.append(
            int(surface_measure(fixture, reset_minus, step, before_event=True)["support"])
        )
        reset_density = reset_event_channel(
            reset_minus,
            fixture["eigenvalues"][step - 1],
            fixture["eigenvectors"][step - 1],
            fixture["eigenvalues"][step],
            fixture["eigenvectors"][step],
        )
        reset_plus_supports.append(
            int(surface_measure(fixture, reset_density, step, before_event=False)["support"])
        )
        reset_distances.append(np.linalg.norm(reset_density - prefixes[step - 1]["plus"].density))

    groups = fixture["groups"]
    initial_energy = float(np.vdot(initial, fixture["hamiltonians"][0] @ initial).real)
    conserved_total = initial_energy + primary.PACKET_MEAN
    reverse_energy_deviations = []
    reverse_ledger_drifts = []
    for step, prefix in enumerate(prefixes, start=1):
        wrong_energy = reverse_moment_energy(prefix["plus_components"], groups[0], groups[step])
        reverse_energy_deviations.append(abs(wrong_energy - prefix["plus"].battery_energy))
        system_energy = float(
            np.trace(prefix["plus"].density @ fixture["hamiltonians"][step]).real
        )
        reverse_ledger_drifts.append(abs(system_energy + wrong_energy - conserved_total))

    return [
        "VARIANT stationary_dephase "
        f"caught={max(stationary_distances) > 1e-6} max_rho_distance={max(stationary_distances):.6e} "
        f"post_supports={stationary_supports}",
        "VARIANT fresh_reset_each_event "
        f"caught={max(reset_distances) > 1e-6} max_rho_distance={max(reset_distances):.6e} "
        f"minus_supports={reset_minus_supports} plus_supports={reset_plus_supports}",
        "VARIANT reverse_shift_battery_moment "
        f"caught={max(reverse_ledger_drifts) > 1e-8} max_EB_deviation={max(reverse_energy_deviations):.6e} "
        f"max_ledger_drift={max(reverse_ledger_drifts):.6e}",
        "VARIANT overlap_one_ideal "
        f"distinct={max(ideal_distances) > 1e-6} max_rho_distance={max(ideal_distances):.6e} "
        f"minus_supports={ideal_minus_supports} plus_supports={ideal_plus_supports} "
        "baseline_failures_remain_visible=P0,P1",
    ]


def ideal_margin_lines(fixture: dict[str, object]) -> list[str]:
    state = fixture["initial"].copy()
    lines = []
    front_values = []
    for step, (edge, dwell) in enumerate(zip(primary.EDGE_ORDER, primary.DWELLS), start=1):
        dwell_unitary = primary.unitary_from_eigensystem(
            fixture["eigenvalues"][step - 1],
            fixture["eigenvectors"][step - 1],
            dwell,
        )
        state = dwell_unitary @ state
        density = np.outer(state, state.conj())
        before = surface_measure(fixture, density, step, before_event=True)
        after = surface_measure(fixture, density, step, before_event=False)
        fourth = fourth_largest(before["currents"])
        front = float(before["currents"][edge])
        front_values.append(abs(front))
        densities = after["densities"]
        ground = float(np.min(fixture["eigenvalues"][step]))
        energy = float(after["energy"])
        lines.append(
            "IDEAL_MARGIN "
            f"k={step} support={int(before['support'])} fourth_absJ={fourth:.6f} "
            f"fourth_margin={fourth - primary.CURRENT_FLOOR:+.6f} front={front:+.6f} "
            f"rho_low_margin={min(densities) - primary.DENSITY_LOW:+.6f} "
            f"rho_high_margin={primary.DENSITY_HIGH - max(densities):+.6f} "
            f"negative_E_margin={-energy:+.6f} fixedN_excess={energy - ground:+.6f}"
        )
    lines.append(
        "IDEAL_MARGIN aggregate "
        f"maxfront={max(front_values):.6f} maxfront_margin={max(front_values) - 0.05:+.6f}"
    )
    return lines


def main() -> int:
    fixture = load_fixture()
    prefixes = baseline_prefixes(fixture)
    lines = []
    lines.extend(physical_variant_lines(fixture, prefixes))
    lines.extend(ideal_margin_lines(fixture))
    lines.extend(mutation_family_checks(fixture, prefixes))
    source_path = Path(__file__)
    lines.append(f"HASH primary={hashlib.sha256(PRIMARY_PATH.read_bytes()).hexdigest()}")
    lines.append(f"HASH scratch={hashlib.sha256(source_path.read_bytes()).hexdigest()}")
    print("\n".join(lines))
    caught = ["caught=True" in line for line in lines if line.startswith("MUTATION")]
    return 0 if caught and all(caught) else 1


if __name__ == "__main__":
    raise SystemExit(main())
