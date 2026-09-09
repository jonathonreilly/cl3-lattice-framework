---
claim_id: record_content_only_shared_effect_descent_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "At one M_2(C) site the Aug 10 atomic restriction assigns two probabilities to one shared effect. If the two outcome pairs produce identical effect-only record content, one fixed deterministic readout function gives them the same value, so the unequal restriction probabilities cannot both be identified as direct readout values under that content map. A context-tagged content map and fixed readout realizing the two restriction values are exhibited as one formal escape. Other context-bearing contents and probability-process interpretations remain live. The note edits no axiom, proves no axiom necessity, proves no Born uniqueness, and supplies no formation rate."
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
  - admissibility_barycenter_evaluation_menu_kernel_bounded_theorem_note_2026-08-12
runner: scripts/record_content_only_shared_effect_descent_2026_08_12.py
---

# Record Content-Only Shared-Effect Descent

**Date:** 2026-08-12
**Type:** bounded_theorem
**Scope:** one-site Record readout versus the Aug 10 shared-effect
restriction kernel.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_content_only_shared_effect_descent_2026_08_12.py`](../scripts/record_content_only_shared_effect_descent_2026_08_12.py)
**Runner cache:**
[`logs/runner-cache/record_content_only_shared_effect_descent_2026_08_12.txt`](../logs/runner-cache/record_content_only_shared_effect_descent_2026_08_12.txt)

## Result Up Front

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) says:

> Only records are readable. A readout value is determined by record content alone.

The same Record section now also says that a site with no record cannot be
read. It supplies no named scalar functional, no additivity rule, and no value
for absence. None of those removed structures is used below.

The Aug 10 type-separation note
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md)
assigns two different normalized restriction values to one shared scaled
effect `E_0` in two ternary menus. If those probabilities are proposed as
direct readout values, identical effect-only content cannot realize both.
Some content distinction or a different probability-process interpretation
is then required. A menu tag is one formal content distinction, not the only
one.

Three exact statements locate the boundary.

1. **Effect-only content is menu-independent.** The map `Φ_eff(M,E)=E` stores
   the effect and forgets the menu. Any fixed deterministic readout function
   `R` assigns one value to `E_0` in both menus.
2. **Restriction is not a direct effect-only readout.** Recomputing the Aug 10
   atomic masses gives `K_ν(E_0|M_A)=25/142` and `K_ν(E_0|M_B)=2/11`. Those
   are two values on identical content, so they are not both of the form
   `R ∘ Φ_eff` for one fixed `R`.
3. **Context-bearing content remains a live escape.** Encoding a menu tag as
   `Φ_ctx(M,E)=E+i α_M 1_2`, with `α_A=1` and `α_B=2`, and applying the
   fixed affine readout `R_ctx` defined below yields exactly `25/142` and
   `2/11`. The construction is a formal witness, not a physical law.

No axiom is edited. The result is a compatibility theorem, not a Born
uniqueness theorem and not a formation-rate statement.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The same-content implication, exact restriction mismatch, and one context-tagged witness are proved on declared one-site maps. Identifying restriction probabilities as direct readout values is an explicit hypothesis; physical content formation, other context encodings, probability-process interpretations, axiom necessity, and Born uniqueness remain open."
trace_class: negative_route_pruning
target_claim_id: record_content_only_shared_effect_descent
target_blocker_text: "test whether the two Aug 10 restriction probabilities can be identified as direct readout values of identical effect-only Record content"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for identical effect-only content under one fixed deterministic readout, and for the displayed context-tagged witness; restriction-as-formation-probability and physical content formation remain outside the target"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
next_trace_action: "derive a physical content map or probability-process bridge from Admissibility and Record; the displayed context tag is only a formal witness"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site, with possibility domain `X=M_2(C)` as in the current Qubit
axiom. For a unit Bloch vector `n` write

`P(n)=(I+n · σ)/2`.

Reuse the Aug 10 shared-effect menus exactly. Fix

`E_0=(1/2)P(z)=((1/2,0),(0,0))`.

The two ternary scaled-projector menus sharing only `E_0` are

`M_A={E_0,(9/10)P(n_1),(3/5)P(n_2)}`

with

`n_1=(4 √2/9, 0, -7/9)`,
`n_2=(-2 √2/3, 0, 1/3)`,

and

`M_B={E_0,(3/4)P(m_1),(3/4)P(m_2)}`

with

`m_1=(2 √2/3, 0, -1/3)`,
`m_2=(-2 √2/3, 0, -1/3)`.

Each displayed vector has norm one. In both menus the scalar coefficients sum
to two and the coefficient-weighted Bloch vectors sum to zero, so each menu
sums to `I`. The parent note records the resolution check; the runner repeats
it.

The Aug 10 atomic measure `ν` lives on the five distinct effects in
`M_A ∪ M_B` and assigns mass proportional to the square of the effect's
trace. Writing `c=Tr(cP(n))` for a scaled rank-one effect, the five masses
before normalization are

`(1/2)^2=1/4`,
`(9/10)^2=81/100`,
`(3/5)^2=9/25`,
`(3/4)^2=9/16`,
`(3/4)^2=9/16`.

Their sum is

`Z=1/4+81/100+9/25+9/16+9/16`.

The common denominator `400` gives

`100/400+324/400+144/400+225/400+225/400=1018/400=509/200`.

Normalized restriction on each menu is then

`K_ν(E|M)=ν({E})/ν(M)`

whenever the denominator is positive.

A **content map** is a function `Φ` from outcome pairs `(M,E)` with `E∈M` into
`M_2(C)`. A **content-only readout** is one fixed deterministic function
`R:M_2(C)→Y` of that matrix, for any readout-value set `Y`. The Record
sentence quoted above supplies only the same-content implication once a
content map is chosen. It neither chooses `Φ` nor supplies a numerical
codomain or formula. To test the proposed identification with restriction,
Theorem 2 explicitly takes the two restriction probabilities themselves as
the candidate direct readout values.

Two maps are used.

1. **Effect-only.** `Φ_eff(M,E)=E`. The menu name is discarded. On the shared
   effect this is the same Hermitian matrix in both menus.
2. **Menu-context.** `Φ_ctx(M,E)=E+i α_M 1_2` with labels `α_A=1` and `α_B=2`.
   The pair `(label(M),E)` is written as one matrix in the Qubit possibility
   domain. The imaginary multiple of the identity is a label encoding, not a
   claimed physical formation mechanism.

For the context witness define the tag extractor

`τ(Φ)=Im Tr(Φ)/2`

and the fixed affine readout

`R_ctx(Φ)=(2-τ(Φ))(25/142)+(τ(Φ)-1)(2/11)`.

On `Φ_ctx` the tag is `α_M`, so this one function returns the two exact
restriction probabilities. The affine formula is a declared witness, not
Record-axiom content; no additivity property or value for absence is assumed.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the Aug 10 restriction kernel on the shared
effect can be a Record readout of effect-only content, and whether writing the
menu name into the record restores formal compatibility with the content-only
sentence.

| Obligation | Role | Disposition |
|---|---|---|
| pin the current content-only Record sentence | premise | quoted from the axiom memo |
| reuse the Aug 10 menus and atomic masses | common objects | restated and recomputed |
| show every `R ∘ Φ_eff` is menu-independent on `E_0` | Theorem 1 | proved by substitution |
| recompute `K_ν(E_0|M_A)` and `K_ν(E_0|M_B)` | Theorem 2 input | exact fractions below |
| show restriction is not a direct `R ∘ Φ_eff` readout | Theorem 2 | two unequal values on identical content |
| exhibit a fixed `R_ctx ∘ Φ_ctx` with the restriction values | Theorem 3 | `25/142` and `2/11` |
| derive a physical context-bearing content encoding | autonomous closure | open |
| decide whether restriction instead describes formation/event probability | semantic bridge | open; outside the direct-readout target |
| prove axiom necessity or Born uniqueness | non-claims | not attempted |

## Theorem 1 — Effect-Only Content Maps Are Menu-Independent On Shared Effects

Let `R:M_2(C)→Y` be any fixed deterministic readout function. Then

`R(Φ_eff(M_A,E_0))=R(E_0)=R(Φ_eff(M_B,E_0))`.

The two outcome pairs `(M_A,E_0)` and `(M_B,E_0)` produce the same record
content, so they produce the same readout. This is substitution, not an extra
continuity or positivity hypothesis.

No linearity, additivity, scalar codomain, or zero-value premise enters this
substitution. Thus every fixed deterministic content-only readout of an
effect-only record is menu-independent on the shared effect.

## Theorem 2 — Restriction Is Not A Direct Readout Of Identical Effect-Only Content

The Aug 10 atomic masses on `M_A` are `1/4`, `81/100`, and `9/25`. Their sum
is

`1/4+81/100+9/25=100/400+324/400+144/400=568/400=142/100`.

Normalized restriction of the shared effect is therefore

`K_ν(E_0|M_A)=(1/4)/(142/100)=(1/4)·(100/142)=25/142`.

The Aug 10 atomic masses on `M_B` are `1/4`, `9/16`, and `9/16`. Their sum is

`1/4+9/16+9/16=100/400+225/400+225/400=550/400=11/8`.

Normalized restriction of the shared effect is therefore

`K_ν(E_0|M_B)=(1/4)/(11/8)=(1/4)·(8/11)=2/11`.

These are unequal:

`25/142-2/11=(275-284)/1562=-9/1562`.

Suppose the two restriction probabilities were direct readout values under one
fixed content-only function `R`, so that

`K_ν(E_0|M)=R(Φ_eff(M,E_0))`

on both menus. Theorem 1 would force `25/142=2/11`, contradicting the
difference just computed. Therefore the two restriction probabilities cannot
both be direct values of `R ∘ Φ_eff`.

This conclusion is deliberately narrower than a Record or probability no-go.
Restriction may instead describe a formation/event probability, or a content
map may preserve contextual information. What fails is only the simultaneous
identification of two unequal numbers as direct readout values of identical
effect-only content under one fixed function.

## Theorem 3 — Context-Bearing Content Realizes Both Restriction Values

Define `Φ_ctx(M,E)=E+i α_M 1_2` with `α_A=1` and `α_B=2`, and use
the fixed readout `R_ctx` above. Then

`Φ_ctx(M_A,E_0)=((1/2+i,0),(0,i))`,

`Tr=1/2+2i`,
`τ=Im(1/2+2i)/2=1`,
`R_ctx=25/142`,

and

`Φ_ctx(M_B,E_0)=((1/2+2i,0),(0,2i))`,

`Tr=1/2+4i`,
`τ=Im(1/2+4i)/2=2`,
`R_ctx=2/11`.

The two matrices are distinct elements of `M_2(C)`. The readout is the same
function of the stored matrix in both cases, so it is content-only in the
sense of the quoted Record sentence. The two values differ because the stored
matrices differ.

This is one live formal escape from Theorem 2: on the two declared outcome
pairs, contextual dependence can be represented by distinct content followed
by one fixed readout. The escape is not a physical record-formation mechanism,
is not forced by the four axioms, and does not select the Born grade. A later
construction would have to derive which content actually forms and how any
contextual distinction is physically stored. A menu name is only the displayed
tag; apparatus state, preparation history, or another content variable could
play the same formal role.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- identify `K_ν` with a physical Record law;
- prove uniqueness of the Born trace grade;
- supply a record-formation site or rate;
- construct a dynamics that writes `α_M` into a forming record;
- exhaust other content maps or probability-process interpretations.

The discriminating gate is only this: identical effect-only content under one
fixed deterministic function has one readout value on `E_0`; distinct
context-bearing contents may have two values. This says neither that a record
must contain the menu name nor that restriction probabilities are physical
readout values.

## No-Go Discipline Gate

The negative part of Theorem 2 was stress-tested before being stated. The gate
passes only for the narrow direct-readout identification in the theorem. It
fails for any broader claim that effect-only records, contextual probability
laws, or the current Record axiom are impossible.

### N1 — Alternative Route Enumeration

| Route family | Concrete attack on the obstruction | Disposition |
|---|---|---|
| arbitrary or nonlinear fixed readout | replace `R` by any deterministic function on `M_2(C)` | ATTEMPTED; identical input still has identical output, so the narrow obstruction survives |
| stochastic readout kernel | let one content support a distribution of later values | ATTEMPTED; live probability-level route, but it leaves the theorem's direct deterministic readout target |
| context-indexed readout | use `R_M(E)` instead of one fixed `R(E)` | ATTEMPTED; live contextual-rule route outside the content-alone antecedent |
| context-bearing content | store a menu, apparatus, history, or other context tag in content | ATTEMPTED; Theorem 3 gives one exact witness and defeats the broad no-go |
| formation/event probability | read `K_ν(E|M)` as the probability that content forms rather than the value displayed by formed content | ATTEMPTED; live semantic route outside the direct-readout identification |

### N2 — Wall Independence Audit

There is one wall, not a collection of independent walls: a function has one
value on one input. The exact contradiction is the conjunction of identical
`Φ_eff` content, one fixed deterministic `R`, and two unequal candidate direct
readout values. No independent continuity, positivity, linearity, additivity,
absence-value, support, or dynamical obstruction is claimed.

### N3 — Hidden-Wall Scan

| Ingredient | Status |
|---|---|
| `Φ_eff(M,E)=E` | explicit theorem hypothesis, not axiom-selected content |
| restriction probabilities are direct readout values | explicit temporary identification tested by Theorem 2 |
| fixed deterministic content-only implication | imported from the quoted Record sentence |
| physical admissibility of the displayed context tag | open; no physical formation claim |
| support or rate for context-bearing content | open |
| named scalar readout, additivity, or a value at absence | absent and unused |

### N4 — Residual Matching

| Source | Residual match | Use here |
|---|---|---|
| [Aug 10 type-separation note](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md) | exact: the same `E_0` has restriction values `25/142` and `2/11` | supplies the two unequal candidate values |
| [Aug 12 barycenter-evaluation note](ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md) | not a negative witness: it gives an exact menu-independent effect grade from one fixed supplied barycenter | bounds scope by keeping a separate effect-functional probability grade live |

The barycenter construction is neither the Aug 10 restriction identity nor a
physical Record bridge, but its existence rules out rhetoric that the shared
effect witness closes all effect-functional routes.

### N5 — Quantifier-Scope Audit

| Scope | Executed status |
|---|---|
| per-element | checked on the exact shared effect `E_0` |
| per-site | checked for one site's same-content substitution |
| per-mode | checked and not executed; no spectral-mode or mode-exhaustion conclusion is in the theorem |
| per-block | checked only for the two declared menus and the direct-readout identification |
| lattice-wide | checked and not executed; no multi-site dynamics, formation law, or Born uniqueness is claimed |

The runner emits the same five-line scope certificate so that these limits are
machine-visible rather than prose-only.

### N6 — Partial-Closure Path Scan

Three positive paths remain explicit: derive physically formed
context-bearing content; derive a bridge interpreting restriction as a
formation/event probability; or develop the unresolved physical bridge for
the separate barycenter-evaluation grade in the companion note. The narrow
substitution theorem supplies no
axiom update, minimality result, or necessity claim for any of them.

### N7 — Steelman

The strongest live alternative is that `K_ν(E|M)` governs how often a record
with content associated to `E` forms, while the value read after formation is
fixed by that content. Then the same formed content can display the same value
in both menus even though its formation frequencies are `25/142` and `2/11`.
That interpretation does not refute the narrow direct-value contradiction,
because it rejects its explicit identification premise, but it blocks a broad
physical impossibility claim and remains unresolved here.

### N8 — Cross-Cycle Echo

| Earlier surface | Rechecked lesson |
|---|---|
| Aug 10 type separation | a menu restriction kernel must not be silently retyped as an effect-only global value |
| Aug 12 barycenter evaluation | a different exact menu kernel can arise from a fixed supplied barycenter and effect evaluation |
| current Aug 13 Record simplification | content determines a readout value, while no named scalar functional, additivity rule, or value for absence is supplied |

**Gate disposition:** PASS for Theorems 1–3 as narrowed. FAIL for the original
broader inferences that content must encode the menu name, that restriction is
necessarily a direct readout law, or that the Record axiom requires updating.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record content-only sentence | premise | quoted; no edit |
| Aug 10 menus, `ν`, and restriction arithmetic | common objects | restated and recomputed |
| `Φ_eff`, `Φ_ctx`, `τ`, and `R_ctx` | declared maps/functions | constructed here; no axiom-supplied scalar or additivity |
| physical context-bearing content encoding | escape route | live, not derived |
| restriction as formation/event probability rather than direct readout | semantic route | live, not decided here |
| barycenter-evaluation grade from the August 12 companion | counterexample to a broad effect-only no-go | exact separate construction; not a restriction identity or physical bridge |
| axiom necessity, Born uniqueness, formation rate | non-claims | not used |

The exact advance is a compatibility theorem between the Record content-only
sentence and the Aug 10 shared-effect restriction witness. Independent audit
remains required before any effective status may change.
