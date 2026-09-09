#!/usr/bin/env python3
"""Cycle-718 carrier-return support core.

This bounded probe repairs one specific recurrent-interface wall exposed by
adversarial review of the inter-bank allocator candidate.  A link predicate
is retained across the packet write, the endpoint carrier is returned to its
source bank, and the link predicate/work are then cleaned from a post-image
predicate.  The Cycle-713 source inverse is not composed here.

This is a support module for a bounded Cycle-718 construction.  Its circuit
steps are not time and its reversible packet is not a permanent Record.
"""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle715_recurrent_directional_packet_bank_2026_07_26 as A


LEFT = 0
RIGHT = A.N
LATCH = 2 * A.N
LINK_WORK = tuple(range(LATCH + 1, LATCH + 191))
N_LINK = LINK_WORK[-1] + 1


def off(gate: A.Gate, base: int) -> A.Gate:
    return A.Gate(gate.kind, tuple(base + wire for wire in gate.wires))


def q(base: int, wire: int) -> int:
    return base + wire


def controlled_latch(
    positives: tuple[int, ...], negatives: tuple[int, ...]
) -> tuple[A.Gate, ...]:
    word: list[A.Gate] = []
    word.extend(A.x(wire) for wire in negatives)
    word.extend(A.mcx(positives + negatives, LATCH, LINK_WORK))
    word.extend(A.x(wire) for wire in reversed(negatives))
    return tuple(word)


def fredkin(control: int, left: int, right: int) -> tuple[A.Gate, ...]:
    return (A.cn(right, left), A.tof(control, left, right), A.cn(right, left))


def inactive_bank() -> tuple[int, ...]:
    return A.initial_bank(head=0, rotor=0, token=(0, 0))


def full_bank(rotor: int) -> tuple[int, ...]:
    state = A.initial_bank(rotor=rotor)
    state = A.combined_step(state, (1, 0))
    return A.combined_step(state, (0, 1))


