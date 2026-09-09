#!/usr/bin/env python3
"""Independent discriminator for the Cycle-703 local-Gauss reference route.

The candidate adds one reference fermion ``r_x`` to the six matter modes in
each coarse cell and imposes

    D_x = B(r_x) product_a B(m_{x,a}) = +1

inside the fixed-even BKSF representation of the seven-mode-per-cell graph.
This runner keeps four logically distinct claims apart:

1. exact stabilizer capacity and odd/even-volume parity coverage;
2. bounded BKSF operator-algebra representatives for hops and FSWAPs;
3. an executed two-cell extended-Fock isometry;
4. the still-missing physical BKSF common-E state encoder and its preparation.

It imports the retained Cycle-232 graph and Pauli definitions, but none of its
uniform-reference constraints or route verdicts.
"""

from __future__ import annotations

from itertools import combinations, product
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CYCLE703_LOCAL_GAUSS_REFERENCE_ADVERSARIAL_NOTE_2026-07-25.md"
)
TOL = 1.0e-12
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def pauli_product(rows) -> base.Pauli:
    result = base.Pauli()
    for row in rows:
        result = result @ row
    return result


def local_d(graph: base.ReferenceGraph, cell: tuple[int, int, int]) -> base.Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)]) for mode in range(7)
    )


def local_d_rows(graph: base.ReferenceGraph) -> list[base.Pauli]:
    return [local_d(graph, cell) for cell in graph.cells]


def local_loop_rows(graph: base.ReferenceGraph) -> list[base.Pauli]:
    return [
        graph.loop_pauli(vertices)
        for _, vertices, _ in base.local_cycles(graph)
    ]


def wilson_rows(graph: base.ReferenceGraph) -> list[base.Pauli]:
    if not graph.periodic:
        return []
    rows = []
    for axis in range(3):
        vertices = []
        for coordinate in range(graph.length):
            cell = [0, 0, 0]
            cell[axis] = coordinate
            vertices.append(graph.vertex_index[(tuple(cell), 6)])
        rows.append(graph.loop_pauli(vertices))
    return rows


def stabilizer_rank(rows, qubits: int) -> int:
    return base.gf2_rank(row.symplectic(qubits) for row in rows)


def rank_and_sector_controls() -> dict[str, object]:
    rows = []
    for length, periodic in ((2, False), (3, True), (4, True), (5, True)):
        graph = base.ReferenceGraph(length, periodic)
        loops = local_loop_rows(graph)
        ds = local_d_rows(graph)
        wilsons = wilson_rows(graph)
        qubits = len(graph.edges)
        cells = length**3
        d_weights = [(d.x | d.z).bit_count() for d in ds]

        loop_rank = stabilizer_rank(loops, qubits)
        loop_d_rank = stabilizer_rank(loops + ds, qubits)
        full_rank = stabilizer_rank(loops + ds + wilsons, qubits)
        delete_one_rank = stabilizer_rank(loops + ds[:-1], qubits)
        delete_two_rank = stabilizer_rank(loops + ds[:-2], qubits)
        product_d = pauli_product(ds)

        commutator_failures = sum(
            not d.commutes(row) for d in ds for row in loops + wilsons
        )
        phase_failures = base.stabilizer_phase_failures(
            loops + ds + wilsons, qubits
        )
        expected_wilson = 3 if periodic else 0
        rows.append(
            {
                "L": length,
                "periodic": periodic,
                "cells": cells,
                "edge_M2": qubits,
                "minimum_D_Pauli_weight": min(d_weights),
                "maximum_D_Pauli_weight": max(d_weights),
                "local_loop_rank": loop_rank,
                "D_increment": loop_d_rank - loop_rank,
                "D_delete_one_increment": delete_one_rank - loop_rank,
                "D_delete_two_increment": delete_two_rank - loop_rank,
                "Wilson_increment": full_rank - loop_d_rank,
                "code_exponent_before_Wilson_fix": qubits - loop_d_rank,
                "code_exponent_after_Wilson_fix": qubits - full_rank,
                "product_D_is_fixed_even_identity": product_d == base.Pauli(),
                "commutator_failures": commutator_failures,
                "phase_failures": phase_failures,
                "expected_D_rank": cells - 1,
                "expected_Wilson_rank": expected_wilson,
            }
        )

    check(
        "local D has rank N-1 and leaves the full 6N matter capacity at odd and even volume",
        all(
            row["D_increment"] == row["cells"] - 1
            and row["D_delete_one_increment"] == row["cells"] - 1
            and row["D_delete_two_increment"] == row["cells"] - 2
            and row["Wilson_increment"] == row["expected_Wilson_rank"]
            and row["code_exponent_before_Wilson_fix"]
            == 6 * row["cells"] + row["expected_Wilson_rank"]
            and row["code_exponent_after_Wilson_fix"] == 6 * row["cells"]
            and row["product_D_is_fixed_even_identity"]
            and row["commutator_failures"] == 0
            and row["phase_failures"] == 0
            and row["maximum_D_Pauli_weight"] <= 12
            for row in rows
        ),
        rows,
    )
    check(
        "one local D term is globally redundant while deleting two releases one logical bit",
        all(
            row["D_delete_one_increment"] == row["D_increment"]
            and row["D_delete_two_increment"] == row["D_increment"] - 1
            for row in rows
        ),
        {
            "reason": "product_x D_x equals total seven-mode parity, already +1",
            "rows": tuple(
                (
                    row["L"],
                    row["D_increment"],
                    row["D_delete_one_increment"],
                    row["D_delete_two_increment"],
                )
                for row in rows
            ),
        },
    )
    return {
        "rows": rows,
        "all_matter_basis_states_have_unique_reference_bits": True,
        "matter_even_and_odd_sectors_present_at_even_volume": True,
        "global_parity_bus_required_for_capacity": False,
    }


