---
claim_id: admissibility_registered_partition_barycenter_pushforward_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "No deterministic measurable-set partition of D or X can realize the fractional barycenter grade for every Dirac law by set membership. On the declared atom-splitting space D×[0,1], explicit Borel inverse-transform cells push the newly supplied law μ⊗λ to Tr(ρ_μ E) for every finite-support μ and every finite effect resolution. The construction does not push a pre-existing Admissibility law on X, is not a physical compiler or Record readout law, and edits no axiom."
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
  - admissibility_barycenter_evaluation_menu_kernel_bounded_theorem_note_2026-08-12
  - record_content_only_shared_effect_descent_bounded_theorem_note_2026-08-12
runner: scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py
---

# Registered Partitions That Push Finite-Support Measures To Barycenter Evaluation

**Date:** 2026-08-12
**Type:** bounded_theorem
**Scope:** exact Dirac obstruction for μ-independent measurable partitions of
the density body or of `M_2(C)`, together with an explicit product
registration on `D×[0,1]` whose pushforward of every finite-support measure
equals barycenter evaluation on the August 10 hostile menus.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py`](../scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py)
**Runner cache:**
[`logs/runner-cache/admissibility_registered_partition_barycenter_pushforward_2026_08_12.txt`](../logs/runner-cache/admissibility_registered_partition_barycenter_pushforward_2026_08_12.txt)

## Result Up Front

The August 10 type-separation note names a sufficient interface: registered
measurable partitions whose pushforward supplies a menu-independent effect
grade. This note constructs a mathematical instance after a declared
atom-splitting lift and records the precise obstruction on the original
atomic support. It does not construct partitions for an already-supplied
Admissibility law on `X`.

1. **Dirac obstruction (scoped negative).** There is no family of
   μ-independent measurable subsets `A(i|M)` of the density body `D`, or of
   the current possibility domain `X=M_2(C)`, such that for every Dirac
   `μ=δ_ρ` one has `μ(A(i|M))=Tr(ρ E_i)` on the August 10 menus. Dirac measure
   of a measurable set is in `{0,1}`, while `Tr((I/2)E_0)=1/4∉{0,1}` and
   `Tr(diag(3/5,2/5) E_0)=3/10∉{0,1}`. Raw atomic Admissibility mass on `D`
   (or on `X` with support in `D`) cannot be pushed by a partition of that
   space to the barycenter kernel through deterministic set membership.
2. **Product registration is a measurable partition.** On `Y=D×[0,1]`, the
   cumulative interval sets `A(i|M)` built from prefix sums of `Tr(ρ E_j)` are
   Borel, pairwise disjoint, cover `Y` exactly when the last cell includes
   `t=1`, and do not depend on `μ`.
3. **Pushforward equals the barycenter kernel.** For every finite-support
   `μ=Σ_k p_k δ_{ρ_k}` on `D` and Lebesgue measure `λ` on `[0,1]`,
   `(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i)=w_μ(E_i)`. The identity is exact finite
   arithmetic. The set `A` depends on `M`, but the pushforward of the shared
   effect `E_0` is the same number in both hostile menus.
4. **Hostile-menu identities recomputed.** On the August 10 menus the
   pushforward of `E_0` is `1/4` at `I/2`, `3/10` at `diag(3/5,2/5)`, and
   `2/5` at `diag(4/5,1/5)`, in both menus; each menu normalizes; these values
   disagree with restriction `25/142` and `2/11`; spectral endpoints of `E_0`
   are `1/2` and `0`; reordering a menu moves the `E_0` interval without
   changing its Lebesgue length.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The current Record content-only sentence is used only to state the unresolved
interpretive boundary:

A readout value is determined by record content alone.

The same current section says that a site with no record cannot be read. It
supplies no named scalar functional, additivity rule, or value for absence;
none is used here. The product-cell probability is a mathematical event law,
not a direct Record readout value.

The product factor `[0,1]` is a declared registration coordinate. It is not
derived from the four axioms, not a primitive of the axiom surface, and not a
physical menu compiler.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The deterministic-set Dirac obstruction on D/X, Borel partition property, and product-law pushforward identity are proved by elementary measure and finite-arithmetic steps on declared one-site objects. The supplied law μ⊗λ is new mathematical input; deriving any atom-splitting registration from the physical Admissibility law and identifying its event with Record content remain open."
trace_class: direct_blocker_closure
target_claim_id: admissibility_distribution_to_effect_grade_bridge
target_blocker_text: "derive distribution-to-effect-grade identification/functionality and universal binary-and-ternary physical menu eligibility"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "derive an atom-splitting event registration from the actual Admissibility law on X and a content-only Record bridge; the displayed μ⊗λ law is supplied, not derived"
conditional_surface_status: "exact for deterministic partitions evaluated by Dirac set membership and for the declared μ⊗λ pushforward on finite-support measures; no pre-existing Admissibility law, physical registration, or direct Record readout is identified"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `D` be the `2x2` density body

`D={ρ∈M_2(C): ρ=ρ^†, ρ≥0, Tr(ρ)=1}`.

Write `X=M_2(C)` for the current one-site possibility domain. A finite-support
probability on `D` is

`μ=Σ_k p_k δ_{ρ_k}`, `p_k>0`, `Σ_k p_k=1`, `ρ_k∈D`.

Its barycenter is `ρ_μ=Σ_k p_k ρ_k∈D`. Barycenter evaluation is the kernel

`w_μ(E)=Tr(ρ_μ E)`.

The product registration space is

`Y=D×[0,1]`

with the product σ-algebra of the Borel structure on `D` and Lebesgue
measurable sets on `[0,1]`. Let `λ` denote Lebesgue measure on `[0,1]`.

Write `P(n)=(I+n·σ)/2` for a unit Bloch vector `n`. The declared hostile menus
are those of
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md):

`E_0=(1/2)P(z)`,

`M_A=(E_0, (9/10)P(n_1), (3/5)P(n_2))` with
`n_1=(4√2/9,0,-7/9)` and `n_2=(-2√2/3,0,1/3)`,

`M_B=(E_0, (3/4)P(m_1), (3/4)P(m_2))` with
`m_1=(2√2/3,0,-1/3)` and `m_2=(-2√2/3,0,-1/3)`.

Each displayed vector is unit. Matrix addition gives `Σ M_A=I` and `Σ M_B=I`.
The five effects are pairwise distinct. Parenthetical aliases: the first
remaining `M_A` effect is `(9/10)P(n_1)`; the second remaining `M_A` effect is
`(3/5)P(n_2)`; the two remaining `M_B` effects are the equal-coefficient pair
`(3/4)P(m_1)` and `(3/4)P(m_2)`.

For a finite menu `M=(E_1,...,E_r)` with `Σ_i E_i=I` and for `ρ∈D`, set

`S_0(ρ)=0`, `S_i(ρ)=Σ_{j=1}^{i} Tr(ρ E_j)` for `i=1,...,r`.

Because `Σ E_i=I` and `Tr(ρ)=1`, one has `S_r(ρ)=1`. Define

`A(i|M)={(ρ,t)∈Y: S_{i-1}(ρ) ≤ t < S_i(ρ)}` for `i=1,...,r-1`,

and

`A(r|M)={(ρ,t)∈Y: S_{r-1}(ρ) ≤ t ≤ 1}`.

Each `S_i` is continuous on the finite-dimensional density body, so these
inequality preimages are Borel subsets of `Y`. The final closed endpoint makes
the cells cover `Y` exactly; it changes no Lebesgue length. The sets depend on
`M` and on the trace pairing, not on a choice of measure `μ`.

The August 10 atomic restriction witness `ν` places mass proportional to
`(Tr E)^2` on the five distinct menu atoms. Its normalization is
`Z=509/200`, and

`K_ν(E_0|M_A)=25/142`, `K_ν(E_0|M_B)=2/11`,

with difference `-9/1562`. Restriction is a hostile control in this note, not
the constructed pushforward.

Optional embedding remark (not a numbered theorem). The map

`ι(ρ,t)=ρ + i(t-1/2)I`

injects `Y` into `X`: equality of two images fixes their Hermitian parts and
then their imaginary scalar coefficients. Since `Y` is compact and the
finite-dimensional space `X` is Hausdorff, `ι` is a homeomorphism onto its
compact, hence closed, image. The Borel cells therefore have Borel images in
`X`, and `ι_*(μ⊗λ)` gives the same probabilities there. Crucially, this is a
new lifted measure on `X`, not the original atomic `μ` supported on `D`.
Theorem 1 applies to deterministic set membership under that original atomic
law. More generally, some atom-splitting or stochastic enrichment is needed
for an all-Dirac fractional set law; this particular lift is sufficient, not
necessary or canonical. This note does not claim that the embedding is
physical, and does not identify the imaginary-multiple-of-identity coordinate
with any menu-label encoding.

The barycenter-evaluation parent
[`ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md`](ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md)
supplies the exact affine effect grade used as the pushforward target and its
separation from restriction. The Record-descent parent
[`RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md`](RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md)
keeps formation/event probabilities distinct from direct values read from
formed content. The present product measure is of the former mathematical
type; it supplies no physical formation interpretation and no readout value.

## Exact Target And Obligation Graph

**Exact target.** On the declared one-site objects, decide whether a
μ-independent measurable partition of `D` or of `X` can realize the
barycenter kernel on Dirac measures; if not, construct an explicit
μ-independent product partition of a declared lift whose pushforward equals
barycenter evaluation on every finite-support measure and on the August 10
menus.

| Obligation | Role | Disposition |
|---|---|---|
| rule out μ-independent partitions of `D` realizing fractional Dirac grades | Dirac obstruction | Theorem 1 |
| rule out the same construction on `X` with support in `D` | Dirac obstruction | Theorem 1 |
| define all `r` μ-independent Borel cells, including the `t=1` endpoint | positive interface | Theorem 2 |
| prove `(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i)` for finite-support `μ` | pushforward identity | Theorem 3 |
| recompute hostile-menu numbers against restriction | control identities | Theorem 4 |
| derive the registration coordinate from Record/Admissibility structure | physical compiler | open |
| identify the event label with Record formation/content or a readout value | content-only bridge | open; current Record supplies no scalar law |

## Theorem 1 — Dirac Obstruction On Atomic Support

**Claim.** There is no family of μ-independent measurable subsets
`A(i|M)⊂D`, or `A(i|M)⊂X`, such that for every Dirac probability `μ=δ_ρ` on
`D` one has

`μ(A(i|M))=Tr(ρ E_i)`

for every member `E_i` of the August 10 menus `M_A` and `M_B`.

**Proof.** Let `A⊂D` be any measurable set that does not depend on the choice
of Dirac measure. For any `ρ∈D`,

`δ_ρ(A) ∈ {0,1}`,

because a Dirac measure evaluates the indicator of membership. Take
`ρ_*=I/2`. Matrix pairing gives

`Tr(ρ_* E_0)=Tr((I/2)·(1/2)P(z))=(1/2)·(1/2)=1/4`,

since `Tr(P(z))=1`. The value `1/4` is not in `{0,1}`. Therefore no single
measurable set `A` can satisfy `δ_{ρ_*}(A)=Tr(ρ_* E_0)`.

The same contradiction appears at the non-mixed state
`ρ=diag(3/5,2/5)`. Because `E_0=(1/2)P(z)=diag(1/2,0)`,

`Tr(ρ E_0)=(3/5)·(1/2)=3/10 ∉ {0,1}`.

If the ambient space is enlarged from `D` to `X=M_2(C)` while the measures
remain Diracs supported on `D`, the same arithmetic applies: Dirac measure of
any measurable subset of `X` is still in `{0,1}` at those points. Hence no
μ-independent measurable partition of `D` or of `X` pushes every Dirac on `D`
to the barycenter kernel on the declared menus.

**Scope.** This is a scoped negative only. It is not a no-go against product
lifts, fiber lifts, non-atomic measures, μ-dependent constructions that change
the measure, or non-affine kernels. In particular it does not address the
product construction of Theorems 2--3, which changes the measure from `μ` on
`D` to `μ⊗λ` on `Y`.

## Theorem 2 — Product Registration Is A Partition

**Claim.** For every finite menu `M=(E_1,...,E_r)` with `Σ_i E_i=I`, the sets
`A(i|M)` defined above are Borel, pairwise disjoint, their union is exactly
`Y`, and they do not depend on any choice of measure `μ`.

**Proof.** Fix `ρ∈D`. The numbers `S_i(ρ)` are nondecreasing because each
`Tr(ρ E_j)≥0` for effects (Hermitian, spectrum in `[0,1]`). Moreover

`S_r(ρ)=Σ_{j=1}^{r} Tr(ρ E_j)=Tr(ρ Σ_j E_j)=Tr(ρ I)=1`,

and `S_0(ρ)=0` by definition. Therefore the half-open intervals

`[S_{0}(ρ),S_1(ρ)), ..., [S_{r-2}(ρ),S_{r-1}(ρ)),
[S_{r-1}(ρ),1]`

form an exact partition of `[0,1]`. The product sets

`A(i|M)={ρ}×[S_{i-1}(ρ),S_i(ρ))` (fiberwise)

are pairwise disjoint because the intervals are, and their union over `i` is
`{ρ}×[0,1]`. Varying `ρ` over `D` gives an exact partition of `Y`. Finally,
each map `(ρ,t)↦t-S_i(ρ)` is continuous, so each weak or strict inequality in
the displayed definitions has Borel preimage. Thus every cell is measurable.
The definition uses only the menu matrices and the trace pairing at `ρ`; it
does not mention `μ`.

## Theorem 3 — Pushforward Equals The Barycenter Kernel

**Claim.** For every finite-support probability `μ=Σ_k p_k δ_{ρ_k}` on `D`,
every finite resolution `M=(E_1,...,E_r)` of `I`, and every index `i`,

`(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i)=w_μ(E_i)`.

**Proof.** By definition of product measure for a finite atomic first factor,

`(μ⊗λ)(A(i|M))=Σ_k p_k λ({t∈[0,1]: S_{i-1}(ρ_k) ≤ t < S_i(ρ_k)})`.

For `i=r`, the displayed fiber also contains `t=1`; that singleton has zero
Lebesgue measure, so the same length calculation applies.

Each fiber set is an interval of length

`S_i(ρ_k)-S_{i-1}(ρ_k)=Tr(ρ_k E_i)`,

so

`(μ⊗λ)(A(i|M))=Σ_k p_k Tr(ρ_k E_i)=Tr((Σ_k p_k ρ_k) E_i)=Tr(ρ_μ E_i)`.

The identity is exact finite arithmetic, not an approximation. Menu
independence on a shared effect follows at once: the set `A(i|M)` depends on
which menu contains the effect and on the ordering of the other members, but
the Lebesgue length of the fiber assigned to a fixed effect `E` at a fixed
`ρ` is always `Tr(ρ E)`. Consequently the pushforward of `E_0` is
`Tr(ρ_μ E_0)` in both `M_A` and `M_B`.

## Theorem 4 — Hostile-Menu Identities Recomputed

All identities below are recomputed from the declared matrices; none is
imported as an un-checked number.

**Menu resolutions.** Both `M_A` and `M_B` sum to `I` by the parent Bloch
construction (scalar coefficients sum to two; coefficient-weighted Bloch
vectors sum to zero). Direct matrix addition confirms the same. Each member
is a scaled projector, and the five matrices are pairwise distinct.

**Restriction control.** On the five atoms,

`Z=Σ(Tr E)^2=1/4+81/100+9/25+9/16+9/16=509/200`,

`K_ν(E_0|M_A)=(1/4)/(1/4+81/100+9/25)=25/142`,

`K_ν(E_0|M_B)=(1/4)/(1/4+9/16+9/16)=2/11`,

difference `-9/1562`.

**Mixed state.** At `ρ_*=I/2`, fiber length of `E_0` is
`Tr((I/2)E_0)=1/4` in both menus. Summing fiber lengths over each menu
returns `1`.

**Biased states.** At `ρ=diag(3/5,2/5)`, the `E_0` length is `3/10` in both
menus. At `ρ'=diag(4/5,1/5)`, the `E_0` length is `2/5` in both menus. Both
menus normalize at each of these states.

