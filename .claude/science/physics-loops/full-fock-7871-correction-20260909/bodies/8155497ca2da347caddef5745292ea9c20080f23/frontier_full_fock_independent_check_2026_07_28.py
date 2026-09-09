#!/usr/bin/env python3
"""Independent checker for the bounded full-Fock unit-weight construction.

The construction source is parsed as data and is never imported.  Numerical
operators below are independently assembled from the landed U320 and S322
public interfaces.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any, Callable

import numpy as np
from scipy.linalg import expm


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/FULL_FOCK_UNIT_WEIGHT_SOURCE_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
)

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_DATA_PATH = (
    ROOT / "scripts/frontier_full_fock_unit_weight_source_2026_07_28.py"
)
IMPORT_BLOCKLIST = (
    "frontier_full_fock_unit_weight_source_2026_07_28",
)

# Frozen audit anchors.  The first two are independently recounted below.
FROZEN_N_MAX = 2
FROZEN_LAYER_CHANNEL_COUNTS = (0, 6, 24)
FROZEN_LAYER1_WEIGHT = 0.12589921612871374
FROZEN_S322_PASS = 20
FROZEN_S322_FAIL = 0
FROZEN_CYCLE322_SHA256 = (
    "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75"
)
TOLERANCE = 3e-10

sys.path.insert(0, str(ROOT / "scripts"))

import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322


PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ExtractedConvention:
    text: str
    n_max: int
    reservoir_q: int
    pair_q_offset: int
    audit_input_paths: tuple[str, ...]
    tolerance: float
    cycle322_sha256: str
    cycle322_summary_marker: str
    cycle322_terminal_marker: str


@dataclass(frozen=True)
class Channel:
    number: int
    source_mask: int
    target_mask: int
    direction: int
    sign: int
    reservoir_index: int
    pair_index: int


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def _literal_assignments(tree: ast.AST) -> dict[str, Any]:
    assignments: dict[str, Any] = {}
    for node in getattr(tree, "body", ()):
        name: str | None = None
        value: ast.expr | None = None
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            if isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                value = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name = node.target.id
            value = node.value
        if name is None or value is None:
            continue
        try:
            assignments[name] = ast.literal_eval(value)
        except (ValueError, TypeError):
            continue
    return assignments


def _primary_ast() -> tuple[str, ast.Module]:
    source = PRIMARY_DATA_PATH.read_text(encoding="utf-8")
    return source, ast.parse(source, filename=str(PRIMARY_DATA_PATH))


def extraction() -> tuple[bool, dict[str, object], ExtractedConvention | None]:
    """Extract only literal conventions and anchors from the primary AST."""
    _source, tree = _primary_ast()
    literals = _literal_assignments(tree)
    required = (
        "AUDIT_TIMEOUT_SEC",
        "NOTE_PATH",
        "AUDIT_INPUT_PATHS",
        "N_MAX",
        "TOLERANCE",
        "CYCLE322_SHA256",
        "LAYER_EMBEDDING",
    )
    missing = tuple(name for name in required if name not in literals)
    if missing:
        return False, {"missing_literal_assignments": missing}, None

    embedding = literals["LAYER_EMBEDDING"]
    source_audit_paths = literals["AUDIT_INPUT_PATHS"]
    strings = {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    summary_marker = (
        f"SUMMARY {{'pass': {FROZEN_S322_PASS}, 'fail': {FROZEN_S322_FAIL}}}"
    )
    terminal_marker = "RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED"

    reservoir_match = re.search(r"\bq=(\d+)\s+is the endpoint reservoir", embedding)
    pair_match = re.search(r"\bq=(\d+)\+d\s+is the landed matched", embedding)
    convention = None
    if reservoir_match and pair_match:
        convention = ExtractedConvention(
            text=embedding,
            n_max=literals["N_MAX"],
            reservoir_q=int(reservoir_match.group(1)),
            pair_q_offset=int(pair_match.group(1)),
            audit_input_paths=source_audit_paths,
            tolerance=literals["TOLERANCE"],
            cycle322_sha256=literals["CYCLE322_SHA256"],
            cycle322_summary_marker=summary_marker,
            cycle322_terminal_marker=terminal_marker,
        )

    conditions = (
        isinstance(embedding, str)
        and "P_n selects local six-mode matter masks with bit_count(mask)=n"
        in embedding
        and "(F_d,A_d)" in embedding
        and "V_left tensor I" in embedding
        and "I tensor V_right" in embedding
        and convention is not None
        and convention.reservoir_q == 0
        and convention.pair_q_offset == 1
        and literals["N_MAX"] == FROZEN_N_MAX
        and literals["TOLERANCE"] == TOLERANCE
        and literals["CYCLE322_SHA256"] == FROZEN_CYCLE322_SHA256
        and source_audit_paths == AUDIT_INPUT_PATHS
        and literals["AUDIT_TIMEOUT_SEC"] == AUDIT_TIMEOUT_SEC
        and literals["NOTE_PATH"] == NOTE_PATH
        and summary_marker in strings
        and terminal_marker in strings
    )
    ok = bool(conditions)
    detail = {
        "audit_tuple_literal_eval": source_audit_paths,
        "cycle322_sha256": literals["CYCLE322_SHA256"],
        "embedding": embedding,
        "frozen_layer1_weight": FROZEN_LAYER1_WEIGHT,
        "frozen_layer_channel_counts": FROZEN_LAYER_CHANNEL_COUNTS,
        "n_max": literals["N_MAX"],
        "reservoir_q": None if convention is None else convention.reservoir_q,
        "pair_q": None if convention is None else "1+d",
        "summary_anchor": (FROZEN_S322_PASS, FROZEN_S322_FAIL),
    }
    return ok, detail, convention


def layer1_anchor_recount() -> tuple[bool, dict[str, object]]:
    """Recount the six U320 source branches without using the primary."""
    origin = (0, 0, 0)
    rows = []
    for direction in range(6):
        excited = np.zeros(6, dtype=complex)
        excited[direction] = 1.0
        state = U320.LinkState({origin: excited}, {})
        output, report = U320.vertex_gate(state, U320.ANGLE)
        pair = output.pair[(origin, origin)]
        emitted_weight = float(np.vdot(pair, pair).real)
        expected_index = (
            U320.REVERSE[direction],
            direction,
            direction,
        )
        support = tuple(
            tuple(int(index) for index in row)
            for row in np.argwhere(abs(pair) > 0.0)
        )
        rows.append(
            {
                "direction": direction,
                "emitted_weight": emitted_weight,
                "expected_index": expected_index,
                "support": support,
                "local_Q_residual": report["local_Q_residual"],
                "local_P_residual": report["local_P_residual"],
            }
        )

    weights = tuple(row["emitted_weight"] for row in rows)
    maximum_ulp_error = max(
        abs(weight - FROZEN_LAYER1_WEIGHT) / math.ulp(FROZEN_LAYER1_WEIGHT)
        for weight in weights
    )
    ok = (
        all(weight == FROZEN_LAYER1_WEIGHT for weight in weights)
        and all(row["support"] == (row["expected_index"],) for row in rows)
        and max(row["local_Q_residual"] for row in rows) < TOLERANCE
        and max(row["local_P_residual"] for row in rows) < TOLERANCE
    )
    return ok, {
        "directions": len(rows),
        "frozen_weight": FROZEN_LAYER1_WEIGHT,
        "weight_range": (min(weights), max(weights)),
        "maximum_ulp_error": maximum_ulp_error,
    }


def _own_hop(mask: int, direction: int) -> tuple[int, int] | None:
    target = U320.REVERSE[direction]
    if not ((mask >> direction) & 1) or ((mask >> target) & 1):
        return None
    source_parity = (mask & ((1 << direction) - 1)).bit_count()
    reduced = mask ^ (1 << direction)
    target_parity = (reduced & ((1 << target) - 1)).bit_count()
    sign = -1 if (source_parity + target_parity) % 2 else 1
    return reduced | (1 << target), sign


def layer_channel_recount() -> tuple[bool, dict[str, object]]:
    """Recount bit masks and active opposing-mode hops for n=0,1,2."""
    masks = tuple(range(1 << 6))
    mask_counts = []
    channel_counts = []
    formula_counts = []
    landed_hop_mismatches = []
    for number in range(FROZEN_N_MAX + 1):
        layer_masks = tuple(mask for mask in masks if mask.bit_count() == number)
        channels = 0
        for mask in layer_masks:
            for direction in range(6):
                own = _own_hop(mask, direction)
                landed = S322.fermion_hop(
                    mask, direction, U320.REVERSE[direction]
                )
                channels += own is not None
                if own != landed:
                    landed_hop_mismatches.append((mask, direction, own, landed))
        mask_counts.append(len(layer_masks))
        channel_counts.append(channels)
        formula_counts.append(6 * math.comb(4, number - 1) if number else 0)

    expected_masks = tuple(math.comb(6, number) for number in range(3))
    ok = (
        tuple(mask_counts) == expected_masks
        and tuple(channel_counts) == FROZEN_LAYER_CHANNEL_COUNTS
        and tuple(formula_counts) == FROZEN_LAYER_CHANNEL_COUNTS
        and set(S322.LOCAL_MASKS) == set(masks)
        and not landed_hop_mismatches
    )
    return ok, {
        "C(6,n)_mask_counts": tuple(mask_counts),
        "active_channel_counts": tuple(channel_counts),
        "formula_6*C(4,n-1)": tuple(formula_counts),
        "hop_mismatches": len(landed_hop_mismatches),
    }


def _own_local_operators(
    convention: ExtractedConvention,
) -> tuple[np.ndarray, np.ndarray, tuple[Channel, ...]]:
    dimension = len(S322.LOCAL_MASKS) * 7
    exchange = np.zeros((dimension, dimension), dtype=complex)
    channels = []
    for source_index, source_mask in enumerate(S322.LOCAL_MASKS):
        for direction in range(6):
            hopped = _own_hop(source_mask, direction)
            if hopped is None:
                continue
            target_mask, sign = hopped
            target_index = S322.LOCAL_INDEX[target_mask]
            reservoir_index = 7 * source_index + convention.reservoir_q
            pair_index = (
                7 * target_index + convention.pair_q_offset + direction
            )
            exchange[pair_index, reservoir_index] += sign
            exchange[reservoir_index, pair_index] += sign
            channels.append(
                Channel(
                    number=source_mask.bit_count(),
                    source_mask=source_mask,
                    target_mask=target_mask,
                    direction=direction,
                    sign=sign,
                    reservoir_index=reservoir_index,
                    pair_index=pair_index,
                )
            )
    vertex = expm(1j * U320.ANGLE * exchange)
    return exchange, vertex, tuple(channels)


def _mask_vector(mask: int) -> np.ndarray:
    total = np.zeros(3, dtype=int)
    for direction in range(6):
        if (mask >> direction) & 1:
            total += U320.c210.DIRECTIONS[direction]
    return total


def leakage_spot_recount(
    convention: ExtractedConvention,
) -> tuple[bool, dict[str, object]]:
    """Check every active n=1 by n=2 channel pair on the left local cell."""
    exchange, vertex, channels = _own_local_operators(convention)
    layer1 = tuple(channel for channel in channels if channel.number == 1)
    layer2 = tuple(channel for channel in channels if channel.number == 2)

    maximum_leakage = 0.0
    leakage_entries_checked = 0
    recoil_failures = []
    for left in layer1:
        for right in layer2:
            for left_index in (left.reservoir_index, left.pair_index):
                for right_index in (right.reservoir_index, right.pair_index):
                    values = (
                        exchange[left_index, right_index],
                        exchange[right_index, left_index],
                        vertex[left_index, right_index],
                        vertex[right_index, left_index],
                    )
                    leakage_entries_checked += len(values)
                    maximum_leakage = max(
                        maximum_leakage,
                        max(float(abs(value)) for value in values),
                    )

    for channel in layer1 + layer2:
        direction_vector = U320.c210.DIRECTIONS[channel.direction]
        recoil = _mask_vector(channel.target_mask) - _mask_vector(
            channel.source_mask
        )
        triple = (
            tuple(int(value) for value in recoil),
            tuple(int(value) for value in direction_vector),
            tuple(int(value) for value in direction_vector),
        )
        expected = (
            tuple(int(value) for value in -2 * direction_vector),
            tuple(int(value) for value in direction_vector),
            tuple(int(value) for value in direction_vector),
        )
        if triple != expected:
            recoil_failures.append(
                (channel.source_mask, channel.direction, triple, expected)
            )

    landed_exchange, landed_vertex, *_rest = S322.local_source_blocks(
        U320.ANGLE
    )
    operator_residuals = {
        "exchange": float(np.linalg.norm(exchange - landed_exchange)),
        "vertex": float(np.linalg.norm(vertex - landed_vertex)),
    }
    ok = (
        len(layer1) == FROZEN_LAYER_CHANNEL_COUNTS[1]
        and len(layer2) == FROZEN_LAYER_CHANNEL_COUNTS[2]
        and len(layer1) * len(layer2) == 144
        and leakage_entries_checked == 2304
        and maximum_leakage == 0.0
        and not recoil_failures
        and max(operator_residuals.values()) < TOLERANCE
    )
    return ok, {
        "cell": S322.LEFT,
        "channel_family": "all n=1 x n=2 active channel pairs",
        "channel_pairs": len(layer1) * len(layer2),
        "directed_operator_entries_checked": leakage_entries_checked,
        "maximum_cross_layer_leakage": maximum_leakage,
        "operator_residuals_against_landed": operator_residuals,
        "recoil_channels_checked": len(layer1) + len(layer2),
        "recoil_equation": "(-2d, +d, +d)",
        "recoil_failures": len(recoil_failures),
    }


def anchor_replay(
    convention: ExtractedConvention,
) -> tuple[bool, dict[str, object]]:
    """Run the landed S322 main and require its frozen 20/20 result."""
    source_path = ROOT / convention.audit_input_paths[1]
    environment = os.environ.copy()
    scripts_path = str(ROOT / "scripts")
    environment["PYTHONPATH"] = (
        scripts_path
        if not environment.get("PYTHONPATH")
        else scripts_path + os.pathsep + environment["PYTHONPATH"]
    )
    started = time.monotonic()
    try:
        completed = subprocess.run(
            [sys.executable, str(source_path)],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        return False, {
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_tail": (error.stdout or "")[-500:],
            "stderr_tail": (error.stderr or "")[-500:],
        }
    runtime = time.monotonic() - started
    pass_lines = sum(
        line.startswith("PASS ") for line in completed.stdout.splitlines()
    )
    fail_lines = sum(
        line.startswith("FAIL ") for line in completed.stdout.splitlines()
    )
    ok = (
        completed.returncode == 0
        and pass_lines == FROZEN_S322_PASS
        and fail_lines == FROZEN_S322_FAIL
        and convention.cycle322_summary_marker in completed.stdout
        and convention.cycle322_terminal_marker in completed.stdout
        and completed.stderr == ""
    )
    return ok, {
        "returncode": completed.returncode,
        "pass_lines": pass_lines,
        "fail_lines": fail_lines,
        "frozen_result": (FROZEN_S322_PASS, FROZEN_S322_FAIL),
        "runtime_seconds": round(runtime, 6),
        "stderr_tail": completed.stderr[-500:],
    }


def _target_roots(target: ast.AST) -> set[str]:
    while isinstance(target, (ast.Attribute, ast.Subscript)):
        target = target.value
    if isinstance(target, ast.Name):
        return {target.id}
    if isinstance(target, (ast.Tuple, ast.List)):
        roots: set[str] = set()
        for element in target.elts:
            roots.update(_target_roots(element))
        return roots
    return set()


def discipline() -> tuple[bool, dict[str, object]]:
    """Enforce data-only primary use and inspect its AST mutation controls."""
    _source, tree = _primary_ast()
    forbidden_writes = []
    for node in ast.walk(tree):
        targets: tuple[ast.AST, ...] = ()
        if isinstance(node, ast.Assign):
            targets = tuple(node.targets)
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
        elif isinstance(node, ast.AugAssign):
            targets = (node.target,)
        elif isinstance(node, ast.NamedExpr):
            targets = (node.target,)
        elif isinstance(node, ast.Delete):
            targets = tuple(node.targets)
        for target in targets:
            roots = _target_roots(target)
            if roots & {"U320", "S322"}:
                forbidden_writes.append((node.lineno, type(node).__name__))

    function_defs = {
        node.name: node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    misembedding = function_defs.get("misembedding_control")
    misembedding_names = (
        {node.id for node in ast.walk(misembedding) if isinstance(node, ast.Name)}
        if misembedding is not None
        else set()
    )
    misembedding_strings = (
        {
            node.value
            for node in ast.walk(misembedding)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        }
        if misembedding is not None
        else set()
    )
    literals = _literal_assignments(tree)
    convention_literals = (
        "LAYER_EMBEDDING" in literals
        and "N_MAX" in literals
        and "AUDIT_INPUT_PATHS" in literals
    )
    blocklisted_loaded = tuple(
        module for module in IMPORT_BLOCKLIST if module in sys.modules
    )
    ok = (
        IMPORT_BLOCKLIST
        == ("frontier_full_fock_unit_weight_source_2026_07_28",)
        and not blocklisted_loaded
        and not forbidden_writes
        and convention_literals
        and misembedding is not None
        and {"bad_exchange", "bad_target_mask", "commutator"}
        <= misembedding_names
        and "cross_layer_generator_amplitude" in misembedding_strings
        and "number_commutator_frobenius" in misembedding_strings
    )
    return ok, {
        "blocklist": IMPORT_BLOCKLIST,
        "blocklisted_modules_loaded": blocklisted_loaded,
        "conventions_are_literal_eval_data": convention_literals,
        "misembedding_control_in_primary_ast": misembedding is not None,
        "primary_attribute_writes": forbidden_writes,
    }


def _run(
    label: str,
    certificate: Callable[[], tuple[bool, dict[str, object]]],
) -> None:
    try:
        condition, detail = certificate()
    except Exception as error:
        condition = False
        detail = {
            "exception": type(error).__name__,
            "message": str(error),
        }
    check(label, condition, detail)


def main() -> int:
    started = time.monotonic()
    print("FULL-FOCK INDEPENDENT CHECK")
    print("primary_mode = AST data only; import blocklisted")

    convention: ExtractedConvention | None = None
    try:
        extracted_ok, extracted_detail, convention = extraction()
    except Exception as error:
        extracted_ok = False
        extracted_detail = {
            "exception": type(error).__name__,
            "message": str(error),
        }
    check("extraction()", extracted_ok, extracted_detail)

    _run("layer1_anchor_recount()", layer1_anchor_recount)
    _run("layer_channel_recount()", layer_channel_recount)
    if convention is None:
        check(
            "leakage_spot_recount()",
            False,
            "skipped because extraction produced no valid convention",
        )
        check(
            "anchor_replay()",
            False,
            "skipped because extraction produced no valid convention",
        )
    else:
        _run(
            "leakage_spot_recount()",
            lambda: leakage_spot_recount(convention),
        )
        _run("anchor_replay()", lambda: anchor_replay(convention))
    _run("discipline()", discipline)

    runtime = time.monotonic() - started
    print(
        "SUMMARY",
        {
            "pass": PASS,
            "fail": FAIL,
            "runtime_seconds": round(runtime, 6),
        },
    )
    print(
        "FINAL",
        "ALL_PASS" if FAIL == 0 else "HONEST_FAIL",
        f"{PASS}/{PASS + FAIL}",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
