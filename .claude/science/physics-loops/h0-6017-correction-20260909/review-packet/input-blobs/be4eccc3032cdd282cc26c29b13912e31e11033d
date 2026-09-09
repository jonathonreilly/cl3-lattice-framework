#!/usr/bin/env python3
"""Independent coherent Cycle713-to-Cycle714 fixed-packet composition check.

The routed packet circuit is executed as a sparse complex circuit, including
every H/T/T-dagger phase and route SWAP, then composed with all 4096 Cycle713
decoded matter/pointer columns.  Circuit order is not interpreted as time.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 300
NOTE_PATH = (
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_"
    "CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_"
    "CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_"
    "CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/"
    "CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_independent_route_replay_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
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
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as F
import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as E

TOL = 3.0e-10
PRUNE = 3.0e-14
COIN = E.I712.c219.common_species(E.I712.BETA).coin
LOCAL_COIN = E.I712.c229.fock_lift(COIN)
ONE_PARTICLE, _ONE_PARTICLE_PERMUTATION = E.I712.one_particle_schedule(COIN)
SEAM_TARGETS, SEAM_SIGNS = E.I712.schedule_arrays(E.I712.SEAM_ADJACENT)
CONTACT = E.I712.contact_diagonal()


def apply_sparse(state, matrix, wires):
    """Apply a one/two-bit matrix to a sparse arbitrary-width state."""
    output = {}
    for source, source_amplitude in state.items():
        local_source = sum(((source >> wire) & 1) << i for i, wire in enumerate(wires))
        for local_target in range(1 << len(wires)):
            amplitude = matrix[local_target, local_source]
            if abs(amplitude) <= 1.0e-16:
                continue
            target = source
            for i, wire in enumerate(wires):
                target = (target & ~(1 << wire)) | (((local_target >> i) & 1) << wire)
            output[target] = output.get(target, 0.0j) + amplitude * source_amplitude
    return {basis: amplitude for basis, amplitude in output.items() if abs(amplitude) > PRUNE}


def vector_residual(left, right):
    keys = set(left) | set(right)
    return float(np.sqrt(sum(abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2 for key in keys)))


def packet_layout():
    eq, graph, site_map, gauges, matter_sites, collisions = F.P.placement_bundle(
        ((0, 0, 0), (1, 0, 0))
    )
    endpoint_sites = F.retained_endpoint_sites(eq, graph, site_map, gauges, matter_sites)
    occupied = set(matter_sites) | set(endpoint_sites)
    candidates = []
    for radius in range(1, 12):
        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):
                for z in range(-radius, radius + 1):
                    site = (x, y, z)
                    if max(abs(x), abs(y), abs(z)) != radius:
                        continue
                    if site not in occupied and site not in candidates:
                        candidates.append(site)
                    if len(candidates) >= F.N:
                        break
                if len(candidates) >= F.N:
                    break
            if len(candidates) >= F.N:
                break
        if len(candidates) >= F.N:
            break
    new_sites = iter(candidates)
    sites = tuple(endpoint_sites[2] if wire == F.POINTER else next(new_sites) for wire in range(F.N))
    matrices = {"H": F.H, "T": F.T, "TD": F.TD, "CNOT": F.CNOT}
    instructions = tuple(
        F.P.c707.Instruction("packet_" + kind, tuple(sites[wire] for wire in wires), matrices[kind])
        for kind, wires in F.expanded(F.word())
    )
    routed, route = F.P.c707.route_word(instructions)
    routed_touched = {site for gate in routed for site in gate.sites}
    universe = tuple(sorted(routed_touched | set(sites)))
    index = {site: offset for offset, site in enumerate(universe)}
    return {
        "matter_sites": tuple(matter_sites),
        "endpoint_sites": endpoint_sites,
        "sites": sites,
        "routed": routed,
        "route": route,
        "touched": tuple(sorted(routed_touched)),
        "universe": universe,
        "index": index,
        "collisions": collisions,
    }


def abstract_initial(pointer):
    return F.initial(14, F.SENTINEL_NONE, 1, (pointer, 1, 1, 1, 1, 1))


def manual_expected_packet_bits(pointer):
    """Checker-local field equation; does not execute the candidate semantic word."""
    before = abstract_initial(pointer)
    if not pointer:
        return before
    after = list(before)
    head = F.SENTINEL_NONE
    rotor = 14
    for bit, wire in enumerate(F.PRED):
        after[wire] = (head >> bit) & 1
    for bit, wire in enumerate(F.RB):
        after[wire] = (rotor >> bit) & 1
    for bit, wire in enumerate(F.RA):
        after[wire] = (15 >> bit) & 1
    after[F.CARRY] = 0
    after[F.PDELTA[1]] = after[F.PDELTA[6]] = 1
    for wire in (F.PEND, F.PBIND, F.PVALID, F.PACT, F.PADM, F.PLAW):
        after[wire] = 1
    after[F.PORIENT] = 1
    for bit, wire in enumerate(F.HEAD):
        after[wire] = (F.FIXED_ADDRESS >> bit) & 1
    for bit, wire in enumerate(F.ROT):
        after[wire] = (15 >> bit) & 1
    return tuple(after)


def physical_basis(bits, layout):
    basis = 0
    for wire, value in enumerate(bits):
        if value:
            basis |= 1 << layout["index"][layout["sites"][wire]]
    return basis


def routed_packet_outputs(layout):
    outputs = {}
    diagnostics = {}
    assigned = {layout["index"][site] for site in layout["sites"]}
    external = tuple(bit for bit in range(len(layout["universe"])) if bit not in assigned)
    background_masks = {
        "vacuum": 0,
        "all_external": sum(1 << bit for bit in external),
        "alternating_external": sum(1 << bit for index, bit in enumerate(external) if index & 1),
        "opposite_alternating_external": sum(
            1 << bit for index, bit in enumerate(external) if not (index & 1)
        ),
    }
    for pointer in (0, 1):
        before = abstract_initial(pointer)
        expected_bits = manual_expected_packet_bits(pointer)
        expected_basis = physical_basis(expected_bits, layout)
        rows = {}
        vacuum_state = None
        maximum_support = 1
        for label, background in background_masks.items():
            state = {physical_basis(before, layout) | background: 1.0 + 0.0j}
            local_maximum_support = 1
            for gate in layout["routed"]:
                wires = tuple(layout["index"][site] for site in gate.sites)
                state = apply_sparse(state, gate.matrix, wires)
                local_maximum_support = max(local_maximum_support, len(state))
            expected = {expected_basis | background: 1.0 + 0.0j}
            rows[label] = {
                "sparse_residual": vector_residual(state, expected),
                "maximum_transient_support": local_maximum_support,
                "final_support": len(state),
                "final_amplitude": [float(state.get(expected_basis | background, 0.0j).real),
                                    float(state.get(expected_basis | background, 0.0j).imag)],
            }
            maximum_support = max(maximum_support, local_maximum_support)
            if label == "vacuum":
                vacuum_state = state
        assert vacuum_state is not None
        outputs[pointer] = vacuum_state
        diagnostics[pointer] = {
            "maximum_background_residual": max(row["sparse_residual"] for row in rows.values()),
            "maximum_transient_support": maximum_support,
            "semantic_output_basis": expected_basis,
            "arbitrary_external_basis_patterns": rows,
        }
    return outputs, diagnostics


def decoded_cycle713_column(source):
    left, right = source & 63, source >> 6
    pre = np.outer(LOCAL_COIN[:, right], LOCAL_COIN[:, left]).reshape(-1)
    pre = E.I712.apply_fswap_schedule(pre, E.I712.REVERSE_PAIRS)
    output = {}
    for basis, amplitude in enumerate(pre):
        if abs(amplitude) <= 1.0e-15:
            continue
        target = int(SEAM_TARGETS[basis])
        pointer = ((basis >> 1) & 1) ^ ((basis >> 6) & 1)
        value = SEAM_SIGNS[basis] * CONTACT[target] * amplitude
        output[(target, pointer)] = output.get((target, pointer), 0.0j) + value
    return output


def expected_cycle713_column(source):
    coarse = E.I712.exterior_column(ONE_PARTICLE, source)
    return {
        (target, ((target >> 1) & 1) ^ ((target >> 6) & 1)): amplitude
        for target, amplitude in enumerate(coarse) if abs(amplitude) > 1.0e-15
    }


def compose_packet(column, packet_outputs):
    output = {}
    for (matter, pointer), matter_amplitude in column.items():
        for packet_basis, packet_amplitude in packet_outputs[pointer].items():
            key = (matter, packet_basis)
            output[key] = output.get(key, 0.0j) + matter_amplitude * packet_amplitude
    return output


def expected_packet(column, layout):
    output = {}
    for (matter, pointer), amplitude in column.items():
        bits = manual_expected_packet_bits(pointer)
        output[(matter, physical_basis(bits, layout))] = amplitude
    return output


def all_columns_certificate(layout, packet_outputs):
    sources = tuple(range(1 << 12))
    maximum_endpoint = maximum_composed = maximum_norm = 0.0
    maxima_by_number = {number: 0.0 for number in range(13)}
    for source in sources:
        observed_endpoint = decoded_cycle713_column(source)
        expected_endpoint = expected_cycle713_column(source)
        endpoint_residual = vector_residual(observed_endpoint, expected_endpoint)
        observed = compose_packet(observed_endpoint, packet_outputs)
        expected = expected_packet(expected_endpoint, layout)
        composed_residual = vector_residual(observed, expected)
        norm = abs(sum(abs(value) ** 2 for value in observed.values()) - 1.0)
        maximum_endpoint = max(maximum_endpoint, endpoint_residual)
        maximum_composed = max(maximum_composed, composed_residual)
        maximum_norm = max(maximum_norm, norm)
        maxima_by_number[source.bit_count()] = max(
            maxima_by_number[source.bit_count()], composed_residual
        )
    sign_control_sources = tuple(source for source in sources if source.bit_count() <= 2)
    negative_phase_rows = 0
    # Bounded active control: delete all seam CAR signs but retain the same
    # occupation permutation on the complete N<=2 subspace.
    sign_deletion_maximum = 0.0
    for source in sign_control_sources:
        left, right = source & 63, source >> 6
        pre = np.outer(LOCAL_COIN[:, right], LOCAL_COIN[:, left]).reshape(-1)
        pre = E.I712.apply_fswap_schedule(pre, E.I712.REVERSE_PAIRS)
        negative_phase_rows += int(sum(
            abs(amplitude) > 1.0e-15 and SEAM_SIGNS[basis] < 0
            for basis, amplitude in enumerate(pre)
        ))
        deleted = {}
        for basis, amplitude in enumerate(pre):
            if abs(amplitude) <= 1.0e-15:
                continue
            target = int(SEAM_TARGETS[basis])
            pointer = ((basis >> 1) & 1) ^ ((basis >> 6) & 1)
            deleted[(target, pointer)] = deleted.get((target, pointer), 0.0j) + CONTACT[target] * amplitude
        sign_deletion_maximum = max(
            sign_deletion_maximum,
            vector_residual(deleted, expected_cycle713_column(source)),
        )
    return {
        "source_columns": len(sources),
        "source_columns_by_number": {
            str(number): sum(source.bit_count() == number for source in sources)
            for number in range(13)
        },
        "maximum_Cycle713_decoded_instrument_residual": float(maximum_endpoint),
        "maximum_composed_packet_EG_residual": float(maximum_composed),
        "maximum_composed_norm_residual": float(maximum_norm),
        "maximum_composed_residual_by_number": {
            number: float(value) for number, value in maxima_by_number.items()
        },
        "negative_CAR_phase_contributing_rows_in_N_le_2_control": negative_phase_rows,
        "delete_all_seam_CAR_signs_N_le_2_maximum_residual": float(sign_deletion_maximum),
    }


def main():
    provenance = F.provenance_certificate(AUDIT_INPUT_PATHS, __file__)
    source_closure = (
        provenance["baseline_is_ancestor"]
        and provenance["declared_path_failures"] == 0
        and provenance["duplicate_declared_paths"] == 0
        and not provenance["missing_transitive_scripts"]
        and not provenance["missing_dynamic_scripts"]
        and not provenance["untracked_inputs"]
    )
    cycle713_literal = E.exhaustive_two_cell_instrument()
    layout = packet_layout()
    packet_outputs, route_diagnostics = routed_packet_outputs(layout)
    certificate = all_columns_certificate(layout, packet_outputs)
    cycle713_sites = tuple(E.physical_word_certificate(2)["pointer_sites"])
    pointer_match = layout["endpoint_sites"] == cycle713_sites
    checks = {label: bool(value) for label, value in {
        "source_closure": source_closure,
        "exact_pointer_coordinate": pointer_match,
        "packet_route_returns": layout["route"]["route_return_failures"] == 0,
        "packet_route_is_phase_coherent": all(
            row["maximum_background_residual"] < TOL
            for row in route_diagnostics.values()
        ),
        "all_4096_inherited_same_E_composition": certificate["source_columns"] == 4096
        and certificate["maximum_composed_packet_EG_residual"] < TOL
        and certificate["maximum_composed_norm_residual"] < TOL
        and cycle713_literal["literal_segment_basis_rows"] == 4096
        and cycle713_literal["maximum_EG_instrument_residual"] < TOL
        and cycle713_literal["maximum_norm_residual"] < TOL
        and not any(cycle713_literal[key] for key in (
            "literal_segment_support_failures", "literal_segment_phase_failures",
            "literal_gate_census_failures", "literal_gate_order_failures",
            "scratch_cleanup_failures", "inherited_stabilizer_auxiliary_touches",
            "unexpected_new_auxiliary_touches",
        )),
        "CAR_phase_control_active": certificate["negative_CAR_phase_contributing_rows_in_N_le_2_control"] > 0
        and certificate["delete_all_seam_CAR_signs_N_le_2_maximum_residual"] > 1.0e-3,
        "full_width_address": len(F.PRED) == len(F.HEAD) == 6,
    }.items()}
    report = {
        "baseline": F.BASELINE,
        "provenance": provenance,
        "checks": checks,
        "pass": all(checks.values()),
        "pointer_sites_cycle713": cycle713_sites,
        "pointer_sites_rederived": layout["endpoint_sites"],
        "retained_pointer_site": layout["sites"][F.POINTER],
        "routed_packet": {
            "touched_M2": len(layout["touched"]),
            "routed_gates": len(layout["routed"]),
            "maximum_route_distance": layout["route"]["maximum_route_distance"],
            "route_return_failures": layout["route"]["route_return_failures"],
            "routed_word_sha256": layout["route"]["word_sha256"],
            "pointer_conditioned_sparse_execution": route_diagnostics,
        },
        "all_4096_composition": certificate,
        "Cycle713_literal_instrument_acceptance": cycle713_literal,
        "address_width": {
            "packet_predecessor_bits": len(F.PRED),
            "head_bits": len(F.HEAD),
            "fixed_address": F.FIXED_ADDRESS,
            "None_sentinel": F.SENTINEL_NONE,
        },
        "interpretation": (
            "Cycle713's repaired literal matter/pointer word may be followed by the exact routed "
            "fixed-address Cycle714 packet word on the identical retained pointer coordinate. "
            "The concatenation is phase coherent on every one of the 4096 source columns; its routing SWAPs "
            "return every intermediate register, and deleting the CAR seam signs is detected."
        ),
        "same_E_argument": (
            "Extend Cycle713 E by the supplied blank packet/head/rotor/control registers. "
            "Its retained pointer coordinate is exactly the packet control coordinate. The "
            "Cycle713 routed word returns its routing permutation, and the independently executed "
            "packet routed word returns its routing permutation, so their literal concatenation "
            "implements the checked decoded composition on the extended Cycle713 code space."
        ),
        "execution_scope": (
            "All 4096 decoded matter/pointer source columns and both pointer-conditioned 2598-gate "
            "routed packet actions were executed. A dense monolithic state vector over the full "
            "100-M2 assigned space was not formed; the target-code decode/encode intertwiner is the "
            "locally imported Cycle713 theorem supply."
        ),
        "boundary": (
            "This closes only a supplied fixed-address, blank-register, admitted packet append. "
            "The all-column splice re-executes the repaired Cycle713 literal-instrument acceptance. It does not "
            "derive occurrence, admission, allocation, genesis, permanence, time, or a recurrent law."
        ),
        "declared_inputs": AUDIT_INPUT_PATHS,
        "input_sha256": {
            path: sha256((ROOT / path).read_bytes()).hexdigest()
            for path in AUDIT_INPUT_PATHS if (ROOT / path).is_file()
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, default=str, separators=(",", ":")
    ).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE714_FIXED_PACKET_COHERENT_COMPOSITION_PASS" if report["pass"]
          else "CYCLE714_FIXED_PACKET_COHERENT_COMPOSITION_INCOMPLETE")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
