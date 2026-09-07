---
claim_id: admissibility_random_priority_formation_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional construction on Z^3 for the supplied six-projector positive product rule with orbit weights p,q,r>0, its records-only extension, iid continuous site priorities, and independent outcome marks. Finite decreasing ancestry defines a unique measurable mark-driven permanent-Record process, covariant under translations and proper cubic rotations, with one-site formation conditionals equal to the supplied rule. A factorial ancestry bound gives finite-window total-variation errors and a two-site covariance bound. On p=q=t>1,r=1, a direct three-color Potts bond expansion bounds every free-boundary static limit's axis-indicator covariance below exponentially; the formation bound is smaller at sufficiently large separation. At t=2 and distance 512 the inequality is certified exactly. No axiom-side scheduler, clock, weight, statistical Bridge, Born, action identification, static uniqueness, or arbitrary-scheduler conclusion is claimed by the construction. A separate finite-C4 adaptive-scheduler appendix remains provisional for focused review."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_random_priority_formation_2026_09_07.py
---

# A covariant random-priority formation law on the infinite lattice

**Date:** 2026-09-07. **Claim type:** bounded_theorem.
**Source stage:** conditional research proposal; no audit status assigned.
**Frozen main:** `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`.
**Runner:** [admissibility_random_priority_formation_2026_09_07.py](../scripts/admissibility_random_priority_formation_2026_09_07.py).
**Author evidence:** [readout packet](../.claude/science/physics-loops/toe-campaign-20260907/readout/HANDOFF.md).

One supplied local rule can define different static and formation laws. This
note constructs the latter on all of `Z^3` without choosing a spatial sweep
direction. Give each site an independent continuous priority and an
independent mark for its eventual local draw. A site's value depends only on
neighbors of lower priority. Their predecessors form a finite set almost
surely, so the site's record can be computed from finitely many marks.

The construction gives a permanent-record process and an explicit error for
computing its finite marginals in a finite window. Its record correlations
also have a uniform factorial upper bound. On one declared ferromagnetic
subfamily, a static law has a larger, positive correlation lower bound at a
sufficiently distant pair. Thus a specific content-only statistic
distinguishes the two laws on the infinite lattice itself.

The iid priorities, independent outcome marks, finite menu, local weights,
and records-only extension are supplied conditions. The four axioms and the
three approved primitives do not supply these choices. This is a
construction and comparison of conditional models, not an identification of
the physical law or the framework's committed action.

## 1. Exact domain, inputs, and output

Sites are `Z^3`, with graph distance `d_1` and six nearest neighbors. The
supplied local menu is

`M={P(±e_1),P(±e_2),P(±e_3)}`, where `P(n)=(I+n·σ)/2`.

These are six distinct matrix contents in `M_2(C)`. A declared proper cubic
rotation acts simultaneously on site coordinates and the corresponding
Bloch directions. This finite menu and its coordinate correspondence are
model choices. The full Qubit possibility domain is not replaced by it.

For `p,q,r>0`, let the symmetric pair weight `φ(s,t)` be p on identical
projectors, q on opposite projectors of the same axis, and r on orthogonal
Bloch directions. The **records-only local rule** on any partial neighbor
assignment `η:A→M`, `A⊆N(x)`, is

`r_x(s|η) = product_{y∈A} φ(s,η_y) / sum_{u∈M} product_{y∈A} φ(u,η_y)`.

An absent neighbor contributes no factor. Every denominator is positive;
every member of M is supported. If p,q,r are not all equal, the rule varies
with the neighbor contents. The constant triple is included solely as a
mathematical control; a law constant on the whole possibility domain would
not satisfy the axiom's variation clause. Variation on this finite menu is
not inferred from variation somewhere in `M_2(C)`.

The additional stochastic data are mutually independent:

- `T_x`, iid uniform on `(0,1)`, used only through relative order;
- `E_{x,s}`, iid rate-one exponential variables, for `x∈Z^3,s∈M`, used to
  implement the local distribution.

Any iid atomless priority distribution on the real line gives the same
terminal record law, since every finite relative ordering is uniform. No
claim is made about non-iid marks. The priorities need no physical units and
are not identified with time measured by a record. The independent
exponential marks are a mathematical realization of fresh conditional draws;
they do not make the outcome distribution uniform.

