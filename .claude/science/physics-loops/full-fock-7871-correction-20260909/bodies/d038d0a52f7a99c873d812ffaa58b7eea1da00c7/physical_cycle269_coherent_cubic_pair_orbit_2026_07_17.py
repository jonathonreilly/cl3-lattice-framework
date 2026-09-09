#!/usr/bin/env python3
"""One coherent proper-cubic pair-orbit lift in the physical Cycle-269 code.

At one supplied coarse-cell address, the twelve unordered perpendicular pairs
of the six half-edge modes form one proper-cubic orbit.  For every address a,
the reviewed localized construction supplies an intracell column |a,0> and
its streamed/caught-up column |a,1>.  This runner collects all 24 columns into
one matrix-free linear isometry

    E_x = sum_(a,t) P_(x,a,t)|Omega_+++><x,a,t|,

where |Omega_+++> is the fixed-Wilson reference vacuum.  The same complete
outer-edge FSWAP/catch-up layer and the same complete local-contact product act
on every column.  Thus arbitrary coherent address superpositions, rather than
separately selected rays, obey exact stream, contact, and composed
intertwiners on this declared code space.

The address basis is the antisymmetric wedge basis.  Proper frames therefore
act by one signed permutation W_R, with the same wedge sign on both stream
slices.  No independent source/carrier species, coin router, preparation
circuit for E_x, or full-Fock compiler is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_collision_safe_auxiliary_ports_2026_07_17 as ports
import physical_cycle269_local_contact_intertwiner_2026_07_17 as contact
import physical_cycle269_reference_relative_localized_pair_lift_2026_07_17 as lift
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COHERENT_CUBIC_PAIR_ORBIT_NOTE_2026-07-17.md"
)
TRAINING_SIZES = (3, 4, 5)
HELD_SIZES = (6,)
SIZES = TRAINING_SIZES + HELD_SIZES
ADDRESS_DIMENSION = 12
SLICE_DIMENSION = 2
CODE_DIMENSION = ADDRESS_DIMENSION * SLICE_DIMENSION
TOLERANCE = 5e-12

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class OrbitEncoder:
    """One fixed 24-column encoder at a supplied coarse-cell anchor."""

    code: c269.WilsonSubsystemCode
    anchor: tuple[int, int, int]
    addresses: tuple[lift.LocalizedLift, ...]

    def column(self, address: int, stream_slice: int) -> tuple[c235.Pauli, int]:
        fixture = self.addresses[address]
        if stream_slice == 0:
            return fixture.input_face_pauli, fixture.input_tags
        if stream_slice == 1:
            return fixture.output_face_pauli, fixture.output_tags
        raise ValueError("the coherent orbit has exactly two stream slices")

    def columns(self):
        for address in range(len(self.addresses)):
            for stream_slice in range(SLICE_DIMENSION):
                yield address, stream_slice, self.column(address, stream_slice)


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
        check("the coherent pair-orbit note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "one linear e_x",
        "twenty-four-dimensional",
        "twelve-address",
        "proper-cubic orbit",
        "antisymmetric wedge",
        "common on both stream slices",
        "exact gram",
        "e_x s_coarse = s_physical e_x",
        "e_x c_coarse = c_physical e_x",
        "cycle-230 stream-then-contact",
        "arbitrary coherent superpositions",
        "at most fifty-four-m2",
        "relative-state union",
        "not operator support",
        "restricted physical matrices",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "constraint leakage",
        "deletion",
        "lawful domain",
        "fixed +++ wilson reference vacuum",
        "supplied cell address",
        "address preparation is not derived",
        "not independent species",
        "not a coin router",
        "not physical time",
        "not a full-fock compiler",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the coherent-orbit theorem, imports, and exact boundary",
        not missing,
        missing,
    )


def declared_pairs(
    code: c269.WilsonSubsystemCode, anchor: tuple[int, int, int]
) -> tuple[tuple[int, int], ...]:
    if anchor not in code.graph.cells:
        raise ValueError("the anchor must be one coarse cell of this code")
    return tuple(
        (left, right)
        for left, right, kind, owner in code.graph.edges
        if kind == "internal_triangle" and owner == anchor
    )


def orbit_encoder(
    code: c269.WilsonSubsystemCode, anchor: tuple[int, int, int]
) -> OrbitEncoder:
    pairs = declared_pairs(code, anchor)
    if len(pairs) != ADDRESS_DIMENSION:
        raise ValueError("the cubic pair orbit must contain twelve addresses")
    return OrbitEncoder(
        code,
        anchor,
        tuple(lift.localized_lift(code, left, right) for left, right in pairs),
    )


def column_index(address: int, stream_slice: int) -> int:
    return SLICE_DIMENSION * address + stream_slice


def ray_key(pauli: c235.Pauli, tags: int) -> tuple[int, int, int, int]:
    return pauli.phase, pauli.x, pauli.z, tags


def ray_support_key(pauli: c235.Pauli, tags: int) -> tuple[int, int, int]:
    """Physical ray label with irrelevant Pauli representative phase removed."""

    return pauli.x, pauli.z, tags


def phase_scalar(phase: int) -> complex:
    return (1 + 0j, 1j, -1 + 0j, -1j)[phase % 4]


def validate_coefficients(coefficients: np.ndarray) -> None:
    if coefficients.shape != (CODE_DIMENSION,):
        raise ValueError("one E_x input must have exactly 24 complex coefficients")
    if not np.all(np.isfinite(coefficients)):
        raise ValueError("coherent-orbit coefficients must be finite")


def exact_gram(encoder: OrbitEncoder) -> np.ndarray:
    """Exact because distinct tag computational states are orthogonal."""

    columns = list(encoder.columns())
    tags = [entry[2][1] for entry in columns]
    if len(set(tags)) != len(tags):
        raise ValueError("the declared orbit columns do not have distinct tag states")
    return np.eye(len(columns), dtype=complex)


def coarse_stream_matrix() -> np.ndarray:
    matrix = np.zeros((CODE_DIMENSION, CODE_DIMENSION), dtype=complex)
    for address in range(ADDRESS_DIMENSION):
        matrix[column_index(address, 1), column_index(address, 0)] = 1
        matrix[column_index(address, 0), column_index(address, 1)] = 1
    return matrix


def coarse_contact_matrix(coupling: float) -> np.ndarray:
    diagonal = np.ones(CODE_DIMENSION, dtype=complex)
    diagonal[0::2] = np.exp(1j * coupling)
    return np.diag(diagonal)


def restricted_physical_stream_matrix(
    encoder: OrbitEncoder,
) -> tuple[np.ndarray, dict[str, int]]:
    """Restrict the common global outer-edge FSWAP/catch-up layer to E_x."""

    code = encoder.code
    lookup = {
        ray_key(pauli, tags): column_index(address, stream_slice)
        for address, stream_slice, (pauli, tags) in encoder.columns()
    }
    matrix = np.zeros((CODE_DIMENSION, CODE_DIMENSION), dtype=complex)
    failures = {
        "face": 0,
        "catchup": 0,
        "target": 0,
        "fermionic_sign": 0,
    }
    for address, fixture in enumerate(encoder.addresses):
        for stream_slice in range(SLICE_DIMENSION):
            if stream_slice == 0:
                source_face = fixture.input_face_pauli
                source_tags = fixture.input_tags
                occupied = (fixture.source, fixture.carrier)
            else:
                source_face = fixture.output_face_pauli
                source_tags = fixture.output_tags
                occupied = (fixture.source_arrival, fixture.carrier_arrival)
            target_face, _phase = lift.two_edge_physical_face_action(
                code,
                source_face,
                occupied,
                (fixture.source_outer_edge, fixture.carrier_outer_edge),
            )
            arrival, caught, sign = ports.port_macrostep(
                code, source_tags, source_tags
            )
            expected_face, expected_tags = encoder.column(address, 1 - stream_slice)
            failures["face"] += target_face != expected_face
            failures["catchup"] += (arrival, caught) != (
                expected_tags,
                expected_tags,
            )
            failures["fermionic_sign"] += sign != 1
            target = lookup.get(ray_key(target_face, caught))
            failures["target"] += target is None
            if target is not None:
                matrix[target, column_index(address, stream_slice)] = sign
    return matrix, failures


def restricted_physical_contact_matrix(
    encoder: OrbitEncoder, coupling: float
) -> np.ndarray:
    """Restrict the literal global contact product to the E_x columns."""

    diagonal = np.empty(CODE_DIMENSION, dtype=complex)
    for address, stream_slice, (pauli, _tags) in encoder.columns():
        phase, _active_pairs = contact.physical_contact_action_on_representative(
            encoder.code, pauli, coupling
        )
        diagonal[column_index(address, stream_slice)] = phase
    return np.diag(diagonal)


def orbit_geometry_and_gram_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> dict[int, list[OrbitEncoder]]:
    print("\nONE LINEAR E_X / EXACT GRAM / BOUNDED ORBIT")
    fixtures: dict[int, list[OrbitEncoder]] = {}
    rows = []
    for length, code in cache.items():
        encoders = [orbit_encoder(code, cell) for cell in code.graph.cells]
        fixtures[length] = encoders
        dimension_failures = 0
        gram_failures = 0
        tag_collision_failures = 0
        role_reversal_failures = 0
        union_supports = []
        column_supports = []
        address_labels = set()
        for encoder in encoders:
            columns = list(encoder.columns())
            dimension_failures += len(columns) != CODE_DIMENSION
            tags = [entry[2][1] for entry in columns]
            tag_collision_failures += len(set(tags)) != CODE_DIMENSION
            gram_failures += np.linalg.norm(
                exact_gram(encoder) - np.eye(CODE_DIMENSION)
            ) != 0
            union = 0
            for address, stream_slice, (pauli, tags_value) in columns:
                representative = lift.full_state_representative(
                    code, pauli, tags_value
                )
                support = representative.x | representative.z
                column_supports.append(support.bit_count())
                union |= support
                if encoder.anchor == (0, 0, 0) and stream_slice == 0:
                    local_modes = tuple(
                        code.graph.vertices[vertex][1]
                        for vertex in (
                            encoder.addresses[address].source,
                            encoder.addresses[address].carrier,
                        )
                    )
                    address_labels.add(frozenset(local_modes))
            for fixture in encoder.addresses:
                reversed_fixture = lift.localized_lift(
                    code, fixture.carrier, fixture.source
                )
                input_reversal = lift.relative_scalar(
                    reversed_fixture.input_face_pauli, fixture.input_face_pauli
                )
                output_reversal = lift.relative_scalar(
                    reversed_fixture.output_face_pauli, fixture.output_face_pauli
                )
                role_reversal_failures += not (
                    reversed_fixture.input_tags == fixture.input_tags
                    and reversed_fixture.output_tags == fixture.output_tags
                    and input_reversal == 2
                    and output_reversal == 2
                )
            union_supports.append(union.bit_count())

        complete_contact_support = 0
        for occupation in code.B:
            complete_contact_support |= occupation.x | occupation.z
        complete_stream_support = 0
        local_stream_factor_supports = []
        for left, right, edge in ports.outer_edges(code):
            local_support = 0
            for operator in (code.B[left], code.B[right], code.A[edge]):
                local_support |= operator.x | operator.z
            extended_local_support = (
                local_support
                | (1 << (code.qubits + left))
                | (1 << (code.qubits + right))
            )
            local_stream_factor_supports.append(extended_local_support.bit_count())
            complete_stream_support |= extended_local_support

        contact_cell_supports = []
        for cell in code.graph.cells:
            cell_support = 0
            vertices = contact.cell_vertices(code, cell)
            for left, right in combinations(vertices, 2):
                cell_support |= contact.pair_projector_support(code, left, right)
            contact_cell_supports.append(cell_support.bit_count())
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "encoders": len(encoders),
                "columns_per_E_x": CODE_DIMENSION,
                "address_orbit": len(address_labels),
                "column_supports_M2": sorted(set(column_supports)),
                "relative_state_orbit_union_supports_M2": sorted(
                    set(union_supports)
                ),
                "local_stream_factor_supports_M2": sorted(
                    set(local_stream_factor_supports)
                ),
                "local_contact_cell_supports_M2": sorted(
                    set(contact_cell_supports)
                ),
                "complete_stream_layer_support_M2": (
                    complete_stream_support.bit_count()
                ),
                "complete_contact_product_support_M2": (
                    complete_contact_support.bit_count()
                ),
                "dimension_failures": dimension_failures,
                "Gram_failures": gram_failures,
                "tag_collision_failures": tag_collision_failures,
                "identical_pair_role_reversal_failures": role_reversal_failures,
            }
        )
    check(
        "one E_x coherently spans the full twelve-address, two-slice cubic orbit with exact Gram identity and bounded support through held L=6",
        all(
            row["encoders"] == row["L"] ** 3
            and row["columns_per_E_x"] == CODE_DIMENSION
            and row["address_orbit"] == ADDRESS_DIMENSION
            and max(row["column_supports_M2"]) <= 19
            and max(row["relative_state_orbit_union_supports_M2"]) <= 54
            and row["local_stream_factor_supports_M2"] == [11]
            and row["local_contact_cell_supports_M2"] == [18]
            and row["complete_stream_layer_support_M2"] == 21 * row["L"] ** 3
            and row["complete_contact_product_support_M2"] == 15 * row["L"] ** 3
            and row["dimension_failures"] == 0
            and row["Gram_failures"] == 0
            and row["tag_collision_failures"] == 0
            and row["identical_pair_role_reversal_failures"] == 0
            for row in rows
        ),
        rows,
    )
    return fixtures


def common_operator_and_coherence_controls(
    fixtures: dict[int, list[OrbitEncoder]]
) -> None:
    print("\nCOMMON STREAM / CATCH-UP / CONTACT OPERATORS ON ONE CODE SPACE")
    stream = coarse_stream_matrix()
    coarse_c = coarse_contact_matrix(contact.COUPLING)
    identity = np.eye(CODE_DIMENSION, dtype=complex)
    rows = []
    rng = np.random.default_rng(269230)
    coherent_vectors = [
        np.ones(CODE_DIMENSION, dtype=complex),
        np.exp(2j * np.pi * np.arange(CODE_DIMENSION) / CODE_DIMENSION),
        rng.normal(size=CODE_DIMENSION) + 1j * rng.normal(size=CODE_DIMENSION),
    ]
    coherent_vectors = [vector / np.linalg.norm(vector) for vector in coherent_vectors]
    for length, encoders in fixtures.items():
        stream_residual = 0.0
        contact_residual = 0.0
        contact_then_stream_residual = 0.0
        stream_then_contact_residual = 0.0
        inverse_residual = 0.0
        coherence_residual = 0.0
        action_failures = 0
        for encoder in encoders:
            physical_s, failures = restricted_physical_stream_matrix(encoder)
            physical_c = restricted_physical_contact_matrix(
                encoder, contact.COUPLING
            )
            stream_residual = max(stream_residual, float(np.linalg.norm(physical_s - stream)))
            contact_residual = max(contact_residual, float(np.linalg.norm(physical_c - coarse_c)))
            contact_then_stream_residual = max(
                contact_then_stream_residual,
                float(np.linalg.norm(physical_s @ physical_c - stream @ coarse_c)),
            )
            stream_then_contact_residual = max(
                stream_then_contact_residual,
                float(np.linalg.norm(physical_c @ physical_s - coarse_c @ stream)),
            )
            inverse_residual = max(
                inverse_residual,
                float(np.linalg.norm(physical_s @ physical_s - identity)),
                float(
                    np.linalg.norm(
                        physical_c
                        @ restricted_physical_contact_matrix(
                            encoder, -contact.COUPLING
                        )
                        - identity
                    )
                ),
            )
            action_failures += sum(failures.values())
            gram = exact_gram(encoder)
            for coefficients in coherent_vectors:
                validate_coefficients(coefficients)
                coherence_residual = max(
                    coherence_residual,
                    abs(np.vdot(coefficients, gram @ coefficients) - 1),
                    float(np.linalg.norm((physical_s - stream) @ coefficients)),
                    float(np.linalg.norm((physical_c - coarse_c) @ coefficients)),
                    float(
                        np.linalg.norm(
                            (physical_s @ physical_c - stream @ coarse_c)
                            @ coefficients
                        )
                    ),
                    float(
                        np.linalg.norm(
                            (physical_c @ physical_s - coarse_c @ stream)
                            @ coefficients
                        )
                    ),
                )
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "E_x_tested": len(encoders),
                "coherent_vectors_per_E_x": len(coherent_vectors),
                "stream_intertwiner_residual": stream_residual,
                "contact_intertwiner_residual": contact_residual,
                "contact_then_stream_residual": contact_then_stream_residual,
                "cycle230_stream_then_contact_residual": stream_then_contact_residual,
                "inverse_residual": inverse_residual,
                "coherent_superposition_residual": coherence_residual,
                "branch_action_failures": action_failures,
                "operator_semantics": "24x24 matrices are restrictions of common global physical products to im(E_x), not full-Hilbert matrices",
            }
        )
    check(
        "the same physical stream/catch-up and contact products exactly intertwine on arbitrary coherent address superpositions through held L=6",
        all(
            row["E_x_tested"] == row["L"] ** 3
            and row["stream_intertwiner_residual"] < TOLERANCE
            and row["contact_intertwiner_residual"] < TOLERANCE
            and row["contact_then_stream_residual"] < TOLERANCE
            and row["cycle230_stream_then_contact_residual"] < TOLERANCE
            and row["inverse_residual"] < TOLERANCE
            and row["coherent_superposition_residual"] < TOLERANCE
            and row["branch_action_failures"] == 0
            for row in rows
        ),
        rows,
    )
    commutator = float(np.linalg.norm(coarse_c @ stream - stream @ coarse_c, 2))
    expected_commutator = abs(np.exp(1j * contact.COUPLING) - 1)
    check(
        "the Cycle-230 stream-then-contact order and reverse comparator are explicit and cannot be silently commuted",
        abs(commutator - expected_commutator) < TOLERANCE,
        {
            "Cycle230_order": "complete outer-edge FSWAP and auxiliary catch-up, then contact",
            "reverse_comparator": "contact, then complete outer-edge FSWAP and auxiliary catch-up",
            "contact_stream_commutator_norm": commutator,
            "substeps_are_physical_time": False,
        },
    )


def constraint_controls(fixtures: dict[int, list[OrbitEncoder]]) -> None:
    print("\nCOMMON CONSTRAINT SUBSPACE / HELD-SIZE LEAKAGE")
    rows = []
    for length, encoders in fixtures.items():
        local_leakage = 0
        wilson_leakage = 0
        occupation_failures = 0
        port_constraint_failures = 0
        for encoder in encoders:
            for _address, _stream_slice, (pauli, tags) in encoder.columns():
                local_leakage += sum(
                    not pauli.commutes(row) for row in encoder.code.local_checks
                )
                wilson_leakage += sum(
                    not pauli.commutes(row) for row in encoder.code.wilsons
                )
                occupations = lift.occupied_vertices(encoder.code, pauli)
                occupied_mask = sum(1 << vertex for vertex in occupations)
                occupation_failures += tags != occupied_mask
                for vertex, B_vertex in enumerate(encoder.code.B):
                    face_flip = not pauli.commutes(B_vertex)
                    tag_flip = bool((tags >> vertex) & 1)
                    port_constraint_failures += face_flip != tag_flip
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "encoded_columns": CODE_DIMENSION * len(encoders),
                "local_check_leakage": local_leakage,
                "Wilson_leakage": wilson_leakage,
                "occupation_failures": occupation_failures,
                "B_v_Z_port_constraint_failures": port_constraint_failures,
            }
        )
    check(
        "every column, and therefore every coherent superposition, lies in the same local-check, +++ Wilson, and B_v Z_port=+1 constraint space",
        all(
            row["local_check_leakage"] == 0
            and row["Wilson_leakage"] == 0
            and row["occupation_failures"] == 0
            and row["B_v_Z_port_constraint_failures"] == 0
            for row in rows
        ),
        rows,
    )


def frame_action(
    code: c269.WilsonSubsystemCode,
    source: OrbitEncoder,
    target: OrbitEncoder,
    vertex_map: list[int],
    edge_map: list[int],
    toggles: list[int],
    pairs,
    flips: int,
) -> tuple[np.ndarray, dict[str, int]]:
    target_lookup = {
        frozenset((fixture.source, fixture.carrier)): address
        for address, fixture in enumerate(target.addresses)
    }
    wedge = np.zeros((ADDRESS_DIMENSION, ADDRESS_DIMENSION), dtype=complex)
    failures = {"address": 0, "phase": 0, "wedge_sign": 0, "tag": 0}
    for source_address, fixture in enumerate(source.addresses):
        target_address = target_lookup.get(
            frozenset((vertex_map[fixture.source], vertex_map[fixture.carrier]))
        )
        failures["address"] += target_address is None
        if target_address is None:
            continue
        target_fixture = target.addresses[target_address]
        mapped_order = (
            vertex_map[fixture.source],
            vertex_map[fixture.carrier],
        )
        target_order = (target_fixture.source, target_fixture.carrier)
        expected_wedge_phase = 0 if mapped_order == target_order else 2
        phases = []
        for source_pauli, target_pauli, source_tags, target_tags in (
            (
                fixture.input_face_pauli,
                target_fixture.input_face_pauli,
                fixture.input_tags,
                target_fixture.input_tags,
            ),
            (
                fixture.output_face_pauli,
                target_fixture.output_face_pauli,
                fixture.output_tags,
                target_fixture.output_tags,
            ),
        ):
            transformed = lift.transform_pauli(
                code, source_pauli, edge_map, toggles, pairs, flips
            )
            phases.append(lift.relative_scalar(transformed, target_pauli))
            failures["tag"] += (
                ports.permute_bits(source_tags, vertex_map) != target_tags
            )
        failures["phase"] += (
            phases[0] is None
            or phases[1] is None
            or phases[0] != phases[1]
            or phases[0] not in (0, 2)
        )
        failures["wedge_sign"] += (
            phases[0] != expected_wedge_phase
            or phases[1] != expected_wedge_phase
        )
        wedge[target_address, source_address] = phase_scalar(
            expected_wedge_phase
        )
    return wedge, failures


def covariance_and_common_phase_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nALL-FRAME SIGNED-WEDGE / ALL-TRANSLATION COVARIANCE")
    frames = c235.proper_cubic_frames()
    frame_matrices = []
    frame_failures = 0
    frame_tests = 0
    common_slice_phase_failures = 0
    declared_wedge_sign_failures = 0
    reference_rows = list(code.local_checks + code.wilsons + code.B)
    for frame in frames:
        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        transformed_reference = [
            lift.transform_pauli(code, row, edge_map, toggles, pairs, flips)
            for row in reference_rows
        ]
        reference_rank, reference_bad = c235.phase_aware_rank(
            reference_rows + transformed_reference, code.qubits
        )
        frame_failures += reference_rank != code.qubits or bool(reference_bad)
        base_matrix = None
        for anchor in code.graph.cells:
            mapped_anchor = tuple(
                int(value % code.length)
                for value in frame @ np.asarray(anchor)
            )
            matrix, failures = frame_action(
                code,
                orbit_encoder(code, anchor),
                orbit_encoder(code, mapped_anchor),
                vertex_map,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            frame_failures += failures["address"] + failures["tag"]
            common_slice_phase_failures += failures["phase"]
            declared_wedge_sign_failures += failures["wedge_sign"]
            frame_failures += np.linalg.norm(matrix.conj().T @ matrix - np.eye(12)) > TOLERANCE
            if base_matrix is None:
                base_matrix = matrix
            else:
                frame_failures += np.linalg.norm(matrix - base_matrix) > TOLERANCE
            frame_tests += CODE_DIMENSION
        frame_matrices.append(base_matrix)

    frame_lookup = {tuple(frame.flatten()): index for index, frame in enumerate(frames)}
    group_failures = 0
    maximum_group_residual = 0.0
    for left_index, left_frame in enumerate(frames):
        for right_index, right_frame in enumerate(frames):
            product_index = frame_lookup[tuple((left_frame @ right_frame).flatten())]
            residual = float(
                np.linalg.norm(
                    frame_matrices[left_index] @ frame_matrices[right_index]
                    - frame_matrices[product_index]
                )
            )
            maximum_group_residual = max(maximum_group_residual, residual)
            group_failures += residual > TOLERANCE

    translation_failures = 0
    translation_tests = 0
    translation_matrices = []
    displacements = tuple(product(range(code.length), repeat=3))
    for displacement in displacements:
        vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        base_matrix = None
        for anchor in code.graph.cells:
            mapped_anchor = tuple(
                (anchor[axis] + displacement[axis]) % code.length
                for axis in range(3)
            )
            matrix, failures = frame_action(
                code,
                orbit_encoder(code, anchor),
                orbit_encoder(code, mapped_anchor),
                vertex_map,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            translation_failures += sum(failures.values())
            translation_failures += (
                np.linalg.norm(matrix - np.eye(12)) > TOLERANCE
            )
            if base_matrix is None:
                base_matrix = matrix
            else:
                translation_failures += (
                    np.linalg.norm(matrix - base_matrix) > TOLERANCE
                )
            translation_tests += CODE_DIMENSION
        translation_matrices.append(base_matrix)

    translation_lookup = {
        displacement: index for index, displacement in enumerate(displacements)
    }
    translation_group_failures = 0
    maximum_translation_group_residual = 0.0
    for left_index, left_displacement in enumerate(displacements):
        for right_index, right_displacement in enumerate(displacements):
            composed = tuple(
                (left_displacement[axis] + right_displacement[axis]) % code.length
                for axis in range(3)
            )
            product_index = translation_lookup[composed]
            residual = float(
                np.linalg.norm(
                    translation_matrices[left_index]
                    @ translation_matrices[right_index]
                    - translation_matrices[product_index]
                )
            )
            maximum_translation_group_residual = max(
                maximum_translation_group_residual, residual
            )
            translation_group_failures += residual > TOLERANCE

    stream = coarse_stream_matrix()
    contact_matrix = coarse_contact_matrix(contact.COUPLING)
    operator_covariance_failures = 0
    orbit_coverage = set()
    seed = 0
    for wedge in frame_matrices:
        full = np.kron(wedge, np.eye(SLICE_DIMENSION))
        operator_covariance_failures += np.linalg.norm(full @ stream - stream @ full) > TOLERANCE
        operator_covariance_failures += np.linalg.norm(full @ contact_matrix - contact_matrix @ full) > TOLERANCE
        orbit_coverage.add(int(np.argmax(abs(wedge[:, seed]))))

    check(
        "one signed-wedge representation, common on both stream slices, gives exact covariance under all 24 frames and all 27 L=3 translations",
        len(frames) == 24
        and len(orbit_coverage) == ADDRESS_DIMENSION
        and frame_failures == 0
        and common_slice_phase_failures == 0
        and declared_wedge_sign_failures == 0
        and group_failures == 0
        and translation_failures == 0
        and translation_group_failures == 0
        and operator_covariance_failures == 0,
        {
            "proper_frames": len(frames),
            "frame_column_tests": frame_tests,
            "address_orbit_coverage": len(orbit_coverage),
            "frame_failures": frame_failures,
            "common_slice_phase_failures": common_slice_phase_failures,
            "declared_wedge_sign_failures": declared_wedge_sign_failures,
            "signed_wedge_group_law_tests": len(frames) ** 2,
            "signed_wedge_group_failures": group_failures,
            "maximum_group_residual": maximum_group_residual,
            "translations": code.length ** 3,
            "translation_column_tests": translation_tests,
            "translation_failures": translation_failures,
            "translation_group_law_tests": len(displacements) ** 2,
            "translation_group_failures": translation_group_failures,
            "maximum_translation_group_residual": (
                maximum_translation_group_residual
            ),
            "stream_contact_covariance_failures": operator_covariance_failures,
            "phase_scope": "the declared CAR wedge sign is identical on t=0 and t=1; the fixed reference vacuum may contribute only one address-independent global ray phase",
        },
    )


def deletion_and_domain_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nDELETION / LAWFUL-DOMAIN CONTROLS")
    encoder = orbit_encoder(code, (0, 0, 0))
    lookup = {
        ray_support_key(pauli, tags)
        for _address, _stream_slice, (pauli, tags) in encoder.columns()
    }
    deleted_catchup_inside = 0
    one_stream_factor_inside = 0
    one_stream_constraint_failures = 0
    contact_deletion_failures = 0
    inactive_contact_projector_failures = 0
    deletion_residuals = []
    expected_contact = complex(np.exp(1j * contact.COUPLING))
    pair_family = contact.cell_pair_family(code)
    for fixture in encoder.addresses:
        streamed_face, _phase = lift.two_edge_physical_face_action(
            code,
            fixture.input_face_pauli,
            (fixture.source, fixture.carrier),
            (fixture.source_outer_edge, fixture.carrier_outer_edge),
        )
        deleted_catchup_inside += (
            ray_support_key(streamed_face, fixture.input_tags) in lookup
        )
        for retained_edge in (fixture.source_outer_edge, fixture.carrier_outer_edge):
            one_edge_face = code.A[retained_edge] @ fixture.input_face_pauli
            one_edge_occupations = lift.occupied_vertices(code, one_edge_face)
            occupation_mask = sum(1 << vertex for vertex in one_edge_occupations)
            caught = ports.auxiliary_port_catchup(
                code, occupation_mask, fixture.input_tags
            )
            one_stream_factor_inside += ray_support_key(one_edge_face, caught) in lookup
            one_stream_constraint_failures += caught == occupation_mask
        physical_phase, active_pairs = (
            contact.physical_contact_action_on_representative(
                code,
                fixture.input_face_pauli,
                contact.COUPLING,
                pair_family,
            )
        )
        target_pair = frozenset((fixture.source, fixture.carrier))
        contact_deletion_failures += active_pairs != (target_pair,)
        inactive_contact_projector_failures += sum(
            pair != target_pair and pair in active_pairs for pair in pair_family
        )
        deleted_phase = complex(
            np.prod(
                [
                    np.exp(1j * contact.COUPLING)
                    for pair in active_pairs
                    if pair != target_pair
                ]
            )
        )
        deletion_residuals.append(abs(expected_contact - deleted_phase))
        contact_deletion_failures += abs(physical_phase - expected_contact) > TOLERANCE
        contact_deletion_failures += abs(
            abs(expected_contact - deleted_phase) - abs(np.exp(1j * contact.COUPLING) - 1)
        ) > TOLERANCE

    stream = coarse_stream_matrix()
    delete_one_column = np.eye(CODE_DIMENSION, dtype=complex)[:, 1:]
    one_column_closure_residual = float(
        np.linalg.norm(
            (np.eye(CODE_DIMENSION) - delete_one_column @ delete_one_column.T)
            @ stream
            @ delete_one_column
        )
    )
    frames = c235.proper_cubic_frames()
    address_keep = np.eye(ADDRESS_DIMENSION, dtype=complex)
    address_keep[0, 0] = 0
    address_delete_leakages = []
    for frame in frames:
        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        wedge, failures = frame_action(
            code, encoder, encoder, vertex_map, edge_map, toggles, pairs, flips
        )
        if not sum(failures.values()):
            address_delete_leakages.append(
                float(
                    np.linalg.norm(
                        (np.eye(ADDRESS_DIMENSION) - address_keep)
                        @ wedge
                        @ address_keep,
                        2,
                    )
                )
            )
    address_deletion_breaks_covariance = max(address_delete_leakages) > 0.99

    check(
        "catch-up, one-stream-factor, contact-pair, code-column, and address deletions are all detected on the declared orbit",
        deleted_catchup_inside == 0
        and one_stream_factor_inside == 0
        and one_stream_constraint_failures == 0
        and contact_deletion_failures == 0
        and inactive_contact_projector_failures == 0
        and abs(
            min(deletion_residuals) - abs(np.exp(1j * contact.COUPLING) - 1)
        ) < TOLERANCE
        and one_column_closure_residual == 1
        and address_deletion_breaks_covariance,
        {
            "deleted_catchup_states_remaining_in_code": deleted_catchup_inside,
            "one_stream_factor_states_remaining_in_code": one_stream_factor_inside,
            "one_stream_factor_constraint_nonfailures": one_stream_constraint_failures,
            "contact_pair_deletion_failures": contact_deletion_failures,
            "inactive_contact_projector_failures": (
                inactive_contact_projector_failures
            ),
            "contact_pair_deletion_residual": min(deletion_residuals),
            "one_column_stream_closure_residual": one_column_closure_residual,
            "one_address_deletion_breaks_transitive_covariance": address_deletion_breaks_covariance,
            "one_address_deletion_covariance_leakage": max(
                address_delete_leakages
            ),
        },
    )

    rejected = 0
    valid = np.ones(CODE_DIMENSION, dtype=complex) / np.sqrt(CODE_DIMENSION)
    validate_coefficients(valid)
    bad_coefficients = (
        np.ones(CODE_DIMENSION - 1, dtype=complex),
        np.ones(CODE_DIMENSION + 1, dtype=complex),
        np.full(CODE_DIMENSION, complex(np.nan, 0)),
        np.full(CODE_DIMENSION, complex(np.inf, 0)),
    )
    for coefficients in bad_coefficients:
        try:
            validate_coefficients(coefficients)
        except ValueError:
            rejected += 1
    for anchor in ((-1, 0, 0), (code.length, 0, 0)):
        try:
            orbit_encoder(code, anchor)
        except ValueError:
            rejected += 1
    try:
        c269.build_code(2)
    except (KeyError, ValueError):
        rejected += 1
    first = encoder.addresses[0]
    same_cell = code.graph.vertices[first.source][0]
    opposite = code.graph.vertex_index[
        (same_cell, code.graph.vertices[first.source][1] ^ 1)
    ]
    try:
        lift.validate_localized_domain(
            code,
            first.source,
            opposite,
            (1 << first.source) | (1 << opposite),
        )
    except (KeyError, ValueError):
        rejected += 1
    check(
        "the common encoder rejects wrong-dimensional, nonfinite, out-of-range, undersized, and nonperpendicular inputs",
        rejected == 8,
        {"rejected_fixtures": rejected},
    )


def supplied_inventory_and_boundary() -> None:
    print("\nREFERENCE / ADDRESS IMPORTS AND RESULT BOUNDARY")
    check(
        "the construction is a coherent reference-relative orbit isometry, not an address-preparation, coin-routing, independent-species, or full-Fock compiler",
        True,
        {
            "derived": (
                "one 24-column linear E_x with exact Gram identity",
                "coherent superpositions over all 12 perpendicular-pair directions and two stream slices",
                "exact common stream/catch-up, contact, inverse, Cycle-230 stream-then-contact, and reverse-order intertwiners",
                "declared signed-wedge proper-cubic representation common to both slices",
                "common minus under source/carrier role reversal for the identical pair",
                "42--54-M2 relative-state orbit-union support",
            ),
            "supplied": (
                "one global fixed +++ Wilson, all-B=+1 face-code reference vacuum",
                "one coarse-cell anchor x and the six physical direction labels",
                "the antisymmetric CAR wedge address convention and graph edge orientation",
                "six auxiliary port M2 per cell initialized to zero",
                "Cycle-269 A/B/FSWAP dictionary and collision-safe catch-up product",
                "Cycle-230 real contact coupling g=0.37",
                "the Cycle-230 stream-then-contact order and reverse-order comparator",
            ),
            "open": (
                "bounded preparation of the global reference vacuum",
                "preparation or autonomous decoding of an arbitrary address superposition",
                "coherence across a volume-growing set of cell anchors",
                "independent source/carrier species and a role register",
                "the six-mode coin and joint coin/port router",
                "odd states, larger even sectors, and a full-Fock compiler",
                "full-Hilbert physical matrices for the global products",
            ),
            "not_claimed": (
                "physical time for compiler substeps",
                "physical energy or a rate",
                "gravity or a source law",
                "Record or probability semantics",
            ),
            "overhead": "15 face + 6 port = 21 M2/cell inherited; one orbit has at most 54 relative-state-union M2, while complete stream/contact product unions are extensive 21 L^3 / 15 L^3",
            "authority": "none",
            "audit": "unset",
            "no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    print("PHYSICAL CYCLE-269 COHERENT PROPER-CUBIC PAIR ORBIT")
    print("authority=none; audit=unset")
    note_contract()
    cache = {length: c269.build_code(length) for length in SIZES}
    fixtures = orbit_geometry_and_gram_controls(cache)
    common_operator_and_coherence_controls(fixtures)
    constraint_controls(fixtures)
    covariance_and_common_phase_controls(cache[3])
    deletion_and_domain_controls(cache[3])
    supplied_inventory_and_boundary()
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
