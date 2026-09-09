# Block 230 Preregistration

No Block-230 primary runner may be written or executed before this packet is
committed. The abstract algebra, carrier map, topology class, contact
semantics, terminal guard, test order, and pivot gates below are frozen.

## Exact target contract

| Field | Contract |
|---|---|
| statement | every fair execution of the frozen local summary compiler on a finite typed arm/two-child tree reaches the same contact-sensitive Record outcome; the associated positive-rate physical generator absorbs with probability one |
| domain | finite connected trees with one typed root, one typed seam, zero or two typed child leaves, maximum degree three, arbitrary finite contact subset, exact labelled darts |
| allowed premises | the stacked Block-229 carrier and participant model; local tree incidence; supplied positive local rate `gamma` as a time unit |
| forbidden weakenings | fixed length/density only; unlabelled word-only lift; imported scheduler fairness in place of absorption; supplied winner/owner/order; topology known through a size/count field |
| completion witness | symbolic ACI/local-diamond/rank theorem, exact terminal-safety lemma, full labelled lift, CP/Lindblad completeness, and absorption theorem with independent reproduction |
| not closure | algebra alone, bounded census, global normalization requiring a distinguished distant head, or a supplied action/clock/law-selection rule |

## Frozen semilattice

Let the atom order be

```text
bit 0: rho    typed root incidence
bit 1: alpha  typed seam incidence
bit 2: lambda typed child-0 incidence
bit 3: chi    typed child-1 incidence
bit 4: phi    at least one incident foreign participant was encountered
```

The summary set is exactly `Sigma = {0,...,31}` interpreted as subsets of
these five atoms. Its bottom is `0`; its product is

```text
x join y = x bitwise-OR y.
```

The canonical list `[[x,y,x|y] for x in 0..31 for y in 0..31]`, serialized as
compact JSON with no whitespace, has SHA-256
`5e7bfc1cb5c5d43ec8df382bfe491c4e12ce7cb1e6d6929d8358148812be5c18`.
No sixth atom or alternate product may be introduced after execution.

Initial onsite summaries are `rho` at the root, `alpha` at the seam,
`lambda/chi` at the corresponding child leaves, and `0` elsewhere. A foreign
participant remains an exact labelled incidence until a local rule whose
support touches its endpoint consumes it atomically and joins `phi` into that
site's outgoing summary. No participant is inferred from an aggregate bit and
no `phi` bit substitutes for literal quench accounting.

For every adjacent tree edge, the only summary merge is

```text
(x,y) -> (x join y, x join y),  when x != y.
```

Every exact contact-mask product lift of that row joins `phi` before the union
and consumes precisely the displayed participants. A one-site seed row covers
the degenerate one-site component. Every other physical row touching a live
participant must use the same product lift; no quiet row may pass through it.

## Frozen terminal semantics

The expected coverage mask is topology-typed, never counted:

```text
linear arm:     E = {rho,alpha}
two-child tree: E = {rho,alpha,lambda,chi}
```

A writer may terminalize only when its local summary contains `E`. It writes
`ABORT` iff `phi` is also present and `CLEAN` otherwise. The proof must show
that, on the frozen tree domain, acquiring all typed leaves forces every path
carrying a possible contact to have crossed an exact participant-aware merge.
One false-clean reachable history stops the block.

Cleanup latency may grow with diameter. What must be `n`-independent is the
summary algebra, row support, rank formula, critical-pair diagram, carrier,
and terminal safety—not the number of local jumps to absorption.

## Frozen carrier map

Use two parity copies of all 32 summaries, four terminal rays
`CLEAN/ABORT/RECORD_CLEAN/RECORD_ABORT`, and a rank-60 default complement:

```text
even summaries: rays 0..31
odd summaries:  rays 32..63
terminals:       rays 64..67
default:         rays 68..127
```

The canonical 128-entry compact-JSON map has SHA-256
`80405b56598bd2724d7724e829acc7d223c9559dc72e4cf5954b9cda2b99f33e`.
The total carrier rank remains 128. Relabelling within these declared blocks is
allowed only as an explicitly conjugate presentation; adding a ray or reducing
the default complement after execution is failure.

## Stage A0 — algebra and factorization

1. Materialize all 1,024 ordered products and reproduce the frozen digest.
2. Exhaust all `32^3=32,768` triples for associativity and all pairs for
   commutativity/idempotence/bottom.
3. Reconstruct the Block-229 exact witness and map visible `L` plus raw/quenched
   contact incidence into `phi` without importing its conclusion.