**Disagreement with restriction.** The values `1/4`, `3/10`, and `2/5` are
distinct from both `25/142` and `2/11`.

**Spectral endpoints.** At `δ_{P(z)}`, the `E_0` interval has length
`Tr(P(z)E_0)=1/2`. At `δ_{P(-z)}`, the length is `0`.

**Order independence of lengths.** Reversing the order of `M_A` moves the
placement of the `E_0` interval among the prefix sums, but the multiset of the
three fiber lengths is unchanged, and the `E_0` length remains `Tr(ρ E_0)`.

**Mixture equals barycenter.** For the two-point law
`μ=(3/5)δ_{P(z)}+(2/5)δ_{P(-z)}`, Theorem 3 gives

`(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i)`

on every member of both menus, with barycenter `ρ_μ=diag(3/5,2/5)`.

## Boundary And Non-Claims

- No axiom sentence is edited. Admissibility supplies context for the target;
  the Record sentence supplies only the unresolved interpretation boundary.
- The extra `[0,1]` factor is a declared registration coordinate. It is not
  derived from the four axioms, not a new primitive of the axiom surface, and
  not an axiom edit.
- The law `μ⊗λ` is newly supplied mathematical input. The construction does not
  take an already-given Admissibility measure on `X` and partition it into the
  barycenter probabilities.
