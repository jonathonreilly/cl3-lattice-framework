#!/usr/bin/env python3
"""Exact source work and a closed two-tick dipole radiation packet.

For the finite-depth local Maxwell tick, a supplied edge current obeys the
exact discrete work identity

    H_h(x') - H_h(x) = h J^T (E + E') / 2.

A current pulse followed one tick later by its negative creates a temporary
nearest-neighbor charge dipole, returns charge exactly to zero, and leaves a
nonzero field entirely in the curl/co-curl photon sector.  Sparse propagation
then checks exact field-energy conservation, the causal support ladder, and
outward transport on a larger periodic block before wraparound.
"""

from __future__ import annotations

import numpy as np
from scipy import sparse

from u1_conserved_source_coulomb_photon_bridge_2026_09_03 import sourced_tick
from u1_local_reversible_yee_leapfrog_tick_2026_09_03 import (
    all_cubic_transformations,
    exact_half_step_matrices,
    modified_energy_metric,
    periodic_l1,
)
from u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03 import (
    curl_symbol,
    edge_axis,
    face_boundary_sites,
    physical_incidence,
    role_bits,
    role_kind,
    sites,
)


AUDIT_TIMEOUT_SEC = 120

# Actual helper closure plus the declared conditional premise/context closure.
AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_EXACT_MIDPOINT_SOURCE_WORK_CLOSED_DIPOLE_PURE_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_conserved_source_coulomb_photon_bridge_2026_09_03.py",
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


def field_energy(
    curl: np.ndarray | sparse.spmatrix,
    electric: np.ndarray,
    magnetic: np.ndarray,
    step: float,
) -> float:
    face_curl = curl @ electric
    return float(
        0.5 * (electric @ electric + magnetic @ magnetic)
        - step**2 * (face_curl @ face_curl) / 8.0
    )


def source_work(
    electric_old: np.ndarray,
    electric_new: np.ndarray,
    current: np.ndarray,
    step: float,
) -> float:
    return float(0.5 * step * current @ (electric_old + electric_new))


def sparse_physical_curl(
    coarse_size: int,
) -> tuple[
    tuple[tuple[int, int, int], ...],
    tuple[tuple[int, int, int], ...],
    sparse.csr_matrix,
]:
    """Build the role compiler's curl without allocating a dense L^6 array."""

    physical_size = 2 * coarse_size
    sector = (0, 0, 0)
    role_sites: dict[str, list[tuple[int, int, int]]] = {
        "vertex": [],
        "edge": [],
        "face": [],
        "cube": [],
    }
    for raw_point in sites(physical_size):
        point = tuple(raw_point)
        role_sites[role_kind(role_bits(point, sector))].append(point)
    edges = tuple(sorted(role_sites["edge"]))
    faces = tuple(sorted(role_sites["face"]))
    edge_index = {point: index for index, point in enumerate(edges)}

    rows: list[int] = []
    columns: list[int] = []
    values: list[int] = []
    for row, face in enumerate(faces):
        boundary = face_boundary_sites(
            face, role_bits(face, sector), physical_size
        )
        for edge, sign in zip(boundary, (1, 1, -1, -1)):
            rows.append(row)
            columns.append(edge_index[edge])
            values.append(sign)
    curl = sparse.csr_matrix(
        (values, (rows, columns)),
        shape=(len(faces), len(edges)),
        dtype=float,
    )
    return edges, faces, curl


def closed_dipole_formula(
    curl: np.ndarray,
    current: np.ndarray,
    step: float,
) -> tuple[np.ndarray, np.ndarray]:
    curl_current = curl @ current
    electric = -(step**3) * curl.T @ curl_current
    magnetic = (
        step**2 * curl_current
        - 0.5 * step**4 * curl @ (curl.T @ curl_current)
    )
    return electric, magnetic