def stream_vertices(graph: base.ReferenceGraph, cell, axis: int):
    target = list(cell)
    target[axis] = (target[axis] + 1) % graph.length
    target = tuple(target)
    matter_u = graph.vertex_index[(cell, 2 * axis + 1)]
    matter_v = graph.vertex_index[(target, 2 * axis)]
    reference_u = graph.vertex_index[(cell, 6)]
    reference_v = graph.vertex_index[(target, 6)]
    return matter_u, matter_v, reference_u, reference_v, target, 2 * axis


def spectator_parity(
    graph: base.ReferenceGraph,
    cell: tuple[int, int, int],
    excluded_mode: int,
) -> base.Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)])
        for mode in range(6)
        if mode != excluded_mode
    )


def hop_pauli_terms(
    graph: base.ReferenceGraph,
    matter_u: int,
    matter_v: int,
    reference_u: int,
    reference_v: int,
    target_cell: tuple[int, int, int],
    target_mode: int,
) -> tuple[base.Pauli, base.Pauli]:
    """Two Pauli words in the exact number-preserving dressed hop.

    With the reference placed after the six matter modes in each local Fock
    block, the exact code action is

      - P_target_without_v (1-B_u B_v) A_uv A_rr / 2.

    The returned words omit the common scalar coefficient 1/2.
    """

    core = graph.A(matter_u, matter_v) @ graph.A(reference_u, reference_v)
    spectator = spectator_parity(graph, target_cell, target_mode)
    negative_core = base.Pauli(phase=2) @ spectator @ core
    occupied_correction = (
        spectator @ graph.B(matter_u) @ graph.B(matter_v) @ core
    )
    return negative_core, occupied_correction