- This note is not a physical menu compiler, not a formation site or rate, and
  not a Record-content identification or direct readout law for the event
  label.
- Partitions are not unique: reorderings and null modifications give other
  families with the same pushforward lengths.
- Non-affine kernels remain live. Theorem 1 does not address them.
- Independent audit is required. This note authors no audit verdict.
- Status prose is bounded-support / bounded_theorem only. No broader surface
  status is asserted.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | exact semantic baseline | supplied; no edit |
| August 10 type-separation note | hostile menus, restriction witness, partition interface | parent dependency |
| August 12 barycenter-evaluation note | exact affine grade and restriction separation | direct parent dependency |
| August 12 Record-descent note | event/formation probability versus direct readout type boundary | direct scope dependency |
| Dirac measure range `{0,1}` | Theorem 1 | definition-level mathematics |
| product measure `μ⊗λ` and fiber Lebesgue length | Theorems 2--3 | supplied/constructed mathematical law; not the pre-existing measure on `X` |
| finite-support barycenter evaluation `Tr(ρ_μ E)` | pushforward target | imported from the direct parent and recomputed here |
| physical registration compiler | derivation of `[0,1]` from Record/Admissibility | open |
| content-only event-label bridge | physical Record readout | open |
| observed probabilities, frequencies, fits | none | not used |

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | August 10 named registered measurable partitions as a sufficient interface and left their construction open. This note supplies an explicit product family whose pushforward is the August 12 barycenter grade, and isolates the deterministic atomic-support obstruction that necessitates atom splitting or stochasticity for an all-Dirac fractional set law. |
| V2 | New content? | Rechecked current `main` at review base `7b8c99b8c`: August 10 names the partition interface, August 12 constructs the barycenter grade, and the Record-descent note preserves event-probability interpretations, but none constructs Borel inverse-transform cells `A(i|M)` with `(μ⊗λ)(A)=Tr(ρ_μ E)`. The exact partition and finite-support product identity are new on this surface. |
| V3 | Independently checkable? | Yes. The runner recomputes menu sums, restriction weights, fiber lengths, pushforwards, spectral endpoints, order independence, and the Dirac range contradiction from the matrices in exact `Q(√2)` arithmetic. |
| V4 | More than a restatement? | Yes. The parents separate types and construct the target grade; this note constructs every Borel cell, proves exact cover/measurability, and proves the pushforward identity on finite-support measures. |
| V5 | One-step relabel? | No. Naming the interface and barycenter evaluation does not produce the inverse-transform cells or product-measure identity. The new input `μ⊗λ` is disclosed rather than silently identified with the pre-existing Admissibility law. |

