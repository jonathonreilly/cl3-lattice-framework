#!/usr/bin/env python3
"""Bounded full-Fock lift of the landed Cycle-320 unit-weight source.

The construction is deliberately narrow.  It combines the Cycle-322 local
fermionic Fock hop with the Cycle-320 interpretation of each directional
source branch as the matched pair (F_d, A_d), with unit vector weight on
each member.  Occupation number is truncated only for the exhaustive
certificate; the landed 64-mask operator itself is left unchanged.

This certifies the source/recoil/reciprocity algebra on the landed two-cell
fixture.  It does not claim a new recurrent physical encoding or an
auxiliary catch-up law for simultaneous carriers.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import numpy as np


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/FULL_FOCK_UNIT_WEIGHT_SOURCE_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322


N_MAX = 2
TOLERANCE = 3e-10
CYCLE322_SHA256 = "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75"
LAYER_EMBEDDING = (
    "P_n selects local six-mode matter masks with bit_count(mask)=n; "
    "q=0 is the endpoint reservoir and q=1+d is the landed matched "
    "unit-weight pair (F_d,A_d).  The two-cell factors are V_left tensor I "
    "and I tensor V_right in S322.JOINT_INDEX, so the spectator mask and "
    "every other number sector are unchanged."
)

PASS = 0
FAIL = 0
FAILED_LABELS: list[str] = []


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        FAILED_LABELS.append(label)
        print("FAIL", label, "::", detail)


def mask_vector(mask: int) -> np.ndarray:
    return sum(
        (
            U320.c210.DIRECTIONS[direction]
            for direction in range(6)
            if (mask >> direction) & 1
        ),
        start=np.zeros(3, dtype=int),
    )


def component_operators() -> tuple[
    tuple[np.ndarray, ...],
    tuple[np.ndarray, ...],
    tuple[np.ndarray, ...],
    tuple[np.ndarray, ...],
]:
    """Split S322's coefficient-two diagonal into two landed unit weights."""
    matter = []
    mediator = []
    auxiliary = []
    total = []
    for axis in range(3):
        matter_values = []
        mediator_values = []
        auxiliary_values = []
        for mask in S322.LOCAL_MASKS:
            base = float(mask_vector(mask)[axis])
            matter_values.extend([base] * 7)
            mediator_values.append(0.0)
            auxiliary_values.append(0.0)
            mediator_values.extend(
                float(U320.c210.DIRECTIONS[direction, axis])
                for direction in range(6)
            )
            auxiliary_values.extend(
                float(U320.c210.DIRECTIONS[direction, axis])
                for direction in range(6)
            )
        matter_axis = np.diag(matter_values)
        mediator_axis = np.diag(mediator_values)
        auxiliary_axis = np.diag(auxiliary_values)
        matter.append(matter_axis)
        mediator.append(mediator_axis)
        auxiliary.append(auxiliary_axis)
        total.append(matter_axis + mediator_axis + auxiliary_axis)
    return tuple(matter), tuple(mediator), tuple(auxiliary), tuple(total)


def layer_indices(number: int) -> list[int]:
    return [
        7 * local_index + q_index
        for local_index, mask in enumerate(S322.LOCAL_MASKS)
        if mask.bit_count() == number
        for q_index in range(7)
    ]


