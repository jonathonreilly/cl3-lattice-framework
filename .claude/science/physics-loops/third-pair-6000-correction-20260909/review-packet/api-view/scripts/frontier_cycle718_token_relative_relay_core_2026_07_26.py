#!/usr/bin/env python3
"""Cycle-718 token-relative Cycle-713 carrier-relay support core.

Two edge-exclusive link tubes distinguish allocator handoff from carrier-only
relay.  The same decoded word can therefore deliver a new Cycle-713 event from
the fixed matter seam to an allocator token that has advanced through two
banks, then return and uncompute the carrier at its source.

The tested domain stops at four appended events in six available cells.
Destination backpressure and replacement of the structural bank-index prefix
remain open, so this is not a completed recurrent compiler.
"""
from __future__ import annotations

from hashlib import sha256
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26 as X


A = X.A
P = X.P
TOL = 4.0e-10
MATTER_WIDTH = 41
BANK_BASES = (41, 172, 303)
AFTER_BANKS = 434


def link_layout() -> tuple[tuple[int, tuple[int, ...], int, tuple[int, ...]], ...]:
    links = []
    cursor = AFTER_BANKS
    for _edge in range(2):
        handoff_latch = cursor
        handoff_work = tuple(range(cursor + 1, cursor + 191))
        relay_latch = cursor + 191
        relay_work = tuple(range(relay_latch + 1, relay_latch + 191))
        cursor = relay_latch + 191
        links.append((handoff_latch, handoff_work, relay_latch, relay_work))
    return tuple(links)


LINKS = link_layout()
TOTAL_WIRES = LINKS[-1][2] + 191


def offset(gate: A.Gate, base: int) -> A.Gate:
    return A.Gate(gate.kind, tuple(base + wire for wire in gate.wires))


def mapped_handoff_gate(gate: A.Gate, edge: int) -> A.Gate:
    handoff_latch, handoff_work, _relay_latch, _relay_work = LINKS[edge]
    wires = []
    for wire in gate.wires:
        if wire < A.N:
            wires.append(BANK_BASES[edge] + wire)
        elif wire < 2 * A.N:
            wires.append(BANK_BASES[edge + 1] + wire - A.N)
        elif wire == P.LATCH:
            wires.append(handoff_latch)
        else:
            wires.append(handoff_work[wire - (P.LATCH + 1)])
    return A.Gate(gate.kind, tuple(wires))


def controlled_latch(
    target: int,
    work: tuple[int, ...],
    positives: tuple[int, ...],
    negatives: tuple[int, ...],
) -> tuple[A.Gate, ...]:
    word: list[A.Gate] = []
    word.extend(A.x(wire) for wire in negatives)
    word.extend(A.mcx(positives + negatives, target, work))
    word.extend(A.x(wire) for wire in reversed(negatives))
    return tuple(word)


def fredkin(control: int, left: int, right: int) -> tuple[A.Gate, ...]:
    return (A.cn(right, left), A.tof(control, left, right), A.cn(right, left))


