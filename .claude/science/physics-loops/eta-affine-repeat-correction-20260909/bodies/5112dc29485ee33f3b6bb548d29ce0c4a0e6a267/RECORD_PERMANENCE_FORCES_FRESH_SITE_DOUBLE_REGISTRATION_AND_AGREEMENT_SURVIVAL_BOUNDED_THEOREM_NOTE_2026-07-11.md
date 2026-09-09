# Record Permanence Forces Fresh-Site Double Registration, and Persistence Equals Agreement-Conditioned Survival (Bounded Theorem Note)

**Date:** 2026-07-11
**Review repair:** 2026-07-12
**Type:** bounded_theorem
**Claim scope:** Under the explicit site-tagged monotone-history reading below,
the Record axiom gives a necessary fresh-site and retention condition for any
history already identified as repeated record formation.
On the separately supplied agreement-conditioned map and a common
epoch-comparable lane-readout rule, a constant readout orbit is equivalent to
a map fixed point. Exact iteration gives finite-horizon offset bounds, but no
finite observation forces exact fixed-point siting. The physical
identification of records-flow self-composition with repeated record formation,
the readout rule, outcome independence, and the bookkeeping multiplicity
remain supplied or open conditions.
**Status authority:** independent audit lane only. This source note sets no
audit outcome and changes no premise registry or audit-owned surface.
**Primary runner:**
[`scripts/frontier_record_permanence_double_registration_2026_07_11.py`](../scripts/frontier_record_permanence_double_registration_2026_07_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_record_permanence_double_registration_2026_07_11.txt`](../logs/runner-cache/frontier_record_permanence_double_registration_2026_07_11.txt)

The note filename and its first two theorem labels are retained for downstream
citation stability. “Double registration” always means two events already
specified as record-formation events. “Forces” is conditional on representing
a formed record by its site and locked content and comparing later states by
monotone inclusion of those same site-tagged records. The bare axiom text does
not separately state an immobility law or identify a physical self-composition
step with record formation.

> **Bounded claim.** First, in the explicit site-tagged monotone-history model,
> every repeated record-formation history compatible with permanence and
> one-record-per-site uses distinct sites and retains all earlier records. This
> is a necessary Record-clause condition within that representation, not a
> converse theorem about the full Admissibility rule or an exhaustion of
> alternative record-identity semantics. Second, under the supplied map
> `f(r)=2r^2` and a supplied common rule relating record content to an
> epoch-indexed lane coordinate, constant map orbits are exactly fixed-point
> orbits. Third, the exact conjugacy `q=2r`, `q_{k+1}=q_k^2` quantifies how a
> nonzero offset escapes a fixed band. For every finite observation window a
> nonzero interval of offsets remains in band, so permanence cannot turn
> finite-precision persistence into proof of exact siting.

## Inputs and boundaries

The runner guards the following Record text from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> Records form.

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

The supplied algebraic surface comes from the
[`agreement-conditioned double-registration anatomy note`](RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md):

```text
r = |b|^2/a^2,
(p_s,p_d) proportional to (a^2,2|b|^2),
p_i' = p_i^2/(p_s^2+p_d^2),
f(r) = 2r^2.
```

That dependency is currently unaudited and is consumed only as a supplied
condition. In particular, neither independent outcome composition nor the
agreement filter is derived here from Record.

The T1 finite-history model uses one additional explicit representation
condition:

> **Site-tagged monotone record history.** A formed record is individuated by
> its target site and locked content. Permanence means that the same
> site/content record remains an element of every later state.

This is the usual partial-map representation of the displayed Record clauses,
but the note does not promote it to new axiom text. Without site-tagged identity,
a hypothetical migrating-record semantics would be an untested alternative.

## T1 (axiom-forced fresh-site double-registration geometry)

**Statement.** Consider a finite site-tagged monotone history whose `n` events
have already been specified as formation of one new record each, at target
sites `s_1,...,s_n`. If the history is compatible with the two Record clauses

```text
no site carries more than one record,
records are permanent,
```

then the target sites are pairwise distinct. After event `k`, all `k` records
remain present with their original site assignments. Thus any physical
re-registration proposal that separately adopts this site-tagged history model
and identifies its steps with successive record-formation events must use fresh
sites and full retention.

**Proof.** Suppose event `k` targets a site used by an earlier event. Keeping
both records makes that site carry more than one record. Replacing the earlier
record removes it from the later state and violates permanence. Both same-site
policies fail a Record clause, so every compatible event targets a fresh site.
Because each event forms one record and permanence retains each earlier one,
the state after event `k` contains the `k` records formed so far. ∎

The converse is not claimed. An injective site sequence can still fail the
unknown nearest-neighbor Admissibility rule or record-production dynamics. The
runner includes an explicit extra-veto model in which an injective sequence is
Record-clause-compatible but not admissible, preventing the former false
equivalence “admissible iff injective.”

The theorem also does not prove that a physical records-flow
self-composition is a second record-formation event or exclude a record-identity
semantics outside the site-tagged monotone model. It only constrains the
geometry after those conditions are supplied. The anatomy note's same-site
pinch map

```text
D(M) = P_s M P_s + P_d M P_d
```

is independently idempotent, `D(D(M))=D(M)`. This shows same-site re-pinching
is a bookkeeping no-op; it does not by itself make the fresh-site physical
identification.

## T2 (persistence equals agreement-conditioned survival)

**Statement.** Supply both of the following conditions:

1. the agreement-conditioned coordinate transition `r_{k+1}=f(r_k)` with
   `f(r)=2r^2`;
2. a **common epoch-comparable lane-readout rule**: the same mapping from
   record content to the coordinate `r_k` is used at every formation epoch, so
   values at different epochs may be compared. The rule does not assume those
   values are equal.

Then the readout orbit is constant for all epochs if and only if its initial
value is a fixed point of `f`. On the finite nonnegative line the fixed set is

```text
Fix(f) = {0,1/2}.
```

**Proof.** If the orbit is constant at `r`, the transition gives
`f(r)=r`. Conversely, if `f(r)=r`, induction gives `r_k=r` for every `k`.
Solving `2r^2=r` on `r>=0` gives `r=0` or `r=1/2`. ∎

Under the supplied independent-draw and agreement-filter interpretation,
“agreement-conditioned survival” means that the conditional distribution is
unchanged at a fixed point. This is a statement about the supplied kernel. It
does not show that physical record persistence is generated by that filter.

The earlier premise name “epoch-independent lane readout” was circular because
it defined every epoch to have the same value and then concluded persistence.
The repaired common-rule premise fixes only the readout mapping; equality of
the resulting values is the persistence predicate tested by the theorem.

### Record additivity does not supply the common rule

The Record axiom states additivity for a scalar readout `I` on disjoint
records. It does not define the lane coordinate or its aggregation. On the
supplied algebraic content assignment

```text
record 1: (a_1^2,|b_1|^2)=(2,1) -> r_1=1/2,
record 2: (a_2^2,|b_2|^2)=(1,1) -> r_2=1,
pooled aggregates: A=3, B=2 -> B/A=2/3,
```

the two per-record ratios and the pooled ratio are three distinct observables.
This does not make one observable “multi-valued”; it shows that Record
additivity alone does not say which observable is the cross-epoch lane
readout. When both per-record ratios agree, their pooled ratio agrees as well,
which is the positive control.

This assignment is an algebraic non-entailment exhibit on supplied record
content. It is not asserted to be a full model of the nearest-neighbor
Admissibility rule.

## T3 (finite-horizon persistence bound; exactness withdrawn)

The former statement name “exactness from permanence” is withdrawn because a
finite observation cannot distinguish zero offset from an arbitrarily smaller
nonzero offset. The exact replacement is a finite-horizon bound.

Set

```text
q_k = 2r_k.
```

For `f(r)=2r^2`,

```text
q_{k+1}=q_k^2,
q_n=q_0^(2^n).
```

At the interior fixed point `r*=1/2`, write `u_0=r_0-r*` and choose a band
`0<B<1/2`. Staying inside `|r_n-r*|<B` through step `N` requires

```text
((1-2B)^(1/2^N)-1)/2 < u_0
                             < ((1+2B)^(1/2^N)-1)/2.
```

For every finite `N`, both bounds are nonzero and the interval contains
nonzero offsets. Therefore finite persistence narrows the allowed initial
offset but never proves `u_0=0`.

For an illustrative positive offset `epsilon` and upper band edge, the exact
escape step is

```text
n_+ = ceil(log2(log(1+2B)/log(1+2epsilon))).
```

For a negative offset `-epsilon`, it is

```text
n_- = ceil(log2(log(1-2B)/log(1-2epsilon))).
```

The runner checks direct high-precision iteration against these formulas. Two
illustrative parameter pairs give:

| `epsilon` | `B` | positive escape | negative escape |
|---:|---:|---:|---:|
| `10^-5` | `0.1` | 14 | 14 |
| `10^-8` | `0.2` | 25 | 25 |

These values are mathematical test parameters, not observational inputs or
precision claims. They are not used to compare with measured masses.

Permanence has a narrower role: once an out-of-band record has formed, the
record cannot be erased to hide that history. Permanence does not accelerate
the map, lower the initial-offset bound, or make finite precision exact.

## Conditional agreement-survival arithmetic

At `r*=1/2`, the supplied bookkeeping gives

```text
p_s=p_d=1/2,
p_s^2+p_d^2=1/2.
```

If each step applies the supplied independent agreement filter to the retained
subpopulation, its fraction after `n` filters is `2^-n`. This is conditional
probability arithmetic. Disagreeing outcome histories are excluded from that
conditional subpopulation; the theorem does not equate their outcomes with an
out-of-band value of the ensemble coordinate `r`.

The alternative map `psi(r)=r^2` has nonnegative fixed set `{0,1}` and local
multiplier `2` at `r=1`. The Record freshness theorem and finite-horizon logic
do not select between `f` and `psi`; bookkeeping multiplicity remains open.

## Condition ledger for the durability/self-composition bridge (R-D)

- **Fresh-site and retention condition:** established as a necessary
  Record-clause consequence within the site-tagged monotone model for histories
  already identified as repeated record formation (T1).
- **Site-tagged monotone record identity:** explicit representation condition;
  not promoted to axiom text and not an exhaustion of possible semantics.
- **Physical re-registration identification:** open. Record does not identify
  a records-flow self-composition with formation of another record.
- **Constant-orbit/fixed-point equivalence:** exact, conditional on the
  supplied transition and common epoch-comparable readout rule (T2).
- **Common epoch-comparable readout rule:** supplied and not adopted. Record
  content-determination and additive `I` do not define this ratio rule.
- **Independent outcome composition and agreement filtering:** supplied by
  the anatomy surface and unaudited for this use; not derived here.
- **Finite-horizon offset constraint:** exact under `f`; exact siting is not a
  finite-observation consequence (T3).
- **Bookkeeping multiplicity / flow-class choice:** open and addressed by the
  companion bookkeeping-flow note; this source selects neither `f` nor `psi`.

The durability/self-composition bridge is therefore not discharged by this
note. No premise is adopted or registered.

## Import and support inventory

- **Approved foundation:** the Record sentences in `minimal_axioms`.
- **Explicit representation condition:** site-tagged monotone record identity
  for the T1 finite-history model.
- **Supplied bounded dependency:** the agreement-conditioned map and its
  singlet/doublet bookkeeping from the linked anatomy note; that row is
  unaudited on current main.
- **Explicit supplied conditions:** physical re-registration identification,
  common epoch-comparable readout rule, and independent outcome filtering.
- **Exact conditional algebra:** site freshness as a necessary Record-clause
  condition, fixed points, map conjugacy, escape formulas, finite-horizon
  bounds, and survival fractions.
- **Not consumed:** PDG values, fitted selectors, empirical precision
  thresholds, a probability rule derived from Record, or a physical
  spectrum-to-mass bridge.

## No-Go Discipline Gate

The negative claim is only that the named current-source surface does not
supply the remaining physical identifications or make finite observation
exact. It is not a universal derivation no-go.

### N1 — Alternative-route enumeration

1. **Site-tagged Record clauses — ATTEMPTED.** In the displayed representation
   they force distinct sites and retention after events are identified as
   record formation, but do not identify the physical self-composition step or
   define the lane ratio.
2. **Migrating-record semantics — OPEN.** Bare permanence does not separately
   state site immobility. A semantics that preserves record identity while
   changing its site lies outside the tested site-tagged monotone model.
3. **Full Admissibility rule — OPEN.** Its nearest-neighbor content is not
   instantiated; it may further restrict or generate record histories.
4. **Record-production dynamics — OPEN.** A concrete dynamics could supply the
   physical re-registration identification or the common readout rule.
5. **Additive scalar readout — ATTEMPTED.** The constructed ratio example shows
   that additive aggregates do not select a cross-epoch ratio observable.
6. **Agreement-conditioned anatomy — ATTEMPTED.** It supplies exact kernel
   algebra but explicitly leaves independent outcome composition as a
   condition.
7. **Finite-time instability — ATTEMPTED.** Exact conjugacy gives shrinking
   offset bounds, while a nonzero witness survives every chosen finite window.
8. **Alternative flow class — OPEN.** `psi(r)=r^2` remains compatible with the
   Record freshness result and has a different fixed point.

### N2 — Wall-independence audit

The physical self-composition/record-formation identification, common readout
rule, outcome independence, and bookkeeping multiplicity are distinct in the
displayed construction: each changes a different map from physical events to
the conditional algebra. No claim is made that this list exhausts future
dynamics or that the conditions are axioms.

### N3 — Hidden-wall scan

The two Record clauses are the only axiom content used in T1; site-tagged
monotone identity is labeled as representation data. Full Admissibility is not
inferred. The map, readout rule, outcome filter, and bookkeeping multiplicity
are labeled supplied or open. The numerical pairs are illustrative. No
empirical precision, mass data, probability postulate, or species
identification is hidden in a PASS condition.

### N4 — Residual matching

| source | source role | residual used here | match |
|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Record permanence, one-record-per-site, content-determined and additive readout | whether Record also supplies re-registration dynamics or a ratio rule | yes |
| [`RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`](RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md) | conditional map and independent-composition residual | whether its supplied map is physically selected | yes |
| [paired runner](../scripts/frontier_record_permanence_double_registration_2026_07_11.py) | finite site histories and exact map checks | whether the displayed necessary and conditional implications hold | yes |

### N5 — Rhetoric audit

T1 is a model-relative per-history necessary condition, not a theorem that
every injective sequence is globally admissible or that every record semantics
is site-tagged. T2 is a coordinate-orbit identity, not a lattice-wide
persistence mechanism. T3 is a finite-horizon bound, not an exactness or
asymptotic observation claim. No per-record outcome is conflated with an
ensemble ratio.

### N6 — Partial-closure path scan

The residuals are physical conditions, not naming conventions: changing them
changes which events are composed, how values are compared, or which map is
iterated. A retained record-production theorem, concrete Admissibility model,
or independently derived probability/readout construction could close part of
the bridge. Premise approval would be a separate governance path; this note
does not request or infer it.

### N7 — Steelman

A future microscopic dynamics could make successive records independent draws
of one physical lane distribution and could derive a canonical ratio readout
from record content. Such a result would turn the conditional algebra here
into a physical bridge. Conversely, correlated outcomes or a different
bookkeeping multiplicity could replace `f`. These routes are not tested, so a
universal no-go would be unjustified.

### N8 — Cross-cycle echo

The repaired orbit-occupancy and locked-record notes likewise distinguish
Record outcome labels from unsupplied statistical weights. The same lesson is
applied here: fresh-site record geometry does not silently supply outcome
factorization or an energy/readout law. Historical admission or campaign
language is not reused.

**No-Go Discipline result:** `PASS` for the narrow current-source
nonselection and finite-observation boundary. It would be `FAIL` for a claim
that future Record-compatible dynamics cannot derive the bridge; this note
makes no such claim.

## Consumers and citation stability

The context-only
`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`
consumes the durability/self-composition bridge as a named condition. This note
does not edit or discharge that chain. The context-only
`KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md`
exhibits `psi(r)=r^2`; the repaired result remains consistent with it. These
consumer names are intentionally not citation-graph dependencies.

Downstream citations may continue using this note filename and its T1/T2
labels. Any downstream text citing the old T3 “exactness from permanence”
statement must instead cite the finite-horizon bound and preserve the open
finite-precision residual.

## What this note does not claim

- no converse from injective sites to full admissibility;
- no axiom-text derivation or exhaustion of site-tagged record identity;
- no derivation of the physical re-registration identification, common
  epoch-comparable readout rule, independent outcomes, or agreement filter;
- no adoption or discharge of the durability/self-composition bridge;
- no finite-time or finite-precision proof of exact fixed-point siting;
- no selection between `f(r)=2r^2` and `psi(r)=r^2`;
- no derivation of `r=1/2`, mass prediction, empirical match, new axiom,
  approved primitive, audit verdict, or effective-status change.

## Verification

```bash
python3 scripts/frontier_record_permanence_double_registration_2026_07_11.py
```

Exit code is zero iff `FAIL=0`. Independent audit is required before any
status promotion.