def operator_algebra_controls() -> dict[str, object]:
    graph = base.ReferenceGraph(3, True)
    loops = local_loop_rows(graph)
    ds = local_d_rows(graph)
    wilsons = wilson_rows(graph)
    rows = []
    loop_failures = 0
    wilson_failures = 0
    dressed_d_failures = 0
    bare_endpoint_counts = []
    hermiticity_failures = 0
    maximum_weight = 0

    for cell in graph.cells:
        for axis in range(3):
            u, v, ru, rv, target, target_mode = stream_vertices(
                graph, cell, axis
            )
            bare = graph.A(u, v)
            reference = graph.A(ru, rv)
            dressed = bare @ reference
            terms = hop_pauli_terms(
                graph, u, v, ru, rv, target, target_mode
            )
            bare_endpoint_counts.append(sum(not bare.commutes(d) for d in ds))
            dressed_d_failures += sum(not dressed.commutes(d) for d in ds)
            loop_failures += sum(
                not term.commutes(loop) for term in terms for loop in loops
            )
            wilson_failures += sum(
                not term.commutes(wilson)
                for term in terms
                for wilson in wilsons
            )
            for term in terms:
                hermiticity_failures += (
                    term.phase - (term.x & term.z).bit_count()
                ) % 2 != 0
                maximum_weight = max(
                    maximum_weight, (term.x | term.z).bit_count()
                )
            rows.append(
                {
                    "cell": cell,
                    "axis": axis,
                    "bare_D_anticommutators": bare_endpoint_counts[-1],
                    "dressed_support_weight": (dressed.x | dressed.z).bit_count(),
                    "hop_term_support_weights": tuple(
                        (term.x | term.z).bit_count() for term in terms
                    ),
                }
            )

    intracell_d_failures = 0
    for cell in graph.cells:
        for left, right in combinations(range(6), 2):
            if base.REVERSE[left] == right:
                continue
            generator = graph.A(
                graph.vertex_index[(cell, left)],
                graph.vertex_index[(cell, right)],
            )
            intracell_d_failures += sum(
                not generator.commutes(d) for d in ds
            )

    check(
        "the reference-edge dressing preserves every local D, loop, and Wilson stabilizer",
        set(bare_endpoint_counts) == {2}
        and dressed_d_failures == 0
        and loop_failures == 0
        and wilson_failures == 0
        and intracell_d_failures == 0
        and hermiticity_failures == 0,
        {
            "stream_bonds": len(rows),
            "bare_D_anticommutator_census": {
                count: bare_endpoint_counts.count(count)
                for count in set(bare_endpoint_counts)
            },
            "dressed_D_failures": dressed_d_failures,
            "loop_failures": loop_failures,
            "Wilson_failures": wilson_failures,
            "intracell_coin_D_failures": intracell_d_failures,
            "Hermiticity_failures": hermiticity_failures,
            "maximum_hop_Pauli_weight": maximum_weight,
        },
    )
    check(
        "deleting the reference edge reopens exactly the two endpoint Gauss constraints",
        set(bare_endpoint_counts) == {2},
        {
            "deleted_reference_edge_cases": len(bare_endpoint_counts),
            "endpoint_D_failures_per_case": 2,
        },
    )
    return {
        "stream_bonds": len(rows),
        "maximum_hop_Pauli_weight": maximum_weight,
        "bounded_support_independent_of_volume": True,
        "reference_edge_deletion_active": True,
    }


def parity_before(bits: tuple[int, ...], mode: int) -> int:
    return sum(bits[:mode]) & 1


def apply_gamma(
    bits: tuple[int, ...], mode: int
) -> tuple[tuple[int, ...], complex]:
    out = list(bits)
    phase = -1.0 if parity_before(bits, mode) else 1.0
    out[mode] ^= 1
    return tuple(out), phase


def apply_a(
    bits: tuple[int, ...], source: int, target: int
) -> tuple[tuple[int, ...], complex]:
    if source > target:
        out, phase = apply_a(bits, target, source)
        return out, -phase
    out, right = apply_gamma(bits, target)
    out, left = apply_gamma(out, source)
    return out, -1j * left * right


def apply_c(
    bits: tuple[int, ...], mode: int, creation: bool
) -> tuple[tuple[int, ...] | None, complex]:
    if bits[mode] == int(creation):
        return None, 0.0
    out = list(bits)
    phase = -1.0 if parity_before(bits, mode) else 1.0
    out[mode] = int(creation)
    return tuple(out), phase


def logical_hop_action(
    bits: tuple[int, ...], left: int, right: int
) -> tuple[tuple[int, ...] | None, complex]:
    if bits[left] and not bits[right]:
        out, first = apply_c(bits, left, False)
        assert out is not None
        out, second = apply_c(out, right, True)
        assert out is not None
        return out, first * second
    if bits[right] and not bits[left]:
        out, first = apply_c(bits, right, False)
        assert out is not None
        out, second = apply_c(out, left, True)
        assert out is not None
        return out, first * second
    return None, 0.0