def main() -> int:
    checks = Checks()
    (
        vertices,
        edges,
        faces,
        cubes,
        gradient,
        curl_integer,
        divergence,
    ) = physical_incidence(3)
    curl = curl_integer.astype(float)
    edge_count = len(edges)
    face_count = len(faces)
    total_count = edge_count + face_count
    checks.check(
        np.array_equal(curl_integer @ gradient, np.zeros((81, 27), dtype=int))
        and np.array_equal(
            divergence @ curl_integer, np.zeros((27, 81), dtype=int)
        ),
        "the work and radiation checks use the exact physical incidence complex",
    )

    # At h=1/2 the parent tick is U_num/32, its energy metric is M_num/16,
    # and the affine source response is R_num/8 with R_num=(4I,C)^T.
    magnetic_numerator, electric_numerator = exact_half_step_matrices(
        curl_integer
    )
    tick_numerator = (
        magnetic_numerator @ electric_numerator @ magnetic_numerator
    )
    metric_numerator = np.block(
        [
            [
                16 * np.eye(edge_count, dtype=np.int64)
                - curl_integer.T @ curl_integer,
                np.zeros((edge_count, face_count), dtype=np.int64),
            ],
            [
                np.zeros((face_count, edge_count), dtype=np.int64),
                16 * np.eye(face_count, dtype=np.int64),
            ],
        ]
    )
    source_response_numerator = np.vstack(
        (4 * np.eye(edge_count, dtype=np.int64), curl_integer)
    )
    electric_inclusion = np.vstack(
        (
            np.eye(edge_count, dtype=np.int64),
            np.zeros((face_count, edge_count), dtype=np.int64),
        )
    )
    checks.check(
        np.array_equal(
            tick_numerator.T
            @ metric_numerator
            @ source_response_numerator,
            32
            * (
                32 * electric_inclusion
                + tick_numerator.T @ electric_inclusion
            ),
        ),
        "the source-work cross term holds exactly as an integer matrix identity",
    )
    checks.check(
        np.array_equal(
            source_response_numerator.T
            @ metric_numerator
            @ source_response_numerator,
            256 * np.eye(edge_count, dtype=np.int64),
        ),
        "the source-work quadratic term holds exactly as an integer matrix identity",
    )

    step = 0.5
    metric = modified_energy_metric(curl, step)
    deterministic_fields = (
        (
            np.array(
                [(7 * index + 2) % 13 - 6 for index in range(edge_count)],
                dtype=float,
            ),
            np.array(
                [(5 * index + 1) % 11 - 5 for index in range(face_count)],
                dtype=float,
            ),
            np.array(
                [(3 * index + 4) % 9 - 4 for index in range(edge_count)],
                dtype=float,
            ),
        ),
        (
            np.linspace(-0.7, 0.9, edge_count),
            np.linspace(0.6, -0.4, face_count),
            np.cos(np.arange(edge_count, dtype=float)),
        ),
    )
    work_identity_ok = True
    for electric_old, magnetic_old, current in deterministic_fields:
        electric_new, magnetic_new = sourced_tick(
            curl, electric_old, magnetic_old, current, step
        )
        state_old = np.concatenate((electric_old, magnetic_old))
        state_new = np.concatenate((electric_new, magnetic_new))
        energy_change = 0.5 * float(
            state_new @ metric @ state_new - state_old @ metric @ state_old
        )
        work_identity_ok = work_identity_ok and (
            abs(
                energy_change
                - source_work(electric_old, electric_new, current, step)
            )
            < 3.0e-11
        )
    checks.check(
        work_identity_ok,
        "deterministic full-field trials reproduce midpoint source work",
    )

    zero_current = np.zeros(edge_count)
    electric_old, magnetic_old, _current = deterministic_fields[0]
    electric_free, magnetic_free = sourced_tick(
        curl, electric_old, magnetic_old, zero_current, step
    )
    checks.check(
        abs(
            field_energy(curl, electric_free, magnetic_free, step)
            - field_energy(curl, electric_old, magnetic_old, step)
        )
        < 2.0e-11,
        "zero source reduces the work theorem to exact parent field-energy conservation",
    )

    # A current followed by its negative makes and then erases a local charge
    # dipole, while the one-tick delay leaves a transverse field packet.
    current = np.zeros(edge_count)
    current[0] = 1.0 / step
    charge = np.zeros(len(vertices))
    electric = np.zeros(edge_count)
    magnetic = np.zeros(face_count)
    electric_before = electric.copy()
    electric, magnetic = sourced_tick(
        curl, electric, magnetic, current, step
    )
    work_first = source_work(electric_before, electric, current, step)
    charge = charge + step * gradient.T @ current
    first_charge = charge.copy()
    checks.check(
        tuple(sorted(first_charge[first_charge != 0.0])) == (-1.0, 1.0)
        and np.count_nonzero(first_charge) == 2,
        "the first pulse creates a unit nearest-neighbor charge dipole",
    )

    electric_before = electric.copy()
    electric, magnetic = sourced_tick(
        curl, electric, magnetic, -current, step
    )
    work_second = source_work(electric_before, electric, -current, step)
    charge = charge - step * gradient.T @ current
    checks.check(
        np.array_equal(charge, np.zeros(len(vertices))),
        "the reversed second pulse returns every vertex charge exactly to zero",
    )

    expected_electric, expected_magnetic = closed_dipole_formula(
        curl, current, step
    )
    checks.check(
        np.array_equal(electric, expected_electric)
        and np.array_equal(magnetic, expected_magnetic),
        "the closed two-tick pulse has the derived curl/co-curl field formula exactly",
    )

    current_integer = np.zeros(edge_count, dtype=np.int64)
    current_integer[0] = 2
    curl_current = curl_integer @ current_integer
    co_curl_current = curl_integer.T @ curl_current
    electric_final_numerator = -4 * co_curl_current
    magnetic_final_numerator = (
        8 * curl_current - curl_integer @ co_curl_current
    )
    final_state_numerator = np.concatenate(
        (electric_final_numerator, magnetic_final_numerator)
    )
    checks.check(
        np.array_equal(
            gradient.T @ electric_final_numerator,
            np.zeros(len(vertices), dtype=np.int64),
        )
        and np.array_equal(
            divergence @ magnetic_final_numerator,
            np.zeros(len(cubes), dtype=np.int64),
        ),
        "the post-dipole radiation packet obeys both Gauss laws exactly",
    )
    checks.check(
        np.count_nonzero(final_state_numerator) > 0
        and np.array_equal(
            electric_final_numerator, -4 * curl_integer.T @ curl_current
        ),
        "the returned charge leaves a nonzero field wholly in the transverse incidence images",
    )
    checks.check(
        all(
            int(
                np.sum(
                    electric_final_numerator[
                        [
                            index
                            for index, edge in enumerate(edges)
                            if edge_axis(role_bits(edge, (0, 0, 0))) == axis
                        ]
                    ]
                )
            )
            == 0
            and int(
                np.sum(
                    magnetic_final_numerator[
                        [
                            index
                            for index, face in enumerate(faces)
                            if role_bits(face, (0, 0, 0))[axis] == 0
                        ]
                    ]
                )
            )
            == 0
            for axis in range(3)
        ),
        "the pulse leaves no constant harmonic electric or magnetic field",
    )

    exact_energy_numerator = int(
        final_state_numerator @ metric_numerator @ final_state_numerator
    )
    checks.check(
        exact_energy_numerator == 16384,
        "the unit-dipole radiation packet has positive modified energy exactly one half",
    )
    final_energy = field_energy(curl, electric, magnetic, step)
    checks.check(
        abs(final_energy - (work_first + work_second)) < 2.0e-13
        and abs(final_energy - 0.5) < 2.0e-13,
        "accumulated midpoint work equals the complete residual radiation energy",
    )

    reversed_electric, reversed_magnetic = sourced_tick(
        curl, electric, magnetic, -current, -step
    )
    reversed_electric, reversed_magnetic = sourced_tick(
        curl, reversed_electric, reversed_magnetic, current, -step
    )
    checks.check(
        np.array_equal(reversed_electric, np.zeros(edge_count))
        and np.array_equal(reversed_magnetic, np.zeros(face_count)),
        "reversing time and the ordered source history returns the packet to zero exactly",
    )

    opposite_electric = np.zeros(edge_count)
    opposite_magnetic = np.zeros(face_count)
    opposite_electric, opposite_magnetic = sourced_tick(
        curl, opposite_electric, opposite_magnetic, -current, step
    )
    opposite_electric, opposite_magnetic = sourced_tick(
        curl, opposite_electric, opposite_magnetic, current, step
    )
    checks.check(
        np.array_equal(opposite_electric, -electric)
        and np.array_equal(opposite_magnetic, -magnetic),
        "reversing the dipole orientation reverses the field and keeps its energy",
    )

    sparse_edges3, sparse_faces3, sparse_curl3 = sparse_physical_curl(3)
    checks.check(
        sparse_edges3 == edges
        and sparse_faces3 == faces
        and np.array_equal(sparse_curl3.toarray(), curl_integer),
        "the sparse large-volume propagator is byte-identical to the dense role curl at L=3",
    )

    # Large sparse propagation before the light cone wraps around the L=20
    # coarse torus. Squared raw amplitude is used only as a location diagnostic;
    # exact conservation is checked with the modified field energy above.
    large_size = 20
    large_edges, large_faces, large_curl = sparse_physical_curl(large_size)
    edge_index = {point: index for index, point in enumerate(large_edges)}
    source_site = (
        2 * (large_size // 2) + 1,
        2 * (large_size // 2),
        2 * (large_size // 2),
    )
    large_current = np.zeros(len(large_edges))
    large_current[edge_index[source_site]] = 1.0 / step
    large_electric = np.zeros(len(large_edges))
    large_magnetic = np.zeros(len(large_faces))
    large_electric, large_magnetic = sourced_tick(
        large_curl,
        large_electric,
        large_magnetic,
        large_current,
        step,
    )
    large_electric, large_magnetic = sourced_tick(
        large_curl,
        large_electric,
        large_magnetic,
        -large_current,
        step,
    )
    all_sites = large_edges + large_faces
    distances = np.array(
        [periodic_l1(source_site, point, 2 * large_size) for point in all_sites]
    )
    energies = []
    centroids = []
    near_fractions = []
    support_radii = []
    for _cycle in range(9):
        energies.append(
            field_energy(
                large_curl, large_electric, large_magnetic, step
            )
        )
        weights = np.concatenate((large_electric**2, large_magnetic**2))
        centroids.append(float(weights @ distances / np.sum(weights)))
        near_fractions.append(
            float(np.sum(weights[distances <= 3]) / np.sum(weights))
        )
        support_radii.append(
            int(np.max(distances[np.abs(weights) > 1.0e-26]))
        )
        large_electric, large_magnetic = sourced_tick(
            large_curl,
            large_electric,
            large_magnetic,
            np.zeros(len(large_edges)),
            step,
        )
    checks.check(
        max(abs(value - 0.5) for value in energies) < 2.0e-13,
        "the emitted packet conserves its exact modified energy for eight source-free cycles",
    )
    checks.check(
        support_radii == list(range(3, 20, 2)),
        "the radiation support advances on the exact finite causal ladder 3,5,...,19",
    )
    checks.check(
        all(left < right for left, right in zip(centroids, centroids[1:]))
        and centroids[-1] > 8.9,
        "the squared-field centroid moves monotonically away from the closed source",
    )
    checks.check(
        near_fractions[0] == 1.0 and near_fractions[-1] < 0.002,
        "more than 99.8 percent of squared field amplitude leaves the radius-three source neighborhood",
    )

    # The work scalar and source update must not pick a preferred cubic axis.
    cubic_work_ok = True
    sample_electric = np.array([0.2, -0.3, 0.7])
    sample_magnetic = np.array([-0.4, 0.8, 0.1])
    sample_current = np.array([0.6, -0.2, 0.5])
    for symbol in (
        np.array([0.3, 0.7, 1.1]),
        np.array([1.0, 0.0, 0.0]),
    ):
        curl_block = curl_symbol(symbol)
        electric_out, magnetic_out = sourced_tick(
            curl_block,
            sample_electric,
            sample_magnetic,
            sample_current,
            step,
        )
        work = source_work(
            sample_electric, electric_out, sample_current, step
        )
        for transform in all_cubic_transformations():
            determinant = int(round(np.linalg.det(transform)))
            transformed_electric, transformed_magnetic = sourced_tick(
                curl_symbol(transform @ symbol),
                transform @ sample_electric,
                determinant * transform @ sample_magnetic,
                transform @ sample_current,
                step,
            )
            transformed_work = source_work(
                transform @ sample_electric,
                transformed_electric,
                transform @ sample_current,
                step,
            )
            cubic_work_ok = cubic_work_ok and bool(
                abs(transformed_work - work) < 2.0e-13
                and np.max(
                    np.abs(transformed_electric - transform @ electric_out)
                )
                < 2.0e-12
                and np.max(
                    np.abs(
                        transformed_magnetic
                        - determinant * transform @ magnetic_out
                    )
                )
                < 2.0e-12
            )
    checks.check(
        cubic_work_ok,
        "source work and the driven field covary under all 48 cubic transformations",
    )

    # A simultaneous cancellation is the zero-source control. The nonzero
    # packet above is caused by the one-tick temporal separation, not by a
    # hidden static source or an arithmetic offset.
    cancel_electric, cancel_magnetic = sourced_tick(
        curl,
        np.zeros(edge_count),
        np.zeros(face_count),
        current - current,
        step,
    )
    checks.check(
        np.array_equal(cancel_electric, np.zeros(edge_count))
        and np.array_equal(cancel_magnetic, np.zeros(face_count)),
        "simultaneous opposite currents cancel while a one-tick-separated pair radiates",
    )

    print(
        "per_element: each source coefficient, incidence sign, and exact work numerator is checked"
    )
    print(
        "per_site: one edge pulse creates and erases charges only on its two neighboring vertices"
    )
    print(
        "per_mode: the residual field lies in curl/co-curl images with no longitudinal or harmonic component"
    )
    print(
        "per_block: exact work, Gauss laws, reversal, cubic covariance, and dipole controls are checked"
    )
    print(
        "lattice_wide: an L=20 sparse block conserves energy and carries the packet from support radius 3 through 19"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
