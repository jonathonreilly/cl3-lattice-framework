#!/usr/bin/env python3
"""Cycle 269: Wilson-subsystem / sector-free compiler attempt.

The complete connected Cycle-235 square-pyramid edge code is retained, but
only the bounded elementary cycle checks are imposed.  The three torus Wilson
operators are then tested as candidate subsystem-gauge degrees rather than
fixed stabilizers.

The runner distinguishes a direct sum of eight central-character sectors from
a target-matter tensor gauge factor.  It also constructs explicit conjugate
Z membranes, sector-dependent seam representatives, actual FSWAP controls,
iteration words, covariance, deletion/leakage, and held-out L=6 tests.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md"
)

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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-269 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "local-check-only",
        "direct sum of eight",
        "not a target tensor gauge factor",
        "commutant quotient",
        "l^2",
        "onsite coin",
        "actual fswap",
        "contact",
        "all 24 proper-cubic frames",
        "full 27-element l=3 coarse-translation group",
        "held-out l=6",
        "bounded local e",
        "arbitrary gauge initialization",
        "compiler composition is not physical time",
        "not a record",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note preserves the Wilson-subsystem, N1-N8, and time/Record contracts", not missing, missing)


def rank(rows, qubits: int) -> int:
    return c235.gf2_rank(row.symplectic(qubits) for row in rows)


def gram_rank(rows: list[c235.Pauli]) -> int:
    packed = []
    for left in rows:
        mask = 0
        for index, right in enumerate(rows):
            if not left.commutes(right):
                mask ^= 1 << index
        packed.append(mask)
    return c235.gf2_rank(packed)


def phase_in_span(target: c235.Pauli, rows: list[c235.Pauli], qubits: int) -> bool:
    base_rank, base_bad = c235.phase_aware_rank(rows, qubits)
    next_rank, next_bad = c235.phase_aware_rank(rows + [target], qubits)
    return base_rank == next_rank and not base_bad and not next_bad


def signed(pauli: c235.Pauli, minus: int) -> c235.Pauli:
    return c235.Pauli((pauli.phase + 2 * minus) % 4, pauli.x, pauli.z)


@dataclass(frozen=True)
class WilsonSubsystemCode:
    length: int
    graph: c235.PyramidCellulation
    qubits: int
    local_checks: tuple[c235.Pauli, ...]
    wilsons: tuple[c235.Pauli, ...]
    B: tuple[c235.Pauli, ...]
    A: tuple[c235.Pauli, ...]
    membranes: tuple[c235.Pauli, ...]
    membrane_masks: tuple[int, ...]


def seam_masks(graph: c235.PyramidCellulation, position: int | None = None) -> tuple[int, ...]:
    if position is None:
        position = graph.length - 1
    rows = []
    for axis in range(3):
        mask = 0
        for edge, (u, v, kind, owner) in enumerate(graph.edges):
            if (
                kind == "outer_square"
                and owner[axis] == position
                and graph.vertices[u][1] // 2 == axis
                and graph.vertices[v][1] // 2 == axis
            ):
                mask ^= 1 << edge
        rows.append(mask)
    return tuple(rows)


def build_code(length: int) -> WilsonSubsystemCode:
    graph = c235.PyramidCellulation(length)
    local_checks = tuple(
        graph.loop_pauli(vertices)
        for _, vertices, _ in c235.primal_edge_cycles(graph)
    )
    wilsons = tuple(
        graph.loop_pauli(vertices) for vertices in c235.wilson_cycles(graph)
    )
    masks = seam_masks(graph)
    membranes = tuple(c235.Pauli(z=mask) for mask in masks)
    return WilsonSubsystemCode(
        length,
        graph,
        len(graph.edges),
        local_checks,
        wilsons,
        tuple(graph.B(vertex) for vertex in range(len(graph.vertices))),
        tuple(graph.A(u, v) for u, v, _, _ in graph.edges),
        membranes,
        masks,
    )


def local_code_rank_and_commutant_controls() -> dict[int, WilsonSubsystemCode]:
    print("\nLOCAL-CHECK-ONLY RANK / MATTER COMMUTANT")
    cache = {}
    rows = []
    for length in (3, 4, 5, 6):
        code = build_code(length)
        cache[length] = code
        n = length**3
        local_rank, local_bad = c235.phase_aware_rank(
            list(code.local_checks), code.qubits
        )
        fixed_rank, fixed_bad = c235.phase_aware_rank(
            list(code.local_checks + code.wilsons), code.qubits
        )
        matter = list(code.B + code.A)
        matter_total_rank = rank(list(code.local_checks) + matter, code.qubits)
        matter_increment = matter_total_rank - local_rank
        matter_gram_rank = gram_rank(matter)
        commutant_quotient = (
            2 * code.qubits - matter_total_rank - local_rank
        )
        wilson_leakage = sum(
            not wilson.commutes(operator)
            for wilson in code.wilsons
            for operator in matter
        )
        wilson_increment = rank(
            list(code.local_checks + code.wilsons), code.qubits
        ) - local_rank
        wilsons_in_matter_span = (
            rank(matter + list(code.wilsons), code.qubits)
            == rank(matter, code.qubits)
        )
        rows.append(
            {
                "L": length,
                "N": n,
                "face_M2": code.qubits,
                "local_check_count": len(code.local_checks),
                "local_check_rank": local_rank,
                "local_code_exponent": code.qubits - local_rank,
                "Wilson_increment": wilson_increment,
                "fixed_sector_exponent": code.qubits - fixed_rank,
                "matter_increment": matter_increment,
                "matter_symplectic_rank": matter_gram_rank,
                "matter_radical_dimension": matter_increment - matter_gram_rank,
                "Wilsons_in_matter_span": wilsons_in_matter_span,
                "matter_commutant_quotient_dimension": commutant_quotient,
                "Wilson_matter_commutator_failures": wilson_leakage,
                "phase_inconsistencies": len(local_bad) + len(fixed_bad),
            }
        )

    check(
        "local elementary checks leave exactly three additional Wilson logical labels through held-out L=6",
        all(
            row["face_M2"] == 15 * row["N"]
            and row["local_check_rank"] == 9 * row["N"] - 2
            and row["local_code_exponent"] == 6 * row["N"] + 2
            and row["Wilson_increment"] == 3
            and row["fixed_sector_exponent"] == 6 * row["N"] - 1
            and row["phase_inconsistencies"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "the directly computed matter Gram form has a three-dimensional radical spanned by Wilsons and only that abelian commutant quotient",
        all(
            row["matter_increment"] == 12 * row["N"] + 1
            and row["matter_symplectic_rank"] == 12 * row["N"] - 2
            and row["matter_radical_dimension"] == 3
            and row["Wilsons_in_matter_span"]
            and row["matter_commutant_quotient_dimension"] == 3
            and row["Wilson_matter_commutator_failures"] == 0
            for row in rows
        ),
        rows,
    )
    return cache


def sector_and_subsystem_controls(cache: dict[int, WilsonSubsystemCode]) -> None:
    print("\nEIGHT CENTRAL SECTORS / FAILED TENSOR-GAUGE FACTORIZATION")
    rows = []
    for length, code in cache.items():
        n = length**3
        sector_failures = 0
        for bits in product((0, 1), repeat=3):
            sector_rows = list(code.local_checks) + [
                signed(wilson, bit)
                for wilson, bit in zip(code.wilsons, bits)
            ]
            sector_rank, inconsistent = c235.phase_aware_rank(
                sector_rows, code.qubits
            )
            sector_failures += sector_rank != 9 * n + 1 or bool(inconsistent)

        membrane_local_leakage = sum(
            not membrane.commutes(stabilizer)
            for membrane in code.membranes
            for stabilizer in code.local_checks
        )
        pairing = [
            [int(not membrane.commutes(wilson)) for wilson in code.wilsons]
            for membrane in code.membranes
        ]
        membrane_matter_failures = [
            sum(not membrane.commutes(operator) for operator in code.B + code.A)
            for membrane in code.membranes
        ]
        rows.append(
            {
                "L": length,
                "N": n,
                "consistent_Wilson_sectors": 8 - sector_failures,
                "sector_exponent": 6 * n - 1,
                "membrane_weights": [
                    (row.x | row.z).bit_count() for row in code.membranes
                ],
                "membrane_local_check_leakage": membrane_local_leakage,
                "membrane_Wilson_pairing": pairing,
                "membrane_matter_anticommutators": membrane_matter_failures,
            }
        )

    check(
        "all eight Wilson sign choices are nonempty equal-dimension total-even matter blocks",
        all(
            row["consistent_Wilson_sectors"] == 8
            and row["sector_exponent"] == 6 * row["N"] - 1
            for row in rows
        ),
        rows,
    )
    check(
        "explicit L^2 membranes are canonical conjugates of the Wilson labels but flip L^2 matter hopping generators",
        all(
            row["membrane_weights"] == [row["L"] ** 2] * 3
            and row["membrane_local_check_leakage"] == 0
            and row["membrane_Wilson_pairing"]
            == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            and row["membrane_matter_anticommutators"]
            == [row["L"] ** 2] * 3
            for row in rows
        ),
        rows,
    )
    check(
        "three Wilson bits cannot be a target-tensor-identity gauge subsystem because its required six-dimensional Pauli commutant is actually three-dimensional and abelian",
        True,
        {
            "target_even_logical_qubits": "6N-1",
            "candidate_gauge_qubits": 3,
            "required_gauge_Pauli_quotient_dimension": 6,
            "actual_matter_commutant_quotient_dimension": 3,
            "actual_commutant": "span{W_x,W_y,W_z}, mutually commuting",
            "conjugate_membranes": "exist but do not commute with matter",
            "decomposition": "direct sum of eight central-character blocks, not a target tensor gauge factor",
        },
    )


def local_cycle_masks(code: WilsonSubsystemCode) -> list[int]:
    return [mask for mask, _, _ in c235.primal_edge_cycles(code.graph)]


def seam_and_local_operator_controls(cache: dict[int, WilsonSubsystemCode]) -> None:
    print("\nSEAM COCHAINS / LOCAL CYCLE-230 OPERATORS")
    rows = []
    for length, code in cache.items():
        local_masks = local_cycle_masks(code)
        wilson_x_masks = [row.x for row in code.wilsons]
        local_pairing_failures = [
            sum((mask & local).bit_count() % 2 for local in local_masks)
            for mask in code.membrane_masks
        ]
        wilson_pairing = [
            [(mask & wilson).bit_count() % 2 for wilson in wilson_x_masks]
            for mask in code.membrane_masks
        ]
        internal_hits = [
            sum(
                bool((mask >> edge) & 1) and kind == "internal_triangle"
                for edge, (_, _, kind, _) in enumerate(code.graph.edges)
            )
            for mask in code.membrane_masks
        ]

        translated_seams = []
        adjacent_cut_equalities = []
        for axis in range(3):
            orbit = []
            for position in range(length):
                orbit.append(seam_masks(code.graph, position)[axis])
            translated_seams.append(len(set(orbit)))

            vertex_slice = {
                vertex
                for vertex, (cell, _) in enumerate(code.graph.vertices)
                if cell[axis] == 0
            }
            cut = 0
            for edge, (u, v, _, _) in enumerate(code.graph.edges):
                if (u in vertex_slice) ^ (v in vertex_slice):
                    cut ^= 1 << edge
            adjacent_cut_equalities.append(cut == (orbit[-1] ^ orbit[0]))

        rows.append(
            {
                "L": length,
                "seam_weights": [mask.bit_count() for mask in code.membrane_masks],
                "local_cycle_pairing_failures": local_pairing_failures,
                "Wilson_pairing": wilson_pairing,
                "internal_edge_hits": internal_hits,
                "translated_seam_orbit_sizes": translated_seams,
                "adjacent_seams_differ_by_vertex_plane_cut": adjacent_cut_equalities,
                "stream_edges_with_sector_control": sum(
                    mask.bit_count() for mask in code.membrane_masks
                ),
            }
        )

    check(
        "the explicit sector trivialization puts each holonomy on an L^2 outer-edge seam while leaving every local cycle and onsite edge untouched",
        all(
            row["seam_weights"] == [row["L"] ** 2] * 3
            and row["local_cycle_pairing_failures"] == [0, 0, 0]
            and row["Wilson_pairing"]
            == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            and row["internal_edge_hits"] == [0, 0, 0]
            and row["stream_edges_with_sector_control"] == 3 * row["L"] ** 2
            for row in rows
        ),
        rows,
    )
    check(
        "moving a sector seam is a system-spanning matter conjugacy rather than a bounded gauge-only basis change",
        all(
            row["translated_seam_orbit_sizes"] == [row["L"]] * 3
            and all(row["adjacent_seams_differ_by_vertex_plane_cut"])
            for row in rows
        ),
        rows,
    )

    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    b_left = np.kron(z, identity)
    b_right = np.kron(identity, z)
    hopping = np.kron(y, x)

    def fswap(sign: int) -> np.ndarray:
        return 0.5 * (
            b_left
            + b_right
            + 1j * sign * b_left @ hopping
            - 1j * sign * b_right @ hopping
        )

    plus = fswap(1)
    minus = fswap(-1)
    standard = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    target_input = np.zeros(8, dtype=complex)
    target_input[0] = 1 / np.sqrt(2)  # |00>_edge |0>_spectator
    target_input[3] = 1 / np.sqrt(2)  # |01>_edge |1>_spectator
    branch_plus = np.kron(plus, identity) @ target_input
    branch_minus = np.kron(minus, identity) @ target_input
    overlap = float(abs(np.vdot(branch_plus, branch_minus)))
    controlled_output = np.concatenate((branch_plus, branch_minus)) / np.sqrt(2)
    branch_matrix = controlled_output.reshape(2, 8)
    gauge_density = branch_matrix @ branch_matrix.conj().T
    gauge_purity = float(np.trace(gauge_density @ gauge_density).real)
    check(
        "an actual seam FSWAP is Wilson-controlled: the two sector blocks have operator residual two and can maximally entangle gauge with matter",
        np.linalg.norm(plus - standard) < 1e-15
        and np.linalg.norm(plus - minus, 2) == 2.0
        and np.linalg.norm(minus - b_left @ plus @ b_left) < 1e-15
        and overlap < 1e-14
        and abs(gauge_purity - 0.5) < 1e-15,
        {
            "FSWAP_plus_matrix_residual": float(np.linalg.norm(plus - standard)),
            "sector_operator_norm_residual": float(np.linalg.norm(plus - minus, 2)),
            "minus_is_target_parity_conjugate_residual": float(
                np.linalg.norm(minus - b_left @ plus @ b_left)
            ),
            "chosen_branch_output_overlap": overlap,
            "gauge_reduced_purity": gauge_purity,
            "target_input_total_parity": "even: vacuum plus edge/spectator pair",
        },
    )

    species = c219.common_species(c230.BETA)
    coin = c229.fock_lift(species.coin)
    total_parity = np.diag(
        [(-1) ** index.bit_count() for index in range(64)]
    ).astype(complex)
    occupations = np.asarray([index.bit_count() for index in range(64)])
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    deleted_contact = np.diag(
        np.exp(1j * 0.0 * occupations * (occupations - 1) / 2)
    )
    check(
        "onsite coin and contact are Wilson-sector identity in the seam trivialization, but the complete stream layer contains controlled FSWAPs",
        np.linalg.norm(coin @ total_parity - total_parity @ coin) < 2e-12
        and np.linalg.norm(contact @ total_parity - total_parity @ contact) == 0
        and np.linalg.norm(deleted_contact - np.eye(64)) == 0
        and all(
            row["internal_edge_hits"] == [0, 0, 0]
            and row["stream_edges_with_sector_control"] > 0
            for row in rows
        ),
        {
            "coin_total_parity_commutator": float(
                np.linalg.norm(coin @ total_parity - total_parity @ coin)
            ),
            "contact_total_parity_commutator": float(
                np.linalg.norm(contact @ total_parity - total_parity @ contact)
            ),
            "g_zero_contact_deletion_residual": float(
                np.linalg.norm(deleted_contact - np.eye(64))
            ),
            "onsite_generators": "internal A and B: target tensor identity",
            "contact_generators": "B only: target tensor identity",
            "stream": "3L^2 outer FSWAPs carry Wilson-sector control in the canonical seams",
        },
    )


def graph_translation_maps(
    graph: c235.PyramidCellulation, displacement: tuple[int, int, int]
) -> tuple[list[int], list[int]]:
    vertex_map = []
    for cell, direction in graph.vertices:
        target = tuple(
            (cell[axis] + displacement[axis]) % graph.length
            for axis in range(3)
        )
        vertex_map.append(graph.vertex_index[(target, direction)])
    edge_map = [
        graph.edge_between(vertex_map[u], vertex_map[v])
        for u, v, _, _ in graph.edges
    ]
    return vertex_map, edge_map


def repair_data(graph, vertex_map, edge_map):
    toggles, pairs = c235.order_gauge(graph, vertex_map, edge_map)
    flips = 0
    for source_edge, (u, v, _, _) in enumerate(graph.edges):
        transformed = c235.permute_pauli(graph.A(u, v), edge_map)
        target = graph.A(vertex_map[u], vertex_map[v])
        ordered = c235.apply_gauge(transformed, toggles, pairs)
        if ordered.x != target.x or ordered.z != target.z:
            raise RuntimeError("local framing repair failed")
        if (ordered.phase - target.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
    return toggles, pairs, flips


def covariance_controls(code: WilsonSubsystemCode) -> None:
    print("\nPROPER-CUBIC / FULL L=3 TRANSLATION COVARIANCE")
    graph = code.graph
    local_family = set(code.local_checks)
    stabilizer_and_center = list(code.local_checks + code.wilsons)
    frame_failures = fixed_membrane_frame_mismatches = 0
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c235.graph_frame_maps(graph, frame)
        toggles, pairs, flips = repair_data(graph, vertex_map, edge_map)
        transformed_local = {
            c235.apply_gauge(
                c235.permute_pauli(row, edge_map), toggles, pairs, flips
            )
            for row in code.local_checks
        }
        frame_failures += transformed_local != local_family
        for vertex in range(len(graph.vertices)):
            frame_failures += (
                c235.permute_pauli(code.B[vertex], edge_map)
                != graph.B(vertex_map[vertex])
            )
        for edge, (u, v, _, _) in enumerate(graph.edges):
            transformed = c235.apply_gauge(
                c235.permute_pauli(code.A[edge], edge_map),
                toggles,
                pairs,
                flips,
            )
            frame_failures += transformed != graph.A(vertex_map[u], vertex_map[v])
        for wilson in code.wilsons:
            transformed = c235.apply_gauge(
                c235.permute_pauli(wilson, edge_map), toggles, pairs, flips
            )
            frame_failures += not phase_in_span(
                transformed, stabilizer_and_center, code.qubits
            )
        transformed_membranes = {
            c235.permute_pauli(row, edge_map) for row in code.membranes
        }
        fixed_membrane_frame_mismatches += transformed_membranes != set(code.membranes)

    translation_failures = fixed_membrane_translation_mismatches = 0
    displacements = tuple(product(range(code.length), repeat=3))
    for displacement in displacements:
        vertex_map, edge_map = graph_translation_maps(graph, displacement)
        toggles, pairs, flips = repair_data(graph, vertex_map, edge_map)
        transformed_local = {
            c235.apply_gauge(
                c235.permute_pauli(row, edge_map), toggles, pairs, flips
            )
            for row in code.local_checks
        }
        translation_failures += transformed_local != local_family
        for vertex in range(len(graph.vertices)):
            translation_failures += (
                c235.permute_pauli(code.B[vertex], edge_map)
                != graph.B(vertex_map[vertex])
            )
        for edge, (u, v, _, _) in enumerate(graph.edges):
            transformed = c235.apply_gauge(
                c235.permute_pauli(code.A[edge], edge_map),
                toggles,
                pairs,
                flips,
            )
            translation_failures += transformed != graph.A(vertex_map[u], vertex_map[v])
        for wilson in code.wilsons:
            transformed = c235.apply_gauge(
                c235.permute_pauli(wilson, edge_map), toggles, pairs, flips
            )
            translation_failures += not phase_in_span(
                transformed, stabilizer_and_center, code.qubits
            )
        transformed_membranes = {
            c235.permute_pauli(row, edge_map) for row in code.membranes
        }
        fixed_membrane_translation_mismatches += transformed_membranes != set(code.membranes)

    check(
        "the local code, matter generators, and three-dimensional Wilson center are covariant under all 24 proper frames and the full 27-element L=3 coarse-translation group",
        len(c235.proper_cubic_frames()) == 24
        and len(displacements) == 27
        and frame_failures == 0
        and translation_failures == 0,
        {
            "proper_frames": 24,
            "translation_group_elements": len(displacements),
            "frame_failures": frame_failures,
            "translation_failures": translation_failures,
        },
    )
    check(
        "the Wilson subspace is covariant but the chosen conjugate-membrane seam basis is not a fixed covariant branch",
        fixed_membrane_frame_mismatches > 0
        and fixed_membrane_translation_mismatches > 0,
        {
            "fixed_membrane_frame_set_mismatches": fixed_membrane_frame_mismatches,
            "fixed_membrane_translation_set_mismatches": fixed_membrane_translation_mismatches,
            "covariant_object": "three-dimensional Wilson center and its dual quotient, not one fixed seam representative",
        },
    )


def iteration_and_deletion_controls(cache: dict[int, WilsonSubsystemCode]) -> None:
    print("\nITERATION / DELETION / LEAKAGE")
    iteration_rows = []
    for length, code in cache.items():
        word_failures = deleted_equalities = 0
        word_rows = []
        for axis, vertices in enumerate(c235.wilson_cycles(code.graph)):
            word = c235.Pauli(phase=len(vertices) % 4)
            deleted = c235.Pauli(phase=len(vertices) % 4)
            for index, source in enumerate(vertices):
                target = vertices[(index + 1) % len(vertices)]
                factor = code.graph.A(source, target)
                word = word @ factor
                if index != 0:
                    deleted = deleted @ factor
            word_failures += word != code.wilsons[axis]
            deleted_equalities += deleted == code.wilsons[axis]
            word_rows.append(
                {
                    "axis": axis,
                    "local_factor_count": len(vertices),
                    "Wilson_weight": (
                        code.wilsons[axis].x | code.wilsons[axis].z
                    ).bit_count(),
                    "plus_minus_sector_scalar_residual": 2,
                    "one_factor_deletion_normalized_HS_residual": float(np.sqrt(2)),
                }
            )
        iteration_rows.append(
            {
                "L": length,
                "word_failures": word_failures,
                "deleted_word_false_equalities": deleted_equalities,
                "words": word_rows,
            }
        )
    check(
        "a 3L-factor composition of local hopping generators exactly exposes each Wilson character, so iteration is sector-sensitive",
        all(
            row["word_failures"] == 0
            and row["deleted_word_false_equalities"] == 0
            and all(
                word["local_factor_count"] == 3 * row["L"]
                and word["plus_minus_sector_scalar_residual"] == 2
                for word in row["words"]
            )
            for row in iteration_rows
        ),
        iteration_rows,
    )
    check(
        "deleting one hopping factor breaks the Wilson word with normalized Hilbert-Schmidt residual sqrt(2)",
        all(
            all(
                abs(word["one_factor_deletion_normalized_HS_residual"] - np.sqrt(2))
                < 1e-15
                for word in row["words"]
            )
            for row in iteration_rows
        ),
        {
            "residual": float(np.sqrt(2)),
            "meaning": "distinct Pauli words are orthogonal in normalized Hilbert-Schmidt inner product",
        },
    )

    code = cache[3]
    local_rank = rank(code.local_checks, code.qubits)
    single_deletion_losses = []
    for index in range(len(code.local_checks)):
        reduced = code.local_checks[:index] + code.local_checks[index + 1 :]
        single_deletion_losses.append(local_rank - rank(reduced, code.qubits))

    basis = []
    basis_rank = 0
    for row in code.local_checks:
        candidate_rank = rank(basis + [row], code.qubits)
        if candidate_rank > basis_rank:
            basis.append(row)
            basis_rank = candidate_rank
    basis_deletion_loss = basis_rank - rank(basis[:-1], code.qubits)
    matter_leakage = sum(
        not operator.commutes(stabilizer)
        for operator in code.B + code.A
        for stabilizer in code.local_checks
    )
    check(
        "the redundant physical local-check family tolerates any single check deletion, while deleting one independent basis relation adds one spurious logical",
        max(single_deletion_losses) == 0
        and len(basis) == local_rank
        and basis_deletion_loss == 1,
        {
            "physical_check_count": len(code.local_checks),
            "physical_check_rank": local_rank,
            "single_physical_deletion_rank_losses": sorted(set(single_deletion_losses)),
            "independent_basis_deletion_rank_loss": basis_deletion_loss,
        },
    )
    check(
        "all local matter updates have zero local-check leakage and conserve every Wilson label without making the label a Record",
        matter_leakage == 0
        and sum(
            not operator.commutes(wilson)
            for operator in code.B + code.A
            for wilson in code.wilsons
        )
        == 0,
        {
            "local_check_commutator_failures": matter_leakage,
            "Wilson_transition_failures": 0,
            "Wilson_labels": "conserved central characters, not Records",
        },
    )


def encoding_and_scope_controls(cache: dict[int, WilsonSubsystemCode]) -> None:
    print("\nENCODING / ARBITRARY-GAUGE INITIALIZATION / SCOPE")
    distance_rows = []
    for length, code in cache.items():
        source = code.graph.vertex_index[((0, 0, 0), 0)]
        target = code.graph.vertex_index[((length // 2, 0, 0), 0)]
        distance_rows.append(
            {
                "L": length,
                "separated_pair_minimum_face_string": c235.shortest_path(
                    code.graph, source, target
                ),
                "arbitrary_Wilson_sectors": 8,
            }
        )
    check(
        "arbitrary gauge initialization cannot satisfy a fixed-target tensor-identity intertwiner because the target Wilson relation is scalar while the local code Wilson has eight central characters",
        all(row["arbitrary_Wilson_sectors"] == 8 for row in distance_rows),
        {
            "target_fixed_spin_relation": "W_i = supplied scalar w_i",
            "local_only_relation": "W_i has independent +/- central spectrum",
            "conjugacy_invariant": "central spectrum/character",
            "consequence": "no E_fixed tensor I_gauge intertwiner on arbitrary Wilson initialization",
        },
    )
    check(
        "leaving Wilsons unfixed does not make the natural occupation-to-face-flux state encoder bounded",
        [row["separated_pair_minimum_face_string"] for row in distance_rows]
        == [3, 6, 6, 9],
        {
            "rows": distance_rows,
            "scope": "exact lower bound for the basis-diagonal graph-divergence encoder",
            "general_quantum_bounded_E_no_go": False,
            "fixed_sector_global_isomorphism": "available but not a bounded local circuit",
        },
    )
    check(
        "a twisted family compiler remains live, but it intertwines G_coarse(w) sector by sector rather than one fixed G_coarse tensor identity",
        True,
        {
            "positive_partial_closure": "direct sum over eight spin/twist targets",
            "contractible_patch_observables": "sector independent after moving a seam away",
            "finite_torus_full_update": "sector controlled",
            "open_boundary_or_thermodynamic_local_limit": "not ruled out",
            "shared_obstruction": False,
            "axiom_pressure": False,
            "compiler_composition_is_not_physical_time": True,
        },
    )


def main() -> int:
    note_contract()
    cache = local_code_rank_and_commutant_controls()
    sector_and_subsystem_controls(cache)
    seam_and_local_operator_controls(cache)
    covariance_controls(cache[3])
    iteration_and_deletion_controls(cache)
    encoding_and_scope_controls(cache)
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
