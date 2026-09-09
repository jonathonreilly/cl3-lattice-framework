# Record-Instrument Selection And Lüders-Form Primary-Source Audit

**Date:** 2026-07-14

**Type:** meta / bounded primary-source and exact finite-instrument probe

**Authority:** none. This is a conditional literature audit, partial reduction,
and exact countermodel packet. It is not an axiom proposal, primitive,
retained theorem, audit verdict, or selection of an interpretation. It changes
no axiom, primitive, registry, audit, review queue, or retained surface.

Companion runner:

```text
scripts/record_instrument_selection_luders_primary_source_probe_2026_07_14.py
```

## Result Up Front

The strongest honest answer is split.

There is a real derivation available, but it derives **form after context**, not
the physical read itself.

In one line: strong ideality selects Lüders form conditional on a supplied
context; exhaustive binary-qubit repeatability can force the same form, but
neither route selects which context is physical.

1. On a supplied sharp PVM `{P_r}`, strong ideality—meaning that the
   nonselective measurement leaves every observable compatible with that PVM
   unchanged—selects the Lüders instrument

   ```text
   I_r(rho) = P_r rho P_r.
   ```

   Merely requiring the next read to repeat the same outcome does not do this
   for degenerate `P_r`: arbitrary outcome-conditioned unitaries or
   measure-and-prepare channels inside the recorded eigenspace remain.

2. The actual Cycle-13/14 reads have a stronger special case. A complete
   two-outcome instrument on one `M_2(C)` carrier, with both outcomes
   attainable and exact repeatability, is forced to have two rank-one
   projectors. Rank-one output support then forces each branch map to be
   Lüders. Thus the **projective form can be reduced** rather than separately
   supplied once binary exhaustivity, complete positivity, attainability, and
   exact repeatability are accepted.

3. That reduction does not choose the projectors. `X`, `Z`, and every rotated
   qubit basis all support complete, repeatable, rank-one Lüders instruments.
   The same input state gives different record distributions in those
   contexts. Therefore **X versus Z remains supplied** by the programmed append
   law or must be derived from its deeper microscopic interaction/program.

4. Covariance, purification, and dilation do not repair this. Covariant
   instruments form classes; every CP instrument has an indirect realization;
   and inequivalent instruments can each have exact unitary/isometric
   dilations. A dilation is a realization theorem, not a selection theorem.

5. No-broadcasting and quantum Darwinism constrain what can be copied and make
   a supplied pointer observable redundantly accessible. They do not choose
   one outcome of a coherent global state. Redundancy is not actuality.

The programmed append law's projective **shape** is therefore partly
derivable. Its `X` center context, `Z` endpoint context, firing condition,
one-history sample, prepared state/weights, and future operation scope remain
law content. This probe supplies no reason to add “projective,” “Lüders,” or
“read” to the Record axiom. If a final microscopic law supplies a binary
repeatable record event, the projective/Lüders sentence should appear as a
theorem of that law.

## Exact Question And Answer Matrix

| proposed selector | what it genuinely constrains | what survives |
|---|---|---|
| complete CP instrument consistency | positive conditional maps whose sum is trace preserving | a convex family of instruments and contexts |
| repeatability | branch output lies in a sector that returns the same label | internal dynamics in a degenerate sector; context |
| permanence | later admissible operations preserve the written sector | choice of sector and the admissible-operation class |
| weak nondisturbance / first kind | later statistics of the measured PVM are unchanged | all exact degenerate countermodels below |
| strong ideality | every observable commuting with a supplied PVM is unchanged | Lüders map for that PVM |
| covariance | instrument transforms consistently with a supplied group action | generally a parameterized covariant family |
| dilation / purification | CP instrument has a unitary or isometric realization | which CP instrument is physical |
| no-broadcasting | arbitrary noncommuting state families cannot be copied | many alternative commuting pointer algebras |
| Darwinist redundancy | a dynamics-selected pointer observable has many readable imprints | single-outcome actuality and context-independent law selection |
| binary qubit + exact repeatability | sharp rank-one effects and Lüders branch form | which rank-one decomposition, event time, sample, and weights |

## Framework Boundary

The current foundation supplies `Z^3`, one `M_2(C)` local possibility domain,
one covariant nearest-neighbor admissibility rule, and permanent readable
records. It explicitly does not supply a measurement context, update law,
formation rule, weight, probability, or state-selection rule.

