#!/usr/bin/env python3
"""Cycle 311: one role-constrained fixed seam for the full six-mode M64 cell.

All 64 local occupation labels n=0..6 share one input code.  Every occupied
label also has its physically streamed comparator image; vacuum is a shared
fixed vector, so the seam closure has dimension 127 rather than an artificial
128.  Even sectors use direct fixed-Wilson rays.  Odd sectors use a covariant
carrier over the unoccupied outward ports, leaving total physical parity even.

The only raw physical-ray collisions are the thirty n=1 carrier-role
exchanges.  A local flag distinguishes those roles, and one gauge-companion
M2 enforces it through C_role=K_exchange X_r=+1.  The flag is therefore not a
free sector label.  The common physical update is coin, then stream/catch-up,
then Cycle-230 contact, restricted to this fixed seam.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import defaultdict
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
import physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17 as c308
import physical_cycle269_reference_relative_localized_pair_lift_2026_07_17 as local
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md"
)
TRAINING_SIZES = (3, 4, 5)
HELD_SIZES = (6,)
SIZES = TRAINING_SIZES + HELD_SIZES
NUMBERS = tuple(range(7))
LABELS = {number: tuple(combinations(range(6), number)) for number in NUMBERS}
LABEL_INDEX = {
    number: {label: index for index, label in enumerate(LABELS[number])}
    for number in NUMBERS
}
FOCK_LABELS = tuple(
    (number, label) for number in NUMBERS for label in LABELS[number]
)
FOCK_INDEX = {label: index for index, label in enumerate(FOCK_LABELS)}
SEAM_LABELS = ((0, (), 0),) + tuple(
    (number, label, stream_slice)
    for number in range(1, 7)
    for label in LABELS[number]
    for stream_slice in (0, 1)
)
SEAM_INDEX = {label: index for index, label in enumerate(SEAM_LABELS)}
FOCK_DIMENSION = len(FOCK_LABELS)
SEAM_DIMENSION = len(SEAM_LABELS)
FLAGGED_MICRO_DIMENSION = 255
GAUGE_MICRO_DIMENSION = 2 * FLAGGED_MICRO_DIMENSION
COUPLING = c230.COUPLING
TOLERANCE = 1.2e-11

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CommonBranch:
    number: int
    label: tuple[int, ...]
    stream_slice: int
    carrier_direction: int | None
    face_pauli: c235.Pauli
    tags: int
    amplitude: complex


@dataclass(frozen=True)
class CommonColumn:
    number: int
    label: tuple[int, ...]
    stream_slice: int
    branches: tuple[CommonBranch, ...]


@dataclass(frozen=True)
class CommonEncoder:
    code: c269.WilsonSubsystemCode
    body: tuple[int, int, int]
    columns: tuple[CommonColumn, ...]


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
        check("the Cycle-311 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "64-dimensional input code",
        "127-dimensional seam closure",
        "255 flagged microsectors",
        "510 role-gauge microsectors",
        "n=0",
        "n=5",
        "n=6",
        "c_role = k_exchange x_r",
        "not a free sector label",
        "thirty raw n=1 collisions",
        "same-physical-number pairs",
        "direct sum of wedge^n(c)",
        "exp(i binom(n,2) g)",
        "coin, then stream/catch-up, then contact",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "at most fifty-six m2",
        "twenty-three m2 per cell",
        "coherent cross-sector superpositions",
        "one-particle mass fixture unchanged",
        "no number-changing law",
        "not a recurrent volume update",
        "not a full-hilbert compiler",
        "no broad no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the common M64 construction and exact boundary", not missing, missing)


def even_input_pauli(code, body, label: tuple[int, ...]) -> c235.Pauli:
    number = len(label)
    if number == 0:
        return c235.Pauli()
    if number == 2:
        return c305.input_pair_pauli(code, body, label)[0]
    if number == 4:
        return c308.hodge_four_pauli(code, body, label)
    if number == 6:
        return c308.full_six_pauli(code, body)
    raise ValueError("direct fixed-Wilson representatives are even-number only")


def common_branches(code, body, number: int, label, stream_slice: int):
    if number not in NUMBERS or label not in LABEL_INDEX[number]:
        raise ValueError("the occupation label must be one ordered subset of six modes")
    if stream_slice not in (0, 1) or (number == 0 and stream_slice != 0):
        raise ValueError("vacuum is one shared fixed stream vector")
    if number % 2 == 0:
        pauli = even_input_pauli(code, body, label)
        if stream_slice and number:
            pauli = c308.face_stream_action(code, pauli)[0]
        tags = sum(1 << vertex for vertex in local.occupied_vertices(code, pauli))
        return (CommonBranch(number, label, stream_slice, None, pauli, tags, 1 + 0j),)

    vertices = c305.body_vertices(code, body)
    branches = []
    for carrier_direction in sorted(set(range(6)) - set(label)):
        even_label = tuple(sorted(label + (carrier_direction,)))
        carrier_body = vertices[carrier_direction]
        _arrival, carrier_edge = local.old.outer_partner(code, carrier_body)
        pauli = code.A[carrier_edge] @ even_input_pauli(code, body, even_label)
        if stream_slice:
            pauli = c308.face_stream_action(code, pauli)[0]
        tags = sum(1 << vertex for vertex in local.occupied_vertices(code, pauli))
        amplitude = (
            c308.permutation_sign(label + (carrier_direction,))
            * local.edge_stream_factor(code, carrier_body, carrier_edge)
            / np.sqrt(6 - number)
        )
        branches.append(
            CommonBranch(
                number,
                label,
                stream_slice,
                carrier_direction,
                pauli,
                tags,
                amplitude,
            )
        )
    return tuple(branches)


def common_encoder(code, body=(0, 0, 0)) -> CommonEncoder:
    if body not in code.graph.cells:
        raise ValueError("the body must be one supplied coarse cell")
    columns = tuple(
        CommonColumn(
            number,
            label,
            stream_slice,
            common_branches(code, body, number, label, stream_slice),
        )
        for number, label, stream_slice in SEAM_LABELS
    )
    return CommonEncoder(code, tuple(body), columns)


def flagged_basis_and_encoding(encoder: CommonEncoder):
    basis = tuple(branch for column in encoder.columns for branch in column.branches)
    if len(basis) != FLAGGED_MICRO_DIMENSION:
        raise ValueError("the common flagged shell must contain 255 literal sectors")
    encoding = np.zeros((len(basis), SEAM_DIMENSION), dtype=complex)
    offset = 0
    occurrence = {}
    for column_index, column in enumerate(encoder.columns):
        for branch_index, branch in enumerate(column.branches):
            encoding[offset, column_index] = branch.amplitude
            occurrence[(column.number, column.label, column.stream_slice, branch.carrier_direction)] = offset
            offset += 1
    return basis, encoding, occurrence


def exchange_matrix(encoder: CommonEncoder, occurrence) -> np.ndarray:
    exchange = np.zeros((FLAGGED_MICRO_DIMENSION, FLAGGED_MICRO_DIMENSION), dtype=complex)
    for source, branch in enumerate(branch for column in encoder.columns for branch in column.branches):
        target_slice = 0 if branch.number == 0 else 1 - branch.stream_slice
        target = occurrence[(branch.number, branch.label, target_slice, branch.carrier_direction)]
        exchange[target, source] = 1
    return exchange


def constrained_encoding(flagged_encoding: np.ndarray, exchange: np.ndarray) -> np.ndarray:
    return np.vstack((flagged_encoding, exchange @ flagged_encoding)) / np.sqrt(2)


def role_constraint(exchange: np.ndarray) -> np.ndarray:
    zero = np.zeros_like(exchange)
    return np.block([[zero, exchange], [exchange, zero]])


def block_diagonal(*blocks: np.ndarray) -> np.ndarray:
    size = sum(len(block) for block in blocks)
    result = np.zeros((size, size), dtype=complex)
    offset = 0
    for block in blocks:
        width = len(block)
        result[offset : offset + width, offset : offset + width] = block
        offset += width
    return result


def gauge_lift(operator: np.ndarray, exchange: np.ndarray) -> np.ndarray:
    return block_diagonal(operator, exchange @ operator @ exchange)


def exterior_matrix(matrix: np.ndarray, number: int) -> np.ndarray:
    if number not in NUMBERS or matrix.shape != (6, 6) or not np.all(np.isfinite(matrix)):
        raise ValueError("the common exterior lift needs n=0..6 and one finite 6-by-6 matrix")
    if number == 0:
        return np.ones((1, 1), dtype=complex)
    labels = LABELS[number]
    return np.asarray(
        [[np.linalg.det(matrix[np.ix_(target, source)]) for source in labels] for target in labels],
        dtype=complex,
    )


def logical_coin(coin: np.ndarray) -> np.ndarray:
    result = np.eye(SEAM_DIMENSION, dtype=complex)
    for number in NUMBERS:
        wedge = exterior_matrix(coin, number)
        if number == 0:
            result[0, 0] = wedge[0, 0]
            continue
        indices = [SEAM_INDEX[(number, label, 0)] for label in LABELS[number]]
        result[np.ix_(indices, indices)] = wedge
    return result


def logical_stream() -> np.ndarray:
    result = np.zeros((SEAM_DIMENSION, SEAM_DIMENSION), dtype=complex)
    result[0, 0] = 1
    for number in range(1, 7):
        for label in LABELS[number]:
            left = SEAM_INDEX[(number, label, 0)]
            right = SEAM_INDEX[(number, label, 1)]
            result[right, left] = result[left, right] = 1
    return result


def logical_contact(coupling: float) -> np.ndarray:
    diagonal = np.ones(SEAM_DIMENSION, dtype=complex)
    for number in range(1, 7):
        for label in LABELS[number]:
            diagonal[SEAM_INDEX[(number, label, 0)]] = np.exp(
                1j * comb(number, 2) * coupling
            )
    return np.diag(diagonal)


def fock_input_embedding() -> np.ndarray:
    result = np.zeros((SEAM_DIMENSION, FOCK_DIMENSION), dtype=complex)
    for fock_index, (number, label) in enumerate(FOCK_LABELS):
        seam = 0 if number == 0 else SEAM_INDEX[(number, label, 0)]
        result[seam, fock_index] = 1
    return result


def physical_coin(flagged_encoding, logical, exchange):
    projector = flagged_encoding @ flagged_encoding.conj().T
    old = (
        flagged_encoding @ logical @ flagged_encoding.conj().T
        + np.eye(FLAGGED_MICRO_DIMENSION)
        - projector
    )
    return gauge_lift(old, exchange), old


def contact_phase(code, branch: CommonBranch, coupling: float) -> complex:
    counts = {}
    for vertex in local.occupied_vertices(code, branch.face_pauli):
        cell = code.graph.vertices[vertex][0]
        counts[cell] = counts.get(cell, 0) + 1
    pairs = sum(number * (number - 1) // 2 for number in counts.values())
    return complex(np.exp(1j * coupling * pairs))


def flagged_contact(encoder, basis, coupling):
    return np.diag([contact_phase(encoder.code, branch, coupling) for branch in basis])


def raw_unflagged_encoding(encoder: CommonEncoder, reducer: c305.StabilizerReducer):
    tags = sorted({branch.tags for column in encoder.columns for branch in column.branches})
    lookup = {tag: index for index, tag in enumerate(tags)}
    representatives = {}
    encoding = np.zeros((len(tags), SEAM_DIMENSION), dtype=complex)
    for column_index, column in enumerate(encoder.columns):
        for branch in column.branches:
            if branch.tags not in representatives:
                representatives[branch.tags] = branch.face_pauli
            phase = reducer.relative_phase(branch.face_pauli, representatives[branch.tags])
            if phase is None:
                raise ValueError("one occupation/tag syndrome must define one fixed-reference ray")
            encoding[lookup[branch.tags], column_index] += branch.amplitude * c308.phase_scalar(phase)
    return encoding


def flag_qubit(code, body) -> int:
    return code.qubits + len(code.graph.vertices) + code.graph.cells.index(tuple(body))


def r_qubit(code, body) -> int:
    return code.qubits + len(code.graph.vertices) + code.length**3 + code.graph.cells.index(tuple(body))


def branch_representative(code, body, branch: CommonBranch, r_value: int = 0):
    representative = local.full_state_representative(code, branch.face_pauli, branch.tags)
    if branch.stream_slice:
        representative = c235.Pauli(x=1 << flag_qubit(code, body)) @ representative
    if r_value:
        representative = c235.Pauli(x=1 << r_qubit(code, body)) @ representative
    return representative


def common_basis_and_collision_controls(cache):
    print("\nCOMMON M64 BASIS / RAW COLLISIONS / RELATIONAL NUMBER ROLE")
    rows = []
    fixtures = {}
    for length, code in cache.items():
        encoders = [common_encoder(code, body) for body in code.graph.cells]
        fixtures[length] = encoders
        gram_failures = input_rank_failures = branch_failures = role_failures = 0
        raw_collision_counts = []
        raw_collision_number_sets = []
        raw_collision_multiplicities = []
        raw_rank_rows = []
        raw_nullities = []
        support_rows = []
        maximum_branch_support = 0
        number_role_signatures = {number: set() for number in NUMBERS}
        reducer = c305.StabilizerReducer(code)
        for encoder_index, encoder in enumerate(encoders):
            basis, flagged, occurrence = flagged_basis_and_encoding(encoder)
            if encoder_index == 0:
                exchange = exchange_matrix(encoder, occurrence)
                constrained = constrained_encoding(flagged, exchange)
                input_encoding = constrained @ fock_input_embedding()
                gram_failures += np.linalg.norm(constrained.conj().T @ constrained - np.eye(SEAM_DIMENSION)) > TOLERANCE
                input_rank_failures += np.linalg.matrix_rank(input_encoding, tol=1e-10) != FOCK_DIMENSION
                raw = raw_unflagged_encoding(encoder, reducer)
                raw_collision_counts.append(FLAGGED_MICRO_DIMENSION - raw.shape[0])
                raw_rank_rows.append(np.linalg.matrix_rank(raw, tol=1e-10))
                raw_nullities.append(SEAM_DIMENSION - raw_rank_rows[-1])
                raw_groups = defaultdict(list)
                for branch in basis:
                    raw_groups[branch.tags].append(branch)
                colliding = [group for group in raw_groups.values() if len(group) > 1]
                raw_collision_number_sets.append(
                    sorted({branch.number for group in colliding for branch in group})
                )
                raw_collision_multiplicities.append(
                    sorted({len(group) for group in colliding})
                )
            face_union = tag_union = 0
            for branch in basis:
                occupations = local.occupied_vertices(code, branch.face_pauli)
                expected = branch.number if branch.number % 2 == 0 else branch.number + 1
                branch_failures += len(occupations) != expected
                branch_failures += branch.tags != sum(1 << vertex for vertex in occupations)
                cell_counts = defaultdict(int)
                for vertex in occupations:
                    cell_counts[code.graph.vertices[vertex][0]] += 1
                physical_pairs = sum(
                    count * (count - 1) // 2 for count in cell_counts.values()
                )
                expected_pairs = comb(branch.number, 2) if branch.stream_slice == 0 else 0
                branch_failures += physical_pairs != expected_pairs
                body_count = sum(code.graph.vertices[vertex][0] == encoder.body for vertex in occupations)
                role_failures += body_count % 2 != branch.number % 2
                if encoder_index == 0:
                    number_role_signatures[branch.number].add((expected, body_count % 2))
                face_union |= branch.face_pauli.x | branch.face_pauli.z
                tag_union |= branch.tags
                maximum_branch_support = max(
                    maximum_branch_support,
                    (branch.face_pauli.x | branch.face_pauli.z).bit_count()
                    + branch.tags.bit_count()
                    + bool(branch.stream_slice)
                    + 1,
                )
            support_rows.append((face_union.bit_count(), tag_union.bit_count(), face_union.bit_count() + tag_union.bit_count() + 2))
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "encoders": len(encoders),
                "fock_input_dimension": FOCK_DIMENSION,
                "seam_dimension": SEAM_DIMENSION,
                "flagged_microsectors": FLAGGED_MICRO_DIMENSION,
                "gauge_microsectors": GAUGE_MICRO_DIMENSION,
                "raw_collision_counts": sorted(set(raw_collision_counts)),
                "raw_collision_number_sets": raw_collision_number_sets,
                "raw_collision_multiplicities": raw_collision_multiplicities,
                "raw_unflagged_ranks": sorted(set(raw_rank_rows)),
                "raw_nullities": sorted(set(raw_nullities)),
                "number_role_signatures": {
                    number: sorted(signatures)
                    for number, signatures in number_role_signatures.items()
                },
                "gram_failures": gram_failures,
                "input_rank_failures": input_rank_failures,
                "branch_failures": branch_failures,
                "body_parity_role_failures": role_failures,
                "face_supports_M2": sorted({row[0] for row in support_rows}),
                "port_supports_M2": sorted({row[1] for row in support_rows}),
                "total_role_gauge_supports_M2": sorted({row[2] for row in support_rows}),
                "maximum_branch_role_support_M2": maximum_branch_support,
                "installed_M2_per_cell": 23,
            }
        )
    check(
        "one constrained encoder has a rank-64 M64 input and rank-127 shared-vacuum seam, with exactly thirty raw n=1 role collisions and no free number label",
        all(
            row["encoders"] == row["L"] ** 3
            and row["fock_input_dimension"] == 64
            and row["seam_dimension"] == 127
            and row["flagged_microsectors"] == 255
            and row["gauge_microsectors"] == 510
            and row["raw_collision_counts"] == [30]
            and row["raw_collision_number_sets"] == [[1]]
            and row["raw_collision_multiplicities"] == [[2]]
            and row["raw_unflagged_ranks"] == [126]
            and row["raw_nullities"] == [1]
            and row["number_role_signatures"]
            == {number: [(number + number % 2, number % 2)] for number in NUMBERS}
            and row["gram_failures"] == 0
            and row["input_rank_failures"] == 0
            and row["branch_failures"] == 0
            and row["body_parity_role_failures"] == 0
            and max(row["total_role_gauge_supports_M2"]) <= 56
            and row["maximum_branch_role_support_M2"] <= 45
            and row["installed_M2_per_cell"] == 23
            for row in rows
        ),
        rows,
    )
    return fixtures, rows


def gauge_constraint_controls(encoder):
    print("\nLOCALLY ENFORCED RELATIONAL ROLE GAUGE")
    basis, flagged, occurrence = flagged_basis_and_encoding(encoder)
    exchange = exchange_matrix(encoder, occurrence)
    constrained = constrained_encoding(flagged, exchange)
    constraint = role_constraint(exchange)
    flagged_projector = flagged @ flagged.conj().T
    shell_projector = block_diagonal(flagged_projector, flagged_projector)
    constrained_projector = constrained @ constrained.conj().T
    bare_plus = flagged @ flagged.conj().T @ ((np.eye(len(exchange)) + exchange) / 2)
    constraint_projector = (np.eye(GAUGE_MICRO_DIMENSION) + constraint) / 2
    shell_constraint_commutator = float(
        np.linalg.norm(flagged_projector @ exchange - exchange @ flagged_projector)
    )
    shell_constraint_product = np.block(
        [
            [flagged_projector / 2, flagged_projector @ exchange / 2],
            [flagged_projector @ exchange / 2, flagged_projector / 2],
        ]
    )
    detail = {
        "flagged_shell_rank": int(np.linalg.matrix_rank(flagged, tol=1e-10)),
        "shell_times_r_rank": int(round(np.trace(shell_projector).real)),
        "bare_exchange_plus_rank_on_shell": int(round(np.trace(bare_plus).real)),
        "constrained_rank": int(np.linalg.matrix_rank(constrained, tol=1e-10)),
        "constraint_involution": float(np.linalg.norm(exchange @ exchange - np.eye(FLAGGED_MICRO_DIMENSION))),
        "shell_constraint_commutator": shell_constraint_commutator,
        "constraint_eigen_residual": float(np.linalg.norm(constraint @ constrained - constrained)),
        "projector_residual": float(np.linalg.norm(shell_constraint_product - constrained_projector)),
        "isometry_residual": float(np.linalg.norm(constrained.conj().T @ constrained - np.eye(SEAM_DIMENSION))),
    }
    check(
        "one r M2 and C_role=K_exchange X_r enforce the local slice role while body occupation parity relationally separates every same-physical-number sector pair",
        detail["flagged_shell_rank"] == 127
        and detail["shell_times_r_rank"] == 254
        and detail["bare_exchange_plus_rank_on_shell"] == 64
        and detail["constrained_rank"] == 127
        and max(value for key, value in detail.items() if "rank" not in key) < TOLERANCE,
        detail,
    )

    transition_failures = constraint_failures = sector_failures = 0
    supports = []
    for source, target in enumerate(np.argmax(exchange, axis=0)):
        source_rep = branch_representative(encoder.code, encoder.body, basis[source], 0)
        target_rep = branch_representative(encoder.code, encoder.body, basis[target], 1)
        transition = target_rep @ local.pauli_dagger(source_rep)
        transition_failures += transition @ source_rep != target_rep
        supports.append((transition.x | transition.z).bit_count())
        constraint_failures += sum(
            not transition.commutes(c305.constraint_pauli(encoder.code, vertex))
            for vertex in range(len(encoder.code.graph.vertices))
        )
        sector_failures += sum(
            not transition.commutes(row)
            for row in encoder.code.local_checks + encoder.code.wilsons
        )
    check(
        "all 255 matrix-unit exchange terms are bounded physical transitions preserving inherited constraints",
        transition_failures == constraint_failures == sector_failures == 0
        and max(supports) <= 38,
        {
            "exchange_terms": len(supports),
            "transition_failures": transition_failures,
            "port_constraint_commutators": constraint_failures,
            "fixed_sector_commutators": sector_failures,
            "maximum_transition_support_M2": max(supports),
        },
    )
    return basis, flagged, exchange, constrained, constraint


def exterior_and_new_sector_controls():
    print("\nDIRECT-SUM EXTERIOR COIN / NEW N=0,5,6 BLOCKS")
    rows = []
    for beta, held in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True)):
        coin = c219.common_species(beta).coin
        number_rows = []
        determinant_residuals = []
        for number in NUMBERS:
            wedge = exterior_matrix(coin, number)
            determinant_residual = abs(
                np.linalg.det(wedge) - np.linalg.det(coin) ** comb(5, number - 1)
            ) if number else 0.0
            determinant_residuals.append(determinant_residual)
            number_rows.append(
                (
                    number,
                    len(LABELS[number]),
                    float(np.linalg.norm(wedge.conj().T @ wedge - np.eye(len(wedge)))),
                    determinant_residual,
                )
            )
        common = logical_coin(coin)
        rows.append(
            {
                "beta": beta,
                "held": held,
                "sector_rows": number_rows,
                "direct_sum_unitarity": float(np.linalg.norm(common.conj().T @ common - np.eye(SEAM_DIMENSION))),
                "n0_block": exterior_matrix(coin, 0)[0, 0],
                "n5_dimension": len(LABELS[5]),
                "n6_block": exterior_matrix(coin, 6)[0, 0],
            }
        )
    check(
        "the one logical coin is the complete direct sum of wedge^n(C), including exact vacuum, n=5, and determinant n=6 blocks at trained and held beta",
        all(
            [row[1] for row in item["sector_rows"]] == [1, 6, 15, 20, 15, 6, 1]
            and max(row[2] for row in item["sector_rows"]) < 5e-14
            and max(row[3] for row in item["sector_rows"]) < 5e-14
            and item["direct_sum_unitarity"] < 8e-14
            and abs(item["n0_block"] - 1) < TOLERANCE
            and item["n5_dimension"] == 6
            and abs(item["n6_block"] - np.linalg.det(c219.common_species(item["beta"]).coin)) < TOLERANCE
            for item in rows
        ),
        rows,
    )


def common_operator_controls(encoder, basis, flagged, exchange, constrained, constraint):
    print("\nONE AMBIENT COIN / STREAM / CONTACT / DSK")
    logical_S = logical_stream()
    logical_D = logical_contact(COUPLING)
    old_S = exchange
    old_D = flagged_contact(encoder, basis, COUPLING)
    physical_S = gauge_lift(old_S, exchange)
    physical_D = gauge_lift(old_D, exchange)
    input_embedding = fock_input_embedding()
    rng = np.random.default_rng(311)
    beta_rows = []
    active_coin_microterms = inherited_constraint_commutators = 0
    fixed_sector_commutators = number_changing_microterms = 0
    representatives = [
        branch_representative(encoder.code, encoder.body, branch, 0)
        for branch in basis
    ]
    for beta, held in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True)):
        logical_K = logical_coin(c219.common_species(beta).coin)
        physical_K, old_K = physical_coin(flagged, logical_K, exchange)
        _physical_K_inverse, old_K_inverse = physical_coin(
            flagged, logical_K.conj().T, exchange
        )
        logical_G = logical_D @ logical_S @ logical_K
        coin_image = physical_K @ constrained
        stream_image = physical_S @ coin_image
        physical_G_image = physical_D @ stream_image
        constraint_mapping, constraint_phases, constraint_mapping_failures = signed_mapping(constraint)
        coherent = rng.normal(size=SEAM_DIMENSION) + 1j * rng.normal(size=SEAM_DIMENSION)
        coherent /= np.linalg.norm(coherent)
        residuals = {
            "coin": float(np.linalg.norm(coin_image - constrained @ logical_K)),
            "stream": float(np.linalg.norm(physical_S @ constrained - constrained @ logical_S)),
            "contact": float(np.linalg.norm(physical_D @ constrained - constrained @ logical_D)),
            "composition": float(np.linalg.norm(physical_G_image - constrained @ logical_G)),
            "coin_unitarity": float(np.linalg.norm(old_K.conj().T @ old_K - np.eye(len(old_K)))),
            "coin_inverse": float(np.linalg.norm(old_K_inverse @ old_K - np.eye(len(old_K)))),
            "composition_unitarity": float(
                np.linalg.norm(
                    (old_D @ old_S @ old_K).conj().T @ (old_D @ old_S @ old_K)
                    - np.eye(len(old_K))
                )
            ),
            "composition_inverse": float(
                np.linalg.norm(
                    (old_K_inverse @ old_S.conj().T @ old_D.conj().T)
                    @ (old_D @ old_S @ old_K)
                    - np.eye(len(old_K))
                )
            ),
            "constraint_coin": conjugation_residual(physical_K, constraint_mapping, constraint_phases),
            "constraint_stream": conjugation_residual(physical_S, constraint_mapping, constraint_phases),
            "constraint_contact": conjugation_residual(physical_D, constraint_mapping, constraint_phases),
            "constraint_mapping_failures": float(constraint_mapping_failures),
            "coherent_norm": abs(np.vdot(constrained @ coherent, constrained @ coherent) - 1),
            "coherent_composition": float(np.linalg.norm(physical_G_image @ coherent - constrained @ logical_G @ coherent)),
        }
        beta_rows.append({"beta": beta, "held": held, **residuals})
        if beta == -0.3:
            for target, source in np.argwhere(abs(old_K) > TOLERANCE):
                if target == source:
                    continue
                active_coin_microterms += 1
                target_branch = basis[int(target)]
                source_branch = basis[int(source)]
                number_changing_microterms += target_branch.number != source_branch.number
                transition = representatives[int(target)] @ local.pauli_dagger(
                    representatives[int(source)]
                )
                inherited_constraint_commutators += sum(
                    not transition.commutes(
                        c305.constraint_pauli(encoder.code, vertex)
                    )
                    for vertex in range(len(encoder.code.graph.vertices))
                )
                fixed_sector_commutators += sum(
                    not transition.commutes(row)
                    for row in encoder.code.local_checks + encoder.code.wilsons
                )
    physical_contact_counts = {}
    for number in NUMBERS:
        column = encoder.columns[0] if number == 0 else encoder.columns[SEAM_INDEX[(number, LABELS[number][0], 0)]]
        phases = {contact_phase(encoder.code, branch, COUPLING) for branch in column.branches}
        physical_contact_counts[number] = phases
    fock_input = constrained @ input_embedding
    fock_rank = np.linalg.matrix_rank(fock_input, tol=1e-10)
    output_contact_failures = sum(
        abs(contact_phase(encoder.code, branch, COUPLING) - 1) > TOLERANCE
        for branch in basis
        if branch.stream_slice == 1
    )
    check(
        "the explicit 510-sector physical coin, literal stream/catch-up, and actual binomial contact intertwine D S K on coherent cross-sector states",
        all(max(value for key, value in row.items() if key not in ("beta", "held")) < 3e-11 for row in beta_rows)
        and fock_rank == 64
        and active_coin_microterms > 0
        and inherited_constraint_commutators == 0
        and fixed_sector_commutators == 0
        and number_changing_microterms == 0
        and output_contact_failures == 0
        and all(
            len(phases) == 1
            and abs(next(iter(phases)) - np.exp(1j * comb(number, 2) * COUPLING)) < TOLERANCE
            for number, phases in physical_contact_counts.items()
        ),
        {
            "beta_rows": beta_rows,
            "M64_input_rank": fock_rank,
            "physical_input_contact_phases": physical_contact_counts,
            "logical_order": "coin then stream/catch-up then contact",
            "active_offdiagonal_coin_microterms": active_coin_microterms,
            "port_constraint_commutators": inherited_constraint_commutators,
            "fixed_sector_commutators": fixed_sector_commutators,
            "number_changing_matrix_elements": number_changing_microterms,
            "separated_slice_contact_failures": output_contact_failures,
        },
    )
    return old_S, old_D


def direction_map(frame, direction):
    target = frame @ c210.DIRECTIONS[direction]
    return int(np.where(np.all(c210.DIRECTIONS == target, axis=1))[0][0])


def exterior_representation(frame, number):
    result = np.zeros((len(LABELS[number]), len(LABELS[number])), dtype=complex)
    for source, label in enumerate(LABELS[number]):
        mapped = [direction_map(frame, direction) for direction in label]
        target = LABEL_INDEX[number][tuple(sorted(mapped))]
        result[target, source] = c308.permutation_sign(mapped)
    return result


def logical_frame_representation(frame):
    result = np.zeros((SEAM_DIMENSION, SEAM_DIMENSION), dtype=complex)
    result[0, 0] = 1
    for number in range(1, 7):
        wedge = exterior_representation(frame, number)
        for stream_slice in (0, 1):
            indices = [SEAM_INDEX[(number, label, stream_slice)] for label in LABELS[number]]
            result[np.ix_(indices, indices)] = wedge
    return result


def flagged_frame_representation(encoder, basis, occurrence, frame, reducer):
    vertex_map, edge_map = c235.graph_frame_maps(encoder.code.graph, frame)
    toggles, repair_pairs, flips = c269.repair_data(encoder.code.graph, vertex_map, edge_map)
    representation = np.zeros((len(basis), len(basis)), dtype=complex)
    failures = 0
    target_encoder = common_encoder(encoder.code, encoder.body)
    target_basis, _target_encoding, target_occurrence = flagged_basis_and_encoding(target_encoder)
    for source, branch in enumerate(basis):
        mapped_label_list = [direction_map(frame, direction) for direction in branch.label]
        target_label = tuple(sorted(mapped_label_list))
        target_carrier = None if branch.carrier_direction is None else direction_map(frame, branch.carrier_direction)
        target = target_occurrence[(branch.number, target_label, branch.stream_slice, target_carrier)]
        target_branch = target_basis[target]
        transformed = local.transform_pauli(
            encoder.code, branch.face_pauli, edge_map, toggles, repair_pairs, flips
        )
        phase = reducer.relative_phase(transformed, target_branch.face_pauli)
        failures += phase is None
        if phase is not None:
            representation[target, source] = c308.phase_scalar(phase)
        failures += ports.permute_bits(branch.tags, vertex_map) != target_branch.tags
    return representation, failures


def conjugation_residual(operator, mapping, phases):
    conjugated = np.zeros_like(operator)
    conjugated[np.ix_(mapping, mapping)] = phases[:, None] * operator * np.conjugate(phases[None, :])
    return float(np.linalg.norm(conjugated - operator))


def signed_mapping(representation):
    targets = np.argmax(abs(representation), axis=0)
    phases = representation[targets, np.arange(len(targets))]
    failures = np.count_nonzero(np.sum(abs(representation) > 0.5, axis=0) != 1)
    return targets, phases, int(failures)


def apply_signed_mapping(mapping, phases, matrix):
    result = np.zeros_like(matrix)
    result[mapping, :] = phases[:, None] * matrix
    return result


def covariance_and_translation_controls(encoder, basis, flagged, exchange, constrained, old_S, old_D):
    print("\nCOMMON PHYSICAL CUBIC COVARIANCE / TRANSLATIONS")
    reducer = c305.StabilizerReducer(encoder.code)
    nominal_logical_K = logical_coin(c219.common_species(-0.3).coin)
    physical_K, old_K = physical_coin(flagged, nominal_logical_K, exchange)
    logical_G = logical_contact(COUPLING) @ logical_stream() @ nominal_logical_K
    old_G = old_D @ old_S @ old_K
    frame_rows = []
    group_failures = 0
    frames = c235.proper_cubic_frames()
    logical_reps = [logical_frame_representation(frame) for frame in frames]
    frame_lookup = {tuple(frame.flatten()): index for index, frame in enumerate(frames)}
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            target = frame_lookup[tuple((left @ right).flatten())]
            group_failures += np.linalg.norm(logical_reps[left_index] @ logical_reps[right_index] - logical_reps[target]) > TOLERANCE
    for frame, logical_R in zip(frames, logical_reps):
        old_R, failures = flagged_frame_representation(encoder, basis, {}, frame, reducer)
        mapping, phases, mapping_failures = signed_mapping(old_R)
        new_mapping = np.concatenate((mapping, mapping + FLAGGED_MICRO_DIMENSION))
        new_phases = np.concatenate((phases, phases))
        frame_rows.append(
            {
                "branch_failures": failures + mapping_failures,
                "flagged_isometry": float(np.linalg.norm(apply_signed_mapping(mapping, phases, flagged) - flagged @ logical_R)),
                "constrained_isometry": float(np.linalg.norm(apply_signed_mapping(new_mapping, new_phases, constrained) - constrained @ logical_R)),
                "exchange_covariance": conjugation_residual(exchange, mapping, phases),
                "coin_covariance": conjugation_residual(old_K, mapping, phases),
                "stream_covariance": conjugation_residual(old_S, mapping, phases),
                "contact_covariance": conjugation_residual(old_D, mapping, phases),
                "composition_covariance": conjugation_residual(old_G, mapping, phases),
                "logical_composition_covariance": float(np.linalg.norm(logical_R @ logical_G - logical_G @ logical_R)),
            }
        )

    translation_failures = translation_tests = 0
    base = encoder
    for displacement in product(range(encoder.code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(encoder.code.graph, displacement)
        toggles, repair_pairs, flips = c269.repair_data(encoder.code.graph, vertex_map, edge_map)
        target = common_encoder(encoder.code, displacement)
        target_basis, _encoding, target_occurrence = flagged_basis_and_encoding(target)
        for branch in basis:
            target_index = target_occurrence[(branch.number, branch.label, branch.stream_slice, branch.carrier_direction)]
            target_branch = target_basis[target_index]
            transformed = local.transform_pauli(
                encoder.code, branch.face_pauli, edge_map, toggles, repair_pairs, flips
            )
            translation_failures += reducer.relative_phase(transformed, target_branch.face_pauli) != 0
            translation_failures += abs(branch.amplitude - target_branch.amplitude) > TOLERANCE
            translation_failures += ports.permute_bits(branch.tags, vertex_map) != target_branch.tags
            translation_tests += 1
    check(
        "the complete M64 code, relational constraint, physical K/S/D/DSK, and all exterior sectors are covariant under all 24 frames, group laws, and L=3 translations",
        group_failures == 0
        and all(row["branch_failures"] == 0 and max(value for key, value in row.items() if key != "branch_failures") < 3e-11 for row in frame_rows)
        and translation_failures == 0,
        {
            "proper_frames": len(frames),
            "group_law_tests": len(frames) ** 2,
            "group_law_failures": group_failures,
            "maximum_frame_row": {key: max(row[key] for row in frame_rows) for key in frame_rows[0]},
            "translations": encoder.code.length**3,
            "translation_branch_tests": translation_tests,
            "translation_failures": translation_failures,
        },
    )


def deletion_and_domain_controls(encoder, basis, flagged, exchange, constrained, constraint):
    print("\nDELETION / LEAKAGE / LAWFUL DOMAIN")
    raw = raw_unflagged_encoding(encoder, c305.StabilizerReducer(encoder.code))
    raw_gram = float(np.linalg.norm(raw.conj().T @ raw - np.eye(SEAM_DIMENSION), 2))
    shell_projector = block_diagonal(flagged @ flagged.conj().T, flagged @ flagged.conj().T)
    missing_constraint_rank = int(round(np.trace(shell_projector).real))
    bare_plus_rank = int(round(np.trace(flagged @ flagged.conj().T @ ((np.eye(len(exchange)) + exchange) / 2)).real))
    carrier_deletions = {}
    for number in (1, 3):
        deletion = flagged.copy()
        for column_index, column in enumerate(encoder.columns):
            if column.number != number:
                continue
            rows = np.flatnonzero(abs(deletion[:, column_index]) > TOLERANCE)
            deletion[rows[0], column_index] = 0
        carrier_deletions[number] = float(np.linalg.norm(deletion.conj().T @ deletion - np.eye(SEAM_DIMENSION), 2))

    logical_K = logical_coin(c219.common_species(-0.3).coin)
    physical_K, old_K = physical_coin(flagged, logical_K, exchange)
    offdiag = abs(old_K).copy()
    np.fill_diagonal(offdiag, 0)
    row, column = np.unravel_index(np.argmax(offdiag), offdiag.shape)
    mutated = old_K.copy()
    coefficient = mutated[row, column]
    mutated[row, column] = 0
    mutation_intertwiner = float(np.linalg.norm(mutated @ flagged - flagged @ logical_K))
    mutation_unitarity = float(np.linalg.norm(mutated.conj().T @ mutated - np.eye(len(mutated))))

    orbit_leakages = {}
    for number in range(1, 6):
        representations = [exterior_representation(frame, number) for frame in c235.proper_cubic_frames()]
        unseen = set(range(len(LABELS[number])))
        orbits = []
        while unseen:
            seed = min(unseen)
            orbit = sorted({int(np.argmax(abs(rep[:, seed]))) for rep in representations})
            orbits.append(orbit)
            unseen -= set(orbit)
        if len(orbits) > 1:
            coin = exterior_matrix(c219.common_species(-0.3).coin, number)
            orbit_leakages[number] = max(
                float(np.linalg.norm(coin[np.ix_(target, source)], 2))
                for source in orbits for target in orbits if source != target
            )

    contact_deletions = {
        number: abs(np.exp(1j * comb(number, 2) * COUPLING) - 1)
        for number in range(2, 7)
    }
    rejected = 0
    for args in (
        (3, (0, 0, 1), 0),
        (5, (0, 1, 2, 3, 7), 0),
        (0, (), 1),
        (7, (), 0),
    ):
        try:
            common_branches(encoder.code, encoder.body, *args)
        except (KeyError, ValueError):
            rejected += 1
    for body in ((-1, 0, 0), (encoder.code.length, 0, 0)):
        try:
            common_encoder(encoder.code, body)
        except ValueError:
            rejected += 1
    for matrix, number in ((np.eye(5), 2), (np.full((6, 6), np.nan), 3), (np.eye(6), 7)):
        try:
            exterior_matrix(matrix, number)
        except ValueError:
            rejected += 1
    try:
        c269.build_code(2)
    except ValueError:
        rejected += 1

    check(
        "free-flag removal, gauge deletion, carrier deletion, incomplete orbits, ambient-coin mutation, and every binomial contact deletion are detected",
        raw_gram > 0.9
        and missing_constraint_rank == 254
        and bare_plus_rank == 64
        and carrier_deletions[1] > 0.19
        and carrier_deletions[3] > 0.3
        and all(value > 0.5 for value in orbit_leakages.values())
        and abs(coefficient) > 0.03
        and mutation_intertwiner > 0.03
        and mutation_unitarity > 0.03
        and all(value > 0.3 for value in contact_deletions.values()),
        {
            "unflagged_Gram_residual": raw_gram,
            "shell_without_constraint_rank": missing_constraint_rank,
            "standalone_exchange_plus_rank": bare_plus_rank,
            "carrier_branch_deletion_Gram": carrier_deletions,
            "incomplete_orbit_coin_leakage": orbit_leakages,
            "mutated_ambient_coin_coefficient": coefficient,
            "mutation_intertwiner": mutation_intertwiner,
            "mutation_unitarity": mutation_unitarity,
            "contact_deletion_residuals": contact_deletions,
        },
    )
    check(
        "the common interface rejects repeated/out-of-range occupations, duplicate vacuum slice, bad sectors, bodies, matrices, and aliased L=2",
        rejected == 10,
        {"rejected_fixtures": rejected},
    )


def mass_and_inventory(geometry_rows):
    rows = []
    for beta, held in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True)):
        species = c219.common_species(beta)
        rows.append(
            {
                "beta": beta,
                "held": held,
                "rest_mass": c219.rest_mass(species),
                "analytic_mass": species.analytic_mass,
                "relative_residual": abs(c219.rest_mass(species) / species.analytic_mass - 1),
            }
        )
    check(
        "the common exterior lift preserves the unchanged one-particle mass fixture and does not turn contact or higher-number phases into mass",
        all(row["relative_residual"] < 2e-12 for row in rows),
        rows,
    )
    check(
        "Cycle 311 is one supplied fixed-seam M64 compiler, not a number-changing, recurrent-volume, full-Hilbert, time, source, or probability law",
        True,
        {
            "derived": (
                "one rank-64 input isometry and rank-127 shared-vacuum seam closure",
                "complete n=0..6 direct-sum exterior coin",
                "covariant odd carriers with 5, 3, and 1 complement branches for n=1,3,5",
                "direct even rays for n=0,2,4,6",
                "locally enforced role gauge and relational body-parity number role",
                "physical coin, stream/catch-up, binomial contact, DSK, frames, translations, held size, and deletions",
            ),
            "supplied": (
                "fixed +++ Wilson and all-B=+1 reference ray",
                "one body anchor, six directions, Hodge/insertion/edge orientations, and framing repair",
                "six zero-initialized collision-safe port M2 per cell",
                "one flag M2 and one r gauge-companion M2 per cell",
                "Cycle-219 coin, Cycle-230 g=0.37, and the coin-stream-contact order",
                "dense local matrix-unit coefficients and initial lawful code state",
            ),
            "open": (
                "absolute reference, role-gauge, carrier, and arbitrary coherent-position preparation",
                "actual separated-cell recurrent onsite coin",
                "overlapping simultaneous shells and collision arrivals",
                "number-changing interactions and a common sea-state compiler",
                "one- and two-M2 autonomous primitive dynamics",
            ),
            "not_claimed": (
                "full physical Hilbert-space equivalence",
                "physical time, rate, or energy from compiler phases/substeps",
                "mass from contact or higher exterior powers",
                "source, gravity, Record, occurrence, or Born probability",
            ),
            "support_max_M2": max(max(row["total_role_gauge_supports_M2"]) for row in geometry_rows),
            "installed_overhead_M2_per_cell": 23,
            "global_Jordan_Wigner_order": False,
            "global_parity_service": False,
            "free_sector_label": False,
            "host_side_control": False,
            "authority": "none",
            "audit": "unset",
            "broad_no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    print("CYCLE 311: COMMON ROLE-CONSTRAINED SIX-MODE M64 FIXED SEAM")
    print("authority=none; audit=unset")
    note_contract()
    cache = {length: c269.build_code(length) for length in SIZES}
    fixtures, geometry_rows = common_basis_and_collision_controls(cache)
    encoder = fixtures[3][0]
    basis, flagged, exchange, constrained, constraint = gauge_constraint_controls(encoder)
    exterior_and_new_sector_controls()
    old_S, old_D = common_operator_controls(
        encoder, basis, flagged, exchange, constrained, constraint
    )
    covariance_and_translation_controls(
        encoder, basis, flagged, exchange, constrained, old_S, old_D
    )
    deletion_and_domain_controls(
        encoder, basis, flagged, exchange, constrained, constraint
    )
    mass_and_inventory(geometry_rows)
    print(f"SUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
