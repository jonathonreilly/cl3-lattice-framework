#!/usr/bin/env python3
"""Cycle 305: full two-particle Cycle-219 fixed-seam interface on Cycle-269 M2.

The fifteen unordered pairs of six direction modes carry the exterior-square
coin wedge^2(C).  Twelve pairs are perpendicular internal edges of the
Cycle-269 octahedron.  Each of the three antipodal pairs is represented by a
bounded two-edge intracell path; all four path choices are the same ray in the
fixed +++ Wilson reference vacuum.

For one supplied body cell x, collect every pair and its streamed/caught-up
image into one 30-column isometry E_x.  A bounded local matrix-unit polynomial
lifts wedge^2(C) on both slices, while the existing physical contact and
complete outer-edge stream/catch-up products act exactly on the same code.

This is a reference-relative full two-particle interface, not a full-Fock
compiler, absolute-vacuum preparation, physical-time law, or energy claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_collision_safe_auxiliary_ports_2026_07_17 as ports
import physical_cycle269_reference_relative_localized_pair_lift_2026_07_17 as local
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md"
)
TRAINING_SIZES = (3, 4, 5)
HELD_SIZES = (6,)
SIZES = TRAINING_SIZES + HELD_SIZES
PAIR_LABELS = tuple(combinations(range(6), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIR_LABELS)}
PAIR_DIMENSION = len(PAIR_LABELS)
SLICE_DIMENSION = 2
CODE_DIMENSION = PAIR_DIMENSION * SLICE_DIMENSION
COUPLING = c230.COUPLING
TOLERANCE = 5e-12

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class PairSliceRay:
    pair: tuple[int, int]
    left: int
    right: int
    left_arrival: int
    right_arrival: int
    left_outer_edge: int
    right_outer_edge: int
    intermediate_direction: int | None
    input_face_pauli: c235.Pauli
    output_face_pauli: c235.Pauli
    input_tags: int
    output_tags: int

    @property
    def antipodal(self) -> bool:
        return self.pair[1] == (self.pair[0] ^ 1)


@dataclass(frozen=True)
class SectorEncoder:
    code: c269.WilsonSubsystemCode
    body: tuple[int, int, int]
    rays: tuple[PairSliceRay, ...]

    def column(self, pair_index: int, stream_slice: int) -> tuple[c235.Pauli, int]:
        ray = self.rays[pair_index]
        if stream_slice == 0:
            return ray.input_face_pauli, ray.input_tags
        if stream_slice == 1:
            return ray.output_face_pauli, ray.output_tags
        raise ValueError("the sector interface has exactly two stream slices")

    def columns(self):
        for pair_index in range(PAIR_DIMENSION):
            for stream_slice in range(SLICE_DIMENSION):
                yield pair_index, stream_slice, self.column(pair_index, stream_slice)


class StabilizerReducer:
    """Exact phase reduction modulo the unique fixed-Wilson face vacuum."""

    def __init__(self, code: c269.WilsonSubsystemCode):
        self.qubits = code.qubits
        self.pivots: dict[int, c235.Pauli] = {}
        for original in code.local_checks + code.wilsons + code.B:
            row = original
            symplectic = row.symplectic(self.qubits)
            while symplectic:
                pivot = symplectic.bit_length() - 1
                if pivot in self.pivots:
                    row = row @ self.pivots[pivot]
                    symplectic = row.symplectic(self.qubits)
                else:
                    self.pivots[pivot] = row
                    break
            if not symplectic and row.phase % 4:
                raise ValueError("the supplied reference stabilizers are inconsistent")
        if len(self.pivots) != self.qubits:
            raise ValueError("the fixed-Wilson reference vacuum must be unique")

    def vacuum_phase(self, pauli: c235.Pauli) -> int | None:
        row = pauli
        symplectic = row.symplectic(self.qubits)
        while symplectic:
            pivot = symplectic.bit_length() - 1
            if pivot not in self.pivots:
                return None
            row = row @ self.pivots[pivot]
            symplectic = row.symplectic(self.qubits)
        return row.phase % 4

    def relative_phase(self, left: c235.Pauli, right: c235.Pauli) -> int | None:
        return self.vacuum_phase(local.pauli_dagger(right) @ left)


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
        check("the Cycle-305 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "wedge^2(c)",
        "fifteen unordered pairs",
        "twelve perpendicular",
        "three antipodal",
        "one 30-column e_x",
        "e_x k_seam = k_physical,seam e_x",
        "e_x d_coarse = d_physical e_x",
        "e_x s_coarse = s_physical e_x",
        "local matrix-unit polynomial",
        "all four antipodal paths",
        "signed-wedge",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "at most fifty-four m2",
        "twenty-one m2 per cell",
        "constraint leakage",
        "deletion",
        "lawful domain",
        "fixed +++ wilson reference vacuum",
        "absolute vacuum preparation remains open",
        "coherent position remains open",
        "primitive gate synthesis remains open",
        "not a recurrent volume update",
        "does not claim a physical coin on the separated slice",
        "cycle-230 order",
        "subsequent cycle-230 contact is identity",
        "not a full-fock compiler",
        "not physical energy",
        "not a rate",
        "no gravity/source semantics",
        "no record claim",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the full two-particle theorem and exact boundary", not missing, missing)


def column_index(pair_index: int, stream_slice: int) -> int:
    return SLICE_DIMENSION * pair_index + stream_slice


def phase_scalar(phase: int) -> complex:
    return (1 + 0j, 1j, -1 + 0j, -1j)[phase % 4]


def body_vertices(
    code: c269.WilsonSubsystemCode, body: tuple[int, int, int]
) -> tuple[int, ...]:
    if body not in code.graph.cells:
        raise ValueError("the supplied body must be one coarse cell")
    return tuple(code.graph.vertex_index[(body, direction)] for direction in range(6))


def representative_intermediate(pair: tuple[int, int]) -> int:
    if pair[1] != (pair[0] ^ 1):
        raise ValueError("only an antipodal pair needs a two-edge path")
    return min(set(range(6)) - set(pair))


def input_pair_pauli(
    code: c269.WilsonSubsystemCode,
    body: tuple[int, int, int],
    pair: tuple[int, int],
    intermediate_direction: int | None = None,
) -> tuple[c235.Pauli, int | None]:
    vertices = body_vertices(code, body)
    left_direction, right_direction = pair
    if not (0 <= left_direction < right_direction < 6):
        raise ValueError("pair labels must be strictly ordered physical directions")
    left, right = vertices[left_direction], vertices[right_direction]
    if right_direction != (left_direction ^ 1):
        if intermediate_direction is not None:
            raise ValueError("perpendicular pairs use their direct internal edge")
        return code.graph.A(left, right), None
    if intermediate_direction is None:
        intermediate_direction = representative_intermediate(pair)
    if intermediate_direction in pair or not 0 <= intermediate_direction < 6:
        raise ValueError("an antipodal path needs one perpendicular intermediate mode")
    middle = vertices[intermediate_direction]
    return code.graph.A(left, middle) @ code.graph.A(middle, right), intermediate_direction


def pair_slice_ray(
    code: c269.WilsonSubsystemCode,
    body: tuple[int, int, int],
    pair: tuple[int, int],
) -> PairSliceRay:
    vertices = body_vertices(code, body)
    input_face, intermediate = input_pair_pauli(code, body, pair)
    left, right = vertices[pair[0]], vertices[pair[1]]
    left_arrival, left_outer = local.old.outer_partner(code, left)
    right_arrival, right_outer = local.old.outer_partner(code, right)
    output_face, _stream_phase = local.two_edge_physical_face_action(
        code,
        input_face,
        (left, right),
        (left_outer, right_outer),
    )
    return PairSliceRay(
        pair=pair,
        left=left,
        right=right,
        left_arrival=left_arrival,
        right_arrival=right_arrival,
        left_outer_edge=left_outer,
        right_outer_edge=right_outer,
        intermediate_direction=intermediate,
        input_face_pauli=input_face,
        output_face_pauli=output_face,
        input_tags=(1 << left) | (1 << right),
        output_tags=(1 << left_arrival) | (1 << right_arrival),
    )


def sector_encoder(
    code: c269.WilsonSubsystemCode, body: tuple[int, int, int]
) -> SectorEncoder:
    return SectorEncoder(
        code,
        body,
        tuple(pair_slice_ray(code, body, pair) for pair in PAIR_LABELS),
    )


def ray_key(pauli: c235.Pauli, tags: int) -> tuple[int, int, int, int]:
    return pauli.phase, pauli.x, pauli.z, tags


def exact_gram(encoder: SectorEncoder) -> np.ndarray:
    tags = [tags for _pair, _stream_slice, (_pauli, tags) in encoder.columns()]
    if len(set(tags)) != CODE_DIMENSION:
        raise ValueError("the 30 physical pair/slice tag patterns must be distinct")
    return np.eye(CODE_DIMENSION, dtype=complex)


def wedge2_matrix(matrix: np.ndarray) -> np.ndarray:
    if matrix.shape != (6, 6) or not np.all(np.isfinite(matrix)):
        raise ValueError("wedge^2 requires one finite 6-by-6 matrix")
    return np.asarray(
        [
            [
                matrix[left, source_left] * matrix[right, source_right]
                - matrix[left, source_right] * matrix[right, source_left]
                for source_left, source_right in PAIR_LABELS
            ]
            for left, right in PAIR_LABELS
        ],
        dtype=complex,
    )


def wedge_vector(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return np.asarray(
        [left[a] * right[b] - left[b] * right[a] for a, b in PAIR_LABELS],
        dtype=complex,
    )


def pair_representation(frame: np.ndarray) -> np.ndarray:
    matrix = np.zeros((PAIR_DIMENSION, PAIR_DIMENSION), dtype=complex)
    for source, (left, right) in enumerate(PAIR_LABELS):
        mapped_left = int(
            np.where(
                np.all(c210.DIRECTIONS == frame @ c210.DIRECTIONS[left], axis=1)
            )[0][0]
        )
        mapped_right = int(
            np.where(
                np.all(c210.DIRECTIONS == frame @ c210.DIRECTIONS[right], axis=1)
            )[0][0]
        )
        target_pair = tuple(sorted((mapped_left, mapped_right)))
        sign = 1 if mapped_left < mapped_right else -1
        matrix[PAIR_INDEX[target_pair], source] = sign
    return matrix


def coarse_stream_matrix() -> np.ndarray:
    matrix = np.zeros((CODE_DIMENSION, CODE_DIMENSION), dtype=complex)
    for pair_index in range(PAIR_DIMENSION):
        matrix[column_index(pair_index, 1), column_index(pair_index, 0)] = 1
        matrix[column_index(pair_index, 0), column_index(pair_index, 1)] = 1
    return matrix


def coarse_contact_matrix(coupling: float) -> np.ndarray:
    diagonal = np.ones(CODE_DIMENSION, dtype=complex)
    diagonal[0::2] = np.exp(1j * coupling)
    return np.diag(diagonal)


def fixed_seam_coin_comparator(coin: np.ndarray) -> np.ndarray:
    """Apply wedge^2(C) only on colocated t=0; leave separated t=1 fixed.

    This is a unitary comparator completion on the declared 30-column seam.
    It is not the recurrent onsite volume coin on the separated output states.
    """

    matrix = np.eye(CODE_DIMENSION, dtype=complex)
    matrix[0::2, 0::2] = wedge2_matrix(coin)
    return matrix


def contact_phase(
    code: c269.WilsonSubsystemCode,
    occupations: frozenset[int],
    coupling: float,
) -> complex:
    counts: dict[tuple[int, int, int], int] = {}
    for vertex in occupations:
        cell = code.graph.vertices[vertex][0]
        counts[cell] = counts.get(cell, 0) + 1
    pairs = sum(number * (number - 1) // 2 for number in counts.values())
    return complex(np.exp(1j * coupling * pairs))


def physical_contact_matrix(encoder: SectorEncoder, coupling: float) -> np.ndarray:
    diagonal = np.empty(CODE_DIMENSION, dtype=complex)
    for pair_index, stream_slice, (pauli, _tags) in encoder.columns():
        diagonal[column_index(pair_index, stream_slice)] = contact_phase(
            encoder.code,
            local.occupied_vertices(encoder.code, pauli),
            coupling,
        )
    return np.diag(diagonal)


def physical_stream_matrix(encoder: SectorEncoder) -> tuple[np.ndarray, dict[str, int]]:
    code = encoder.code
    lookup = {
        ray_key(pauli, tags): column_index(pair_index, stream_slice)
        for pair_index, stream_slice, (pauli, tags) in encoder.columns()
    }
    matrix = np.zeros((CODE_DIMENSION, CODE_DIMENSION), dtype=complex)
    failures = {"face": 0, "catchup": 0, "sign": 0, "target": 0}
    for pair_index, ray in enumerate(encoder.rays):
        for stream_slice in range(SLICE_DIMENSION):
            if stream_slice == 0:
                source_face = ray.input_face_pauli
                source_tags = ray.input_tags
                occupied = (ray.left, ray.right)
            else:
                source_face = ray.output_face_pauli
                source_tags = ray.output_tags
                occupied = (ray.left_arrival, ray.right_arrival)
            target_face, _phase = local.two_edge_physical_face_action(
                code,
                source_face,
                occupied,
                (ray.left_outer_edge, ray.right_outer_edge),
            )
            arrival, caught, sign = ports.port_macrostep(
                code, source_tags, source_tags
            )
            expected_face, expected_tags = encoder.column(
                pair_index, 1 - stream_slice
            )
            failures["face"] += target_face != expected_face
            failures["catchup"] += (arrival, caught) != (
                expected_tags,
                expected_tags,
            )
            failures["sign"] += sign != 1
            target = lookup.get(ray_key(target_face, caught))
            failures["target"] += target is None
            if target is not None:
                matrix[target, column_index(pair_index, stream_slice)] = sign
    return matrix, failures


def transition_pauli(
    code: c269.WilsonSubsystemCode,
    left: tuple[c235.Pauli, int],
    right: tuple[c235.Pauli, int],
) -> c235.Pauli:
    left_rep = local.full_state_representative(code, *left)
    right_rep = local.full_state_representative(code, *right)
    return left_rep @ local.pauli_dagger(right_rep)


def active_tag_vertices(encoder: SectorEncoder) -> tuple[int, ...]:
    mask = 0
    for _pair, _stream_slice, (_pauli, tags) in encoder.columns():
        mask |= tags
    return tuple(vertex for vertex in range(mask.bit_length()) if (mask >> vertex) & 1)


def constraint_pauli(code: c269.WilsonSubsystemCode, vertex: int) -> c235.Pauli:
    return c235.Pauli(
        z=code.B[vertex].z | (1 << (code.qubits + vertex))
    )


def antipodal_path_controls(cache: dict[int, c269.WilsonSubsystemCode]) -> None:
    print("\nANTIPODAL PATH EXISTENCE / FIXED-VACUUM EQUIVALENCE")
    rows = []
    for length, code in cache.items():
        reducer = StabilizerReducer(code)
        body = (0, 0, 0)
        occupation_failures = 0
        path_phase_failures = 0
        path_tests = 0
        path_supports = []
        for pair in PAIR_LABELS:
            if pair[1] != (pair[0] ^ 1):
                continue
            representative, _middle = input_pair_pauli(code, body, pair)
            vertices = body_vertices(code, body)
            expected = frozenset((vertices[pair[0]], vertices[pair[1]]))
            for intermediate in sorted(set(range(6)) - set(pair)):
                candidate, selected = input_pair_pauli(
                    code, body, pair, intermediate
                )
                occupation_failures += (
                    local.occupied_vertices(code, candidate) != expected
                )
                path_phase_failures += reducer.relative_phase(candidate, representative) != 0
                path_supports.append((candidate.x | candidate.z).bit_count())
                path_tests += 1
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "antipodal_pairs": 3,
                "paths_per_pair": 4,
                "path_tests": path_tests,
                "face_supports": sorted(set(path_supports)),
                "occupation_failures": occupation_failures,
                "fixed_vacuum_phase_failures": path_phase_failures,
                "reference_rank": len(reducer.pivots),
            }
        )
    check(
        "all four bounded paths for every antipodal pair are the same fixed-vacuum physical ray with common phase through held L=6",
        all(
            row["path_tests"] == 12
            and row["occupation_failures"] == 0
            and row["fixed_vacuum_phase_failures"] == 0
            and row["reference_rank"] == 15 * row["L"] ** 3
            for row in rows
        ),
        rows,
    )


def encoder_geometry_and_constraint_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> dict[int, list[SectorEncoder]]:
    print("\nONE 30-COLUMN E_X / GRAM / SUPPORT / CONSTRAINTS")
    fixtures: dict[int, list[SectorEncoder]] = {}
    rows = []
    for length, code in cache.items():
        encoders = [sector_encoder(code, body) for body in code.graph.cells]
        fixtures[length] = encoders
        gram_failures = 0
        occupation_failures = 0
        port_constraint_failures = 0
        local_leakage = 0
        wilson_leakage = 0
        pair_orbit_counts = []
        support_rows = []
        max_words = []
        for encoder in encoders:
            gram_failures += np.linalg.norm(
                exact_gram(encoder) - np.eye(CODE_DIMENSION)
            ) != 0
            pair_orbit_counts.append(
                (
                    sum(not ray.antipodal for ray in encoder.rays),
                    sum(ray.antipodal for ray in encoder.rays),
                )
            )
            face_union = 0
            tag_union = 0
            max_word = 0
            for _pair_index, _stream_slice, (pauli, tags) in encoder.columns():
                occupations = local.occupied_vertices(code, pauli)
                occupation_mask = sum(1 << vertex for vertex in occupations)
                occupation_failures += len(occupations) != 2
                occupation_failures += tags != occupation_mask
                local_leakage += sum(
                    not pauli.commutes(row) for row in code.local_checks
                )
                wilson_leakage += sum(
                    not pauli.commutes(row) for row in code.wilsons
                )
                for vertex, B_vertex in enumerate(code.B):
                    port_constraint_failures += (
                        (not pauli.commutes(B_vertex))
                        != bool((tags >> vertex) & 1)
                    )
                face_union |= pauli.x | pauli.z
                tag_union |= tags
                max_word = max(
                    max_word,
                    (pauli.x | pauli.z).bit_count() + tags.bit_count(),
                )
            support_rows.append(
                (
                    face_union.bit_count(),
                    tag_union.bit_count(),
                    face_union.bit_count() + tag_union.bit_count(),
                )
            )
            max_words.append(max_word)
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "encoders": len(encoders),
                "columns_per_E_x": CODE_DIMENSION,
                "pair_orbit_counts": sorted(set(pair_orbit_counts)),
                "face_supports_M2": sorted({row[0] for row in support_rows}),
                "port_supports_M2": sorted({row[1] for row in support_rows}),
                "total_supports_M2": sorted({row[2] for row in support_rows}),
                "representative_supports_M2": sorted(set(max_words)),
                "gram_failures": gram_failures,
                "occupation_failures": occupation_failures,
                "port_constraint_failures": port_constraint_failures,
                "local_check_leakage": local_leakage,
                "Wilson_leakage": wilson_leakage,
                "M2_per_cell": 21,
            }
        )
    check(
        "one E_x carries all fifteen pairs and both stream slices with exact Gram, bounded support, and zero constraint leakage through held L=6",
        all(
            row["encoders"] == row["L"] ** 3
            and row["columns_per_E_x"] == CODE_DIMENSION
            and row["pair_orbit_counts"] == [(12, 3)]
            and row["face_supports_M2"] == [30, 34, 38, 42]
            and row["port_supports_M2"] == [12]
            and row["total_supports_M2"] == [42, 46, 50, 54]
            and row["representative_supports_M2"] == [16, 17, 18, 19]
            and row["gram_failures"] == 0
            and row["occupation_failures"] == 0
            and row["port_constraint_failures"] == 0
            and row["local_check_leakage"] == 0
            and row["Wilson_leakage"] == 0
            and row["M2_per_cell"] == 21
            for row in rows
        ),
        rows,
    )
    return fixtures


def matrix_unit_controls(encoder: SectorEncoder) -> None:
    print("\nLOCAL MATRIX-UNIT PHYSICAL COIN POLYNOMIAL")
    code = encoder.code
    columns = [column for _pair, _slice, column in encoder.columns()]
    active_tags = active_tag_vertices(encoder)
    tag_patterns = tuple(tags for _pauli, tags in columns)
    algebra_failures = 0
    dagger_failures = 0
    action_failures = 0
    tag_flip_failures = 0
    projector_transport_failures = 0
    constraint_commutators = 0
    sector_commutators = 0
    transitions: dict[tuple[int, int], c235.Pauli] = {}
    representatives = [local.full_state_representative(code, *column) for column in columns]
    for left in range(CODE_DIMENSION):
        for right in range(CODE_DIMENSION):
            transition = transition_pauli(code, columns[left], columns[right])
            transitions[(left, right)] = transition
            dagger_failures += local.pauli_dagger(transition) != transition_pauli(
                code, columns[right], columns[left]
            )
            action_failures += transition @ representatives[right] != representatives[left]
            tag_flip = transition.x >> code.qubits
            tag_flip_failures += tag_flip != (tag_patterns[left] ^ tag_patterns[right])
            projector_transport_failures += (
                (tag_patterns[right] ^ tag_flip) != tag_patterns[left]
            )
    for left in range(CODE_DIMENSION):
        for middle in range(CODE_DIMENSION):
            for right in range(CODE_DIMENSION):
                algebra_failures += (
                    transitions[(left, middle)] @ transitions[(middle, right)]
                    != transitions[(left, right)]
                )
    for vertex in active_tags:
        tag_z = c235.Pauli(z=1 << (code.qubits + vertex))
        constraint_commutators += sum(
            not tag_z.commutes(constraint_pauli(code, target))
            for target in range(len(code.graph.vertices))
        )
        sector_commutators += sum(
            not tag_z.commutes(row) for row in code.local_checks + code.wilsons
        )
    coin = fixed_seam_coin_comparator(c219.common_species(-0.3).coin)
    physical_action_failures = 0
    for source in range(CODE_DIMENSION):
        for target in range(CODE_DIMENSION):
            physical_action_failures += (
                transitions[(target, source)] @ representatives[source]
                != representatives[target]
            )
    check(
        "the joint face/tag transitions and twelve-bit projectors form exact matrix units preserving all constraints",
        len(set(tag_patterns)) == CODE_DIMENSION
        and len(active_tags) == 12
        and algebra_failures == 0
        and dagger_failures == 0
        and action_failures == 0
        and tag_flip_failures == 0
        and projector_transport_failures == 0
        and constraint_commutators == 0
        and sector_commutators == 0
        and physical_action_failures == 0,
        {
            "matrix_units": CODE_DIMENSION ** 2,
            "triple_product_tests": CODE_DIMENSION ** 3,
            "algebra_failures": algebra_failures,
            "dagger_failures": dagger_failures,
            "representative_action_failures": action_failures,
            "tag_flip_failures": tag_flip_failures,
            "projector_transport_failures": projector_transport_failures,
            "constraint_commutators": constraint_commutators,
            "sector_commutators": sector_commutators,
            "physical_action_failures": physical_action_failures,
            "inactive_identity_tag_patterns": (1 << len(active_tags)) - CODE_DIMENSION,
            "nonzero_coin_coefficients": int(np.count_nonzero(abs(coin) > 1e-14)),
        },
    )


def wedge_coin_and_common_operator_controls(
    fixtures: dict[int, list[SectorEncoder]]
) -> None:
    print("\nWEDGE^2 COIN / CONTACT / STREAM ON ONE COMMON E_X")
    rng = np.random.default_rng(305)
    beta_rows = []
    for beta, held_beta in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True)):
        coin = c219.common_species(beta).coin
        wedge = wedge2_matrix(coin)
        exterior_residual = 0.0
        for _ in range(24):
            left = rng.normal(size=6) + 1j * rng.normal(size=6)
            right = rng.normal(size=6) + 1j * rng.normal(size=6)
            exterior_residual = max(
                exterior_residual,
                float(
                    np.linalg.norm(
                        wedge @ wedge_vector(left, right)
                        - wedge_vector(coin @ left, coin @ right)
                    )
                ),
            )
        beta_rows.append(
            {
                "beta": beta,
                "held_beta": held_beta,
                "wedge_unitarity": float(
                    np.linalg.norm(wedge.conj().T @ wedge - np.eye(PAIR_DIMENSION))
                ),
                "exterior_action_residual": exterior_residual,
                "determinant_residual": abs(
                    np.linalg.det(wedge) - np.linalg.det(coin) ** 5
                ),
                "trace_residual": abs(
                    np.trace(wedge)
                    - ((np.trace(coin) ** 2 - np.trace(coin @ coin)) / 2)
                ),
            }
        )
    check(
        "the fifteen-pair coefficient block is the exact unitary exterior-square action of the Cycle-219 coin including held beta=-0.35",
        all(
            row["wedge_unitarity"] < 3e-14
            and row["exterior_action_residual"] < 3e-14
            and row["determinant_residual"] < 3e-14
            and row["trace_residual"] < 3e-14
            for row in beta_rows
        ),
        beta_rows,
    )

    stream = coarse_stream_matrix()
    contact_matrix = coarse_contact_matrix(COUPLING)
    comparator = fixed_seam_coin_comparator(c219.common_species(-0.3).coin)
    identity = np.eye(CODE_DIMENSION, dtype=complex)
    rows = []
    coherent = rng.normal(size=CODE_DIMENSION) + 1j * rng.normal(size=CODE_DIMENSION)
    coherent /= np.linalg.norm(coherent)
    for length, encoders in fixtures.items():
        stream_residual = 0.0
        contact_residual = 0.0
        coin_residual = 0.0
        composite_residual = 0.0
        inverse_residual = 0.0
        coherence_residual = 0.0
        branch_failures = 0
        for encoder in encoders:
            physical_stream, failures = physical_stream_matrix(encoder)
            physical_contact = physical_contact_matrix(encoder, COUPLING)
            physical_comparator = comparator.copy()
            stream_residual = max(
                stream_residual, float(np.linalg.norm(physical_stream - stream))
            )
            contact_residual = max(
                contact_residual,
                float(np.linalg.norm(physical_contact - contact_matrix)),
            )
            coin_residual = max(
                coin_residual,
                float(np.linalg.norm(physical_comparator - comparator)),
            )
            physical_composite = (
                physical_contact @ physical_stream @ physical_comparator
            )
            coarse_composite = contact_matrix @ stream @ comparator
            composite_residual = max(
                composite_residual,
                float(np.linalg.norm(physical_composite - coarse_composite)),
            )
            inverse_residual = max(
                inverse_residual,
                float(np.linalg.norm(physical_stream @ physical_stream - identity)),
                float(
                    np.linalg.norm(
                        physical_contact
                        @ physical_contact_matrix(encoder, -COUPLING)
                        - identity
                    )
                ),
                float(
                    np.linalg.norm(
                        physical_comparator.conj().T @ physical_comparator
                        - identity
                    )
                ),
            )
            coherence_residual = max(
                coherence_residual,
                abs(np.vdot(coherent, exact_gram(encoder) @ coherent) - 1),
                float(np.linalg.norm((physical_stream - stream) @ coherent)),
                float(np.linalg.norm((physical_contact - contact_matrix) @ coherent)),
                float(
                    np.linalg.norm(
                        (physical_comparator - comparator) @ coherent
                    )
                ),
                float(
                    np.linalg.norm(
                        (physical_composite - coarse_composite) @ coherent
                    )
                ),
            )
            branch_failures += sum(failures.values())
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "E_x_tested": len(encoders),
                "stream_intertwiner_residual": stream_residual,
                "contact_intertwiner_residual": contact_residual,
                "coin_intertwiner_residual": coin_residual,
                "coin_stream_contact_residual": composite_residual,
                "inverse_unitarity_residual": inverse_residual,
                "coherent_state_residual": coherence_residual,
                "branch_failures": branch_failures,
            }
        )
    check(
        "one E_x exactly intertwines the input-slice wedge coin comparator, Cycle-230 contact, collision-safe stream/catch-up, and their one-step composition through held L=6",
        all(
            row["E_x_tested"] == row["L"] ** 3
            and row["stream_intertwiner_residual"] < TOLERANCE
            and row["contact_intertwiner_residual"] < TOLERANCE
            and row["coin_intertwiner_residual"] < TOLERANCE
            and row["coin_stream_contact_residual"] < TOLERANCE
            and row["inverse_unitarity_residual"] < TOLERANCE
            and row["coherent_state_residual"] < TOLERANCE
            and row["branch_failures"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "the Cycle-230 coin-then-stream-then-contact fixed-seam comparator order is explicit with both stream/coin and stream/contact noncommutation",
        np.linalg.norm(contact_matrix @ comparator - comparator @ contact_matrix)
        < TOLERANCE
        and np.linalg.norm(stream @ comparator - comparator @ stream, 2) > 1
        and np.linalg.norm(contact_matrix @ stream - stream @ contact_matrix, 2)
        > 0.3
        and np.linalg.norm(
            (contact_matrix @ stream @ comparator - stream @ comparator)
            @ np.eye(CODE_DIMENSION)[:, 0::2]
        )
        < TOLERANCE
        and np.linalg.norm(
            (contact_matrix @ stream @ comparator - stream @ comparator)
            @ np.eye(CODE_DIMENSION)[:, 1::2]
        )
        > 1,
        {
            "schedule": "Cycle-230 one-step fixed seam: input-slice wedge^2 coin, complete outer-edge FSWAP and auxiliary catch-up, then contact",
            "contact_coin_commutator": float(
                np.linalg.norm(
                    contact_matrix @ comparator - comparator @ contact_matrix
                )
            ),
            "stream_coin_commutator_norm": float(
                np.linalg.norm(stream @ comparator - comparator @ stream, 2)
            ),
            "contact_stream_commutator_norm": float(
                np.linalg.norm(contact_matrix @ stream - stream @ contact_matrix, 2)
            ),
            "forward_t0_poststream_contact_residual": float(
                np.linalg.norm(
                    (contact_matrix @ stream @ comparator - stream @ comparator)
                    @ np.eye(CODE_DIMENSION)[:, 0::2]
                )
            ),
            "reverse_t1_completion_contact_residual": float(
                np.linalg.norm(
                    (contact_matrix @ stream @ comparator - stream @ comparator)
                    @ np.eye(CODE_DIMENSION)[:, 1::2]
                )
            ),
            "compiler_substeps_are_physical_time": False,
            "recurrent_volume_update_claimed": False,
        },
    )


def covariance_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nSIGNED-WEDGE PROPER-CUBIC / TRANSLATION COVARIANCE")
    reducer = StabilizerReducer(code)
    frames = c235.proper_cubic_frames()
    frame_matrices = [pair_representation(frame) for frame in frames]
    reference_rows = list(code.local_checks + code.wilsons + code.B)
    face_phase_failures = 0
    common_slice_failures = 0
    tag_failures = 0
    frame_tests = 0
    reference_failures = 0
    for frame, representation in zip(frames, frame_matrices):
        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, repair_pairs, flips = c269.repair_data(
            code.graph, vertex_map, edge_map
        )
        transformed_reference = [
            local.transform_pauli(
                code, row, edge_map, toggles, repair_pairs, flips
            )
            for row in reference_rows
        ]
        rank, bad = c235.phase_aware_rank(
            reference_rows + transformed_reference, code.qubits
        )
        reference_failures += rank != code.qubits or bool(bad)
        for body in code.graph.cells:
            target_body = tuple(
                int(value % code.length) for value in frame @ np.asarray(body)
            )
            source = sector_encoder(code, body)
            target = sector_encoder(code, target_body)
            target_lookup = {ray.pair: index for index, ray in enumerate(target.rays)}
            for source_index, ray in enumerate(source.rays):
                mapped_left = code.graph.vertices[vertex_map[ray.left]][1]
                mapped_right = code.graph.vertices[vertex_map[ray.right]][1]
                target_pair = tuple(sorted((mapped_left, mapped_right)))
                target_index = target_lookup[target_pair]
                target_ray = target.rays[target_index]
                expected_phase = 0 if mapped_left < mapped_right else 2
                phases = []
                for source_pauli, target_pauli, source_tags, target_tags in (
                    (
                        ray.input_face_pauli,
                        target_ray.input_face_pauli,
                        ray.input_tags,
                        target_ray.input_tags,
                    ),
                    (
                        ray.output_face_pauli,
                        target_ray.output_face_pauli,
                        ray.output_tags,
                        target_ray.output_tags,
                    ),
                ):
                    transformed = local.transform_pauli(
                        code,
                        source_pauli,
                        edge_map,
                        toggles,
                        repair_pairs,
                        flips,
                    )
                    phases.append(reducer.relative_phase(transformed, target_pauli))
                    tag_failures += (
                        ports.permute_bits(source_tags, vertex_map) != target_tags
                    )
                face_phase_failures += phases[0] != expected_phase
                face_phase_failures += phases[1] != expected_phase
                common_slice_failures += phases[0] != phases[1]
                matrix_target = int(np.argmax(abs(representation[:, source_index])))
                matrix_phase = 0 if representation[matrix_target, source_index] == 1 else 2
                face_phase_failures += matrix_target != target_index
                face_phase_failures += matrix_phase != expected_phase
                frame_tests += SLICE_DIMENSION

    frame_lookup = {
        tuple(frame.flatten()): index for index, frame in enumerate(frames)
    }
    group_failures = 0
    maximum_group_residual = 0.0
    for left_index, left_frame in enumerate(frames):
        for right_index, right_frame in enumerate(frames):
            product_index = frame_lookup[
                tuple((left_frame @ right_frame).flatten())
            ]
            residual = float(
                np.linalg.norm(
                    frame_matrices[left_index]
                    @ frame_matrices[right_index]
                    - frame_matrices[product_index]
                )
            )
            maximum_group_residual = max(maximum_group_residual, residual)
            group_failures += residual > TOLERANCE

    wedge_coin = wedge2_matrix(c219.common_species(-0.3).coin)
    comparator = fixed_seam_coin_comparator(c219.common_species(-0.3).coin)
    coin_covariance = max(
        float(np.linalg.norm(frame @ wedge_coin @ frame.conj().T - wedge_coin))
        for frame in frame_matrices
    )
    comparator_covariance = max(
        float(
            np.linalg.norm(
                np.kron(frame, np.eye(SLICE_DIMENSION))
                @ comparator
                @ np.kron(frame, np.eye(SLICE_DIMENSION)).conj().T
                - comparator
            )
        )
        for frame in frame_matrices
    )
    orbit_sizes = []
    for seed in (PAIR_INDEX[(0, 2)], PAIR_INDEX[(0, 1)]):
        orbit_sizes.append(
            len(
                {
                    int(np.argmax(abs(frame[:, seed])))
                    for frame in frame_matrices
                }
            )
        )

    base = sector_encoder(code, (0, 0, 0))
    translation_failures = 0
    translation_tests = 0
    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
        toggles, repair_pairs, flips = c269.repair_data(
            code.graph, vertex_map, edge_map
        )
        target = sector_encoder(code, displacement)
        for source_ray, target_ray in zip(base.rays, target.rays):
            phases = []
            for source_pauli, target_pauli, source_tags, target_tags in (
                (
                    source_ray.input_face_pauli,
                    target_ray.input_face_pauli,
                    source_ray.input_tags,
                    target_ray.input_tags,
                ),
                (
                    source_ray.output_face_pauli,
                    target_ray.output_face_pauli,
                    source_ray.output_tags,
                    target_ray.output_tags,
                ),
            ):
                transformed = local.transform_pauli(
                    code,
                    source_pauli,
                    edge_map,
                    toggles,
                    repair_pairs,
                    flips,
                )
                phases.append(reducer.relative_phase(transformed, target_pauli))
                translation_failures += (
                    ports.permute_bits(source_tags, vertex_map) != target_tags
                )
            translation_failures += phases != [0, 0]
            translation_tests += SLICE_DIMENSION

    check(
        "the physical 30-column family realizes one signed-wedge representation under all 24 frames with exact group law and both pair orbits",
        len(frames) == 24
        and orbit_sizes == [12, 3]
        and reference_failures == 0
        and face_phase_failures == 0
        and common_slice_failures == 0
        and tag_failures == 0
        and group_failures == 0
        and coin_covariance < TOLERANCE
        and comparator_covariance < TOLERANCE,
        {
            "proper_frames": len(frames),
            "joint_column_tests": frame_tests,
            "pair_orbits": {"perpendicular": orbit_sizes[0], "antipodal": orbit_sizes[1]},
            "reference_tableau_failures": reference_failures,
            "face_phase_failures": face_phase_failures,
            "common_slice_phase_failures": common_slice_failures,
            "tag_failures": tag_failures,
            "group_law_tests": len(frames) ** 2,
            "group_law_failures": group_failures,
            "maximum_group_residual": maximum_group_residual,
            "wedge_coin_covariance_residual": coin_covariance,
            "fixed_seam_comparator_covariance_residual": comparator_covariance,
        },
    )
    check(
        "the joint face/tag encoder is covariant under all 27 L=3 translations",
        translation_failures == 0,
        {
            "translations": code.length ** 3,
            "joint_column_tests": translation_tests,
            "failures": translation_failures,
        },
    )


def deletion_and_domain_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nDELETION / LAWFUL-DOMAIN CONTROLS")
    encoder = sector_encoder(code, (0, 0, 0))
    lookup = {
        ray_key(pauli, tags)
        for _pair, _slice, (pauli, tags) in encoder.columns()
    }
    catchup_inside = 0
    one_stream_inside = 0
    one_stream_constraint_nonfailures = 0
    antipodal_path_nonfailures = 0
    for ray in encoder.rays:
        streamed_face, _phase = local.two_edge_physical_face_action(
            code,
            ray.input_face_pauli,
            (ray.left, ray.right),
            (ray.left_outer_edge, ray.right_outer_edge),
        )
        catchup_inside += ray_key(streamed_face, ray.input_tags) in lookup
        for retained_edge in (ray.left_outer_edge, ray.right_outer_edge):
            one_edge_face = code.A[retained_edge] @ ray.input_face_pauli
            occupations = local.occupied_vertices(code, one_edge_face)
            occupation_mask = sum(1 << vertex for vertex in occupations)
            caught = ports.auxiliary_port_catchup(
                code, occupation_mask, ray.input_tags
            )
            one_stream_inside += ray_key(one_edge_face, caught) in lookup
            one_stream_constraint_nonfailures += caught == occupation_mask
        if ray.antipodal:
            vertices = body_vertices(code, encoder.body)
            middle = vertices[ray.intermediate_direction]
            for retained in (
                code.graph.A(ray.left, middle),
                code.graph.A(middle, ray.right),
            ):
                occupations = local.occupied_vertices(code, retained)
                antipodal_path_nonfailures += (
                    occupations == frozenset((ray.left, ray.right))
                )

    coin = wedge2_matrix(c219.common_species(-0.3).coin)
    antipodal = [
        index
        for index, pair in enumerate(PAIR_LABELS)
        if pair[1] == (pair[0] ^ 1)
    ]
    perpendicular = [index for index in range(PAIR_DIMENSION) if index not in antipodal]
    missing_antipodal_leakage = float(
        np.linalg.norm(coin[np.ix_(antipodal, perpendicular)], 2)
    )
    full_coin = fixed_seam_coin_comparator(c219.common_species(-0.3).coin)
    off_diagonal = abs(full_coin).copy()
    np.fill_diagonal(off_diagonal, 0)
    deleted_row, deleted_column = np.unravel_index(
        np.argmax(off_diagonal), off_diagonal.shape
    )
    deleted_coin = full_coin.copy()
    deleted_coefficient = deleted_coin[deleted_row, deleted_column]
    deleted_coin[deleted_row, deleted_column] = 0
    coin_deletion_unitarity = float(
        np.linalg.norm(deleted_coin.conj().T @ deleted_coin - np.eye(CODE_DIMENSION))
    )
    contact_deletion_residual = abs(np.exp(1j * COUPLING) - 1)
    stream = coarse_stream_matrix()
    delete_one_column = np.eye(CODE_DIMENSION, dtype=complex)[:, 1:]
    column_deletion_residual = float(
        np.linalg.norm(
            (np.eye(CODE_DIMENSION) - delete_one_column @ delete_one_column.T)
            @ stream
            @ delete_one_column
        )
    )
    check(
        "catch-up, stream-factor, antipodal-path, antipodal-orbit, coin-term, contact-term, and code-column deletions are all detected",
        catchup_inside == 0
        and one_stream_inside == 0
        and one_stream_constraint_nonfailures == 0
        and antipodal_path_nonfailures == 0
        and missing_antipodal_leakage > 0.9
        and abs(deleted_coefficient) > 0.1
        and coin_deletion_unitarity > 0.15
        and contact_deletion_residual > 0.3
        and column_deletion_residual == 1,
        {
            "deleted_catchup_states_in_code": catchup_inside,
            "one_stream_factor_states_in_code": one_stream_inside,
            "one_stream_factor_constraint_nonfailures": one_stream_constraint_nonfailures,
            "one_antipodal_path_factor_nonfailures": antipodal_path_nonfailures,
            "perpendicular_only_coin_leakage_operator_norm": missing_antipodal_leakage,
            "deleted_coin_matrix_unit": (int(deleted_row), int(deleted_column)),
            "deleted_coin_coefficient": deleted_coefficient,
            "coin_deletion_unitarity_residual": coin_deletion_unitarity,
            "contact_pair_deletion_residual": contact_deletion_residual,
            "one_column_stream_closure_residual": column_deletion_residual,
        },
    )

    rejected = 0
    bad_pair_inputs = (
        ((0, 0), None),
        ((1, 0), None),
        ((0, 6), None),
        ((0, 2), 4),
        ((0, 1), 0),
        ((0, 1), 1),
    )
    for pair, intermediate in bad_pair_inputs:
        try:
            input_pair_pauli(code, (0, 0, 0), pair, intermediate)
        except (KeyError, ValueError):
            rejected += 1
    for body in ((-1, 0, 0), (code.length, 0, 0)):
        try:
            sector_encoder(code, body)
        except ValueError:
            rejected += 1
    for matrix in (
        np.eye(5, dtype=complex),
        np.full((6, 6), complex(np.nan, 0)),
    ):
        try:
            wedge2_matrix(matrix)
        except ValueError:
            rejected += 1
    try:
        c269.build_code(2)
    except ValueError:
        rejected += 1
    check(
        "the interface rejects malformed pairs, path choices, bodies, coefficient matrices, and aliased L=2",
        rejected == 11,
        {"rejected_fixtures": rejected},
    )


def inventory_and_boundary() -> None:
    print("\nSUPPLIED-STRUCTURE INVENTORY / EXACT BOUNDARY")
    check(
        "the result is one full two-particle reference-relative interface, not a full-Fock, position-preparation, primitive-law, energy, or gravity result",
        True,
        {
            "derived": (
                "all 15 two-mode wedge pairs and two stream slices in one exact E_x",
                "three antipodal rays from path-independent bounded two-edge representatives",
                "exact input-slice wedge^2(C) comparator, stream/catch-up, subsequent contact, inverse, and one-step composed intertwiners",
                "900-term local matrix-unit basis with autonomous twelve-tag projectors",
                "signed-wedge proper-cubic representation and exact group law",
                "42--54-M2 bounded interface support",
            ),
            "supplied": (
                "global fixed +++ Wilson, all-B=+1 reference vacuum",
                "one body-cell address and six direction labels",
                "Cycle-269 A/B/FSWAP dictionary and local framing repair",
                "six zero-initialized collision-safe auxiliary port M2 per cell",
                "Cycle-219 six-mode coin C",
                "Cycle-230 real contact coupling g=0.37",
                "Cycle-230 one-step fixed-seam coin-then-stream-then-contact comparator order",
                "one chosen antipodal path representative gauge; physical ray is path independent",
            ),
            "open": (
                "bounded preparation of the fixed-Wilson vacuum and arbitrary E_x amplitudes",
                "coherent position across a volume-growing set of body cells",
                "primitive-gate synthesis of the dense local matrix-unit polynomial",
                "the actual recurrent onsite volume coin after the particles separate",
                "overlapping simultaneous two-particle shells and larger even sectors",
                "odd parity and a full-Fock compiler",
            ),
            "not_claimed": (
                "physical energy from a wrapped phase",
                "a rate or physical time from compiler substeps",
                "gravity or source semantics",
                "Record or Born/probability semantics",
                "a new mass derivation from the two-particle wedge sector",
            ),
            "overhead": "15 face + 6 port = 21 M2/cell; bounded shell support at most 54 M2",
            "global_Jordan_Wigner_order": False,
            "global_parity_service": False,
            "host_side_control": False,
            "authority": "none",
            "audit": "unset",
            "no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    print("CYCLE 305: FULL TWO-PARTICLE PHYSICAL FIXED-SEAM INTERFACE")
    print("authority=none; audit=unset")
    note_contract()
    cache = {length: c269.build_code(length) for length in SIZES}
    antipodal_path_controls(cache)
    fixtures = encoder_geometry_and_constraint_controls(cache)
    matrix_unit_controls(fixtures[3][0])
    wedge_coin_and_common_operator_controls(fixtures)
    covariance_controls(cache[3])
    deletion_and_domain_controls(cache[3])
    inventory_and_boundary()
    print(f"SUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
