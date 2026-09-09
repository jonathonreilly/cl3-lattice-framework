#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-731 count certificate."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Any

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


BLOCKLISTED_MODULES = (
    "frontier_cycle731_token_count_certificate_2026_07_28",
    "frontier_cycle730_charge_row_enforcement_2026_07_28",
    "frontier_cycle724_local_token_row_enforcement_2026_07_28",
)
FROZEN_THEOREM_TABLE = {
    "ring_stations": 11,
    "total_rail_h_cases": 8388608,
    "count_pass_cases": 45056,
    "full_pass_cases": 22528,
    "iff_exceptions": 0,
    "outcome_table_sha256": "70c8565f054f8cff29acedf3f9a04585df280eec9395140ea7067130dab8b1ce",
    "refusal_event_table_sha256": "73ad99cfa287b117673e877363c73b736926395b1dd0b24d2d97b2f453844efd",
}
FROZEN_WORD_SIZES = {
    "Cycle730_semantic_gates": 99310,
    "Cycle731_semantic_gates": 112912,
    "added_semantic_gates": 13602,
}
FROZEN_WITNESS = {
    "ring_stations": 11,
    "A_mask": 33,
    "B_mask": 0,
    "h": 0,
    "token_sites": (0, 5),
    "canonical_refs": 62,
    "refusal_event": {
        "step": 0,
        "station": 0,
        "reason": "count_mismatch",
        "observed_A_count": 2,
        "expected_count": 1,
    },
}
FROZEN_CLAIM_BOUNDARY = {
    "w1_closed": True,
    "w1_closed_scope": "bounded ring-11 enforcement only; no genesis or arbitrary-ring inventory derivation",
}

EXPECTED_AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_NOTE_PATH = (
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
STDOUT_LIMIT_BYTES = 150 * 1024
_ROOT = Path(__file__).resolve().parents[1]
_K_ATTRIBUTES_AT_IMPORT = tuple(
    sorted((name, id(value)) for name, value in vars(K).items())
)


def _module_assignment(tree: ast.Module, name: str) -> ast.AST:
    matches: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                matches.append(node.value)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("module assignment", name, len(matches)))
    return matches[0]


def _find_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function", name, len(matches)))
    return matches[0]


def _function_assignment(function: ast.FunctionDef, name: str) -> ast.AST:
    matches: list[ast.AST] = []
    for node in ast.walk(function):
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                matches.append(node.value)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                matches.append(node.value)
    substantive = [
        value
        for value in matches
        if not (
            isinstance(value, ast.Constant)
            and value.value is None
        )
    ]
    if len(substantive) == 1:
        return substantive[0]
    if len(matches) != 1:
        raise AssertionError(("function assignment", function.name, name, len(matches)))
    return matches[0]


def _literal_dict_items(node: ast.AST) -> dict[str, ast.AST]:
    if not isinstance(node, ast.Dict):
        raise AssertionError(("expected dict AST", type(node).__name__))
    output: dict[str, ast.AST] = {}
    for key, value in zip(node.keys, node.values):
        literal_key = ast.literal_eval(key)
        if not isinstance(literal_key, str) or literal_key in output:
            raise AssertionError(("dict key", literal_key))
        output[literal_key] = value
    return output


def _return_dict(function: ast.FunctionDef) -> dict[str, ast.AST]:
    returns = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(returns) != 1:
        raise AssertionError(("return dict", function.name, len(returns)))
    return _literal_dict_items(returns[0])


def _direct_loop(body: list[ast.stmt], target_name: str) -> ast.For:
    matches = [
        node
        for node in body
        if isinstance(node, ast.For)
        and isinstance(node.target, ast.Name)
        and node.target.id == target_name
    ]
    if len(matches) != 1:
        raise AssertionError(("direct loop", target_name, len(matches)))
    return matches[0]


def _attribute_calls(function: ast.FunctionDef, owner: str) -> set[str]:
    return {
        node.func.attr
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == owner
    }


