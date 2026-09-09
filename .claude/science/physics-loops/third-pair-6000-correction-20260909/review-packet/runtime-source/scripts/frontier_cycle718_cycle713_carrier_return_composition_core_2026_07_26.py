#!/usr/bin/env python3
"""Cycle-718 decoded Cycle-713 carrier-return composition support core.

The actual 92-gate decoded Cycle-713 endpoint instrument is followed by a
local carrier copy, the three-phase inter-bank allocator handoff, carrier
return, and an exact source-side uncompute using the retained matter endpoint
bits.  This closes the prior host-clear operation on the bounded N<=2 test
domain.  Physical M2 placement/routing and destination backpressure remain
uncomposed.
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
import frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26 as K714
import frontier_cycle718_carrier_return_core_2026_07_26 as P


A = P.A
TOL = 4.0e-10
MATTER_AND_ENDPOINT_WIDTH = 41
LEFT_BANK = MATTER_AND_ENDPOINT_WIDTH
RIGHT_BANK = LEFT_BANK + A.N
TOTAL_WIRES = MATTER_AND_ENDPOINT_WIDTH + P.N_LINK
SOURCE_POINTER = 40
LEFT_ENDPOINT = 1
RIGHT_ENDPOINT = 6


def offset(gate: A.Gate, base: int) -> A.Gate:
    return A.Gate(gate.kind, tuple(base + wire for wire in gate.wires))


def apply_classical_sparse(
    state: dict[int, complex], word: tuple[A.Gate, ...]
) -> dict[int, complex]:
    output = dict(state)
    for gate in word:
        updated: dict[int, complex] = {}
        for basis, amplitude in output.items():
            target = basis
            if gate.kind == "X":
                target ^= 1 << gate.wires[0]
            elif gate.kind == "CNOT":
                target ^= ((basis >> gate.wires[0]) & 1) << gate.wires[1]
            elif gate.kind == "TOF":
                control = (
                    ((basis >> gate.wires[0]) & 1)
                    & ((basis >> gate.wires[1]) & 1)
                )
                target ^= control << gate.wires[2]
            else:
                raise ValueError(gate.kind)
            updated[target] = updated.get(target, 0.0j) + amplitude
        output = {
            basis: amplitude for basis, amplitude in updated.items()
            if abs(amplitude) > 1.0e-13
        }
    return output


def packed_basis(
    matter: int, left: tuple[int, ...], right: tuple[int, ...]
) -> int:
    basis = matter
    for wire, value in enumerate(left):
        basis |= value << (LEFT_BANK + wire)
    for wire, value in enumerate(right):
        basis |= value << (RIGHT_BANK + wire)
    return basis


def bank_bits(basis: int, base: int) -> tuple[int, ...]:
    return tuple((basis >> (base + wire)) & 1 for wire in range(A.N))


def carrier_compute_word() -> tuple[A.Gate, ...]:
    return (
        A.cn(SOURCE_POINTER, LEFT_BANK + A.POINTER),
        A.tof(SOURCE_POINTER, RIGHT_ENDPOINT, LEFT_BANK + A.U_TO_V),
        A.tof(SOURCE_POINTER, LEFT_ENDPOINT, LEFT_BANK + A.V_TO_U),
        *tuple(offset(gate, LEFT_BANK) for gate in P.direction_witness_word()),
    )


def source_uncompute_word() -> tuple[A.Gate, ...]:
    return (
        *tuple(
            offset(gate, LEFT_BANK)
            for gate in reversed(P.direction_witness_word())
        ),
        A.tof(SOURCE_POINTER, LEFT_ENDPOINT, LEFT_BANK + A.V_TO_U),
        A.tof(SOURCE_POINTER, RIGHT_ENDPOINT, LEFT_BANK + A.U_TO_V),
        A.cn(SOURCE_POINTER, LEFT_BANK + A.POINTER),
        A.cn(LEFT_ENDPOINT, SOURCE_POINTER),
        A.cn(RIGHT_ENDPOINT, SOURCE_POINTER),
    )


def composed_classical_word() -> tuple[A.Gate, ...]:
    return (
        carrier_compute_word()
        + tuple(
            offset(gate, MATTER_AND_ENDPOINT_WIDTH)
            for gate in P.three_phase_word()
        )
        + source_uncompute_word()
    )


def actual_output(
    source: int,
    full: tuple[int, ...],
    blank: tuple[int, ...],
    decoded_word: tuple,
    classical_word: tuple[A.Gate, ...],
) -> dict[int, complex]:
    initial = packed_basis(source, full, blank)
    instrumented = C713.apply_sparse_word({initial: 1.0 + 0.0j}, decoded_word)
    return apply_classical_sparse(instrumented, classical_word)


def expected_output(
    source: int, full: tuple[int, ...], blank: tuple[int, ...]
) -> dict[int, complex]:
    output: dict[int, complex] = {}
    for (matter, pointer), amplitude in K714.expected_cycle713_column(source).items():
        if pointer:
            direction = (
                int(bool((matter >> RIGHT_ENDPOINT) & 1)
                    and not bool((matter >> LEFT_ENDPOINT) & 1)),
                int(bool((matter >> LEFT_ENDPOINT) & 1)
                    and not bool((matter >> RIGHT_ENDPOINT) & 1)),
            )
            local = P.link_input(P.event_ready_bank(full, direction), blank)
            local = A.apply_semantic(local, P.three_phase_word())
            left = local[:A.N]
            right = local[A.N:2 * A.N]
            left = A.apply_semantic(
                left, tuple(reversed(P.direction_witness_word()))
            )
            left = A.clear_interface(left)
        else:
            left, right = full, blank
        key = packed_basis(matter, left, right)
        output[key] = output.get(key, 0.0j) + amplitude
    return output


def vector_residual(
    observed: dict[int, complex], expected: dict[int, complex]
) -> float:
    return math.sqrt(sum(
        abs(observed.get(key, 0.0j) - expected.get(key, 0.0j)) ** 2
        for key in set(observed) | set(expected)
    ))


def dirty_auxiliary(basis: int) -> bool:
    endpoint_dirty = any((basis >> wire) & 1 for wire in (38, 39, 40))
    bank_interface_dirty = any(
        (basis >> (base + wire)) & 1
        for base in (LEFT_BANK, RIGHT_BANK)
        for wire in (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK)
    )
    link_dirty = any(
        (basis >> wire) & 1
        for wire in range(MATTER_AND_ENDPOINT_WIDTH + 2 * A.N, TOTAL_WIRES)
    )
    return endpoint_dirty or bank_interface_dirty or link_dirty


def certificate() -> dict[str, object]:
    decoded_word, _qr = C713.instrumented_decoded_word(2)
    classical_word = composed_classical_word()
    full = P.full_bank(0)
    blank = P.inactive_bank()
    sources = tuple(source for source in range(1 << 12) if source.bit_count() <= 2)

    maximum_residual = maximum_norm = maximum_dirty_weight = 0.0
    maximum_particle_leakage = maximum_support = failures = 0
    one_particle_residual = one_particle_norm = 0.0
    complete_outputs: dict[int, dict[int, complex]] = {}
    for source in sources:
        observed = actual_output(
            source, full, blank, decoded_word, classical_word
        )
        expected = expected_output(source, full, blank)
        complete_outputs[source] = observed
        residual = vector_residual(observed, expected)
        norm = abs(sum(abs(value) ** 2 for value in observed.values()) - 1.0)
        dirty_weight = sum(
            abs(amplitude) ** 2 for basis, amplitude in observed.items()
            if dirty_auxiliary(basis)
        )
        particle_leakage = sum(
            abs(amplitude) ** 2 for basis, amplitude in observed.items()
            if (basis & ((1 << 12) - 1)).bit_count() != source.bit_count()
        )
        maximum_residual = max(maximum_residual, residual)
        maximum_norm = max(maximum_norm, norm)
        maximum_dirty_weight = max(maximum_dirty_weight, dirty_weight)
        maximum_particle_leakage = max(maximum_particle_leakage, particle_leakage)
        maximum_support = max(maximum_support, len(observed))
        failures += residual > TOL
        if source.bit_count() == 1:
            one_particle_residual = max(one_particle_residual, residual)
            one_particle_norm = max(one_particle_norm, norm)

    compute_length = len(carrier_compute_word())
    three_phase = P.three_phase_word()
    return_start = (
        compute_length
        + len(P.pre_latch_word())
        + len(P.forward_transfer_word())
        + len(tuple(offset(gate, P.RIGHT) for gate in P.packet_word_for_bank(1)))
    )
    deletions = {
        "carrier_pointer_copy": classical_word[1:],
        "carrier_return_first_swap": (
            classical_word[:return_start]
            + classical_word[return_start + 3:]
        ),
        "source_pointer_cleanup": classical_word[:-1],
    }
    deletion_residuals = {}
    for label, damaged_word in deletions.items():
        maximum = 0.0
        for source in sources:
            damaged = actual_output(
                source, full, blank, decoded_word, damaged_word
            )
            maximum = max(
                maximum, vector_residual(damaged, complete_outputs[source])
            )
        deletion_residuals[label] = maximum

    report = {
        "decoded_Cycle713_gates": len(decoded_word),
        "classical_carrier_handoff_gates": len(classical_word),
        "total_decoded_plus_classical_gates": len(decoded_word) + len(classical_word),
        "assigned_decoded_registers": TOTAL_WIRES,
        "sources_N_le_2": len(sources),
        "failures": failures,
        "maximum_composed_residual": maximum_residual,
        "maximum_norm_residual": maximum_norm,
        "maximum_dirty_auxiliary_probability_weight": maximum_dirty_weight,
        "maximum_particle_number_leakage": maximum_particle_leakage,
        "maximum_sparse_support": maximum_support,
        "one_particle_sources": 12,
        "maximum_one_particle_residual": one_particle_residual,
        "maximum_one_particle_norm_residual": one_particle_norm,
        "deletion_residuals": deletion_residuals,
        "supplied": [
            "landed decoded Cycle-713 two-cell matter word and endpoint register",
            "Route-A full source bank, blank destination bank, and clean link work",
            "one-hot token and complete BINDER/ACTUAL/ADMISS/LAW inputs",
            "fixed three-phase handoff/append/carrier-return circuit order",
            "six-bit structural bank-prefix ROM",
        ],
        "derived": [
            "literal carrier copy from the retained Cycle-713 endpoint pointer",
            "direction carrier derived from post-update physical matter endpoints",
            "exact carrier return to the original matter seam",
            "exact source-pointer and bank-interface uncompute without host reset",
            "coherent Cycle-713-plus-history composition on every N<=2 source",
        ],
        "open": [
            "safe local destination backpressure/refusal",
            "literal physical-M2 placement and routing of the complete word",
            "active proper-cubic carrier covariance on the routed layout",
            "autonomous ACTUAL/ADMISS law and genesis/enforcement",
            "finite resource exhaustion behavior and unbounded realized history",
        ],
        "boundary": (
            "Positive decoded-gate carrier-copy/uncompute composition on the supplied "
            "N<=2 domain.  This is not yet a routed physical-M2 recurrent compiler, "
            "Record permanence, time, source/gravity, Born realization, or no-go."
        ),
    }
    report["pass"] = (
        failures == 0
        and maximum_residual < TOL
        and maximum_norm < TOL
        and maximum_dirty_weight < TOL
        and maximum_particle_leakage < TOL
        and all(value > 1.0e-3 for value in deletion_residuals.values())
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    return report


def main() -> int:
    report = certificate()
    checks = {
        "all_N_le_2_columns": report["failures"] == 0,
        "coherent_residual": report["maximum_composed_residual"] < TOL,
        "norm": report["maximum_norm_residual"] < TOL,
        "clean_auxiliaries": report["maximum_dirty_auxiliary_probability_weight"] < TOL,
        "particle_number": report["maximum_particle_number_leakage"] < TOL,
        "active_deletions": all(
            value > 1.0e-3 for value in report["deletion_residuals"].values()
        ),
    }
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(
        "CYCLE718_CYCLE713_CARRIER_RETURN_SUPPORT_PASS"
        if report["pass"]
        else "CYCLE718_CYCLE713_CARRIER_RETURN_SUPPORT_INCOMPLETE"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
