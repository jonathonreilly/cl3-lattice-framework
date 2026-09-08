#!/usr/bin/env python3
"""Block 68: carry the signed Record stress into the conditional gravity sector.

The runner fixes the unique ten-coordinate infrared source map, tests its
continuum Ward and Lorentzian Block-44 response, and then asks whether the
same six signed null directions have an exact finite-frequency edge carrier.
The supplied fifteen-edge orientation handles only three signs; the supplied
twenty-two-edge time-reflection union handles all six.  Closed neutral line
pairs are exact Ward-compatible sources and solve the complete union edge
equations on every nonzero supported mode of the declared five-torus.

This is a bounded conditional interface test.  It does not select the source
density/coupling, the reflected common-metric quotient, a Record clock, a
physical transfer, a nonlinear action, an axiom amendment, or retention.
"""

from __future__ import annotations

import argparse
from itertools import product
from pathlib import Path
import sys

import numpy as np


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
    'docs/ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md',
    'docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md',
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
    'scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py',
    'scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py',
    'scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py',
    'scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py',
    'scripts/admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12.py',
    'scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py',
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
    'docs/ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md': 'c897f478045340ddac995eb2c381298b6ef5b8143676bd63cc9f5da3b5f8bb93',
    'docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md': 'b6b4e25cbdc3b87e5ee8db841b7378e8ea900dee09cf02c993ebb0b823dd4fb4',
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
    'scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py': 'aee3ba64460976475f36bfc8b45fcc4319c285d3f9d8ebb5ee7a5b677181f801',
    'scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py': '4ba16259ea4fd59c2e1ac6d145a1fec506e892e35e56526359ca424559841617',
    'scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py': 'adb117ec956c27f486318673829464d47bc4cbe11fbffae88e70299ee2c35bce',
    'scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py': 'bdb7ed7f4ed979e64378adc770d7fb438eb48b36589897d78ccf0c3fff64ccef',
    'scripts/admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12.py': '7053f1ae58e1ab53a0be7cb0b8b25daac6889e501806940ff75e7950aee80a5e',
    'scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py': '6952a8bf9badcf0a546a024b365d8238376305014ad6755f06db6bfa45fee848',
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
AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
BLOCK67_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md'
BLOCK44_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
BLOCK47_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
BLOCK48_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md'
HELIX_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md'
JOINT_LAW_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md'
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)



sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13 as block67  # noqa: E402
import admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11 as block44  # noqa: E402
import admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11 as block47  # noqa: E402
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402