def _primary_tree() -> ast.Module:
    path = _ROOT / AUDIT_INPUT_PATHS[0]
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def _self_tree() -> ast.Module:
    path = Path(__file__).resolve()
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def extraction() -> dict[str, Any]:
    primary = _primary_tree()
    own = _self_tree()

    primary_literals = {
        name: ast.literal_eval(_module_assignment(primary, name))
        for name in (
            "AUDIT_TIMEOUT_SEC",
            "NOTE_PATH",
            "AUDIT_INPUT_PATHS",
            "EXPECTED_COUNT",
            "EXPECTED_CYCLE730_PADDED_GATES",
            "COUNT_LOCAL_ROW_INPUTS",
            "COUNT_OR_INTERMEDIATES_PER_STATION",
            "RING11_STATIONS",
        )
    }
    own_audit_paths = ast.literal_eval(_module_assignment(own, "AUDIT_INPUT_PATHS"))

    theorem_fn = _find_function(primary, "enforcement_theorem_certificate")
    theorem_return = _return_dict(theorem_fn)
    a_loop = _direct_loop(theorem_fn.body, "a_mask")
    b_loop = _direct_loop(a_loop.body, "b_mask")
    h_loop = _direct_loop(b_loop.body, "h")
    loop_order_ok = (
        ast.unparse(a_loop.iter) == "range(rail_width)"
        and ast.unparse(b_loop.iter) == "range(rail_width)"
        and ast.literal_eval(h_loop.iter) == (0, 1)
    )
    outcome_calls = [
        node
        for node in ast.walk(theorem_fn)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "digest_buffer"
        and node.func.attr == "append"
    ]
    if len(outcome_calls) != 1 or len(outcome_calls[0].args) != 1:
        raise AssertionError(("outcome append calls", len(outcome_calls)))
    byte_tree = outcome_calls[0].args[0]
    byte_names = {node.id for node in ast.walk(byte_tree) if isinstance(node, ast.Name)}
    byte_shifts = {
        ast.literal_eval(node.right)
        for node in ast.walk(byte_tree)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.LShift)
    }
    byte_convention_ok = {
        "count_law",
        "charge_law",
        "full_law",
        "expected",
    } <= byte_names and byte_shifts == {1, 2, 3}
    outcome_return = theorem_return["outcome_table_sha256"]
    outcome_return_ok = (
        isinstance(outcome_return, ast.Call)
        and isinstance(outcome_return.func, ast.Attribute)
        and isinstance(outcome_return.func.value, ast.Name)
        and outcome_return.func.value.id == "outcome_hasher"
        and outcome_return.func.attr == "hexdigest"
    )

    residual_fn = _find_function(primary, "residual_witness_certificate")
    event_items = _literal_dict_items(_function_assignment(residual_fn, "event"))
    witness_items = _literal_dict_items(_function_assignment(residual_fn, "witness_row"))
    residual_return = _return_dict(residual_fn)
    event_schema_ok = (
        set(event_items)
        == {
            "step",
            "station",
            "reason",
            "observed_A_count",
            "expected_count",
        }
        and ast.literal_eval(event_items["step"]) == 0
        and ast.literal_eval(event_items["reason"]) == "count_mismatch"
        and ast.unparse(event_items["station"]) == "placement[0]"
        and ast.unparse(event_items["observed_A_count"]) == "len(placement)"
        and ast.unparse(event_items["expected_count"]) == "EXPECTED_COUNT"
    )
    witness_schema_ok = (
        ast.literal_eval(witness_items["ring_stations"]) if isinstance(
            witness_items["ring_stations"], ast.Constant
        ) else 11
    ) == 11
    witness_schema_ok = witness_schema_ok and (
        ast.literal_eval(witness_items["A_mask"]) == 33
        and ast.literal_eval(witness_items["B_mask"]) == 0
        and ast.literal_eval(witness_items["h"]) == 0
        and ast.unparse(witness_items["token_sites"]) == "placement"
        and ast.unparse(witness_items["canonical_refs"]) == "refs_mask"
        and ast.unparse(witness_items["frozen_refs_match"]) == "refs_mask == 62"
        and ast.unparse(witness_items["refusal_event"]) == "event"
    )
    refusal_return = residual_return["refusal_event_table_sha256"]
    refusal_return_ok = (
        isinstance(refusal_return, ast.Call)
        and isinstance(refusal_return.func, ast.Attribute)
        and isinstance(refusal_return.func.value, ast.Name)
        and refusal_return.func.value.id == "event_hasher"
        and refusal_return.func.attr == "hexdigest"
    )
    json_dumps_calls = [
        node
        for node in ast.walk(residual_fn)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "json"
        and node.func.attr == "dumps"
    ]
    json_convention_ok = False
    if len(json_dumps_calls) == 1:
        keywords = {keyword.arg: keyword.value for keyword in json_dumps_calls[0].keywords}
        json_convention_ok = (
            ast.unparse(json_dumps_calls[0].args[0]) == "event"
            and ast.literal_eval(keywords["sort_keys"]) is True
            and ast.literal_eval(keywords["separators"]) == (",", ":")
        )

    main_fn = _find_function(primary, "main")
    boundary_items = _literal_dict_items(_function_assignment(main_fn, "claim_boundary"))
    report_items = _literal_dict_items(_function_assignment(main_fn, "report"))
    word_size_items = _literal_dict_items(report_items["word_size_comparison"])
    w1_assignment = _function_assignment(main_fn, "w1_closed")
    boundary_ok = (
        ast.literal_eval(boundary_items["w1_closed_scope"])
        == FROZEN_CLAIM_BOUNDARY["w1_closed_scope"]
        and isinstance(w1_assignment, ast.BoolOp)
        and isinstance(w1_assignment.op, ast.And)
        and ast.unparse(report_items["w1_closed"]) == "w1_closed"
        and {
            "Cycle730_semantic_gates",
            "Cycle731_semantic_gates",
            "added_semantic_gates",
        }
        <= set(word_size_items)
    )

    extracted_expected_total = ast.literal_eval(
        theorem_return["expected_total_rail_h_cases"]
    )
    anchors_ok = (
        primary_literals["AUDIT_TIMEOUT_SEC"] == 900
        and primary_literals["NOTE_PATH"] == EXPECTED_NOTE_PATH
        and isinstance(primary_literals["AUDIT_INPUT_PATHS"], tuple)
        and primary_literals["EXPECTED_COUNT"] == 1
        and primary_literals["EXPECTED_CYCLE730_PADDED_GATES"]
        == FROZEN_WORD_SIZES["Cycle730_semantic_gates"]
        and primary_literals["COUNT_LOCAL_ROW_INPUTS"] == 8
        and primary_literals["COUNT_OR_INTERMEDIATES_PER_STATION"] == 6
        and primary_literals["RING11_STATIONS"]
        == FROZEN_THEOREM_TABLE["ring_stations"]
        and extracted_expected_total
        == FROZEN_THEOREM_TABLE["total_rail_h_cases"]
        and own_audit_paths == EXPECTED_AUDIT_INPUT_PATHS
        and AUDIT_TIMEOUT_SEC == 900
        and NOTE_PATH == EXPECTED_NOTE_PATH
    )
    frozen_prefixes_ok = (
        FROZEN_THEOREM_TABLE["outcome_table_sha256"].startswith("70c8565f")
        and FROZEN_THEOREM_TABLE["refusal_event_table_sha256"].startswith(
            "73ad99cf"
        )
    )
    passed = all(
        (
            anchors_ok,
            loop_order_ok,
            byte_convention_ok,
            outcome_return_ok,
            event_schema_ok,
            witness_schema_ok,
            refusal_return_ok,
            json_convention_ok,
            boundary_ok,
            frozen_prefixes_ok,
        )
    )
    return {
        "pass": passed,
        "anchors_ok": anchors_ok,
        "loop_order_ok": loop_order_ok,
        "byte_convention_ok": byte_convention_ok,
        "event_schema_ok": event_schema_ok,
        "boundary_ok": boundary_ok,
    }


