#!/usr/bin/env python3
"""Exact bounded signed-Clifford seam compiler for Cycle709.

The source object is the Cycle706/708 OpenReference-to-PatchGraph+rail signed
tableau.  This module replaces its host-sized free symplectic completion, on
the declared code space, by four local Pauli transvections per seam, a fixed
six-colour schedule, and a frozen radius-one rail cleanup predicate.  It does
not prepare the supplied source stabilizer sector or supply a controller.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle708_physical_endpoint_cube_core_2026_07_26 as G
import frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26 as F


Pauli = G.c706.base.Pauli
Coord = tuple[int, int, int]
ALL_COLOURS = tuple(product(range(3), range(2)))
REFERENCE_FACTORS = (
    (0, (13, 30, 36), (14, 15, 16, 17, 31, 32, 33, 34, 35, 37)),
    (0, (13, 30, 36), (14, 15, 16, 17, 31, 32, 33, 34, 35)),
    (0, (), (37,)),
    (1, (37,), (37,)),
)
ROTATION_SIGNS = (1, -1, -1, 1)


def gf2_basis(rows) -> tuple[int, ...]:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return tuple(pivots[key] for key in sorted(pivots, reverse=True))


def xor_selected(rows, selector: int) -> int:
    result = 0
    for index, row in enumerate(rows):
        if (selector >> index) & 1:
            result ^= row
    return result


def anticommutes(left: Pauli, right: Pauli) -> int:
    return (
        (left.x & right.z).bit_count() + (left.z & right.x).bit_count()
    ) & 1


def identity_images(qubits: int) -> tuple[Pauli, ...]:
    return tuple(
        [Pauli(x=1 << index) for index in range(qubits)]
        + [Pauli(z=1 << index) for index in range(qubits)]
    )


def apply_images(images, row: Pauli, qubits: int) -> Pauli:
    result = Pauli(row.phase)
    for offset, bits in ((0, row.x), (qubits, row.z)):
        while bits:
            bit = bits & -bits
            result = result @ images[offset + bit.bit_length() - 1]
            bits ^= bit
    return result


def compose(after, before, qubits: int) -> tuple[Pauli, ...]:
    return tuple(apply_images(after, row, qubits) for row in before)


def natural(eq, row: Pauli) -> Pauli:
    x = z = 0
    for source, target in eq.natural_edge_map.items():
        x |= ((row.x >> source) & 1) << target
        z |= ((row.z >> source) & 1) << target
    return Pauli(row.phase, x, z)


def target_images(eq) -> tuple[Pauli, ...]:
    """Cycle706/708 signed tableau in natural PatchGraph+rail addresses."""
    inverse = {target: source for source, target in eq.natural_edge_map.items()}
    output = []
    for kind in range(2):
        for target in range(eq.qubits):
            source = inverse[target]
            row = Pauli(
                x=(1 << source) if kind == 0 else 0,
                z=(1 << source) if kind == 1 else 0,
            )
            image = eq.forward(row)
            output.append(Pauli(image.phase, image.x, image.z))
    return tuple(output)


def address(eq, qubit: int):
    patch = len(eq.patch_graph.edges)
    if qubit < patch:
        return "edge", G.c706.edge_key(eq.patch_graph, qubit)
    return "rail", eq.rail_labels[qubit - patch]


def address_lookup(eq) -> dict[object, int]:
    return {address(eq, qubit): qubit for qubit in range(eq.qubits)}


def shifted_address(item, shift: Coord):
    kind, label = item
    def move(vertex):
        vertex_cell, mode = vertex
        return tuple(a + b for a, b in zip(vertex_cell, shift)), mode
    if kind == "rail":
        return kind, frozenset(move(vertex) for vertex in label)
    vertices, edge_kind = label
    return kind, (frozenset(move(vertex) for vertex in vertices), edge_kind)


def _reference_factors(pauli_class=F.base.Pauli):
    return tuple(
        pauli_class(
            phase,
            sum(1 << index for index in x_indices),
            sum(1 << index for index in z_indices),
        )
        for phase, x_indices, z_indices in REFERENCE_FACTORS
    )


@lru_cache(maxsize=3)
def positive_axis_template(axis: int):
    """Gauge-aware Cycle706 transport of the +x factorization."""
    source = F.build_equivalence(((0, 0, 0), (1, 0, 0)))
    for frame in F.base.proper_cubic_frames():
        endpoint = tuple(int(value) for value in frame @ F.np.asarray((1, 0, 0)))
        if endpoint != tuple(int(index == axis) for index in range(3)):
            continue
        cells = ((0, 0, 0), endpoint)
        target = F.build_equivalence(cells)
        transform = F.graph_transform_data(source.patch_graph, target.patch_graph, frame)
        if transform[-1]:
            raise AssertionError(("Cycle706 order-gauge transport failed", axis))
        factors = tuple(
            F.transform_augmented_pauli(row, source, target, transform, transform[0])
            for row in _reference_factors()
        )
        return target, factors
    raise ValueError(("missing positive-axis proper frame", axis))


def seam_factors(eq, cell: Coord, axis: int) -> tuple[Pauli, ...]:
    lookup = address_lookup(eq)
    template, factors = positive_axis_template(axis)
    output = []
    for row in factors:
        x = z = 0
        for qubit in range(template.qubits):
            target = lookup[shifted_address(address(template, qubit), cell)]
            x |= ((row.x >> qubit) & 1) << target
            z |= ((row.z >> qubit) & 1) << target
        output.append(Pauli(row.phase, x, z))
    return tuple(output)


def transvection_images(qubits: int, axis: Pauli, sign: int) -> tuple[Pauli, ...]:
    output = []
    for row in identity_images(qubits):
        if anticommutes(row, axis):
            # R_s(P) row R_s(P)^dagger = (-i s P) row.
            output.append(Pauli(3 if sign == 1 else 1) @ axis @ row)
        else:
            output.append(row)
    return tuple(output)


def seam_images(eq, cell: Coord, axis: int) -> tuple[Pauli, ...]:
    current = identity_images(eq.qubits)
    for factor, sign in zip(seam_factors(eq, cell, axis), ROTATION_SIGNS):
        current = compose(transvection_images(eq.qubits, factor, sign), current, eq.qubits)
    return current


def seam_key(label) -> tuple[Coord, int]:
    cells = tuple(vertex[0] for vertex in label)
    lower, upper = min(cells), max(cells)
    delta = tuple(right - left for left, right in zip(lower, upper))
    if delta.count(1) != 1 or any(value not in (0, 1) for value in delta):
        raise ValueError(("unlawful rail label", label))
    return lower, delta.index(1)


def seam_endpoints(key: tuple[Coord, int]) -> tuple[Coord, Coord]:
    lower, axis = key
    upper = tuple(value + int(index == axis) for index, value in enumerate(lower))
    return lower, upper


def seam_colour(key: tuple[Coord, int], colour_origin: Coord = (0, 0, 0)):
    lower, axis = key
    return axis, (lower[axis] - colour_origin[axis]) & 1


def cleanup_predicate(
    left: tuple[Coord, int],
    right: tuple[Coord, int],
    colour_origin: Coord = (0, 0, 0),
) -> bool:
    """Frozen radius-one A_ef; includes orthogonal and collinear pairs."""
    common = set(seam_endpoints(left)) & set(seam_endpoints(right))
    if len(common) != 1:
        return False
    vertex = next(iter(common))
    lcolour, rcolour = seam_colour(left, colour_origin), seam_colour(right, colour_origin)
    llo, lhi = seam_endpoints(left)
    rlo, rhi = seam_endpoints(right)
    return (
        lcolour < rcolour and llo == vertex and rhi == vertex
    ) or (
        rcolour < lcolour and rlo == vertex and lhi == vertex
    )


def cleanup_edges(eq, colour_origin: Coord = (0, 0, 0)) -> tuple[tuple[int, int], ...]:
    keys = tuple(seam_key(label) for label in eq.rail_labels)
    return tuple(
        (left, right)
        for left in range(len(keys))
        for right in range(left + 1, len(keys))
        if cleanup_predicate(keys[left], keys[right], colour_origin)
    )


def cleanup_images(eq, edges=None) -> tuple[Pauli, ...]:
    qubits = eq.qubits
    patch = len(eq.patch_graph.edges)
    edges = cleanup_edges(eq) if edges is None else tuple(edges)

    def h_layer():
        images = list(identity_images(qubits))
        for rail in range(len(eq.rail_labels)):
            qubit = patch + rail
            images[qubit] = Pauli(z=1 << qubit)
            images[qubits + qubit] = Pauli(x=1 << qubit)
        return tuple(images)

    def cz_layer():
        images = list(identity_images(qubits))
        for left, right in edges:
            i, j = patch + left, patch + right
            images[i] = images[i] @ Pauli(z=1 << j)
            images[j] = images[j] @ Pauli(z=1 << i)
        return tuple(images)

    h = h_layer()
    return compose(h, compose(cz_layer(), h, qubits), qubits)


@dataclass(frozen=True)
class Composition:
    equivalence: object
    coloured: tuple[Pauli, ...]
    cleaned: tuple[Pauli, ...]
    target: tuple[Pauli, ...]
    cleanup: tuple[tuple[int, int], ...]


def canonical_box_shape(cells: tuple[Coord, ...]) -> tuple[int, int, int]:
    if not cells:
        raise ValueError("empty cell tuple")
    minimum = tuple(min(cell[axis] for cell in cells) for axis in range(3))
    maximum = tuple(max(cell[axis] for cell in cells) for axis in range(3))
    shape = tuple(maximum[axis] - minimum[axis] + 1 for axis in range(3))
    expected = tuple(
        tuple(cell[axis] + minimum[axis] for axis in range(3))
        for cell in G.box_cells(shape)
    )
    if tuple(cells) != expected:
        raise ValueError("cells must use the supplied canonical box/path order")
    return shape


def coloured_composition(
    cells: tuple[Coord, ...], colour_origin: Coord = (0, 0, 0)
) -> Composition:
    canonical_box_shape(cells)
    eq = G.build_equivalence(cells).equivalence
    layers = {colour: identity_images(eq.qubits) for colour in ALL_COLOURS}
    for cell, axis, _matter, _reference in eq.open_graph.cross_edges:
        colour = seam_colour((cell, axis), colour_origin)
        layers[colour] = compose(seam_images(eq, cell, axis), layers[colour], eq.qubits)
    coloured = identity_images(eq.qubits)
    for colour in ALL_COLOURS:
        coloured = compose(layers[colour], coloured, eq.qubits)
    edges = cleanup_edges(eq, colour_origin)
    cleaned = compose(cleanup_images(eq, edges), coloured, eq.qubits)
    return Composition(eq, coloured, cleaned, target_images(eq), edges)


def mismatch_counts(left, right) -> dict[str, int]:
    return {
        "exact": sum(a != b for a, b in zip(left, right)),
        "symplectic": sum((a.x, a.z) != (b.x, b.z) for a, b in zip(left, right)),
        "phase_only": sum(
            (a.x, a.z) == (b.x, b.z) and a.phase != b.phase
            for a, b in zip(left, right)
        ),
    }


def reference_certificate() -> dict[str, object]:
    eq = G.build_equivalence(((0, 0, 0), (1, 0, 0))).equivalence
    identity = identity_images(eq.qubits)
    target = target_images(eq)
    delta = tuple(
        (left.x ^ right.x) | ((left.z ^ right.z) << eq.qubits)
        for left, right in zip(target, identity)
    )
    basis = gf2_basis(delta)
    nonzero_image = tuple(
        xor_selected(basis, selector)
        for selector in range(1, 1 << len(basis))
    )
    target_binary = tuple(row.symplectic(eq.qubits) for row in target)
    frontier = {tuple(row.symplectic(eq.qubits) for row in identity)}
    depth_hits = {}
    mask = (1 << eq.qubits) - 1
    for depth in range(1, 4):
        frontier = {
            tuple(
                row ^ (
                    axis
                    if (
                        ((row & mask) & (axis >> eq.qubits)).bit_count()
                        + ((row >> eq.qubits) & (axis & mask)).bit_count()
                    ) & 1
                    else 0
                )
                for row in state
            )
            for state in frontier
            for axis in nonzero_image
        }
        depth_hits[depth] = target_binary in frontier
    factors = seam_factors(eq, (0, 0, 0), 0)
    return {
        "qubits": eq.qubits,
        "rank_S_minus_I": len(basis),
        "depth_le_three_hits": depth_hits,
        "constructed_transvection_depth": 4,
        "depth_search_axis_class": "all nonzero axes in im(S-I)",
        "factor_weights": tuple((row.x | row.z).bit_count() for row in factors),
        "factor_phases": tuple(row.phase for row in factors),
        "rotation_signs": ROTATION_SIGNS,
        "hermitian_failures": sum(
            row.phase != ((row.x & row.z).bit_count() & 1) for row in factors
        ),
        "signed_mismatches": mismatch_counts(seam_images(eq, (0, 0, 0), 0), target),
        "delete_factor_failures": tuple(
            mismatch_counts(
                _factor_subset_images(eq, factors, deleted), target
            )["exact"]
            for deleted in range(4)
        ),
    }


def _factor_subset_images(eq, factors, deleted: int) -> tuple[Pauli, ...]:
    current = identity_images(eq.qubits)
    for index, (factor, sign) in enumerate(zip(factors, ROTATION_SIGNS)):
        if index != deleted:
            current = compose(transvection_images(eq.qubits, factor, sign), current, eq.qubits)
    return current


def frame_transport_certificate() -> dict[str, object]:
    """Transport the signed factorization through Cycle706's order gauge."""
    source = F.build_equivalence(((0, 0, 0), (1, 0, 0)))
    factors = _reference_factors()
    rows = []
    for frame in F.base.proper_cubic_frames():
        cells = tuple(
            tuple(int(value) for value in frame @ F.np.asarray(cell))
            for cell in source.cells
        )
        target = F.build_equivalence(cells)
        transform = F.graph_transform_data(source.patch_graph, target.patch_graph, frame)
        moved = tuple(
            F.transform_augmented_pauli(row, source, target, transform, transform[0])
            for row in factors
        )
        current = identity_images(target.qubits)
        for row, sign in zip(moved, ROTATION_SIGNS):
            axis = Pauli(row.phase, row.x, row.z)
            current = compose(
                transvection_images(target.qubits, axis, sign), current, target.qubits
            )
        delta = tuple(cells[1][index] - cells[0][index] for index in range(3))
        rows.append({
            "direction": delta,
            "factor_weights": tuple((row.x | row.z).bit_count() for row in moved),
            "factor_phases": tuple(row.phase for row in moved),
            "transport_failures": transform[-1],
            "hermitian_failures": sum(
                row.phase % 2 != ((row.x & row.z).bit_count() & 1) for row in moved
            ),
            "mismatches": mismatch_counts(current, target_images(target)),
        })
    direction_census = Counter(row["direction"] for row in rows)
    weight_census = Counter(row["factor_weights"] for row in rows)
    phase_census = Counter(row["factor_phases"] for row in rows)
    return {
        "proper_cubic_frames": len(rows),
        "direction_census": dict(sorted(direction_census.items())),
        "weight_census": dict(sorted(weight_census.items())),
        "phase_census": dict(sorted(phase_census.items())),
        "order_gauge_transport_failures": sum(row["transport_failures"] for row in rows),
        "hermitian_failures": sum(row["hermitian_failures"] for row in rows),
        "signed_exact_failures": sum(row["mismatches"]["exact"] for row in rows),
        "signed_phase_only_failures": sum(
            row["mismatches"]["phase_only"] for row in rows
        ),
    }


