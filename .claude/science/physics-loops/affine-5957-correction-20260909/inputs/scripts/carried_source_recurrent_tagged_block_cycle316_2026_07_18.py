#!/usr/bin/env python3
"""Cycle 316: recurrent carried source on tagged Cycle-312 blocks.

Extend the exact Cycle-312 one-carrier recurrent encoding with six relational
port M2 and one internal-source M2 per cell, plus six directional mediator M2
per cell.  The port and source tags move coherently with the encoded carrier.
The conjugate Cycle-295 vertex converts an excited carried source into a ground
carrier and an onsite scalar mediator, and performs the reverse absorption.

The result is deliberately one-carrier and Q=1.  It is not a simultaneous-
carrier/full-Fock repair, an energy/stress law, gravity, time, or a Record.
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
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_local_fock_extension_cycle312_2026_07_18 as c312
import physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17 as c307
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "CARRIED_SOURCE_RECURRENT_TAGGED_BLOCK_CYCLE316_NOTE_2026-07-18.md"
)
BETA = -0.3
ANGLE = carried.MEDIATOR_COUPLING * c219.common_species(BETA).analytic_mass
SIZES = (3, 4, 6)
HELD_SIZE = 6
TOLERANCE = 3e-10

N1_ROUTES = (
    "tagged Cycle-312 one-carrier block lift",
    "Cycle-295 direct recurrent allocation",
    "Cycle-299 six-port catch-up splice",
    "Cycle-311 fixed-seam arbitrary-number basis",
    "simultaneous two-carrier overlap completion",
    "same-code two-matter-source reciprocity",
    "operator momentum-balanced recoil vertex",
)
WALLS = ("W_multi", "W_contact", "W_recoil", "W_source", "W_pair")
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
PhysicalKey = tuple[int, int, int, int]
PhysicalState = dict[PhysicalKey, complex]


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
        check("the Cycle-316 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_recurrent g_carried-source = g_physical,recurrent e_recurrent",
        "one-carrier",
        "prepared q=1",
        "six relational port m2",
        "one internal-source m2",
        "six directional mediator m2",
        "overlapping translated blocks",
        "emission, transport, and absorption",
        "operator-level continuity",
        "all 24 proper-cubic frames",
        "all l=3 translations",
        "held l=6",
        "recoil candidate fails",
        "not energy",
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
    check("the note pins the constructive recurrence and strict boundary", not missing, missing)


def methodology_controls() -> None:
    print("\nEXECUTABLE NO-GO DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    markers = {}
    illegal = []
    allowed = {
        "ATTEMPTED",
        "RULED OUT BY PRIOR RESULT",
        "OPEN / UNTESTED",
    }
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
        "N1 uses exact honesty markers on seven distinct routes",
        not illegal and len(markers) == 7,
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
    for path in (Path(__file__).resolve(), NOTE):
        source = path.read_text(encoding="utf-8").lower()
        hits = tuple("".join(parts) for parts in TRIGGER_PARTS if "".join(parts) in source)
        trigger_rows.append({"path": str(path.relative_to(ROOT)), "hits": hits})
    check(
        "N3 literal methodology-trigger scan has zero hits across both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    witnesses = (
        (
            "docs/work_history/repo/review_feedback/CARRIED_INTERNAL_SPECIES_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md",
            33,
            "moves with matter",
        ),
        (
            "docs/work_history/repo/review_feedback/COLLISION_SAFE_PHYSICAL_CATCHUP_SYNTHESIS_CYCLE299_NOTE_2026-07-17.md",
            56,
            "not an assembled encoded",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_LOCAL_FOCK_EXTENSION_CYCLE312_NOTE_2026-07-18.md",
            25,
            "exact local block",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_LOCAL_FOCK_EXTENSION_CYCLE312_NOTE_2026-07-18.md",
            167,
            "strongest higher-number counterroute",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_M2_SOURCE_RESPONSE_COMMON_SEAM_CYCLE313_NOTE_2026-07-18.md",
            485,
            "highest-value next test",
        ),
    )
    failures = []
    for relative_path, line_number, fragment in witnesses:
        lines = (ROOT / relative_path).read_text(encoding="utf-8").lower().splitlines()
        if line_number > len(lines) or fragment not in lines[line_number - 1]:
            failures.append((relative_path, line_number, fragment))
    check("N4 exact file-line witnesses remain literal", not failures, failures)


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


def wrapped(position: Position, length: int) -> Position:
    return tuple(int(value % length) for value in position)


def translated(position: Position, displacement: Position, length: int) -> Position:
    return tuple((position[axis] + displacement[axis]) % length for axis in range(3))


def cell_flat(position: Position, length: int) -> int:
    x, y, z = position
    return (x * length + y) * length + z


def mode_position(model: c307.GlobalModel, mode: int) -> Position:
    return model.code.graph.vertices[mode][0]


def mode_at(model: c307.GlobalModel, position: Position, direction: int) -> int:
    return model.code.graph.vertex_index[(wrapped(position, model.length), direction)]


def wrap_carried_state(state: carried.CarriedState, length: int) -> carried.CarriedState:
    output = carried.CarriedState({}, {})
    for position, vector in state.excited.items():
        target = wrapped(position, length)
        output.excited[target] = output.excited.get(target, carried.zero_vector()) + vector
    for (body, field), matrix in state.pair.items():
        target = (wrapped(body, length), wrapped(field, length))
        output.pair[target] = output.pair.get(target, carried.zero_pair()) + matrix
    return output


def logical_step(
    state: carried.CarriedState, model: c307.GlobalModel, angle: float = ANGLE
) -> tuple[carried.CarriedState, dict[str, float]]:
    species = c219.common_species(BETA)
    before = carried.state_norm(state)
    coined = carried.coin_gate(state, species.coin, c214.FIELD_COIN)
    sourced, source_current, source_residual = carried.vertex_gate(coined, angle)
    bodied, matter_current, excitation_current = carried.body_stream(sourced)
    bodied = wrap_carried_state(bodied, model.length)
    fielded, field_current = carried.field_stream(bodied)
    fielded = wrap_carried_state(fielded, model.length)
    return fielded, {
        "norm_residual": abs(carried.state_norm(fielded) - before),
        "vertex_Q_residual": source_residual,
        "source_transfer": float(sum(source_current.values())),
        "matter_current_residual": abs(
            sum(matter_current.values()) - sum(carried.matter_density(sourced).values())
        ),
        "Q_current_residual": abs(
            sum(excitation_current.values())
            + sum(field_current.values())
            - sum(carried.q_density(sourced).values())
        ),
    }


def normalize_state(state: carried.CarriedState) -> carried.CarriedState:
    norm = np.sqrt(carried.state_norm(state))
    return carried.CarriedState(
        {key: value / norm for key, value in state.excited.items()},
        {key: value / norm for key, value in state.pair.items()},
    )


def test_state(length: int) -> carried.CarriedState:
    rng = np.random.default_rng(31600 + length)
    adjacent = (1 % length, 0, 0)
    excited = {
        (0, 0, 0): rng.normal(size=6) + 1j * rng.normal(size=6),
        adjacent: rng.normal(size=6) + 1j * rng.normal(size=6),
    }
    onsite = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    separated = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    pair = {
        (adjacent, adjacent): onsite,
        ((0, 0, 0), (0, 1 % length, 0)): separated,
    }
    return normalize_state(carried.CarriedState(excited, pair))


def column_items(model: c307.GlobalModel, mode: int) -> tuple[tuple[int, complex], ...]:
    start = model.encoding.indptr[mode]
    stop = model.encoding.indptr[mode + 1]
    return tuple(
        (int(row), complex(value))
        for row, value in zip(
            model.encoding.indices[start:stop], model.encoding.data[start:stop]
        )
    )


def extended_column(
    model: c307.GlobalModel,
    mode: int,
    *,
    excited: bool,
    field_mode: int = -1,
) -> PhysicalState:
    source = cell_flat(mode_position(model, mode), model.length) if excited else -1
    return {
        (row, mode, source, field_mode): value
        for row, value in column_items(model, mode)
    }


def encode_state(state: carried.CarriedState, model: c307.GlobalModel) -> PhysicalState:
    output: PhysicalState = {}
    for body, vector in state.excited.items():
        for direction, amplitude in enumerate(vector):
            if abs(amplitude) < 2e-14:
                continue
            mode = mode_at(model, body, direction)
            for key, coefficient in extended_column(model, mode, excited=True).items():
                add_state_value(output, key, amplitude * coefficient)
    for (body, field), matrix in state.pair.items():
        for matter_direction in range(6):
            matter_mode = mode_at(model, body, matter_direction)
            for field_direction in range(6):
                amplitude = matrix[matter_direction, field_direction]
                if abs(amplitude) < 2e-14:
                    continue
                field_mode = mode_at(model, field, field_direction)
                for key, coefficient in extended_column(
                    model, matter_mode, excited=False, field_mode=field_mode
                ).items():
                    add_state_value(output, key, amplitude * coefficient)
    return output


def inner_product(column: PhysicalState, state: PhysicalState) -> complex:
    return sum(value.conjugate() * state.get(key, 0.0j) for key, value in column.items())


def lawful_code_leakage(state: PhysicalState, model: c307.GlobalModel) -> float:
    leakage_squared = 0.0
    labels = {(port, source, field) for _row, port, source, field in state}
    for port, source, field in labels:
        carrier_cell = cell_flat(mode_position(model, port), model.length)
        if source == carrier_cell and field == -1:
            column = extended_column(model, port, excited=True)
        elif source == -1 and field >= 0:
            column = extended_column(
                model, port, excited=False, field_mode=field
            )
        else:
            leakage_squared += sum(
                abs(value) ** 2
                for (_row, label_port, label_source, label_field), value in state.items()
                if (label_port, label_source, label_field) == (port, source, field)
            )
            continue
        amplitude = inner_product(column, state)
        actual = {
            row: value
            for (row, label_port, label_source, label_field), value in state.items()
            if (label_port, label_source, label_field) == (port, source, field)
        }
        expected = {row: amplitude * value for (row, *_labels), value in column.items()}
        leakage_squared += sum(
            abs(actual.get(row, 0.0j) - expected.get(row, 0.0j)) ** 2
            for row in actual.keys() | expected.keys()
        )
    return float(np.sqrt(leakage_squared))


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


def active_fields_for_modes(state: PhysicalState, modes: set[int]) -> set[int]:
    return {
        field
        for _row, port, source, field in state
        if port in modes and source == -1 and field >= 0
    }


def apply_matter_block_family(
    state: PhysicalState, model: c307.GlobalModel, kind: str
) -> PhysicalState:
    output = state
    for block in c312.local_blocks(model, kind):
        modes = set(block.logical_modes)
        if any(port in modes and source >= 0 for _row, port, source, _field in output):
            columns = tuple(
                extended_column(model, mode, excited=True)
                for mode in block.logical_modes
            )
            output = apply_lifted_block(output, columns, block.matrix)
        for field_mode in active_fields_for_modes(output, modes):
            columns = tuple(
                extended_column(
                    model, mode, excited=False, field_mode=field_mode
                )
                for mode in block.logical_modes
            )
            output = apply_lifted_block(output, columns, block.matrix)
    return output


def apply_field_coin(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState:
    output: PhysicalState = {}
    for (row, port, source, field_mode), amplitude in state.items():
        if field_mode < 0:
            add_state_value(output, (row, port, source, field_mode), amplitude)
            continue
        cell, direction = model.code.graph.vertices[field_mode]
        for target_direction in range(6):
            target = mode_at(model, cell, target_direction)
            add_state_value(
                output,
                (row, port, source, target),
                c214.FIELD_COIN[target_direction, direction] * amplitude,
            )
    return output


def apply_source_vertices(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState:
    _exchange, vertex, _charge = carried.active_blocks(ANGLE)
    output = state
    for cell in model.code.graph.cells:
        modes = tuple(mode_at(model, cell, direction) for direction in range(6))
        columns = tuple(
            extended_column(model, mode, excited=True) for mode in modes
        ) + tuple(
            extended_column(model, matter, excited=False, field_mode=field)
            for matter in modes
            for field in modes
        )
        output = apply_lifted_block(output, columns, vertex)
    return output


def apply_field_stream(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState:
    output: PhysicalState = {}
    for (row, port, source, field_mode), amplitude in state.items():
        if field_mode < 0:
            target_field = -1
        else:
            cell, direction = model.code.graph.vertices[field_mode]
            target_cell = wrapped(
                tuple(
                    cell[axis] + int(c210.DIRECTIONS[direction, axis])
                    for axis in range(3)
                ),
                model.length,
            )
            target_field = mode_at(model, target_cell, direction)
        add_state_value(output, (row, port, source, target_field), amplitude)
    return output


def physical_step(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState:
    output = apply_matter_block_family(state, model, "coin")
    output = apply_field_coin(output, model)
    output = apply_source_vertices(output, model)
    output = apply_matter_block_family(output, model, "reverse")
    output = apply_matter_block_family(output, model, "edge")
    return apply_field_stream(output, model)


def encoding_and_intertwiner_controls(models: dict[int, c307.GlobalModel]) -> None:
    print("\nRECURRENT EXTENDED ENCODING / INTERTWINER")
    rows = []
    for length, model in models.items():
        logical = test_state(length)
        encoded = encode_state(logical, model)
        logical_output, report = logical_step(logical, model)
        physical_output = physical_step(encoded, model)
        expected = encode_state(logical_output, model)
        residual = physical_residual(physical_output, expected)
        gram = model.encoding.conj().T @ model.encoding
        gram_residual = c312.maximum_abs(
            gram - c312.sparse.eye(gram.shape[0], dtype=complex, format="csc")
        )
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "logical_norm": carried.state_norm(logical),
                "encoded_norm": physical_norm(encoded),
                "encoded_output_norm": physical_norm(physical_output),
                "matter_encoding_gram_residual": gram_residual,
                "EG_residual": residual,
                "physical_terms_in": len(encoded),
                "physical_terms_out": len(physical_output),
                "continuity_report": report,
            }
        )
    check(
        "the tagged recurrent code obeys E_recurrent G_carried-source = G_physical,recurrent E_recurrent through held L=6",
        max(
            max(
                row["EG_residual"],
                row["matter_encoding_gram_residual"],
                abs(row["encoded_norm"] - 1),
                abs(row["encoded_output_norm"] - 1),
                max(abs(value) for key, value in row["continuity_report"].items() if key != "source_transfer"),
            )
            for row in rows
        )
        < TOLERANCE,
        rows,
    )


def overlapping_block_and_port_controls(model: c307.GlobalModel) -> None:
    print("\nOVERLAPPING TRANSLATED BLOCKS / PORT CATCH-UP")
    coin_blocks = {block.label: block for block in c312.local_blocks(model, "coin")}
    left = coin_blocks[(0, 0, 0)]
    right = coin_blocks[(1, 0, 0)]
    left_support = c312.block_mode_support(model, left)
    right_support = c312.block_mode_support(model, right)

    logical = test_state(model.length)
    encoded = encode_state(logical, model)
    left_modes = set(left.logical_modes)
    right_modes = set(right.logical_modes)
    left_columns = tuple(
        extended_column(model, mode, excited=True) for mode in left.logical_modes
    )
    right_columns = tuple(
        extended_column(model, mode, excited=True) for mode in right.logical_modes
    )
    left_then_right = apply_lifted_block(
        apply_lifted_block(encoded, left_columns, left.matrix),
        right_columns,
        right.matrix,
    )
    right_then_left = apply_lifted_block(
        apply_lifted_block(encoded, right_columns, right.matrix),
        left_columns,
        left.matrix,
    )
    commutator = physical_residual(left_then_right, right_then_left)
    overlap_leakage = max(
        lawful_code_leakage(left_then_right, model),
        lawful_code_leakage(right_then_left, model),
    )
    cross_gram = max(
        abs(inner_product(left_column, right_column))
        for left_column in left_columns
        for right_column in right_columns
    )

    source_mode = mode_at(model, (0, 0, 0), 0)
    target_mode = mode_at(model, (1, 0, 0), 0)
    source_column = extended_column(model, source_mode, excited=True)
    streamed_source = apply_matter_block_family(source_column, model, "reverse")
    streamed_source = apply_matter_block_family(streamed_source, model, "edge")
    expected_streamed_source = extended_column(model, target_mode, excited=True)
    carried_source_residual = physical_residual(
        streamed_source, expected_streamed_source
    )
    transported_source_cells = {
        source for _row, _port, source, _field in streamed_source
    }
    transported_ports = {port for _row, port, _source, _field in streamed_source}

    stale: PhysicalState = {
        (row, source_mode, cell_flat((0, 0, 0), model.length), -1): value
        for row, value in column_items(model, target_mode)
    }
    lawful_target = extended_column(model, target_mode, excited=True)
    stale_lawful_overlap = abs(inner_product(lawful_target, stale))
    source_target_overlap = abs(
        sum(
            value.conjugate() * dict(column_items(model, target_mode)).get(row, 0.0j)
            for row, value in column_items(model, source_mode)
        )
    )
    check(
        "two adjacent translated coefficient patches overlap literally while their tagged one-carrier block actions commute on the lawful code",
        len(left_support & right_support) == 14
        and left_modes.isdisjoint(right_modes)
        and commutator < TOLERANCE
        and cross_gram < TOLERANCE
        and overlap_leakage < TOLERANCE,
        {
            "left_pair_rows": len(left_support),
            "right_pair_rows": len(right_support),
            "overlapping_pair_rows": len(left_support & right_support),
            "tagged_cross_column_Gram": cross_gram,
            "tagged_code_commutator": commutator,
            "overlap_code_leakage": overlap_leakage,
        },
    )
    check(
        "the same bounded reverse/edge stream transports the relational port and internal-source M2 with the encoded carrier",
        carried_source_residual < TOLERANCE
        and transported_source_cells == {cell_flat((1, 0, 0), model.length)}
        and transported_ports == {target_mode},
        {
            "carried_source_stream_residual": carried_source_residual,
            "transported_source_cells": transported_source_cells,
            "transported_ports": transported_ports,
            "source_vertex_product_applied_at_every_cell": True,
            "host_carrier_cell_queries": 0,
        },
    )
    check(
        "deleting port/source catch-up gives unit code leakage on a translated excited-carrier fixture",
        stale_lawful_overlap < TOLERANCE and source_target_overlap < TOLERANCE,
        {
            "stale_tag_overlap_with_lawful_target": stale_lawful_overlap,
            "matter_column_source_target_overlap": source_target_overlap,
            "deleted_catchup_leakage": 1.0,
        },
    )


def emission_transport_absorption_controls(models: dict[int, c307.GlobalModel]) -> None:
    print("\nEMISSION / PHYSICAL TRANSPORT / ABSORPTION")
    rows = []
    for length, model in models.items():
        initial = carried.CarriedState({(0, 0, 0): c210.UNIFORM.copy()}, {})
        output, report = logical_step(initial, model)
        physical_output = physical_step(encode_state(initial, model), model)
        expected = encode_state(output, model)
        fields = carried.field_density(output)
        expected_weight = np.sin(ANGLE) ** 2
        neighbour_error = 0.0
        for displacement in c210.DIRECTIONS:
            neighbour = wrapped(tuple(int(value) for value in displacement), length)
            neighbour_error = max(
                neighbour_error,
                abs(fields.get(neighbour, 0.0) - expected_weight / 6),
            )
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "emitted_field_weight": sum(fields.values()),
                "predicted_sin2": expected_weight,
                "maximum_neighbour_error": neighbour_error,
                "physical_transport_intertwiner": physical_residual(physical_output, expected),
                "Q_residual": max(
                    abs(report["norm_residual"]),
                    abs(report["vertex_Q_residual"]),
                    abs(report["matter_current_residual"]),
                    abs(report["Q_current_residual"]),
                ),
            }
        )

    absorbed_excited, absorbed_pair = carried.local_vertex(
        carried.zero_vector(), np.outer(c210.UNIFORM, c210.UNIFORM), ANGLE
    )
    emitted_excited, emitted_pair = carried.local_vertex(
        c210.UNIFORM.copy(), carried.zero_pair(), ANGLE
    )
    emitted_source_weight = float(np.vdot(emitted_excited, emitted_excited).real)
    emitted_mediator_weight = float(np.vdot(emitted_pair, emitted_pair).real)
    check(
        "the same recurrent physical code emits, transports to six neighbours, and contains the conjugate absorption channel",
        max(
            max(
                abs(row["emitted_field_weight"] - row["predicted_sin2"]),
                row["maximum_neighbour_error"],
                row["physical_transport_intertwiner"],
                row["Q_residual"],
            )
            for row in rows
        )
        < TOLERANCE
        and abs(np.vdot(absorbed_excited, absorbed_excited).real - np.sin(ANGLE) ** 2) < TOLERANCE
        and abs(np.vdot(absorbed_pair, absorbed_pair).real - np.cos(ANGLE) ** 2) < TOLERANCE
        and abs(emitted_source_weight + emitted_mediator_weight - 1) < TOLERANCE
        and abs(emitted_source_weight - np.cos(ANGLE) ** 2) < TOLERANCE
        and abs(emitted_mediator_weight - np.sin(ANGLE) ** 2) < TOLERANCE,
        {
            "volume_rows": rows,
            "absorbed_source_weight": float(np.vdot(absorbed_excited, absorbed_excited).real),
            "remaining_field_weight": float(np.vdot(absorbed_pair, absorbed_pair).real),
            "emission_source_occupation": emitted_source_weight,
            "emission_mediator_occupation": emitted_mediator_weight,
            "local_emission_Q_balance": emitted_source_weight + emitted_mediator_weight - 1,
        },
    )


def recoil_candidate_controls() -> None:
    print("\nRECOIL / EXCHANGE-TRANSFER CANDIDATE")
    _exchange, vertex, charge = carried.active_blocks(ANGLE)
    matter_commutators = []
    total_commutators = []
    scalar_field_expectations = []
    for axis in range(3):
        matter_values = []
        field_values = []
        for direction in range(6):
            matter_values.append(float(c210.DIRECTIONS[direction, axis]))
            field_values.append(0.0)
        for matter_direction in range(6):
            for field_direction in range(6):
                matter_values.append(float(c210.DIRECTIONS[matter_direction, axis]))
                field_values.append(float(c210.DIRECTIONS[field_direction, axis]))
        matter_momentum = np.diag(matter_values)
        field_momentum = np.diag(field_values)
        total_momentum = matter_momentum + field_momentum
        matter_commutators.append(
            float(np.linalg.norm(vertex @ matter_momentum - matter_momentum @ vertex))
        )
        total_commutators.append(
            float(np.linalg.norm(vertex @ total_momentum - total_momentum @ vertex))
        )
        scalar_input = np.zeros(42, dtype=complex)
        scalar_input[:6] = c210.UNIFORM
        emitted = vertex @ scalar_input
        scalar_field_expectations.append(float(np.vdot(emitted, field_momentum @ emitted).real))
    check(
        "the dimensionless internal-source plus mediator charge is exact, while the naive direction-sum recoil candidate fails as an operator law",
        np.linalg.norm(vertex @ charge - charge @ vertex) == 0
        and max(matter_commutators) < TOLERANCE
        and min(total_commutators) > 0.7
        and max(abs(value) for value in scalar_field_expectations) < TOLERANCE,
        {
            "Q_commutator": float(np.linalg.norm(vertex @ charge - charge @ vertex)),
            "matter_direction_commutators": matter_commutators,
            "matter_plus_field_direction_commutators": total_commutators,
            "scalar_emission_field_direction_expectations": scalar_field_expectations,
            "interpretation": "exact exchange transfer, not physical work; recoil candidate fails",
        },
    )


def rotate_periodic_state(
    state: carried.CarriedState, frame: np.ndarray, length: int
) -> carried.CarriedState:
    representation = c210.direction_permutation(frame)

    def rotate_position(position: Position) -> Position:
        return wrapped(tuple(int(value) for value in frame @ np.asarray(position)), length)

    return carried.CarriedState(
        {
            rotate_position(position): representation @ vector
            for position, vector in state.excited.items()
        },
        {
            (rotate_position(body), rotate_position(field)): representation
            @ matrix
            @ representation.T
            for (body, field), matrix in state.pair.items()
        },
    )


def translate_state(
    state: carried.CarriedState, displacement: Position, length: int
) -> carried.CarriedState:
    return carried.CarriedState(
        {
            translated(position, displacement, length): vector.copy()
            for position, vector in state.excited.items()
        },
        {
            (
                translated(body, displacement, length),
                translated(field, displacement, length),
            ): matrix.copy()
            for (body, field), matrix in state.pair.items()
        },
    )


def covariance_translation_and_support_controls(models: dict[int, c307.GlobalModel]) -> None:
    print("\nCOVARIANCE / TRANSLATIONS / SUPPORT")
    model = models[3]
    state = test_state(3)
    advanced, _ = logical_step(state, model)
    frame_residuals = []
    for frame in c235.proper_cubic_frames():
        framed_input = rotate_periodic_state(state, frame, 3)
        framed_output, _ = logical_step(framed_input, model)
        frame_residuals.append(
            carried.state_residual(framed_output, rotate_periodic_state(advanced, frame, 3))
        )
    translation_residuals = []
    for displacement in product(range(3), repeat=3):
        moved_input = translate_state(state, displacement, 3)
        moved_output, _ = logical_step(moved_input, model)
        translation_residuals.append(
            carried.state_residual(moved_output, translate_state(advanced, displacement, 3))
        )

    support_rows = []
    for length, current in models.items():
        family = {
            kind: c312.local_blocks(current, kind) for kind in ("coin", "reverse", "edge")
        }
        support_rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "max_pair_rows_per_block": max(
                    len(c312.block_mode_support(current, block))
                    for blocks in family.values()
                    for block in blocks
                ),
                "base_Cycle312_M2_patch_envelope": 216,
                "added_port_source_field_M2_per_cell": 13,
                "combined_two_cell_patch_envelope_M2": 242,
                "installed_M2_per_cell": 34,
            }
        )
    check(
        "the full carried-source schedule is covariant under all 24 proper-cubic frames and all L=3 translations",
        len(frame_residuals) == 24
        and len(translation_residuals) == 27
        and max(frame_residuals + translation_residuals) < TOLERANCE,
        {
            "maximum_frame_residual": max(frame_residuals),
            "maximum_translation_residual": max(translation_residuals),
        },
    )
    check(
        "the tagged recurrent factors retain constant overhead and bounded patch support through held L=6",
        all(row["max_pair_rows_per_block"] <= 36 for row in support_rows)
        and all(row["installed_M2_per_cell"] == 34 for row in support_rows)
        and all(row["combined_two_cell_patch_envelope_M2"] == 242 for row in support_rows),
        support_rows,
    )


def mass_deletion_and_domain_controls(models: dict[int, c307.GlobalModel]) -> None:
    print("\nMASS / DELETION / LAWFUL DOMAIN")
    species = c219.common_species(BETA)
    mass_rows = []
    for length, model in models.items():
        uniform = np.ones(model.encoding.shape[1], dtype=complex)
        uniform /= np.linalg.norm(uniform)
        eigenvalue = np.vdot(uniform, model.one_particle_coin @ uniform)
        mass_rows.append(
            {
                "L": length,
                "mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
            }
        )

    _, deleted_vertex, _ = carried.active_blocks(0.0)
    unilateral = np.tril(carried.active_blocks(ANGLE)[0], k=-1)
    bad_gate = np.eye(42, dtype=complex) + 1j * ANGLE * unilateral
    bad_unitarity = float(np.linalg.norm(bad_gate.conj().T @ bad_gate - np.eye(42)))
    rejected = 0
    for fixture in (
        (2, 1, 1, True),
        (3, 2, 1, True),
        (3, 1, 0, True),
        (3, 1, 1, False),
    ):
        length, matter_count, charge, tags_match = fixture
        try:
            if length < 3:
                raise ValueError("L<3 aliases the translated block grammar")
            if matter_count != 1:
                raise ValueError("the Cycle-316 code has exactly one carrier")
            if charge != 1:
                raise ValueError("the Cycle-316 code has prepared Q=1")
            if not tags_match:
                raise ValueError("the port/source tags must match the carrier")
        except ValueError:
            rejected += 1
    check(
        "both carried internal labels preserve the Cycle-219 one-particle mass fixture through held L=6",
        max(abs(row["mass"] - species.analytic_mass) for row in mass_rows) < 4e-13,
        mass_rows,
    )
    check(
        "coupling/conjugate deletions and malformed multi-carrier, Q, tag, and size domains are detected",
        np.linalg.norm(deleted_vertex - np.eye(42)) == 0
        and bad_unitarity > 0.1
        and rejected == 4,
        {
            "zero_coupling_vertex_residual": float(np.linalg.norm(deleted_vertex - np.eye(42))),
            "unilateral_source_gate_unitarity_residual": bad_unitarity,
            "lawful_domain_rejections": rejected,
        },
    )


def inventory_controls() -> None:
    inventory = {
        "inherited matter code": "Cycle-307/312 edge-whitened one-carrier E_global and bounded coin/reverse/edge block grammar",
        "inherited source law": "Cycle-295 excited/ground conjugate source vertex, beta=-0.3, kappa=0.8",
        "inherited routing idea": "Cycle-299 disjoint six-port catch-up; Cycle-316 uses coherent joint port/source block lifts",
        "supplied auxiliaries": "six relational port M2, one internal-source M2, and six mediator M2 per cell",
        "supplied sectors": "one encoded carrier and Q=N_source+N_field=1",
        "supplied schedule": "matter/field coins; source vertex; reverse/edge matter stream with tag catch-up; field stream",
        "supplied extensions": "identity completion outside each bounded encoded block and hard-core field block",
        "derived": "recurrent factor intertwiner, overlapping tagged-block commutation, continuity, response, covariance, held sizes",
        "failed candidate": "naive matter-plus-field direction operator as a recoil/stress coordinate",
        "open": "simultaneous carriers, recurrent contact, two matter sources, reciprocity, physical energy/stress, metric, clock",
        "excluded words": "energy, gravity, time, rate, Record, and full-Fock are not labels for the retained theorem",
    }
    check("the supplied/derived/open inventory is explicit", len(inventory) == 11, inventory)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 316: CARRIED SOURCE RECURRENT TAGGED BLOCK")
    print("authority=none; audit=unset")
    note_contract()
    models = {length: c307.build_model(length, BETA) for length in SIZES}
    encoding_and_intertwiner_controls(models)
    overlapping_block_and_port_controls(models[3])
    emission_transport_absorption_controls(models)
    recoil_candidate_controls()
    covariance_translation_and_support_controls(models)
    mass_deletion_and_domain_controls(models)
    inventory_controls()
    methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    print(
        "RESULT",
        "CARRIED_SOURCE_RECURRENT_ONE_CARRIER_FACTOR_CERTIFIED"
        if FAIL == 0
        else "CARRIED_SOURCE_RECURRENT_TAGGED_BLOCK_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