The primitive registry was read directly. The scale-reference primitive gives
only a units conversion; kinetic isotropy gives only `c_t=c_s`; and the
realized-state primitive allows pointwise evaluation at a law-admissible
realized state without selecting that state or a probability law. None is an
instrument, outcome context, sample rule, or record-preserving future-operation
class.

The analysis below therefore asks what follows **after** an instrument-level
description is supplied. It does not launder Davies–Lewis/Ozawa measurement
theory into the four axioms.

## 1. What A Quantum Instrument Supplies

Davies and Lewis introduced an instrument as an outcome-indexed operation-valued
measure: its branch maps give both outcome statistics and conditional state
changes, while the sum is normalized. Ozawa's realization theorem identifies
completely positive instruments with physically realizable indirect measuring
processes in the standard system–apparatus formalism.

For a finite outcome set, write

```text
I_r(rho) = sum_alpha K_(r,alpha) rho K_(r,alpha)^dagger,
E_r        = sum_alpha K_(r,alpha)^dagger K_(r,alpha),
sum_r E_r  = I.
```

Then `Tr[I_r(rho)] = Tr[rho E_r]` and the normalized conditional state is
`I_r(rho)/Tr[I_r(rho)]` when the denominator is nonzero.

This is a complete consistency language, not a physical selector. The
conditions say which collections are instruments. They do not say which
`{E_r}`, which branch maps, when the map acts, or whether one outcome becomes
ontically actual. Ozawa's theorem is especially clear on the present question:
realizability covers the whole CP-instrument class, so dilation cannot by
itself pick one member of that class.

## 2. Exact Degenerate Countermodels

Use a qutrit only as the smallest degenerate-sector stress test:

```text
P_0 = |0><0| + |1><1|,
P_1 = |2><2|.
```

Three instruments have exactly these effects.

### Lüders

```text
I_0^L(rho) = P_0 rho P_0,
I_1^L(rho) = P_1 rho P_1.
```

### Repeatable within-sector rotation

Let `U_0=diag(1,-1)` on `P_0 H`. Then

```text
I_0^U(rho) = U_0 P_0 rho P_0 U_0^dagger,
I_1^U(rho) = P_1 rho P_1.
```

### Repeatable measure-and-prepare

```text
I_0^M(rho) = Tr(P_0 rho) |0><0|,
I_1^M(rho) = Tr(P_1 rho) |2><2|.
```

All three are CP, their branches sum to a trace-preserving channel, their
effects are `{P_0,P_1}`, and an immediate second measurement returns the same
outcome with certainty. They give the same first-outcome probabilities for
every `rho`. Yet for `rho=|+><+|`, with
`|+>=(|0>+|1>)/sqrt(2)`, their outcome-zero poststates are respectively
`|+><+|`, `|-><-|`, and `|0><0|`.

This is the exact finite separator:

> Repeatability fixes recorded-sector support. It does not fix dynamics inside
> a degenerate recorded sector.

Permanence does not eliminate this separator unless “permanent” is strengthened
to a complete future-operation contract. Requiring every later admissible map
to preserve the `P_r` blocks prevents sector reconnection; it still permits
arbitrary dynamics within each block. If every mathematical local unitary is
declared admissible, a unitary swapping `P_0` and `P_1` revokes the label.
Absolute permanence therefore always carries an operation scope or a separate
append-only record carrier.

## 3. Covariance Does Not Collapse The Family

The phase representation

```text
V_phi = diag(exp(i phi), exp(-i phi), 1)
```

acts nontrivially inside `P_0`. Every outcome-zero Kraus operator

```text
K_0(theta)=diag(exp(i theta),exp(-i theta),0)
```

commutes with `V_phi`. Hence the continuous family

```text
I_0^theta(rho)=K_0(theta) rho K_0(theta)^dagger,
I_1^theta(rho)=P_1 rho P_1
```

is simultaneously complete, repeatable, and covariant under the same
nontrivial group action. Distinct `theta` give distinct poststates on coherent
inputs.

This is consistent with the primary covariance literature, which derives
structure theorems and parameterizations for covariant instruments rather than
a general one-member selection theorem. A sufficiently rich irreducible group
action plus additional extremality or optimality conditions can shrink a
family. The group representation, outcome action, and optimality objective are
then load-bearing physical input.

For the append law, spatial translation/proper-cubic covariance transports a
record-defined relational frame. It does not say that the center must use `X`
while the endpoints use `Z` inside that frame.

## 4. What “Minimal Disturbance” Must Mean

There are two inequivalent readings.

### Weak reading: repeat the measured property

Require only

