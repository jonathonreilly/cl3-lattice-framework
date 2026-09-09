---
claim_id: admissibility_d4_ordered_h1_front_carrier_interface_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "For the supplied C32 representation consisting of eight copies of two inequivalent Pauli sectors, the detector algebra is M2 direct-sum M2 and no all-state full-three-generator sufficient M2 carrier exists; an explicit CPTP M32-to-M4 multiplicity-trace channel intertwines every detector effect and root. A separately supplied enlarged-register, fixed-frame two-event CP protocol has exact sharp cylinders (1/2,0,1/4,1/4) and half-sharp cylinders (5/16,3/16,1/4,1/4). It is not a framework-native one-site M2/Record realization. Its whole-stencil cubic covariance is false for the displayed rotation and remains open; only the carrier representation covariance and fixed-frame protocol survive."
upstream_dependencies:
  - admissibility_d4_affine_lineage_binary_record_multi_join_repeatability_selector_boundary_bounded_theorem_note_2026-08-29
  - admissibility_d4_record_ready_set_successor_state_typing_boundary_bounded_theorem_note_2026-08-29
  - admissibility_d4_h1_static_record_full_conditional_joint_law_curl_boundary_bounded_theorem_note_2026-08-29
runner: scripts/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py
independent_checker: scripts/independent_admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py
status: proposed_retained
actual_current_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Four-level carrier and fixed-frame enlarged-register protocol

**Date:** 2026-08-29
**Corrected:** 2026-09-09
**Type:** `bounded_theorem`
**Standing:** author-side `proposed_retained`; no formal audit has run.

Primary runner:
[`admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py`](../scripts/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py).
Independent checker:
[`independent_admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py`](../scripts/independent_admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py).

## Exact carrier statement

Let

```text
delta_x=diag(sigma_x,sigma_x),
delta_y=diag(sigma_y,-sigma_y),
delta_z=diag(sigma_z,sigma_z),                         (1)
D_i=I_8 tensor delta_i.                                (2)
```

The central volume `i D_x D_y D_z` has two rank-16 eigenspaces. Matrix units
inside the two sectors show that the generated observable algebra is
`M2 direct-sum M2`, each summand with multiplicity eight. A unital CP dual
that mapped one qubit's three Pauli generators to all three `D_i` would put
the generators in its multiplicative domain. It would then be a
star-homomorphism on `M2`, whose central volume is scalar, contradicting the
two nonzero central sectors. This excludes only an all-state, full-family M2
carrier. A single sector, one direction, restricted states, or an M2 plus a
classical sector label are outside the negative.

Explicitly, with `P_s=(I+s iD_xD_yD_z)/2`, the four units in sector `s` are

```text
e^s_00=P_s(I+D_z)/2,       e^s_11=P_s(I-D_z)/2,
e^s_01=P_s(D_x-i sD_y)/2,  e^s_10=(e^s_01)^*.         (3)
```

They obey `e^s_ab e^t_cd=delta_st delta_bc e^s_ad`; each diagonal unit has
rank eight in C32.

Eight Kraus operators `K_m:C32->C4` select the eight multiplicity copies. They
satisfy

```text
sum_m K_m^* K_m=I32,        K_m D_i=delta_i K_m.       (4)
```

Thus `Lambda(rho)=sum_m K_m rho K_m^*` is CPTP and intertwines every effect
and every positive root that is a function of one `D_i`. Exact quarter-turn
and three-cycle generators produce the 24 proper cubic rotations. With the
second Pauli sector carrying the conjugate spinor, every carrier unitary has
the form `I8 tensor V_R`, so (4) intertwines the full supplied carrier
representation. This is the valid carrier-covariance statement; it does not
imply covariance of a spatial stencil with its classical bits.

## Fixed-frame protocol

In the fixed coordinate frame, use masks 17 and 27 for the `+y` and `+x`
detectors. The supplied finite protocol stores an M4 carrier together with a
classical condition bit, epoch, role, arrow, and orthogonal Record labels.
Its one-event quantum maps use the roots from the preceding note, and a
classical bridge copies the first outcome before the second event. For the
maximally mixed M4 input, the exact two-event cylinders in `(00,01,10,11)`
order are

```text
u=1:   (1/2, 0,   1/4, 1/4),
u=1/2: (5/16,3/16,1/4,1/4).                           (5)
```

The quantum maps and displayed classical transitions define a valid finite
CP protocol on this **supplied enlarged register**. They do not define a
framework-native one-site realization: the current physical local algebra is
M2, and non-Record sites have no licensed readable classical fields. A
spatial encoding of the M4 carrier and the auxiliary fields, plus a physical
readout/condition bridge, is an explicit open obligation.

This boundary uses the corrected
[affine-lineage family](ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md),
[ready-set typing theorem](ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md),
and [static curl result](ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md)
only in their stated finite conditional domains.

## Failed whole-stencil covariance

The proper rotation

```text
R = [[0,0,1],[0,-1,0],[1,0,0]]                        (6)
```

fixes mask 17 under pure shell permutation but maps its `+y` detector to
`-y`. The inherited affine bit action instead sends mask 17 to mask 46,
whose detector is `-y`. The old `transformed_world` preserved condition
bits, and `rotate_mask` performed only the shell permutation. Consequently
the fixed-frame branch effect is not intertwined by (6); at `u=1` the M4
effect difference has rank four.

The old runners checked counts and normalization of rotated worlds, not
branch intertwiners. Their claim of whole-stencil cubic covariance is
withdrawn. The fixed-frame protocol and the separate operator-carrier
covariance remain valid. A compatible spatial affine-bit action would need
to be constructed before any covariant physical-front claim.

## Fault controls and boundary

The corrected runners execute three actual operand changes: a rescaled Kraus
operator breaks trace preservation; explicitly resetting the carrier to
`I4/4` between events changes the two-event cylinders; and the
pure-permutation branch under (6) has a rank-four
covariance residual. These are bounded fault controls. They replace the old
unconditional claims that 30 and 24 source mutations had been executed. No
full mutation sweep is claimed.

The result supplies neither a physical register encoding, an autonomous
condition tape, a site/rate law, a clock, an unbounded history, H2, gravity,
an axiom amendment, a formal audit verdict, nor a TOE.

## Reproduction

```bash
python3 scripts/cached_runner_output.py --refresh scripts/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py
python3 scripts/cached_runner_output.py --refresh scripts/independent_admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py
```
