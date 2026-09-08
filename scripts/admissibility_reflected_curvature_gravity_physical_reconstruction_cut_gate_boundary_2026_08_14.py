#!/usr/bin/env python3
"""Block 75: discriminate the shortest physical gravity reconstructions.

The runner keeps the complete twenty-two-edge reflected action from Block 74.
It resolves a finite-frequency collision between a positive tensor-like pole
and an opposite-residue companion, tests two explicit canonical reductions,
and checks the rank-minimal auxiliary/connection rewrite.  The result is a
boundary on these supplied interfaces, not a no-go for canonical, connection,
or lattice gravity.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import root


ROOT = Path(__file__).resolve().parents[1]


# Current 2026-09-08 input closure. Historical raw identities below are provenance.
from hashlib import sha256 as _input_sha256

AUDIT_INPUT_PATHS = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMMON_METRIC_TT_OS_ONE_TWO_STEP_HANKEL_OBSTRUCTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CYCLE713_ENDPOINT_RECORD_ATTACHMENT_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_NONLINEAR_REGGE_EXTRA_BRANCH_CUBIC_LIFT_SOURCE_COMPATIBILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_PERIODIC_FLAT_EC_CONNECTION_NEGATIVE_MODE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_EDGE_SCORE_RANK_ONE_METRIC_STRESS_SPATIAL_PROJECTIVE_CURVATURE_REACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_WORLDLINE_CONSERVED_STRESS_TWO_TT_LORENTZIAN_CFL_LOCALITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/scripts/admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_2026_08_11.py',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/scripts/admissibility_record_edge_score_rank_one_metric_stress_spatial_projective_curvature_reaction_boundary_2026_08_10.py',
    'docs/ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md',
    'docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md',
    'docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_CUT_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md',
    'docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md',
    'docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md',
    'docs/CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md',
    'docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md',
    'docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md',
    'docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md',
    'docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md',
    'docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md',
    'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md',
    'docs/RECURRENT_ENCODE_UPDATE_DECODE_SANDWICH_CYCLE883_BOUNDED_THEOREM_NOTE_2026-08-03.md',
    'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md',
    'docs/audit/data/axiom_premise_nodes.json',
    'docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md',
    'docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md',
    'docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md',
    'scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py',
    'scripts/active_cubic_source_response_cycle211_2026_07_16.py',
    'scripts/admissibility_canonical_two_tt_positive_transfer_record_source_continuity_lstar_boundary_2026_08_11.py',
    'scripts/admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py',
    'scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py',
    'scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py',
    'scripts/admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py',
    'scripts/admissibility_cycle713_endpoint_record_attachment_intertwiner_boundary_2026_08_12.py',
    'scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py',
    'scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py',
    'scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py',
    'scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py',
    'scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py',
    'scripts/admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12.py',
    'scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py',
    'scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py',
    'scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py',
    'scripts/admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py',
    'scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py',
    'scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py',
    'scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py',
    'scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py',
    'scripts/admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py',
    'scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py',
    'scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py',
    'scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py',
    'scripts/common_matter_field_coin_family_cycle219_2026_07_16.py',
    'scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py',
    'scripts/fock_modular_boundary_current_cycle229_2026_07_17.py',
    'scripts/frontier_cubic_coxeter_regge_linearized_action_selection_2026_06_10.py',
    'scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py',
    'scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py',
    'scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py',
    'scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py',
    'scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py',
    'scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py',
    'scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py',
    'scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py',
    'scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py',
    'scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py',
    'scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py',
    'scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py',
    'scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py',
    'scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py',
    'scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py',
    'scripts/frontier_full128_code_projectors_2026_07_24.py',
    'scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py',
    'scripts/frontier_full128_cycle_encoder_2026_07_24.py',
    'scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py',
    'scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py',
    'scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py',
    'scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py',
    'scripts/local_generator_source_tournament_cycle228_2026_07_17.py',
    'scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py',
    'scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py',
    'scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py',
    'scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py',
    'scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py',
    'scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py',
    'scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py',
    'scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py',
    'scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py',
    'scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py',
    'scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py',
)
# Filled only after all source/prose/input paths are frozen, bottom-up.
CURRENT_INPUT_SHA256 = {
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'e64e84edb6f3571281525ead288e8cabf0581bea01dfc3c003b6dc4c3439db0d',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': 'c93967062ef731caab597d2fd5548f4c2fd74f40270f276d25c1696ecee708b4',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': '7bcb784ababcf1d81c5533ae57d92f0a629dd8568f3614c053e2981882164645',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMMON_METRIC_TT_OS_ONE_TWO_STEP_HANKEL_OBSTRUCTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': '81e16e6eab06ade811d53f3149a81427e60aa91cfa2bfd1f71c1a2fd7d899618',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': '3879d9e7f5dff044a5a80af2e677823892b92a5af792d334eaed529a6c888725',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': '216670e98030b021572db75e5ecca4e2c0d22248ac1f881ad034656da909166e',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': '5c3302965caac115b75d808a013ed572cb9a534db28bdb5b5bb1a17446138613',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CYCLE713_ENDPOINT_RECORD_ATTACHMENT_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md': '3198df874fe72b180fc995a8038a536e976d4538e91f126585221102869c8540',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md': '3179f81553c6d5f16dca06f83984195ef137cba46417dda5981de0e70a8afd5e',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': 'c623841b2641730b65392970538f0a170d744dc5134accb9c750192ecf73a941',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': '5d1c85a2b0074cc5931858bccbc8821f99f9db0afef44a0204729696dfc23d9d',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md': '63241ec60d7dddc2226378f8708551736de5db5311a94706bfe35a4d341f2be0',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_NONLINEAR_REGGE_EXTRA_BRANCH_CUBIC_LIFT_SOURCE_COMPATIBILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': '6e2b6e4447534f564d139a40e60e97f1ffeda2adc4a1403f51739782bf641d5e',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_PERIODIC_FLAT_EC_CONNECTION_NEGATIVE_MODE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'd046be06669a09458555fc7edad98f15cc56a8f89b00eef4597e5168ee9c28d2',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': '59d4af0ceb728bcd769df13dda8dd8e8f7ab3651bbd438ae0caf8fb880f96d2c',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md': 'cbeb0a7d080d419d8bfab901f73fa0e93d09bac63e4a3d462b4112033c5c918c',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': 'fb05667660091209ccdb30356e8b61c08b6a15906edff99ed21405288fdc75d4',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_EDGE_SCORE_RANK_ONE_METRIC_STRESS_SPATIAL_PROJECTIVE_CURVATURE_REACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': 'e64d576bd511492f0b8e1efcacd1101f246eef2eae677505531a74096e52fb3d',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md': '70c0cbe91e079e20111875b26589556dd21c197ade4638512ecd5070bb3e073e',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_WORLDLINE_CONSERVED_STRESS_TWO_TT_LORENTZIAN_CFL_LOCALITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'a773ef431321a8477d332f1f04295ddf18b960cc27c0637153561496cb87fa17',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'c656fd3e96379568bd4132583a93766a7e9296694a23b6c44f7a3284f15195a9',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'd69062c64a44663832d99fa91412f54a9dbada213ca2f441eda9ccfc088e8038',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'bdb422c2dbf43be60d236a3f8981133130b84884e10544d8480c3df535e1cfa9',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'cce0684fded7fa881acf39483b8486bdc28cdc7f6df979a28f51e91aada61277',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'd42e416d15e227c61597bac6db96536105017084494d6714c95e50fe78bedaed',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md': 'aec5700bca3f148c67ff27948e045afaa0ca861d7b29ae16608e890c08b89235',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md': '91b13f3be6f85b5f4184acd63db7fd79a427abcb9b6146d5673c0c662b9b17d2',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'b52d939a514eaee6a314936dea50b9ef2a7ba7139351a68eb3d53e8a44c6b9a8',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/scripts/admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_2026_08_11.py': 'bb21c34a49ac9f97eb37386a643fc0458061791e18736e21ae2f250ceb065bba',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/scripts/admissibility_record_edge_score_rank_one_metric_stress_spatial_projective_curvature_reaction_boundary_2026_08_10.py': '2cb9bb1a9f599b6ab91db95a7104a200b93e8d2b1f88f4cbfd7b8bd99791a7fd',
    'docs/ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md': 'c897f478045340ddac995eb2c381298b6ef5b8143676bd63cc9f5da3b5f8bb93',
    'docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md': 'b6b4e25cbdc3b87e5ee8db841b7378e8ea900dee09cf02c993ebb0b823dd4fb4',
    'docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': 'ec2ee0ae9f5bc7380849538569983517658703b63e4f5e975a7a131558f86528',
    'docs/ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_CUT_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': '10f7239d42f9661cad37444270cbc7ca166e6ae1297aef7678f1651cdf5051e6',
    'docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md': '87c6fa32a8978ea3868a2a3add6ccf1107a7f1d3a92e55715ab4ca664b7babd9',
    'docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md': '1851b00670be98cf4a5f22536ee1f95fd73c7066f5693d4209f43aa439b89ae2',
    'docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md': '798e0df4311aa59f5d0d4f24b20b8949fec863484d1482111b04bce357f0d9ea',
    'docs/CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md': '49450ca37fc5e95cadbeb9ca14dc624599489f2d3198c642e684a3e13bd0c3b5',
    'docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md': '52e6fe20cd162921322e18e794621499674c965cac7260ab2813fbefc0d25750',
    'docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md': '4a4dce8a459102124696e9449fb28e9cfee576645d22ab20da52624642047158',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md': '5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b',
    'docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md': 'c2599377d0627d701589185f942a1a42d2861c6e05136a4790c4f107c0121af1',
    'docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md': '0272a14eb5a1283ac0fb7edb05a0a08e68b9ced428020943d81364cad0033f03',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md': 'fcef8f6f965d1649741acc19302c4cdf4cb48286f9f969ff5d2ad250320f8c06',
    'docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md': '602cd4f5342deb44f064001e1fbc4d8902194d8a4929473e65e295ce10c1eafd',
    'docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md': '5b6e1b1a98eb09ce4b347394a83a51a1264bc1d7749a7810ab6105c17c147e43',
    'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md': '755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563',
    'docs/RECURRENT_ENCODE_UPDATE_DECODE_SANDWICH_CYCLE883_BOUNDED_THEOREM_NOTE_2026-08-03.md': 'f25441ace48d2b850aa6ac5b03601d4e71de4821775ee21c7dc6dc8414169fbd',
    'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md': 'e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
    'docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md': 'f57df7fb23fa2be384cd174162490a1b38a8bee5c300547822e42ee8d6a9ce7b',
    'docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md': 'c26a6f488521b7d138321a5ad23ff42905adec2197c5011d454ae6693c4b9b7e',
    'docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md': '314b7af4d25dbba9038ced26291f01924352e9500bb4fe994fe2902b00edc098',
    'scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py': '717a60f45c7d7e9e354b50005fea6ace4bae7b63d74cebb48ded59546cc561f9',
    'scripts/active_cubic_source_response_cycle211_2026_07_16.py': 'd5392152d322ea8f3850d0345d6caa426db22ae7f7694775b4bd6388704c18a6',
    'scripts/admissibility_canonical_two_tt_positive_transfer_record_source_continuity_lstar_boundary_2026_08_11.py': '0163111fae95de0c6aaed3b8e8caca6fff4eebf58530c3b5d9526d286e5ae722',
    'scripts/admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py': '5231d7fadb03b5026d2c7ce581d56d8f49f12d3d1501440644609503711a53d9',
    'scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py': 'c71a62d1468203e18f1388ff40666221142735dec1fa9fd4050916a5111ded70',
    'scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py': '7f27111aace40c2179bf7a8e5221096e366665d26b2acd9bb5332c811d9094b3',
    'scripts/admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py': '5c8f1d04017d2f6548c2159f1ba61e3f2a0ee3514a633ced2faea35c86860b62',
    'scripts/admissibility_cycle713_endpoint_record_attachment_intertwiner_boundary_2026_08_12.py': '4be3e2fdbec76eef15ccd08391a1c77e9c9d8ae1091d9a19e12f696447328fc8',
    'scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py': '21ece5393b085bca559d481a73e48b203b24d7a5f33feda118ecfbac05d7565b',
    'scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py': 'aee3ba64460976475f36bfc8b45fcc4319c285d3f9d8ebb5ee7a5b677181f801',
    'scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py': '4ba16259ea4fd59c2e1ac6d145a1fec506e892e35e56526359ca424559841617',
    'scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py': 'adb117ec956c27f486318673829464d47bc4cbe11fbffae88e70299ee2c35bce',
    'scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py': 'bdb7ed7f4ed979e64378adc770d7fb438eb48b36589897d78ccf0c3fff64ccef',
    'scripts/admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12.py': '7053f1ae58e1ab53a0be7cb0b8b25daac6889e501806940ff75e7950aee80a5e',
    'scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py': '6952a8bf9badcf0a546a024b365d8238376305014ad6755f06db6bfa45fee848',
    'scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py': '8184091297088a47404f6a94646c62ce72848bb842ec53e70f9536654456dcdd',
    'scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py': '64dc66c6492820b4051080eb4d6167dd55e09da2f23ebd8e920a2e4ed0ae607f',
    'scripts/admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py': '8cfe54ce6a3ecbcb82c52313b9b22bdfd8c6d0db3e131f5d9bf81d4b0e6c9353',
    'scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py': '8b4002ee5491591ee35912e6d91e023a1fe16e0da37d068ae9982c6c560584eb',
    'scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py': '15fd4711c7068412bc47859c8c4ae96dbb07605170745680e849bf7506d3f050',
    'scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py': '663176211b708c62643abf5c6d0abcaea397d19ccc80885ebe8e1fcb4a46e4cb',
    'scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py': '9e8dafb2f8916340e2131814340518cc64c42d418f78605845c782cef551916a',
    'scripts/admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py': '541dab9fa45be3b8333aacaa2c6f8159c2f268dae6d8fd7ab6c5046ee4586bb2',
    'scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py': '58adf86925073ea65bab1f348819a5fa10bcf86e911b2742bab44e11dd132b15',
    'scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py': 'a5e78e40cad0c43ee62ae887df7d84a0b895ab217ba4f3d521353e5d0b6bf95a',
    'scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py': '464e5928b7c1e46c23e4010363b6bd8ff3d0e2379c6e5ecb46891010ef47a5a4',
    'scripts/common_matter_field_coin_family_cycle219_2026_07_16.py': 'ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a',
    'scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py': '3a977106389428d2281ea7e0e32b65fe57f6ce33d783742b80f264f78f4f2c17',
    'scripts/fock_modular_boundary_current_cycle229_2026_07_17.py': 'fbf434a94c8dae57ffb6e68776642e4342a91f0d39f071ee1388fcb89ff846d7',
    'scripts/frontier_cubic_coxeter_regge_linearized_action_selection_2026_06_10.py': '31c0278dfa4223b493621168a310de7613df48db5385f0f8bbb4e33390123445',
    'scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py': '537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce',
    'scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py': '781823cf744be93de73f5e86e4e4cc988e0e7fe19c9c88a264b6f58169c07b0e',
    'scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py': '4d0049dbcb231301e0b0b110bc1933dfb2bda1aea2628e5e30bc5c1cee97d66a',
    'scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py': '71d073a95d089c13baf6fbaff4c3e3ebbd63650a3c152bba49f8de78ee377c69',
    'scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py': 'b42ea07c1ed671b9cbab38bc38eba6f8166fe65be52295941a95e3ed75049abf',
    'scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py': 'f5b604b714e8fbb33e2b6284cb38199e900859d710cd9e1411ee941a021235f3',
    'scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py': '3aa964a6eaca559048a53de580f39d9295a3e4b41ef9d4ff9dcdd4d3ff7444a7',
    'scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py': '64f73efb404f2acacb1a4e5e392aa8c6ac139eafb3e5f05380af9a3b3cc91826',
    'scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py': '5d49d85ddbc4daddfc0b24737dc569eaa9f32a050f5fccf48f048fe0fdd74b40',
    'scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py': 'd74fb32e21879b2a843eae822c8e71b950729d9dc295eaf336911f174cceee3a',
    'scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py': 'd4cb1fe7ba27dcf534d37e413d12dc50531ce17f2ca097a6c8b632644c260027',
    'scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py': 'c2e7f261c47092f11e445b16bde703330ccfd3e3af06bec0dac078ba64cf2297',
    'scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py': 'b61f98d0b44c1496883e8ab2ae1db065772ed053c77b6661a0153086acfd0e2f',
    'scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py': 'e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13',
    'scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py': '94f0fbd1212e210d0e073c3a80cdc2f92afa3c9807f981bd220625a67e8d94a0',
    'scripts/frontier_full128_code_projectors_2026_07_24.py': 'f561714d036c8c7568b1772110303d6c0da11c6d73c9df3bdcbae2db632f5b44',
    'scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py': 'ecae9048b4ee2d257315072cb7120335109f362fa7007573c46a82a1f0ed4195',
    'scripts/frontier_full128_cycle_encoder_2026_07_24.py': '17eca725b72943d8804147dd800be044ffaa80dc209588adb37ae6543d0fa935',
    'scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py': 'b446ace0856b45108ae0ed4ed35614961ae3b69bf20d12132981f54809966afb',
    'scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py': '05cb2f6083cf6c4307c04284632e991b7fd7378cbd2a4eb08a52d5e3c7ae6b99',
    'scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py': 'b418c74e82405a0511de81be0eef7080f98d5fe760ccac5d47783a6a751c2480',
    'scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py': '4ab857755b606d7ba7432179ed66de723ac31d3f66507cafa1168ab60d4965d6',
    'scripts/local_generator_source_tournament_cycle228_2026_07_17.py': '97fdf54189d7da93099aeab4a9b1dd8501c7262d55493b9fa95bf1c2f5c97a9d',
    'scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py': '15db2200b08bc4a5d7669975806fe51e9b8a55049f0660969d427332602bf9e8',
    'scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py': '67aa2435d66fb34b6734cc564a82ac839525139fdc9e8c347dc1b2277d08b40b',
    'scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py': 'ef6805e691a1ddd303a96f7cabd7000517e0cf33d5b1c577b20c2cbbf29aca23',
    'scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py': '4ef60441d31d62b1fc61c9b5e09ff3bc8f7f32d1b68bc3c548834431d24302f6',
    'scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py': '36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac',
    'scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py': 'a9786cf68a9c669e7e7fe310a00ab9912aa404689651682ccfe3045a06e357f1',
    'scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py': '6365d5aed1e70fb9b427ee6fb987879027cc30c818856a992b3fbf9d057e0c1b',
    'scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py': 'c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b',
    'scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py': '472e28c78901368629c8d9d6f614bb8fb3ea003639ac61d480d06941cdf6cb86',
    'scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py': 'b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae',
    'scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py': '9ef0fff433bbf1c96c9b13c5ce79530e01fe705f08c6caf6b60316e20359e011',
}

def current_input_failures(check_loaded: bool = False) -> tuple[str, ...]:
    failures = []
    if set(CURRENT_INPUT_SHA256) != set(AUDIT_INPUT_PATHS):
        failures.append("declared-input/hash-map mismatch")
    for relative in AUDIT_INPUT_PATHS:
        try:
            observed = _input_sha256((ROOT / relative).read_bytes()).hexdigest()
        except OSError:
            failures.append(relative + ": missing or unreadable")
            continue
        if observed != CURRENT_INPUT_SHA256.get(relative):
            failures.append(relative + ": content mismatch")
    if check_loaded:
        # This check runs only on direct main entry, not during parent imports.
        # Keep actual loaded-source coverage separate from historical Git status.
        import sys as _source_sys
        allowed = set(AUDIT_INPUT_PATHS)
        allowed.add(Path(__file__).resolve().relative_to(ROOT).as_posix())
        for module in tuple(_source_sys.modules.values()):
            file_name = getattr(module, "__file__", None)
            if not file_name:
                continue
            try:
                relative = Path(file_name).resolve().relative_to(ROOT).as_posix()
            except (OSError, ValueError):
                continue
            if relative.startswith("scripts/") and relative.endswith(".py") and relative not in allowed:
                failures.append(relative + ": loaded repository source is undeclared")
    return tuple(failures)

# Fail before local imports or scientific computation on input drift/removal.
_INPUT_FAILURES = current_input_failures()
if _INPUT_FAILURES:
    raise RuntimeError("current input binding failed: " + "; ".join(_INPUT_FAILURES))
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_"
    "CUT_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK49_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
BLOCK50_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
BLOCK53_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
BLOCK68_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
BLOCK74_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_"
    "TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"



sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11 as block44  # noqa: E402
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402
import admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11 as block49  # noqa: E402
import admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11 as block53  # noqa: E402
import admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14 as block74  # noqa: E402


MU_VALUES = (1.0 / 2048.0, 1.0 / 1024.0, 2.0 / 1024.0)
MU = MU_VALUES[1]
OUTER_POLES = (
    (1.25, (1.118, 1.159)),
    (1.32, (1.116, 1.160)),
)
COMPLEX_POLES = (
    (1.27, 1.138 + 0.008j, 1.138 - 0.008j),
    (1.28, 1.138 + 0.012j, 1.138 - 0.012j),
    (1.29, 1.138 + 0.012j, 1.138 - 0.012j),
    (1.30, 1.138 + 0.006j, 1.138 - 0.006j),
)
GRID_SIZE = 9
KINETIC_STEP = 1.0e-3


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 168 else detail[:165] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


@dataclass(frozen=True)
class Sector:
    name: str
    edge_basis: np.ndarray
    gauge_basis: np.ndarray
    observable: np.ndarray
    tt_vector: np.ndarray


@dataclass(frozen=True)
class PoleDatum:
    wave_number: float
    frequency: complex
    solver_success: bool
    determinant_residual: float
    bordered_null_ratio: float
    next_singular_ratio: float
    multiplier_ratio: float
    edge_null_ratio: float
    spectral_weights: tuple[complex, complex]
    initial_frequency: complex


@dataclass(frozen=True)
class DiracCertificate:
    ranks: tuple[int, int, int, int, int]
    inertias: tuple[tuple[int, int, int], ...]
    repaired_constraint_norm: float
    einstein_constraint_rank: int
    einstein_constraint_norm: float
    quotient_eigenvalues: tuple[float, float, float]
    tt_scalar_mixing: float
    source_components: tuple[float, float, float]
    source_eigencomponents: tuple[float, float, float]
    source_ward: float


@dataclass(frozen=True)
class ZoneCertificate:
    modes: int
    gauge_identity_error: float
    tt_dimensions: tuple[int, ...]
    negative_counts: tuple[tuple[int, int], ...]
    minimum_static: tuple[float, ...]
    minimum_kinetic: tuple[float, ...]
    hostile_static: tuple[float, float]
    hostile_kinetic: tuple[float, float]


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def matrix_rank(matrix: np.ndarray, tolerance: float = 1.0e-9) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tolerance))


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(np.abs(eigenvalues) <= tolerance)),
    )


def spatial_embedding() -> tuple[np.ndarray, tuple[np.ndarray, ...]]:
    pairs = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))
    embedding = np.zeros((len(block48.HCOMPS), 6), dtype=float)
    tensors = []
    for column, pair in enumerate(pairs):
        value = 1.0 if pair[0] == pair[1] else 1.0 / np.sqrt(2.0)
        embedding[block48.HCOMPS.index(pair), column] = value
        tensor = np.zeros((3, 3), dtype=float)
        tensor[pair] = value
        if pair[0] != pair[1]:
            tensor[pair[::-1]] = value
        tensors.append(tensor)
    return embedding, tuple(tensors)


SPATIAL_EMBEDDING, SPATIAL_TENSORS = spatial_embedding()
TEMPORAL_EMBEDDING = np.zeros((len(block48.HCOMPS), 4), dtype=float)
for _column, _pair in enumerate(((3, 3), (0, 3), (1, 3), (2, 3))):
    TEMPORAL_EMBEDDING[block48.HCOMPS.index(_pair), _column] = 1.0


def swap_matrix(vectors: np.ndarray, left: int, right: int) -> np.ndarray:
    integer_vectors = np.asarray(vectors, dtype=int)
    result = np.zeros((len(integer_vectors), len(integer_vectors)), dtype=float)
    for column, vector in enumerate(integer_vectors):
        image = vector.copy()
        image[left], image[right] = image[right], image[left]
        matches = np.flatnonzero(np.all(integer_vectors == image, axis=1))
        if len(matches) != 1:
            raise AssertionError("coordinate-swap image is not unique")
        result[matches[0], column] = 1.0
    return result


def sign_basis(involution: np.ndarray, sign: int) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(involution)
    return eigenvectors[:, np.isclose(eigenvalues, float(sign))]


def sector_data(
    union: block48.ReflectionUnion,
) -> tuple[tuple[Sector, Sector], np.ndarray, np.ndarray]:
    directions = np.asarray(union.directions, dtype=int)
    edge_swap = swap_matrix(directions, 1, 2)
    gauge_swap = np.eye(4)
    gauge_swap[[1, 2]] = gauge_swap[[2, 1]]
    plus, cross = block74.local_tt_observables(union, "")

    tt_cross = np.zeros(len(block48.HCOMPS), dtype=float)
    tt_cross[block48.HCOMPS.index((1, 2))] = 1.0 / np.sqrt(2.0)
    tt_plus = np.zeros(len(block48.HCOMPS), dtype=float)
    tt_plus[block48.HCOMPS.index((1, 1))] = 1.0 / np.sqrt(2.0)
    tt_plus[block48.HCOMPS.index((2, 2))] = -1.0 / np.sqrt(2.0)

    sectors = (
        Sector(
            "even",
            sign_basis(edge_swap, +1),
            sign_basis(gauge_swap, +1),
            cross,
            tt_cross,
        ),
        Sector(
            "odd",
            sign_basis(edge_swap, -1),
            sign_basis(gauge_swap, -1),
            plus,
            tt_plus,
        ),
    )
    return sectors, edge_swap, gauge_swap


def action_symbol(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    mu: float = MU,
) -> np.ndarray:
    return block74.cross_action_symbol(union, momentum, mu, "")


def axis_momentum(wave_number: float, frequency: complex) -> np.ndarray:
    return np.asarray((wave_number, 0.0, 0.0, -1j * frequency), dtype=complex)


def bordered_operator(
    union: block48.ReflectionUnion,
    wave_number: float,
    frequency: complex,
    sector: Sector,
) -> np.ndarray:
    momentum = axis_momentum(wave_number, frequency)
    symbol = -action_symbol(union, momentum)
    right_gauge = (
        sector.edge_basis.T
        @ block48.union_gauge_map(union, momentum)
        @ sector.gauge_basis
    )
    left_gauge = (
        sector.edge_basis.T
        @ block48.union_gauge_map(union, -momentum)
        @ sector.gauge_basis
    )
    reduced = sector.edge_basis.T @ symbol @ sector.edge_basis
    zeros = np.zeros(
        (sector.gauge_basis.shape[1], sector.gauge_basis.shape[1]), dtype=complex
    )
    return np.block([[reduced, left_gauge], [right_gauge.T, zeros]])


def solve_pole(
    union: block48.ReflectionUnion,
    wave_number: float,
    initial: complex,
    sector: Sector,
) -> tuple[complex, bool, float]:
    scale = float(np.linalg.norm(bordered_operator(union, wave_number, initial, sector)))

    def determinant_pair(values: np.ndarray) -> np.ndarray:
        frequency = complex(values[0], values[1])
        determinant = np.linalg.det(
            bordered_operator(union, wave_number, frequency, sector) / scale
        )
        return np.asarray((determinant.real, determinant.imag), dtype=float)

    result = root(
        determinant_pair,
        np.asarray((initial.real, initial.imag), dtype=float),
        method="hybr",
        options={"xtol": 1.0e-12},
    )
    return complex(result.x[0], result.x[1]), bool(result.success), float(
        np.linalg.norm(result.fun)
    )


def analytic_covariance(
    union: block48.ReflectionUnion,
    wave_number: float,
    frequency: complex,
    observable: np.ndarray,
) -> complex:
    momentum = axis_momentum(wave_number, frequency)
    symbol = -action_symbol(union, momentum)
    right_gauge = block48.union_gauge_map(union, momentum)
    left_gauge = block48.union_gauge_map(union, -momentum)
    bordered = np.block(
        [
            [symbol, left_gauge],
            [right_gauge.T, np.zeros((4, 4), dtype=complex)],
        ]
    )
    response = np.linalg.solve(
        bordered, np.concatenate((observable, np.zeros(4, dtype=complex)))
    )
    return complex(observable.T @ response[: len(union.directions)])


def pole_datum(
    union: block48.ReflectionUnion,
    wave_number: float,
    initial: complex,
    sector: Sector,
    mutation: str,
) -> PoleDatum:
    frequency, success, determinant_residual = solve_pole(
        union, wave_number, initial, sector
    )
    momentum = axis_momentum(wave_number, frequency)
    symbol = -action_symbol(union, momentum)
    bordered = bordered_operator(union, wave_number, frequency, sector)
    _, singular_values, right_vectors = np.linalg.svd(bordered)
    null_vector = right_vectors.conj().T[:, -1]
    edge_count = sector.edge_basis.shape[1]
    sector_edge = null_vector[:edge_count]
    multipliers = null_vector[edge_count:]
    edge_vector = sector.edge_basis @ sector_edge
    edge_vector /= np.linalg.norm(edge_vector)

    delta = 1.0e-7
    weights = tuple(
        -(sign * delta)
        * analytic_covariance(
            union, wave_number, frequency + sign * delta, sector.observable
        )
        for sign in (-1, +1)
    )
    if mutation == "flip_residue":
        weights = tuple(-value for value in weights)

    return PoleDatum(
        wave_number=wave_number,
        frequency=frequency,
        solver_success=success,
        determinant_residual=determinant_residual,
        bordered_null_ratio=float(singular_values[-1] / singular_values[0]),
        next_singular_ratio=float(singular_values[-2] / singular_values[0]),
        multiplier_ratio=float(
            np.linalg.norm(multipliers) / np.linalg.norm(sector_edge)
        ),
        edge_null_ratio=float(np.linalg.norm(symbol @ edge_vector) / np.linalg.norm(symbol)),
        spectral_weights=(complex(weights[0]), complex(weights[1])),
        initial_frequency=initial,
    )


def complete_complex_pole_census(hostile: tuple[tuple[PoleDatum, PoleDatum], ...]) -> bool:
    """Bind every declared wave number/seed and every complete-pole diagnostic."""
    expected = (
        (1.27, 1.138 + 0.008j, 1.138 - 0.008j),
        (1.28, 1.138 + 0.012j, 1.138 - 0.012j),
        (1.29, 1.138 + 0.012j, 1.138 - 0.012j),
        (1.30, 1.138 + 0.006j, 1.138 - 0.006j),
    )
    if len(hostile) != len(expected) or any(len(pair) != 2 for pair in hostile):
        return False
    for pair, (wave_number, upper, lower) in zip(hostile, expected):
        for item, initial in zip(pair, (upper, lower)):
            values = (
                item.frequency, item.determinant_residual,
                item.bordered_null_ratio, item.next_singular_ratio,
                item.multiplier_ratio, item.edge_null_ratio,
                *item.spectral_weights,
            )
            if not (item.wave_number == wave_number
                    and item.initial_frequency == initial
                    and all(np.isfinite(value) for value in values)
                    and item.solver_success
                    and 0 <= item.determinant_residual < 1.0e-14
                    and 0 <= item.bordered_null_ratio < 1.0e-14
                    and item.next_singular_ratio > 2.0e-5
                    and 0 <= item.multiplier_ratio < 1.0e-12
                    and 0 <= item.edge_null_ratio < 1.0e-14):
                return False
    return True


def constant_nonmetric_schur(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    nonmetric: np.ndarray,
    mu: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    q = np.asarray(momentum, dtype=complex)
    symbol = action_symbol(union, q, mu)
    metric = block49.union_line_metric_map(union, q)
    left_metric = block49.union_line_metric_map(union, -q).T
    complement = nonmetric.T @ symbol @ nonmetric
    effective = (
        left_metric @ symbol @ metric
        - left_metric
        @ symbol
        @ nonmetric
        @ np.linalg.solve(complement, nonmetric.T @ symbol @ metric)
    )
    return effective, complement, symbol


def dirac_certificate(
    union: block48.ReflectionUnion,
    mutation: str,
) -> DiracCertificate:
    momentum = np.asarray((0.4, 0.0, 0.0, 0.0), dtype=complex)
    metric_zero = block49.union_line_metric_map(union, np.zeros(4))
    nonmetric = null_space(metric_zero.T, rcond=1.0e-12)
    effective, complement, symbol = constant_nonmetric_schur(
        union, momentum, nonmetric, MU
    )

    spatial = SPATIAL_EMBEDDING
    temporal = TEMPORAL_EMBEDDING
    spatial_block = spatial.T @ effective @ spatial
    mixing = spatial.T @ effective @ temporal
    temporal_block = temporal.T @ effective @ temporal
    temporal_inverse = np.linalg.pinv(temporal_block, rcond=1.0e-10)
    reduced = spatial_block - mixing @ temporal_inverse @ mixing.conj().T

    repaired_left_null = null_space(
        temporal_block.conj().T, rcond=1.0e-10
    )
    repaired_constraint_norm = float(
        np.linalg.norm(repaired_left_null.conj().T @ (temporal.T @ effective @ spatial))
    )

    einstein = -0.5 * block44.einstein_action_pairing(
        np.asarray((0.4, 0.0, 0.0, 0.0)), np.eye(4)
    )
    einstein_temporal = temporal.T @ einstein @ temporal
    einstein_left_null = null_space(
        einstein_temporal.conj().T, rcond=1.0e-10
    )
    einstein_constraints = (
        einstein_left_null.conj().T @ (temporal.T @ einstein @ spatial)
    )

    plus = np.asarray((0.0, 1.0, -1.0, 0.0, 0.0, 0.0)) / np.sqrt(2.0)
    cross = np.asarray((0.0, 0.0, 0.0, 0.0, 0.0, 1.0))
    scalar = np.asarray((0.0, 1.0, 1.0, 0.0, 0.0, 0.0)) / np.sqrt(2.0)
    quotient = np.column_stack((plus, cross, scalar))
    quotient_form = quotient.conj().T @ (-reduced) @ quotient
    quotient_eigenvalues, quotient_vectors = np.linalg.eigh(quotient_form)
    tt_scalar_mixing = float(abs(quotient_form[1, 2]))

    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    source = np.zeros(len(union.directions), dtype=complex)
    source[edge_index[(0, 0, 0, 1)]] = 2.0
    metric = block49.union_line_metric_map(union, momentum)
    left_metric = block49.union_line_metric_map(union, -momentum).T
    effective_source = (
        left_metric @ source
        - left_metric
        @ symbol
        @ nonmetric
        @ np.linalg.solve(complement, nonmetric.T @ source)
    )
    spatial_source = (
        spatial.T @ effective_source
        - mixing @ temporal_inverse @ (temporal.T @ effective_source)
    )
    quotient_source = quotient.conj().T @ spatial_source
    eigen_source = quotient_vectors.conj().T @ quotient_source

    if mutation == "restore_constraint":
        repaired_constraint_norm = float(np.linalg.norm(einstein_constraints))

    return DiracCertificate(
        ranks=(
            matrix_rank(symbol),
            matrix_rank(complement),
            matrix_rank(effective),
            matrix_rank(temporal_block),
            matrix_rank(reduced),
        ),
        inertias=tuple(
            inertia(item)
            for item in (symbol, complement, effective, temporal_block, reduced)
        ),
        repaired_constraint_norm=repaired_constraint_norm,
        einstein_constraint_rank=matrix_rank(einstein_constraints),
        einstein_constraint_norm=float(np.linalg.norm(einstein_constraints)),
        quotient_eigenvalues=tuple(float(item) for item in quotient_eigenvalues),
        tt_scalar_mixing=tt_scalar_mixing,
        source_components=tuple(float(abs(item)) for item in quotient_source),
        source_eigencomponents=tuple(float(abs(item)) for item in eigen_source),
        source_ward=float(
            np.linalg.norm(source.conj() @ block48.union_gauge_map(union, momentum))
        ),
    )


def metric_gauge_coordinates(momentum: np.ndarray, mutation: str) -> np.ndarray:
    q = np.asarray(momentum, dtype=float)
    if mutation == "wrong_gauge_phase":
        q = 2.0 * np.sin(q / 2.0)
    result = np.zeros((len(block48.HCOMPS), 4), dtype=complex)
    for column in range(4):
        for row, (left, right) in enumerate(block48.HCOMPS):
            result[row, column] = 1j * (
                q[left] * int(right == column) + q[right] * int(left == column)
            )
    return result


def spatial_tt_basis(momentum: np.ndarray) -> np.ndarray:
    k = np.asarray(momentum, dtype=float)
    rows = [np.asarray([np.trace(tensor) for tensor in SPATIAL_TENSORS])]
    rows.extend(
        np.asarray([(tensor @ k)[axis] for tensor in SPATIAL_TENSORS])
        for axis in range(3)
    )
    return null_space(np.asarray(rows), rcond=1.0e-11)


def orthogonal_metric_schur(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    mu: float,
    constant_complement: np.ndarray | None,
) -> np.ndarray:
    q = np.asarray(momentum, dtype=complex)
    symbol = action_symbol(union, q, mu)
    metric = block49.union_line_metric_map(union, q)
    nonmetric = (
        null_space(metric.conj().T, rcond=1.0e-11)
        if constant_complement is None
        else constant_complement
    )
    complement = nonmetric.conj().T @ symbol @ nonmetric
    return (
        metric.conj().T @ symbol @ metric
        - metric.conj().T
        @ symbol
        @ nonmetric
        @ np.linalg.solve(complement, nonmetric.conj().T @ symbol @ metric)
    )


def tt_forms(
    union: block48.ReflectionUnion,
    spatial_momentum: np.ndarray,
    mu: float,
    constant_complement: np.ndarray | None,
) -> tuple[np.ndarray, np.ndarray]:
    k = np.asarray(spatial_momentum, dtype=float)
    tensor = SPATIAL_EMBEDDING @ spatial_tt_basis(k)
    values = []
    for temporal in (0.0, KINETIC_STEP, -KINETIC_STEP):
        effective = orthogonal_metric_schur(
            union, np.concatenate((k, (temporal,))), mu, constant_complement
        )
        values.append(tensor.conj().T @ effective @ tensor)
    static = -0.5 * (values[0] + values[0].conj().T)
    kinetic = -(
        0.5 * (values[1] + values[2]) - values[0]
    ) / (4.0 * np.sin(KINETIC_STEP / 2.0) ** 2)
    kinetic = 0.5 * (kinetic + kinetic.conj().T)
    return static, kinetic


def zone_certificate(
    union: block48.ReflectionUnion,
    mutation: str,
) -> ZoneCertificate:
    metric_zero = block49.union_line_metric_map(union, np.zeros(4))
    constant_complement = (
        null_space(metric_zero.T, rcond=1.0e-12)
        if mutation == "constant_complement"
        else None
    )
    gauge_identity_error = 0.0
    tt_dimensions: set[int] = set()
    negative_counts = [[0, 0] for _ in MU_VALUES]
    minimum_static = [np.inf for _ in MU_VALUES]
    minimum_kinetic = [np.inf for _ in MU_VALUES]
    modes = 0

    for integer_mode in np.ndindex((GRID_SIZE, GRID_SIZE, GRID_SIZE)):
        centered = np.asarray(integer_mode, dtype=int) - GRID_SIZE // 2
        if np.all(centered == 0):
            continue
        modes += 1
        k = 2.0 * np.pi * centered / GRID_SIZE
        q = np.concatenate((k, (0.0,)))
        metric = block49.union_line_metric_map(union, q)
        gauge = block48.union_gauge_map(union, q)
        gauge_coordinates = metric_gauge_coordinates(q, mutation)
        gauge_identity_error = max(
            gauge_identity_error, float(np.max(np.abs(metric @ gauge_coordinates - gauge)))
        )
        tt_dimensions.add(spatial_tt_basis(k).shape[1])
        for slot, mu in enumerate(MU_VALUES):
            static, kinetic = tt_forms(union, k, mu, constant_complement)
            static_minimum = float(np.linalg.eigvalsh(static)[0])
            kinetic_minimum = float(np.linalg.eigvalsh(kinetic)[0])
            negative_counts[slot][0] += int(static_minimum < -1.0e-7)
            negative_counts[slot][1] += int(kinetic_minimum < -1.0e-5)
            minimum_static[slot] = min(minimum_static[slot], static_minimum)
            minimum_kinetic[slot] = min(minimum_kinetic[slot], kinetic_minimum)

    hostile_static = tuple(
        float(item)
        for item in np.linalg.eigvalsh(
            tt_forms(
                union,
                2.0 * np.pi * np.asarray((2, 0, -2)) / GRID_SIZE,
                MU,
                constant_complement,
            )[0]
        )
    )
    hostile_kinetic = tuple(
        float(item)
        for item in np.linalg.eigvalsh(
            tt_forms(
                union,
                2.0 * np.pi * np.asarray((3, 4, -3)) / GRID_SIZE,
                MU,
                constant_complement,
            )[1]
        )
    )
    return ZoneCertificate(
        modes=modes,
        gauge_identity_error=gauge_identity_error,
        tt_dimensions=tuple(sorted(tt_dimensions)),
        negative_counts=tuple(tuple(item) for item in negative_counts),
        minimum_static=tuple(float(item) for item in minimum_static),
        minimum_kinetic=tuple(float(item) for item in minimum_kinetic),
        hostile_static=hostile_static,
        hostile_kinetic=hostile_kinetic,
    )


def corner_alias_certificate(
    union: block48.ReflectionUnion,
    mutation: str,
) -> tuple[int, int, float, float]:
    spatial = (
        np.asarray((np.pi, 0.0, 0.0))
        if mutation == "axis_corner"
        else np.asarray((np.pi, np.pi, np.pi))
    )
    momentum = np.concatenate((spatial, (0.0,)))
    tt = null_space(block53.tt_constraint(spatial), rcond=1.0e-11)
    metric = block49.union_line_metric_map(union, momentum)
    carrier = metric @ SPATIAL_EMBEDDING @ tt
    gauge = block48.union_gauge_map(union, momentum)
    fitted = gauge @ np.linalg.lstsq(gauge, carrier, rcond=None)[0]
    symbol = action_symbol(union, momentum)
    return (
        matrix_rank(metric),
        matrix_rank(carrier),
        float(np.linalg.norm(carrier - fitted)),
        float(np.linalg.norm(symbol @ carrier)),
    )


def auxiliary_certificate(
    union: block48.ReflectionUnion,
) -> tuple[int, float, float]:
    momentum = np.asarray((0.37, -0.21, 0.14, 0.42), dtype=complex)
    right = block49.centered_curvature_intertwiner(union, momentum)
    left = block49.centered_curvature_intertwiner(union, -momentum).T
    base = block48.union_symbol(union, momentum)
    edge_block = base + 2.0 * MU * left @ right
    joint_right = -2.0 * MU * left
    joint_left = -2.0 * MU * right
    auxiliary = 4.0 * MU * np.eye(3)
    schur = edge_block - joint_right @ np.linalg.solve(auxiliary, joint_left)
    target = action_symbol(union, momentum)
    schur_error = float(np.max(np.abs(schur - target)))

    index = {direction: slot for slot, direction in enumerate(union.directions)}
    reconstructed = np.zeros_like(right)
    for spatial in range(3):
        axis = np.zeros(4, dtype=int)
        axis[spatial] = 1
        time = np.asarray((0, 0, 0, 1), dtype=int)
        forward = tuple(axis + time)
        reflected = tuple(axis - time)
        plus = np.zeros(len(union.directions), dtype=complex)
        minus = np.zeros(len(union.directions), dtype=complex)
        plus[index[forward]] = np.sqrt(2.0)
        plus[index[tuple(axis)]] = -1.0
        plus[index[tuple(time)]] = -np.exp(1j * momentum[spatial])
        minus[index[reflected]] = np.sqrt(2.0) * np.exp(1j * momentum[3])
        minus[index[tuple(axis)]] = -np.exp(1j * momentum[3])
        minus[index[tuple(time)]] = -1.0
        reconstructed[spatial] = (
            np.exp(-0.5j * (momentum[spatial] + momentum[3])) * (plus + minus)
        )
    connection_error = float(np.max(np.abs(reconstructed - right)))
    zero_rank = matrix_rank(
        block49.centered_curvature_intertwiner(union, np.zeros(4)), 1.0e-12
    )
    return zero_rank, schur_error, connection_error


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    block49_note = flat(BLOCK49_PATH)
    block50_note = flat(BLOCK50_PATH)
    block53_note = flat(BLOCK53_PATH)
    block68_note = flat(BLOCK68_PATH)
    block74_note = flat(BLOCK74_PATH)

    loaded_input_failures = current_input_failures(check_loaded=True)
    if loaded_input_failures:
        raise RuntimeError("loaded source/input binding failed: " + "; ".join(loaded_input_failures))
    checks.check(
        "A-authority-and-parent-bindings",
        'current memo and final source/input bytes are pinned; original parent identities remain historical',
        not current_input_failures() and mutation not in ("stale_axiom_authority", "stale_os_authority"),
    )

    union = block48.build_reflection_union()
    sectors, edge_swap, gauge_swap = sector_data(union)
    symmetry_error = 0.0
    for frequency in (1.118, 1.138 + 0.012j, 1.160):
        momentum = axis_momentum(1.28, frequency)
        symbol = action_symbol(union, momentum)
        gauge = block48.union_gauge_map(union, momentum)
        symmetry_error = max(
            symmetry_error,
            float(np.max(np.abs(edge_swap @ symbol - symbol @ edge_swap))),
            float(np.max(np.abs(edge_swap @ gauge - gauge @ gauge_swap))),
        )
    checks.check(
        "B-exact-axis-sector-and-gauge-split",
        "the reflected action has exact 16+6 edge and 3+1 gauge y/z sectors on the analytic axis",
        len(union.directions) == 22
        and tuple(item.edge_basis.shape[1] for item in sectors) == (16, 6)
        and tuple(item.gauge_basis.shape[1] for item in sectors) == (3, 1)
        and np.max(np.abs(edge_swap @ edge_swap - np.eye(22))) < 1.0e-15
        and symmetry_error < 2.0e-13,
        f"sector dims={(16, 6)}/{(3, 1)}; symmetry error={symmetry_error:.3e}",
    )

    even = sectors[0]
    outer = tuple(
        pole_datum(union, wave_number, complex(initial), even, mutation)
        for wave_number, initials in OUTER_POLES
        for initial in initials
    )
    checks.check(
        "C-two-real-pole-pairs-are-complete-edge-nulls",
        "two isolated real even-sector poles exist on each side of the hostile collision band",
        all(item.solver_success for item in outer)
        and max(item.determinant_residual for item in outer) < 1.0e-14
        and max(abs(item.frequency.imag) for item in outer) < 5.0e-10
        and max(item.bordered_null_ratio for item in outer) < 1.0e-14
        and min(item.next_singular_ratio for item in outer) > 2.0e-5
        and max(item.multiplier_ratio for item in outer) < 1.0e-12
        and max(item.edge_null_ratio for item in outer) < 1.0e-14,
        "frequencies=" + ",".join(f"{item.frequency.real:.9f}" for item in outer)
        + f"; max null={max(item.bordered_null_ratio for item in outer):.3e}",
    )

    hostile_inputs = (
        COMPLEX_POLES
        if mutation != "erase_complex_pair"
        else ((1.25, 1.118 + 0j, 1.159 + 0j),) * len(COMPLEX_POLES)
    )
    hostile = tuple(
        (
            pole_datum(union, wave_number, complex(upper), even, mutation),
            pole_datum(union, wave_number, complex(lower), even, mutation),
        )
        for wave_number, upper, lower in hostile_inputs
    )
    conjugacy_error = max(
        abs(pair[0].frequency - pair[1].frequency.conjugate()) for pair in hostile
    )
    hostile_phases = tuple(abs(pair[0].frequency.imag) for pair in hostile)
    checks.check(
        "D-open-sampled-complex-pole-band",
        "the two real poles leave the real axis as a conjugate pair at four interior momenta",
        complete_complex_pole_census(hostile)
        and all(item.solver_success for pair in hostile for item in pair)
        and conjugacy_error < 2.0e-9
        and min(hostile_phases) > 4.0e-3
        and max(hostile_phases) < 2.0e-2
        and max(
            item.bordered_null_ratio for pair in hostile for item in pair
        )
        < 1.0e-14
        and max(item.edge_null_ratio for pair in hostile for item in pair) < 1.0e-14,
        "|Im omega|=" + ",".join(f"{item:.8f}" for item in hostile_phases)
        + f"; conjugacy={conjugacy_error:.3e}",
    )

    mean_weights = tuple(
        float(np.mean([value.real for value in item.spectral_weights]))
        for item in outer
    )
    side_error = max(
        abs(item.spectral_weights[0] - item.spectral_weights[1]) for item in outer
    )
    checks.check(
        "E-opposite-residue-companion-and-sign-exchange",
        "the local cross observable has one positive and one negative spectral weight which exchange branches",
        mean_weights[0] > 0.70
        and mean_weights[1] < -0.04
        and mean_weights[2] < -0.04
        and mean_weights[3] > 0.70
        and side_error < 2.0e-4,
        "-Res_E C=" + ",".join(f"{item:.9f}" for item in mean_weights)
        + f"; side error={side_error:.3e}",
    )

    dirac = dirac_certificate(union, mutation)
    checks.check(
        "F-repair-loses-einstein-hamiltonian-constraint",
        "the constant-complement metric Schur has only a gauge lapse null while Einstein has one constraint row",
        dirac.ranks == (18, 12, 6, 3, 3)
        and dirac.inertias[2] == (4, 2, 4)
        and dirac.inertias[3] == (2, 1, 1)
        and dirac.inertias[4] == (2, 1, 3)
        and dirac.repaired_constraint_norm < 1.0e-12
        and dirac.einstein_constraint_rank == 1
        and 0.05 < dirac.einstein_constraint_norm < 0.06,
        f"ranks={dirac.ranks}; repaired constraint={dirac.repaired_constraint_norm:.3e}; Einstein={dirac.einstein_constraint_norm:.9f}",
    )
    checks.check(
        "G-extra-indefinite-source-coupled-channel",
        "the three-channel quotient is indefinite, mixes TT with scalar, and the conserved static source reaches both",
        dirac.quotient_eigenvalues[0] < -0.018
        and dirac.quotient_eigenvalues[1] > 0.025
        and dirac.quotient_eigenvalues[2] > 0.038
        and dirac.tt_scalar_mixing > 0.011
        and dirac.source_components[1] > 0.20
        and dirac.source_components[2] > 0.27
        and dirac.source_eigencomponents[0] > 0.30
        and dirac.source_eigencomponents[2] > 0.14
        and dirac.source_ward < 1.0e-14,
        "eig=" + ",".join(f"{item:.9f}" for item in dirac.quotient_eigenvalues)
        + "; source eig="
        + ",".join(f"{item:.6f}" for item in dirac.source_eigencomponents),
    )

    zone = zone_certificate(union, mutation)
    checks.check(
        "H-exact-line-metric-gauge-and-two-tt-interface",
        "the raw-momentum metric gauge identity and two-dimensional analytic TT quotient hold on all 728 modes",
        zone.modes == 728
        and zone.gauge_identity_error < 2.0e-13
        and zone.tt_dimensions == (2,),
        f"modes={zone.modes}; gauge identity={zone.gauge_identity_error:.3e}; TT dims={zone.tt_dimensions}",
    )
    checks.check(
        "I-full-zone-canonical-schur-positivity-killed",
        "the three executed mu values share 276 static eigenvalues below -1e-7 and 174 finite-delta kinetic estimates below -1e-5",
        zone.negative_counts == ((276, 174), (276, 174), (276, 174))
        and max(zone.minimum_static) < -40.0
        and max(zone.minimum_kinetic) < -3000.0
        and zone.hostile_static[0] < -47.0
        and zone.hostile_static[1] > 0.59
        and zone.hostile_kinetic[0] < -3000.0
        and zone.hostile_kinetic[1] > 0.16,
        f"counts={zone.negative_counts}; hostile B={zone.hostile_static}; hostile A={zone.hostile_kinetic}",
    )

    corner = corner_alias_certificate(union, mutation)
    checks.check(
        "J-cubic-corner-two-tt-carrier-alias",
        "both site-TT directions map into exact edge gauge at the cubic corner while the metric chart drops to rank eight",
        corner[0] == 8
        and corner[1] == 2
        and corner[2] < 1.0e-12
        and corner[3] < 1.0e-12,
        f"rank(M/F)={corner[:2]}; gauge residual={corner[2]:.3e}; QF={corner[3]:.3e}",
    )

    auxiliary = auxiliary_certificate(union)
    checks.check(
        "K-rank-three-connection-rewrite-is-exact-marginal",
        "the exact triangle-connection stencil and rank-three positive auxiliary Schur reduce back to Q_mu",
        auxiliary[0] == 3
        and auxiliary[1] < 1.0e-13
        and auxiliary[2] < 1.0e-13
        and "inherits every raw-edge moment" in note,
        f"rank D0={auxiliary[0]}; Schur={auxiliary[1]:.3e}; stencil={auxiliary[2]:.3e}",
    )

    checks.check(
        "L-physical-boundary-and-no-go-discipline",
        "the current scope record preserves changed-action and changed-quotient alternatives without a complete N1/N2 independence claim",
        mutation != "note_scope"
        and all(f"### n{index}" in note for index in range(1, 9))
        and "premise-scoped mathematical outcome:" in note.replace("**", "")
        and all(
            phrase in note
            for phrase in (
                "not a gravity no-go",
                "changed physical quotient",
                "changed cross action",
                "no canonical axiom is edited",
                "no toe percentage movement",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: 22 edges, four exact gauge columns, two axis sectors, twelve nonmetric directions, 12 hostile poles, 728 spatial modes, three mu values, and two TT coordinates are resolved"
    )
    print(
        "per_element: checked every reflected edge, gauge column, metric coordinate, auxiliary row, and local TT observable"
    )
    print(
        "per_site: the supplied translation-invariant reflected Block-74 action and Block-49 line-metric chart are used unchanged"
    )
    print(
        "per_mode: checked the explicit pole-collision sample and all nonzero L=9 spatial momenta at three coefficients"
    )
    print(
        "per_block: checked analytic poles/residues, Dirac ranks, source coupling, full-zone TT Schurs, corner alias, and auxiliary elimination"
    )
    print(
        "lattice_wide: no continuum momentum theorem, nonlinear constraint algebra, selected clock, physical inner product, or complete Record dynamics is inferred"
    )
    print(
        "scope_boundary: route cut for the supplied Q_mu raw-edge marginal and two declared canonical charts; not canonical/connection gravity, axiom, or TOE closure"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