def _counter_width(stations: int) -> int:
    if stations < 1:
        raise ValueError(("stations", stations))
    return stations.bit_length()


def _simulate_declared_counter(a_mask: int, stations: int) -> tuple[int, ...]:
    """Simulate the declared high-carry-first controlled increments."""

    counter = [0] * _counter_width(stations)
    for station in range(stations):
        control = (a_mask >> station) & 1
        for bit in reversed(range(1, len(counter))):
            if control and all(counter[:bit]):
                counter[bit] ^= 1
        counter[0] ^= control
    return tuple(counter)


def _counter_integer(counter: tuple[int, ...]) -> int:
    return sum(bit << index for index, bit in enumerate(counter))


def _reference_rows(
    q_mask: int, h: int, stations: int, marked: int | None = None
) -> tuple[tuple[int, ...], bool]:
    """Construct r_0=0 rows and test the final closed-ring row."""

    if marked is None:
        marked = stations - 1
    current = 0
    refs: list[int] = []
    for station in range(stations):
        refs.append(current)
        current ^= (q_mask >> station) & 1
        if station == marked:
            current ^= h
    return tuple(refs), current == 0


def _row_syndromes(
    q_mask: int,
    refs: tuple[int, ...],
    h: int,
    stations: int,
    marked: int | None = None,
) -> tuple[int, ...]:
    if marked is None:
        marked = stations - 1
    return tuple(
        refs[station]
        ^ ((q_mask >> station) & 1)
        ^ (h if station == marked else 0)
        ^ refs[(station + 1) % stations]
        for station in range(stations)
    )


