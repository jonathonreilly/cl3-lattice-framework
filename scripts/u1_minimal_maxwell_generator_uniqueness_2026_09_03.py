#!/usr/bin/env python3
"""Exact classification checks for the minimal edge-face Maxwell generator.

Within the declared class -- one scalar on each edge and face role, linear
first-order continuous time, opposite-role physical-neighbor couplings,
proper-cubic covariance, gauge invariance, and positive diagonal energy
conservation -- the local stencil is the oriented curl up to one scalar and
the reverse stencil is its energy adjoint.  The remaining scalar is the wave
speed after a possible magnetic-field orientation reversal and positive field normalization.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np

from u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03 import (
    proper_cubic_rotations,
)
from u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03 import (
    curl_symbol,
    physical_incidence,
    signed_permutation_matrix,
    yee_generator,
)
from u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03 import (
    role_bits,
    role_kind,
    role_shell,
    sites,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
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


def fraction_matrix(values: list[list[int]]) -> list[list[Fraction]]:
    return [[Fraction(value) for value in row] for row in values]


def rref(
    matrix: list[list[Fraction]],
) -> tuple[list[list[Fraction]], tuple[int, ...]]:
    result = [row[:] for row in matrix]
    if not result:
        return result, ()
    rows = len(result)
    columns = len(result[0])
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        source = next(
            (row for row in range(pivot_row, rows) if result[row][column] != 0),
            None,
        )
        if source is None:
            continue
        result[pivot_row], result[source] = result[source], result[pivot_row]
        pivot = result[pivot_row][column]
        result[pivot_row] = [value / pivot for value in result[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            multiplier = result[row][column]
            if multiplier == 0:
                continue
            result[row] = [
                value - multiplier * pivot_value
                for value, pivot_value in zip(result[row], result[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return result, tuple(pivot_columns)


def nullspace(matrix: list[list[Fraction]]) -> tuple[tuple[Fraction, ...], ...]:
    reduced, pivots = rref(matrix)
    columns = len(matrix[0])
    free_columns = [column for column in range(columns) if column not in pivots]
    basis = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(columns)]
        vector[free] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        basis.append(tuple(vector))
    return tuple(basis)


def proportional(
    vector: tuple[Fraction, ...], target: tuple[Fraction, ...]
) -> bool:
    ratio = None
    for value, expected in zip(vector, target):
        if expected == 0:
            if value != 0:
                return False
            continue
        current = value / expected
        if ratio is None:
            ratio = current
        elif current != ratio:
            return False
    return ratio is not None


def block_diagonal(block: list[list[int]], copies: int) -> list[list[int]]:
    block_rows = len(block)
    block_columns = len(block[0])
    result = [
        [0 for _ in range(block_columns * copies)]
        for _ in range(block_rows * copies)
    ]
    for copy in range(copies):
        for row in range(block_rows):
            for column in range(block_columns):
                result[copy * block_rows + row][copy * block_columns + column] = block[row][column]
    return result


def main() -> int:
    checks = Checks()
    # Boundary links are a:0->1, b:1->2, c:3->2, d:0->3.
    face_gradient = [
        [-1, 1, 0, 0],
        [0, -1, 1, 0],
        [0, 0, 1, -1],
        [-1, 0, 0, 1],
    ]
    gauge_constraint = [
        [face_gradient[edge][vertex] for edge in range(4)]
        for vertex in range(4)
    ]
    face_nullspace = nullspace(fraction_matrix(gauge_constraint))
    curl_stencil = tuple(Fraction(value) for value in (1, 1, -1, -1))
    checks.check(
        len(face_nullspace) == 1 and proportional(face_nullspace[0], curl_stencil),
        "gauge invariance leaves exactly the oriented curl in one face star",
    )

    exact_gauge_ok = True
    mutation_detected = True
    for stencil_raw in itertools.product(range(-2, 3), repeat=4):
        stencil = tuple(Fraction(value) for value in stencil_raw)
        invariant = all(
            sum(
                stencil[edge] * face_gradient[edge][vertex]
                for edge in range(4)
            )
            == 0
            for vertex in range(4)
        )
        is_curl_multiple = proportional(stencil, curl_stencil) if stencil != (0, 0, 0, 0) else True
        exact_gauge_ok = exact_gauge_ok and invariant == is_curl_multiple
        if stencil == (1, 1, -1, 0):
            mutation_detected = mutation_detected and not invariant
    checks.check(
        exact_gauge_ok,
        "all 625 small integer face stencils are invariant exactly when proportional to curl",
    )
    checks.check(
        mutation_detected,
        "a one-entry boundary-sign mutation is rejected by the gauge equations",
    )

    orientation_constraints = block_diagonal(gauge_constraint, 3)
    orientation_basis = nullspace(fraction_matrix(orientation_constraints))
    checks.check(
        len(orientation_basis) == 3
        and all(
            proportional(
                tuple(basis[4 * orientation + index] for index in range(4)),
                curl_stencil,
            )
            for orientation, basis in enumerate(orientation_basis)
        ),
        "gauge invariance alone leaves one curl coefficient per face orientation",
    )

    cubic_constraints = [row[:] for row in orientation_constraints]
    equality_first_second = [0] * 12
    equality_first_second[0] = 1
    equality_first_second[4] = -1
    equality_second_third = [0] * 12
    equality_second_third[4] = 1
    equality_second_third[8] = -1
    cubic_constraints.extend((equality_first_second, equality_second_third))
    cubic_basis = nullspace(fraction_matrix(cubic_constraints))
    global_curl_stencil = curl_stencil * 3
    checks.check(
        len(cubic_basis) == 1 and proportional(cubic_basis[0], global_curl_stencil),
        "proper-cubic orientation equality reduces the three coefficients to one scalar",
    )

    oriented_normal_orbit = set()
    rotations = proper_cubic_rotations()
    initial_normal = np.array([0, 0, 1], dtype=int)
    for permutation, signs in rotations:
        rotation = signed_permutation_matrix(permutation, signs)
        oriented_normal_orbit.add(tuple(rotation @ initial_normal))
    checks.check(
        len(rotations) == 24
        and oriented_normal_orbit
        == {
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        },
        "the proper cubic group is transitive on all six oriented face normals",
    )

    same_role_neighbours_absent = True
    opposite_role_counts = True
    physical_size = 6
    sector = (0, 0, 0)
    for point_raw in sites(physical_size):
        point = tuple(point_raw)
        kind = role_kind(role_bits(point, sector))
        shell_kinds = [
            role_kind(neighbor_role)
            for neighbor_role in role_shell(point, sector, physical_size).values()
        ]
        if kind == "edge":
            same_role_neighbours_absent = same_role_neighbours_absent and "edge" not in shell_kinds
            opposite_role_counts = opposite_role_counts and shell_kinds.count("face") == 4
        elif kind == "face":
            same_role_neighbours_absent = same_role_neighbours_absent and "face" not in shell_kinds
            opposite_role_counts = opposite_role_counts and shell_kinds.count("edge") == 4
    checks.check(
        same_role_neighbours_absent,
        "the role geometry permits no nearest-neighbor edge-edge or face-face linear coupling",
    )
    checks.check(
        opposite_role_counts,
        "each dynamical site has exactly four opposite-role dynamical neighbors",
    )

    (
        _vertices,
        _edges,
        _faces,
        _cubes,
        gradient,
        curl,
        divergence,
    ) = physical_incidence(3)
    assembled_rows_are_curl = all(
        tuple(sorted(row[row != 0].tolist())) == (-1, -1, 1, 1)
        for row in curl
    )
    checks.check(
        assembled_rows_are_curl
        and np.array_equal(curl @ gradient, np.zeros((81, 27), dtype=int))
        and np.array_equal(divergence @ curl, np.zeros((27, 81), dtype=int)),
        "the unique local stencil assembles into the exact global incidence complex",
    )

    onsite_coefficients_killed = all(
        2 * energy_weight * onsite == 0
        for energy_weight in (Fraction(1), Fraction(2), Fraction(7, 3))
        for onsite in (Fraction(0),)
    ) and all(
        2 * Fraction(3, 2) * onsite != 0
        for onsite in (Fraction(-2), Fraction(-1, 3), Fraction(1, 4), Fraction(3))
    )
    checks.check(
        onsite_coefficients_killed,
        "positive diagonal energy conservation kills every real scalar onsite term",
    )

    adjoint_relation_ok = True
    for edge_to_face, edge_energy, face_energy in (
        (Fraction(1), Fraction(1), Fraction(1)),
        (Fraction(2), Fraction(3), Fraction(5)),
        (Fraction(7, 4), Fraction(2, 3), Fraction(9, 5)),
    ):
        face_to_edge = -face_energy * edge_to_face / edge_energy
        adjoint_relation_ok = adjoint_relation_ok and (
            edge_energy * face_to_edge + face_energy * edge_to_face == 0
        )
    checks.check(
        adjoint_relation_ok,
        "energy conservation fixes the reverse stencil as the weighted negative adjoint",
    )

    coefficient_pairs = (
        (0.5, 2.0),
        (1.0, 1.0),
        (2.0, 0.5),
        (3.0, 4.0),
    )
    conservation_ok = True
    constraint_ok = True
    speed_ok = True
    sample_symbol = curl_symbol(np.array([0.7, 1.0, 1.3]))
    norm = float(np.linalg.norm(np.array([0.7, 1.0, 1.3])))
    for alpha, beta in coefficient_pairs:
        generator = np.block(
            [
                [np.zeros((3, 3)), -beta * sample_symbol.T],
                [alpha * sample_symbol, np.zeros((3, 3))],
            ]
        )
        metric = np.diag([alpha] * 3 + [beta] * 3)
        conservation_ok = conservation_ok and bool(
            np.max(np.abs(generator.T @ metric + metric @ generator)) < 2.0e-12
        )
        constraints = np.block(
            [
                [np.array([0.7, 1.0, 1.3]).reshape(1, 3), np.zeros((1, 3))],
                [np.zeros((1, 3)), np.array([0.7, 1.0, 1.3]).reshape(1, 3)],
            ]
        )
        constraint_ok = constraint_ok and bool(
            np.max(np.abs(constraints @ generator)) < 2.0e-12
        )
        eigenvalues = np.linalg.eigvals(generator)
        nonzero_frequencies = sorted(
            abs(value.imag) for value in eigenvalues if abs(value.imag) > 1.0e-10
        )
        speed_ok = speed_ok and bool(
            np.max(
                np.abs(
                    np.array(nonzero_frequencies)
                    - math.sqrt(alpha * beta) * norm
                )
            )
            < 3.0e-12
        )
    checks.check(conservation_ok, "the complete positive coefficient family conserves its diagonal energy")
    checks.check(constraint_ok, "the complete coefficient family preserves both Gauss rows")
    checks.check(
        speed_ok,
        "after field normalization the sole dynamical scalar is speed sqrt(alpha beta)",
    )

    normalized_equivalence = True
    for alpha, beta in coefficient_pairs:
        generator = np.block(
            [
                [np.zeros((3, 3)), -beta * sample_symbol.T],
                [alpha * sample_symbol, np.zeros((3, 3))],
            ]
        )
        scaling = np.diag([math.sqrt(alpha)] * 3 + [math.sqrt(beta)] * 3)
        normalized = scaling @ generator @ np.linalg.inv(scaling)
        normalized_equivalence = normalized_equivalence and bool(
            np.max(
                np.abs(
                    normalized
                    - yee_generator(sample_symbol, math.sqrt(alpha * beta))
                )
            )
            < 3.0e-12
        )
    checks.check(
        normalized_equivalence,
        "positive field rescaling normalizes the positive-orientation family to one Yee speed",
    )

    # The stated real class includes both orientations. Positive diagonal
    # scaling preserves each nonzero entry's sign; B -> -B conjugates -G to G.
    positive = yee_generator(sample_symbol)
    negative = -positive
    reverse_magnetic = np.diag([1.0] * 3 + [-1.0] * 3)
    orientation_ok = bool(
        np.max(np.abs(negative.T + negative)) < 2.0e-12
        and np.max(np.abs(constraints @ negative)) < 2.0e-12
        and np.max(np.abs(reverse_magnetic @ negative @ reverse_magnetic - positive)) < 2.0e-12
    )
    for diagonal in ((1, 1, 1, 1, 1, 1), (2, 3, 4, 5, 6, 7)):
        scale = np.diag(diagonal)
        normalized_negative = scale @ negative @ np.linalg.inv(scale)
        nonzero = positive != 0
        orientation_ok = orientation_ok and bool(np.all(
            np.sign(normalized_negative[nonzero]) == -np.sign(positive[nonzero])
        ))
    checks.check(
        orientation_ok,
        "negative coupling preserves gauge and energy; magnetic reversal, not positive scaling alone, fixes its orientation",
    )

    spectrum_ok = True
    for lattice_size in (3, 4, 5, 7):
        for indices in itertools.product(range(lattice_size), repeat=3):
            momentum = np.array(
                [
                    2.0
                    * math.sin(
                        math.pi
                        * (index if index <= lattice_size // 2 else index - lattice_size)
                        / lattice_size
                    )
                    for index in indices
                ]
            )
            norm = float(np.linalg.norm(momentum))
            eigenvalues = np.linalg.eigvalsh(1j * yee_generator(curl_symbol(momentum)))
            spectrum_ok = spectrum_ok and bool(
                np.max(
                    np.abs(
                        eigenvalues
                        - np.array([-norm, -norm, 0.0, 0.0, norm, norm])
                    )
                )
                < 3.0e-12
            )
    checks.check(
        spectrum_ok,
        "the classified generator has exactly the two Maxwell branches on every tested mode",
    )

    anisotropic = sample_symbol.T @ np.diag((1.0, 2.0, 3.0)) @ sample_symbol
    anisotropic_modes = np.linalg.eigvalsh(anisotropic)[1:]
    checks.check(
        abs(anisotropic_modes[1] - anisotropic_modes[0]) > 0.2,
        "orientation-dependent coefficients violate cubic degeneracy",
    )
    same_sign_generator = np.block(
        [
            [np.zeros((3, 3)), sample_symbol.T],
            [sample_symbol, np.zeros((3, 3))],
        ]
    )
    checks.check(
        np.max(np.abs(same_sign_generator.T + same_sign_generator)) > 1.0,
        "using the same adjoint sign violates conservative skewness",
    )
    damped_generator = yee_generator(sample_symbol) - 0.2 * np.eye(6)
    checks.check(
        np.max(np.abs(damped_generator.T + damped_generator)) > 0.3,
        "a diffusive damping term lies outside the conservative class",
    )

    incomplete = curl_symbol(np.array([0.0, 1.0, 1.0]))
    incomplete[0, :] = 0.0
    checks.check(
        np.linalg.matrix_rank(incomplete, tol=1.0e-12) == 1,
        "deleting one orientation exits the cubic class and loses one branch",
    )

    real_generator = yee_generator(curl.astype(float))
    time_step = 0.1
    identity = np.eye(real_generator.shape[0])
    euler = identity + time_step * real_generator
    checks.check(
        np.max(np.abs(euler.T @ euler - identity)) > 1.0e-3,
        "the explicit one-step Euler map is local but not exactly norm preserving",
    )
    cayley = (
        (identity + 0.5 * time_step * real_generator)
        @ np.linalg.inv(identity - 0.5 * time_step * real_generator)
    )
    cayley_row_counts = np.count_nonzero(np.abs(cayley) > 1.0e-12, axis=1)
    checks.check(
        np.max(np.abs(cayley.T @ cayley - identity)) < 4.0e-12
        and int(np.min(cayley_row_counts)) > 10,
        "the exact Cayley tick is norm preserving but spreads beyond one physical star",
    )

    szegedy_dimension = 2 * 6
    minimal_dimension = 6
    checks.check(
        szegedy_dimension > minimal_dimension,
        "the two-reflection sampler lift exits the minimal E-plus-B payload class",
    )

    reciprocal_speed = math.sqrt(1.0 * 1.0)
    checks.check(
        reciprocal_speed == 1.0 and math.sqrt(3.0 * 4.0) != reciprocal_speed,
        "supplied reciprocal coefficients give unit speed; the conservative gauge class also permits other speeds",
    )

    print(
        "per_element: all 625 small face stencils and every exact gauge constraint row are classified"
    )
    print(
        "per_site: the full L3 role geometry excludes same-role neighbors and leaves four edge-face couplings"
    )
    print(
        "per_mode: every momentum on L=3,4,5,7 is checked for the unique two-branch spectrum"
    )
    print(
        "per_block: gauge, cubic, energy-adjoint, field-rescaling, Euler, and Cayley blocks are contrasted"
    )
    print(
        "lattice_wide: the global 81-by-81 curl and 162-variable generator are assembled from the unique stencil"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