def frame_product_certificate() -> dict[str, object]:
    source = F.build_equivalence(((0, 0, 0), (1, 0, 0)))
    factors = _reference_factors()
    frames = F.base.proper_cubic_frames()
    frame_keys = {tuple(int(value) for value in frame.flat) for frame in frames}
    closure_failures = cell_failures = factor_failures = 0
    for left in frames:
        for right in frames:
            product_frame = left @ right
            closure_failures += tuple(int(value) for value in product_frame.flat) not in frame_keys
            mid_cells = tuple(
                tuple(int(value) for value in right @ F.np.asarray(cell))
                for cell in source.cells
            )
            final_cells = tuple(
                tuple(int(value) for value in left @ F.np.asarray(cell))
                for cell in mid_cells
            )
            direct_cells = tuple(
                tuple(int(value) for value in product_frame @ F.np.asarray(cell))
                for cell in source.cells
            )
            cell_failures += final_cells != direct_cells
            mid = F.build_equivalence(mid_cells)
            final = F.build_equivalence(final_cells)
            first = F.graph_transform_data(source.patch_graph, mid.patch_graph, right)
            second = F.graph_transform_data(mid.patch_graph, final.patch_graph, left)
            direct = F.graph_transform_data(
                source.patch_graph, final.patch_graph, product_frame
            )
            sequential_rows = tuple(
                F.transform_augmented_pauli(
                    F.transform_augmented_pauli(row, source, mid, first, first[0]),
                    mid, final, second, second[0],
                )
                for row in factors
            )
            direct_rows = tuple(
                F.transform_augmented_pauli(row, source, final, direct, direct[0])
                for row in factors
            )
            factor_failures += sequential_rows != direct_rows
    return {
        "ordered_frame_products": len(frames) ** 2,
        "group_closure_failures": closure_failures,
        "cell_diagram_failures": cell_failures,
        "signed_factor_diagram_failures": factor_failures,
    }


