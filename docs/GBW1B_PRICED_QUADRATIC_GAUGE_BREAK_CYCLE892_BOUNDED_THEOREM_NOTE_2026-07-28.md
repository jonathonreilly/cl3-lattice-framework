# Finite window masses and a supplied blocked-walk kernel — Cycles 887/892

Date: 2026-07-28; corrected 2026-09-08

Authority: none

Audit: unset

Status: conditional bounded mathematical source; independent correction review pending.

Claim type: bounded_theorem

Runners:

- [Primary](../scripts/frontier_cycle892_gbw1b_pricing_2026_07_28.py)
- [Companion](../scripts/frontier_cycle892_gbw1b_independent_check_2026_07_28.py)

## Current premises and provenance

The [current governing memo](MINIMAL_AXIOMS_2026-06-29.md) is the current authority boundary. This note **supplies**, rather than derives from that memo, any rational linear scalar readout, representation, source, walk kernel, barrier, window and interpretation specified below. The removed historical scalar-Record/additivity wording is not current axiom authority. Finite labels, selected representations and squared amplitudes do not supply physical Records, a Born law, a clock, or a source/action relation.

The [original source and receipts](../.claude/science/physics-loops/multiplicity-correction-20260908/CORRECTION_HISTORY.md) are immutable dated provenance. Historical Gate-B/882/883/885/888 text is archived outside active note discovery. Exact quotation/segmentation and old result comparisons validate those identities only. No missing parent campaign, historical status or unselected theorem is accepted here.

## C08–C09: window maps and the containment correction

For a finite nonempty rotation-invariant S, W_S(R)=supp(R)+S is translation/rotation equivariant, monotone and nonconstant. Evaluating a singleton at the origin recovers S, proving injectivity of S↦W_S. The original 15 radius-one structuring sets and complete declared radius-two comparison are retained. Erosion, content-keyed inflation and other supplied maps remain counterexamples to exhaustion by this family.

On untyped finite support sets, translation equivariance plus union preservation gives W(A)=⋃_{a∈A}W({a})=A+W({0}); the no-interaction/union rule is an extra premise. Typed content can instead carry separate structuring sets by label.

The former derivation “scalar additivity forces containment” is false. Give label 0 weight 1 and label 1 weight 2, and let W select only label-1 sites. Then I_W(R)=2·#label1 is additive, content-transport equivariant and permanent under the supplied restrictions, but omits every label-0 site. The actual family has zero additivity failures while containment holds only on 1/12 configurations. We now impose containment explicitly when choosing the nine-window subcatalogue. Alternatively faithful nonzero calibration of **every** singleton label, together with scalar additivity and positive weights, implies containment: I_W=I and omission would lose positive weight. The earlier catalogue coincidence between additive survivors and containment holders is finite data, not that general implication.

## C10: retained finite quadratic data

On the original nine containment-holding windows, twelve configurations and six rational theta values, all 648 exact evaluations are retained. They give eight quadratic mass classes and 35/36 separating window pairs on ten configurations; the nonseparating pair is set-identical on this family. This does not make mass injective on all windows. The annular chart has eight profiles here but does not compute mass: the 51 original filled-annulus counterexamples remain.

## C11–C12 / T1–T2: full amplitude and exact difference

Supply the finite box, finite path depth, source set, barrier supp(R), uniform real seed and common edge phase. Positive-length paths avoid record sites. At those sites the only amplitude is the allowed zero-step seed; a seed may also be outside the records. For fixed R and theta define A by the complete finite path sum, including length zero, and Z(W)=Σ_{x∈W∩Box}|A(x)|². For W⊆W′,

    Z(W′)−Z(W)=Σ_{x∈(W′\W)∩Box}|A(x)|² ≥ 0.

Equality holds exactly when every added amplitude is zero. Containment makes supp(R) the inclusion-minimum, not a unique mass minimizer. Over containment-holding windows the common mass on supp(R) cancels, so mass is window-independent iff **full exterior amplitude mass** is equal, including exterior zero-step seeds. Positive-step reach alone is insufficient: records on the six neighbors block a source at the unrecorded origin; positive-step reach is empty, yet the support window has mass 0 and adding the origin gives mass 1.

