#!/usr/bin/env python3
"""Quantum-link backreaction and overlapping-layer energy checks.

A finite flux link and a two-site charge form an exact local joint unitary:
matter transfer raises/lowers the oriented electric flux, both Gauss
generators commute with the Hamiltonian, and electric work is exactly the
negative change of hopping energy.  On two overlapping bonds, palindromic
colored composition keeps unitarity, Gauss, and reversibility exactly but
conserves the naive summed Hamiltonian only to third order per tick.  Its
principal Floquet generator is exactly conserved and acquires cross-bond
matrix elements.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.linalg import schur


AUDIT_TIMEOUT_SEC = 120

# Actual helper closure plus the declared conditional premise/context closure.
AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_EXACT_MIDPOINT_SOURCE_WORK_CLOSED_DIPOLE_PURE_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_conserved_source_coulomb_photon_bridge_2026_09_03.py",
    "scripts/u1_exact_source_work_closed_dipole_radiation_2026_09_03.py",
    "scripts/u1_finite_step_matter_current_operator_work_interface_2026_09_03.py",
    "scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py",
    "scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py",
    "scripts/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.py",
    "scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py",
    "scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py",
    "scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py",
    "scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py",
    "scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py",
)


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


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def hermitian_exponential(hamiltonian: np.ndarray, step: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    return (
        eigenvectors
        @ np.diag(np.exp(-1.0j * step * eigenvalues))
        @ eigenvectors.conj().T
    )


def flux_shift(spin: int) -> tuple[np.ndarray, np.ndarray]:
    flux = np.diag(np.arange(-spin, spin + 1, dtype=float))
    shift = np.zeros_like(flux, dtype=complex)
    for index in range(2 * spin):
        shift[index + 1, index] = 1.0
    return flux, shift


def matter_transfer(size: int, tail: int, head: int) -> np.ndarray:
    result = np.zeros((size, size), dtype=complex)
    result[head, tail] = 1.0
    return result


def number_operator(size: int, vertex: int) -> np.ndarray:
    result = np.zeros((size, size), dtype=complex)
    result[vertex, vertex] = 1.0
    return result


@dataclass(frozen=True)
class OneBond:
    electric: np.ndarray
    number_tail: np.ndarray
    number_head: np.ndarray
    electric_energy: np.ndarray
    hopping_energy: np.ndarray
    hamiltonian: np.ndarray
    gauss_tail: np.ndarray
    gauss_head: np.ndarray
    shift: np.ndarray


def one_bond_model(spin: int, coupling: float, hopping: float) -> OneBond:
    flux, shift = flux_shift(spin)
    rotor_identity = np.eye(2 * spin + 1, dtype=complex)
    matter_identity = np.eye(2, dtype=complex)
    number_tail_small = number_operator(2, 0)
    number_head_small = number_operator(2, 1)
    forward = matter_transfer(2, 0, 1)

    electric = np.kron(flux, matter_identity)
    number_tail = np.kron(rotor_identity, number_tail_small)
    number_head = np.kron(rotor_identity, number_head_small)
    joint_shift = np.kron(shift, forward)
    electric_energy = 0.5 * coupling * electric @ electric
    hopping_energy = -hopping * (joint_shift + joint_shift.conj().T)
    hamiltonian = electric_energy + hopping_energy
    return OneBond(
        electric=electric,
        number_tail=number_tail,
        number_head=number_head,
        electric_energy=electric_energy,
        hopping_energy=hopping_energy,
        hamiltonian=hamiltonian,
        gauss_tail=-electric - number_tail,
        gauss_head=electric - number_head,
        shift=shift,
    )


@dataclass(frozen=True)
class TwoBond:
    electric_first: np.ndarray
    electric_second: np.ndarray
    numbers: tuple[np.ndarray, ...]
    electric_energy_first: np.ndarray
    electric_energy_second: np.ndarray
    hopping_first: np.ndarray
    hopping_second: np.ndarray
    hamiltonian_first: np.ndarray
    hamiltonian_second: np.ndarray
    hamiltonian: np.ndarray
    gauss: tuple[np.ndarray, ...]


def two_bond_model(
    spin: int,
    coupling: float,
    first_hopping: float,
    second_hopping: float,
    *,
    shared: bool,
) -> TwoBond:
    flux, shift = flux_shift(spin)
    rotor_dimension = 2 * spin + 1
    rotor_identity = np.eye(rotor_dimension, dtype=complex)
    matter_size = 3 if shared else 4
    matter_identity = np.eye(matter_size, dtype=complex)

    electric_first = np.kron(
        np.kron(flux, rotor_identity), matter_identity
    )
    electric_second = np.kron(
        np.kron(rotor_identity, flux), matter_identity
    )
    numbers = tuple(
        np.kron(
            np.kron(rotor_identity, rotor_identity),
            number_operator(matter_size, vertex),
        )
        for vertex in range(matter_size)
    )

    first_tail, first_head = 0, 1
    second_tail, second_head = (1, 2) if shared else (2, 3)
    first_shift = np.kron(
        np.kron(shift, rotor_identity),
        matter_transfer(matter_size, first_tail, first_head),
    )
    second_shift = np.kron(
        np.kron(rotor_identity, shift),
        matter_transfer(matter_size, second_tail, second_head),
    )
    hopping_first = -first_hopping * (
        first_shift + first_shift.conj().T
    )
    hopping_second = -second_hopping * (
        second_shift + second_shift.conj().T
    )
    electric_energy_first = (
        0.5 * coupling * electric_first @ electric_first
    )
    electric_energy_second = (
        0.5 * coupling * electric_second @ electric_second
    )
    hamiltonian_first = electric_energy_first + hopping_first
    hamiltonian_second = electric_energy_second + hopping_second
    hamiltonian = hamiltonian_first + hamiltonian_second

    if shared:
        gauss = (
            -electric_first - numbers[0],
            electric_first - electric_second - numbers[1],
            electric_second - numbers[2],
        )
    else:
        gauss = (
            -electric_first - numbers[0],
            electric_first - numbers[1],
            -electric_second - numbers[2],
            electric_second - numbers[3],
        )
    return TwoBond(
        electric_first=electric_first,
        electric_second=electric_second,
        numbers=numbers,
        electric_energy_first=electric_energy_first,
        electric_energy_second=electric_energy_second,
        hopping_first=hopping_first,
        hopping_second=hopping_second,
        hamiltonian_first=hamiltonian_first,
        hamiltonian_second=hamiltonian_second,
        hamiltonian=hamiltonian,
        gauss=gauss,
    )


def evolved(operator: np.ndarray, unitary: np.ndarray) -> np.ndarray:
    return unitary.conj().T @ operator @ unitary


def spectral_norm(operator: np.ndarray) -> float:
    return float(np.linalg.norm(operator, ord=2))


def principal_floquet_generator(
    unitary: np.ndarray, step: float
) -> np.ndarray:
    triangular, vectors = schur(unitary, output="complex")
    phases = np.angle(np.diag(triangular))
    generator = (
        vectors @ np.diag(-phases / step) @ vectors.conj().T
    )
    return 0.5 * (generator + generator.conj().T)


def local_exchange_residuals(
    electric: np.ndarray,
    number_tail: np.ndarray,
    number_head: np.ndarray,
    electric_energy: np.ndarray,
    hopping_energy: np.ndarray,
    hamiltonian: np.ndarray,
    coupling: float,
    step: float,
) -> tuple[float, float, float, float, float]:
    unitary = hermitian_exponential(hamiltonian, step)
    electric_new = evolved(electric, unitary)
    tail_new = evolved(number_tail, unitary)
    head_new = evolved(number_head, unitary)
    integrated_current = (electric_new - electric) / step
    electric_change = evolved(electric_energy, unitary) - electric_energy
    hopping_change = evolved(hopping_energy, unitary) - hopping_energy
    work = 0.25 * coupling * step * (
        integrated_current @ (electric + electric_new)
        + (electric + electric_new) @ integrated_current
    )
    return (
        spectral_norm(head_new - number_head - step * integrated_current),
        spectral_norm(tail_new - number_tail + step * integrated_current),
        spectral_norm(electric_change - work),
        spectral_norm(hopping_change + work),
        spectral_norm(evolved(hamiltonian, unitary) - hamiltonian),
    )


def main() -> int:
    checks = Checks()
    coupling = 1.3
    hopping = 0.7
    step = 0.4

    shift_algebra_ok = True
    boundary_cost_ok = True
    gauss_generator_ok = True
    component_count_ok = True
    for spin in (1, 2, 3):
        model = one_bond_model(spin, coupling, hopping)
        flux, shift = flux_shift(spin)
        shift_algebra_ok = shift_algebra_ok and bool(
            np.array_equal(commutator(flux, shift), shift)
        )
        boundary_cost_ok = boundary_cost_ok and bool(
            np.max(np.abs(shift.conj().T @ shift - np.eye(2 * spin + 1)))
            == 1.0
            and np.count_nonzero(shift[-1, :]) == 1
            and np.count_nonzero(shift[:, -1]) == 0
        )
        gauss_generator_ok = gauss_generator_ok and bool(
            np.max(
                np.abs(commutator(model.gauss_tail, model.hamiltonian))
            )
            < 1.0e-15
            and np.max(
                np.abs(commutator(model.gauss_head, model.hamiltonian))
            )
            < 1.0e-15
        )
        adjacency = np.abs(model.hopping_energy) > 1.0e-14
        degrees = np.count_nonzero(adjacency, axis=1)
        component_count_ok = component_count_ok and bool(
            np.count_nonzero(degrees == 1) == 4 * spin
            and np.count_nonzero(degrees == 0) == 2
            and np.max(degrees) == 1
        )
    checks.check(
        shift_algebra_ok,
        "the hard-cutoff quantum link obeys [E,U]=U exactly",
    )
    checks.check(
        boundary_cost_ok,
        "finite flux has one explicit nonunitary raising boundary at its top state",
    )
    checks.check(
        gauss_generator_ok,
        "both endpoint Gauss generators commute with every one-bond Hamiltonian",
    )
    checks.check(
        component_count_ok,
        "each finite link decomposes into paired transfer sectors plus two boundary dark states",
    )

    unitary_ok = True
    gauss_evolution_ok = True
    current_ok = True
    work_ok = True
    opposite_work_ok = True
    energy_ok = True
    for spin in (1, 2, 3):
        for local_coupling, local_hopping, local_step in (
            (1.3, 0.7, 0.4),
            (0.8, 0.45, 0.23),
            (1.7, 0.9, 0.17),
        ):
            model = one_bond_model(
                spin, local_coupling, local_hopping
            )
            unitary = hermitian_exponential(
                model.hamiltonian, local_step
            )
            electric_new = evolved(model.electric, unitary)
            current = (electric_new - model.electric) / local_step
            head_current = (
                evolved(model.number_head, unitary) - model.number_head
            ) / local_step
            tail_current = -(
                evolved(model.number_tail, unitary) - model.number_tail
            ) / local_step
            residuals = local_exchange_residuals(
                model.electric,
                model.number_tail,
                model.number_head,
                model.electric_energy,
                model.hopping_energy,
                model.hamiltonian,
                local_coupling,
                local_step,
            )
            unitary_ok = unitary_ok and bool(
                spectral_norm(
                    unitary.conj().T @ unitary
                    - np.eye(unitary.shape[0])
                )
                < 4.0e-15
            )
            gauss_evolution_ok = gauss_evolution_ok and bool(
                spectral_norm(
                    evolved(model.gauss_tail, unitary) - model.gauss_tail
                )
                < 4.0e-15
                and spectral_norm(
                    evolved(model.gauss_head, unitary) - model.gauss_head
                )
                < 4.0e-15
            )
            current_ok = current_ok and bool(
                spectral_norm(current - head_current) < 2.0e-14
                and spectral_norm(current - tail_current) < 2.0e-14
                and spectral_norm(current - current.conj().T) < 2.0e-14
            )
            work_ok = work_ok and residuals[0] < 2.0e-14
            work_ok = work_ok and residuals[1] < 2.0e-14
            work_ok = work_ok and residuals[2] < 2.0e-14
            opposite_work_ok = opposite_work_ok and residuals[3] < 2.0e-14
            energy_ok = energy_ok and residuals[4] < 2.0e-14
    checks.check(
        unitary_ok,
        "the joint matter-flux evolution is unitary throughout the parameter grid",
    )
    checks.check(
        gauss_evolution_ok,
        "the finite joint unitary preserves both endpoint Gauss operators",
    )
    checks.check(
        current_ok,
        "one integrated current equals electric-flux gain and both matter endpoint transfers",
    )
    checks.check(
        work_ok,
        "electric energy gain equals the anticommutator midpoint work",
    )
    checks.check(
        opposite_work_ok,
        "the active matter hopping energy loses exactly the electric work",
    )
    checks.check(
        energy_ok,
        "the complete one-bond matter-plus-electric Hamiltonian is exactly conserved",
    )

    model = one_bond_model(2, coupling, hopping)
    tangent_current = 1.0j * commutator(
        model.hamiltonian, model.electric
    )
    tangent_errors = []
    for trial_step in (0.4, 0.2, 0.1, 0.05):
        unitary = hermitian_exponential(model.hamiltonian, trial_step)
        integrated = (
            evolved(model.electric, unitary) - model.electric
        ) / trial_step
        tangent_errors.append(spectral_norm(integrated - tangent_current))
    checks.check(
        all(
            1.90 < left / right < 2.10
            for left, right in zip(tangent_errors, tangent_errors[1:])
        ),
        "the exact flux current approaches its instantaneous commutator linearly in the step",
    )

    shared = two_bond_model(1, 1.2, 0.7, 0.55, shared=True)
    local_gauss_ok = all(
        spectral_norm(commutator(generator, local_hamiltonian)) < 1.0e-15
        for generator in shared.gauss
        for local_hamiltonian in (
            shared.hamiltonian_first,
            shared.hamiltonian_second,
        )
    )
    checks.check(
        local_gauss_ok,
        "each adjacent bond Hamiltonian commutes with all three shared-vertex Gauss generators",
    )

    first_exchange = local_exchange_residuals(
        shared.electric_first,
        shared.numbers[0],
        shared.numbers[1],
        shared.electric_energy_first,
        shared.hopping_first,
        shared.hamiltonian_first,
        1.2,
        0.31,
    )
    second_exchange = local_exchange_residuals(
        shared.electric_second,
        shared.numbers[1],
        shared.numbers[2],
        shared.electric_energy_second,
        shared.hopping_second,
        shared.hamiltonian_second,
        1.2,
        0.31,
    )
    checks.check(
        max(first_exchange + second_exchange) < 5.0e-15,
        "each operational adjacent-bond layer closes charge and opposite electric work exactly",
    )

    trial_steps = (0.4, 0.2, 0.1, 0.05)
    lie_energy_drifts = []
    strang_energy_drifts = []
    lie_flow_errors = []
    strang_flow_errors = []
    floquet_deviations = []
    floquet_extra_entries = []
    floquet_conservation_ok = True
    exact_flow_ok = True
    gauss_tick_ok = True
    reversal_ok = True
    for trial_step in trial_steps:
        first_full = hermitian_exponential(
            shared.hamiltonian_first, trial_step
        )
        second_full = hermitian_exponential(
            shared.hamiltonian_second, trial_step
        )
        first_half = hermitian_exponential(
            shared.hamiltonian_first, 0.5 * trial_step
        )
        lie_tick = second_full @ first_full
        strang_tick = first_half @ second_full @ first_half
        exact_tick = hermitian_exponential(shared.hamiltonian, trial_step)

        lie_energy_drifts.append(
            spectral_norm(
                evolved(shared.hamiltonian, lie_tick) - shared.hamiltonian
            )
        )
        strang_energy_drifts.append(
            spectral_norm(
                evolved(shared.hamiltonian, strang_tick)
                - shared.hamiltonian
            )
        )
        lie_flow_errors.append(spectral_norm(lie_tick - exact_tick))
        strang_flow_errors.append(spectral_norm(strang_tick - exact_tick))
        exact_flow_ok = exact_flow_ok and bool(
            spectral_norm(
                evolved(shared.hamiltonian, exact_tick)
                - shared.hamiltonian
            )
            < 5.0e-15
        )
        gauss_tick_ok = gauss_tick_ok and all(
            spectral_norm(evolved(generator, strang_tick) - generator)
            < 5.0e-15
            for generator in shared.gauss
        )
        negative_first_half = hermitian_exponential(
            shared.hamiltonian_first, -0.5 * trial_step
        )
        negative_second = hermitian_exponential(
            shared.hamiltonian_second, -trial_step
        )
        reverse_tick = (
            negative_first_half @ negative_second @ negative_first_half
        )
        reversal_ok = reversal_ok and bool(
            spectral_norm(reverse_tick @ strang_tick - np.eye(27))
            < 5.0e-15
        )

        floquet = principal_floquet_generator(strang_tick, trial_step)
        floquet_conservation_ok = floquet_conservation_ok and bool(
            spectral_norm(evolved(floquet, strang_tick) - floquet)
            < 7.0e-15
            and spectral_norm(floquet - floquet.conj().T) < 2.0e-15
        )
        floquet_deviations.append(
            spectral_norm(floquet - shared.hamiltonian)
        )
        zero_mask = np.abs(shared.hamiltonian) < 1.0e-14
        floquet_extra_entries.append(float(np.max(np.abs(floquet[zero_mask]))))

    checks.check(
        gauss_tick_ok and reversal_ok,
        "the palindromic adjacent-bond tick is exactly Gauss preserving and reversible",
    )
    checks.check(
        exact_flow_ok,
        "the unsplit two-bond exponential exactly conserves the summed Hamiltonian",
    )
    checks.check(
        all(
            3.8 < left / right < 4.2
            for left, right in zip(lie_energy_drifts, lie_energy_drifts[1:])
        )
        and lie_energy_drifts[0] > 0.04,
        "a nonpalindromic two-color product has a quadratic one-tick energy drift",
    )
    checks.check(
        all(
            7.8 < left / right < 8.2
            for left, right in zip(
                strang_energy_drifts, strang_energy_drifts[1:]
            )
        )
        and strang_energy_drifts[0] < 0.005,
        "the palindromic two-color product suppresses summed-energy drift to cubic order",
    )
    checks.check(
        all(
            3.8 < left / right < 4.2
            for left, right in zip(lie_flow_errors, lie_flow_errors[1:])
        )
        and all(
            7.8 < left / right < 8.2
            for left, right in zip(strang_flow_errors, strang_flow_errors[1:])
        ),
        "Lie and palindromic products approach the exact joint flow at orders two and three",
    )
    checks.check(
        floquet_conservation_ok,
        "the principal palindromic Floquet generator is Hermitian and exactly conserved",
    )
    checks.check(
        all(
            3.9 < left / right < 4.1
            for left, right in zip(
                floquet_deviations, floquet_deviations[1:]
            )
        ),
        "the conserved Floquet generator differs from the summed Hamiltonian at quadratic order",
    )
    checks.check(
        all(value > 5.0e-5 for value in floquet_extra_entries)
        and all(
            3.9 < left / right < 4.1
            for left, right in zip(
                floquet_extra_entries, floquet_extra_entries[1:]
            )
        ),
        "the exact Floquet energy acquires resolved cross-bond entries at quadratic order",
    )

    disjoint = two_bond_model(1, 1.2, 0.7, 0.55, shared=False)
    disjoint_step = 0.4
    disjoint_first = hermitian_exponential(
        disjoint.hamiltonian_first, disjoint_step
    )
    disjoint_second = hermitian_exponential(
        disjoint.hamiltonian_second, disjoint_step
    )
    disjoint_product = disjoint_second @ disjoint_first
    disjoint_exact = hermitian_exponential(
        disjoint.hamiltonian, disjoint_step
    )
    checks.check(
        spectral_norm(
            commutator(
                disjoint.hamiltonian_first,
                disjoint.hamiltonian_second,
            )
        )
        < 1.0e-15
        and spectral_norm(disjoint_product - disjoint_exact) < 5.0e-15
        and spectral_norm(
            evolved(disjoint.hamiltonian, disjoint_product)
            - disjoint.hamiltonian
        )
        < 5.0e-15,
        "disjoint colored bonds commute and conserve the summed energy exactly",
    )

    shared_commutator = spectral_norm(
        commutator(
            shared.hamiltonian_first, shared.hamiltonian_second
        )
    )
    inactive_hop_change = spectral_norm(
        evolved(
            shared.hopping_second,
            hermitian_exponential(shared.hamiltonian_first, 0.4),
        )
        - shared.hopping_second
    )
    checks.check(
        shared_commutator > 0.3 and inactive_hop_change > 0.1,
        "shared matter makes neighboring bond energies noncommute and exposes the splitting residual",
    )

    print(
        "per_element: finite flux raising, matter transfer, current, and anticommutator work are checked"
    )
    print(
        "per_site: both endpoint Gauss generators and the shared middle-vertex generator are checked"
    )
    print(
        "per_mode: instantaneous-current and Lie/Strang/Floquet refinement orders are resolved"
    )
    print(
        "per_block: one-bond exact backreaction and two-bond overlapping/disjoint controls are checked"
    )
    print(
        "lattice_wide: colored local layers preserve Gauss by composition; exact summed energy versus Floquet energy remains the global schedule choice"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