## No-Go Discipline Gate (Theorem 1 only)

The negative claim is restricted to deterministic measurable-set partitions
of `D` or `X` evaluated by Dirac set membership. The gate does not ship a
global non-derivability theorem, a no-go against stochastic kernels, or a
claim that the displayed product lift is physically necessary.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| arbitrary deterministic Borel cells on the original atom | allow any regular or irregular set in `D`, or in `X` with the Dirac supported on `D` | ambient enlargement alone does not change the indicator range `{0,1}` | **ATTEMPTED** |
| measure-dependent deterministic cells on the same atom | choose a different set after seeing `μ=δ_ρ` | each chosen set still contains the atom or does not, so its Dirac mass is `{0,1}` | **ATTEMPTED** |
| stochastic/Markov readout kernel on `D` | use `q_i(ρ)=Tr(ρE_i)` rather than an indicator `1_{A_i}(ρ)` | exact live escape, but it changes the target from a deterministic set partition to a stochastic kernel | **ATTEMPTED** |
| non-atomic auxiliary coordinate | use `D×[0,1]` and inverse-transform cells | exact escape constructed in Theorems 2--3 with a newly supplied law | **ATTEMPTED** |
| fixed non-atomic law on `D` or `X` | partition one atomless measure into cells of prescribed masses | live per-law route, but it does not satisfy the theorem's equality for every Dirac law | **ATTEMPTED** |
| operator-valued or Naimark event model | compute an expectation of effects or a dilated projector rather than set membership of the original density atom | live operator/dilation route outside the deterministic-set antecedent | **ATTEMPTED** |