def fixture_certificate(shape: tuple[int, int, int]) -> dict[str, object]:
    composition = coloured_composition(G.box_cells(shape))
    eq = composition.equivalence
    keys = tuple(seam_key(label) for label in eq.rail_labels)
    degrees = Counter(index for edge in composition.cleanup for index in edge)
    collinear = tuple(edge for edge in composition.cleanup if keys[edge[0]][1] == keys[edge[1]][1])
    orthogonal = tuple(edge for edge in composition.cleanup if edge not in collinear)
    orthogonal_result = compose(cleanup_images(eq, orthogonal), composition.coloured, eq.qubits)
    patch = len(eq.patch_graph.edges)
    bond_images = tuple(
        apply_images(composition.coloured, natural(eq, source), eq.qubits)
        for source in eq.source_bond_loops
    )
    observed_edges = tuple(
        (left, right)
        for left in range(len(bond_images))
        for right in range(left + 1, len(bond_images))
        if (bond_images[left].x >> (patch + right)) & 1
    )
    single_collinear_delete_failures = tuple(
        mismatch_counts(
            compose(
                cleanup_images(
                    eq, tuple(candidate for candidate in composition.cleanup if candidate != edge)
                ),
                composition.coloured,
                eq.qubits,
            ),
            composition.target,
        )["exact"]
        for edge in collinear
    )
    by_colour = _coloured_operations(eq)
    support_collisions = 0
    for colour in ALL_COLOURS:
        supports = []
        for cell, axis in by_colour[colour]:
            factors = seam_factors(eq, cell, axis)
            support = 0
            for factor in factors:
                support |= factor.x | factor.z
            support_collisions += sum(bool(support & prior) for prior in supports)
            supports.append(support)
    cleanup_vertex_colours: dict[int, int] = {}
    bipartite_failures = 0
    adjacency = {index: set() for index in range(len(keys))}
    for left, right in composition.cleanup:
        adjacency[left].add(right)
        adjacency[right].add(left)
    for start in adjacency:
        if start in cleanup_vertex_colours:
            continue
        cleanup_vertex_colours[start] = 0
        stack = [start]
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor not in cleanup_vertex_colours:
                    cleanup_vertex_colours[neighbor] = 1 - cleanup_vertex_colours[vertex]
                    stack.append(neighbor)
                elif cleanup_vertex_colours[neighbor] == cleanup_vertex_colours[vertex]:
                    bipartite_failures += 1
    identity = identity_images(eq.qubits)
    return {
        "shape": shape,
        "cells": len(eq.open_graph.cells),
        "qubits": eq.qubits,
        "seams": len(eq.rail_labels),
        "rank_S_minus_I": len(gf2_basis(
            (left.x ^ right.x) | ((left.z ^ right.z) << eq.qubits)
            for left, right in zip(composition.target, identity)
        )),
        "six_colour_layers": len(ALL_COLOURS),
        "colours_present": tuple(sorted({seam_colour(key) for key in keys})),
        "same_colour_factor_support_collisions": support_collisions,
        "coloured_mismatches": mismatch_counts(composition.coloured, composition.target),
        "cleanup_edges": len(composition.cleanup),
        "collinear_cleanup_edges": len(collinear),
        "cleanup_max_degree": max(degrees.values(), default=0),
        "cleanup_bipartite_failures": bipartite_failures,
        "orthogonal_only_mismatches": mismatch_counts(orthogonal_result, composition.target),
        "single_collinear_delete_failures": single_collinear_delete_failures,
        "cleaned_mismatches": mismatch_counts(composition.cleaned, composition.target),
        "predicate_false_positives": tuple(sorted(set(composition.cleanup) - set(observed_edges))),
        "predicate_false_negatives": tuple(sorted(set(observed_edges) - set(composition.cleanup))),
        "independent_bond_row_oracle_edges": len(observed_edges),
        "parameters_refit": 0,
    }


