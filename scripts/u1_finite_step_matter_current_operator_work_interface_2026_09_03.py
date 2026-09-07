#!/usr/bin/env python3
"""Finite-step charged-hop current and operator-valued field-work checks.

An instantaneous matter current i[H,n] is not the exact current of a finite
tick.  For a local bond unitary V, the step-integrated oriented current is

    Jbar = (V^dagger n_head V - n_head) / h.

It obeys exact endpoint continuity, composes layer by layer on overlapping
bonds, and preserves the electric Gauss residual when used in the sourced
field shear.  For noncommuting operator currents, the field-work theorem is
the anticommutator midpoint law rather than the classical ordered product.
"""

from __future__ import annotations

import math

import numpy as np

from u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03 import (
    curl_symbol,
)


AUDIT_TIMEOUT_SEC = 120

# Actual helper closure plus the declared conditional premise/context closure.
AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_EXACT_MIDPOINT_SOURCE_WORK_CLOSED_DIPOLE_PURE_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_conserved_source_coulomb_photon_bridge_2026_09_03.py",
    "scripts/u1_exact_source_work_closed_dipole_radiation_2026_09_03.py",
    "scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py",
    "scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py",
    "scripts/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.py",
    "scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py",
    "scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py",
    "scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py",
    "scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py",
    "scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py",
)


IDENTITY_2 = np.eye(2, dtype=complex)
PAULI_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
PAULI_Y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
PAULI_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
NUMBER_TAIL = 0.5 * (IDENTITY_2 + PAULI_Z)
NUMBER_HEAD = 0.5 * (IDENTITY_2 - PAULI_Z)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, condition: bool, label: str) -> None:
        if condition:
            self.passed += 1
            print(f"[PASS] {self.passed + self.failed:02d} {label}")
        else:
            self.failed += 1
            print(f"[FAIL] {self.passed + self.failed:02d} {label}")


def bond_hamiltonian(phase: float, hopping: float) -> np.ndarray:
    """One-particle charged hop on an oriented tail-to-head link."""

    return -hopping * (
        math.cos(phase) * PAULI_X + math.sin(phase) * PAULI_Y
    )


def bond_unitary(phase: float, hopping: float, step: float) -> np.ndarray:
    direction = math.cos(phase) * PAULI_X + math.sin(phase) * PAULI_Y
    angle = hopping * step
    return math.cos(angle) * IDENTITY_2 + 1.0j * math.sin(angle) * direction


def instantaneous_current(phase: float, hopping: float) -> np.ndarray:
    hamiltonian = bond_hamiltonian(phase, hopping)
    return 1.0j * (
        hamiltonian @ NUMBER_HEAD - NUMBER_HEAD @ hamiltonian
    )


def integrated_current(phase: float, hopping: float, step: float) -> np.ndarray:
    unitary = bond_unitary(phase, hopping, step)
    return (
        unitary.conj().T @ NUMBER_HEAD @ unitary - NUMBER_HEAD
    ) / step


def analytic_integrated_current(
    phase: float, hopping: float, step: float
) -> np.ndarray:
    tangent_direction = (
        math.cos(phase) * PAULI_Y - math.sin(phase) * PAULI_X
    )
    angle = 2.0 * hopping * step
    return (
        math.sin(angle) * tangent_direction
        + (1.0 - math.cos(angle)) * PAULI_Z
    ) / (2.0 * step)


