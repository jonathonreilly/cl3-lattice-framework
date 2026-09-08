#!/usr/bin/env python3
"""Block 74: falsify the shortest reflected-curvature gravity transfer route.

The runner adds the exact Block-49 curvature intertwiner to the Block-48
twenty-two-edge reflected action,

    Q_mu(q) = Q_union(q) + mu D(-q)^T D(q),  mu = 1/1024.

It first tests the constructive target: lift only the three relative h_it
flat modes, retain the common ten-coordinate metric, exact displacement Ward
identities, time reflection, all six Block-68 Record sources, and
six finite static-source diagnostics at mu=1/1024 (not a proved limit).  It then applies a necessary Stieltjes/Hankel positivity
test to two genuinely local, same-time transverse edge observables.  The test
separates the attractive infrared two-slice result from a hostile finite-zone
counterexample.  It is a boundary on this action/cadence pair, not a gravity
no-go.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import os
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space


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
    "ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_"
    "TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK48_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
BLOCK49_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
BLOCK53_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
BLOCK68_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"



sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402
import admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11 as block49  # noqa: E402
import admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13 as block68  # noqa: E402


MU = 1.0 / 1024.0
RIVAL_MU = 2.0 / 1024.0
HALF_MU = 1.0 / 2048.0
TIME_SIZES = (256, 512, 1024, 2048)
IR_WAVE_NUMBER = 0.4
HOSTILE_WAVE_NUMBER = np.pi / 2.0
STATIC_WAVE_NUMBERS = (0.0125, 0.025, 0.05, 0.10, 0.20, 0.40)
TORUS_SIZES = tuple(range(3, 9))


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
class SourceCertificate:
    samples: int
    nullities: tuple[int, ...]
    maximum_ward: float
    maximum_relative_residual: tuple[float, ...]
    selection_ratio: float


@dataclass(frozen=True)
class TemporalCarrier:
    size: int
    wave_number: float
    moments: tuple[np.ndarray, np.ndarray]
    quotient_inertias: tuple[tuple[int, int, int], ...]
    maximum_gauge_overlap: float
    maximum_reflection_overlap: float
    maximum_ward: float
    maximum_hermiticity: float
    maximum_bordered_error: float
    minimum_quotient_gap: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    hermitian = 0.5 * (matrix + matrix.conj().T)
    eigenvalues = np.linalg.eigvalsh(hermitian)
    return (
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(np.abs(eigenvalues) <= tolerance)),
    )


def cross_action_symbol(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    mu: float,
    mutation: str = "",
) -> np.ndarray:
    """Finite-range reflected action with an analytic D(-q)^T D(q) term."""

    q = np.asarray(momentum, dtype=complex)
    right = block49.centered_curvature_intertwiner(union, q)
    if mutation == "wrong_reflection_factor":
        left = right.T
        penalty = left @ right
    else:
        left = block49.centered_curvature_intertwiner(union, -q).T
        penalty = left @ right
    return block48.union_symbol(union, q) + mu * penalty


def relative_shift_modes(
    union: block48.ReflectionUnion,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    (shared_constraint, pair_to_union, _), _ = block48.union_reflection_split(union)
    relative_pairs = np.zeros((20, 3), dtype=float)
    for column, spatial in enumerate(range(3)):
        component = block48.HCOMPS.index((spatial, 3))
        relative_pairs[component, column] = 1.0
        relative_pairs[len(block48.HCOMPS) + component, column] = -1.0
    return shared_constraint, pair_to_union, pair_to_union @ relative_pairs


def structural_certificate(
    union: block48.ReflectionUnion, mu: float, mutation: str
) -> dict[str, object]:
    shared, pair_to_union, relative = relative_shift_modes(union)
    common = block48.metric_coefficients(np.asarray(union.directions))
    zero = np.zeros(4, dtype=complex)
    rows_zero = block49.centered_curvature_intertwiner(union, zero)
    symbol_zero = cross_action_symbol(union, zero, mu, mutation)

    common_residual = float(np.max(np.abs(rows_zero @ common)))
    relative_singular = np.linalg.svd(rows_zero @ relative, compute_uv=False)
    combined_rank = int(
        np.linalg.matrix_rank(
            np.column_stack((common, relative)), tol=1.0e-12
        )
    )

    momenta = (
        np.asarray((0.025, 0.0, 0.0, 0.0)),
        np.asarray((0.40, 0.0, 0.0, 0.0)),
        np.asarray((0.30, 0.20, -0.10, 0.40)),
        np.asarray((1.20, -0.20, 0.40, 0.70)),
    )
    nullities: set[int] = set()
    maximum_ward = 0.0
    maximum_reflection = 0.0
    maximum_hermiticity = 0.0
    for momentum in momenta:
        symbol = cross_action_symbol(union, momentum, mu, mutation)
        right_gauge = block48.union_gauge_map(union, momentum)
        left_gauge = block48.union_gauge_map(union, -momentum)
        nullities.add(22 - int(np.linalg.matrix_rank(symbol, tol=1.0e-9)))
        maximum_ward = max(
            maximum_ward,
            float(np.max(np.abs(symbol @ right_gauge))),
            float(np.max(np.abs(left_gauge.T @ symbol))),
        )
        reflected = block48.TIME_REFLECTION @ momentum
        theta_right = block48.union_time_reflection_matrix(union, momentum)
        theta_left = block48.union_time_reflection_matrix(union, -momentum)
        transformed = (
            theta_left.T
            @ cross_action_symbol(union, reflected, mu, mutation)
            @ theta_right
        )
        maximum_reflection = max(
            maximum_reflection, float(np.max(np.abs(symbol - transformed)))
        )
        maximum_hermiticity = max(
            maximum_hermiticity, float(np.max(np.abs(symbol - symbol.conj().T)))
        )

    return {
        "zero_inertia": inertia(symbol_zero),
        "common_residual": common_residual,
        "relative_singular": relative_singular,
        "combined_rank": combined_rank,
        "shared_rank": int(np.linalg.matrix_rank(shared, tol=1.0e-12)),
        "pair_rank": int(np.linalg.matrix_rank(pair_to_union, tol=1.0e-12)),
        "nullities": tuple(sorted(nullities)),
        "ward": maximum_ward,
        "reflection": maximum_reflection,
        "hermiticity": maximum_hermiticity,
    }


def source_certificate(
    union: block48.ReflectionUnion,
    mus: tuple[float, ...],
    drop_closure_edge: bool,
    mutation: str,
) -> SourceCertificate:
    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    maximum_ward = 0.0
    maximum_relative_residual = np.zeros(len(mus), dtype=float)
    nullities: set[int] = set()
    samples = 0
    selection_pair: tuple[np.ndarray, np.ndarray] | None = None

    for size in TORUS_SIZES:
        for direction in block68.DIRECTIONS:
            carrier = block68.canonical_carrier(tuple(union.directions), direction)
            if carrier is None:
                raise AssertionError("reflected union must carry every signed direction")
            edge, base_offset = carrier
            row = edge_index[edge]
            step = np.concatenate((direction, (1,))).astype(int)
            separation = block68.transverse_offset(direction)
            line_length = size - int(drop_closure_edge)
            for mode in product(range(size), repeat=4):
                momentum = 2.0 * np.pi * np.asarray(mode, dtype=float) / size
                line_factor = sum(
                    np.exp(1j * np.dot(momentum, count * step + base_offset))
                    for count in range(line_length)
                )
                neutral_factor = line_factor * (
                    1.0 - np.exp(1j * np.dot(momentum, separation))
                )
                source = np.zeros(len(union.directions), dtype=complex)
                source[row] = 2.0 * neutral_factor
                source_norm = float(np.linalg.norm(source))
                if source_norm < 1.0e-9:
                    continue

                samples += 1
                gauge = block48.union_gauge_map(union, momentum)
                maximum_ward = max(
                    maximum_ward, float(np.linalg.norm(source.conj() @ gauge))
                )
                source_column = source.conj()
                curvature = block49.centered_curvature_intertwiner(union, momentum)
                responses = []
                for slot, mu in enumerate(mus):
                    symbol = cross_action_symbol(union, momentum, mu, mutation)
                    nullities.add(22 - int(np.linalg.matrix_rank(symbol, tol=1.0e-9)))
                    response = -np.linalg.pinv(symbol, rcond=1.0e-9) @ source_column
                    residual = float(np.linalg.norm(symbol @ response + source_column))
                    maximum_relative_residual[slot] = max(
                        maximum_relative_residual[slot], residual / source_norm
                    )
                    responses.append(curvature @ response)

                if (
                    size == 5
                    and tuple(int(item) for item in direction) == (1, 0, 0)
                    and tuple(mode) == (1, 1, 0, 4)
                ):
                    selection_pair = (responses[0], responses[1])

    if selection_pair is None:
        raise AssertionError("declared coefficient-selection witness was not executed")
    selection_ratio = float(
        (np.linalg.norm(selection_pair[0]) - np.linalg.norm(selection_pair[1]))
        / np.linalg.norm(selection_pair[0])
    )
    return SourceCertificate(
        samples=samples,
        nullities=tuple(sorted(nullities)),
        maximum_ward=maximum_ward,
        maximum_relative_residual=tuple(float(item) for item in maximum_relative_residual),
        selection_ratio=selection_ratio,
    )


def static_source_certificate(
    union: block48.ReflectionUnion, mu: float, mutation: str
) -> dict[str, tuple[float, ...]]:
    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    source = np.zeros(len(union.directions), dtype=complex)
    source[edge_index[(0, 0, 0, 1)]] = 2.0
    residues = []
    nonmetric_fractions = []
    solve_residuals = []
    for wave_number in STATIC_WAVE_NUMBERS:
        momentum = np.asarray((wave_number, 0.0, 0.0, 0.0), dtype=complex)
        symbol = cross_action_symbol(union, momentum, mu, mutation)
        response = -np.linalg.pinv(symbol, rcond=1.0e-10) @ source
        metric_map = block49.union_line_metric_map(union, momentum)
        metric = np.linalg.lstsq(metric_map, response, rcond=None)[0]
        fitted = metric_map @ metric
        residues.append(
            float(
                (wave_number**2 * metric[block48.HCOMPS.index((3, 3))]).real
            )
        )
        nonmetric_fractions.append(
            float(np.linalg.norm(response - fitted) / np.linalg.norm(response))
        )
        solve_residuals.append(float(np.linalg.norm(symbol @ response + source)))
    return {
        "residues": tuple(residues),
        "nonmetric": tuple(nonmetric_fractions),
        "solve": tuple(solve_residuals),
    }


def local_tt_observables(
    union: block48.ReflectionUnion, mutation: str
) -> tuple[np.ndarray, np.ndarray]:
    index = {direction: slot for slot, direction in enumerate(union.directions)}
    plus = np.zeros(len(union.directions), dtype=complex)
    plus[index[(0, 1, 0, 0)]] = 1.0
    plus[index[(0, 0, 1, 0)]] = -1.0

    cross = np.zeros(len(union.directions), dtype=complex)
    cross[index[(0, 1, 1, 0)]] = np.sqrt(2.0)
    cross[index[(0, 1, 0, 0)]] = -1.0
    cross[index[(0, 0, 1, 0)]] = -1.0
    if mutation == "gauge_observable":
        cross[index[(1, 0, 0, 0)]] += 1.0
    return plus, cross


def temporal_carrier(
    union: block48.ReflectionUnion,
    size: int,
    wave_number: float,
    mu: float,
    mutation: str,
) -> TemporalCarrier:
    frequencies = -np.pi + np.arange(size) * (2.0 * np.pi / size)
    observables = local_tt_observables(union, mutation)
    covariance = tuple(np.empty(size, dtype=complex) for _ in observables)
    quotient_inertias: set[tuple[int, int, int]] = set()
    maximum_gauge_overlap = 0.0
    maximum_reflection_overlap = 0.0
    maximum_ward = 0.0
    maximum_hermiticity = 0.0
    maximum_bordered_error = 0.0
    minimum_quotient_gap = np.inf

    for frequency_index, frequency in enumerate(frequencies):
        momentum = np.asarray((wave_number, 0.0, 0.0, frequency), dtype=complex)
        symbol = cross_action_symbol(union, momentum, mu, mutation)
        gauge = block48.union_gauge_map(union, momentum)
        quotient = null_space(gauge.conj().T, rcond=1.0e-11)
        operator = quotient.conj().T @ (-symbol) @ quotient
        operator = 0.5 * (operator + operator.conj().T)
        quotient_inertias.add(inertia(operator))
        minimum_quotient_gap = min(
            minimum_quotient_gap,
            float(np.min(np.abs(np.linalg.eigvalsh(operator)))),
        )
        maximum_ward = max(maximum_ward, float(np.linalg.norm(symbol @ gauge)))
        maximum_hermiticity = max(
            maximum_hermiticity, float(np.linalg.norm(symbol - symbol.conj().T))
        )
        for slot, observable in enumerate(observables):
            maximum_gauge_overlap = max(
                maximum_gauge_overlap,
                float(np.linalg.norm(gauge.conj().T @ observable)),
            )
            reflection = block48.union_time_reflection_matrix(union, momentum)
            maximum_reflection_overlap = max(
                maximum_reflection_overlap,
                float(np.linalg.norm(reflection @ observable - observable)),
            )
            projected = quotient.conj().T @ observable
            covariance_value = projected.conj() @ np.linalg.solve(operator, projected)
            covariance[slot][frequency_index] = covariance_value
            bordered = np.block(
                [
                    [-symbol, gauge],
                    [gauge.conj().T, np.zeros((4, 4), dtype=complex)],
                ]
            )
            right_hand_side = np.concatenate((observable, np.zeros(4, dtype=complex)))
            bordered_response = np.linalg.solve(bordered, right_hand_side)[:22]
            bordered_value = observable.conj() @ bordered_response
            maximum_bordered_error = max(
                maximum_bordered_error,
                float(abs(covariance_value - bordered_value)),
            )

    moments = tuple(
        np.asarray(
            [
                np.mean(np.exp(1j * frequencies * time) * values).real
                for time in range(13)
            ]
        )
        for values in covariance
    )
    return TemporalCarrier(
        size=size,
        wave_number=wave_number,
        moments=(moments[0], moments[1]),
        quotient_inertias=tuple(sorted(quotient_inertias)),
        maximum_gauge_overlap=maximum_gauge_overlap,
        maximum_reflection_overlap=maximum_reflection_overlap,
        maximum_ward=maximum_ward,
        maximum_hermiticity=maximum_hermiticity,
        maximum_bordered_error=maximum_bordered_error,
        minimum_quotient_gap=minimum_quotient_gap,
    )


def hankel_minimum(
    moments: np.ndarray, step: int, order: int, shift: int
) -> float:
    matrix = np.asarray(
        [
            [moments[step * (left + right + shift)] for right in range(order)]
            for left in range(order)
        ],
        dtype=float,
    )
    return float(np.linalg.eigvalsh(matrix)[0])


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    block48_note = flat(BLOCK48_PATH)
    block49_note = flat(BLOCK49_PATH)
    block53_note = flat(BLOCK53_PATH)
    block68_note = flat(BLOCK68_PATH)

    loaded_input_failures = current_input_failures(check_loaded=True)
    if loaded_input_failures:
        raise RuntimeError("loaded source/input binding failed: " + "; ".join(loaded_input_failures))
    checks.check(
        "A-authority-and-scope-bindings",
        'current memo and final source/input bytes are pinned; original parent identities remain historical',
        not current_input_failures() and mutation not in ("stale_axiom_authority", "stale_os_authority"),
    )

    union = block48.build_reflection_union()
    applied_mu = 0.0 if mutation == "remove_cross_action" else MU
    structural = structural_certificate(union, applied_mu, mutation)
    checks.check(
        "B-exact-flat-fiber-thirteen-to-ten",
        "the local curvature square lifts exactly three relative h_it modes and leaves ten common flat metrics",
        len(union.directions) == 22
        and structural["shared_rank"] == 7
        and structural["pair_rank"] == 17
        and structural["combined_rank"] == 13
        and structural["zero_inertia"] == (7, 5, 10)
        and structural["common_residual"] < 5.0e-15
        and np.max(np.abs(np.asarray(structural["relative_singular"]) - 2.0)) < 5.0e-15,
        "Q0 inertia=" + str(structural["zero_inertia"])
        + f"; D common={structural['common_residual']:.3e}; relative singular="
        + np.array2string(np.asarray(structural["relative_singular"]), precision=9),
    )
    checks.check(
        "C-local-ward-reflection-and-four-null-sector",
        "the cross action is Hermitian, reflection covariant, Ward null, and leaves only four generic gauge nulls",
        structural["nullities"] == (4,)
        and structural["ward"] < 1.0e-12
        and structural["reflection"] < 1.0e-12
        and structural["hermiticity"] < 1.0e-12,
        f"nullities={structural['nullities']}; Ward={structural['ward']:.3e}; reflection={structural['reflection']:.3e}; Hermiticity={structural['hermiticity']:.3e}",
    )

    source = source_certificate(
        union,
        (MU, RIVAL_MU if mutation != "erase_rival" else MU),
        mutation == "drop_closure_edge",
        mutation,
    )
    checks.check(
        "D-all-six-record-sources-survive",
        "all 6,528 supported closed neutral six-direction Record sources solve with exactly four nulls",
        source.samples == 6528
        and source.nullities == (4,)
        and source.maximum_ward < 1.0e-12
        and max(source.maximum_relative_residual) < 1.0e-10,
        f"samples={source.samples}; nullities={source.nullities}; Ward={source.maximum_ward:.3e}; relative solve={source.maximum_relative_residual}",
    )

    static = static_source_certificate(union, MU, mutation)
    checks.check(
        "E-newtonian-residue-and-common-metric-limit",
        "the six executed mu=1/1024 static samples meet the stated residue and nonmetric-fraction tolerances",
        abs(static["residues"][0] - 2.0) < 5.0e-5
        and abs(static["residues"][-1] - 2.0) < 0.02
        and static["nonmetric"][0] < 5.0e-6
        and static["nonmetric"][-1] < 5.0e-3
        and max(static["solve"]) < 2.0e-10,
        "k^2h_tt=" + ",".join(f"{item:.9f}" for item in static["residues"])
        + "; nonmetric=" + ",".join(f"{item:.3e}" for item in static["nonmetric"]),
    )

    checks.check(
        "F-coefficient-selection-countermodel",
        "mu and two-mu pass the executed source-solvability checks and give different algebraic curvature responses; structural/static checks use mu only",
        0.17 < source.selection_ratio < 0.19
        and mutation != "note_scope",
        f"L=5, d=+x, mode=(1,1,0,4) relative curvature-response norm drop={source.selection_ratio:.9f}",
    )

    ir_data = tuple(
        temporal_carrier(union, size, IR_WAVE_NUMBER, MU, mutation)
        for size in TIME_SIZES
    )
    hostile_wave = IR_WAVE_NUMBER if mutation == "replace_hostile_by_ir" else HOSTILE_WAVE_NUMBER
    hostile_data = tuple(
        temporal_carrier(union, size, hostile_wave, MU, mutation)
        for size in TIME_SIZES
    )
    all_carriers = ir_data + hostile_data
    checks.check(
        "G-local-same-time-tt-observable-interface",
        "the plus and cross edge combinations are exactly gauge invariant and the quotient calculation is stable",
        max(item.maximum_gauge_overlap for item in all_carriers) < 1.0e-13
        and max(item.maximum_reflection_overlap for item in all_carriers) < 1.0e-13
        and max(item.maximum_ward for item in all_carriers) < 2.0e-12
        and max(item.maximum_hermiticity for item in all_carriers) < 2.0e-12
        and max(item.maximum_bordered_error for item in all_carriers) < 2.0e-12
        and min(item.minimum_quotient_gap for item in all_carriers) > 2.0e-3
        and all(item.quotient_inertias == ((4, 14, 0),) for item in all_carriers),
        f"gauge={max(item.maximum_gauge_overlap for item in all_carriers):.3e}; reflection={max(item.maximum_reflection_overlap for item in all_carriers):.3e}; bordered={max(item.maximum_bordered_error for item in all_carriers):.3e}; gap={min(item.minimum_quotient_gap for item in all_carriers):.3e}; inertias={sorted(set(item.quotient_inertias for item in all_carriers))}",
    )

    convergence = max(
        float(np.max(np.abs(data[-1].moments[observable][:9] - data[-2].moments[observable][:9])))
        for data in (ir_data, hostile_data)
        for observable in range(2)
    )
    checks.check(
        "H-temporal-carrier-convergence",
        "the first nine local-observable moments converge across the two finest temporal carriers",
        convergence < 1.0e-9,
        f"maximum N=1024 to N=2048 moment change={convergence:.3e}",
    )

    ir = ir_data[-1]
    one_step_shifted = tuple(
        hankel_minimum(moments, step=1, order=2, shift=1)
        for moments in ir.moments
    )
    checks.check(
        "I-one-step-positive-transfer-killed",
        "the shifted Stieltjes Hankel condition is negative for both local TT observables at k=0.4",
        one_step_shifted[0] < -1.0e-6
        and one_step_shifted[1] < -1.0e-4,
        f"shifted one-step minima plus={one_step_shifted[0]:.9e}, cross={one_step_shifted[1]:.9e}",
    )

    ir_two_step = tuple(
        (
            hankel_minimum(moments, step=2, order=2, shift=0),
            hankel_minimum(moments, step=2, order=2, shift=1),
        )
        for moments in ir.moments
    )
    checks.check(
        "J-infrared-two-step-escape-retained",
        "the first unshifted and shifted two-step tests are positive at k=0.4, so the hostile test is load bearing",
        min(value for pair in ir_two_step for value in pair) > 1.0e-10,
        f"IR two-step minima plus={ir_two_step[0]}, cross={ir_two_step[1]}",
    )

    hostile = hostile_data[-1]
    hostile_two_step = tuple(
        (
            hankel_minimum(moments, step=2, order=3, shift=0),
            hankel_minimum(moments, step=2, order=2, shift=1),
        )
        for moments in hostile.moments
    )
    tuning_rows = []
    for mu in (HALF_MU, MU, RIVAL_MU):
        datum = temporal_carrier(union, TIME_SIZES[-1], hostile_wave, mu, mutation)
        tuning_rows.append(
            tuple(
                hankel_minimum(moments, step=2, order=3, shift=0)
                for moments in datum.moments
            )
        )
    checks.check(
        "K-two-step-full-zone-transfer-killed",
        "the apparent infrared two-step escape has a stable negative half-space Gram at k=pi/2 for both TT observables",
        hostile_two_step[0][0] < -3.0e-7
        and hostile_two_step[1][0] < -5.0e-8
        and hostile_two_step[1][1] < -3.0e-7
        and all(row[0] < -3.0e-7 for row in tuning_rows)
        and all(row[1] < -1.0e-9 for row in tuning_rows),
        f"hostile plus={hostile_two_step[0]}, cross={hostile_two_step[1]}; half/base/double unshifted={tuning_rows}",
    )

    checks.check(
        "L-no-go-discipline-and-axiom-boundary",
        "the scope record preserves longer-block, boundary, canonical, and connection routes; N1/N2 completeness and independence remain unresolved",
        all(f"n{index} —" in note for index in range(1, 9))
        and all(
            phrase in note
            for phrase in (
                "longer blocking",
                "boundary term",
                "canonical constraint reduction",
                "connection/holonomy",
                "no canonical axiom is edited",
                "zero toe percentage movement",
            )
        )
        and mutation != "note_scope",
    )

    print(
        "N5_CERTIFICATE: 22 reflected edges, 3 local curvature rows, 10 common metric modes, 3 relative shifts, 4 gauge nulls, 6,528 Record-source modes, 6 static residues, 2 local TT observables, 4 temporal carriers, 2 momenta, and 3 mu values are resolved"
    )
    print(
        "per_element: every coefficient of the three reflected curvature rows, both local same-time TT edge observables, and every source/response vector enters the checks"
    )
    print(
        "per_site: the finite-range original-plus-reflected unit-cell action and its transverse same-time y-z edge combinations are executed without a metric-only projection"
    )
    print(
        "per_mode: every supported Block-68 source mode on periodic L=3 through L=8 is solved; temporal moments use k=0.4 and the hostile k=pi/2"
    )
    print(
        "per_block: exact 13-to-10 fiber reduction, Ward/reflection, source range, Newton residue, coefficient rivalry, and one/two-step Stieltjes gates are composed"
    )
    print(
        "lattice_wide: full temporal-frequency circles are integrated on four carrier sizes, but no full-Z3 phase, nonlinear solved branch, longer-block transfer, or selected Record clock is claimed"
    )
    print(
        "scope_boundary: constructive local source/common-metric action plus a narrow one- and two-slice physical-transfer obstruction; not gravity failure, all-cadence failure, axiom adoption, retention, or TOE closure"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