def five_box_certificate() -> tuple[dict[str, object], ...]:
    return tuple(
        fixture_certificate(shape)
        for shape in ((2, 2, 2), (3, 2, 2), (4, 2, 2), (3, 3, 2), (3, 3, 3))
    )


def _coloured_operations(eq, colour_origin=(0, 0, 0)):
    by_colour = {colour: [] for colour in ALL_COLOURS}
    for cell, axis, _matter, _reference in eq.open_graph.cross_edges:
        by_colour[seam_colour((cell, axis), colour_origin)].append((cell, axis))
    return by_colour


def deletion_certificate() -> dict[str, object]:
    composition = coloured_composition(G.box_cells((3, 2, 2)))
    eq = composition.equivalence
    by_colour = _coloured_operations(eq)
    present = tuple(colour for colour in ALL_COLOURS if by_colour[colour])
    deleted_colour_failures = []
    for deleted in present:
        coloured = identity_images(eq.qubits)
        for colour in ALL_COLOURS:
            if colour == deleted:
                continue
            for cell, axis in by_colour[colour]:
                coloured = compose(seam_images(eq, cell, axis), coloured, eq.qubits)
        cleaned = compose(cleanup_images(eq, composition.cleanup), coloured, eq.qubits)
        deleted_colour_failures.append(mismatch_counts(cleaned, composition.target)["exact"])
    deleted_cleanup_failures = tuple(
        mismatch_counts(
            compose(
                cleanup_images(
                    eq, tuple(edge for index, edge in enumerate(composition.cleanup) if index != deleted)
                ),
                composition.coloured,
                eq.qubits,
            ),
            composition.target,
        )["exact"]
        for deleted in range(len(composition.cleanup))
    )
    reference = G.build_equivalence(((0, 0, 0), (1, 0, 0))).equivalence
    factors = seam_factors(reference, (0, 0, 0), 0)
    wrong_sign_failures = []
    for flipped in range(4):
        current = identity_images(reference.qubits)
        for index, (factor, sign) in enumerate(zip(factors, ROTATION_SIGNS)):
            current = compose(
                transvection_images(reference.qubits, factor, -sign if index == flipped else sign),
                current,
                reference.qubits,
            )
        wrong_sign_failures.append(
            mismatch_counts(current, target_images(reference))["exact"]
        )
    return {
        "active_colours_present": present,
        "delete_active_colour_failures": tuple(deleted_colour_failures),
        "delete_cleanup_edge_failures": deleted_cleanup_failures,
        "wrong_rotation_sign_failures": tuple(wrong_sign_failures),
        "empty_colour_layers_declared_noops": tuple(
            colour for colour in ALL_COLOURS if not by_colour[colour]
        ),
    }


