---
claim_id: admissibility_block38_transaction_grant_total_absorptive_collision_boundary_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "Conditional normalized transaction-grant composition on valid clean causal-prefix Record maps; finite six-axis controls are distinct from the supplied atomless Haar law. Valid preloaded maps exhibit state-alias and mutual-head obstructions. No physical law selection or total productive collision theorem."
runner: scripts/admissibility_block38_transaction_grant_total_collision_2026_09_01.py
required_parents:
  - minimal_axioms
actual_current_surface_status: conditional-support
authority: none
---

# Clean transaction grants and preloaded-map boundaries

Date: 2026-09-01; corrected 2026-09-09 from original PR #7845.

Type: bounded_theorem

This is a supplied finite-footprint stochastic construction. On its valid
clean causal-prefix sector, it preserves the specified singleton row law,
absorbs competing heads, and has a linear total-rate bound. It does not derive
a physical formation law from the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
Independent landing review and formal audit are separate; no audit verdict or
retained status is assigned here.

## Supplied domain and literal rows

A configuration is a finite map from integer lattice sites to permanent
carriers. A proper-cubic frame supplies perpendicular unit lattice vectors
`d,t`; there are 24 such frames. Each carrier has an exact role/frame tag and
seven real payload coordinates. A protocol contains mode RND or DIR,
preparations `u0,u1` with `|ui|<=1`, and selector weight `0<=p<=1`.
The common response and successor sharpness satisfy `|lambda|,|kappa|<=1`.
These bounds are hypotheses, not consequences of a decodable tag.

The executable interface accepts integer sites and exact rational payloads,
including closed-boundary values; mathematical real-valued kernels are defined
by the formulas below. It rejects floats, out-of-ball preparations, invalid
selector weights, noncanonical role fields/padding, nonunit axes, inconsistent
first-outcome directions, and response/sharpness outside the closed square.
`transaction_terms` raises `ValueError` outside this host domain;
`transaction_from_head` returns no transaction for an invalid head.
Rejection is distinct from a valid absorbing state with no terms.

H/T/C carry protocols without selector or outcome. R/P/Q1–Q8 carry a protocol
and selector 0 or 1. G carries mode and selector with zero payload. A carries a
unit axis; F carries axis and direction `b a` with `b=+1` or `-1`; M carries
axis and a Bloch-ball successor; B2 carries a unit outcome direction and label.
All non-H/T/C roles have a selector. Only F/B2 have an outcome label. Exact
canonical reconstruction checks unused payload coordinates. These syntactic
conditions allow valid preloaded maps; they do not assert causal reachability.
The positive result further requires the reachable causal-prefix condition.

The current [Block38 helper note](../archive/notes/docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md)
provides construction context. Only the following literal definitions and the
loaded helper implementation are used here; its standalone campaign, physical
attachment selection and historical status are not imported as established
premises. The helper loads Block37 for rotations and three elementary
Gaussian/PIT/Haar integrals, without executing its standalone campaign.

For head H, the write footprint has exactly 18 distinct sites:

```text
T=H-t, G=H+d-t, R=H+d, P=H+2d, A=H+3d,
F=H+4d, M=H+5d, B2=H+6d, C=H+7d,
Qr=H+r d+t (r=1,...,8), H_next=H+8d.
```

The DAG has rows T←H, G←T, R←(H,G), P←R, A←P, Q1←R,
Qr←Q(r−1), F←(A,Q4), M←(F,Q5), B2←(M,Q6), C←(B2,Q7),
and H_next←(C,Q8). Every DAG bond is a lattice edge. The grant eligibility
rule reads the whole finite footprint; nearest-neighbor implementation of
that test is not proved by the nearest-neighbor DAG alone.