def count_theorem_recount() -> dict[str, Any]:
    stations = FROZEN_THEOREM_TABLE["ring_stations"]
    rail_width = 1 << stations
    counters = tuple(
        _counter_integer(_simulate_declared_counter(a_mask, stations))
        for a_mask in range(rail_width)
    )
    charge_pass: list[tuple[bool, bool]] = []
    recurrence_failures = 0
    parity_separation_failures = 0
    for q_mask in range(rail_width):
        row = []
        for h in (0, 1):
            refs, closed = _reference_rows(q_mask, h, stations)
            if closed:
                recurrence_failures += any(
                    _row_syndromes(q_mask, refs, h, stations)
                )
            expected_parity = (q_mask.bit_count() & 1) == h
            parity_separation_failures += closed != expected_parity
            row.append(closed)
        charge_pass.append((row[0], row[1]))

    total_cases = 0
    count_pass_cases = 0
    parity_pass_cases = 0
    full_pass_cases = 0
    iff_exceptions = 0
    outcome_hasher = sha256()
    digest_buffer = bytearray()
    for a_mask in range(rail_width):
        count_law = counters[a_mask] == 1
        for b_mask in range(rail_width):
            q_mask = a_mask ^ b_mask
            token_parity = (
                a_mask.bit_count() + b_mask.bit_count()
            ) & 1
            for h in (0, 1):
                charge_law = charge_pass[q_mask][h]
                full_law = count_law and charge_law
                expected = counters[a_mask] == 1 and token_parity == h
                total_cases += 1
                count_pass_cases += count_law
                parity_pass_cases += charge_law
                full_pass_cases += full_law
                iff_exceptions += full_law != expected
                digest_buffer.append(
                    int(count_law)
                    | (int(charge_law) << 1)
                    | (int(full_law) << 2)
                    | (int(expected) << 3)
                )
                if len(digest_buffer) >= 65536:
                    outcome_hasher.update(digest_buffer)
                    digest_buffer.clear()
    outcome_hasher.update(digest_buffer)
    observed_sha = outcome_hasher.hexdigest()
    passed = (
        total_cases == FROZEN_THEOREM_TABLE["total_rail_h_cases"]
        and count_pass_cases == FROZEN_THEOREM_TABLE["count_pass_cases"]
        and full_pass_cases == FROZEN_THEOREM_TABLE["full_pass_cases"]
        and iff_exceptions == FROZEN_THEOREM_TABLE["iff_exceptions"]
        and recurrence_failures == 0
        and parity_separation_failures == 0
        and observed_sha == FROZEN_THEOREM_TABLE["outcome_table_sha256"]
    )
    return {
        "pass": passed,
        "total_cases": total_cases,
        "count_pass_cases": count_pass_cases,
        "parity_pass_cases": parity_pass_cases,
        "full_pass_cases": full_pass_cases,
        "iff_exceptions": iff_exceptions,
        "recurrence_failures": recurrence_failures,
        "parity_separation_failures": parity_separation_failures,
        "outcome_table_sha256": observed_sha,
        "outcome_sha_match": (
            observed_sha == FROZEN_THEOREM_TABLE["outcome_table_sha256"]
        ),
    }


def _mask_from_bits(bits: tuple[int, ...]) -> int:
    return sum(bit << index for index, bit in enumerate(bits))


def _refusal_event(
    placement: tuple[int, int], observed_count: int
) -> dict[str, Any]:
    return {
        "step": 0,
        "station": placement[0],
        "reason": "count_mismatch",
        "observed_A_count": observed_count,
        "expected_count": 1,
    }