All index sets are countable and all single-coordinate spaces are standard
Borel probability spaces, so the countable product probability measure
exists. This standard measure-construction fact is a mathematical tool,
not a physics premise.

The output is a measurable field `X∈M^(Z^3)` and a history

`R_u = {x↦X_x : T_x≤u}`, `0≤u≤1`.

The history parameter u is a supplied order parameter, not a derived
physical clock. Every bounded spatial window has finitely many jumps.
Every site forms once and its value is permanent. No priority or unused draw
mark is itself declared readable; the readout used below depends only on X.

## 2. Finite ancestry and the construction

A predecessor of x is any site reached from x along a nearest-neighbor path
with strictly decreasing priorities. Include x itself and call the resulting
set `A(x)`. Let `A(B)=union_{x∈B} A(x)` for finite B. Priorities are distinct
at every pair of sites almost surely, by atomlessness and a countable union.

For `m≥1`, define

`b_m = min{1, 6·5^(m−1)/(m+1)!}`.

**Lemma 1 (finite ancestry).** For each x,

`P(A(x) contains a site at distance ≥m from x) ≤ b_m`.

Every `A(B)` is finite almost surely. In particular there is no infinite
strictly decreasing nearest-neighbor path from any site almost surely.

**Proof.** A decreasing path cannot revisit a site. There are at most six
choices for its first edge and at most five for each later edge, because an
immediate return is forbidden. Thus there are at most `6·5^(m−1)` simple
paths of length m from x. On any fixed such path, the m+1 iid atomless
priorities have all `(m+1)!` relative orders with equal probabilities.
Exactly one order decreases. A union bound gives b_m. Reaching distance m
requires a decreasing path of at least m edges; its first m edges are
already a counted path. The uncapped bound tends to zero, since successive
terms have ratio `5/(m+2)`. If A(x) were infinite, it would leave every finite
ball. The probabilities of those decreasing events tend to zero. Therefore
A(x) is finite almost surely. Countability of sites makes this simultaneous
for all x, and a finite union proves the B statement. ∎

An infinite global order need not have a first site. Indeed, the infimum of
the iid uniform priorities is zero almost surely, and no site has priority
zero. Every interval `(0,u]`, u>0, contains priorities of infinitely many
sites almost surely. This does not obstruct Lemma 1: a fixed site's finite
predecessor set has a lowest-priority member. The proof never enumerates all
lattice sites as a sequence of globally earliest events.

For positive probabilities `a_s` summing to one, set

`F(a,E)=argmin_s E_s/a_s`.

The variables `E_s/a_s` are independent exponentials of rates a_s. Their
minimum is unique almost surely and

`P(F(a,E)=s)=integral_0^∞ a_s exp(−u sum_t a_t) du=a_s`.

This proves the sampling identity, including its normalization.

**Theorem 2 (mark-driven formation).** On the common probability-one set of
finite ancestry and tie-free marks, there is exactly one field satisfying

`X_x = F(r_x(·|X restricted to {y∈N(x):T_y<T_x}), E_x)`

at every site. It is measurable, translation- and proper-cubic-covariant in
law, and the displayed local r is its conditional distribution at formation.

**Proof.** Sort the finite set A(x) by increasing priority and apply F at
each site. Every lower-priority neighbor of a member lies in A(x), so this
procedure uses all and only the neighbors required by the formula. On
overlapping predecessor sets, the same recursive assignments agree by
induction in increasing priority. This constructs a single field and proves
uniqueness for the supplied marks. Uniqueness here does not quantify over
other schedulers or other possible statistical laws.

Each finite-window algorithm is Borel: there are finitely many priority
orders and finitely many comparisons of continuous marks. For each site,
its finite-window outputs eventually stabilize to X_x as the windows
exhaust Z3, by finite ancestry. Consequently X_x, and then the countable
field, are measurable. Define any fixed value on the null exceptional set;
that convention affects no distribution.

Translations and proper rotations preserve adjacency, priority comparison,
and φ. Transform the draw marks by `E'_{gx,gs}=E_{x,s}`. The minimization and
finite recursion commute with that transformation on the probability-one
set. The product mark measure is invariant under these index permutations,
giving covariance of the field and the history in law. An arbitrary
inverse-CDF ordering of labels need not commute pointwise; the race map
avoids that implementation issue.