### N2 — wall independence

There is one wall: an indicator evaluated at one atom has range `{0,1}`. The
`D` and `X` formulations collapse to that same wall and are not counted as
independent obstructions. Product lifts, Markov kernels, operator-valued
events, and fixed non-atomic laws evade an explicit antecedent; Theorem 1
does not purport to close them.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `D`, `X`, `Y` | declared mathematical domains |
| deterministic measurable-set membership | explicit hypothesis of Theorem 1 |
| equality for every Dirac law | explicit quantifier; a fixed atomless law is outside it |
| Dirac range `{0,1}` | definition of Dirac measure |
| August 10 menus | declared finite hostile family |
| product registration coordinate `[0,1]` | declared lift for the positive construction; not current axiom content |
| physical menu compiler | open; not assumed |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | current possibility domain and Admissibility distribution sentence; simplified Record boundary | exact current text; no scalar/additivity/absence premise and no edit |
| [August 10 type-separation note](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md) | hostile menus, restriction numbers, registered-partition interface left open | exact interface match; the displayed product law is not its pre-existing `μ_η` |
| [August 12 barycenter-evaluation note](ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md) | `Tr(ρ_μE)` effect grade and restriction separation | exact positive target; no physical law imported |
| [August 12 Record-descent note](RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md) | formation/event probability remains distinct from a direct value read from content | exact semantic boundary; no readout identification inferred |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | checked on `E_0` and all five distinct declared menu effects | no classification of every measure-to-effect map |
| per site | checked at one `M_2(C)` site / one density body | no composite theorem |
| per mode | checked and not executed; no spectral or harmonic mode claim exists | no mode exhaustion |
| per block | checked for the atomic-support obstruction and supplied product-registration block | no physical dynamics or compiler |
| lattice-wide | checked and not executed; no multi-site or lattice-wide law is claimed | no lattice-wide no-go |

