---
claim_id: native_edge_record_reduced_cell_full_isometry_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional exact native reduced-cell Stinespring isometry for both sign outcomes and one capped-battery refusal on the entire eight-dimensional ready-input space, using explicit globally energy-conserving pulses of support at most three. Physical controls, timing and boundary roles remain supplied."
upstream_dependencies:
  - native_edge_record_reduced_cell_control_support_bounded_theorem_note_2026-09-07
  - native_edge_record_finite_collision_apparatus_bounded_theorem_note_2026-09-07
runner: scripts/native_edge_record_reduced_cell_full_isometry_2026_09_07.py
---

# Full native reduced-cell isometry by explicit three-site pulses

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained

Actual current-surface status is conditional-support; independent audit is unset.
The [reduced-cell control test](NATIVE_EDGE_RECORD_REDUCED_CELL_CONTROL_SUPPORT_BOUNDED_THEOREM_NOTE_2026-09-07.md) is extended to every ready-input matter/battery state with exact native outcome amplitudes. The [finite collision apparatus](NATIVE_EDGE_RECORD_FINITE_COLLISION_APPARATUS_BOUNDED_THEOREM_NOTE_2026-09-07.md) motivates the physical coupling gap; this fixed cell is distinct from its full cube.

Nine explicitly supplied coherent pulses realize the complete sign/refusal isometry. A separately derived eight-pulse sequence realizes the same map. Both use globally energy-conserving controls of support at most three on the complete interaction graph. Tensor/Born typing, input preparation, boundary roles, controls and timing remain supplied.

~~~yaml
packet_helper_runner:
  - scripts/native_edge_record_reduced_cell_full_isometry_check_2026_09_07.py
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Two explicit pulse constructions implement the exact native sign/refusal isometry on all ready-input columns; symbolic identities and independent native matrices preserve energy, phases and reference-entangled input scope."
trace_class: upstream_support
target_claim_id: native_edge_record_reduced_cell_control_support_bounded_theorem_note_2026-09-07
target_blocker_text: "Implement the complete native accepted/refusal isometry on its whole declared input space rather than only a selected normalized transition."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Replace the timed pulse sequence by a finite autonomous controller and price its locality, initialization and finite retention window."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

## Fixture and exact target

The active carrier has B_v=Z_x, B_w=-Z_x, A_vw=X_x and real hopping h=Y_x, with active N=1. It is a reduced sector of a native square: old Z12=-1,Z23=+1,Z03=+1 leave edge01 live, with spectator occupations n2=1,n3=0 and full N=2. The nine-register fixture does not include all those physical parent registers; their boundary values are supplied. Register order is r,hv,hw,x,f,b0,b1,l0,l1. The sentinel r remains 0. Head input is 10, fuel input 1, labels 00; all two matter states and all four battery levels are allowed. Battery energy is E_B=1/2+n_b0+2n_b1, cap 4. Conserved K=q(1+Y_x)+E_B, q=n_f. The interaction graph here is complete, not the earlier physical path.

Write p±=(I±Y_x)/2, P±=(I±Z_x)/2, a=1-q, n=n_b1. With T2 the capped raise by two battery levels, the accepted branches are S_z=P_z p+ T2+P_z p-. Their outputs have fuel 0, head 01 and labels +=01 or -=10. The refused output retains fuel 1, head 10 and its original matter/battery state, with label 11.

Since sum_z P_z=I and p+p-=0,

    sum_z S_z†S_z = p- + p+(I-n) = I-F,   F=p+n.

F is a projector, hence the single combined-sign complementary square root is exactly F. Thus the target V has the two S_z branches and the one F branch with their original amplitudes; V†V=I. There is no per-sign refusal completion or normalized selected outcome. Each S_z intertwines source and output K: bright acceptance lowers active energy 2 and raises battery 2; dark acceptance lowers active energy 0; refusal changes neither.

## Explicit nine-pulse construction

Define C(P,l)=exp[-i(pi/2)P(X_l-I)]=(I-P)+PX_l for a commuting projector P. Let E_f,b=|0><1|_f |1><0|_b1+h.c. and E_h=|01><10|_head+h.c. Apply, in this order:

1. C(p+n,l0).
2. C(p+n,l1).
3. exp[-i(pi/2)p+ E_f,b].
4. exp[-i(pi/2)p- X_f].
5. C(a,l1).
6. C(aP-,l0).
7. C(aP-,l1).
8. exp[-i(pi/2)a E_h].
9. exp[-i pi a].

The first two pulses mark bright upper-half refusal. Pulses 3–4 map every accepted branch to fuel 0 with the correct battery shift and common phase -i; refusal is unchanged. Pulses 5–7 copy the physical edge-Z sign coherently to its two-bit label without changing its amplitude. Pulse 8 moves only accepted heads, adding another -i. Pulse 9 cancels that accepted phase -1. Consequently the full ready-input map equals V, including relative phases and interference between initial Y± components.

Every displayed generator is a Hermitian Pauli sum of weight at most 3. All commute globally with K, old Z_r and N_head. In particular the apparently noncommuting edge-Z label controls are multiplied by a: q=0 makes the matter-energy term vanish. For cubic generators H³=H, the pi/2 exponential is I-H²-iH. For the controlled-flip generators H=P(X-I), H²=-2H and the exponential is I+H. These identities prove full unitarity, rather than only normalization on a chosen state.

## Independently derived eight-pulse alternative

The independent sequence is p+ E_f,b; p- X_f; a E_h; aP+ X_l1; aP- X_l0; qX_l0; qX_l1; then I+q, all with duration pi/2. Accepted transport gives -i, head and accepted-label flips give two further -i factors, and the final pulse supplies -i, for total phase 1. Refusal receives two label flips (-1) and the final phase -1, also giving 1. Its ready-input columns therefore realize the same V. This alternative uses the same roles and no extra ancillas. Its helper constructs the compressed native operators from the frozen parent representation; the conditional parent itself is a declared imported dependency.

## Verification and quantifiers

The standalone exact primary expands all nine generators, checks their global commutators and polynomial unitarity, and compares every amplitude of all eight computational matter/battery columns with a separately assembled target. It checks all 64 inner products, energy intertwining, old Record/head constraints, an extra coherent input and adverse sign-phase/refusal changes: 163 actual assertions. All columns match exactly in rational complex arithmetic. Full sparse columns and canonical hashes are emitted. No full dense 512-unitary is needed.

All-column equality is linear, so it covers arbitrary mixed source matter/battery inputs and arbitrary reference entanglement, including correlated matter/battery states within the eight-dimensional ready-input space. This is stronger than the earlier fixed-input state transfer. The pulse product is an energy-preserving unitary extension of V; it is not asserted to equal the previous small-angle collision-star unitary on arbitrary initially non-ready labels. The independent eight-pulse helper performs 62 named matrix assertions using actual 256-dimensional operators with the unchanged old sentinel factored out. Every unrounded complex entry of all eight columns is checked. Its result agrees with the separate exact primary columns within 1.16e-16 after the disclosed physical-bit permutation. Its output-only 14-digit rounding does not enter any assertion. Both canonical runners pass unchanged 180-second and 180-MiB limits and emit source/dependency hashes.

The resource statement is nine reduced qubits, no additional ancillas, nine explicit supplied pulses for the exact primary, and an eight-pulse alternative. It excludes physical controller/clock, bath/renewal, preparation, native parent boundary storage and nearest-neighbor synthesis. New labels remain coherent workspace until supplied decoupling/readout; their permanent formation is not derived. No full-cube transport success, axiomatic interaction primitive or generic higher-dimensional controllability follows.