Finally, fix x and condition on all priorities and all outcome marks at
sites y with `T_y<T_x`. Every earlier record is measurable with respect to
this information, because its predecessors are earlier still. E_x remains
independent with its original law. The displayed probability vector depends
only on the earlier neighboring records, so the race identity gives exactly
r_x. Conditioning down to the corresponding record history preserves that
same vector by conditional expectation. No future record content is read
to choose a site or to choose its odds. ∎

The occupation sets are increasing and no value is overwritten. For every
u>0 the state is spatially infinite but locally finite. There is no derived
autonomous discrete update `state→next globally formed site`, no claimed
finite-speed physical evolution in u, and no selection of an actual sample.

## 3. Certified finite-window computation

Let `X^W` be the finite algorithm on the induced finite graph W with absent
exterior sites, using the same T and E marks as X. A finite relative
priority order is uniform among the `|W|!` permutations. Conditional on that
order, the product of the successive local r vectors is the complete
formation law. Thus `Law(X^W)` is the uniform average of the fixed-order
formation laws; this statement concerns the finite window, not a uniform
choice of one site from infinite Z3.

**Theorem 3 (window bound).** If `B⊆W` is finite and
`d_1(B,W^c)≥m≥1`, then

`TV(Law(X_B), Law(X^W_B)) ≤ min{1, |B| b_m}`.

**Proof.** If A(B) stays inside W, both algorithms see identical predecessors
and draw marks at every required site, hence produce the same X_B. An
ancestor leaving W gives a decreasing path of at least m edges from some
member of B. Lemma 1 and a union bound bound the mismatch probability. For
every event C, the difference of its probabilities under the two outputs is
at most that mismatch probability, which is the stated total-variation
bound. ∎

The same coupling proves eventual almost-sure agreement along every nested
exhaustion and independence of the terminal limit from that exhaustion.
This is a limit of formation algorithms, not a DLR/static consistency
statement about finite formation laws.

An on-demand implementation first reveals priorities along lower-priority
neighbors until the search closes, then samples its finite predecessor DAG.
To certify closure it also inspects the immediate neighbor shell of A(B).
The output is therefore fixed by marks on that finite shell as well as
A(B). The extra shell must not be omitted when calling this a finite coding
radius. If `A(x)⊆ball(x,r)`, the certificate lies in `ball(x,r+1)`.

The expected work is finite without a temperature assumption. Counting a
possible path to each ancestor, with overcounting permitted, gives

`E|A(x)| ≤ 1+sum_{m≥1} 6·5^(m−1)/(m+1)! = 1+(6/25)(e^5−6)`.

At most seven times the number of ancestors are queried, including their
neighbor shell. This is an expected mark-count bound, not a hard cutoff.
The runner's `solve_local_z3` accepts a supplied consistent mark source and
implements exactly this search. Its deterministic fixture has seven
ancestors and 25 queried sites. No finite fixture is represented as a
sample of the ideal infinite iid law.

## 4. A content-only covariance bound

Let f,g be functions from M to `[0,1]`, and let x,y be at distance D. For any
integer `r≥0` with `2r<D`, compute the two truncated outputs in their separate
radius-r balls. These two outputs depend on disjoint sets of iid marks and
are independent. Each differs from its infinite-lattice output with
probability at most `b_(r+1)`.

For variables in `[0,1]`, changing either argument changes their product by
at most the sum of their absolute changes. Therefore the difference of the
joint expectations is at most `2 b_(r+1)`, and the difference of the products
of the means is at most the same amount. The independent truncated
covariance is zero, proving

`|Cov_form(f(X_x),g(X_y))| ≤ 4 b_(r+1)`.

This bound holds for every positive p,q,r in this supplied formation model.
No bound on the interaction strength was used. It does not apply to a
correlated-priority field, an infinite-time repeated update process, or a
static Gibbs law merely because that law has local conditionals.

## 5. A different infinite-lattice static statistic

Take the declared subfamily `p=q=t>1`, `r=1`. Write a projector's label as
an axis `a∈{0,1,2}` and a sign. Then