def inverse_certificate() -> dict[str, object]:
    composition = coloured_composition(G.box_cells((3, 2, 2)))
    eq = composition.equivalence
    operations = []
    by_colour = _coloured_operations(eq)
    for colour in ALL_COLOURS:
        for cell, axis in by_colour[colour]:
            operations.extend(zip(seam_factors(eq, cell, axis), ROTATION_SIGNS))
    inverse_coloured = identity_images(eq.qubits)
    for factor, sign in reversed(operations):
        inverse_coloured = compose(
            transvection_images(eq.qubits, factor, -sign), inverse_coloured, eq.qubits
        )
    inverse = compose(inverse_coloured, cleanup_images(eq, composition.cleanup), eq.qubits)
    return {
        "primary_signed_inverse_failures": mismatch_counts(
            compose(inverse, composition.cleaned, eq.qubits), identity_images(eq.qubits)
        ),
        "inverse_gate_order": "cleanup inverse then reversed seams/factors with negated signs",
    }


def translation_certificate() -> dict[str, object]:
    base_cells = G.box_cells((2, 2, 2))
    failures = omitted_origin_changes = 0
    for shift in product(range(2), repeat=3):
        moved_cells = tuple(
            tuple(value + delta for value, delta in zip(cell, shift)) for cell in base_cells
        )
        moved = coloured_composition(moved_cells, shift)
        failures += mismatch_counts(moved.cleaned, moved.target)["exact"]
        if shift != (0, 0, 0):
            wrong = coloured_composition(moved_cells, (0, 0, 0))
            omitted_origin_changes += wrong.cleanup != moved.cleanup
    return {
        "parity_residue_translations": 8,
        "translated_semantic_failures": failures,
        "omit_translated_colour_origin_changes_cleanup": omitted_origin_changes,
        "colour_origin": "supplied and translated with the chart",
    }