```text
Phi^*(P_r)=P_r,
Phi=sum_r I_r.
```

All three qutrit instruments satisfy it. This is first-kind stability of the
measured label, not Lüders uniqueness.

### Strong reading: preserve every compatible property

Require

```text
Phi^*(B)=B
```

for every block-diagonal `B` commuting with every `P_r`. The rotated and
measure-and-prepare instruments fail: both disturb some observable wholly
inside `P_0`. Lüders fixes the full block-diagonal algebra.

More directly, require each outcome branch to act as the identity on every
state already supported in its outcome sector. A CP branch with effect `P_r`
and output support in `P_r` has Kraus operators
`K_(r,alpha)=P_r K_(r,alpha) P_r`. If it fixes every state on
`P_r H`, its restriction is the identity channel. Therefore

```text
I_r(rho)=P_r rho P_r.
```

This is the clean conditional Lüders theorem needed here. But “preserve every
compatible property” is a strong physical ideality premise, not a synonym for
permanence or repeatability. The Busch–Singh Lüders theorem and the broader
nondisturbance literature likewise begin with a specified observable and ask
what an ideal measurement does to another observable; they do not derive the
first observable.

## 5. Sharp Binary-Qubit Reduction

The one-site append law is more constrained than the qutrit stress test.

Let a complete two-outcome qubit instrument have effects

```text
0 <= E_0 <= I,
E_1=I-E_0.
```

Suppose both outcomes are attainable and exactly repeatable. After outcome
`r`, some nonzero output state must give the same outcome with probability
one. Thus each `E_r` has eigenvalue one. Since `E_1=I-E_0`, `E_0` must have
both an eigenvalue one and an eigenvalue zero. In dimension two,

```text
E_0=P,
E_1=I-P
```

for a rank-one projector `P`.

Exact repeatability puts the output of branch `r` in the corresponding
one-dimensional range. Every branch Kraus operator is then `c_alpha P_r`.
The effect condition gives `sum_alpha |c_alpha|^2=1`, so

```text
I_r(rho)=P_r rho P_r.
```

This is the **sharp binary-qubit reduction**. It improves the earlier finite
FD-SLIR statement by showing that sharpness itself follows from exhaustive
two-outcome qubit repeatability, provided both outcomes are genuinely
attainable and the Davies–Lewis/Ozawa CP-instrument framework is already the
right physical language.

The reduction has exact limits:

- it does not apply to a degenerate outcome sector;
- it does not derive that nature uses a two-outcome instrument;
- it does not define when the instrument fires;
- it does not choose `P`;
- it does not turn the nonselective sum into one actual outcome; and
- it does not derive a prepared state, repeated-trial corpus, or frequency
  theorem.

Both

```text
{ |0><0|, |1><1| }            Z context
{ |+><+|, |-><-| }            X context
```

satisfy every conclusion above. On input `|0>`, the first gives probabilities
`(1,0)` and the second `(1/2,1/2)`. Projective/Lüders **form** is forced;
physical context is not.

## 6. Dilation And Purification

For Kraus operators `K_(r,alpha)`, the stack

```text
V |psi> = sum_(r,alpha) |r,alpha> tensor K_(r,alpha)|psi>
```

is an isometry exactly when the instrument is complete. The runner constructs
such isometries for the Lüders, within-sector-unitary, and measure-and-prepare
countermodels. All are legitimate dilations; their conditional system states
differ.

There is also representation freedom inside one instrument. A unitary mixing
of Kraus labels belonging to the same outcome leaves the CP branch map
unchanged while changing the displayed dilation coordinates.

Therefore neither of these statements is a selector:

- “the process admits a purification”; or
- “the instrument comes from unitary system–apparatus dynamics.”

They establish compatibility with a larger reversible description. They do not
choose the instrument, pointer PVM, apparatus initial state, pointer readout,
or one actual result. Ozawa and the finite-dimensional realization theorems
support exactly this interpretation.

## 7. No-Broadcasting And Quantum Darwinism

Barnum, Caves, Fuchs, Jozsa, and Schumacher prove that a noncommuting family
of mixed states cannot be broadcast. The pure-state inner-product control is
already decisive for `|0>` and `|+>`: a unitary copier would have to preserve
`<0|+>=1/sqrt(2)` while the copied outputs have overlap `1/2`.

Orthogonal pointer states can be copied. But that does not select a unique
pointer basis:

- CNOT copies the `Z` basis given a `|0>` blank;
- its Hadamard conjugate copies the `X` basis given a `|+>` blank.

Both are unitary and exact.