`φ(s_x,s_y)=1+v 1_{a_x=a_y}`, where `v=t−1>0`.

The finite static law on W has mass proportional to `product_edges φ`.
Its signs are independent fair signs and its axis law is the three-color
ferromagnetic Potts law. Both statements follow directly because the weight
depends only on the axes. These are properties of the displayed finite
weight, not a Born or physical-statistics assumption.

For a finite graph with edges E, expand

`product_{xy∈E}(1+v 1_{a_x=a_y})
 = sum_{A⊆E} v^|A| product_{xy∈A}1_{a_x=a_y}`.

Summing colors gives the bond weight `v^|A| 3^k(A)`, where k(A) counts all
connected components, including isolated vertices. Conditional on A, the
components choose their colors independently and uniformly. Hence, for
`f(s)=1_{axis(s)=0}`,

`E_static f(X_x)=1/3`,

`Cov_static(f(X_x),f(X_y))=(2/9) P_bond(x connected to y)`.

The factor `2/9` is `1/3−1/9`: connected sites share one uniform color;
unconnected components have independent colors. This is the usual
spin/bond representation, derived here on the exact finite domain used.

Fix all bonds except one. Inserting that bond either leaves k unchanged,
giving conditional occupation probability `v/(1+v)`, or merges two
components, giving `v/(3+v)`. Both are at least

`α = v/(3+v) = (t−1)/(t+2)>0`.

The same floor holds conditional on any subset of the other bonds, by
conditional expectation. Along any fixed path of D distinct edges, the
chain rule then gives probability at least `α^D` that every edge is
occupied. Thus, in every finite window containing such a path,

`Cov_static(f(X_x),f(X_y)) ≥ (2/9) α^D`.

There is at least one free-boundary infinite-volume static limit. To state
the standard extension step precisely: take an increasing sequence of
finite boxes. The probabilities of all cylinder events have a simultaneous
convergent subsequence by a diagonal extraction, since there are countably
many such events. Their limits are consistent finite-dimensional
probability measures on a countable product of finite discrete spaces;
the countable-product extension theorem gives a probability measure. The
static conditional identity at any fixed site and finite exterior cylinder
test passes to the limit, since it involves only finitely many coordinates
and eventually lies inside the boxes. A monotone-class extension then
gives that site's full conditional against the exterior sigma-algebra.
Thus the limit is a static law of the specified positive local kernel.

Every such free-boundary subsequential limit has the same one-site mean
`1/3` and retains the preceding pair lower bound, because these are cylinder
expectations. No uniqueness, phase claim, boundary-independent static limit,
or selection of a particular static measure is required.

**Theorem 4 (infinite-lattice discriminator).** For each `t>1`, the
random-priority formation law at `(p,q,r)=(t,t,1)` differs from every
free-boundary static subsequential limit at the same weights. A
content-only two-site covariance distinguishes them.

**Proof.** Use sites of even separation `D=2m` and disjoint radius `m−1`
balls. The formation covariance has absolute value at most `4 b_m`; the
static covariance is at least `(2/9)α^(2m)`. Once the uncapped b_m is below
one, the ratio of the former bound to the latter is

`R_m=108·5^(m−1) α^(−2m)/(m+1)!`.

Its successive ratio is `R_(m+1)/R_m=5/[(m+2)α^2]`, which tends to zero.
Consequently R_m tends to zero. Choose an m with R_m<1. The covariance
intervals are disjoint. ∎

For an explicit exact certificate choose `t=2`, `x=0`, `y=512 e_1`, and
`m=256`. Then α=1/4, and the two bounds are

`|Cov_form| ≤ 24·5^255/257!`,

`Cov_static ≥ 2/(9·4^512)`.

They are separated by the exact integer inequality

`257! > 108·5^255·4^512`.

The runner checks this independently of fraction simplification and also
checks `10^−21 < R_256 < 10^−20`. This distance was chosen to make the loose
analytic bounds separate; it is not a claim of the first distance at which
the laws differ, a sharp correlation estimate, or a practical experimental
resolution. No simulation of a 512-site sample proves the statement: the
probability bounds and the integer comparison do.

