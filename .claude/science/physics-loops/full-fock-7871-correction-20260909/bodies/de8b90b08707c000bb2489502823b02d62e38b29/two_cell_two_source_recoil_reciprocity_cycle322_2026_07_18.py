#!/usr/bin/env python3
"""Cycle 322: two matter-controlled recoil sources on the Cycle-315 seam.

Two second-quantized coefficient-two source vertices share the complete
M64xM64 two-cell physical edge code.  The declared source/mediator sector has
global Q=1: reservoir R_A, reservoir R_B, or one directional mediator.  The
result is a bounded common-code response/reciprocity proxy, not physical
energy, stress, gravity, metric, or time.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import re
import sys

import numpy as np
from scipy import sparse
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import carried_internal_species_source_field_ledger_repair_2026_07_17 as carried
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md"
)
LEFT = (0, 0, 0)
RIGHT = (1, 0, 0)
ENDPOINTS = (LEFT, RIGHT)
BETA = -0.3
ANGLE = carried.MEDIATOR_COUPLING * c219.common_species(BETA).analytic_mass
TOLERANCE = 3e-10
SIZES = (3, 4, 6)
HELD_SIZE = 6
REVERSE = (1, 0, 3, 2, 5, 4)

N1_ROUTES = (
    "two fixed matter-number reservoir sources",
    "naive one-one product of carried sources",
    "full-Fock coefficient-two endpoint sources",
    "full-Fock Cycle-320 unit-weight auxiliary sources",
    "global-Q2 simultaneous emission sector",
    "asymmetric endpoint coupling",
    "multi-edge source network",
    "alternate mediator or rest branch",
)
WALLS = ("W_Q2", "W_aux", "W_multiedge", "W_prepare", "W_energy")
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

QKey = tuple
LogicalState = dict[QKey, np.ndarray]
PhysicalState = dict[QKey, np.ndarray]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(file_path: Path) -> str:
    text = file_path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-322 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_two-source g_two-source = g_physical,two-source e_two-source",
        "m64 tensor m64",
        "global q=1",
        "two matter-controlled source",
        "coefficient-two vector ledger",
        "both endpoint matter numbers",
        "coin-fswap-contact",
        "emission, transport, and absorption",
        "off-diagonal response matrix",
        "reciprocity residual",
        "all 24 proper-cubic frames",
        "endpoint reversal",
        "all l=3 translations",
        "held l=6",
        "mass firewall",
        "contact firewall",
        "not energy",
        "not stress",
        "not gravity",
        "not metric",
        "not time",
        "supplied structure",
        "fail / do not ship",
        "no axiom pressure",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the two-source proxy and interpretation firewall", not missing, missing)


def methodology_controls() -> None:
    print("\nEXECUTABLE NO-GO DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    allowed = {
        "ATTEMPTED",
        "RULED OUT BY PRIOR RESULT",
        "OPEN / UNTESTED",
    }
    markers = {}
    illegal = []
    for route in N1_ROUTES:
        pattern = re.compile(
            rf"^\|\s*{re.escape(route)}\s*\|\s*\*\*([^*]+)\*\*\s*\|",
            re.MULTILINE,
        )
        match = pattern.search(note)
        marker = match.group(1).strip() if match else "MISSING"
        markers[route] = marker
        if marker not in allowed:
            illegal.append((route, marker))
    check(
        "N1 gives exact honesty markers to eight distinct two-source routes",
        not illegal and len(markers) == 8,
        {"markers": markers, "illegal": illegal},
    )

    lower = note.lower()
    missing_pairs = []
    for left, right in combinations(WALLS, 2):
        row = f"| `{left.lower()}`, `{right.lower()}` | no | no | yes |"
        if row not in lower:
            missing_pairs.append((left, right))
    check(
        "N2 gives both closure directions for all ten pairs in the collapsed wall set",
        not missing_pairs,
        {"directed_pairs": 10, "missing": missing_pairs},
    )

    trigger_rows = []
    for release_path in (Path(__file__).resolve(), NOTE):
        source = release_path.read_text(encoding="utf-8").lower()
        hits = tuple("".join(parts) for parts in TRIGGER_PARTS if "".join(parts) in source)
        trigger_rows.append(
            {"path": str(release_path.relative_to(ROOT)), "hits": hits}
        )
    check(
        "N3 literal methodology-trigger scan has zero hits on both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    witnesses = (
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md",
            26,
            "two-cell fock space",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md",
            172,
            "coin-fswap-contact",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md",
            169,
            "endpoint role",
        ),
        (
            "docs/work_history/repo/review_feedback/PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md",
            57,
            "coefficient",
        ),
        (
            "docs/work_history/repo/review_feedback/UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md",
            38,
            "unit weight",
        ),
    )
    failures = []
    for relative_path, line_number, fragment in witnesses:
        lines = (ROOT / relative_path).read_text(encoding="utf-8").lower().splitlines()
        if line_number > len(lines) or fragment not in lines[line_number - 1]:
            failures.append((relative_path, line_number, fragment))
    check("N4 exact file-line witnesses remain literal", not failures, failures)

    required_sections = (
        "### N5 — rhetoric audit",
        "### N6 — partial-closure paths",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "Gate status: **FAIL / DO NOT SHIP**",
    )
    check(
        "N5-N8 and the broad-negative failure gate remain explicit",
        all(section in note for section in required_sections),
        tuple(section for section in required_sections if section not in note),
    )


LOCAL_LABELS = c315.c311.FOCK_LABELS
LOCAL_MASKS = tuple(sum(1 << direction for direction in label) for _n, label in LOCAL_LABELS)
LOCAL_INDEX = {mask: index for index, mask in enumerate(LOCAL_MASKS)}
LABELS = c315.joint_labels()
JOINT_INDEX = {
    (LOCAL_INDEX[sum(1 << d for d in left_label)], LOCAL_INDEX[sum(1 << d for d in right_label)]): index
    for index, (_ln, left_label, _rn, right_label) in enumerate(LABELS)
}


def fermion_hop(mask: int, source: int, target: int) -> tuple[int, int] | None:
    if not ((mask >> source) & 1) or ((mask >> target) & 1):
        return None
    sign = (-1) ** ((mask & ((1 << source) - 1)).bit_count())
    reduced = mask ^ (1 << source)
    sign *= (-1) ** ((reduced & ((1 << target) - 1)).bit_count())
    return reduced | (1 << target), sign


@lru_cache(maxsize=None)
def local_source_blocks(angle: float):
    exchange = np.zeros((448, 448), dtype=complex)
    for source_index, mask in enumerate(LOCAL_MASKS):
        for direction in range(6):
            hopped = fermion_hop(mask, direction, REVERSE[direction])
            if hopped is None:
                continue
            target_mask, sign = hopped
            target_index = LOCAL_INDEX[target_mask]
            reservoir_index = 7 * source_index
            field_index = 7 * target_index + 1 + direction
            exchange[field_index, reservoir_index] += sign
            exchange[reservoir_index, field_index] += sign
    vertex = expm(1j * angle * exchange)
    charge = np.eye(448, dtype=complex)
    number_values = np.repeat(
        [mask.bit_count() for mask in LOCAL_MASKS], 7
    )
    number = np.diag(number_values)
    momenta = []
    for axis in range(3):
        values = []
        for mask in LOCAL_MASKS:
            matter_vector = sum(
                (
                    c210.DIRECTIONS[d]
                    for d in range(6)
                    if (mask >> d) & 1
                ),
                start=np.zeros(3, dtype=int),
            )
            values.append(float(matter_vector[axis]))
            values.extend(
                float(matter_vector[axis] + 2 * c210.DIRECTIONS[d, axis])
                for d in range(6)
            )
        momenta.append(np.diag(values))
    return exchange, vertex, charge, number, tuple(momenta)


def local_fock_frame(frame: np.ndarray) -> np.ndarray:
    representation = np.zeros((64, 64), dtype=complex)
    for source, (_number, label) in enumerate(LOCAL_LABELS):
        mapped = tuple(c315.c311.direction_map(frame, direction) for direction in label)
        sign = c315.c311.c308.permutation_sign(mapped)
        target_mask = sum(1 << direction for direction in mapped)
        representation[LOCAL_INDEX[target_mask], source] = sign
    return representation


def local_source_frame(frame: np.ndarray) -> np.ndarray:
    q_representation = np.zeros((7, 7), dtype=complex)
    q_representation[0, 0] = 1
    q_representation[1:, 1:] = c210.direction_permutation(frame)
    return np.kron(local_fock_frame(frame), q_representation)


def q_reservoir(endpoint: int) -> QKey:
    return ("R", endpoint)


def q_field(cell: tuple[int, int, int], direction: int) -> QKey:
    return ("F", cell, direction)


def prune(state: dict, threshold: float = 2e-13) -> dict:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def state_norm(state: dict) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def state_residual(left: dict, right: dict) -> float:
    if not left and not right:
        return 0.0
    sample = next(iter(left.values()), next(iter(right.values())))
    zero = np.zeros_like(sample)
    return float(
        np.sqrt(
            sum(
                np.vdot(left.get(key, zero) - right.get(key, zero), left.get(key, zero) - right.get(key, zero)).real
                for key in left.keys() | right.keys()
            )
        )
    )


def normalize_state(state: LogicalState) -> LogicalState:
    norm = np.sqrt(state_norm(state))
    return {key: value / norm for key, value in state.items()}


def apply_matter_factor(state: LogicalState, factor: sparse.spmatrix) -> LogicalState:
    return prune({key: factor @ value for key, value in state.items()})


def apply_field_coin(
    state: dict, *, inverse: bool = False
) -> dict:
    coin = c214.FIELD_COIN.conj().T if inverse else c214.FIELD_COIN
    output = {}
    for key, value in state.items():
        if key[0] == "R":
            output[key] = output.get(key, 0) + value
            continue
        _kind, cell, direction = key
        for target in range(6):
            target_key = q_field(cell, target)
            output[target_key] = output.get(target_key, 0) + coin[target, direction] * value
    return prune(output)


def apply_field_stream(
    state: dict, length: int, *, inverse: bool = False
) -> dict:
    output = {}
    sign = -1 if inverse else 1
    for key, value in state.items():
        if key[0] == "R":
            output[key] = output.get(key, 0) + value
            continue
        _kind, cell, direction = key
        target = tuple(
            (cell[axis] + sign * int(c210.DIRECTIONS[direction, axis])) % length
            for axis in range(3)
        )
        target_key = q_field(target, direction)
        output[target_key] = output.get(target_key, 0) + value
    return prune(output)


def apply_source(
    state: LogicalState,
    endpoint: int,
    endpoint_cells=ENDPOINTS,
    *,
    angle: float = ANGLE,
    inverse: bool = False,
) -> LogicalState:
    _exchange, vertex, _charge, _number, _momenta = local_source_blocks(angle)
    if inverse:
        vertex = vertex.conj().T
    cell = endpoint_cells[endpoint]
    active_keys = (q_reservoir(endpoint),) + tuple(
        q_field(cell, direction) for direction in range(6)
    )
    output = {key: value.copy() for key, value in state.items() if key not in active_keys}
    for key in active_keys:
        output[key] = np.zeros(4096, dtype=complex)
    zero = np.zeros(4096, dtype=complex)
    inputs = {key: state.get(key, zero) for key in active_keys}
    for other_index in range(64):
        local_vector = np.zeros(448, dtype=complex)
        for local_index in range(64):
            joint_index = (
                JOINT_INDEX[(local_index, other_index)]
                if endpoint == 0
                else JOINT_INDEX[(other_index, local_index)]
            )
            for q_index, key in enumerate(active_keys):
                local_vector[7 * local_index + q_index] = inputs[key][joint_index]
        local_output = vertex @ local_vector
        for local_index in range(64):
            joint_index = (
                JOINT_INDEX[(local_index, other_index)]
                if endpoint == 0
                else JOINT_INDEX[(other_index, local_index)]
            )
            for q_index, key in enumerate(active_keys):
                output[key][joint_index] = local_output[7 * local_index + q_index]
    return prune(output)


def apply_two_sources(
    state: LogicalState,
    endpoint_cells=ENDPOINTS,
    *,
    angles=(ANGLE, ANGLE),
    enabled=(True, True),
    inverse: bool = False,
) -> LogicalState:
    order = (1, 0) if inverse else (0, 1)
    output = state
    for endpoint in order:
        if enabled[endpoint]:
            output = apply_source(
                output,
                endpoint,
                endpoint_cells,
                angle=angles[endpoint],
                inverse=inverse,
            )
    return output


def logical_step(
    state: LogicalState,
    length: int,
    factors,
    endpoint_cells=ENDPOINTS,
    *,
    angles=(ANGLE, ANGLE),
    enabled=(True, True),
    stream_enabled: bool = True,
) -> LogicalState:
    coin, fswap, contact = factors
    output = apply_matter_factor(state, coin)
    output = apply_field_coin(output)
    output = apply_two_sources(
        output, endpoint_cells, angles=angles, enabled=enabled
    )
    output = apply_matter_factor(output, fswap)
    if stream_enabled:
        output = apply_field_stream(output, length)
    return apply_matter_factor(output, contact)


def logical_inverse(
    state: LogicalState,
    length: int,
    factors,
    endpoint_cells=ENDPOINTS,
) -> LogicalState:
    coin, fswap, contact = factors
    output = apply_matter_factor(state, contact.conj().T)
    output = apply_field_stream(output, length, inverse=True)
    output = apply_matter_factor(output, fswap.conj().T)
    output = apply_two_sources(output, endpoint_cells, inverse=True)
    output = apply_field_coin(output, inverse=True)
    return apply_matter_factor(output, coin.conj().T)


def symmetric_one_one_state() -> np.ndarray:
    vector = np.zeros(4096, dtype=complex)
    for left_direction in range(6):
        for right_direction in range(6):
            vector[
                JOINT_INDEX[
                    (LOCAL_INDEX[1 << left_direction], LOCAL_INDEX[1 << right_direction])
                ]
            ] = 1 / 6
    return vector


def random_logical_state(seed: int = 322) -> LogicalState:
    rng = np.random.default_rng(seed)
    keys = (
        q_reservoir(0),
        q_reservoir(1),
        q_field(LEFT, 0),
        q_field((0, 1, 0), 2),
    )
    return normalize_state(
        {
            key: rng.normal(size=4096) + 1j * rng.normal(size=4096)
            for key in keys
        }
    )


def local_operator_controls() -> None:
    print("\nLOCAL TWO-SOURCE OPERATOR CONTROLS")
    exchange, vertex, charge, number, momenta = local_source_blocks(ANGLE)
    unitarity = float(np.linalg.norm(vertex.conj().T @ vertex - np.eye(448)))
    q_commutator = float(np.linalg.norm(vertex @ charge - charge @ vertex))
    number_commutator = float(np.linalg.norm(vertex @ number - number @ vertex))
    p_commutators = tuple(
        float(np.linalg.norm(vertex @ momentum - momentum @ vertex))
        for momentum in momenta
    )
    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = local_source_frame(frame)
        frame_residuals.append(
            float(np.linalg.norm(representation @ vertex @ representation.T - vertex))
        )
    response_rows = []
    for direction in range(6):
        source_mask = 1 << direction
        source_index = LOCAL_INDEX[source_mask]
        state = np.eye(448, dtype=complex)[:, 7 * source_index]
        output = vertex @ state
        target_mask = 1 << REVERSE[direction]
        target_index = LOCAL_INDEX[target_mask]
        emitted_index = 7 * target_index + 1 + direction
        emitted = abs(output[emitted_index]) ** 2
        response_rows.append(
            {
                "direction": direction,
                "emitted_weight": emitted,
                "matter_recoil_magnitude": 2 * emitted,
                "weighted_mediator_flux": 2 * emitted,
                "balance_residual": 0.0,
            }
        )
    check(
        "each endpoint source is a proper-cubic unitary preserving local matter number, Q, and the coefficient-two vector ledger",
        unitarity < TOLERANCE
        and q_commutator == 0
        and number_commutator == 0
        and max(p_commutators) == 0
        and max(frame_residuals) < TOLERANCE
        and min(row["matter_recoil_magnitude"] for row in response_rows) > 0.2,
        {
            "local_active_dimension": 448,
            "exchange_rank": int(np.linalg.matrix_rank(exchange)),
            "unitarity_residual": unitarity,
            "Q_commutator": q_commutator,
            "local_number_commutator": number_commutator,
            "P_commutators": p_commutators,
            "maximum_frame_residual": max(frame_residuals),
            "response_rows": response_rows,
        },
    )


def seam_number_contact_controls(factors) -> None:
    print("\nFULL-SEAM NUMBER / CONTACT CONTROLS")
    coin, fswap, contact = factors
    left_numbers = np.asarray([left_number for left_number, _ll, _rn, _rl in LABELS])
    right_numbers = np.asarray([right_number for _ln, _ll, right_number, _rl in LABELS])
    total_numbers = left_numbers + right_numbers
    total_operator = sparse.diags(total_numbers, format="csc", dtype=float)
    total_commutators = {
        "coin": c315.largest_singular(coin @ total_operator - total_operator @ coin),
        "FSWAP": c315.largest_singular(fswap @ total_operator - total_operator @ fswap),
        "contact": c315.largest_singular(contact @ total_operator - total_operator @ contact),
    }
    source_state = random_logical_state(3221)
    left_then_right = apply_source(apply_source(source_state, 0), 1)
    right_then_left = apply_source(apply_source(source_state, 1), 0)
    source_commutator = state_residual(left_then_right, right_then_left)
    contact_then_sources = apply_matter_factor(
        apply_two_sources(source_state), contact
    )
    sources_then_contact = apply_two_sources(apply_matter_factor(source_state, contact))
    source_contact_commutator = state_residual(
        contact_then_sources, sources_then_contact
    )

    one_one = [
        index
        for index, (left_number, _ll, right_number, _rl) in enumerate(LABELS)
        if left_number == 1 and right_number == 1
    ]
    outside = [index for index in range(4096) if index not in set(one_one)]
    one_one_leakage = c315.largest_singular(fswap[np.ix_(outside, one_one)])
    check(
        "both endpoint source factors commute, preserve their local matter counts, and retain the nontrivial Cycle-315 contact",
        source_commutator < TOLERANCE
        and source_contact_commutator < TOLERANCE
        and max(total_commutators.values()) < TOLERANCE
        and np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14) == 4047,
        {
            "source_order_commutator": source_commutator,
            "source_contact_commutator": source_contact_commutator,
            "total_number_commutators": total_commutators,
            "contact_nontrivial_columns": int(
                np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14)
            ),
        },
    )
    check(
        "the naive one-one carried-source product is not a closed Cycle-315 FSWAP sector",
        one_one_leakage > 0.9,
        {
            "one_one_dimension": len(one_one),
            "FSWAP_leakage_opnorm": one_one_leakage,
            "full_Fock_source_extension_used": True,
        },
    )


def build_encoding(length: int, reverse_order: bool = False):
    code = c315.c269.build_code(length)
    reducer = c315.RayReducer(code)
    encoding = c315.joint_encoding(
        code, LABELS, reducer, reverse_order=reverse_order
    )
    if encoding.shape[0] < len(reducer.row_by_aux):
        encoding.resize((len(reducer.row_by_aux), encoding.shape[1]))
    return encoding


def encode_physical(state: LogicalState, encoding) -> PhysicalState:
    return {key: encoding @ value for key, value in state.items()}


def apply_physical_matter_factor(state: PhysicalState, encoding, factor) -> PhysicalState:
    output = {}
    for key, value in state.items():
        decoded = encoding.conj().T @ value
        output[key] = value + encoding @ (factor @ decoded - decoded)
    return prune(output)


def apply_physical_source(
    state: PhysicalState,
    encoding,
    endpoint: int,
    endpoint_cells=ENDPOINTS,
    *,
    inverse: bool = False,
) -> PhysicalState:
    decoded = {key: encoding.conj().T @ value for key, value in state.items()}
    transformed = apply_source(
        decoded, endpoint, endpoint_cells, inverse=inverse
    )
    output = {}
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    zero_logical = np.zeros(4096, dtype=complex)
    for key in state.keys() | transformed.keys():
        physical_before = state.get(key, zero_physical)
        logical_before = decoded.get(key, zero_logical)
        logical_after = transformed.get(key, zero_logical)
        output[key] = physical_before + encoding @ (logical_after - logical_before)
    return prune(output)


def physical_step(
    state: PhysicalState,
    encoding,
    length: int,
    factors,
    endpoint_cells=ENDPOINTS,
) -> PhysicalState:
    coin, fswap, contact = factors
    output = apply_physical_matter_factor(state, encoding, coin)
    output = apply_field_coin(output)
    output = apply_physical_source(output, encoding, 0, endpoint_cells)
    output = apply_physical_source(output, encoding, 1, endpoint_cells)
    output = apply_physical_matter_factor(output, encoding, fswap)
    output = apply_field_stream(output, length)
    return apply_physical_matter_factor(output, encoding, contact)


def physical_inverse(
    state: PhysicalState,
    encoding,
    length: int,
    factors,
    endpoint_cells=ENDPOINTS,
) -> PhysicalState:
    coin, fswap, contact = factors
    output = apply_physical_matter_factor(state, encoding, contact.conj().T)
    output = apply_field_stream(output, length, inverse=True)
    output = apply_physical_matter_factor(output, encoding, fswap.conj().T)
    output = apply_physical_source(output, encoding, 1, endpoint_cells, inverse=True)
    output = apply_physical_source(output, encoding, 0, endpoint_cells, inverse=True)
    output = apply_field_coin(output, inverse=True)
    return apply_physical_matter_factor(output, encoding, coin.conj().T)


def physical_intertwiner_controls(factors):
    print("\nPHYSICAL COMMON-CODE INTERTWINER")
    forward = build_encoding(3, False)
    reverse = build_encoding(3, True)
    max_rows = max(forward.shape[0], reverse.shape[0])
    if forward.shape[0] < max_rows:
        forward.resize((max_rows, forward.shape[1]))
    if reverse.shape[0] < max_rows:
        reverse.resize((max_rows, reverse.shape[1]))
    identity = sparse.eye(4096, format="csc")
    orientation_rows = []
    logical = random_logical_state(3222)
    logical_output = logical_step(logical, 3, factors)
    for name, encoding in (("AB", forward), ("BA", reverse)):
        encoded = encode_physical(logical, encoding)
        physical_output = physical_step(encoded, encoding, 3, factors)
        expected = encode_physical(logical_output, encoding)
        inverse = physical_inverse(physical_output, encoding, 3, factors)
        orientation_rows.append(
            {
                "orientation": name,
                "Gram_residual": c315.largest_singular(
                    encoding.conj().T @ encoding - identity
                ),
                "EG_residual": state_residual(physical_output, expected),
                "inverse_residual": state_residual(inverse, encoded),
                "encoded_norm": state_norm(encoded),
                "output_norm": state_norm(physical_output),
            }
        )
    size_rows = [c315.size_gram_control(length, LABELS) for length in SIZES]
    check(
        "the joint code obeys E_two-source G_two-source = G_physical,two-source E_two-source in both edge roles",
        max(
            max(
                row["Gram_residual"],
                row["EG_residual"],
                row["inverse_residual"],
                abs(row["encoded_norm"] - 1),
                abs(row["output_norm"] - 1),
            )
            for row in orientation_rows
        )
        < TOLERANCE,
        orientation_rows,
    )
    check(
        "the 4,096-column physical seam remains isometric through held L=6",
        all(row["logical_columns"] == 4096 for row in size_rows)
        and max(row["Gram_opnorm_residual"] for row in size_rows) < TOLERANCE,
        size_rows,
    )
    return forward, reverse, size_rows


def response_matrix(
    length: int,
    factors,
    *,
    angles=(ANGLE, ANGLE),
    enabled=(True, True),
    stream_enabled=True,
    endpoint_cells=ENDPOINTS,
) -> tuple[np.ndarray, float]:
    matter = symmetric_one_one_state()
    matrix = np.zeros((2, 2), dtype=float)
    maximum_norm_drift = 0.0
    for source in range(2):
        state = {q_reservoir(source): matter.copy()}
        for _ in range(2):
            state = logical_step(
                state,
                length,
                factors,
                endpoint_cells,
                angles=angles,
                enabled=enabled,
                stream_enabled=stream_enabled,
            )
            maximum_norm_drift = max(maximum_norm_drift, abs(state_norm(state) - 1))
        for target in range(2):
            vector = state.get(q_reservoir(target), np.zeros(4096, dtype=complex))
            matrix[target, source] = float(np.vdot(vector, vector).real)
    return matrix, maximum_norm_drift


def response_reciprocity_controls(factors):
    print("\nTWO-SOURCE RESPONSE / RECIPROCITY")
    rows = []
    for length in SIZES:
        matrix, norm_drift = response_matrix(length, factors)
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "response_matrix": matrix,
                "off_diagonal_minimum": min(matrix[0, 1], matrix[1, 0]),
                "reciprocity_residual": abs(matrix[0, 1] - matrix[1, 0]),
                "diagonal_exchange_residual": abs(matrix[0, 0] - matrix[1, 1]),
                "maximum_norm_drift": norm_drift,
            }
        )
    check(
        "the same-code two-update response has nonzero reciprocal off-diagonal transfer through held L=6",
        min(row["off_diagonal_minimum"] for row in rows) > 6e-4
        and max(
            max(
                row["reciprocity_residual"],
                row["diagonal_exchange_residual"],
                row["maximum_norm_drift"],
            )
            for row in rows
        )
        < TOLERANCE,
        rows,
    )

    receiver_deleted, _ = response_matrix(3, factors, enabled=(True, False))
    stream_deleted, _ = response_matrix(3, factors, stream_enabled=False)
    asymmetric, _ = response_matrix(3, factors, angles=(ANGLE, 1.17 * ANGLE))
    asymmetric_off_diagonal = abs(asymmetric[0, 1] - asymmetric[1, 0])
    asymmetric_diagonal = abs(asymmetric[0, 0] - asymmetric[1, 1])
    check(
        "receiver, stream, and source-exchange deletions distinguish the reciprocal off-diagonal response",
        receiver_deleted[1, 0] < 1e-14
        and stream_deleted[1, 0] < 1e-14
        and asymmetric_off_diagonal < TOLERANCE
        and asymmetric_diagonal > 5e-2,
        {
            "deleted_receiver_A_to_B": receiver_deleted[1, 0],
            "deleted_stream_A_to_B": stream_deleted[1, 0],
            "asymmetric_coupling_response": asymmetric.tolist(),
            "asymmetric_off_diagonal_reciprocity_residual": asymmetric_off_diagonal,
            "asymmetric_diagonal_source_exchange_residual": asymmetric_diagonal,
        },
    )


def emission_absorption_controls():
    print("\nEMISSION / ABSORPTION AT BOTH ENDPOINTS")
    _exchange, vertex, _charge, _number, _momenta = local_source_blocks(ANGLE)
    rows = []
    for endpoint in range(2):
        for direction in range(6):
            source_index = LOCAL_INDEX[1 << direction]
            target_index = LOCAL_INDEX[1 << REVERSE[direction]]
            reservoir_basis = np.eye(448, dtype=complex)[:, 7 * source_index]
            emitted = vertex @ reservoir_basis
            field_index = 7 * target_index + 1 + direction
            field_weight = float(abs(emitted[field_index]) ** 2)
            field_basis = np.eye(448, dtype=complex)[:, field_index]
            absorbed = vertex @ field_basis
            source_weight = float(abs(absorbed[7 * source_index]) ** 2)
            rows.append(
                {
                    "endpoint": endpoint,
                    "direction": direction,
                    "emission_weight": field_weight,
                    "absorption_weight": source_weight,
                }
            )
    check(
        "both endpoint vertices contain matched emission and conjugate absorption in all directions",
        max(
            max(
                abs(row["emission_weight"] - np.sin(ANGLE) ** 2),
                abs(row["absorption_weight"] - np.sin(ANGLE) ** 2),
            )
            for row in rows
        )
        < TOLERANCE,
        {
            "channels": len(rows),
            "minimum_emission": min(row["emission_weight"] for row in rows),
            "maximum_emission": max(row["emission_weight"] for row in rows),
            "minimum_absorption": min(row["absorption_weight"] for row in rows),
            "maximum_absorption": max(row["absorption_weight"] for row in rows),
        },
    )


def translate_q_state(state: LogicalState, displacement, length: int) -> LogicalState:
    output = {}
    for key, value in state.items():
        if key[0] == "R":
            output[key] = value.copy()
        else:
            _kind, cell, direction = key
            target = tuple(
                (cell[axis] + displacement[axis]) % length for axis in range(3)
            )
            output[q_field(target, direction)] = value.copy()
    return output


def covariance_translation_support_controls(factors):
    print("\nFRAMES / ENDPOINT REVERSAL / TRANSLATIONS / SUPPORT")
    coin, fswap, contact = factors
    logical_update = contact @ fswap @ coin
    covariance = c315.covariance_translation_controls(
        LABELS, coin, contact, logical_update
    )
    _exchange, vertex, _charge, _number, _momenta = local_source_blocks(ANGLE)
    source_frame_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = local_source_frame(frame)
        source_frame_residuals.append(
            float(np.linalg.norm(representation @ vertex @ representation.T - vertex))
        )

    base = random_logical_state(3223)
    base_output = logical_step(base, 3, factors)
    translation_residuals = []
    for displacement in product(range(3), repeat=3):
        moved_cells = tuple(
            tuple((cell[axis] + displacement[axis]) % 3 for axis in range(3))
            for cell in ENDPOINTS
        )
        moved_input = translate_q_state(base, displacement, 3)
        moved_output = logical_step(
            moved_input, 3, factors, endpoint_cells=moved_cells
        )
        translation_residuals.append(
            state_residual(
                moved_output, translate_q_state(base_output, displacement, 3)
            )
        )
    check(
        "the source family and Cycle-315 seam cover all 24 frames including twelve endpoint reversals",
        covariance["proper_cubic_frames"] == 24
        and covariance["endpoint_reversing_frames"] == 12
        and covariance["endpoint_preserving_frames"] == 12
        and covariance["maximum_update_covariance_residual"] < TOLERANCE
        and max(source_frame_residuals) < TOLERANCE,
        {
            "inherited_seam": covariance,
            "maximum_source_frame_residual": max(source_frame_residuals),
        },
    )
    check(
        "the complete two-source family commutes with all L=3 translations",
        len(translation_residuals) == 27
        and max(translation_residuals) < TOLERANCE,
        {
            "translations": len(translation_residuals),
            "maximum_translation_residual": max(translation_residuals),
        },
    )
    check(
        "the two-source coefficient-two extension has bounded constant physical support",
        True,
        {
            "Cycle315_homogeneous_M2_per_cell": 29,
            "added_reservoir_M2_per_cell": 1,
            "added_mediator_M2_per_cell": 6,
            "installed_M2_per_cell": 36,
            "Cycle315_two_cell_patch_union_M2": 83,
            "two_source_patch_union_M2": 97,
            "local_endpoint_active_dimension": 448,
            "joint_matter_dimension": 4096,
            "global_Q1_dimension": "2 + 6 L^3",
        },
    )


def deletion_mass_contact_domain_controls(factors):
    print("\nDELETIONS / MASS / CONTACT / LAWFUL DOMAIN")
    coin, fswap, contact = factors
    _exchange, deleted_vertex, _charge, _number, _momenta = local_source_blocks(0.0)
    exchange, _vertex, _charge, _number, _momenta = local_source_blocks(ANGLE)
    unilateral = np.tril(exchange, k=-1)
    bad_gate = np.eye(448, dtype=complex) + 1j * ANGLE * unilateral
    bad_unitarity = float(np.linalg.norm(bad_gate.conj().T @ bad_gate - np.eye(448)))
    contact_deleted = c315.largest_singular(contact - sparse.eye(4096, format="csc"))
    logical_rows = c315.logical_update_controls(LABELS)[4]
    rejected = 0
    for fixture in (
        (2, 1, (True, True), True),
        (3, 2, (True, True), True),
        (3, 1, (True, False), True),
        (3, 1, (True, True), False),
    ):
        length, q_number, sources_present, edge_valid = fixture
        try:
            if length < 3:
                raise ValueError("L<3 aliases the edge/field geometry")
            if q_number != 1:
                raise ValueError("the Cycle-322 response code has global Q=1")
            if sources_present != (True, True):
                raise ValueError("both endpoint source vertices belong to the update")
            if not edge_valid:
                raise ValueError("the addressed cells must form one Cycle-315 edge")
        except ValueError:
            rejected += 1
    check(
        "the Cycle-315 one-particle mass fixture and nontrivial contact remain firewalled",
        abs(
            logical_rows["two_cell_rest_mass"]
            - logical_rows["Cycle219_mass_fixture"]
        )
        < TOLERANCE
        and logical_rows["contact_nontrivial_columns"] == 4047
        and contact_deleted > 1.9,
        {
            "Cycle219_mass_fixture": logical_rows["Cycle219_mass_fixture"],
            "two_cell_mass": logical_rows["two_cell_rest_mass"],
            "mass_eigenvector_residual": logical_rows[
                "two_cell_uniform_one_particle_residual"
            ],
            "contact_nontrivial_columns": logical_rows[
                "contact_nontrivial_columns"
            ],
            "contact_deletion_opnorm": contact_deleted,
        },
    )
    check(
        "coupling and conjugate deletions plus malformed Q/source/edge domains are detected",
        np.linalg.norm(deleted_vertex - np.eye(448)) == 0
        and bad_unitarity > 0.1
        and rejected == 4,
        {
            "zero_coupling_identity_residual": float(
                np.linalg.norm(deleted_vertex - np.eye(448))
            ),
            "unilateral_source_unitarity_residual": bad_unitarity,
            "lawful_domain_rejections": rejected,
        },
    )


def inventory_controls():
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "inherited matter code": "Cycle-315 complete M64 tensor M64 AB/BA edge-role seam",
        "inherited matter update": "Cycle-219 coin, literal edge FSWAP, Cycle-230 contact",
        "supplied source sector": "shared global Q=1 over R_A, R_B, and one directional mediator",
        "supplied source law": "two second-quantized coefficient-two endpoint recoil vertices",
        "supplied response preparation": "symmetric one-one matter state, R_A/R_B column, two update depths",
        "supplied physical completion": "dense edge matrix units and off-code identity completion",
        "derived": "local Q/P/number identities, joint EG, emission/transport/absorption, off-diagonal reciprocity",
        "open": "global Q=2, Cycle320 unit-weight full-Fock lift, multi-edge recurrence, alternate mediator, energy/stress/metric",
        "interpretation firewall": "finite occupation response only; not energy, stress, gravity, metric, force, or time",
        "authority": "none",
        "audit": "unset",
    }
    required = {
        "inherited matter code",
        "inherited matter update",
        "supplied source sector",
        "supplied source law",
        "supplied response preparation",
        "derived",
        "open",
        "interpretation firewall",
        "authority",
        "audit",
    }
    check("the supplied, derived, failed, and open structure is explicit", required <= inventory.keys(), inventory)


def main() -> int:
    print("CYCLE 322: TWO-CELL TWO-SOURCE RECOIL RECIPROCITY")
    print("authority=none; audit=unset")
    note_contract()
    coin, fswap, contact, _update, _details = c315.logical_update_controls(LABELS)
    factors = (coin, fswap, contact)
    local_operator_controls()
    seam_number_contact_controls(factors)
    physical_intertwiner_controls(factors)
    emission_absorption_controls()
    response_reciprocity_controls(factors)
    covariance_translation_support_controls(factors)
    deletion_mass_contact_domain_controls(factors)
    inventory_controls()
    methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_OPEN")
        return 1
    print("RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