4. Require the two witness successors to enter one common summary diagram
   within their six-site overlap plus exact incident participants, independent
   of translation `n>=10`.
5. Test whether the frozen 46-row table factors through `Sigma`; report every
   source pair with equal summary but unequal summary target. Failure of this
   comparator does not authorize a new row and does not kill the new compiler.

## Stage A1 — reduced arbitrary-size theorem

Generate every asynchronous seed/merge/terminal schedule for:

- every contact subset on linear arms through length twelve;
- all zero/one/two-contact linear arms through length twenty-four;
- every two-child tree with total internal size through ten and every contact
  subset;
- translated unequal branch lengths, adjacent/dense contacts, the Block-229
  witness family, and one-site/zero-edge degeneracies.

Required normal summaries are the union of all initial boundary/contact atoms;
required outcome is `CLEAN` without contact and `ABORT` with contact. Report
fixture/state/transition counts, first exact failure, maximum graph size, and
complete participant accounting.

Then prove, for arbitrary finite frozen-domain trees:

- local confluence: disjoint edges commute; two edges sharing one site join
  inside their three-site union by associativity/idempotence;
- termination: the integer rank
  `sum_site (5 - popcount(summary_site)) + live_participant_count + live_writer`
  strictly decreases on every nonidentity seed/merge/terminal step, with the
  writer term phase-gated explicitly;
- unique summary normal form: every site in a connected component holds the
  union of all initial atoms;
- terminal safety: no clean terminal is reachable while any participant can
  contribute `phi` to the typed component.

Any target-equivalent unproved lemma fails Stage A1; bounded tests cannot stand
in for these proofs.

## Stage B — labelled full-state lift

Only after Stage A passes, generate exact physical rows on:

- all simple labelled arms through length eight and every one/two-contact image;
- width-two equal-neighbor ports with distinct darts;
- all twelve parent/two-child Y triples, unequal child lengths, and every
  contact subset through total internal size eight;
- the 47 inherited contact signatures and reciprocal-crosswire orbit;
- the Block-229 translated family at multiple separations.

Require `target == Row.apply(source)`, consecutive histories, exact root/path/
seam/Y darts, participant-local quench, no orphan role, same 128-ray carrier,
and identical visible summary joins. `lambda` and `chi` are typed ports, not
ordered winners; reflection must exchange them equivariantly.

Any root/dart/Y alias, need for a sixth atom, summary set growing with boundary
count, or carrier overflow stops the compiler and pivots to distributed
set-valued incidence.

## Stage C — physical generator and absorption

Compile one local Lindblad jump per disjoint exact source cylinder and
environment label:

```text
L_e = sqrt(gamma) |target_e><source_e|.
```

Keep distinct environment labels for many-to-one rows, identity/QND action on
unmatched default and Record sectors, and the standard local anticommutator.
Require exact trace preservation of the generator on every used support,
nonnegative rates, no cross-cylinder coherence leak, and no CP deficit.

On every finite frozen-domain component, prove absorption from the generator's
own strictly positive local rates. Enumerate closed recurrent classes and show
that only the declared Record terminals remain. Report expected jump count,
dimensionless absorption time, the supplied rate unit, physical-time status,
Record writing, probability form, and law selection separately.

## Decision classes

- `positive-aci-component-summary-physical-instrument`;
- `positive-aci-summary-arbitrary-tree-open-labelled-lift`;
- `positive-bounded-aci-summary-open-arbitrary-proof`;
- `scoped-summary-factorization-failure-new-compiler-live`;
- `scoped-summary-terminal-safety-failure`;
- `scoped-summary-rank-or-confluence-failure`;
- `scoped-summary-labelled-capacity-or-alias-failure`;
- `scoped-summary-cp-or-absorption-failure`;
- `partial-attempt-with-named-untested-routes` when no broader negative passes
  the current N1--N8 gate.

No author result changes an axiom, audit status, retained status, obligation,
or TOE percentage. Any negative broader than the exact frozen compiler must
land the current no-go-discipline packet and preserve the Haar, distributed
incidence, serial, coherent, and global-normalization routes.

## Pivot

Non-ACI multiplication, false-clean terminal, history dependence, or another
diameter-dependent summary reconciliation kills this route. Unbounded summary
cardinality, a sixth atom, fixed-carrier overflow, or labelled incidence alias
pivots immediately to distributed set-valued incidence. Haar reranks only
after associative graph-family iteration, uniform locality/truncation, and a
selected action/source/clock result.