The obstruction is per-Dirac / one-site / declared menus; it is not
lattice-wide.

### N6 — live partial-closure paths

1. Product or other atom-splitting lifts, as in Theorems 2--3.
2. A Markov kernel `q_i(ρ)` that keeps randomness in the readout rule instead
   of externalizing it as a coordinate.
3. A derived non-atomic Admissibility law on `D` or `X` with registered cells.
4. Operator-valued or Naimark event models, subject to a physical bridge.
5. A compiler deriving the event law from Admissibility and relating event
   formation to content without retyping it as a direct Record value.

### N7 — hostile steelman

> A registered probability law need not be a deterministic indicator on the
> density atom. The Markov kernel `q_i(ρ)=Tr(ρE_i)` already gives the desired
> probabilities, and any atomless physical Admissibility law could realize the
> same numbers by ordinary measurable cells without an appended coordinate.
> The product construction merely externalizes randomization, so it cannot
> establish that a new `[0,1]` carrier is physically needed.

**Answer.** This steelman defeats any physical-necessity claim, which is why
none is made. It does not refute the narrow theorem: deterministic membership
of the original Dirac atom is still binary. Theorems 2--3 give one exact
mathematical escape, not the unique escape. The actionable terminal obligation
is to derive either an atomless registered Admissibility law or a stochastic
event kernel from the framework and then prove how its event becomes formed
content without treating the event probability as the displayed readout.

### N8 — cross-cycle echo

| Earlier surface | Rechecked lesson |
|---|---|
| August 10 type separation | a global measure, menu kernel, and registered event partition are distinct types |
| August 12 barycenter evaluation | the positive effect grade exists mathematically before any registered event construction |
| August 12 Record descent | an event/formation probability is not automatically a direct value read from identical content |
| current Record simplification | no named scalar functional, additivity rule, or value for absence may be imported |

The present negative isolates a new but narrower residual: deterministic
partitions of the original atomic support cannot realize a fractional grade.
The positive product construction does not cancel the parent boundaries or
derive the physical registration they leave open.

**Gate disposition.** PASS for the scoped Dirac obstruction on deterministic
set partitions of the original atomic support. FAIL / DO NOT SHIP for "a
product coordinate is physically necessary," "no stochastic or operator
event model works," "no partition of any atomless law works," or "the four
axioms cannot supply a physical registration."

## Primary Runner

[`scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py`](../scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py)
recomputes the Dirac obstruction, the product partition cover, the
finite-support pushforward identity, the hostile-menu controls, spectral
endpoints, order independence, and a finite injectivity sample for the
optional embedding, all in exact `Q(√2)` arithmetic. Identity gates call the
constructed fiber length and pushforward; replacing either by restriction
must fail the checks.
