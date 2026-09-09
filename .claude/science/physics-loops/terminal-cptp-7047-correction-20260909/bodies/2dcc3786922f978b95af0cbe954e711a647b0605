#!/usr/bin/env python3
"""Cycle 308: n=3 carrier and n=4 direct fixed-seam M2 interfaces.

The Cycle-219 six-mode coin is lifted to the complete exterior-cube and
exterior-fourth-power occupation bases.  The n=4 columns live directly in the
fixed-Wilson total-even Cycle-269 sector.  Each n=3 logical triple is paired
with one physical matter carrier coherently distributed over its three empty
outward ports, so every literal branch has even physical parity without a
chosen carrier direction.

Both sectors use the Cycle-230 order coin, then complete stream/catch-up, then
contact.  The coin acts only on the colocated input slice; identity on the
separated slice is an explicit unitary comparator completion, not a recurrent
volume law.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import comb
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_collision_safe_auxiliary_ports_2026_07_17 as ports
import physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17 as c305
import physical_cycle269_reference_relative_localized_pair_lift_2026_07_17 as local
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md"
)
TRAINING_SIZES = (3, 4, 5)
HELD_SIZES = (6,)
SIZES = TRAINING_SIZES + HELD_SIZES
SECTORS = (3, 4)
LABELS = {number: tuple(combinations(range(6), number)) for number in SECTORS}
LABEL_INDEX = {
    number: {label: index for index, label in enumerate(LABELS[number])}
    for number in SECTORS
}
SLICE_DIMENSION = 2
COUPLING = c230.COUPLING
TOLERANCE = 8e-12

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CarrierBranch:
    logical_label: tuple[int, ...]
    carrier_direction: int | None
    amplitude: complex
    input_face_pauli: c235.Pauli
    output_face_pauli: c235.Pauli
    input_tags: int
    output_tags: int

    def state(self, stream_slice: int) -> tuple[c235.Pauli, int, complex]:
        if stream_slice == 0:
            return self.input_face_pauli, self.input_tags, self.amplitude
        if stream_slice == 1:
            return self.output_face_pauli, self.output_tags, self.amplitude
        raise ValueError("the fixed seam has exactly two comparator slices")


@dataclass(frozen=True)
class HigherSectorEncoder:
    code: c269.WilsonSubsystemCode
    body: tuple[int, int, int]
    number: int
    columns_by_label: tuple[tuple[CarrierBranch, ...], ...]

    @property
    def occupation_dimension(self) -> int:
        return len(self.columns_by_label)

    @property
    def code_dimension(self) -> int:
        return SLICE_DIMENSION * self.occupation_dimension

    def column(self, label_index: int, stream_slice: int):
        return tuple(
            branch.state(stream_slice)
            for branch in self.columns_by_label[label_index]
        )

    def columns(self):
        for label_index in range(self.occupation_dimension):
            for stream_slice in range(SLICE_DIMENSION):
                yield label_index, stream_slice, self.column(label_index, stream_slice)


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
        check("the Cycle-308 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "wedge^3(c)",
        "wedge^4(c)",
        "twenty logical triples",
        "fifteen logical quadruples",
        "one coherently distributed physical carrier",
        "three unoccupied outward ports",
        "fixed-wilson total-even sector",
        "identity comparator completion",
        "coin, then stream/catch-up, then contact",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "matrix-unit completion",
        "one-particle mass fixture unchanged",
        "constraint leakage",
        "deletion controls",
        "lawful-domain controls",
        "no preferred carrier direction",
        "no global jordan–wigner ordering",
        "not a recurrent volume update",
        "overlap remains open",
        "preparation remains open",
        "not a full-fock compiler",
        "no broad no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins both higher-number constructions and their boundary", not missing, missing)


def column_index(label_index: int, stream_slice: int) -> int:
    return SLICE_DIMENSION * label_index + stream_slice


def permutation_sign(sequence: tuple[int, ...] | list[int]) -> int:
    inversions = sum(
        sequence[left] > sequence[right]
        for left in range(len(sequence))
        for right in range(left + 1, len(sequence))
    )
    return -1 if inversions % 2 else 1


def phase_scalar(phase: int) -> complex:
    return (1 + 0j, 1j, -1 + 0j, -1j)[phase % 4]


def full_six_pauli(
    code: c269.WilsonSubsystemCode, body: tuple[int, int, int]
) -> c235.Pauli:
    result = c235.Pauli()
    for pair in ((0, 1), (2, 3), (4, 5)):
        pair_pauli, _intermediate = c305.input_pair_pauli(code, body, pair)
        result = pair_pauli @ result
    return result


def hodge_four_pauli(
    code: c269.WilsonSubsystemCode,
    body: tuple[int, int, int],
    label: tuple[int, ...],
) -> c235.Pauli:
    if label not in LABEL_INDEX[4]:
        raise ValueError("an n=4 label must contain four distinct ordered directions")
    complement = tuple(sorted(set(range(6)) - set(label)))
    complement_pauli, _intermediate = c305.input_pair_pauli(
        code, body, complement
    )
    representative = full_six_pauli(code, body) @ local.pauli_dagger(
        complement_pauli
    )
    orientation = permutation_sign(label + complement)
    return local.scalar_times(representative, complex(orientation))


def face_stream_action(
    code: c269.WilsonSubsystemCode, face_pauli: c235.Pauli
) -> tuple[c235.Pauli, int, complex]:
    occupations = local.occupied_vertices(code, face_pauli)
    occupation_mask = sum(1 << vertex for vertex in occupations)
    output = face_pauli
    scalar = 1 + 0j
    active_edges = 0
    for left, right, edge in ports.outer_edges(code):
        left_occupied = left in occupations
        right_occupied = right in occupations
        if left_occupied ^ right_occupied:
            occupied = left if left_occupied else right
            scalar *= local.edge_stream_factor(code, occupied, edge)
            output = code.A[edge] @ output
            active_edges += 1
        elif left_occupied and right_occupied:
            raise ValueError("the declared higher-number seam excludes outer-edge overlap")
    return local.scalar_times(output, scalar), active_edges, scalar


def four_branch(
    code: c269.WilsonSubsystemCode,
    body: tuple[int, int, int],
    label: tuple[int, ...],
) -> CarrierBranch:
    input_face = hodge_four_pauli(code, body, label)
    output_face, active_edges, _scalar = face_stream_action(code, input_face)
    if active_edges != 4:
        raise ValueError("an n=4 fixed-seam branch must stream on four outer edges")
    input_tags = sum(
        1 << vertex for vertex in local.occupied_vertices(code, input_face)
    )
    output_tags = sum(
        1 << vertex for vertex in local.occupied_vertices(code, output_face)
    )
    return CarrierBranch(
        label,
        None,
        1 + 0j,
        input_face,
        output_face,
        input_tags,
        output_tags,
    )


def three_carrier_branch(
    code: c269.WilsonSubsystemCode,
    body: tuple[int, int, int],
    label: tuple[int, ...],
    carrier_direction: int,
) -> CarrierBranch:
    if label not in LABEL_INDEX[3]:
        raise ValueError("an n=3 label must contain three distinct ordered directions")
    if carrier_direction in label or not 0 <= carrier_direction < 6:
        raise ValueError("the n=3 carrier must use one unoccupied outward port")
    quadruple = tuple(sorted(label + (carrier_direction,)))
    body_vertices = c305.body_vertices(code, body)
    carrier_body_vertex = body_vertices[carrier_direction]
    carrier_arrival, carrier_edge = local.old.outer_partner(
        code, carrier_body_vertex
    )
    input_face = code.A[carrier_edge] @ hodge_four_pauli(
        code, body, quadruple
    )
    output_face, active_edges, _scalar = face_stream_action(code, input_face)
    if active_edges != 4:
        raise ValueError("an n=3 carrier branch must stream on four outer edges")
    input_tags = sum(
        1 << vertex for vertex in local.occupied_vertices(code, input_face)
    )
    output_tags = sum(
        1 << vertex for vertex in local.occupied_vertices(code, output_face)
    )
    insertion_orientation = permutation_sign(label + (carrier_direction,))
    edge_orientation = local.edge_stream_factor(
        code, carrier_body_vertex, carrier_edge
    )
    amplitude = insertion_orientation * edge_orientation / np.sqrt(3)
    expected_input = frozenset(
        [body_vertices[direction] for direction in label] + [carrier_arrival]
    )
    expected_output = frozenset(
        [local.old.outer_partner(code, body_vertices[direction])[0] for direction in label]
        + [carrier_body_vertex]
    )
    if local.occupied_vertices(code, input_face) != expected_input:
        raise ValueError("the n=3 input carrier branch has the wrong occupations")
    if local.occupied_vertices(code, output_face) != expected_output:
        raise ValueError("the n=3 output carrier branch has the wrong occupations")
    return CarrierBranch(
        label,
        carrier_direction,
        amplitude,
        input_face,
        output_face,
        input_tags,
        output_tags,
    )


def sector_encoder(
    code: c269.WilsonSubsystemCode,
    body: tuple[int, int, int],
    number: int,
) -> HigherSectorEncoder:
    if body not in code.graph.cells:
        raise ValueError("the supplied body must be one coarse cell")
    if number == 4:
        columns = tuple((four_branch(code, body, label),) for label in LABELS[4])
    elif number == 3:
        columns = tuple(
            tuple(
                three_carrier_branch(code, body, label, carrier)
                for carrier in sorted(set(range(6)) - set(label))
            )
            for label in LABELS[3]
        )
    else:
        raise ValueError("Cycle 308 constructs only n=3 and n=4")
    return HigherSectorEncoder(code, body, number, columns)


def micro_key(pauli: c235.Pauli, tags: int) -> tuple[int, int, int, int]:
    return pauli.phase, pauli.x, pauli.z, tags


def ambient_encoding(
    encoder: HigherSectorEncoder,
) -> tuple[tuple[tuple[int, int, int, int], ...], np.ndarray]:
    keys = []
    for _label_index, _stream_slice, branches in encoder.columns():
        keys.extend(micro_key(pauli, tags) for pauli, tags, _amplitude in branches)
    if len(set(keys)) != len(keys):
        raise ValueError("the literal branch microstates must be distinct")
    basis = tuple(keys)
    lookup = {key: index for index, key in enumerate(basis)}
    encoding = np.zeros((len(basis), encoder.code_dimension), dtype=complex)
    for label_index, stream_slice, branches in encoder.columns():
        column = column_index(label_index, stream_slice)
        for pauli, tags, amplitude in branches:
            encoding[lookup[micro_key(pauli, tags)], column] = amplitude
    return basis, encoding


def exterior_matrix(matrix: np.ndarray, number: int) -> np.ndarray:
    if number not in SECTORS or matrix.shape != (6, 6) or not np.all(np.isfinite(matrix)):
        raise ValueError("Cycle 308 exterior powers need n=3 or n=4 and a finite 6-by-6 matrix")
    labels = LABELS[number]
    return np.asarray(
        [
            [np.linalg.det(matrix[np.ix_(target, source)]) for source in labels]
            for target in labels
        ],
        dtype=complex,
    )


def exterior_vector(vectors: tuple[np.ndarray, ...]) -> np.ndarray:
    number = len(vectors)
    if number not in SECTORS or any(vector.shape != (6,) for vector in vectors):
        raise ValueError("the exterior vector needs three or four six-mode vectors")
    stacked = np.column_stack(vectors)
    return np.asarray(
        [np.linalg.det(stacked[np.asarray(label), :]) for label in LABELS[number]],
        dtype=complex,
    )


def exterior_representation(frame: np.ndarray, number: int) -> np.ndarray:
    labels = LABELS[number]
    result = np.zeros((len(labels), len(labels)), dtype=complex)
    for source_index, source in enumerate(labels):
        mapped = [
            int(
                np.where(
                    np.all(
                        c210.DIRECTIONS
                        == frame @ c210.DIRECTIONS[direction],
                        axis=1,
                    )
                )[0][0]
            )
            for direction in source
        ]
        target = tuple(sorted(mapped))
        result[LABEL_INDEX[number][target], source_index] = permutation_sign(mapped)
    return result


def fixed_seam_comparator(coin: np.ndarray, number: int) -> np.ndarray:
    dimension = len(LABELS[number])
    result = np.eye(2 * dimension, dtype=complex)
    result[0::2, 0::2] = exterior_matrix(coin, number)
    return result


def coarse_stream(number: int) -> np.ndarray:
    dimension = len(LABELS[number])
    result = np.zeros((2 * dimension, 2 * dimension), dtype=complex)
    for label_index in range(dimension):
        result[column_index(label_index, 1), column_index(label_index, 0)] = 1
        result[column_index(label_index, 0), column_index(label_index, 1)] = 1
    return result


def coarse_contact(number: int, coupling: float) -> np.ndarray:
    dimension = len(LABELS[number])
    diagonal = np.ones(2 * dimension, dtype=complex)
    diagonal[0::2] = np.exp(1j * coupling * (number * (number - 1) // 2))
    return np.diag(diagonal)


def contact_phase(code, pauli: c235.Pauli, coupling: float) -> complex:
    counts = {}
    for vertex in local.occupied_vertices(code, pauli):
        cell = code.graph.vertices[vertex][0]
        counts[cell] = counts.get(cell, 0) + 1
    pairs = sum(count * (count - 1) // 2 for count in counts.values())
    return complex(np.exp(1j * coupling * pairs))


def ambient_stream_matrix(
    encoder: HigherSectorEncoder, basis
) -> tuple[np.ndarray, dict[str, int]]:
    lookup = {key: index for index, key in enumerate(basis)}
    matrix = np.zeros((len(basis), len(basis)), dtype=complex)
    failures = {"face": 0, "catchup": 0, "target": 0, "sign": 0}
    for source_index, key in enumerate(basis):
        phase, x_bits, z_bits, tags = key
        pauli = c235.Pauli(phase, x_bits, z_bits)
        output_face, _active, _scalar = face_stream_action(encoder.code, pauli)
        occupations = sum(
            1 << vertex for vertex in local.occupied_vertices(encoder.code, pauli)
        )
        arrival, caught, sign = ports.port_macrostep(
            encoder.code, occupations, tags
        )
        expected_occupations = sum(
            1 << vertex
            for vertex in local.occupied_vertices(encoder.code, output_face)
        )
        failures["face"] += arrival != expected_occupations
        failures["catchup"] += caught != expected_occupations
        failures["sign"] += sign != 1
        target = lookup.get(micro_key(output_face, caught))
        failures["target"] += target is None
        if target is not None:
            matrix[target, source_index] = sign
    return matrix, failures


def ambient_contact_matrix(encoder, basis, coupling: float) -> np.ndarray:
    return np.diag(
        [
            contact_phase(encoder.code, c235.Pauli(phase, x_bits, z_bits), coupling)
            for phase, x_bits, z_bits, _tags in basis
        ]
    )


def ambient_coin_matrix(
    encoding: np.ndarray, logical_comparator: np.ndarray
) -> np.ndarray:
    """Unitary matrix-unit completion on the declared literal microbasis.

    The code block is E K E^dagger.  Its n=3 microcoefficients are therefore
    K_ij times target_amplitude times conjugate(source_amplitude).  Identity on
    the orthogonal complement is a comparator completion, not another law.
    """

    projector = encoding @ encoding.conj().T
    return (
        encoding @ logical_comparator @ encoding.conj().T
        + np.eye(encoding.shape[0], dtype=complex)
        - projector
    )


def ambient_frame_representation(
    encoder: HigherSectorEncoder,
    basis,
    frame: np.ndarray,
    reducer: c305.StabilizerReducer,
) -> tuple[np.ndarray, int]:
    """Literal signed permutation of the anchor microbasis under one frame."""

    code = encoder.code
    vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
    toggles, repair_pairs, flips = c269.repair_data(
        code.graph, vertex_map, edge_map
    )
    tag_lookup = {
        tags: (index, c235.Pauli(phase, x_bits, z_bits))
        for index, (phase, x_bits, z_bits, tags) in enumerate(basis)
    }
    representation = np.zeros((len(basis), len(basis)), dtype=complex)
    failures = 0
    for source, (phase, x_bits, z_bits, tags) in enumerate(basis):
        transformed = local.transform_pauli(
            code,
            c235.Pauli(phase, x_bits, z_bits),
            edge_map,
            toggles,
            repair_pairs,
            flips,
        )
        transformed_tags = ports.permute_bits(tags, vertex_map)
        target_row = tag_lookup.get(transformed_tags)
        failures += target_row is None
        if target_row is None:
            continue
        target, target_pauli = target_row
        relative_phase = reducer.relative_phase(transformed, target_pauli)
        failures += relative_phase is None
        if relative_phase is not None:
            representation[target, source] = phase_scalar(relative_phase)
    return representation, failures


def path_and_parity_carrier_controls(cache) -> None:
    print("\nN=4 FIXED-WILSON RAYS / N=3 PARITY CARRIER")
    rows = []
    for length, code in cache.items():
        reducer = c305.StabilizerReducer(code)
        body = (0, 0, 0)
        vertices = c305.body_vertices(code, body)
        path_tests = 0
        path_failures = 0
        ray_phase_counts = {phase: 0 for phase in range(4)}
        for label in LABELS[4]:
            target = hodge_four_pauli(code, body, label)
            a, b, c, d = label
            matchings = (((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c)))
            for matching in matchings:
                variants = []
                for pair in matching:
                    if pair[1] == (pair[0] ^ 1):
                        variants.append(tuple(sorted(set(range(6)) - set(pair))))
                    else:
                        variants.append((None,))
                for choices in product(*variants):
                    pair_words = [
                        c305.input_pair_pauli(code, body, pair, choice)[0]
                        for pair, choice in zip(matching, choices)
                    ]
                    for ordered in (pair_words, list(reversed(pair_words))):
                        candidate = ordered[0] @ ordered[1]
                        phase = reducer.relative_phase(candidate, target)
                        path_failures += phase is None
                        path_failures += local.occupied_vertices(code, candidate) != frozenset(
                            vertices[direction] for direction in label
                        )
                        if phase is not None:
                            ray_phase_counts[phase] += 1
                        path_tests += 1

        odd_syndrome_parity_failures = 0
        product_B = c235.Pauli()
        for row in code.B:
            product_B = product_B @ row
        odd_syndrome_parity_failures += product_B != c235.Pauli()
        odd_syndrome_generator_failures = 0
        for qubit in range(code.qubits):
            for generator in (c235.Pauli(x=1 << qubit), c235.Pauli(z=1 << qubit)):
                odd_syndrome_generator_failures += (
                    sum(not generator.commutes(row) for row in code.B) % 2 != 0
                )
        carrier_branches = 0
        carrier_failures = 0
        carrier_norm_failures = 0
        for label in LABELS[3]:
            branches = [
                three_carrier_branch(code, body, label, direction)
                for direction in sorted(set(range(6)) - set(label))
            ]
            carrier_branches += len(branches)
            carrier_norm_failures += abs(sum(abs(branch.amplitude) ** 2 for branch in branches) - 1) > TOLERANCE
            for branch in branches:
                for stream_slice in (0, 1):
                    pauli, tags, _amplitude = branch.state(stream_slice)
                    occupations = local.occupied_vertices(code, pauli)
                    carrier_failures += len(occupations) != 4
                    carrier_failures += occupations != frozenset(
                        vertex for vertex in range(len(code.graph.vertices)) if (tags >> vertex) & 1
                    )
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "n4_pairing_path_tests": path_tests,
                "n4_nonray_failures": path_failures,
                "n4_exact_reference_phase_counts": ray_phase_counts,
                "product_B_is_identity": odd_syndrome_parity_failures == 0,
                "direct_three_occupation_syndrome_lawful": False,
                "odd_syndrome_generator_failures": odd_syndrome_generator_failures,
                "n3_coherent_carrier_branches": carrier_branches,
                "n3_carrier_failures": carrier_failures,
                "n3_carrier_norm_failures": carrier_norm_failures,
                "reference_rank": len(reducer.pivots),
            }
        )
    check(
        "all n=4 pairing/path words are one fixed-Wilson ray while the explicit three-branch carrier embeds n=3 into lawful even physical parity",
        all(
            row["n4_pairing_path_tests"] > 100
            and row["n4_nonray_failures"] == 0
            and sum(row["n4_exact_reference_phase_counts"].values()) == row["n4_pairing_path_tests"]
            and row["product_B_is_identity"]
            and not row["direct_three_occupation_syndrome_lawful"]
            and row["odd_syndrome_generator_failures"] == 0
            and row["n3_coherent_carrier_branches"] == 60
            and row["n3_carrier_failures"] == 0
            and row["n3_carrier_norm_failures"] == 0
            and row["reference_rank"] == 15 * row["L"] ** 3
            for row in rows
        ),
        rows,
    )


def geometry_and_constraint_controls(cache):
    print("\nCOMPLETE OCCUPATION ORBITS / LITERAL COLUMNS / CONSTRAINTS")
    fixtures = {number: {} for number in SECTORS}
    rows = []
    for length, code in cache.items():
        for number in SECTORS:
            encoders = [sector_encoder(code, body, number) for body in code.graph.cells]
            fixtures[number][length] = encoders
            support_census = []
            branch_supports = []
            gram_failures = occupation_failures = port_failures = 0
            local_leakage = wilson_leakage = 0
            microstate_counts = []
            for encoder in encoders:
                basis, encoding = ambient_encoding(encoder)
                microstate_counts.append(len(basis))
                gram_failures += np.linalg.norm(
                    encoding.conj().T @ encoding - np.eye(encoder.code_dimension)
                ) > TOLERANCE
                face_union = tag_union = 0
                for _label_index, _slice, branches in encoder.columns():
                    for pauli, tags, _amplitude in branches:
                        occupations = local.occupied_vertices(code, pauli)
                        expected_physical_number = 4
                        occupation_failures += len(occupations) != expected_physical_number
                        occupation_failures += tags != sum(1 << vertex for vertex in occupations)
                        local_leakage += sum(not pauli.commutes(row) for row in code.local_checks)
                        wilson_leakage += sum(not pauli.commutes(row) for row in code.wilsons)
                        for vertex, B_vertex in enumerate(code.B):
                            port_failures += (
                                (not pauli.commutes(B_vertex))
                                != bool((tags >> vertex) & 1)
                            )
                        face_union |= pauli.x | pauli.z
                        tag_union |= tags
                        branch_supports.append((pauli.x | pauli.z).bit_count() + tags.bit_count())
                support_census.append(
                    (face_union.bit_count(), tag_union.bit_count(), face_union.bit_count() + tag_union.bit_count())
                )
            rows.append(
                {
                    "n": number,
                    "L": length,
                    "held": length in HELD_SIZES,
                    "encoders": len(encoders),
                    "logical_occupations": len(LABELS[number]),
                    "columns_per_E_x": 2 * len(LABELS[number]),
                    "literal_microstates_per_E_x": sorted(set(microstate_counts)),
                    "face_supports_M2": sorted({row[0] for row in support_census}),
                    "port_supports_M2": sorted({row[1] for row in support_census}),
                    "total_supports_M2": sorted({row[2] for row in support_census}),
                    "maximum_branch_support_M2": max(branch_supports),
                    "gram_failures": gram_failures,
                    "occupation_failures": occupation_failures,
                    "port_constraint_failures": port_failures,
                    "local_check_leakage": local_leakage,
                    "Wilson_leakage": wilson_leakage,
                    "installed_M2_per_cell": 21,
                }
            )
    check(
        "the complete n=3 and n=4 encoders have exact Gram, bounded support, literal even-parity branches, and zero inherited-constraint leakage through held L=6",
        all(
            row["encoders"] == row["L"] ** 3
            and row["logical_occupations"] == (20 if row["n"] == 3 else 15)
            and row["columns_per_E_x"] == (40 if row["n"] == 3 else 30)
            and row["literal_microstates_per_E_x"] == ([120] if row["n"] == 3 else [30])
            and max(row["total_supports_M2"]) <= 66
            and row["maximum_branch_support_M2"] <= 34
            and row["gram_failures"] == 0
            and row["occupation_failures"] == 0
            and row["port_constraint_failures"] == 0
            and row["local_check_leakage"] == 0
            and row["Wilson_leakage"] == 0
            and row["installed_M2_per_cell"] == 21
            for row in rows
        ),
        rows,
    )
    return fixtures, rows


def matrix_unit_controls(fixtures) -> None:
    print("\nLOCAL MATRIX-UNIT COMPLETIONS")
    rows = []
    for number in SECTORS:
        encoder = fixtures[number][3][0]
        basis, encoding = ambient_encoding(encoder)
        columns = encoding.T
        gram = encoding.conj().T @ encoding
        transition_failures = constraint_commutators = sector_commutators = 0
        physical_terms = 0
        branch_states = []
        for _label_index, _slice, branches in encoder.columns():
            branch_states.append(
                tuple((pauli, tags, amplitude) for pauli, tags, amplitude in branches)
            )
        for target_branches in branch_states:
            for source_branches in branch_states:
                physical_terms += len(target_branches) * len(source_branches)
                for target_pauli, target_tags, _target_amplitude in target_branches:
                    target_rep = local.full_state_representative(
                        encoder.code, target_pauli, target_tags
                    )
                    for source_pauli, source_tags, _source_amplitude in source_branches:
                        source_rep = local.full_state_representative(
                            encoder.code, source_pauli, source_tags
                        )
                        transition = c305.transition_pauli(
                            encoder.code,
                            (target_pauli, target_tags),
                            (source_pauli, source_tags),
                        )
                        transition_failures += transition @ source_rep != target_rep
                        for vertex in range(len(encoder.code.graph.vertices)):
                            constraint_commutators += not transition.commutes(
                                c305.constraint_pauli(encoder.code, vertex)
                            )
                        sector_commutators += sum(
                            not transition.commutes(row)
                            for row in encoder.code.local_checks + encoder.code.wilsons
                        )
        triple_failures = 0
        for left in range(encoder.code_dimension):
            for middle in range(encoder.code_dimension):
                overlap = gram[middle, middle]
                for right in range(encoder.code_dimension):
                    triple_failures += abs(overlap - 1) > TOLERANCE
        comparator = fixed_seam_comparator(c219.common_species(-0.3).coin, number)
        physical_coin = ambient_coin_matrix(encoding, comparator)
        lookup = {key: index for index, key in enumerate(basis)}
        coefficient_weight_failures = 0
        coefficient_weight_tests = 0
        for target_column, source_column in np.argwhere(abs(comparator) > 1e-14):
            if target_column == source_column:
                continue
            for target_pauli, target_tags, target_amplitude in branch_states[target_column]:
                target_micro = lookup[micro_key(target_pauli, target_tags)]
                for source_pauli, source_tags, source_amplitude in branch_states[source_column]:
                    source_micro = lookup[micro_key(source_pauli, source_tags)]
                    expected = (
                        comparator[target_column, source_column]
                        * target_amplitude
                        * np.conjugate(source_amplitude)
                    )
                    coefficient_weight_failures += abs(
                        physical_coin[target_micro, source_micro] - expected
                    ) > TOLERANCE
                    coefficient_weight_tests += 1
        nonzero = np.argwhere(abs(comparator) > 1e-14)
        expanded_comparator_terms = sum(
            len(branch_states[target]) * len(branch_states[source])
            for target, source in nonzero
        )
        rows.append(
            {
                "n": number,
                "ambient_literal_microstates": len(basis),
                "matrix_units": encoder.code_dimension ** 2,
                "matrix_unit_microterms": physical_terms,
                "triple_product_tests": encoder.code_dimension ** 3,
                "triple_product_failures": triple_failures,
                "transition_action_failures": transition_failures,
                "constraint_commutators": constraint_commutators,
                "sector_commutators": sector_commutators,
                "logical_comparator_nonzero_coefficients": len(nonzero),
                "expanded_comparator_microterms": expanded_comparator_terms,
                "offdiagonal_amplitude_weight_tests": coefficient_weight_tests,
                "offdiagonal_amplitude_weight_failures": coefficient_weight_failures,
            }
        )
    check(
        "the bounded branch projectors and physical Pauli transitions give exact n=3 and n=4 matrix-unit completions preserving every declared constraint",
        all(
            row["matrix_units"] == (1600 if row["n"] == 3 else 900)
            and row["triple_product_tests"] == (64000 if row["n"] == 3 else 27000)
            and row["triple_product_failures"] == 0
            and row["transition_action_failures"] == 0
            and row["constraint_commutators"] == 0
            and row["sector_commutators"] == 0
            and row["offdiagonal_amplitude_weight_tests"] > 0
            and row["offdiagonal_amplitude_weight_failures"] == 0
            for row in rows
        ),
        rows,
    )


def exterior_and_operator_controls(fixtures) -> None:
    print("\nEXTERIOR COINS / STREAM / CONTACT / ORDERED COMPOSITION")
    rng = np.random.default_rng(308)
    exterior_rows = []
    for number in SECTORS:
        for beta, held_beta in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True)):
            coin = c219.common_species(beta).coin
            exterior = exterior_matrix(coin, number)
            action_residual = 0.0
            for _ in range(20):
                vectors = tuple(
                    (lambda vector: vector / np.linalg.norm(vector))(
                        rng.normal(size=6) + 1j * rng.normal(size=6)
                    )
                    for _index in range(number)
                )
                action_residual = max(
                    action_residual,
                    float(
                        np.linalg.norm(
                            exterior @ exterior_vector(vectors)
                            - exterior_vector(tuple(coin @ vector for vector in vectors))
                        )
                    ),
                )
            exterior_rows.append(
                {
                    "n": number,
                    "beta": beta,
                    "held_beta": held_beta,
                    "dimension": len(LABELS[number]),
                    "unitarity_residual": float(
                        np.linalg.norm(exterior.conj().T @ exterior - np.eye(len(LABELS[number])))
                    ),
                    "exterior_action_residual": action_residual,
                    "determinant_residual": abs(
                        np.linalg.det(exterior)
                        - np.linalg.det(coin) ** comb(5, number - 1)
                    ),
                }
            )
    check(
        "the complete wedge^3(C) and wedge^4(C) blocks are unitary exterior powers including held beta=-0.35",
        all(
            row["unitarity_residual"] < 4e-14
            and row["exterior_action_residual"] < 8e-14
            and row["determinant_residual"] < 4e-14
            for row in exterior_rows
        ),
        exterior_rows,
    )

    operator_rows = []
    for number in SECTORS:
        comparator = fixed_seam_comparator(c219.common_species(-0.3).coin, number)
        stream = coarse_stream(number)
        contact = coarse_contact(number, COUPLING)
        code_identity = np.eye(comparator.shape[0])
        _template_basis, template_encoding = ambient_encoding(
            fixtures[number][3][0]
        )
        physical_coin = ambient_coin_matrix(template_encoding, comparator)
        template_stream, template_stream_failures = ambient_stream_matrix(
            fixtures[number][3][0], _template_basis
        )
        template_contact = ambient_contact_matrix(
            fixtures[number][3][0], _template_basis, COUPLING
        )
        ambient_beta_rows = []
        for beta, held_beta in (
            (-0.2, False),
            (-0.3, False),
            (-0.4, False),
            (-0.35, True),
        ):
            beta_comparator = fixed_seam_comparator(
                c219.common_species(beta).coin, number
            )
            beta_physical_coin = ambient_coin_matrix(
                template_encoding, beta_comparator
            )
            beta_composition_image = (
                template_contact
                @ template_stream
                @ beta_physical_coin
                @ template_encoding
            )
            beta_coarse_composite = contact @ stream @ beta_comparator
            ambient_beta_rows.append(
                {
                    "beta": beta,
                    "held_beta": held_beta,
                    "coin_intertwiner": float(
                        np.linalg.norm(
                            beta_physical_coin @ template_encoding
                            - template_encoding @ beta_comparator
                        )
                    ),
                    "coin_unitarity": float(
                        np.linalg.norm(
                            beta_physical_coin.conj().T @ beta_physical_coin
                            - np.eye(len(beta_physical_coin))
                        )
                    ),
                    "coin_inverse": float(
                        np.linalg.norm(
                            beta_physical_coin.conj().T @ beta_physical_coin
                            - np.eye(len(beta_physical_coin))
                        )
                    ),
                    "composition_intertwiner": float(
                        np.linalg.norm(
                            beta_composition_image
                            - template_encoding @ beta_coarse_composite
                        )
                    ),
                    "stream_branch_failures": sum(template_stream_failures.values()),
                }
            )
        maximums = {
            "coin_intertwiner": 0.0,
            "stream_intertwiner": 0.0,
            "contact_intertwiner": 0.0,
            "composition_intertwiner": 0.0,
            "physical_unitarity": 0.0,
            "inverse_residual": 0.0,
            "leakage": 0.0,
        }
        branch_failures = 0
        for length, encoders in fixtures[number].items():
            for encoder in encoders:
                basis, encoding = ambient_encoding(encoder)
                ambient_identity = np.eye(len(basis), dtype=complex)
                physical_stream, failures = ambient_stream_matrix(encoder, basis)
                physical_contact = ambient_contact_matrix(encoder, basis, COUPLING)
                physical_contact_inverse = ambient_contact_matrix(
                    encoder, basis, -COUPLING
                )
                branch_failures += sum(failures.values())
                coarse_G = contact @ stream @ comparator
                coin_image = physical_coin @ encoding
                stream_image = physical_stream @ encoding
                contact_image = physical_contact @ encoding
                composition_image = physical_contact @ physical_stream @ coin_image
                maximums["coin_intertwiner"] = max(
                    maximums["coin_intertwiner"],
                    float(np.linalg.norm(coin_image - encoding @ comparator)),
                )
                maximums["stream_intertwiner"] = max(
                    maximums["stream_intertwiner"],
                    float(np.linalg.norm(stream_image - encoding @ stream)),
                )
                maximums["contact_intertwiner"] = max(
                    maximums["contact_intertwiner"],
                    float(np.linalg.norm(contact_image - encoding @ contact)),
                )
                maximums["composition_intertwiner"] = max(
                    maximums["composition_intertwiner"],
                    float(np.linalg.norm(composition_image - encoding @ coarse_G)),
                )
                maximums["physical_unitarity"] = max(
                    maximums["physical_unitarity"],
                    float(np.linalg.norm(physical_coin.conj().T @ physical_coin - ambient_identity)),
                    float(np.linalg.norm(physical_stream.conj().T @ physical_stream - ambient_identity)),
                    float(np.linalg.norm(physical_contact.conj().T @ physical_contact - ambient_identity)),
                )
                maximums["inverse_residual"] = max(
                    maximums["inverse_residual"],
                    float(np.linalg.norm(physical_coin.conj().T @ physical_coin - ambient_identity)),
                    float(np.linalg.norm(physical_stream @ physical_stream - ambient_identity)),
                    float(np.linalg.norm(physical_contact @ physical_contact_inverse - ambient_identity)),
                )
                maximums["leakage"] = max(
                    maximums["leakage"],
                    float(
                        np.linalg.norm(
                            composition_image
                            - encoding @ (encoding.conj().T @ composition_image)
                        )
                    ),
                )
        t0 = code_identity[:, 0::2]
        t1 = code_identity[:, 1::2]
        schedule_rows = {
            "contact_coin_commutator": float(np.linalg.norm(contact @ comparator - comparator @ contact, 2)),
            "stream_coin_commutator": float(np.linalg.norm(stream @ comparator - comparator @ stream, 2)),
            "stream_contact_commutator": float(np.linalg.norm(stream @ contact - contact @ stream, 2)),
            "forward_poststream_contact_residual": float(np.linalg.norm((contact @ stream @ comparator - stream @ comparator) @ t0)),
            "reverse_completion_contact_residual": float(np.linalg.norm((contact @ stream @ comparator - stream @ comparator) @ t1)),
        }
        operator_rows.append(
            {
                "n": number,
                "sizes": sorted(fixtures[number]),
                "encoders_tested": sum(len(encoders) for encoders in fixtures[number].values()),
                "branch_failures": branch_failures,
                "ambient_beta_rows": ambient_beta_rows,
                **maximums,
                **schedule_rows,
            }
        )
    check(
        "both physical seams exactly intertwine input-slice coin, stream/catch-up, contact, and actual coin-stream-contact composition through held L=6",
        all(
            row["sizes"] == [3, 4, 5, 6]
            and row["encoders_tested"] == 432
            and row["branch_failures"] == 0
            and all(
                beta_row["stream_branch_failures"] == 0
                and max(
                    beta_row["coin_intertwiner"],
                    beta_row["coin_unitarity"],
                    beta_row["coin_inverse"],
                    beta_row["composition_intertwiner"],
                ) < 2e-11
                for beta_row in row["ambient_beta_rows"]
            )
            and max(
                row["coin_intertwiner"],
                row["stream_intertwiner"],
                row["contact_intertwiner"],
                row["composition_intertwiner"],
                row["physical_unitarity"],
                row["inverse_residual"],
                row["leakage"],
            ) < 2e-11
            and row["contact_coin_commutator"] < TOLERANCE
            and row["stream_coin_commutator"] > 1
            and row["stream_contact_commutator"] > 0.5
            and row["forward_poststream_contact_residual"] < TOLERANCE
            and row["reverse_completion_contact_residual"] > 1
            for row in operator_rows
        ),
        operator_rows,
    )


def covariance_controls(code) -> None:
    print("\nPROPER-CUBIC COVARIANCE / GROUP LAWS / TRANSLATIONS")
    frames = c235.proper_cubic_frames()
    reducer = c305.StabilizerReducer(code)
    frame_rows = []
    frame_lookup = {tuple(frame.flatten()): index for index, frame in enumerate(frames)}
    for number in SECTORS:
        representations = [exterior_representation(frame, number) for frame in frames]
        anchor_encoder = sector_encoder(code, (0, 0, 0), number)
        anchor_basis, anchor_encoding = ambient_encoding(anchor_encoder)
        anchor_comparator = fixed_seam_comparator(
            c219.common_species(-0.3).coin, number
        )
        anchor_physical_coin = ambient_coin_matrix(
            anchor_encoding, anchor_comparator
        )
        anchor_physical_stream, anchor_stream_failures = ambient_stream_matrix(
            anchor_encoder, anchor_basis
        )
        anchor_physical_contact = ambient_contact_matrix(
            anchor_encoder, anchor_basis, COUPLING
        )
        anchor_physical_composite = (
            anchor_physical_contact
            @ anchor_physical_stream
            @ anchor_physical_coin
        )
        ambient_frame_failures = sum(anchor_stream_failures.values())
        ambient_isometry_covariance = 0.0
        ambient_coin_covariance = 0.0
        ambient_stream_covariance = 0.0
        ambient_contact_covariance = 0.0
        ambient_composite_covariance = 0.0
        ambient_frame_unitarity = 0.0
        phase_failures = tag_failures = carrier_failures = 0
        physical_tests = 0
        for frame, representation in zip(frames, representations):
            micro_representation, micro_failures = ambient_frame_representation(
                anchor_encoder, anchor_basis, frame, reducer
            )
            ambient_frame_failures += micro_failures
            logical_representation = np.kron(
                representation, np.eye(SLICE_DIMENSION)
            )
            ambient_isometry_covariance = max(
                ambient_isometry_covariance,
                float(
                    np.linalg.norm(
                        micro_representation @ anchor_encoding
                        - anchor_encoding @ logical_representation
                    )
                ),
            )
            ambient_frame_unitarity = max(
                ambient_frame_unitarity,
                float(
                    np.linalg.norm(
                        micro_representation.conj().T @ micro_representation
                        - np.eye(len(anchor_basis))
                    )
                ),
            )
            for operator, name in (
                (anchor_physical_coin, "coin"),
                (anchor_physical_stream, "stream"),
                (anchor_physical_contact, "contact"),
                (anchor_physical_composite, "composite"),
            ):
                residual = float(
                    np.linalg.norm(
                        micro_representation @ operator
                        - operator @ micro_representation
                    )
                )
                if name == "coin":
                    ambient_coin_covariance = max(ambient_coin_covariance, residual)
                elif name == "stream":
                    ambient_stream_covariance = max(ambient_stream_covariance, residual)
                elif name == "contact":
                    ambient_contact_covariance = max(ambient_contact_covariance, residual)
                else:
                    ambient_composite_covariance = max(ambient_composite_covariance, residual)
            vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
            toggles, repair_pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
            for body in code.graph.cells:
                target_body = tuple(int(value % code.length) for value in frame @ np.asarray(body))
                source = sector_encoder(code, body, number)
                target = sector_encoder(code, target_body, number)
                for source_index, label in enumerate(LABELS[number]):
                    target_index = int(np.argmax(abs(representation[:, source_index])))
                    expected_sign = representation[target_index, source_index]
                    target_label = LABELS[number][target_index]
                    source_branches = source.columns_by_label[source_index]
                    target_branches = target.columns_by_label[target_index]
                    target_by_carrier = {branch.carrier_direction: branch for branch in target_branches}
                    mapped_label = tuple(
                        sorted(code.graph.vertices[vertex_map[c305.body_vertices(code, body)[direction]]][1] for direction in label)
                    )
                    phase_failures += mapped_label != target_label
                    for source_branch in source_branches:
                        if number == 3:
                            source_carrier_vertex = c305.body_vertices(code, body)[source_branch.carrier_direction]
                            target_carrier = code.graph.vertices[vertex_map[source_carrier_vertex]][1]
                        else:
                            target_carrier = None
                        target_branch = target_by_carrier.get(target_carrier)
                        carrier_failures += target_branch is None
                        if target_branch is None:
                            continue
                        for stream_slice in (0, 1):
                            source_pauli, source_tags, source_amplitude = source_branch.state(stream_slice)
                            target_pauli, target_tags, target_amplitude = target_branch.state(stream_slice)
                            transformed = local.transform_pauli(
                                code, source_pauli, edge_map, toggles, repair_pairs, flips
                            )
                            phase = reducer.relative_phase(transformed, target_pauli)
                            phase_failures += phase is None or abs(
                                source_amplitude * phase_scalar(phase or 0)
                                - expected_sign * target_amplitude
                            ) > TOLERANCE
                            tag_failures += ports.permute_bits(source_tags, vertex_map) != target_tags
                            physical_tests += 1
        group_failures = 0
        maximum_group_residual = 0.0
        for left_index, left_frame in enumerate(frames):
            for right_index, right_frame in enumerate(frames):
                product_index = frame_lookup[tuple((left_frame @ right_frame).flatten())]
                residual = float(
                    np.linalg.norm(
                        representations[left_index] @ representations[right_index]
                        - representations[product_index]
                    )
                )
                maximum_group_residual = max(maximum_group_residual, residual)
                group_failures += residual > TOLERANCE
        coin = exterior_matrix(c219.common_species(-0.3).coin, number)
        coin_covariance = max(
            float(np.linalg.norm(rep @ coin @ rep.conj().T - coin))
            for rep in representations
        )
        orbit_sizes = []
        unseen = set(range(len(LABELS[number])))
        while unseen:
            seed = min(unseen)
            orbit = {int(np.argmax(abs(rep[:, seed]))) for rep in representations}
            orbit_sizes.append(len(orbit))
            unseen -= orbit

        base = sector_encoder(code, (0, 0, 0), number)
        translation_failures = translation_tests = 0
        for displacement in product(range(code.length), repeat=3):
            vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
            toggles, repair_pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
            target = sector_encoder(code, displacement, number)
            for source_branches, target_branches in zip(base.columns_by_label, target.columns_by_label):
                target_by_carrier = {branch.carrier_direction: branch for branch in target_branches}
                for source_branch in source_branches:
                    target_branch = target_by_carrier[source_branch.carrier_direction]
                    for stream_slice in (0, 1):
                        source_pauli, source_tags, source_amplitude = source_branch.state(stream_slice)
                        target_pauli, target_tags, target_amplitude = target_branch.state(stream_slice)
                        transformed = local.transform_pauli(
                            code, source_pauli, edge_map, toggles, repair_pairs, flips
                        )
                        phase = reducer.relative_phase(transformed, target_pauli)
                        translation_failures += phase != 0
                        translation_failures += source_amplitude != target_amplitude
                        translation_failures += ports.permute_bits(source_tags, vertex_map) != target_tags
                        translation_tests += 1
        frame_rows.append(
            {
                "n": number,
                "proper_frames": len(frames),
                "occupation_orbits": sorted(orbit_sizes),
                "physical_branch_slice_tests": physical_tests,
                "phase_failures": phase_failures,
                "tag_failures": tag_failures,
                "carrier_map_failures": carrier_failures,
                "group_law_tests": len(frames) ** 2,
                "group_law_failures": group_failures,
                "maximum_group_residual": maximum_group_residual,
                "coin_covariance_residual": coin_covariance,
                "ambient_frame_failures": ambient_frame_failures,
                "ambient_frame_unitarity_residual": ambient_frame_unitarity,
                "ambient_isometry_covariance_residual": ambient_isometry_covariance,
                "ambient_physical_coin_covariance_residual": ambient_coin_covariance,
                "ambient_physical_stream_covariance_residual": ambient_stream_covariance,
                "ambient_physical_contact_covariance_residual": ambient_contact_covariance,
                "ambient_physical_composite_covariance_residual": ambient_composite_covariance,
                "translations": code.length ** 3,
                "translation_branch_slice_tests": translation_tests,
                "translation_failures": translation_failures,
            }
        )
    check(
        "the complete occupation bases and literal carrier branches realize exact exterior-power covariance under all 24 frames, group products, and L=3 translations",
        all(
            row["proper_frames"] == 24
            and row["occupation_orbits"] == ([8, 12] if row["n"] == 3 else [3, 12])
            and row["phase_failures"] == 0
            and row["tag_failures"] == 0
            and row["carrier_map_failures"] == 0
            and row["group_law_failures"] == 0
            and row["coin_covariance_residual"] < TOLERANCE
            and row["ambient_frame_failures"] == 0
            and max(
                row["ambient_frame_unitarity_residual"],
                row["ambient_isometry_covariance_residual"],
                row["ambient_physical_coin_covariance_residual"],
                row["ambient_physical_stream_covariance_residual"],
                row["ambient_physical_contact_covariance_residual"],
                row["ambient_physical_composite_covariance_residual"],
            ) < 2e-11
            and row["translations"] == 27
            and row["translation_failures"] == 0
            for row in frame_rows
        ),
        frame_rows,
    )


def one_particle_mass_firewall() -> None:
    rows = []
    for beta, held in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True)):
        species = c219.common_species(beta)
        rows.append(
            {
                "beta": beta,
                "held": held,
                "rest_mass": c219.rest_mass(species),
                "analytic_mass": species.analytic_mass,
                "relative_residual": abs(
                    c219.rest_mass(species) / species.analytic_mass - 1
                ),
            }
        )
    check(
        "the higher-number lifts import the unchanged Cycle-219 coin and preserve its one-particle mass fixture without reinterpreting contact",
        all(row["relative_residual"] < 2e-12 for row in rows),
        rows,
    )


def deletion_and_domain_controls(code) -> None:
    print("\nLEAKAGE / DELETION / LAWFUL-DOMAIN CONTROLS")
    leakage_rows = []
    for number in SECTORS:
        frames = [exterior_representation(frame, number) for frame in c235.proper_cubic_frames()]
        unseen = set(range(len(LABELS[number])))
        orbits = []
        while unseen:
            seed = min(unseen)
            orbit = sorted({int(np.argmax(abs(rep[:, seed]))) for rep in frames})
            orbits.append(orbit)
            unseen -= set(orbit)
        coin = exterior_matrix(c219.common_species(-0.3).coin, number)
        orbit_leakage = max(
            float(np.linalg.norm(coin[np.ix_(target, source)], 2))
            for source in orbits
            for target in orbits
            if source is not target
        )
        comparator = fixed_seam_comparator(c219.common_species(-0.3).coin, number)
        off_diagonal = abs(comparator).copy()
        np.fill_diagonal(off_diagonal, 0)
        row, column = np.unravel_index(np.argmax(off_diagonal), off_diagonal.shape)
        deleted = comparator.copy()
        coefficient = deleted[row, column]
        deleted[row, column] = 0
        deletion_unitarity = float(np.linalg.norm(deleted.conj().T @ deleted - np.eye(len(deleted))))
        stream = coarse_stream(number)
        delete_column = np.eye(len(stream))[:, 1:]
        column_leakage = float(
            np.linalg.norm((np.eye(len(stream)) - delete_column @ delete_column.T) @ stream @ delete_column)
        )
        encoder = sector_encoder(code, (0, 0, 0), number)
        _basis, encoding = ambient_encoding(encoder)
        physical_coin = ambient_coin_matrix(encoding, comparator)
        physical_offdiagonal = abs(physical_coin).copy()
        np.fill_diagonal(physical_offdiagonal, 0)
        physical_row, physical_column = np.unravel_index(
            np.argmax(physical_offdiagonal), physical_offdiagonal.shape
        )
        mutated_physical_coin = physical_coin.copy()
        mutated_physical_coefficient = mutated_physical_coin[
            physical_row, physical_column
        ]
        mutated_physical_coin[physical_row, physical_column] = 0
        physical_mutation_intertwiner = float(
            np.linalg.norm(mutated_physical_coin @ encoding - encoding @ comparator)
        )
        physical_mutation_unitarity = float(
            np.linalg.norm(
                mutated_physical_coin.conj().T @ mutated_physical_coin
                - np.eye(len(physical_coin))
            )
        )
        leakage_rows.append(
            {
                "n": number,
                "proper_cubic_orbit_sizes": sorted(map(len, orbits)),
                "one_orbit_coin_leakage_operator_norm": orbit_leakage,
                "deleted_coin_coefficient": coefficient,
                "deleted_coin_unitarity_residual": deletion_unitarity,
                "one_column_stream_leakage": column_leakage,
                "deleted_contact_residual": abs(np.exp(1j * COUPLING * (number * (number - 1) // 2)) - 1),
                "mutated_ambient_coin_coefficient": mutated_physical_coefficient,
                "mutated_ambient_coin_intertwiner_residual": physical_mutation_intertwiner,
                "mutated_ambient_coin_unitarity_residual": physical_mutation_unitarity,
            }
        )

    encoder3 = sector_encoder(code, (0, 0, 0), 3)
    _basis3, encoding3 = ambient_encoding(encoder3)
    deletion = encoding3.copy()
    for column in range(encoding3.shape[1]):
        nonzero = np.flatnonzero(abs(deletion[:, column]) > TOLERANCE)
        deletion[nonzero[0], column] = 0
    carrier_deletion_gram = float(
        np.linalg.norm(deletion.conj().T @ deletion - np.eye(encoding3.shape[1]), 2)
    )
    phase_stripped = encoding3.copy()
    phase_stripped[abs(phase_stripped) > TOLERANCE] = 1 / np.sqrt(3)
    carrier_phase_change = float(np.linalg.norm(phase_stripped - encoding3, 2))
    stripped_covariance_failures = 0
    reducer = c305.StabilizerReducer(code)
    base = sector_encoder(code, (0, 0, 0), 3)
    for frame in c235.proper_cubic_frames():
        representation = exterior_representation(frame, 3)
        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, repair_pairs, flips = c269.repair_data(
            code.graph, vertex_map, edge_map
        )
        target = sector_encoder(code, (0, 0, 0), 3)
        for source_index, source_branches in enumerate(base.columns_by_label):
            target_index = int(np.argmax(abs(representation[:, source_index])))
            expected_sign = representation[target_index, source_index]
            target_by_carrier = {
                branch.carrier_direction: branch
                for branch in target.columns_by_label[target_index]
            }
            for source_branch in source_branches:
                source_vertex = c305.body_vertices(code, (0, 0, 0))[
                    source_branch.carrier_direction
                ]
                target_carrier = code.graph.vertices[vertex_map[source_vertex]][1]
                target_branch = target_by_carrier[target_carrier]
                transformed = local.transform_pauli(
                    code,
                    source_branch.input_face_pauli,
                    edge_map,
                    toggles,
                    repair_pairs,
                    flips,
                )
                phase = reducer.relative_phase(
                    transformed, target_branch.input_face_pauli
                )
                stripped_covariance_failures += phase is None or abs(
                    phase_scalar(phase or 0) - expected_sign
                ) > TOLERANCE

    encoder4 = sector_encoder(code, (0, 0, 0), 4)
    basis4, _encoding4 = ambient_encoding(encoder4)
    catchup_inside = 0
    basis4_set = set(basis4)
    for phase, x_bits, z_bits, tags in basis4:
        pauli = c235.Pauli(phase, x_bits, z_bits)
        output, _active, _scalar = face_stream_action(code, pauli)
        catchup_inside += micro_key(output, tags) in basis4_set

    rejected = 0
    for bad in (((0, 0, 1), 2), ((0, 1, 2), 1), ((0, 1, 6), 3)):
        try:
            three_carrier_branch(code, (0, 0, 0), bad[0], bad[1])
        except (KeyError, ValueError):
            rejected += 1
    for number in (2, 5):
        try:
            sector_encoder(code, (0, 0, 0), number)
        except ValueError:
            rejected += 1
    for body in ((-1, 0, 0), (code.length, 0, 0)):
        try:
            sector_encoder(code, body, 4)
        except ValueError:
            rejected += 1
    for matrix, number in ((np.eye(5), 3), (np.full((6, 6), np.nan), 4), (np.eye(6), 2)):
        try:
            exterior_matrix(matrix, number)
        except ValueError:
            rejected += 1
    try:
        c269.build_code(2)
    except ValueError:
        rejected += 1

    check(
        "proper-cubic orbit, carrier-branch, orientation-phase, catch-up, coin-term, contact-term, and code-column deletions are detected",
        all(
            row["one_orbit_coin_leakage_operator_norm"] > 0.5
            and abs(row["deleted_coin_coefficient"]) > 0.1
            and row["deleted_coin_unitarity_residual"] > 0.1
            and row["one_column_stream_leakage"] == 1
            and row["deleted_contact_residual"] > 1
            and abs(row["mutated_ambient_coin_coefficient"]) > 0.03
            and row["mutated_ambient_coin_intertwiner_residual"] > 0.03
            and row["mutated_ambient_coin_unitarity_residual"] > 0.03
            for row in leakage_rows
        )
        and carrier_deletion_gram > 0.3
        and carrier_phase_change > 1
        and stripped_covariance_failures > 0
        and catchup_inside == 0,
        {
            "sector_rows": leakage_rows,
            "one_of_three_carrier_branch_deletion_gram_residual": carrier_deletion_gram,
            "carrier_orientation_phase_deletion_residual": carrier_phase_change,
            "carrier_orientation_phase_deletion_covariance_failures": stripped_covariance_failures,
            "stream_without_catchup_microstates_in_code": catchup_inside,
        },
    )
    check(
        "the higher-number interface rejects repeated directions, occupied carrier ports, bad sectors, bodies, matrices, and aliased L=2",
        rejected == 11,
        {"rejected_fixtures": rejected},
    )


def inventory_and_boundary(geometry_rows) -> None:
    print("\nSUPPLIED-STRUCTURE INVENTORY / EXACT BOUNDARY")
    maxima = {
        number: max(
            max(row["total_supports_M2"])
            for row in geometry_rows
            if row["n"] == number
        )
        for number in SECTORS
    }
    check(
        "Cycle 308 supplies bounded n=3-carrier and direct n=4 fixed seams, not recurrence, overlap, preparation, full Fock, time, source, or probability physics",
        True,
        {
            "derived": (
                "complete 20-dimensional wedge^3 and 15-dimensional wedge^4 occupation bases",
                "one covariant three-branch complement-port parity carrier for every logical triple",
                "direct fixed-Wilson Hodge representatives for every logical quadruple",
                "input-slice exterior coin comparators, stream/catch-up, contact, and D S K compositions",
                "proper-cubic exterior representations, exact group laws, translations, and held L=6",
                "bounded matrix-unit completions and destructive controls",
            ),
            "supplied": (
                "fixed +++ Wilson and all-B=+1 reference vacuum",
                "one body-cell address, six directions, and the Cycle-269 framing repair",
                "six collision-safe zero-initialized port M2 per cell",
                "Cycle-219 six-mode coin coefficient matrix",
                "Cycle-230 coupling g=0.37 and coin-stream-contact order",
                "the fixed-seam code domain and locally supplied dense matrix-unit coefficients",
                "preparation of the conditional n=3 carrier superposition",
            ),
            "open": (
                "actual separated-cell recurrent onsite coins",
                "simultaneous overlapping shells and collision arrival sectors",
                "absolute reference, carrier, and arbitrary coherent-position preparation",
                "n=0,1,2,5,6 common-sector integration and a full-Fock compiler",
                "primitive synthesis of dense local comparator polynomials",
            ),
            "not_claimed": (
                "physical time, rate, or energy from comparator phases or substeps",
                "mass, source, gravity, Record, occurrence, or Born probability",
                "a direct three-physical-particle state in the total-even face code",
                "a recurrent law from the separated-slice identity completion",
            ),
            "bounded_support_maxima_M2": maxima,
            "installed_overhead": "15 face + 6 port = 21 M2 per cell; no new M2 species",
            "global_Jordan_Wigner_order": False,
            "global_parity_service": False,
            "preferred_carrier_direction": False,
            "host_side_control": False,
            "authority": "none",
            "audit": "unset",
            "broad_no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    print("CYCLE 308: HIGHER-NUMBER PHYSICAL FIXED-SEAM TOURNAMENT")
    print("authority=none; audit=unset")
    note_contract()
    cache = {length: c269.build_code(length) for length in SIZES}
    path_and_parity_carrier_controls(cache)
    fixtures, geometry_rows = geometry_and_constraint_controls(cache)
    matrix_unit_controls(fixtures)
    exterior_and_operator_controls(fixtures)
    covariance_controls(cache[3])
    one_particle_mass_firewall()
    deletion_and_domain_controls(cache[3])
    inventory_and_boundary(geometry_rows)
    print(f"SUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
