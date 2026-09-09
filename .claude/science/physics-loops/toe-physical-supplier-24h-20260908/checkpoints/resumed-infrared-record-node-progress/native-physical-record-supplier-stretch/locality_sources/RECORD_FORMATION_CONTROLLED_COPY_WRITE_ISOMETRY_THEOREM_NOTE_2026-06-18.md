# Record Formation Controlled-Copy Write-Isometry Theorem

**Date:** 2026-06-18
**Type:** exact support theorem
**Claim type:** bounded_theorem
**Status:** exact support; source-side bridge only.
**Primary runner:**
[`scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py`](../scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py)
**Generated output:**
[`outputs/record_formation_controlled_copy_write_isometry_2026_06_18.json`](../outputs/record_formation_controlled_copy_write_isometry_2026_06_18.json)

## Claim

In the explicit finite pointer-record model of
[`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md),
the nonzero controlled-copy kick on a fresh blank fragment derives the
projective record-write isometry used by the target bridge
`RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`.

Let the system pointer projectors be

```text
P_0 = |0><0|,  P_1 = |1><1|,
P_0 + P_1 = I.
```

Let the fresh record fragment start in `|0>_R`, and let

```text
U_cc(theta) = exp(-i theta sigma_z(S) tensor sigma_x(R)),
theta = pi/4.
```

Then

```text
U_cc(pi/4)(|psi> tensor |0>_R)
  = P_0|psi> tensor |eta_0> + P_1|psi> tensor |eta_1>,
```

where

```text
|eta_0> = exp(-i pi sigma_x/4)|0>,
|eta_1> = exp(+i pi sigma_x/4)|0>,
<eta_0|eta_1> = 0.
```

Thus the controlled-copy dynamics itself supplies orthogonal record labels.
After the fixed record-register calibration sending `|eta_r>` to the canonical
label `|r>`, the induced isometry is exactly

```text
W|psi> = P_0|psi> tensor |0> + P_1|psi> tensor |1>.
```

Consequently the extracted record blocks are the projectors:

```text
K_r = <r|W = P_r.
```

This is the missing source-side bridge from the controlled-copy/fresh-fragment
dynamics to the ideal pointer-label write used by the finite Kraus bridge.

## Cited Authority Surface

- [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  supplies the explicit finite `S + E_1..E_n` controlled-copy construction,
  the recording time `t = pi/(4g)`, and the fresh/idle fragment persistence
  condition under its bounded quantum-Darwinism record reading.
- `RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md` is the target
  bridge whose finite projective write to Kraus/CPTP algebra this theorem now
  feeds.
- `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md` supplies the
  finite normalized-isometry to Kraus-instrument algebra downstream of this
  theorem's write isometry (downstream-consumer pointer, not a
  citation-graph dependency; 2026-07-13 cycle-break demotion).

## Proof

Since `sigma_z` has eigenprojectors `P_0` and `P_1`,

```text
U_cc(theta)
  = P_0 tensor exp(-i theta sigma_x)
    + P_1 tensor exp(+i theta sigma_x).
```

For `theta = pi/4`, define

```text
|eta_0> = exp(-i pi sigma_x/4)|0>,
|eta_1> = exp(+i pi sigma_x/4)|0>.
```

Their overlap is

```text
<eta_0|eta_1>
  = <0| exp(+i pi sigma_x/4) exp(+i pi sigma_x/4) |0>
  = <0| exp(+i pi sigma_x/2) |0>
  = cos(pi/2)
  = 0.
```

Therefore the single-fragment controlled-copy kick maps any system vector
`|psi>` to an orthogonal pointer-label superposition:

```text
U_cc(pi/4)(|psi> tensor |0>)
  = P_0|psi> tensor |eta_0> + P_1|psi> tensor |eta_1>.
```

Let `C_R` be the fixed record-basis calibration with rows
`<eta_0|` and `<eta_1|`. Then

```text
(I tensor C_R) U_cc(pi/4)(|psi> tensor |0>)
  = P_0|psi> tensor |0> + P_1|psi> tensor |1>.
```

This is exactly the ideal write-isometry `W` used by the finite Kraus bridge,
up to the harmless ordering convention between `system tensor record` and
`record tensor system`.

The fresh-fragment chain statement follows because a later controlled-copy
kick acts on `S tensor E_k` for a new fragment `E_k` and is the identity on
the completed fragment's register. Hence it commutes with every projector onto
the completed fragment's label subspace, so the earlier label remains idle and
available for repeat read while later fragments record.

## What This Closes

This note supplies the missing source-side theorem requested by the conditional
audit of `record_formation_to_kraus_isometry_bridge_2026-06-06`: the ideal
pointer-label record-write isometry is no longer an extra premise inside the
explicit controlled-copy/fresh-fragment finite model. It is the calibrated
isometry induced by the controlled-copy kick at `t = pi/(4g)`.

Independent audit still decides whether this repair moves the existing row.
This note does not edit any audit ledger, queue, publication effective-status
file, or front-door status surface.

## What This Does Not Close

This note does not claim:

- an arbitrary persistent dynamics to `W` theorem;
- a derivation of the quantum-Darwinism record reading from the minimal
  axioms;
- a physical Hamiltonian, action, coupling, clock, rate, or beta value;
- a Born rule or probability law from post-record counts;
- a generation, Koide dial, or other downstream selector;
- any audit verdict.

The result is exact support for the explicit finite controlled-copy model only.

## Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: closes_source_side_blocker
conditional_surface_status: bounded-support for the explicit finite
  controlled-copy/fresh-fragment record model
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This derives the ideal write isometry only inside the explicit finite controlled-copy model; independent audit is still required."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Verification

```text
python3 scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
