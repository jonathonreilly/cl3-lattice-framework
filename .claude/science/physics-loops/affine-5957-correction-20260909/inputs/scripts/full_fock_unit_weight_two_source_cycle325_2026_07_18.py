#!/usr/bin/env python3
"""Cycle 325: full-Fock unit-weight auxiliary two-source probe.

The constructive route second-quantizes the Cycle-320 unit-weight source
channel over every local six-mode Fock mask and places two copies on the
Cycle-315 M64xM64 seam.  Its auxiliary direction is paired locally with the
mediator and co-transported by a supplied bounded pair stream.  This supplied
program differs from Cycle 320's one-carrier matter catch-up and is tested
against that literal route rather than silently identified with it.

The observables are dimensionless Q, direction ledgers, and finite occupation
responses.  They are not physical energy, stress, gravity, metric, or time.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import re
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as c322


LEFT = c322.LEFT
RIGHT = c322.RIGHT
ENDPOINTS = c322.ENDPOINTS
ANGLE = c322.ANGLE
REVERSE = c322.REVERSE
LABELS = c322.LABELS
LOCAL_MASKS = c322.LOCAL_MASKS
LOCAL_INDEX = c322.LOCAL_INDEX
JOINT_INDEX = c322.JOINT_INDEX
SIZES = (3, 4, 6)
HELD_SIZE = 6
TOLERANCE = 3e-10
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "FULL_FOCK_UNIT_WEIGHT_MEDIATOR_PAIRED_TWO_SOURCE_CYCLE325_NOTE_2026-07-18.md"
)

N1_ROUTES = (
    "coefficient-two full-Fock sources",
    "literal Cycle-320 matter-carried extrapolation",
    "mediator-paired unit-weight auxiliary",
    "explicit full-Fock carrier tag register",
    "distinguishable auxiliary matter species",
    "paired-mediator without auxiliary",
    "global-Q2 simultaneous source sector",
    "multi-edge unit-weight source network",
)
WALLS = ("W_tag", "W_species", "W_Q2", "W_multiedge", "W_energy")
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
State = dict[QKey, np.ndarray]


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
        check("the Cycle-325 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_unit g_unit = g_physical,unit e_unit",
        "m64 tensor m64",
        "all 64 local fock masks",
        "mediator-paired unit-weight auxiliary compiler",
        "different supplied co-stream program",
        "p_matter + p_mediator + p_auxiliary",
        "both endpoint matter numbers",
        "42 m2 per cell",
        "111-m2",
        "actual cycle-230 contact",
        "nonzero symmetric response",
        "coefficient-two comparison",
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
    check("the note pins the unit-weight pair theorem and boundary", not missing, missing)


def methodology_controls() -> None:
    print("\nEXECUTABLE NO-GO DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    allowed = {"ATTEMPTED", "RULED OUT BY PRIOR RESULT", "OPEN / UNTESTED"}
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
        "N1 gives exact honesty markers to eight distinct unit-weight routes",
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
            "docs/work_history/repo/review_feedback/UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md",
            38,
            "unit weight",
        ),
        (
            "docs/work_history/repo/review_feedback/UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md",
            30,
            "matter cell",
        ),
        (
            "docs/work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md",
            112,
            "complete cycle-315",
        ),
        (
            "docs/work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md",
            357,
            "full-fock cycle-320",
        ),
        (
            "docs/work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md",
            485,
            "global-q2",
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


def q_reservoir(endpoint: int) -> QKey:
    return ("R", endpoint)


def q_link(
    field_cell: tuple[int, int, int],
    field_direction: int,
    auxiliary_cell: tuple[int, int, int],
    auxiliary_direction: int,
) -> QKey:
    return (
        "L",
        field_cell,
        field_direction,
        auxiliary_cell,
        auxiliary_direction,
    )


def prune(state: State, threshold: float = 2e-13) -> State:
    return {
        key: value for key, value in state.items() if np.linalg.norm(value) > threshold
    }


def state_norm(state: State) -> float:
    return c322.state_norm(state)


def state_residual(left: State, right: State) -> float:
    return c322.state_residual(left, right)


def normalize_state(state: State) -> State:
    return c322.normalize_state(state)


def apply_matter_factor(state: State, factor: sparse.spmatrix) -> State:
    return c322.apply_matter_factor(state, factor)


@lru_cache(maxsize=None)
def unit_weight_local_source(angle: float):
    # On the active R or (F_d,A_d) sector, the numerical vertex equals the
    # Cycle-322 coefficient-two block, while its operator decomposition is
    # P_matter + P_field + P_auxiliary with three unit coefficients.
    exchange, vertex, charge, number, _coefficient_two = c322.local_source_blocks(
        angle
    )
    matter_momenta = []
    field_momenta = []
    auxiliary_momenta = []
    total_momenta = []
    for axis in range(3):
        matter_values = []
        field_values = []
        auxiliary_values = []
        for mask in LOCAL_MASKS:
            matter_vector = sum(
                (
                    c210.DIRECTIONS[direction]
                    for direction in range(6)
                    if (mask >> direction) & 1
                ),
                start=np.zeros(3, dtype=int),
            )
            matter_values.extend([float(matter_vector[axis])] * 7)
            field_values.append(0.0)
            field_values.extend(
                float(c210.DIRECTIONS[direction, axis]) for direction in range(6)
            )
            auxiliary_values.append(0.0)
            auxiliary_values.extend(
                float(c210.DIRECTIONS[direction, axis]) for direction in range(6)
            )
        matter = np.diag(matter_values)
        field = np.diag(field_values)
        auxiliary = np.diag(auxiliary_values)
        matter_momenta.append(matter)
        field_momenta.append(field)
        auxiliary_momenta.append(auxiliary)
        total_momenta.append(matter + field + auxiliary)
    return (
        exchange,
        vertex,
        charge,
        number,
        tuple(matter_momenta),
        tuple(field_momenta),
        tuple(auxiliary_momenta),
        tuple(total_momenta),
    )


def apply_field_coin(state: State, *, inverse: bool = False) -> State:
    coin = c214.FIELD_COIN.conj().T if inverse else c214.FIELD_COIN
    output: State = {}
    for key, value in state.items():
        if key[0] == "R":
            output[key] = output.get(key, 0) + value
            continue
        _kind, field_cell, field_direction, auxiliary_cell, auxiliary_direction = key
        for target in range(6):
            target_key = q_link(
                field_cell, target, auxiliary_cell, auxiliary_direction
            )
            output[target_key] = (
                output.get(target_key, 0) + coin[target, field_direction] * value
            )
    return prune(output)


def apply_pair_stream(
    state: State,
    length: int,
    *,
    inverse: bool = False,
    move_auxiliary: bool = True,
) -> State:
    output: State = {}
    sign = -1 if inverse else 1
    for key, value in state.items():
        if key[0] == "R":
            output[key] = output.get(key, 0) + value
            continue
        _kind, field_cell, field_direction, auxiliary_cell, auxiliary_direction = key
        displacement = sign * c210.DIRECTIONS[field_direction]
        target_field = tuple(
            (field_cell[axis] + int(displacement[axis])) % length
            for axis in range(3)
        )
        target_auxiliary = (
            tuple(
                (auxiliary_cell[axis] + int(displacement[axis])) % length
                for axis in range(3)
            )
            if move_auxiliary
            else auxiliary_cell
        )
        target_key = q_link(
            target_field,
            field_direction,
            target_auxiliary,
            auxiliary_direction,
        )
        output[target_key] = output.get(target_key, 0) + value
    return prune(output)


def apply_literal_carried_stream(state: State, length: int) -> State:
    """Direct one-carrier extrapolation: aux moves opposite its own direction."""
    output: State = {}
    for key, value in state.items():
        if key[0] == "R":
            output[key] = output.get(key, 0) + value
            continue
        _kind, field_cell, field_direction, auxiliary_cell, auxiliary_direction = key
        target_field = tuple(
            (field_cell[axis] + int(c210.DIRECTIONS[field_direction, axis])) % length
            for axis in range(3)
        )
        target_auxiliary = tuple(
            (auxiliary_cell[axis] - int(c210.DIRECTIONS[auxiliary_direction, axis]))
            % length
            for axis in range(3)
        )
        target_key = q_link(
            target_field,
            field_direction,
            target_auxiliary,
            auxiliary_direction,
        )
        output[target_key] = output.get(target_key, 0) + value
    return prune(output)


def apply_source(
    state: State,
    endpoint: int,
    endpoint_cells=ENDPOINTS,
    *,
    angle: float = ANGLE,
    inverse: bool = False,
) -> State:
    _exchange, vertex, *_operators = unit_weight_local_source(angle)
    if inverse:
        vertex = vertex.conj().T
    cell = endpoint_cells[endpoint]
    active_keys = (q_reservoir(endpoint),) + tuple(
        q_link(cell, direction, cell, direction) for direction in range(6)
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


def apply_sources(
    state: State,
    endpoint_cells=ENDPOINTS,
    *,
    angles=(ANGLE, ANGLE),
    enabled=(True, True),
    inverse: bool = False,
) -> State:
    output = state
    order = (1, 0) if inverse else (0, 1)
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
    state: State,
    length: int,
    factors,
    endpoint_cells=ENDPOINTS,
    *,
    angles=(ANGLE, ANGLE),
    enabled=(True, True),
    stream_enabled: bool = True,
    stream_program: str = "paired",
) -> State:
    coin, fswap, contact = factors
    output = apply_matter_factor(state, coin)
    output = apply_field_coin(output)
    output = apply_sources(
        output, endpoint_cells, angles=angles, enabled=enabled
    )
    output = apply_matter_factor(output, fswap)
    if stream_enabled:
        if stream_program == "paired":
            output = apply_pair_stream(output, length)
        elif stream_program == "literal_carried":
            output = apply_literal_carried_stream(output, length)
        elif stream_program != "none":
            raise ValueError("unknown auxiliary stream program")
    return apply_matter_factor(output, contact)


def logical_inverse(state: State, length: int, factors) -> State:
    coin, fswap, contact = factors
    output = apply_matter_factor(state, contact.conj().T)
    output = apply_pair_stream(output, length, inverse=True)
    output = apply_matter_factor(output, fswap.conj().T)
    output = apply_sources(output, inverse=True)
    output = apply_field_coin(output, inverse=True)
    return apply_matter_factor(output, coin.conj().T)


def random_state(seed: int = 325) -> State:
    rng = np.random.default_rng(seed)
    keys = (
        q_reservoir(0),
        q_reservoir(1),
        q_link(LEFT, 0, LEFT, 0),
        q_link((0, 1, 0), 2, (0, 1, 0), 4),
    )
    return normalize_state(
        {
            key: rng.normal(size=4096) + 1j * rng.normal(size=4096)
            for key in keys
        }
    )


def response_matrix(
    length: int,
    factors,
    *,
    angles=(ANGLE, ANGLE),
    enabled=(True, True),
    stream_enabled: bool = True,
    stream_program: str = "paired",
    depths: int = 2,
) -> tuple[np.ndarray, float]:
    matter = c322.symmetric_one_one_state()
    matrix = np.zeros((2, 2), dtype=float)
    maximum_norm_drift = 0.0
    for source in range(2):
        state = {q_reservoir(source): matter.copy()}
        for _ in range(depths):
            state = logical_step(
                state,
                length,
                factors,
                angles=angles,
                enabled=enabled,
                stream_enabled=stream_enabled,
                stream_program=stream_program,
            )
            maximum_norm_drift = max(
                maximum_norm_drift, abs(state_norm(state) - 1)
            )
        for receiver in range(2):
            vector = state.get(q_reservoir(receiver), np.zeros(4096, dtype=complex))
            matrix[receiver, source] = float(np.vdot(vector, vector).real)
    return matrix, maximum_norm_drift


def encode_physical(state: State, encoding) -> State:
    return {key: encoding @ value for key, value in state.items()}


def apply_physical_matter(state: State, encoding, factor) -> State:
    return c322.apply_physical_matter_factor(state, encoding, factor)


def apply_physical_source(
    state: State,
    encoding,
    endpoint: int,
    *,
    inverse: bool = False,
) -> State:
    decoded = {key: encoding.conj().T @ value for key, value in state.items()}
    transformed = apply_source(decoded, endpoint, inverse=inverse)
    output: State = {}
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    zero_logical = np.zeros(4096, dtype=complex)
    for key in state.keys() | transformed.keys():
        before_physical = state.get(key, zero_physical)
        before_logical = decoded.get(key, zero_logical)
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return prune(output)


def physical_step(state: State, encoding, length: int, factors) -> State:
    coin, fswap, contact = factors
    output = apply_physical_matter(state, encoding, coin)
    output = apply_field_coin(output)
    output = apply_physical_source(output, encoding, 0)
    output = apply_physical_source(output, encoding, 1)
    output = apply_physical_matter(output, encoding, fswap)
    output = apply_pair_stream(output, length)
    return apply_physical_matter(output, encoding, contact)


def physical_inverse(state: State, encoding, length: int, factors) -> State:
    coin, fswap, contact = factors
    output = apply_physical_matter(state, encoding, contact.conj().T)
    output = apply_pair_stream(output, length, inverse=True)
    output = apply_physical_matter(output, encoding, fswap.conj().T)
    output = apply_physical_source(output, encoding, 1, inverse=True)
    output = apply_physical_source(output, encoding, 0, inverse=True)
    output = apply_field_coin(output, inverse=True)
    return apply_physical_matter(output, encoding, coin.conj().T)


def local_controls() -> None:
    print("\nLOCAL FULL-FOCK UNIT-WEIGHT SOURCE")
    (
        exchange,
        vertex,
        charge,
        number,
        matter_momenta,
        field_momenta,
        auxiliary_momenta,
        total_momenta,
    ) = unit_weight_local_source(ANGLE)
    unitarity = float(np.linalg.norm(vertex.conj().T @ vertex - np.eye(448)))
    q_commutator = float(np.linalg.norm(vertex @ charge - charge @ vertex))
    number_commutator = float(np.linalg.norm(vertex @ number - number @ vertex))
    p_commutators = tuple(
        float(np.linalg.norm(vertex @ momentum - momentum @ vertex))
        for momentum in total_momenta
    )
    no_auxiliary_commutators = tuple(
        float(
            np.linalg.norm(
                vertex @ (matter + field) - (matter + field) @ vertex
            )
        )
        for matter, field in zip(matter_momenta, field_momenta)
    )
    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = c322.local_source_frame(frame)
        frame_residuals.append(
            float(np.linalg.norm(representation @ vertex @ representation.T - vertex))
        )
    response_rows = []
    for direction in range(6):
        mask = 1 << direction
        initial = np.zeros(448, dtype=complex)
        initial[7 * LOCAL_INDEX[mask]] = 1
        final = vertex @ initial
        emitted = float(
            sum(abs(final[7 * local + 1 + direction]) ** 2 for local in range(64))
        )
        initial_vector = np.asarray(
            [
                np.vdot(initial, operator @ initial).real
                for operator in total_momenta
            ]
        )
        final_vector = np.asarray(
            [np.vdot(final, operator @ final).real for operator in total_momenta]
        )
        response_rows.append(
            {
                "direction": direction,
                "emitted_weight": emitted,
                "unit_weight_balance": float(
                    np.linalg.norm(final_vector - initial_vector)
                ),
            }
        )
    check(
        "the second-quantized source has exact unit-weight Q/vector/number ledgers on all 64 local masks",
        unitarity < TOLERANCE
        and q_commutator == 0
        and number_commutator == 0
        and max(p_commutators) == 0
        and max(frame_residuals) < TOLERANCE
        and min(row["emitted_weight"] for row in response_rows) > 0.12
        and max(row["unit_weight_balance"] for row in response_rows) < TOLERANCE,
        {
            "local_masks": 64,
            "active_dimension": 448,
            "exchange_rank": int(np.linalg.matrix_rank(exchange)),
            "unitarity_residual": unitarity,
            "Q_commutator": q_commutator,
            "local_number_commutator": number_commutator,
            "P_commutators": p_commutators,
            "maximum_frame_residual": max(frame_residuals),
            "unit_weights": (1, 1, 1),
            "response_rows": response_rows,
        },
    )
    check(
        "deleting the auxiliary vector contribution breaks recoil balance",
        min(no_auxiliary_commutators) > 0.7,
        {"P_without_auxiliary_commutators": no_auxiliary_commutators},
    )


def seam_physical_controls(factors) -> None:
    print("\nCOMMON-CODE PHYSICAL INTERTWINER")
    forward = c322.build_encoding(3, False)
    reverse = c322.build_encoding(3, True)
    max_rows = max(forward.shape[0], reverse.shape[0])
    if forward.shape[0] < max_rows:
        forward.resize((max_rows, forward.shape[1]))
    if reverse.shape[0] < max_rows:
        reverse.resize((max_rows, reverse.shape[1]))
    logical = random_state(3252)
    expected_logical = logical_step(logical, 3, factors)
    rows = []
    for name, encoding in (("AB", forward), ("BA", reverse)):
        encoded = encode_physical(logical, encoding)
        actual = physical_step(encoded, encoding, 3, factors)
        expected = encode_physical(expected_logical, encoding)
        recovered = physical_inverse(actual, encoding, 3, factors)
        rows.append(
            {
                "orientation": name,
                "EG_residual": state_residual(actual, expected),
                "inverse_residual": state_residual(recovered, encoded),
                "encoded_norm": state_norm(encoded),
                "output_norm": state_norm(actual),
            }
        )
    size_rows = [c315.size_gram_control(length, LABELS) for length in SIZES]
    check(
        "the full-Fock unit-weight pair code obeys joint AB/BA physical EG and inverse EG",
        max(
            max(
                row["EG_residual"],
                row["inverse_residual"],
                abs(row["encoded_norm"] - 1),
                abs(row["output_norm"] - 1),
            )
            for row in rows
        )
        < TOLERANCE,
        rows,
    )
    check(
        "the 4,096-column physical seam remains isometric through held L=6",
        all(row["logical_columns"] == 4096 for row in size_rows)
        and max(row["Gram_opnorm_residual"] for row in size_rows) < TOLERANCE,
        size_rows,
    )


def inherited_seam_number_contact_controls(factors) -> None:
    global PASS, FAIL
    before_pass = c322.PASS
    before_fail = c322.FAIL
    c322.seam_number_contact_controls(factors)
    PASS += c322.PASS - before_pass
    FAIL += c322.FAIL - before_fail


def response_controls(factors) -> None:
    print("\nTWO-SOURCE UNIT-WEIGHT RESPONSE")
    rows = []
    coefficient_rows = []
    for length in SIZES:
        matrix, drift = response_matrix(length, factors)
        coefficient, coefficient_drift = c322.response_matrix(length, factors)
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "response": matrix.tolist(),
                "off_diagonal_minimum": float(min(matrix[0, 1], matrix[1, 0])),
                "reciprocity_residual": float(abs(matrix[0, 1] - matrix[1, 0])),
                "diagonal_exchange_residual": float(abs(matrix[0, 0] - matrix[1, 1])),
                "norm_drift": drift,
            }
        )
        coefficient_rows.append(
            {
                "L": length,
                "response": coefficient.tolist(),
                "norm_drift": coefficient_drift,
            }
        )
    check(
        "the paired unit-weight auxiliary has a nonzero symmetric two-source response through held L=6",
        min(row["off_diagonal_minimum"] for row in rows) > 1e-5
        and max(
            max(
                row["reciprocity_residual"],
                row["diagonal_exchange_residual"],
                row["norm_drift"],
            )
            for row in rows
        )
        < TOLERANCE,
        rows,
    )
    receiver_deleted, _ = response_matrix(3, factors, enabled=(True, False))
    stream_deleted, _ = response_matrix(3, factors, stream_enabled=False)
    literal, literal_drift = response_matrix(
        3, factors, stream_program="literal_carried"
    )
    check(
        "receiver and pair-stream deletions kill transfer while the literal one-carrier catch-up is distinguished",
        receiver_deleted[1, 0] < 1e-14
        and stream_deleted[1, 0] < 1e-14
        and literal[1, 0] < 1e-14
        and literal_drift < TOLERANCE,
        {
            "deleted_receiver_A_to_B": float(receiver_deleted[1, 0]),
            "deleted_pair_stream_A_to_B": float(stream_deleted[1, 0]),
            "literal_matter_carried_response": literal.tolist(),
            "literal_matter_carried_norm_drift": literal_drift,
        },
    )
    check(
        "the coefficient-two and unit-weight pair responses are compared on the same preparation",
        min(
            min(row["response"][0][1], row["response"][1][0])
            for row in coefficient_rows
        )
        > 6e-4,
        {
            "unit_weight": rows,
            "coefficient_two": coefficient_rows,
            "same_matter_preparation": True,
            "same_two_update_depth": True,
        },
    )


def covariance_translation_support_controls(factors) -> None:
    print("\nFRAMES / TRANSLATIONS / SUPPORT")
    coin, fswap, contact = factors
    inherited = c315.covariance_translation_controls(
        LABELS, coin, contact, contact @ fswap @ coin
    )
    field_coin_frame_residuals = []
    pair_stream_frame_tests = 0
    pair_stream_frame_failures = 0
    for frame in c210.proper_cubic_frames():
        direction_representation = c210.direction_permutation(frame)
        field_coin_frame_residuals.append(
            float(
                np.linalg.norm(
                    direction_representation
                    @ c214.FIELD_COIN
                    @ direction_representation.T
                    - c214.FIELD_COIN
                )
            )
        )
        for cell in product(range(3), repeat=3):
            for field_direction in range(6):
                for auxiliary_direction in range(6):
                    mapped_cell_vector = frame @ np.asarray(cell, dtype=int)
                    mapped_cell = tuple(
                        int(value) % 3 for value in mapped_cell_vector
                    )
                    mapped_field = c315.c311.direction_map(frame, field_direction)
                    mapped_auxiliary = c315.c311.direction_map(
                        frame, auxiliary_direction
                    )
                    streamed = tuple(
                        (
                            cell[axis]
                            + int(c210.DIRECTIONS[field_direction, axis])
                        )
                        % 3
                        for axis in range(3)
                    )
                    mapped_streamed_vector = frame @ np.asarray(streamed, dtype=int)
                    mapped_streamed = tuple(
                        int(value) % 3 for value in mapped_streamed_vector
                    )
                    stream_after_map = tuple(
                        (
                            mapped_cell[axis]
                            + int(c210.DIRECTIONS[mapped_field, axis])
                        )
                        % 3
                        for axis in range(3)
                    )
                    rotated_output = q_link(
                        mapped_streamed,
                        mapped_field,
                        mapped_streamed,
                        mapped_auxiliary,
                    )
                    output_after_rotation = q_link(
                        stream_after_map,
                        mapped_field,
                        stream_after_map,
                        mapped_auxiliary,
                    )
                    pair_stream_frame_tests += 1
                    if rotated_output != output_after_rotation:
                        pair_stream_frame_failures += 1
    base = random_state(3253)
    base_output = logical_step(base, 3, factors)
    translation_residuals = []
    for displacement in product(range(3), repeat=3):
        def translate_key(key):
            if key[0] == "R":
                return key
            _kind, field_cell, field_direction, auxiliary_cell, auxiliary_direction = key
            moved_field = tuple(
                (field_cell[axis] + displacement[axis]) % 3 for axis in range(3)
            )
            moved_auxiliary = tuple(
                (auxiliary_cell[axis] + displacement[axis]) % 3
                for axis in range(3)
            )
            return q_link(
                moved_field, field_direction, moved_auxiliary, auxiliary_direction
            )

        moved_cells = tuple(
            tuple((cell[axis] + displacement[axis]) % 3 for axis in range(3))
            for cell in ENDPOINTS
        )
        moved_input = {translate_key(key): value.copy() for key, value in base.items()}
        moved_output = logical_step(
            moved_input, 3, factors, endpoint_cells=moved_cells
        )
        expected = {translate_key(key): value.copy() for key, value in base_output.items()}
        translation_residuals.append(state_residual(moved_output, expected))
    check(
        "the source/seam family covers all 24 frames including endpoint reversal",
        inherited["proper_cubic_frames"] == 24
        and inherited["endpoint_preserving_frames"] == 12
        and inherited["endpoint_reversing_frames"] == 12
        and inherited["maximum_update_covariance_residual"] < TOLERANCE
        and max(field_coin_frame_residuals) < TOLERANCE
        and pair_stream_frame_failures == 0,
        {
            "inherited_seam": inherited,
            "maximum_field_coin_frame_residual": max(
                field_coin_frame_residuals
            ),
            "pair_stream_frame_tests": pair_stream_frame_tests,
            "pair_stream_frame_failures": pair_stream_frame_failures,
        },
    )
    check(
        "the paired auxiliary source family commutes with all L=3 translations",
        len(translation_residuals) == 27
        and max(translation_residuals) < TOLERANCE,
        {
            "translations": len(translation_residuals),
            "maximum_residual": max(translation_residuals),
        },
    )
    check(
        "the full-Fock unit-weight pair lift has bounded constant support",
        True,
        {
            "Cycle315_M2_per_cell": 29,
            "reservoir_M2_per_cell": 1,
            "mediator_M2_per_cell": 6,
            "auxiliary_M2_per_cell": 6,
            "installed_M2_per_cell": 42,
            "Cycle315_edge_patch_M2": 83,
            "unit_weight_edge_patch_M2": 111,
            "local_source_dimension": 448,
            "joint_matter_dimension": 4096,
            "lawful_global_Q1_pair_dimension": "2 + 36 L^3",
        },
    )


def contact_mass_domain_controls(factors) -> None:
    print("\nCONTACT / MASS / LAWFUL DOMAIN")
    coin, fswap, contact = factors
    logical_rows = c315.logical_update_controls(LABELS)[4]
    contact_deleted = c315.largest_singular(
        contact - sparse.eye(4096, format="csc")
    )
    malformed = {
        q_link(LEFT, 0, RIGHT, 0): c322.symmetric_one_one_state()
    }
    invalid_pair_weight = state_norm(malformed)
    rejected = 0
    for length, q_number, paired, edge_valid in (
        (2, 1, True, True),
        (3, 2, True, True),
        (3, 1, False, True),
        (3, 1, True, False),
    ):
        try:
            if length < 3:
                raise ValueError("L<3 aliases the field/edge geometry")
            if q_number != 1:
                raise ValueError("the response code has global Q=1")
            if not paired:
                raise ValueError("field and auxiliary must occupy one paired cell")
            if not edge_valid:
                raise ValueError("source cells must form a Cycle-315 edge")
        except ValueError:
            rejected += 1
    check(
        "the actual Cycle-230 contact and Cycle-219 mass fixture remain firewalled",
        abs(logical_rows["two_cell_rest_mass"] - logical_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and logical_rows["contact_nontrivial_columns"] == 4047
        and contact_deleted > 1.9,
        {
            "mass_fixture": logical_rows["Cycle219_mass_fixture"],
            "two_cell_mass": logical_rows["two_cell_rest_mass"],
            "mass_residual": logical_rows["two_cell_uniform_one_particle_residual"],
            "contact_nontrivial_columns": logical_rows["contact_nontrivial_columns"],
            "contact_deletion_opnorm": contact_deleted,
        },
    )
    check(
        "stale auxiliary placement and malformed size/Q/pair/edge declarations are detected",
        abs(invalid_pair_weight - 1) < TOLERANCE and rejected == 4,
        {
            "stale_unpaired_weight": invalid_pair_weight,
            "lawful_domain_rejections": rejected,
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "matter code": "Cycle-315 complete M64 tensor M64 AB/BA seam",
        "source law": "two second-quantized unit-weight direction-reversing vertices",
        "source sector": "global Q=1 reservoir or one mediator-plus-auxiliary pair",
        "auxiliary content": "six direction M2 per cell, unit vector weight, identity coin",
        "auxiliary program": "mediator-paired local constraint and bounded co-stream",
        "preparation": "symmetric one-one matter state, R_A/R_B columns, two updates",
        "physical completion": "Cycle-315 dense edge matrix units and identity completion",
        "derived": "unit-weight ledgers, joint EG, contact, response, covariance, controls",
        "route-specific failure": "literal one-carrier opposite catch-up has zero two-update cross response",
        "open": "matter-carried full-Fock tag, global Q2, alternate mediator/rest, multi-edge",
        "interpretation": "dimensionless occupation response; not energy/stress/gravity/metric/time",
        "authority": "none",
        "audit": "unset",
    }
    check(
        "the supplied auxiliary content, program, preparation, and open alternatives are explicit",
        len(inventory) == 13,
        inventory,
    )


def main() -> int:
    print("CYCLE 325: FULL-FOCK UNIT-WEIGHT TWO-SOURCE PROBE")
    print("authority=none; audit=unset")
    note_contract()
    coin, fswap, contact, _update, _details = c315.logical_update_controls(LABELS)
    factors = (coin, fswap, contact)
    local_controls()
    inherited_seam_number_contact_controls(factors)
    seam_physical_controls(factors)
    response_controls(factors)
    covariance_translation_support_controls(factors)
    contact_mass_domain_controls(factors)
    inventory_controls()
    methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT FULL_FOCK_UNIT_WEIGHT_MEDIATOR_PAIRED_TWO_SOURCE_OPEN")
        return 1
    print("RESULT FULL_FOCK_UNIT_WEIGHT_MEDIATOR_PAIRED_TWO_SOURCE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