def link_input(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return left + right + (0,) * (N_LINK - 2 * A.N)


def direction_witness_word() -> tuple[A.Gate, ...]:
    return (
        A.cn(A.U_TO_V, A.DIRECTION_OK),
        A.cn(A.V_TO_U, A.DIRECTION_OK),
    )


def event_ready_bank(
    bank: tuple[int, ...], direction: tuple[int, int]
) -> tuple[int, ...]:
    state = A.set_interface(bank, 1, *direction)
    return A.apply_semantic(state, direction_witness_word())


def safe_packet_body_word() -> tuple[A.Gate, ...]:
    """Retain the direction witness and admission-gate the token mover."""
    base = list(A.packet_word())
    move = A.ZERO_WORK[0]
    valid0 = int(A.CELLS[0]["valid"])
    valid1 = int(A.CELLS[1]["valid"])
    original = [
        A.tof(A.TOKEN[0], valid0, move),
        A.tof(A.TOKEN[1], valid1, move),
        A.cn(A.TOKEN[1], A.TOKEN[0]),
        A.tof(move, A.TOKEN[0], A.TOKEN[1]),
        A.cn(A.TOKEN[1], A.TOKEN[0]),
        A.tof(A.TOKEN[1], valid0, move),
        A.tof(A.TOKEN[0], valid1, move),
    ]
    start = next(
        index for index in range(len(base) - len(original) + 1)
        if base[index:index + len(original)] == original
    )
    common = (
        A.POINTER, A.DIRECTION_OK, A.BINDER, A.ACTUAL, A.ADMISS, A.LAW,
    )
    replacement = (
        *A.mcx(common + (A.TOKEN[0], valid0), move, A.ZERO_WORK[1:]),
        *A.mcx(common + (A.TOKEN[1], valid1), move, A.ZERO_WORK[1:]),
        A.cn(A.TOKEN[1], A.TOKEN[0]),
        A.tof(move, A.TOKEN[0], A.TOKEN[1]),
        A.cn(A.TOKEN[1], A.TOKEN[0]),
        *A.mcx(common + (A.TOKEN[1], valid0), move, A.ZERO_WORK[1:]),
        *A.mcx(common + (A.TOKEN[0], valid1), move, A.ZERO_WORK[1:]),
    )
    base[start:start + len(original)] = replacement
    base = [
        gate for gate in base
        if not (
            gate.kind == "CNOT"
            and gate.wires[1] == A.DIRECTION_OK
            and gate.wires[0] in (A.U_TO_V, A.V_TO_U)
        )
    ]
    return tuple(base)


def structural_prefix_word(bank_index: int) -> tuple[A.Gate, ...]:
    if not 0 <= bank_index < 32:
        raise ValueError(bank_index)
    word: list[A.Gate] = []
    valid0 = int(A.CELLS[0]["valid"])
    valid1 = int(A.CELLS[1]["valid"])
    admitted = (
        A.POINTER, A.DIRECTION_OK, A.BINDER, A.ACTUAL, A.ADMISS, A.LAW,
    )
    for head_bit in range(1, 6):
        if not ((bank_index >> (head_bit - 1)) & 1):
            continue
        word.append(A.x(valid1))
        word.extend(A.mcx(
            admitted + (A.TOKEN[1], A.FRESH[0], valid0, valid1),
            A.HEAD[head_bit], A.ZERO_WORK,
        ))
        word.append(A.x(valid1))
        word.extend(A.mcx(
            admitted + (A.TOKEN[0], *A.FRESH, valid0, valid1),
            A.HEAD[head_bit], A.ZERO_WORK,
        ))
    return tuple(word)


def packet_word_for_bank(bank_index: int) -> tuple[A.Gate, ...]:
    return safe_packet_body_word() + structural_prefix_word(bank_index)


def pre_latch_word() -> tuple[A.Gate, ...]:
    positives = (
        q(LEFT, A.TOKEN[0]),
        q(LEFT, A.FRESH[0]), q(LEFT, A.FRESH[1]),
        q(LEFT, int(A.CELLS[0]["valid"])),
        q(LEFT, int(A.CELLS[1]["valid"])),
        q(LEFT, A.POINTER), q(LEFT, A.DIRECTION_OK),
        q(LEFT, A.BINDER), q(LEFT, A.ACTUAL),
        q(LEFT, A.ADMISS), q(LEFT, A.LAW),
        q(RIGHT, A.BINDER), q(RIGHT, A.ACTUAL),
        q(RIGHT, A.ADMISS), q(RIGHT, A.LAW),
    )
    right_blank = tuple(
        q(RIGHT, wire) for layout in A.CELLS for wire in layout["payload"]
    )
    negatives = right_blank + tuple(q(RIGHT, wire) for wire in (
        *A.FRESH, *A.TOKEN, *A.HEAD, *A.ROTOR, *A.ZERO_WORK, A.TOKEN_OK,
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
    )) + tuple(q(LEFT, wire) for wire in (
        A.TOKEN[1], *A.ZERO_WORK, A.TOKEN_OK,
    ))
    return controlled_latch(positives, negatives)


def forward_transfer_word() -> tuple[A.Gate, ...]:
    word: list[A.Gate] = []
    for left_wire, right_wire in (
        (q(LEFT, A.TOKEN[0]), q(RIGHT, A.TOKEN[0])),
        *((q(LEFT, wire), q(RIGHT, wire)) for wire in (*A.HEAD, *A.ROTOR)),
        *((q(LEFT, wire), q(RIGHT, wire)) for wire in (
            A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
        )),
    ):
        word.extend(fredkin(LATCH, left_wire, right_wire))
    return tuple(word)


def carrier_return_word() -> tuple[A.Gate, ...]:
    word: list[A.Gate] = []
    for wire in (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK):
        word.extend(fredkin(LATCH, q(LEFT, wire), q(RIGHT, wire)))
    return tuple(word)


def post_latch_word() -> tuple[A.Gate, ...]:
    """Clean the retained latch from the first-packet post-image."""
    cell0, cell1 = A.CELLS
    positives = (
        q(LEFT, A.FRESH[0]), q(LEFT, A.FRESH[1]),
        q(LEFT, int(A.CELLS[0]["valid"])),
        q(LEFT, int(A.CELLS[1]["valid"])),
        q(LEFT, A.POINTER), q(LEFT, A.DIRECTION_OK),
        q(LEFT, A.BINDER), q(LEFT, A.ACTUAL),
        q(LEFT, A.ADMISS), q(LEFT, A.LAW),
        q(RIGHT, A.TOKEN[1]), q(RIGHT, A.FRESH[0]),
        q(RIGHT, int(cell0["valid"])),
        q(RIGHT, int(cell0["endpoint"])),
        q(RIGHT, int(cell0["binder"])),
        q(RIGHT, int(cell0["actual"])),
        q(RIGHT, int(cell0["admiss"])),
        q(RIGHT, int(cell0["law"])),
        q(RIGHT, A.BINDER), q(RIGHT, A.ACTUAL),
        q(RIGHT, A.ADMISS), q(RIGHT, A.LAW),
    )
    negatives = tuple(q(LEFT, wire) for wire in (
        *A.TOKEN, *A.HEAD, *A.ROTOR, *A.ZERO_WORK, A.TOKEN_OK,
    )) + tuple(q(RIGHT, wire) for wire in (
        *cell1["payload"], A.FRESH[1], A.TOKEN[0],
        *A.ZERO_WORK, A.TOKEN_OK,
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
    ))
    return controlled_latch(positives, negatives)


def three_phase_word() -> tuple[A.Gate, ...]:
    return (
        pre_latch_word()
        + forward_transfer_word()
        + tuple(off(gate, RIGHT) for gate in packet_word_for_bank(1))
        + carrier_return_word()
        + post_latch_word()
    )


def basis_residual(left: tuple[int, ...], right: tuple[int, ...]) -> float:
    return 0.0 if left == right else 2.0 ** 0.5


LINK_AUX_WIDTH = N_LINK - 2 * A.N


def apply_link_phase(
    left: tuple[int, ...],
    right: tuple[int, ...],
    link_aux: tuple[int, ...],
    word: tuple[A.Gate, ...],
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    output = A.apply_semantic(left + right + link_aux, word)
    return output[:A.N], output[A.N:2 * A.N], output[2 * A.N:]


def semantic_chain_step_with_host_source_cleanup(
    banks: tuple[tuple[int, ...], ...],
    links: tuple[tuple[int, ...], ...],
    direction: tuple[int, int],
    forward_order: tuple[int, ...] | None = None,
    reverse_order: tuple[int, ...] | None = None,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    """Persistent-link chain step with the Cycle-713 inverse still hosted.

    The endpoint carrier is supplied at the one-token bank.  After the exact
    physical carrier-return phases, the final source cleanup is deliberately
    performed by semantic assignment and remains outside the claimed word.
    """
    bank_state = list(banks)
    link_state = list(links)
    source = next(
        index for index, bank in enumerate(bank_state)
        if sum(bank[wire] for wire in A.TOKEN) == 1
    )
    if direction != (0, 0):
        bank_state[source] = event_ready_bank(bank_state[source], direction)

    edges = tuple(range(len(bank_state) - 1))
    forward_order = edges if forward_order is None else forward_order
    reverse_order = tuple(reversed(edges)) if reverse_order is None else reverse_order
    forward = pre_latch_word() + forward_transfer_word()
    carrier_back = carrier_return_word() + post_latch_word()
    for edge in forward_order:
        bank_state[edge], bank_state[edge + 1], link_state[edge] = apply_link_phase(
            bank_state[edge], bank_state[edge + 1], link_state[edge], forward
        )
    bank_state = [
        A.apply_semantic(bank, packet_word_for_bank(index))
        for index, bank in enumerate(bank_state)
    ]
    for edge in reverse_order:
        bank_state[edge], bank_state[edge + 1], link_state[edge] = apply_link_phase(
            bank_state[edge], bank_state[edge + 1], link_state[edge], carrier_back
        )

    # This is the remaining literal-composition wall, not part of the derived
    # carrier-return word: direction witness removal plus interface assignment.
    for index, bank in enumerate(bank_state):
        if bank[A.POINTER]:
            bank = A.apply_semantic(
                bank, tuple(reversed(direction_witness_word()))
            )
            bank_state[index] = A.clear_interface(bank)
    return tuple(bank_state), tuple(link_state)


def chain_genesis(
    bank_count: int,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    banks = (A.initial_bank(),) + (inactive_bank(),) * (bank_count - 1)
    links = tuple((0,) * LINK_AUX_WIDTH for _ in range(bank_count - 1))
    return banks, links


def chain_issues(
    banks: tuple[tuple[int, ...], ...],
    links: tuple[tuple[int, ...], ...],
    history: tuple[int, ...],
) -> tuple[str, ...]:
    issues: list[str] = []
    count = len(history)
    if any(any(link) for link in links):
        issues.append("dirty_link")
    packet_count = sum(
        bank[int(layout["valid"])] for bank in banks for layout in A.CELLS
    )
    if packet_count != count:
        issues.append("packet_count")
    token_banks = [
        index for index, bank in enumerate(banks)
        if sum(bank[wire] for wire in A.TOKEN)
    ]
    expected_bank = 0 if count == 0 else (count - 1) // 2
    if token_banks != [expected_bank]:
        issues.append("token")
    active = banks[expected_bank]
    if A.integer(active, A.HEAD) != (
        A.NONE_SENTINEL if count == 0 else count - 1
    ):
        issues.append("head")
    if A.integer(active, A.ROTOR) != ((14 + count) % 16):
        issues.append("rotor")
    for event, orientation in enumerate(history):
        packet = A.packet_projection(banks[event // 2], event % 2)
        rotor_before = (14 + event) % 16
        expected = {
            "identity": event % 2,
            "predecessor": None if event == 0 else event - 1,
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
    return tuple(issues)


def persistent_chain_certificate() -> dict[str, object]:
    choices = {(0, 0): None, (1, 0): 1, (0, 1): -1}
    mixed_failures = 0
    for sequence in itertools.product(choices, repeat=6):
        banks, links = chain_genesis(4)
        history: list[int] = []
        for direction in sequence:
            banks, links = semantic_chain_step_with_host_source_cleanup(
                banks, links, direction
            )
            if choices[direction] is not None:
                history.append(int(choices[direction]))
        mixed_failures += bool(chain_issues(banks, links, tuple(history)))

    held_rows = []
    held_failures = 0
    for bank_count in (2, 5, 12):
        banks, links = chain_genesis(bank_count)
        history = []
        for event in range(2 * bank_count):
            banks, links = semantic_chain_step_with_host_source_cleanup(
                banks, links, (0, 0)
            )
            direction = (1, 0) if event % 2 == 0 else (0, 1)
            banks, links = semantic_chain_step_with_host_source_cleanup(
                banks, links, direction
            )
            history.append(1 if direction == (1, 0) else -1)
        issues = chain_issues(banks, links, tuple(history))
        held_failures += bool(issues)
        held_rows.append({
            "banks": bank_count,
            "events": len(history),
            "issues": issues,
        })

    banks, links = chain_genesis(4)
    phases = [(banks, links)]
    for event in range(7):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        banks, links = semantic_chain_step_with_host_source_cleanup(
            banks, links, direction
        )
        phases.append((banks, links))
    edges = (0, 1, 2)
    orders = tuple(itertools.permutations(edges))
    order_rows = order_failures = 0
    for banks, links in phases:
        for direction in choices:
            expected = semantic_chain_step_with_host_source_cleanup(
                banks, links, direction, edges, tuple(reversed(edges))
            )
            for forward_order in orders:
                for reverse_order in orders:
                    observed = semantic_chain_step_with_host_source_cleanup(
                        banks, links, direction, forward_order, reverse_order
                    )
                    order_rows += 1
                    order_failures += observed != expected
    return {
        "persistent_aux_bits_per_link": LINK_AUX_WIDTH,
        "mixed_sequences": 3 ** 6,
        "mixed_failures": mixed_failures,
        "held_rows": held_rows,
        "held_failures": held_failures,
        "order_fill_phases": len(phases),
        "edge_permutations": len(orders),
        "forward_reverse_order_comparisons": order_rows,
        "order_failures": order_failures,
        "host_source_cleanup_still_supplied": True,
    }


def certificate() -> dict[str, object]:
    pre = pre_latch_word()
    forward = forward_transfer_word()
    packet = tuple(off(gate, RIGHT) for gate in packet_word_for_bank(1))
    carrier_return = carrier_return_word()
    post = post_latch_word()
    word = pre + forward + packet + carrier_return + post
    inverse = tuple(reversed(word))

    failures = 0
    maximum_state_residual = 0.0
    maximum_inverse_residual = 0.0
    maximum_work_population = 0
    rows = []
    for rotor in range(16):
        for direction in ((1, 0), (0, 1)):
            left_before = event_ready_bank(full_bank(rotor), direction)
            before = link_input(left_before, inactive_bank())
            after = A.apply_semantic(before, word)
            left_after = after[:A.N]
            right_after = after[A.N:2 * A.N]

            expected_left = list(left_before)
            for wire in (*A.TOKEN, *A.HEAD, *A.ROTOR):
                expected_left[wire] = 0
            expected_left = tuple(expected_left)

            transferred = list(inactive_bank())
            for wire in (*A.TOKEN, *A.HEAD, *A.ROTOR):
                transferred[wire] = left_before[wire]
            transferred = A.set_interface(
                tuple(transferred), 1, direction[0], direction[1]
            )
            transferred = A.apply_semantic(transferred, direction_witness_word())
            expected_right = A.apply_semantic(
                transferred, packet_word_for_bank(1)
            )
            expected_right = list(expected_right)
            for wire in (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK):
                expected_right[wire] = 0
            expected_right = tuple(expected_right)
            expected = link_input(expected_left, expected_right)

            state_residual = basis_residual(after, expected)
            restored = A.apply_semantic(after, inverse)
            inverse_residual = basis_residual(restored, before)
            work_population = sum(after[wire] for wire in LINK_WORK) + after[LATCH]
            maximum_state_residual = max(maximum_state_residual, state_residual)
            maximum_inverse_residual = max(maximum_inverse_residual, inverse_residual)
            maximum_work_population = max(maximum_work_population, work_population)
            packet_projection = A.packet_projection(right_after, 0)
            row_failed = any((
                state_residual,
                inverse_residual,
                work_population,
                tuple(left_after[wire] for wire in A.TOKEN) != (0, 0),
                tuple(right_after[wire] for wire in A.TOKEN) != (0, 1),
                tuple(left_after[wire] for wire in (
                    A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
                )) != (1, direction[0], direction[1], 1),
                any(right_after[wire] for wire in (
                    A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
                )),
                packet_projection is None,
                packet_projection is not None
                and packet_projection["orientation"] != (
                    1 if direction == (1, 0) else -1
                ),
            ))
            failures += row_failed
            rows.append({
                "rotor": rotor,
                "direction": direction,
                "state_residual": state_residual,
                "inverse_residual": inverse_residual,
                "work_population": work_population,
                "failed": bool(row_failed),
            })

    deletion = word[:len(pre) + len(forward) + len(packet)] + word[
        len(pre) + len(forward) + len(packet) + 3:
    ]
    deletion_before = link_input(event_ready_bank(full_bank(0), (1, 0)), inactive_bank())
    deletion_expected = A.apply_semantic(deletion_before, word)
    deletion_observed = A.apply_semantic(deletion_before, deletion)
    chain = persistent_chain_certificate()
    report = {
        "rows": len(rows),
        "failures": failures,
        "maximum_state_basis_residual": maximum_state_residual,
        "maximum_inverse_basis_residual": maximum_inverse_residual,
        "maximum_returned_work_population": maximum_work_population,
        "gate_counts": {
            "pre_latch": len(pre),
            "forward_transfer": len(forward),
            "packet_and_prefix": len(packet),
            "carrier_return": len(carrier_return),
            "post_latch": len(post),
            "total_semantic": len(word),
        },
        "carrier_return_deletion_basis_residual": basis_residual(
            deletion_observed, deletion_expected
        ),
        "persistent_chain": chain,
        "supplied": [
            "Route-A two-cell bank and safe admitted packet body",
            "full source bank, blank destination bank, and clean 190-bit link work",
            "one-hot allocator token and complete BINDER/ACTUAL/ADMISS/LAW inputs",
            "one endpoint direction carrier and fixed handoff/packet/return order",
            "six-bit structural destination-bank ROM prefix",
            "host carrier injection and host source cleanup in the semantic chain",
        ],
        "derived": [
            "retained local transfer predicate across one packet append",
            "allocator token/head/rotor advances while endpoint carrier returns to source",
            "returned-clean link latch and link work",
            "exact reverse-word inverse on all 32 tested source rows",
            "persistent-link semantic fills through 12 banks with hosted source cleanup",
            "forward/reverse boundary-order independence on the declared one-token code",
        ],
        "open": [
            "literal composition with the Cycle-713 source extractor and its inverse",
            "literal M2 placement/routing of the persistent per-link reverse pass",
            "safe backpressure/refusal when the downstream bank is occupied or unlawful",
            "autonomous event admission, genesis/enforcement, and finite exhaustion behavior",
            "active proper-cubic carrier action and same-E recurrent physical update",
        ],
        "boundary": (
            "Positive bounded carrier-return and persistent-link semantic chain only.  "
            "It does not compose the Cycle-713 source inverse, physically place/route "
            "the link chain, supply backpressure, or close an autonomous recurrent "
            "physical-M2 compiler."
        ),
    }
    report["pass"] = (
        failures == 0
        and maximum_state_residual == 0.0
        and maximum_inverse_residual == 0.0
        and maximum_work_population == 0
        and report["carrier_return_deletion_basis_residual"] > 1.0e-3
        and chain["mixed_failures"] == 0
        and chain["held_failures"] == 0
        and chain["order_failures"] == 0
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    return report


def main() -> int:
    report = certificate()
    for label, value in (
        ("all_32_rows", report["failures"] == 0),
        ("exact_state", report["maximum_state_basis_residual"] == 0.0),
        ("exact_inverse", report["maximum_inverse_basis_residual"] == 0.0),
        ("returned_clean_work", report["maximum_returned_work_population"] == 0),
        ("active_carrier_return_deletion", report["carrier_return_deletion_basis_residual"] > 1.0e-3),
        ("persistent_mixed_chain", report["persistent_chain"]["mixed_failures"] == 0),
        ("held_12_bank_chain", report["persistent_chain"]["held_failures"] == 0),
        ("code_space_order_independence", report["persistent_chain"]["order_failures"] == 0),
    ):
        print("PASS" if value else "FAIL", label, "::", value)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(
        "CYCLE718_CARRIER_RETURN_SUPPORT_PASS"
        if report["pass"]
        else "CYCLE718_CARRIER_RETURN_SUPPORT_INCOMPLETE"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
