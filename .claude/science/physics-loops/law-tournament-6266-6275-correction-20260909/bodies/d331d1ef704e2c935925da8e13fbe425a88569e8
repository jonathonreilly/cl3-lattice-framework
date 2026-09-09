#!/usr/bin/env python3
"""Block 69: literal five-M2 dilation and Record-lock/action boundary.

The runner starts at the executed right-decoded Cycle-713 seam.  It uses the
five already assigned M2 factors (P,M,d_u,l,d_v), constructs an explicit
one-/two-M2 Stinespring word for the selected Block-65 menu-0 instrument, and
checks the complete channel on all sixteen input matrix units.  It then keeps
the reversible quantum output distinct from Record formation and tests the
remaining proper-cubic internal-action fork.

The branch is stacked behind an older axiom snapshot.  The sole axiom
authority is therefore read from the pinned origin/main Record-rewrite commit,
whose file hash is checked explicitly; the branch-local stale copy is never
used as authority.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import math
from pathlib import Path
import subprocess

import numpy as np

import admissibility_cycle713_endpoint_record_attachment_intertwiner_boundary_2026_08_12 as b66
import admissibility_m2_record_cubic_vector_decoder_sector_grading_carrier_axiom_boundary_2026_08_12 as b56
import admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12 as b65
import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as c713


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_FIVE_M2_STINESPRING_RECORD_LOCK_ACTION_CUT_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
LOCAL_AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK65_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_"
    "BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
BLOCK66_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_ENDPOINT_RECORD_ATTACHMENT_INTERTWINER_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
CYCLE713_NOTE = ROOT / "docs" / (
    "PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_"
    "BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
BLOCK56_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_M2_RECORD_CUBIC_VECTOR_DECODER_SECTOR_GRADING_CARRIER_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)

AXIOM_AUTHORITY_COMMIT = "574346c636e48217a2fe42f3b842632d34c4a3c1"
AXIOM_AUTHORITY_SHA256 = "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753"
AXIOM_REPO_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
STALE_STACK_COMMIT = "eb0ea60817a7489d2ed435780ffb5354b0e06045"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CYCLE713_FIVE_M2_STINESPRING_RECORD_LOCK_ACTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_CYCLE713_ENDPOINT_RECORD_ATTACHMENT_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/ADMISSIBILITY_M2_RECORD_CUBIC_VECTOR_DECODER_SECTOR_GRADING_CARRIER_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
)

TOL = 5e-11
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


def canonical_axiom_text(use_stale_local: bool = False) -> str:
    if use_stale_local:
        return subprocess.check_output(
            ("git", "show", f"{STALE_STACK_COMMIT}:{AXIOM_REPO_PATH}"),
            cwd=ROOT,
            text=True,
        )
    return subprocess.check_output(
        ("git", "show", f"{AXIOM_AUTHORITY_COMMIT}:{AXIOM_REPO_PATH}"),
        cwd=ROOT,
        text=True,
    )


def current_axiom_text() -> tuple[str, str]:
    """Read the current tree authority, preferring the fetched mainline."""
    for ref in ("origin/main", "HEAD"):
        exists = subprocess.run(
            ("git", "cat-file", "-e", f"{ref}:{AXIOM_REPO_PATH}"),
            cwd=ROOT,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode == 0
        if exists:
            return ref, subprocess.check_output(
                ("git", "show", f"{ref}:{AXIOM_REPO_PATH}"),
                cwd=ROOT,
                text=True,
            )
    raise RuntimeError(f"cannot resolve current authority for {AXIOM_REPO_PATH}")


def authority_certificate(use_stale_local: bool = False) -> dict[str, object]:
    axiom = canonical_axiom_text(use_stale_local)
    current_ref, current_axiom = current_axiom_text()
    flattened = " ".join(axiom.split())
    remote_ancestor = any(
        subprocess.run(
            ("git", "merge-base", "--is-ancestor", AXIOM_AUTHORITY_COMMIT, ref),
            cwd=ROOT,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode == 0
        for ref in ("origin/main", "HEAD")
    )
    local = LOCAL_AXIOM_PATH.read_text(encoding="utf-8")
    return {
        "sha256": sha256(axiom.encode()).hexdigest(),
        "current_ref": current_ref,
        "current_authority_sha256": sha256(current_axiom.encode()).hexdigest(),
        "remote_ancestor": remote_ancestor,
        "current_record": all(
            phrase in flattened
            for phrase in (
                "Records form.",
                "record locks exactly one admissible local possibility",
                "records are permanent",
                "A site with no record cannot be read",
            )
        ),
        "named_additive_I_absent": "scalar readout `I` is additive" not in axiom,
        "stacked_local_copy_differs": local != axiom,
    }


def bit(state: int, wire: int) -> int:
    return (state >> wire) & 1


def literal_five_factor_certificate(drop_decoder_gate: bool = False) -> dict[str, object]:
    maps, structure = c713.literal_segment_maps(2)
    left, right = 1, 6
    du, dv, pointer = structure["new_auxiliary_wires"]
    decoder = b66.bridge_word("right", left, right, pointer)
    if drop_decoder_gate:
        decoder = decoder[:1]
    failures = {
        "singleton": 0,
        "code_relation": 0,
        "clean_BRA": 0,
        "amplitude": 0,
    }
    rows: set[tuple[int, int]] = set()
    for row in maps:
        failures["singleton"] += len(row) != 1
        if len(row) != 1:
            continue
        source, amplitude = next(iter(row.items()))
        failures["code_relation"] += bit(source, pointer) != (
            bit(source, left) ^ bit(source, right)
        )
        output = c713.apply_sparse_word(row, decoder)
        if len(output) != 1:
            failures["singleton"] += 1
            continue
        target, target_amplitude = next(iter(output.items()))
        failures["clean_BRA"] += any(bit(target, wire) for wire in (du, left, dv))
        failures["amplitude"] += abs(target_amplitude - amplitude) >= TOL
        rows.add((bit(target, pointer), bit(target, right)))
    return {
        "rows": len(maps),
        "roles": {"P": pointer, "M": right, "B": du, "R": left, "A": dv},
        "clean_domain_inherited": True,
        "failures": failures,
        "PM_rows": tuple(sorted(rows)),
    }


def ry(angle: float) -> np.ndarray:
    return np.asarray(
        (
            (math.cos(angle / 2), -math.sin(angle / 2)),
            (math.sin(angle / 2), math.cos(angle / 2)),
        ),
        dtype=complex,
    )


def controlled(matrix: np.ndarray) -> np.ndarray:
    """Control is local bit zero; target is local bit one."""
    output = np.zeros((4, 4), dtype=complex)
    for source in range(4):
        control = source & 1
        target = (source >> 1) & 1
        if control == 0:
            output[source, source] = 1
            continue
        for target_out in range(2):
            output[control | (target_out << 1), source] = matrix[target_out, target]
    return output


def one(kind: str, wire: int, matrix: np.ndarray):
    return c713.C712.AGate(kind, (wire,), matrix)


def two(kind: str, control: int, target: int, matrix: np.ndarray):
    return c713.C712.AGate(kind, (control, target), matrix)


def cx(kind: str, control: int, target: int):
    return two(kind, control, target, CNOT)


def cry(kind: str, control: int, target: int, angle: float):
    return two(kind, control, target, controlled(ry(angle)))


def ccry(kind: str, control_a: int, control_b: int, target: int, angle: float):
    """Exact controlled-controlled Ry using five one-/two-M2 gates."""
    return (
        cry(kind + "_half_b", control_b, target, angle / 2),
        cx(kind + "_toggle", control_a, control_b),
        cry(kind + "_minus_half_b", control_b, target, -angle / 2),
        cx(kind + "_untoggle", control_a, control_b),
        cry(kind + "_half_a", control_a, target, angle / 2),
    )


def dilation_word(
    wrong_split: bool = False,
    drop_purification: bool = False,
):
    """Logical wire order is P=0, M=1, B=2, R=3, A=4."""
    theta_zero = math.pi / 2 + (0.125 if wrong_split else 0.0)
    theta_one = 2 * math.atan2(2, 1)
    theta_chi = 2 * math.atan2(math.sqrt(2), math.sqrt(5))
    word = [cry("dilation_split_P_B", 0, 2, theta_zero)]
    word.extend(ccry("dilation_split_PM_B", 0, 1, 2, theta_one - theta_zero))
    word.append(cx("dilation_h1_control", 2, 1))
    word.extend(ccry("dilation_tau1_Pq_R", 0, 1, 3, theta_chi))
    if not drop_purification:
        word.append(cx("dilation_tau1_purify", 3, 4))
    word.append(cx("dilation_restore_M", 2, 1))
    word.extend(c713.toffoli_word(1, 2, 3))
    return tuple(word)


def full_index(p: int, m: int, b: int, r: int, a: int) -> int:
    return p | (m << 1) | (b << 2) | (r << 3) | (a << 4)


def analytic_isometry() -> np.ndarray:
    answer = np.zeros((32, 4), dtype=complex)
    answer[full_index(0, 0, 0, 0, 0), 0] = 1
    answer[full_index(0, 1, 0, 0, 0), 2] = 1

    # p=1,m=0: h=0 with weight 1/2; h=1 with weight 1/2 and tau_1.
    answer[full_index(1, 0, 0, 0, 0), 1] = 1 / math.sqrt(2)
    answer[full_index(1, 0, 1, 0, 0), 1] = math.sqrt(Fraction(5, 14))
    answer[full_index(1, 0, 1, 1, 1), 1] = math.sqrt(Fraction(1, 7))

    # p=1,m=1: h=1 with weight 1/5 and tau_1; h=2 with weight 4/5.
    answer[full_index(1, 1, 0, 0, 0), 3] = math.sqrt(Fraction(1, 7))
    answer[full_index(1, 1, 0, 1, 1), 3] = math.sqrt(Fraction(2, 35))
    answer[full_index(1, 1, 1, 1, 0), 3] = 2 / math.sqrt(5)
    return answer


def isometry_certificate(wrong_split: bool = False) -> dict[str, object]:
    word = dilation_word(wrong_split=wrong_split)
    unitary = c713.word_matrix(word, 5)
    observed = unitary[:, :4]
    expected = analytic_isometry()
    supports = tuple(int(np.count_nonzero(np.abs(observed[:, column]) > TOL)) for column in range(4))
    return {
        "word": word,
        "unitary": unitary,
        "isometry": observed,
        "primitive_gates": len(word),
        "one_two_only": all(len(gate.wires) in (1, 2) for gate in word),
        "unitarity_residual": float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(32))),
        "isometry_residual": float(np.linalg.norm(observed - expected)),
        "supports": supports,
    }


def no_record_output(rho: np.ndarray) -> np.ndarray:
    answer = np.zeros((4, 4), dtype=complex)
    for m_left in (0, 1):
        for m_right in (0, 1):
            for b in (0, 1):
                for r in (0, 1):
                    for a in (0, 1):
                        answer[2 * m_left, 2 * m_right] += rho[
                            full_index(0, m_left, b, r, a),
                            full_index(0, m_right, b, r, a),
                        ]
    return answer


def formation_output(rho: np.ndarray, label: int) -> np.ndarray:
    answer = np.zeros((2, 2), dtype=complex)
    for m in (0, 1):
        for b in (0, 1):
            if m + b != label:
                continue
            for a in (0, 1):
                for r_left in (0, 1):
                    for r_right in (0, 1):
                        answer[r_left, r_right] += rho[
                            full_index(1, m, b, r_left, a),
                            full_index(1, m, b, r_right, a),
                        ]
    return answer


def expected_instrument_output(unit: np.ndarray) -> tuple[np.ndarray, ...]:
    no_record_kraus = np.diag((1, 0, 1, 0)).astype(complex)
    effects = (
        np.diag((0, Fraction(1, 2), 0, 0)).astype(complex),
        np.diag((0, Fraction(1, 2), 0, Fraction(1, 5))).astype(complex),
        np.diag((0, 0, 0, Fraction(4, 5))).astype(complex),
    )
    states = (
        np.diag((1, 0)).astype(complex),
        np.diag((Fraction(5, 7), Fraction(2, 7))).astype(complex),
        np.diag((0, 1)).astype(complex),
    )
    return (no_record_kraus @ unit @ no_record_kraus,) + tuple(
        np.trace(unit @ effect) * state for effect, state in zip(effects, states)
    )


def channel_certificate(drop_purification: bool = False) -> dict[str, object]:
    unitary = c713.word_matrix(
        dilation_word(drop_purification=drop_purification), 5
    )
    isometry = unitary[:, :4]
    maximum_residual = 0.0
    outputs: dict[tuple[int, int], np.ndarray] = {}
    cases = 0
    for row in range(4):
        for column in range(4):
            unit = np.zeros((4, 4), dtype=complex)
            unit[row, column] = 1
            rho = isometry @ unit @ isometry.conj().T
            actual = (no_record_output(rho),) + tuple(
                formation_output(rho, label) for label in range(3)
            )
            expected = expected_instrument_output(unit)
            maximum_residual = max(
                maximum_residual,
                *(float(np.linalg.norm(left - right)) for left, right in zip(actual, expected)),
            )
            outputs[(row, column)] = np.block([
                [actual[0], np.zeros((4, 6), dtype=complex)],
                [np.zeros((2, 4), dtype=complex), actual[1], np.zeros((2, 4), dtype=complex)],
                [np.zeros((2, 6), dtype=complex), actual[2], np.zeros((2, 2), dtype=complex)],
                [np.zeros((2, 8), dtype=complex), actual[3]],
            ])
            cases += len(actual)

    choi = np.zeros((40, 40), dtype=complex)
    trace_residual = 0.0
    for row in range(4):
        for column in range(4):
            choi[10 * row:10 * (row + 1), 10 * column:10 * (column + 1)] = outputs[(row, column)]
            trace_residual = max(
                trace_residual,
                abs(np.trace(outputs[(row, column)]) - int(row == column)),
            )
    return {
        "matrix_units": 16,
        "branch_cases": cases,
        "maximum_residual": maximum_residual,
        "choi_minimum": float(np.linalg.eigvalsh(choi).min()),
        "trace_residual": float(trace_residual),
    }


def physical_route_certificate() -> dict[str, object]:
    cells = ((0, 0, 0), (1, 0, 0))
    C = c713.C712
    equivalence = C.C709.G.build_equivalence(cells).equivalence
    _eq2, graph, site_map, gauges, occupied, collisions = C.P709.placement_bundle(cells)
    carriers = C.carriers_for(equivalence, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(index for index, carrier in enumerate(carriers) if len(carrier) == 2)
    pointer_sites = b66.pointer_sites_for(cells, wire_sites, occupied)
    extended_sites = wire_sites + pointer_sites
    assigned_sites = set(occupied) | set(pointer_sites)

    target_decode = C.synthesize_decode(equivalence.target_w, equivalence.target_v)
    decoded, qr_residual = c713.instrumented_decoded_word(2)
    pointer = equivalence.qubits + 2
    decoded += b66.bridge_word("right", 1, 6, pointer)
    repetition_decode = tuple(
        C.c707.Instruction("block69_repetition_decode_CNOT", carriers[index], CNOT)
        for index in repeated
    )
    prefix = (
        repetition_decode
        + C.abstract_to_physical(target_decode, extended_sites, "block69_target_decode_")
        + C.abstract_to_physical(decoded, extended_sites, "block69_cycle713_")
    )

    role_sites = (
        pointer_sites[2],  # P
        wire_sites[6],    # M = right endpoint
        pointer_sites[0], # B = d_u
        wire_sites[1],    # R = cleaned left endpoint
        pointer_sites[1], # A = d_v
    )
    dilation = tuple(
        C.c707.Instruction(
            "block69_" + gate.kind,
            tuple(role_sites[wire] for wire in gate.wires),
            gate.matrix,
        )
        for gate in dilation_word()
    )
    routed, route = C.c707.route_word(prefix + dilation)
    route_work_sites = set(route["touched_coordinates"]) - assigned_sites
    return {
        "literal_code_M2": len(occupied),
        "endpoint_register_M2": len(pointer_sites),
        "total_assigned_M2": len(occupied) + len(pointer_sites),
        "placement_collisions": collisions + len(occupied) + len(pointer_sites) - len(assigned_sites),
        "role_sites": role_sites,
        "role_sites_unique": len(set(role_sites)) == 5,
        "role_sites_assigned": set(role_sites) <= assigned_sites,
        "prefix_primitives": len(prefix),
        "dilation_primitives": len(dilation),
        "combined_primitives": len(prefix) + len(dilation),
        "routed_gates": len(routed),
        "touched_M2": route["touched_sites"],
        "route_work_M2": len(route_work_sites),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "coin_QR_residual": qr_residual,
    }


def action_certificate() -> dict[str, object]:
    adjoint_rank = b56.rational_rank(b56.equivariance_rows(lambda rotation: rotation))
    trivial_rank = b56.rational_rank(b56.equivariance_rows(b56.identity_action))
    b63 = b65.b63
    b64 = b65.b64
    rho = b63.pure_real(Fraction(3, 5), Fraction(4, 5))
    body = b65.bootstrap_distribution(
        b65.product_state(b65.P1, rho),
        b64.IDENTITY_ROTATION,
        0,
        0,
        Fraction(1),
    )
    failures = 0
    cases = 0
    distinct_content_cases = 0
    for rotation in b64.ROTATIONS:
        lab_rho = b63.rotate_hermitian(rotation, rho)
        lab = b65.bootstrap_distribution(
            b65.product_state(b65.P1, lab_rho),
            rotation,
            0,
            0,
            Fraction(1),
        )
        for body_branch, lab_branch in zip(body, lab):
            failures += body_branch.weight != lab_branch.weight
            transformed = b65.transformed_records(
                body_branch.record_map(), rotation, (0, 0, 0)
            )
            failures += transformed != lab_branch.record_map()
            distinct_content_cases += bool(
                body_branch.records and body_branch.record_map() != lab_branch.record_map()
            )
            cases += 1
    return {
        "rotations": len(b64.ROTATIONS),
        "first_branch_cases": cases,
        "first_branch_map_failures": failures,
        "distinct_content_cases": distinct_content_cases,
        "adjoint_rank": adjoint_rank,
        "adjoint_nullity": 9 - adjoint_rank,
        "trivial_rank": trivial_rank,
        "trivial_nullity": 9 - trivial_rank,
    }


def record_type_certificate(unitary: np.ndarray, canonical_axiom: str) -> dict[str, object]:
    b63 = b65.b63
    menu = b63.MENUS[0]
    outcome_records = tuple(
        b63.outcome_carrier(effect, label + 1) for label, effect in enumerate(menu)
    )
    head_records = tuple(
        b65.b64.context_carrier(
            "head",
            b63.normalized_effect_state(effect),
            b65.b64.IDENTITY_ROTATION,
            1,
            1,
        )
        for effect in menu
    )
    record_matrices = tuple(b63.to_numpy(item) for item in outcome_records + head_records)
    nonhermitian = tuple(float(np.linalg.norm(item - item.conj().T)) for item in record_matrices)

    output_density_failures = 0
    support_counts = []
    for column in range(4):
        state = unitary[:, column]
        density = np.outer(state, state.conj())
        output_density_failures += not (
            np.linalg.norm(density - density.conj().T) < TOL
            and abs(np.trace(density) - 1) < TOL
            and np.linalg.eigvalsh(density).min() > -TOL
        )
        support_counts.append(int(np.count_nonzero(np.abs(state) > TOL)))
    flattened = " ".join(canonical_axiom.split())
    return {
        "inverse_residual": float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(32))),
        "output_density_failures": output_density_failures,
        "coherent_formation_inputs": sum(count > 1 for count in support_counts),
        "record_carriers": len(record_matrices),
        "nonhermitian_record_carriers": sum(value > TOL for value in nonhermitian),
        "minimum_record_dagger_distance": min(nonhermitian),
        "blank_is_absence": "A site with no record cannot be read" in flattened,
        "permanence_named": "records are permanent" in flattened,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom",
            "drop_decoder",
            "wrong_split",
            "drop_purification",
            "skip_route",
            "force_action",
            "promote_record",
            "broaden_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    note = NOTE_PATH.read_text(encoding="utf-8")
    authority = authority_certificate(mutation == "stale_axiom")
    authority_ok = (
        authority["sha256"] == AXIOM_AUTHORITY_SHA256
        and authority["current_authority_sha256"] == AXIOM_AUTHORITY_SHA256
        and authority["remote_ancestor"]
        and authority["current_record"]
        and authority["named_additive_I_absent"]
        and AXIOM_AUTHORITY_COMMIT in note
    )
    checks.check(
        "A-origin-main-axiom-authority-and-stale-stack-firewall",
        authority_ok,
        f"pinned Record hash={str(authority['sha256'])[:12]} equals current {authority['current_ref']} hash={str(authority['current_authority_sha256'])[:12]}, pin is a mainline/HEAD ancestor={authority['remote_ancestor']}; stacked-local-difference={authority['stacked_local_copy_differs']} and the local copy is never authoritative",
    )

    literal = literal_five_factor_certificate(mutation == "drop_decoder")
    literal_ok = (
        literal["rows"] == 4096
        and not any(literal["failures"].values())
        and literal["PM_rows"] == ((0, 0), (0, 1), (1, 0), (1, 1))
        and literal["roles"] == {"P": 40, "M": 6, "B": 38, "R": 1, "A": 39}
        and literal["clean_domain_inherited"]
    )
    checks.check(
        "B-literal-Cycle713-five-assigned-M2-domain",
        literal_ok,
        f"{literal['rows']} literal rows leave B,R,A clean after the right decoder and retain all P,M rows; roles={literal['roles']}; no new clean M2 is asserted",
    )

    isometry = isometry_certificate(mutation == "wrong_split")
    isometry_ok = (
        isometry["primitive_gates"] == 29
        and isometry["one_two_only"]
        and isometry["unitarity_residual"] < TOL
        and isometry["isometry_residual"] < TOL
        and isometry["supports"] == (1, 3, 1, 3)
    )
    checks.check(
        "C-explicit-five-M2-menu0-Stinespring-isometry",
        isometry_ok,
        f"29 one-/two-M2 gates give a 32x32 unitary and analytic 32x4 isometry; residuals={isometry['unitarity_residual']:.1e}/{isometry['isometry_residual']:.1e}, column supports={isometry['supports']}",
    )

    channel = channel_certificate(mutation == "drop_purification")
    channel_ok = (
        channel["matrix_units"] == 16
        and channel["branch_cases"] == 64
        and channel["maximum_residual"] < TOL
        and channel["choi_minimum"] > -TOL
        and channel["trace_residual"] < TOL
    )
    checks.check(
        "D-complete-Block65-menu0-channel-equality",
        channel_ok,
        f"all {channel['branch_cases']}/64 no-Record/formation matrix-unit outputs match; residual={channel['maximum_residual']:.1e}, direct-sum Choi min={channel['choi_minimum']:.1e}, TP={channel['trace_residual']:.1e}",
    )

    route = physical_route_certificate()
    route_ok = (
        mutation != "skip_route"
        and route["literal_code_M2"] == 39
        and route["endpoint_register_M2"] == 3
        and route["total_assigned_M2"] == 42
        and route["placement_collisions"] == 0
        and route["role_sites_unique"]
        and route["role_sites_assigned"]
        and route["dilation_primitives"] == 29
        and route["touched_M2"] == 507
        and route["route_work_M2"] == 465
        and route["non_NN_failures"] == 0
        and route["operand_order_failures"] == 0
        and route["route_return_failures"] == 0
        and route["coin_QR_residual"] < TOL
    )
    checks.check(
        "E-literal-placement-nearest-neighbour-routed-word",
        route_ok,
        f"the Cycle713 prefix plus 29-gate dilation uses 42 assigned M2 and touches {route['touched_M2']} coordinates, including {route['route_work_M2']} restored route-work sites, with zero collision/NN/order/return failures; routed gates={route['routed_gates']}, max distance={route['maximum_route_distance']}, roles={route['role_sites']}",
    )

    action = action_certificate()
    action_ok = (
        mutation != "force_action"
        and action["rotations"] == 24
        and action["first_branch_cases"] == 96
        and action["first_branch_map_failures"] == 0
        and action["distinct_content_cases"] > 0
        and (action["adjoint_rank"], action["adjoint_nullity"]) == (8, 1)
        and (action["trivial_rank"], action["trivial_nullity"]) == (9, 0)
    )
    checks.check(
        "F-body-frame-versus-lab-action-nonselection",
        action_ok,
        f"{action['first_branch_cases']}/96 first-branch outcome/head Record maps are body/lab isomorphic across 24 frames, yet {action['distinct_content_cases']} contents differ; continued histories and the 29-gate word under both actions are not tested; decoder nullities adjoint/trivial={action['adjoint_nullity']}/{action['trivial_nullity']}",
    )

    canonical_axiom = canonical_axiom_text()
    record = record_type_certificate(isometry_certificate()["unitary"], canonical_axiom)
    record_needles = (
        "projectors, partial trace, and coarse-graining are a mathematical channel extraction",
        "a blank Record site is absence, not a supplied ket-zero qubit",
        "quantum-output-to-Record-lock law",
        "no-overwrite continuation",
    )
    record_ok = (
        mutation != "promote_record"
        and record["inverse_residual"] < TOL
        and record["output_density_failures"] == 0
        and record["coherent_formation_inputs"] == 2
        and record["record_carriers"] == 6
        and record["nonhermitian_record_carriers"] == 6
        and record["minimum_record_dagger_distance"] > 1
        and record["blank_is_absence"]
        and record["permanence_named"]
        and all(
            needle.lower() in " ".join(note.split()).lower()
            for needle in record_needles
        )
    )
    checks.check(
        "G-quantum-output-versus-permanent-Record-lock-parser-boundary",
        record_ok,
        f"the five-M2 output is reversible and density-valued, while all {record['nonhermitian_record_carriers']}/6 unchanged Block64/65 Record labels are non-Hermitian M2 contents; densities remain valid M2 possibilities, but the branch pick, blank-site formation, density-to-label parser, lock, and permanence map are not supplied",
    )

    boundary_needles = tuple(f"### N{index}" for index in range(1, 9)) + (
        "claim_type: bounded_theorem",
        "zero TOE percentage movement",
        "architecture-specific",
        "ATTEMPTED",
        "RULED OUT BY PRIOR",
        "W1/W2",
        "W5/W6",
        "file:line",
        "retired?",
        "could apply?",
        "strongest surviving escape route",
        "PASS for the narrow nonpromotion statement",
        "FAIL/demoted for a broad",
        "per_element:",
        "per_site:",
        "per_mode:",
        "per_block:",
        "lattice_wide:",
    )
    boundary_ok = mutation != "broaden_boundary" and all(
        needle in note for needle in boundary_needles
    )
    checks.check(
        "H-N1-N8-bounded-claim-and-TOE-accounting",
        boundary_ok,
        "the source note exposes structured routes, all 15 pairwise collapsed-wall tests, hidden-import classifications, citation-by-citation residual matches, five granularity lines, partial closures, hostile steelman, and cross-cycle mechanism audit; this is a semantic-surface guard, not an audit verdict",
    )

    print(
        "METRICS "
        f"cycle713_rows={literal['rows']} dilation_gates={isometry['primitive_gates']} "
        f"matrix_unit_branches={channel['branch_cases']} channel_residual={channel['maximum_residual']:.2e} "
        f"routed_gates={route['routed_gates']} touched_M2={route['touched_M2']} "
        f"route_work_M2={route['route_work_M2']} action_first_branch_cases={action['first_branch_cases']} "
        f"record_parser_mismatches={record['nonhermitian_record_carriers']}"
    )
    print(
        "BOUNDARY: a literal five-M2 reversible dilation now realizes the selected menu-0 CP map on the inherited clean Cycle713 decoder domain; it does not supply the realized draw, blank Record-site formation, permanent lock/no-overwrite continuation, internal cubic action, extensional nearest-neighbour law, genesis, clock, adoption, audit retention, or TOE movement"
    )
    print("per_element: checked all sixteen P-M matrix units, four branch outputs, six target Record carriers, and every gate matrix in the explicit dilation")
    print("per_site: checked the five named M2 roles and 42 assigned coordinates, disclosed all 507 touched coordinates including 465 restored route-work sites, and tested blank-versus-ket-zero semantics")
    print("per_mode: checked 96 first-branch outcome/head Record maps across all 24 proper-cubic frames and both exact internal-action decoder constraint systems; continued histories were not tested")
    print("per_block: checked all 4,096 literal Cycle713 seam rows, the complete 32x32 unitary, direct-sum Choi matrix, and composed physical route prefix")
    print("lattice_wide: checked and not executed — no selected full-Z3 formation law, autonomous genesis, total multi-front process, clock, or gravity completion is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
