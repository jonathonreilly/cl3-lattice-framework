# Exact Predictive Specification Tournament — Cycles 1–42

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is a local derive-first research packet. It does not
amend the framework axioms, add a premise node, set an audit verdict, or claim
that the final constitutional wording is ready.

## Question

What is the smallest substrate language capable of supplying or deriving the
ten fields in the canonical-law completeness contract, and which pieces remain
independent physical content rather than definitions or theorems?

The distinction tested here is load-bearing:

1. a **law type** says what kind of object a law is;
2. a **law value** gives the exact table, equation, kernel, action, or
   operational-equivalence class that makes predictions; and
3. a **record theorem** proves when an outcome becomes an invariant fact under
   that exact law.

Typing a law as local, covariant, causal, unitary, stochastic, or
instrument-valued does not identify its value.

## Cycles 1–8 Result

The leading expressive substrate candidate is not one object. It is the exact
tuple

```text
process/preparation state
+ compatible local outcome-labelled instruments
+ one-outcome sampling semantics
+ the post-formation family of record-preserving operations.
```

A process comb describes the multi-time environment into whose slots
instruments are inserted; an instrument describes an intervention and its
outcome-labelled completely positive maps. They are related by representation
and composition theorems but are not interchangeable names.

Once the entire tuple is supplied, it can express all ten fields without
confusing a nonselective channel with an actual result. Normalization gives
one-shot trace weights, explicit sampling gives one operational outcome, and a
future-operation restriction can make the selected record sector invariant.
Stable trial frequencies require a separately defined repeated-preparation
corpus or an ergodic/frequency theorem.

This is language-level closure, not yet a TOE law. None of the current four
axioms, the three registered primitives, the Wilson-plus-staggered action
surface, monotone continuation separation, or the representation theorems
selects this exact tuple. The first-cycle runner tests the negative separations
below. The later finite-diamond and full-lattice runners construct and exercise
the positive process architecture conditionally; they do not select it as the
physical law.

The leading bare-metal architecture therefore remains:

```text
exact process plus local instrument law
    -> one sampled outcome
    -> supported continuations and compatible concurrency
    -> post-sample invariant outcome blocks
    -> records and nonreconnection
    -> event order
```

Physical duration/lapse, the exact law value, the post-sample operation scope,
and any contingent global boundary or preparation data remain separate. Event
order alone does not fix a clock rate.

## Exact Finite Separations

The paired runner checks the following countermodel pairs.

### Availability does not determine continuation

On the ternary six-neighbour profile domain, let availability be the recorded
unanimous value when all recorded neighbours agree, and both labels otherwise.
Two translation-, proper-cubic-, and global-label-covariant support laws fit
that same availability rule:

- the full-support law retains every available label; and
- the majority-support law selects the strict recorded majority on mixed,
  unequal profiles while retaining both labels on ties and the empty profile.

They disagree on a `2:1` mixed profile. Thus even an exact availability table
does not determine physical successor support.

### Continuation separation does not determine actuality

If transitions only append a site-tagged label, siblings that write `0` and
`1` at the same site have disjoint future record cones. The same branching
graph nevertheless admits different selected maximal histories. A history,
boundary selector, deterministic tie-break, or sampled transition remains
needed for one branch to be actual.

### Continuation separation does not determine statistics

For a local profile with `n_0,n_1` recorded neighbours, both

```text
p_alpha(0 | n_0,n_1) = (n_0 + alpha)/(n_0+n_1+2 alpha), alpha=1
p_alpha(0 | n_0,n_1) = (n_0 + alpha)/(n_0+n_1+2 alpha), alpha=2
```

are local, normalized, strictly positive, global-label-covariant, and compose
as a product on disjoint simultaneous sites. They have the same continuation
support but give different probabilities on the `2:1` profile. Cylinder
normalization and disjoint composition therefore do not choose a kernel.

Uniform branch counting is not a rescue: splitting one operational outcome
into two presentation-equivalent microbranches changes naive branch-count
weights from `1/2` to `1/3` versus `2/3`. A physical quotient or measure is
needed before counting can be presentation independent.

### The nonuniqueness survives hard probability constraints

For the exact six-port menu used by the deeper route-two probe, define

```text
q_lambda(a | n) = lambda^(n_a) / sum_(b in A(n)) lambda^(n_b).
```

The `lambda=1` and `lambda=2` kernels have identical support and obey exact
normalization on all 729 local profiles, all 24 proper cubic rotations, global
label covariance, strict nearest-neighbour locality, product composition on
disjoint dependency regions, cylinder consistency for a stated update order,
and additive record expectation. They differ at one recorded-zero neighbour:
`1/2` versus `2/3`.

Even global presentation independence does not restore uniqueness. On the
eight-vertex periodic cube,

```text
mu_lambda(s) = Z_lambda^(-1)
               lambda^(number of equal nearest-neighbour edges)
```

gives two full-support, spatially covariant, label-covariant, nearest-neighbour
Markov random fields. Exact enumeration gives

```text
Z_1 = 256,                 P_1(neighbours equal) = 1/2,
Z_2 = 36,450,              P_2(neighbours equal) = 32/45.
```

Both cylinder families are consistent on all `3^8` partial records and
factorize on disconnected components.

### Locality, update order, and global consistency form a trilemma

On a three-site path, require a strictly local label-covariant reveal kernel
to give the same final weights whether the centre or endpoints are revealed
first. If `alpha` is the probability of repeating one recorded neighbour and
`beta` the probability of `0` beside two recorded zeros, schedule equality for
`000` and `010` gives

```text
beta = 2 alpha^2,
1 - beta = 2(1-alpha)^2.
```

The unique solution is `alpha=beta=1/2`. The route-two hard singleton menu has
`beta=1` and is incompatible with arbitrary order erasure on this path. The
finite result exposes three honest choices:

1. retain update order/context as physical data for a strictly local
   nonuniform sequential law;
2. accept the tested uniform kernel; or
3. use a globally consistent nonuniform Gibbs/history measure, whose reveal
   conditional given only a partial record can depend on remote recorded
   sites.

On the periodic cube at `lambda=2`, an opposite-corner record changes a site's
conditional `P(0)` from `416/675` to `259/675` even while that site's currently
recorded nearest-neighbour set is empty. This is not a universal no-go; it is a
finite discriminator that prevents the three meanings of “local” and
“order-independent” from being merged silently.

### Symmetry does not create a classical first result

From a homogeneous all-open state on a finite transitive lattice, a
deterministic result that is equivariant under translations and under global
`0 <-> 1` exchange cannot produce a nonempty classical record without an
additional asymmetry. Translation invariance leaves only constant
configurations, and label exchange fixes only the all-open one. A symmetric
distribution or coherent alternative can exist, but selecting one classical
label is extra dynamical or boundary content.

### A channel is not an actual outcome

The qubit dephasing channel

```text
rho -> P_0 rho P_0 + P_1 rho P_1
```

maps `|+><+|` to a diagonal mixture. The same two maps treated as an
outcome-labelled instrument give probabilities `1/2,1/2` and conditional
post-outcome states. The nonselective channel alone contains no variable saying
which outcome occurred. Decoherence or block diagonalization is therefore not
operational actuality.

### An exact equilibrium action does not identify a transition law

Take a two-state positive action with equilibrium law `pi=(2/3,1/3)`. Both

```text
K_1 = [[3/4, 1/4], [1/2, 1/2]],
K_2 = [[7/8, 1/8], [1/4, 3/4]]
```

are reversible with respect to the same `pi`, but their equilibrium transition
fluxes are `1/6` and `1/12`. Thus an exact positive action or Gibbs measure
does not, without a transfer/instrument prescription, fix record continuation
or physical event rate.

### Event order is not physical duration

One causal event chain admits multiple positive lapse assignments with the
same order and different elapsed durations. Formation events can define a
clock reading or tick count, but a rate/lapse theorem needs further dynamics.
The registered scale-reference primitive supplies a unit comparison only; it
does not select a lapse field.

## Candidate Tournament

`D` means definitional packaging, `T` means derivable after the exact atomic
law is supplied, `A` means a still-independent physical atom, and `B` means
contingent boundary/preparation data.

| candidate | exact strengths | irreducible residue exposed in this cycle | disposition |
|---|---|---|---|
| monotone availability closure plus invariant refinement | continuation, rank growth, disjoint update confluence, and nonreconnection can be theorems | exact activation/support law, allowed-operation algebra, actuality, statistics | strongest route-two reduct; incomplete law |
| process state + compatible sampled instruments + record-preserving future operations | exact contexts, composition, sampled outcome, one-shot trace weights, and fixed-record theorem are expressible in one architecture | exact process/instruments, sampling semantics, operation restriction, corpus, and boundary/preparation data are not selected | leading expressive candidate; finite construction under test |
| Wilson-plus-staggered action | provides a familiar conditional amplitude/dynamics surface and downstream matter/gauge calculations | Wilson action selection, staggered kinetic selection, context, actual result, record trigger, and normalized operational corpus remain unsupplied | downstream effective candidate, not the missing bare-metal law |
| global tensor/action history with normalized cylinder measure | can package concurrency, interference, boundary data, and record-cylinder statistics exactly | exact tensor/action, modulus-square/measure rule, boundary class, and one-history semantics must be supplied | viable only when those atoms are explicit |
| Wolfram-style multiway hypergraph rewriting | exact local rewrite support, event DAGs, update-order analysis, branchial structure, and candidate discrete covariance/gravity mechanisms | exact rewrite rule and initial hypergraph, physical branch quotient, actuality, robust weights, quantum/Bell map, and compatibility with fixed `Z^3 x M_2(C)` remain | serious inspiration route; causal-invariance/record tension under probe |
| error-correcting/topological archive | derives bounded robustness and sector separation relative to a restricted operation class | pointer, threshold, fresh support, operation cutoff, actuality, weights | record subtheorem, not a complete substrate |
| Bell-current objective-jump QCA | explicit actuality and equivariant quantum statistics are possible | wavefunction/configuration state beyond records, exact Hamiltonian/rates, equilibrium boundary | exact alternative, conflicts with present record-only state claim |
| deterministic or stochastic classical append-only CA | fills all ten fields exactly and is bare-metal executable | fails the independent-setting Bell/contextual quantum target unless locality, setting independence, or record-only completeness is relaxed | negative control |

