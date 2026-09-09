#!/usr/bin/env python3
"""Bounded physical-M2 endpoint-instrument splice from Cycle712 to Cycle704/612.

This inserts a coherent seam-change opportunity pointer into the decoded
Cycle712 joint state isometry.  The pointer is an instrument output, not an
occurrence, clock, Record, or Born variable.  Its clean ancillas and the
Cycle610/612 actuality/admission inputs remain supplied.
"""

from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = (
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_"
    "CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_"
    "CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_"
    "CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/"
    "CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26 as I712
import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704


TOL = 3e-11
BASELINE = "ebd05531036b844883e2e73186ebd95c46ffc119"
T = np.diag((1.0, np.exp(0.25j * np.pi))).astype(complex)
TDG = T.conj().T
H = C712.c707.c655.H
CNOT = C712.c707.c655.CNOT


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def transitive_repo_script_paths():
    scripts_dir = ROOT / "scripts"
    module_paths = {path.stem: path for path in scripts_dir.glob("*.py")}
    pending = [Path(__file__).resolve()]
    seen = set()
    while pending:
        path = pending.pop()
        if path in seen:
            continue
        seen.add(path)
        tree = ast.parse(path.read_text(), filename=str(path))
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.append(node.module.split(".")[0])
        pending.extend(
            module_paths[name]
            for name in imported
            if name in module_paths and module_paths[name] not in seen
        )
    return tuple(sorted(path.relative_to(ROOT).as_posix() for path in seen))


def provenance_certificate():
    source_paths = transitive_repo_script_paths()
    declared_scripts = {
        path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")
    }
    missing = tuple(path for path in source_paths if path not in declared_scripts)
    declared = tuple((ROOT / path).resolve() for path in AUDIT_INPUT_PATHS)
    actual_head = subprocess.check_output(
        ("git", "rev-parse", "HEAD"), cwd=ROOT, text=True
    ).strip()
    ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", BASELINE, actual_head),
        cwd=ROOT, check=False,
    ).returncode == 0
    untracked = tuple(
        path for path in AUDIT_INPUT_PATHS
        if subprocess.run(
            ("git", "ls-files", "--error-unmatch", "--", path),
            cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode != 0
    )
    return {
        "baseline_commit": BASELINE,
        "actual_HEAD": actual_head,
        "baseline_is_ancestor": ancestor,
        "declared_paths": len(declared),
        "declared_path_failures": sum(
            not path.is_file() or not path.is_relative_to(ROOT) for path in declared
        ),
        "duplicate_declared_paths": len(declared) - len(set(declared)),
        "transitive_repo_scripts": len(source_paths),
        "missing_transitive_scripts": missing,
        "untracked_declared_paths": untracked,
        "source_inventory_sha256": {
            path: digest(ROOT / path) for path in AUDIT_INPUT_PATHS
            if (ROOT / path).is_file()
        },
    }


def one(kind, wire, matrix):
    return C712.AGate(kind, (wire,), matrix)


def cnot(kind, control, target):
    return C712.AGate(kind, (control, target), CNOT)


def toffoli_word(control_a, control_b, target):
    """Exact H/T/CNOT decomposition, all gates one- or two-M2."""
    return (
        one("endpoint_OR_Toffoli_H", target, H),
        cnot("endpoint_OR_Toffoli_CNOT", control_b, target),
        one("endpoint_OR_Toffoli_Tdg", target, TDG),
        cnot("endpoint_OR_Toffoli_CNOT", control_a, target),
        one("endpoint_OR_Toffoli_T", target, T),
        cnot("endpoint_OR_Toffoli_CNOT", control_b, target),
        one("endpoint_OR_Toffoli_Tdg", target, TDG),
        cnot("endpoint_OR_Toffoli_CNOT", control_a, target),
        one("endpoint_OR_Toffoli_T", control_b, T),
        one("endpoint_OR_Toffoli_T", target, T),
        one("endpoint_OR_Toffoli_H", target, H),
        cnot("endpoint_OR_Toffoli_CNOT", control_a, control_b),
        one("endpoint_OR_Toffoli_T", control_a, T),
        one("endpoint_OR_Toffoli_Tdg", control_b, TDG),
        cnot("endpoint_OR_Toffoli_CNOT", control_a, control_b),
    )


def word_matrix(word, count):
    output = np.eye(1 << count, dtype=complex)
    for gate in word:
        output = C712.S25.embed_gate(gate.matrix, gate.wires, count) @ output
    return output


def exact_toffoli():
    output = np.zeros((8, 8), complex)
    for source in range(8):
        target = source
        if ((source >> 0) & 1) and ((source >> 1) & 1):
            target ^= 1 << 2
        output[target, source] = 1
    return output


def endpoint_register_word(left, right, du, dv, pointer):
    """Pre-seam writes, OR after seam, then clean delta scratch."""
    before = (
        cnot("endpoint_pre_left", left, du),
        cnot("endpoint_pre_right", right, dv),
    )
    after_and_or = (
        cnot("endpoint_post_left", left, du),
        cnot("endpoint_post_right", right, dv),
        cnot("endpoint_OR_CNOT", du, pointer),
        cnot("endpoint_OR_CNOT", dv, pointer),
    ) + toffoli_word(du, dv, pointer)
    clean = (
        cnot("endpoint_clean_left_from_left", left, du),
        cnot("endpoint_clean_left_from_right", right, du),
        cnot("endpoint_clean_right_from_left", left, dv),
        cnot("endpoint_clean_right_from_right", right, dv),
    )
    return before, after_and_or, clean


def instrumented_decoded_word(cell_count=2):
    coarse, qr_residual = C712.decoded_word(cell_count)
    first_seam = next(i for i, gate in enumerate(coarse) if gate.kind == "seam_FSWAP")
    first_contact = next(i for i, gate in enumerate(coarse) if gate.kind == "onsite_contact")
    prefix = list(coarse[:first_seam])
    seams = coarse[first_seam:first_contact]
    contacts = coarse[first_contact:]
    output = list(prefix)
    # The decoded tableau always places matter first, then stabilizer auxiliaries.
    aux_base = C712.C709.G.build_equivalence(
        tuple((i, 0, 0) for i in range(cell_count))
    ).equivalence.qubits
    for seam_index in range(cell_count - 1):
        left, right = 6 * seam_index + 1, 6 * (seam_index + 1)
        du, dv, pointer = (
            aux_base + 3 * seam_index,
            aux_base + 3 * seam_index + 1,
            aux_base + 3 * seam_index + 2,
        )
        before, after_and_or, clean = endpoint_register_word(
            left, right, du, dv, pointer
        )
        output.extend(before)
        output.extend(seams[9 * seam_index:9 * (seam_index + 1)])
        output.extend(after_and_or)
        output.extend(clean)
    output.extend(contacts)
    return tuple(output), qr_residual


def apply_sparse_gate(state, gate):
    """Apply one actual AGate to a sparse arbitrary-width state."""
    output = {}
    for source, source_amplitude in state.items():
        local_source = sum(
            ((source >> wire) & 1) << index
            for index, wire in enumerate(gate.wires)
        )
        for local_target in range(1 << len(gate.wires)):
            coefficient = gate.matrix[local_target, local_source]
            if abs(coefficient) <= 1e-16:
                continue
            target = source
            for index, wire in enumerate(gate.wires):
                target = (
                    target & ~(1 << wire)
                ) | (((local_target >> index) & 1) << wire)
            output[target] = output.get(target, 0.0j) + coefficient * source_amplitude
    return {
        basis: amplitude for basis, amplitude in output.items()
        if abs(amplitude) > 1e-13
    }


def apply_sparse_word(state, word):
    output = dict(state)
    for gate in word:
        output = apply_sparse_gate(output, gate)
    return output


def decoded_instrument_structure(cell_count=2):
    """Extract and audit the literal endpoint splice from its actual gate word."""
    instrumented, _qr = instrumented_decoded_word(cell_count)
    coarse, _coarse_qr = C712.decoded_word(cell_count)
    start = next(
        index for index, gate in enumerate(instrumented)
        if gate.kind == "endpoint_pre_left"
    )
    first_seam = next(
        index for index, gate in enumerate(coarse) if gate.kind == "seam_FSWAP"
    )
    prefix = instrumented[:start]
    segment = instrumented[start:]
    kinds = tuple(gate.kind for gate in segment)
    expected_counts = {
        "endpoint_pre_left": cell_count - 1,
        "endpoint_pre_right": cell_count - 1,
        "endpoint_post_left": cell_count - 1,
        "endpoint_post_right": cell_count - 1,
        "endpoint_OR_CNOT": 2 * (cell_count - 1),
        "endpoint_OR_Toffoli_H": 2 * (cell_count - 1),
        "endpoint_OR_Toffoli_CNOT": 6 * (cell_count - 1),
        "endpoint_OR_Toffoli_T": 4 * (cell_count - 1),
        "endpoint_OR_Toffoli_Tdg": 3 * (cell_count - 1),
        "endpoint_clean_left_from_left": cell_count - 1,
        "endpoint_clean_left_from_right": cell_count - 1,
        "endpoint_clean_right_from_left": cell_count - 1,
        "endpoint_clean_right_from_right": cell_count - 1,
        "seam_FSWAP": 9 * (cell_count - 1),
        "onsite_contact": 15 * cell_count,
    }
    observed_counts = Counter(kinds)
    count_failures = sum(
        observed_counts[kind] != count for kind, count in expected_counts.items()
    )
    count_failures += sum(
        kind not in expected_counts for kind in observed_counts
    )
    aux_base = C712.C709.G.build_equivalence(
        tuple((index, 0, 0) for index in range(cell_count))
    ).equivalence.qubits
    auxiliary_wires = set(range(aux_base, aux_base + 3 * (cell_count - 1)))
    inherited_auxiliary_touches = sum(
        any(
            6 * cell_count <= wire < aux_base
            for wire in gate.wires
        )
        for gate in instrumented
    )
    unexpected_new_auxiliary_touches = sum(
        any(wire >= aux_base and wire not in auxiliary_wires for wire in gate.wires)
        for gate in segment
    )
    def signature(gate):
        return (
            gate.kind,
            gate.wires,
            C712.c707.c655.matrix_digest(gate.matrix),
        )
    ordering_failures = tuple(map(signature, prefix)) != tuple(
        map(signature, coarse[:first_seam])
    )
    cursor = 0
    for seam_index in range(cell_count - 1):
        block = segment[cursor:]
        ordering_failures += tuple(gate.kind for gate in block[:2]) != (
            "endpoint_pre_left", "endpoint_pre_right"
        )
        cursor += 2
        ordering_failures += any(
            gate.kind != "seam_FSWAP" for gate in segment[cursor:cursor + 9]
        )
        cursor += 9
        post_kinds = tuple(gate.kind for gate in segment[cursor:cursor + 19])
        ordering_failures += post_kinds[:4] != (
            "endpoint_post_left", "endpoint_post_right",
            "endpoint_OR_CNOT", "endpoint_OR_CNOT",
        )
        ordering_failures += sum(
            kind.startswith("endpoint_OR_Toffoli") for kind in post_kinds[4:]
        ) != 15
        cursor += 19
        ordering_failures += tuple(
            gate.kind for gate in segment[cursor:cursor + 4]
        ) != (
            "endpoint_clean_left_from_left",
            "endpoint_clean_left_from_right",
            "endpoint_clean_right_from_left",
            "endpoint_clean_right_from_right",
        )
        cursor += 4
    ordering_failures += any(
        gate.kind != "onsite_contact" for gate in segment[cursor:]
    )
    ordering_failures += len(segment[cursor:]) != 15 * cell_count
    return {
        "instrumented": instrumented,
        "segment": segment,
        "aux_base": aux_base,
        "new_auxiliary_wires": tuple(sorted(auxiliary_wires)),
        "gate_census": dict(observed_counts),
        "gate_census_failures": count_failures,
        "gate_order_failures": int(ordering_failures),
        "inherited_stabilizer_auxiliary_touches": inherited_auxiliary_touches,
        "unexpected_new_auxiliary_touches": unexpected_new_auxiliary_touches,
    }


def literal_segment_maps(cell_count=2, deletion=None, bases=None):
    structure = decoded_instrument_structure(cell_count)
    segment = structure["segment"]
    if deletion == "left_prewrite":
        skipped = False
        damaged = []
        for gate in segment:
            if not skipped and gate.kind == "endpoint_pre_left":
                skipped = True
                continue
            damaged.append(gate)
        segment = tuple(damaged)
    elif deletion == "OR_Toffoli":
        segment = tuple(
            gate for gate in segment
            if not gate.kind.startswith("endpoint_OR_Toffoli")
        )
    elif deletion is not None:
        raise ValueError(deletion)
    outputs = []
    matter_modes = 6 * cell_count
    domain = tuple(range(1 << matter_modes)) if bases is None else tuple(bases)
    for basis in domain:
        outputs.append(apply_sparse_word({basis: 1.0 + 0.0j}, segment))
    return tuple(outputs), structure


def held_two_seam_literal_truth():
    """Held three-cell truth over all N<=2 rows plus hostile backgrounds."""
    matter_modes = 18
    endpoint_modes = (1, 6, 7, 12)
    other_modes = tuple(mode for mode in range(matter_modes) if mode not in endpoint_modes)
    domain = {
        basis for basis in range(1 << matter_modes) if basis.bit_count() <= 2
    }
    background_patterns = (
        0,
        sum(1 << mode for mode in other_modes),
        sum(1 << mode for index, mode in enumerate(other_modes) if index & 1),
        sum(1 << mode for index, mode in enumerate(other_modes) if not index & 1),
        sum(1 << mode for index, mode in enumerate(other_modes) if index % 3 == 0),
        sum(1 << mode for index, mode in enumerate(other_modes) if index % 3 != 0),
        sum(1 << mode for mode in other_modes[: len(other_modes) // 2]),
        sum(1 << mode for mode in other_modes[len(other_modes) // 2:]),
    )
    for endpoint_pattern in range(1 << len(endpoint_modes)):
        endpoint_basis = sum(
            ((endpoint_pattern >> index) & 1) << mode
            for index, mode in enumerate(endpoint_modes)
        )
        domain.update(endpoint_basis | background for background in background_patterns)
    domain = tuple(sorted(domain))
    outputs, structure = literal_segment_maps(3, bases=domain)
    support_failures = pointer_failures = scratch_failures = 0
    matter_failures = number_failures = norm_failures = 0
    aux_base = structure["aux_base"]
    for basis, row in zip(domain, outputs):
        support_failures += len(row) != 1
        if len(row) != 1:
            continue
        target_state, amplitude = next(iter(row.items()))
        target = target_state & ((1 << matter_modes) - 1)
        expected_target = basis
        for left, right in ((1, 6), (7, 12)):
            if ((expected_target >> left) ^ (expected_target >> right)) & 1:
                expected_target ^= (1 << left) | (1 << right)
        matter_failures += target != expected_target
        number_failures += target.bit_count() != basis.bit_count()
        norm_failures += abs(abs(amplitude) - 1.0) >= TOL
        for seam, (left, right) in enumerate(((1, 6), (7, 12))):
            du, dv, pointer = (
                aux_base + 3 * seam,
                aux_base + 3 * seam + 1,
                aux_base + 3 * seam + 2,
            )
            pointer_failures += (
                ((target_state >> pointer) & 1)
                != (((basis >> left) ^ (basis >> right)) & 1)
            )
            scratch_failures += ((target_state >> du) & 1) != 0
            scratch_failures += ((target_state >> dv) & 1) != 0
    return {
        "rows": len(domain),
        "complete_N_le_2_rows": sum(basis.bit_count() <= 2 for basis in domain),
        "hostile_background_rows": len(domain) - sum(
            basis.bit_count() <= 2 for basis in domain
        ),
        "support_failures": support_failures,
        "matter_failures": matter_failures,
        "number_failures": number_failures,
        "pointer_failures": pointer_failures,
        "scratch_cleanup_failures": scratch_failures,
        "norm_failures": int(norm_failures),
        "literal_gate_census_failures": structure["gate_census_failures"],
        "literal_gate_order_failures": structure["gate_order_failures"],
        "inherited_stabilizer_auxiliary_touches": structure[
            "inherited_stabilizer_auxiliary_touches"
        ],
        "unexpected_new_auxiliary_touches": structure[
            "unexpected_new_auxiliary_touches"
        ],
    }


def dirty_ancilla_domain_control():
    structure = decoded_instrument_structure(2)
    segment = structure["segment"]
    auxiliary = structure["new_auxiliary_wires"]
    matter = 1 << 1
    clean = apply_sparse_word({matter: 1.0 + 0.0j}, segment)
    rejected = differences = 0
    rows = []
    for wire in auxiliary:
        source = matter | (1 << wire)
        lawful = all(((source >> candidate) & 1) == 0 for candidate in auxiliary)
        observed = apply_sparse_word({source: 1.0 + 0.0j}, segment)
        difference = float(np.sqrt(sum(
            abs(observed.get(key, 0.0j) - clean.get(key, 0.0j)) ** 2
            for key in set(observed) | set(clean)
        )))
        rejected += not lawful
        differences += difference > 1e-3
        rows.append({
            "dirty_wire": wire,
            "lawful_clean_ancilla_domain": lawful,
            "output_difference_from_clean": difference,
        })
    return {
        "dirty_rows": len(rows),
        "rejected_by_declared_domain": rejected,
        "output_differences_detected": differences,
        "rows": rows,
    }


def exhaustive_two_cell_instrument():
    coin = I712.c219.common_species(I712.BETA).coin
    local_coin = I712.c229.fock_lift(coin)
    one_particle, _permutation = I712.one_particle_schedule(coin)
    literal_maps, structure = literal_segment_maps(2)
    deleted_pre_maps, _ = literal_segment_maps(2, "left_prewrite")
    deleted_or_maps, _ = literal_segment_maps(2, "OR_Toffoli")
    pointer_wire = structure["aux_base"] + 2
    du_wire, dv_wire = structure["new_auxiliary_wires"][:2]
    maximum = maximum_norm = maximum_number = 0.0
    pointer_true_weight_min = 1.0
    pointer_true_weight_max = 0.0
    endpoint_failures = delta_failures = scratch_failures = 0
    deletion_pre_max = deletion_or_max = 0.0
    literal_support_failures = 0
    literal_phase_failures = 0
    for source in range(1 << 12):
        left, right = source & 63, source >> 6
        pre = np.outer(local_coin[:, right], local_coin[:, left]).reshape(-1)
        pre = I712.apply_fswap_schedule(pre, I712.REVERSE_PAIRS)
        observed = {}
        deleted_pre = {}
        deleted_or = {}
        for basis, amplitude in enumerate(pre):
            for target, coefficient in literal_maps[basis].items():
                observed[target] = observed.get(target, 0.0j) + coefficient * amplitude
            for target, coefficient in deleted_pre_maps[basis].items():
                deleted_pre[target] = deleted_pre.get(target, 0.0j) + coefficient * amplitude
            for target, coefficient in deleted_or_maps[basis].items():
                deleted_or[target] = deleted_or.get(target, 0.0j) + coefficient * amplitude
        coarse = I712.exterior_column(one_particle, source)
        expected = {}
        for target, amplitude in enumerate(coarse):
            p = ((target >> 1) & 1) ^ ((target >> 6) & 1)
            if abs(amplitude) > 1e-15:
                expected[target | (p << pointer_wire)] = amplitude
        keys = set(observed) | set(expected)
        delta = np.asarray([
            observed.get(key, 0.0j) - expected.get(key, 0.0j)
            for key in keys
        ])
        maximum = max(maximum, float(np.max(np.abs(delta), initial=0.0)))
        maximum_norm = max(
            maximum_norm,
            abs(sum(abs(value) ** 2 for value in observed.values()) - 1),
        )
        number = source.bit_count()
        maximum_number = max(maximum_number, max([
            abs(amplitude) for state, amplitude in observed.items()
            if (state & 4095).bit_count() != number
        ], default=0.0))
        pointer_weight = float(sum(
            abs(amplitude) ** 2 for state, amplitude in observed.items()
            if (state >> pointer_wire) & 1
        ))
        pointer_true_weight_min = min(pointer_true_weight_min, pointer_weight)
        pointer_true_weight_max = max(pointer_true_weight_max, pointer_weight)
        deletion_pre_max = max(deletion_pre_max, float(np.sqrt(sum(
            abs(deleted_pre.get(key, 0.0j) - expected.get(key, 0.0j)) ** 2
            for key in set(deleted_pre) | set(expected)
        ))))
        deletion_or_max = max(deletion_or_max, float(np.sqrt(sum(
            abs(deleted_or.get(key, 0.0j) - expected.get(key, 0.0j)) ** 2
            for key in set(deleted_or) | set(expected)
        ))))
    seam_targets, seam_signs = I712.schedule_arrays(I712.SEAM_ADJACENT)
    contact = I712.contact_diagonal()
    for basis, row in enumerate(literal_maps):
        literal_support_failures += len(row) != 1
        if len(row) != 1:
            continue
        state, amplitude = next(iter(row.items()))
        target = state & 4095
        pointer = (state >> pointer_wire) & 1
        du = (state >> du_wire) & 1
        dv = (state >> dv_wire) & 1
        expected_target = int(seam_targets[basis])
        expected_pointer = ((basis >> 1) & 1) ^ ((basis >> 6) & 1)
        before = tuple((basis >> mode) & 1 for mode in range(12))
        after = tuple((target >> mode) & 1 for mode in range(12))
        endpoint = C704.endpoint_from_b_change(before, after)
        endpoint_failures += target != expected_target or endpoint != pointer
        endpoint_failures += pointer != expected_pointer
        delta_failures += (
            C704.matter_delta_mask(before, after).bit_count()
            != 2 * expected_pointer
        )
        scratch_failures += du != 0 or dv != 0
        literal_phase_failures += abs(
            amplitude - seam_signs[basis] * contact[target]
        ) >= TOL
    return {
        "columns": 4096,
        "maximum_EG_instrument_residual": maximum,
        "maximum_norm_residual": maximum_norm,
        "maximum_number_leakage": maximum_number,
        "endpoint_predicate_failures": endpoint_failures,
        "matter_delta_failures": delta_failures,
        "scratch_cleanup_failures": scratch_failures,
        "pointer_true_weight_range": (pointer_true_weight_min, pointer_true_weight_max),
        "delete_left_prewrite_maximum_residual": deletion_pre_max,
        "delete_OR_Toffoli_maximum_residual": deletion_or_max,
        "literal_segment_basis_rows": len(literal_maps),
        "literal_segment_support_failures": literal_support_failures,
        "literal_segment_phase_failures": int(literal_phase_failures),
        "literal_gate_census_failures": structure["gate_census_failures"],
        "literal_gate_order_failures": structure["gate_order_failures"],
        "inherited_stabilizer_auxiliary_touches": structure[
            "inherited_stabilizer_auxiliary_touches"
        ],
        "unexpected_new_auxiliary_touches": structure[
            "unexpected_new_auxiliary_touches"
        ],
    }


def physical_word_certificate(cell_count=2):
    cells = tuple((index, 0, 0) for index in range(cell_count))
    eq = C712.C709.G.build_equivalence(cells).equivalence
    _eq2, graph, site_map, gauges, occupied, collisions = C712.P709.placement_bundle(cells)
    carriers = C712.carriers_for(eq, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(i for i, carrier in enumerate(carriers) if len(carrier) == 2)
    pointer_sites = []
    occupied_set = set(occupied)
    for seam in range(cell_count - 1):
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
    extended_sites = wire_sites + tuple(pointer_sites)
    target_decode = C712.synthesize_decode(eq.target_w, eq.target_v)
    target_encode = C712.inverse_word(target_decode)
    decoded, qr_residual = instrumented_decoded_word(cell_count)
    repetition_decode = tuple(
        C712.c707.Instruction("endpoint_repetition_decode_CNOT", carriers[i], CNOT)
        for i in repeated
    )
    repetition_encode = tuple(
        C712.c707.Instruction("endpoint_repetition_encode_CNOT", carriers[i], CNOT)
        for i in reversed(repeated)
    )
    word = (
        repetition_decode
        + C712.abstract_to_physical(target_decode, extended_sites, "endpoint_target_decode_")
        + C712.abstract_to_physical(decoded, extended_sites, "endpoint_decoded_")
        + C712.abstract_to_physical(target_encode, extended_sites, "endpoint_target_encode_")
        + repetition_encode
    )
    routed, route = C712.c707.route_word(word)
    return {
        "cells": cells,
        "matter_modes": 6 * cell_count,
        "abstract_code_qubits": eq.qubits,
        "code_stabilizer_rank": C712.rank(eq.target_w[6 * cell_count:], eq.qubits),
        "code_dimension": 1 << (eq.qubits - C712.rank(eq.target_w[6 * cell_count:], eq.qubits)),
        "literal_code_M2": len(occupied),
        "endpoint_register_M2": len(pointer_sites),
        "total_assigned_M2": len(occupied) + len(pointer_sites),
        "pointer_sites": pointer_sites,
        "placement_collisions": collisions + len(pointer_sites) - len(set(pointer_sites)),
        "decoded_gate_census": dict(Counter(gate.kind for gate in decoded)),
        "coin_QR_residual": qr_residual,
        "primitive_gates": len(word),
        "routed_gates": len(routed),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "routed_word_sha256": route["word_sha256"],
        "touched_M2": len(route["touched_coordinates"]),
        "blank_route_work_M2": len(set(route["touched_coordinates"]) - set(occupied) - set(pointer_sites)),
        "decoded_stabilizer_failures": C712.tableau_failures(
            C712.apply_word_rows(eq.target_w[6 * cell_count:], target_decode),
            [C712.c707.Pauli(z=1 << i) for i in range(6 * cell_count, eq.qubits)],
        ),
    }


def frame_pointer_certificate():
    frames = C712.C709.F.base.proper_cubic_frames()
    permutations = []
    truth_failures = 0
    for frame in frames:
        matrix = C712.C709.F.base.c210.direction_permutation(frame)
        permutation = tuple(
            next(target for target in range(6) if abs(matrix[target, source]) > 0.5)
            for source in range(6)
        )
        permutations.append(permutation)
        for state in range(1 << 12):
            transported_state = 0
            for cell in range(2):
                for source in range(6):
                    bit = (state >> (6 * cell + source)) & 1
                    transported_state |= bit << (6 * cell + permutation[source])
            base = ((state >> 1) & 1) ^ ((state >> 6) & 1)
            transported = (
                ((transported_state >> permutation[1]) & 1)
                ^ ((transported_state >> (6 + permutation[0])) & 1)
            )
            truth_failures += base != transported
    composition_failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product = left @ right
            product_index = next(
                index for index, frame in enumerate(frames)
                if np.array_equal(frame, product)
            )
            composed = tuple(
                permutations[left_index][permutations[right_index][source]]
                for source in range(6)
            )
            composition_failures += composed != permutations[product_index]
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "endpoint_XOR_truth_failures": truth_failures,
        "direction_composition_failures": composition_failures,
        "scope": (
            "abstract decoded endpoint naturality; literal routed physical words "
            "for each transported chart are not constructed here"
        ),
    }


def main():
    toffoli = word_matrix(toffoli_word(0, 1, 2), 3)
    toffoli_residual = float(np.linalg.norm(toffoli - exact_toffoli()))
    deleted_toffoli = word_matrix(toffoli_word(0, 1, 2)[:-1], 3)
    toffoli_deletion = float(np.linalg.norm(deleted_toffoli - exact_toffoli()))
    exhaustive = exhaustive_two_cell_instrument()
    held_literal = held_two_seam_literal_truth()
    dirty_ancilla = dirty_ancilla_domain_control()
    physical2 = physical_word_certificate(2)
    physical3 = physical_word_certificate(3)
    frames = frame_pointer_certificate()
    endpoint704 = C704.endpoint_controls()
    packet704 = C704.packet_interface_controls()
    joint704 = C704.joint_order_controls()
    provenance = provenance_certificate()
    checks = {
        "source_closure": provenance["baseline_is_ancestor"]
        and provenance["declared_path_failures"] == 0
        and provenance["duplicate_declared_paths"] == 0
        and not provenance["missing_transitive_scripts"]
        and not provenance["untracked_declared_paths"],
        "Toffoli": toffoli_residual < TOL and toffoli_deletion > 1e-3,
        "all_4096_instrument": exhaustive["maximum_EG_instrument_residual"] < TOL
        and exhaustive["maximum_norm_residual"] < TOL
        and exhaustive["maximum_number_leakage"] < TOL
        and exhaustive["endpoint_predicate_failures"] == 0
        and exhaustive["matter_delta_failures"] == 0
        and exhaustive["scratch_cleanup_failures"] == 0
        and exhaustive["literal_segment_basis_rows"] == 4096
        and exhaustive["literal_segment_support_failures"] == 0
        and exhaustive["literal_segment_phase_failures"] == 0
        and exhaustive["literal_gate_census_failures"] == 0
        and exhaustive["literal_gate_order_failures"] == 0
        and exhaustive["inherited_stabilizer_auxiliary_touches"] == 0
        and exhaustive["unexpected_new_auxiliary_touches"] == 0,
        "deletions": exhaustive["delete_left_prewrite_maximum_residual"] > 1e-3
        and exhaustive["delete_OR_Toffoli_maximum_residual"] > 1e-3,
        "dirty_ancilla_domain": dirty_ancilla["dirty_rows"] == 3
        and dirty_ancilla["rejected_by_declared_domain"] == 3
        and dirty_ancilla["output_differences_detected"] == 3,
        "physical_two_cell": physical2["code_dimension"] == 4096
        and physical2["endpoint_register_M2"] == 3
        and physical2["primitive_gates"] == 1400
        and physical2["routed_gates"] == 17798
        and physical2["maximum_route_distance"] == 24
        and physical2["touched_M2"] == 503
        and physical2["blank_route_work_M2"] == 461
        and physical2["routed_word_sha256"]
        == "185fdb5270931877474ef720926bde016ff2fece03c1b8b58588e52e517d04f7"
        and not any(physical2[key] for key in (
            "placement_collisions", "non_NN_failures", "operand_order_failures",
            "route_return_failures", "decoded_stabilizer_failures"
        )),
        "held_three_cell": physical3["code_dimension"] == 64 ** 3
        and physical3["endpoint_register_M2"] == 6
        and physical3["primitive_gates"] == 2165
        and physical3["routed_gates"] == 38829
        and physical3["maximum_route_distance"] == 40
        and physical3["touched_M2"] == 790
        and physical3["blank_route_work_M2"] == 724
        and physical3["routed_word_sha256"]
        == "a1040745b93c60bf766b369d1c344f0ee7b5d3cd1e747ba5d561edb1e76de210"
        and not any(physical3[key] for key in (
            "placement_collisions", "non_NN_failures", "operand_order_failures",
            "route_return_failures", "decoded_stabilizer_failures"
        ))
        and held_literal["complete_N_le_2_rows"] == 172
        and not any(held_literal[key] for key in (
            "support_failures", "matter_failures", "number_failures",
            "pointer_failures", "scratch_cleanup_failures", "norm_failures",
            "literal_gate_census_failures", "literal_gate_order_failures",
            "inherited_stabilizer_auxiliary_touches",
            "unexpected_new_auxiliary_touches",
        )),
        "frames_24_576": frames["proper_cubic_frames"] == 24
        and frames["ordered_frame_products"] == 576
        and frames["endpoint_XOR_truth_failures"] == 0
        and frames["direction_composition_failures"] == 0,
        "unchanged_Cycle704_endpoint": endpoint704["pointer_inverse_failures"] == 0
        and endpoint704["seam_predicate_failures"] == 0
        and endpoint704["B_pointer_failures"] == 0
        and endpoint704["frame_port_failures"] == 0
        and endpoint704["matter_delta_count_failures"] == 0
        and endpoint704["local_D_or_reference_failures"] == 0
        and endpoint704["contact_false_positives"] == 0
        and endpoint704["maximum_B_support_owner_cells"] <= 2
        and endpoint704["maximum_single_B_edge_qubit_weight"] <= 6
        and endpoint704["maximum_two_endpoint_B_edge_qubit_union"] <= 11,
        "unchanged_Cycle610_packet": packet704["projection_failures"] == 0
        and packet704["interval_failures"] == 0
        and packet704["carry_truth_failures"] == 0
        and packet704["additivity_closed"] and packet704["reversal_closed"]
        and packet704["register_inverse_failures"] == 0
        and packet704["d_ab"] == 9
        and packet704["d_bc"] == 12
        and packet704["d_ac"] == 21,
        "unchanged_Cycle612_order": joint704["consistent_acyclic"]
        and joint704["inverted_refusal"] == "refused_inverted"
        and joint704["forced_cycle_detected"],
    }
    report = {
        "baseline_commit": BASELINE,
        "provenance": provenance,
        "checks": checks,
        "pass": all(checks.values()),
        "Toffoli_residual": toffoli_residual,
        "Toffoli_deletion_residual": toffoli_deletion,
        "exhaustive_two_cell": exhaustive,
        "held_literal_two_seam_truth": held_literal,
        "dirty_ancilla_domain": dirty_ancilla,
        "physical_two_cell": physical2,
        "held_three_cell": physical3,
        "proper_cubic_pointer_naturality": frames,
        "Cycle704_endpoint": endpoint704,
        "Cycle704_Cycle610_packet": packet704,
        "Cycle704_Cycle612_joint_order": joint704,
        "supplied": (
            "Cycle712 target code state and fixed decoded coin/reverse/seam/contact order",
            "three clean endpoint-register M2 per internal seam and blank route work",
            "Cycle704 binder plus Cycle610 actuality/admissibility/law-domain/bank inputs",
            "offline serial gate word and Manhattan route",
        ),
        "derived": (
            "coherent seam matter-change opportunity pointer on the same joint E",
            "clean du/dv scratch with one retained pointer per internal seam",
            "literal one/two-M2 gate decomposition and routed two/three-cell words",
            "exact projection of the pointer truth semantics into unchanged Cycle704/610/612 harnesses",
        ),
        "open": (
            "objective occurrence, autonomous admission, bank selector, packet circuit, and Record permanence",
            "clean-register/code/work genesis and autonomous recurrent scheduling",
            "exterior streams, independently active coframes, empirical unit, and physical time",
            "source/gravity, Born/probability, and realized-history meaning",
        ),
        "boundary": (
            "The retained pointer is a coherent candidate opportunity. The unchanged packet and order "
            "harnesses remain host software with supplied admission tokens; no pointer branch is selected."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, default=str, separators=(",", ":")
    ).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE713_PHYSICAL_M2_ENDPOINT_INSTRUMENT_BRIDGE_PASS" if report["pass"]
          else "CYCLE713_PHYSICAL_M2_ENDPOINT_INSTRUMENT_BRIDGE_INCOMPLETE")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
