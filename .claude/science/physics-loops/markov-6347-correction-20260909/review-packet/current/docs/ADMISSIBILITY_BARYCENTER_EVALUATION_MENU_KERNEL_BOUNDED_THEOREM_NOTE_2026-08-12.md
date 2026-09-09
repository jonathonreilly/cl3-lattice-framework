---
claim_id: admissibility_barycenter_evaluation_menu_kernel_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "For a fixed supplied finite-support measure on the density body, barycenter evaluation is a real affine functional on Hermitian matrices whose restriction to effects is a menu-independent probability grade, unique among affine positive normalized grades on the declared effects once spectral endpoints are imposed. The construction is not a physical Record law, not an axiom edit, and not a no-go against non-affine kernels."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.py
---

# Barycenter-Evaluation Menu Kernel As Affine Type-Bridge

**Date:** 2026-08-12
**Type:** bounded_theorem
**Scope:** exact finite-support construction on the qubit density body, on
the two hostile menus of the 2026-08-10 type-separation note.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.py`](../scripts/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.py)
**Runner cache:**
[`logs/runner-cache/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.txt`](../logs/runner-cache/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.txt)

## Result Up Front

Let `D` be the `2x2` density body. For a finite-support probability
`μ=Σ_k p_k δ_{ρ_k}` on `D`, the barycenter `ρ_μ=Σ_k p_k ρ_k` lies in `D`,
and barycenter evaluation

`w_μ(E)=Tr(ρ_μ E)`

is a well-defined real affine functional on Hermitian matrices. For effects
`0≤E≤I` it takes values in `[0,1]`, and for the same fixed supplied `μ`
it is a menu-independent probability grade. It is normalized on every
positive-effect resolution of `I`, matches the spectral endpoints of each
declared scaled projector, and on the August 10 hostile pair disagrees with
atomic restriction. Among grades of the affine Bloch form
`K(μ,E)=a(E)+Σ_i b_i(E) m_i(μ)` that are positive on `D`, normalized on the
declared menus, and tight at those spectral endpoints, it is the only
solution on `{E0,A1,A2,B1,B2}`.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) remains
untouched:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

This note does not identify `M_2(C)` with `D`, does not register a physical
menu, and does not exclude non-affine kernels.

## Exact Objects And The Construction

Write `P(n)=(I+n·σ)/2` for a unit Bloch vector `n`. The density body is

`D={ρ∈M_2(C): ρ=ρ^†, ρ≥0, Tr(ρ)=1}`.

Its Bloch chart is `ρ=(I+m·σ)/2` with `|m|≤1`. A finite-support measure on
`D` is `μ=Σ_k p_k δ_{ρ_k}` with `p_k>0`, `Σ_k p_k=1`, and each `ρ_k∈D`.
The barycenter `ρ_μ=Σ_k p_k ρ_k` stays in `D` by convexity. Barycenter
evaluation is the functional `w_μ(E)=Tr(ρ_μ E)`, restricted to an effect
grade whenever `0≤E≤I`.

## Inputs And Dependency Roles

- **Framework context:** the current Qubit and Admissibility sentences in the
  minimal-axiom memo supply the repository's `M_2(C)` possibility-domain and
  neighbor-dependent probability-distribution context. The density-body
  restriction and barycenter-evaluation rule enter this theorem as separate,
  explicitly supplied mathematical inputs.
- **Explicit bounded mathematical input:** this theorem is conditional on a
  supplied finite-support probability measure on `D`. The restriction from
  the full `M_2(C)` possibility domain to `D`, and the identification of its
  barycenter with an effect-evaluation state, are premises of the bounded
  construction rather than conclusions of this theorem.
- **Exact finite witness:** the August 10 note supplies provenance for the two
  displayed menus and restriction proposal. Their matrix sums, traces, and
  restriction values are recomputed here, so no earlier scalar Record
  functional or empty-record value is imported.
- **Consequence-only parent:** the August 9 frame-lift theorem states what a
  grade on the full binary/ternary scaled family would imply. It is not used
  to prove the construction or finite-family uniqueness below.
- **External inputs:** no measured, fitted, observational, or numerical
  literature values are used.

The declared hostile menus are those of
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md):

`E0=(1/2)P(z)`,

`M_A={E0,(9/10)P(n1),(3/5)P(n2)}` with
`n1=(4√2/9,0,-7/9)` and `n2=(-2√2/3,0,1/3)`,

`M_B={E0,(3/4)P(m1),(3/4)P(m2)}` with
`m1=(2√2/3,0,-1/3)` and `m2=(-2√2/3,0,-1/3)`.

Each displayed vector is unit. Direct matrix addition gives `Σ M_A=I` and
`Σ M_B=I`. The five effects are pairwise distinct.

The August 10 atomic restriction witness `ν` places mass proportional to
`(Tr E)^2` on those five atoms. Its normalization is `Z=509/200`, and

`K_ν(E0|M_A)=25/142`, `K_ν(E0|M_B)=2/11`,

with difference `-9/1562`. Restriction is therefore not menu-independent.

An affine kernel on the declared family has the form

`K(μ,E)=a(E)+b(E)·m(μ)`,

where `m(μ)` is the Bloch vector of `ρ_μ`. The kernel is **positive on `D`**
when `K(μ,E)≥0` for every `ρ_μ∈D`, equivalently `a(E)≥|b(E)|`. It is
**normalized** when `K(μ,I)=1`, `K(μ,0)=0`, and `K` is additive on `M_A`
and on `M_B`. It meets the **spectral endpoints** of a declared scaled
projector `E=cP(n)` when

`K(δ_{P(n)},E)=c` and `K(δ_{P(-n)},E)=0`.

Those two numbers are the eigenvalues of `E`, read from the matrix identity
`E^2=cE` together with `Tr(E)=c`. They are not imported from a target trace
value.

The parent
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
supplies uniqueness of a trace form once a menu-independent grade exists on
the full binary/ternary scaled family. The present note constructs one
affine grade on the declared finite family. It does not rerun the frame
lift.

## Theorem 1 — Affine Functional, Effect Positivity, Endpoints, Normalization

The barycenter of a finite-support probability on `D` is a convex combination
of densities, hence lies in `D`. The pairing `Tr(ρ_μ E)` is therefore defined
for every Hermitian `E`. If `0≤E≤I`, then positivity of `ρ_μ` gives
`Tr(ρ_μ E)≥0`, and applying the same argument to `I-E` gives
`Tr(ρ_μ E)≤1`. Thus the restriction to effects is a probability grade.
It depends on `μ` only through `ρ_μ` and on the effect only through the
matrix `E`, so for the same supplied `μ` the same effect receives the same
value in `M_A` and in `M_B`: the grade is menu-independent.

Linearity in `E` gives the endpoints `w_μ(0)=0` and `w_μ(I)=Tr(ρ_μ)=1`. If
`{E_i}` is any finite resolution of `I`, then `Σ_i w_μ(E_i)=Tr(ρ_μ I)=1`.
In particular both hostile menus are normalized.

For a declared scaled projector `E=cP(n)` the matrix identities `E^2=cE` and
`Tr(E)=c` give spectrum `{0,c}`. Direct evaluation of the pairing yields
the matching spectral endpoints

`w_{δ_{P(n)}}(E)=c`, `w_{δ_{P(-n)}}(E)=0`.

Explicit barycenters on `E0` are recorded for later comparison. The
maximally mixed state `ρ_*=I/2` has

`w_*(E0)=Tr((I/2)E0)=1/4`

in both menus. Two non-mixed barycenters are the finite-support laws
`μ=(3/5)δ_{P(z)}+(2/5)δ_{P(-z)}` and `μ'=(4/5)δ_{P(z)}+(1/5)δ_{P(-z)}`,
with barycenters `diag(3/5,2/5)` and `diag(4/5,1/5)`. Matrix pairing gives