## Theorem-Backed Operational Quotient

There is a precise physical-equivalence target for the instrument route:

> Two local causal implementations are equivalent exactly when every finite
> compatible family of record-ending instruments/testers gives the same
> transcript probabilities, including all declared interface labels.

For finite systems this can be checked by probabilistic reward bisimulation:
related states carry identical interface labels and send equal total
probability into every related class under every recorded context. It permits
unobservable implementation differences—adding a hidden toggling bit can
double the state space without changing any transcript—while separating two
laws as soon as one finite tester sees different probabilities.

The supporting representation stack is conditional but exact:

- [Chiribella–D’Ariano–Perinotti](https://arxiv.org/abs/0904.4483) represent
  deterministic combs by positive Choi operators with recursive trace
  constraints and realize admissible transformations by memory channels;
- [Milz–Sakuldee–Pollock–Modi](https://arxiv.org/abs/1712.02589) give the
  intervention-compatible extension theorem from finite processes to a
  global process;
- [Okamura–Ozawa](https://arxiv.org/abs/1501.00239) identify CP instruments
  with statistical-equivalence classes of measuring processes on the
  relevant atomic/type-I surface; and
- QCA/local-rule representation theorems can turn a supplied compatible local
  rule into global continuation, but do not select that local rule.

This quotient removes Kraus, ancilla, and apparatus presentation redundancy.
It does not derive the Choi entries or their probabilities. Informationally
complete testers reconstruct a supplied process from data; they do not predict
it from the four axioms.

### Probability reconstruction does not remove all probability content

POVM-Gleason reconstruction for a qubit requires a probability assignment on
all effects, positivity, normalization, and additivity across every POVM. A
process-matrix reconstruction similarly requires CP events, exhaustive
instruments, instrument noncontextuality, normalization, and sufficiently rich
ancillas before Choi positivity. These theorems derive the trace
*representation* from a physical probability package; they do not obtain
stable frequencies or one actual outcome from continuation support.

The stronger operational reconstruction route of
[Masanes–Galley–Müller](https://arxiv.org/abs/1811.11060) avoids taking outcome
noncontextuality as a primitive, but assumes a much larger package: Hilbert-ray
pure states, unitary reversibles, tensor composites, normalized outcome
functions, closure under mixtures and embeddings, an associative local outcome
product, and finite tomography. The current `M_2(C)` site presentation plus
generated finite composition supplies only part of that package. This route
stays live as a derivation program; it is not present closure.

### Two witnesses move to a downstream certificate

Spectrum-broadcast and redundant-record theorems can make two disjoint
fragments independently readable when their conditional states are orthogonal
and conditionally independent. They do not show that the second fragment
causes actuality or is the universal minimum formation trigger. In the
instrument/fixed-algebra route, two witnesses are therefore a readability and
robustness certificate after invariant-sector formation, not constitutional
formation content.

## Wolfram-Style Multiway Route

Multiway hypergraph rewriting is directly relevant because it cleanly
separates a local rewrite rule, the graph of all updates, causal dependency,
and update-order quotients. Its causal-invariance machinery can remove
scheduling presentation from physics. Causal invariance and Church–Rosser
confluence must not be conflated, however. A Wolfram Research bulletin gives
finite counterexamples in both directions: isomorphic causal graphs need not
end in one state, and confluent final states need not have isomorphic causal
graphs
([source](https://bulletins.wolframphysics.org/2020/11/confluence-and-causal-invariance/)).
The strong confluence reading—not causal invariance alone—has a precise tension
with records, because two distinct permanent same-site contents must not
reconnect.

One sufficient record-safe use is **sectorwise causal invariance**:

- update-order branches within one fixed outcome sector yield the same causal
  graph, and may reconverge when the rewrite is also confluent;
- record-forming outcome sectors do not reconnect, although their causal
  graphs may still be isomorphic; and
- the law still needs a selector or measure over those sectors.

This retains the useful Wolfram causal engine while treating the physical
outcome split as more than an update-order gauge choice. It also matches the
finite append result: two independent partial records have a common union,
while conflicting same-site contents have no append-only common future.

The weight issue is not hidden. The Wolfram technical discussion of
[weighted multiway graphs](https://www.wolframphysics.org/technical-introduction/the-updating-process-for-string-substitution-systems/weighted-multiway-graphs/)
itself notes that equal splitting can fail normalization under another
foliation and that path counting needs a later normalization. Exact rule
duplication gives the sharper physical-quotient control: two syntactic paths to
one record versus one path to another changes raw weights from `1/2,1/2` to
`2/3,1/3` without changing the collapsed outcome set.

Primary Wolfram-model work gives serious conditional results for discrete
causal/general covariance and candidate curvature/gravity limits
([Gorard](https://arxiv.org/abs/2004.14810)). Those results assume a rewrite
rule, causal-invariance/limit hypotheses, and a dynamic hypergraph rather than
the present fixed `Z^3` plus one-site `M_2(C)` carrier. They are inspiration
for `CONCURRENCY`, `CLOCK`, `CONTINUUM`, and `GRAVITY`; they do not yet close
the framework's exact rule, quantum instrument, actuality, record, or
statistics fields.

A targeted check of the latest official observer account strengthens rather
than weakens this boundary. Wolfram's 2026 ruliad essay explicitly separates
the formal collection of all paths from the extra fact that fixes an
observer's perceived path, and says there is presently no theory selecting the
observer's branchial location
([source](https://writings.stephenwolfram.com/2026/02/what-ultimately-is-there-metaphysics-and-the-ruliad/)).
The detailed observer essay likewise locates a particular outcome in the
observer's branchial situation rather than deriving it from the multiway graph
alone
([source](https://writings.stephenwolfram.com/2023/12/observer-theory/)).
The technical quantum-formalism page proposes path multiplicity, geodesic
bundle measure, and branchial phase as a route to amplitudes, while the
weighted-multiway page records the foliation and normalization failures of
simple equal-splitting weights
([quantum formalism](https://www.wolframphysics.org/technical-introduction/potential-relation-to-physics/quantum-formalism/),
[weighted graphs](https://www.wolframphysics.org/technical-introduction/the-updating-process-for-string-substitution-systems/weighted-multiway-graphs/)).
Thus observer equivalencing is a serious candidate for the physical quotient,
not a presently complete numerical measure or actuality theorem.

## Wilson-Plus-Staggered Field Audit

The repository's current source notes themselves bound this candidate:

- the Wilson bridge is explicitly internal to a supplied standard Wilson
  plaquette surface and does not derive action-form selection;
- the real-positive Wilson selector is bounded to a stipulated
  single-plaquette/leading-beta ansatz and named measure conventions;
- the July 10 kinetic countermodel proves that the current minimal surface does
  not select the staggered kinetic law or its corner structure; and
- neither action note supplies one recorded outcome, a record-formation
  certificate, or an operational trial corpus.

The action can be a consumer of an exact substrate or part of an exact
instrument's effective limit. It cannot currently replace the missing
substrate law.

## Provisional Ten-Field Classification

| field | monotone closure | exact process + sampled-instrument architecture | Wilson + staggered surface |
|---|---|---|---|
| `DOMAIN` | A/T | A/T | A, enlarged beyond one-site `M_2(C)` |
| `STATE` | D only if strong predictive sufficiency of records is proved | process memory or preparation-record reconstruction must be exact | quantum field state/path configuration supplied |
| `CONTEXT` | A | supplied compatible instruments and recorded settings | A |
| `ATOMIC_LAW` | A | A | A/conditional |
| `CONTINUATION` | T | T | amplitude composition only after action/measure choices |
| `AVAILABILITY` | T | T | not identical to record-forming support without a bridge |
| `CONCURRENCY` | T for disjoint sites; overlap order may be A | T from comb causality/compatibility | Euclidean contraction order is not operational event order |
| `RECORD` | A -> T after append/fixed-operation scope is supplied | A -> T from a supplied future-operation restriction | A |
| `ACTUALITY` | conditional: Record supplies actual record facts, while a complete history must be uniquely derived, owned by one-outcome law semantics, supplied as contingent world-history data, or reconstructed from records | the realized-state primitive licenses pointwise evaluation at one world-supplied state only; it does not supply a complete history | amplitudes/channels still need a normalized record-history measure theorem and a declared one-history/data interface |
| `STATISTICS` | A | one-shot trace kernel supplied; trial/frequency bridge A/T | conditional path-integral rule; operational corpus link A |

### The live “state is records” sentence has a precise test

Let complete histories `h,h'` have the same record configuration `R(h)`. The
record configuration is a sufficient predictive state exactly when every
finite adaptive future protocol has the same conditional transcript law from
`h` and `h'`. For a finite hidden/instrument kernel, this is strong lumpability
of every record fibre under every context and output.

Finite quantum fixtures show what must be encoded:

- `|+00>` and `|-00>` can carry the same ordinary preparation-complete flag;
  adjacent swaps transport their relative phase inside the light cone, after
  which a local `X` test distinguishes them perfectly;
- two instruments with the same immediate outcome effect can leave different
  post-outcome states, so instrument/preparation identity matters; and
- `Phi+` and `Phi-` have identical one-site marginals and `ZZ` records but
  opposite `XX` correlations. A relational phase record splits this restricted
  pair into the necessary predictive classes.

For unrestricted quantum continuations, the minimum state is the equivalence
class under all future protocol laws—information-equivalent to a density
operator or tomographically complete preparation/process-memory record. If the
full record configuration already contains that information, the live sentence
can survive. If it does not, reading or clocking cannot repair it after the
fact.

There is a separate Bell wall. An arbitrary mixture of local deterministic
response tables carried by shared classical records obeys `|CHSH| <= 2`; the
quantum target is `2 sqrt(2)`. A record-only nearest-neighbour Markov reading
therefore needs an explicit escape: quantum process memory, contextual/global
law, nonlocal response, measurement dependence, retrocausal/two-boundary data,
or a proof that the “records” already encode the nonclassical process rather
than a classical hidden variable.

### Append-only absorption is weaker than a global fixed algebra

Append-only semantics proves that a formed record is absorbing on its own
future cone. It does not imply that its projector `P` obeys
`Phi*(P)=P` on every pre- and post-formation state. For a CPTP map, that
two-sided equality holds exactly when every Kraus operator commutes with `P`.
One-way record stability only requires `(I-P) K_i P=0` and permits inflow from
open states. The constitution must not silently replace branch-relative
permanence with a stronger global superselection algebra.

## What This Does To Candidate Axiom Language

No final sentence is frozen by this cycle. It does rule out three tempting
shortcuts:

1. “continuations do not reconnect” cannot by itself supply outcome occurrence
   or weights;
2. “the clock locks the record” confuses an order/rate consumer with the
   invariant that makes a record; and
3. “one fixed instrument exists” is still not predictive unless the exact
   instrument or its exact physical-equivalence class is supplied or uniquely
   derived.

If an exact instrument law is found, the Record clause can plausibly shrink to
an invariant-outcome definition and permanence/nonreconnection can become
theorems. If no such law is derived, the minimum honest constitutional content
is not merely a polished formation sentence: it includes an exact law
reference.

The exact route-two finite census reinforces that boundary:

- one varying availability menu admits 2,187 distinct nonempty
  label-equivariant continuation-support tables;
- the full eight-site append candidate has 6,427 reachable partial records,
  29,392 edges, 12,216 nonvacuous same-site splits, and 254 terminal records;
- those terminals are reached by 4,843,392 complete histories with path
  multiplicities ranging from 456 to 40,320; and
- independently toggling operational, time, individuation, resource/gravity,
  and boundary labels yields 32 full-interface completions of one bare record
  support graph.

The graph is a real nonreconnecting substrate candidate. It is not already its
own unique TOE completion.

## Cycles 4–6: Constructive Closure And Remaining Boundary

The later probes close several questions that were still phrased as future
work above.

### The sampled-record architecture is mathematically coherent

The finite-diamond sampled Lüders invariant-record model supplies an exact
conditional construction with normalized branch maps, one explicit sample,
repeatability, record-preserving future operations, projective cylinders,
exact `2 sqrt(2)` CHSH statistics, and no-signalling marginals. A compatible
family on every finite causal diamond extends to the quasilocal `Z^3` carrier
and to a probability measure on infinite record histories when the generated
tensor net, event domain, decoder, instruments, gluing, sampling, preservation,
projective compatibility, and renewal/export conditions are supplied.

This proves existence and compatibility. It does not derive the supplied
instrument entries, their physical context repertoire, the one-history
sampling instruction, the event net, or the renewal rule from the four
axioms.

### A causal front is the strongest bare-metal record model

The clock thought becomes exact only when “clock” means a causal transaction
phase. The commit samples and writes one outcome and moves the process into a
future operation domain that preserves that outcome. An outcome-blind tick is
not a witness; an outcome-conditioned front can be a second witness, but the
resulting GHZ correlation is unitary and exactly reversible. Redundancy alone
does not select an outcome or make it permanent.

One `M_2(C)` can carry the two locked contents but not a third orthogonal
`open` value. The open/locked bit may instead be the absence/presence of a
record or an endogenous front state. Any dynamically relevant front phase
must be recoverable from the present record configuration; otherwise equal
record configurations have different futures and `state = records` fails.

### Symmetry sharply narrows kinetics but does not select a full law

Common-basis `SU(2)` covariance reduces a two-qubit autonomous pair generator
to `span{I,SWAP}`. After pair-additivity and removal of the scalar term this
leaves exchange up to sign and scale. Independent onsite covariance instead
leaves only the identity. Continuous exchange has quasilocal propagation
tails, not an exact circuit cone, and cannot create an absorbing record on the
same reversible carrier.

The stronger three-dimensional isotropic Weyl-walk classification uses the
eight-neighbour BCC graph, not the live six-neighbour cubic adjacency. It also
leaves two chirality partners; a Dirac automaton needs a larger coupled carrier
and a mass parameter. A block/staggered realization on the current lattice
remains live, but no direct Lattice or Qubit amendment is justified by this
classification.

### Permanent storage creates a renewal constraint, not a formation rule

A bounded archive of permanent site-tethered records saturates. Sparse
formation delays saturation but does not renew capacity. Infinite `Z^3`
permits export at unbounded radius, while migration/export needs a physical
lineage relation saying which later carrier is the same fact. This is a full-law
job; it does not by itself force an extra Record sentence.

### Record-conditioned capacity is local, not yet gravity

Hard removal of exchange edges incident on a record makes that pointer value
invariant relative to exchange-only dynamics and gives a covariant local
throughput field. The direct response is exactly one edge deep, its energy sign
follows the free exchange sign, and a permanent archive leaves a saturating
trail. A separately supplied discrete Poisson inverse creates an approximate
`1/r` window, but that inverse, its source, coupling, and clock/lapse map are
additional law content.

### Corrected law inventory

Under exact normalized-instrument typing, the uncompressed conditional-law
core has ten semantic jobs: generated carrier; record status and identity;
event/readiness domain; predictive record decoder; context repertoire; exact
normalized local CP instruments; gluing and exhaustive continuation; one
actual history; projective full-lattice extension; and renewal/export.
Positive support and one-shot weights then derive from the instrument, writing
derives after actuality, and the operational physical quotient derives from
the complete intervention law. `FORMATION_ELIGIBILITY`, trial-corpus
semantics, and actual cosmological boundary selection remain separately
conditional only when the intended claims require them.

One exact local law can package and derive several of these jobs. Naming that
law once is syntactic compression, not a proof that the jobs disappear. The
current constitutional blocker has therefore narrowed, not multiplied:

> identify the exact physical law value, or prove the exact operational
> equivalence class that contains it.

Until that succeeds, neither two-witness prose nor a causal-front slogan makes
the foundation predictive, and no final axiom cut is scientifically ready.

## Cycles 7–8: Exact Reductions, Bell-Capable Construction, And Selection Wall

The next probes remove three possible reasons to enlarge the visible axiom
surface while strengthening the exact-law lower bound.

### Neither BCC adjacency nor a larger primitive site is forced

The published BCC Weyl macro-step factors exactly into three conditional
shifts along the standard cubic cardinal edges. A finite block also carries
the larger Clifford/Fock sectors needed by Dirac, Wilson, and staggered
realizations. These are exact compatibility results, not selections of a
physical kinetic law.

The exact covariance tournament goes further. The direct sum of all six axis
orders is a finite-range, unitary, fully proper-cubic-covariant `M_12` walk
with six identical Weyl first derivatives. A cubic-invariant onsite mixer
separates one two-dimensional low-phase Weyl sector from five orientation
modes at the origin. Four primitive qubits have enough carrier dimension for
an `M_12` code inside `M_16`.

That construction proves existence on a derived finite block and removes an
exact-covariance obstruction. It does not derive the code, mixer phase,
spectator treatment, physical tick, handed sector, eight-corner Floquet
content, interactions, or record instrument. `M_12` is minimal only inside
the tested six-order permutation-orbit completion. Smaller coherent
dilations and arbitrary primitive-`M_2` paraunitaries remain open.

The primary-source audit reaches the same constitutional boundary from the
classification side. The strongest two-component uniqueness theorem selects
a BCC single-particle walk under its own smaller isotropy representation, not
a standard-cardinal, all-24, many-body primitive-qubit law. On the actual six
cardinal directions, exact full-cubic unitary walks form a continuous coin
family. Identity and a cubic-edge controlled-`Z` circuit also give distinct
exact full-cubic primitive-qubit QCAs. Spatial symmetry, finite propagation,
unitarity, and the current carrier therefore do not identify the update.

### A coherent Bell-capable record process fits the present carrier

`CFSI-Q7` is an exact seven-site conditional construction on one `M_2(C)` per
site. Boundary/program records supply a preparation phase, two settings, a
common relational frame, and a causal policy. Nearest-neighbor gates prepare
and propagate a Bell pair to two front sites; commuting local instruments
sample and append their outcome records. The runner verifies exact

```text
CHSH = 2 sqrt(2),
```

no-signalling marginals, repeatability, record-sector preservation,
Alice/Bob linear-extension invariance, projective finite cylinders, coherent
source reset, and indefinite fresh-site allocation on a boundary-oriented
`Z^3` ray.

This closes the objection that the earlier causal front was necessarily
entanglement-breaking. It also cleanly separates formation from later readout:
the atomic normalized branch selection and append form the record; a later
compatible read only reveals and preserves it. No reader, second witness, or
ordinary clock is needed as a constitutional trigger.

The state test is exact but bounded. Outcome values alone are not a
predictive state. In the binary preparation family, `Phi+` and `Phi-` have the
same local marginals and `ZZ` transcript but opposite `XX` futures; one
preparation-phase record bit is minimally required. Outcome identity also
includes its recorded setting. Causal predecessors must be reconstructed from
records and boundary or retained as provenance. With the complete declared
packet, equal records give equal tested future cylinders at atomic transaction
boundaries; hidden randomizer identity has no later predictive effect.

The construction remains a programmed architecture rather than an autonomous
homogeneous TOE. The Bell state, gates, angles, trace kernel, one-branch sample
instruction, frame, causal decoder, atomic scope, and allocator are supplied.
Replacing visibility `v=1` by `v=1/2` preserves the architecture and outcome
support while changing `CHSH` from `2 sqrt(2)` to `sqrt(2)`. Thus even the
complete causal quantum interface does not select its exact law value.

### Wolfram-style causal invariance removes schedule, not causal input

A new exact schedule control identifies the useful part of the multiway idea.
If events read fixed causal predecessors, every linear extension gives the
same joint record law; total simulator order is presentation. If an
asynchronous event instead reads whatever record happens to exist when it is
executed, two opposite orders give `00/01` versus `01/11` terminal laws.
Those differences are permanent and readable. Randomizing the schedules
creates a third law rather than a quotient.

Therefore a final law may replace a global synchronous clock by an invariant
causal predecessor relation plus a linear-extension theorem. It cannot omit
both. Noncommuting split-step orders likewise differ at second order and are
not causal gauge merely because they share a Weyl continuum derivative. A
coherently mixed order register is physical carrier content unless a future
causal reconstruction proves otherwise.

### Symmetry and refinement do not select counting

All 64 binary six-neighbor colorings form ten proper-cubic rotation orbits.
After outcome-name exchange and homogeneous-copy behavior, three exact kernel
parameters remain. Even requiring dependence on counts alone leaves two.
Incidence, label-uniform, quadratic-power, and shape-sensitive kernels all
obey the tested covariance/support conditions and predict different records.
Proportional refinement leaves every homogeneous power kernel intact.

Finite additivity over **physically identified disjoint elementary causal
channels** does force linear weights and hence incidence probabilities. That
is the positive theorem route for “one ticket per possibility.” It requires
the exact law to identify those channels and their coarse-graining. Record's
additive scalar readout of already formed records is logically independent
and is shared by all the inequivalent kernels. No generic counting sentence
is therefore justified in Record.

### Cycle-8 constitutional reduction

After these controls, the presently justified minimum is narrower:

```text
not forced into Lattice:
  BCC adjacency, a preferred axis schedule, or a new clock direction

not forced into Qubit:
  a larger primitive onsite algebra, conditional on generated finite blocks

not forced into Record:
  reader, witness count, clock trigger, Born/counting rule, or schedule

unavoidable unless uniquely derived:
  one exact predictive law value, or one exact operational-equivalence class
  that fixes every finite record transcript

branching-law type requirement:
  a normalized measure on complete physical record histories; Record plus the
  world-supplied history and the realized-state reference already give
  occurrence and a licensed pointwise evaluation
```

Site-tagged permanence, composition, state representation, support,
probability representation, causal schedule, and renewal can all be theorems
of a sufficiently complete exact law. The current four axioms do not select
that law. A placeholder architecture name cannot fill the gap.

## Cycles 9–11: Actualization, Autonomous Initiation, And Resource Gravity

The next three cycles attacked the strongest remaining ways that a short
bare-metal slogan might have supplied the law indirectly. They did not enlarge
the constitutional minimum. They did substantially improve the constructive
picture downstream of an exact law.

### Copying and clocks do not actualize a branch

The primary-source actualization audit and its finite controls separate five
operations that earlier prose had allowed to blur together:

```text
causal readiness
coherent correlation or copying
nonselective physical channel
labelled branch instrument
one actual record append
```

Two controlled copies of a qubit can be reversed coherently. Adding a second
witness therefore increases redundancy without selecting one component of the
global state. A clock can define causal order or count commits, but advancing
it does not turn a nonselective channel into one sampled branch. Every audited
route that produces one public append history places the missing information
in an exact sampled law, a deterministic unique continuation, or physical
boundary/history data.

This does not prove that fundamental stochasticity is necessary. A
deterministic exact law can remove a separate sampling atom. It then carries
the outcome choice in its exact successor function and still does not remove
the exact-law identity obligation.

### Homogeneous initiation can be local, but its measure and law value remain

A positive-density factor construction now gives a translation- and
proper-cubic-covariant set of sparse candidate events without a privileged
origin. A repaired relational binary carrier represents every four-bit word
using only equality or complement relative to a physically recorded rank-one
reference. Global label complement and simultaneous algebra conjugation leave
the decoded packet invariant.

This closes two genuine architecture problems: homogeneous local candidate
selection is possible at positive density, and a fixed absolute `P0/P1` basis
is unnecessary. It does not yet give the microscopic law. The activity,
random marks, actual sample, all-open initiation layer, cross-site transport of
the relational reference, and Bell kernel remain supplied. The ten-record
program packet is a finite-radius atomic write, not a compiled nearest-neighbor
process. Changing the activity or kernel preserves the architecture and
changes predictions.

The paired deterministic control is equally informative. A deterministic
translation-covariant map from a fully translation-invariant all-open input
cannot output one finite asymmetric classical packet. Positive-density
stochastic nucleation, coherent symmetry breaking followed by actualization,
a pre-existing physical boundary, or a global history constraint remain live
escapes. This scoped obstruction is not a new axiom need.

### A local resource law can derive a gravity-shaped Green response

The Cycle-9 conservative resource probe is the first positive construction in
this campaign to derive a controlled inverse-distance profile from strictly
local cubic transport rather than insert `1/r` into a microscopic kernel. Its
one-point debt field obeys a discrete diffusion equation; a maintained local
commit/export current converges to the corresponding lattice Green profile.
The finite window has `R^2 > 0.9998` against `a+b/r`. A common scalar scheduler
then gives every tested local clock the same fractional gap response.

This makes the storage/compute intuition scientifically useful in a precise
conditional form: a commit may source a locally conserved resource deficit,
and conservation can spread the bookkeeping cost nonlocally. It does not make
“the universe is compute-limited” an axiom. The construction still needs the
exact current, mass-to-current map, coefficients, renewal/export, and common
matter coupling.

### Reversible closure moves rather than erases the thermodynamic cost

The Cycle-10 attack gives the lazy cubic diffusion step an exact finite-range
unitary dilation and gives a local edge average a one-ancilla reversible
dilation. Reusing one finite coin is ballistic and recurrent rather than
diffusive; fresh environmental degrees of freedom reproduce repeated Markov
powers. A fixed finite system plus finite environment and fixed unitary cannot
realize a genuinely mixing finite Markov semigroup for all times, because its
expectations are finite almost-periodic sums. An infinite lattice environment,
ever-growing tape, time-dependent law, or fundamental nonunitarity remains
open.

A fully local two-layer return cycle removes an ideal token sink and retains
the Green equation. Nonzero stationary current, however, requires nonzero
cycle affinity; detailed balance kills both current and the nonconstant Green
amplitude. The external sink has become an explicit arrow/fuel condition, not
disappeared.

The same attack prevents a scalar-clock overclaim. Identical onsite lapse
blocks permit different spatial propagation, and pure lapse gives the
`gamma_PPN=0` deflection `2GM/b` rather than the GR value `4GM/b`. The resource
route has a real Newtonian-shaped opening, but tensor transport, lensing, and
nonlinear gravity remain law/theorem work.

### Structural language still does not select the law

The independent qualitative-language probe closes the last easy rhetorical
escape. Local positive normalized label-covariant kernels form a continuous
family with different predictions. Requiring reversibility does not select a
member: the partial-swap family

```text
U_theta = cos(theta) I + i sin(theta) SWAP
```

is unitary, exchange-covariant, and covariant under every simultaneous
one-qubit basis change for every `theta`, while its transition probability is
`sin(theta)^2`. `Local`, `causal`, `covariant`, `reversible`, `minimal`, and
`compute-limited` can each be important constraints. Their conjunction is not
an exact rule unless a uniqueness theorem fixes all remaining values.

### Deterministic uniqueness does not select its component or law

The strongest deterministic escape now has an exact positive and negative
boundary. A uniquely extendible law needs no sampled-branch instruction, and a
uniquely ergodic irreducible component can derive long-run decoder
frequencies. Permanent distinguishable record cylinders are forward invariant,
however. Whenever two stable archives are lawful, each supports an invariant
measure, so their union is not uniquely ergodic. Component and decoder remain
law or boundary content.

Deterministic translation covariance also preserves an all-open homogeneous
input and cannot produce one sparse classical archive without a boundary or
other symmetry-breaking input. For Bell experiments, a local deterministic
response with one setting-independent hidden distribution obeys `CHSH <= 2`.
The quantum table is possible only after the exact theory exposes
measurement-dependent boundary correlation, nonlocal/joint-context response,
or a global constraint. Determinism can compress actuality and statistics; it
does not identify the exact function.

### Counting and chirality remain exact-law or boundary content

Two explicit positive normalized `M_2(C)` instruments fit the same four-axiom
envelope. One ties a conjugate pair into physical atoms `{s,d}` and assigns
equal weight `1/2`; one retains `{s,d_plus,d_minus}` as three physical effects
exchanged by conjugation and assigns `1/3`. Under the named energy and mass
bridges they give the distinct chains

```text
1/2 -> r=1/2 -> Q=2/3,
1/3 -> r=1   -> Q=1.
```

Finite additivity derives atom-count weights only after the exact physical
event algebra, operational quotient, and equal-atom symmetry are supplied.
Record readout additivity does not provide those objects.

Proper-cubic covariance likewise admits determinant-opposite mirror-law twins.
The six-neighbor Weyl corners and six-order block have balanced hands, and a
domain wall obtains a hand from its supplied profile. No counting or chirality
sentence is justified in Record.

### Infinite reversible export is real but boundary-relative

An exact 22-qubit-per-macrocell QCA correlates a signal with a local relational
record and exports inverse information on a proper-cubic-symmetric spent shell
and witness rails. In an isolated infinite blank no-return sector, the local
record is stable and the global dynamics remains unitary.

The same construction gives the boundary sharply. A finite torus returns the
shell and reverses the record; incoming inverse shells and positive-density
witness collisions do the same on `Z^3`. The global state retains both GHZ
branches, and Bell-phase recombination separates states with identical
decoded equality records. Fresh blank rails are low-record boundary fuel, not
a theorem of the QCA.

In finite dimension, an invariant record subspace under a unitary is reducing,
so its blank complement cannot enter it. Reversible formation plus absolute
permanence therefore needs an infinite proper invariant/superselection sector
or an explicit no-inverse domain. Fundamental irreversible append remains the
other route. Neither is selected by a read or clock. The macrocell has also not
been compiled into the fundamental one-`M_2` lattice with unit-translation and
proper-cubic covariance.

### Cycle-11 constitutional reduction

The new constructive results refine where the missing pieces live:

```text
can be exact-law fields or theorems:
  relational binary carrier, causal readiness, coherent propagation,
  instrument support, homogeneous event allocation, record preservation,
  renewal/export, local resource transport, clock response

remain boundary/history rather than microscopic-axiom content:
  actual cosmological seed, low-record condition, random sample or deterministic
  initial state, invariant component/domain, blank no-return sector, and any
  nonequilibrium boundary sustaining an arrow

remain exact quantitative law content unless uniquely derived:
  update value, event activity, branch kernel or deterministic successor,
  physical event quotient, chiral sign, interaction angles, resource current
  and couplings, transport geometry

not justified as Record additions:
  reader, two-witness trigger, clock lock, probability/counting rule,
  chirality selector, storage budget, or gravity slogan
```

Within the declared inventory and routes tested to this point, the
universal-looking residue is unchanged: one exact predictive law identity, or
one proved exact physical-equivalence class, unless the present foundation
uniquely derives it. Deterministic, law-owned, reconstruction, and contingent-
history routes prevent a stochastic actualization sentence from becoming a
proven universal second atom. No final sentence is frozen and no axiom edit is
authorized by this tournament.

## Cycles 12–17: Autonomous Append, Exact Equivalence, And Law-Selection Boundary

The later cycles substantially strengthen the constructive side without
changing that bounded universal-looking residue.

### Programmed and self-writing append laws derive formation language

One fundamental `M_2(C)` per actual site can host a finite relational program,
nearest-neighbor `CZ-X-Z` Bell interaction, record-visible causal phase, and
collision-safe append front. In that exact transition list, a record forms
only as a permanent local extension of the record configuration. The sentence
is a theorem of the law, not another Record atom.

A self-writing version removes the prewritten infinite program and unknown
fresh-site preparation in an isolated-front sector. Seven seed records and a
record-visible reset certificate propagate the header through nearest-neighbor
builder layers, consuming twenty-two fresh sites per cycle. The exact costs
are reset or reversible archive, finite seed, blank corridor, collision law,
actuality/weights, and rate.

Same-content multi-front growth has one abelian compatible-union closure under
every fair schedule. Different contents proposed at one permanent site have
no common append extension. Thus duplicate-cause order can be derived away,
while genuine conflict must be prevented, routed, globally constrained, or
selected before locking.

A delayed-lock protocol gives that upstream idea exact finite content. Two
coherent fronts leave permanent wakes, terminate at finite named ports, write
two local close certificates, and only then lock one symmetric parity fact.
Within the supplied law this is local, covariant, record-driven, and
schedule-independent. It cannot certify that nothing will arrive through an
unbounded unclosed channel: for every finite radius, a farther source has the
same local record prefix. The close rule is therefore a theorem of a law with
finite-interface and conserved-front semantics, not a free Record clause.

The autonomous successor removes that supplied interface after one realized
seed. A homogeneous radius-one law builds an exact 99-site cubic fence,
generates its stops, prepared proposals, ports, and close records, and commits
Bell parity only after the shell closes. It supplies no first localized seed:
the all-open homogeneous state makes every site fire or none, and all-site
nucleation creates immediate overlap. The formation/closure language is thus
a theorem of the post-seed law, while nucleation and arbitrary-seed collision
remain exact-law or boundary content.

The invariant-seed follow-up replaces the misleading demand for one uniformly
located global first record. A finite-torus exactly-one seed law has an empty
local limit, and no translation-invariant probability on infinite `Z3` is
concentrated on one finite nonempty seed set. Nevertheless a finite-range
positive-density hard-core seed process exists. At the tight frame-independent
exclusion radius nine its intensity is

```text
[1-(1-q)^6859]/6859,
```

and it produces infinitely many collision-safe seeds almost surely. A periodic
invariant-orbit construction supplies another exact seed field. The broad
homogeneous-nucleation obstruction is therefore false. Nearest-neighbor
one-`M_2` compilation, the numerical kernel/rate, and the actual history remain
law or boundary content.

The compilation follow-up retires continuous priorities. An
**isolated-Bernoulli factor** is covariant, finite-bit, positive density, and
collision-safe. Its origin decision depends on the cube corner at graph
distance 27, proving the exact nearest-neighbor causal-depth floor is 27. A
typed source-tagged monotone DAG reaches the bound and is schedule-independent.

The direct one-qubit append compile still fails its clean interface. It assumes
a closed candidate antichain, transient mutable messages, and garbage
disposal; a local direct controller needs four classical cases; and permanent
loser/message records cannot rewrite and can block a required diamond site.
This is a **record-only clean-output obstruction**, not a universal QCA or
dissipative no-go. Clean garbage export and autonomous finalization remain the
exact target.

The quantum/dissipative escape now fixes the reference behavior exactly at
range nine. A guarded, branch-labelled pure-birth instrument with independent
exponential attempts and 24 covariant frame outcomes produces permanent
positive-density seeds without a global synchronous clock. Direct positive-
rate NN commits cannot reproduce it because disjoint conflicting jumps can
both occur. Strict product-noise circuits need depth at least 14 to
anticorrelate a forbidden corner pair, while the isolated-candidate function
retains the depth-27 dependency floor. A bounded Lindbladian cannot reach an
exact terminal projection at finite deterministic time, though individual
absorbing jumps can occur at random finite times. Reversible QCA computation
must retain arbitration information; capacity and local geometry keep
collision-safe spatial export live, while one naive opposite-frame rail fails.
Finally, an averaged dephasing channel admits record-inequivalent instruments,
so formation must be owned by the branch-labelled law rather than inferred
from a channel, reader, or clock. No new Record sentence follows.

The commit-clock theorem also retires the causal slogan. A clock does not make
a record lock. After the exact event law generates a named append-only commit
chain, its count is a monotone, additive, schedule-invariant relational clock.
It is not automatically total record count or longest-chain length; a readable
intermediate record changes tick count and additive cost. Two positive rate
laws share event-order support but have different waiting times, and a common
capacity bound admits distinct utilizations. Absolute parameter rescaling may
be convention, while dimensionless clock ratios and tensor response remain
law content.

### Physical equivalence must preserve complete record protocols

The classified Weyl pair is conjugate after transporting a staggered phase
frame, context, and boundary. The live foundation safely licenses
translations, proper cubic rotations, and common complex-linear one-site
recodings with complete decoder transport. It does not license reflections,
arbitrary site-dependent frames, or fixed-protocol relabelings. The smallest
safe current referent is two proper-chiral presentation orbits, pending a
record/context theorem that either equates or separates them.

Intrinsic simulation is also weaker than physical equivalence. A simulator
phase that becomes a permanent record changes readable transcripts, additive
readout, causal depth, and capacity. Hiding it can make equal record states
predict different futures, and path refinement can change naive `1/2` weights
to `2/3`. The zero-edit equivalence route therefore needs full abstraction for
every finite record protocol, not common computability or causal reachability
after subdivision.

The universal all-rules steelman does not evade that requirement. In the
finite Boolean control, the all-rule union on a de Bruijn cyclic seed permits
every eight-bit successor. Symmetry still leaves identity and complement
members with distinct records; equal causal DAGs do not make those records
equivalent; syntax aliases and code assignments make naive weights
compiler-relative. A universal multiway object remains a live exact
architecture only after its grammar, record-faithful quotient, and
measure/selection/actuality reading are exact.

Observer boundedness does not by itself make that quotient exact. For every
finite horizon, paired laws can agree on the entire observed prefix and differ
at the next permanent record; a persistent bounded observer can later read the
separator without storing the prefix. The resource/protocol bound or
all-finite-record equivalence must therefore be stated and tested.

### Actions, topology, conservation, and Ward identities compress but do not select

A unique frustration-free history action can embed different update matrices
with the same spectrum. A transcript-distance functional can select any target
law by containing its target. One scalar wrapper is not one derived physical
principle.

Topological quantization can fix a magnitude to `plus/minus 1`; exact identity
links can collapse five signs to one mirror pair; and one conserved current can
be the record increment, exported information unit, Green source, and causal
tick. The scoped anomaly-plus-minimum-norm problem also uniquely selects
`(-9,-5,-1,7,8)` up to presentation. Conservation still admits zero and
nonzero event sectors and does not trigger formation.

The exact proper-cubic QCA implementation confirms the boundary. A generated
six-direction carrier transports the unit, but the cubic collision commutant
retains two phase ratios. The same number Ward identity permits quarter, half,
or unit transfer and fixes vacuum. After occurrence is supplied, spatial
orientation, actual sector, metric rate, tensor response, and species coupling
remain paired. QCA/Ward language is therefore a theorem mechanism, not a law
referent.

A later boundary-index construction derives a covariant outward normal after
a record exists. Its six nearest-neighbor record gradients transform under
translations and all proper cubic rotations, and six outward rails carry shell
wire-flow index `64`. This removes an absolute boundary direction. It does not
nucleate the first record: with no record the normal vanishes. The same index
also admits distinct occurrence domains, transfer amounts, collision phases,
coherent or actual instruments, tensor responses, and species couplings.
Index language therefore identifies protected transport, not the complete
record law.

The genuine 3-D anomaly follow-up strengthens the protected-bulk side. An
explicit three-fermion Clifford QCA has the required anomalous boundary
algebra, though its cubic realization is compiled at six qubits per cell. The
class is defined modulo finite-depth circuits: proper-cubic primitive
`CP(pi/2)` and `CP(pi)` edge layers have different entangling strength while
leaving the same general circuit-quotient bulk class. Hence the category can
constrain boundary algebra and sometimes hand, but not the microscopic
representative, event instrument, or first record. A primitive one-site
compiler plus record-observable representative theorem remains live.

The primitive representative probe supplies the needed distinction. Same-
class non-Clifford proper-cubic one-qubit phase circuits are separated by a
fixed decoder, including opposite deterministic record contents. If the
finite-depth representative and every record branch are transported together,
the complete one-step probabilities, conditional states, labels, and future
content reads agree exactly. The referent must therefore be the
update-plus-commit protocol or a proved complete-protocol equivalence class.
A bare update/anomaly class is insufficient.

The finite adaptive follow-up closes the algebraic multi-time problem exactly.
For any finite adaptive protocol tree, transporting each branch through
history-dependent frames gives a functor with inverse and a natural
isomorphism. It preserves instrument completeness, every transcript
probability, normalized post-record states, all transported future reads, and
record-defined clock/resource functionals. The primitive phase family even
admits uniformly local bounded-depth frames at every repeated time.

That is physical gauge only inside a protocol category closed under the whole
transport. An entangling phase frame preserves local `Z` records but maps a
one-site `X` record to a two-site operator, can change a fixed coherent
boundary, and ceases to be cost-neutral if its implementation writes a
readable phase or schedule record. The remaining equivalence question is
therefore record-net closure—site identity, one-site record locality, boundary,
and additive cost—not finite adaptive algebra.

The maximal foundation-level closure can now be classified. Any star
automorphism of a finite tensor product that permutes the named one-site
`M_2` factors is a site permutation followed by onsite unitary recodings. The
exact two-qubit census finds `720` maps in `Sp(4,2)` but only `72` that permute
the site planes. Entangling `CZ` preserves local `Z` yet sends local `X_1` to
the distributed `X_1 Z_2`. Hence translations/proper cubic maps plus common
onsite recoding are foundation-licensed; a larger entangling quotient is
possible only inside a law-selected record category with proven pointer,
boundary, and additive-cost closure.

The complete classification makes the representation fork explicit. With the full
named net fixed, the bare group is `PU(2)^n semidirect product S_n`; a common
onsite recoding additionally needs a homogeneous content dictionary. If only a
selected pointer-record algebra is held fixed, entangling diagonal phases can
survive. If the entire site/rule/record/readout/boundary net is transported,
the same phases are exact morphisms in a **groupoid rather than one
fixed-object group**. Cubic adjacency admits 48 signed coordinate maps and the
supplied proper subgroup has 24.

The foundation semantics now removes this as a constitutional fork. A faithful
model equivalence is a sort-preserving isomorphism: sites map to sites and each
whole owned `M_2` fiber maps to one target-site fiber. The foundation supplies
no concrete global tensor embedding, so transporting an entire entangled net
relates representation expansions rather than splitting one abstract site.
The remaining law equivalence must be compositional, uniformly local, and
record-history/readout preserving. Without those restrictions arbitrary
history frames trivialize every finite reversible edge, although nonunitary
effect/Choi ranks, transcript labels, and shift-like locality classes survive.
This is downstream definitional content, not a Lattice or Qubit addition.

### Instrument and infinite-sector theorems retire more prose

For a complete attainable exactly repeatable binary-qubit CP instrument, the
effects are complementary rank-one projectors and the branches are Lüders.
This derives projective form after a context exists. It does not choose `X`
versus `Z`, event occurrence, actual branch, prepared-state statistics, or the
future preservation scope.

There is a sharper context-after-dynamics theorem. A supplied exact qubit
interaction with a two-dimensional system-side commutant has one unique binary
pointer PVM up to outcome swap. The current `CZ-CZ` interaction thereby selects
onsite `Z`, including the endpoint reads. It does not select the center
transverse read: both `X` and `Y` create maximally entangled endpoints, and a
one-axis frame stabilizer rotates one into the other. Thus pointer context can
be derived from the complete interaction, but Bell capability, locality, and
covariance do not select that interaction or its remaining `X/Y` azimuth.

The chiral-triad follow-up derives still more. Stable `Z_f` plus the existing
transported header `Y_f` constructs `X_f=-iY_fZ_f` and a full relational Pauli
frame. Once a cubic-to-internal lift and an apparatus leg are fixed, the
equivariant soldering is unique. But the same full frame admits exact `X_f`-
and `Y_f`-reading apparatus laws with distinct future record statistics.
Chirality changes `X_f` to `-X_f`, which only swaps outcome labels; it does not
choose the apparatus role. The remaining context field is the typed
header-to-leg/apparatus decoder inside the exact interaction law.

The actual header now fixes that spatial decoder and a collision-free apparatus
rail. Its cluster identity `Z_a X_b Z_c=1` conditionally finishes the internal
choice: requiring center sign to certify endpoint-`Z` parity forces the `X`
PVM up to outcome swap. Without that parity-certificate contract, exact `X`
and `Y` complete apparatus laws remain. Since the current readiness grammar
hard-codes `X`, it cannot serve as its own derivation; the parity relation must
be operationally definitional or remain a field of the exact law.

The complete-future audit now settles the definitional half. Parity certificate
is a valid role-specific operational definition with no `X` label, and the
prepared cluster makes role-to-`X` a conditional theorem. Yet `PC` alone is not
complete record content. Coherent Bell branches and dephased parity mixtures
have identical certificate tables while later `XX`/Bell futures distinguish
them with probabilities one versus one-half. The exact law must therefore
specify the physically legal tester repertoire and history cut and prove
record-fibre strong lumpability or preserve the preparation/process record.
No Context or Record axiom is created.

The operational probability follow-up retires four further imports. Once the
exact law provides a normalized conditional transcript measure on the complete
physically available qubit effects, complete operational equivalence makes
effect noncontextuality definitional. A recorded physical randomizer derives
affinity; exclusive record coarse-graining derives additivity; and the exact
full-effect POVM theorem and hypotheses recorded in
`OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md` give the
trace/Born representation. A prepared state can
be defined as its complete operational class. The numerical normalized law
`W`, its physical effect repertoire, a reset/trial corpus and frequency
conditions, and almost-sure-versus-pointwise scope remain exact scientific
content. Complete-history status still follows the conditional routes stated
in Cycle 30; no generic standalone selector axiom is forced.

The certified-corpus theorem now closes the form of the frequency bridge.
Visible reset/outcome/close records define trial blocks, counts, and finite
frequencies, but do not prove predictive reset. For a stationary block process
with one-shot mean `q=W`, Birkhoff gives

```text
F_N -> E[X_0 | I_T]    almost surely.
```

Thus the weakest stationary condition for this outcome is the component-mean
identity `E[X_0|I_T]=q` almost surely. Ergodicity is sufficient but not
necessary; IID is stronger. Exact frozen and permanent-sector processes are
stationary and finite-causal-local with the same one-shot `q`, yet converge to
sector-valued frequencies. A complete global `W` must therefore prove
certificate ancestry, projective recurrence/stationarity, and component means,
or use a deterministic unique-ergodic route. These are law theorems, not IID,
reset, stationary, or ergodic Record clauses.

The blind packing audit then tests whether the remaining list really needs
multiple constitutional atoms. It does not. One complete exact history law
`L*` can own or derive initialization, generator and relative rates, record
instrument, normalized global `W`, certified corpus, collision/routing,
protocol/equivalence category, matter couplings, tensor response, and
branch-to-record semantics. This is honest one-reference packing only when
every internal field is exact or has a named derivation.

Actual boundary values, seeds, branch outcomes, interventions, corpus, and
chiral domain are projections of one law-admissible realized history `H`, not
six axioms. A boundary measure remains independent of a bare local generator;
it must be derived, packed into global `L*`, or left contingent. The existing
realized-state primitive already licenses the pointwise reference slot for
`H`, and a
unique-history law can derive it. Thus no separate actual-history or lane-
specific constitutional clause is forced.

The record-only-state Bell probe adds a type gate without enlarging the
universal minimum. All setting-independent Bell-local response laws on the
complete record data lie in the convex hull of 16 deterministic vertices and
obey `CHSH <= 2`. A positive normalized context-labelled record-history table
with local marginals `1/2` is no-signalling and reaches `2 sqrt(2)`. Therefore
the current state ontology can support quantum predictions through a global
history law whose amplitudes are law-side machinery, not an ontic state.

Conversely, a local QCA/process law that treats an unrecorded quantum carrier
as physical state is not literally a record configuration and would require a
Qualification state-type revision. Persistent preparation records or a
record-fibre lumpability theorem may close the seam without that revision.
The law's exact type therefore determines placement: separate Law for a global
history/action/measure, or retyped local law plus an explicit state change if
an enlarged carrier is indispensable. No state/Record clause is forced before
that choice is scientifically resolved.

Infinite redundancy supplies another real closure. Every proper-support
observable sees a finite GHZ cat as its branch mixture; in the quasilocal
limit, the phase is retired and finite operations cannot interconvert the two
infinite record branches. The mixture still does not select its central weight
or one actual member, and a finite seed cannot finish an infinite tail in
finite nearest-neighbor time.

### Cycle-29 constitutional reduction

The later results remove candidate axiom prose rather than add it:

```text
derivable from a complete exact law under stated conditions:
  permanent local extension, compatible schedule confluence, binary Lüders
  form, quasilocal phase retirement, finite-operation sector permanence,
  linked commit/export/tick/source bookkeeping, post-record covariant boundary
  normals, finite-interface causal-close certificates, a full relational frame
  from two rays, a unique pointer PVM for a simple-fixed-axis interaction, and
  exact finite adaptive protocol transport under a category-preserving frame;
  invariant positive-density collision-safe seed fields exist, and the
  foundation-maximal site-net quotient is site permutation plus onsite
  recoding; faithful foundation equivalence preserves sites and whole fibers;
  a named commit chain gives a relational integer clock; operational
  equivalence, randomization, coarse-graining, and full effects derive the
  noncontextual affine trace/Born representation and prepared-state identity;
  Birkhoff reduces certified-corpus frequency to the component-mean contract

remain contingent boundary/history:
  finite seed, actual low-record tail, chosen representation/sector, blank
  corridor, prepared program, and any world-supplied actual history not derived
  or generated by the complete law

remain exact-law fields unless jointly derived:
  complete interaction/context member, event readiness/occurrence, exact
  successor or instrument, clean one-qubit seed finalization/garbage export,
  downstream law-equivalence category,
  collision/interaction phases, spatial hand, numerical
  normalized law W, certified-corpus recurrence/component means, rate, tensor
  response, species coupling, collision/routing policy

universal-looking constitutional residue within the declared inventory and
tested routes:
  one exact predictive law identity or exact transcript-preserving physical-
  equivalence class, unless the present foundation uniquely derives it

state-type gate:
  global record-history weights preserve record-only ontology; a physically
  ontic unrecorded process carrier would require an explicit Qualification edit

realized-world instance gate:
  actual seeds, branches, corpus, boundary, and domain are projections of one
  L*-admissible history H only when L* derives or owns one-history semantics,
  a complete-history data interface supplies H, or a record-reconstruction
  theorem recovers it
```

No generic formation, witness, clock, conservation, QCA, projective, counting,
or storage sentence fills that residue. No exact referent has yet survived the
complete contract, so no final cut is authorized.

### Cycle-30 actuality correction

The finite measure/member separation remains valid. Record says that actual
record facts occur and lock one value; the registered realized-state primitive
licenses pointwise reference to one state supplied by physical history. It
does not supply a complete member of a history space. A complete stochastic
law therefore closes the seam only by one of four explicit routes: derive a
unique history from law plus boundary data, include objective one-outcome
semantics in the law, accept a complete history as contingent world data, or
prove that the record corpus reconstructs it. Typing a sample space as
complete record histories and normalizing its cylinder measure is necessary
but does not itself choose the actual member.

This does not turn amplitudes, decoherence functionals, or nonselective
channels into record probabilities. They still need a theorem producing a
normalized measure on mutually exclusive complete record histories. Nor does
it turn a measure-one theorem into pointwise truth. A record-visible objective
sampler and a typicality rule are stronger claims, not generic constitutional
atoms. Nor is a standalone history axiom forced: deterministic, law-owned,
contingent-data, and reconstruction architectures close the interface
differently.

### Cycle-31 record-state fortress correction

The one-`M_2`, nearest-neighbor state seam has a positive record-only existence
construction. A homogeneous proper-cubic Markov append law grows a 5,202-site
fortress from one framed source, uses the permanent record prefix as its whole
phase, embeds the exact 111-role terminal diamond, and writes `B0` last.
Overlapping forbidden centres demand incompatible filler records, while finite
isolation cylinders give positive-density completions. No mutable proposal,
cursor, message, scheduler, environment, or garbage state exists outside the
record configuration.

The price keeps this far from a selected law: thousands of permanent debris
records, over-exclusion, different jamming and weights, reversed seed order,
and an extensional table of many nonorthogonal `M_2(C)` labels. A direct qubit
controller cannot nondestructively distinguish all of those labels, though
finite orthogonal spatial codes remain live. The result closes only the broad
claim that local formation forces hidden unrecorded state. A future-relevant
coherent carrier still requires record-fibre strong lumpability, reconstruction
from records, gauge status, or a conditional Qualification widening. It forces
no universal Qubit, Admissibility, Record, or state edit.

### Cycle-32 global record-process route

A record-only global law can carry the missing quantum composition without
making its operator representation an ontic state. A normalized strongly
positive decoherence functional handles a fixed closed protocol. A positive
process functional/comb, or equivalent multilinear rule with identity-slot
containment, handles arbitrary active instruments. Finite exact controls
reproduce `CHSH=2 sqrt(2)`, constructive/destructive interference,
instrument-dependent future records, and cylinder consistency. Omitting a
slot means inserting the identity; measuring and forgetting is a different
nonselective channel.

This closes a law type, not the law value. A scalar classical measure loses
interference, and a scalar quantum measure on a fixed event algebra can lose
phase information needed after a later context. The exact complex/process
functional, protocol domain, containment maps, decoder, boundary, and
record-fibre theorem remain fields of one referent. No homogeneous NN
amplitude rule or local-to-global gluing theorem has yet produced that
referent. If one does, Admissibility can be retyped around the local law; if
the global process is irreducible, it belongs in a separate Law slot. Record
does not change on either route.

### Cycle-33 model-theory correction

Admissibility already gives each model one fixed rule slot, so a second
existence-only Law axiom is redundant. It does not implicitly define one
extension across models. Majority and minority availability maps on the same
foundation reduct satisfy the displayed locality, covariance, variation, and
label-neutrality conditions yet give opposite records under the same
singleton-write protocol. Even one exact availability table admits complete
record laws with weights `1/2` and `2/3`.

The missing item is therefore extensional identity of complete `L*`, not the
existence of a symbol. A stable cross-reference is conservative if it exposes a
unique theorem, substantive selection if it removes live predictive models,
and conditional model data if left outside the theory. An A-only definition
does not complete the dynamics. A complete local law can retype Admissibility;
a type-distinct global law requires separate Law placement. No Record clause
follows.

### Integration-cycle aliases for Cycles 34–38

The master packet retained its chronological integration counter while five
source artifacts kept their original campaign numbers. The mapping is:

| master section | canonical source artifact |
|---|---|
| Cycle 34 | `LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md` |
| Cycle 35 | `LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md` |
| Cycle 36 | `MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md` |
| Cycle 37 | `FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md` |
| Cycle 38 | `CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md` |

Cycles 39–42 use matching master and source numbers.

### Cycle-34 long-run record-capacity theorem

Under site-tethered permanence, a finite region can certify only finitely many
new trials, its long-run local formation rate is zero, and its append
transition graph has no nontrivial physical cycle. The infinite-volume result
is stronger: a time-stationary process with at most one formation per site has
per-site intensity `lambda=0`. A homogeneous NN expanding front still gives
infinitely many records and an unbounded commit count, but its apparatus moves
into fresh space and its spacetime formation density vanishes.

Lossless compression and copy/export do not renew old carriers. A bounded
recurring apparatus therefore needs a moving logical pattern, migratory record
identity, recyclable working state, or a global-history law. The exact law
must choose. Migratory identity may conditionally pressure Record; an
irreducible mutable carrier may conditionally pressure Qualification; growing
and global routes may preserve both. The theorem derives finite capacity but
does not select entropy, resource dynamics, lapse, gravity, or another axiom.

### Cycle-35 exact local-to-global process glue

One exact local composition rule can derive the global process law. Put the
same `CZ` on every undirected cubic NN edge. The commuting product gives the
proper-cubic radius-one quasilocal automorphism
`Z_x -> Z_x`, `X_x -> X_x product_(y~x) Z_y`. With an exact positive product
boundary and physical record instruments, finite contraction and the
quasilocal extension derive normalization, strong positivity, Bell and
interference weights, adaptive instruments, identity containment, and
compatible finite restrictions. No separately selectable global `W` remains
for this architecture.

The same local rule with all-zero and all-plus boundaries gives different
record laws, and the instrument category is not selected by the automorphism.
The residue is therefore the complete local rule, boundary class/data, and
record decoder, packageable in one `L*`; not another axiom for global
consistency. `CZ` is only a type witness and misses formation, matter,
chirality, clock rate, gravity, and law selection. A selected complete local
law with such a theorem supports retyped Admissibility; an irreducibly global
law still supports separate Law placement.

### Cycle-36 moving logical apparatus

An exact nearest-neighbor append front closes the remaining generic recurrence
concern without changing Record. From one seed it writes one fresh binary
record per step along an otherwise open ray. Every old record stays locked at
its original site, while the unique pointed head pattern is translated into
fresh support. Conditional future-word laws agree for equal head contents, so
the recurring apparatus is an exact process bisimulation, not a migrating
physical record. Indefinite logical trials are therefore compatible with the
current record-only state ontology.

The price remains explicit: a seed and open ray, a direction or covariant
direction decoder, a selected outcome kernel, physical rate, routing and
collision law, and linearly growing storage. A fixed laboratory patch sees
only finitely many events. These are boundary and `L*` fields, not a generic
Record, state, storage, or clock clause.

### Cycle-37 final missing-content census

A clause-deletion census retested recurrence, identity, preparation/context,
identity-slot containment, typicality, and projective local-to-global
consistency. None survives as a second universal-looking constitutional atom
within the tested census.
Preparation and apparatus content can be records plus an exact decoder;
containment and gluing are law theorems; typicality is claim-specific; and an
actual boundary/history needs an explicit law/data route rather than being
supplied wholesale by the realized-state primitive. Record changes only if a selected law makes an official record
move, disappear, or change. Qualification changes only if equal complete
record configurations retain different legal future laws after honest
recording and gauge closures fail. Both are conditional compatibility gates.

### Cycle-38 cubic-CZ uniqueness attack

The local gluing witness does not select itself. In the smallest selected-`Z`,
homogeneous, radius-one diagonal-Clifford class, entanglement and global
involution leave two tied laws:

```text
U_0 = product_<xy> CZ_xy,
U_1 = Z_all U_0.
```

They share translation/proper-cubic covariance, support, depth, radius, and
involution. A fixed coherent boundary and fixed `X`/neighbor-`Z` record
dictionary distinguish them by a sign. The alternating frame
`F_t=Z_all^t` exactly relates them only when boundary, instruments, labels,
decoders, and every adaptive protocol are co-transported. Thus the next
irreducible selector is the physical temporal record/instrument equivalence
category; under a fixed dictionary the remaining onsite parity is a binary
law value. Even after that choice, this layer lacks propagation, formation,
weights, corpus, matter, and gravity, so it is not complete `L*`.

### Cycle-39 temporal protocol-equivalence classification

The alternating frame is neither an automatic foundation gauge nor an
intrinsic physical bit. Each fixed-time component is a uniformly local,
site-net-preserving onsite recoding, but the time-indexed family becomes an
equivalence only when the complete boundary, instruments, decoders, adaptive
branches, and cross-time calibrations are co-transported. Holding a fixed
odd-time transverse record or a named one-tick idle map distinguishes the two
candidate laws with certainty. In particular, a same-slice identity remains
identity while the cross-time idle `J_t=I` transports to `Z_all`.

The exact consequence is downstream and law-relative: full temporal record-protocol law
equivalence must be compositional, uniformly local, sort preserving, and
record faithful over complete adaptive histories, including every named
temporal calibration. This sharpens the required `L*` referent or equivalence
theorem. It supplies no temporal-gauge, Record, or clock axiom sentence.

### Cycle-40 broad cubic one-qubit Clifford-QCA uniqueness attack

The broader radius-one Clifford census exposes an earlier selector than the
Cycle-38 onsite parity: how proper cubic rotations act on the onsite Pauli
module. The three Clifford action types leave respectively `18`, `2`, and `0`
neighbor-coupled symplectic skeletons. With literal site-only action, four
static classes remain and three classes remain even after every uniformly
bounded-range time-dependent Clifford protocol frame is allowed. One
nontrivial skeleton class appears only after additionally selecting site-only
action, neighbor coupling, involution, and a uniformly onsite complete-
protocol quotient.

That conditional closure is a live positive route, not exact-law selection.
Phase/sign lifts, record-category closure, boundary/history, occurrence,
statistics, and the other TOE interfaces remain. Proper-cubic covariance and
one qubit per site therefore do not yet name a complete constitutional
referent.

### Cycle-41 complete-candidate assembly

The strongest compatible components assemble into one exact radius-three
object `L41^R3`. On its declared single-front boundary it explicitly populates
all thirteen record-process contract jobs: a generated carrier, record
decoder, reset and branch instruments, append recurrence, normalized
projective cylinders, and a certified corpus. It is a genuine positive
partial law rather than a list of slogans.

It does not meet the strict nearest-neighbor target. Two seeds with identical
radius-one record neighborhoods but different radius-three headers have
opposite readiness answers. The first missing local field is therefore an
exact Boolean causal compiler, `EVENT_READINESS_LOCAL_CAUSAL_DOMAIN`, not
another scalar. A raw all-edge `CZ` shortcut preserves `Z` records but sends
an `X` record into a seven-site stabilizer sector; restricting it to fresh
sites consumes the same readiness map. A compiled NN/QCA or Z-coded escape
remains live.

Even at radius three the first open TOE interface is physical clock rate and
lapse response, and the first hard channel conflict is matter: the constant
reset erases orthogonal input distinguishability. Resource, continuum, and
gravity interpretations also remain unconstructed. These are fields and
tests of a candidate complete `L*`, not independent generic axiom clauses.

### Cycle-42 realized-history identifiability firewall

The realized-state primitive closes pointwise actuality but does not invert
one history into a counterfactual law. Two deterministic laws can agree on
every visited state and disagree at an unvisited legal preparation; every
finite Bernoulli transcript fits a continuum of parameters; and two causal
laws can share the exact observational distribution while differing under an
intervention. The positive zero-edit route is a separating all-protocol
reconstruction theorem with a certified recurrent corpus. No such theorem
currently exists for the complete framework, so actual `H` does not remove
the exact-law referent obligation and adds no second atom.

## No-Go Discipline: Narrow Claim Only

The negative claim tested here is:

> Generic monotone continuation separation does not entail actuality or a
> unique statistics law.

No claim is made that no exact law can derive them.

### N1 — Alternative routes

| route | status | exact result |
|---|---|---|
| maximum/maximal continuation | `ATTEMPTED` | the three-node fork has two equally maximal record histories |
| uniform branch or terminal count | `ATTEMPTED` | operationally equivalent refinement changes coarse weights |
| minimum computation/description | `ATTEMPTED` | recoding swaps the shortest branch; two minimal-Kraus unravelings of one channel have different record meanings |
| covariance/symmetry | `ATTEMPTED` | constrains a supplied kernel but cannot choose a classical leaf in a transitive two-leaf fork |
| projective/cylinder consistency | `ATTEMPTED` | fair and nontrivial Markov/Gibbs families remain distinct |
| exact positive action | `ATTEMPTED` | two reversible kernels share one exact equilibrium law |
| global Church–Rosser confluence | `ATTEMPTED` | reconnects or erases conflicting record labels if imposed across all permanent outcome sectors |
| causal-graph invariance | `LIVE PARTIAL ROUTE` | can quotient update order without requiring terminal-state confluence; does not supply outcome measure or actuality |
| sampled instrument or objective-jump law | `LIVE POSITIVE ROUTE` | closes actuality and one-shot weights because the atomic law explicitly contains them |
| unique global boundary/history | `LIVE POSITIVE ROUTE` | can close actuality, with contingent boundary data exposed |
| uniquely ergodic exact contextual law | `LIVE POSITIVE ROUTE` | could derive long-run frequencies after the law and trial corpus are fixed |
| Hilbert ancilla-refinement reconstruction | `LIVE PARTIAL ROUTE` | can force norm-square form under unitary/refinement/additivity hypotheses |

### N2 — Wall independence

| pair | exact separation |
|---|---|
| availability / successor support | full-support and majority-support laws share one availability table |
| support / record identity | append-only and overwrite completions share formation siblings but differ on reconnection |
| support / actuality | one branch graph admits distinct selected histories |
| support / statistics | `lambda=1,2` kernels share exact support |
| actuality / statistics | fix one selected history while changing ensemble weights, or fix a measure while changing the realized sample |
| order / duration | one event poset admits distinct positive lapse assignments |
| action / transition rate | `K_1,K_2` share one reversible equilibrium law |

A strictly positive measure recovers its support, so the independence claim is
directional: support does not determine the measure, not vice versa.

### N3 — Hidden-wall scan

“Lawful,” “physical operation,” “sample,” “context,” “complete state,”
“uniform,” “branch,” and “fixed” are treated as fields requiring exact
definitions, not as free explanatory words. The scan additionally exposes
physical quotient, branch identity, code/cost language, normalization,
symmetry group, preparation, trial corpus, update order, boundary data,
allowed-operation algebra, and state/process memory.

### N4 — Residual matching

| witness | residual it actually tests | use here |
|---|---|---|
| 729-profile two-support pair | availability -> support | exact match |
| append versus overwrite cones | support/identity -> nonreconnection | exact match |
| two selected leaves | support -> actuality | exact match |
| local and Gibbs `lambda=1,2` pairs | support/symmetry/consistency -> weights | exact match |
| two reversible kernels with one `pi` | action/equilibrium -> event dynamics | exact match |
| Wilson/staggered source disclaimers | named action candidate only | classification, not universal evidence |
| comb/Gleason representation theorems | representation after supplied hypotheses | partial closure, not evidence of non-entailment |

### N5 — Rhetoric audit

The result is non-entailment from a specified generic reduct, not impossibility,
fundamental randomness, proof that one interpretation is correct, or evidence
that all exact local laws fail. Runner PASS counts overlap and are not
independent evidence counts.

### N6 — Partial-closure paths

Append-only continuation closes branch-relative nonreconnection. Sectorwise
causal invariance can remove disjoint schedule gauge without erasing records.
Sharp rank-one repeatability can fix the Lüders branch update. Hilbert
ancilla-refinement invariance can conditionally fix norm-square weight form.
Sampled instruments close operational actuality and normalized one-shot
weights once process, context, sample semantics, and maps are supplied.
Process-comb extension and operational-equivalence theorems remove
implementation redundancy. These are real partial closures.

### N7 — Steelman

The strongest steelman is one algebra-valued local law whose context family is
fixed by covariance, whose sharp records force Lüders maps, whose Hilbert
refinements force norm-square weights, and whose global contextual dynamics is
uniquely extendible and uniquely ergodic. A presentation-invariant amplitude
or quantum measure on a sectorwise-causal multiway system is another live
version. Constructing either would jointly retire several residual atoms; no
probe here excludes it.

### N8 — Cross-cycle echo

This result matches the July 13 separation between availability, continuation,
actuality, and statistics. The new content is the exact hard-constraint kernel
pair, Gibbs comparator, schedule/locality trilemma, action/transition pair,
record-state lumpability test, Kraus absorption boundary, and multiway causal
quotient. The refinement-count result is an exact reformulation of the earlier
branch-count wall and is not counted as independent evidence.

## Next Decisive Probes

1. compile the displayed radius-three readiness/phase decoder into a
   translation- and proper-cubic-covariant radius-one process on one `M_2` per
   site, with record-visible phases and no overwritten official record;
2. replace the reset sector with a protected injective/coherent matter carrier
   and re-prove recurrence, collision, corpus, and record-fibre sufficiency;
3. derive a physical clock-rate/lapse observable and then the resource,
   continuum, interaction, and gravity responses from the same candidate;
4. finish the exact phase/sign, rotation-action, boundary, and complete-
   protocol equivalence classification, including temporal idle calibration;
5. attempt a separating all-protocol reconstruction theorem or empirically
   discriminate every surviving unquotiented representative; and
6. only after one TOE-predictively complete law or complete record-faithful
   equivalence class survives, delete every derived clause and begin
   constitutional prose iteration.

## Verification

Run:

```bash
python3 scripts/exact_predictive_specification_tournament_2026_07_14.py
python3 scripts/route_two_exact_completion_probe_2026_07_14.py
python3 scripts/finite_diamond_sampled_luders_invariant_record_probe_2026_07_14.py
python3 scripts/wolfram_multiway_record_sector_probe_2026_07_14.py
python3 scripts/temporal_protocol_equivalence_alternating_frame_cycle39_2026_07_14.py
python3 scripts/cubic_one_qubit_clifford_qca_uniqueness_cycle40_2026_07_14.py
python3 scripts/complete_candidate_lstar_assembly_cycle41_2026_07_14.py
python3 scripts/realized_history_exact_law_identifiability_cycle42_2026_07_14.py
```

The runner is a finite exact probe. It does not establish a continuum limit,
select the physical law, or authorize an axiom edit.