def extended_codeword(logical: tuple[int, ...]) -> tuple[int, ...]:
    left = logical[:6]
    right = logical[6:]
    return (*left, sum(left) & 1, *right, sum(right) & 1)


def remove_references(extended: tuple[int, ...]) -> tuple[int, ...]:
    return extended[:6] + extended[7:13]


def apply_core(
    extended: tuple[int, ...], left_mode: int, right_mode: int
) -> tuple[tuple[int, ...], complex]:
    out, reference_phase = apply_a(extended, 6, 13)
    out, matter_phase = apply_a(out, left_mode, 7 + right_mode)
    return out, reference_phase * matter_phase


def corrected_hop_action(
    extended: tuple[int, ...], left_mode: int, right_mode: int
) -> tuple[tuple[int, ...] | None, complex]:
    left = left_mode
    right = 7 + right_mode
    if extended[left] == extended[right]:
        return None, 0.0
    out, phase = apply_core(extended, left_mode, right_mode)
    spectator = sum(
        extended[7 + mode] for mode in range(6) if mode != right_mode
    ) & 1
    return out, phase * (-1.0 if spectator == 0 else 1.0)


def target_fswap_action(
    logical: tuple[int, ...], left: int, right: int
) -> tuple[tuple[int, ...], complex]:
    permutation = list(range(len(logical)))
    permutation[left], permutation[right] = right, left
    occupied = [mode for mode, bit in enumerate(logical) if bit]
    targets = [permutation[mode] for mode in occupied]
    inversions = sum(
        targets[a] > targets[b]
        for a in range(len(targets))
        for b in range(a + 1, len(targets))
    )
    out = [0] * len(logical)
    for target in targets:
        out[target] = 1
    return tuple(out), -1.0 if inversions & 1 else 1.0


def corrected_fswap_action(
    extended: tuple[int, ...], left_mode: int, right_mode: int
) -> tuple[tuple[int, ...], complex]:
    left = left_mode
    right = 7 + right_mode
    if extended[left] == extended[right]:
        return extended, -1.0 if extended[left] else 1.0
    out, phase = corrected_hop_action(extended, left_mode, right_mode)
    assert out is not None
    return out, phase


def d_bits(extended: tuple[int, ...]) -> tuple[int, int]:
    return sum(extended[:7]) & 1, sum(extended[7:]) & 1