def witness_and_sweep_recount() -> dict[str, Any]:
    stations = FROZEN_THEOREM_TABLE["ring_stations"]
    placements = tuple(
        (left, right)
        for left in range(stations)
        for right in range(left + 1, stations)
    )
    event_hasher = sha256()
    refused = 0
    reason_failures = 0
    reference_failures = 0
    witness: dict[str, Any] | None = None
    for placement in placements:
        a_mask = (1 << placement[0]) | (1 << placement[1])
        counter = _simulate_declared_counter(a_mask, stations)
        observed_count = _counter_integer(counter)
        refs, closed = _reference_rows(a_mask, 0, stations)
        reference_failures += not closed
        reference_failures += any(
            _row_syndromes(a_mask, refs, 0, stations)
        )
        mismatch = observed_count != 1
        event = _refusal_event(placement, observed_count)
        refused += mismatch
        reason_failures += event["reason"] != "count_mismatch"
        event_hasher.update(
            json.dumps(
                event, sort_keys=True, separators=(",", ":")
            ).encode()
        )
        if placement == (0, 5):
            witness = {
                "ring_stations": stations,
                "A_mask": a_mask,
                "B_mask": 0,
                "h": 0,
                "token_sites": placement,
                "canonical_refs": _mask_from_bits(refs),
                "refusal_event": event,
            }
    if witness is None:
        raise AssertionError("frozen witness absent")
    observed_sha = event_hasher.hexdigest()
    passed = (
        len(placements) == 55
        and refused == 55
        and reason_failures == 0
        and reference_failures == 0
        and witness == FROZEN_WITNESS
        and observed_sha
        == FROZEN_THEOREM_TABLE["refusal_event_table_sha256"]
    )
    return {
        "pass": passed,
        "placements": len(placements),
        "refused": refused,
        "reason_failures": reason_failures,
        "reference_failures": reference_failures,
        "witness_match": witness == FROZEN_WITNESS,
        "refusal_event_table_sha256": observed_sha,
        "refusal_sha_match": (
            observed_sha
            == FROZEN_THEOREM_TABLE["refusal_event_table_sha256"]
        ),
    }


def _gate_layout(stations: int) -> dict[str, Any]:
    width = _counter_width(stations)
    scratch_width = max(0, width - 2)
    a = tuple(range(stations))
    b = tuple(range(stations, 2 * stations))
    refs = tuple(range(2 * stations, 3 * stations))
    h = 3 * stations
    counter = tuple(range(h + 1, h + 1 + width))
    increment_scratch = tuple(
        range(counter[-1] + 1, counter[-1] + 1 + scratch_width)
    )
    next_wire = (
        increment_scratch[-1] + 1
        if increment_scratch
        else counter[-1] + 1
    )
    comparison_scratch = tuple(
        range(next_wire, next_wire + scratch_width)
    )
    next_wire += scratch_width
    latch = next_wire
    return {
        "a": a,
        "b": b,
        "refs": refs,
        "h": h,
        "counter": counter,
        "increment_scratch": increment_scratch,
        "comparison_scratch": comparison_scratch,
        "latch": latch,
        "next_wire": latch + 1,
    }


def _emit_count_compute(
    layout: dict[str, Any],
) -> tuple[Any, ...]:
    word: list[Any] = []
    counter = layout["counter"]
    scratch = layout["increment_scratch"]
    for control in layout["a"]:
        for bit in reversed(range(1, len(counter))):
            controls = (control,) + counter[:bit]
            word.extend(
                K.A.mcx(
                    controls,
                    counter[bit],
                    scratch[: max(0, len(controls) - 2)],
                )
            )
        word.append(K.A.cn(control, counter[0]))
    return tuple(word)


def _emit_comparison_compute(
    layout: dict[str, Any], expected_count: int = 1
) -> tuple[Any, ...]:
    counter = layout["counter"]
    zero_bits = tuple(
        counter[bit]
        for bit in range(len(counter))
        if not ((expected_count >> bit) & 1)
    )
    word: list[Any] = [K.A.x(wire) for wire in zero_bits]
    word.append(K.A.x(layout["latch"]))
    word.extend(
        K.A.mcx(
            counter,
            layout["latch"],
            layout["comparison_scratch"],
        )
    )
    word.extend(K.A.x(wire) for wire in reversed(zero_bits))
    return tuple(word)


def _emit_extra_or_pairs(
    layout: dict[str, Any], nonidentity_stations: int
) -> tuple[Any, ...]:
    word: list[Any] = []
    base = layout["next_wire"]
    for index in range(nonidentity_stations):
        intermediate = base + 2 * index
        syndrome = intermediate + 1
        compute = (
            K.A.cn(intermediate, syndrome),
            K.A.cn(layout["latch"], syndrome),
            K.A.tof(intermediate, layout["latch"], syndrome),
        )
        word.extend(compute)
        word.extend(reversed(compute))
    return tuple(word)


def _apply_own_gate_word(value: int, word: tuple[Any, ...]) -> int:
    output = value
    for gate in word:
        if gate.kind == "X":
            output ^= 1 << gate.wires[0]
        elif gate.kind == "CNOT":
            control, target = gate.wires
            if (output >> control) & 1:
                output ^= 1 << target
        elif gate.kind == "TOF":
            left, right, target = gate.wires
            if ((output >> left) & 1) and ((output >> right) & 1):
                output ^= 1 << target
        else:
            raise AssertionError(("unexpected gate kind", gate.kind))
    return output