def landed_one_carrier_rows(vertex: np.ndarray) -> tuple[list[dict], float]:
    """Use U320.LinkState and compare its six numerical response rows."""
    origin = (0, 0, 0)
    rows = []
    maximum_residual = 0.0
    for direction in range(6):
        excited = np.zeros(6, dtype=complex)
        excited[direction] = 1.0
        landed_input = U320.LinkState({origin: excited}, {})
        landed_output, _report = U320.vertex_gate(landed_input, U320.ANGLE)
        landed_excited = landed_output.excited[origin]
        landed_pair = landed_output.pair[(origin, origin)]

        pair_probabilities = abs(landed_pair) ** 2
        landed_matter = (
            abs(landed_excited) ** 2
            + np.sum(pair_probabilities, axis=(1, 2))
        ) @ U320.c210.DIRECTIONS
        landed_mediator = (
            np.sum(pair_probabilities, axis=(0, 2)) @ U320.c210.DIRECTIONS
        )
        landed_auxiliary = (
            np.sum(pair_probabilities, axis=(0, 1)) @ U320.c210.DIRECTIONS
        )

        source_index = S322.LOCAL_INDEX[1 << direction]
        local_input = np.zeros(448, dtype=complex)
        local_input[7 * source_index] = 1.0
        local_output = vertex @ local_input
        lifted_matter = np.zeros(3)
        lifted_mediator = np.zeros(3)
        lifted_auxiliary = np.zeros(3)
        for local_index, mask in enumerate(S322.LOCAL_MASKS):
            for q_index in range(7):
                probability = float(abs(local_output[7 * local_index + q_index]) ** 2)
                lifted_matter += probability * mask_vector(mask)
                if q_index:
                    lifted_mediator += (
                        probability * U320.c210.DIRECTIONS[q_index - 1]
                    )
                    lifted_auxiliary += (
                        probability * U320.c210.DIRECTIONS[q_index - 1]
                    )

        initial = U320.c210.DIRECTIONS[direction].astype(float)
        component_residual = max(
            float(np.max(abs(lifted_matter - landed_matter))),
            float(np.max(abs(lifted_mediator - landed_mediator))),
            float(np.max(abs(lifted_auxiliary - landed_auxiliary))),
        )
        maximum_residual = max(maximum_residual, component_residual)
        emitted_index = (
            7 * S322.LOCAL_INDEX[1 << U320.REVERSE[direction]]
            + 1
            + direction
        )
        rows.append(
            {
                "direction": direction,
                "emitted_weight": float(abs(local_output[emitted_index]) ** 2),
                "matter_recoil": [
                    float(value) for value in (lifted_matter - initial)
                ],
                "mediator_flux": [float(value) for value in lifted_mediator],
                "auxiliary_flux": [float(value) for value in lifted_auxiliary],
            }
        )
    return rows, maximum_residual


def per_layer_certificates(
    exchange: np.ndarray,
    vertex: np.ndarray,
) -> tuple[list[dict], float, float]:
    """Certify exact generator ledgers and reciprocal number blocks."""
    rows = []
    maximum_ledger_residual = 0.0
    maximum_reciprocity_residual = 0.0
    for number in range(N_MAX + 1):
        indices = layer_indices(number)
        block = vertex[np.ix_(indices, indices)]
        channels = 0
        emitted_weights = []
        layer_ledger_residual = 0.0
        for source_index, mask in enumerate(S322.LOCAL_MASKS):
            if mask.bit_count() != number:
                continue
            for direction in range(6):
                hopped = S322.fermion_hop(
                    mask, direction, U320.REVERSE[direction]
                )
                if hopped is None:
                    continue
                target_mask, sign = hopped
                target_index = S322.LOCAL_INDEX[target_mask]
                reservoir_column = 7 * source_index
                pair_row = 7 * target_index + 1 + direction
                edge_exact = (
                    exchange[pair_row, reservoir_column] == sign
                    and exchange[reservoir_column, pair_row] == sign
                )
                matter_recoil = mask_vector(target_mask) - mask_vector(mask)
                mediator_flux = U320.c210.DIRECTIONS[direction]
                auxiliary_flux = U320.c210.DIRECTIONS[direction]
                expected_recoil = -2 * U320.c210.DIRECTIONS[direction]
                residual = max(
                    float(np.max(abs(matter_recoil - expected_recoil))),
                    float(
                        np.max(
                            abs(
                                matter_recoil
                                + mediator_flux
                                + auxiliary_flux
                            )
                        )
                    ),
                    0.0 if edge_exact else 1.0,
                )
                layer_ledger_residual = max(layer_ledger_residual, residual)
                emitted_weights.append(
                    float(abs(vertex[pair_row, reservoir_column]) ** 2)
                )
                channels += 1
        reciprocity_residual = float(np.linalg.norm(block.T - block))
        unitarity_residual = float(
            np.linalg.norm(block.conj().T @ block - np.eye(len(indices)))
        )
        maximum_ledger_residual = max(
            maximum_ledger_residual, layer_ledger_residual
        )
        maximum_reciprocity_residual = max(
            maximum_reciprocity_residual, reciprocity_residual
        )
        rows.append(
            {
                "active_channels": channels,
                "dimension": len(indices),
                "emitted_weight_max": max(emitted_weights, default=0.0),
                "emitted_weight_min": min(emitted_weights, default=0.0),
                "generator_ledger_residual": layer_ledger_residual,
                "number": number,
                "reciprocity_residual": reciprocity_residual,
                "unitarity_residual": unitarity_residual,
                "vacuum_source_is_identity": number != 0
                or float(np.linalg.norm(block - np.eye(len(indices)))) == 0.0,
            }
        )
    return rows, maximum_ledger_residual, maximum_reciprocity_residual


