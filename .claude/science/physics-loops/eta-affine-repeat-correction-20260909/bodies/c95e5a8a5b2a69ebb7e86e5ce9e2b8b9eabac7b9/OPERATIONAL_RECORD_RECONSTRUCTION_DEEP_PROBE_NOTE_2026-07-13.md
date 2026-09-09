# Operational Quantum Objects From Record Histories: Deep Reconstruction Probe

**Date:** 2026-07-13

**Type:** meta

**Scope:** operational reconstruction and finite non-entailment probe

**Authority:** none. This note introduces no axiom, primitive, physical rule,
probability law, or audit verdict.

**Primary runner:**
[`scripts/operational_record_reconstruction_deep_probe_2026_07_13.py`](../../../../scripts/operational_record_reconstruction_deep_probe_2026_07_13.py)

## Question

Can preparations, effects, density matrices, channels, and instruments be
reconstructed from records and their continuation histories without adding
new ontology or new physical content to the four axioms?

## Result

The answer is **yes for the operational nouns, but no for their probability
and quantum structure**.

Once a physical continuation law and a normalized record-statistics rule are
available, the operational objects can be definitions:

- a **preparation** is an equivalence class of record-defined starting
  procedures that gives the same statistics for every later readable event;
- an **effect** is an equivalence class of later record events that gives the
  same probability for every preparation;
- a **transformation** is an equivalence class of interventions with the same
  statistics in every later record test; and
- an **instrument** is an outcome-indexed transformation, distinguished by
  sequential as well as immediate record statistics.

These definitions do not enlarge the instantaneous ontology. The physical
state can remain a configuration of records. An "operational state" is then a
summary of all future record statistics conditional on a preparation; it is
not an additional hidden thing at a site.

There is one nonnegotiable state-sufficiency gate. If the physical law takes a
record configuration as its complete state, then two preparation procedures
ending in the same configuration necessarily have the same continuation
support and statistics. Distinct quantum phases can therefore survive only if:

1. the full persistent record configuration distinguishes the preparations
   and the rule converts that relational record information into the later
   interference statistics; or
2. the Qualification is widened beyond a configuration of records, for
   example to a history-equivalence class or another explicitly typed state.

Route 1 is the cleaner bare-metal route because records are permanent: source,
setting, and phase-reference records can in principle remain in the global
configuration. But the actual extensional rule must prove that this suffices.
The present axioms do not yet do so.

But records plus a continuation support relation give only statements of the
form "this readable future can occur." They do not supply:

- a normalized measure over those futures;
- trial conditioning and a denominator;
- convex mixing probabilities;
- the full set of quantum effects or measurement contexts;
- ordinary finite-region tensor composition;
- marginal consistency when a site is embedded in a larger system;
- complete positivity of transformations; or
- a realized outcome of a nonselective channel.

Thus operational typing can probably be kept out of the final axiom text. The
physical content that makes the typing quantum cannot.

## Bare-Metal Construction

Let `c` be a finite record configuration and let `H(c)` be its set of lawful
continuation histories. A future event is record-defined when membership can
be decided entirely from later readable records.

Without a measure, one can define only the support functional

```text
s(E | c) = 1  iff  some history in H(c) produces E.
```

If a normalized conditional measure `mu_c` is separately available, then

```text
p(E | c) = mu_c(E)
```

supports the operational quotients above. Two different positive measures can
have exactly the same support, so the second line is not a relabeling of the
first.

This is the clean location of the operational bridge. Record supplies what is
read; a physical law supplies what may follow; a statistics law supplies how
often. None of those jobs should be hidden inside the word "preparation."

## Exact Probes

### 0. Record-state sufficiency

Let two named preparation procedures terminate in the same record
configuration `c`. If both the continuation set `H(c)` and its eventual
measure `mu_c` are functions of `c`, their complete future-record fingerprints
are identical by substitution. They cannot represent `|+>` and `|->`, because
an `X` record test distinguishes those preparations with certainty.

The runner checks both sides of this gate. Collapsing two procedure labels to
one record state collapses their fingerprints. Adding one persistent
preparation-reference record permits distinct fingerprints without adding a
second ontic state kind. This is only a logical repair pattern; the physical
nearest-neighbor rule must still generate the quantum table from that record.

### 1. Support is not probability

The runner places two normalized measures, `(1/2, 1/2)` and `(1/4, 3/4)`, on
the same two supported record futures. Their support is identical and their
predictions differ. This is the smallest exact witness that a continuation
rule does not by itself reconstruct weights.

### 2. One readable context is not a quantum state

For a qubit, `|+><+|`, `|-><-|`, and `I/2` all give probabilities `(1/2,1/2)`
in the `Z` record context. The `X` context distinguishes the first two from
each other and from the mixture.

The two `Z` projectors span only a two-dimensional real subspace of the
four-dimensional Hermitian qubit algebra. The six `+/- X`, `+/- Y`, and
`+/- Z` projectors span all four dimensions. The runner reconstructs

```text
rho = (I + r_x X + r_y Y + r_z Z) / 2,
r_j = 2 p(+j) - 1,
```

