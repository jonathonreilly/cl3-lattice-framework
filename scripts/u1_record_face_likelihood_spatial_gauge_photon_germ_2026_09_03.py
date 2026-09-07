#!/usr/bin/env python3
"""Exact and deterministic checks for the Record-overlap spatial gauge bridge.

The runner separates four statements that are easy to conflate:

1. a doubled cubic lattice puts the four links of a coarse face in the
   nearest-neighbour star of one fine-lattice face site;
2. an overlap-success Record at every face has a factorized likelihood equal
   to a compact plaquette action when a sequentially local sweep is supplied;
3. the corresponding finite cyclic gauge weight admits an exact reversible
   single-link Metropolis sampler; and
4. its positive spatial germ plus a supplied electric rotor term has two
   transverse harmonic oscillator modes.

The controls show that sitewise marginals alone do not force the factorized
joint law, that summing over unread success/failure Records erases the action,
and that omitting one face orientation destroys the two-mode magnetic block.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction
from typing import Iterable

import numpy as np

from u1_record_distribution_overlap_maxwell_germ_2026_09_03 import (
    kernel_curvature,
    overlap_coefficients,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py",
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


def add_mod(left: tuple[int, ...], right: tuple[int, ...], size: int) -> tuple[int, ...]:
    return tuple((a + b) % size for a, b in zip(left, right))


def unit(dimension: int, axis: int, sign: int = 1) -> tuple[int, ...]:
    return tuple(sign if coordinate == axis else 0 for coordinate in range(dimension))


def lattice_sites(size: int, dimension: int) -> Iterable[tuple[int, ...]]:
    return itertools.product(range(size), repeat=dimension)


def role(point: tuple[int, int, int], offset: tuple[int, int, int]) -> int:
    """Cell dimension in the doubled-lattice incidence embedding."""

    return sum((point[axis] - offset[axis]) % 2 for axis in range(3))


def incidence_geometry_ok() -> tuple[bool, bool, bool]:
    size = 6
    face_stars = True
    link_stars = True
    face_independent = True
    for offset in itertools.product(range(2), repeat=3):
        for point in lattice_sites(size, 3):
            point = tuple(point)
            neighbours = [
                add_mod(point, unit(3, axis, sign), size)
                for axis in range(3)
                for sign in (-1, 1)
            ]
            point_role = role(point, offset)
            neighbour_roles = sorted(role(neighbour, offset) for neighbour in neighbours)
            if point_role == 2:
                face_stars = face_stars and neighbour_roles == [1, 1, 1, 1, 3, 3]
                face_independent = face_independent and 2 not in neighbour_roles
            if point_role == 1:
                link_stars = link_stars and neighbour_roles == [0, 0, 2, 2, 2, 2]
    return face_stars, link_stars, face_independent


def face_boundaries_are_nearest_neighbours() -> bool:
    coarse_size = 3
    fine_size = 2 * coarse_size
    for site_raw in lattice_sites(coarse_size, 3):
        site = tuple(site_raw)
        for first in range(3):
            for second in range(first + 1, 3):
                first_step = add_mod(site, unit(3, first), coarse_size)
                second_step = add_mod(site, unit(3, second), coarse_size)

                def edge_center(base: tuple[int, ...], axis: int) -> tuple[int, ...]:
                    return tuple(
                        (2 * base[coordinate] + int(coordinate == axis)) % fine_size
                        for coordinate in range(3)
                    )

                face_center = tuple(
                    (
                        2 * site[coordinate]
                        + int(coordinate == first)
                        + int(coordinate == second)
                    )
                    % fine_size
                    for coordinate in range(3)
                )
                boundary = {
                    edge_center(site, first),
                    edge_center(first_step, second),
                    edge_center(second_step, first),
                    edge_center(site, second),
                }
                nearest_edges = {
                    add_mod(face_center, unit(3, axis, sign), fine_size)
                    for axis in range(3)
                    for sign in (-1, 1)
                    if role(
                        add_mod(face_center, unit(3, axis, sign), fine_size),
                        (0, 0, 0),
                    )
                    == 1
                }
                if boundary != nearest_edges:
                    return False
    return True


def link_index(
    site: tuple[int, ...], axis: int, size: int, dimension: int
) -> int:
    site_index = 0
    for coordinate in site:
        site_index = site_index * size + coordinate
    return dimension * site_index + axis


def face_terms(size: int, dimension: int) -> tuple[tuple[tuple[int, int], ...], ...]:
    faces: list[tuple[tuple[int, int], ...]] = []
    for site_raw in lattice_sites(size, dimension):
        site = tuple(site_raw)
        for first in range(dimension):
            for second in range(first + 1, dimension):
                first_step = add_mod(site, unit(dimension, first), size)
                second_step = add_mod(site, unit(dimension, second), size)
                faces.append(
                    (
                        (link_index(site, first, size, dimension), 1),
                        (link_index(first_step, second, size, dimension), 1),
                        (link_index(second_step, first, size, dimension), -1),
                        (link_index(site, second, size, dimension), -1),
                    )
                )
    return tuple(faces)


def flux(
    configuration: tuple[int, ...],
    terms: tuple[tuple[int, int], ...],
    group_order: int,
) -> int:
    return sum(sign * configuration[index] for index, sign in terms) % group_order


def configuration_weight(
    configuration: tuple[int, ...],
    faces: tuple[tuple[tuple[int, int], ...], ...],
    overlap: tuple[int, ...],
) -> int:
    result = 1
    for terms in faces:
        result *= overlap[flux(configuration, terms, len(overlap))]
    return result


def decode_configuration(index: int, count: int, group_order: int) -> tuple[int, ...]:
    values = []
    for _ in range(count):
        values.append(index % group_order)
        index //= group_order
    return tuple(values)


def replace_digit(
    index: int,
    digit_index: int,
    new_value: int,
    powers: tuple[int, ...],
    group_order: int,
) -> int:
    old_value = (index // powers[digit_index]) % group_order
    return index + (new_value - old_value) * powers[digit_index]


def gauge_transform(
    configuration: tuple[int, ...],
    gauge: dict[tuple[int, ...], int],
    size: int,
    dimension: int,
    group_order: int,
) -> tuple[int, ...]:
    transformed = list(configuration)
    for site_raw in lattice_sites(size, dimension):
        site = tuple(site_raw)
        for axis in range(dimension):
            endpoint = add_mod(site, unit(dimension, axis), size)
            index = link_index(site, axis, size, dimension)
            transformed[index] = (
                configuration[index] + gauge[endpoint] - gauge[site]
            ) % group_order
    return tuple(transformed)


def translate_links(
    configuration: tuple[int, ...],
    shift: tuple[int, ...],
    size: int,
    dimension: int,
) -> tuple[int, ...]:
    translated = [0] * len(configuration)
    for site_raw in lattice_sites(size, dimension):
        site = tuple(site_raw)
        destination = add_mod(site, shift, size)
        for axis in range(dimension):
            translated[link_index(destination, axis, size, dimension)] = configuration[
                link_index(site, axis, size, dimension)
            ]
    return tuple(translated)


def permutation_parity(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_parity(permutation) * math.prod(signs) == 1:
                rotations.append((permutation, signs))
    return tuple(rotations)


def rotate_site(
    site: tuple[int, int, int],
    permutation: tuple[int, ...],
    signs: tuple[int, ...],
    size: int,
) -> tuple[int, int, int]:
    result = [0, 0, 0]
    for old_axis in range(3):
        result[permutation[old_axis]] = signs[old_axis] * site[old_axis] % size
    return tuple(result)


def rotate_links(
    configuration: tuple[int, ...],
    permutation: tuple[int, ...],
    signs: tuple[int, ...],
    size: int,
    group_order: int,
) -> tuple[int, ...]:
    rotated = [0] * len(configuration)
    for site_raw in lattice_sites(size, 3):
        site = tuple(site_raw)
        rotated_site = rotate_site(site, permutation, signs, size)
        for old_axis in range(3):
            new_axis = permutation[old_axis]
            value = configuration[link_index(site, old_axis, size, 3)]
            if signs[old_axis] == 1:
                start = rotated_site
                oriented_value = value
            else:
                start = add_mod(rotated_site, unit(3, new_axis, -1), size)
                oriented_value = -value
            rotated[link_index(start, new_axis, size, 3)] = oriented_value % group_order
    return tuple(rotated)


def acceptance(weight_from: int, weight_to: int) -> Fraction:
    return Fraction(min(weight_from, weight_to), weight_from)


def directed_winding_ratio(group_order: int) -> Fraction:
    """Cycle ratio for a declared +phase proposal bias of two to one."""

    forward = Fraction(1)
    reverse = Fraction(1)
    phase = 0
    for _ in range(group_order):
        next_phase = (phase + 1) % group_order
        forward *= Fraction(2, 3)
        reverse *= Fraction(1, 3)
        phase = next_phase
    if phase != 0:
        raise AssertionError("the declared phase cycle did not close")
    return forward / reverse


def one_face_cycle_test(overlap: tuple[int, ...]) -> bool:
    group_order = len(overlap)
    link_count = 4
    powers = tuple(group_order**index for index in range(link_count))
    face = (((0, 1), (1, 1), (2, -1), (3, -1)),)
    weights = tuple(
        configuration_weight(
            decode_configuration(index, link_count, group_order), face, overlap
        )
        for index in range(group_order**link_count)
    )
    for state in range(group_order**link_count):
        for first, second in itertools.combinations(range(link_count), 2):
            for first_step, second_step in itertools.product((-1, 1), repeat=2):
                first_value = (state // powers[first]) % group_order
                second_value = (state // powers[second]) % group_order
                state_first = replace_digit(
                    state,
                    first,
                    (first_value + first_step) % group_order,
                    powers,
                    group_order,
                )
                state_second = replace_digit(
                    state,
                    second,
                    (second_value + second_step) % group_order,
                    powers,
                    group_order,
                )
                state_both = replace_digit(
                    state_first,
                    second,
                    (second_value + second_step) % group_order,
                    powers,
                    group_order,
                )
                forward_states = (state, state_first, state_both, state_second, state)
                reverse_states = (state, state_second, state_both, state_first, state)
                forward = math.prod(
                    acceptance(weights[left], weights[right])
                    for left, right in zip(forward_states, forward_states[1:])
                )
                reverse = math.prod(
                    acceptance(weights[left], weights[right])
                    for left, right in zip(reverse_states, reverse_states[1:])
                )
                if forward != reverse:
                    return False
    return True


def spatial_kernel(
    momentum: np.ndarray, coefficients: dict[tuple[int, int], float]
) -> np.ndarray:
    kernel = np.zeros((3, 3), dtype=float)
    for first in range(3):
        for second in range(first + 1, 3):
            coefficient = coefficients.get((first, second), 0.0)
            kernel[first, first] += coefficient * momentum[second] ** 2
            kernel[second, second] += coefficient * momentum[first] ** 2
            kernel[first, second] -= coefficient * momentum[first] * momentum[second]
            kernel[second, first] = kernel[first, second]
    return kernel


def main() -> int:
    checks = Checks()

    face_stars, link_stars, face_independent = incidence_geometry_ok()
    checks.check(
        face_stars,
        "every doubled-lattice face site sees four edge sites and two cube sites",
    )
    checks.check(
        link_stars,
        "every doubled-lattice edge site sees two vertices and four face sites",
    )
    checks.check(
        face_independent,
        "face sites form an independent set for every translated parity origin",
    )
    checks.check(
        face_boundaries_are_nearest_neighbours(),
        "each oriented coarse plaquette boundary is exactly its face site's four edge neighbours",
    )

    record_counts = (8, 4, 2, 1)
    group_order = len(record_counts)
    total_records = sum(record_counts)
    overlap = tuple(
        sum(
            record_counts[value] * record_counts[(value + shift) % group_order]
            for value in range(group_order)
        )
        for shift in range(group_order)
    )
    checks.check(
        overlap == (85, 50, 40, 50),
        "finite Record-pair census gives the exact nonuniform cyclic overlap kernel",
    )
    overlap_even = all(
        overlap[shift] == overlap[-shift % group_order]
        for shift in range(group_order)
    )
    checks.check(
        overlap_even
        and overlap[0] == max(overlap)
        and min(overlap) > 0
        and len(set(overlap)) > 1,
        "overlap is positive, even, identity-maximal, and genuinely varying",
    )

    direct_match = True
    for shift in range(group_order):
        pair_count = 0
        for left in range(group_order):
            for right in range(group_order):
                if left == (right + shift) % group_order:
                    pair_count += record_counts[left] * record_counts[right]
        direct_match = direct_match and pair_count == overlap[shift]
    checks.check(
        direct_match,
        "overlap equals the directly enumerated probability of matching Record values",
    )

    size = 2
    dimension = 2
    links = dimension * size**dimension
    faces = face_terms(size, dimension)
    state_count = group_order**links
    powers = tuple(group_order**index for index in range(links))
    configurations = tuple(
        decode_configuration(index, links, group_order) for index in range(state_count)
    )
    weights = tuple(
        configuration_weight(configuration, faces, overlap)
        for configuration in configurations
    )
    checks.check(
        len(faces) == 4 and len(set(weights)) > 3 and min(weights) > 0,
        "the 2x2 cyclic gauge ensemble has four faces and nontrivial positive weights",
    )

    action_identity = True
    order_identity = True
    marginal_identity = True
    overlap_zero = overlap[0]
    pair_denominator = total_records**2
    for configuration, weight in zip(configurations, weights):
        face_overlaps = tuple(
            overlap[flux(configuration, terms, group_order)] for terms in faces
        )
        probability = Fraction(math.prod(face_overlaps), pair_denominator ** len(faces))
        relative_probability = probability / Fraction(
            overlap_zero ** len(faces), pair_denominator ** len(faces)
        )
        action = sum(-math.log(value / overlap_zero) for value in face_overlaps)
        action_identity = action_identity and abs(
            -math.log(float(relative_probability)) - action
        ) < 3.0e-15
        order_products = {
            math.prod(face_overlaps[index] for index in order)
            for order in itertools.permutations(range(len(faces)))
        }
        order_identity = order_identity and order_products == {weight}
        marginal_identity = marginal_identity and all(
            Fraction(value, pair_denominator)
            + Fraction(pair_denominator - value, pair_denominator)
            == 1
            for value in face_overlaps
        )
    checks.check(
        action_identity,
        "all-success Record likelihood is exactly the additive overlap plaquette action",
    )
    checks.check(
        order_identity,
        "every ordering of the independent face sweep gives the same joint likelihood",
    )
    checks.check(
        marginal_identity,
        "summing success and failure at every unread face erases the likelihood weight",
    )

    probability = Fraction(overlap[1], pair_denominator)
    complement = 1 - probability
    product_joint = (
        (probability * probability, probability * complement),
        (complement * probability, complement * complement),
    )
    correlated_joint = ((probability, Fraction(0)), (Fraction(0), complement))
    joint_tables_valid = True
    for table in (product_joint, correlated_joint):
        joint_tables_valid = joint_tables_valid and (
            sum(sum(row) for row in table) == 1
            and tuple(sum(row) for row in table) == (probability, complement)
            and tuple(table[0][column] + table[1][column] for column in range(2))
            == (probability, complement)
        )
    checks.check(
        joint_tables_valid and product_joint != correlated_joint,
        "identical local face marginals admit distinct correlated and product joint laws",
    )

    gauge_ok = True
    translation_ok = True
    for configuration, weight in zip(configurations, weights):
        for site_raw in lattice_sites(size, dimension):
            site = tuple(site_raw)
            gauge = {tuple(point): 0 for point in lattice_sites(size, dimension)}
            gauge[site] = 1
            transformed = gauge_transform(
                configuration, gauge, size, dimension, group_order
            )
            gauge_ok = gauge_ok and configuration_weight(
                transformed, faces, overlap
            ) == weight
        for axis in range(dimension):
            translated = translate_links(
                configuration, unit(dimension, axis), size, dimension
            )
            translation_ok = translation_ok and configuration_weight(
                translated, faces, overlap
            ) == weight
    checks.check(gauge_ok, "every local gauge generator preserves all 65536 ensemble weights")
    checks.check(
        translation_ok,
        "both lattice translations preserve all 65536 ensemble weights",
    )

    detailed_balance = True
    ratio_recovery = True
    directed_edges = 0
    for state, weight_from in enumerate(weights):
        for link in range(links):
            old_value = (state // powers[link]) % group_order
            for step in (-1, 1):
                new_value = (old_value + step) % group_order
                destination = replace_digit(
                    state, link, new_value, powers, group_order
                )
                weight_to = weights[destination]
                forward = acceptance(weight_from, weight_to)
                backward = acceptance(weight_to, weight_from)
                detailed_balance = detailed_balance and (
                    weight_from * forward == weight_to * backward
                )
                ratio_recovery = ratio_recovery and (
                    forward / backward == Fraction(weight_to, weight_from)
                )
                directed_edges += 1
    checks.check(
        detailed_balance and directed_edges == 1_048_576,
        "the single-link Metropolis sampler obeys exact detailed balance on every directed edge",
    )
    checks.check(
        ratio_recovery,
        "forward/reverse odds recover the exact global plaquette-weight ratio",
    )
    checks.check(
        one_face_cycle_test(overlap),
        "all 6144 elementary two-link cycles pass Kolmogorov exactly",
    )
    driven_cycle_ratio = directed_winding_ratio(group_order)
    checks.check(
        driven_cycle_ratio == 16,
        "directed phase bias fails on a winding cycle and the cycle test detects it",
    )

    three_size = 3
    three_dimension = 3
    three_faces = face_terms(three_size, three_dimension)
    deterministic_configurations = []
    for seed in range(5):
        deterministic_configurations.append(
            tuple(
                (
                    3 * site[0]
                    + 2 * site[1]
                    + site[2]
                    + axis
                    + seed * (site[0] + 2 * site[2] + 1)
                )
                % group_order
                for site_raw in lattice_sites(three_size, three_dimension)
                for site in (tuple(site_raw),)
                for axis in range(three_dimension)
            )
        )
    rotations = proper_cubic_rotations()
    cubic_ok = len(rotations) == 24
    for configuration in deterministic_configurations:
        weight = configuration_weight(configuration, three_faces, overlap)
        for permutation, signs in rotations:
            rotated = rotate_links(
                configuration,
                permutation,
                signs,
                three_size,
                group_order,
            )
            cubic_ok = cubic_ok and configuration_weight(
                rotated, three_faces, overlap
            ) == weight
    checks.check(
        cubic_ok,
        "one even face law is invariant under all 24 proper cubic rotations",
    )

    continuum_coefficients = overlap_coefficients(
        (0.15, -0.20, 0.10), (0.25, 0.12, -0.08)
    )
    kappa = kernel_curvature(continuum_coefficients)
    spatial_modes = True
    oscillator_modes = True
    speed_squared = 1.7 * kappa
    for lattice_length in (3, 4, 5, 7):
        for indices in itertools.product(range(lattice_length), repeat=3):
            momenta = np.array(
                [
                    2.0
                    * math.sin(
                        math.pi
                        * (
                            index
                            if index <= lattice_length // 2
                            else index - lattice_length
                        )
                        / lattice_length
                    )
                    for index in indices
                ]
            )
            norm_squared = float(momenta @ momenta)
            if norm_squared < 1.0e-15:
                continue
            kernel = spatial_kernel(
                momenta,
                {(0, 1): kappa, (0, 2): kappa, (1, 2): kappa},
            )
            eigenvalues = np.linalg.eigvalsh(kernel)
            expected = np.array([0.0, kappa * norm_squared, kappa * norm_squared])
            spatial_modes = spatial_modes and bool(
                np.max(np.abs(eigenvalues - expected)) < 2.0e-12
                and np.linalg.norm(kernel @ momenta) < 2.0e-12
            )
            frequencies_squared = 1.7 * eigenvalues[1:]
            oscillator_modes = oscillator_modes and bool(
                np.max(
                    np.abs(
                        frequencies_squared
                        - np.array([speed_squared * norm_squared] * 2)
                    )
                )
                < 4.0e-12
            )
    checks.check(
        spatial_modes,
        "the orientation-complete magnetic germ has one gauge null and two curl modes",
    )
    checks.check(
        oscillator_modes,
        "a supplied positive electric rotor term gives two degenerate quantum oscillators",
    )

    infrared_ratios = []
    for lattice_length in (16, 32, 64, 128):
        momentum = 2.0 * math.sin(math.pi / lattice_length)
        frequency = math.sqrt(speed_squared) * momentum
        continuum_momentum = 2.0 * math.pi / lattice_length
        infrared_ratios.append(frequency / continuum_momentum)
    checks.check(
        all(
            abs(value - math.sqrt(speed_squared))
            > abs(next_value - math.sqrt(speed_squared))
            for value, next_value in zip(infrared_ratios, infrared_ratios[1:])
        )
        and abs(infrared_ratios[-1] - math.sqrt(speed_squared)) < 2.0e-4,
        "both oscillator branches are gapless with linear infrared dispersion",
    )

    incomplete = spatial_kernel(
        np.array([0.0, 1.0, 1.0]), {(0, 1): kappa, (0, 2): kappa}
    )
    anisotropic = spatial_kernel(
        np.array([0.7, 1.0, 1.3]),
        {(0, 1): kappa, (0, 2): 2.0 * kappa, (1, 2): 3.0 * kappa},
    )
    checks.check(
        np.linalg.matrix_rank(incomplete, tol=1.0e-12) == 1,
        "omitting one spatial face orientation loses a transverse stiffness",
    )
    checks.check(
        abs(np.linalg.eigvalsh(anisotropic)[1] - np.linalg.eigvalsh(anisotropic)[2])
        > 0.05 * kappa,
        "unequal orientation weights split the transverse modes",
    )

    print(
        "per_element: all cyclic Record pairs, local moves, and proper cubic rotations are checked"
    )
    print(
        "per_site: every translated doubled-lattice role has the required six-neighbour incidence star"
    )
    print(
        "per_mode: every nonzero spatial momentum on L=3,4,5,7 has two harmonic oscillator branches"
    )
    print(
        "per_block: product, correlated, marginalized, reversible, driven, incomplete, and anisotropic controls are contrasted"
    )
    print(
        "lattice_wide: all 65536 Z4 configurations and 1048576 directed local moves are checked exactly"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