def exhaustive_two_cell_independence(
    vertex: np.ndarray,
) -> tuple[int, int, float]:
    """Exhaust all active q columns on the n<=2 two-cell matter fixture."""
    allowed = [
        index
        for index, mask in enumerate(S322.LOCAL_MASKS)
        if mask.bit_count() <= N_MAX
    ]
    supports = {
        (local_index, q_index): np.flatnonzero(
            abs(vertex[:, 7 * local_index + q_index]) > 2e-13
        )
        for local_index in allowed
        for q_index in range(7)
    }
    failures = 0
    columns_checked = 0
    maximum_cross_layer_amplitude = 0.0
    for endpoint in range(2):
        for local_index in allowed:
            source_number = S322.LOCAL_MASKS[local_index].bit_count()
            for spectator_index in allowed:
                joint_index = (
                    S322.JOINT_INDEX[(local_index, spectator_index)]
                    if endpoint == 0
                    else S322.JOINT_INDEX[(spectator_index, local_index)]
                )
                left_number, _left_label, right_number, _right_label = (
                    S322.LABELS[joint_index]
                )
                expected_numbers = (
                    (source_number, S322.LOCAL_MASKS[spectator_index].bit_count())
                    if endpoint == 0
                    else (S322.LOCAL_MASKS[spectator_index].bit_count(), source_number)
                )
                if (left_number, right_number) != expected_numbers:
                    failures += 1
                for q_index in range(7):
                    columns_checked += 1
                    for row in supports[(local_index, q_index)]:
                        target_number = S322.LOCAL_MASKS[row // 7].bit_count()
                        if target_number != source_number:
                            failures += 1
                            maximum_cross_layer_amplitude = max(
                                maximum_cross_layer_amplitude,
                                float(
                                    abs(
                                        vertex[
                                            row,
                                            7 * local_index + q_index,
                                        ]
                                    )
                                ),
                            )
    return columns_checked, failures, maximum_cross_layer_amplitude


def superposed_layer_control() -> dict[str, float]:
    """Exercise S322.LogicalState on a coherent n=1/n=2 source state."""
    vacuum = S322.LOCAL_INDEX[0]
    one = S322.LOCAL_INDEX[1 << 0]
    two = S322.LOCAL_INDEX[(1 << 0) | (1 << 2)]
    matter = np.zeros(4096, dtype=complex)
    matter[S322.JOINT_INDEX[(one, vacuum)]] = 1 / np.sqrt(2)
    matter[S322.JOINT_INDEX[(two, vacuum)]] = 1j / np.sqrt(2)
    state = S322.LogicalState({S322.q_reservoir(0): matter})

    before_weights = layer_weights(state, endpoint=0)
    emitted = S322.apply_source(state, 0, angle=U320.ANGLE)
    after_weights = layer_weights(emitted, endpoint=0)
    recovered = S322.apply_source(
        emitted, 0, angle=U320.ANGLE, inverse=True
    )
    return {
        "inverse_residual": S322.state_residual(recovered, state),
        "layer_weight_residual": max(
            abs(after_weights[number] - before_weights[number])
            for number in range(N_MAX + 1)
        ),
        "norm_residual": abs(S322.state_norm(emitted) - S322.state_norm(state)),
    }


def layer_weights(state: S322.LogicalState, endpoint: int) -> dict[int, float]:
    weights = {number: 0.0 for number in range(N_MAX + 1)}
    for vector in state.values():
        for index, amplitude in enumerate(vector):
            if amplitude == 0:
                continue
            left_number, _left, right_number, _right = S322.LABELS[index]
            number = left_number if endpoint == 0 else right_number
            if number <= N_MAX:
                weights[number] += float(abs(amplitude) ** 2)
    return weights


def reciprocal_superposition(vertex: np.ndarray, exchange: np.ndarray) -> dict[str, float]:
    one = S322.LOCAL_INDEX[1 << 0]
    two = S322.LOCAL_INDEX[(1 << 0) | (1 << 2)]
    reservoir = np.zeros(448, dtype=complex)
    reservoir[7 * one] = 1 / np.sqrt(2)
    reservoir[7 * two] = 1 / np.sqrt(2)
    paired = exchange @ reservoir
    paired /= np.linalg.norm(paired)
    forward = np.vdot(paired, vertex @ reservoir)
    reverse = np.vdot(reservoir, vertex @ paired)
    return {
        "forward_abs": float(abs(forward)),
        "matrix_element_residual": float(abs(forward - reverse)),
        "reverse_abs": float(abs(reverse)),
    }


def misembedding_control(exchange: np.ndarray) -> dict[str, float | int]:
    """Move the smallest n=2 target into n=1 and expose the number leak."""
    source_mask = (1 << 0) | (1 << 2)
    source_index = S322.LOCAL_INDEX[source_mask]
    proper_target_mask, sign = S322.fermion_hop(
        source_mask, 0, U320.REVERSE[0]
    )
    proper_row = 7 * S322.LOCAL_INDEX[proper_target_mask] + 1
    bad_target_mask = 1 << U320.REVERSE[0]
    bad_row = 7 * S322.LOCAL_INDEX[bad_target_mask] + 1
    source_column = 7 * source_index

    bad_exchange = exchange.copy()
    bad_exchange[proper_row, source_column] = 0
    bad_exchange[source_column, proper_row] = 0
    bad_exchange[bad_row, source_column] = sign
    bad_exchange[source_column, bad_row] = sign
    _exchange, _vertex, _charge, number, _momenta = (
        S322.local_source_blocks(U320.ANGLE)
    )
    commutator = bad_exchange @ number - number @ bad_exchange
    return {
        "cross_layer_generator_amplitude": float(
            abs(bad_exchange[bad_row, source_column])
        ),
        "number_commutator_frobenius": float(np.linalg.norm(commutator)),
        "source_number": source_mask.bit_count(),
        "target_number": bad_target_mask.bit_count(),
    }


def cycle322_anchor() -> dict[str, object]:
    source_path = ROOT / AUDIT_INPUT_PATHS[1]
    before = hashlib.sha256(source_path.read_bytes()).hexdigest()
    environment = os.environ.copy()
    scripts_path = str(ROOT / "scripts")
    environment["PYTHONPATH"] = (
        scripts_path
        if not environment.get("PYTHONPATH")
        else scripts_path + os.pathsep + environment["PYTHONPATH"]
    )
    started = time.monotonic()
    completed = subprocess.run(
        [sys.executable, str(source_path)],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    runtime = time.monotonic() - started
    after = hashlib.sha256(source_path.read_bytes()).hexdigest()
    return {
        "returncode": completed.returncode,
        "runtime_seconds": round(runtime, 6),
        "sha256_after": after,
        "sha256_before": before,
        "stderr_empty": completed.stderr == "",
        "summary_pinned": "SUMMARY {'pass': 20, 'fail': 0}" in completed.stdout,
        "terminal_marker_pinned": (
            "RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED"
            in completed.stdout
        ),
    }


def main() -> int:
    started = time.monotonic()
    print("FULL-FOCK CYCLE-320 UNIT-WEIGHT AUXILIARY SOURCE")
    print("occupancy_truncation_n_max =", N_MAX)
    print("layer_embedding =", LAYER_EMBEDDING)
    print("interpretation = dimensionless source/recoil algebra only")

    exchange, vertex, charge, number, landed_total_momenta = (
        S322.local_source_blocks(U320.ANGLE)
    )
    _matter_ops, _mediator_ops, _auxiliary_ops, unit_total_ops = (
        component_operators()
    )

    split_matches_landed = all(
        np.array_equal(unit_total_ops[axis], landed_total_momenta[axis])
        for axis in range(3)
    )
    generator_commutators = tuple(
        float(
            np.linalg.norm(
                exchange @ unit_total_ops[axis]
                - unit_total_ops[axis] @ exchange
            )
        )
        for axis in range(3)
    )
    vertex_commutators = tuple(
        float(
            np.linalg.norm(
                vertex @ unit_total_ops[axis]
                - unit_total_ops[axis] @ vertex
            )
        )
        for axis in range(3)
    )
    check(
        "the landed coefficient-two diagonal splits exactly into mediator weight one plus auxiliary weight one",
        split_matches_landed
        and max(generator_commutators) == 0.0
        and max(vertex_commutators) < TOLERANCE,
        {
            "generator_P_commutators": generator_commutators,
            "unit_weights": (1, 1, 1),
            "vertex_P_commutators": vertex_commutators,
        },
    )
    check(
        "the reused source preserves Q and local occupation number",
        float(np.linalg.norm(vertex @ charge - charge @ vertex)) == 0.0
        and float(np.linalg.norm(vertex @ number - number @ vertex)) == 0.0,
        {
            "Q_commutator": float(
                np.linalg.norm(vertex @ charge - charge @ vertex)
            ),
            "number_commutator": float(
                np.linalg.norm(vertex @ number - number @ vertex)
            ),
        },
    )

    landed_rows, anchor_residual = landed_one_carrier_rows(vertex)
    anchor_weight_min = min(row["emitted_weight"] for row in landed_rows)
    anchor_weight_max = max(row["emitted_weight"] for row in landed_rows)
    check(
        "layer 1 reproduces all six landed U320 LinkState recoil rows",
        anchor_residual < TOLERANCE
        and abs(anchor_weight_min - np.sin(U320.ANGLE) ** 2) < TOLERANCE
        and abs(anchor_weight_max - np.sin(U320.ANGLE) ** 2) < TOLERANCE,
        {
            "emitted_weight_range": (anchor_weight_min, anchor_weight_max),
            "maximum_component_residual": anchor_residual,
            "matter_recoil_magnitude": 2 * anchor_weight_min,
            "mediator_flux_magnitude": anchor_weight_min,
            "auxiliary_flux_magnitude": anchor_weight_min,
        },
    )

    layer_rows, ledger_residual, reciprocity_residual = per_layer_certificates(
        exchange, vertex
    )
    check(
        "every allowed channel through n_max has the exact landed unit-weight recoil ledger",
        ledger_residual == 0.0
        and all(row["vacuum_source_is_identity"] for row in layer_rows),
        {
            "layers": [
                {
                    "active_channels": row["active_channels"],
                    "generator_ledger_residual": row[
                        "generator_ledger_residual"
                    ],
                    "number": row["number"],
                }
                for row in layer_rows
            ],
            "recoil_equation": "Delta P_matter=-2 d; P_F=+d; P_A=+d",
        },
    )

    columns_checked, independence_failures, cross_layer_amplitude = (
        exhaustive_two_cell_independence(vertex)
    )
    check(
        "the two-cell truncated Fock space is exhaustively layer-independent",
        columns_checked == 6776
        and independence_failures == 0
        and cross_layer_amplitude == 0.0,
        {
            "active_q_columns_checked": columns_checked,
            "cross_layer_failures": independence_failures,
            "joint_matter_states": 22**2,
            "maximum_cross_layer_amplitude": cross_layer_amplitude,
        },
    )

    superposed = superposed_layer_control()
    reciprocal = reciprocal_superposition(vertex, exchange)
    check(
        "reciprocity holds in every layer and on a coherent n=1 plus n=2 state",
        reciprocity_residual < TOLERANCE
        and max(superposed.values()) < TOLERANCE
        and reciprocal["matrix_element_residual"] < TOLERANCE
        and reciprocal["forward_abs"] > 0.1,
        {
            "maximum_layer_reciprocity_residual": reciprocity_residual,
            "superposed_state": superposed,
            "superposed_matrix_element": reciprocal,
        },
    )

    bad = misembedding_control(exchange)
    check(
        "a deliberate n=2 to n=1 mis-embedding breaks layer independence",
        bad["source_number"] == 2
        and bad["target_number"] == 1
        and bad["cross_layer_generator_amplitude"] == 1.0
        and bad["number_commutator_frobenius"] > 1.4,
        bad,
    )

    anchor = cycle322_anchor()
    check(
        "the byte-pinned Cycle-322 harness reruns unchanged",
        anchor["sha256_before"] == CYCLE322_SHA256
        and anchor["sha256_after"] == CYCLE322_SHA256
        and anchor["returncode"] == 0
        and anchor["stderr_empty"]
        and anchor["summary_pinned"]
        and anchor["terminal_marker_pinned"],
        anchor,
    )

    runtime = time.monotonic() - started
    achieved = FAIL == 0
    package = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "certificate_failures": FAILED_LABELS,
        "cycle322_anchor": {
            "returncode": anchor["returncode"],
            "runtime_seconds": anchor["runtime_seconds"],
            "sha256": anchor["sha256_after"],
        },
        "full_fock_construction_achieved": achieved,
        "layer_embedding": LAYER_EMBEDDING,
        "layer_rows": layer_rows,
        "n_max": N_MAX,
        "note_path": NOTE_PATH,
        "obstruction": None,
        "runtime_seconds": round(runtime, 6),
        "scope": (
            "local full-Fock source algebra on the landed two-cell fixture; "
            "no new recurrent simultaneous-carrier transport claim"
        ),
        "summary": {"fail": FAIL, "pass": PASS},
    }
    print("FINAL_JSON", json.dumps(package, sort_keys=True))

    # A failed certificate without a numerically frozen obstruction would be
    # an incomplete/dishonest package, so only that state exits nonzero.
    return 0 if achieved else 1


if __name__ == "__main__":
    raise SystemExit(main())
