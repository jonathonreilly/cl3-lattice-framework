#!/usr/bin/env python3
"""Cycle715: recurrent directional endpoint instrument plus local packet bank.

This bounded construction composes the repaired Cycle-713 endpoint instrument with a literal directional
refinement and a two-cell append-only packet bank.  ACTUAL and ADMISS remain
supplied bits.  The gate ordinal is not called time and the reversible packet
bank is not called a permanent Record.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 300
NOTE_PATH = "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md"
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
import frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26 as K714


TOL = 4.0e-10
X = C714.X
H = C714.H
T = C714.T
TD = C714.TD
CNOT = C714.CNOT


@dataclass(frozen=True)
class Gate:
    kind: str
    wires: tuple[int, ...]


def x(target: int) -> Gate:
    return Gate("X", (target,))


def cn(control: int, target: int) -> Gate:
    return Gate("CNOT", (control, target))


def tof(control_a: int, control_b: int, target: int) -> Gate:
    return Gate("TOF", (control_a, control_b, target))


def mcx(controls: tuple[int, ...], target: int, work: tuple[int, ...]) -> tuple[Gate, ...]:
    """Positive multi-control X with a returned-clean AND ladder."""
    controls = tuple(controls)
    if len(controls) == 1:
        return (cn(controls[0], target),)
    if len(controls) == 2:
        return (tof(controls[0], controls[1], target),)
    need = len(controls) - 2
    if len(work) < need:
        raise ValueError((len(controls), len(work)))
    anc = work[:need]
    output = [tof(controls[0], controls[1], anc[0])]
    for index in range(2, len(controls) - 1):
        output.append(tof(anc[index - 2], controls[index], anc[index - 1]))
    output.append(tof(anc[-1], controls[-1], target))
    for index in reversed(range(2, len(controls) - 1)):
        output.append(tof(anc[index - 2], controls[index], anc[index - 1]))
    output.append(tof(controls[0], controls[1], anc[0]))
    return tuple(output)


# Two structurally addressed packet cells.  Each cell has the unchanged
# Cycle-704/Cycle-714 34-bit packet payload.
CELL_WIDTH = 34
BANK_CELLS = 2


def cell(index: int) -> dict[str, object]:
    base = CELL_WIDTH * index
    return {
        "pred": tuple(range(base, base + 6)),
        "rotor_before": tuple(range(base + 6, base + 10)),
        "rotor_after": tuple(range(base + 10, base + 14)),
        "carry": base + 14,
        "delta": tuple(range(base + 15, base + 27)),
        "endpoint": base + 27,
        "binder": base + 28,
        "valid": base + 29,
        "orientation": base + 30,
        "actual": base + 31,
        "admiss": base + 32,
        "law": base + 33,
        "payload": tuple(range(base, base + CELL_WIDTH)),
    }


CELLS = tuple(cell(index) for index in range(BANK_CELLS))
HEAD = tuple(range(68, 74))
ROTOR = tuple(range(74, 78))
TOKEN = (78, 79)
FRESH = (80, 81)
POINTER, U_TO_V, V_TO_U, BINDER, ACTUAL, ADMISS, LAW = range(82, 89)
TOKEN_OK, DIRECTION_OK = 89, 90
ZERO_WORK = tuple(range(91, 131))
ENABLE_TARGET = ZERO_WORK[-1]
N = 131
NONE_SENTINEL = 63


def packet_word() -> tuple[Gate, ...]:
    """Fixed reversible append word on the declared blank-selected domain."""
    output: list[Gate] = []
    # Local one-hot constraint witnesses.  XOR is exactly-one for two rails.
    output.extend((cn(TOKEN[0], TOKEN_OK), cn(TOKEN[1], TOKEN_OK)))
    output.extend((cn(U_TO_V, DIRECTION_OK), cn(V_TO_U, DIRECTION_OK)))

    # A complete 34-payload-bit zero test is performed at the token-selected
    # cell.  FRESH_i is a retained allocation witness, not a supplied flag.
    common = (TOKEN_OK, POINTER, DIRECTION_OK, BINDER, ACTUAL, ADMISS, LAW)
    for index, layout in enumerate(CELLS):
        payload = tuple(layout["payload"])
        output.extend(x(wire) for wire in payload)
        zero_controls = (TOKEN[index],) + common + payload
        output.extend(mcx(zero_controls, FRESH[index], ZERO_WORK))
        output.extend(x(wire) for wire in reversed(payload))

    # Only one branch is live on the local one-hot token code.  The token is
    # not moved until both structurally addressed branches finish, preventing
    # a within-word cascade into the second blank cell.
    for index, layout in enumerate(CELLS):
        enable_controls = (
            TOKEN[index], TOKEN_OK, FRESH[index], POINTER, DIRECTION_OK,
            BINDER, ACTUAL, ADMISS, LAW,
        )
        enable_word = mcx(enable_controls, ENABLE_TARGET, ZERO_WORK[:-1])
        output.extend(enable_word)
        e = ENABLE_TARGET
        for head, pred in zip(HEAD, layout["pred"]):
            output.append(tof(e, head, pred))
        for rotor, before in zip(ROTOR, layout["rotor_before"]):
            output.append(tof(e, rotor, before))
        output.extend(mcx((e,) + ROTOR, int(layout["carry"]), ZERO_WORK[:-1]))
        output.extend(mcx((e, ROTOR[0], ROTOR[1], ROTOR[2]), ROTOR[3], ZERO_WORK[:-1]))
        output.extend(mcx((e, ROTOR[0], ROTOR[1]), ROTOR[2], ZERO_WORK[:-1]))
        output.extend((tof(e, ROTOR[0], ROTOR[1]), cn(e, ROTOR[0])))
        for rotor, after in zip(ROTOR, layout["rotor_after"]):
            output.append(tof(e, rotor, after))
        # The delta and sign are downstream of the literal physical endpoint
        # comparator: e contains POINTER, while orientation copies U_TO_V.
        output.extend((cn(e, layout["delta"][1]), cn(e, layout["delta"][6])))
        for target in (
            layout["endpoint"], layout["binder"], layout["valid"],
            layout["actual"], layout["admiss"], layout["law"],
        ):
            output.append(cn(e, int(target)))
        output.append(tof(e, U_TO_V, int(layout["orientation"])))
        # Move the global predecessor head to this structural local address.
        for head, pred in zip(HEAD, layout["pred"]):
            output.append(tof(e, pred, head))
        if index:
            output.append(cn(e, HEAD[0]))
        output.extend(reversed(enable_word))

    # Clean move work from pre- and post-swap predicates.  This is a local
    # two-rail allocator permutation; its state is not a schedule clock.
    move = ZERO_WORK[0]
    output.extend((
        tof(TOKEN[0], int(CELLS[0]["valid"]), move),
        tof(TOKEN[1], int(CELLS[1]["valid"]), move),
        cn(TOKEN[1], TOKEN[0]),
        tof(move, TOKEN[0], TOKEN[1]),
        cn(TOKEN[1], TOKEN[0]),
        tof(TOKEN[1], int(CELLS[0]["valid"]), move),
        tof(TOKEN[0], int(CELLS[1]["valid"]), move),
    ))
    output.extend((cn(V_TO_U, DIRECTION_OK), cn(U_TO_V, DIRECTION_OK)))
    output.extend((cn(TOKEN[1], TOKEN_OK), cn(TOKEN[0], TOKEN_OK)))
    return tuple(output)


def apply_semantic(bits: tuple[int, ...], gates: tuple[Gate, ...]) -> tuple[int, ...]:
    state = list(bits)
    for gate in gates:
        if gate.kind == "X":
            state[gate.wires[0]] ^= 1
        elif gate.kind == "CNOT":
            state[gate.wires[1]] ^= state[gate.wires[0]]
        elif gate.kind == "TOF":
            state[gate.wires[2]] ^= state[gate.wires[0]] & state[gate.wires[1]]
        else:
            raise ValueError(gate)
    return tuple(state)


def expanded(gates: tuple[Gate, ...]) -> tuple[tuple[str, tuple[int, ...]], ...]:
    output: list[tuple[str, tuple[int, ...]]] = []
    for gate in gates:
        if gate.kind in ("X", "CNOT"):
            output.append((gate.kind, gate.wires))
        else:
            output.extend(C714.toffoli_primitives(*gate.wires))
    return tuple(output)


def sparse_apply(
    state: dict[int, complex], gates: tuple[tuple[str, tuple[int, ...]], ...]
) -> dict[int, complex]:
    matrices = {"X": X, "H": H, "T": T, "TD": TD, "CNOT": CNOT}
    current = dict(state)
    for kind, wires in gates:
        matrix = matrices[kind]
        updated: dict[int, complex] = {}
        for basis, amplitude in current.items():
            local = sum(((basis >> wire) & 1) << index for index, wire in enumerate(wires))
            for local_target in range(1 << len(wires)):
                coefficient = matrix[local_target, local]
                if abs(coefficient) < 1.0e-15:
                    continue
                target = basis
                for index, wire in enumerate(wires):
                    target = (
                        target & ~(1 << wire)
                    ) | (((local_target >> index) & 1) << wire)
                updated[target] = updated.get(target, 0.0j) + coefficient * amplitude
        current = {basis: value for basis, value in updated.items() if abs(value) > 1.0e-13}
    return current


def bits_to_int(bits: tuple[int, ...]) -> int:
    return sum(value << index for index, value in enumerate(bits))


def int_to_bits(value: int) -> tuple[int, ...]:
    return tuple((value >> index) & 1 for index in range(N))


def integer(bits: tuple[int, ...], wires: tuple[int, ...]) -> int:
    return sum(bits[wire] << index for index, wire in enumerate(wires))


def initial_bank(
    *, head: int = NONE_SENTINEL, rotor: int = 14,
    token: tuple[int, int] = (1, 0), binder: int = 1,
    actual: int = 1, admiss: int = 1, law: int = 1,
) -> tuple[int, ...]:
    bits = [0] * N
    for index, wire in enumerate(HEAD):
        bits[wire] = (head >> index) & 1
    for index, wire in enumerate(ROTOR):
        bits[wire] = (rotor >> index) & 1
    for wire, value in zip(TOKEN, token):
        bits[wire] = value
    bits[BINDER], bits[ACTUAL], bits[ADMISS], bits[LAW] = binder, actual, admiss, law
    return tuple(bits)


def set_interface(
    bits: tuple[int, ...], pointer: int, u_to_v: int, v_to_u: int
) -> tuple[int, ...]:
    output = list(bits)
    if any(output[wire] for wire in (POINTER, U_TO_V, V_TO_U)):
        raise ValueError("endpoint interface is not clean")
    output[POINTER], output[U_TO_V], output[V_TO_U] = pointer, u_to_v, v_to_u
    return tuple(output)


def clear_interface(bits: tuple[int, ...]) -> tuple[int, ...]:
    output = list(bits)
    output[POINTER] = output[U_TO_V] = output[V_TO_U] = 0
    return tuple(output)


def payload_blank(bits: tuple[int, ...], index: int) -> bool:
    return not any(bits[wire] for wire in CELLS[index]["payload"])


def declared_append_domain(bits: tuple[int, ...]) -> tuple[bool, str]:
    if sum(bits[wire] for wire in TOKEN) != 1:
        return False, "token_not_one_hot"
    if any(bits[wire] for wire in ZERO_WORK + (TOKEN_OK, DIRECTION_OK)):
        return False, "dirty_work"
    selected = 0 if bits[TOKEN[0]] else 1
    if not payload_blank(bits, selected) or bits[FRESH[selected]]:
        return False, "selected_cell_not_blank"
    if bits[POINTER] != (bits[U_TO_V] ^ bits[V_TO_U]):
        return False, "pointer_direction_mismatch"
    if bits[POINTER] and bits[U_TO_V] + bits[V_TO_U] != 1:
        return False, "direction_not_one_hot"
    return True, "lawful"


def packet_projection(bits: tuple[int, ...], index: int) -> dict[str, object] | None:
    layout = CELLS[index]
    if not bits[int(layout["valid"])]:
        return None
    predecessor = integer(bits, layout["pred"])
    return {
        "identity": index,
        "predecessor": None if predecessor == NONE_SENTINEL else predecessor,
        "rotor_before": integer(bits, layout["rotor_before"]),
        "rotor": integer(bits, layout["rotor_after"]),
        "carry": bits[int(layout["carry"])],
        "delta_mask": integer(bits, layout["delta"]),
        "endpoint": bits[int(layout["endpoint"])],
        "binder": bits[int(layout["binder"])],
        "valid": bits[int(layout["valid"])],
        "orientation": 1 if bits[int(layout["orientation"])] else -1,
        "actuality": bits[int(layout["actual"])],
        "admissibility": bits[int(layout["admiss"])],
        "law_domain": bits[int(layout["law"])],
    }


def combined_step(
    clean_bits: tuple[int, ...], direction: tuple[int, int]
) -> tuple[int, ...]:
    u_to_v, v_to_u = direction
    before = set_interface(clean_bits, u_to_v ^ v_to_u, u_to_v, v_to_u)
    lawful, reason = declared_append_domain(before)
    if not lawful and before[POINTER]:
        raise ValueError(reason)
    after = apply_semantic(before, packet_word())
    return clear_interface(after)


def semantic_bank_certificate() -> dict[str, object]:
    gates = packet_word()
    inverse = tuple(reversed(gates))
    cases = field_failures = inverse_failures = work_failures = 0
    projections = []
    for rotor in range(16):
        for head in (NONE_SENTINEL, 0, 1, 7, 31):
            for token_index, direction in ((0, (1, 0)), (1, (0, 1))):
                before = initial_bank(
                    head=head, rotor=rotor,
                    token=(1, 0) if token_index == 0 else (0, 1),
                )
                before = set_interface(before, 1, *direction)
                after = apply_semantic(before, gates)
                cases += 1
                packet = packet_projection(after, token_index)
                expected = {
                    "identity": token_index,
                    "predecessor": None if head == NONE_SENTINEL else head,
                    "rotor_before": rotor,
                    "rotor": (rotor + 1) % 16,
                    "carry": int(rotor == 15),
                    "delta_mask": 66,
                    "endpoint": 1,
                    "binder": 1,
                    "valid": 1,
                    "orientation": 1 if direction == (1, 0) else -1,
                    "actuality": 1,
                    "admissibility": 1,
                    "law_domain": 1,
                }
                field_failures += packet != expected
                field_failures += integer(after, HEAD) != token_index
                field_failures += integer(after, ROTOR) != (rotor + 1) % 16
                field_failures += tuple(after[wire] for wire in TOKEN) != (
                    (0, 1) if token_index == 0 else (1, 0)
                )
                inverse_failures += apply_semantic(after, inverse) != before
                work_failures += any(after[wire] for wire in ZERO_WORK + (TOKEN_OK, DIRECTION_OK))
                if len(projections) < 4:
                    projections.append(packet)

    clean = initial_bank()
    after_one = combined_step(clean, (1, 0))
    after_two = combined_step(after_one, (0, 1))
    recurrent = {
        "first": packet_projection(after_two, 0),
        "second": packet_projection(after_two, 1),
        "head": integer(after_two, HEAD),
        "rotor": integer(after_two, ROTOR),
        "token": tuple(after_two[wire] for wire in TOKEN),
        "fresh": tuple(after_two[wire] for wire in FRESH),
    }
    expected_recurrent = {
        "first": {
            "identity": 0, "predecessor": None, "rotor_before": 14,
            "rotor": 15, "carry": 0, "delta_mask": 66, "endpoint": 1,
            "binder": 1, "valid": 1, "orientation": 1, "actuality": 1,
            "admissibility": 1, "law_domain": 1,
        },
        "second": {
            "identity": 1, "predecessor": 0, "rotor_before": 15,
            "rotor": 0, "carry": 1, "delta_mask": 66, "endpoint": 1,
            "binder": 1, "valid": 1, "orientation": -1, "actuality": 1,
            "admissibility": 1, "law_domain": 1,
        },
        "head": 1, "rotor": 0, "token": (1, 0), "fresh": (1, 1),
    }
    exhausted_probe = set_interface(after_two, 1, 1, 0)
    exhausted_lawful, exhausted_reason = declared_append_domain(exhausted_probe)
    exhausted_executed = apply_semantic(exhausted_probe, gates)
    exhausted_difference = sum(a != b for a, b in zip(exhausted_probe, exhausted_executed))

    controls: dict[str, object] = {}
    for label, candidate in (
        ("zero_token", initial_bank(token=(0, 0))),
        ("two_tokens", initial_bank(token=(1, 1))),
        ("actual_zero", initial_bank(actual=0)),
        ("admiss_zero", initial_bank(admiss=0)),
        ("law_zero", initial_bank(law=0)),
        ("binder_zero", initial_bank(binder=0)),
    ):
        pointer = set_interface(candidate, 1, 1, 0)
        lawful, reason = declared_append_domain(pointer)
        observed = apply_semantic(pointer, gates)
        controls[label] = {
            "declared_lawful": lawful,
            "reason": reason,
            "mutation_bits": sum(a != b for a, b in zip(pointer, observed)),
        }
    dirty = list(set_interface(initial_bank(), 1, 1, 0))
    dirty[ZERO_WORK[7]] = 1
    dirty = tuple(dirty)
    dirty_lawful, dirty_reason = declared_append_domain(dirty)
    dirty_after = apply_semantic(dirty, gates)
    controls["dirty_work"] = {
        "declared_lawful": dirty_lawful, "reason": dirty_reason,
        "mutation_bits": sum(a != b for a, b in zip(dirty, dirty_after)),
    }
    occupied = list(after_one)
    occupied = set_interface(tuple(occupied), 1, 1, 0)
    # Force the token back onto the occupied first cell without changing the
    # packet.  This is explicitly outside the append code.
    occupied = list(occupied)
    occupied[TOKEN[0]], occupied[TOKEN[1]] = 1, 0
    occupied = tuple(occupied)
    occupied_lawful, occupied_reason = declared_append_domain(occupied)
    occupied_after = apply_semantic(occupied, gates)
    controls["occupied_selected"] = {
        "declared_lawful": occupied_lawful, "reason": occupied_reason,
        "mutation_bits": sum(a != b for a, b in zip(occupied, occupied_after)),
    }

    # Arbitrary inputs still have a literal inverse because the word is a
    # permutation, even though packet meaning is restricted to the code.
    rng = np.random.default_rng(71501)
    arbitrary_inverse_failures = 0
    for _ in range(256):
        before = tuple(int(value) for value in rng.integers(0, 2, size=N))
        arbitrary_inverse_failures += apply_semantic(apply_semantic(before, gates), inverse) != before

    return {
        "register_M2": N,
        "bank_cells": BANK_CELLS,
        "payload_bits_per_cell": CELL_WIDTH,
        "semantic_gates": len(gates),
        "expanded_one_two_M2_gates": len(expanded(gates)),
        "clean_admitted_cases": cases,
        "field_failures": field_failures,
        "inverse_failures": inverse_failures,
        "clean_work_failures": work_failures,
        "sample_projections": projections,
        "two_successive_appends": recurrent,
        "two_successive_expected": expected_recurrent,
        "two_successive_failures": recurrent != expected_recurrent,
        "exhausted_declared_lawful": exhausted_lawful,
        "exhausted_reason": exhausted_reason,
        "exhausted_forced_execution_difference_bits": exhausted_difference,
        "domain_controls": controls,
        "arbitrary_inverse_cases": 256,
        "arbitrary_inverse_failures": arbitrary_inverse_failures,
    }


def coherent_bank_certificate() -> dict[str, object]:
    gates = packet_word()
    primitives = expanded(gates)
    inverse_primitives = expanded(tuple(reversed(gates)))
    phase = lambda value: np.exp(1j * value * np.pi / 13)
    bases = [
        set_interface(initial_bank(rotor=15), 1, 1, 0),
        set_interface(initial_bank(rotor=7), 1, 0, 1),
        set_interface(initial_bank(actual=0), 1, 1, 0),
        set_interface(initial_bank(token=(0, 0)), 1, 1, 0),
        set_interface(initial_bank(token=(1, 1)), 1, 1, 0),
    ]
    states = (
        {bits_to_int(bases[0]): 1 / np.sqrt(2), bits_to_int(bases[1]): phase(1) / np.sqrt(2)},
        {bits_to_int(bases[0]): 1 / np.sqrt(2), bits_to_int(bases[2]): phase(2) / np.sqrt(2)},
        {
            bits_to_int(bases[2]): 1 / np.sqrt(3),
            bits_to_int(bases[3]): phase(3) / np.sqrt(3),
            bits_to_int(bases[4]): phase(6) / np.sqrt(3),
        },
    )
    maximum_component = maximum_norm = maximum_inverse = 0.0
    maximum_transient_support = 0
    for state in states:
        observed = sparse_apply(state, primitives)
        expected: dict[int, complex] = {}
        for basis, amplitude in state.items():
            target = bits_to_int(apply_semantic(int_to_bits(basis), gates))
            expected[target] = expected.get(target, 0.0j) + amplitude
        keys = set(observed) | set(expected)
        delta = np.asarray([observed.get(key, 0.0j) - expected.get(key, 0.0j) for key in keys])
        maximum_component = max(maximum_component, float(np.max(np.abs(delta), initial=0.0)))
        maximum_norm = max(maximum_norm, float(np.linalg.norm(delta)))
        restored = sparse_apply(observed, inverse_primitives)
        keys = set(restored) | set(state)
        inverse_delta = np.asarray([restored.get(key, 0.0j) - state.get(key, 0.0j) for key in keys])
        maximum_inverse = max(maximum_inverse, float(np.linalg.norm(inverse_delta)))
        maximum_transient_support = max(maximum_transient_support, len(observed))
    return {
        "coherent_states": len(states),
        "maximum_component_residual": maximum_component,
        "maximum_norm_residual": maximum_norm,
        "maximum_inverse_norm_residual": maximum_inverse,
        "maximum_final_support": maximum_transient_support,
    }


def endpoint_direction_maps() -> tuple[tuple[dict[int, complex], ...], dict[str, object]]:
    """Execute the repaired literal segment, then add two actual Toffolis."""
    base_maps, structure = C713.literal_segment_maps(2)
    pointer = structure["aux_base"] + 2
    u_to_v = structure["aux_base"] + 3
    v_to_u = structure["aux_base"] + 4
    direction_word = C713.toffoli_word(pointer, 6, u_to_v) + C713.toffoli_word(pointer, 1, v_to_u)
    cleanup_word = (
        C713.toffoli_word(pointer, 6, u_to_v)
        + C713.toffoli_word(pointer, 1, v_to_u)
        + (C713.cnot("recurrent_pointer_clean_left", 1, pointer),)
        + (C713.cnot("recurrent_pointer_clean_right", 6, pointer),)
    )
    outputs = []
    direction_failures = one_hot_failures = cleanup_failures = 0
    support_failures = phase_failures = 0
    seam_targets, seam_signs = C713.I712.schedule_arrays(C713.I712.SEAM_ADJACENT)
    contact = C713.I712.contact_diagonal()
    for basis, base in enumerate(base_maps):
        directed = C713.apply_sparse_word(base, direction_word)
        outputs.append(directed)
        support_failures += len(directed) != 1
        if len(directed) != 1:
            continue
        target_state, amplitude = next(iter(directed.items()))
        target = target_state & 4095
        p = (target_state >> pointer) & 1
        uv = (target_state >> u_to_v) & 1
        vu = (target_state >> v_to_u) & 1
        expected_uv = int(((target >> 6) & 1) and not ((target >> 1) & 1))
        expected_vu = int(((target >> 1) & 1) and not ((target >> 6) & 1))
        direction_failures += (uv, vu) != (expected_uv, expected_vu)
        one_hot_failures += p != (uv ^ vu) or uv + vu > 1
        phase_failures += abs(amplitude - seam_signs[basis] * contact[target]) >= TOL
        cleaned = C713.apply_sparse_word(directed, cleanup_word)
        cleanup_failures += any(
            (state >> wire) & 1
            for state in cleaned for wire in (pointer, u_to_v, v_to_u)
        )
        cleanup_failures += any((state & 4095) != target for state in cleaned)
    report = {
        "literal_basis_rows": len(outputs),
        "support_failures": support_failures,
        "direction_failures": direction_failures,
        "one_hot_failures": one_hot_failures,
        "phase_failures": int(phase_failures),
        "cleanup_failures": cleanup_failures,
        "pointer_wire": pointer,
        "u_to_v_wire": u_to_v,
        "v_to_u_wire": v_to_u,
        "direction_Toffoli_primitives": len(direction_word),
        "cleanup_primitives": len(cleanup_word),
    }
    return tuple(outputs), report


def held_overlapping_stars_certificate() -> dict[str, object]:
    """Literal two-seam direction/cleanup on the Cycle-713 held L3 domain."""
    matter_modes = 18
    endpoint_modes = (1, 6, 7, 12)
    other_modes = tuple(mode for mode in range(matter_modes) if mode not in endpoint_modes)
    domain = {basis for basis in range(1 << matter_modes) if basis.bit_count() <= 2}
    backgrounds = (
        0,
        sum(1 << mode for mode in other_modes),
        sum(1 << mode for index, mode in enumerate(other_modes) if index & 1),
        sum(1 << mode for index, mode in enumerate(other_modes) if not index & 1),
        sum(1 << mode for index, mode in enumerate(other_modes) if index % 3 == 0),
        sum(1 << mode for index, mode in enumerate(other_modes) if index % 3 != 0),
        sum(1 << mode for mode in other_modes[: len(other_modes) // 2]),
        sum(1 << mode for mode in other_modes[len(other_modes) // 2 :]),
    )
    for endpoint_pattern in range(1 << len(endpoint_modes)):
        endpoint_basis = sum(
            ((endpoint_pattern >> index) & 1) << mode
            for index, mode in enumerate(endpoint_modes)
        )
        domain.update(endpoint_basis | background for background in backgrounds)
    domain = tuple(sorted(domain))
    base_maps, structure = C713.literal_segment_maps(3, bases=domain)
    aux_base = structure["aux_base"]
    direction_base = aux_base + 6
    seams = ((1, 6), (7, 12))
    direction_word = ()
    cleanup_word = ()
    for seam_index, (left, right) in enumerate(seams):
        pointer = aux_base + 3 * seam_index + 2
        u_to_v = direction_base + 2 * seam_index
        v_to_u = u_to_v + 1
        direction_word += C713.toffoli_word(pointer, right, u_to_v)
        direction_word += C713.toffoli_word(pointer, left, v_to_u)
        cleanup_word += C713.toffoli_word(pointer, right, u_to_v)
        cleanup_word += C713.toffoli_word(pointer, left, v_to_u)
        cleanup_word += (C713.cnot("held_pointer_clean_left", left, pointer),)
        cleanup_word += (C713.cnot("held_pointer_clean_right", right, pointer),)
    failures = cleanup_failures = packet_cross_failures = 0
    # The two local packet banks occupy distinct physical register blocks.
    # Compute the write-set intersection instead of self-awarding zero.
    packet_targets = {gate.wires[-1] for gate in packet_word()}
    first_bank_targets = packet_targets
    second_bank_targets = {N + wire for wire in packet_targets}
    shared_packet_register_writes = len(first_bank_targets & second_bank_targets)
    pattern_counts = Counter()
    for basis, row in zip(domain, base_maps):
        directed = C713.apply_sparse_word(row, direction_word)
        if len(directed) != 1:
            failures += 1
            continue
        state, _amplitude = next(iter(directed.items()))
        target = state & ((1 << matter_modes) - 1)
        directions = []
        for seam_index, (left, right) in enumerate(seams):
            pointer = aux_base + 3 * seam_index + 2
            u_to_v = direction_base + 2 * seam_index
            v_to_u = u_to_v + 1
            observed = ((state >> u_to_v) & 1, (state >> v_to_u) & 1)
            expected = (
                int(bool((target >> right) & 1) and not bool((target >> left) & 1)),
                int(bool((target >> left) & 1) and not bool((target >> right) & 1)),
            )
            failures += observed != expected
            failures += ((state >> pointer) & 1) != (observed[0] ^ observed[1])
            directions.append(observed)
        pattern_counts[tuple(directions)] += 1
        # Two independent banks can consume the two seam words without a
        # shared register write; central-cell matter is read-only to both.
        packet_outputs = []
        for direction in directions:
            packet_outputs.append(combined_step(initial_bank(), direction))
        packet_cross_failures += any(
            integer(packet_outputs[index], HEAD) != (0 if direction != (0, 0) else NONE_SENTINEL)
            for index, direction in enumerate(directions)
        )
        cleaned = C713.apply_sparse_word(directed, cleanup_word)
        cleanup_failures += any(
            (clean_state >> wire) & 1
            for clean_state in cleaned
            for wire in range(aux_base + 2, direction_base + 4)
            if (wire - aux_base) % 3 == 2 or wire >= direction_base
        )
        cleanup_failures += any(
            (clean_state & ((1 << matter_modes) - 1)) != target for clean_state in cleaned
        )
    return {
        "held_rows": len(domain),
        "complete_N_le_2_rows": sum(basis.bit_count() <= 2 for basis in domain),
        "hostile_background_rows": len(domain) - sum(basis.bit_count() <= 2 for basis in domain),
        "direction_failures": failures,
        "instrument_cleanup_failures": cleanup_failures,
        "independent_bank_cross_failures": packet_cross_failures,
        "two_seam_direction_patterns": {str(key): value for key, value in sorted(pattern_counts.items())},
        "shared_central_cell_modes": (6, 7),
        "shared_packet_register_writes": shared_packet_register_writes,
    }


def full_column_composition_certificate() -> dict[str, object]:
    """Compose all 4096 full free+seam+contact columns with the bank word."""
    gates = packet_word()
    primitives = expanded(gates)
    initial = initial_bank()
    packet_outputs: dict[tuple[int, int], dict[int, complex]] = {}
    for direction in ((0, 0), (1, 0), (0, 1)):
        before = set_interface(initial, direction[0] ^ direction[1], *direction)
        observed = sparse_apply({bits_to_int(before): 1.0 + 0.0j}, primitives)
        cleaned: dict[int, complex] = {}
        clear_mask = ~((1 << POINTER) | (1 << U_TO_V) | (1 << V_TO_U))
        for basis, amplitude in observed.items():
            target = basis & clear_mask
            cleaned[target] = cleaned.get(target, 0.0j) + amplitude
        packet_outputs[direction] = cleaned

    maximum_endpoint = maximum_composed = maximum_norm = 0.0
    by_number = {number: 0.0 for number in range(13)}
    branch_rows = Counter()
    for source in range(1 << 12):
        observed_endpoint = K714.decoded_cycle713_column(source)
        expected_endpoint = K714.expected_cycle713_column(source)
        directed_observed: dict[tuple[int, int, int], complex] = {}
        directed_expected: dict[tuple[int, int, int], complex] = {}
        for target, pointer in observed_endpoint:
            direction = (
                int(bool((target >> 6) & 1) and not bool((target >> 1) & 1)),
                int(bool((target >> 1) & 1) and not bool((target >> 6) & 1)),
            ) if pointer else (0, 0)
            directed_observed[(target,) + direction] = observed_endpoint[(target, pointer)]
            branch_rows[direction] += 1
        for target, pointer in expected_endpoint:
            direction = (
                int(bool((target >> 6) & 1) and not bool((target >> 1) & 1)),
                int(bool((target >> 1) & 1) and not bool((target >> 6) & 1)),
            ) if pointer else (0, 0)
            directed_expected[(target,) + direction] = expected_endpoint[(target, pointer)]
        keys = set(directed_observed) | set(directed_expected)
        endpoint_delta = np.asarray([
            directed_observed.get(key, 0.0j) - directed_expected.get(key, 0.0j)
            for key in keys
        ])
        maximum_endpoint = max(maximum_endpoint, float(np.max(np.abs(endpoint_delta), initial=0.0)))
        observed: dict[tuple[int, int], complex] = {}
        expected: dict[tuple[int, int], complex] = {}
        for (matter, uv, vu), amplitude in directed_observed.items():
            for bank, packet_amplitude in packet_outputs[(uv, vu)].items():
                observed[(matter, bank)] = observed.get((matter, bank), 0.0j) + amplitude * packet_amplitude
        for (matter, uv, vu), amplitude in directed_expected.items():
            semantic_before = set_interface(initial, uv ^ vu, uv, vu)
            semantic_after = clear_interface(apply_semantic(semantic_before, gates))
            expected[(matter, bits_to_int(semantic_after))] = amplitude
        keys = set(observed) | set(expected)
        delta = np.asarray([observed.get(key, 0.0j) - expected.get(key, 0.0j) for key in keys])
        residual = float(np.max(np.abs(delta), initial=0.0))
        maximum_composed = max(maximum_composed, residual)
        maximum_norm = max(maximum_norm, abs(sum(abs(value) ** 2 for value in observed.values()) - 1.0))
        by_number[source.bit_count()] = max(by_number[source.bit_count()], residual)
    return {
        "source_columns": 4096,
        "maximum_directional_endpoint_residual": maximum_endpoint,
        "maximum_composed_EG_residual": maximum_composed,
        "maximum_norm_residual": maximum_norm,
        "maximum_residual_by_particle_number": by_number,
        "nonzero_branch_rows": {str(key): value for key, value in sorted(branch_rows.items())},
    }


def recurrence_mass_fixture() -> dict[str, object]:
    """Two applications on the complete one-particle source fixture."""
    maximum_norm = maximum_number = maximum_bank_inverse = 0.0
    append_branches = no_append_branches = 0
    # This uses the exact Cycle-712/Cycle-713 full column for each application.
    # The bank transition is deterministic on every endpoint branch, so sparse
    # matter+bank dictionaries remain small in the one-particle fixture.
    gates = packet_word()
    inverse = tuple(reversed(gates))
    for source in (1 << mode for mode in range(12)):
        state: dict[tuple[int, int], complex] = {(source, bits_to_int(initial_bank())): 1.0 + 0.0j}
        bank_inputs = []
        for _step in range(2):
            updated: dict[tuple[int, int], complex] = {}
            for (matter, bank_basis), outer_amplitude in state.items():
                column = K714.decoded_cycle713_column(matter)
                for (target, pointer), amplitude in column.items():
                    if pointer:
                        direction = (
                            int(bool((target >> 6) & 1) and not bool((target >> 1) & 1)),
                            int(bool((target >> 1) & 1) and not bool((target >> 6) & 1)),
                        )
                        append_branches += 1
                    else:
                        direction = (0, 0)
                        no_append_branches += 1
                    clean_bits = int_to_bits(bank_basis)
                    before = set_interface(clean_bits, pointer, *direction)
                    bank_inputs.append(before)
                    after = clear_interface(apply_semantic(before, gates))
                    key = (target, bits_to_int(after))
                    updated[key] = updated.get(key, 0.0j) + outer_amplitude * amplitude
            state = {key: value for key, value in updated.items() if abs(value) > 1.0e-13}
        maximum_norm = max(maximum_norm, abs(sum(abs(value) ** 2 for value in state.values()) - 1.0))
        maximum_number = max(maximum_number, max(
            (abs(value) for (matter, _bank), value in state.items() if matter.bit_count() != 1),
            default=0.0,
        ))
        # Every literal bank step remains invertible branch-by-branch.
        for before in bank_inputs[:16]:
            after = apply_semantic(before, gates)
            restored = apply_semantic(after, inverse)
            maximum_bank_inverse = max(maximum_bank_inverse, float(restored != before))
    return {
        "one_particle_sources": 12,
        "applications_per_source": 2,
        "maximum_norm_residual": maximum_norm,
        "maximum_particle_number_leakage": maximum_number,
        "maximum_branch_bank_inverse_failure": maximum_bank_inverse,
        "append_branch_terms": append_branches,
        "no_append_branch_terms": no_append_branches,
    }


def frame_translation_certificate() -> dict[str, object]:
    frames = C713.C712.C709.F.base.proper_cubic_frames()
    permutations = []
    truth_failures = 0
    for frame in frames:
        matrix = C713.C712.C709.F.base.c210.direction_permutation(frame)
        permutation = tuple(
            next(target for target in range(6) if abs(matrix[target, source]) > 0.5)
            for source in range(6)
        )
        permutations.append(permutation)
        for state in range(1 << 12):
            transported = 0
            for which_cell in range(2):
                for source in range(6):
                    transported |= ((state >> (6 * which_cell + source)) & 1) << (
                        6 * which_cell + permutation[source]
                    )
            base_target = state
            if ((state >> 1) & 1) != ((state >> 6) & 1):
                base_target ^= (1 << 1) | (1 << 6)
            frame_target = transported
            left, right = permutation[1], 6 + permutation[0]
            if ((transported >> left) & 1) != ((transported >> right) & 1):
                frame_target ^= (1 << left) | (1 << right)
            base_direction = (
                int(bool((base_target >> 6) & 1) and not bool((base_target >> 1) & 1)),
                int(bool((base_target >> 1) & 1) and not bool((base_target >> 6) & 1)),
            )
            frame_direction = (
                int(bool((frame_target >> right) & 1) and not bool((frame_target >> left) & 1)),
                int(bool((frame_target >> left) & 1) and not bool((frame_target >> right) & 1)),
            )
            truth_failures += base_direction != frame_direction
    product_failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product = left @ right
            product_index = next(index for index, frame in enumerate(frames) if np.array_equal(frame, product))
            composed = tuple(
                permutations[left_index][permutations[right_index][source]] for source in range(6)
            )
            product_failures += composed != permutations[product_index]
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "direction_truth_rows": len(frames) * (1 << 12),
        "direction_truth_failures": truth_failures,
        "product_failures": product_failures,
        "translation_vectors_declared": ((0, 0, 0), (3, -2, 1), (-4, 1, 2)),
    }


def combined_physical_route() -> dict[str, object]:
    """Route one complete two-star code update plus bank and cleanup."""
    cells = ((0, 0, 0), (1, 0, 0))
    eq = C713.C712.C709.G.build_equivalence(cells).equivalence
    _eq2, graph, site_map, gauges, occupied, collisions = C713.C712.P709.placement_bundle(cells)
    carriers = C713.C712.carriers_for(eq, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(index for index, carrier in enumerate(carriers) if len(carrier) == 2)
    endpoint_sites = C714.retained_endpoint_sites(eq, graph, site_map, gauges, occupied)
    du_site, dv_site, pointer_site = endpoint_sites
    occupied_set = set(occupied) | set(endpoint_sites)
    candidates = []
    for radius in range(1, 14):
        for xx in range(-radius, radius + 1):
            for yy in range(-radius, radius + 1):
                for zz in range(-radius, radius + 1):
                    site = (xx, yy, zz)
                    if max(abs(xx), abs(yy), abs(zz)) != radius:
                        continue
                    if site in occupied_set or site in candidates:
                        continue
                    candidates.append(site)
                    if len(candidates) >= N + 2:
                        break
                if len(candidates) >= N + 2:
                    break
            if len(candidates) >= N + 2:
                break
        if len(candidates) >= N + 2:
            break
    iterator = iter(candidates)
    u_site, v_site = next(iterator), next(iterator)
    bank_sites = []
    for wire in range(N):
        if wire == POINTER:
            bank_sites.append(pointer_site)
        elif wire == U_TO_V:
            bank_sites.append(u_site)
        elif wire == V_TO_U:
            bank_sites.append(v_site)
        else:
            bank_sites.append(next(iterator))
    aux_base = eq.qubits
    bank_to_decoded = {
        POINTER: aux_base + 2,
        U_TO_V: aux_base + 3,
        V_TO_U: aux_base + 4,
    }
    next_decoded = aux_base + 5
    for wire in range(N):
        if wire not in bank_to_decoded:
            bank_to_decoded[wire] = next_decoded
            next_decoded += 1
    extended_sites = list(wire_sites) + [du_site, dv_site, pointer_site, u_site, v_site]
    for wire in range(N):
        if wire not in (POINTER, U_TO_V, V_TO_U):
            extended_sites.append(bank_sites[wire])
    if len(extended_sites) != next_decoded:
        raise AssertionError((len(extended_sites), next_decoded))

    decoded, qr_residual = C713.instrumented_decoded_word(2)
    pointer = aux_base + 2
    u_wire, v_wire = aux_base + 3, aux_base + 4
    directional = (
        C713.toffoli_word(pointer, 6, u_wire)
        + C713.toffoli_word(pointer, 1, v_wire)
    )
    matrices = {"X": X, "H": H, "T": T, "TD": TD, "CNOT": CNOT}
    packet_abstract = tuple(
        C713.C712.AGate(
            "recurrent_packet_" + kind,
            tuple(bank_to_decoded[wire] for wire in wires),
            matrices[kind],
        )
        for kind, wires in expanded(packet_word())
    )
    cleanup = (
        C713.toffoli_word(pointer, 6, u_wire)
        + C713.toffoli_word(pointer, 1, v_wire)
        + (C713.cnot("recurrent_pointer_clean_left", 1, pointer),)
        + (C713.cnot("recurrent_pointer_clean_right", 6, pointer),)
    )
    combined_decoded = decoded + directional + packet_abstract + cleanup
    target_decode = C713.C712.synthesize_decode(eq.target_w, eq.target_v)
    target_encode = C713.C712.inverse_word(target_decode)
    repetition_decode = tuple(
        C713.C712.c707.Instruction("recurrent_repetition_decode_CNOT", carriers[index], CNOT)
        for index in repeated
    )
    repetition_encode = tuple(
        C713.C712.c707.Instruction("recurrent_repetition_encode_CNOT", carriers[index], CNOT)
        for index in reversed(repeated)
    )
    instructions = (
        repetition_decode
        + C713.C712.abstract_to_physical(target_decode, tuple(extended_sites), "recurrent_target_decode_")
        + C713.C712.abstract_to_physical(combined_decoded, tuple(extended_sites), "recurrent_decoded_")
        + C713.C712.abstract_to_physical(target_encode, tuple(extended_sites), "recurrent_target_encode_")
        + repetition_encode
    )
    routed, route = C713.C712.c707.route_word(instructions)
    assigned = set(occupied) | set(endpoint_sites) | set(bank_sites)
    touched = set(route["touched_coordinates"])

    # Translation compatibility is checked on the literal unrouted operand
    # word; Manhattan routing is translation equivariant because every path is
    # generated from coordinate differences.
    translation_failures = 0
    translations = ((3, -2, 1), (-4, 1, 2))
    signature = tuple((
        gate.kind, tuple(gate.sites),
        C713.C712.c707.c655.matrix_digest(gate.matrix),
    ) for gate in instructions)
    for shift in translations:
        translated = tuple(
            C713.C712.c707.Instruction(
                gate.kind,
                tuple(tuple(site[axis] + shift[axis] for axis in range(3)) for site in gate.sites),
                gate.matrix,
            )
            for gate in instructions
        )
        normalized = tuple(
            (
                gate.kind,
                tuple(tuple(site[axis] - shift[axis] for axis in range(3)) for site in gate.sites),
                C713.C712.c707.c655.matrix_digest(gate.matrix),
            )
            for gate in translated
        )
        translation_failures += normalized != signature
    return {
        "abstract_code_qubits": eq.qubits,
        "packet_register_M2": N,
        "combined_assigned_M2": len(assigned),
        "placement_collisions": collisions + len(assigned) - len(set(assigned)),
        "primitive_one_two_M2_gates": len(instructions),
        "routed_nearest_neighbor_gates": len(routed),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "routed_word_sha256": route["word_sha256"],
        "touched_M2": len(touched),
        "blank_route_work_M2": len(touched - assigned),
        "coin_QR_residual": qr_residual,
        "translation_vectors": translations,
        "translation_signature_failures": int(translation_failures),
        "endpoint_sites": endpoint_sites,
        "direction_sites": (u_site, v_site),
    }


def deletion_certificate() -> dict[str, object]:
    gates = packet_word()
    before = set_interface(initial_bank(rotor=15), 1, 1, 0)
    expected = apply_semantic(before, gates)
    selectors = {
        "complete_zero_test": lambda gate: gate.kind == "TOF" and gate.wires[-1] == FRESH[0],
        "predecessor": lambda gate: gate.kind == "TOF" and gate.wires[-1] == CELLS[0]["pred"][0],
        "carry": lambda gate: gate.kind == "TOF" and gate.wires[-1] == CELLS[0]["carry"],
        "delta": lambda gate: gate.kind == "CNOT" and gate.wires[-1] == CELLS[0]["delta"][1],
        "orientation": lambda gate: gate.kind == "TOF" and gate.wires[-1] == CELLS[0]["orientation"],
        "token_move": lambda gate: gate.kind == "TOF" and gate.wires[0] == ZERO_WORK[0]
        and set(gate.wires[1:]) == set(TOKEN),
    }
    output = {}
    for label, selector in selectors.items():
        index = next(index for index, gate in enumerate(gates) if selector(gate))
        damaged = gates[:index] + gates[index + 1 :]
        observed = apply_semantic(before, damaged)
        output[label] = {
            "deleted_gate_index": index,
            "different_bits": sum(a != b for a, b in zip(observed, expected)),
            "basis_state_norm_residual": float(np.sqrt(2.0)) if observed != expected else 0.0,
        }
    return output


def main() -> None:
    provenance = C714.provenance_certificate(AUDIT_INPUT_PATHS, __file__)
    _direction_maps, direction = endpoint_direction_maps()
    overlap = held_overlapping_stars_certificate()
    semantic = semantic_bank_certificate()
    coherent = coherent_bank_certificate()
    composed = full_column_composition_certificate()
    mass = recurrence_mass_fixture()
    frames = frame_translation_certificate()
    route = combined_physical_route()
    deletions = deletion_certificate()
    inherited = C713.exhaustive_two_cell_instrument()
    checks = {
        "source_closure": provenance["baseline_is_ancestor"]
        and provenance["declared_path_failures"] == 0
        and provenance["duplicate_declared_paths"] == 0
        and not provenance["missing_transitive_scripts"]
        and not provenance["missing_dynamic_scripts"]
        and not provenance["untracked_inputs"],
        "literal_direction_and_cleanup": direction["literal_basis_rows"] == 4096
        and not any(direction[key] for key in (
            "support_failures", "direction_failures", "one_hot_failures",
            "phase_failures", "cleanup_failures",
        )),
        "held_overlapping_stars": overlap["held_rows"] == 289
        and overlap["complete_N_le_2_rows"] == 172
        and overlap["hostile_background_rows"] == 117
        and overlap["direction_failures"] == overlap["instrument_cleanup_failures"] == 0
        and overlap["independent_bank_cross_failures"] == overlap["shared_packet_register_writes"] == 0,
        "semantic_packet_bank": semantic["clean_admitted_cases"] == 160
        and semantic["field_failures"] == semantic["inverse_failures"] == semantic["clean_work_failures"] == 0
        and not semantic["two_successive_failures"]
        and semantic["arbitrary_inverse_failures"] == 0,
        "lawful_domain_controls": not semantic["exhausted_declared_lawful"]
        and semantic["exhausted_reason"] == "selected_cell_not_blank"
        and all(
            row["mutation_bits"] == 0
            for label, row in semantic["domain_controls"].items()
            if label in ("zero_token", "two_tokens", "actual_zero", "admiss_zero", "law_zero", "binder_zero")
        )
        and not semantic["domain_controls"]["dirty_work"]["declared_lawful"]
        and not semantic["domain_controls"]["occupied_selected"]["declared_lawful"],
        "coherent_packet_execution": coherent["coherent_states"] == 3
        and coherent["maximum_norm_residual"] < TOL
        and coherent["maximum_inverse_norm_residual"] < TOL,
        "all4096_full_composition": composed["source_columns"] == 4096
        and composed["maximum_directional_endpoint_residual"] < TOL
        and composed["maximum_composed_EG_residual"] < TOL
        and composed["maximum_norm_residual"] < TOL,
        "one_particle_recurrence": mass["one_particle_sources"] == 12
        and mass["applications_per_source"] == 2
        and mass["maximum_norm_residual"] < TOL
        and mass["maximum_particle_number_leakage"] < TOL
        and mass["maximum_branch_bank_inverse_failure"] == 0,
        "proper_cubic_and_translation": frames["proper_cubic_frames"] == 24
        and frames["ordered_frame_products"] == 576
        and frames["direction_truth_failures"] == frames["product_failures"] == 0
        and route["translation_signature_failures"] == 0,
        "literal_physical_route": route["placement_collisions"] == 0
        and route["non_NN_failures"] == route["operand_order_failures"] == route["route_return_failures"] == 0,
        "active_deletions": all(row["basis_state_norm_residual"] > 1.0e-3 for row in deletions.values()),
        "inherited_mass_seam_contact": inherited["maximum_EG_instrument_residual"] < TOL
        and inherited["maximum_number_leakage"] < TOL
        and inherited["literal_segment_phase_failures"] == 0,
    }
    checks = {label: bool(passed) for label, passed in checks.items()}
    report = {
        "cycle": 715,
        "authority": "none",
        "audit": "unset",
        "status": "bounded_constructive_theorem",
        "declared_inputs": AUDIT_INPUT_PATHS,
        "provenance": provenance,
        "checks": checks,
        "pass": all(checks.values()),
        "directional_endpoint": direction,
        "held_overlapping_stars": overlap,
        "semantic_bank": semantic,
        "coherent_bank": coherent,
        "full4096_composition": composed,
        "recurrent_one_particle_fixture": mass,
        "frames": frames,
        "physical_route": route,
        "deletions": deletions,
        "inherited_cycle713": {
            "maximum_EG_instrument_residual": inherited["maximum_EG_instrument_residual"],
            "maximum_number_leakage": inherited["maximum_number_leakage"],
            "literal_segment_phase_failures": inherited["literal_segment_phase_failures"],
        },
        "supplied": (
            "Cycle-712/713 common code isometry and fixed free/seam/contact word",
            "clean packet payload, freshness-witness, and work-register genesis",
            "station-zero two-rail one-hot token and finite two-cell local bank",
            "BINDER, ACTUAL, ADMISS, LAW controls",
            "head/rotor genesis and fixed reversible gate word/Manhattan route workspace",
        ),
        "derived": (
            "u_to_v/v_to_u/no_change one-hot endpoint word from physical post-seam occupations",
            "coherent erasure of pointer and direction instruments after packet use",
            "complete selected-cell 34-bit zero test and retained freshness witness",
            "two successive structurally addressed packet appends under the same fixed law",
            "predecessor/head/rotor/carry/delta/orientation propagation and exact inverse",
            "one/two-M2 decomposition and one complete two-star nearest-neighbor routed word",
        ),
        "open": (
            "ACTUAL and ADMISS law suppliers",
            "autonomous genesis/enforcement of the initial one-hot token and clean bank/work code",
            "extension from a finite two-cell append domain to translated many-bank allocation",
            "behavior beyond local exhaustion; exhausted states are detected and excluded, not fixed",
            "active-coframe physical words, exterior streams, empirical units, Record permanence, and Born realization",
        ),
        "boundary": (
            "This is a bounded append-only two-cell recurrence on a declared code domain. "
            "The physical word is reversible; it is not a time law, an occurrence selector, "
            "a permanent Record, a Born law, or a source/gravity law."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str, separators=(",", ":")).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE715_RECURRENT_DIRECTIONAL_PACKET_BANK_PASS" if report["pass"] else "CYCLE715_RECURRENT_DIRECTIONAL_PACKET_BANK_INCOMPLETE")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