def relay_predicate(edge: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Carrier at a tokenless left bank, clean carrier interface at right."""
    left, right = BANK_BASES[edge], BANK_BASES[edge + 1]
    positives = (
        left + A.POINTER, left + A.DIRECTION_OK,
        left + A.BINDER, left + A.ACTUAL, left + A.ADMISS, left + A.LAW,
        right + A.BINDER, right + A.ACTUAL, right + A.ADMISS, right + A.LAW,
    )
    negatives = tuple(left + wire for wire in (
        *A.TOKEN, *A.ZERO_WORK, A.TOKEN_OK,
    )) + tuple(right + wire for wire in (
        *A.ZERO_WORK, A.TOKEN_OK,
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
    ))
    return positives, negatives


def relay_latch_word(edge: int) -> tuple[A.Gate, ...]:
    _handoff_latch, _handoff_work, relay_latch, relay_work = LINKS[edge]
    positives, negatives = relay_predicate(edge)
    return controlled_latch(
        relay_latch, relay_work, positives, negatives
    )


def relay_swap_word(edge: int) -> tuple[A.Gate, ...]:
    left, right = BANK_BASES[edge], BANK_BASES[edge + 1]
    relay_latch = LINKS[edge][2]
    word: list[A.Gate] = []
    for wire in (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK):
        word.extend(fredkin(relay_latch, left + wire, right + wire))
    return tuple(word)


def source_compute_word() -> tuple[A.Gate, ...]:
    left = BANK_BASES[0]
    return (
        A.cn(X.SOURCE_POINTER, left + A.POINTER),
        A.tof(X.SOURCE_POINTER, X.RIGHT_ENDPOINT, left + A.U_TO_V),
        A.tof(X.SOURCE_POINTER, X.LEFT_ENDPOINT, left + A.V_TO_U),
        *tuple(offset(gate, left) for gate in P.direction_witness_word()),
    )


def source_uncompute_word() -> tuple[A.Gate, ...]:
    left = BANK_BASES[0]
    return (
        *tuple(
            offset(gate, left) for gate in reversed(P.direction_witness_word())
        ),
        A.tof(X.SOURCE_POINTER, X.LEFT_ENDPOINT, left + A.V_TO_U),
        A.tof(X.SOURCE_POINTER, X.RIGHT_ENDPOINT, left + A.U_TO_V),
        A.cn(X.SOURCE_POINTER, left + A.POINTER),
        A.cn(X.LEFT_ENDPOINT, X.SOURCE_POINTER),
        A.cn(X.RIGHT_ENDPOINT, X.SOURCE_POINTER),
    )


def classical_word(
    deletion: str | None = None,
    edge_local_predecessor: bool = False,
) -> tuple[A.Gate, ...]:
    stages: list[tuple[str, tuple[A.Gate, ...]]] = [
        ("source_compute", source_compute_word()),
    ]
    for edge in range(2):
        stages.append((
            f"handoff_forward_{edge}",
            tuple(
                mapped_handoff_gate(gate, edge)
                for gate in P.pre_latch_word() + P.forward_transfer_word()
            ),
        ))
        stages.append((f"relay_latch_forward_{edge}", relay_latch_word(edge)))
        stages.append((f"relay_swap_forward_{edge}", relay_swap_word(edge)))
    for bank_index, base in enumerate(BANK_BASES):
        if edge_local_predecessor:
            packet = tuple(offset(gate, base) for gate in P.safe_packet_body_word())
            if bank_index:
                # On the first packet after a handoff, retained local HEAD=1
                # already writes predecessor-cell 1.  This edge-owned bit says
                # that predecessor is across the left edge, not in this bank.
                packet += (
                    A.cn(
                        LINKS[bank_index - 1][0],
                        base + int(A.CELLS[0]["pred"][1]),
                    ),
                )
        else:
            packet = tuple(
                offset(gate, base)
                for gate in P.packet_word_for_bank(bank_index)
            )
        stages.append((
            f"packet_{bank_index}",
            packet,
        ))
    for edge in reversed(range(2)):
        stages.append((f"relay_swap_return_{edge}", relay_swap_word(edge)))
        stages.append((f"relay_latch_return_{edge}", relay_latch_word(edge)))
        stages.append((
            f"handoff_return_{edge}",
            tuple(
                mapped_handoff_gate(gate, edge)
                for gate in P.carrier_return_word() + P.post_latch_word()
            ),
        ))
    stages.append(("source_uncompute", source_uncompute_word()))

    word: list[A.Gate] = []
    for label, stage in stages:
        if deletion == "edge0_relay_first_swap" and label == "relay_swap_forward_0":
            word.extend(stage[3:])
        elif deletion == "edge1_handoff_token" and label == "handoff_forward_1":
            pre_length = len(P.pre_latch_word())
            word.extend(stage[:pre_length])
            word.extend(stage[pre_length + 3:])
        elif deletion == "source_pointer_cleanup" and label == "source_uncompute":
            word.extend(stage[:-1])
        else:
            word.extend(stage)
    return tuple(word)


def packed_basis(source: int) -> int:
    banks = (P.full_bank(0), P.inactive_bank(), P.inactive_bank())
    basis = source
    for base, bank in zip(BANK_BASES, banks):
        for wire, value in enumerate(bank):
            basis |= value << (base + wire)
    return basis


def bank_bits(basis: int, base: int) -> tuple[int, ...]:
    return tuple((basis >> (base + wire)) & 1 for wire in range(A.N))


def instrument_tagged(
    state: dict[tuple[int, tuple[int, ...]], complex], decoded_word: tuple
) -> dict[tuple[int, tuple[int, ...]], complex]:
    output: dict[tuple[int, tuple[int, ...]], complex] = {}
    for (basis, history), amplitude in state.items():
        column = C713.apply_sparse_word({basis: amplitude}, decoded_word)
        for target, value in column.items():
            if (target >> X.SOURCE_POINTER) & 1:
                orientation = (
                    1 if ((target >> X.RIGHT_ENDPOINT) & 1)
                    and not ((target >> X.LEFT_ENDPOINT) & 1) else -1
                )
                next_history = history + (orientation,)
            else:
                next_history = history
            key = (target, next_history)
            output[key] = output.get(key, 0.0j) + value
    return {
        key: value for key, value in output.items() if abs(value) > 1.0e-13
    }


def apply_recurrent(
    source: int,
    applications: int,
    decoded_word: tuple,
    packet_word: tuple[A.Gate, ...],
) -> dict[tuple[int, tuple[int, ...]], complex]:
    state = {(packed_basis(source), ()): 1.0 + 0.0j}
    for _application in range(applications):
        state = instrument_tagged(state, decoded_word)
        updated: dict[tuple[int, tuple[int, ...]], complex] = {}
        for (basis, history), amplitude in state.items():
            column = X.apply_classical_sparse({basis: amplitude}, packet_word)
            for target, value in column.items():
                key = (target, history)
                updated[key] = updated.get(key, 0.0j) + value
        state = {
            key: value for key, value in updated.items()
            if abs(value) > 1.0e-13
        }
    return state


def state_issues(basis: int, history: tuple[int, ...]) -> tuple[str, ...]:
    banks = tuple(bank_bits(basis, base) for base in BANK_BASES)
    issues: list[str] = []
    event_count = len(history)
    packet_count = sum(
        bank[int(layout["valid"])] for bank in banks for layout in A.CELLS
    )
    if packet_count != 2 + event_count:
        issues.append("packet_count")
    token_banks = [
        index for index, bank in enumerate(banks)
        if sum(bank[wire] for wire in A.TOKEN)
    ]
    expected_bank = 0 if event_count == 0 else 1 + (event_count - 1) // 2
    if token_banks != [expected_bank]:
        issues.append("token")
    for event, orientation in enumerate(history):
        packet = A.packet_projection(banks[1 + event // 2], event % 2)
        rotor_before = 2 + event
        expected = {
            "identity": event % 2,
            "predecessor": 1 + event,
            "rotor_before": rotor_before,
            "rotor": (rotor_before + 1) % 16,
            "carry": int(rotor_before == 15),
            "delta_mask": 66,
            "endpoint": 1,
            "binder": 1,
            "valid": 1,
            "orientation": orientation,
            "actuality": 1,
            "admissibility": 1,
            "law_domain": 1,
        }
        if packet != expected:
            issues.append("packet")
            break
    endpoint_dirty = any((basis >> wire) & 1 for wire in (38, 39, 40))
    bank_dirty = any(
        (basis >> (base + wire)) & 1
        for base in BANK_BASES
        for wire in (
            A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
            *A.ZERO_WORK, A.TOKEN_OK,
        )
    )
    link_dirty = any(
        (basis >> wire) & 1 for wire in range(AFTER_BANKS, TOTAL_WIRES)
    )
    if endpoint_dirty or bank_dirty or link_dirty:
        issues.append("dirty_auxiliary")
    return tuple(issues)


def vector_residual(
    left: dict[tuple[int, tuple[int, ...]], complex],
    right: dict[tuple[int, tuple[int, ...]], complex],
) -> float:
    return math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    ))


def domain_certificate() -> tuple[dict[str, object], dict[int, dict]]:
    decoded_word, _qr = C713.instrumented_decoded_word(2)
    complete = classical_word()
    sources = tuple(source for source in range(1 << 12) if source.bit_count() <= 2)
    reports = {}
    outputs: dict[int, dict] = {}
    for applications in (2, 4):
        maximum_bad_weight = maximum_norm = maximum_leakage = 0.0
        maximum_support = 0
        application_outputs = {}
        for source in sources:
            state = apply_recurrent(source, applications, decoded_word, complete)
            application_outputs[source] = state
            bad_weight = sum(
                abs(amplitude) ** 2
                for (basis, history), amplitude in state.items()
                if state_issues(basis, history)
            )
            norm = abs(sum(abs(value) ** 2 for value in state.values()) - 1.0)
            leakage = sum(
                abs(amplitude) ** 2
                for (basis, _history), amplitude in state.items()
                if (basis & ((1 << 12) - 1)).bit_count() != source.bit_count()
            )
            maximum_bad_weight = max(maximum_bad_weight, bad_weight)
            maximum_norm = max(maximum_norm, norm)
            maximum_leakage = max(maximum_leakage, leakage)
            maximum_support = max(maximum_support, len(state))
        reports[applications] = {
            "sources_N_le_2": len(sources),
            "applications": applications,
            "maximum_bad_history_or_auxiliary_probability_weight": maximum_bad_weight,
            "maximum_norm_residual": maximum_norm,
            "maximum_particle_number_leakage": maximum_leakage,
            "maximum_sparse_support": maximum_support,
        }
        outputs[applications] = application_outputs
    return reports, outputs


def deletion_certificate(
    complete_outputs: dict[int, dict]
) -> dict[str, float]:
    decoded_word, _qr = C713.instrumented_decoded_word(2)
    sources = tuple(1 << mode for mode in range(12))
    report = {}
    for deletion in (
        "edge0_relay_first_swap",
        "edge1_handoff_token",
        "source_pointer_cleanup",
    ):
        damaged_word = classical_word(deletion)
        maximum = 0.0
        for source in sources:
            damaged = apply_recurrent(source, 4, decoded_word, damaged_word)
            maximum = max(
                maximum, vector_residual(damaged, complete_outputs[source])
            )
        report[deletion] = maximum
    return report


def main() -> int:
    domains, outputs = domain_certificate()
    deletions = deletion_certificate(outputs[4])
    complete = classical_word()
    checks = {
        "two_identical_applications": (
            domains[2]["maximum_bad_history_or_auxiliary_probability_weight"] < TOL
            and domains[2]["maximum_norm_residual"] < TOL
            and domains[2]["maximum_particle_number_leakage"] < TOL
        ),
        "four_identical_applications": (
            domains[4]["maximum_bad_history_or_auxiliary_probability_weight"] < TOL
            and domains[4]["maximum_norm_residual"] < TOL
            and domains[4]["maximum_particle_number_leakage"] < TOL
        ),
        "active_deletions": all(value > 1.0e-3 for value in deletions.values()),
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "domains": domains,
        "deletion_residuals": deletions,
        "decoded_Cycle713_gates_per_application": len(
            C713.instrumented_decoded_word(2)[0]
        ),
        "classical_gates_per_application": len(complete),
        "assigned_decoded_registers": TOTAL_WIRES,
        "edge_tubes": [
            {
                "handoff_latch": handoff_latch,
                "handoff_work": len(handoff_work),
                "relay_latch": relay_latch,
                "relay_work": len(relay_work),
            }
            for handoff_latch, handoff_work, relay_latch, relay_work in LINKS
        ],
        "supplied": [
            "decoded Cycle-713 two-cell matter word at one fixed source seam",
            "three-bank chain with one token, blank downstream banks, and clean link tubes",
            "BINDER/ACTUAL/ADMISS/LAW event inputs and fixed forward/reverse edge order",
            "six-bit structural bank-index prefix ROM",
        ],
        "derived": [
            "carrier-only relay across tokenless completed banks",
            "token/head/rotor handoff only at a full allocator frontier",
            "carrier return through the same active edge tubes",
            "identical-word recurrence for two and four applications on all N<=2 sources",
        ],
        "open": [
            "transient complete-blank NEW predicate and append ACK",
            "exact pending-event refusal under occupied, dirty, or exhausted destinations",
            "edge-local predecessor/frontier replacing structural bank-index ROM",
            "literal physical-M2 placement/routing and active proper-cubic covariance",
            "unbounded resources, autonomous ACTUAL/ADMISS, Record/Born/time/source bridges",
        ],
        "boundary": (
            "Positive finite-capacity token-relative relay on a supplied clean three-bank "
            "chain.  The test stops before exhaustion and is not yet a safe recurrent "
            "physical-M2 compiler."
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(
        "CYCLE718_TOKEN_RELATIVE_RELAY_SUPPORT_PASS"
        if report["pass"] else "CYCLE718_TOKEN_RELATIVE_RELAY_SUPPORT_INCOMPLETE"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