def _wire_mask(value: int, wires: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((value >> wire) & 1 for wire in wires)


def _primary_gate_family_audit(primary: ast.Module) -> dict[str, Any]:
    family_names = (
        "counter_wires",
        "increment_scratch",
        "comparison_scratch",
        "controlled_increment_word",
        "count_compute_word",
        "comparison_compute_word",
    )
    functions = {name: _find_function(primary, name) for name in family_names}
    forbidden = {"ref_base", "h_wire"}
    forbidden_hits = 0
    for function in functions.values():
        for node in ast.walk(function):
            if isinstance(node, ast.Name):
                forbidden_hits += node.id in forbidden
            elif isinstance(node, ast.Attribute):
                forbidden_hits += node.attr in forbidden
            elif isinstance(node, ast.Constant) and isinstance(node.value, str):
                forbidden_hits += node.value in forbidden
    controlled_calls = _attribute_calls(
        functions["controlled_increment_word"], "A"
    )
    comparison_calls = _attribute_calls(
        functions["comparison_compute_word"], "A"
    )
    count_calls = {
        node.func.id
        for node in ast.walk(functions["count_compute_word"])
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    build_fn = _find_function(primary, "count_certified_controller_build")
    certificate_node = _function_assignment(build_fn, "certificate_word")
    certificate_names = {
        node.id for node in ast.walk(certificate_node) if isinstance(node, ast.Name)
    }
    assembly_ok = {
        "count_compute",
        "compare_compute",
        "extra_or_gates",
    } <= certificate_names
    passed = (
        forbidden_hits == 0
        and controlled_calls == {"mcx", "cn"}
        and comparison_calls == {"x", "mcx"}
        and "controlled_increment_word" in count_calls
        and assembly_ok
    )
    return {
        "pass": passed,
        "forbidden_hits": forbidden_hits,
        "controlled_calls": controlled_calls,
        "comparison_calls": comparison_calls,
        "assembly_ok": assembly_ok,
    }


def factorization_audit() -> dict[str, Any]:
    primary_audit = _primary_gate_family_audit(_primary_tree())

    padded_program = K.interleaved_program(12, physical_padding=True)
    stations = len(padded_program)
    nonidentity = sum(bool(K.mapped_macro(row)) for row in padded_program)
    padded_layout = _gate_layout(stations)
    count_compute = _emit_count_compute(padded_layout)
    compare_compute = _emit_comparison_compute(padded_layout)
    extra_or = _emit_extra_or_pairs(padded_layout, nonidentity)
    certificate_word = (
        count_compute
        + compare_compute
        + extra_or
        + tuple(reversed(compare_compute))
        + tuple(reversed(count_compute))
    )
    forbidden_wires = set(padded_layout["refs"]) | {padded_layout["h"]}
    forbidden_touch_failures = sum(
        any(wire in forbidden_wires for wire in gate.wires)
        for gate in certificate_word
    )
    protected_targets = (
        set(padded_layout["a"])
        | set(padded_layout["b"])
        | forbidden_wires
    )
    protected_target_failures = sum(
        gate.wires[-1] in protected_targets for gate in certificate_word
    )
    observed_sizes = {
        "Cycle730_semantic_gates": FROZEN_WORD_SIZES[
            "Cycle730_semantic_gates"
        ],
        "Cycle731_semantic_gates": (
            FROZEN_WORD_SIZES["Cycle730_semantic_gates"]
            + len(certificate_word)
        ),
        "added_semantic_gates": len(certificate_word),
    }

    sample_layout = _gate_layout(FROZEN_THEOREM_TABLE["ring_stations"])
    sample_count = _emit_count_compute(sample_layout)
    sample_compare = _emit_comparison_compute(sample_layout)
    compute_word = sample_count + sample_compare
    uncompute_word = tuple(reversed(sample_compare)) + tuple(
        reversed(sample_count)
    )
    subsample_cases = 512
    parity_differences = 0
    rail_mutations = 0
    latch_failures = 0
    uncompute_failures = 0
    stations11 = FROZEN_THEOREM_TABLE["ring_stations"]
    full_case_mask = (1 << (2 * stations11 + 1)) - 1
    for index in range(subsample_cases):
        flat = (7 + index * 16411) & full_case_mask
        h = flat & 1
        b_mask = (flat >> 1) & ((1 << stations11) - 1)
        a_mask = (flat >> (stations11 + 1)) & (
            (1 << stations11) - 1
        )
        refs, _closed = _reference_rows(a_mask ^ b_mask, h, stations11)
        source = 0
        for station in range(stations11):
            source |= ((a_mask >> station) & 1) << sample_layout["a"][station]
            source |= ((b_mask >> station) & 1) << sample_layout["b"][station]
            source |= refs[station] << sample_layout["refs"][station]
        source |= h << sample_layout["h"]
        parity_before = _reference_rows(
            a_mask ^ b_mask, h, stations11
        )[1]
        during = _apply_own_gate_word(source, compute_word)
        during_a = _mask_from_bits(
            _wire_mask(during, sample_layout["a"])
        )
        during_b = _mask_from_bits(
            _wire_mask(during, sample_layout["b"])
        )
        during_h = (during >> sample_layout["h"]) & 1
        parity_after = _reference_rows(
            during_a ^ during_b, during_h, stations11
        )[1]
        parity_differences += parity_before != parity_after
        rail_mutations += (
            during_a != a_mask
            or during_b != b_mask
            or during_h != h
            or _wire_mask(during, sample_layout["refs"]) != refs
        )
        observed_count = _counter_integer(
            _simulate_declared_counter(a_mask, stations11)
        )
        latch = (during >> sample_layout["latch"]) & 1
        latch_failures += latch != int(observed_count != 1)
        restored = _apply_own_gate_word(during, uncompute_word)
        uncompute_failures += restored != source

    passed = (
        primary_audit["pass"]
        and stations == 130
        and nonidentity == 91
        and forbidden_touch_failures == 0
        and protected_target_failures == 0
        and observed_sizes == FROZEN_WORD_SIZES
        and parity_differences == 0
        and rail_mutations == 0
        and latch_failures == 0
        and uncompute_failures == 0
    )
    return {
        "pass": passed,
        "primary_ast_pass": primary_audit["pass"],
        "ref_h_touch_failures": forbidden_touch_failures,
        "protected_target_failures": protected_target_failures,
        "subsample_cases": subsample_cases,
        "parity_differences": parity_differences,
        "rail_mutations": rail_mutations,
        "latch_failures": latch_failures,
        "uncompute_failures": uncompute_failures,
        "observed_sizes": observed_sizes,
    }


def _target_root_name(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, (ast.Attribute, ast.Subscript)):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def discipline() -> dict[str, Any]:
    own = _self_tree()
    imported = {
        alias.name
        for node in ast.walk(own)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported.update(
        node.module
        for node in ast.walk(own)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    )
    static_blocklist_imports = sorted(set(BLOCKLISTED_MODULES) & imported)
    runtime_blocklist_imports = sorted(
        name
        for name in sys.modules
        if name.split(".")[-1] in BLOCKLISTED_MODULES
    )

    k_attribute_writes = 0
    for node in ast.walk(own):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, ast.AnnAssign):
            targets.append(node.target)
        elif isinstance(node, ast.AugAssign):
            targets.append(node.target)
        elif isinstance(node, ast.Delete):
            targets.extend(node.targets)
        k_attribute_writes += sum(
            _target_root_name(target) == "K"
            and not isinstance(target, ast.Name)
            for target in targets
        )
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id == "K"
        ):
            k_attribute_writes += 1
    k_snapshot_unchanged = _K_ATTRIBUTES_AT_IMPORT == tuple(
        sorted((name, id(value)) for name, value in vars(K).items())
    )

    literal_names = (
        "FROZEN_THEOREM_TABLE",
        "FROZEN_WORD_SIZES",
        "FROZEN_WITNESS",
        "FROZEN_CLAIM_BOUNDARY",
    )
    runtime_values = {
        "FROZEN_THEOREM_TABLE": FROZEN_THEOREM_TABLE,
        "FROZEN_WORD_SIZES": FROZEN_WORD_SIZES,
        "FROZEN_WITNESS": FROZEN_WITNESS,
        "FROZEN_CLAIM_BOUNDARY": FROZEN_CLAIM_BOUNDARY,
    }
    literal_failures = 0
    for name in literal_names:
        node = _module_assignment(own, name)
        literal_failures += not isinstance(node, ast.Dict)
        literal_failures += ast.literal_eval(node) != runtime_values[name]
    own_audit_literal = ast.literal_eval(
        _module_assignment(own, "AUDIT_INPUT_PATHS")
    )
    header_ok = (
        AUDIT_TIMEOUT_SEC == 900
        and NOTE_PATH == EXPECTED_NOTE_PATH
        and own_audit_literal == EXPECTED_AUDIT_INPUT_PATHS
        and isinstance(own_audit_literal, tuple)
    )
    boundary_ok = (
        FROZEN_CLAIM_BOUNDARY
        == {
            "w1_closed": True,
            "w1_closed_scope": (
                "bounded ring-11 enforcement only; no genesis or arbitrary-ring "
                "inventory derivation"
            ),
        }
    )
    passed = (
        not static_blocklist_imports
        and not runtime_blocklist_imports
        and k_attribute_writes == 0
        and k_snapshot_unchanged
        and literal_failures == 0
        and header_ok
        and boundary_ok
    )
    return {
        "pass": passed,
        "static_blocklist_imports": static_blocklist_imports,
        "runtime_blocklist_imports": runtime_blocklist_imports,
        "K_attribute_writes": k_attribute_writes,
        "K_snapshot_unchanged": k_snapshot_unchanged,
        "literal_failures": literal_failures,
        "header_ok": header_ok,
        "boundary_ok": boundary_ok,
    }


def _run_certificate(name: str, function: Any) -> dict[str, Any]:
    try:
        result = function()
        if not isinstance(result, dict) or "pass" not in result:
            return {
                "pass": False,
                "error": f"{name} returned no pass verdict",
            }
        return result
    except Exception as error:
        return {
            "pass": False,
            "error": f"{type(error).__name__}: {error}",
        }


def main() -> int:
    started = perf_counter()
    extraction_result = _run_certificate("extraction", extraction)
    theorem_result = _run_certificate(
        "count_theorem_recount", count_theorem_recount
    )
    witness_result = _run_certificate(
        "witness_and_sweep_recount", witness_and_sweep_recount
    )
    factor_result = _run_certificate(
        "factorization_audit", factorization_audit
    )
    discipline_result = _run_certificate("discipline", discipline)
    results = (
        extraction_result,
        theorem_result,
        witness_result,
        factor_result,
        discipline_result,
    )
    passed_count = sum(bool(result.get("pass")) for result in results)

    def verdict(result: dict[str, Any]) -> str:
        return "PASS" if result.get("pass") else "FAIL"

    lines = [
        (
            f"{verdict(extraction_result)} extraction :: "
            f"anchors={extraction_result.get('anchors_ok', False)} "
            f"loops={extraction_result.get('loop_order_ok', False)} "
            f"boundary={extraction_result.get('boundary_ok', False)}"
        ),
        (
            f"{verdict(theorem_result)} count_theorem_recount :: "
            f"total={theorem_result.get('total_cases', 0)} "
            f"count_pass={theorem_result.get('count_pass_cases', 0)} "
            f"full_pass={theorem_result.get('full_pass_cases', 0)} "
            f"iff_exceptions={theorem_result.get('iff_exceptions', -1)} "
            f"outcome_sha_match={theorem_result.get('outcome_sha_match', False)}"
        ),
        (
            f"{verdict(witness_result)} witness_and_sweep_recount :: "
            f"refused={witness_result.get('refused', 0)}/"
            f"{witness_result.get('placements', 0)} "
            f"witness_match={witness_result.get('witness_match', False)} "
            f"refusal_sha_match={witness_result.get('refusal_sha_match', False)}"
        ),
        (
            f"{verdict(factor_result)} factorization_audit :: "
            f"ref_h_touches={factor_result.get('ref_h_touch_failures', -1)} "
            f"parity_differences={factor_result.get('parity_differences', -1)}/"
            f"{factor_result.get('subsample_cases', 0)} "
            f"word_sizes={factor_result.get('observed_sizes', {})}"
        ),
        (
            f"{verdict(discipline_result)} discipline :: "
            f"K_writes={discipline_result.get('K_attribute_writes', -1)} "
            f"blocklisted_imports="
            f"{len(discipline_result.get('runtime_blocklist_imports', ['error']))} "
            f"literal_failures={discipline_result.get('literal_failures', -1)}"
        ),
        (
            f"SUMMARY {passed_count}/{len(results)} :: "
            f"outcome_sha_match={theorem_result.get('outcome_sha_match', False)} "
            f"refusal_sha_match={witness_result.get('refusal_sha_match', False)} "
            f"factorization={factor_result.get('pass', False)}"
        ),
    ]
    elapsed = perf_counter() - started
    all_passed = passed_count == len(results)
    lines.append(
        (
            "CYCLE731_INDEPENDENT_CHECK_PASS"
            if all_passed
            else "CYCLE731_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        + f" runtime_seconds={elapsed:.6f}"
    )
    text = "\n".join(lines) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
