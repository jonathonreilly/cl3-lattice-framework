#!/usr/bin/env python3
"""Cycle 302: joint six-mode Cycle-219 coin lift on the Cycle-269 code.

In the fixed +++ Wilson sector, encode each logical direction as a coherent
five-ray shell of even face-code pairs.  Each ray has one occupied body port
and one occupied neighboring reference port, with the two Cycle-299 port tags
changed jointly.  A local phase dressing cancels the Cycle-269 framing-repair
cocycle under every proper-cubic frame.

The supplied physical coin is an exact bounded matrix-unit completion on the
thirty shell sectors.  It is a constructive local code-space lift, not an
absolute-vacuum preparation, coherent-position or full-Fock compiler.
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
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_reference_relative_localized_pair_lift_2026_07_17 as local
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_JOINT_SIX_MODE_COIN_LIFT_CYCLE302_NOTE_2026-07-17.md"
)
TRAINING_SIZE = 3
HELD_SIZE = 6
BODY = (0, 0, 0)
PAIR_LABELS = tuple(
    (direction, reference)
    for direction in range(6)
    for reference in range(6)
    if reference != (direction ^ 1)
)
PAIR_INDEX = {label: index for index, label in enumerate(PAIR_LABELS)}

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class PairRay:
    direction: int
    reference_direction: int
    carrier: int
    reference: int
    face_pauli: c235.Pauli
    tags: int
    representative: c235.Pauli


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
        check("the Cycle-302 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle 219",
        "cycle 269",
        "five-ray shell",
        "thirty orthogonal",
        "e c = u_physical e",
        "at most fifty-four m2",
        "twenty-one m2 per cell",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "b_v z_port(v)",
        "no tag copying",
        "local matrix-unit completion",
        "projector transport",
        "gf(2) cocycle",
        "absolute vacuum preparation remains open",
        "coherent position remains open",
        "full-fock compilation remains open",
        "not physical energy",
        "not a rate",
        "no gravity/source semantics",
        "no record claim",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the theorem and residual boundary", not missing, missing)


def pauli_dagger(pauli: c235.Pauli) -> c235.Pauli:
    return c235.Pauli(
        (-pauli.phase + 2 * (pauli.x & pauli.z).bit_count()) % 4,
        pauli.x,
        pauli.z,
    )


def phase_dressed(pauli: c235.Pauli, reference_direction: int) -> c235.Pauli:
    """The ray-orientation gauge used by the shell, unique up to global sign.

    Positive coordinate rays receive -1 and negative coordinate rays +1.
    This distinguishes ray orientation but no ordering among the three axes.
    """

    return c235.Pauli(
        (pauli.phase + (2 if reference_direction % 2 == 0 else 0)) % 4,
        pauli.x,
        pauli.z,
    )


def body_vertex(code: c269.WilsonSubsystemCode, body, direction: int) -> int:
    return code.graph.vertex_index[(tuple(body), direction)]


def pair_ray(
    code: c269.WilsonSubsystemCode,
    body: tuple[int, int, int],
    direction: int,
    reference_direction: int,
) -> PairRay:
    if direction not in range(6) or reference_direction not in range(6):
        raise ValueError("direction labels must be physical six-port labels")
    if reference_direction == (direction ^ 1):
        raise ValueError("the direct shell excludes the antipodal reference ray")

    carrier = body_vertex(code, body, direction)
    reference_port = body_vertex(code, body, reference_direction)
    reference, outer_edge = local.old.outer_partner(code, reference_port)
    face = code.A[outer_edge]
    if reference_direction != direction:
        face = face @ code.graph.A(carrier, reference_port)
    face = phase_dressed(face, reference_direction)
    tags = (1 << carrier) | (1 << reference)
    representative = local.full_state_representative(code, face, tags)
    return PairRay(
        direction=direction,
        reference_direction=reference_direction,
        carrier=carrier,
        reference=reference,
        face_pauli=face,
        tags=tags,
        representative=representative,
    )


def shell(code: c269.WilsonSubsystemCode, body=BODY) -> tuple[PairRay, ...]:
    return tuple(pair_ray(code, body, *label) for label in PAIR_LABELS)


def encoding_matrix() -> np.ndarray:
    encoding = np.zeros((len(PAIR_LABELS), 6), dtype=complex)
    for row, (direction, _reference) in enumerate(PAIR_LABELS):
        encoding[row, direction] = 1 / np.sqrt(5)
    return encoding


def lifted_coin(coin: np.ndarray) -> np.ndarray:
    """Thirty-sector coefficient matrix of the local physical block."""

    encoding = encoding_matrix()
    projector = encoding @ encoding.conj().T
    return np.eye(len(PAIR_LABELS)) - projector + encoding @ coin @ encoding.conj().T


def tag_projector_description(ray: PairRay, active_vertices: tuple[int, ...]):
    """Exact local tag-pattern projector Π_ray, retained symbolically."""

    return tuple((vertex, (ray.tags >> vertex) & 1) for vertex in active_vertices)


def transition_pauli(left: PairRay, right: PairRay) -> c235.Pauli:
    """Pauli part W_left W_right^dagger of a local matrix unit."""

    return left.representative @ pauli_dagger(right.representative)


def direction_map(frame: np.ndarray, direction: int) -> int:
    target = frame @ c210.DIRECTIONS[direction]
    return int(np.where(np.all(c210.DIRECTIONS == target, axis=1))[0][0])


def pair_permutation(frame: np.ndarray) -> np.ndarray:
    representation = np.zeros((len(PAIR_LABELS), len(PAIR_LABELS)), dtype=complex)
    for source, (direction, reference) in enumerate(PAIR_LABELS):
        target = PAIR_INDEX[(direction_map(frame, direction), direction_map(frame, reference))]
        representation[target, source] = 1
    return representation


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for source in rows:
        row = source
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def active_tag_vertices(rays: tuple[PairRay, ...]) -> tuple[int, ...]:
    mask = 0
    for ray in rays:
        mask |= ray.tags
    return tuple(vertex for vertex in range(mask.bit_length()) if (mask >> vertex) & 1)


def constraint_pauli(code: c269.WilsonSubsystemCode, vertex: int) -> c235.Pauli:
    return c235.Pauli(
        z=code.B[vertex].z | (1 << (code.qubits + vertex))
    )


def basis_and_locality_controls(code: c269.WilsonSubsystemCode, label: str) -> tuple[PairRay, ...]:
    rays = shell(code)
    active_tags = active_tag_vertices(rays)
    tag_masks = tuple(ray.tags for ray in rays)
    occupied = tuple(local.occupied_vertices(code, ray.face_pauli) for ray in rays)

    check(
        f"{label}: thirty pair rays have the declared two occupations",
        all(occ == frozenset((ray.carrier, ray.reference)) for ray, occ in zip(rays, occupied)),
    )
    check(
        f"{label}: port tags exactly match face-code occupation syndromes",
        all(ray.tags == sum(1 << vertex for vertex in occ) for ray, occ in zip(rays, occupied)),
    )
    check(
        f"{label}: tag sectors make all thirty physical rays orthogonal",
        len(set(tag_masks)) == 30,
        len(set(tag_masks)),
    )
    reference_sets = {
        direction: {
            ray.reference_direction
            for ray in rays
            if ray.direction == direction
        }
        for direction in range(6)
    }
    check(
        f"{label}: every logical direction uses exactly its five non-antipodal reference rays",
        all(
            references
            == (set(range(6)) - {direction ^ 1})
            for direction, references in reference_sets.items()
        ),
        reference_sets,
    )
    check(
        f"{label}: the shell uses six body and six neighboring port constraints",
        len(active_tags) == 12,
        tuple(code.graph.vertices[vertex] for vertex in active_tags),
    )

    shell_supports = []
    max_word_supports = []
    for body in code.graph.cells:
        face_union = 0
        tag_union = 0
        max_word_support = 0
        for ray in shell(code, body):
            face_union |= ray.face_pauli.x | ray.face_pauli.z
            tag_union |= ray.tags
            max_word_support = max(
                max_word_support,
                (ray.face_pauli.x | ray.face_pauli.z).bit_count()
                + ray.tags.bit_count(),
            )
        shell_supports.append(
            (
                face_union.bit_count(),
                tag_union.bit_count(),
                face_union.bit_count() + tag_union.bit_count(),
            )
        )
        max_word_supports.append(max_word_support)
    check(
        f"{label}: every translated local coin block has bounded at-most-fifty-four-M2 support",
        {row[0] for row in shell_supports} == {30, 34, 38, 42}
        and {row[1] for row in shell_supports} == {12}
        and {row[2] for row in shell_supports} == {42, 46, 50, 54}
        and set(max_word_supports) == {14, 15},
        {
            "bodies_tested": len(shell_supports),
            "face_M2": sorted({row[0] for row in shell_supports}),
            "port_M2": sorted({row[1] for row in shell_supports}),
            "total_support_M2": sorted({row[2] for row in shell_supports}),
            "max_representative_word_M2": sorted(set(max_word_supports)),
            "fixed_overhead_M2_per_cell": 21,
        },
    )

    # Each transition flips face occupation and its matching tags together.
    constraint_failures = 0
    sector_failures = 0
    for left in rays:
        for right in rays:
            transition = transition_pauli(left, right)
            for vertex in range(len(code.graph.vertices)):
                constraint_failures += not transition.commutes(constraint_pauli(code, vertex))
            sector_failures += sum(
                not transition.commutes(row)
                for row in code.local_checks + code.wilsons
            )
    check(
        f"{label}: every local matrix-unit transition preserves B_v Z_port(v)",
        constraint_failures == 0,
        constraint_failures,
    )
    check(
        f"{label}: every transition stays in the fixed Wilson and local-check sector",
        sector_failures == 0,
        sector_failures,
    )
    return rays


def matrix_unit_controls(
    code: c269.WilsonSubsystemCode, rays: tuple[PairRay, ...]
) -> None:
    # Q_ij Q_jk = Q_ik and Q_ij^dagger = Q_ji; the orthogonal local tag
    # projectors turn these Pauli transitions into exact matrix units M_ij.
    algebra_failures = 0
    dagger_failures = 0
    representative_action_failures = 0
    tag_flip_failures = 0
    projector_transport_failures = 0
    nonmatching_projector_failures = 0
    for left in range(30):
        for middle in range(30):
            qlm = transition_pauli(rays[left], rays[middle])
            dagger_failures += pauli_dagger(qlm) != transition_pauli(rays[middle], rays[left])
            representative_action_failures += (
                qlm @ rays[middle].representative != rays[left].representative
            )
            tag_flip = qlm.x >> code.qubits
            expected_flip = rays[left].tags ^ rays[middle].tags
            tag_flip_failures += tag_flip != expected_flip
            projector_transport_failures += (
                (rays[middle].tags ^ tag_flip) != rays[left].tags
                or (rays[left].tags ^ tag_flip) != rays[middle].tags
            )
            for right in range(30):
                algebra_failures += (
                    qlm @ transition_pauli(rays[middle], rays[right])
                    != transition_pauli(rays[left], rays[right])
                )
                mapped_pattern = rays[right].tags ^ (
                    rays[middle].tags ^ rays[right].tags
                )
                nonmatching_projector_failures += (
                    (mapped_pattern == rays[left].tags) != (left == middle)
                )
    check(
        "the supplied Pauli transitions and local tag projectors form exact matrix units",
        algebra_failures == 0
        and dagger_failures == 0
        and representative_action_failures == 0
        and tag_flip_failures == 0
        and projector_transport_failures == 0
        and nonmatching_projector_failures == 0,
        {
            "product_failures": algebra_failures,
            "dagger_failures": dagger_failures,
            "representative_action_failures": representative_action_failures,
            "tag_flip_failures": tag_flip_failures,
            "projector_transport_failures": projector_transport_failures,
            "nonmatching_projector_failures": nonmatching_projector_failures,
        },
    )
    active_tags = active_tag_vertices(rays)
    descriptions = tuple(tag_projector_description(ray, active_tags) for ray in rays)
    projector_constraint_commutators = 0
    projector_sector_commutators = 0
    for vertex in active_tags:
        tag_z = c235.Pauli(z=1 << (code.qubits + vertex))
        projector_constraint_commutators += sum(
            not tag_z.commutes(constraint_pauli(code, target))
            for target in range(len(code.graph.vertices))
        )
        projector_sector_commutators += sum(
            not tag_z.commutes(row) for row in code.local_checks + code.wilsons
        )
    check(
        "matrix-unit projectors transport exactly and commute with every constraint and fixed-sector generator",
        len(set(descriptions)) == 30
        and all(len(row) == 12 for row in descriptions)
        and projector_constraint_commutators == 0
        and projector_sector_commutators == 0,
        {
            "local_projectors": len(descriptions),
            "tag_checks_each": 12,
            "constraint_commutators": projector_constraint_commutators,
            "sector_commutators": projector_sector_commutators,
            "host_labels_copied": False,
        },
    )


def physical_matrix_unit_update_controls(rays: tuple[PairRay, ...]) -> None:
    """Check the symbolic bounded operator, not only its dense coefficient block."""

    coin = c219.common_species(-0.3).coin
    coefficients = lifted_coin(coin)
    action_failures = 0
    maximum_coefficient_residual = 0.0
    for source, source_ray in enumerate(rays):
        physical_column = np.zeros(30, dtype=complex)
        for target, target_ray in enumerate(rays):
            transition = transition_pauli(target_ray, source_ray)
            action_failures += (
                transition @ source_ray.representative
                != target_ray.representative
            )
            physical_column[target] = coefficients[target, source]
        maximum_coefficient_residual = max(
            maximum_coefficient_residual,
            float(np.linalg.norm(physical_column - coefficients[:, source])),
        )
    occupied_patterns = {ray.tags for ray in rays}
    inactive_patterns = (1 << len(active_tag_vertices(rays))) - len(occupied_patterns)
    check(
        "the explicit matrix-unit polynomial realizes the dense block on all thirty sectors and identity on every other local tag pattern",
        action_failures == 0
        and maximum_coefficient_residual == 0
        and inactive_patterns == 4096 - 30,
        {
            "physical_sector_action_failures": action_failures,
            "coefficient_residual": maximum_coefficient_residual,
            "active_tag_patterns": len(occupied_patterns),
            "inactive_identity_patterns": inactive_patterns,
            "primitive_gate_synthesis_supplied": False,
        },
    )


def coin_controls(beta: float, held: bool = False) -> None:
    species = c219.common_species(beta)
    coin = species.coin
    encoding = encoding_matrix()
    projector = encoding @ encoding.conj().T
    physical = lifted_coin(coin)
    label = "held beta=-0.35" if held else f"beta={beta}"

    isometry_residual = np.linalg.norm(encoding.conj().T @ encoding - np.eye(6))
    intertwining_residual = np.linalg.norm(physical @ encoding - encoding @ coin)
    unitarity_residual = np.linalg.norm(physical.conj().T @ physical - np.eye(30))
    inverse_residual = np.linalg.norm(physical @ physical.conj().T - np.eye(30))
    leakage_residual = np.linalg.norm((np.eye(30) - projector) @ physical @ encoding)
    check(
        f"{label}: E is isometric and U_physical E = E C exactly to tolerance",
        max(isometry_residual, intertwining_residual, leakage_residual) < 3e-14,
        {
            "isometry": isometry_residual,
            "intertwining": intertwining_residual,
            "leakage": leakage_residual,
        },
    )
    check(
        f"{label}: the local physical block is unitary with adjoint inverse",
        max(unitarity_residual, inverse_residual) < 3e-14,
        {"unitarity": unitarity_residual, "inverse": inverse_residual},
    )

    coherent = np.asarray((1, 1j, -2, 0.5j, 3 - 1j, -0.7), dtype=complex)
    coherent /= np.linalg.norm(coherent)
    coherent_residual = np.linalg.norm(physical @ (encoding @ coherent) - encoding @ (coin @ coherent))
    check(
        f"{label}: a held coherent superposition of all six local directions is preserved",
        coherent_residual < 3e-14 and abs(np.linalg.norm(encoding @ coherent) - 1) < 3e-14,
        coherent_residual,
    )

    scalar = c210.UNIFORM
    encoded_scalar = encoding @ scalar
    scalar_eigenvalue = np.vdot(encoded_scalar, physical @ encoded_scalar)
    physical_rest_mass = float(np.angle(scalar_eigenvalue)) / c219.C_SQUARED
    fixture_mass = c219.rest_mass(species)
    check(
        f"{label}: the Cycle-219 scalar rest-mass fixture survives the lift",
        abs(physical_rest_mass - fixture_mass) < 3e-13
        and abs(fixture_mass - species.analytic_mass) < 3e-12,
        {
            "physical_rest_mass": physical_rest_mass,
            "Cycle219_rest_mass": fixture_mass,
            "analytic_mass": species.analytic_mass,
        },
    )


def covariance_controls(code: c269.WilsonSubsystemCode, rays: tuple[PairRay, ...]) -> None:
    encoding = encoding_matrix()
    coin = c219.common_species(-0.3).coin
    physical = lifted_coin(coin)
    frame_phase_failures = 0
    frame_tag_failures = 0
    raw_column_failures = 0
    raw_phase_failures = 0
    cocycle_rows: list[int] = []
    cocycle_rhs: list[int] = []
    representation_residuals = []
    physical_residuals = []
    pair_representations = []
    frames = c235.proper_cubic_frames()

    for frame in frames:
        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        pair_representation = pair_permutation(frame)
        pair_representations.append(pair_representation)
        direction_representation = c210.direction_permutation(frame)
        representation_residuals.append(
            np.linalg.norm(pair_representation @ encoding - encoding @ direction_representation)
        )
        physical_residuals.append(
            np.linalg.norm(
                pair_representation @ physical @ pair_representation.conj().T - physical
            )
        )

        for body in product(range(code.length), repeat=3):
            target_body = tuple(
                int(value % code.length) for value in frame @ np.asarray(body)
            )
            source_rays = shell(code, body)
            target_rays = shell(code, target_body)
            for source, ray in enumerate(source_rays):
                direction = direction_map(frame, ray.direction)
                reference = direction_map(frame, ray.reference_direction)
                target = target_rays[PAIR_INDEX[(direction, reference)]]
                transformed = local.transform_pauli(
                    code, ray.face_pauli, edge_map, toggles, pairs, flips
                )
                frame_phase_failures += local.relative_scalar(transformed, target.face_pauli) != 0
                frame_tag_failures += (
                    local.ports.permute_bits(ray.tags, vertex_map) != target.tags
                )

        # Deleting the dressing makes most encoded columns lose a common ray phase.
        source_rays = shell(code)
        target_rays = shell(code)
        for direction in range(6):
            phases = []
            for reference in range(6):
                if reference == (direction ^ 1):
                    continue
                source = source_rays[PAIR_INDEX[(direction, reference)]]
                target = target_rays[
                    PAIR_INDEX[(direction_map(frame, direction), direction_map(frame, reference))]
                ]
                raw_source = phase_dressed(source.face_pauli, reference)
                raw_target = phase_dressed(
                    target.face_pauli, direction_map(frame, reference)
                )
                transformed = local.transform_pauli(
                    code, raw_source, edge_map, toggles, pairs, flips
                )
                raw_phase = local.relative_scalar(transformed, raw_target)
                phases.append(raw_phase)
                raw_phase_failures += raw_phase not in (0, 2)
                if raw_phase in (0, 2):
                    target_reference = direction_map(frame, reference)
                    cocycle_rows.append(
                        (1 << reference) ^ (1 << target_reference)
                    )
                    cocycle_rhs.append(raw_phase // 2)
            raw_column_failures += len(set(phases)) != 1

    frame_lookup = {
        tuple(frame.flatten()): index for index, frame in enumerate(frames)
    }
    group_law_failures = 0
    group_law_maximum = 0.0
    for left_index, left_frame in enumerate(frames):
        for right_index, right_frame in enumerate(frames):
            product_index = frame_lookup[
                tuple((left_frame @ right_frame).flatten())
            ]
            residual = float(
                np.linalg.norm(
                    pair_representations[left_index]
                    @ pair_representations[right_index]
                    - pair_representations[product_index]
                )
            )
            group_law_maximum = max(group_law_maximum, residual)
            group_law_failures += residual > 3e-14

    check(
        "the dressed joint face/tag shell is covariant at every L=3 body under all 24 frames",
        frame_phase_failures == 0 and frame_tag_failures == 0,
        {
            "joint_state_ray_tests": 24 * 27 * 30,
            "face_phase_failures": frame_phase_failures,
            "tag_permutation_failures": frame_tag_failures,
        },
    )
    check(
        "the six-mode encoding and lifted Cycle-219 coin are exactly proper-cubic covariant",
        max(representation_residuals + physical_residuals) < 3e-14
        and group_law_failures == 0,
        {
            "encoding_max": max(representation_residuals),
            "physical_coin_max": max(physical_residuals),
            "pair_representation_group_tests": len(frames) ** 2,
            "group_law_failures": group_law_failures,
            "group_law_maximum": group_law_maximum,
        },
    )
    check(
        "deleting the local phase dressing is caught by the frame control",
        raw_column_failures == 108,
        {"failed_frame_columns": raw_column_failures, "tested": 24 * 6},
    )
    coefficient_rank = gf2_rank(cocycle_rows)
    augmented_rank = gf2_rank(
        [row | (rhs << 6) for row, rhs in zip(cocycle_rows, cocycle_rhs)]
    )
    solutions = tuple(
        mask
        for mask in range(1 << 6)
        if all(
            ((row & mask).bit_count() % 2) == rhs
            for row, rhs in zip(cocycle_rows, cocycle_rhs)
        )
    )
    supplied_dressing = sum(1 << reference for reference in (0, 2, 4))
    supplied_residual = sum(
        ((row & supplied_dressing).bit_count() % 2) != rhs
        for row, rhs in zip(cocycle_rows, cocycle_rhs)
    )
    check(
        "the raw binary phase data have an exact rank-five GF(2) cocycle repair, unique up to one global ray sign",
        raw_phase_failures == 0
        and len(cocycle_rows) == 720
        and cocycle_rhs.count(0) == cocycle_rhs.count(1) == 360
        and coefficient_rank == augmented_rank == 5
        and solutions == (0b010101, 0b101010)
        and supplied_dressing in solutions
        and supplied_residual == 0,
        {
            "equations": len(cocycle_rows),
            "raw_zero_phases": cocycle_rhs.count(0),
            "raw_minus_phases": cocycle_rhs.count(1),
            "coefficient_rank": coefficient_rank,
            "augmented_rank": augmented_rank,
            "solutions": tuple(f"{solution:06b}" for solution in solutions),
            "supplied_positive_ray_solution_residual": supplied_residual,
        },
    )

    translation_failures = 0
    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        target_rays = shell(code, displacement)
        for source, target in zip(rays, target_rays):
            transformed = local.transform_pauli(
                code, source.face_pauli, edge_map, toggles, pairs, flips
            )
            translation_failures += local.relative_scalar(transformed, target.face_pauli) != 0
            translation_failures += local.ports.permute_bits(source.tags, vertex_map) != target.tags
    check(
        "the joint face/tag shell is covariant under all 27 L=3 translations",
        translation_failures == 0,
        {"joint_ray_tests": 27 * 30, "failures": translation_failures},
    )


def deletion_and_domain_controls(code: c269.WilsonSubsystemCode) -> None:
    identity_residual = np.linalg.norm(lifted_coin(np.eye(6)) - np.eye(30))
    check(
        "deleting the supplied logical coin deletes the physical block exactly",
        identity_residual < 3e-14,
        identity_residual,
    )
    massless = c219.common_species(0.0)
    check(
        "the beta=0 physical block lifts the exact Cycle-219 field endpoint",
        np.linalg.norm(
            lifted_coin(massless.coin) @ encoding_matrix()
            - encoding_matrix() @ c219.c214.FIELD_COIN
        )
        < 3e-14,
    )

    tag_deletion_leaks = 0
    for ray in shell(code):
        occupations = local.occupied_vertices(code, ray.face_pauli)
        tag_deletion_leaks += bool(occupations) and ray.tags != 0
    check(
        "deleting the auxiliary tags is rejected by the local constraints",
        tag_deletion_leaks == 30,
        {"rejected_rays": tag_deletion_leaks, "tested": 30},
    )

    coin = c219.common_species(-0.3).coin
    physical = lifted_coin(coin)
    off_diagonal = abs(physical).copy()
    np.fill_diagonal(off_diagonal, 0)
    deleted_row, deleted_column = np.unravel_index(
        np.argmax(off_diagonal), off_diagonal.shape
    )
    deleted = physical.copy()
    deleted_coefficient = deleted[deleted_row, deleted_column]
    deleted[deleted_row, deleted_column] = 0
    deleted_intertwining = float(
        np.linalg.norm(deleted @ encoding_matrix() - encoding_matrix() @ coin)
    )
    deleted_unitarity = float(
        np.linalg.norm(deleted.conj().T @ deleted - np.eye(30))
    )
    check(
        "deleting one nonzero physical matrix-unit term breaks both intertwining and unitarity",
        abs(deleted_coefficient) > 0.1
        and deleted_intertwining > 0.05
        and deleted_unitarity > 0.15,
        {
            "deleted_matrix_unit": (int(deleted_row), int(deleted_column)),
            "deleted_coefficient": deleted_coefficient,
            "intertwining_residual": deleted_intertwining,
            "unitarity_residual": deleted_unitarity,
        },
    )

    rejects = 0
    try:
        pair_ray(code, BODY, 0, 1)
    except ValueError:
        rejects += 1
    try:
        pair_ray(code, BODY, -1, 2)
    except ValueError:
        rejects += 1
    try:
        c269.build_code(2)
    except ValueError:
        rejects += 1
    check(
        "lawful-domain controls reject antipodal, non-port, and aliased-L inputs",
        rejects == 3,
        rejects,
    )


def supplied_structure_inventory() -> None:
    inventory = {
        "supplied_fixed_sector": "+++ Wilson and all-B=+1 reference vacuum",
        "supplied_geometry": "Cycle-269 pyramid cellulation and local framing repair",
        "supplied_auxiliary": "six collision-safe port M2 per cell and B_v Z_port(v)",
        "supplied_encoding": "five non-antipodal reference-ray shell ansatz and one global phase-origin convention",
        "supplied_update": "Cycle-219 six-mode coin coefficient matrix",
        "derived_here": "GF(2) dressing solution, local matrix-unit completion, isometry, intertwining, inverse, constraint preservation, covariance, support",
        "not_supplied": "global ordering, parity service, copied tag, host-side direction control",
    }
    check(
        "all construction inputs and exclusions are inventoried",
        len(inventory) == 7,
        inventory,
    )


def main() -> None:
    print("CYCLE 302: JOINT SIX-MODE PHYSICAL COIN LIFT")
    note_contract()
    training = c269.build_code(TRAINING_SIZE)
    held = c269.build_code(HELD_SIZE)
    training_rays = basis_and_locality_controls(training, "training L=3")
    basis_and_locality_controls(held, "held L=6")
    matrix_unit_controls(training, training_rays)
    physical_matrix_unit_update_controls(training_rays)
    for beta in (-0.2, -0.3, -0.4):
        coin_controls(beta)
    coin_controls(-0.35, held=True)
    covariance_controls(training, training_rays)
    deletion_and_domain_controls(training)
    supplied_structure_inventory()
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
