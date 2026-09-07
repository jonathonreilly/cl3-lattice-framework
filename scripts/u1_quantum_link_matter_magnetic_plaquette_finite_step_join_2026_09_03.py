#!/usr/bin/env python3
"""Finite-step quantum-link matter and magnetic-plaquette join.

The runner puts one gauge-covariant charged hop on the bottom edge of one
oriented square, equips all four finite-flux links with electric energy, and
adds the Wilson plaquette shift.  It checks Gauss preservation, exact local
matter/electric work, magnetic circulation, exact unsplit energy evolution,
and the conserved Floquet generator of a reversible electric-matter / magnetic
Strang tick.  It also resolves the correlated matter-plaquette transitions
generated at finite step.
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


def spectral_norm(operator: np.ndarray) -> float:
    return float(np.linalg.norm(operator, ord=2))


def evolved(operator: np.ndarray, unitary: np.ndarray) -> np.ndarray:
    return unitary.conj().T @ operator @ unitary


def hermitian_exponential(
    hamiltonian: np.ndarray, step: float
) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    return (
        eigenvectors
        @ np.diag(np.exp(-1.0j * step * eigenvalues))
        @ eigenvectors.conj().T
    )


def principal_floquet_generator(
    unitary: np.ndarray, step: float
) -> np.ndarray:
    triangular, vectors = schur(unitary, output="complex")
    phases = np.angle(np.diag(triangular))
    generator = vectors @ np.diag(-phases / step) @ vectors.conj().T
    return 0.5 * (generator + generator.conj().T)


def kron_all(factors: tuple[np.ndarray, ...]) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for factor in factors:
        result = np.kron(result, factor)
    return result


def flux_shift(spin: int) -> tuple[np.ndarray, np.ndarray]:
    electric = np.diag(np.arange(-spin, spin + 1, dtype=float))
    shift = np.zeros_like(electric, dtype=complex)
    for index in range(2 * spin):
        shift[index + 1, index] = 1.0
    return electric, shift


def number_operator(size: int, vertex: int) -> np.ndarray:
    result = np.zeros((size, size), dtype=complex)
    result[vertex, vertex] = 1.0
    return result


def matter_transfer(size: int, tail: int, head: int) -> np.ndarray:
    result = np.zeros((size, size), dtype=complex)
    result[head, tail] = 1.0
    return result


@dataclass(frozen=True)
class PlaquetteModel:
    spin: int
    electric: tuple[np.ndarray, ...]
    number_tail: np.ndarray
    number_head: np.ndarray
    gauss: tuple[np.ndarray, ...]
    plaquette_shift: np.ndarray
    electric_energy: np.ndarray
    hopping_energy: np.ndarray
    magnetic_energy: np.ndarray
    electric_matter: np.ndarray
    hamiltonian: np.ndarray


def plaquette_model(
    spin: int,
    electric_coupling: float,
    hopping: float,
    magnetic_coupling: float,
) -> PlaquetteModel:
    """Square 0->1->2->3->0, with stored edges 0->1,1->2,3->2,0->3."""

    small_electric, small_shift = flux_shift(spin)
    link_dimension = 2 * spin + 1
    link_identity = np.eye(link_dimension, dtype=complex)
    matter_identity = np.eye(2, dtype=complex)
    number_tail_small = number_operator(2, 0)
    number_head_small = number_operator(2, 1)
    transfer = matter_transfer(2, 0, 1)

    def links_with(
        replacements: dict[int, np.ndarray],
        matter: np.ndarray = matter_identity,
    ) -> np.ndarray:
        factors = tuple(
            replacements.get(index, link_identity) for index in range(4)
        ) + (matter,)
        return kron_all(factors)

    electric = tuple(
        links_with({index: small_electric}) for index in range(4)
    )
    number_tail = links_with({}, number_tail_small)
    number_head = links_with({}, number_head_small)

    charged_forward = links_with({0: small_shift}, transfer)
    hopping_energy = -hopping * (
        charged_forward + charged_forward.conj().T
    )

    plaquette_shift = links_with(
        {
            0: small_shift,
            1: small_shift,
            2: small_shift.conj().T,
            3: small_shift.conj().T,
        }
    )
    magnetic_energy = -0.5 * magnetic_coupling * (
        plaquette_shift + plaquette_shift.conj().T
    )
    electric_energy = 0.5 * electric_coupling * sum(
        operator @ operator for operator in electric
    )
    electric_matter = electric_energy + hopping_energy
    hamiltonian = electric_matter + magnetic_energy

    gauss = (
        -electric[0] - electric[3] - number_tail,
        +electric[0] - electric[1] - number_head,
        +electric[1] + electric[2],
        -electric[2] + electric[3],
    )
    return PlaquetteModel(
        spin=spin,
        electric=electric,
        number_tail=number_tail,
        number_head=number_head,
        gauss=gauss,
        plaquette_shift=plaquette_shift,
        electric_energy=electric_energy,
        hopping_energy=hopping_energy,
        magnetic_energy=magnetic_energy,
        electric_matter=electric_matter,
        hamiltonian=hamiltonian,
    )


def combined_transition_mask(spin: int) -> np.ndarray:
    """Entries changing matter and at least one non-matter edge of the face."""

    dimension = (2 * spin + 1) ** 4 * 2
    shape = (2 * spin + 1,) * 4 + (2,)
    labels = [np.unravel_index(index, shape) for index in range(dimension)]
    mask = np.zeros((dimension, dimension), dtype=bool)
    for row, row_label in enumerate(labels):
        for column, column_label in enumerate(labels):
            matter_changes = row_label[4] != column_label[4]
            other_face_edge_changes = any(
                row_label[index] != column_label[index]
                for index in (1, 2, 3)
            )
            mask[row, column] = matter_changes and other_face_edge_changes
    return mask


def square_dihedral_edge_maps() -> tuple[np.ndarray, ...]:
    """Signed edge permutations induced by all eight square symmetries."""

    vertices = ((0, 0), (1, 0), (1, 1), (0, 1))
    stored_edges = ((0, 1), (1, 2), (3, 2), (0, 3))
    transforms = (
        lambda x, y: (x, y),
        lambda x, y: (1 - y, x),
        lambda x, y: (1 - x, 1 - y),
        lambda x, y: (y, 1 - x),
        lambda x, y: (1 - x, y),
        lambda x, y: (x, 1 - y),
        lambda x, y: (y, x),
        lambda x, y: (1 - y, 1 - x),
    )
    vertex_lookup = {coordinate: index for index, coordinate in enumerate(vertices)}
    maps = []
    for transform in transforms:
        vertex_map = {
            index: vertex_lookup[transform(*coordinate)]
            for index, coordinate in enumerate(vertices)
        }
        edge_map = np.zeros((4, 4), dtype=float)
        for source, (tail, head) in enumerate(stored_edges):
            mapped = (vertex_map[tail], vertex_map[head])
            for target, target_edge in enumerate(stored_edges):
                if mapped == target_edge:
                    edge_map[target, source] = 1.0
                    break
                if mapped == target_edge[::-1]:
                    edge_map[target, source] = -1.0
                    break
            else:
                raise AssertionError("square symmetry did not map an edge to an edge")
        maps.append(edge_map)
    return tuple(maps)


def ratios(values: list[float]) -> list[float]:
    return [left / right for left, right in zip(values, values[1:])]


def main() -> int:
    checks = Checks()
    spin = 1
    electric_coupling = 1.2
    hopping = 0.7
    magnetic_coupling = 0.9
    model = plaquette_model(
        spin, electric_coupling, hopping, magnetic_coupling
    )
    dimension = model.hamiltonian.shape[0]

    small_electric, small_shift = flux_shift(spin)
    checks.check(
        np.array_equal(commutator(small_electric, small_shift), small_shift),
        "each hard-cutoff link obeys [E,U]=U exactly",
    )
    checks.check(
        np.max(
            np.abs(
                small_shift.conj().T @ small_shift
                - np.eye(2 * spin + 1)
            )
        )
        == 1.0
        and np.count_nonzero(small_shift[:, -1]) == 0,
        "the finite link exposes its one top-flux raising boundary",
    )
    checks.check(
        all(
            spectral_norm(operator - operator.conj().T) < 1.0e-15
            for operator in (
                model.electric_energy,
                model.hopping_energy,
                model.magnetic_energy,
                model.hamiltonian,
            )
        ),
        "electric, charged-hop, magnetic, and summed generators are Hermitian",
    )
    checks.check(
        all(
            spectral_norm(commutator(generator, layer)) < 1.0e-14
            for generator in model.gauss
            for layer in (model.electric_matter, model.magnetic_energy)
        ),
        "electric-matter and magnetic layers separately commute with all four Gauss generators",
    )
    checks.check(
        spectral_norm(
            commutator(model.electric_matter, model.magnetic_energy)
        )
        > 0.2,
        "the overlapping electric-matter and magnetic layers genuinely do not commute",
    )

    magnetic_step = 0.31
    magnetic_tick = hermitian_exponential(
        model.magnetic_energy, magnetic_step
    )
    magnetic_delta = tuple(
        evolved(operator, magnetic_tick) - operator
        for operator in model.electric
    )
    checks.check(
        spectral_norm(magnetic_delta[0]) > 0.1
        and spectral_norm(magnetic_delta[0] - magnetic_delta[1]) < 2.0e-14
        and spectral_norm(magnetic_delta[0] + magnetic_delta[2]) < 2.0e-14
        and spectral_norm(magnetic_delta[0] + magnetic_delta[3]) < 2.0e-14,
        "the magnetic layer circulates one divergence-free flux around the face",
    )
    checks.check(
        spectral_norm(
            evolved(model.number_tail, magnetic_tick) - model.number_tail
        )
        < 2.0e-14
        and spectral_norm(
            evolved(model.number_head, magnetic_tick) - model.number_head
        )
        < 2.0e-14,
        "the pure magnetic circulation leaves matter charge unchanged",
    )

    matter_step = 0.27
    matter_tick = hermitian_exponential(model.electric_matter, matter_step)
    electric_new = evolved(model.electric[0], matter_tick)
    current = (electric_new - model.electric[0]) / matter_step
    tail_new = evolved(model.number_tail, matter_tick)
    head_new = evolved(model.number_head, matter_tick)
    electric_energy_change = (
        evolved(model.electric_energy, matter_tick) - model.electric_energy
    )
    hopping_energy_change = (
        evolved(model.hopping_energy, matter_tick) - model.hopping_energy
    )
    work = 0.25 * electric_coupling * matter_step * (
        current @ (model.electric[0] + electric_new)
        + (model.electric[0] + electric_new) @ current
    )
    checks.check(
        spectral_norm(
            head_new - model.number_head - matter_step * current
        )
        < 2.0e-14
        and spectral_norm(
            tail_new - model.number_tail + matter_step * current
        )
        < 2.0e-14,
        "one finite current equals flux gain, head gain, and negative tail gain in the active layer",
    )
    checks.check(
        all(
            spectral_norm(evolved(operator, matter_tick) - operator)
            < 2.0e-14
            for operator in model.electric[1:]
        ),
        "the active matter layer changes no spectator face-edge flux",
    )
    checks.check(
        spectral_norm(electric_energy_change - work) < 2.0e-14
        and spectral_norm(hopping_energy_change + work) < 2.0e-14
        and spectral_norm(
            evolved(model.electric_matter, matter_tick)
            - model.electric_matter
        )
        < 2.0e-14,
        "the electric-matter layer closes exact opposite work and its local energy",
    )

    full_step = 0.19
    exact_tick = hermitian_exponential(model.hamiltonian, full_step)
    checks.check(
        spectral_norm(
            exact_tick.conj().T @ exact_tick - np.eye(dimension)
        )
        < 2.0e-14
        and all(
            spectral_norm(evolved(generator, exact_tick) - generator)
            < 2.0e-14
            for generator in model.gauss
        ),
        "the unsplit matter-electric-magnetic evolution is unitary and preserves every Gauss operator",
    )
    checks.check(
        spectral_norm(
            evolved(model.hamiltonian, exact_tick) - model.hamiltonian
        )
        < 2.0e-14,
        "the unsplit joint evolution exactly conserves the full Hamiltonian",
    )
    full_electric_delta = tuple(
        evolved(operator, exact_tick) - operator
        for operator in model.electric
    )
    full_head_delta = (
        evolved(model.number_head, exact_tick) - model.number_head
    )
    loop_remainder = full_electric_delta[0] - full_head_delta
    checks.check(
        spectral_norm(loop_remainder - full_electric_delta[1]) < 2.0e-14
        and spectral_norm(loop_remainder + full_electric_delta[2]) < 2.0e-14
        and spectral_norm(loop_remainder + full_electric_delta[3]) < 2.0e-14,
        "the full flux change splits exactly into matter transfer plus a divergence-free face circulation",
    )

    trial_steps = (0.16, 0.08, 0.04, 0.02)
    energy_drifts: list[float] = []
    flow_errors: list[float] = []
    floquet_deviations: list[float] = []
    floquet_bch_residuals: list[float] = []
    combined_entries: list[float] = []
    gauss_and_reversal_ok = True
    floquet_ok = True
    principal_branch_ok = True
    mask = combined_transition_mask(spin)
    summed_zero_on_combined = float(np.max(np.abs(model.hamiltonian[mask])))

    double_a = commutator(
        model.electric_matter,
        commutator(model.electric_matter, model.magnetic_energy),
    )
    double_b = commutator(
        model.magnetic_energy,
        commutator(model.electric_matter, model.magnetic_energy),
    )
    # This coefficient is verified below against the principal logarithm.
    bch_second_order = (double_a + 2.0 * double_b) / 24.0

    for trial_step in trial_steps:
        half_matter = hermitian_exponential(
            model.electric_matter, 0.5 * trial_step
        )
        full_magnetic = hermitian_exponential(
            model.magnetic_energy, trial_step
        )
        strang_tick = half_matter @ full_magnetic @ half_matter
        exact_trial_tick = hermitian_exponential(
            model.hamiltonian, trial_step
        )
        energy_drifts.append(
            spectral_norm(
                evolved(model.hamiltonian, strang_tick)
                - model.hamiltonian
            )
        )
        flow_errors.append(spectral_norm(strang_tick - exact_trial_tick))

        negative_half_matter = hermitian_exponential(
            model.electric_matter, -0.5 * trial_step
        )
        negative_full_magnetic = hermitian_exponential(
            model.magnetic_energy, -trial_step
        )
        reverse_tick = (
            negative_half_matter
            @ negative_full_magnetic
            @ negative_half_matter
        )
        gauss_and_reversal_ok = gauss_and_reversal_ok and bool(
            spectral_norm(reverse_tick @ strang_tick - np.eye(dimension))
            < 3.0e-14
            and all(
                spectral_norm(evolved(generator, strang_tick) - generator)
                < 4.0e-14
                for generator in model.gauss
            )
        )

        floquet = principal_floquet_generator(strang_tick, trial_step)
        floquet_ok = floquet_ok and bool(
            spectral_norm(floquet - floquet.conj().T) < 3.0e-15
            and spectral_norm(evolved(floquet, strang_tick) - floquet)
            < 4.0e-13
            and all(
                spectral_norm(commutator(floquet, generator)) < 1.0e-12
                for generator in model.gauss
            )
        )
        principal_branch_ok = principal_branch_ok and bool(
            trial_step * np.max(np.abs(np.linalg.eigvalsh(floquet)))
            < 0.7 * np.pi
        )
        floquet_deviations.append(spectral_norm(floquet - model.hamiltonian))
        floquet_bch_residuals.append(
            spectral_norm(
                floquet
                - model.hamiltonian
                - trial_step**2 * bch_second_order
            )
        )
        combined_entries.append(float(np.max(np.abs(floquet[mask]))))

    checks.check(
        gauss_and_reversal_ok,
        "the palindromic matter/magnetic tick is exactly reversible and Gauss preserving",
    )
    checks.check(
        all(7.7 < value < 8.3 for value in ratios(energy_drifts))
        and energy_drifts[0] > 1.0e-4,
        "the reversible tick's full-Hamiltonian drift is cubic per step",
    )
    checks.check(
        all(7.7 < value < 8.3 for value in ratios(flow_errors)),
        "the reversible tick approaches exact joint evolution at third order per step",
    )
    checks.check(
        floquet_ok and principal_branch_ok,
        "the tick has a branch-resolved Hermitian Floquet generator that exactly preserves Gauss and itself",
    )
    checks.check(
        all(3.8 < value < 4.2 for value in ratios(floquet_deviations)),
        "the exact Floquet generator differs from the simple Hamiltonian at quadratic order",
    )
    checks.check(
        all(14.0 < value < 18.0 for value in ratios(floquet_bch_residuals)),
        "the resolved double-commutator term predicts the Floquet generator through quadratic order",
    )
    checks.check(
        summed_zero_on_combined < 1.0e-15
        and all(value > 1.0e-5 for value in combined_entries)
        and all(3.8 < value < 4.2 for value in ratios(combined_entries)),
        "finite stepping generates quadratic correlated matter-plus-plaquette transitions absent from the summed law",
    )

    no_matter = plaquette_model(
        spin, electric_coupling, 0.0, magnetic_coupling
    )
    no_magnetic = plaquette_model(
        spin, electric_coupling, hopping, 0.0
    )
    control_step = 0.12
    no_matter_half = hermitian_exponential(
        no_matter.electric_matter, 0.5 * control_step
    )
    no_matter_tick = (
        no_matter_half
        @ hermitian_exponential(no_matter.magnetic_energy, control_step)
        @ no_matter_half
    )
    no_matter_floquet = principal_floquet_generator(
        no_matter_tick, control_step
    )
    no_magnetic_half = hermitian_exponential(
        no_magnetic.electric_matter, 0.5 * control_step
    )
    no_magnetic_tick = no_magnetic_half @ no_magnetic_half
    no_magnetic_exact = hermitian_exponential(
        no_magnetic.hamiltonian, control_step
    )
    checks.check(
        float(np.max(np.abs(no_matter_floquet[mask]))) < 2.0e-14
        and spectral_norm(no_magnetic_tick - no_magnetic_exact) < 7.0e-15,
        "removing either charged hopping or magnetic curvature removes the correlated-transition effect",
    )

    boundary = np.array((1.0, 1.0, -1.0, -1.0))
    curvature = magnetic_coupling * np.outer(boundary, boundary)
    curvature_eigenvalues = np.linalg.eigvalsh(curvature)
    dihedral_maps = square_dihedral_edge_maps()
    checks.check(
        np.count_nonzero(curvature_eigenvalues > 1.0e-12) == 1
        and abs(curvature_eigenvalues[-1] - 4.0 * magnetic_coupling)
        < 1.0e-14
        and curvature_eigenvalues[0] > -1.0e-14,
        "the separate continuous-phase comparison has one positive curl curvature and three curl-flat directions",
    )
    checks.check(
        len(dihedral_maps) == 8
        and all(
            np.allclose(edge_map @ curvature @ edge_map.T, curvature)
            for edge_map in dihedral_maps
        ),
        "the separate phase-comparison curvature is covariant under all eight square symmetries",
    )
    probe = np.array((0.3, -0.2, 0.4, 0.1))
    expansion_errors = []
    for epsilon in (0.4, 0.2, 0.1, 0.05):
        angle = float(boundary @ (epsilon * probe))
        exact_potential = magnetic_coupling * (1.0 - np.cos(angle))
        quadratic = 0.5 * magnetic_coupling * angle**2
        expansion_errors.append(abs(exact_potential - quadratic))
    checks.check(
        all(15.5 < value < 16.5 for value in ratios(expansion_errors)),
        "the Wilson magnetic potential approaches the Maxwell curl quadratic at fourth-order remainder",
    )

    print(
        "diagnostic energy-drift ratios:",
        " ".join(f"{value:.6f}" for value in ratios(energy_drifts)),
    )
    print(
        "diagnostic Floquet-deviation ratios:",
        " ".join(f"{value:.6f}" for value in ratios(floquet_deviations)),
    )
    print(
        "diagnostic combined-entry maxima:",
        " ".join(f"{value:.8e}" for value in combined_entries),
    )
    print(
        "per_element: finite electric shifts, charged hopping, and face circulation are checked"
    )
    print(
        "per_site: four vertex Gauss generators and exact matter continuity are checked"
    )
    print(
        "per_mode: separate phase-comparison curl curvature and finite-operator Floquet refinement orders are resolved"
    )
    print(
        "per_block: the 162-state spin-one four-link face plus one charged edge is checked"
    )
    print(
        "lattice_wide: the local junction is compatible; photon survival on an extended quantum-link lattice is not claimed"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