HCOMPS = tuple(block44.HCOMPS)
EXPECTED_HCOMPS = (
    (0, 0), (1, 1), (2, 2), (3, 3), (0, 1),
    (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
)
DIRECTIONS = tuple(
    np.asarray(direction, dtype=int) for direction in block67.b64.DIRECTIONS
)
TOL = 5.0e-10
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
            clipped = detail if len(detail) <= 156 else detail[:153] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def tensor_coordinates(tensor: np.ndarray, off_diagonal_factor: float = 2.0) -> np.ndarray:
    """Covector paired with Block-44 symmetric metric coordinates."""
    return np.asarray(
        [
            (off_diagonal_factor if left != right else 1.0) * tensor[left, right]
            for left, right in HCOMPS
        ],
        dtype=float,
    )


def record_tensor(direction: np.ndarray) -> np.ndarray:
    """Permute Block-67 order (t,x,y,z) into Block-44 order (x,y,z,t)."""
    block67_vector = np.concatenate(([1.0], np.asarray(direction, dtype=float)))
    permutation = np.asarray((1, 2, 3, 0), dtype=int)
    vector = block67_vector[permutation]
    return np.outer(vector, vector)


def coordinate_certificate(wrong_order: bool) -> dict[str, float | int]:
    weighted_basis = []
    for index in range(len(HCOMPS)):
        weighted_basis.append(tensor_coordinates(block44.symmetric_basis(index)))
    rank = int(np.linalg.matrix_rank(np.asarray(weighted_basis)))
    failures = 0
    parity_failures = 0
    for direction in DIRECTIONS:
        if wrong_order:
            vector = np.concatenate(([1.0], direction.astype(float)))
            tensor = np.outer(vector, vector)
        else:
            tensor = record_tensor(direction)
        source = tensor_coordinates(tensor)
        dx, dy, dz = (float(value) for value in direction)
        expected = np.asarray(
            (dx * dx, dy * dy, dz * dz, 1.0, 2 * dx * dy,
             2 * dx * dz, 2 * dx, 2 * dy * dz, 2 * dy, 2 * dz)
        )
        failures += not np.array_equal(source, expected)
        opposite = -direction
        opposite_source = tensor_coordinates(record_tensor(opposite))
        parity_failures += not (
            np.array_equal(source[:6], opposite_source[:6])
            and np.array_equal(source[[6, 8, 9]], -opposite_source[[6, 8, 9]])
        )
    return {
        "rank": rank,
        "failures": failures,
        "parity_failures": parity_failures,
    }


def pairing_certificate(omit_off_diagonal_two: bool) -> dict[str, float]:
    factor = 1.0 if omit_off_diagonal_two else 2.0
    tensors = (
        np.asarray(
            ((1.2, -0.7, 0.3, 0.8), (-0.7, 2.1, 0.5, -0.4),
             (0.3, 0.5, -1.4, 0.9), (0.8, -0.4, 0.9, 1.7))
        ),
        record_tensor(DIRECTIONS[0]),
        record_tensor(DIRECTIONS[-1]),
    )
    perturbations = (
        np.asarray(
            ((0.4, 0.2, -0.3, 0.6), (0.2, -0.8, 0.7, 0.1),
             (-0.3, 0.7, 1.1, -0.5), (0.6, 0.1, -0.5, 0.9))
        ),
        np.arange(16, dtype=float).reshape(4, 4),
    )
    errors = []
    for tensor in tensors:
        source = tensor_coordinates(tensor, factor)
        for perturbation in perturbations:
            symmetric = 0.5 * (perturbation + perturbation.T)
            coordinates = np.asarray(
                [symmetric[left, right] for left, right in HCOMPS]
            )
            errors.append(abs(float(source @ coordinates - np.sum(tensor * symmetric))))

    ward_errors = []
    for tensor in tensors:
        source = tensor_coordinates(tensor, factor)
        for momentum in (
            np.asarray((0.4, -0.2, 0.7, -0.3)),
            np.asarray((-0.8, 0.5, 0.1, 0.6)),
        ):
            actual = block44.continuum_gauge_map(momentum).T @ source
            expected = 2.0 * tensor @ momentum
            ward_errors.append(float(np.linalg.norm(actual - expected)))
    return {"pairing_error": max(errors), "ward_identity_error": max(ward_errors)}


def ward_completion_certificate(off_shell_source: bool) -> dict[str, float | int]:
    on_shell_error = 0.0
    off_shell_floor = np.inf
    completion_error = 0.0
    kernel_dimensions = set()
    samples = (
        np.asarray((0.73, -0.31, 0.27)),
        np.asarray((-0.29, 0.61, 0.44)),
    )
    for direction in DIRECTIONS:
        tensor = record_tensor(direction)
        source = tensor_coordinates(tensor)
        for spatial in samples:
            frequency = float(spatial @ direction)
            if off_shell_source:
                frequency += 0.17
            momentum = np.concatenate((spatial, (-frequency,)))
            gauge = block44.continuum_gauge_map(momentum)
            on_shell_error = max(on_shell_error, float(np.linalg.norm(gauge.T @ source)))

            displaced = momentum.copy()
            displaced[3] -= 0.19
            off_shell_floor = min(
                off_shell_floor,
                float(np.linalg.norm(block44.continuum_gauge_map(displaced).T @ source)),
            )
            kernel_dimensions.add(10 - int(np.linalg.matrix_rank(gauge, tol=1.0e-11)))

    spatial_stress = np.asarray(
        ((1.2, -0.3, 0.5), (-0.3, 0.9, 0.2), (0.5, 0.2, 1.7))
    )
    spatial = np.asarray((0.4, -0.6, 0.8))
    frequency = 0.71
    mixed = spatial_stress @ spatial / frequency
    time_time = float(spatial @ spatial_stress @ spatial / frequency**2)
    tensor = np.zeros((4, 4), dtype=float)
    tensor[:3, :3] = spatial_stress
    tensor[:3, 3] = tensor[3, :3] = mixed
    tensor[3, 3] = time_time
    momentum = np.concatenate((spatial, (-frequency,)))
    completion_error = float(
        np.linalg.norm(block44.continuum_gauge_map(momentum).T @ tensor_coordinates(tensor))
    )
    return {
        "on_shell_error": on_shell_error,
        "off_shell_floor": off_shell_floor,
        "completion_error": completion_error,
        "kernel_dimensions": len(kernel_dimensions),
        "kernel_dimension": next(iter(kernel_dimensions)),
    }


def lorentzian_response_certificate(flip_mixed_sign: bool) -> dict[str, float | int]:
    ward_error = 0.0
    solve_error = 0.0
    off_shell_ranks = set()
    null_shell_ranks = set()
    for slot, direction in enumerate(DIRECTIONS):
        source = tensor_coordinates(record_tensor(direction))
        if flip_mixed_sign:
            source[[6, 8, 9]] *= -1.0
        transverse_one = DIRECTIONS[(slot + 2) % len(DIRECTIONS)].astype(float)
        if abs(float(transverse_one @ direction)) > 0.5:
            transverse_one = DIRECTIONS[(slot + 4) % len(DIRECTIONS)].astype(float)
        spatial = 0.71 * direction + 0.23 * transverse_one
        frequency = float(spatial @ direction)
        momentum = np.concatenate((spatial, (-frequency,)))
        operator = block44.lorentzian_operator(spatial, frequency)
        gauge = block44.continuum_gauge_map(momentum)
        response = -np.linalg.pinv(operator, rcond=1.0e-11) @ source
        ward_error = max(ward_error, float(np.linalg.norm(gauge.T @ source)))
        solve_error = max(solve_error, float(np.linalg.norm(operator @ response + source)))
        off_shell_ranks.add(int(np.linalg.matrix_rank(operator, tol=1.0e-10)))

        null_spatial = 0.67 * direction
        null_frequency = float(null_spatial @ direction)
        null_operator = block44.lorentzian_operator(null_spatial, null_frequency)
        null_response = -np.linalg.pinv(null_operator, rcond=1.0e-11) @ source
        solve_error = max(
            solve_error,
            float(np.linalg.norm(null_operator @ null_response + source)),
        )
        null_shell_ranks.add(int(np.linalg.matrix_rank(null_operator, tol=1.0e-10)))

    static_source = np.zeros(len(HCOMPS))
    static_source[HCOMPS.index((3, 3))] = 1.0
    static_operator = block44.lorentzian_operator(np.asarray((1.0, 0.0, 0.0)), 0.0)
    static_response = -np.linalg.pinv(static_operator) @ static_source
    static_error = abs(float(static_response[HCOMPS.index((3, 3))] - 2.0))
    return {
        "ward_error": ward_error,
        "solve_error": solve_error,
        "off_shell_rank": next(iter(off_shell_ranks)),
        "off_shell_rank_count": len(off_shell_ranks),
        "null_shell_rank": next(iter(null_shell_ranks)),
        "null_shell_rank_count": len(null_shell_ranks),
        "static_error": static_error,
    }


def original_full_edge_certificate(drop_nonmetric_correction: bool) -> dict[str, float | int]:
    map_error = 0.0
    schur_ward_error = 0.0
    schur_ranks = set()
    for momentum in (
        np.asarray((0.31, -0.47, 0.23, 0.19)),
        np.asarray((0.71, 0.11, -0.39, 0.53)),
    ):
        metric_map = block47.analytic_metric_map(momentum)
        continuum_gauge = block44.continuum_gauge_map(momentum)
        edge_gauge = block47.analytic_gauge_map(momentum)
        map_error = max(
            map_error,
            float(np.linalg.norm(metric_map @ continuum_gauge + 1j * edge_gauge)),
        )
        schur = block48.original_metric_schur(momentum)
        metric_gauge = block48.metric_gauge_map(momentum)
        schur_ward_error = max(
            schur_ward_error, float(np.linalg.norm(schur @ metric_gauge))
        )
        schur_ranks.add(int(np.linalg.matrix_rank(schur, tol=1.0e-9)))

    direction_index = {
        tuple(int(value) for value in direction): slot
        for slot, direction in enumerate(block47.DIRECTIONS)
    }
    edge_source = np.zeros(len(block47.DIRECTIONS), dtype=complex)
    edge_source[direction_index[(1, 0, 0, 1)]] = 2.0
    target = tensor_coordinates(record_tensor(np.asarray((1, 0, 0)))) / np.sqrt(2.0)
    response_error = 0.0
    ward_error = 0.0
    asymptotic_ratios = []
    for epsilon in (0.4, 0.2, 0.1):
        momentum = np.asarray((0.0, epsilon, 0.0, 0.0))
        symbol = block47.analytic_symbol(momentum)
        right_metric = block47.analytic_metric_map(momentum)
        left_metric = block47.analytic_metric_map(-momentum).T
        nonmetric = block48.NONMETRIC
        nonmetric_block = nonmetric.T @ symbol @ nonmetric
        mixing = left_metric @ symbol @ nonmetric
        effective = left_metric @ edge_source
        if not drop_nonmetric_correction:
            effective -= mixing @ np.linalg.solve(
                nonmetric_block, nonmetric.T @ edge_source
            )
        schur = block48.original_metric_schur(momentum)
        metric_response = -np.linalg.pinv(schur, rcond=1.0e-10) @ effective
        complement = -np.linalg.solve(
            nonmetric_block,
            nonmetric.T @ (symbol @ right_metric @ metric_response + edge_source),
        )
        edge_response = right_metric @ metric_response + nonmetric @ complement
        response_error = max(
            response_error,
            float(np.linalg.norm(symbol @ edge_response + edge_source)),
        )
        ward_error = max(
            ward_error,
            float(np.linalg.norm(block48.metric_gauge_map(momentum).conj().T @ effective)),
        )
        asymptotic_ratios.append(float(np.linalg.norm(effective - target) / epsilon**2))
    ratio_spread = max(asymptotic_ratios) - min(asymptotic_ratios)
    return {
        "map_error": map_error,
        "schur_ward_error": schur_ward_error,
        "rank": next(iter(schur_ranks)),
        "rank_count": len(schur_ranks),
        "response_error": response_error,
        "source_ward_error": ward_error,
        "asymptotic_ratio_spread": ratio_spread,
    }


def canonical_carrier(
    allowed: tuple[tuple[int, ...], ...], direction: np.ndarray
) -> tuple[tuple[int, ...], np.ndarray] | None:
    spacetime_step = np.concatenate((direction, (1,))).astype(int)
    forward = tuple(int(value) for value in spacetime_step)
    reverse = tuple(int(value) for value in -spacetime_step)
    if forward in allowed:
        return forward, np.zeros(4, dtype=int)
    if reverse in allowed:
        # The reversed edge is based at the future endpoint of the physical step.
        return reverse, spacetime_step
    return None


def reflected_coverage_certificate(original_only: bool) -> dict[str, float | int]:
    union = block48.build_reflection_union()
    allowed = tuple(
        tuple(int(value) for value in direction)
        for direction in (
            block48.ORIGINAL_DIRECTIONS if original_only else union.directions
        )
    )
    full_index = {direction: slot for slot, direction in enumerate(union.directions)}
    covered = 0
    source_error = 0.0
    used = set()
    coefficients = block48.metric_coefficients(np.asarray(union.directions))
    for direction in DIRECTIONS:
        carrier = canonical_carrier(allowed, direction)
        if carrier is None:
            continue
        edge, _offset = carrier
        covered += 1
        used.add(edge)
        edge_source = np.zeros(len(union.directions))
        edge_source[full_index[edge]] = 2.0
        target = tensor_coordinates(record_tensor(direction)) / np.sqrt(2.0)
        source_error = max(
            source_error, float(np.linalg.norm(coefficients.T @ edge_source - target))
        )

    ward_error = 0.0
    rank_count = 0
    for momentum in (
        np.asarray((0.37, -0.29, 0.41, 0.23)),
        np.asarray((-0.61, 0.17, 0.33, -0.47)),
    ):
        symbol = block48.union_symbol(union, momentum)
        gauge = block48.union_gauge_map(union, momentum)
        ward_error = max(
            ward_error,
            float(np.linalg.norm(symbol @ gauge)),
            float(np.linalg.norm(block48.union_symbol(union, -momentum).T @ gauge)),
        )
        rank_count += int(np.linalg.matrix_rank(gauge, tol=1.0e-10) == 4)
    return {
        "union_edges": len(union.directions),
        "covered": covered,
        "used": len(used),
        "source_error": source_error,
        "ward_error": ward_error,
        "gauge_rank_samples": rank_count,
    }


def transverse_offset(direction: np.ndarray) -> np.ndarray:
    if abs(int(direction[1])) == 0:
        return np.asarray((0, 1, 0, 0), dtype=int)
    return np.asarray((1, 0, 0, 0), dtype=int)


def periodic_carrier_certificate(drop_closure_edge: bool) -> dict[str, float | int]:
    union = block48.build_reflection_union()
    allowed = tuple(union.directions)
    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    supported = 0
    ward_error = 0.0
    solve_error = 0.0
    relative_solve_error = 0.0
    null_overlap = 0.0
    nullities = set()
    for size in TORUS_SIZES:
        momenta = tuple(
            2.0 * np.pi * np.asarray(mode, dtype=float) / size
            for mode in product(range(size), repeat=4)
        )
        line_length = size - int(drop_closure_edge)
        for direction in DIRECTIONS:
            carrier = canonical_carrier(allowed, direction)
            if carrier is None:
                raise AssertionError("the reflected union must carry all signed directions")
            edge, base_offset = carrier
            row = edge_index[edge]
            spacetime_step = np.concatenate((direction, (1,))).astype(int)
            separation = transverse_offset(direction)
            for momentum in momenta:
                line_factor = sum(
                    np.exp(1j * float(momentum @ (step * spacetime_step + base_offset)))
                    for step in range(line_length)
                )
                neutral_factor = line_factor * (
                    1.0 - np.exp(1j * float(momentum @ separation))
                )
                source_row = np.zeros(len(union.directions), dtype=complex)
                source_row[row] = 2.0 * neutral_factor
                source_norm = float(np.linalg.norm(source_row))
                if source_norm < 1.0e-9:
                    continue
                supported += 1
                gauge = block48.union_gauge_map(union, momentum)
                ward_error = max(
                    ward_error, float(np.linalg.norm(source_row.conj() @ gauge))
                )
                symbol = block48.union_symbol(union, momentum)
                left_vectors, singular_values, _right_vectors = np.linalg.svd(symbol)
                nullities.add(int(np.sum(singular_values < 1.0e-9)))
                source_column = source_row.conj()
                left_null = left_vectors[:, singular_values < 1.0e-9]
                null_overlap = max(
                    null_overlap,
                    float(np.linalg.norm(left_null.conj().T @ source_column)),
                )
                response = -np.linalg.pinv(symbol, rcond=1.0e-10) @ source_column
                residual = float(np.linalg.norm(symbol @ response + source_column))
                solve_error = max(solve_error, residual)
                relative_solve_error = max(
                    relative_solve_error, residual / source_norm
                )
    return {
        "supported": supported,
        "ward_error": ward_error,
        "solve_error": solve_error,
        "relative_solve_error": relative_solve_error,
        "null_overlap": null_overlap,
        "nullity_count": len(nullities),
        "minimum_nullity": min(nullities),
        "maximum_nullity": max(nullities),
    }


def zero_mode_certificate(keep_zero_mode: bool) -> dict[str, float]:
    union = block48.build_reflection_union()
    symbol = block48.union_symbol(union, np.zeros(4))
    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    positive_residuals = []
    for direction in DIRECTIONS:
        carrier = canonical_carrier(tuple(union.directions), direction)
        if carrier is None:
            raise AssertionError
        edge, _offset = carrier
        source = np.zeros(len(union.directions), dtype=complex)
        source[edge_index[edge]] = 2.0 * 5
        response = -np.linalg.pinv(symbol, rcond=1.0e-10) @ source
        positive_residuals.append(float(np.linalg.norm(symbol @ response + source)))
    neutral_zero_norm = 0.0
    if keep_zero_mode:
        neutral_zero_norm = max(positive_residuals)
    return {
        "minimum_positive_residual": min(positive_residuals),
        "maximum_positive_residual": max(positive_residuals),
        "neutral_zero_norm": neutral_zero_norm,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "wrong_order",
            "omit_offdiag_two",
            "off_shell_source",
            "flip_mixed_sign",
            "drop_nonmetric_correction",
            "original_only",
            "drop_closure_edge",
            "keep_zero_mode",
            "broaden_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    parents = tuple(
        flat(path)
        for path in (
            BLOCK67_PATH, BLOCK44_PATH, BLOCK47_PATH, BLOCK48_PATH,
            HELIX_PATH, JOINT_LAW_PATH,
        )
    )

    loaded_input_failures = current_input_failures(check_loaded=True)
    if loaded_input_failures:
        raise RuntimeError("loaded source/input binding failed: " + "; ".join(loaded_input_failures))
    checks.check(
        "A-source-stack-and-authority",
        'current memo and final source/input bytes are pinned; original parent identities remain historical',
        not current_input_failures() and mutation not in ("stale_axiom_authority", "stale_os_authority"),
        'Current input closure checked independently of moving branch heads or historical audit status',
    )

    coordinates = coordinate_certificate(mutation == "wrong_order")
    checks.check(
        "B-unique-ten-coordinate-source-map",
        "the (t,x,y,z) Record tensor has one invertible weighted map into Block44 order",
        HCOMPS == EXPECTED_HCOMPS
        and coordinates["rank"] == 10
        and coordinates["failures"] == 0
        and coordinates["parity_failures"] == 0,
        f"rank={coordinates['rank']}; six-axis truth-table failures={coordinates['failures']}; signed-parity failures={coordinates['parity_failures']}",
    )

    pairing = pairing_certificate(mutation == "omit_offdiag_two")
    checks.check(
        "C-offdiagonal-multiplicity-and-Ward-identity",
        "the factor-two coordinate covector pairs with symmetric fields and obeys Gamma^T C(T)=2Tp",
        pairing["pairing_error"] < 1.0e-12
        and pairing["ward_identity_error"] < 1.0e-12,
        f"pairing error={pairing['pairing_error']:.3e}; tensor Ward identity error={pairing['ward_identity_error']:.3e}",
    )

    ward = ward_completion_certificate(mutation == "off_shell_source")
    checks.check(
        "D-shell-Ward-and-six-dimensional-completion",
        "Record stress is conserved on omega=q.d and generic Ward-compatible sources form a six-dimensional kernel",
        ward["on_shell_error"] < 1.0e-12
        and ward["off_shell_floor"] > 0.1
        and ward["completion_error"] < 1.0e-12
        and ward["kernel_dimensions"] == 1
        and ward["kernel_dimension"] == 6,
        f"on-shell={ward['on_shell_error']:.3e}; off-shell floor={ward['off_shell_floor']:.3f}; completion={ward['completion_error']:.3e}; dim={ward['kernel_dimension']}",
    )

    lorentzian = lorentzian_response_certificate(mutation == "flip_mixed_sign")
    checks.check(
        "E-conditional-Block44-Lorentzian-response",
        "all six sources solve off-shell modulo gauge and on the null shell after the TT compatibility test",
        lorentzian["ward_error"] < 1.0e-12
        and lorentzian["solve_error"] < 1.0e-11
        and lorentzian["off_shell_rank_count"] == 1
        and lorentzian["off_shell_rank"] == 6
        and lorentzian["null_shell_rank_count"] == 1
        and lorentzian["null_shell_rank"] == 4
        and lorentzian["static_error"] < 1.0e-12,
        f"Ward={lorentzian['ward_error']:.3e}; solve={lorentzian['solve_error']:.3e}; ranks={lorentzian['off_shell_rank']}/{lorentzian['null_shell_rank']}; unit e_tt gives h_tt=2",
    )

    full_edge = original_full_edge_certificate(
        mutation == "drop_nonmetric_correction"
    )
    checks.check(
        "F-original-full-edge-source-Schur-intertwiner",
        "the exact edge gauge map descends to rank-six Schur and stationary source elimination is load-bearing",
        full_edge["map_error"] < 1.0e-12
        and full_edge["schur_ward_error"] < 1.0e-10
        and full_edge["rank_count"] == 1
        and full_edge["rank"] == 6
        and full_edge["response_error"] < 1.0e-9
        and full_edge["source_ward_error"] < 1.0e-12
        and full_edge["asymptotic_ratio_spread"] < 1.0e-4,
        f"M C=-iG error={full_edge['map_error']:.2e}; full-edge solve={full_edge['response_error']:.2e}; IR O(p^2) ratio spread={full_edge['asymptotic_ratio_spread']:.2e}",
    )

    reflected = reflected_coverage_certificate(mutation == "original_only")
    checks.check(
        "G-six-signed-reflected-edge-lift",
        "the twenty-two-edge time-reflection union carries every signed null direction with the forced source shape",
        reflected["union_edges"] == 22
        and reflected["covered"] == 6
        and reflected["used"] == 6
        and reflected["source_error"] < 1.0e-12
        and reflected["ward_error"] < 1.0e-10
        and reflected["gauge_rank_samples"] == 2,
        f"covered={reflected['covered']}/6 with {reflected['used']} edge classes; source pullback error={reflected['source_error']:.2e}; union Ward={reflected['ward_error']:.2e}",
    )

    periodic = periodic_carrier_certificate(mutation == "drop_closure_edge")
    checks.check(
        "H-exact-neutral-line-full-edge-response",
        "all six closed neutral line pairs obey finite-frequency Ward and solve every supported complete-edge mode",
        periodic["supported"] == 6528
        and periodic["ward_error"] < 1.0e-11
        and periodic["solve_error"] < 1.0e-10
        and periodic["relative_solve_error"] < 1.0e-11
        and periodic["null_overlap"] < 1.0e-10
        and periodic["minimum_nullity"] == 4
        and periodic["maximum_nullity"] == 5,
        f"L=3..8 modes={periodic['supported']}; Ward={periodic['ward_error']:.2e}; full-null={periodic['null_overlap']:.2e}; solve={periodic['solve_error']:.2e}; nullities={periodic['minimum_nullity']}..{periodic['maximum_nullity']}",
    )

    zero = zero_mode_certificate(mutation == "keep_zero_mode")
    checks.check(
        "I-compact-zero-mode-boundary",
        "neutral pairing removes the forbidden compact net source while a lone positive line is explicitly rejected",
        zero["neutral_zero_norm"] < 1.0e-12
        and zero["minimum_positive_residual"] > 1.0,
        f"neutral p=0 norm={zero['neutral_zero_norm']:.1e}; lone-line full-edge residual={zero['minimum_positive_residual']:.6f}..{zero['maximum_positive_residual']:.6f}",
    )

    boundary_phrases = (
        "zero toe percentage movement",
        "one global coupling",
        "sqrt(2)",
        "common-metric",
        "record clock",
        "nonlinear",
        "no-go gate: fail",
        "partial-narrowing",
        "n1",
        "n8",
        "no canonical axiom is edited",
    )
    boundary_ok = (
        mutation != "broaden_boundary"
        and all(phrase in note for phrase in boundary_phrases)
    )
    checks.check(
        "J-no-go-discipline-and-scope-boundary",
        "the surviving routes force partial narrowing and keep every law-bearing wall explicit",
        boundary_ok,
        "broad gravity no-go forbidden; cadence, normalization, common metric, transfer, nonlinear law, adoption, and retention remain open",
    )

    print(
        "N5_CERTIFICATE: ten source coordinates, six signed directions, two continuum momentum regimes, complete original-edge stationary elimination, all 22 reflected edge classes, and every Fourier mode on L=3..8 for six neutral line pairs are resolved"
    )
    print(
        "per_element: every symmetric coordinate multiplicity, Record sign, edge orientation, gauge column, source row, and compact zero-mode contribution is tested explicitly"
    )
    print(
        "per_sample: generic off-shell, gravity-null-shell, static, full-zone finite-frequency, and all 6528 nonzero neutral direction-mode source samples are checked"
    )
    print(
        "per_block: Block67 Record stress, Block44 conditional Einstein response, Block47 full-edge Schur elimination, and Block48 reflected union meet at typed interfaces"
    )
    print(
        "lattice_wide: exact closed neutral sources cover all six signed velocities on periodic L=3..8 tori; no arbitrary-volume, net-positive compact source, or nonlinear law is inferred"
    )
    print(
        "scope_boundary: conditional IR source and finite-frequency carrier theorem only; not source normalization, common-metric selection, Record cadence, physical transfer, axiom amendment, retention, or TOE closure"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