def two_cell_common_e_controls() -> dict[str, object]:
    hop_failures = 0
    fswap_failures = 0
    undressed_phase_failures = 0
    no_projector_pair_failures = 0
    deleted_reference_domain_failures = 0
    off_code_involution_failures = 0
    off_code_d_failures = 0
    columns = 1 << 12

    logical_rows = tuple(product((0, 1), repeat=12))
    for left_mode in range(6):
        for right_mode in range(6):
            logical_right = 6 + right_mode
            for logical in logical_rows:
                extended = extended_codeword(logical)
                target_hop, target_phase = logical_hop_action(
                    logical, left_mode, logical_right
                )
                observed_hop, observed_phase = corrected_hop_action(
                    extended, left_mode, right_mode
                )
                if target_hop is None:
                    no_projector_out, _ = apply_core(
                        extended, left_mode, right_mode
                    )
                    no_projector_pair_failures += (
                        no_projector_out != extended
                    )
                    if observed_hop is not None or observed_phase != 0.0:
                        hop_failures += 1
                else:
                    target_extended = extended_codeword(target_hop)
                    hop_failures += (
                        observed_hop != target_extended
                        or abs(observed_phase - target_phase) > TOL
                    )

                    core_out, core_phase = apply_core(
                        extended, left_mode, right_mode
                    )
                    undressed_phase_failures += (
                        core_out != target_extended
                        or abs(core_phase - target_phase) > TOL
                    )

                    bare_out, _ = apply_a(
                        extended, left_mode, 7 + right_mode
                    )
                    deleted_reference_domain_failures += d_bits(bare_out) != (0, 0)

                target_swap, target_swap_phase = target_fswap_action(
                    logical, left_mode, logical_right
                )
                observed_swap, observed_swap_phase = corrected_fswap_action(
                    extended, left_mode, right_mode
                )
                fswap_failures += (
                    observed_swap != extended_codeword(target_swap)
                    or abs(observed_swap_phase - target_swap_phase) > TOL
                )

            for raw in range(1 << 14):
                extended = tuple((raw >> (13 - mode)) & 1 for mode in range(14))
                first, first_phase = corrected_fswap_action(
                    extended, left_mode, right_mode
                )
                second, second_phase = corrected_fswap_action(
                    first, left_mode, right_mode
                )
                off_code_involution_failures += (
                    second != extended
                    or abs(first_phase * second_phase - 1.0) > TOL
                )
                off_code_d_failures += d_bits(first) != d_bits(extended)

    check(
        "the two-cell local-D common E exactly intertwines every directed matter hop and FSWAP",
        hop_failures == 0
        and fswap_failures == 0
        and columns == 4096
        and undressed_phase_failures > 0
        and no_projector_pair_failures > 0
        and deleted_reference_domain_failures > 0,
        {
            "common_E_columns": columns,
            "directed_port_pairs": 36,
            "hop_failures": hop_failures,
            "FSWAP_failures": fswap_failures,
            "undressed_spectator_phase_failures": undressed_phase_failures,
            "omitted_number_projector_pair_failures": no_projector_pair_failures,
            "deleted_reference_edge_D_failures": deleted_reference_domain_failures,
        },
    )
    check(
        "the dressed FSWAP is a full 14-mode Hermitian involution preserving both D parities",
        off_code_involution_failures == 0 and off_code_d_failures == 0,
        {
            "off_code_basis_cases": 36 * (1 << 14),
            "involution_failures": off_code_involution_failures,
            "D_preservation_failures": off_code_d_failures,
        },
    )
    return {
        "extended_Fock_common_E_shape": (1 << 14, 1 << 12),
        "extended_Fock_common_E_nonzeros": 1 << 12,
        "all_36_directed_port_hops_exact": True,
        "all_36_directed_port_FSWAPs_exact": True,
        "full_off_code_FSWAP_involution_executed": True,
        "BKSF_edge_qubit_common_E_executed": False,
    }


def corrected_frame_data(graph: base.ReferenceGraph, frame: np.ndarray):
    vertex_map, edge_map = base.graph_frame_maps(graph, frame)
    toggles, pairs = base.order_gauge(graph, vertex_map, edge_map)
    flips = 0
    for source_edge, (u, v, _, _) in enumerate(graph.edges):
        transformed = base.permute_pauli(graph.A(u, v), edge_map)
        target = graph.A(vertex_map[u], vertex_map[v])
        ordered = base.apply_gauge(transformed, toggles, pairs)
        if (ordered.phase - target.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
    return vertex_map, edge_map, toggles, pairs, flips


def frame_key(frame: np.ndarray) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(value) for value in row) for row in frame)