def _unordered_coloured_composition(
    cells: tuple[Coord, ...], colour_origin: Coord = (0, 0, 0)
) -> Composition:
    """Diagnostic only: expose the semantic effect hidden by the lawful guard."""
    eq = G.build_equivalence(tuple(cells)).equivalence
    layers = {colour: identity_images(eq.qubits) for colour in ALL_COLOURS}
    for cell, axis, _matter, _reference in eq.open_graph.cross_edges:
        colour = seam_colour((cell, axis), colour_origin)
        layers[colour] = compose(
            seam_images(eq, cell, axis), layers[colour], eq.qubits
        )
    coloured = identity_images(eq.qubits)
    for colour in ALL_COLOURS:
        coloured = compose(layers[colour], coloured, eq.qubits)
    edges = cleanup_edges(eq, colour_origin)
    cleaned = compose(cleanup_images(eq, edges), coloured, eq.qubits)
    return Composition(eq, coloured, cleaned, target_images(eq), edges)


def _semantic_rows(eq) -> dict[str, tuple[tuple[Pauli, Pauli], ...]]:
    rows = {
        "logical_Z": tuple(zip(eq.source_logical_z, eq.target_logical_z)),
        "logical_X": tuple(zip(eq.source_logical_x, eq.target_logical_x)),
        "local_D_all": tuple(
            (
                G.c706.local_d(eq.open_graph, cell),
                G.c706.local_d(eq.patch_graph, cell),
            )
            for cell in eq.cells
        ),
        "bond_to_rail": tuple(zip(eq.source_bond_loops, eq.target_rails)),
    }
    loops: dict[str, list[tuple[Pauli, Pauli]]] = {}
    for descriptor in G.c706.local_cycles(eq.open_graph):
        if descriptor.kind == "bond_rectangle":
            continue
        source = eq.open_graph.loop_pauli(descriptor.vertices)
        vertices = tuple(
            eq.patch_graph.vertex_index[eq.open_graph.vertices[vertex]]
            for vertex in descriptor.vertices
        )
        target = eq.patch_graph.loop_pauli(vertices)
        loops.setdefault(descriptor.kind, []).append((source, target))
    rows.update({kind: tuple(pairs) for kind, pairs in loops.items()})
    return rows


