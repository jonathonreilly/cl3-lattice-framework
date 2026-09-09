#!/usr/bin/env python3
"""Cycle 320: unit-weight carried-link recoil compiler.

The retained route extends the Cycle-316 one-carrier physical code by six
auxiliary direction M2 per cell.  Its source channels are
E_d <-> G_reverse(d),F_d,A_d.  They conserve Q and the dimensionless
unit-weight vector P_matter + P_mediator + P_aux at operator level.  The
auxiliary direction is transported with matter by the same bounded block
catch-up.  No physical momentum, work, energy, stress, or gravity meaning is
assigned.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import re
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import carried_internal_species_source_field_ledger_repair_2026_07_17 as carried
import carried_source_recurrent_tagged_block_cycle316_2026_07_18 as c316
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import physical_cycle269_local_fock_extension_cycle312_2026_07_18 as c312
import physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17 as c307
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import proper_cubic_recoil_balanced_carried_source_cycle318_2026_07_18 as c318


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md"
)
BETA = -0.3
ANGLE = carried.MEDIATOR_COUPLING * c219.common_species(BETA).analytic_mass
SIZES = (3, 4, 6)
HELD_SIZE = 6
TOLERANCE = 3e-10
REVERSE = (1, 0, 3, 2, 5, 4)

N1_ROUTES = (
    "Cycle-316 direction-preserving source",
    "Cycle-318 coefficient-two recoil source",
    "direction-preserving link reservoir",
    "direction-changing carried-link source",
    "uniform six-port rest-column candidate",
    "independent physical matter-rest column",
    "paired-mediator unit-weight branch",
    "simultaneous-carrier recoil/contact splice",
)
WALLS = ("W_aux", "W_rest", "W_multi", "W_contact", "W_energy")
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

Position = tuple[int, int, int]
PhysicalKey = tuple[int, int, int, int, int]
PhysicalState = dict[PhysicalKey, complex]


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
        check("the Cycle-320 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_link g_link = g_physical,link e_link",
        "one-carrier",
        "40 m2 per cell",
        "p_matter + p_mediator + p_aux",
        "unit-weight operator ledger",
        "nonzero matter recoil",
        "six auxiliary direction m2",
        "locally constrained",
        "source/tag/auxiliary catch-up",
        "emission, transport, and absorption",
        "all 24 proper-cubic frames",
        "all l=3 translations",
        "held l=6",
        "mass firewall",
        "contact firewall",
        "not physical momentum",
        "not work",
        "not energy",
        "not stress",
        "not gravity",
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
    check("the note pins the unit-weight theorem and interpretation firewall", not missing, missing)


def methodology_controls() -> None:
    print("\nEXECUTABLE NO-GO DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    allowed = {
        "ATTEMPTED",
        "RULED OUT BY PRIOR RESULT",
        "OPEN / UNTESTED",
    }
    markers: dict[str, str] = {}
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
        "N1 gives exact honesty markers to eight distinct normalization routes",
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
            "docs/work_history/repo/review_feedback/PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md",
            57,
            "coefficient",
        ),
        (
            "docs/work_history/repo/review_feedback/PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md",
            71,
            "recurrent auxiliary compiler",
        ),
        (
            "docs/work_history/repo/review_feedback/PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md",
            143,
            "unit-weight rest-mode route remains open",
        ),
        (
            "docs/work_history/repo/review_feedback/CARRIED_SOURCE_RECURRENT_TAGGED_BLOCK_CYCLE316_NOTE_2026-07-18.md",
            171,
            "simultaneous carriers are outside",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_LOCAL_FOCK_EXTENSION_CYCLE312_NOTE_2026-07-18.md",
            171,
            "simultaneous patches",
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


def zero_tensor() -> np.ndarray:
    return np.zeros((6, 6, 6), dtype=complex)


@dataclass
class LinkState:
    """One matter carrier: excited/no field/aux or ground/field/carried aux."""

    excited: dict[Position, np.ndarray]
    pair: dict[tuple[Position, Position], np.ndarray]

    def copy(self) -> "LinkState":
        return LinkState(
            {key: value.copy() for key, value in self.excited.items()},
            {key: value.copy() for key, value in self.pair.items()},
        )


def state_norm(state: LinkState) -> float:
    return float(
        sum(np.vdot(value, value).real for value in state.excited.values())
        + sum(np.vdot(value, value).real for value in state.pair.values())
    )


def state_residual(left: LinkState, right: LinkState) -> float:
    total = 0.0
    for key in left.excited.keys() | right.excited.keys():
        difference = left.excited.get(key, carried.zero_vector()) - right.excited.get(
            key, carried.zero_vector()
        )
        total += float(np.vdot(difference, difference).real)
    for key in left.pair.keys() | right.pair.keys():
        difference = left.pair.get(key, zero_tensor()) - right.pair.get(
            key, zero_tensor()
        )
        total += float(np.vdot(difference, difference).real)
    return float(np.sqrt(total))


def normalize_state(state: LinkState) -> LinkState:
    norm = np.sqrt(state_norm(state))
    return LinkState(
        {key: value / norm for key, value in state.excited.items()},
        {key: value / norm for key, value in state.pair.items()},
    )


def wrap_state(state: LinkState, length: int) -> LinkState:
    output = LinkState({}, {})
    for position, vector in state.excited.items():
        target = c316.wrapped(position, length)
        output.excited[target] = output.excited.get(target, carried.zero_vector()) + vector
    for (body, field), tensor in state.pair.items():
        target = (c316.wrapped(body, length), c316.wrapped(field, length))
        output.pair[target] = output.pair.get(target, zero_tensor()) + tensor
    return output


def test_state(length: int) -> LinkState:
    rng = np.random.default_rng(32000 + length)
    adjacent = (1 % length, 0, 0)
    excited = {
        (0, 0, 0): rng.normal(size=6) + 1j * rng.normal(size=6),
        adjacent: rng.normal(size=6) + 1j * rng.normal(size=6),
    }
    onsite = rng.normal(size=(6, 6, 6)) + 1j * rng.normal(size=(6, 6, 6))
    separated = rng.normal(size=(6, 6, 6)) + 1j * rng.normal(size=(6, 6, 6))
    pair = {
        (adjacent, adjacent): onsite,
        ((0, 0, 0), (0, 1 % length, 0)): separated,
    }
    return normalize_state(LinkState(excited, pair))


def link_recoil_vertex(
    angle: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, tuple[np.ndarray, ...]]:
    dimension = 6 + 6**3
    exchange = np.zeros((dimension, dimension), dtype=complex)
    for direction in range(6):
        pair_index = 6 + 36 * REVERSE[direction] + 6 * direction + direction
        exchange[pair_index, direction] = 1.0
        exchange[direction, pair_index] = 1.0
    square = exchange @ exchange
    vertex = (
        np.eye(dimension, dtype=complex)
        + (np.cos(angle) - 1) * square
        + 1j * np.sin(angle) * exchange
    )
    charge = np.eye(dimension, dtype=complex)
    momenta = []
    for axis in range(3):
        values = [float(c210.DIRECTIONS[d, axis]) for d in range(6)]
        values.extend(
            float(
                c210.DIRECTIONS[matter, axis]
                + c210.DIRECTIONS[field, axis]
                + c210.DIRECTIONS[auxiliary, axis]
            )
            for matter in range(6)
            for field in range(6)
            for auxiliary in range(6)
        )
        momenta.append(np.diag(values))
    return exchange, vertex, charge, tuple(momenta)


def active_frame_222(frame: np.ndarray) -> np.ndarray:
    representation = c210.direction_permutation(frame)
    active = np.zeros((222, 222), dtype=complex)
    active[:6, :6] = representation
    active[6:, 6:] = np.kron(np.kron(representation, representation), representation)
    return active


def vector_expectation(excited: np.ndarray, pair: np.ndarray) -> np.ndarray:
    probabilities = abs(pair) ** 2
    matter_weights = abs(excited) ** 2 + np.sum(probabilities, axis=(1, 2))
    field_weights = np.sum(probabilities, axis=(0, 2))
    auxiliary_weights = np.sum(probabilities, axis=(0, 1))
    return (
        matter_weights @ c210.DIRECTIONS
        + field_weights @ c210.DIRECTIONS
        + auxiliary_weights @ c210.DIRECTIONS
    )


def local_vertex(
    excited: np.ndarray, contact_pair: np.ndarray, angle: float
) -> tuple[np.ndarray, np.ndarray]:
    _exchange, vertex, _charge, _momenta = link_recoil_vertex(angle)
    vector = np.concatenate((excited, contact_pair.reshape(-1)))
    output = vertex @ vector
    return output[:6], output[6:].reshape(6, 6, 6)


def vertex_gate(state: LinkState, angle: float) -> tuple[LinkState, dict[str, object]]:
    output = state.copy()
    positions = set(state.excited)
    positions.update(body for body, field in state.pair if body == field)
    q_residual = 0.0
    p_residual = 0.0
    source_current: dict[Position, float] = {}
    for position in positions:
        excited = state.excited.get(position, carried.zero_vector())
        pair = state.pair.get((position, position), zero_tensor())
        before_q = float(np.vdot(excited, excited).real + np.vdot(pair, pair).real)
        before_p = vector_expectation(excited, pair)
        new_excited, new_pair = local_vertex(excited, pair, angle)
        after_q = float(
            np.vdot(new_excited, new_excited).real + np.vdot(new_pair, new_pair).real
        )
        after_p = vector_expectation(new_excited, new_pair)
        q_residual = max(q_residual, abs(after_q - before_q))
        p_residual = max(p_residual, float(np.linalg.norm(after_p - before_p)))
        source_current[position] = float(
            np.vdot(new_pair, new_pair).real - np.vdot(pair, pair).real
        )
        output.excited[position] = new_excited
        output.pair[(position, position)] = new_pair
    return output, {
        "local_Q_residual": q_residual,
        "local_P_residual": p_residual,
        "source_current": source_current,
    }


def coin_gate(
    state: LinkState, matter_coin: np.ndarray, field_coin: np.ndarray
) -> LinkState:
    return LinkState(
        {position: matter_coin @ value for position, value in state.excited.items()},
        {
            key: np.einsum(
                "im,jf,mfa->ija", matter_coin, field_coin, value, optimize=True
            )
            for key, value in state.pair.items()
        },
    )


def body_stream(
    state: LinkState,
) -> tuple[LinkState, dict[tuple[Position, int], float], dict[tuple[Position, int], float]]:
    output = LinkState({}, {})
    matter_current: dict[tuple[Position, int], float] = {}
    excitation_current: dict[tuple[Position, int], float] = {}
    for body, value in state.excited.items():
        for direction in range(6):
            destination = carried.add_position(body, c210.DIRECTIONS[direction])
            output.excited.setdefault(destination, carried.zero_vector())[direction] += value[
                direction
            ]
            amount = float(abs(value[direction]) ** 2)
            matter_current[(body, direction)] = amount
            excitation_current[(body, direction)] = amount
    for (body, field), value in state.pair.items():
        for direction in range(6):
            destination = carried.add_position(body, c210.DIRECTIONS[direction])
            output.pair.setdefault((destination, field), zero_tensor())[
                direction, :, :
            ] += value[direction, :, :]
            amount = float(np.vdot(value[direction, :, :], value[direction, :, :]).real)
            matter_current[(body, direction)] = (
                matter_current.get((body, direction), 0.0) + amount
            )
    return output, matter_current, excitation_current


def field_stream(
    state: LinkState,
) -> tuple[LinkState, dict[tuple[Position, int], float]]:
    output = LinkState(
        {key: value.copy() for key, value in state.excited.items()}, {}
    )
    current: dict[tuple[Position, int], float] = {}
    for (body, field), value in state.pair.items():
        for direction in range(6):
            destination = carried.add_position(field, c210.DIRECTIONS[direction])
            output.pair.setdefault((body, destination), zero_tensor())[
                :, direction, :
            ] += value[:, direction, :]
            amount = float(np.vdot(value[:, direction, :], value[:, direction, :]).real)
            current[(field, direction)] = current.get((field, direction), 0.0) + amount
    return output, current


def matter_density(state: LinkState) -> dict[Position, float]:
    answer: dict[Position, float] = {}
    for body, value in state.excited.items():
        answer[body] = answer.get(body, 0.0) + float(np.vdot(value, value).real)
    for (body, _field), value in state.pair.items():
        answer[body] = answer.get(body, 0.0) + float(np.vdot(value, value).real)
    return answer


def q_density(state: LinkState) -> dict[Position, float]:
    answer = {
        body: float(np.vdot(value, value).real)
        for body, value in state.excited.items()
    }
    for (_body, field), value in state.pair.items():
        answer[field] = answer.get(field, 0.0) + float(np.vdot(value, value).real)
    return answer


def logical_step(
    state: LinkState, model: c307.GlobalModel
) -> tuple[LinkState, dict[str, float]]:
    species = c219.common_species(BETA)
    before = state_norm(state)
    coined = coin_gate(state, species.coin, c214.FIELD_COIN)
    sourced, vertex_report = vertex_gate(coined, ANGLE)
    bodied, matter_current, excitation_current = body_stream(sourced)
    bodied = wrap_state(bodied, model.length)
    fielded, field_current = field_stream(bodied)
    fielded = wrap_state(fielded, model.length)
    return fielded, {
        "norm_residual": abs(state_norm(fielded) - before),
        "local_Q_residual": float(vertex_report["local_Q_residual"]),
        "local_P_residual": float(vertex_report["local_P_residual"]),
        "matter_current_residual": abs(
            sum(matter_current.values()) - sum(matter_density(sourced).values())
        ),
        "Q_current_residual": abs(
            sum(excitation_current.values())
            + sum(field_current.values())
            - sum(q_density(sourced).values())
        ),
    }


def add_state_value(state: PhysicalState, key: PhysicalKey, value: complex) -> None:
    if abs(value) < 2e-14:
        return
    state[key] = state.get(key, 0.0j) + value
    if abs(state[key]) < 2e-14:
        del state[key]


def physical_norm(state: PhysicalState) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def physical_residual(left: PhysicalState, right: PhysicalState) -> float:
    return float(
        np.sqrt(
            sum(
                abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
                for key in left.keys() | right.keys()
            )
        )
    )


def extended_column(
    model: c307.GlobalModel,
    matter_mode: int,
    *,
    excited: bool,
    field_mode: int = -1,
    auxiliary_direction: int = -1,
) -> PhysicalState:
    carrier_position = c316.mode_position(model, matter_mode)
    source = c316.cell_flat(carrier_position, model.length) if excited else -1
    auxiliary_mode = (
        -1
        if excited
        else c316.mode_at(model, carrier_position, auxiliary_direction)
    )
    return {
        (row, matter_mode, source, field_mode, auxiliary_mode): value
        for row, value in c316.column_items(model, matter_mode)
    }


def encode_state(state: LinkState, model: c307.GlobalModel) -> PhysicalState:
    output: PhysicalState = {}
    for body, vector in state.excited.items():
        for direction, amplitude in enumerate(vector):
            if abs(amplitude) < 2e-14:
                continue
            matter_mode = c316.mode_at(model, body, direction)
            for key, coefficient in extended_column(
                model, matter_mode, excited=True
            ).items():
                add_state_value(output, key, amplitude * coefficient)
    for (body, field), tensor in state.pair.items():
        for matter_direction in range(6):
            matter_mode = c316.mode_at(model, body, matter_direction)
            for field_direction in range(6):
                field_mode = c316.mode_at(model, field, field_direction)
                for auxiliary_direction in range(6):
                    amplitude = tensor[
                        matter_direction, field_direction, auxiliary_direction
                    ]
                    if abs(amplitude) < 2e-14:
                        continue
                    for key, coefficient in extended_column(
                        model,
                        matter_mode,
                        excited=False,
                        field_mode=field_mode,
                        auxiliary_direction=auxiliary_direction,
                    ).items():
                        add_state_value(output, key, amplitude * coefficient)
    return output


def inner_product(column: PhysicalState, state: PhysicalState) -> complex:
    return sum(value.conjugate() * state.get(key, 0.0j) for key, value in column.items())


def apply_lifted_block(
    state: PhysicalState,
    columns: tuple[PhysicalState, ...],
    matrix: np.ndarray,
) -> PhysicalState:
    overlaps = np.asarray([inner_product(column, state) for column in columns])
    correction = (matrix - np.eye(len(columns), dtype=complex)) @ overlaps
    output = dict(state)
    for amplitude, column in zip(correction, columns):
        if abs(amplitude) < 2e-14:
            continue
        for key, value in column.items():
            add_state_value(output, key, amplitude * value)
    return output


def lawful_code_leakage(state: PhysicalState, model: c307.GlobalModel) -> float:
    leakage_squared = 0.0
    labels = {
        (port, source, field, auxiliary)
        for _row, port, source, field, auxiliary in state
    }
    for port, source, field, auxiliary in labels:
        carrier_position = c316.mode_position(model, port)
        carrier_cell = c316.cell_flat(carrier_position, model.length)
        if source == carrier_cell and field == -1 and auxiliary == -1:
            column = extended_column(model, port, excited=True)
        elif source == -1 and field >= 0 and auxiliary >= 0:
            auxiliary_position, auxiliary_direction = model.code.graph.vertices[
                auxiliary
            ]
            if auxiliary_position != carrier_position:
                column = None
            else:
                column = extended_column(
                    model,
                    port,
                    excited=False,
                    field_mode=field,
                    auxiliary_direction=auxiliary_direction,
                )
        else:
            column = None
        actual = {
            row: value
            for (row, label_port, label_source, label_field, label_auxiliary), value in state.items()
            if (label_port, label_source, label_field, label_auxiliary)
            == (port, source, field, auxiliary)
        }
        if column is None:
            leakage_squared += sum(abs(value) ** 2 for value in actual.values())
            continue
        amplitude = inner_product(column, state)
        expected = {row: amplitude * value for (row, *_labels), value in column.items()}
        leakage_squared += sum(
            abs(actual.get(row, 0.0j) - expected.get(row, 0.0j)) ** 2
            for row in actual.keys() | expected.keys()
        )
    return float(np.sqrt(leakage_squared))


def active_field_auxiliary_labels(
    state: PhysicalState, modes: set[int], model: c307.GlobalModel
) -> set[tuple[int, int]]:
    answer = set()
    for _row, port, source, field, auxiliary in state:
        if port in modes and source == -1 and field >= 0 and auxiliary >= 0:
            _position, auxiliary_direction = model.code.graph.vertices[auxiliary]
            answer.add((field, auxiliary_direction))
    return answer


def apply_matter_block_family(
    state: PhysicalState, model: c307.GlobalModel, kind: str
) -> PhysicalState:
    output = state
    for block in c312.local_blocks(model, kind):
        modes = set(block.logical_modes)
        if any(
            port in modes and source >= 0
            for _row, port, source, _field, _auxiliary in output
        ):
            columns = tuple(
                extended_column(model, mode, excited=True)
                for mode in block.logical_modes
            )
            output = apply_lifted_block(output, columns, block.matrix)
        for field_mode, auxiliary_direction in active_field_auxiliary_labels(
            output, modes, model
        ):
            columns = tuple(
                extended_column(
                    model,
                    mode,
                    excited=False,
                    field_mode=field_mode,
                    auxiliary_direction=auxiliary_direction,
                )
                for mode in block.logical_modes
            )
            output = apply_lifted_block(output, columns, block.matrix)
    return output


def apply_field_coin(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState:
    output: PhysicalState = {}
    for (row, port, source, field_mode, auxiliary), amplitude in state.items():
        if field_mode < 0:
            add_state_value(output, (row, port, source, field_mode, auxiliary), amplitude)
            continue
        field_cell, field_direction = model.code.graph.vertices[field_mode]
        for target_direction in range(6):
            target = c316.mode_at(model, field_cell, target_direction)
            add_state_value(
                output,
                (row, port, source, target, auxiliary),
                c214.FIELD_COIN[target_direction, field_direction] * amplitude,
            )
    return output


def apply_source_block(
    state: PhysicalState, model: c307.GlobalModel, cell: Position
) -> PhysicalState:
    _exchange, vertex, _charge, _momenta = link_recoil_vertex(ANGLE)
    modes = tuple(c316.mode_at(model, cell, direction) for direction in range(6))
    columns = tuple(
        extended_column(model, mode, excited=True) for mode in modes
    ) + tuple(
        extended_column(
            model,
            matter,
            excited=False,
            field_mode=field,
            auxiliary_direction=auxiliary_direction,
        )
        for matter in modes
        for field in modes
        for auxiliary_direction in range(6)
    )
    return apply_lifted_block(state, columns, vertex)


def apply_source_vertices(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState:
    output = state
    for cell in model.code.graph.cells:
        output = apply_source_block(output, model, cell)
    return output


def apply_field_stream(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState:
    output: PhysicalState = {}
    for (row, port, source, field_mode, auxiliary), amplitude in state.items():
        if field_mode < 0:
            target_field = -1
        else:
            field_cell, field_direction = model.code.graph.vertices[field_mode]
            target_cell = c316.wrapped(
                tuple(
                    field_cell[axis] + int(c210.DIRECTIONS[field_direction, axis])
                    for axis in range(3)
                ),
                model.length,
            )
            target_field = c316.mode_at(model, target_cell, field_direction)
        add_state_value(
            output, (row, port, source, target_field, auxiliary), amplitude
        )
    return output


def physical_step(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState:
    output = apply_matter_block_family(state, model, "coin")
    output = apply_field_coin(output, model)
    output = apply_source_vertices(output, model)
    output = apply_matter_block_family(output, model, "reverse")
    output = apply_matter_block_family(output, model, "edge")
    return apply_field_stream(output, model)


def local_route_controls() -> None:
    print("\nLOCAL UNIT-NORMALIZATION TOURNAMENT")
    _exchange, vertex, charge, momenta = link_recoil_vertex(ANGLE)
    unitarity = float(np.linalg.norm(vertex.conj().T @ vertex - np.eye(222)))
    q_commutator = float(np.linalg.norm(vertex @ charge - charge @ vertex))
    p_commutators = tuple(
        float(np.linalg.norm(vertex @ momentum - momentum @ vertex))
        for momentum in momenta
    )
    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        active = active_frame_222(frame)
        frame_residuals.append(float(np.linalg.norm(active @ vertex @ active.T - vertex)))

    response_rows = []
    for direction in range(6):
        initial = np.eye(222, dtype=complex)[:, direction]
        final = vertex @ initial
        probabilities = abs(final) ** 2
        final_matter = np.zeros(3)
        final_field = np.zeros(3)
        final_auxiliary = np.zeros(3)
        for matter_direction in range(6):
            final_matter += probabilities[matter_direction] * c210.DIRECTIONS[matter_direction]
        for matter_direction in range(6):
            for field_direction in range(6):
                for auxiliary_direction in range(6):
                    index = (
                        6
                        + 36 * matter_direction
                        + 6 * field_direction
                        + auxiliary_direction
                    )
                    final_matter += probabilities[index] * c210.DIRECTIONS[matter_direction]
                    final_field += probabilities[index] * c210.DIRECTIONS[field_direction]
                    final_auxiliary += probabilities[index] * c210.DIRECTIONS[auxiliary_direction]
        initial_vector = c210.DIRECTIONS[direction].astype(float)
        response_rows.append(
            {
                "direction": direction,
                "matter_recoil": tuple(final_matter - initial_vector),
                "mediator_flux": tuple(final_field),
                "auxiliary_flux": tuple(final_auxiliary),
                "balance_residual": float(
                    np.linalg.norm(
                        final_matter + final_field + final_auxiliary - initial_vector
                    )
                ),
            }
        )
    check(
        "the direction-changing carried-link vertex has exact unit-weight Q/P operator balance and nonzero matter recoil",
        unitarity < TOLERANCE
        and q_commutator == 0
        and max(p_commutators) == 0
        and max(frame_residuals) == 0
        and max(row["balance_residual"] for row in response_rows) < TOLERANCE
        and min(np.linalg.norm(row["matter_recoil"]) for row in response_rows) > 0.2,
        {
            "active_dimension": 222,
            "unitarity_residual": unitarity,
            "Q_commutator": q_commutator,
            "P_commutators": p_commutators,
            "maximum_frame_residual": max(frame_residuals),
            "unit_weights": (1, 1, 1),
            "response_rows": response_rows,
        },
    )

    _old_exchange, old_link, old_charge, old_momenta = c318.link_vertex(ANGLE)
    old_matter_commutators = []
    for axis in range(3):
        values = [float(c210.DIRECTIONS[d, axis]) for d in range(6)]
        values.extend(
            float(c210.DIRECTIONS[matter, axis])
            for matter in range(6)
            for _field in range(6)
            for _auxiliary in range(6)
        )
        matter_operator = np.diag(values)
        old_matter_commutators.append(
            float(np.linalg.norm(old_link @ matter_operator - matter_operator @ old_link))
        )
    check(
        "the direction-preserving link comparator balances unit P but has zero matter recoil operator",
        np.linalg.norm(old_link @ old_charge - old_charge @ old_link) == 0
        and max(
            np.linalg.norm(old_link @ momentum - momentum @ old_link)
            for momentum in old_momenta
        )
        == 0
        and max(old_matter_commutators) == 0,
        {
            "P_commutators": tuple(
                float(np.linalg.norm(old_link @ momentum - momentum @ old_link))
                for momentum in old_momenta
            ),
            "matter_direction_commutators": old_matter_commutators,
            "disposition": "exact balance but no matter recoil",
        },
    )


def recurrent_intertwiner_controls(models: dict[int, c307.GlobalModel]) -> None:
    print("\nRECURRENT 40-M2 PHYSICAL INTERTWINER")
    rows = []
    for length, model in models.items():
        logical = test_state(length)
        encoded = encode_state(logical, model)
        logical_output, report = logical_step(logical, model)
        physical_output = physical_step(encoded, model)
        expected = encode_state(logical_output, model)
        gram = model.encoding.conj().T @ model.encoding
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "matter_Gram_residual": c312.maximum_abs(
                    gram
                    - c312.sparse.eye(gram.shape[0], dtype=complex, format="csc")
                ),
                "EG_residual": physical_residual(physical_output, expected),
                "encoded_norm_residual": abs(physical_norm(encoded) - 1),
                "output_norm_residual": abs(physical_norm(physical_output) - 1),
                "continuity": report,
            }
        )
    check(
        "the carried-link code obeys E_link G_link = G_physical,link E_link through held L=6",
        max(
            max(
                row["matter_Gram_residual"],
                row["EG_residual"],
                row["encoded_norm_residual"],
                row["output_norm_residual"],
                max(row["continuity"].values()),
            )
            for row in rows
        )
        < TOLERANCE,
        rows,
    )


def emission_transport_absorption_catchup(
    models: dict[int, c307.GlobalModel]
) -> None:
    print("\nEMISSION / TRANSPORT / ABSORPTION / AUXILIARY CATCH-UP")
    rows = []
    for length, model in models.items():
        initial = LinkState({(0, 0, 0): c210.UNIFORM.copy()}, {})
        sourced, report = vertex_gate(initial, ANGLE)
        bodied, _matter_current, _excitation_current = body_stream(sourced)
        bodied = wrap_state(bodied, length)
        transported, _field_current = field_stream(bodied)
        transported = wrap_state(transported, length)

        field_density: dict[Position, float] = {}
        auxiliary_cells: dict[tuple[Position, int], float] = {}
        for (body, field), tensor in transported.pair.items():
            field_density[field] = field_density.get(field, 0.0) + float(
                np.vdot(tensor, tensor).real
            )
            for auxiliary_direction in range(6):
                weight = float(
                    np.vdot(
                        tensor[:, :, auxiliary_direction],
                        tensor[:, :, auxiliary_direction],
                    ).real
                )
                auxiliary_cells[(body, auxiliary_direction)] = (
                    auxiliary_cells.get((body, auxiliary_direction), 0.0) + weight
                )
        predicted = np.sin(ANGLE) ** 2 / 6
        field_error = 0.0
        auxiliary_error = 0.0
        for direction in range(6):
            field_target = c316.wrapped(
                tuple(int(value) for value in c210.DIRECTIONS[direction]), length
            )
            matter_target = c316.wrapped(
                tuple(-int(value) for value in c210.DIRECTIONS[direction]), length
            )
            field_error = max(
                field_error, abs(field_density.get(field_target, 0.0) - predicted)
            )
            auxiliary_error = max(
                auxiliary_error,
                abs(auxiliary_cells.get((matter_target, direction), 0.0) - predicted),
            )

        physical_initial = encode_state(initial, model)
        physical_sourced = apply_source_vertices(physical_initial, model)
        physical_sourced = apply_matter_block_family(physical_sourced, model, "reverse")
        physical_sourced = apply_matter_block_family(physical_sourced, model, "edge")
        physical_transported = apply_field_stream(physical_sourced, model)
        expected = encode_state(transported, model)
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "emitted_weight": sum(field_density.values()),
                "predicted_sin2": np.sin(ANGLE) ** 2,
                "maximum_field_error": field_error,
                "maximum_auxiliary_catchup_error": auxiliary_error,
                "source_stream_intertwiner": physical_residual(
                    physical_transported, expected
                ),
                "local_Q_residual": report["local_Q_residual"],
                "local_P_residual": report["local_P_residual"],
            }
        )

    incoming = zero_tensor()
    for direction in range(6):
        incoming[REVERSE[direction], direction, direction] = c210.UNIFORM[direction]
    absorbed_excited, remaining_pair = local_vertex(
        carried.zero_vector(), incoming, ANGLE
    )
    absorbed_weight = float(np.vdot(absorbed_excited, absorbed_excited).real)
    remaining_weight = float(np.vdot(remaining_pair, remaining_pair).real)

    model = models[3]
    source_mode = c316.mode_at(model, (0, 0, 0), 0)
    target_mode = c316.mode_at(model, (1, 0, 0), 0)
    stale_auxiliary = c316.mode_at(model, (0, 0, 0), 0)
    field_mode = c316.mode_at(model, (0, 1, 0), 2)
    stale: PhysicalState = {
        (row, target_mode, -1, field_mode, stale_auxiliary): value
        for row, value in c316.column_items(model, target_mode)
    }
    deleted_auxiliary_catchup = lawful_code_leakage(stale, model)
    check(
        "emission, physical transport, conjugate absorption, and source/tag/auxiliary catch-up are exact with no host query",
        max(
            max(
                abs(row["emitted_weight"] - row["predicted_sin2"]),
                row["maximum_field_error"],
                row["maximum_auxiliary_catchup_error"],
                row["source_stream_intertwiner"],
                row["local_Q_residual"],
                row["local_P_residual"],
            )
            for row in rows
        )
        < TOLERANCE
        and abs(absorbed_weight - np.sin(ANGLE) ** 2) < TOLERANCE
        and abs(remaining_weight - np.cos(ANGLE) ** 2) < TOLERANCE
        and abs(deleted_auxiliary_catchup - 1) < TOLERANCE,
        {
            "volume_rows": rows,
            "absorption_source_weight": absorbed_weight,
            "remaining_link_weight": remaining_weight,
            "deleted_auxiliary_catchup_leakage": deleted_auxiliary_catchup,
            "source_blocks_applied_at_every_cell": True,
            "host_carrier_cell_queries": 0,
        },
    )


def rotate_state(state: LinkState, frame: np.ndarray, length: int) -> LinkState:
    representation = c210.direction_permutation(frame)

    def rotate_position(position: Position) -> Position:
        vector = frame @ np.asarray(position, dtype=int)
        return c316.wrapped(tuple(int(value) for value in vector), length)

    return LinkState(
        {
            rotate_position(position): representation @ vector
            for position, vector in state.excited.items()
        },
        {
            (rotate_position(body), rotate_position(field)): np.einsum(
                "im,jf,ka,mfa->ijk",
                representation,
                representation,
                representation,
                tensor,
                optimize=True,
            )
            for (body, field), tensor in state.pair.items()
        },
    )


def translate_state(
    state: LinkState, displacement: Position, length: int
) -> LinkState:
    return LinkState(
        {
            c316.translated(position, displacement, length): vector.copy()
            for position, vector in state.excited.items()
        },
        {
            (
                c316.translated(body, displacement, length),
                c316.translated(field, displacement, length),
            ): tensor.copy()
            for (body, field), tensor in state.pair.items()
        },
    )


def overlap_covariance_support_controls(
    models: dict[int, c307.GlobalModel]
) -> None:
    print("\nOVERLAP / COVARIANCE / TRANSLATIONS / SUPPORT")
    model = models[3]
    coin_blocks = {block.label: block for block in c312.local_blocks(model, "coin")}
    left_block = coin_blocks[(0, 0, 0)]
    right_block = coin_blocks[(1, 0, 0)]
    left_support = c312.block_mode_support(model, left_block)
    right_support = c312.block_mode_support(model, right_block)
    encoded = encode_state(test_state(3), model)
    left_then_right = apply_source_block(
        apply_source_block(encoded, model, (0, 0, 0)), model, (1, 0, 0)
    )
    right_then_left = apply_source_block(
        apply_source_block(encoded, model, (1, 0, 0)), model, (0, 0, 0)
    )
    overlap_commutator = physical_residual(left_then_right, right_then_left)
    overlap_leakage = max(
        lawful_code_leakage(left_then_right, model),
        lawful_code_leakage(right_then_left, model),
    )

    state = test_state(3)
    advanced, _ = logical_step(state, model)
    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        framed_input = rotate_state(state, frame, 3)
        framed_output, _ = logical_step(framed_input, model)
        frame_residuals.append(
            state_residual(framed_output, rotate_state(advanced, frame, 3))
        )
    translation_residuals = []
    for displacement in product(range(3), repeat=3):
        moved_input = translate_state(state, displacement, 3)
        moved_output, _ = logical_step(moved_input, model)
        translation_residuals.append(
            state_residual(moved_output, translate_state(advanced, displacement, 3))
        )

    support_rows = []
    for length, current in models.items():
        support_rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "base_Cycle316_M2_per_cell": 34,
                "added_auxiliary_direction_M2_per_cell": 6,
                "installed_M2_per_cell": 40,
                "source_active_dimension": 222,
                "combined_two_cell_patch_envelope_M2": 254,
                "maximum_pair_rows_per_block": max(
                    len(c312.block_mode_support(current, block))
                    for kind in ("coin", "reverse", "edge")
                    for block in c312.local_blocks(current, kind)
                ),
            }
        )
    check(
        "adjacent translated 222-state source blocks retain the literal 14-row overlap without order ambiguity or leakage",
        len(left_support & right_support) == 14
        and overlap_commutator < TOLERANCE
        and overlap_leakage < TOLERANCE,
        {
            "overlapping_pair_rows": len(left_support & right_support),
            "opposite_order_residual": overlap_commutator,
            "lawful_code_leakage": overlap_leakage,
        },
    )
    check(
        "the full carried-link update is covariant in all 24 frames and all L=3 translations",
        len(frame_residuals) == 24
        and len(translation_residuals) == 27
        and max(frame_residuals + translation_residuals) < TOLERANCE,
        {
            "maximum_frame_residual": max(frame_residuals),
            "maximum_translation_residual": max(translation_residuals),
        },
    )
    check(
        "the recurrent carried-link compiler has constant 40-M2 overhead and bounded blocks through held L=6",
        all(row["installed_M2_per_cell"] == 40 for row in support_rows)
        and all(row["maximum_pair_rows_per_block"] <= 36 for row in support_rows)
        and all(row["combined_two_cell_patch_envelope_M2"] == 254 for row in support_rows),
        support_rows,
    )


def rest_mass_contact_deletion_controls(
    models: dict[int, c307.GlobalModel]
) -> None:
    print("\nREST COMPARATOR / MASS / CONTACT / DELETIONS")
    rest_rows = []
    mass_rows = []
    species = c219.common_species(BETA)
    for length, model in models.items():
        rest = np.zeros(model.encoding.shape[1], dtype=complex)
        for direction in range(6):
            rest[c316.mode_at(model, (0, 0, 0), direction)] = c210.UNIFORM[direction]
        _coin, _reverse, _edge, stream = c312.logical_layers(model)
        streamed = stream @ rest
        rest_rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "stationarity_residual": float(np.linalg.norm(streamed - rest)),
                "physical_stationarity_residual": float(
                    np.linalg.norm(model.encoding @ streamed - model.encoding @ rest)
                ),
            }
        )
        uniform = np.ones(model.encoding.shape[1], dtype=complex)
        uniform /= np.linalg.norm(uniform)
        eigenvalue = np.vdot(uniform, model.one_particle_coin @ uniform)
        mass_rows.append(
            {
                "L": length,
                "source_off_mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
            }
        )
    check(
        "the uniform six-port bounded rest-column candidate is not stationary under the actual matter stream",
        min(row["stationarity_residual"] for row in rest_rows) > 1.4
        and max(
            abs(row["stationarity_residual"] - row["physical_stationarity_residual"])
            for row in rest_rows
        )
        < TOLERANCE,
        rest_rows,
    )

    exchange, _vertex, _charge, _momenta = link_recoil_vertex(ANGLE)
    _exchange, deleted, _charge, _momenta = link_recoil_vertex(0.0)
    unilateral = np.tril(exchange, k=-1)
    bad_gate = np.eye(222, dtype=complex) + 1j * ANGLE * unilateral
    bad_unitarity = float(np.linalg.norm(bad_gate.conj().T @ bad_gate - np.eye(222)))

    no_aux_momenta = []
    _exchange, vertex, _charge, _momenta = link_recoil_vertex(ANGLE)
    for axis in range(3):
        values = [float(c210.DIRECTIONS[d, axis]) for d in range(6)]
        values.extend(
            float(c210.DIRECTIONS[matter, axis] + c210.DIRECTIONS[field, axis])
            for matter in range(6)
            for field in range(6)
            for _auxiliary in range(6)
        )
        no_aux_momenta.append(np.diag(values))
    deleted_aux_commutator = max(
        float(np.linalg.norm(vertex @ momentum - momentum @ vertex))
        for momentum in no_aux_momenta
    )

    rejected = 0
    for fixture in (
        (2, 1, 1, True, True),
        (3, 2, 1, True, True),
        (3, 1, 0, True, True),
        (3, 1, 1, False, True),
        (3, 1, 1, True, False),
    ):
        length, matter_count, charge, tags_match, auxiliary_matches = fixture
        try:
            if length < 3:
                raise ValueError("L<3 aliases the translated block grammar")
            if matter_count != 1:
                raise ValueError("the Cycle-320 code has exactly one carrier")
            if charge != 1:
                raise ValueError("the Cycle-320 code has prepared Q=1")
            if not tags_match:
                raise ValueError("the port/source tag must match the carrier")
            if not auxiliary_matches:
                raise ValueError("the auxiliary direction M2 must occupy the carrier cell")
        except ValueError:
            rejected += 1
    check(
        "the source-off mass fixture is unchanged through held L=6",
        max(abs(row["source_off_mass"] - species.analytic_mass) for row in mass_rows)
        < 4e-13,
        mass_rows,
    )
    check(
        "the one-carrier carried-link code cannot fire recurrent multiparticle contact",
        rejected == 5,
        {
            "matter_carriers_in_lawful_code": 1,
            "Cycle230_contact_calls": 0,
            "recurrent_contact_compiled": False,
            "lawful_domain_rejections": rejected,
        },
    )
    check(
        "coupling, conjugate, and auxiliary-ledger deletions are nontrivial controls",
        np.linalg.norm(deleted - np.eye(222)) == 0
        and bad_unitarity > 0.1
        and deleted_aux_commutator > 0.5,
        {
            "zero_coupling_identity_residual": float(
                np.linalg.norm(deleted - np.eye(222))
            ),
            "unilateral_gate_unitarity_residual": bad_unitarity,
            "deleted_auxiliary_P_commutator": deleted_aux_commutator,
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "inherited physical code": "Cycle-316 recurrent tagged matter/source/mediator compiler",
        "added physical M2": "six auxiliary direction M2 per cell, one-hot only in the ground-field branch",
        "supplied vertex": "E_d to G_reverse(d),F_d,A_d with coupling kappa*m_fixture",
        "supplied sectors": "one matter carrier and Q=N_source+N_field=1",
        "supplied auxiliary law": "auxiliary direction has unit P weight, identity coin, and matter-carried catch-up",
        "derived": "unit-weight operator Q/P, recoil response, 40-M2 recurrence, emission/transport/absorption, covariance",
        "failed comparator": "uniform six-port rest column has stationarity residual sqrt(2)",
        "open": "independent rest column, paired mediator, simultaneous carriers, contact, two sources, physical calibration",
        "interpretation firewall": "dimensionless direction/flux only; not physical momentum, work, energy, stress, gravity, or metric",
        "authority": "none",
        "audit": "unset",
    }
    required = {
        "inherited physical code",
        "added physical M2",
        "supplied vertex",
        "supplied auxiliary law",
        "derived",
        "failed comparator",
        "open",
        "interpretation firewall",
        "authority",
        "audit",
    }
    check("the supplied, derived, failed, and open structure is explicit", required <= inventory.keys(), inventory)


def main() -> int:
    print("CYCLE 320: UNIT-WEIGHT CARRIED-LINK RECOIL")
    print("authority=none; audit=unset")
    note_contract()
    models = {length: c307.build_model(length) for length in SIZES}
    local_route_controls()
    recurrent_intertwiner_controls(models)
    emission_transport_absorption_catchup(models)
    overlap_covariance_support_controls(models)
    rest_mass_contact_deletion_controls(models)
    inventory_controls()
    methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT UNIT_WEIGHT_CARRIED_LINK_RECOIL_OPEN")
        return 1
    print("RESULT UNIT_WEIGHT_CARRIED_LINK_RECOIL_FACTOR_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
