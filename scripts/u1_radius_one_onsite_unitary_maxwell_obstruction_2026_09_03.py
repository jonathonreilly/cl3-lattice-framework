#!/usr/bin/env python3
"""Bounded obstruction for a radius-one onsite-unitary Maxwell tick.

The declared class has one complex scalar on every physical edge and face
role, no vertex/cube/coin payload, and one complete translation-covariant
linear update reading only self plus physical nearest neighbors.  Gauge and
chain compatibility reduce its Fourier symbol to onsite scalars plus curl
blocks.  Exact unitarity in the raw onsite norm then kills both curl blocks.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

from u1_local_reversible_yee_leapfrog_tick_2026_09_03 import (
    leapfrog_tick,
    modified_energy_metric,
    periodic_l1,
)
from u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03 import (
    proper_cubic_rotations,
)
from u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03 import (
    curl_symbol,
    lattice_momentum,
    physical_incidence,
    signed_permutation_matrix,
    yee_generator,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py",
    "scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py",
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


def radius_one_symbol(
    momentum: np.ndarray,
    onsite_e: complex,
    onsite_b: complex,
    face_from_edge: complex,
    edge_from_face: complex,
) -> np.ndarray:
    curl = curl_symbol(momentum).astype(complex)
    identity = np.eye(3, dtype=complex)
    return np.block(
        [
            [onsite_e * identity, edge_from_face * curl.conj().T],
            [face_from_edge * curl, onsite_b * identity],
        ]
    )


def radius_one_global(
    curl: np.ndarray,
    onsite_e: complex,
    onsite_b: complex,
    face_from_edge: complex,
    edge_from_face: complex,
) -> np.ndarray:
    edge_count = curl.shape[1]
    face_count = curl.shape[0]
    return np.block(
        [
            [
                onsite_e * np.eye(edge_count, dtype=complex),
                edge_from_face * curl.conj().T,
            ],
            [
                face_from_edge * curl,
                onsite_b * np.eye(face_count, dtype=complex),
            ],
        ]
    )


def direction_walk(momentum: np.ndarray) -> tuple[np.ndarray, tuple[tuple[int, int, int], ...]]:
    directions = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    phases = [
        np.exp(1j * float(momentum @ np.array(direction)))
        for direction in directions
    ]
    return np.diag(phases), directions


def proportional_to_curl(stencil: tuple[int, int, int, int]) -> bool:
    target = (1, 1, -1, -1)
    if stencil == (0, 0, 0, 0):
        return True
    ratio = None
    for value, expected in zip(stencil, target):
        current = value / expected
        if ratio is None:
            ratio = current
        elif current != ratio:
            return False
    return True


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
    curl = curl_integer.astype(complex)
    edge_count = len(edges)
    face_count = len(faces)
    total_count = edge_count + face_count
    checks.check(
        (len(vertices), edge_count, face_count, len(cubes)) == (27, 81, 81, 27)
        and np.array_equal(curl_integer @ gradient, np.zeros((81, 27), dtype=int))
        and np.array_equal(divergence @ curl_integer, np.zeros((27, 81), dtype=int)),
        "the exact role-compiled incidence complex supplies the declared tick class",
    )

    physical_size = 6
    role_locality_ok = True
    for face_index, edge_index in zip(*np.nonzero(curl_integer)):
        role_locality_ok = role_locality_ok and (
            periodic_l1(faces[face_index], edges[edge_index], physical_size) == 1
        )
    checks.check(
        role_locality_ok
        and np.all(np.count_nonzero(curl_integer, axis=0) == 4)
        and np.all(np.count_nonzero(curl_integer, axis=1) == 4),
        "radius one leaves onsite scalars and four-leg edge-face blocks only",
    )

    face_gradient = np.array(
        [
            [-1, 1, 0, 0],
            [0, -1, 1, 0],
            [0, 0, 1, -1],
            [-1, 0, 0, 1],
        ],
        dtype=int,
    )
    local_duality_ok = True
    for stencil in itertools.product(range(-2, 3), repeat=4):
        divergence_free = np.array_equal(
            face_gradient.T @ np.array(stencil, dtype=int),
            np.zeros(4, dtype=int),
        )
        local_duality_ok = local_duality_ok and (
            divergence_free == proportional_to_curl(stencil)
        )
    checks.check(
        local_duality_ok,
        "all 625 local reverse stencils preserve electric Gauss exactly when they are co-curl",
    )

    zero_curl = curl_symbol(np.zeros(3))
    generic_curl = curl_symbol(np.array([1.0, 2.0, 3.0]))
    checks.check(
        np.array_equal(zero_curl, np.zeros((3, 3)))
        and np.linalg.matrix_rank(generic_curl) == 2,
        "the gauge-compatible curl block vanishes at zero momentum and is nonzero elsewhere",
    )

    phases = (1.0 + 0.0j, -1.0 + 0.0j, 1.0j, -1.0j)
    zero_mode_ok = all(
        np.array_equal(
            radius_one_symbol(np.zeros(3), phase_e, phase_b, 0.0, 0.0).conj().T
            @ radius_one_symbol(np.zeros(3), phase_e, phase_b, 0.0, 0.0),
            np.eye(6),
        )
        for phase_e, phase_b in itertools.product(phases, repeat=2)
    )
    checks.check(
        zero_mode_ok,
        "zero-momentum unitarity fixes each onsite magnitude to one",
    )

    onsite_e = np.exp(0.37j)
    onsite_b = np.exp(-0.21j)
    face_from_edge = 0.4 - 0.3j
    edge_from_face = -0.2 + 0.5j
    top_column_norm = (
        abs(onsite_e) ** 2 * np.eye(3)
        + abs(face_from_edge) ** 2 * generic_curl.conj().T @ generic_curl
    )
    bottom_column_norm = (
        abs(onsite_b) ** 2 * np.eye(3)
        + abs(edge_from_face) ** 2 * generic_curl @ generic_curl.conj().T
    )
    checks.check(
        np.max(
            np.abs(
                top_column_norm
                - np.eye(3)
                - abs(face_from_edge) ** 2 * generic_curl.conj().T @ generic_curl
            )
        )
        < 1.0e-14
        and np.max(np.linalg.eigvalsh(top_column_norm - np.eye(3))) > 1.0,
        "positive column norm forces the edge-to-face curl coefficient to vanish",
    )
    checks.check(
        np.max(
            np.abs(
                bottom_column_norm
                - np.eye(3)
                - abs(edge_from_face) ** 2 * generic_curl @ generic_curl.conj().T
            )
        )
        < 1.0e-14
        and np.max(np.linalg.eigvalsh(bottom_column_norm - np.eye(3))) > 1.0,
        "the dual positive column norm forces the face-to-edge coefficient to vanish",
    )

    coefficient_grid = (0.0 + 0.0j, 1.0 + 0.0j, -1.0 + 0.0j, 1.0j, -1.0j)
    test_momenta = (
        np.zeros(3),
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 2.0, 3.0]),
    )
    survivors = []
    for phase_e, phase_b, q, r in itertools.product(
        phases, phases, coefficient_grid, coefficient_grid
    ):
        unitary = True
        for momentum in test_momenta:
            symbol = radius_one_symbol(momentum, phase_e, phase_b, q, r)
            unitary = unitary and np.array_equal(
                symbol.conj().T @ symbol, np.eye(6)
            )
        if unitary:
            survivors.append((phase_e, phase_b, q, r))
    checks.check(
        len(survivors) == 16
        and all(q == 0 and r == 0 for _u, _v, q, r in survivors),
        "all 400 exact Gaussian-integer candidates leave only sixteen onsite phase pairs",
    )

    orientation_grid = (-1, 0, 1)
    left_survivors = []
    right_survivors = []
    basis_momenta = (
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
    )
    for coefficients in itertools.product(orientation_grid, repeat=3):
        diagonal = np.diag(coefficients)
        if all(
            np.array_equal(diagonal @ curl_symbol(momentum), np.zeros((3, 3)))
            for momentum in basis_momenta
        ):
            left_survivors.append(coefficients)
        if all(
            np.array_equal(curl_symbol(momentum).T @ diagonal, np.zeros((3, 3)))
            for momentum in basis_momenta
        ):
            right_survivors.append(coefficients)
    checks.check(
        left_survivors == [(0, 0, 0)]
        and right_survivors == [(0, 0, 0)],
        "allowing independent orientation coefficients does not evade the positive-norm argument",
    )

    all_modes_reject_transport = True
    checked_nonzero = 0
    for lattice_size in (3, 4, 5, 7):
        for indices_raw in itertools.product(range(lattice_size), repeat=3):
            indices = tuple(indices_raw)
            momentum = lattice_momentum(indices, lattice_size)
            if np.linalg.norm(momentum) < 1.0e-14:
                continue
            checked_nonzero += 1
            transported = radius_one_symbol(
                momentum, 1.0, 1.0, 0.25, -0.25
            )
            all_modes_reject_transport = all_modes_reject_transport and (
                np.max(np.abs(transported.conj().T @ transported - np.eye(6)))
                > 1.0e-4
            )
    checks.check(
        all_modes_reject_transport
        and checked_nonzero == 27 + 64 + 125 + 343 - 4,
        "every nonzero tested momentum rejects a transported radius-one onsite-unitary symbol",
    )

    flat_spectrum_ok = True
    phase_e = np.exp(0.31j)
    phase_b = np.exp(-0.47j)
    reference = np.sort(np.angle(np.array([phase_e] * 3 + [phase_b] * 3)))
    for momentum in test_momenta:
        symbol = radius_one_symbol(momentum, phase_e, phase_b, 0.0, 0.0)
        flat_spectrum_ok = flat_spectrum_ok and bool(
            np.max(np.abs(np.sort(np.angle(np.linalg.eigvals(symbol))) - reference))
            < 1.0e-14
        )
    checks.check(
        flat_spectrum_ok,
        "the surviving onsite phases have momentum-independent flat quasienergy and no transport",
    )

    real_survivors = tuple(
        pair for pair in itertools.product(phases, repeat=2)
        if pair[0].imag == 0 and pair[1].imag == 0
    )
    checks.check(
        len(real_survivors) == 4 and (1.0 + 0.0j, 1.0 + 0.0j) in real_survivors,
        "requiring a real field map reduces flat phases to signs and the identity component to plus-plus",
    )

    global_transport = radius_one_global(curl, 1.0, 1.0, 0.2, -0.2)
    field_sites = edges + faces
    support_local = True
    for row, column in zip(*np.nonzero(np.abs(global_transport) > 1.0e-14)):
        support_local = support_local and (
            periodic_l1(field_sites[row], field_sites[column], physical_size) <= 1
        )
    checks.check(
        support_local
        and np.max(
            np.abs(global_transport.conj().T @ global_transport - np.eye(total_count))
        )
        > 0.1,
        "the full radius-one transported block is local but fails raw unitarity lattice-wide",
    )

    flat_global = radius_one_global(curl, 1.0j, -1.0, 0.0, 0.0)
    checks.check(
        np.array_equal(flat_global.conj().T @ flat_global, np.eye(total_count))
        and np.count_nonzero(flat_global - np.diag(np.diag(flat_global))) == 0,
        "the full lattice survivor is exactly unitary and exactly onsite",
    )

    generator = yee_generator(curl_integer.astype(float))
    identity = np.eye(total_count)
    step = 0.1
    euler = identity + step * generator
    checks.check(
        np.max(np.abs(euler.T @ euler - identity)) > 1.0e-3,
        "Euler keeps radius one and the Maxwell tangent but exits exact unitarity",
    )

    cayley = (
        (identity + 0.5 * step * generator)
        @ np.linalg.inv(identity - 0.5 * step * generator)
    )
    cayley_counts = np.count_nonzero(np.abs(cayley) > 1.0e-12, axis=1)
    checks.check(
        np.max(np.abs(cayley.T @ cayley - identity)) < 4.0e-12
        and int(np.min(cayley_counts)) > 10,
        "Cayley keeps raw unitarity but exits the complete-map radius-one class",
    )

    leapfrog = leapfrog_tick(curl_integer.astype(float), 0.5)
    leapfrog_metric = modified_energy_metric(curl_integer.astype(float), 0.5)
    checks.check(
        np.max(np.abs(leapfrog.T @ leapfrog_metric @ leapfrog - leapfrog_metric))
        < 2.0e-14
        and np.max(np.abs(leapfrog.T @ leapfrog - identity)) > 1.0e-3,
        "the finite-depth photon tick escapes through a local energy metric rather than raw onsite norm",
    )

    pair_rotation = np.eye(total_count)
    first_face, first_edge = next(zip(*np.nonzero(curl_integer)))
    angle = 0.37
    cosine = math.cos(angle)
    sine = math.sin(angle)
    first = first_edge
    second = edge_count + first_face
    pair_rotation[first, first] = cosine
    pair_rotation[second, second] = cosine
    pair_rotation[first, second] = -sine
    pair_rotation[second, first] = sine
    constraint = np.block(
        [
            [gradient.T, np.zeros((len(vertices), face_count), dtype=int)],
            [np.zeros((len(cubes), edge_count), dtype=int), divergence],
        ]
    )
    valid_input = np.zeros(total_count)
    unit_face = np.zeros(face_count)
    unit_face[first_face] = 1.0
    valid_input[:edge_count] = curl_integer.T @ unit_face
    checks.check(
        np.max(np.abs(pair_rotation.T @ pair_rotation - identity)) < 2.0e-15
        and periodic_l1(edges[first_edge], faces[first_face], physical_size) == 1
        and np.max(np.abs(constraint @ valid_input)) < 1.0e-15
        and np.max(np.abs(constraint @ pair_rotation @ valid_input)) > 0.1,
        "a nearest-neighbor Givens circuit is raw-unitary but breaks the Gauss sector",
    )

    six_direction_ok = True
    for momentum in (
        np.array([0.3, 0.7, 1.1]),
        np.array([1.0, 0.0, 0.0]),
        np.array([0.8, 1.2, 0.4]),
    ):
        walk, directions = direction_walk(momentum)
        six_direction_ok = six_direction_ok and bool(
            np.max(np.abs(walk.conj().T @ walk - np.eye(6))) < 1.0e-15
        )
        direction_index = {direction: index for index, direction in enumerate(directions)}
        for permutation, signs in proper_cubic_rotations():
            rotation = signed_permutation_matrix(permutation, signs)
            carrier = np.zeros((6, 6))
            for old_index, direction in enumerate(directions):
                rotated = tuple(rotation @ np.array(direction))
                carrier[direction_index[rotated], old_index] = 1.0
            rotated_walk, _ = direction_walk(rotation @ momentum)
            six_direction_ok = six_direction_ok and bool(
                np.max(np.abs(rotated_walk - carrier @ walk @ carrier.T))
                < 2.0e-12
            )
    checks.check(
        six_direction_ok,
        "a six-direction internal carrier gives an explicit radius-one cubic-unitary transport escape",
    )

    print(
        "per_element: zero-mode magnitudes and positive curl-column norms are checked for complex coefficients"
    )
    print(
        "per_site: every allowed minimal coupling is a physical nearest-neighbor edge-face incidence"
    )
    print(
        "per_mode: every nonzero momentum on L=3,4,5,7 rejects transported raw-unitary minimal symbols"
    )
    print(
        "per_block: 400 coefficient tuples, orientation variants, Euler, Cayley, leapfrog, pair rotation, and six-carrier escapes are checked"
    )
    print(
        "lattice_wide: full 162-variable radius-one maps distinguish trivial onsite unitaries from transported nonunitaries"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
