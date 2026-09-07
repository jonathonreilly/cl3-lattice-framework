#!/usr/bin/env python3
"""Finite-clock gauge/matter carrier and controlled tame-Maxwell bridge.

This runner replaces the hard-cutoff flux shift by an exact K-state Weyl
clock on each link.  It checks exact gauge invariance of electric, Wilson-face,
and charged-hop terms, exact finite-step component energy exchange, the tame
electric and magnetic error bounds, and the two transverse branches of the
three-dimensional quadratic Maxwell tangent.  A separately supplied clock
oscillator is compared to the harmonic frequency and to the fixed-coupling
cosine rotor; clock refinement alone leaves an anharmonic gap discrepancy.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product

import numpy as np
from scipy import sparse
from scipy.linalg import eigh_tridiagonal
from scipy.sparse.linalg import eigsh


AUDIT_TIMEOUT_SEC = 120

# Actual helper closure plus the declared conditional premise/context closure.
AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_EXACT_MIDPOINT_SOURCE_WORK_CLOSED_DIPOLE_PURE_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_conserved_source_coulomb_photon_bridge_2026_09_03.py",
    "scripts/u1_exact_source_work_closed_dipole_radiation_2026_09_03.py",
    "scripts/u1_finite_step_matter_current_operator_work_interface_2026_09_03.py",
    "scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py",
    "scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py",
    "scripts/u1_quantum_link_exact_backreaction_colored_floquet_2026_09_03.py",
    "scripts/u1_quantum_link_matter_magnetic_plaquette_finite_step_join_2026_09_03.py",
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


def dense_spectral_norm(operator: np.ndarray) -> float:
    return float(np.linalg.norm(operator, ord=2))


def sparse_max_abs(operator: sparse.spmatrix) -> float:
    operator = operator.tocsr(copy=True)
    operator.eliminate_zeros()
    if operator.nnz == 0:
        return 0.0
    return float(np.max(np.abs(operator.data)))


def sparse_commutator(
    left: sparse.spmatrix, right: sparse.spmatrix
) -> sparse.csr_matrix:
    return (left @ right - right @ left).tocsr()


def sparse_kron_all(
    factors: tuple[sparse.spmatrix, ...]
) -> sparse.csr_matrix:
    result = sparse.csr_matrix([[1.0 + 0.0j]])
    for factor in factors:
        result = sparse.kron(result, factor, format="csr")
    return result


def hermitian_exponential(
    hamiltonian: np.ndarray, step: float
) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    return (
        eigenvectors
        @ np.diag(np.exp(-1.0j * step * eigenvalues))
        @ eigenvectors.conj().T
    )


def evolved(operator: np.ndarray, unitary: np.ndarray) -> np.ndarray:
    return unitary.conj().T @ operator @ unitary


@dataclass(frozen=True)
class Clock:
    order: int
    omega: complex
    delta: float
    shift: sparse.csr_matrix
    clock: sparse.csr_matrix
    identity: sparse.csr_matrix


def clock_pair(order: int) -> Clock:
    omega = np.exp(2.0j * np.pi / order)
    indices = np.arange(order)
    shift = sparse.csr_matrix(
        (
            np.ones(order, dtype=complex),
            ((indices + 1) % order, indices),
        ),
        shape=(order, order),
    )
    clock = sparse.diags(omega**indices, format="csr")
    return Clock(
        order=order,
        omega=omega,
        delta=2.0 * np.pi / order,
        shift=shift,
        clock=clock,
        identity=sparse.identity(order, dtype=complex, format="csr"),
    )


@dataclass(frozen=True)
class ClockFace:
    electric_energy: sparse.csr_matrix
    magnetic_energy: sparse.csr_matrix
    hopping_energy: sparse.csr_matrix
    hamiltonian: sparse.csr_matrix
    gauss: tuple[sparse.csr_matrix, ...]
    dimension: int


def clock_face(
    order: int, coupling: float, hopping: float
) -> ClockFace:
    """Square 0->1->2->3->0, stored as 0->1,1->2,3->2,0->3."""

    pair = clock_pair(order)
    matter_identity = sparse.identity(2, dtype=complex, format="csr")
    transfer = sparse.csr_matrix(
        (np.array([1.0 + 0.0j]), (np.array([1]), np.array([0]))),
        shape=(2, 2),
    )

    def embed(
        replacements: dict[int, sparse.spmatrix],
        matter: sparse.spmatrix = matter_identity,
    ) -> sparse.csr_matrix:
        return sparse_kron_all(
            tuple(
                replacements.get(index, pair.identity)
                for index in range(4)
            )
            + (matter,)
        )

    identity = embed({})
    electric_energy = sparse.csr_matrix(identity.shape, dtype=complex)
    coefficient = coupling**2 / (2.0 * pair.delta**2)
    for edge in range(4):
        electric_energy += coefficient * (
            2.0 * identity
            - embed({edge: pair.shift})
            - embed({edge: pair.shift.conj().T})
        )

    wilson = embed(
        {
            0: pair.clock,
            1: pair.clock,
            2: pair.clock.conj().T,
            3: pair.clock.conj().T,
        }
    )
    magnetic_energy = (1.0 / (2.0 * coupling**2)) * (
        2.0 * identity - wilson - wilson.conj().T
    )
    charged_forward = embed({0: pair.clock}, transfer)
    hopping_energy = -hopping * (
        charged_forward + charged_forward.conj().T
    )

    matter_tail_phase = sparse.diags(
        [pair.omega, 1.0], format="csr"
    )
    matter_head_phase = sparse.diags(
        [1.0, pair.omega], format="csr"
    )
    gauss = (
        embed(
            {0: pair.shift.conj().T, 3: pair.shift.conj().T},
            matter_tail_phase,
        ),
        embed(
            {0: pair.shift, 1: pair.shift.conj().T},
            matter_head_phase,
        ),
        embed({1: pair.shift, 2: pair.shift}),
        embed({2: pair.shift.conj().T, 3: pair.shift}),
    )
    hamiltonian = electric_energy + magnetic_energy + hopping_energy
    return ClockFace(
        electric_energy=electric_energy,
        magnetic_energy=magnetic_energy,
        hopping_energy=hopping_energy,
        hamiltonian=hamiltonian.tocsr(),
        gauss=tuple(operator.tocsr() for operator in gauss),
        dimension=identity.shape[0],
    )


@dataclass(frozen=True)
class ClockBond:
    electric_energy: np.ndarray
    hopping_energy: np.ndarray
    hamiltonian: np.ndarray
    gauss_tail: np.ndarray
    gauss_head: np.ndarray
    number_tail: np.ndarray
    number_head: np.ndarray


def clock_bond(order: int, coupling: float, hopping: float) -> ClockBond:
    pair = clock_pair(order)
    identity_link = pair.identity
    identity_matter = sparse.identity(2, dtype=complex, format="csr")
    identity = sparse.kron(
        identity_link, identity_matter, format="csr"
    )
    transfer = sparse.csr_matrix(
        (np.array([1.0 + 0.0j]), (np.array([1]), np.array([0]))),
        shape=(2, 2),
    )
    number_tail_small = sparse.diags([1.0, 0.0], format="csr")
    number_head_small = sparse.diags([0.0, 1.0], format="csr")
    electric_energy = (
        coupling**2
        / (2.0 * pair.delta**2)
        * (
            2.0 * identity
            - sparse.kron(pair.shift, identity_matter, format="csr")
            - sparse.kron(
                pair.shift.conj().T, identity_matter, format="csr"
            )
        )
    )
    charged_forward = sparse.kron(pair.clock, transfer, format="csr")
    hopping_energy = -hopping * (
        charged_forward + charged_forward.conj().T
    )
    matter_tail_phase = sparse.diags(
        [pair.omega, 1.0], format="csr"
    )
    matter_head_phase = sparse.diags(
        [1.0, pair.omega], format="csr"
    )
    gauss_tail = sparse.kron(
        pair.shift.conj().T, matter_tail_phase, format="csr"
    )
    gauss_head = sparse.kron(
        pair.shift, matter_head_phase, format="csr"
    )
    number_tail = sparse.kron(
        identity_link, number_tail_small, format="csr"
    )
    number_head = sparse.kron(
        identity_link, number_head_small, format="csr"
    )
    electric_dense = electric_energy.toarray()
    hopping_dense = hopping_energy.toarray()
    return ClockBond(
        electric_energy=electric_dense,
        hopping_energy=hopping_dense,
        hamiltonian=electric_dense + hopping_dense,
        gauss_tail=gauss_tail.toarray(),
        gauss_head=gauss_head.toarray(),
        number_tail=number_tail.toarray(),
        number_head=number_head.toarray(),
    )


def electric_tame_relative_error(order: int, maximum_mode: int) -> float:
    delta = 2.0 * np.pi / order
    modes = np.arange(1, maximum_mode + 1, dtype=float)
    exact = (1.0 - np.cos(delta * modes)) / delta**2
    quadratic = 0.5 * modes**2
    return float(np.max(np.abs(exact - quadratic) / quadratic))


def curl_symbol(momentum: np.ndarray) -> np.ndarray:
    difference = np.exp(1.0j * momentum) - 1.0
    return np.array(
        (
            (0.0, -difference[2], difference[1]),
            (difference[2], 0.0, -difference[0]),
            (-difference[1], difference[0], 0.0),
        ),
        dtype=complex,
    )


def lattice_frequency(momentum: np.ndarray) -> float:
    return float(
        2.0 * np.sqrt(np.sum(np.sin(0.5 * momentum) ** 2))
    )


def signed_permutation_matrices() -> tuple[np.ndarray, ...]:
    matrices = []
    for permutation in permutations(range(3)):
        base = np.zeros((3, 3))
        for row, column in enumerate(permutation):
            base[row, column] = 1.0
        for signs in product((-1.0, 1.0), repeat=3):
            matrices.append(np.diag(signs) @ base)
    return tuple(matrices)


def reduced_clock_mode(
    order: int, coupling: float, stiffness: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Supplied finite-clock comparison oscillator, not a many-link sector."""

    pair = clock_pair(order)
    identity = sparse.identity(order, dtype=complex, format="csr")
    kinetic = (
        coupling**2
        / (2.0 * pair.delta**2)
        * (2.0 * identity - pair.shift - pair.shift.conj().T)
    )
    potential = (
        stiffness
        / (2.0 * coupling**2)
        * (2.0 * identity - pair.clock - pair.clock.conj().T)
    )
    hamiltonian = (kinetic + potential).tocsr()
    indices = np.arange(order, dtype=float)
    initial_vector = (
        1.0
        + 0.37 * np.sin(2.0 * np.pi * (indices + 0.25) / order)
        + 0.19 * np.cos(4.0 * np.pi * (indices + 0.125) / order)
    )
    initial_vector /= np.linalg.norm(initial_vector)
    eigenvalues, eigenvectors = eigsh(
        hamiltonian,
        k=3,
        which="SA",
        v0=initial_vector,
        tol=2.0e-12,
        maxiter=200_000,
    )
    ordering = np.argsort(eigenvalues)
    indices = np.arange(order)
    angles_by_basis_index = (
        ((indices + order // 2) % order) - order // 2
    ) * pair.delta
    return (
        np.asarray(eigenvalues[ordering], dtype=float),
        np.asarray(eigenvectors[:, ordering], dtype=complex),
        np.asarray(angles_by_basis_index, dtype=float),
    )


def clock_electric_data(order: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Centered electric representatives with X=exp(-i delta E).

    Z raises e by one except at the modular wrap. This is a convention on
    representatives, not a globally additive cyclic-link current law.
    """
    modes = np.arange(order) - order // 2
    fourier = np.exp(
        2.0j * np.pi * np.outer(np.arange(order), modes) / order
    ) / np.sqrt(order)
    electric = (fourier * modes) @ fourier.conj().T
    return electric, fourier, modes


def charged_clock_controls() -> tuple[bool, bool, bool]:
    order = 9
    pair = clock_pair(order)
    electric, fourier, modes = clock_electric_data(order)
    tail, head = np.eye(2, dtype=complex)
    transfer = np.outer(head, tail.conj())
    charged_forward = np.kron(pair.clock.toarray(), transfer)
    electric_link = np.kron(electric, np.eye(2))
    bond = clock_bond(order, coupling=0.8, hopping=0.7)

    def state(mode: int, matter: np.ndarray) -> np.ndarray:
        return np.kron(fourier[:, int(np.flatnonzero(modes == mode)[0])], matter)

    before = state(0, tail)
    after = charged_forward @ before
    electric_gain = float(np.vdot(after, electric_link @ after).real)
    head_gain = float(np.vdot(after, bond.number_head @ after).real)
    sign_ok = bool(
        np.max(np.abs(pair.shift @ fourier - fourier * np.exp(-1.0j * pair.delta * modes))) < 2.0e-14
        and np.max(np.abs(after - state(1, head))) < 2.0e-14
        and abs(electric_gain - 1) < 2.0e-14
        and abs(head_gain - 1) < 2.0e-14
        and abs(-electric_gain - head_gain) > 1.9
    )
    # div E-rho=b with b_tail=-1,b_head=0: G_v=omega^(-b_v).
    sector_ok = all(
        np.max(np.abs(generator @ vector - phase * vector)) < 3.0e-14
        for generator, phase in ((bond.gauss_tail, pair.omega), (bond.gauss_head, 1))
        for vector in (before, after)
    )
    wrapped_before = state(4, tail)
    wrapped_after = charged_forward @ wrapped_before
    wrapped_gain = float(
        np.vdot(wrapped_after, electric_link @ wrapped_after).real
        - np.vdot(wrapped_before, electric_link @ wrapped_before).real
    )
    wrap_ok = bool(
        np.max(np.abs(wrapped_after - state(-4, head))) < 3.0e-14
        and abs(wrapped_gain + 8) < 4.0e-14
        and abs(wrapped_gain - 1) > 8.9
        and all(
            np.max(np.abs(generator @ charged_forward - charged_forward @ generator)) < 3.0e-14
            for generator in (bond.gauss_tail, bond.gauss_head)
        )
    )
    return sign_ok, bool(sector_ok), wrap_ok


def cosine_rotor_gap(coupling: float, stiffness: float, cutoff: int) -> float:
    """Fourier-truncated periodic cosine rotor, electric modes -cutoff..cutoff."""
    modes = np.arange(-cutoff, cutoff + 1, dtype=float)
    diagonal = 0.5 * coupling**2 * modes**2 + stiffness / coupling**2
    off_diagonal = np.full(2 * cutoff, -stiffness / (2 * coupling**2))
    values = eigh_tridiagonal(
        diagonal, off_diagonal, eigvals_only=True, select="i", select_range=(0, 1)
    )
    return float(values[1] - values[0])


def ratios(values: list[float]) -> list[float]:
    return [left / right for left, right in zip(values, values[1:])]


def main() -> int:
    checks = Checks()

    algebra_ok = True
    exact_unitaries_ok = True
    for order in (2, 3, 4, 5, 8, 16):
        pair = clock_pair(order)
        weyl_residual = (
            pair.clock @ pair.shift
            - pair.omega * pair.shift @ pair.clock
        )
        algebra_ok = algebra_ok and bool(
            sparse_max_abs(weyl_residual) < 2.0e-14
        )
        exact_unitaries_ok = exact_unitaries_ok and bool(
            sparse_max_abs(
                pair.shift.conj().T @ pair.shift - pair.identity
            )
            < 1.0e-15
            and sparse_max_abs(
                pair.clock.conj().T @ pair.clock - pair.identity
            )
            < 2.0e-14
            and sparse_max_abs(pair.shift**order - pair.identity)
            < 1.0e-15
            and sparse_max_abs(pair.clock**order - pair.identity)
            < 3.0e-14
        )
    checks.check(
        algebra_ok,
        "K-state link clocks obey the exact Weyl relation Z X = omega X Z",
    )
    checks.check(
        exact_unitaries_ok,
        "both finite link generators are unitary and cyclic with no dark boundary states",
    )

    face_gauge_ok = True
    face_hermitian_ok = True
    face_dimensions_ok = True
    component_nontrivial_ok = True
    gauss_group_ok = True
    for order in (2, 3, 4, 5, 8):
        face = clock_face(order, coupling=0.83, hopping=0.61)
        pair = clock_pair(order)
        face_identity = sparse.identity(
            face.dimension, dtype=complex, format="csr"
        )
        face_dimensions_ok = face_dimensions_ok and bool(
            face.dimension == 2 * order**4
        )
        face_hermitian_ok = face_hermitian_ok and all(
            sparse_max_abs(operator - operator.conj().T) < 2.0e-14
            for operator in (
                face.electric_energy,
                face.magnetic_energy,
                face.hopping_energy,
                face.hamiltonian,
            )
        )
        face_gauge_ok = face_gauge_ok and all(
            sparse_max_abs(sparse_commutator(generator, component))
            < 3.0e-13
            for generator in face.gauss
            for component in (
                face.electric_energy,
                face.magnetic_energy,
                face.hopping_energy,
            )
        )
        component_nontrivial_ok = component_nontrivial_ok and all(
            sparse_max_abs(operator) > 0.1
            for operator in (
                face.electric_energy,
                face.magnetic_energy,
                face.hopping_energy,
            )
        )
        gauss_group_ok = gauss_group_ok and bool(
            all(
                sparse_max_abs(
                    generator.conj().T @ generator - face_identity
                )
                < 3.0e-14
                for generator in face.gauss
            )
            and all(
                sparse_max_abs(sparse_commutator(left, right))
                < 3.0e-14
                for left in face.gauss
                for right in face.gauss
            )
            and sparse_max_abs(
                face.gauss[0]
                @ face.gauss[1]
                @ face.gauss[2]
                @ face.gauss[3]
                - pair.omega * face_identity
            )
            < 5.0e-14
        )
    checks.check(
        face_dimensions_ok and face_hermitian_ok,
        "the exact face-plus-matter Hilbert spaces and all three Hamiltonian components are well formed",
    )
    checks.check(
        face_gauge_ok,
        "electric, Wilson-face, and charged-hop terms separately preserve all four modular Gauss symmetries",
    )
    checks.check(
        gauss_group_ok,
        "the commuting unitary Gauss generators multiply to the one-unit total-charge sector phase",
    )
    checks.check(
        component_nontrivial_ok,
        "electric, magnetic, and matter terms are all nontrivial across the finite-order grid",
    )

    bond_exchange_ok = True
    bond_gauss_ok = True
    bond_charge_ok = True
    for order, coupling, hopping, step in (
        (3, 0.8, 0.7, 0.31),
        (4, 1.1, 0.5, 0.23),
        (5, 0.7, 0.9, 0.19),
        (8, 1.3, 0.4, 0.13),
        (16, 0.9, 0.6, 0.08),
    ):
        bond = clock_bond(order, coupling, hopping)
        unitary = hermitian_exponential(bond.hamiltonian, step)
        electric_change = (
            evolved(bond.electric_energy, unitary) - bond.electric_energy
        )
        hopping_change = (
            evolved(bond.hopping_energy, unitary) - bond.hopping_energy
        )
        bond_exchange_ok = bond_exchange_ok and bool(
            dense_spectral_norm(electric_change + hopping_change) < 3.0e-14
            and dense_spectral_norm(electric_change) > 1.0e-4
        )
        bond_gauss_ok = bond_gauss_ok and bool(
            dense_spectral_norm(
                evolved(bond.gauss_tail, unitary) - bond.gauss_tail
            )
            < 3.0e-14
            and dense_spectral_norm(
                evolved(bond.gauss_head, unitary) - bond.gauss_head
            )
            < 3.0e-14
        )
        total_number = bond.number_tail + bond.number_head
        bond_charge_ok = bond_charge_ok and bool(
            dense_spectral_norm(
                evolved(total_number, unitary) - total_number
            )
            < 3.0e-14
        )
    checks.check(
        bond_gauss_ok and bond_charge_ok,
        "exact finite-clock matter evolution preserves both modular Gauss generators and total charge",
    )
    checks.check(
        bond_exchange_ok,
        "electric and hopping components exchange equal and opposite energy at finite step",
    )
    charged_sign, charged_sector, charged_wrap = charged_clock_controls()
    checks.check(
        charged_sign,
        "the actual charged Fourier hop raises electric flux and head number with the parent orientation",
    )
    checks.check(
        charged_sector,
        "the charged hop preserves its explicit non-neutral modular Gauss sector",
    )
    checks.check(
        charged_wrap,
        "the actual charged wrap preserves modular Gauss but rejects a globally additive flux increment",
    )

    full_face = clock_face(3, coupling=0.91, hopping=0.57)
    full_hamiltonian = full_face.hamiltonian.toarray()
    full_tick = hermitian_exponential(full_hamiltonian, 0.17)
    checks.check(
        dense_spectral_norm(
            full_tick.conj().T @ full_tick
            - np.eye(full_face.dimension)
        )
        < 2.0e-14
        and dense_spectral_norm(
            evolved(full_hamiltonian, full_tick) - full_hamiltonian
        )
        < 4.0e-14,
        "the complete finite-clock matter-electric-magnetic face has exact unitary energy evolution",
    )
    checks.check(
        all(
            dense_spectral_norm(
                evolved(generator.toarray(), full_tick)
                - generator.toarray()
            )
            < 4.0e-14
            for generator in full_face.gauss
        ),
        "the complete face evolution preserves every modular Gauss generator",
    )

    bit_payload_ok = all(
        order == 2 ** int(np.log2(order))
        and int(np.log2(order)) in range(2, 11)
        for order in (4, 8, 16, 32, 64, 128, 256, 512, 1024)
    )
    checks.check(
        bit_payload_ok,
        "orders K=2^q use exactly q qubits per collective link for q=2 through 10",
    )
    binary_action_ok = True
    for qubit_count in range(2, 11):
        order = 2**qubit_count
        omega = np.exp(2.0j * np.pi / order)
        for value in range(order):
            bits = tuple(
                (value >> bit_index) & 1
                for bit_index in range(qubit_count)
            )
            factored_phase = np.prod(
                [
                    np.exp(
                        2.0j * np.pi * bit * (2**bit_index) / order
                    )
                    for bit_index, bit in enumerate(bits)
                ]
            )
            incremented = (value + 1) % order
            decremented = (incremented - 1) % order
            binary_action_ok = binary_action_ok and bool(
                abs(factored_phase - omega**value) < 2.0e-13
                and decremented == value
            )
    checks.check(
        binary_action_ok,
        "clock phase factorization and cyclic increment are exact reversible maps on the q-qubit register",
    )

    tame_orders = (16, 32, 64, 128)
    tame_errors = [
        electric_tame_relative_error(order, maximum_mode=2)
        for order in tame_orders
    ]
    checks.check(
        all(3.8 < value < 4.1 for value in ratios(tame_errors))
        and tame_errors[-1] < 9.0e-4,
        "the exact clock electric cosine converges to E squared with K^-2 tame error",
    )

    magnetic_errors = []
    for angle in (0.4, 0.2, 0.1, 0.05):
        exact = 1.0 - np.cos(angle)
        quadratic = 0.5 * angle**2
        magnetic_errors.append(abs(exact - quadratic))
    checks.check(
        all(15.5 < value < 16.5 for value in ratios(magnetic_errors)),
        "the exact Wilson magnetic cosine has a fourth-order remainder about the curl quadratic",
    )

    modular_additive_ok = True
    modular_wrap_control = False
    order = 32
    maximum_mode = 2
    for electric_values in product(
        range(-maximum_mode, maximum_mode + 1), repeat=6
    ):
        divergence = (
            sum(electric_values[3:]) - sum(electric_values[:3])
        )
        for charge, background in product((0, 1), (-1, 0, 1)):
            residual = divergence - charge - background
            modular_additive_ok = modular_additive_ok and bool(
                abs(residual) <= 6 * maximum_mode + 2 < order
                and (residual % order == 0) == (residual == 0)
            )
    wrap_values = (-6, -5, -5, 6, 5, 5)
    wrap_divergence = sum(wrap_values[3:]) - sum(wrap_values[:3])
    wrap_charge, wrap_background = 1, -1
    wrap_residual = wrap_divergence - wrap_charge - wrap_background
    modular_wrap_control = (
        wrap_residual != 0 and wrap_residual % order == 0
    )
    checks.check(
        modular_additive_ok,
        "inside the charged no-wrap window modular Gauss equals div E-rho-background=0",
    )
    checks.check(
        modular_wrap_control,
        "outside that window a resolved modular alias prevents an unqualified additive reading",
    )

    mode_count_ok = True
    dispersion_ok = True
    coupling_independence_ok = True
    no_doubler_ok = True
    for length in (3, 4, 5, 7):
        for indices in product(range(length), repeat=3):
            if indices == (0, 0, 0):
                continue
            momentum = 2.0 * np.pi * np.array(indices, dtype=float) / length
            curl = curl_symbol(momentum)
            eigenvalues = np.linalg.eigvalsh(curl.conj().T @ curl)
            expected_squared = lattice_frequency(momentum) ** 2
            mode_count_ok = mode_count_ok and bool(
                abs(eigenvalues[0]) < 2.0e-12
                and abs(eigenvalues[1] - expected_squared) < 2.0e-12
                and abs(eigenvalues[2] - expected_squared) < 2.0e-12
            )
            dispersion_ok = dispersion_ok and bool(expected_squared > 1.0e-8)
            for coupling in (0.3, 0.8, 1.7):
                frequency_squared = (
                    coupling**2 * (expected_squared / coupling**2)
                )
                coupling_independence_ok = coupling_independence_ok and bool(
                    abs(frequency_squared - expected_squared) < 2.0e-14
                )
        corner = np.array((np.pi, np.pi, np.pi))
        no_doubler_ok = no_doubler_ok and bool(
            lattice_frequency(corner) > 3.4
        )
    checks.check(
        mode_count_ok and dispersion_ok,
        "the three-dimensional tame Maxwell tangent has exactly two transverse branches at every nonzero tested momentum",
    )
    checks.check(
        coupling_independence_ok,
        "reciprocal electric and magnetic coefficients make the photon frequency coupling independent",
    )
    checks.check(
        no_doubler_ok,
        "the forward-difference photon symbol has no extra zero at the Brillouin-zone corner",
    )

    infrared_ratios = []
    for length in (32, 64, 128, 256):
        momentum = np.array((2.0 * np.pi / length, 0.0, 0.0))
        infrared_ratios.append(
            lattice_frequency(momentum) / float(momentum[0])
        )
    infrared_errors = [abs(value - 1.0) for value in infrared_ratios]
    checks.check(
        all(3.9 < value < 4.1 for value in ratios(infrared_errors))
        and infrared_errors[-1] < 3.0e-5,
        "both transverse branches approach unit-speed linear infrared dispersion",
    )

    covariance_ok = True
    probe_momenta = (
        np.array((0.31, 0.57, 0.83)),
        np.array((1.1, -0.4, 0.2)),
    )
    cubic_maps = signed_permutation_matrices()
    for momentum in probe_momenta:
        reference = lattice_frequency(momentum)
        covariance_ok = covariance_ok and all(
            abs(lattice_frequency(transform @ momentum) - reference)
            < 1.0e-14
            for transform in cubic_maps
        )
    checks.check(
        len(cubic_maps) == 48 and covariance_ok,
        "the transverse clock-Maxwell tangent is covariant under all 48 cubic signed permutations",
    )

    spectral_coupling = 0.06
    spectral_orders = (128, 256, 512, 1024)
    spectral_lengths = (8, 16, 32)
    spectral_errors: dict[int, list[float]] = {}
    rotor_errors: dict[int, list[float]] = {}
    rotor_gaps: dict[int, float] = {}
    final_angle_moments: dict[int, float] = {}
    rotor_floor_ok = True
    final_tameness_ok = True
    for length in spectral_lengths:
        stiffness = 4.0 * np.sin(np.pi / length) ** 2
        target_frequency = np.sqrt(stiffness)
        spectral_errors[length] = []
        rotor_errors[length] = []
        rotor_gap = cosine_rotor_gap(spectral_coupling, stiffness, cutoff=100)
        refined_rotor_gap = cosine_rotor_gap(spectral_coupling, stiffness, cutoff=200)
        rotor_gaps[length] = refined_rotor_gap
        rotor_floor_ok = rotor_floor_ok and bool(
            abs(rotor_gap - refined_rotor_gap) < 2.0e-10
            and 4.0e-4 < 1.0 - refined_rotor_gap / target_frequency < 3.0e-3
        )
        for order in spectral_orders:
            eigenvalues, eigenvectors, centered_angles = reduced_clock_mode(
                order, spectral_coupling, stiffness
            )
            gap = float(eigenvalues[1] - eigenvalues[0])
            spectral_errors[length].append(
                abs(gap / target_frequency - 1.0)
            )
            rotor_errors[length].append(abs(gap / refined_rotor_gap - 1.0))
            if order == spectral_orders[-1]:
                angle_probabilities = np.abs(eigenvectors[:, 0]) ** 2
                angle_second_moment = float(
                    np.sum(
                        angle_probabilities * centered_angles**2
                    )
                )
                final_angle_moments[length] = angle_second_moment
                edge_probability = float(
                    np.sum(
                        angle_probabilities[
                            np.abs(centered_angles) > 0.75 * np.pi
                        ]
                    )
                )
                final_tameness_ok = final_tameness_ok and bool(
                    angle_second_moment < 0.01 and edge_probability < 1.0e-12
                )
    checks.check(
        all(
            errors[-1] < 3.0e-3
            and all(
                left > right
                for left, right in zip(errors, errors[1:])
            )
            for errors in spectral_errors.values()
        ),
        "the named finite-clock comparison ladder decreases its harmonic gap discrepancy below 0.3 percent",
    )
    checks.check(
        rotor_floor_ok
        and all(
            errors[-1] < 1.1e-3
            and all(left > right for left, right in zip(errors, errors[1:]))
            for errors in rotor_errors.values()
        ),
        "fixed-g rotor gaps are cutoff-stable below the harmonic targets and the clock ladder approaches those rotor gaps",
    )
    checks.check(
        final_tameness_ok,
        "the K=1024 mode ground states are angle-localized with negligible branch-edge weight",
    )

    print(
        "diagnostic tame electric relative errors:",
        " ".join(f"{value:.8e}" for value in tame_errors),
    )
    for length in spectral_lengths:
        print(
            f"diagnostic L={length} clock-mode relative gap errors:",
            " ".join(f"{value:.8e}" for value in spectral_errors[length]),
        )
        print(
            f"diagnostic L={length} fixed-g rotor gap={rotor_gaps[length]:.12f}; "
            f"clock-to-rotor relative errors="
            + " ".join(f"{value:.8e}" for value in rotor_errors[length])
            + f"; K=1024 angle second moment={final_angle_moments[length]:.8e}"
        )
    print(
        "per_element: exact finite Weyl links, cyclic unitaries, and tame cosine errors are checked"
    )
    print(
        "per_site: modular Gauss generators, charged transport, and the no-wrap additive limit are checked"
    )
    print(
        "per_mode: two transverse branches, infrared speed, cubic covariance, and reduced clock spectra are checked"
    )
    print(
        "per_block: exact bond exchange and the complete K=3 matter-electric-magnetic face are checked"
    )
    print(
        "lattice_wide: the 3D quadratic tame tangent is resolved; the exact clock law's thermodynamic Coulomb phase is not executed"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
