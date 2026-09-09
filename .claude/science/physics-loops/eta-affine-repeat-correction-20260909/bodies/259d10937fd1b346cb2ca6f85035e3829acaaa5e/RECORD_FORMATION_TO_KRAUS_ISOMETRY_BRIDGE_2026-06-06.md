# Record Formation to Kraus Isometry Bridge

**Date:** 2026-06-06
**Type:** bounded bridge theorem
**Claim type:** bounded_theorem
**Status:** exact-support branch-local, conditional on the finite pointer-record
model premises listed below; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py`](../scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.txt`](../logs/runner-cache/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.txt)

## Claim

The earlier finite Kraus note proves the following algebra:

```text
normalized record-writing isometry W
  => extracted blocks K_r form a Kraus/CPTP instrument.
```

It deliberately leaves open the harder bridge:

```text
persistent record dynamics
  => normalized record-writing isometry W.
```

This note supplies a narrow bridge for the explicit finite pointer model used
in
[`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md).
The missing source-side ideal-write step is now supplied by
[`RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`](RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md):
inside the same explicit controlled-copy/fresh-fragment model, the
controlled-copy kick at `t = pi/(4g)` induces the ideal pointer-label
record-write isometry after a fixed record-register basis calibration.

Condition on:

- a finite system Hilbert space `H_sys`;
- a pointer observable with finite spectral projectors `{P_r}` satisfying
  `P_r P_s = delta_rs P_r`, `P_r^dagger = P_r`, and `sum_r P_r = I`;
- the finite pointer-non-demolition record-formation bridge, so the pointer
  sectors are stable record sectors in the model;
- a blank finite record register `H_record` initialized as a fresh fragment;
- the controlled-copy/fresh-fragment write-isometry theorem, which derives the
  ideal pointer-label write from the controlled-copy kick rather than leaving
  it as an unqualified premise.

Define

```text
W |psi> = sum_r (P_r |psi>) tensor |r>.
```

Then:

1. `W` is a normalized isometry: `W^dagger W = I`.
2. The extracted blocks are exactly projective Kraus operators:
   `K_r = <r| W = P_r`.
3. The unconditional post-record update is the pointer-dephasing CPTP map
   `rho -> sum_r P_r rho P_r`.
4. Each nonzero selective branch
   `rho_r = P_r rho P_r / Tr(P_r rho)` is normalized, positive, and stable
   under an immediate repeat read of the same pointer record.
5. The realized record labels are orthogonal one-hot atoms, so the exact
   post-record word/count layer can consume them as realized symbols.

This is an exact finite-model bridge from the pointer-formation layer to the
Kraus-instrument algebra. It does not solve the general physical production
problem.

## Proof

By the projector resolution and orthonormal record labels,

```text
W^dagger W
  = sum_{r,s} P_r^dagger P_s <r|s>
  = sum_r P_r
  = I.
```

So `W` is a normalized isometry. Contracting against record label `<r|` gives

```text
K_r = <r| W = P_r.
```

The Kraus resolution is therefore

```text
sum_r K_r^dagger K_r = sum_r P_r = I.
```

Thus the unconditional update

```text
E(rho) = sum_r P_r rho P_r
```

is completely positive and trace preserving by the same finite Kraus algebra
proved in
[`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md).
For any branch with `p_r = Tr(P_r rho) > 0`, positivity of
`P_r rho P_r` and division by `p_r` give a normalized positive selective
state. Idempotence `P_r P_r = P_r` gives immediate repeat-read stability,
and orthogonality `P_s P_r = 0` for `s != r` gives cross-read exclusion.

## Relation to the formation dynamics note

The pointer-non-demolition note establishes, inside an explicit finite
`S + E_1..E_n` model and under the quantum-Darwinism record reading, that
additive + redundant + persistent + objective record formation by local
evolution is equivalent to a conserved pointer:

```text
[H_int, Pi_S] = 0.
```

That result supplies stable pointer sectors for the bounded model. The
2026-06-18 controlled-copy write-isometry theorem now supplies the ideal
record-write isometry from the explicit controlled-copy/fresh-fragment
dynamics: `U_cc(pi/4)(|psi>|0>) = sum_r P_r|psi>|eta_r>`, with orthogonal
record labels `|eta_r>`, so a fixed record-basis calibration gives the
projective `W`.

The composition is:

```text
finite quantum-Darwinism pointer model
  + pointer-non-demolition record formation
  + blank fresh record fragment
  + controlled-copy write-isometry bridge
    => normalized W
    => projective Kraus instrument
    => realized record atom for post-record word/count dynamics.
```

The quantum-Darwinism record reading and explicit finite controlled-copy model
remain bounded bridge/model premises. The ideal write isometry is no longer an
additional free premise within that model.
Equivalently: the ideal pointer-label write is supplied by the controlled-copy
write-isometry theorem for the explicit finite model, not by an additional
framework axiom.

## What this buys

- It narrows the open "record dynamics to Kraus instrument" gap for the
  projective finite pointer model.
- It retires the source-side ideal-write subpremise for the explicit
  controlled-copy/fresh-fragment model: the write isometry is the calibrated
  controlled-copy dynamics.
- It gives a concrete interface between bounded formation dynamics and exact
  post-record information dynamics.
- It explains the pre-record/post-record distinction without making it an
  extra axiom:
  - before the record-write, the carrier state can contain coherence and
    predictive branch weights;
  - the record-write extracts an orthogonal realized label;
  - after the record-write, the word/count layer operates on realized symbols,
    not on unresolved amplitudes.
- It supplies a reusable audit target for projective measurement/instrument
  lanes: check whether the proposed physical bridge really supplies stable
  pointer projectors, orthogonal record labels, and an ideal or derived
  record-write isometry.

## What this does not claim

- It does not derive the pointer observable from the minimal axioms.
- It does not derive the physical Hamiltonian, action, coupling, clock, rate,
  or beta value.
- It does not derive arbitrary persistent-record dynamics into a normalized
  isometry.
- It does not derive the bounded quantum-Darwinism record reading from the
  minimal axioms.
- It does not derive a Born rule or probability law from post-record counts.
  Branch weights are read from the pre-record density matrix through the
  supplied projective instrument.
- It does not select a generation or Koide dial location. The dial remains a
  separate stable-location question, not a forced selection.
- It does not apply any audit verdict.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: closes_source_side_blocker_for_the_finite_model
conditional_surface_status: bounded-support for the finite
  pointer-non-demolition record model
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a finite-model bridge, not an audit-ratified framework-wide record-production theorem."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries in the formation, finite-isometry, instrument, and
  dynamics-reconciliation notes;
- the controlled-copy write-isometry bridge note and runner markers;
- exact projector primitives in the qubit pointer model;
- construction of `W` as the projective block-column isometry;
- extraction `K_r = P_r`;
- Kraus resolution, trace preservation, Choi positivity, selective branch
  normalization and positivity;
- pointer-dephasing of pre-record coherence into post-record realized labels;
- immediate repeat-read stability and cross-branch exclusion;
- explicit firewall flags: no general dynamics-to-`W` derivation, no physical
  Hamiltonian selection, no probability-law derivation, and no dial selection.

Run:

```text
python3 scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py
```