def _positive_stabilizer_difference(row: Pauli, eq) -> bool:
    coordinates = G.c706.decode(row, eq.target_w, eq.target_v, eq.qubits)
    logical_mask = (1 << len(eq.target_logical_z)) - 1
    return (
        coordinates.phase == 0
        and coordinates.v_mask == 0
        and (coordinates.w_mask & logical_mask) == 0
    )


def _semantic_code_failures(images, eq) -> dict[str, dict[str, int]]:
    report = {}
    for name, pairs in _semantic_rows(eq).items():
        exact = symplectic = phase_only = code = 0
        for source, expected in pairs:
            observed = apply_images(images, natural(eq, source), eq.qubits)
            exact += observed != expected
            symplectic += (observed.x, observed.z) != (expected.x, expected.z)
            phase_only += (
                (observed.x, observed.z) == (expected.x, expected.z)
                and observed.phase != expected.phase
            )
            difference = observed @ expected
            code += not _positive_stabilizer_difference(difference, eq)
        report[name] = {
            "exact": exact,
            "symplectic": symplectic,
            "phase_only": phase_only,
            "code": code,
        }
    return report


def cell_order_adversary_certificate() -> dict[str, object]:
    """Twelve deterministic shuffles reveal the load-bearing order import."""
    canonical = G.box_cells((2, 2, 2))
    rng = F.np.random.default_rng(1709)
    permutations = [canonical]
    for _ in range(12):
        order = list(canonical)
        rng.shuffle(order)
        permutations.append(tuple(order))
    rows = []
    for index, cells in enumerate(permutations):
        composition = _unordered_coloured_composition(cells)
        eq = composition.equivalence
        keys = tuple(seam_key(label) for label in eq.rail_labels)
        semantic = _semantic_code_failures(composition.cleaned, eq)
        rows.append({
            "index": index,
            "full_exact_mismatches": mismatch_counts(
                composition.cleaned, composition.target
            )["exact"],
            "semantic_code_failures": semantic,
            "cleanup_edge_keys": tuple(sorted(
                tuple(sorted((keys[left], keys[right])))
                for left, right in composition.cleanup
            )),
        })
    base_edges = rows[0]["cleanup_edge_keys"]
    names = rows[0]["semantic_code_failures"]
    return {
        "orders": len(rows),
        "shuffles": len(rows) - 1,
        "canonical_full_mismatches": rows[0]["full_exact_mismatches"],
        "shuffled_full_mismatch_census": tuple(
            row["full_exact_mismatches"] for row in rows[1:]
        ),
        "semantic_code_failure_sums": {
            name: {
                field: sum(
                    row["semantic_code_failures"][name][field] for row in rows
                )
                for field in ("exact", "symplectic", "phase_only", "code")
            }
            for name in names
        },
        "coarse_plaquette_exact_per_shuffle": tuple(
            row["semantic_code_failures"]["coarse_plaquette"]["exact"]
            for row in rows[1:]
        ),
        "geometric_cleanup_edge_order_failures": sum(
            row["cleanup_edge_keys"] != base_edges for row in rows
        ),
    }