The readout f is determined by a record's matrix content: on this menu it
equals `(Tr(σ_1 P))^2`. Both sites carry records in the terminal state. The
comparison is between the two explicitly supplied mathematical probability
laws; it does not turn these ensemble probabilities into measured physical
frequencies.

At `t=1`, the rule is constant and both terminal laws are the uniform
product law. The static lower-bound argument is not asserted for t<1 or
for general unequal p,q. The formation construction and its error bounds
still hold for all strictly positive triples.

## 6. Exact finite controls and actual results

The standard-library runner uses rational and integer arithmetic only. It
imports no prior runner, makes no network requests, and writes no files.
The mathematical infinite arguments are in this note; the tests are finite
controls and arithmetic certificates, not a finite enumeration of Z3.

- All 924 multisets of zero through six neighbor values: positive normalized
  conditionals at `(3,1,2)`, with 133,056 per-label covariance comparisons.
- A full cube fixture: direct sorted evaluation versus ancestor evaluation;
  all 24 proper rotations with transformed marks; a translation; an
  on-demand Z3 fixture whose certificate reads exactly 25 sites.
- All 216 path3 and 1,296 C4 configurations: complete averaging over orders
  agrees with independent forward probability flow over partial states.
- Nested path4/path3 controls at `(3,1,2)`: the first-edge marginal has
  exactly zero error despite a nonzero ancestry-escape probability `1/6`;
  the `(0,2)` pair has total-variation error `1/8424`, below its exact escape
  probability `1/2`. The initial runner incorrectly expected the first of
  these errors to be positive. That assertion failed and was replaced by
  the proved equality control; the failed output remains in the packet.
- Independent spin sums (`3^4`, `3^8` configurations) and bond sums (`2^4`,
  `2^12` configurations): C4 partition 258 and opposite-site covariance
  `11/387`; cube partition 219042 and opposite-corner covariance
  `2632/109521`. Every conditional bond insertion floor is exactly `1/4`.
- The displayed distance-512 inequality and its rational margin.

The adaptive finite-C4 appendix below has additional enumerated controls.
Current full runner result: `TOTAL: PASS=41 FAIL=0`. Author execution is
separate from the requested independent review.

## 7. Priors, novelty, and supplied mathematical tools

The frozen four axioms in
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) supply the
lattice, possibility presentation, local distribution clause, and permanent
record/readability interface. Neither they nor the scale-reference,
kinetic-isotropy, or realized-state primitive supply the mark law used here.
The parked statistical Bridge stays unadopted under its standing default.
No source/action identification or decision wake condition is claimed.

The nearest actual open-PR predecessors were read at these exact heads:

| Prior | Exact contribution used for comparison, not hidden premise |
|---|---|
| #7998, `8b26a1c59aa0dd30ca25c8f07a4240723c032c8b` | Same finite menu and product rule; fixed-order/static classification, and a computed uniform C4 order mixture. The definitions and needed finite identities are stated here. |
| #7999, `bf1710f71fe3c81b656864f9a6a043e6fadd84df` | Static specification/existence on Z3 and an infinite directed row sweep on a strip. It supplies no covariant random-priority formation law on Z3. |
| #8000, `d61adbe4cb0bcb245235b6525b6ff577cafb6bb1` | Static uniqueness under one-site contraction. This note does not need that criterion. |
| #8002, `be102438f655dd18019634fa46ab7aba8b1a14d9` | Pair-block sensitivity and the corrected joint-supremum coupling bound. Its gravity probe concerns a different complex action; no Gaussian/action conclusion is imported here. |
| #6347, `66ded17d80d44d90f5aa9ec52a8950ba573d4b55` | A synchronous Borel kernel and finite-time histories from finite Record states, with a different occupancy-difference law. Its scope explicitly excludes arbitrary infinite-state construction. |
| Main, `INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md` | An iid local-minimum seed construction for isolated finite diamonds. It already establishes that invariant iid seed models can be supplied. It is not this recursive content-dependent full-lattice law. |

