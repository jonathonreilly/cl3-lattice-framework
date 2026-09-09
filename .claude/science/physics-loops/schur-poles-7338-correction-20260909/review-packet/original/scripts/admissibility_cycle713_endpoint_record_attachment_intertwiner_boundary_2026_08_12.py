#!/usr/bin/env python3
"""Block 66: literal Cycle-713 endpoint to Block-65 attachment intertwiner.

The runner composes the executed Cycle-713 seam pointer with a two-CNOT decoder
requiring no additional clean ancilla into the Block-65 P tensor M input type.
It checks arbitrary coherence by matrix units, routes both endpoint choices on
the literal M2 placement, composes the decoded state with the Block-65
instrument/front, and
exposes the endpoint-orientation datum that remains unselected.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path

import numpy as np

import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as c713
import admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12 as b65


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_CYCLE713_ENDPOINT_RECORD_ATTACHMENT_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
CYCLE713_NOTE = ROOT / "docs" / "PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md"
BLOCK65_NOTE = ROOT / "docs" / "ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CYCLE713_ENDPOINT_RECORD_ATTACHMENT_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
)

TOL = 3e-11
CNOT = c713.CNOT


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def bit(state: int, wire: int) -> int:
    return (state >> wire) & 1


def bridge_word(choice: str, left: int, right: int, pointer: int):
    if choice == "right":
        return (
            c713.cnot("record_bridge_pointer_to_clean_left", pointer, left),
            c713.cnot("record_bridge_right_to_clean_left", right, left),
        )
    if choice == "left":
        return (
            c713.cnot("record_bridge_pointer_to_clean_right", pointer, right),
            c713.cnot("record_bridge_left_to_clean_right", left, right),
        )
    raise ValueError(choice)


def literal_cycle713_decoder(drop_second_gate: bool = False) -> dict[str, object]:
    maps, structure = c713.literal_segment_maps(2)
    left, right = 1, 6
    du, dv, pointer = structure["new_auxiliary_wires"]
    failures = {
        "source_support": 0,
        "pointer_constraint": 0,
        "right_clean": 0,
        "left_clean": 0,
        "scratch": 0,
        "amplitude": 0,
    }
    right_rows: set[tuple[int, int]] = set()
    left_rows: set[tuple[int, int]] = set()
    for row in maps:
        failures["source_support"] += len(row) != 1
        if len(row) != 1:
            continue
        source_state, source_amplitude = next(iter(row.items()))
        failures["pointer_constraint"] += bit(source_state, pointer) != (
            bit(source_state, left) ^ bit(source_state, right)
        )
        failures["scratch"] += bit(source_state, du) != 0 or bit(source_state, dv) != 0

        right_word = bridge_word("right", left, right, pointer)
        if drop_second_gate:
            right_word = right_word[:1]
        right_output = c713.apply_sparse_word(row, right_word)
        left_output = c713.apply_sparse_word(
            row, bridge_word("left", left, right, pointer)
        )
        if len(right_output) != 1 or len(left_output) != 1:
            failures["source_support"] += 1
            continue
        right_state, right_amplitude = next(iter(right_output.items()))
        left_state, left_amplitude = next(iter(left_output.items()))
        failures["right_clean"] += bit(right_state, left) != 0
        failures["left_clean"] += bit(left_state, right) != 0
        failures["amplitude"] += (
            abs(right_amplitude - source_amplitude) >= TOL
            or abs(left_amplitude - source_amplitude) >= TOL
        )
        right_rows.add((bit(right_state, pointer), bit(right_state, right)))
        left_rows.add((bit(left_state, pointer), bit(left_state, left)))
    return {
        "rows": len(maps),
        "failures": failures,
        "right_PM_rows": tuple(sorted(right_rows)),
        "left_PM_rows": tuple(sorted(left_rows)),
        "aux_base": structure["aux_base"],
    }


def encoding(choice: str) -> np.ndarray:
    """Code isometry in local bit order (left,right,pointer)."""
    answer = np.zeros((8, 4), dtype=complex)
    for pointer in (0, 1):
        for matter in (0, 1):
            if choice == "right":
                left, right = pointer ^ matter, matter
            elif choice == "left":
                left, right = matter, pointer ^ matter
            else:
                raise ValueError(choice)
            answer[left | (right << 1) | (pointer << 2), 2 * pointer + matter] = 1
    return answer


def extraction(choice: str) -> np.ndarray:
    answer = np.zeros((4, 8), dtype=complex)
    for pointer in (0, 1):
        for matter in (0, 1):
            if choice == "right":
                state = (matter << 1) | (pointer << 2)
            elif choice == "left":
                state = matter | (pointer << 2)
            else:
                raise ValueError(choice)
            answer[2 * pointer + matter, state] = 1
    return answer


def controlled_x() -> np.ndarray:
    answer = np.zeros((4, 4), dtype=complex)
    for pointer in (0, 1):
        for matter in (0, 1):
            answer[2 * pointer + (matter ^ pointer), 2 * pointer + matter] = 1
    return answer


def coherent_code_intertwiner() -> dict[str, object]:
    right_decoder = c713.word_matrix(
        bridge_word("right", 0, 1, 2), 3
    )
    left_decoder = c713.word_matrix(
        bridge_word("left", 0, 1, 2), 3
    )
    right_encoding = encoding("right")
    right_extract = extraction("right")
    left_extract = extraction("left")
    cx = controlled_x()
    identity4 = np.eye(4, dtype=complex)
    identity8 = np.eye(8, dtype=complex)

    right_reduced = right_extract @ right_decoder @ right_encoding
    left_reduced = left_extract @ left_decoder @ right_encoding
    right_leakage = (
        identity8 - right_extract.conj().T @ right_extract
    ) @ right_decoder @ right_encoding
    left_leakage = (
        identity8 - left_extract.conj().T @ left_extract
    ) @ left_decoder @ right_encoding

    matrix_unit_residual = 0.0
    matrix_units = 0
    for row in range(4):
        for column in range(4):
            unit = np.zeros((4, 4), dtype=complex)
            unit[row, column] = 1
            encoded = right_encoding @ unit @ right_encoding.conj().T
            observed = right_decoder @ encoded @ right_decoder.conj().T
            expected = right_extract.conj().T @ unit @ right_extract
            matrix_unit_residual = max(
                matrix_unit_residual, float(np.linalg.norm(observed - expected))
            )
            matrix_units += 1

    return {
        "right_unitarity_residual": float(
            np.linalg.norm(right_decoder.conj().T @ right_decoder - identity8)
        ),
        "left_unitarity_residual": float(
            np.linalg.norm(left_decoder.conj().T @ left_decoder - identity8)
        ),
        "right_identity_residual": float(np.linalg.norm(right_reduced - identity4)),
        "left_controlled_X_residual": float(np.linalg.norm(left_reduced - cx)),
        "right_clean_leakage": float(np.linalg.norm(right_leakage)),
        "left_clean_leakage": float(np.linalg.norm(left_leakage)),
        "matrix_units": matrix_units,
        "matrix_unit_residual": matrix_unit_residual,
    }


def charge_dictionary() -> dict[str, object]:
    """Track the Cycle-713 two-endpoint number through the decoder.

    The decoder is a qubit basis change, not a number-preserving fermion word.
    The complete P,M pair still carries the old number exactly as
    N=M+(P xor M), and the formation sector P=1 is exactly N=1.
    """
    rows = []
    reconstruction_failures = parity_failures = 0
    naive_matter_mismatches = formation_number_failures = 0
    for pointer in (0, 1):
        for matter in (0, 1):
            left = pointer ^ matter
            right = matter
            endpoint_number = left + right
            reconstructed = matter + (pointer ^ matter)
            reconstruction_failures += reconstructed != endpoint_number
            parity_failures += endpoint_number % 2 != pointer
            naive_matter_mismatches += matter != endpoint_number
            if pointer == 1:
                formation_number_failures += endpoint_number != 1
            rows.append((pointer, matter, endpoint_number, reconstructed))

    number = np.diag(
        [((state >> 0) & 1) + ((state >> 1) & 1) for state in range(8)]
    ).astype(complex)
    right_decoder = c713.word_matrix(bridge_word("right", 0, 1, 2), 3)
    commutator = right_decoder @ number - number @ right_decoder
    transformed_number = np.diag([
        (
            (((state >> 0) & 1) ^ ((state >> 2) & 1) ^ ((state >> 1) & 1))
            + ((state >> 1) & 1)
        )
        for state in range(8)
    ]).astype(complex)
    return {
        "rows": tuple(rows),
        "reconstruction_failures": reconstruction_failures,
        "parity_failures": parity_failures,
        "naive_matter_mismatches": naive_matter_mismatches,
        "formation_number_failures": formation_number_failures,
        "number_commutator_norm": float(np.linalg.norm(commutator)),
        "operator_identity_residual": float(
            np.linalg.norm(
                right_decoder @ number @ right_decoder.conj().T - transformed_number
            )
        ),
    }


def pointer_sites_for(cells, wire_sites, occupied):
    pointer_sites: list[tuple[int, int, int]] = []
    occupied_set = set(occupied)
    for seam in range(len(cells) - 1):
        left_site = wire_sites[6 * seam + 1]
        right_site = wire_sites[6 * (seam + 1)]
        candidates = []
        for x in range(min(left_site[0], right_site[0]) - 2, max(left_site[0], right_site[0]) + 3):
            for y in range(min(left_site[1], right_site[1]) - 2, max(left_site[1], right_site[1]) + 3):
                for z in range(min(left_site[2], right_site[2]) - 2, max(left_site[2], right_site[2]) + 3):
                    site = (x, y, z)
                    if site in occupied_set or site in pointer_sites:
                        continue
                    dl = sum(abs(site[i] - left_site[i]) for i in range(3))
                    dr = sum(abs(site[i] - right_site[i]) for i in range(3))
                    candidates.append((max(dl, dr), dl + dr, site))
        pointer_sites.extend(row[2] for row in sorted(candidates)[:3])
    return tuple(pointer_sites)


def physical_bridge_certificate(choice: str) -> dict[str, object]:
    cells = ((0, 0, 0), (1, 0, 0))
    C = c713.C712
    eq = C.C709.G.build_equivalence(cells).equivalence
    _eq2, graph, site_map, gauges, occupied, collisions = C.P709.placement_bundle(cells)
    carriers = C.carriers_for(eq, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(index for index, carrier in enumerate(carriers) if len(carrier) == 2)
    pointer_sites = pointer_sites_for(cells, wire_sites, occupied)
    extended_sites = wire_sites + pointer_sites
    target_decode = C.synthesize_decode(eq.target_w, eq.target_v)
    target_encode = C.inverse_word(target_decode)
    decoded, qr_residual = c713.instrumented_decoded_word(2)
    pointer = eq.qubits + 2
    decoded += bridge_word(choice, 1, 6, pointer)
    repetition_decode = tuple(
        C.c707.Instruction("record_bridge_repetition_decode_CNOT", carriers[index], CNOT)
        for index in repeated
    )
    repetition_encode = tuple(
        C.c707.Instruction("record_bridge_repetition_encode_CNOT", carriers[index], CNOT)
        for index in reversed(repeated)
    )
    word = (
        repetition_decode
        + C.abstract_to_physical(target_decode, extended_sites, "record_bridge_target_decode_")
        + C.abstract_to_physical(decoded, extended_sites, "record_bridge_decoded_")
        + C.abstract_to_physical(target_encode, extended_sites, "record_bridge_target_encode_")
        + repetition_encode
    )
    routed, route = C.c707.route_word(word)
    return {
        "choice": choice,
        "literal_code_M2": len(occupied),
        "endpoint_register_M2": len(pointer_sites),
        "total_assigned_M2": len(occupied) + len(pointer_sites),
        "placement_collisions": collisions + len(pointer_sites) - len(set(pointer_sites)),
        "primitive_gates": len(word),
        "routed_gates": len(routed),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "touched_M2": len(route["touched_coordinates"]),
        "blank_route_work_M2": len(
            set(route["touched_coordinates"]) - set(occupied) - set(pointer_sites)
        ),
        "routed_word_sha256": route["word_sha256"],
        "coin_QR_residual": qr_residual,
    }


def cx_density(omega: b65.QMatrix) -> b65.QMatrix:
    permutation = tuple(2 * pointer + (matter ^ pointer) for pointer in (0, 1) for matter in (0, 1))
    answer = [list(row) for row in b65.qzero(4)]
    for row in range(4):
        for column in range(4):
            answer[permutation[row]][permutation[column]] = omega[row][column]
    return tuple(tuple(row) for row in answer)


def oriented_weights(
    omega: b65.QMatrix,
    effects: tuple[b65.Matrix, ...],
    hazard: Fraction,
) -> tuple[Fraction, ...]:
    no_record = b65.qadd(
        b65.qkron(b65.P0, b65.b63.IDENTITY),
        b65.qscale(1 - hazard, b65.qkron(b65.P1, b65.b63.IDENTITY)),
    )
    formation = tuple(
        b65.qscale(hazard, b65.qkron(b65.P1, effect)) for effect in effects
    )
    return tuple(
        b65.qtrace_product(omega, effect) for effect in (no_record,) + formation
    )


def x_conjugate(matrix: b65.Matrix) -> b65.Matrix:
    return b65.b63.matrix_multiply(
        b65.b63.PAULI_X,
        b65.b63.matrix_multiply(matrix, b65.b63.PAULI_X),
    )


def internal_instrument_intertwiner() -> dict[str, object]:
    """Tomographically complete controlled-X check of all four CP branches.

    This is an internal endpoint-coordinate equivalence.  It is deliberately
    not called a spatial proper-cubic endpoint-reversal theorem.
    """
    cx = controlled_x()
    x = b65.b63.to_numpy(b65.b63.PAULI_X)
    residual = 0.0
    cases = 0
    roots = {Fraction(1): 0.0, Fraction(3, 4): 0.5}
    for menu in (0, 1):
        right_effects_exact = b65.rotated_effects(b65.b64.IDENTITY_ROTATION, menu)
        left_effects_exact = tuple(x_conjugate(effect) for effect in right_effects_exact)
        for hazard in (Fraction(1), Fraction(3, 4)):
            root = roots[hazard]
            p0 = b65.qnumpy(b65.P0)
            p1 = b65.qnumpy(b65.P1)
            identity2 = np.eye(2, dtype=complex)
            kraus = np.kron(p0, identity2) + root * np.kron(p1, identity2)
            right_effects = tuple(
                float(hazard) * np.kron(p1, b65.b63.to_numpy(effect))
                for effect in right_effects_exact
            )
            left_effects = tuple(
                float(hazard) * np.kron(p1, b65.b63.to_numpy(effect))
                for effect in left_effects_exact
            )
            right_states = tuple(
                b65.b63.to_numpy(b65.b63.normalized_effect_state(effect))
                for effect in right_effects_exact
            )
            left_states = tuple(
                b65.b63.to_numpy(b65.b63.normalized_effect_state(effect))
                for effect in left_effects_exact
            )
            for row in range(4):
                for column in range(4):
                    unit = np.zeros((4, 4), dtype=complex)
                    unit[row, column] = 1
                    left_unit = cx @ unit @ cx.conj().T
                    right_no_record = kraus @ unit @ kraus.conj().T
                    left_no_record = kraus @ left_unit @ kraus.conj().T
                    residual = max(
                        residual,
                        float(np.linalg.norm(left_no_record - cx @ right_no_record @ cx.conj().T)),
                    )
                    cases += 1
                    for right_effect, left_effect, right_state, left_state in zip(
                        right_effects, left_effects, right_states, left_states
                    ):
                        right_output = np.trace(unit @ right_effect) * right_state
                        left_output = np.trace(left_unit @ left_effect) * left_state
                        residual = max(
                            residual,
                            float(np.linalg.norm(left_output - x @ right_output @ x.conj().T)),
                        )
                        cases += 1
    return {"branch_matrix_unit_cases": cases, "maximum_residual": residual}


def block65_composition() -> dict[str, object]:
    b63 = b65.b63
    b64 = b65.b64
    rho_zero = b63.matrix(1, 0, 0, 0)
    rho_fixture = b63.pure_real(Fraction(3, 5), Fraction(4, 5))
    rho_mix = b63.matrix_scale(Fraction(1, 2), b63.IDENTITY)
    fixtures = (
        b65.product_state(b65.P0, rho_zero),
        b65.product_state(b65.P1, rho_fixture),
        b65.product_state(b65.PPLUS, rho_mix),
        b65.bell_state(),
        b65.qscale(Fraction(1, 4), b65.qidentity(4)),
    )
    equivariant_failures = 0
    equivariant_cases = 0
    for omega_right in fixtures:
        omega_left = cx_density(omega_right)
        for menu in (0, 1):
            for hazard in (Fraction(1), Fraction(3, 4)):
                effects = b65.rotated_effects(b64.IDENTITY_ROTATION, menu)
                transformed_effects = tuple(
                    x_conjugate(effect) for effect in effects
                )
                right = oriented_weights(omega_right, effects, hazard)
                left = oriented_weights(omega_left, transformed_effects, hazard)
                equivariant_failures += right != left
                equivariant_cases += 1

    carrier_failures = 0
    carrier_cases = 0
    for menu in b63.MENUS:
        for label, effect in enumerate(menu, start=1):
            transformed = x_conjugate(effect)
            carrier_failures += x_conjugate(
                b63.outcome_carrier(effect, label)
            ) != b63.outcome_carrier(transformed, label)
            carrier_cases += 1

    fork_right_omega = b65.product_state(b65.P1, rho_zero)
    fork_left_omega = cx_density(fork_right_omega)
    base_effects = b65.rotated_effects(b64.IDENTITY_ROTATION, 0)
    fork_right = oriented_weights(fork_right_omega, base_effects, Fraction(1))
    fork_left_same_literal = oriented_weights(
        fork_left_omega, base_effects, Fraction(1)
    )

    initial = b65.bootstrap_distribution(
        b65.product_state(b65.P1, rho_fixture),
        b64.IDENTITY_ROTATION,
        0,
        0,
        Fraction(1),
    )[1:]
    stream = tuple(Fraction(value, 19) for value in (1, 5, 9, 13, 17, 3, 7, 11, 15))
    continuation_failures = 0
    continuation_microsteps = 0
    record_count = 0
    for first_outcome, branch in enumerate(initial):
        run = b65.continue_block64(branch.record_map(), 63, stream)
        word = (first_outcome,) + run.history
        expected = b63.cylinder_weight((rho_fixture, 0), word)
        future = b65.future_cylinder_weight(
            (b63.normalized_effect_state(b63.MENUS[0][first_outcome]), 1),
            run.history,
        )
        continuation_failures += not (
            run.ok
            and len(run.history) == 63
            and len(run.records) == 191
            and branch.weight * future == expected
        )
        continuation_microsteps += run.active_checks
        record_count = len(run.records)
    return {
        "fixtures": len(fixtures),
        "equivariant_cases": equivariant_cases,
        "equivariant_failures": equivariant_failures,
        "carrier_cases": carrier_cases,
        "carrier_failures": carrier_failures,
        "fork_right": fork_right,
        "fork_left_same_literal": fork_left_same_literal,
        "orientation_fork_distinct": fork_right != fork_left_same_literal,
        "continuation_failures": continuation_failures,
        "continuation_microsteps": continuation_microsteps,
        "records_N64": record_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "drop_decoder_gate",
            "basis_only",
            "skip_physical_route",
            "hide_charge_dictionary",
            "break_equivariance",
            "erase_orientation_fork",
            "broaden_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    cycle713_note = CYCLE713_NOTE.read_text(encoding="utf-8")
    block65_note = BLOCK65_NOTE.read_text(encoding="utf-8")
    source = " ".join(" ".join(item.split()) for item in (note, axiom, cycle713_note, block65_note))
    source_ok = all(
        phrase in source
        for phrase in (
            "it does not supply the formation site, probability, or rate",
            "It is not an occurrence selector",
            "retained identification of the runner's matter qubit",
            "oriented_endpoint_selector",
        )
    )
    checks.check(
        "A-current-source-and-target-boundary",
        source_ok,
        "current axioms, literal Cycle 713, and Block 65 identify the endpoint-state bridge without importing occurrence or context selection",
    )

    literal = literal_cycle713_decoder(mutation == "drop_decoder_gate")
    literal_ok = (
        literal["rows"] == 4096
        and not any(literal["failures"].values())
        and literal["right_PM_rows"] == ((0, 0), (0, 1), (1, 0), (1, 1))
        and literal["left_PM_rows"] == ((0, 0), (0, 1), (1, 0), (1, 1))
    )
    checks.check(
        "B-literal-Cycle713-no-additional-clean-ancilla-endpoint-decoder",
        literal_ok,
        f"{literal['rows']} executed seam rows obey p=l xor r; using Cycle 713's supplied p, each two-CNOT choice needs no additional clean ancilla and covers all four P-tensor-M basis rows",
    )

    coherent = coherent_code_intertwiner()
    coherent_ok = (
        coherent["matrix_units"] == (4 if mutation == "basis_only" else 16)
        and max(
            coherent["right_unitarity_residual"],
            coherent["left_unitarity_residual"],
            coherent["right_identity_residual"],
            coherent["left_controlled_X_residual"],
            coherent["right_clean_leakage"],
            coherent["left_clean_leakage"],
            coherent["matrix_unit_residual"],
        ) < TOL
    )
    checks.check(
        "C-arbitrary-coherent-density-intertwiner",
        coherent_ok,
        f"{coherent['matrix_units']}/16 matrix units intertwine with max residual {coherent['matrix_unit_residual']:.1e}; left/right reduced states differ by controlled X",
    )

    baseline_physical = c713.physical_word_certificate(2)
    physical_right = physical_bridge_certificate("right")
    physical_left = physical_bridge_certificate("left")
    route_failures = sum(
        int(item[key])
        for item in (physical_right, physical_left)
        for key in (
            "placement_collisions",
            "non_NN_failures",
            "operand_order_failures",
            "route_return_failures",
        )
    )
    physical_ok = (
        mutation != "skip_physical_route"
        and route_failures == 0
        and all(item["primitive_gates"] == baseline_physical["primitive_gates"] + 2 for item in (physical_right, physical_left))
        and all(item["total_assigned_M2"] == baseline_physical["total_assigned_M2"] for item in (physical_right, physical_left))
        and all(item["maximum_route_distance"] <= baseline_physical["maximum_route_distance"] for item in (physical_right, physical_left))
    )
    checks.check(
        "D-literal-nearest-neighbor-physical-routing",
        physical_ok,
        f"both logical basis changes add two qubit primitives with zero routing failures; routed gates right/left={physical_right['routed_gates']}/{physical_left['routed_gates']}, assigned M2={physical_right['total_assigned_M2']}",
    )

    charge = charge_dictionary()
    charge_ok = (
        mutation != "hide_charge_dictionary"
        and charge["reconstruction_failures"] == 0
        and charge["parity_failures"] == 0
        and charge["formation_number_failures"] == 0
        and charge["naive_matter_mismatches"] == 2
        and charge["number_commutator_norm"] > 1e-3
        and charge["operator_identity_residual"] < TOL
    )
    checks.check(
        "E-transformed-charge-dictionary-and-nonconservation-boundary",
        charge_ok,
        f"U N_old U^dagger=N_transformed with residual {charge['operator_identity_residual']:.1e}; on the code N=M+(P xor M), while commutator norm {charge['number_commutator_norm']:.3g} forbids an unchanged-number claim",
    )

    composition = block65_composition()
    superoperator = internal_instrument_intertwiner()
    equivariant_ok = (
        mutation != "break_equivariance"
        and composition["equivariant_cases"] == 20
        and composition["equivariant_failures"] == 0
        and composition["carrier_cases"] == 6
        and composition["carrier_failures"] == 0
        and superoperator["branch_matrix_unit_cases"] == 256
        and superoperator["maximum_residual"] < TOL
    )
    checks.check(
        "F-internal-controlled-X-Block65-instrument-intertwiner",
        equivariant_ok,
        f"{superoperator['branch_matrix_unit_cases']}/256 full branch/matrix-unit outputs intertwine with max residual {superoperator['maximum_residual']:.1e}; full spatial 24/576 endpoint-frame covariance remains open",
    )

    continuation_ok = (
        composition["continuation_failures"] == 0
        and composition["continuation_microsteps"] == 567
        and composition["records_N64"] == 191
    )
    checks.check(
        "G-conditional-Block65-Block64-history-continuation",
        continuation_ok,
        f"all three decoded-input formation branches continue conditionally for 64 outcomes through {composition['continuation_microsteps']} microsteps and {composition['records_N64']} permanent Records",
    )

    orientation_ok = (
        mutation != "erase_orientation_fork"
        and composition["orientation_fork_distinct"]
        and composition["fork_right"] == (Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(0))
        and composition["fork_left_same_literal"] == (Fraction(0), Fraction(0), Fraction(1, 5), Fraction(4, 5))
    )
    checks.check(
        "H-oriented-endpoint-selection-fork",
        orientation_ok,
        f"same literal menu gives right={composition['fork_right']} versus left={composition['fork_left_same_literal']}; the internal endpoint transform is fixed but its signed spatial-frame realization is physical law data",
    )

    boundary_needles = (
        "claim_type: bounded_theorem",
        "zero TOE percentage movement",
        "not a physical compilation of the",
        "not an unchanged number-preserving Cycle-713 matter word",
        "context/program/phase",
        "### N1",
        "### N8",
    )
    boundary_ok = all(needle in note for needle in boundary_needles) and mutation != "broaden_boundary"
    checks.check(
        "I-owner-interface-and-no-go-boundary",
        boundary_ok,
        "the decoded logical factor is literal, while one-site physical locality, spatial frame action, orientation, context, occurrence, source disposition, law adoption, and retention remain explicit",
    )

    print(
        "METRICS "
        f"cycle713_rows={literal['rows']} matrix_units={coherent['matrix_units']} "
        f"routed_right_left={physical_right['routed_gates']}/{physical_left['routed_gates']} "
        f"number_commutator={charge['number_commutator_norm']:.3g} "
        f"instrument_matrix_units={superoperator['branch_matrix_unit_cases']} continuation_microsteps={composition['continuation_microsteps']} "
        f"records_N64={composition['records_N64']}"
    )
    print(
        "BOUNDARY: Cycle 713 supplies an exact decoded P-tensor-M logical factor after an oriented two-CNOT basis change; the internal controlled-X instrument intertwiner is exact, but the signed 24-frame endpoint action, one-site physical implementation, transformed source disposition, context, occurrence, and law selection remain open"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
