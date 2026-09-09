---
claim_id: admissibility_d4_affine_lineage_binary_record_multi_join_repeatability_selector_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied 24-mask active set and a supplied family of detector involutions, the binary effects E_b(u)=(I+(-1)^b uS)/2 are positive and complete for 0<u<=1, have exact positive roots, admit an eta-controlled orthogonal-record channel, and form inequivalent laws as u varies. Active-block action repeatability selects u=1, while the declared inactive zero-detector blocks have cross-effect I/4 for every u. A displayed Neumann bound preserves positivity on |e|<=10^-9 conditional on the stated baseline norm and gap bounds. The affine action, decoder, H1 source, Schur baseline, and cubic response coefficient are supplied finite-model inputs rather than physical consequences or freshly recomputed quantities."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py
independent_checker: scripts/independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py
status: proposed_retained
actual_current_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Conditional affine-lineage binary Record family

**Date:** 2026-08-29
**Corrected:** 2026-09-09
**Type:** `bounded_theorem`
**Standing:** author-side `proposed_retained`; no formal audit has run.

Primary runner:
[`admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py`](../scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py).
Independent checker:
[`independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py`](../scripts/independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py).

## Result

Fix the supplied active-mask set

```text
A={5,6,9,10,17,18,20,23,24,27,29,30,
   33,34,36,39,40,43,45,46,53,54,57,58}.
```

It has 24 elements, twelve of Hamming weight two and twelve of weight four.
The earlier campaign supplied this set through a particular affine action and
Boolean decoder. This corrected note uses the displayed set as finite input;
it does not claim that the framework selects that action or decoder.

For each active mask let `S_eta` be a Hermitian involution whose `+1` and `-1`
eigenspaces are both nonzero. For `0<u<=1`,

```text
E_b(u,eta) = (I + (-1)^b u S_eta)/2.                 (1)
```

The spectrum is `{(1+u)/2,(1-u)/2}` on this supplied two-sector domain, so
both effects are positive and sum to the identity. With
`Q_±=(I±S_eta)/2`, their positive roots are

```text
K_b = sqrt((1+u)/2) Q_((-1)^b)
    + sqrt((1-u)/2) Q_(-(-1)^b).                    (2)
```

Equations (1)-(2) give `K_b^*K_b=E_b` exactly. Adding an orthogonal output
label `|b>` gives the isometry `W=sum_b K_b tensor |b>`, hence a CP, trace
preserving one-event Record channel. A direct sum over eta preserves the eta
label. This is an operator construction conditional on an occurrence event;
it does not supply a formation site, rate, clock, or physical eta carrier.
The comparison with a physical Record uses only the boundary stated by the
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md); the finite register itself is
supplied model data.

Two different positive values of `u` have different effect spectra. Thus the
family is inequivalent even without a scalar response calculation. The old
claim that this block freshly contracted the cubic Schur response was false:
both old runners inserted a coefficient disclosed by a parent calculation.
That coefficient remains historical conditional input and is not evidence in
the present proof.

On active blocks,

```text
K_b E_(1-b) K_b = (1-u^2) I/4.                       (3)
```

Consequently the extra action-system repeatability condition selects `u=1`
within `0<u<=1`. This condition concerns the action system, not permanence
of the output Record. On the declared inactive extension `S_eta=0`, both
effects are `I/2`, both roots are `I/sqrt(2)`, and the cross-effect is `I/4`
for all `u`. No reachability theorem says those inactive blocks occur, so
(3) is not a global uniqueness or no-member theorem.

## Conditional positivity interval

The earlier finite Schur construction supplied the resolvents

```text
Y(e) = (I + e Y0 T)^(-1) Y0,
R(e) = (I + e K0 T)^(-1) R0,
H(e) = R(e)^T Y(e) R(e),
G(e) = H(e) + H(e)^*.                              (4)
```

It also supplied the exact bounds

```text
||Y0||<22, ||K0||<16, ||R0||<20, ||T||<13,
lambda_min(G(0))>1/71.                               (5)
```

For `x=|e|<=10^-9`, the Neumann estimates are

```text
delta_Y <= x 22^2 13/(1-22 13 x),
delta_R <= x 16 13 20/(1-16 13 x),
||Y(e)|| <= 22/(1-22 13 x),
||R(e)|| <= 20/(1-16 13 x).
```

Telescoping the three factors in `H(e)` and then adding the adjoint gives

```text
||G(e)-G(0)|| <= 2(delta_R ||Y(e)|| ||R(e)||
                         + 20 delta_Y ||R(e)||
                         + 20 22 delta_R)
```

and hence

```text
||G(e)-G(0)|| <=
2193749493000038667200 / 177556693536960624997803
< 1/71.                                               (6)
```

Therefore the displayed baseline remains positive on that interval,
conditional on (4)-(5). The current runners verify the final rational in (6)
against the supplied gap; they do not independently reconstruct the bounds or
historical Schur tensors. Any use of the interval must carry those explicit
inputs.

## Exact boundary

This packet establishes a finite conditional family, its root/channel
algebra, spectral inequivalence, and the active/inactive repeatability split.
It does not establish:

- a framework-derived affine bit action or decoder;
- the old 110-term H1 source or a fresh Schur-response contraction;
- a physical encoding of eta, autonomous preparation, or event selection;
- repeated or unbounded histories, H2, gravity, or a TOE;
- a formal audit verdict, obligation retirement, or retained status.

The original four-PR source, caches, packet prose, intermediate endpoints,
and failed control setup remain in the correction history as attributed
historical evidence. They are not current execution evidence.

## Reproduction

```bash
python3 scripts/cached_runner_output.py --refresh scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py
python3 scripts/cached_runner_output.py --refresh scripts/independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py
```

The primary checks the projector calculus and exact bound. The checker uses
an independent diagonal calculation. Neither reports an unexecuted mutation
sweep.
