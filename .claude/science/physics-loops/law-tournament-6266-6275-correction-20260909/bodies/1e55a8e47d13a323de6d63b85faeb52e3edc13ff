#!/usr/bin/env python3
"""Primary fail-closed runner for the bounded Cycle709 seam compiler."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle709_local_seam_clifford_core_2026_07_26 as C
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

import numpy as np


PASS = 0
FAIL = 0
NOTE_PATH = (
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_"
    "CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
ACTIVE_SOURCE_PATHS = (
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
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
)
AUDIT_INPUT_PATHS = (
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_"
    "CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_"
    "EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_"
    "CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_"
    "CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
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
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
EXPECTED_DEPENDENCIES = {
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py":
        "71d073a95d089c13baf6fbaff4c3e3ebbd63650a3c152bba49f8de78ee377c69",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py":
        "f5b604b714e8fbb33e2b6284cb38199e900859d710cd9e1411ee941a021235f3",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py":
        "3aa964a6eaca559048a53de580f39d9295a3e4b41ef9d4ff9dcdd4d3ff7444a7",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py":
        "b418c74e82405a0511de81be0eef7080f98d5fe760ccac5d47783a6a751c2480",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py":
        "e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
}


def check(label: str, condition: bool, detail: object) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def json_ready(value):
    if isinstance(value, dict):
        return {
            key if isinstance(key, (str, int, float, bool)) else repr(key): json_ready(item)
            for key, item in value.items()
        }
    if isinstance(value, (tuple, list)):
        return [json_ready(item) for item in value]
    return value


def dependency_controls() -> dict[str, object]:
    actual = {
        name: sha256((ROOT / name).read_bytes()).hexdigest()
        for name in EXPECTED_DEPENDENCIES
    }
    return {
        "expected": EXPECTED_DEPENDENCIES,
        "actual": actual,
        "mismatches": {
            name: digest for name, digest in actual.items()
            if digest != EXPECTED_DEPENDENCIES[name]
        },
        "baseline_commit": "57d6361fa50c82b6a468b7687a1b9f599e567c1f",
    }


def mass_contact_regression_certificate() -> dict[str, object]:
    """Re-execute the inherited Cycle219/230 fixtures used by this compiler."""
    species = c219.common_species(-0.3)
    uniform = np.ones(6, dtype=complex) / np.sqrt(6.0)
    eigenvalue = np.vdot(uniform, species.coin @ uniform)
    measured_mass = float(np.angle(eigenvalue)) / c219.C_SQUARED
    fixture_mass = c219.rest_mass(species)
    contact = np.diag(
        (1.0, 1.0, 1.0, np.exp(1j * c230.COUPLING))
    ).astype(complex)
    return {
        "one_particle_coin_eigen_residual": float(
            np.linalg.norm(species.coin @ uniform - eigenvalue * uniform)
        ),
        "one_particle_mass": measured_mass,
        "Cycle219_mass_fixture": fixture_mass,
        "one_particle_mass_residual": abs(measured_mass - fixture_mass),
        "contact_vacuum_and_one_particle_residual": float(
            np.linalg.norm(np.diag(contact)[:3] - 1.0)
        ),
        "contact_double_occupation_phase_residual": abs(
            contact[3, 3] - np.exp(1j * c230.COUPLING)
        ),
        "contact_coupling": c230.COUPLING,
        "Cycle219_runner_sha256": EXPECTED_DEPENDENCIES[
            "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"
        ],
        "Cycle230_runner_sha256": EXPECTED_DEPENDENCIES[
            "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"
        ],
        "packaged": True,
    }
def main() -> int:
    dependencies = dependency_controls()
    check(
        "Cycle219/230/706/708 algebra sources are pinned to main@57d6361fa5",
        not dependencies["mismatches"],
        dependencies,
    )

    mass_contact = mass_contact_regression_certificate()
    check(
        "the primary runner re-executes the Cycle219 one-particle mass fixture and Cycle230 local contact controls",
        mass_contact["one_particle_coin_eigen_residual"] < 3e-12
        and mass_contact["one_particle_mass_residual"] < 3e-12
        and mass_contact["contact_vacuum_and_one_particle_residual"] < 3e-12
        and mass_contact["contact_double_occupation_phase_residual"] < 3e-12
        and mass_contact["packaged"],
        mass_contact,
    )

    reference = C.reference_certificate()
    check(
        "the +x reference seam is exactly four signed transvections and no depth-one-through-three word with axes in im(S-I) reaches its symplectic map",
        reference["qubits"] == 38
        and reference["rank_S_minus_I"] == 3
        and reference["depth_le_three_hits"] == {1: False, 2: False, 3: False}
        and reference["constructed_transvection_depth"] == 4
        and reference["depth_search_axis_class"] == "all nonzero axes in im(S-I)"
        and reference["factor_weights"] == (13, 12, 1, 1)
        and reference["factor_phases"] == (0, 0, 0, 1)
        and reference["rotation_signs"] == (1, -1, -1, 1)
        and reference["hermitian_failures"] == 0
        and not any(reference["signed_mismatches"].values()),
        reference,
    )
    check(
        "every one-seam factor deletion is active",
        all(value > 0 for value in reference["delete_factor_failures"]),
        reference["delete_factor_failures"],
    )

    frames = C.frame_transport_certificate()
    expected_directions = {
        (-1, 0, 0): 4, (0, -1, 0): 4, (0, 0, -1): 4,
        (0, 0, 1): 4, (0, 1, 0): 4, (1, 0, 0): 4,
    }
    expected_weights = {
        (5, 4, 1, 1): 8, (9, 8, 1, 1): 8, (13, 12, 1, 1): 8,
    }
    check(
        "Cycle706 signed order-gauge transport closes the four factors in all 24 proper-cubic frames",
        frames["proper_cubic_frames"] == 24
        and frames["direction_census"] == expected_directions
        and frames["weight_census"] == expected_weights
        and frames["phase_census"] == {(0, 0, 0, 1): 24}
        and frames["order_gauge_transport_failures"] == 0
        and frames["hermitian_failures"] == 0
        and frames["signed_exact_failures"] == 0
        and frames["signed_phase_only_failures"] == 0,
        frames,
    )

    products = C.frame_product_certificate()
    check(
        "all 576 ordered frame products commute with signed factor transport",
        products == {
            "ordered_frame_products": 576,
            "group_closure_failures": 0,
            "cell_diagram_failures": 0,
            "signed_factor_diagram_failures": 0,
        },
        products,
    )

    boxes = C.five_box_certificate()
    expected = (
        ((2, 2, 2), 168, 12, 36, 9, 6, 0, 2, 0),
        ((3, 2, 2), 256, 20, 60, 16, 11, 0, 2, 0),
        ((4, 2, 2), 344, 28, 84, 25, 20, 4, 3, 8),
        ((3, 3, 2), 390, 33, 99, 28, 20, 0, 2, 0),
        ((3, 3, 3), 594, 54, 162, 48, 36, 0, 2, 0),
    )
    observed = tuple(
        (
            row["shape"], row["qubits"], row["seams"], row["rank_S_minus_I"],
            row["coloured_mismatches"]["exact"], row["cleanup_edges"],
            row["collinear_cleanup_edges"], row["cleanup_max_degree"],
            row["orthogonal_only_mismatches"]["exact"],
        )
        for row in boxes
    )
    check(
        "the fixed six-colour schedule plus frozen radius-one A_ef closes five boxes without refitting",
        observed == expected
        and all(not any(row["cleaned_mismatches"].values()) for row in boxes)
        and all(row["same_colour_factor_support_collisions"] == 0 for row in boxes)
        and all(row["cleanup_bipartite_failures"] == 0 for row in boxes)
        and all(not row["predicate_false_positives"] for row in boxes)
        and all(not row["predicate_false_negatives"] for row in boxes)
        and all(row["parameters_refit"] == 0 for row in boxes),
        {"observed": observed, "rows": boxes},
    )
    check(
        "the 4x2x2 held box activates the collinear cleanup discriminator",
        boxes[2]["collinear_cleanup_edges"] == 4
        and boxes[2]["single_collinear_delete_failures"] == (2, 2, 2, 2)
        and boxes[2]["orthogonal_only_mismatches"] == {
            "exact": 8, "symplectic": 8, "phase_only": 0,
        },
        boxes[2],
    )

    deletions = C.deletion_certificate()
    check(
        "active colour layers, every primary cleanup edge, and every rotation sign are deletion-sensitive",
        all(value > 0 for value in deletions["delete_active_colour_failures"])
        and all(value > 0 for value in deletions["delete_cleanup_edge_failures"])
        and all(value > 0 for value in deletions["wrong_rotation_sign_failures"]),
        deletions,
    )
    inverse = C.inverse_certificate()
    check(
        "the primary signed compiler has an exact explicit inverse",
        not any(inverse["primary_signed_inverse_failures"].values()),
        inverse,
    )

    translations = C.translation_certificate()
    check(
        "all eight colour-parity translation residues preserve the exact signed diagram",
        translations["parity_residue_translations"] == 8
        and translations["translated_semantic_failures"] == 0,
        translations,
    )
    unlawful = C.unlawful_certificate()
    check(
        "the bounded domain rejects shuffled path order, disconnected cells, and duplicates",
        unlawful["shuffled_cell_path_order_rejected"]
        and unlawful["disconnected_box_rejected"]
        and unlawful["duplicate_cell_rejected"],
        unlawful,
    )
    order_adversary = C.cell_order_adversary_certificate()
    zero_semantic_families = (
        "logical_Z", "logical_X", "local_D_all", "bond_to_rail", "cell_triangle"
    )
    check(
        "twelve deterministic order shuffles isolate 24 code-sector phase failures to coarse plaquettes",
        order_adversary["orders"] == 13
        and order_adversary["shuffles"] == 12
        and order_adversary["canonical_full_mismatches"] == 0
        and order_adversary["shuffled_full_mismatch_census"]
        == (54, 6, 55, 52, 57, 56, 57, 68, 51, 28, 28, 54)
        and order_adversary["coarse_plaquette_exact_per_shuffle"]
        == (2, 2, 0, 2, 2, 2, 2, 4, 2, 2, 0, 4)
        and all(
            not any(order_adversary["semantic_code_failure_sums"][name].values())
            for name in zero_semantic_families
        )
        and order_adversary["semantic_code_failure_sums"]["coarse_plaquette"]
        == {"exact": 24, "symplectic": 0, "phase_only": 24, "code": 24}
        and order_adversary["geometric_cleanup_edge_order_failures"] == 0,
        order_adversary,
    )

    inventory = C.boundary_inventory()
    check(
        "all supplied runtime structure and residual genesis/controller walls are explicit",
        "translated rectangular open box in supplied canonical product cell/path order"
        in inventory["runtime_inputs"]
        and "held-size fitted cleanup adjacency table"
        in inventory["removed_runtime_imports"]
        and "autonomous recurrent controller" in inventory["not_supplied_here"],
        inventory,
    )

    physical_reference = P.reference_certificate()
    route_covariance = physical_reference["reference_route_geometry_covariance"]
    check(
        "the reference seam lifts to 39 literal M2 and its four rotations compile to explicit H/S/CNOT/SWAP nearest-neighbour routes",
        physical_reference["abstract_qubits"] == 38
        and physical_reference["literal_M2"] == 39
        and physical_reference["placement_collisions"] == 0
        and physical_reference["abstract_factor_weights"] == (13, 12, 1, 1)
        and physical_reference["physical_factor_weights"] == (14, 13, 1, 1)
        and physical_reference["factor_union_M2"] == 14
        and physical_reference["repetition_stabilizer_failures"] == 0
        and physical_reference["primitive_gate_count"] == 74
        and physical_reference["maximum_state_residual_up_to_global_phase"] < 3e-12
        and physical_reference["routed_gate_count"] == 1558
        and physical_reference["maximum_route_distance"] == 24
        and physical_reference["non_NN_failures"] == 0
        and physical_reference["operand_order_failures"] == 0
        and physical_reference["route_return_failures"] == 0
        and physical_reference["maximum_local_gate_inverse_residual"] < 3e-12
        and physical_reference["H_CNOT_H_minus_CZ_residual"] < 3e-12,
        {key: value for key, value in physical_reference.items() if key != "routed_word"},
    )
    check(
        "every reference primitive class and a routed SWAP deletion are active while traversed occupied spectators return",
        all(
            residual > 1e-6
            for residual in physical_reference["delete_primitive_kind_residuals"].values()
        )
        and physical_reference["delete_first_swap_detected_macros"] == 50
        and physical_reference["occupied_spectator_sites_traversed_and_returned"] == 1,
        {
            "primitive_deletions": physical_reference["delete_primitive_kind_residuals"],
            "swap_deletion_macros": physical_reference["delete_first_swap_detected_macros"],
            "returned_spectators": physical_reference[
                "occupied_spectator_sites_traversed_and_returned"
            ],
        },
    )
    check(
        "the transported reference-route geometry closes 24 frame and 576 product coordinate diagrams",
        route_covariance["proper_cubic_frames"] == 24
        and route_covariance["ordered_frame_products"] == 576
        and route_covariance["rotated_word_NN_failures"] == 0
        and route_covariance["frame_product_site_diagram_failures"] == 0
        and route_covariance["translated_word_NN_failures"] == 0,
        route_covariance,
    )
    physical_axes = P.axis_physical_certificates()
    check(
        "the same physical H/S/CNOT/SWAP compiler closes all three positive seam axes",
        tuple(row["abstract_factor_weights"] for row in physical_axes)
        == ((13, 12, 1, 1), (9, 8, 1, 1), (5, 4, 1, 1))
        and tuple(row["physical_factor_weights"] for row in physical_axes)
        == ((14, 13, 1, 1), (10, 9, 1, 1), (6, 5, 1, 1))
        and all(row["literal_M2"] == 39 for row in physical_axes)
        and all(row["placement_collisions"] == 0 for row in physical_axes)
        and all(row["repetition_stabilizer_failures"] == 0 for row in physical_axes)
        and all(row["state_residual_up_to_global_phase"] < 3e-12 for row in physical_axes)
        and all(row["non_NN_failures"] == 0 for row in physical_axes)
        and all(row["operand_order_failures"] == 0 for row in physical_axes)
        and all(row["route_return_failures"] == 0 for row in physical_axes),
        physical_axes,
    )

    physical_primary = P.primary_certificate()
    overlap = physical_primary["overlap"]
    check(
        "the primary 3x2x2 compiler emits an explicit 276-M2 routed word with repetition, seam-colour, cleanup, phase, and Cycle708 endpoint controls",
        physical_primary["cells"] == 12
        and physical_primary["abstract_qubits"] == 256
        and physical_primary["seams"] == 20
        and physical_primary["literal_M2"] == 276
        and physical_primary["placement_collisions"] == 0
        and not physical_primary["signed_abstract_compiler_failures"]
        and physical_primary["physical_factor_rows"] == 80
        and physical_primary["repetition_stabilizer_failures"] == 0
        and physical_primary["same_colour_abstract_support_collisions"] == 0
        and physical_primary["seam_colour_layers"] == 6
        and physical_primary["cleanup_edge_layers"] == 2
        and physical_primary["cleanup_edge_layer_collisions"] == 0
        and physical_primary["primitive_gate_count"] == 1265
        and physical_primary["routed_gate_count"] == 22635
        and physical_primary["maximum_route_distance"] == 24
        and physical_primary["non_NN_failures"] == 0
        and physical_primary["operand_order_failures"] == 0
        and physical_primary["route_return_failures"] == 0
        and physical_primary["Cycle708_endpoint_rows"] == 36
        and physical_primary["Cycle708_endpoint_regression_failures"] == 0,
        {key: value for key, value in physical_primary.items() if key != "overlap"},
    )
    check(
        "the two 180-M2 cube views share the same 84-M2 ports and exactly cover the 276-M2 primary placement",
        overlap == {
            "left_cube_M2": 180,
            "right_cube_M2": 180,
            "cube_overlap_M2": 84,
            "cube_union_M2": 276,
            "primary_M2": 276,
            "shared_address_count": 80,
            "shared_cube_address_failures": 0,
            "left_to_primary_address_failures": 0,
            "right_to_primary_address_failures": 0,
            "cube_union_equals_primary": True,
        },
        overlap,
    )
    check(
        "the full-box covariance and autonomous parallel-routing boundaries remain explicit",
        physical_primary["full_box_semantic_covariance"].startswith("open:")
        and "remain open" in physical_primary["physical_schedule_boundary"],
        {
            "covariance": physical_primary["full_box_semantic_covariance"],
            "schedule": physical_primary["physical_schedule_boundary"],
        },
    )
    physical_scaling = P.placement_scaling_certificate()
    check(
        "the five literal placements obey 18N+3M <= 27N with no refit or collision",
        all(row["literal_M2"] == row["formula_18N_plus_3M"] for row in physical_scaling)
        and all(row["literal_M2"] <= row["constant_bound_27N"] for row in physical_scaling)
        and all(row["placement_collisions"] == 0 for row in physical_scaling)
        and all(row["parameters_refit"] == 0 for row in physical_scaling),
        physical_scaling,
    )

    summary = {
        "authority": "none",
        "audit": "unset",
        "claim_scope": (
            "bounded code-space signed-Clifford seam compiler on supplied-order "
            "translated boxes; free completion retained only as verification oracle; "
            "no source-genesis or autonomous-controller claim"
        ),
        "pass": PASS,
        "fail": FAIL,
        "reference": reference,
        "frames": frames,
        "frame_products": products,
        "boxes": boxes,
        "deletions": deletions,
        "mass_contact_regression": mass_contact,
        "inverse": inverse,
        "translations": translations,
        "unlawful": unlawful,
        "cell_order_adversary": order_adversary,
        "boundary": inventory,
        "physical_reference": {
            key: value for key, value in physical_reference.items() if key != "routed_word"
        },
        "physical_axes": physical_axes,
        "physical_primary": physical_primary,
        "physical_scaling": physical_scaling,
        "terminal": "CYCLE709_LOCAL_SEAM_PHYSICAL_M2_BOUNDED_COMPILER_PASS",
    }
    print("SUMMARY_JSON", json.dumps(json_ready(summary), sort_keys=True))
    if FAIL:
        return 1
    print("CYCLE709_LOCAL_SEAM_PHYSICAL_M2_BOUNDED_COMPILER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