`w_μ(E0)=Tr(ρ E0)=3/10`, `w_{μ'}(E0)=2/5`,

again in both menus. The two pure Diracs `δ_{P(z)}` and `δ_{P(-z)}` return
the spectral endpoints `1/2` and `0`.

## Theorem 2 — Disagreement With The August 10 Restriction Witness On `E0`

Atomic restriction of `ν` is a normalized probability vector on each hostile
menu separately, but it is not a function of the shared effect. The matrix
traces of the five atoms recompute

`Z=Σ(Tr E)^2=509/200`,

`K_ν(E0|M_A)=(Tr E0)^2/Σ_{M_A}(Tr E)^2=25/142`,

`K_ν(E0|M_B)=(Tr E0)^2/Σ_{M_B}(Tr E)^2=2/11`.

Barycenter evaluation assigns `E0` a single value at each `μ`. At `ρ_*=I/2`
that value is `1/4`, which is not `25/142` and is not `2/11`. At the biased
barycenter it is `3/10`, again distinct from both restriction numbers. Thus
restriction is not this kernel.

The August 9/10 singleton-mass attempt on the four distinct projective atoms
`P(±z),P(±x)` is unchanged: demanding raw point masses that normalize both
binary menus forces total mass two inside a probability space of mass one.
That contradiction is the parent argument; it is not a new obstruction.

## Theorem 3 — Affine Uniqueness On The Declared Finite Family