Equal observed amplitude-support sets imply equal mass; the converse fails, and unequal sets do not imply a new class. Symmetric distinct windows can have identical weights. The corrected new-window prediction compares complete path-length coefficient vectors. The original 7,192-window finite search and earlier per-configuration fingerprint bug remain disclosed; no infinite-domain exhaustiveness follows.

## C13–C14 / T3–T4: interference coefficients and parity

Write A(x)=Σ_{L=0}^D c_L(x)u^L, with the supplied nonnegative rational path coefficients and |u|=1. Then

    M_d=Σ_{x∈W} Σ_{|L−L′|=d} c_L(x)c_L′(x),
    Z=Σ_{d=0}^D M_d T_d(cos(phi)),
    cos(phi)=(1−theta²)/(1+theta²).

This absolute-difference convention includes both cross terms. A one-sided convention must double coefficients at d>0. The implemented coefficient computation already used the absolute difference; the old printed formula did not. For A=1+u² at theta=1/2, Z=36/25; the undoubled one-sided formula gives 43/25.

Bipartiteness makes both source parities necessary for odd interference. It is sufficient only if opposite-parity sources have allowed positive-count coarrivals of opposite length parity at a measured site. This is equivalent to some odd M_d>0 for these nonnegative coefficients. Both source parities alone fail, for example in a window containing only two blocked seed sites, whose spectrum is (1/2,0,…). The original catalogue's parity coincidence remains finite data. Potential path support is theta-independent; coherent nonzero support can shrink by cancellation.

## C15: actual predictor scope

The companion's three new windows use the exact coefficient-vector predictor before comparing direct amplitudes. On this depth-four protocol, the six distinct cos(phi) samples distinguish degree-at-most-four polynomials. Equal set fingerprints suffice but are not required. The finite generated-window collisions and zero-step counterexample remain controls against a set-only predictor.

## C16–C17: interface diagnostics, not seven independent necessities

IF2 is a theorem for this supplied construction: Z is finitely additive on disjoint measured pieces. It does not derive a Born probability or scalar Record readout. IF1/IF3–IF6 are conditional interpretation questions, not necessary physical axioms. Amplitude inside/outside counts do not prove disjoint supports; a single seed Record has I=Z=1. For fixed theta and positive total mass, ordinary normalization is defined even if that total depends on theta. Theta-dependent normalized ratios are legitimate conditional functions. Window monotonicity is non-strict unless added mass is positive. A zero measured mass does not imply no motion. Polynomial dependence limits the fixed model's functional form but does not prohibit fitting theta.

The original seven-label accounting is preserved as a historical bookkeeping convention, not a proof of seven independent dimensions or a unique next route. Barrier, source, kernel, window, scalar readout, event law and physical formation remain supplied or open, with possible dependencies. A different barrier is one alternative, not the sole route.

## C18: executable scope

The only executed imported definitions are the four exact Cycle-885 configuration nodes and the selected Cycle-887 window catalogue. Historical parent text/cache receipts are identity comparisons only. No Cycle-878 absence scan proves a missing physical mechanism. Old failures, all original finite grids, and actual corrected controls remain part of the source-bound history.

## Publication and unresolved scope

The named computations are finite conditional evidence, not an audit or retained-grade decision. Historical cache totals, obsolete claims, failed attempts and the old trace are retained exactly in the outside-docs history. Current caches are generated only from the corrected source and its complete declared inputs; companion checks must be included by both actual consumers.

N1–N8 are not certified by counting routes or labels. The counterexamples below delimit the stated models; they do not enumerate every physical route or prove that the remaining choices are independent. No new axiom, registration, physical selection rule or formation law is proposed. Formal audit is deferred by the owner until a solid TOE; historical audit scheduling does not govern this correction.

```yaml
trace_class: conditional_support
target_claim_id: null
reachability_to_target: conditional
artifact_role: theorem
next_trace_action: "Independently confirm the corrected finite statements and actual inputs; retain all unsupplied physical interpretation and selection obligations."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
bare_retained_allowed: false
```