def unlawful_certificate() -> dict[str, object]:
    cells = list(G.box_cells((2, 2, 2)))
    cells[1], cells[2] = cells[2], cells[1]
    shuffled_rejected = False
    try:
        coloured_composition(tuple(cells))
    except ValueError:
        shuffled_rejected = True
    disconnected_rejected = False
    try:
        coloured_composition(((0, 0, 0), (2, 0, 0)))
    except ValueError:
        disconnected_rejected = True
    duplicate_rejected = False
    try:
        coloured_composition(((0, 0, 0), (0, 0, 0)))
    except ValueError:
        duplicate_rejected = True
    return {
        "shuffled_cell_path_order_rejected": shuffled_rejected,
        "disconnected_box_rejected": disconnected_rejected,
        "duplicate_cell_rejected": duplicate_rejected,
        "accepted_domain": "translated rectangular boxes in supplied canonical product order",
    }


def boundary_inventory() -> dict[str, tuple[str, ...]]:
    return {
        "runtime_inputs": (
            "translated rectangular open box in supplied canonical product cell/path order",
            "Cycle706 OpenReference +1 loop/D/bond source sector",
            "Cycle706 natural PatchGraph edge map and one rail per seam",
            "supplied integer chart origin and proper-cubic coframe",
            "supplied colour origin and fixed lexicographic six-layer order",
            "four signed reference-seam factor template",
            "frozen radius-one cleanup predicate A_ef",
        ),
        "removed_runtime_imports": (
            "host-sized lexicographic seam sweep",
            "free-zero global symplectic completion from the emitted local compiler word; retained only as a verification oracle",
            "cube 30-row deletion choice on the code-space compiler path",
            "held-size fitted cleanup adjacency table",
        ),
        "not_supplied_here": (
            "source stabilizer/repetition-sector genesis",
            "autonomous coframe, colour-origin, or layer-clock derivation",
            "autonomous recurrent controller",
            "periodic Wilson-sector character",
            "order-gauge repair for arbitrary permutations of the supplied cell/path tuple",
        ),
    }