for `|0>`, `|1>`, `|+>`, `|+i>`, and `I/2` exactly.

This is a representation theorem after a tomographically complete probability
table is supplied. It does not create that table. Arbitrary context-wise
numbers need not be quantum: choosing `p(+X)=p(+Y)=p(+Z)=0.99` gives a Bloch
vector longer than one and a matrix with a negative eigenvalue.

### 3. Density matrices can represent operational preparations

The existing
[`Busch/CFMR effect-Gleason qubit authority bridge`](../../../BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
already proves the qubit statement on a supplied normalized nonnegative
additive functional over all effects:

```text
m(E) = Tr(rho E)
```

The important reconstruction point is that `rho` can be *defined* as the
unique representative of one preparation's complete future-record functional.
On that reading, `PREP-FRAME` is not a second physical identification premise:
the preparation state is the representative returned by the theorem.

That simplification is conditional. It works only if every downstream use of
"prepared state" means this operational equivalence class. If an independently
specified ontic or dynamical matrix is also called the prepared state, a bridge
between that object and the record functional is still required.

There is also a sharper projective-only route. Fiorentino and Weigert show that
for a qubit, ordinary tensor-product composition plus consistency between the
probabilities assigned to the qubit alone and as a subsystem yields a density
matrix and Born form using projective measurements alone. Their theorem is a
valuable possible replacement for the all-effects Busch extension, but it
does not derive the tensor product or the normalized noncontextual projective
probabilities. See [Gleason's Theorem for a Qubit as Part of a Composite
System](https://arxiv.org/abs/2511.15607).

### 4. An effect is not an instrument

The exact control uses

```text
K_keep = |0><0|,
K_flip = X |0><0|.
```

Both have the same effect,

```text
K_keep^* K_keep = K_flip^* K_flip = |0><0|,
```

and hence the same immediate outcome probability. Conditional on that
outcome, the first prepares `|0>` and the second prepares `|1>`. A later `Z`
record distinguishes them with certainty. Therefore immediate record counts
reconstruct an effect, while sequential record statistics are required to
reconstruct an instrument.

An even stronger ambiguity occurs at the channel level. The dephasing map has
both the projective decomposition `{P_0, P_1}` and the random-unitary
decomposition `{I/sqrt(2), Z/sqrt(2)}`. The averaged channel is identical, but
the candidate event labels and their probabilities are not. A deterministic
CPTP update does not choose its physical unraveling or an actual record.

### 5. Complete positivity already asks for composition

Matrix transposition is positive and trace preserving on a single qubit. When
applied to half of a Bell state, however, the partial transpose has eigenvalues

```text
{-1/2, 1/2, 1/2, 1/2}.
```

So the distinction between a merely positive map and a physical completely
positive channel is visible only after an ancillary composite is supplied.
The ordinary composite is therefore prior to, or co-defined with, channel
typing; it cannot be recovered from the one-site channel word alone.

The same point appears in tomography. States supported in different summands
of `M_4(C) direct-sum M_4(C)` can agree on every ordinary local-product record
statistic while differing on the central sector observable. Local record
statistics do not exclude invisible global sectors.

## Reconstruction Ladder

| supplied surface | object that can be reconstructed | what still does not follow |
|---|---|---|
| records + continuation relation | readable event support | weights, trials, actual member |
| normalized conditional history statistics | operational preparation/effect quotients | quantum effect completeness and Born form |
| complete additive qubit effect functional | unique density representative | origin of the functional and physical composition |
| ordinary composite + projective frame weights + marginal consistency | projective qubit density/Born representation | why those weights govern realized frequencies |
| tomographically complete sequential statistics | operational transformations and instruments | affine/linear closure and complete positivity |
| ordinary ancilla composition + affine quantum tables | CPTP channel representation | physical unraveling and actual outcome |

The ladder separates definition from physics. The left column contains the
real work; the middle column is mostly representation.

### Weakest operational closure ledger

The remaining interface can be compressed without pretending the entries are
independent axioms:

| key | rule-level obligation |
|---|---|
| `H` | normalized, context-consistent probabilities on record tests, with an explicit trial/conditioning semantics |
| `R` | a sufficiently separating repertoire of preparation and record contexts, with the same physical event identified across contexts |
| `M` | physical classical randomization and forgetting, if convex states and affine maps are to be used |
| `C` | an ordinary generated composite, local embeddings such as `P -> P tensor I`, and consistent spectator marginals |
| `S` | sequential/ancilla stability: transformations remain valid under every later test and beside an untouched ancilla |

An exact predictive specification for the fixed rule may derive several
entries together. The list is a
test interface, not a proposal for five new clauses.

The highest-leverage next construction is the one-spectator marginality test:

1. construct a qubit and one spectator from actual record configurations;
2. identify the globally recordable projective menus;
3. derive normalization and context-independence on those menus;
4. prove that `P` tested alone and `P tensor I` tested with an untouched
   spectator have the same record probability; and
5. prove that every operational one-site preparation has such a composite
   extension.

If all five are rule theorems, the projective composite-Gleason route returns
the qubit density/Born representation. Transformation tomography and the
ancilla-stability test remain separate: the Born state/effect pairing does not
determine the post-outcome update.

## Consequence For The Axiom Update

This probe does **not** support adding `preparation`, `effect`, `density
matrix`, `channel`, or `instrument` to the four axioms. Those are downstream
operational definitions and representation theorems once the relevant record
statistics exist.

It does strengthen three unresolved physical requirements:

1. **record-state sufficiency:** all phase- and entanglement-relevant
   preparation information must remain encoded in the global record
   configuration and affect later continuations, or the current state
   Qualification must be widened;
2. **finite-region composition:** an ordinary composite with no invisible
   global sector, or a rule from which it is proved; and
3. **statistics/actuality:** a normalized conditional history law or a
   deterministic frequency theorem, including trials, intervention semantics,
   and the relation between ensemble weights and realized records.

Composition now has two jobs: it closes the multi-site quantum carrier and it
opens the projective-only qubit Gleason route. That makes the composition probe
more, not less, important before constitutional language is frozen.

`PREP-FRAME` should be held open rather than promoted. It may dissolve into the
definition of operational preparation. `FRAME-EXT` can potentially shrink to
projective frame consistency plus ordinary composition and marginal
consistency. Neither probability consistency nor composition is derived here.

## No-Go Discipline Gate

**Gate result:** `PASS` for the explicitly proved finite representation and
separation lemmas. No broader no-go or complete reconstruction is claimed, so
a No-Go Discipline verdict for either is not applicable. The result does not
say that records can never generate quantum operational structure. It gives a
current checklist for what a successful derivation must supply, not an
exhaustive classification of all operational theories.

### N1 -- alternative routes

1. All-effects Busch/Gleason representation -- already available; imports a
   normalized additive functional on the full effect interval.
2. Composite-projective Gleason route -- live and stronger for a qubit;
   imports ordinary composition, projective frame weights, and marginal
   consistency.
3. Process tomography from sequential records -- viable once complete
   preparation/effect tables and probabilities exist.
4. Histories/decoherence-functional reconstruction -- live; would have to
   derive an event algebra, additivity, normalization, and actual-frequency
   semantics.
5. Generalized probabilistic reconstruction -- live; operational quotients
   are natural but extra principles are required to isolate complex quantum
   theory from broader probabilistic theories.
6. Direct rule-first reconstruction -- strongest route; one exact physical
   rule could generate the operational tables, composition, and frequency
   theorem together.

### N2 -- wall independence

- Support and weights are independent: two measures share one support.
- Record-state sufficiency and phase-sensitive preparation are independent
  until the full record configuration is proved to carry the phase reference.
- One context and state tomography are independent: three states share the
  same `Z` statistics.
- Effects and instruments are independent: equal `K^*K` does not fix the
  post-record state.
- Positive one-site dynamics and complete positivity are independent: partial
  transpose detects the difference only on a composite.
- Local tables and global tomography are independent: a duplicate central
  sector is invisible locally.

### N3 -- hidden-wall scan

Every operational quotient is conditioned on a supplied probability table.
The Markov/state-sufficiency assumption is exposed: procedure history may be
forgotten only when its future-relevant content remains in persistent records.
Tomographic completeness, convex mixing, ordinary tensor composition,
marginal consistency, and sequential access are named rather than smuggled
into the word "record."

### N4 -- residual matching

The collapsed-preparation witness prices record-state sufficiency; the
same-support witness prices the measure; the Pauli witness prices complete
contexts and positivity; equal-effect instruments price sequential data; the
partial transpose prices composition; and the duplicate sector prices global
tomography. No witness is used to claim closure of a different residual.

### N5 -- resolution audit

The matrix controls are exact finite-dimensional witnesses. They establish
logical separation and conditional reconstruction, not a classification of
all operational theories or all possible physical rules.

### N6 -- partial closure

Operational nomenclature closes by definition as soon as complete record
statistics exist. Density and channel matrices then close by finite-dimensional
representation theorems. This materially reduces the candidate axiom content,
even though it does not derive the statistics themselves.

### N7 -- steelman

The strongest opposing route is a deterministic, local, covariant rule whose
complete histories are uniquely ergodic and whose record-defined experiments
generate an ordinary locally tomographic complex composite. Such a rule could
make probabilities long-run frequencies, define preparations entirely by
record-conditioned histories, and derive density matrices and channels as
representations. Nothing in this probe rules it out.

### N8 -- cross-cycle echo

Earlier probability, Busch, Kraus/Choi, and tensor rows repeatedly reached the
same boundary from different sides: the mathematics represents supplied
operational data but does not identify the physical data-generating law. This
probe preserves that boundary while showing that the operational nouns
themselves need not become constitutional atoms.

## Literature Boundary

Operational reconstruction frameworks confirm the distinction rather than
removing it. Chiribella, D'Ariano, and Perinotti use several informational
principles plus purification to single out quantum theory
([paper](https://arxiv.org/abs/1011.6451)); Barrett's generalized probabilistic
framework contains quantum theory alongside many nonquantum theories
([paper](https://arxiv.org/abs/quant-ph/0508211)). These are route maps, not
premise authority for the present framework.
