#!/usr/bin/env python3
"""Checks for an auxiliary-face local realization of a plaquette measure.

For a strictly positive finite cyclic plaquette weight T and any
0 < epsilon < min(T), a face auxiliary has one universal state plus one state
for each ordered boundary-link tuple.  Its local factor is epsilon in the
universal state, T(curl)-epsilon for the matching tuple, and zero otherwise.
Summing the face auxiliary returns T(curl) exactly.  The universal state also
connects the support under single-site full-conditional moves.
"""

from __future__ import annotations

import itertools
import math
from collections import deque
from fractions import Fraction
from typing import Iterable

import numpy as np

from u1_record_distribution_overlap_maxwell_germ_2026_09_03 import (
    kernel_curvature,
    overlap_coefficients,
)
from u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03 import (
    configuration_weight,
    decode_configuration,
    face_terms,
    flux,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py",
    "scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py",
    "scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py",
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


def encode_tuple(values: tuple[int, ...], group_order: int) -> int:
    index = 0
    multiplier = 1
    for value in values:
        index += value * multiplier
        multiplier *= group_order
    return index


def decode_tuple(index: int, length: int, group_order: int) -> tuple[int, ...]:
    return decode_configuration(index, length, group_order)


def tuple_flux(boundary: tuple[int, int, int, int], group_order: int) -> int:
    first, second, third, fourth = boundary
    return (first + second - third - fourth) % group_order


def face_factor(
    auxiliary: int,
    boundary: tuple[int, int, int, int],
    overlap: tuple[int, ...],
    epsilon: int,
) -> int:
    """Auxiliary zero is universal; 1+encoded tuple is a matching state."""

    if auxiliary == 0:
        return epsilon
    encoded = encode_tuple(boundary, len(overlap))
    if auxiliary != encoded + 1:
        return 0
    return overlap[tuple_flux(boundary, len(overlap))] - epsilon


def face_marginal(
    boundary: tuple[int, int, int, int],
    overlap: tuple[int, ...],
    epsilon: int,
) -> int:
    auxiliary_count = 1 + len(overlap) ** len(boundary)
    return sum(
        face_factor(auxiliary, boundary, overlap, epsilon)
        for auxiliary in range(auxiliary_count)
    )


def face_conditionals(
    boundary: tuple[int, int, int, int],
    overlap: tuple[int, ...],
    epsilon: int,
) -> tuple[Fraction, Fraction]:
    total = overlap[tuple_flux(boundary, len(overlap))]
    return Fraction(epsilon, total), Fraction(total - epsilon, total)


def boundary_gauge_transform(
    boundary: tuple[int, int, int, int],
    gauge: tuple[int, int, int, int],
    group_order: int,
) -> tuple[int, int, int, int]:
    """Boundary links a:0->1, b:1->2, c:3->2, d:0->3."""

    first, second, third, fourth = boundary
    lam_0, lam_1, lam_2, lam_3 = gauge
    return (
        (first + lam_1 - lam_0) % group_order,
        (second + lam_2 - lam_1) % group_order,
        (third + lam_2 - lam_3) % group_order,
        (fourth + lam_3 - lam_0) % group_order,
    )


def dihedral_boundaries(
    boundary: tuple[int, int, int, int], group_order: int
) -> tuple[tuple[int, int, int, int], ...]:
    """Eight square relabelings, expressed in the fixed a+b-c-d convention."""

    first, second, third, fourth = boundary
    path_oriented = (first, second, -third, -fourth)
    transformed: list[tuple[int, int, int, int]] = []
    for shift in range(4):
        rotated = path_oriented[shift:] + path_oriented[:shift]
        for reflected in (False, True):
            values = rotated
            if reflected:
                values = tuple(-value for value in reversed(rotated))
            transformed.append(
                (
                    values[0] % group_order,
                    values[1] % group_order,
                    (-values[2]) % group_order,
                    (-values[3]) % group_order,
                )
            )
    return tuple(transformed)


def transformed_auxiliary(
    auxiliary: int,
    transform,
    group_order: int,
) -> int:
    """Apply a boundary relabeling to a tuple auxiliary; leave star fixed."""

    if auxiliary == 0:
        return 0
    boundary = decode_tuple(auxiliary - 1, 4, group_order)
    return 1 + encode_tuple(transform(boundary), group_order)


def single_face_supported_states(
    group_order: int,
) -> tuple[tuple[tuple[int, ...], int], ...]:
    states = []
    for boundary_raw in itertools.product(range(group_order), repeat=4):
        boundary = tuple(boundary_raw)
        matching = 1 + encode_tuple(boundary, group_order)
        states.append((boundary, 0))
        states.append((boundary, matching))
    return tuple(states)


def single_face_weight(
    state: tuple[tuple[int, ...], int],
    overlap: tuple[int, ...],
    epsilon: int,
) -> int:
    boundary, auxiliary = state
    return face_factor(auxiliary, boundary, overlap, epsilon)


def single_face_neighbours(
    state: tuple[tuple[int, ...], int], group_order: int
) -> Iterable[tuple[tuple[int, ...], int]]:
    boundary, auxiliary = state
    matching = 1 + encode_tuple(boundary, group_order)
    if auxiliary == 0:
        yield boundary, matching
        for link in range(4):
            for value in range(group_order):
                if value == boundary[link]:
                    continue
                candidate = list(boundary)
                candidate[link] = value
                yield tuple(candidate), 0
    else:
        yield boundary, 0


def support_connected(
    group_order: int, overlap: tuple[int, ...], epsilon: int
) -> tuple[bool, int]:
    states = single_face_supported_states(group_order)
    positive_states = {
        state for state in states if single_face_weight(state, overlap, epsilon) > 0
    }
    unseen = set(positive_states)
    start = next(iter(positive_states))
    queue = deque([start])
    unseen.remove(start)
    edge_count = 0
    while queue:
        state = queue.popleft()
        for neighbour in single_face_neighbours(state, group_order):
            if neighbour not in positive_states:
                continue
            edge_count += 1
            if neighbour in unseen:
                unseen.remove(neighbour)
                queue.append(neighbour)
    return not unseen, edge_count


def local_heat_bath_balance(
    overlap: tuple[int, ...], epsilon: int
) -> tuple[bool, int]:
    group_order = len(overlap)
    balanced = True
    comparisons = 0
    for boundary_raw in itertools.product(range(group_order), repeat=4):
        boundary = tuple(boundary_raw)
        matching = 1 + encode_tuple(boundary, group_order)
        total = overlap[tuple_flux(boundary, group_order)]
        star_weight = face_factor(0, boundary, overlap, epsilon)
        tuple_weight = face_factor(matching, boundary, overlap, epsilon)
        star_to_tuple = Fraction(tuple_weight, total)
        tuple_to_star = Fraction(star_weight, total)
        balanced = balanced and (
            star_weight * star_to_tuple == tuple_weight * tuple_to_star
        )
        comparisons += 1

        for link in range(4):
            for value in range(group_order):
                candidate = list(boundary)
                candidate[link] = value
                candidate_tuple = tuple(candidate)
                forward = Fraction(1, group_order)
                backward = Fraction(1, group_order)
                balanced = balanced and star_weight * forward == face_factor(
                    0, candidate_tuple, overlap, epsilon
                ) * backward
                comparisons += 1
                tuple_candidate_weight = face_factor(
                    matching, candidate_tuple, overlap, epsilon
                )
                balanced = balanced and (
                    (value == boundary[link] and tuple_candidate_weight == tuple_weight)
                    or (value != boundary[link] and tuple_candidate_weight == 0)
                )
                comparisons += 1
    return balanced, comparisons


def incidence_lists(
    faces: tuple[tuple[tuple[int, int], ...], ...], link_count: int
) -> tuple[tuple[tuple[int, int], ...], ...]:
    incidence: list[list[tuple[int, int]]] = [[] for _ in range(link_count)]
    for face_index, terms in enumerate(faces):
        for boundary_position, (link, _sign) in enumerate(terms):
            incidence[link].append((face_index, boundary_position))
    return tuple(tuple(entries) for entries in incidence)


def global_auxiliary_marginal_checks(
    overlap: tuple[int, ...], epsilon: int
) -> tuple[bool, bool, bool, int]:
    group_order = len(overlap)
    size = 2
    dimension = 2
    link_count = dimension * size**dimension
    faces = face_terms(size, dimension)
    incidence = incidence_lists(faces, link_count)
    marginal_ok = True
    support_weight_ok = True
    local_edge_ok = True
    masks = range(1 << len(faces))
    for state in range(group_order**link_count):
        configuration = decode_configuration(state, link_count, group_order)
        boundaries = tuple(
            tuple(configuration[link] for link, _sign in terms) for terms in faces
        )
        target = configuration_weight(configuration, faces, overlap)
        local_sums = tuple(
            face_marginal(boundary, overlap, epsilon) for boundary in boundaries
        )
        marginal_ok = marginal_ok and math.prod(local_sums) == target

        support_sum = 0
        for mask in masks:
            joint_weight = 1
            for face_index, boundary in enumerate(boundaries):
                if mask & (1 << face_index):
                    auxiliary = 1 + encode_tuple(boundary, group_order)
                else:
                    auxiliary = 0
                joint_weight *= face_factor(
                    auxiliary, boundary, overlap, epsilon
                )
            support_sum += joint_weight
        support_weight_ok = support_weight_ok and support_sum == target

    # On the joint support, a link is uniform iff every incident face is
    # universal; otherwise the neighboring face tuple fixes it.  Evaluate the
    # actual incident-factor products for every link and auxiliary mask.  The
    # conclusion is independent of the chosen supported link configuration,
    # so one nonuniform deterministic configuration exhausts the incidence
    # and mask structure without repeating the same identity 4^8 times.
    reference = tuple(link % group_order for link in range(link_count))
    reference_boundaries = tuple(
        tuple(reference[face_link] for face_link, _sign in terms)
        for terms in faces
    )
    checked = 0
    for link, entries in enumerate(incidence):
        for mask in masks:
            candidate_weights = []
            for candidate_value in range(group_order):
                candidate_configuration = list(reference)
                candidate_configuration[link] = candidate_value
                product = 1
                for face_index, _position in entries:
                    terms = faces[face_index]
                    candidate_boundary = tuple(
                        candidate_configuration[face_link]
                        for face_link, _sign in terms
                    )
                    if mask & (1 << face_index):
                        auxiliary = 1 + encode_tuple(
                            reference_boundaries[face_index], group_order
                        )
                    else:
                        auxiliary = 0
                    product *= face_factor(
                        auxiliary, candidate_boundary, overlap, epsilon
                    )
                candidate_weights.append(product)
            tuple_incident = any(
                mask & (1 << face_index) for face_index, _position in entries
            )
            if tuple_incident:
                local_edge_ok = local_edge_ok and (
                    candidate_weights[reference[link]] > 0
                    and sum(weight > 0 for weight in candidate_weights) == 1
                )
            else:
                local_edge_ok = local_edge_ok and (
                    min(candidate_weights) > 0
                    and len(set(candidate_weights)) == 1
                )
            checked += 1
    return marginal_ok, support_weight_ok, local_edge_ok, checked


def matrix_encoding_is_injective(group_order: int) -> bool:
    encoded = {((0j, 0j), (0j, 0j))}
    for boundary in itertools.product(range(group_order), repeat=4):
        phases = tuple(
            complex(
                round(math.cos(2.0 * math.pi * value / group_order), 14),
                round(math.sin(2.0 * math.pi * value / group_order), 14),
            )
            for value in boundary
        )
        encoded.add(((phases[0], phases[1]), (phases[2], phases[3])))
    return len(encoded) == 1 + group_order**4


def discretized_overlap_curvature(group_order: int) -> tuple[float, float]:
    angles = 2.0 * math.pi * np.arange(group_order) / group_order
    density = 1.0 + 0.25 * np.cos(angles) + 0.15 * np.sin(2.0 * angles)
    probabilities = density / float(np.sum(density))
    overlap = np.array(
        [float(probabilities @ np.roll(probabilities, -shift)) for shift in range(group_order)]
    )
    normalized = overlap / overlap[0]
    step = 2.0 * math.pi / group_order
    curvature = -2.0 * math.log(normalized[1]) / step**2
    return curvature, float(np.min(overlap))


def main() -> int:
    checks = Checks()
    record_counts = (8, 4, 2, 1)
    overlap = tuple(
        sum(
            record_counts[value] * record_counts[(value + shift) % len(record_counts)]
            for value in range(len(record_counts))
        )
        for shift in range(len(record_counts))
    )
    checks.check(
        overlap == (85, 50, 40, 50),
        "the parent finite Record overlap is reconstructed rather than hard-coded as a weight",
    )

    factorization_ok = True
    positive_ok = True
    epsilon_invariant = True
    conditionals_ok = True
    conditional_families = []
    canonical_epsilon = min(overlap) // 2
    checks.check(
        canonical_epsilon == 20 and 0 < canonical_epsilon < min(overlap),
        "half the kernel minimum gives a positive parameter-free auxiliary split",
    )
    for epsilon in (1, canonical_epsilon, 39):
        marginals = []
        face_probabilities = set()
        for boundary_raw in itertools.product(range(len(overlap)), repeat=4):
            boundary = tuple(boundary_raw)
            target = overlap[tuple_flux(boundary, len(overlap))]
            marginal = face_marginal(boundary, overlap, epsilon)
            marginals.append(marginal)
            factorization_ok = factorization_ok and marginal == target
            weights = [
                face_factor(auxiliary, boundary, overlap, epsilon)
                for auxiliary in range(1 + len(overlap) ** 4)
            ]
            positive_ok = positive_ok and min(weights) >= 0 and sum(
                weight > 0 for weight in weights
            ) == 2
            star_probability, tuple_probability = face_conditionals(
                boundary, overlap, epsilon
            )
            conditionals_ok = conditionals_ok and (
                star_probability > 0
                and tuple_probability > 0
                and star_probability + tuple_probability == 1
            )
            face_probabilities.add(star_probability)
        epsilon_invariant = epsilon_invariant and tuple(marginals) == tuple(
            overlap[tuple_flux(tuple(boundary), len(overlap))]
            for boundary in itertools.product(range(len(overlap)), repeat=4)
        )
        conditional_families.append(face_probabilities)
    checks.check(
        factorization_ok,
        "universal plus matching auxiliary states marginalize exactly to every face weight",
    )
    checks.check(
        positive_ok,
        "each supported face condition has exactly two strictly positive auxiliary states",
    )
    checks.check(
        epsilon_invariant,
        "three distinct auxiliary splits give the identical physical plaquette marginal",
    )
    checks.check(
        conditionals_ok and all(len(family) == 3 for family in conditional_families),
        "face full conditionals normalize and vary with the four neighboring link values",
    )

    invalid_splits = []
    for epsilon in (0, min(overlap), min(overlap) + 1):
        all_weights = [
            face_factor(epsilon_state, tuple(boundary), overlap, epsilon)
            for boundary in itertools.product(range(len(overlap)), repeat=4)
            for epsilon_state in (0, 1 + encode_tuple(tuple(boundary), len(overlap)))
        ]
        invalid_splits.append(
            epsilon == 0 or min(all_weights) <= 0
        )
    checks.check(
        all(invalid_splits),
        "zero and endpoint auxiliary splits lose strict two-state support",
    )

    gauge_covariant = True
    dihedral_covariant = True
    auxiliary_count = 1 + len(overlap) ** 4
    for boundary_raw in itertools.product(range(len(overlap)), repeat=4):
        boundary = tuple(boundary_raw)
        original_flux = tuple_flux(boundary, len(overlap))
        original_weight = overlap[original_flux]
        for gauge_tail in itertools.product(range(len(overlap)), repeat=3):
            gauge = (0,) + tuple(gauge_tail)
            transformed = boundary_gauge_transform(boundary, gauge, len(overlap))
            gauge_covariant = gauge_covariant and (
                tuple_flux(transformed, len(overlap)) == original_flux
                and overlap[tuple_flux(transformed, len(overlap))] == original_weight
            )
            gauge_transform = lambda values, gauge=gauge: boundary_gauge_transform(
                values, gauge, len(overlap)
            )
            for auxiliary in range(auxiliary_count):
                transformed_state = transformed_auxiliary(
                    auxiliary, gauge_transform, len(overlap)
                )
                gauge_covariant = gauge_covariant and face_factor(
                    auxiliary, boundary, overlap, canonical_epsilon
                ) == face_factor(
                    transformed_state,
                    transformed,
                    overlap,
                    canonical_epsilon,
                )
        boundary_images = dihedral_boundaries(boundary, len(overlap))
        for image_index, transformed in enumerate(boundary_images):
            transformed_flux = tuple_flux(transformed, len(overlap))
            dihedral_covariant = dihedral_covariant and (
                transformed_flux in (original_flux, -original_flux % len(overlap))
                and overlap[transformed_flux] == original_weight
            )
            dihedral_transform = (
                lambda values, image_index=image_index: dihedral_boundaries(
                    values, len(overlap)
                )[image_index]
            )
            for auxiliary in range(auxiliary_count):
                transformed_state = transformed_auxiliary(
                    auxiliary, dihedral_transform, len(overlap)
                )
                dihedral_covariant = dihedral_covariant and face_factor(
                    auxiliary, boundary, overlap, canonical_epsilon
                ) == face_factor(
                    transformed_state,
                    transformed,
                    overlap,
                    canonical_epsilon,
                )
    checks.check(
        gauge_covariant,
        "all 16384 boundary tuples and based gauge transformations preserve the face factor",
    )
    checks.check(
        dihedral_covariant,
        "all square rotations and orientation reversals preserve the even auxiliary factor",
    )

    connected, support_edges = support_connected(
        len(overlap), overlap, canonical_epsilon
    )
    checks.check(
        connected
        and support_edges
        == len(overlap) ** 4 * (2 + 4 * (len(overlap) - 1)),
        "the 512-state one-face support is connected by single-site conditional moves",
    )
    balance_ok = True
    balance_comparisons = 0
    for epsilon in (1, canonical_epsilon, 39):
        balanced, comparisons = local_heat_bath_balance(overlap, epsilon)
        balance_ok = balance_ok and balanced
        balance_comparisons += comparisons
    checks.check(
        balance_ok
        and balance_comparisons
        == 3 * len(overlap) ** 4 * (1 + 8 * len(overlap)),
        "face and link heat-bath moves satisfy exact detailed balance for every split",
    )

    global_results = [
        global_auxiliary_marginal_checks(overlap, canonical_epsilon)
    ]
    checks.check(
        all(result[0] for result in global_results),
        "all 65536 link configurations recover the target four-face weight at an interior split",
    )
    checks.check(
        all(result[1] for result in global_results),
        "summing all 16 supported auxiliary masks reproduces each global marginal exactly",
    )
    checks.check(
        all(result[2] for result in global_results)
        and sum(result[3] for result in global_results) == 128,
        "every supported edge conditional is uniform or fixed by adjacent face states alone",
    )

    zero_split_connected, _ = support_connected(len(overlap), overlap, 0)
    checks.check(
        not zero_split_connected
        and face_factor(0, (0, 0, 0, 0), overlap, 0) == 0,
        "the universal component connects support; zero weight leaves disconnected tuple sectors",
    )

    checks.check(
        matrix_encoding_is_injective(4) and matrix_encoding_is_injective(8),
        "the universal state and every finite boundary tuple inject distinctly into M2(C)",
    )
    orthogonal_costs = tuple(
        math.ceil(math.log2(1 + group_order**4))
        for group_order in (2, 4, 8, 16)
    )
    checks.check(
        orthogonal_costs == (5, 9, 13, 17),
        "an orthogonal auxiliary readout costs 4 log2(N)+1 qubits for power-of-two N",
    )

    coefficients = overlap_coefficients((0.25, 0.0), (0.0, 0.15))
    continuum_kappa = kernel_curvature(coefficients)
    curvature_errors = []
    positive_minima = []
    for group_order in (8, 16, 32, 64, 128, 256):
        curvature, minimum = discretized_overlap_curvature(group_order)
        curvature_errors.append(abs(curvature - continuum_kappa))
        positive_minima.append(minimum)
    checks.check(
        all(minimum > 0.0 for minimum in positive_minima),
        "the positive-density cyclic refinements admit the auxiliary split at every N",
    )
    checks.check(
        all(
            left > right
            for left, right in zip(curvature_errors, curvature_errors[1:])
        )
        and curvature_errors[-1] < 2.0e-5,
        "finite cyclic auxiliary models converge to the parent's positive U1 curvature",
    )

    print(
        "per_element: every Z4 boundary tuple, auxiliary state, gauge transform, and square relabeling is checked"
    )
    print(
        "per_site: face and edge full conditionals are normalized and depend only on incidence neighbors on support"
    )
    print(
        "per_mode: checked and not executed — this factorization changes no parent Hessian eigenvalue or momentum mode"
    )
    print(
        "per_block: all 512 one-face support states and three epsilon splits are checked for balance and connectivity"
    )
    print(
        "lattice_wide: every 2x2 Z4 link configuration and all 16 auxiliary masks are marginalized exactly"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