Let `K(μ,E)=a(E)+b(E)·m(μ)` be affine, positive on `D`, normalized on the
declared menus, and tight at the spectral endpoints of each declared scaled
projector. Fix `E=cP(n)` in `{E0,A1,A2,B1,B2}`. The two endpoints read

`a+b·n=c`, `a-b·n=0`,

so `a=c/2` and `b·n=c/2`. Write `b=(c/2)n+v` with `v⊥n`. Positivity is
`|b|≤a`, hence

`|(c/2)n+v|^2=(c/2)^2+|v|^2≤(c/2)^2`,

so `v=0`. Therefore `b=(c/2)n` and

`K(μ,E)=(c/2)(1+n·m(μ))=Tr(ρ_μ E)`.

Additivity on `M_A` and `M_B` is then inherited from `Σ E=I`. The same
coefficient match is obtained by extracting `a=Tr((I/2)E)` and
`b_i=Tr(P(e_i)E)-a` from the five matrices; those extracted coefficients
equal the unique solution just named.

Two rejectors sit outside the solution set.

1. Restriction is not of affine Bloch form in `μ`: it ignores the barycenter
   and returns two different numbers for the one effect `E0`. Restriction
   is not this kernel.
2. The wrong linear kernel `K(μ,E)=Tr(E)/2+δ_{E,E0} m_z` is affine and
   positive near the origin, but it fails additivity on `M_A` because the
   extra Bloch term does not sum to zero. The state-independent pairing
   `Tr(E)/2` itself fails the spectral endpoints of `E0`.

If the spectral-endpoint clause is dropped and only positivity, `K(μ,I)=1`,
`K(μ,0)=0`, and additivity on the two hostile menus are kept, uniqueness
fails. The contraction family `K_λ(μ,E)=Tr(ρ^{(λ)} E)` with Bloch vector
`λ m(μ)` and `λ∈[0,1]` remains affine, positive, and additive on both
menus; its residual to barycenter evaluation is the factor `(1-λ)` in front
of every Bloch term. The endpoint clause removes that residual. Non-affine
kernels are outside the ansatz and remain live.

## Boundary And Non-Claims

- No axiom sentence is edited. The displayed Admissibility wording is the
  current wording; this construction is not an axiom edit.
- Finite-support measures are taken on the density body `D`, not on the full
  possibility domain `M_2(C)`. That typing is an input of the construction.
- The kernel is not a physical Record law. Laboratory-menu registration,
  event-label identification with record content, and a formation site or rate
  remain separate physical inputs.
- Uniqueness is only among affine positive normalized kernels on the declared
  five-effect family. It is not a no-go against non-affine kernels.
- The August 9 frame-lift still consumes a grade on every binary and ternary
  scaled menu. The present kernel extends by the same trace formula, but
  physical coverage of that family is not claimed.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The affine functional, effect positivity, normalization, exact restriction disagreement, and uniqueness on the declared five-effect family follow from displayed finite-dimensional data. Restricting the physical possibility law to density matrices, selecting barycenter evaluation, registering eligible menus, and identifying outcomes with Record content remain outside the theorem."
trace_class: upstream_support
target_claim_id: admissibility_distribution_to_effect_grade_bridge
target_blocker_text: "derive distribution-to-effect-grade identification/functionality and universal binary-and-ternary physical menu eligibility"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "derive a physical map from the current full-domain Admissibility distribution to the density-body barycenter grade, together with eligible-menu registration and the content-only Record bridge"
conditional_surface_status: "exact for a supplied finite-support probability measure on the density body and for affine uniqueness on the declared five effects; the physical distribution-to-density restriction and outcome-registration bridge remain open"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | August 10 left barycenter evaluation live after restriction failed. This note constructs that kernel on finite-support states in `D` and checks it on the same hostile menus. |
| V2 | New content? | Yes: the barycenter-evaluation formula, matrix-level disagreement with `25/142` and `2/11`, and the affine uniqueness argument on the declared five-effect family. |
| V3 | Independently checkable? | Yes. The runner recomputes traces, the restriction weights, and the Bloch-coefficient uniqueness identity from the matrices. |
| V4 | More than a restatement? | Yes. The parents separate types and name a sufficient grade; this note supplies the affine kernel those interfaces consume on the declared family. |
| V5 | One-step relabel? | No. Restriction-failure and frame-lift uniqueness do not by themselves produce the barycenter kernel or the five-effect affine classification. |

## Negative-Claim Scope Check

This is a positive construction. The only negative sentence is that
restriction is not this kernel. No other measure-to-effect map is excluded.
In particular non-affine kernels remain live.

## Primary Runner

[`scripts/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.py`](../scripts/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.py)
recomputes the menu sums, the restriction weights, the barycenter traces,
and the affine uniqueness identities in exact `Q(√2)` arithmetic.