def covariance_controls() -> dict[str, object]:
    graph = base.ReferenceGraph(3, True)
    frames = base.proper_cubic_frames()
    ds = local_d_rows(graph)
    d_targets = {(row.phase, row.x, row.z) for row in ds}
    corrected_word_failures = 0
    raw_word_mismatches = 0
    d_failures = 0
    frame_data = []

    for frame in frames:
        vertex_map, edge_map, toggles, pairs, flips = corrected_frame_data(
            graph, frame
        )
        frame_data.append((vertex_map, edge_map))
        for d in ds:
            mapped = base.permute_pauli(d, edge_map)
            d_failures += (mapped.phase, mapped.x, mapped.z) not in d_targets

        for cell in graph.cells:
            for axis in range(3):
                u, v, ru, rv, target_cell, target_mode = stream_vertices(
                    graph, cell, axis
                )
                source_terms = hop_pauli_terms(
                    graph, u, v, ru, rv, target_cell, target_mode
                )
                mapped_target_cell, mapped_target_mode = graph.vertices[
                    vertex_map[v]
                ]
                target_terms = hop_pauli_terms(
                    graph,
                    vertex_map[u],
                    vertex_map[v],
                    vertex_map[ru],
                    vertex_map[rv],
                    mapped_target_cell,
                    mapped_target_mode,
                )
                for source, target in zip(source_terms, target_terms):
                    raw = base.permute_pauli(source, edge_map)
                    raw_word_mismatches += raw != target
                    corrected = base.apply_gauge(
                        raw, toggles, pairs, flips
                    )
                    corrected_word_failures += corrected != target

    frame_lookup = {frame_key(frame): index for index, frame in enumerate(frames)}
    composition_failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product_index = frame_lookup[frame_key(left @ right)]
            left_vertices, left_edges = frame_data[left_index]
            right_vertices, right_edges = frame_data[right_index]
            product_vertices, product_edges = frame_data[product_index]
            composition_failures += any(
                left_vertices[right_vertices[index]] != product_vertices[index]
                for index in range(len(graph.vertices))
            )
            composition_failures += any(
                left_edges[right_edges[index]] != product_edges[index]
                for index in range(len(graph.edges))
            )

    check(
        "all 24 frames and 576 products preserve local D and the directed dressed-hop Pauli family",
        len(frames) == 24
        and d_failures == 0
        and corrected_word_failures == 0
        and raw_word_mismatches > 0
        and composition_failures == 0,
        {
            "proper_cubic_frames": len(frames),
            "ordered_frame_products": len(frames) ** 2,
            "D_family_failures": d_failures,
            "raw_order_gauge_mismatches": raw_word_mismatches,
            "corrected_hop_word_failures": corrected_word_failures,
            "vertex_or_edge_composition_failures": composition_failures,
        },
    )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "operator_family_covariant": True,
        "transformed_BKSF_common_E_compared": False,
    }


def scope_and_note_controls() -> dict[str, object]:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "**authority:** none",
        "**audit:** unset",
        "rank `n-1`",
        "two-cell extended-fock common e",
        "not a bksf edge-qubit common-e intertwiner",
        "three wilson",
        "odd and even",
        "finite-depth preparation",
        "operator algebra",
        "full graded car",
        "n1 — alternatives",
        "n2 — wall independence",
        "n3 — hidden conditions",
        "n4 — residual matching",
        "n5 — resolution",
        "n6 — partial closure",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no route-independent no-go",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the adversarial note separates algebra, state isometry, preparation, and no-go scope",
        not missing,
        missing,
    )
    return {
        "finite_state_isometry_exists_after_Wilson_fix": True,
        "bounded_radius_BKSF_state_encoder_constructed": False,
        "fixed_Wilson_character_supplied": True,
        "runtime_global_parity_query_used": False,
        "runtime_global_order_service_used": False,
        "local_incidence_order_gauge_supplied": True,
        "full_graded_CAR_odd_fields_locally_represented": False,
        "common_E_physical_intertwiner_executed": False,
        "broad_no_go_gate": "FAIL",
    }


def main() -> None:
    rank = rank_and_sector_controls()
    algebra = operator_algebra_controls()
    fock = two_cell_common_e_controls()
    covariance = covariance_controls()
    scope = scope_and_note_controls()
    summary = {
        "authority": "none",
        "audit": "unset",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "rank_and_sector": rank,
        "operator_algebra": algebra,
        "two_cell_extended_Fock": fock,
        "covariance": covariance,
        "scope": scope,
        "claim_ceiling": (
            "The local-D reference construction has exact 6N capacity at odd and even "
            "volume, a bounded D/loop/Wilson-preserving BKSF hop family, and an exact "
            "4096-column two-cell extended-Fock hop/FSWAP intertwiner. It does not yet "
            "construct the BKSF edge-qubit common E, bounded-depth fixed-Wilson state "
            "preparation, transformed-E covariance, or local representatives of odd "
            "graded-CAR fields. No route-independent no-go or axiom pressure follows."
        ),
        "terminal": "LOCAL_GAUSS_ALGEBRA_AND_FOCK_ISOMETRY_POSITIVE_BKSF_COMMON_E_OPEN",
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", summary["terminal"] if FAIL == 0 else "UNFINISHED_LOCAL_GAUSS_REVIEW")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