def hermitian_exponential(hamiltonian: np.ndarray, step: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    return (
        eigenvectors
        @ np.diag(np.exp(-1.0j * step * eigenvalues))
        @ eigenvectors.conj().T
    )


def embedded_bond_hamiltonian(
    size: int,
    tail: int,
    head: int,
    phase: float,
    hopping: float,
) -> np.ndarray:
    result = np.zeros((size, size), dtype=complex)
    result[head, tail] = -hopping * np.exp(1.0j * phase)
    result[tail, head] = -hopping * np.exp(-1.0j * phase)
    return result


def zero_operator(dimension: int = 2) -> np.ndarray:
    return np.zeros((dimension, dimension), dtype=complex)


def linear_operator_map(
    coefficients: np.ndarray, operators: list[np.ndarray]
) -> list[np.ndarray]:
    return [
        sum(
            (
                coefficients[row, column] * operators[column]
                for column in range(len(operators))
            ),
            zero_operator(operators[0].shape[0]),
        )
        for row in range(coefficients.shape[0])
    ]


def combine_operators(
    first: list[np.ndarray],
    second: list[np.ndarray],
    first_coefficient: float = 1.0,
    second_coefficient: float = 1.0,
) -> list[np.ndarray]:
    return [
        first_coefficient * left + second_coefficient * right
        for left, right in zip(first, second)
    ]


def sourced_operator_tick(
    curl: np.ndarray,
    electric: list[np.ndarray],
    magnetic: list[np.ndarray],
    current: list[np.ndarray],
    step: float,
) -> tuple[list[np.ndarray], list[np.ndarray]]:
    magnetic_half = combine_operators(
        magnetic,
        linear_operator_map(curl, electric),
        second_coefficient=0.5 * step,
    )
    electric_new = combine_operators(
        combine_operators(
            electric,
            linear_operator_map(curl.T, magnetic_half),
            second_coefficient=-step,
        ),
        current,
        second_coefficient=step,
    )
    magnetic_new = combine_operators(
        magnetic_half,
        linear_operator_map(curl, electric_new),
        second_coefficient=0.5 * step,
    )
    return electric_new, magnetic_new


def operator_field_energy(
    curl: np.ndarray,
    electric: list[np.ndarray],
    magnetic: list[np.ndarray],
    step: float,
) -> np.ndarray:
    dimension = electric[0].shape[0]
    curl_electric = linear_operator_map(curl, electric)
    squares = sum(
        (operator @ operator for operator in electric + magnetic),
        zero_operator(dimension),
    )
    curl_squares = sum(
        (operator @ operator for operator in curl_electric),
        zero_operator(dimension),
    )
    return 0.5 * squares - step**2 * curl_squares / 8.0


def symmetrized_operator_work(
    electric_old: list[np.ndarray],
    electric_new: list[np.ndarray],
    current: list[np.ndarray],
    step: float,
) -> np.ndarray:
    dimension = electric_old[0].shape[0]
    return 0.25 * step * sum(
        (
            current[index] @ (electric_old[index] + electric_new[index])
            + (electric_old[index] + electric_new[index]) @ current[index]
            for index in range(len(current))
        ),
        zero_operator(dimension),
    )


def cubic_colored_schedule(
    size: int, step: float
) -> tuple[bool, bool, bool]:
    """Check six matching layers and their integrated continuity on a torus."""

    vertices = tuple(
        (first, second, third)
        for first in range(size)
        for second in range(size)
        for third in range(size)
    )
    vertex_index = {point: index for index, point in enumerate(vertices)}
    edges: list[tuple[int, int, int, int, float, float]] = []
    for tail_point in vertices:
        for axis in range(3):
            head_point_list = list(tail_point)
            head_point_list[axis] = (head_point_list[axis] + 1) % size
            head_point = tuple(head_point_list)
            edge_number = len(edges)
            phase = 0.031 * (1 + (7 * edge_number) % 19)
            hopping = 0.22 + 0.01 * ((5 * edge_number) % 11)
            edges.append(
                (
                    vertex_index[tail_point],
                    vertex_index[head_point],
                    axis,
                    tail_point[axis] % 2,
                    phase,
                    hopping,
                )
            )

    matching_ok = len(edges) == 3 * size**3
    colors = tuple((axis, parity) for axis in range(3) for parity in range(2))
    for color in colors:
        color_edges = [edge for edge in edges if edge[2:4] == color]
        endpoints = [
            endpoint for edge in color_edges for endpoint in edge[:2]
        ]
        matching_ok = matching_ok and (
            len(color_edges) == size**3 // 2
            and len(endpoints) == len(set(endpoints)) == size**3
        )

    dimension = len(vertices)
    identity = np.eye(dimension, dtype=complex)
    number_operators = tuple(
        np.diag(
            [1.0 if index == vertex else 0.0 for index in range(dimension)]
        ).astype(complex)
        for vertex in range(dimension)
    )
    complete_unitary = identity.copy()
    divergence_increments = [
        zero_operator(dimension) for _vertex in range(dimension)
    ]
    operational_locality_ok = True

    for color in colors:
        layer_unitary = identity.copy()
        layer_currents: list[tuple[int, int, np.ndarray]] = []
        for tail, head, axis, parity, phase, hopping in edges:
            if (axis, parity) != color:
                continue
            local_unitary = bond_unitary(phase, hopping, step)
            layer_unitary[np.ix_((tail, head), (tail, head))] = local_unitary
            local_current = integrated_current(phase, hopping, step)
            current_operator = zero_operator(dimension)
            current_operator[np.ix_((tail, head), (tail, head))] = local_current
            outside = current_operator.copy()
            outside[np.ix_((tail, head), (tail, head))] = 0.0
            operational_locality_ok = operational_locality_ok and bool(
                np.max(np.abs(outside)) < 1.0e-15
            )
            layer_currents.append((tail, head, current_operator))

        for tail, head, current_operator in layer_currents:
            initial_current = (
                complete_unitary.conj().T
                @ current_operator
                @ complete_unitary
            )
            divergence_increments[tail] -= step * initial_current
            divergence_increments[head] += step * initial_current
        complete_unitary = layer_unitary @ complete_unitary

    continuity_ok = bool(
        np.max(
            np.abs(complete_unitary.conj().T @ complete_unitary - identity)
        )
        < 2.0e-14
    )
    for vertex in range(dimension):
        number_new = (
            complete_unitary.conj().T
            @ number_operators[vertex]
            @ complete_unitary
        )
        continuity_ok = continuity_ok and bool(
            np.max(
                np.abs(
                    number_new
                    - number_operators[vertex]
                    - divergence_increments[vertex]
                )
            )
            < 3.0e-14
        )
    return matching_ok, operational_locality_ok, continuity_ok


def main() -> int:
    checks = Checks()

    phases = (-1.1, -0.2, 0.0, 0.7, 1.9)
    hoppings = (0.25, 0.7, 1.1)
    steps = (0.1, 0.3, 0.55)
    unitary_ok = True
    conservation_ok = True
    continuity_ok = True
    current_ok = True
    formula_ok = True
    for phase in phases:
        for hopping in hoppings:
            for step in steps:
                hamiltonian = bond_hamiltonian(phase, hopping)
                unitary = bond_unitary(phase, hopping, step)
                current = integrated_current(phase, hopping, step)
                number_tail_new = (
                    unitary.conj().T @ NUMBER_TAIL @ unitary
                )
                number_head_new = (
                    unitary.conj().T @ NUMBER_HEAD @ unitary
                )
                unitary_ok = unitary_ok and bool(
                    np.max(
                        np.abs(unitary.conj().T @ unitary - IDENTITY_2)
                    )
                    < 2.0e-15
                    and np.max(np.abs(hamiltonian - hamiltonian.conj().T))
                    < 2.0e-15
                )
                conservation_ok = conservation_ok and bool(
                    np.max(
                        np.abs(
                            number_tail_new
                            + number_head_new
                            - NUMBER_TAIL
                            - NUMBER_HEAD
                        )
                    )
                    < 3.0e-15
                )
                continuity_ok = continuity_ok and bool(
                    np.max(
                        np.abs(
                            number_tail_new - NUMBER_TAIL + step * current
                        )
                    )
                    < 3.0e-15
                    and np.max(
                        np.abs(
                            number_head_new - NUMBER_HEAD - step * current
                        )
                    )
                    < 3.0e-15
                )
                current_ok = current_ok and bool(
                    np.max(np.abs(current - current.conj().T)) < 2.0e-15
                    and abs(np.trace(current)) < 2.0e-15
                )
                formula_ok = formula_ok and bool(
                    np.max(
                        np.abs(
                            current
                            - analytic_integrated_current(
                                phase, hopping, step
                            )
                        )
                    )
                    < 3.0e-15
                )
    checks.check(
        unitary_ok,
        "every charged bond Hamiltonian is Hermitian and every finite hop is unitary",
    )
    checks.check(
        conservation_ok,
        "the finite bond hop conserves total matter charge exactly",
    )
    checks.check(
        continuity_ok,
        "the integrated oriented current obeys exact endpoint continuity",
    )
    checks.check(
        current_ok,
        "the finite-step current is Hermitian and traceless throughout the grid",
    )
    checks.check(
        formula_ok,
        "the analytic sine-cosine current formula matches the unitary definition",
    )

    phase = 0.37
    hopping = 0.7
    tangent = instantaneous_current(phase, hopping)
    midpoint_errors = []
    endpoint_errors = []
    for step in (0.4, 0.2, 0.1, 0.05):
        current = integrated_current(phase, hopping, step)
        half_unitary = bond_unitary(phase, hopping, 0.5 * step)
        midpoint_current = half_unitary.conj().T @ tangent @ half_unitary
        midpoint_errors.append(float(np.linalg.norm(current - midpoint_current)))
        endpoint_errors.append(float(np.linalg.norm(current - tangent)))
    checks.check(
        all(
            3.95 < left / right < 4.05
            for left, right in zip(midpoint_errors, midpoint_errors[1:])
        ),
        "the exact integrated current approaches the midpoint current quadratically",
    )
    checks.check(
        all(
            1.95 < left / right < 2.05
            for left, right in zip(endpoint_errors, endpoint_errors[1:])
        ),
        "using the instantaneous endpoint current instead leaves a first-order tick error",
    )
    checks.check(
        np.linalg.norm(
            integrated_current(phase, hopping, 0.4) - tangent
        )
        > 0.25,
        "the finite-step correction is nonzero at a resolved tick and cannot be dropped",
    )

    gauge_ok = True
    for phase, alpha_tail, alpha_head in (
        (0.37, 0.23, -0.51),
        (-0.8, -0.4, 0.6),
        (1.2, 0.9, -0.2),
    ):
        transformed_phase = phase + alpha_head - alpha_tail
        gauge = np.diag(
            np.exp(1.0j * np.array((alpha_tail, alpha_head)))
        )
        original_hamiltonian = bond_hamiltonian(phase, hopping)
        transformed_hamiltonian = bond_hamiltonian(
            transformed_phase, hopping
        )
        original_current = integrated_current(phase, hopping, 0.41)
        transformed_current = integrated_current(
            transformed_phase, hopping, 0.41
        )
        gauge_ok = gauge_ok and bool(
            np.max(
                np.abs(
                    transformed_hamiltonian
                    - gauge @ original_hamiltonian @ gauge.conj().T
                )
            )
            < 3.0e-15
            and np.max(
                np.abs(
                    transformed_current
                    - gauge @ original_current @ gauge.conj().T
                )
            )
            < 3.0e-15
        )
    checks.check(
        gauge_ok,
        "the finite-step current covaries with the charged hop under endpoint gauge phases",
    )

    swap = PAULI_X
    orientation_ok = True
    for phase in phases:
        current = integrated_current(phase, 0.7, 0.41)
        reversed_current = integrated_current(-phase, 0.7, 0.41)
        orientation_ok = orientation_ok and bool(
            np.max(
                np.abs(swap @ current @ swap + reversed_current)
            )
            < 4.0e-15
        )
    checks.check(
        orientation_ok,
        "reversing the bond orientation reverses the integrated current",
    )
    checks.check(
        np.array_equal(
            integrated_current(0.9, 0.0, 0.37), zero_operator()
        ),
        "a zero hopping coefficient produces exactly zero finite-step current",
    )

    # Two colored layers on an open three-site chain.  The second operational
    # current is local on sites 1-2; its initial Heisenberg representative is
    # pulled through the first layer when the two increments are aggregated.
    dimension = 3
    number = tuple(
        np.diag(
            [1.0 if index == vertex else 0.0 for index in range(dimension)]
        ).astype(complex)
        for vertex in range(dimension)
    )
    layer_step = 0.4
    first_hamiltonian = embedded_bond_hamiltonian(
        dimension, 0, 1, 0.2, 0.7
    )
    second_hamiltonian = embedded_bond_hamiltonian(
        dimension, 1, 2, -0.3, 0.5
    )
    first_unitary = hermitian_exponential(first_hamiltonian, layer_step)
    second_unitary = hermitian_exponential(second_hamiltonian, layer_step)
    complete_unitary = second_unitary @ first_unitary
    first_current = (
        first_unitary.conj().T @ number[1] @ first_unitary - number[1]
    ) / layer_step
    second_current_operational = (
        second_unitary.conj().T @ number[2] @ second_unitary - number[2]
    ) / layer_step
    second_current_initial = (
        first_unitary.conj().T
        @ second_current_operational
        @ first_unitary
    )
    incidence = np.array([[-1, 1, 0], [0, -1, 1]], dtype=int)
    initial_currents = (first_current, second_current_initial)
    layered_continuity_ok = True
    for vertex in range(dimension):
        number_new = (
            complete_unitary.conj().T
            @ number[vertex]
            @ complete_unitary
        )
        divergence_current = layer_step * sum(
            (
                incidence[edge, vertex] * initial_currents[edge]
                for edge in range(2)
            ),
            zero_operator(dimension),
        )
        layered_continuity_ok = layered_continuity_ok and bool(
            np.max(
                np.abs(number_new - number[vertex] - divergence_current)
            )
            < 4.0e-15
        )
    checks.check(
        np.max(
            np.abs(
                complete_unitary.conj().T
                @ complete_unitary
                - np.eye(dimension)
            )
        )
        < 3.0e-15,
        "two overlapping colored bond layers compose to an exact unitary",
    )
    checks.check(
        layered_continuity_ok,
        "the two-layer three-site hop obeys exact finite-step continuity at every vertex",
    )
    checks.check(
        np.max(
            np.abs(
                complete_unitary.conj().T
                @ sum(number)
                @ complete_unitary
                - sum(number)
            )
        )
        < 3.0e-15,
        "the colored matter schedule preserves total charge",
    )

    gauss_ok = True
    for vertex in range(dimension):
        electric_new_divergence = layer_step * sum(
            (
                incidence[edge, vertex] * initial_currents[edge]
                for edge in range(2)
            ),
            zero_operator(dimension),
        )
        matter_new = (
            complete_unitary.conj().T
            @ number[vertex]
            @ complete_unitary
        )
        initial_gauss_residual = -number[vertex]
        final_gauss_residual = electric_new_divergence - matter_new
        gauss_ok = gauss_ok and bool(
            np.max(
                np.abs(final_gauss_residual - initial_gauss_residual)
            )
            < 4.0e-15
        )
    checks.check(
        gauss_ok,
        "using the integrated layer currents preserves the electric Gauss residual exactly",
    )

    first_local = first_current.copy()
    first_local[0:2, 0:2] = 0.0
    second_local = second_current_operational.copy()
    second_local[1:3, 1:3] = 0.0
    checks.check(
        np.max(np.abs(first_local)) < 2.0e-15
        and np.max(np.abs(second_local)) < 2.0e-15,
        "each operational current is confined to its active two-site bond layer",
    )
    checks.check(
        abs(second_current_initial[0, 2]) > 0.1
        and abs(second_current_operational[0, 2]) < 2.0e-15,
        "aggregating layers in the initial frame spreads support, so local field coupling must follow the layers",
    )

    matching_ok, cubic_locality_ok, cubic_continuity_ok = (
        cubic_colored_schedule(4, 0.2)
    )
    checks.check(
        matching_ok and cubic_locality_ok,
        "the L=4 cubic torus decomposes all 192 bonds into six local matching layers",
    )
    checks.check(
        cubic_continuity_ok,
        "the six-layer cubic matter tick obeys finite-step continuity at all 64 vertices",
    )

    # Noncommuting operator-valued version of the exact source-work law.
    field_step = 0.5
    curl = curl_symbol(np.array([0.3, 0.7, 1.1]))
    electric_old = [
        0.2 * PAULI_X + 0.1 * PAULI_Z,
        -0.3 * PAULI_Y + 0.2 * PAULI_Z,
        0.4 * PAULI_X - 0.2 * PAULI_Y,
    ]
    magnetic_old = [
        0.1 * PAULI_Y + 0.3 * PAULI_Z,
        -0.5 * PAULI_X + 0.2 * PAULI_Y,
        0.2 * IDENTITY_2 - 0.1 * PAULI_Z,
    ]
    operator_current = [
        integrated_current(0.37, 0.7, field_step),
        -0.4 * PAULI_Y + 0.1 * PAULI_Z,
        0.2 * PAULI_X + 0.4 * PAULI_Z,
    ]
    electric_new, magnetic_new = sourced_operator_tick(
        curl,
        electric_old,
        magnetic_old,
        operator_current,
        field_step,
    )
    energy_change = operator_field_energy(
        curl, electric_new, magnetic_new, field_step
    ) - operator_field_energy(
        curl, electric_old, magnetic_old, field_step
    )
    symmetric_work = symmetrized_operator_work(
        electric_old, electric_new, operator_current, field_step
    )
    checks.check(
        np.max(np.abs(energy_change - symmetric_work)) < 3.0e-15,
        "the field-energy change equals anticommutator midpoint work for noncommuting currents",
    )
    checks.check(
        np.max(np.abs(symmetric_work - symmetric_work.conj().T)) < 3.0e-15,
        "the symmetrized operator work is Hermitian",
    )

    ordered_work = 0.5 * field_step * sum(
        (
            operator_current[index]
            @ (electric_old[index] + electric_new[index])
            for index in range(3)
        ),
        zero_operator(),
    )
    checks.check(
        np.max(np.abs(energy_change - ordered_work)) > 0.04
        and np.max(np.abs(ordered_work - ordered_work.conj().T)) > 0.08,
        "the unsymmetrized classical product fails as a noncommuting work observable",
    )

    commuting_current = [
        0.3 * IDENTITY_2,
        -0.2 * IDENTITY_2,
        0.4 * IDENTITY_2,
    ]
    commuting_electric = [
        0.1 * IDENTITY_2,
        -0.5 * IDENTITY_2,
        0.2 * IDENTITY_2,
    ]
    commuting_magnetic = [
        -0.3 * IDENTITY_2,
        0.4 * IDENTITY_2,
        0.6 * IDENTITY_2,
    ]
    commuting_new_electric, commuting_new_magnetic = sourced_operator_tick(
        curl,
        commuting_electric,
        commuting_magnetic,
        commuting_current,
        field_step,
    )
    commuting_change = operator_field_energy(
        curl,
        commuting_new_electric,
        commuting_new_magnetic,
        field_step,
    ) - operator_field_energy(
        curl, commuting_electric, commuting_magnetic, field_step
    )
    commuting_symmetric = symmetrized_operator_work(
        commuting_electric,
        commuting_new_electric,
        commuting_current,
        field_step,
    )
    checks.check(
        np.max(np.abs(commuting_change - commuting_symmetric)) < 2.0e-15
        and np.max(
            np.abs(
                commuting_symmetric
                - 0.5
                * field_step
                * sum(
                    (
                        commuting_current[index]
                        @ (
                            commuting_electric[index]
                            + commuting_new_electric[index]
                        )
                        for index in range(3)
                    ),
                    zero_operator(),
                )
            )
        )
        < 2.0e-15,
        "commuting field and current operators reduce to the classical midpoint law",
    )

    state = np.array([1.0, 1.0j], dtype=complex) / math.sqrt(2.0)
    checks.check(
        abs(
            float(np.real(state.conj().T @ energy_change @ state))
            - float(np.real(state.conj().T @ symmetric_work @ state))
        )
        < 2.0e-15,
        "the operator work identity agrees in a nontrivial matter-state expectation value",
    )

    print(
        "per_element: the oriented bond phase, finite current, and operator anticommutator coefficients are checked"
    )
    print(
        "per_site: exact tail/head continuity and each operational two-site current support are checked"
    )
    print(
        "per_mode: instantaneous, midpoint, and integrated current orders are separated on a refinement ladder"
    )
    print(
        "per_block: one-bond gauge covariance, three-site colored continuity, Gauss preservation, and operator work are checked"
    )
    print(
        "lattice_wide: the layerwise construction generalizes by finite edge coloring; no global solve or all-at-once current is used"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