The Ollivier–Poulin–Zurek environment-as-witness results show that, for a
supplied system/environment split and interaction, only dynamics-selected
pointer observables can leave many independently readable imprints. The
Horodecki–Korbicz spectrum-broadcast structure sharpens the structural form of
objective records. These are powerful **CONTEXT-after-dynamics** and
readability results.

They are not one-history formation laws. The runner makes two disjoint CNOT
witnesses of a system qubit:

```text
(|0>+|1>)/sqrt(2) tensor |00>
    -> (|000>+|111>)/sqrt(2).
```

Each environment fragment carries the same perfect `Z` record, yet reversing
the two CNOTs recovers the coherent input and blank witnesses. Hadamard
conjugation gives an equally redundant `X` construction. Redundancy certifies
agreement and accessibility relative to the interaction. Reversible redundancy
alone neither makes the record permanent nor chooses one GHZ term.

## 8. Mapping To The Four Formation Interfaces

| interface | what these principles can derive | exact open content |
|---|---|---|
| `RECORD` | repeatability gives stable outcome-sector support; a declared invariant future-operation class gives nonreconnection; binary qubit repeatability gives rank-one Lüders branch form | which physical carrier is append-only, what later operations are admissible, and when a new record forms |
| `CONTEXT` | strong ideality determines the branch map conditional on `{P_r}`; Darwinism can identify the pointer observable conditional on a supplied interaction/environment split | the physical PVM/POVM, `X` versus `Z`, setting/program decoder, and why that interaction is the law |
| `ACTUALITY` | an instrument enumerates labelled conditional continuations | which single continuation is actual; the nonselective CP sum contains every nonzero branch |
| `STATISTICS` | an instrument gives trace weights conditional on its effects and input state; later probability theorems can reduce weight form | prepared state, physical probability semantics, one sample, repeated-trial preparation/corpus, independence, and frequency law |

The four interfaces are not four proposed axioms. One exact physical law may
close several at once.

## 9. Consequence For The Programmed Append Law

Cycle 13 explicitly declared:

```text
D2 center read   = projective X instrument
D3 endpoint read = projective Z instruments.
```

Cycle 14 retained those reads after adding a reset certificate and
self-writing front.

The present result reclassifies their minimum content.

### What can become theorem content

If each onsite read is established as:

1. a complete binary CP instrument on that site's `M_2(C)` carrier;
2. both outcomes are physically attainable; and
3. the written label is exactly repeatable,

then its effects are a rank-one PVM and its branch maps are Lüders. The law
does not need a separate `K_r=P_r` atom.

### What remains explicit law content

- why the center context is the relational `X` decomposition;
- why the endpoint context is the relational `Z` decomposition;
- how the seed/header transports that qubit frame;
- why the event is ready and eventually occurs;
- the `CZ` interaction and reset target;
- which one of the nonzero outcomes becomes actual;
- the state/weight/repeated-trial semantics; and
- which future operations preserve the record forever.

Bell capability can test the relative `CZ-X-Z` package, but it cannot select
that package without Bell capability being supplied as a target. Global common
unitary conjugation produces presentation-equivalent packages, while other
interaction/read choices give genuinely different record laws.

### Axiom need

This route does not force a new axiom sentence. “A read uses a projective
Lüders instrument” is too specific for Record and, in the binary-qubit case,
is partly derivable from a completed law. “Records are repeatable” is weaker
than current permanence and still does not select context or formation.

The constitutional question remains the one already exposed by the append-law
cycles: whether the final axiom set should require formation to be a permanent
local extension or should instead refer to one exact formation law from which
extension follows. Instrument theory favors the latter derive-first route. It
can compress a fully stated law; it cannot replace that law with the word
“read.”

## 10. Minimal Chiral `U(1)` Tuple: Primary Precedent Only

The tuple from the topological/conservation/RG probe is

```text
(-9,-5,-1,7,8).
```

It has exact primary-source precedent. Batra, Dobrescu, and Spivak list the
five-fermion anomaly-free chiral set

```text
(1,5,-7,-8,9),
```

which is the same tuple up to permutation and overall charge conjugation. They
also state the two anomaly equations, the no-vectorlike chiral condition, and
that at least five fermions are needed. Their table minimizes the largest
positive charge in the stated search, not `sum q_i^2`.

Costa, Dobrescu, and Fox later parameterize the general integer solutions of
the linear and cubic `U(1)` anomaly equations and again identify sign,
permutation, and common integer rescaling freedoms.

Thus:

- the anomaly equations and the winning tuple are not novel;
- the repo probe's exact contribution is its bounded exhaustive certificate
  that the tuple uniquely minimizes the quadratic charge norm among primitive
  nonzero nonvectorlike five-charge integer solutions;
- the quadratic norm objective is additional selector content not supplied by
  either primary source; and
- none of this identifies the framework's gauge group, derives a gauge field,
  couples the quintet to the `M_2` lattice carrier, or selects the microscopic
  record law.

The tuple is a useful matter-lane compression and a good precedent for a
selection theorem after a class and invariant objective are fixed. It must not
be inflated into evidence that anomaly cancellation selects the full TOE law.

## 11. Primary-Source Ledger

| source | content used | boundary |
|---|---|---|
| Davies and Lewis, [*An operational approach to quantum probability*](https://doi.org/10.1007/BF01647093), CMP 17 (1970) 239–260 | instrument as normalized outcome-indexed operations; repeatability deliberately not universal | formalizes the instrument; does not select a physical one |
| Lüders, [English translation of the 1951 paper](https://arxiv.org/abs/quant-ph/0403007) | projective state-change proposal and compatibility theorem | begins with the measured observable/projectors |
| Ozawa, [*Quantum measuring processes of continuous observables*](https://doi.org/10.1063/1.526000), JMP 25 (1984) 79–87 | CP-instrument/measuring-process realization and no repeatable CP instrument for nondiscrete observables | realization theorem and repeatability boundary, not law selection |
| Busch, Grabowski, and Lahti, [*Repeatable measurements in quantum theory*](https://doi.org/10.1007/BF02055331), Found. Phys. 25 (1995) 1239–1266 | repeatability, first-kind, ideality, discreteness, and degenerate nonideality distinctions | repeatability alone does not give Lüders inside degenerate sectors |
| Buscemi, D'Ariano, and Perinotti, [*There exist nonorthogonal quantum measurements that are perfectly repeatable*](https://arxiv.org/abs/quant-ph/0310041) | nonorthogonal repeatability exists in infinite dimension, not finite dimension | blocks a universal “repeatable means PVM” claim while preserving the finite qubit reduction |
| Busch and Singh, [*Lüders theorem for unsharp quantum measurements*](https://arxiv.org/abs/1304.0054) | ideal nondisturbance/commutativity relation for supplied observables | does not derive the observable or actual outcome |
| Heinosaari and Wolf, [*Non-disturbing quantum measurements*](https://arxiv.org/abs/1005.5659) | nondisturbance, compatibility, and commutativity can coincide or differ by dimension/effect structure | “minimal disturbance” needs an exact definition |
| Carmeli, Heinosaari, and Toigo, [*Covariant quantum instruments*](https://arxiv.org/abs/0805.3917) | general structure and characterization of covariant-instrument families | covariance is a classifier, not generically a unique selector |
| Chiribella, D'Ariano, and Perinotti, [*Realization schemes for quantum instruments in finite dimensions*](https://arxiv.org/abs/0810.3211) | general finite-dimensional dilation schemes, including covariant families | realization does not identify nature's instrument |
| Barnum et al., [*Noncommuting mixed states cannot be broadcast*](https://arxiv.org/abs/quant-ph/9511010) | noncommuting state families cannot be broadcast | permits commuting pointer families and does not choose one |
| Ollivier, Poulin, and Zurek, [*Objective properties from subjective quantum states*](https://arxiv.org/abs/quant-ph/0307229) and [*Environment as a Witness*](https://arxiv.org/abs/quant-ph/0408125) | redundant environmental imprint and pointer-observable accessibility | conditional on split, interaction, state, and quantum information/probability structure; no one-branch selector |
| Horodecki, Korbicz, and Horodecki, [*Quantum origins of objectivity*](https://arxiv.org/abs/1312.6588) | spectrum-broadcast structure from nondisturbance/objectivity assumptions | structural objective records, not microscopic occurrence or single actuality |
| Batra, Dobrescu, and Spivak, [*Anomaly-Free Sets of Fermions*](https://arxiv.org/abs/hep-ph/0510181) | exact five-charge tuple, anomaly equations, minimum multiplicity, broad chiral completions | no quadratic-norm selection or microscopic-law connection |
| Costa, Dobrescu, and Fox, [*General solution to the U(1) anomaly equations*](https://arxiv.org/abs/1905.13729) | general integer solution and presentation freedoms | classifies anomaly solutions; does not select gauge group or dynamics |

## 12. Exact Runner Coverage

The companion checks:

1. the live foundation and primitive-registry boundary;
2. three inequivalent CP-complete repeatable instruments for one degenerate
   PVM;
3. a nontrivial covariant continuous family of repeatable instruments;
4. weak versus strong compatible-observable nondisturbance;
5. the binary-qubit sharpness reduction and rank-one branch uniqueness;
6. `X`/`Z` context nonselection on the same state;
7. isometric dilations for inequivalent instruments and Kraus-coordinate
   freedom within one instrument;
8. no-cloning inner-product separation, exact `X`/`Z` copiers, two-witness GHZ
   redundancy, and exact reversal;
9. nonselective mixture versus one actual branch and prepared-state-dependent
   weights;
10. exact equivalence of the Batra tuple to the repo quintet; and
11. the interface and N1–N8 source-note contract.

The PASS count is a contract/check count, not an independent evidence count.

## No-Go Discipline Gate

**No-go discipline status: `PASS`** for the narrow premise-bounded claims in
this note. Overall status remains
`partial-attempt-with-named-untested-routes`, because a completed microscopic
admissibility/interaction law could derive the context and strong ideality.
This is not a universal no-go.

The bounded negative is:

> Complete instrument consistency, repeatability/permanence, generic
> covariance, dilation/purification, and broadcast/objectivity constraints do
> not jointly select a unique physical record-forming instrument. Strong
> ideality selects Lüders form conditional on a supplied PVM; exhaustive binary
> qubit repeatability can also force sharp Lüders form, but neither route
> selects the physical context, firing event, actual branch, or statistics.

### N1 — Alternative-route enumeration

| route | marker | strongest attempted closure | exact residual |
|---|---|---|---|
| complete Davies–Lewis/Ozawa CP consistency | `ATTEMPTED` | defines/realizes the full instrument class | no member, context, firing event, or actuality selector |
| exact repeatability | `ATTEMPTED` | fixes output support; in exhaustive binary qubit case forces rank-one Lüders form | degenerate internal maps generally; context always |
| permanent invariant sector | `ATTEMPTED` | prevents reconnection under a supplied future-operation class | does not choose sector or operation class |
| strong minimal disturbance | `ATTEMPTED` | uniquely fixes Lüders map for a supplied sharp PVM | strong ideality premise and PVM remain supplied/derived elsewhere |
| spatial/internal covariance | `ATTEMPTED` | restricts Kraus intertwiners | exact continuous covariant counterfamily survives |
| purification / instrument dilation | `ATTEMPTED` | realizes every tested CP instrument isometrically | inequivalent instruments and pointer contexts all dilate |
| no-broadcasting | `ATTEMPTED` | restricts exactly broadcastable information to compatible/classical families | does not choose which commuting family is physical |
| quantum Darwinism / spectrum broadcasting | `ATTEMPTED` | gives objective redundant access to a dynamics-selected pointer observable | supplied interaction/split/state and no single actual branch |
| binary-qubit attainability plus repeatability | `ATTEMPTED` | strongest positive route: PVM and Lüders branch form follow | `X` versus `Z`, event occurrence, sample, and weights |
| composition/Bayes Lüders route | `RULED OUT BY PRIOR` | repo conditional Lüders row fixes normalized compression after trace/effect and sequential premises | those premises and physical context remain outside the four axioms; see `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md:207-222` |

Ten genuinely distinct routes are recorded. The negative claim is limited to
what these generic conditions entail, not every future microscopic theorem.

### N2 — Wall-independence audit

For a general finite record instrument, the collapsed residual set is:

- `C`: physical outcome context `{E_r}`;
- `D`: conditional disturbance map inside degenerate sectors;
- `E`: readiness and occurrence of the event;
- `A`: one actual outcome;
- `W`: prepared state, physical weights, and repeated-trial statistics; and
- `P`: exhaustive future-operation scope that makes the record permanent.

For an exhaustive repeatable binary qubit instrument, `D` collapses: rank-one
support forces Lüders. The other five do not.

| pair | first closes second? | second closes first? | exact separator |
|---|---:|---:|---|
| `C,D` | no | no | one degenerate PVM has three branch maps; Lüders form can be attached to `X` or `Z` |
| `C,E` | no | no | a PVM can be named with no firing rule; one ready event can use alternative PVMs |
| `C,A` | no | no | a complete context gives several branches; a hidden/global selector can choose without deriving the context |
| `C,W` | no | no | same state has different `X/Z` distributions; one context accepts many input states |
| `C,P` | no | no | block invariance can preserve any supplied PVM; a PVM alone does not restrict later maps |
| `D,E` | no | no | same readiness supports Lüders, rotated, or measure-prepare maps; a branch map has no schedule |
| `D,A` | no | no | one conditional map does not sample; a sample does not fix poststate disturbance |
| `D,W` | no | no | identical branch maps accept state-dependent weights; identical weights can accompany different degenerate postmaps |
| `D,P` | no | no | immediate update and all-future sector invariance are different contracts |
| `E,A` | no | no | a ready nonselective instrument has no selected member; a boundary history can select without local readiness |
| `E,W` | no | no | event schedule leaves state weights open; a measure gives no firing time |
| `E,P` | no | no | a firing event may write erasable or invariant tokens; permanence supplies no trigger |
| `A,W` | no | no | normalized weights are not a sample; one deterministic history supplies no ensemble law |
| `A,P` | no | no | one changing actual state need not be append-only; invariant sectors do not select one |
| `W,P` | no | no | Born weights do not make a carrier immutable; invariant carriers do not select state/frequencies |

No pair collapses except `D` under the explicitly narrower binary-qubit theorem.
The note uses the collapsed counts.

### N3 — Hidden-wall scan

The scientific body was checked for the skill triggers and close variants.

| phrase class | classification |
|---|---|
| “supplied PVM/context/interaction/state” | explicit physical condition, retained as `C` or `W` |
| “by construction” | avoided as a proof substitute; every finite construction has displayed Kraus operators or unitary |
| “standard instrument” | not used as authority; CP, completeness, effects, and outcome semantics are separated |
| “minimal disturbance” | promoted into weak and strong definitions; only the strong version closes `D` |
| “permanent” | scoped to an exhaustive future-operation family; otherwise not credited |
| “covariant” | group representation and outcome action are required; not treated as uniqueness |
| “objective/redundant” | accessibility classification, not actuality |
| “registered primitive” | registry checked directly; no primitive is enlarged into measurement content |
| “canonical Lüders” | representative/form statement only, not physical selection |

No new hidden condition was found after this classification. In particular,
attainability of both binary outcomes is explicit in the sharpness proof.

### N4 — Residual matching

| cited repository witness | residual there | residual used here | match? |
|---|---|---|---:|
| `LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md:312-327` | canonical `K_r=P_r` does not imply instrument uniqueness or a measurement axiom | dilation/canonical representative does not select physical instrument | yes |
| `RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md:169-180` | supplied pointer model gives projective Kraus isometry but not pointer observable, general persistence, Born law, or rate | realization and repeatability do not select `C/P/W/E` | yes |
| `RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md:46-56,148-164` | same qubit state admits different `X/Z` record kernels; context remains supplied | context nonselection `C` | yes |
| `RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO_2026-06-17.md:79-123` | projective/Lüders algebra does not select context, generator, or rate | form after context does not select `C/E` | yes |
| `FINITE_DIAMOND_SAMPLED_LUDERS_INVARIANT_RECORD_MODEL_NOTE_2026-07-14.md:127-161` | rank-one effect plus repeatable support fixes Lüders; weight form still consumes extra premises | positive reduction of `D`, no closure of `C/W/A` | yes |
| `BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md:115-135` | instruments supply branch maps/statistics after schedule/sample; one channel has inequivalent instruments | CP/channel consistency does not select physical instrument or actuality | yes |
| `BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md:235-254` | Darwinist redundancy gives accessibility but reversible copies do not actualize | redundancy does not close `A/P` | yes |

Every cited residual matches. No clock, gravity, chirality, or continuum no-go
is used as evidence for instrument nonselection.

### N5 — Rhetoric and resolution audit

| bounded negative phrase | tested resolutions | untested scope / required wording |
|---|---|---|
| repeatability does not select Lüders | exact degenerate qutrit block and primary finite/infinite repeatability literature | false for exhaustive binary qubit and for strong ideality; always carry those exceptions |
| covariance does not select the instrument | exact nontrivial finite internal-covariance family; primary general structure theorem | no theorem over every irreducible group/optimality package; say “generic covariance alone” |
| dilation does not select | exact finite qutrit instruments plus primary CP realization theorem | a specified minimal dilation plus a complete physical pointer interaction may add selection content; not tested universally |
| broadcasting does not select context | exact qubit `X/Z` copiers and primary no-broadcasting theorem | no classification of every many-body pointer algebra; claim only non-entailment from broadcastability |
| redundancy is not actuality | exact three-qubit reversible GHZ witness plus primary Darwinism/SBS sources | no infinite-volume superselection or collapse sector tested; say “reversible redundancy alone” |
| projective/Lüders form does not select physical read | exact one-site `M_2` `X/Z` separator and prior three-context control | no completed final admissibility law exists to test; claim stays conditional on current generic principles |

No lattice-wide or continuum impossibility is claimed from the finite
countermodels. The narrow theorem is a logical non-entailment because two exact
models satisfy the same premises and differ in the claimed conclusion.

### N6 — Partial-closure paths and primitive scan

Real closure paths are preserved:

1. derive binary exhaustivity, attainability, and exact repeatability from the
   final formation law; projective/Lüders form then retires automatically;
2. derive a pointer observable from the exact system/environment interaction
   and a no-hidden-disturbance theorem;
3. derive strong compatible-algebra ideality from the admissible-operation
   rule rather than postulate “minimal disturbance”;
4. let relational program records select `X/Z` settings as realized-state data,
   while keeping the law-level decoder covariant;
5. derive a unique physical interaction/action whose low-level instrument is
   the append law;
6. use a boundary/superselection theorem rather than stochastic sampling to
   close actuality; and
7. use a frame-weight/operational reconstruction plus repeated-preparation
   theorem to close statistics after events exist.

The registry contains only `minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. The last three do
not supply `C/D/E/A/W/P`. A proposed formation or measurement primitive absent
from that registry has zero premise weight.

This still does not imply “new axiom required.” The legitimate route is an
explicit conditional law, bounded theorems such as the binary-qubit reduction,
and an import-retirement audit. A complete law may make append-only formation
and Lüders form theorems without adding either phrase to Record.

### N7 — Strongest hostile steelman

A hostile reviewer should reject any broad no-go here. The framework has not
yet supplied its final nearest-neighbor admissibility law. That law could define
a unique relational interaction at every ready front; exact pointer
repeatability on one qubit would then force sharp Lüders branches by the theorem
in this note; the interaction's commutant and environment redundancy could
derive the `X/Z` contexts; and a low-record boundary or superselection theorem
could select one sector. In that construction, no independent measurement
axiom or instrument choice would remain. The primary realization and Darwinism
literature, together with the exact binary reduction, makes this route credible.
Therefore the only defensible negative is that the **generic principles tested
here**, without that microscopic law, do not uniquely select the read. The
overall result is correctly demoted to
`partial-attempt-with-named-untested-routes`.

### N8 — Cross-cycle echo

The prescribed repo phrase search and all `NO_GO_LEDGER.md` files were checked.
The closest exact echoes are:

- the June projective-Kraus note established a canonical representative but
  explicitly refused instrument uniqueness;
- the June prerecord/context no-go established `X/Y/Z` nonidentifiability;
- the June formation-to-isometry bridge made pointer observable, probability,
  and persistence residuals explicit;
- FD-SLIR later retired one piece by proving rank-one repeatability fixes the
  branch map;
- the July actualization audit separated instruments, redundancy, weights, and
  one-history actuality; and
- the post-record-selector ledger warns that normalized finite arithmetic is
  not selector authority.

One prior wall **was** partly retired: “Lüders must be separately imported” was
reframed as a theorem after sharp rank-one effect and repeatability are
supplied. This note applies the same mechanism one step earlier and derives
sharpness for the exhaustive binary qubit. It does not repeat the older broader
negative.

The same import-retirement mechanism may yet close context if a complete
microscopic interaction derives a unique pointer algebra. That route is the
N7 target and is why no universal no-go or new-axiom demand is made.

## Bottom Line

For the bare-metal framework, “a record is read” is still too opaque to be
axiom language. The mathematical content decomposes into a physical context,
a conditional branch map, a firing condition, a single actual continuation,
statistics, and a future invariance scope.

Instrument theory genuinely compresses that list. On the actual one-qubit
binary carrier, exact repeatability can force projective Lüders **form**. It
cannot tell the universe to read `X` here and `Z` there, cannot make a ready
event occur, cannot choose one branch, and cannot turn a state-dependent trace
weight into an observed frequency corpus.

So the correct next target is not another Record adjective. It is a
microscopic law/context theorem strong enough that binary repeatability becomes
a consequence. Once that law exists, the append-only and Lüders descriptions
should be proved from it and only genuinely irreducible formation content
should face the later constitutional decision.

## Verification

Run:

```bash
python3 scripts/record_instrument_selection_luders_primary_source_probe_2026_07_14.py
```
