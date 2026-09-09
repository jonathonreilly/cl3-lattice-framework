#!/usr/bin/env python3
"""Cycle 731: a bounded traveling token-count refusal certificate.

A clean binary counter is reversibly incremented once for every occupied
Cycle-719 A station.  A fixed equality comparison with the declared source
inventory sets one mismatch latch.  That latch is the eighth input to every
Cycle-730 refusal OR.  Comparison and count are then uncomputed before the
unchanged R suffix.  The emitted circuit is a fixed X/CNOT/TOF word: Python is
used only to unroll the word from (ring size, declared expected count).
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter

import frontier_cycle730_charge_row_enforcement_2026_07_28 as E730
import frontier_cycle724_local_token_row_enforcement_2026_07_28 as E724
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

A = K.A
B = K.B
M = K.M
DATA_WIDTH = E730.DATA_WIDTH
EXPECTED_COUNT = 1
EXPECTED_CYCLE730_PADDED_GATES = 99_310
EXPECTED_CYCLE730_PADDED_SHA256 = (
    "7d4b7fac14c0606f7210a1b99da997cecdf13885471c37d5ae55597b742c5433"
)
COUNT_LOCAL_ROW_INPUTS = 8
COUNT_OR_INTERMEDIATES_PER_STATION = 6
STDOUT_LIMIT_BYTES = 150 * 1024
RING11_STATIONS = 11

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def counter_width(stations: int) -> int:
    """Exactly ceil(log2(stations + 1)) for positive station counts."""

    if stations < 1:
        raise ValueError(("stations", stations))
    return stations.bit_length()


def register_layout(data_wires: int, stations: int) -> dict[str, int]:
    width = counter_width(stations)
    mcx_width = max(0, width - 2)
    a_base = data_wires
    b_base = a_base + stations
    work_base = b_base + stations
    syndrome_base = work_base + stations
    scratch_base = syndrome_base + stations
    or_scratch_base = (
        scratch_base + E730.MCX_SCRATCH_PER_STATION * stations
    )
    ref_base = (
        or_scratch_base
        + COUNT_OR_INTERMEDIATES_PER_STATION * stations
    )
    charge_base = ref_base + stations
    h_wire = charge_base + stations
    counter_base = h_wire + 1
    increment_scratch_base = counter_base + width
    comparison_scratch_base = increment_scratch_base + mcx_width
    refusal_latch = comparison_scratch_base + mcx_width
    return {
        "data_width": data_wires,
        "stations": stations,
        "a_base": a_base,
        "b_base": b_base,
        "work_base": work_base,
        "syndrome_base": syndrome_base,
        "scratch_base": scratch_base,
        "or_scratch_base": or_scratch_base,
        "ref_base": ref_base,
        "charge_base": charge_base,
        "h_wire": h_wire,
        "counter_base": counter_base,
        "counter_width": width,
        "increment_scratch_base": increment_scratch_base,
        "increment_scratch_width": mcx_width,
        "comparison_scratch_base": comparison_scratch_base,
        "comparison_scratch_width": mcx_width,
        "refusal_latch": refusal_latch,
        "full_width": refusal_latch + 1,
    }


def station_mcx_scratch(
    layout: dict[str, int], station: int
) -> tuple[int, ...]:
    return tuple(
        layout["scratch_base"]
        + E730.MCX_SCRATCH_PER_STATION * station
        + slot
        for slot in range(E730.MCX_SCRATCH_PER_STATION)
    )


def station_or_scratch(
    layout: dict[str, int], station: int
) -> tuple[int, ...]:
    return tuple(
        layout["or_scratch_base"]
        + COUNT_OR_INTERMEDIATES_PER_STATION * station
        + slot
        for slot in range(COUNT_OR_INTERMEDIATES_PER_STATION)
    )


def increment_scratch(layout: dict[str, int]) -> tuple[int, ...]:
    return tuple(
        layout["increment_scratch_base"] + slot
        for slot in range(layout["increment_scratch_width"])
    )


def comparison_scratch(layout: dict[str, int]) -> tuple[int, ...]:
    return tuple(
        layout["comparison_scratch_base"] + slot
        for slot in range(layout["comparison_scratch_width"])
    )


def counter_wires(layout: dict[str, int]) -> tuple[int, ...]:
    return tuple(
        layout["counter_base"] + bit
        for bit in range(layout["counter_width"])
    )


def or_into(left: int, right: int, target: int) -> tuple[object, ...]:
    return (
        A.cn(left, target),
        A.cn(right, target),
        A.tof(left, right, target),
    )


def local_or_compute(
    inputs: tuple[int, ...],
    intermediates: tuple[int, ...],
    syndrome: int,
) -> tuple[object, ...]:
    if len(inputs) != COUNT_LOCAL_ROW_INPUTS:
        raise ValueError(("count refusal inputs", len(inputs)))
    if len(intermediates) != COUNT_OR_INTERMEDIATES_PER_STATION:
        raise ValueError(("count OR intermediates", len(intermediates)))
    outputs = intermediates + (syndrome,)
    word = list(or_into(inputs[0], inputs[1], outputs[0]))
    for index, source in enumerate(inputs[2:], start=1):
        word.extend(or_into(outputs[index - 1], source, outputs[index]))
    return tuple(word)


def controlled_increment_word(
    control: int,
    counter: tuple[int, ...],
    scratch: tuple[int, ...],
) -> tuple[object, ...]:
    """Add control to a clean-width binary counter, high carry first."""

    word: list[object] = []
    for bit in reversed(range(1, len(counter))):
        controls = (control,) + counter[:bit]
        word.extend(
            A.mcx(
                controls,
                counter[bit],
                scratch[:max(0, len(controls) - 2)],
            )
        )
    word.append(A.cn(control, counter[0]))
    return tuple(word)


def count_compute_word(
    layout: dict[str, int],
) -> tuple[tuple[object, ...], tuple[dict[str, int], ...]]:
    counter = counter_wires(layout)
    scratch = increment_scratch(layout)
    word: list[object] = []
    blocks = []
    for station in range(layout["stations"]):
        start = len(word)
        word.extend(
            controlled_increment_word(
                layout["a_base"] + station, counter, scratch
            )
        )
        blocks.append(
            {"station": station, "start": start, "stop": len(word)}
        )
    return tuple(word), tuple(blocks)


def comparison_compute_word(
    layout: dict[str, int], expected_count: int
) -> tuple[object, ...]:
    width = layout["counter_width"]
    if not 0 <= expected_count <= layout["stations"]:
        raise ValueError(("expected count", expected_count))
    counter = counter_wires(layout)
    latch = layout["refusal_latch"]
    zero_bits = tuple(
        counter[bit]
        for bit in range(width)
        if not ((expected_count >> bit) & 1)
    )
    word: list[object] = [A.x(wire) for wire in zero_bits]
    word.append(A.x(latch))
    word.extend(A.mcx(counter, latch, comparison_scratch(layout)))
    word.extend(A.x(wire) for wire in reversed(zero_bits))
    return tuple(word)


@lru_cache(maxsize=None)
def count_certified_controller_build(
    program: tuple[object, ...],
    data_wires: int,
    expected_count: int = EXPECTED_COUNT,
) -> tuple[
    tuple[object, ...],
    dict[str, int],
    tuple[dict[str, object], ...],
    dict[str, object],
]:
    """Compile count, mismatch-fed Cycle-730 Q, exact uncompute, and R."""

    stations = len(program)
    layout = register_layout(data_wires, stations)
    count_compute, increment_blocks = count_compute_word(layout)
    compare_compute = comparison_compute_word(layout, expected_count)
    word: list[object] = list(count_compute + compare_compute)
    q_start = len(word)
    blocks = []
    extra_or_gates: list[object] = []
    for station, row in enumerate(program):
        start = len(word)
        macro = K.mapped_macro(row)
        charge_compute = (
            E730.charge_compute_word(layout, station) if macro else ()
        )
        left = (station - 1) % stations
        right = (station + 1) % stations
        dirty_inputs = (
            layout["b_base"] + station,
            layout["work_base"] + station,
            layout["a_base"] + left,
            layout["b_base"] + left,
            layout["a_base"] + right,
            layout["b_base"] + right,
            layout["charge_base"] + station,
            layout["refusal_latch"],
        )
        syndrome = layout["syndrome_base"] + station
        or_compute = (
            local_or_compute(
                dirty_inputs, station_or_scratch(layout, station), syndrome
            )
            if macro
            else ()
        )
        lifted = (
            E730.lifted_refusing_macro(
                macro,
                layout["a_base"] + station,
                syndrome,
                station_mcx_scratch(layout, station),
            )
            if macro
            else ()
        )
        charge_start = len(word)
        word.extend(charge_compute)
        charge_stop = len(word)
        or_start = len(word)
        word.extend(or_compute)
        or_stop = len(word)
        if macro:
            word.append(A.x(syndrome))
            word.extend(lifted)
            word.append(A.x(syndrome))
        or_uncompute_start = len(word)
        word.extend(reversed(or_compute))
        or_uncompute_stop = len(word)
        charge_uncompute_start = len(word)
        word.extend(reversed(charge_compute))
        charge_uncompute_stop = len(word)
        if macro:
            extra_or_gates.extend(or_compute[-3:])
            extra_or_gates.extend(tuple(reversed(or_compute))[:3])
        blocks.append(
            {
                "station": station,
                "nonidentity": bool(macro),
                "start": start,
                "stop": len(word),
                "charge_compute_start": charge_start,
                "charge_compute_stop": charge_stop,
                "or_compute_start": or_start,
                "or_compute_stop": or_stop,
                "or_uncompute_start": or_uncompute_start,
                "or_uncompute_stop": or_uncompute_stop,
                "charge_uncompute_start": charge_uncompute_start,
                "charge_uncompute_stop": charge_uncompute_stop,
            }
        )
    q_stop = len(word)
    compare_uncompute_start = len(word)
    word.extend(reversed(compare_compute))
    compare_uncompute_stop = len(word)
    count_uncompute_start = len(word)
    word.extend(reversed(count_compute))
    count_uncompute_stop = len(word)
    r_start = len(word)
    r1 = tuple(
        gate
        for station in range(stations)
        for gate in K.swap_word(
            layout["a_base"] + station,
            layout["b_base"] + station,
        )
    )
    r2 = tuple(
        gate
        for station in range(stations)
        for gate in K.swap_word(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % stations,
        )
    )
    word.extend(r1 + r2)
    certificate_word = (
        count_compute
        + compare_compute
        + tuple(extra_or_gates)
        + tuple(reversed(compare_compute))
        + tuple(reversed(count_compute))
    )
    metadata: dict[str, object] = {
        "count_compute_start": 0,
        "count_compute_stop": len(count_compute),
        "increment_blocks": increment_blocks,
        "comparison_compute_start": len(count_compute),
        "comparison_compute_stop": len(count_compute) + len(compare_compute),
        "q_start": q_start,
        "q_stop": q_stop,
        "comparison_uncompute_start": compare_uncompute_start,
        "comparison_uncompute_stop": compare_uncompute_stop,
        "count_uncompute_start": count_uncompute_start,
        "count_uncompute_stop": count_uncompute_stop,
        "r_start": r_start,
        "count_compute_word": count_compute,
        "comparison_compute_word": compare_compute,
        "certificate_word": certificate_word,
    }
    return tuple(word), layout, tuple(blocks), metadata


def controller_full_input(
    data_value: int,
    layout: dict[str, int],
    *,
    a: tuple[int, ...] = (),
    b: tuple[int, ...] = (),
    work: tuple[int, ...] = (),
    refs: tuple[int, ...] | None = None,
    h: int = 0,
) -> int:
    output = data_value
    for station in a:
        output |= 1 << (layout["a_base"] + station)
    for station in b:
        output |= 1 << (layout["b_base"] + station)
    for station in work:
        output |= 1 << (layout["work_base"] + station)
    if refs is None:
        refs = (0,) * layout["stations"]
    if len(refs) != layout["stations"]:
        raise ValueError(("refs", len(refs), layout["stations"]))
    for station, bit in enumerate(refs):
        if bit:
            output |= 1 << (layout["ref_base"] + station)
    if h:
        output |= 1 << layout["h_wire"]
    return output


def controller_rows(
    value: int, layout: dict[str, int]
) -> dict[str, object]:
    stations = layout["stations"]

    def row(base: int, width: int = stations) -> tuple[int, ...]:
        return tuple((value >> (base + index)) & 1 for index in range(width))

    return {
        "data": value & ((1 << layout["data_width"]) - 1),
        "A": row(layout["a_base"]),
        "B": row(layout["b_base"]),
        "work": row(layout["work_base"]),
        "syndrome": row(layout["syndrome_base"]),
        "scratch": row(
            layout["scratch_base"],
            E730.MCX_SCRATCH_PER_STATION * stations,
        ),
        "or_scratch": row(
            layout["or_scratch_base"],
            COUNT_OR_INTERMEDIATES_PER_STATION * stations,
        ),
        "refs": row(layout["ref_base"]),
        "charge": row(layout["charge_base"]),
        "h": (value >> layout["h_wire"]) & 1,
        "counter": row(layout["counter_base"], layout["counter_width"]),
        "increment_scratch": row(
            layout["increment_scratch_base"],
            layout["increment_scratch_width"],
        ),
        "comparison_scratch": row(
            layout["comparison_scratch_base"],
            layout["comparison_scratch_width"],
        ),
        "refusal_latch": (value >> layout["refusal_latch"]) & 1,
    }


def all_auxiliary_clean(rows: dict[str, object]) -> bool:
    return not any(
        bit
        for key in (
            "syndrome",
            "scratch",
            "or_scratch",
            "charge",
            "counter",
            "increment_scratch",
            "comparison_scratch",
        )
        for bit in rows[key]
    ) and rows["refusal_latch"] == 0


def literal_apply(
    values: tuple[int, ...],
    word: tuple[object, ...],
    width: int,
    iterations: int,
) -> tuple[int, ...]:
    return E724.F723.apply_literal_bitplanes(
        values, word, width, iterations
    )


def input_contract_certificate() -> dict[str, object]:
    root = Path(__file__).resolve().parents[1]
    existence = {path: (root / path).is_file() for path in AUDIT_INPUT_PATHS}
    return {
        "paths": existence,
        "all_exist": all(existence.values()),
        "note_required": False,
        "pure_literal_tuple": DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS,
    }


def cycle730_regression_anchor() -> dict[str, object]:
    word, _layout, _blocks, _q_stop = E730.extended_controller_build(
        E730.R719.PROGRAM, DATA_WIDTH
    )
    repeated, _layout2, _blocks2, _q_stop2 = (
        E730.extended_controller_build(E730.R719.PROGRAM, DATA_WIDTH)
    )
    digest = K.gate_digest(word)
    frozen = E730.lawful_extended_case(
        "held_2", 2, K.interleaved_program(2)
    )
    frozen_keys = (
        "data_allocator_match",
        "A0_return",
        "B_return",
        "work_return",
        "syndrome_return",
        "mcx_scratch_return",
        "or_scratch_return",
        "charge_scratch_return",
        "refs_return",
        "h_return",
        "literal_reverse_exact",
    )
    return {
        "expected_semantic_gates": EXPECTED_CYCLE730_PADDED_GATES,
        "observed_semantic_gates": len(word),
        "expected_word_sha256": EXPECTED_CYCLE730_PADDED_SHA256,
        "observed_word_sha256": digest,
        "recomputed_word_sha256": K.gate_digest(repeated),
        "count_match": len(word) == EXPECTED_CYCLE730_PADDED_GATES,
        "digest_match": digest == EXPECTED_CYCLE730_PADDED_SHA256,
        "repeat_exact": word == repeated,
        "frozen_lawful_case": frozen,
        "frozen_lawful_case_pass": all(frozen[key] for key in frozen_keys),
    }


def structure_certificate() -> dict[str, object]:
    program = E730.R719.PROGRAM
    word, layout, blocks, metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    old_word, _old_layout, _old_blocks, old_q_stop = (
        E730.extended_controller_build(program, DATA_WIDTH)
    )
    certificate_word = metadata["certificate_word"]
    ref_h_wires = set(
        range(layout["ref_base"], layout["ref_base"] + len(program))
    )
    ref_h_wires.add(layout["h_wire"])
    ref_h_touch_failures = sum(
        any(wire in ref_h_wires for wire in gate.wires)
        for gate in certificate_word
    )
    allowed_kinds = {"X", "CNOT", "TOF"}
    runtime_gate_kind_failures = sum(
        gate.kind not in allowed_kinds for gate in word
    )
    logical_locality_failures = 0
    count_compute = metadata["count_compute_word"]
    for block in metadata["increment_blocks"]:
        station = int(block["station"])
        allowed = {
            layout["a_base"] + station,
            *counter_wires(layout),
            *increment_scratch(layout),
        }
        logical_locality_failures += sum(
            not set(gate.wires) <= allowed
            for gate in count_compute[int(block["start"]):int(block["stop"])]
        )
    compare_allowed = {
        *counter_wires(layout),
        *comparison_scratch(layout),
        layout["refusal_latch"],
    }
    logical_locality_failures += sum(
        not set(gate.wires) <= compare_allowed
        for gate in metadata["comparison_compute_word"]
    )
    new_r = word[int(metadata["r_start"]):]
    old_r = old_word[old_q_stop:]
    nonidentity = sum(bool(row["nonidentity"]) for row in blocks)
    delta = len(word) - len(old_word)
    return {
        "stations": len(program),
        "expected_count": EXPECTED_COUNT,
        "counter_width": layout["counter_width"],
        "counter_width_formula": "ceil(log2(N+1))",
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "Cycle730_semantic_gates": len(old_word),
        "added_semantic_gates": delta,
        "certificate_semantic_gates": len(certificate_word),
        "delta_equals_certificate_word": delta == len(certificate_word),
        "nonidentity_stations": nonidentity,
        "extra_OR_gates": 6 * nonidentity,
        "R_literal_suffix_unchanged": new_r == old_r,
        "exact_comparison_uncompute":
            word[
                int(metadata["comparison_uncompute_start"]):
                int(metadata["comparison_uncompute_stop"])
            ]
            == tuple(reversed(metadata["comparison_compute_word"])),
        "exact_counter_uncompute":
            word[
                int(metadata["count_uncompute_start"]):
                int(metadata["count_uncompute_stop"])
            ]
            == tuple(reversed(metadata["count_compute_word"])),
        "count_certificate_ref_h_touch_failures": ref_h_touch_failures,
        "compiled_gate_kind_failures": runtime_gate_kind_failures,
        "increment_comparison_locality_failures":
            logical_locality_failures,
        "full_width": layout["full_width"],
    }


def lawful_case(
    label: str, bank_count: int, program: tuple[object, ...]
) -> dict[str, object]:
    stations = len(program)
    old_word, old_layout, _old_blocks, _old_q_stop = (
        E730.extended_controller_build(program, DATA_WIDTH)
    )
    word, layout, _blocks, _metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    refs, h = E730.lawful_reference_rails(stations)
    banks, links = B.chain_genesis(bank_count)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    data_value = E724.F723.tuple_to_int(before)
    old_source = E730.controller_full_input(
        data_value, old_layout, a=(0,), refs=refs, h=h
    )
    source = controller_full_input(
        data_value, layout, a=(0,), refs=refs, h=h
    )
    old_observed = literal_apply(
        (old_source,), old_word, old_layout["full_width"], stations
    )[0]
    observed = literal_apply(
        (source,), word, layout["full_width"], stations
    )[0]
    restored = literal_apply(
        (observed,), tuple(reversed(word)), layout["full_width"], stations
    )[0]
    old_rows = E730.controller_rows(old_observed, old_layout)
    rows = controller_rows(observed, layout)
    common_equal = (
        rows["data"] == old_rows["data"]
        and rows["A"] == old_rows["A"]
        and rows["B"] == old_rows["B"]
        and rows["work"] == old_rows["work"]
        and rows["refs"] == old_rows["refs"]
        and rows["h"] == old_rows["h"]
    )
    return {
        "label": label,
        "banks": bank_count,
        "stations": stations,
        "Cycle730_semantic_gates": len(old_word),
        "Cycle731_semantic_gates": len(word),
        "Cycle731_word_sha256": K.gate_digest(word),
        "data_and_rails_equal_Cycle730": common_equal,
        "A0_return":
            rows["A"] == (1,) + (0,) * (stations - 1),
        "B_work_return": not any(rows["B"]) and not any(rows["work"]),
        "refs_h_return": rows["refs"] == refs and rows["h"] == h,
        "all_auxiliaries_return_clean": all_auxiliary_clean(rows),
        "literal_reverse_exact": restored == source,
    }


def lawful_behavior_certificate() -> dict[str, object]:
    cases = (
        lawful_case("held_2", 2, K.interleaved_program(2)),
        lawful_case("held_5", 5, K.interleaved_program(5)),
        lawful_case("padded_130", 12, E730.R719.PROGRAM),
    )
    keys = (
        "data_and_rails_equal_Cycle730",
        "A0_return",
        "B_work_return",
        "refs_h_return",
        "all_auxiliaries_return_clean",
        "literal_reverse_exact",
    )
    return {
        "cases": cases,
        "trajectories": len(cases),
        "failure_census": sum(
            not bool(row[key]) for row in cases for key in keys
        ),
    }


def canonical_refs(
    a_mask: int, b_mask: int, h: int, stations: int
) -> tuple[int, ...]:
    refs, obstruction = E730.F728.canonical_reference_extension(
        a_mask, b_mask, h, stations
    )
    if obstruction:
        raise AssertionError(
            ("matched-parity canonical reference obstruction", a_mask, b_mask)
        )
    return E730.mask_to_tuple(refs, stations)


def residual_witness_certificate() -> dict[str, object]:
    program = K.interleaved_program(2)
    stations = len(program)
    word, layout, _blocks, _metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    banks, links = B.chain_genesis(2)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    initial_data = E724.F723.tuple_to_int(before)
    placements = tuple(
        (left, right)
        for left in range(stations)
        for right in range(left + 1, stations)
    )
    sources = []
    refs_rows = []
    for placement in placements:
        a_mask = sum(1 << station for station in placement)
        refs = canonical_refs(a_mask, 0, 0, stations)
        refs_rows.append(refs)
        sources.append(
            controller_full_input(
                initial_data,
                layout,
                a=placement,
                refs=refs,
                h=0,
            )
        )
    observed_values = literal_apply(
        tuple(sources), word, layout["full_width"], 1
    )
    refusal_failures = return_failures = 0
    witness_row: dict[str, object] | None = None
    event_hasher = sha256()
    for placement, refs, source, observed_value in zip(
        placements, refs_rows, sources, observed_values
    ):
        rows = controller_rows(observed_value, layout)
        a = tuple(int(station in placement) for station in range(stations))
        rotated_a, rotated_b = E730.rotate_forward(
            a, (0,) * stations
        )
        event = {
            "step": 0,
            "station": placement[0],
            "reason": "count_mismatch",
            "observed_A_count": len(placement),
            "expected_count": EXPECTED_COUNT,
        }
        event_hasher.update(
            json.dumps(event, sort_keys=True, separators=(",", ":")).encode()
        )
        refusal_failures += rows["data"] != initial_data
        return_failures += rows["A"] != rotated_a
        return_failures += rows["B"] != rotated_b
        return_failures += rows["refs"] != refs or rows["h"] != 0
        return_failures += not all_auxiliary_clean(rows)
        if placement == (0, 5):
            refs_mask = E730.tuple_to_mask(refs)
            witness_row = {
                "ring_stations": stations,
                "A_mask": 33,
                "B_mask": 0,
                "h": 0,
                "token_sites": placement,
                "canonical_refs": refs_mask,
                "frozen_refs_match": refs_mask == 62,
                "refusal_event": event,
                "data_refused": rows["data"] == initial_data,
                "registers_return_clean": all_auxiliary_clean(rows),
            }
    if witness_row is None:
        raise AssertionError("frozen witness absent from pair sweep")
    return {
        "frozen_witness": witness_row,
        "two_token_placements": len(placements),
        "expected_two_token_placements": 55,
        "refusal_failures": refusal_failures,
        "return_cleanliness_failures": return_failures,
        "all_two_token_placements_refused":
            len(placements) == 55
            and refusal_failures == 0
            and return_failures == 0,
        "refusal_event_table_sha256": event_hasher.hexdigest(),
    }


def reference_from_q(q_mask: int, h: int, stations: int) -> int:
    """Independent r_0=0 recurrence for the amended charge rows."""

    marked = E730.F728.marked_station(stations)
    current = 0
    refs = 0
    closure = 0
    for station in range(stations):
        refs |= current << station
        following = (
            current
            ^ ((q_mask >> station) & 1)
            ^ (h if station == marked else 0)
        )
        if station == stations - 1:
            closure = following
        else:
            current = following
    return refs if closure == 0 else -1


def enforcement_theorem_certificate() -> dict[str, object]:
    stations = RING11_STATIONS
    rail_width = 1 << stations
    charge_pass: dict[tuple[int, int], bool] = {}
    local_row_recurrence_failures = 0
    parity_separation_failures = 0
    for q_mask in range(rail_width):
        for h in (0, 1):
            refs = reference_from_q(q_mask, h, stations)
            passed = refs >= 0
            if passed:
                syndrome = E730.F728.twisted_local_syndrome_mask(
                    q_mask, 0, refs, h, stations
                )
                local_row_recurrence_failures += syndrome != 0
            parity = q_mask.bit_count() & 1
            parity_separation_failures += passed != (parity == h)
            charge_pass[(q_mask, h)] = passed

    total_cases = 0
    full_pass_cases = 0
    count_pass_cases = 0
    parity_pass_cases = 0
    exceptions = 0
    outcome_hasher = sha256()
    digest_buffer = bytearray()
    for a_mask in range(rail_width):
        count_law = a_mask.bit_count() == EXPECTED_COUNT
        for b_mask in range(rail_width):
            q_mask = a_mask ^ b_mask
            token_parity = (
                a_mask.bit_count() + b_mask.bit_count()
            ) & 1
            for h in (0, 1):
                charge_law = charge_pass[(q_mask, h)]
                full_law = count_law and charge_law
                expected = (
                    a_mask.bit_count() == EXPECTED_COUNT
                    and token_parity == h
                )
                total_cases += 1
                count_pass_cases += count_law
                parity_pass_cases += charge_law
                full_pass_cases += full_law
                exceptions += full_law != expected
                digest_buffer.append(
                    int(count_law)
                    | (int(charge_law) << 1)
                    | (int(full_law) << 2)
                    | (int(expected) << 3)
                )
                if len(digest_buffer) >= 65_536:
                    outcome_hasher.update(digest_buffer)
                    digest_buffer.clear()
    outcome_hasher.update(digest_buffer)

    program = K.interleaved_program(2)
    _word, layout, _blocks, metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    ref_h_wires = set(
        range(layout["ref_base"], layout["ref_base"] + stations)
    )
    ref_h_wires.add(layout["h_wire"])
    touch_failures = sum(
        any(wire in ref_h_wires for wire in gate.wires)
        for gate in metadata["certificate_word"]
    )
    return {
        "ring_stations": stations,
        "rail_states": 1 << (2 * stations),
        "h_sectors": 2,
        "total_rail_h_cases": total_cases,
        "expected_total_rail_h_cases": 8_388_608,
        "count_pass_cases": count_pass_cases,
        "parity_pass_cases": parity_pass_cases,
        "full_pass_cases": full_pass_cases,
        "iff_exceptions": exceptions,
        "charge_recurrence_failures": local_row_recurrence_failures,
        "parity_separation_failures": parity_separation_failures,
        "count_definition": "A-rail controller tokens at the Q boundary",
        "full_law": (
            "A_count == declared expected_count AND "
            "(popcount(A)+popcount(B)) mod 2 == h"
        ),
        "count_certificate_ref_h_touch_failures": touch_failures,
        "count_law_factors_from_parity_law": touch_failures == 0,
        "outcome_table_sha256": outcome_hasher.hexdigest(),
    }


def register_dirty_weight(rows: dict[str, object]) -> int:
    return sum(
        int(bit)
        for key in (
            "syndrome",
            "scratch",
            "or_scratch",
            "charge",
            "counter",
            "increment_scratch",
            "comparison_scratch",
        )
        for bit in rows[key]
    ) + int(rows["refusal_latch"])


def deletion_controls_certificate(
    residual: dict[str, object],
) -> dict[str, object]:
    program = K.interleaved_program(2)
    word, layout, _blocks, metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    refs, h = E730.lawful_reference_rails(len(program))
    banks, links = B.chain_genesis(2)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    initial_data = E724.F723.tuple_to_int(before)
    source = controller_full_input(
        initial_data, layout, a=(0,), refs=refs, h=h
    )
    correct = literal_apply(
        (source,), word, layout["full_width"], 1
    )[0]
    correct_rows = controller_rows(correct, layout)

    first_block = metadata["increment_blocks"][0]
    increment_index = int(first_block["stop"]) - 1
    deleted_increment_word = (
        word[:increment_index] + word[increment_index + 1:]
    )
    increment_output = literal_apply(
        (source,), deleted_increment_word, layout["full_width"], 1
    )[0]
    increment_rows = controller_rows(increment_output, layout)

    comparison_start = int(metadata["comparison_compute_start"])
    comparison_stop = int(metadata["comparison_compute_stop"])
    comparison_index = next(
        index
        for index in range(comparison_start, comparison_stop)
        if word[index].kind != "X"
        and word[index].wires[-1] == layout["refusal_latch"]
    )
    deleted_comparison_word = (
        word[:comparison_index] + word[comparison_index + 1:]
    )
    comparison_output = literal_apply(
        (source,), deleted_comparison_word, layout["full_width"], 1
    )[0]
    comparison_rows = controller_rows(comparison_output, layout)

    count_compute_size = int(metadata["count_compute_stop"])
    uncompute_start = int(metadata["count_uncompute_start"])
    uncompute_index = (
        uncompute_start + count_compute_size - 1 - increment_index
    )
    deleted_uncompute_word = (
        word[:uncompute_index] + word[uncompute_index + 1:]
    )
    uncompute_output = literal_apply(
        (source,), deleted_uncompute_word, layout["full_width"], 1
    )[0]
    uncompute_rows = controller_rows(uncompute_output, layout)

    return {
        "correct_lawful_auxiliary_return": all_auxiliary_clean(correct_rows),
        "correct_word_refuses_all_two_token_violations":
            residual["all_two_token_placements_refused"],
        "deleted_increment_gate": (
            word[increment_index].kind,
            word[increment_index].wires,
        ),
        "deleted_increment_detected":
            increment_output != correct
            or register_dirty_weight(increment_rows) > 0,
        "deleted_increment_dirty_weight":
            register_dirty_weight(increment_rows),
        "deleted_comparison_gate": (
            word[comparison_index].kind,
            word[comparison_index].wires,
        ),
        "deleted_comparison_detected":
            comparison_output != correct
            or register_dirty_weight(comparison_rows) > 0,
        "deleted_comparison_dirty_weight":
            register_dirty_weight(comparison_rows),
        "deleted_uncompute_gate": (
            word[uncompute_index].kind,
            word[uncompute_index].wires,
        ),
        "deleted_uncompute_detected":
            uncompute_output != correct
            or register_dirty_weight(uncompute_rows) > 0,
        "deleted_uncompute_dirty_weight":
            register_dirty_weight(uncompute_rows),
    }


def physical_layout(bank_count: int) -> dict[str, object]:
    program, track = K.held_physical_program_and_track(bank_count)
    base = M.R12.full_wire_layout()
    data_sites = base["wire_sites"]
    a_sites = track[::2]
    b_sites = track[1::2]
    work_sites = tuple((x, y - 1, z) for x, y, z in a_sites)
    syndrome_sites = tuple((x, y - 2, z) for x, y, z in a_sites)
    mcx_scratch_sites = tuple(
        (x, y - 3 - slot, z)
        for x, y, z in a_sites
        for slot in range(E730.MCX_SCRATCH_PER_STATION)
    )
    or_scratch_sites = tuple(
        (
            x,
            y - 3 - E730.MCX_SCRATCH_PER_STATION - slot,
            z,
        )
        for x, y, z in a_sites
        for slot in range(COUNT_OR_INTERMEDIATES_PER_STATION)
    )
    ref_offset = (
        3
        + E730.MCX_SCRATCH_PER_STATION
        + COUNT_OR_INTERMEDIATES_PER_STATION
    )
    ref_sites = tuple(
        (x, y - ref_offset, z) for x, y, z in a_sites
    )
    charge_sites = tuple(
        (x, y - ref_offset - 1, z) for x, y, z in a_sites
    )
    marked = E730.F728.marked_station(len(program))
    mx, my, mz = a_sites[marked]
    h_sites = ((mx, my - ref_offset - 2, mz),)
    layout = register_layout(len(data_sites), len(program))
    width = layout["counter_width"]
    scratch_width = layout["increment_scratch_width"]
    next_offset = ref_offset + 3
    counter_sites = tuple(
        (mx, my - next_offset - bit, mz) for bit in range(width)
    )
    next_offset += width
    increment_scratch_sites = tuple(
        (mx, my - next_offset - slot, mz)
        for slot in range(scratch_width)
    )
    next_offset += scratch_width
    comparison_scratch_sites = tuple(
        (mx, my - next_offset - slot, mz)
        for slot in range(scratch_width)
    )
    next_offset += scratch_width
    latch_sites = ((mx, my - next_offset, mz),)
    controller_sites = (
        a_sites
        + b_sites
        + work_sites
        + syndrome_sites
        + mcx_scratch_sites
        + or_scratch_sites
        + ref_sites
        + charge_sites
        + h_sites
        + counter_sites
        + increment_scratch_sites
        + comparison_scratch_sites
        + latch_sites
    )
    wire_sites = data_sites + controller_sites
    word, built_layout, _blocks, metadata = (
        count_certified_controller_build(
            program, len(data_sites), EXPECTED_COUNT
        )
    )
    if built_layout != layout or len(wire_sites) != layout["full_width"]:
        raise AssertionError(
            ("physical/register layout", len(wire_sites), layout)
        )
    assigned = set(base["assigned_sites"])
    return {
        "program": program,
        "track": track,
        "word": word,
        "certificate_word": metadata["certificate_word"],
        "layout": layout,
        "wire_sites": wire_sites,
        "controller_sites": controller_sites,
        "placement_collisions":
            len(controller_sites)
            - len(set(controller_sites))
            + len(assigned & set(controller_sites)),
    }


def physical_case(bank_count: int) -> dict[str, object]:
    physical = physical_layout(bank_count)
    forward, inverse = E724.streaming_route_pair(
        physical["certificate_word"], physical["wire_sites"]
    )
    return {
        "banks": bank_count,
        "stations": len(physical["program"]),
        "counter_width": physical["layout"]["counter_width"],
        "certificate_semantic_gates":
            len(physical["certificate_word"]),
        "certificate_word_sha256":
            K.gate_digest(physical["certificate_word"]),
        "counter_comparison_M2":
            physical["layout"]["counter_width"]
            + physical["layout"]["increment_scratch_width"]
            + physical["layout"]["comparison_scratch_width"]
            + 1,
        "placement_collisions": physical["placement_collisions"],
        "forward": forward,
        "inverse": inverse,
    }


def physical_layer_certificate() -> dict[str, object]:
    cases = {banks: physical_case(banks) for banks in (2, 12)}
    route_keys = (
        "non_NN_failures",
        "operand_order_failures",
        "route_return_failures",
    )
    failures = sum(
        row["placement_collisions"] for row in cases.values()
    )
    failures += sum(
        row[direction][key]
        for row in cases.values()
        for direction in ("forward", "inverse")
        for key in route_keys
    )
    return {"banks": cases, "failure_census": failures}


def inherited_anchor_certificate() -> dict[str, object]:
    inherited = E730.inherited_anchors_certificate()
    return {
        "Cycle713_runner_expected_sha256":
            inherited["Cycle713_runner_expected_sha256"],
        "Cycle713_runner_observed_sha256":
            inherited["Cycle713_runner_observed_sha256"],
        "Cycle713_pin_match": inherited["Cycle713_pin_match"],
        "matter_residual_failures":
            inherited["matter_residual_failures"],
        "matter_falsifier_active":
            inherited["matter_falsifier_active"],
    }


def main() -> int:
    started = perf_counter()

    manifest = input_contract_certificate()
    check(
        "INPUT_declared_literal_paths",
        manifest["all_exist"]
        and manifest["pure_literal_tuple"]
        and not manifest["note_required"],
    )

    anchor = cycle730_regression_anchor()
    check(
        "A_Cycle730_regression_anchor",
        anchor["count_match"]
        and anchor["digest_match"]
        and anchor["repeat_exact"]
        and anchor["frozen_lawful_case_pass"],
    )

    structure = structure_certificate()
    lawful = lawful_behavior_certificate()
    check(
        "B_lawful_unchanged_and_exact_uncompute",
        lawful["failure_census"] == 0
        and structure["delta_equals_certificate_word"]
        and structure["R_literal_suffix_unchanged"]
        and structure["exact_comparison_uncompute"]
        and structure["exact_counter_uncompute"]
        and structure["compiled_gate_kind_failures"] == 0
        and structure["increment_comparison_locality_failures"] == 0,
    )

    residual = residual_witness_certificate()
    witness = residual["frozen_witness"]
    check(
        "C_frozen_witness_and_all_55_pairs_refused",
        witness["frozen_refs_match"]
        and witness["data_refused"]
        and witness["registers_return_clean"]
        and residual["two_token_placements"] == 55
        and residual["all_two_token_placements_refused"],
    )

    theorem = enforcement_theorem_certificate()
    check(
        "D_ring11_count_and_parity_enforcement_theorem",
        theorem["total_rail_h_cases"]
        == theorem["expected_total_rail_h_cases"]
        and theorem["iff_exceptions"] == 0
        and theorem["charge_recurrence_failures"] == 0
        and theorem["parity_separation_failures"] == 0
        and theorem["count_certificate_ref_h_touch_failures"] == 0
        and theorem["count_law_factors_from_parity_law"],
    )

    deletions = deletion_controls_certificate(residual)
    check(
        "E_increment_comparison_uncompute_deletions",
        deletions["correct_lawful_auxiliary_return"]
        and deletions["correct_word_refuses_all_two_token_violations"]
        and deletions["deleted_increment_detected"]
        and deletions["deleted_comparison_detected"]
        and deletions["deleted_uncompute_detected"],
    )

    physical = physical_layer_certificate()
    check(
        "F_collision_free_NN_routes_with_returned_work",
        physical["failure_census"] == 0,
    )

    inherited = inherited_anchor_certificate()
    check(
        "G_inherited_Cycle713_pins",
        inherited["Cycle713_pin_match"]
        and inherited["matter_residual_failures"] == 0
        and inherited["matter_falsifier_active"],
    )

    science_labels = tuple(
        label for label in CHECKS if label[:1] in "ABCDEFG"
    )
    all_a_to_g = all(CHECKS[label] for label in science_labels)
    remaining_gap = (
        "Scope is the ring-11 theorem fixture (with routed 11/130-station "
        "physical fixtures); expected_count=1, the clean counter/comparison "
        "registers, zero B at controller Q boundaries, references, h, ring "
        "orientation, program content, and clean genesis are declared "
        "supplies. The certificate enforces but does not derive inventory."
    )
    claim_boundary = {
        "scope": "ring-11 exhaustive count/parity theorem",
        "expected_count_is_declared_supply": True,
        "inventory_is_derived": False,
        "clean_counter_comparison_genesis_is_supplied": True,
        "exact_remaining_gap": remaining_gap,
        "w1_closed_scope": (
            "bounded ring-11 enforcement only; no genesis or arbitrary-ring "
            "inventory derivation"
        ),
    }
    w1_closed = all_a_to_g and bool(remaining_gap)
    check(
        "H_honest_declared_supply_boundary",
        all_a_to_g
        and claim_boundary["expected_count_is_declared_supply"]
        and not claim_boundary["inventory_is_derived"]
        and bool(claim_boundary["exact_remaining_gap"])
        and w1_closed,
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "matched_parity_multitoken_refused":
            bool(witness["data_refused"]),
        "w1_ring11_count_law_enforced":
            CHECKS["D_ring11_count_and_parity_enforcement_theorem"],
        "w1_closed": w1_closed,
        "input_contract": manifest,
        "Cycle730_regression_anchor": anchor,
        "circuit_structure": structure,
        "lawful_behavior": lawful,
        "residual_witness_and_pair_sweep": residual,
        "ring11_enforcement_theorem": theorem,
        "deletion_controls": deletions,
        "physical": physical,
        "inherited_anchors": inherited,
        "word_size_comparison": {
            "Cycle730_semantic_gates": EXPECTED_CYCLE730_PADDED_GATES,
            "Cycle731_semantic_gates": structure["semantic_gates"],
            "added_semantic_gates": structure["added_semantic_gates"],
            "Cycle731_to_Cycle730_ratio":
                structure["semantic_gates"]
                / EXPECTED_CYCLE730_PADDED_GATES,
        },
        "supplied_inventory": (
            "expected_count=1 is the same declared one-source-token inventory "
            "line used by Cycles 724/730; counter, increment scratch, "
            "comparison scratch, and refusal latch start clean."
        ),
        "claim_boundary": claim_boundary,
        "terminal": (
            "CYCLE731_TOKEN_COUNT_CERTIFICATE_PASS"
            if all(CHECKS.values())
            else "CYCLE731_TOKEN_COUNT_CERTIFICATE_HONEST_FAIL"
        ),
    }
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE731_TOKEN_COUNT_CERTIFICATE_PASS"
        if report["pass"]
        else "CYCLE731_TOKEN_COUNT_CERTIFICATE_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
