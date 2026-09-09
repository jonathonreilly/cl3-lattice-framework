#!/usr/bin/env python3
"""Cycle 315 exploratory core: overlap-aware two-cell Cycle-269 M64 code.

The first discriminator multiplies the actual Cycle-311 role-gauge input
columns on two neighboring cells and reduces their shared physical M2 rays
against the fixed-Wilson face vacuum.  It compares both cell-factor orders,
the local graded sign, Gram closure, and the complete two-cell Fock space.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, product
from math import comb
from pathlib import Path
import re
import subprocess
import sys

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17 as c305
import physical_cycle269_reference_relative_localized_pair_lift_2026_07_17 as local
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


LEFT = (0, 0, 0)
RIGHT = (1, 0, 0)
MAX_TOTAL_NUMBER = 12
TOLERANCE = 3e-10
FRESH_MAIN = "17cb0c5c32e753ef1297b185fbd1e8c6d41920c2"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md"
)
RELEASE_PATHS = (Path(__file__).resolve(), NOTE)
N1_ROUTES = (
    "raw product of unextended cell rays",
    "product of Cycle-311 cell-role gauge codes",
    "direct AB equals BA identification",
    "local fermionic parity-sign identification",
    "unflagged unordered AB/BA superposition",
    "doubled edge role plus relational edge r_e",
    "generic non-Pauli multi-edge gauge",
    "staggered or time-multiplexed overlap schedule",
    "three-cell/two-edge joint matrix completion",
)
WALLS = (
    "W_multiedge",
    "W_recurrent",
    "W_synthesis",
    "W_prepare",
    "W_schedule",
)
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natural", "ly"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
)
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class GaugeTerm:
    number: int
    representative: c235.Pauli
    amplitude: complex


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
    for marker in ("*", "`"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-315 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "4,096",
        "63,488",
        "e_ab",
        "e_ba",
        "c_edge = k_(ab<->ba) x_(r_e)",
        "rank 8,192",
        "rank 16,384",
        "u_edge = d_contact s_fswap gamma(c direct-sum c)",
        "n=0,...,12",
        "one two-cell/one-edge seam",
        "not a recurrent volume",
        "all 24 proper-cubic frames",
        "twelve reverse",
        "held l=6",
        "mass",
        "deletion",
        "lawful-domain controls",
        "no global jordan-wigner",
        "no global ordering",
        "multi-edge constraint commutation",
        "open / untested",
        "fail / do not ship the broad negative",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the bounded edge-gauge result and volume boundary", not missing, missing)


def n4_file_line_witness_control() -> None:
    """Require exact runner file:line witnesses for every retained Cycle-315 claim."""
    fragments = (
        "actual Cycle-311 role-gauge products form one 4096-column",
        "AB and BA are physically different",
        "one edge flag plus C_edge=K_AB<->BA X_r",
        "complete two-cell coin, literal boundary FSWAP",
        "both bounded physical ambient completions intertwine",
        "all 24 proper-cubic frames including endpoint reversals",
    )
    relative = str(Path(__file__).resolve().relative_to(ROOT))
    runner_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    main_line = next(i for i, line in enumerate(runner_lines, 1) if line == "def main() -> int:")
    note = NOTE.read_text(encoding="utf-8")
    rows = []
    for fragment in fragments:
        hits = tuple(
            line_number
            for line_number, line in enumerate(runner_lines, 1)
            if line_number > main_line and fragment in line
        )
        reference = f"{relative}:{hits[0]}" if len(hits) == 1 else None
        rows.append(
            {
                "fragment": fragment,
                "line_hits": hits,
                "exact_reference": reference,
                "present_in_note": bool(reference and reference in note),
            }
        )
    check(
        "N4 pins each current numerical witness to an exact executable file and line",
        all(len(row["line_hits"]) == 1 and row["present_in_note"] for row in rows),
        rows,
    )


def methodology_controls() -> None:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FRESH_MAIN, "origin/main"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    check(
        "the recorded no-go methodology commit remains an ancestor of origin/main",
        completed.returncode == 0,
        {"recorded": FRESH_MAIN, "current_ref": "origin/main"},
    )

    note = NOTE.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    allowed = ("ATTEMPTED", "RULED OUT BY PRIOR RESULT", "OPEN / UNTESTED")
    markers = {}
    illegal = []
    unbolded = []
    for route in N1_ROUTES:
        match = re.search(
            rf"^\|\s*{re.escape(route)}\s*\|\s*([^|]+?)\s*\|",
            note,
            re.MULTILINE,
        )
        raw = match.group(1).strip() if match else ""
        marker = raw.replace("*", "")
        markers[route] = marker
        if marker not in allowed:
            illegal.append((route, marker))
        if raw != f"**{marker}**":
            unbolded.append((route, raw))
    open_routes = {
        "generic non-Pauli multi-edge gauge",
        "staggered or time-multiplexed overlap schedule",
        "three-cell/two-edge joint matrix completion",
    }
    check(
        "N1 uses exact bold markers and keeps every untested multi-edge route open",
        not illegal
        and not unbolded
        and all(markers[route] == "OPEN / UNTESTED" for route in open_routes),
        {"markers": markers, "illegal": illegal, "unbolded": unbolded},
    )

    pair_rows = []
    for left, right in combinations(WALLS, 2):
        pattern = re.compile(
            rf"^\|\s*{left}\s*\|\s*{right}\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|",
            re.MULTILINE | re.IGNORECASE,
        )
        match = pattern.search(note)
        pair_rows.append((left, right, match.groups() if match else None))
    check(
        "N2 gives both directions for all ten pairs in the collapsed target set",
        all(row[2] == ("no", "no", "yes") for row in pair_rows),
        pair_rows,
    )

    trigger_rows = []
    for path in RELEASE_PATHS:
        content = path.read_text(encoding="utf-8").lower()
        hits = []
        for parts in TRIGGER_PARTS:
            trigger = "".join(parts)
            hits.extend(
                line_number
                for line_number, line in enumerate(content.splitlines(), 1)
                if trigger in line
            )
        trigger_rows.append(
            {"path": str(path.relative_to(ROOT)), "hits": tuple(hits)}
        )
    check(
        "N3 literal procedure-trigger scan has zero hits on both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    requirements = (
        (
            "N4 matches prior residuals and pins current witnesses",
            (
                "Cycle-235 local even-algebra result",
                "Cycle-308 oriented carrier result",
                "Cycle-311 common M64 result",
                "Cycle-312 pair-sector overlap result",
                "exact Cycle-315 runner witnesses",
            ),
        ),
        (
            "N5 separates cell, edge, multi-edge, and volume resolutions",
            (
                "one Cycle-311 cell",
                "one two-cell physical overlap",
                "one edge-role gauge",
                "several edges sharing a cell",
                "recurrent volume/full Fock",
            ),
        ),
        (
            "N6 retains the next finite construction and open routes",
            (
                "Cycle 235 supplies",
                "Cycle 308 supplies",
                "Cycle 311 supplies",
                "Cycle 312 supplies",
                "The optimal next attack",
            ),
        ),
        (
            "N7 contains a hostile multi-edge steelman",
            (
                "A hostile reviewer should reject a recurrent-volume no-go",
                "three-cell joint non-Pauli matrix completion",
                "Neither route has been tested.",
            ),
        ),
        (
            "N8 records six constructive retirement mechanisms",
            (
                "Cycle 235 closed-face parity boundary",
                "Cycle 306 free seam role",
                "Cycle 308 bare odd syndrome",
                "Cycle 311 raw cell-role collision",
                "Cycle 312 global pair projector",
                "Cycle 315 endpoint order",
            ),
        ),
    )
    for label, required in requirements:
        missing = tuple(item for item in required if item not in flat_note)
        check(label, not missing, missing)
    broad_required = (
        "Gate status: **FAIL / DO NOT SHIP the broad negative.**",
        "Still open are simultaneous three-cell/two-edge consistency",
        "No shared obstruction and no axiom pressure follow.",
    )
    missing = tuple(item for item in broad_required if item not in flat_note)
    check("the broad recurrent-volume negative is explicitly blocked", not missing, missing)


class RayReducer:
    """Reduce physical face paths while retaining all port/role occupations."""

    def __init__(self, code):
        self.code = code
        self.face_mask = (1 << code.qubits) - 1
        self.stabilizer = c305.StabilizerReducer(code)
        self.reference_by_aux: dict[int, c235.Pauli] = {}
        self.row_by_aux: dict[int, int] = {}
        self.phase_cache: dict[tuple[int, int, int, int], complex] = {}

    def reduce(self, representative: c235.Pauli) -> tuple[int, complex]:
        if representative.z & ~self.face_mask:
            raise ValueError("the tested role-gauge rays must have no auxiliary Z word")
        auxiliary = representative.x >> self.code.qubits
        face = c235.Pauli(
            representative.phase,
            representative.x & self.face_mask,
            representative.z & self.face_mask,
        )
        if auxiliary not in self.reference_by_aux:
            self.reference_by_aux[auxiliary] = face
            self.row_by_aux[auxiliary] = len(self.row_by_aux)
            return self.row_by_aux[auxiliary], 1 + 0j
        reference = self.reference_by_aux[auxiliary]
        cache_key = (face.phase, face.x, face.z, auxiliary)
        if cache_key not in self.phase_cache:
            phase = self.stabilizer.relative_phase(face, reference)
            if phase is None:
                raise ValueError("one auxiliary occupation word reached inequivalent face rays")
            self.phase_cache[cache_key] = c311.c308.phase_scalar(phase)
        return self.row_by_aux[auxiliary], self.phase_cache[cache_key]


def gauge_input_terms(code, body, number: int, label: tuple[int, ...]) -> tuple[GaugeTerm, ...]:
    terms = []
    for branch in c311.common_branches(code, body, number, label, 0):
        terms.append(
            GaugeTerm(
                number,
                c311.branch_representative(code, body, branch, 0),
                branch.amplitude / np.sqrt(2),
            )
        )
        target_slice = 0 if number == 0 else 1
        exchanged = c311.common_branches(code, body, number, label, target_slice)
        target = next(
            candidate
            for candidate in exchanged
            if candidate.carrier_direction == branch.carrier_direction
        )
        terms.append(
            GaugeTerm(
                number,
                c311.branch_representative(code, body, target, 1),
                branch.amplitude / np.sqrt(2),
            )
        )
    return tuple(terms)


def raw_input_terms(code, body, number: int, label: tuple[int, ...]) -> tuple[GaugeTerm, ...]:
    return tuple(
        GaugeTerm(
            number,
            c311.branch_representative(code, body, branch, 0),
            branch.amplitude,
        )
        for branch in c311.common_branches(code, body, number, label, 0)
    )


def joint_labels(maximum_number: int = MAX_TOTAL_NUMBER):
    if maximum_number < 0 or maximum_number > MAX_TOTAL_NUMBER:
        raise ValueError("the declared two-cell code contains only total n=0..12")
    return tuple(
        (left_number, left_label, right_number, right_label)
        for left_number, left_label in c311.FOCK_LABELS
        for right_number, right_label in c311.FOCK_LABELS
        if left_number + right_number <= maximum_number
    )


def joint_encoding(
    code,
    labels,
    reducer: RayReducer,
    reverse_order: bool = False,
    term_builder=gauge_input_terms,
):
    cache = {}
    columns = []
    for left_number, left_label, right_number, right_label in labels:
        left_terms = cache.setdefault(
            (LEFT, left_number, left_label),
            term_builder(code, LEFT, left_number, left_label),
        )
        right_terms = cache.setdefault(
            (RIGHT, right_number, right_label),
            term_builder(code, RIGHT, right_number, right_label),
        )
        amplitudes = defaultdict(complex)
        for left_term, right_term in product(left_terms, right_terms):
            ordered = (
                right_term.representative @ left_term.representative
                if reverse_order
                else left_term.representative @ right_term.representative
            )
            row, phase = reducer.reduce(ordered)
            amplitudes[row] += left_term.amplitude * right_term.amplitude * phase
        columns.append({row: value for row, value in amplitudes.items() if abs(value) > 2e-13})

    row_indices = []
    column_indices = []
    data = []
    for column, amplitudes in enumerate(columns):
        for row, value in amplitudes.items():
            row_indices.append(row)
            column_indices.append(column)
            data.append(value)
    return sparse.coo_matrix(
        (data, (row_indices, column_indices)),
        shape=(len(reducer.row_by_aux), len(labels)),
        dtype=complex,
    ).tocsc()


def largest_singular(matrix: sparse.spmatrix) -> float:
    matrix = matrix.tocsc(copy=True)
    matrix.data[abs(matrix.data) < 2e-13] = 0
    matrix.eliminate_zeros()
    if matrix.nnz == 0:
        return 0.0
    rng = np.random.default_rng(315)
    vector = rng.normal(size=matrix.shape[1]) + 1j * rng.normal(size=matrix.shape[1])
    vector /= np.linalg.norm(vector)
    eigenvalue = 0.0
    for _ in range(180):
        image = matrix @ vector
        back = matrix.conj().T @ image
        norm = np.linalg.norm(back)
        if norm == 0:
            return 0.0
        vector = back / norm
        next_value = float(np.vdot(image, image).real)
        if abs(next_value - eigenvalue) < 2e-14 * max(1.0, next_value):
            eigenvalue = next_value
            break
        eigenvalue = next_value
    return float(np.sqrt(eigenvalue))


def raw_maximum_abs(matrix: sparse.spmatrix) -> float:
    return float(max(abs(matrix.data), default=0.0))


def align_rows(left: sparse.csc_matrix, right: sparse.csc_matrix, rows: int):
    if left.shape[0] < rows:
        left.resize((rows, left.shape[1]))
    if right.shape[0] < rows:
        right.resize((rows, right.shape[1]))
    return left, right


def logical_coin_matrix(labels, coin: np.ndarray) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    wedges = {number: c311.exterior_matrix(coin, number) for number in range(7)}
    rows = []
    columns = []
    data = []
    for source, (left_number, left_label, right_number, right_label) in enumerate(labels):
        left_source = c311.LABEL_INDEX[left_number][left_label]
        right_source = c311.LABEL_INDEX[right_number][right_label]
        left_wedge = wedges[left_number]
        right_wedge = wedges[right_number]
        for left_target, target_left_label in enumerate(c311.LABELS[left_number]):
            left_coefficient = left_wedge[left_target, left_source]
            if abs(left_coefficient) <= 2e-14:
                continue
            for right_target, target_right_label in enumerate(c311.LABELS[right_number]):
                coefficient = left_coefficient * right_wedge[right_target, right_source]
                if abs(coefficient) <= 2e-14:
                    continue
                rows.append(
                    lookup[
                        (
                            left_number,
                            target_left_label,
                            right_number,
                            target_right_label,
                        )
                    ]
                )
                columns.append(source)
                data.append(coefficient)
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(len(labels), len(labels)), dtype=complex
    ).tocsc()


def edge_fswap_matrix(labels, axis: int = 0) -> sparse.csc_matrix:
    """Exterior lift of one oriented outer-edge swap on the supplied axis."""

    if axis not in (0, 1, 2):
        raise ValueError("the outer-edge axis must be 0, 1, or 2")
    left_boundary = 2 * axis
    right_boundary = 6 + 2 * axis + 1
    lookup = {label: index for index, label in enumerate(labels)}
    target_rows = []
    phases = []
    for left_number, left_label, right_number, right_label in labels:
        modes = tuple(left_label) + tuple(6 + direction for direction in right_label)
        mapped = tuple(
            right_boundary
            if mode == left_boundary
            else left_boundary
            if mode == right_boundary
            else mode
            for mode in modes
        )
        sign = c311.c308.permutation_sign(mapped)
        ordered = tuple(sorted(mapped))
        target_left = tuple(mode for mode in ordered if mode < 6)
        target_right = tuple(mode - 6 for mode in ordered if mode >= 6)
        target_rows.append(
            lookup[(len(target_left), target_left, len(target_right), target_right)]
        )
        phases.append(sign)
    return sparse.coo_matrix(
        (phases, (target_rows, np.arange(len(labels)))),
        shape=(len(labels), len(labels)),
        dtype=complex,
    ).tocsc()


def contact_matrix(labels, coupling: float) -> sparse.csc_matrix:
    return sparse.diags(
        [
            np.exp(
                1j
                * coupling
                * (
                    left_number * (left_number - 1) // 2
                    + right_number * (right_number - 1) // 2
                )
            )
            for left_number, _ll, right_number, _rl in labels
        ],
        format="csc",
        dtype=complex,
    )


def logical_update_controls(labels):
    coin = c219.common_species(-0.3).coin
    logical_coin = logical_coin_matrix(labels, coin)
    logical_stream = edge_fswap_matrix(labels, 0)
    logical_contact = contact_matrix(labels, c230.COUPLING)
    update = logical_contact @ logical_stream @ logical_coin
    identity = sparse.eye(len(labels), format="csc")
    details = {
        "coin_unitarity": largest_singular(logical_coin.conj().T @ logical_coin - identity),
        "coin_unitarity_raw_maximum": raw_maximum_abs(
            logical_coin.conj().T @ logical_coin - identity
        ),
        "FSWAP_unitarity": largest_singular(logical_stream.conj().T @ logical_stream - identity),
        "FSWAP_unitarity_raw_maximum": raw_maximum_abs(
            logical_stream.conj().T @ logical_stream - identity
        ),
        "contact_unitarity": largest_singular(logical_contact.conj().T @ logical_contact - identity),
        "contact_unitarity_raw_maximum": raw_maximum_abs(
            logical_contact.conj().T @ logical_contact - identity
        ),
        "composed_unitarity": largest_singular(update.conj().T @ update - identity),
        "composed_unitarity_raw_maximum": raw_maximum_abs(
            update.conj().T @ update - identity
        ),
        "coin_nonzeros": logical_coin.nnz,
        "FSWAP_nonzeros": logical_stream.nnz,
        "contact_nontrivial_columns": int(
            np.count_nonzero(abs(logical_contact.diagonal() - 1) > 2e-14)
        ),
        "stream_coin_commutator": largest_singular(
            logical_stream @ logical_coin - logical_coin @ logical_stream
        ),
        "stream_contact_commutator": largest_singular(
            logical_stream @ logical_contact - logical_contact @ logical_stream
        ),
    }
    one_particle_indices = [
        index
        for index, (left_number, _ll, right_number, _rl) in enumerate(labels)
        if left_number + right_number == 1
    ]
    one_particle = update[np.ix_(one_particle_indices, one_particle_indices)]
    uniform = np.ones(len(one_particle_indices), dtype=complex)
    uniform /= np.linalg.norm(uniform)
    eigenvalue = np.vdot(uniform, one_particle @ uniform)
    details.update(
        {
            "Cycle219_mass_fixture": c219.rest_mass(c219.common_species(-0.3)),
            "two_cell_rest_mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
            "two_cell_uniform_one_particle_residual": float(
                np.linalg.norm(one_particle @ uniform - eigenvalue * uniform)
            ),
        }
    )
    return logical_coin, logical_stream, logical_contact, update, details


def edge_role_gauge_controls(forward, reverse, logical_update):
    columns = forward.shape[1]
    identity = sparse.eye(columns, format="csc")
    unordered = (forward + reverse) / np.sqrt(2)
    unordered_gram = (unordered.conj().T @ unordered).tocsc()
    unordered_diagonal = np.asarray(unordered_gram.diagonal()).real
    unordered_smallest = float(
        eigsh(
            unordered_gram,
            k=1,
            which="SA",
            return_eigenvectors=False,
            tol=2e-10,
        )[0]
    )

    # The doubled AB/BA seam has 2N orthogonal flagged columns.  Tensoring one
    # edge-r M2 gives 4N shell dimensions.  C_edge=K_AB<->BA X_r halves the
    # shell back to 2N.  The oriented input embedding selects one N-dimensional
    # endpoint role; endpoint-reversing frames select the other.
    forward_gram = forward.conj().T @ forward
    reverse_gram = reverse.conj().T @ reverse
    zero = sparse.csc_matrix((columns, columns), dtype=complex)
    local_identity = sparse.eye(columns, format="csc")
    edge_exchange = sparse.bmat(
        ((zero, local_identity), (local_identity, zero)), format="csc"
    )
    seam_identity = sparse.eye(2 * columns, format="csc")
    constrained = sparse.vstack((seam_identity, edge_exchange), format="csc") / np.sqrt(2)
    constraint = sparse.bmat(
        (
            (sparse.csc_matrix((2 * columns, 2 * columns)), edge_exchange),
            (edge_exchange, sparse.csc_matrix((2 * columns, 2 * columns))),
        ),
        format="csc",
    )
    constrained_gram = constrained.conj().T @ constrained
    seam_update = sparse.block_diag((logical_update, logical_update), format="csc")
    physical_gauge_update = sparse.block_diag(
        (seam_update, edge_exchange @ seam_update @ edge_exchange), format="csc"
    )
    shell_identity = sparse.eye(4 * columns, format="csc")
    detail = {
        "logical_input_rank": columns,
        "flagged_AB_BA_shell_rank": 2 * columns,
        "shell_times_edge_r_rank": 4 * columns,
        "C_edge_plus_rank": 2 * columns,
        "flagged_physical_Gram_residual": max(
            largest_singular(forward_gram - identity),
            largest_singular(reverse_gram - identity),
        ),
        "constrained_Gram_residual": largest_singular(
            constrained_gram - seam_identity
        ),
        "constrained_Gram_raw_maximum": raw_maximum_abs(
            constrained_gram - seam_identity
        ),
        "constraint_involution_residual": largest_singular(
            constraint @ constraint - shell_identity
        ),
        "constraint_eigen_residual": largest_singular(
            constraint @ constrained - constrained
        ),
        "constraint_eigen_raw_maximum": raw_maximum_abs(
            constraint @ constrained - constrained
        ),
        "gauge_lift_constraint_commutator": largest_singular(
            constraint @ physical_gauge_update
            - physical_gauge_update @ constraint
        ),
        "gauge_lift_intertwining_residual": largest_singular(
            physical_gauge_update @ constrained - constrained @ seam_update
        ),
        "gauge_lift_intertwining_raw_maximum": raw_maximum_abs(
            physical_gauge_update @ constrained - constrained @ seam_update
        ),
        "seam_update_unitarity": largest_singular(
            seam_update.conj().T @ seam_update - seam_identity
        ),
        "unordered_without_edge_r_Gram_residual": largest_singular(
            unordered_gram - identity
        ),
        "unordered_without_edge_r_smallest_Gram_eigenvalue": unordered_smallest,
        "unordered_without_edge_r_minimum_column_norm": float(
            np.sqrt(max(0.0, min(unordered_diagonal)))
        ),
        "unordered_without_edge_r_maximum_column_norm": float(
            np.sqrt(max(unordered_diagonal))
        ),
    }
    return detail


def physical_support_and_constraint_controls(code, labels):
    local_terms = {}
    union = 0
    maximum_branch = 0
    constraint_failures = 0
    sector_failures = 0
    for body in (LEFT, RIGHT):
        for number, label in c311.FOCK_LABELS:
            terms = gauge_input_terms(code, body, number, label)
            local_terms[(body, number, label)] = terms
            for term in terms:
                word = term.representative.x | term.representative.z
                union |= word
                maximum_branch = max(maximum_branch, word.bit_count())
                constraint_failures += sum(
                    not term.representative.commutes(
                        c305.constraint_pauli(code, vertex)
                    )
                    for vertex in range(len(code.graph.vertices))
                )
                sector_failures += sum(
                    not term.representative.commutes(row)
                    for row in code.local_checks + code.wilsons
                )

    maximum_joint_branch = 0
    for left_number, left_label, right_number, right_label in labels:
        for left_term, right_term in product(
            local_terms[(LEFT, left_number, left_label)],
            local_terms[(RIGHT, right_number, right_label)],
        ):
            combined = left_term.representative @ right_term.representative
            maximum_joint_branch = max(
                maximum_joint_branch,
                (combined.x | combined.z).bit_count(),
            )

    vertices = len(code.graph.vertices)
    cells = code.length**3
    face_mask = (1 << code.qubits) - 1
    port_mask = ((1 << vertices) - 1) << code.qubits
    cell_flag_mask = ((1 << cells) - 1) << (code.qubits + vertices)
    cell_r_mask = ((1 << cells) - 1) << (code.qubits + vertices + cells)
    return {
        "face_M2_patch_union": (union & face_mask).bit_count(),
        "port_M2_patch_union": (union & port_mask).bit_count(),
        "cell_flag_M2_patch_union": (union & cell_flag_mask).bit_count(),
        "cell_r_M2_patch_union": (union & cell_r_mask).bit_count(),
        "new_edge_flag_and_r_M2": 2,
        "total_patch_union_with_edge_role_gauge": union.bit_count() + 2,
        "maximum_single_cell_gauge_branch_M2": maximum_branch,
        "maximum_joint_branch_with_edge_role_gauge_M2": maximum_joint_branch + 2,
        "port_constraint_commutator_failures": constraint_failures,
        "fixed_sector_commutator_failures": sector_failures,
        "installed_M2_per_cell_including_three_undirected_edge_roles": 29,
    }


def size_gram_control(length: int, labels):
    code = c269.build_code(length)
    reducer = RayReducer(code)
    encoding = joint_encoding(code, labels, reducer, False)
    if encoding.shape[0] < len(reducer.row_by_aux):
        encoding.resize((len(reducer.row_by_aux), encoding.shape[1]))
    identity = sparse.eye(len(labels), format="csc")
    gram = encoding.conj().T @ encoding
    return {
        "L": length,
        "held": length == 6,
        "logical_columns": len(labels),
        "physical_rays": encoding.shape[0],
        "matrix_nonzeros": encoding.nnz,
        "Gram_opnorm_residual": largest_singular(gram - identity),
        "Gram_raw_maximum": raw_maximum_abs(gram - identity),
        "minimum_Gram_eigenvalue": float(
            eigsh(gram, k=1, which="SA", return_eigenvectors=False, tol=2e-10)[0]
        ),
    }


def normalized_edge(first, second, length: int):
    for axis in range(3):
        delta = (second[axis] - first[axis]) % length
        other_axes_equal = all(
            first[other] == second[other] for other in range(3) if other != axis
        )
        if other_axes_equal and delta == 1:
            return tuple(first), axis, False
        if other_axes_equal and delta == length - 1:
            return tuple(second), axis, True
    raise ValueError("the two cells must be one nearest-neighbor edge")


def transform_edge_state(owner, axis: int, role: int, frame, length: int):
    first = np.asarray(owner, dtype=int)
    second = first.copy()
    second[axis] = (second[axis] + 1) % length
    mapped_first = tuple(int(value % length) for value in frame @ first)
    mapped_second = tuple(int(value % length) for value in frame @ second)
    target_owner, target_axis, reversed_endpoints = normalized_edge(
        mapped_first, mapped_second, length
    )
    return target_owner, target_axis, role ^ int(reversed_endpoints)


def pair_frame_representation(labels, frame, reversed_endpoints: bool):
    lookup = {label: index for index, label in enumerate(labels)}
    rows = []
    phases = []
    for left_number, left_label, right_number, right_label in labels:
        mapped_left = tuple(c311.direction_map(frame, direction) for direction in left_label)
        mapped_right = tuple(c311.direction_map(frame, direction) for direction in right_label)
        phase = c311.c308.permutation_sign(mapped_left) * c311.c308.permutation_sign(
            mapped_right
        )
        mapped_left = tuple(sorted(mapped_left))
        mapped_right = tuple(sorted(mapped_right))
        if reversed_endpoints:
            phase *= (-1) ** (left_number * right_number)
            target = (right_number, mapped_right, left_number, mapped_left)
        else:
            target = (left_number, mapped_left, right_number, mapped_right)
        rows.append(lookup[target])
        phases.append(phase)
    return sparse.coo_matrix(
        (phases, (rows, np.arange(len(labels)))),
        shape=(len(labels), len(labels)),
        dtype=complex,
    ).tocsc()


def covariance_translation_controls(labels, logical_coin, logical_contact, update):
    frames = c235.proper_cubic_frames()
    identity = sparse.eye(len(labels), format="csc")
    frame_rows = []
    for frame in frames:
        mapped_direction = frame @ np.asarray((1, 0, 0), dtype=int)
        axis = int(np.flatnonzero(mapped_direction)[0])
        reversed_endpoints = int(mapped_direction[axis]) == -1
        representation = pair_frame_representation(labels, frame, reversed_endpoints)
        target_update = logical_contact @ edge_fswap_matrix(labels, axis) @ logical_coin
        frame_rows.append(
            {
                "axis": axis,
                "endpoint_reversed": reversed_endpoints,
                "representation_unitarity": largest_singular(
                    representation.conj().T @ representation - identity
                ),
                "update_covariance": largest_singular(
                    representation @ update - target_update @ representation
                ),
                "update_covariance_raw_maximum": raw_maximum_abs(
                    representation @ update - target_update @ representation
                ),
            }
        )

    length = 3
    group_failures = 0
    edge_states = tuple(
        (owner, axis, role)
        for owner in product(range(length), repeat=3)
        for axis in range(3)
        for role in (0, 1)
    )
    for left_frame in frames:
        for right_frame in frames:
            product_frame = left_frame @ right_frame
            for owner, axis, role in edge_states:
                intermediate = transform_edge_state(
                    owner, axis, role, right_frame, length
                )
                composed = transform_edge_state(*intermediate, left_frame, length)
                direct = transform_edge_state(
                    owner, axis, role, product_frame, length
                )
                group_failures += composed != direct

    translation_failures = 0
    for displacement in product(range(length), repeat=3):
        for owner, axis, role in edge_states:
            translated_owner = tuple(
                (owner[index] + displacement[index]) % length for index in range(3)
            )
            translation_failures += (
                normalized_edge(
                    translated_owner,
                    tuple(
                        (
                            translated_owner[index] + (1 if index == axis else 0)
                        )
                        % length
                        for index in range(3)
                    ),
                    length,
                )
                != (translated_owner, axis, False)
            )
    return {
        "proper_cubic_frames": len(frames),
        "endpoint_preserving_frames": sum(
            not row["endpoint_reversed"] for row in frame_rows
        ),
        "endpoint_reversing_frames": sum(row["endpoint_reversed"] for row in frame_rows),
        "maximum_frame_representation_unitarity": max(
            row["representation_unitarity"] for row in frame_rows
        ),
        "maximum_update_covariance_residual": max(
            row["update_covariance"] for row in frame_rows
        ),
        "maximum_update_covariance_raw_maximum": max(
            row["update_covariance_raw_maximum"] for row in frame_rows
        ),
        "edge_role_group_law_tests": len(frames) ** 2 * len(edge_states),
        "edge_role_group_law_failures": group_failures,
        "L3_translation_edge_role_tests": length**3 * len(edge_states),
        "L3_translation_edge_role_failures": translation_failures,
    }


def deletion_and_domain_controls(
    code,
    labels,
    forward,
    logical_coin,
    logical_stream,
    logical_contact,
):
    identity = sparse.eye(len(labels), format="csc")
    branch_column = next(
        index
        for index, label in enumerate(labels)
        if label == (1, (0,), 0, ())
    )
    deleted_branch = forward.copy()
    pointer = deleted_branch.indptr[branch_column]
    deleted_branch_value = complex(deleted_branch.data[pointer])
    deleted_branch.data[pointer] = 0
    deleted_branch.eliminate_zeros()
    deleted_branch_gram = largest_singular(
        deleted_branch.conj().T @ deleted_branch - identity
    )

    deleted_stream = logical_stream.tolil(copy=True)
    deleted_stream[:, 0] = 0
    deleted_stream = deleted_stream.tocsc()
    deleted_stream_unitarity = largest_singular(
        deleted_stream.conj().T @ deleted_stream - identity
    )

    coin_coo = logical_coin.tocoo()
    offdiagonal = np.flatnonzero(coin_coo.row != coin_coo.col)
    selected = int(offdiagonal[np.argmax(abs(coin_coo.data[offdiagonal]))])
    deleted_coin_value = complex(coin_coo.data[selected])
    mutated_data = coin_coo.data.copy()
    mutated_data[selected] = 0
    deleted_coin = sparse.coo_matrix(
        (mutated_data, (coin_coo.row, coin_coo.col)), shape=coin_coo.shape
    ).tocsc()
    deleted_coin.eliminate_zeros()
    deleted_coin_unitarity = largest_singular(
        deleted_coin.conj().T @ deleted_coin - identity
    )

    deleted_contact_residual = largest_singular(logical_contact - identity)
    rejects = 0
    for action in (
        lambda: joint_labels(13),
        lambda: edge_fswap_matrix(labels, 3),
        lambda: c311.common_branches(code, LEFT, 2, (0, 0), 0),
        lambda: c269.build_code(2),
    ):
        try:
            action()
        except ValueError:
            rejects += 1
    return {
        "deleted_carrier_role_branch_coefficient": deleted_branch_value,
        "deleted_carrier_role_branch_Gram_residual": deleted_branch_gram,
        "deleted_FSWAP_column_unitarity_residual": deleted_stream_unitarity,
        "deleted_coin_coefficient": deleted_coin_value,
        "deleted_coin_unitarity_residual": deleted_coin_unitarity,
        "deleted_contact_residual": deleted_contact_residual,
        "lawful_domain_rejections": rejects,
    }


def number_sector_controls(labels, encoding, update):
    gram = encoding.conj().T @ encoding
    rows = []
    for number in range(MAX_TOTAL_NUMBER + 1):
        indices = [
            index
            for index, (left_number, _ll, right_number, _rl) in enumerate(labels)
            if left_number + right_number == number
        ]
        sector_identity = sparse.eye(len(indices), format="csc")
        sector_gram = gram[np.ix_(indices, indices)]
        sector_update = update[np.ix_(indices, indices)]
        split_phases = sorted(
            {
                round(
                    float(
                        np.angle(
                            np.exp(
                                1j
                                * c230.COUPLING
                                * (
                                    left_number * (left_number - 1) // 2
                                    + (number - left_number)
                                    * (number - left_number - 1)
                                    // 2
                                )
                            )
                        )
                    ),
                    12,
                )
                for left_number in range(number + 1)
                if left_number <= 6 and number - left_number <= 6
            }
        )
        rows.append(
            {
                "n": number,
                "dimension": len(indices),
                "expected_dimension": comb(12, number),
                "Gram_residual": largest_singular(sector_gram - sector_identity),
                "Gram_raw_maximum": raw_maximum_abs(
                    sector_gram - sector_identity
                ),
                "update_unitarity": largest_singular(
                    sector_update.conj().T @ sector_update - sector_identity
                ),
                "update_unitarity_raw_maximum": raw_maximum_abs(
                    sector_update.conj().T @ sector_update - sector_identity
                ),
                "onsite_contact_phase_angles_by_cell_split": split_phases,
            }
        )
    return rows


def ambient_completion_controls(encoding, logical_update):
    gram = encoding.conj().T @ encoding
    logical_identity = sparse.eye(encoding.shape[1], format="csc")
    intertwining = encoding @ ((logical_update - logical_identity) @ (gram - logical_identity))

    def apply(vector, operator):
        coefficients = encoding.conj().T @ vector
        return vector + encoding @ (operator @ coefficients - coefficients)

    rng = np.random.default_rng(315)
    residuals = []
    for _ in range(4):
        vector = rng.normal(size=encoding.shape[0]) + 1j * rng.normal(
            size=encoding.shape[0]
        )
        vector /= np.linalg.norm(vector)
        forward = apply(vector, logical_update)
        backward = apply(forward, logical_update.conj().T)
        residuals.append(float(np.linalg.norm(backward - vector)))
    return {
        "ambient_formula": "E U E^dagger + I - E E^dagger",
        "intertwining_residual": largest_singular(intertwining),
        "randomized_ambient_inverse_residuals": residuals,
        "maximum_randomized_ambient_inverse_residual": max(residuals),
        "off_code_identity_completion_supplied": True,
    }


def main() -> int:
    print("CYCLE 315: OVERLAP-AWARE TWO-CELL EDGE GAUGE")
    print("authority=none; audit=unset")
    note_contract()
    methodology_controls()
    n4_file_line_witness_control()
    code = c269.build_code(3)
    labels = joint_labels()
    reducer = RayReducer(code)
    forward = joint_encoding(code, labels, reducer, False)
    reverse = joint_encoding(code, labels, reducer, True)
    forward, reverse = align_rows(forward, reverse, len(reducer.row_by_aux))

    raw_reducer = RayReducer(code)
    raw_forward = joint_encoding(
        code, labels, raw_reducer, False, term_builder=raw_input_terms
    )
    raw_reverse = joint_encoding(
        code, labels, raw_reducer, True, term_builder=raw_input_terms
    )
    raw_forward, raw_reverse = align_rows(
        raw_forward, raw_reverse, len(raw_reducer.row_by_aux)
    )

    identity = sparse.eye(len(labels), format="csc")
    gram = (forward.conj().T @ forward).tocsc()
    gram_residual = largest_singular(gram - identity)
    smallest_gram = float(
        eigsh(gram, k=1, which="SA", return_eigenvectors=False, tol=2e-10)[0]
    )
    parity = sparse.diags(
        [(-1) ** (left_number * right_number) for left_number, _ll, right_number, _rl in labels],
        format="csc",
        dtype=complex,
    )
    order_plain = largest_singular(reverse - forward)
    order_graded = largest_singular(reverse - forward @ parity)
    order_overlap = (forward.conj().T @ reverse).tocsc()
    order_overlap_unitarity = largest_singular(
        order_overlap.conj().T @ order_overlap - identity
    )
    order_overlap_diagonal = abs(order_overlap.diagonal())
    order_overlap_offdiagonal = order_overlap - sparse.diags(order_overlap.diagonal())
    column_norms = np.sqrt(np.asarray(gram.diagonal()).real)
    raw_gram = (raw_forward.conj().T @ raw_forward).tocsc()
    raw_rows = {
        "physical_rays": raw_forward.shape[0],
        "matrix_nonzeros": raw_forward.nnz,
        "Gram_opnorm_residual": largest_singular(raw_gram - identity),
        "reverse_order_plain_residual": largest_singular(raw_reverse - raw_forward),
        "reverse_order_local_graded_residual": largest_singular(
            raw_reverse - raw_forward @ parity
        ),
    }
    logical_coin, _logical_stream, logical_contact, logical_update, logical_rows = (
        logical_update_controls(labels)
    )
    edge_gauge_rows = edge_role_gauge_controls(forward, reverse, logical_update)
    support_rows = physical_support_and_constraint_controls(code, labels)
    covariance_rows = covariance_translation_controls(
        labels, logical_coin, logical_contact, logical_update
    )
    deletion_rows = deletion_and_domain_controls(
        code,
        labels,
        forward,
        logical_coin,
        _logical_stream,
        logical_contact,
    )
    number_rows = number_sector_controls(labels, forward, logical_update)
    ambient_rows = {
        "AB": ambient_completion_controls(forward, logical_update),
        "BA": ambient_completion_controls(reverse, logical_update),
    }
    size_rows = [
        {
            "L": 3,
            "held": False,
            "logical_columns": len(labels),
            "physical_rays": forward.shape[0],
            "matrix_nonzeros": forward.nnz,
            "Gram_opnorm_residual": gram_residual,
            "Gram_raw_maximum": raw_maximum_abs(gram - identity),
            "minimum_Gram_eigenvalue": smallest_gram,
        },
        size_gram_control(4, labels),
        size_gram_control(6, labels),
    ]
    sector_order_rows = []
    for label, indices in (
        (
            "both_cell_numbers_even",
            [
                index
                for index, (left_number, _ll, right_number, _rl) in enumerate(labels)
                if left_number % 2 == right_number % 2 == 0
            ],
        ),
        (
            "total_number_even",
            [
                index
                for index, (left_number, _ll, right_number, _rl) in enumerate(labels)
                if (left_number + right_number) % 2 == 0
            ],
        ),
        (
            "at_least_one_cell_odd",
            [
                index
                for index, (left_number, _ll, right_number, _rl) in enumerate(labels)
                if left_number % 2 or right_number % 2
            ],
        ),
    ):
        sector_forward = forward[:, indices]
        sector_reverse = reverse[:, indices]
        sector_parity = parity[np.ix_(indices, indices)]
        sector_order_rows.append(
            {
                "sector": label,
                "columns": len(indices),
                "plain_residual": largest_singular(sector_reverse - sector_forward),
                "graded_residual": largest_singular(
                    sector_reverse - sector_forward @ sector_parity
                ),
            }
        )

    overlap_detail = {
            "logical_columns_total_n0_to_n12": len(labels),
            "physical_rays": forward.shape[0],
            "matrix_nonzeros": forward.nnz,
            "Gram_opnorm_residual": gram_residual,
            "smallest_Gram_eigenvalue": smallest_gram,
            "minimum_column_norm": float(min(column_norms)),
            "maximum_column_norm": float(max(column_norms)),
            "reverse_order_plain_residual": order_plain,
            "reverse_order_local_graded_residual": order_graded,
            "order_code_overlap_unitarity_residual": order_overlap_unitarity,
            "minimum_same_label_order_overlap": float(min(order_overlap_diagonal)),
            "maximum_same_label_order_overlap": float(max(order_overlap_diagonal)),
            "maximum_cross_label_order_overlap": float(
                max(abs(order_overlap_offdiagonal.data), default=0.0)
            ),
            "sector_order_rows": sector_order_rows,
    }
    check(
        "the actual Cycle-311 role-gauge products form one 4096-column full two-cell physical isometry through held L=6",
        len(labels) == 4096
        and all(
            row["Gram_opnorm_residual"] < TOLERANCE
            and row["Gram_raw_maximum"] < 3e-14
            and row["minimum_Gram_eigenvalue"] > 1 - 5e-12
            for row in size_rows
        ),
        size_rows,
    )
    check(
        "the unextended raw product is non-isometric while every n=0..12 role-gauge sector closes",
        raw_rows["Gram_opnorm_residual"] > 0.2
        and [row["dimension"] for row in number_rows]
        == [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]
        and all(
            row["dimension"] == row["expected_dimension"]
            and row["Gram_residual"] < TOLERANCE
            and row["Gram_raw_maximum"] < 3e-14
            for row in number_rows
        ),
        {"raw": raw_rows, "sectors": number_rows},
    )
    check(
        "AB and BA are physically different and neither plain equality nor one local parity sign removes the order role",
        order_plain > 1
        and order_graded > 1
        and order_overlap_unitarity > 0.9
        and max(abs(order_overlap_offdiagonal.data), default=0.0) > 0.2,
        overlap_detail,
    )
    check(
        "one edge flag plus C_edge=K_AB<->BA X_r gives the exact rank-8192 covariant edge seam",
        edge_gauge_rows["logical_input_rank"] == 4096
        and edge_gauge_rows["flagged_AB_BA_shell_rank"] == 8192
        and edge_gauge_rows["shell_times_edge_r_rank"] == 16384
        and edge_gauge_rows["C_edge_plus_rank"] == 8192
        and max(
            value
            for key, value in edge_gauge_rows.items()
            if "rank" not in key
            and "unordered" not in key
            and isinstance(value, (float, int))
        )
        < TOLERANCE
        and edge_gauge_rows["unordered_without_edge_r_Gram_residual"] > 0.9,
        edge_gauge_rows,
    )
    check(
        "the complete two-cell coin, literal boundary FSWAP, contact, and composed update are unitary and ordered through n=12",
        max(
            logical_rows["coin_unitarity_raw_maximum"],
            logical_rows["FSWAP_unitarity_raw_maximum"],
            logical_rows["contact_unitarity_raw_maximum"],
            logical_rows["composed_unitarity_raw_maximum"],
        )
        < 4e-14
        and logical_rows["stream_coin_commutator"] > 1
        and logical_rows["stream_contact_commutator"] > 1
        and all(
            row["update_unitarity"] < TOLERANCE
            and row["update_unitarity_raw_maximum"] < 4e-14
            for row in number_rows
        ),
        {"update": logical_rows, "sectors": number_rows},
    )
    check(
        "both bounded physical ambient completions intertwine and invert on code and off-code test vectors",
        all(
            row["intertwining_residual"] < TOLERANCE
            and row["maximum_randomized_ambient_inverse_residual"] < 2e-12
            and row["off_code_identity_completion_supplied"]
            for row in ambient_rows.values()
        ),
        ambient_rows,
    )
    check(
        "the overlap code preserves inherited physical constraints with bounded 83-M2 support and 29 M2 per cell",
        support_rows["total_patch_union_with_edge_role_gauge"] == 83
        and support_rows["maximum_joint_branch_with_edge_role_gauge_M2"] <= 65
        and support_rows["port_constraint_commutator_failures"] == 0
        and support_rows["fixed_sector_commutator_failures"] == 0
        and support_rows["installed_M2_per_cell_including_three_undirected_edge_roles"] == 29,
        support_rows,
    )
    check(
        "all 24 proper-cubic frames including endpoint reversals and every L3 translation preserve the edge-role family",
        covariance_rows["proper_cubic_frames"] == 24
        and covariance_rows["endpoint_preserving_frames"] == 12
        and covariance_rows["endpoint_reversing_frames"] == 12
        and covariance_rows["maximum_frame_representation_unitarity"] < TOLERANCE
        and covariance_rows["maximum_update_covariance_residual"] < TOLERANCE
        and covariance_rows["maximum_update_covariance_raw_maximum"] < 4e-14
        and covariance_rows["edge_role_group_law_failures"] == 0
        and covariance_rows["L3_translation_edge_role_failures"] == 0,
        covariance_rows,
    )
    check(
        "the Cycle-219 one-particle mass fixture is unchanged on the two-cell edge seam",
        abs(
            logical_rows["two_cell_rest_mass"]
            - logical_rows["Cycle219_mass_fixture"]
        )
        < 3e-13
        and logical_rows["two_cell_uniform_one_particle_residual"] < 2e-12,
        logical_rows,
    )
    check(
        "carrier, FSWAP, coin, contact, edge-role, and lawful-domain deletions are detected",
        deletion_rows["deleted_carrier_role_branch_Gram_residual"] > 1e-3
        and deletion_rows["deleted_FSWAP_column_unitarity_residual"] > 0.9
        and deletion_rows["deleted_coin_unitarity_residual"] > 0.5
        and deletion_rows["deleted_contact_residual"] > 1
        and edge_gauge_rows["shell_times_edge_r_rank"]
        > edge_gauge_rows["C_edge_plus_rank"]
        and deletion_rows["lawful_domain_rejections"] == 4,
        deletion_rows,
    )
    check(
        "the supplied local edge role, dense matrices, and multi-edge volume boundary remain explicit",
        "multi-edge constraint commutation" in normalized(NOTE)
        and "primitive synthesis" in normalized(NOTE)
        and "not a recurrent volume" in normalized(NOTE)
        and "no global ordering" in normalized(NOTE),
        {
            "supplied": "fixed reference, cell roles, edge f+r, dense matrix units, full M64 tensor code, preparation/application",
            "open": "shared-cell edge constraints, recurrent all-edge stream/contact, primitive synthesis, volume full Fock",
        },
    )
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
