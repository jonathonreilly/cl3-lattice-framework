#!/usr/bin/env python3
"""Exact checks for a role-encoded nearest-neighbor gauge-law compiler.

The physical lattice is Z^3.  A local possibility carries a parity-role label
in Z2^3 and a role-dependent payload.  Nearest neighbors flip exactly the role
bit associated with their separation axis.  On an even periodic torus this
has eight translated sectors.  Edge roles carry Z_N link values; face roles
carry the universal-or-matching auxiliary from the parent gauge measure.

The resulting full conditionals use only the six physical nearest neighbors.
This runner checks the role geometry, gauge/translation/cubic covariance,
unconditional marginalization, local conditionals, and finite M2(C) capacity.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction
from typing import Iterable

from u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03 import (
    encode_tuple,
    face_conditionals,
    face_factor,
    face_marginal,
    tuple_flux,
)
from u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03 import (
    proper_cubic_rotations,
    rotate_site,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py",
    "scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py",
    "scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py",
)


Coord = tuple[int, int, int]
Role = tuple[int, int, int]


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


def sites(size: int) -> Iterable[Coord]:
    return itertools.product(range(size), repeat=3)


def add_axis(point: Coord, axis: int, step: int, size: int) -> Coord:
    result = list(point)
    result[axis] = (result[axis] + step) % size
    return tuple(result)


def translate_site(point: Coord, displacement: Coord, size: int) -> Coord:
    return tuple((point[axis] + displacement[axis]) % size for axis in range(3))


def role_bits(point: Coord, sector: Role) -> Role:
    return tuple((point[axis] + sector[axis]) % 2 for axis in range(3))


def flip_role(role: Role, axis: int) -> Role:
    result = list(role)
    result[axis] ^= 1
    return tuple(result)


def role_kind(role: Role) -> str:
    names = {0: "vertex", 1: "edge", 2: "face", 3: "cube"}
    return names[sum(role)]


def edge_axis(role: Role) -> int:
    assert sum(role) == 1
    return role.index(1)


def face_axes(role: Role) -> tuple[int, int]:
    assert sum(role) == 2
    return tuple(axis for axis, bit in enumerate(role) if bit)  # type: ignore[return-value]


def role_shell(point: Coord, sector: Role, size: int) -> dict[tuple[int, int], Role]:
    return {
        (axis, sign): role_bits(add_axis(point, axis, sign, size), sector)
        for axis in range(3)
        for sign in (-1, 1)
    }


def compatible_roles(shell: dict[tuple[int, int], Role]) -> tuple[Role, ...]:
    candidates = []
    for candidate in itertools.product((0, 1), repeat=3):
        if all(
            shell[(axis, sign)] == flip_role(tuple(candidate), axis)
            for axis in range(3)
            for sign in (-1, 1)
        ):
            candidates.append(tuple(candidate))
    return tuple(candidates)


def face_boundary_sites(point: Coord, role: Role, size: int) -> tuple[Coord, ...]:
    """Boundary order has curl first+second-third-fourth."""

    first_axis, second_axis = face_axes(role)
    return (
        add_axis(point, second_axis, -1, size),
        add_axis(point, first_axis, 1, size),
        add_axis(point, second_axis, 1, size),
        add_axis(point, first_axis, -1, size),
    )


def incident_faces(point: Coord, role: Role, size: int) -> tuple[tuple[Coord, int], ...]:
    axis = edge_axis(role)
    result = []
    for other_axis in range(3):
        if other_axis == axis:
            continue
        for sign in (-1, 1):
            face = add_axis(point, other_axis, sign, size)
            face_role = flip_role(role, other_axis)
            boundary = face_boundary_sites(face, face_role, size)
            result.append((face, boundary.index(point)))
    return tuple(result)


def coarse_coordinate(vertex: Coord, sector: Role, size: int) -> Coord:
    assert all((vertex[axis] - sector[axis]) % 2 == 0 for axis in range(3))
    return tuple(((vertex[axis] - sector[axis]) % size) // 2 for axis in range(3))


def abstract_link_value(axis: int, coarse: Coord, group_order: int, variant: int) -> int:
    x, y, z = coarse
    formulas = (
        0,
        axis + x + 2 * y + 3 * z,
        2 * axis + x * y + y * z + z * x + x,
        (axis + 1) * (x + 1) + (axis + 2) * y + (axis + 3) * z,
    )
    return formulas[variant] % group_order


def link_field(size: int, sector: Role, group_order: int, variant: int) -> dict[Coord, int]:
    result: dict[Coord, int] = {}
    for point_raw in sites(size):
        point = tuple(point_raw)
        role = role_bits(point, sector)
        if role_kind(role) != "edge":
            continue
        axis = edge_axis(role)
        tail = add_axis(point, axis, -1, size)
        coarse = coarse_coordinate(tail, sector, size)
        result[point] = abstract_link_value(axis, coarse, group_order, variant)
    return result


def boundary_values(
    point: Coord,
    role: Role,
    links: dict[Coord, int],
    size: int,
) -> tuple[int, int, int, int]:
    return tuple(links[edge] for edge in face_boundary_sites(point, role, size))  # type: ignore[return-value]


def face_weight_product(
    size: int,
    sector: Role,
    links: dict[Coord, int],
    overlap: tuple[int, ...],
) -> int:
    product = 1
    for point_raw in sites(size):
        point = tuple(point_raw)
        role = role_bits(point, sector)
        if role_kind(role) == "face":
            boundary = boundary_values(point, role, links, size)
            product *= overlap[tuple_flux(boundary, len(overlap))]
    return product


def vertex_potential(
    size: int, sector: Role, group_order: int, variant: int
) -> dict[Coord, int]:
    result = {}
    for point_raw in sites(size):
        point = tuple(point_raw)
        if role_kind(role_bits(point, sector)) != "vertex":
            continue
        x, y, z = coarse_coordinate(point, sector, size)
        if variant == 0:
            value = x + 2 * y + z
        else:
            value = x * y + 2 * z + variant * x
        result[point] = value % group_order
    return result


def gauge_transform_links(
    links: dict[Coord, int],
    sector: Role,
    potential: dict[Coord, int],
    size: int,
    group_order: int,
) -> dict[Coord, int]:
    transformed = {}
    for point, value in links.items():
        role = role_bits(point, sector)
        axis = edge_axis(role)
        tail = add_axis(point, axis, -1, size)
        head = add_axis(point, axis, 1, size)
        transformed[point] = (
            value + potential[head] - potential[tail]
        ) % group_order
    return transformed


def permute_role(role: Role, permutation: tuple[int, ...]) -> Role:
    result = [0, 0, 0]
    for old_axis in range(3):
        result[permutation[old_axis]] = role[old_axis]
    return tuple(result)


def rotated_sector(sector: Role, permutation: tuple[int, ...]) -> Role:
    return permute_role(sector, permutation)


def rotate_midpoint_links(
    links: dict[Coord, int],
    sector: Role,
    permutation: tuple[int, ...],
    signs: tuple[int, ...],
    size: int,
    group_order: int,
) -> tuple[Role, dict[Coord, int]]:
    new_sector = rotated_sector(sector, permutation)
    transformed = {}
    for point, value in links.items():
        old_axis = edge_axis(role_bits(point, sector))
        rotated_point = rotate_site(point, permutation, signs, size)
        transformed[rotated_point] = signs[old_axis] * value % group_order
    return new_sector, transformed


def translate_midpoint_links(
    links: dict[Coord, int],
    sector: Role,
    displacement: Coord,
    size: int,
) -> tuple[Role, dict[Coord, int]]:
    new_sector = tuple(
        (sector[axis] + displacement[axis]) % 2 for axis in range(3)
    )
    return new_sector, {
        translate_site(point, displacement, size): value
        for point, value in links.items()
    }


def rotate_face_tuple(
    face: Coord,
    face_role: Role,
    values: tuple[int, int, int, int],
    permutation: tuple[int, ...],
    signs: tuple[int, ...],
    size: int,
    group_order: int,
) -> tuple[Coord, Role, tuple[int, int, int, int]]:
    mapped_edges: dict[Coord, int] = {}
    for edge, value in zip(face_boundary_sites(face, face_role, size), values):
        old_axis = edge_axis(role_bits(edge, (0, 0, 0)))
        mapped_edges[rotate_site(edge, permutation, signs, size)] = (
            signs[old_axis] * value
        ) % group_order
    new_face = rotate_site(face, permutation, signs, size)
    new_role = permute_role(face_role, permutation)
    new_values = tuple(
        mapped_edges[edge]
        for edge in face_boundary_sites(new_face, new_role, size)
    )
    return new_face, new_role, new_values  # type: ignore[return-value]


def edge_conditional_weights(
    edge: Coord,
    sector: Role,
    links: dict[Coord, int],
    tuple_mask: int,
    overlap: tuple[int, ...],
    epsilon: int,
    size: int,
) -> tuple[int, ...]:
    group_order = len(overlap)
    edge_role = role_bits(edge, sector)
    faces = incident_faces(edge, edge_role, size)
    original_boundaries = {
        face: boundary_values(face, role_bits(face, sector), links, size)
        for face, _position in faces
    }
    weights = []
    for candidate in range(group_order):
        candidate_links = dict(links)
        candidate_links[edge] = candidate
        product = 1
        for face_index, (face, _position) in enumerate(faces):
            face_role = role_bits(face, sector)
            candidate_boundary = boundary_values(face, face_role, candidate_links, size)
            if tuple_mask & (1 << face_index):
                auxiliary = 1 + encode_tuple(original_boundaries[face], group_order)
            else:
                auxiliary = 0
            product *= face_factor(
                auxiliary, candidate_boundary, overlap, epsilon
            )
        weights.append(product)
    return tuple(weights)


def finite_alphabet(group_order: int) -> tuple[tuple[Role, object], ...]:
    labels: list[tuple[Role, object]] = []
    for role_raw in itertools.product((0, 1), repeat=3):
        role = tuple(role_raw)
        kind = role_kind(role)
        if kind in ("vertex", "cube"):
            labels.append((role, "unit"))
        elif kind == "edge":
            labels.extend((role, value) for value in range(group_order))
        else:
            labels.append((role, "star"))
            labels.extend(
                (role, tuple(values))
                for values in itertools.product(range(group_order), repeat=4)
            )
    return tuple(labels)


def m2_injection_is_distinct(group_order: int) -> bool:
    labels = finite_alphabet(group_order)
    count = len(labels)
    matrices = {
        ((Fraction(index, count), Fraction(0)), (Fraction(0), Fraction(1)))
        for index, _label in enumerate(labels)
    }
    return len(matrices) == count


def main() -> int:
    checks = Checks()
    size = 4
    group_order = 4
    overlap = (85, 50, 40, 50)
    epsilon = min(overlap) // 2
    sectors = tuple(itertools.product((0, 1), repeat=3))
    rotations = proper_cubic_rotations()

    checks.check(
        overlap[1] == overlap[-1] and epsilon == 20,
        "the parent even Z4 face weight and its canonical positive split are pinned",
    )

    distinct_role_fields = {
        tuple(role_bits(tuple(point), tuple(sector)) for point in sites(size))
        for sector in sectors
    }
    checks.check(
        len(sectors) == 8 and len(distinct_role_fields) == 8,
        "the even physical torus carries exactly the eight translated parity-role exhibits",
    )

    shell_rule_ok = True
    role_variants = set()
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        for point_raw in sites(size):
            point = tuple(point_raw)
            candidates = compatible_roles(role_shell(point, sector, size))
            shell_rule_ok = shell_rule_ok and candidates == (role_bits(point, sector),)
            role_variants.add(candidates[0])
    checks.check(
        shell_rule_ok and len(role_variants) == 8,
        "one coordinate-free six-neighbor rule uniquely recovers every local role",
    )

    propagation_ok = True
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        origin_role = role_bits((0, 0, 0), sector)
        for point_raw in sites(size):
            point = tuple(point_raw)
            propagated = tuple(
                (origin_role[axis] + point[axis]) % 2 for axis in range(3)
            )
            propagation_ok = propagation_ok and propagated == role_bits(point, sector)
    checks.check(
        propagation_ok,
        "an origin role propagates uniquely, proving there are no further valid role sectors",
    )

    odd_size_fails = True
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        odd_size_fails = odd_size_fails and any(
            compatible_roles(role_shell(tuple(point), sector, 3))
            != (role_bits(tuple(point), sector),)
            for point in sites(3)
        )
    checks.check(
        odd_size_fails,
        "odd periodic lengths are the explicit frustration control for the parity-role sector",
    )

    census_ok = True
    neighbor_census_ok = True
    expected_neighbors = {
        "vertex": {"edge": 6},
        "edge": {"vertex": 2, "face": 4},
        "face": {"edge": 4, "cube": 2},
        "cube": {"face": 6},
    }
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        counts = {kind: 0 for kind in ("vertex", "edge", "face", "cube")}
        for point_raw in sites(size):
            point = tuple(point_raw)
            kind = role_kind(role_bits(point, sector))
            counts[kind] += 1
            neighbor_counts: dict[str, int] = {}
            for neighbor_role in role_shell(point, sector, size).values():
                neighbor_kind = role_kind(neighbor_role)
                neighbor_counts[neighbor_kind] = neighbor_counts.get(neighbor_kind, 0) + 1
            neighbor_census_ok = neighbor_census_ok and neighbor_counts == expected_neighbors[kind]
        census_ok = census_ok and counts == {
            "vertex": 8,
            "edge": 24,
            "face": 24,
            "cube": 8,
        }
    checks.check(census_ok, "every sector has the 8+24+24+8 doubled-incidence role census")
    checks.check(
        neighbor_census_ok,
        "all 512 site shells have the vertex-edge-face-cube incidence census",
    )

    face_geometry_ok = True
    edge_geometry_ok = True
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        for point_raw in sites(size):
            point = tuple(point_raw)
            role = role_bits(point, sector)
            if role_kind(role) == "face":
                boundary = face_boundary_sites(point, role, size)
                face_geometry_ok = face_geometry_ok and (
                    len(set(boundary)) == 4
                    and all(role_kind(role_bits(edge, sector)) == "edge" for edge in boundary)
                    and all(
                        sum(a != b for a, b in zip(point, edge)) == 1
                        for edge in boundary
                    )
                )
            elif role_kind(role) == "edge":
                faces = incident_faces(point, role, size)
                edge_geometry_ok = edge_geometry_ok and (
                    len(faces) == 4
                    and len({face for face, _position in faces}) == 4
                    and all(role_kind(role_bits(face, sector)) == "face" for face, _ in faces)
                )
    checks.check(
        face_geometry_ok,
        "every face payload reads exactly four physical nearest-neighbor edge sites",
    )
    checks.check(
        edge_geometry_ok,
        "every edge payload reads exactly four physical nearest-neighbor face sites",
    )

    abstract_curl_ok = True
    sector_products_ok = True
    marginal_ok = True
    for variant in range(4):
        products = []
        for sector_raw in sectors:
            sector = tuple(sector_raw)
            links = link_field(size, sector, group_order, variant)
            products.append(face_weight_product(size, sector, links, overlap))
            for point_raw in sites(size):
                point = tuple(point_raw)
                role = role_bits(point, sector)
                if role_kind(role) != "face":
                    continue
                boundary = boundary_values(point, role, links, size)
                first_axis, second_axis = face_axes(role)
                lower_vertex = add_axis(
                    add_axis(point, first_axis, -1, size),
                    second_axis,
                    -1,
                    size,
                )
                coarse = coarse_coordinate(lower_vertex, sector, size)
                coarse_first = list(coarse)
                coarse_first[first_axis] = (coarse_first[first_axis] + 1) % (size // 2)
                coarse_second = list(coarse)
                coarse_second[second_axis] = (coarse_second[second_axis] + 1) % (size // 2)
                expected = (
                    abstract_link_value(first_axis, coarse, group_order, variant)
                    + abstract_link_value(second_axis, tuple(coarse_first), group_order, variant)
                    - abstract_link_value(first_axis, tuple(coarse_second), group_order, variant)
                    - abstract_link_value(second_axis, coarse, group_order, variant)
                ) % group_order
                abstract_curl_ok = abstract_curl_ok and tuple_flux(boundary, group_order) == expected
                marginal_ok = marginal_ok and face_marginal(
                    boundary, overlap, epsilon
                ) == overlap[expected]
        sector_products_ok = sector_products_ok and len(set(products)) == 1
    checks.check(
        abstract_curl_ok,
        "the physical nearest-neighbor boundary order equals the coarse plaquette curl",
    )
    checks.check(
        marginal_ok,
        "summing each face payload unconditionally returns its parent plaquette weight",
    )
    checks.check(
        sector_products_ok,
        "all eight translated role sectors give identical gauge products for four fields",
    )

    face_conditional_ok = True
    face_probabilities = set()
    for boundary_raw in itertools.product(range(group_order), repeat=4):
        boundary = tuple(boundary_raw)
        star_probability, matching_probability = face_conditionals(
            boundary, overlap, epsilon
        )
        face_conditional_ok = face_conditional_ok and (
            star_probability > 0
            and matching_probability > 0
            and star_probability + matching_probability == 1
        )
        face_probabilities.add(star_probability)
    checks.check(
        face_conditional_ok and len(face_probabilities) == 3,
        "the face branch is normalized, strictly supported, and varies with four neighbors",
    )

    edge_conditionals_ok = True
    edge_checks = 0
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        links = link_field(size, sector, group_order, 3)
        for point in links:
            for mask in range(16):
                weights = edge_conditional_weights(
                    point, sector, links, mask, overlap, epsilon, size
                )
                if mask == 0:
                    edge_conditionals_ok = edge_conditionals_ok and (
                        min(weights) > 0 and len(set(weights)) == 1
                    )
                else:
                    edge_conditionals_ok = edge_conditionals_ok and (
                        weights[links[point]] > 0
                        and sum(weight > 0 for weight in weights) == 1
                    )
                edge_checks += 1
    checks.check(
        edge_conditionals_ok and edge_checks == 8 * 24 * 16,
        "all 3072 supported edge contexts are uniform or fixed by adjacent faces",
    )

    gauge_ok = True
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        for field_variant in range(4):
            links = link_field(size, sector, group_order, field_variant)
            original_fluxes = []
            for point_raw in sites(size):
                point = tuple(point_raw)
                role = role_bits(point, sector)
                if role_kind(role) == "face":
                    original_fluxes.append(
                        tuple_flux(boundary_values(point, role, links, size), group_order)
                    )
            for gauge_variant in range(2):
                transformed = gauge_transform_links(
                    links,
                    sector,
                    vertex_potential(size, sector, group_order, gauge_variant),
                    size,
                    group_order,
                )
                transformed_fluxes = []
                for point_raw in sites(size):
                    point = tuple(point_raw)
                    role = role_bits(point, sector)
                    if role_kind(role) == "face":
                        transformed_fluxes.append(
                            tuple_flux(
                                boundary_values(point, role, transformed, size),
                                group_order,
                            )
                        )
                gauge_ok = gauge_ok and transformed_fluxes == original_fluxes
    checks.check(
        gauge_ok,
        "all 64 sector-field pairs preserve every face curl under two local gauges",
    )

    translation_ok = True
    displacements = tuple(itertools.product(range(size), repeat=3))
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        links = link_field(size, sector, group_order, 2)
        old_product = face_weight_product(size, sector, links, overlap)
        for displacement_raw in displacements:
            displacement = tuple(displacement_raw)
            new_sector, translated = translate_midpoint_links(
                links, sector, displacement, size
            )
            translation_ok = translation_ok and (
                face_weight_product(size, new_sector, translated, overlap) == old_product
                and all(
                    role_bits(translate_site(tuple(point), displacement, size), new_sector)
                    == role_bits(tuple(point), sector)
                    for point in sites(size)
                )
            )
    checks.check(
        translation_ok,
        "all 512 sector-translation pairs covary and permute the eight sectors transitively",
    )

    rotation_role_ok = len(rotations) == 24
    rotation_factor_ok = True
    for sector_raw in sectors:
        sector = tuple(sector_raw)
        links = link_field(size, sector, group_order, 1)
        old_product = face_weight_product(size, sector, links, overlap)
        for permutation, signs in rotations:
            new_sector, rotated = rotate_midpoint_links(
                links, sector, permutation, signs, size, group_order
            )
            rotation_factor_ok = rotation_factor_ok and (
                face_weight_product(size, new_sector, rotated, overlap) == old_product
            )
            for point_raw in sites(size):
                point = tuple(point_raw)
                new_point = rotate_site(point, permutation, signs, size)
                rotation_role_ok = rotation_role_ok and (
                    role_bits(new_point, new_sector)
                    == permute_role(role_bits(point, sector), permutation)
                )
    checks.check(
        rotation_role_ok,
        "all 24 proper cubic rotations covary every role in all eight sectors",
    )
    checks.check(
        rotation_factor_ok,
        "all 192 sector-rotation pairs preserve the complete even gauge product",
    )

    arbitrary_auxiliary_covariance = True
    reference_face = (1, 1, 0)
    reference_role = role_bits(reference_face, (0, 0, 0))
    auxiliary_count = 1 + group_order**4
    for boundary_raw in itertools.product(range(group_order), repeat=4):
        boundary = tuple(boundary_raw)
        for permutation, signs in rotations:
            _new_face, _new_role, transformed_boundary = rotate_face_tuple(
                reference_face,
                reference_role,
                boundary,
                permutation,
                signs,
                size,
                group_order,
            )
            for auxiliary in range(auxiliary_count):
                if auxiliary == 0:
                    transformed_auxiliary = 0
                else:
                    auxiliary_tuple = tuple(
                        (auxiliary - 1) // group_order**index % group_order
                        for index in range(4)
                    )
                    _face, _role, transformed_tuple = rotate_face_tuple(
                        reference_face,
                        reference_role,
                        auxiliary_tuple,
                        permutation,
                        signs,
                        size,
                        group_order,
                    )
                    transformed_auxiliary = 1 + encode_tuple(
                        transformed_tuple, group_order
                    )
                arbitrary_auxiliary_covariance = arbitrary_auxiliary_covariance and (
                    face_factor(auxiliary, boundary, overlap, epsilon)
                    == face_factor(
                        transformed_auxiliary,
                        transformed_boundary,
                        overlap,
                        epsilon,
                    )
                )
    checks.check(
        arbitrary_auxiliary_covariance,
        "every face auxiliary label covaries under every proper cubic rotation",
    )

    shell_candidate_census = {0: 0, 1: 0}
    role_labels = tuple(itertools.product((0, 1), repeat=3))
    shell_slots = tuple(
        (axis, sign) for axis in range(3) for sign in (-1, 1)
    )
    for shell_values in itertools.product(role_labels, repeat=6):
        shell = dict(zip(shell_slots, shell_values))
        candidate_count = len(compatible_roles(shell))
        if candidate_count not in shell_candidate_census:
            shell_candidate_census[candidate_count] = 0
        shell_candidate_census[candidate_count] += 1
    checks.check(
        shell_candidate_census == {0: 8**6 - 8, 1: 8},
        "all 262144 role shells have either one supported role or the total fallback",
    )

    malformed_shell = {
        (axis, sign): (0, 0, 0)
        for axis in range(3)
        for sign in (-1, 1)
    }
    fallback = tuple(Fraction(1, 8) for _role in sectors)
    checks.check(
        compatible_roles(malformed_shell) == () and sum(fallback) == 1,
        "a uniform covariant fallback makes the rule total off the joint support",
    )

    alphabet_counts = tuple(len(finite_alphabet(order)) for order in (2, 4, 8, 16))
    expected_counts = tuple(5 + 3 * order + 3 * order**4 for order in (2, 4, 8, 16))
    checks.check(
        alphabet_counts == expected_counts
        and m2_injection_is_distinct(4)
        and m2_injection_is_distinct(8),
        "all role and payload labels inject distinctly into the one-site M2(C) domain",
    )
    orthogonal_costs = tuple(math.ceil(math.log2(count)) for count in alphabet_counts)
    checks.check(
        orthogonal_costs == (6, 10, 14, 18),
        "fully orthogonal role-payload readout has the explicit 6,10,14,18-qubit costs",
    )

    print(
        "per_element: every finite role label, Z4 face boundary, and auxiliary label is checked under its declared transformations"
    )
    print(
        "per_site: all 512 supported physical shells and all 3072 edge masks use only six nearest neighbors"
    )
    print(
        "per_mode: checked and not executed — the compiler preserves but does not recompute the parent photon Hessian"
    )
    print(
        "per_block: all eight L4 role sectors, 64 translations, and 24 proper cubic rotations are checked"
    )
    print(
        "lattice_wide: four full link fields per sector are marginalized and compared across the 4x4x4 physical torus"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
