# Postexecution Validation

Scratch command:

`python3 /private/tmp/gauge54_probe.py`

Result: `TOTAL PASS=81 FAIL=0`.

Validated surfaces:

- canonical half-trace Gram and two-dimensional `3+1` commutant;
- invariant binary effect cone `E=aP_3+bP_1`, `0<=a,b<=1`;
- unique nontrivial invariant sharp PVM up to outcome labels;
- a continuous `lambda in [0,1]` family of CP, trace-complete, repeatable,
  gauge-covariant triplet/singlet instruments with different post-states
  (an explicit nonuniqueness witness, not a complete instrument classification);
- positive two-coefficient electric/magnetic family with fixed product and free ratio;
- unbounded `SU(3)` Casimir sequence versus bounded Wilson plaquette multiplier;
- exact Wilson tangent-Hessian coefficients `1` at beta `6` and `4` at beta `24`.

Recovery rerun:

`python3 scripts/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.py`

Result: `TOTAL: PASS=81 FAIL=0`.

The original scratch script survived with SHA-256
`2f80aa2cd4eafacc2d25dcb0848a61649514294b1a183cd751c1d1f77bb920e1`.
Its scientific body is now preserved with a source note and fresh cache in draft
PR #7841.