G selects bit 0 with mass p and bit 1 with mass 1−p, the supplied Gaussian/PIT
partition. RND uses `s=u_bit`; DIR uses `s=p u0+(1−p)u1`. A has normalized
atomless Haar law `mu(da)` on the unit sphere. F has conditional label mass
`(1+b lambda a.s)/2` and direction `b a`; M stores `v=kappa b a`;
B2 has mass `(1+c lambda a.v)/2` and direction `c a`. The remaining rows are
deterministic protocol copies or closure. The two binary masses are nonnegative
and sum to one by Cauchy–Schwarz and the domain bounds. Convexity keeps DIR
inside the Bloch ball, and `|v|<=1`. Thus these rows preserve the carrier domain.
The Gaussian selector is a two-bin pushforward, not a claim that its underlying
continuous randomizer has two atoms. Normalization uses the explicit supplied
Gaussian and Haar measures; no probability values are selected by the axioms.

## Grant composition and its conditional proof

Each eligible clean H has one rate-one H→T term, using its ordinary deterministic
T row. Clean means all 18 write sites are blank. Transactions conflict exactly
when their complete write footprints intersect. An ordinary matching H/T pair
is a literal grant. It is valid only if no other literal grant conflicts with
it and every occupied site in its owner view is a supported causal prefix of
the DAG above. The owner view contains only its H and 18 write sites. This
recognition is extensional; it cannot recover hidden write order.

Continuation terms use that owner view and retain the original row object,
including source-measure family, frame/mode/selector fields, complete atomic
branches and parent roles. They have rate one and stop when H_next is present.
Other heads are retained but supply no ungranted continuation terms. A jump
appends a supported carrier to one blank target; overwriting is rejected.
The append helper presumes a term returned for the current configuration;
it is not a verifier for adversarially fabricated or stale transaction terms.

For initially clean heads with mutually compatible source sites, a winning
T disables every conflicting head: if its T lies in the loser's footprint,
that footprint is no longer blank; otherwise the valid grant conflict test
blocks it. A loser stays an occupied Record. Disjoint granted write footprints
prevent shared output targets. Source heads that obstruct another footprint
are excluded by clean eligibility, rather than silently erased. Valid owner
views prevent cross-owner hybrid parents. These facts prove append preservation
on the stated clean causal-prefix sector, not productive completion on every
valid preloaded map.

The singleton law is unchanged pointwise on that sector: owner restriction
removes no singleton parent and the emitted row is the same local row, with
the same rate and source measure. This statement applies to every supported
axis, not just the six representative directions in the finite check. For the
continuum statement, regard each row as the displayed normalized measurable
kernel. Its read parents are earlier permanent vertices of a finite DAG.
Co-enabled vertices have distinct blank outputs and neither reads the other's
output; their kernels therefore commute as product kernels conditional on
the common past. Adjacent swaps relate all topological orders. Iterated
integration gives the same terminal law in every such order. This supplies
the conditional all-order argument; a finite census alone does not supply it.
A single off-axis rational point exercises the current implementation of this
same schema, without claiming enumeration of real points.

For a fixed finite eligible conflict graph, equal independent exponential
grant clocks select a uniformly random remaining vertex, then remove that
vertex and its neighbors. Induction on the number of remaining vertices proves
that the exact recursion has total mass one and returns a maximal independent
set. This abstract graph statement holds for every fixed finite graph. It is
not a census or proof of changing multi-generation lattice eligibility.
Separated components have the union of their generator terms whenever their
owner domains do not interact. The runner checks this for two clean components.

Translations and proper cubic rotations transport heads and footprints,
preserve intersection/blankness, and relabel the same protocol rows. Rotations
preserve the dot products and Haar measure; rates are the same unit constant.
Consequently the supplied grant/continuation law is covariant on its domain.
This is an analytic transport argument. The finite geometry check tests 1,728
rotated footprint cases; it does not claim to rerun the old 2,976 combined
footprint/inherited-transcript checks.

For finite C, at most `|C|` head Records contribute terms. Each has at most one
grant or at most 18 continuation targets, all at unit rate. Thus the conservative
bound `Gamma(C)<=19|C|` holds wherever this construction is defined. Each jump
increases Record count by one. For the supplied pure-jump process, its stopped
Lyapunov function `V=1+|C|` obeys `LV<=19V`; equivalently it is dominated in
count growth by a linear birth process. The stopped expectation bound and
Markov's inequality give vanishing probability of arbitrarily many jumps in
a finite time interval. This proves nonexplosion for that finite-initial-state
process. It supplies no physical time unit, infinite-density construction,
genesis or recurrence theorem.