The primary mathematical precedent for decreasing-path ancestry and
factorial tails is [Ritchie, *Construction of the Thermodynamic Jamming
Limit*, arXiv:math/0412343v2](https://arxiv.org/abs/math/0412343v2), especially
section 3. Its exclusion update is different, so the argument needed here
is re-proved in sections 2–4. The count uses nearest-neighbor degree six,
rather than importing the paper's general-range neighborhood constant.

The spin/bond expansion is the classical representation described by
[Edwards and Sokal, Phys. Rev. D 38, 2009 (1988)](https://doi.org/10.1103/PhysRevD.38.2009).
Section 5 derives the finite identity, conditional floor, and pair readout
directly, with explicit conditions `v>0` and three colors. Standard
countable-product measure extension, conditional expectation, and the
monotone-class principle are mathematical tools with their domains stated;
they do not supply a physics law. No external theorem is invoked to assert
that the present axioms select this model.

The novelty claim is limited to this repository target: a self-contained
infinite formation process for the stated local rule, its finite-window
error certificate, and a same-carrier static/formation statistic. Random
sequential construction and the spin/bond representation are established
mathematics. The open-PR inventory and frozen-main exact-term search found
no duplicate of this combined statement; that search is not a universal
literature-priority claim.

## 8. Provisional finite-C4 adaptive-scheduler appendix

This appendix preserves a useful independent-review target. It is a
finite-domain lemma proposal with exact controls; it is not packaged as a
global no-go or as a claim that every irreversible formation mechanism
fails. The main construction and infinite discriminator do not consume it.

Let W be a single open C4 with the same positive product rule. At each step,
a scheduler chooses a still blank site using the entire formed history and
its own randomness; the chosen site then makes a fresh draw from r. All
four sites eventually form. The scheduler cannot inspect pending values,
change a drawn value, select a site by a correlated pending draw while
keeping the declared selected-site odds r, or condition on eventual success.

For each complete assignment v and order σ, let `a_σ(v)` be the product of
the scheduler's conditional site-choice probabilities along the prefixes
of v in that order. The finite choice tree has

`a_σ(v)≥0`, `sum_σ a_σ(v)=1`,

and its terminal probability is

`P_sched(v)=sum_σ a_σ(v) μ_σ(v) ≤ max_σ μ_σ(v)`.

These mixture coefficients can depend on v; this is a pointwise envelope,
not a fixed convex mixture of measures. Auxiliary scheduler memory can be
included in its histories or integrated out in the same chain rule. The
fresh-r-draw condition is essential to that factorization.

Write `z=p+q+4r`, `a=p+q−2r`, `b=p−q`. The pair matrix has eigenvalues z,a,b
of multiplicities 1,2,3: constant vectors; sign-even vectors with zero sum
over axes; and sign-odd vectors on each axis. Thus

`Z_C4=Tr Φ^4=z^4+2a^4+3b^4`.

For a fixed monochromatic v, 16 orders give probability

`p^4/[z^2(z^2+2a^2+3b^2)]`,

and the other eight give

`p^4/(z^2+2a^2+3b^2)^2`.

The two cases are whether the first two formed sites are adjacent or
opposite. Their predecessor counts are respectively `(0,1,1,2)` and
`(0,0,2,2)`. The one-neighbor normalizer is z and the same-value
two-neighbor normalizer is `(z^2+2a^2+3b^2)/6`, which gives both formulas.

The first is the larger. Positivity gives `|a|,|b|<z`; nonconstant weights
give `(a,b)≠(0,0)`. Therefore

`z^2(z^2+2a^2+3b^2)−Z_C4
 =2a^2(z^2−a^2)+3b^2(z^2−b^2)>0`.

The static probability of every monochromatic v is consequently above its
adaptive envelope. At `(3,1,2)`, the event that all four records are equal
has static probability `81/3464`, adaptive upper bound `9/416`, and gap
`315/180128`. The constant rule gives equality. The runner checks the two
order formulas and the event gap at five triples, and checks all 1,296
pointwise envelopes for one normalized scheduler that favors sites next to
already formed label-0 records. Its arbitrary label preference is permitted
only as a test of the unrestricted finite scheduler lemma; it is not the
covariant scheduler of Theorem 2.

This lemma, if independently confirmed, addresses only fresh local draws
under a one-at-a-time nonanticipating schedule on the open plaquette.
Simultaneous correlated formation, a different absence rule, nonlocal
marginal draws, and correlated seeds remain different models. No infinite
static conclusion is inferred from this finite event.