## Valid preloaded boundaries and what stays open

The same matching `{H,T}` map results from H then T or preloaded T then H.
A content-only Markov rule gives that map the same continuation in either case;
no positive-probability assertion about both histories under the restricted
law is needed. The implemented convention recognizes one valid grant and one
Gaussian continuation in this map. It does not infer its temporal origin.

The preserved concrete witness uses frame 23 at `(0,0,0)` and frame 3 at
`(8,0,0)`, with ordinary valid default protocols. Each H occupies the other's
future H_next site. Both are unclean and absorbed: zero terms, two absorbed
heads. Adding their matching Ts gives two literal grants, zero valid grants,
and zero terms. They are valid preloaded counterexamples to universal productive
collision totality, outside the clean-ready pair census.

More generally, a fully occupied fixed reporting neighborhood has no blank
site for mandatory append-only reporting in that neighborhood. This narrow
resource obstruction leaves absorbing outcomes, added writable resources,
overwriting/enlarged capacity, or a supplied covariant nonlocal search rule
available. A nearest-free-site proposal needs an explicit covariant tie
distribution; a deterministic coordinate priority is not such a derivation.
There is no general no-go for collisions or alternative formation laws.

This is absorptive/exclusion behavior: losing heads remain permanent Records.
It does not establish elastic scattering or lineage survival. It does not
select lambda, physical Record-to-matter attachment, a physical formation
clock, a nearest-neighbor realization of footprint arbitration, or a law from
the four axioms. W3 retirement, homogeneous infinite-density dynamics,
source/gravity and TOE completion remain open. These are limitations of the
specified construction, not an audit verdict.

## Bounded reproduction and historical disposition

Run `python3 scripts/admissibility_block38_transaction_grant_total_collision_2026_09_01.py`.
The final protocol has a 150-second wall cap, 2 GiB measured RSS cap and one
BLAS thread, with no child campaigns. It checks:

- actual invalid-domain rejection and valid parameter endpoints;
- the six-axis singleton structural quotient: 652 states, 852 rows, 48 terminals;
- overlaps for frames 0–3, first 24 lexicographic displacement candidates per
  frame pair, plus both winners of one distinct-trigger pair (96 finite rows);
- actual changed conflict/rate implementations against the same exclusion and
  translation predicates, plus changed finite/axis rows against normalization
  and off-axis support predicates;
- the non-cubature axis `(3/5,4/5,0)` through actual transaction F→M→B2 rows;
- all 1,100 labelled simple graphs through five vertices and 3,726 outcome sets;
- separated initial components, the preloaded witnesses, footprint transport,
  and actual append/mass checks. The universal rate bound is the proof above.

These finite counts are expected controls, not a count of atomless states or
literal continuum transcripts. The historical 70,200-pair census, four-response
singleton sweep and 2,976-case combined covariance run are preserved but not
freshly rerun or credited as the current finite protocol. The historical
20/20 mutant claim is withdrawn: several original failures were assigned by
name without changing the relevant kernel. No rejection quota is retained.
All other old scope/dispatch checks are historical metadata, not proof tests.

The runner binds its own note, actual loaded Block38 and Block37 source files,
the archived Block38 construction note, and the current minimal memo. Missing
inputs raise rather than disappear from its fingerprint. The own source is
bound by the cache runner hash and complete input fingerprint; other inputs
are explicitly content-pinned. No helper standalone preregistration packet,
other historical parent, or reserved PR #6379/#6858/#6859 is executed or
accepted transitively. See [correction history](../.claude/science/physics-loops/admissibility-7845-correction-20260909/HISTORY.md)
for all original path and predicate dispositions. The historical cache is
unaltered recovery evidence, not this run's receipt.
