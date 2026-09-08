---
claim_id: matter_law_ticks_realise_menus_in_one_frame_only_abundance_unpaid_2026_09_04
claim_type: bounded_theorem
claim_scope: "On finite subgraphs of the cubic lattice with qubits on the EDGE sites, the superfast encoding, the corner parity dictionary n_v = (1 - B_v)/2, the staggered (pi-flux) Kawamoto-Smit sector H = -sum_e eta_e T_e at half filling, and the STIPULATED tick of PR #7876 Model A -- the 2x2x2 cube, the 2x2x3 slab, the 4^3 torus in its ground twist sector (1,1,1) and, for closure counts only, the 6^3 and 8^3 tori. For the DECLARED formation units (single edge site, corner star, column pair, whole superlattice class) the exact conditional record law P(w|w_0) = q_F(n_0 + A_U w)/sum q_F is computed over complete condition families. (T1) The record law is P(w) = 2^-g p(A w) with p the determinantal corner law; on the cube it is rational with D = 144, values {1/144, 1/48, 1/36, 1/16}, support 1984 = 32 x 62, agreeing with the many-body sea to 3.5e-18; K_AA = K_BB = I/2 exactly on the cube, the slab and the 4^3 torus; the slab support is 411648 = 512 x 804. (T2) Single-site formation on the cube, complete over all 3^11 conditions at each of the 12 sites: exactly three menus {P0,P1}, {P0}, {P1}, 129 odds vectors, first forcing at k = 8; PR #7919's control table 1/24/264/1760, its five odds at k = 3 and its edge-9 witness reproduce; nearest-neighbour records never move a site off 1/2, while all 192 (site, NN pattern) pairs vary with far records. (T3) The cube corner star is complete over all 3^9 conditions at all 8 corners: 69 menus of sizes 4 to 8, never 3; 1329 odds vectors; exactly one full basis. The slab column pair and degree-4 star are reduced here to the class tick's own conditions (421 and 285 menus); their complete counts 11405/95631 and 1093/358125 are quoted from the source computation. The class tick's first two events on every object offer the full basis at uniform odds -- one menu, condition-independent -- and proper supports with non-uniform odds enter only when an event closes a corner of the other sublattice. (T4) On the 4^3 torus, families T0-T3 are exact with 1/5/25/141 menus and 1/12/200/4096 odds vectors; the T6 float census over 2097152 condition classes (21656 menus, no full basis) is quoted, its exact declared sub-family agreeing on 312 of 312 classes. (T5) At every unit the global menu-independence clause is refuted by the supports alone: the incidence system is inconsistent, witnessed by two disjoint realised menus together with the full basis. The fibred clause of PR #7931 holds as an identity to 3.7e-15 with exactly one menu per fibre and 0 exceptions, and forces nothing: the uniform-on-support grading is a menu-independent non-Born grading on 126 of 129 site fibres, 1324 of 1329 star fibres, 95630 of 95631 pair fibres and 4765 of 4766 torus fibres. None of PR #7950's killing menus appears in the qubit-domain or the joint-domain sense; no realised menu has three outcomes at any unit. The abundance item of the Born price is therefore unpaid by this tick. The cluster, encoding, sector, filling, tick, units and the Born line's own definitions are all supplied; no axiom content is derived here. No seeds anywhere."
upstream_dependencies: []
runner: scripts/matter_law_ticks_realise_menus_in_one_frame_only_check_2026_09_04.py
---

# The matter law's own ticks realise menus in one frame only: at every formation unit the global menu clause is refuted by the supports, the fibred clause is an identity with a uniform rogue, and the abundance item of the Born price is unpaid

**Date:** 2026-09-04 | **Type:** bounded_theorem | **Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, registry, queue, policy or audit verdict.
**Primary runner:** [`scripts/matter_law_ticks_realise_menus_in_one_frame_only_check_2026_09_04.py`](../scripts/matter_law_ticks_realise_menus_in_one_frame_only_check_2026_09_04.py)
**Runner cache:** [`logs/runner-cache/matter_law_ticks_realise_menus_in_one_frame_only_check_2026_09_04.txt`](../logs/runner-cache/matter_law_ticks_realise_menus_in_one_frame_only_check_2026_09_04.txt)
**Parents:** none on main. Every premise used below is declared in this note.
**Open sibling branches, none on main:** the Born line — PR #7919 (menu-independence and abundance), PR #7926 (the continuum record alphabet),
PR #7931 (the fibred clause), PR #7950 (the killing menus); the tick line — PR #7947 (site-wise formation) and PR #7968 (the class tick); and the note
on the determinantal record statistics of the half-filled sea.

## Result Up Front

The Born line prices the Born form in three items: a fibred menu-independence clause, abundance of realised menus, and a frame import that PR #7950
removes. The open question this note answers is whether the matter law's own formation events supply the second item by themselves. They do not, and
the reason is structural rather than a matter of unit size. Record locks one `Z` value at each edge site, so the possibilities a formation event
offers are computational-basis vectors of its record domain: **every realised menu is a subset of one fixed orthonormal frame**, the record basis of
the unit's edge sites, with odds the diagonal of the conditioned sea. On that family the **global** menu-independence clause is not merely unforcing
but inconsistent — refuted by the supports alone, two disjoint realised menus together with the full basis — while the **fibred** clause holds as an
identity, carries exactly one menu per fibre, and leaves an explicit menu-independent non-Born grading standing on almost every fibre. The abundance
item is unpaid at the single site, the corner star, the column pair and the whole class alike.

## Machine status

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on three clusters in the staggered sector at half filling, for the stipulated tick of PR #7876 Model A and formation units declared in full here. Every support and every odds vector is exact -- rational on the cube and the 4^3 torus, in Q(sqrt2) on the slab -- and every odds vector is canonicalised exactly in Z[sqrt m]. The rank certificates are exact eliminations over Q on integer incidence rows. The only floating point is the cross-check of the exact record law against the many-body sea and the reduced record-conditioned states behind the fibred clause, both labelled where they appear. Condition families are complete enumerations or lists written out in the runner; three of the source computation's complete censuses are reduced here to declared sub-families and their complete counts quoted. Nothing is sampled, there is no seed anywhere, and no dense object above 4096 x 4096 is formed."
trace_class: upstream_support
target_claim_id: born_form_scaled_projector_arity_three_threshold
target_blocker_text: "prove ternary scaled-projector sufficiency or find a rogue"
source_of_blocker_text: frontier_question
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Price the missing item where it can be paid: ask which record alphabet a designed matter law would need for a formation event to register in a second frame, and whether any law of that kind preserves a sea at all. The continuum alphabet of PR #7926 is the one on record."
conditional_surface_status: "exact statements conditional on the supplied cluster, encoding, sector, filling, tick and formation units, and on the Born line's own definitions of menu, grading, menu-independence, the fibred clause and abundance"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

A finite subgraph `G = (V, E)` of the cubic lattice carries one qubit per **edge site**; the superfast encoding with Kawamoto-Smit staggered signs
gives flux `-1` on every face, `H = -sum_e eta_e T_e`, one-particle matrix `h_ij = -eta_ij`, and the sea is the code-space ground state at half
filling, a Slater determinant with one-particle kernel `K = P_W`. A record at edge `e` registers `Z_e`; the corner parity dictionary is `n_v = (1 -
B_v)/2`, the parity of the records on `star(v)`. The tick is PR #7876 Model A: Lueders formation with the odds of the pre-record state, `exp(-i tau
H_R)` between formations. All of that is supplied, not derived.

The Born line's terms transport to a formation unit as follows. A **formation event** forms the unrecorded edges `U` of a unit — a site, a corner
star, a column pair, a whole superlattice class — jointly, under a **condition** `(R_0, w_0)`: records already present on the other edges `R_0`. Its
**menu** is the support of the conditional record law on `U`, which is reading note (3) of Admissibility read at the unit; its **possibilities** are
the record patterns `w in {0,1}^U`, that is the rank-one projectors `|w><w|` of the record basis of the unit's domain `C^(2^|U|)`. A **grading**
assigns a number to a possibility without regard to the menu it appears in; **menu-independence** is that clause, and the **fibred** clause of PR
#7931 asks it only within a fibre of the conditioned state. A menu is a projective decomposition of the unit's domain iff it is the full basis;
otherwise it resolves the projector onto its own span.

With `A` the corner-edge incidence over `F2` and `g = |E| - rank A`, the record law is `P(w) = 2^-g p(A w)` with `p(n) = det(diag(n) K + diag(1-n)(I -
K))`. Conditioning is exact and combinatorial: with `F = E` minus `(U u R_0)` the still-unrecorded edges and `L_F = A_F F2^F`,

> `P(w | w_0) = q_F(n_0 + A_U w) / sum_{w'} q_F(n_0 + A_U w')`, `q_F(n) = sum_{l in L_F} p(n + l)`, `n_0 = A_{R_0} w_0`,

so a condition acts only through the coset `n_0 + L_F`. Conditions are therefore enumerated by coset classes with their exact multiplicities, `q_F` is
an exact integer Walsh-Hadamard convolution, and every odds vector is canonicalised exactly in `Z[sqrt m]`.

**Four lemmas.** *(1) One frame.* Record locks exactly one value at each edge site and this law registers `Z_e`, so a joint outcome is a
computational-basis vector: every realised menu is a subset of one fixed orthonormal basis, any two realised menus commute, and no realised effect has
scale `c < 1`. *(2) The state fixes the menu.* With `sigma(n)` the record-conditioned sea reduced to the unit's qubits, the menu is `supp
diag(sigma(n))`, so each fibre of the fibred clause carries exactly one menu. *(3) The Born identity.* `p(w|n) = <w|sigma(n)|w>` is the record-basis
marginal read two ways; it is an identity, not a test of the Born form. *(4) Uniform until closure.* If a formation event of the class tick closes no
corner of the other sublattice, its menu is the full basis with uniform odds `2^-|U|`, because `q_F(n)` is then the marginal law on the closure, the
outcome enters only through `n_S(w)`, each class has `2^(|U| - |S|)` members, and `n_S` is uniform and independent of the formed corners by `K_AA =
I/2`.

## The axioms, quoted

> **Admissibility / Local Constraint.** *There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
> rotations.* *For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.*
>
> **Record / Fixed Reality.** *When present, a record locks exactly one admissible local possibility. A site never carries more than one record;
> records are permanent.* *Only records are readable. A readout value is determined by record content alone.*

Nothing below is derived from an axiom. Reading note (3) fixes "menu" as the support of the local distribution; reading note (2) leaves the formation
site, probability, rate and unit open.

## T1 — The exact record laws

On the `2x2x2` cube `h^2 = 3I`, so `K = (I - h/sqrt3)/2` is exact in `Q(sqrt3)` and nearest-neighbour, with `K = K^T = K^2`, `tr K = 4` and `[h, K] =
0` exactly. The corner law has `62` nonzero patterns of `256`, all at `|n| = 4`, summing to `1`, **rational** with common denominator `D = 144` and
values `{1/144, 1/48, 1/36, 1/16}`; its eight cancellation zeros are exactly the eight closed corner stars `{v} u N(v)`. The record law `P(w) = 2^-5
p(A w)` has support `1984 = 32 x 62` on the `4096` labels and agrees with the many-body sea of the superfast encoding — code dimension `128`, `E = -4
sqrt3` — to `3.5e-18`.

On the `2x2x3` slab `spec(h^2) = {2,4}` and `K` is exact in `Q(sqrt2)`; the corner law has `804` nonzero patterns of `4096`, all at `|n| = 6`, `D =
8192`, `23` distinct values and `392` patterns with a `sqrt2` part, and the record law `P(w) = 2^-9 p(A w)` has support `411648 = 512 x 804`. On the
`4^3` torus in its ground twist sector `(1,1,1)`, `h^2 = 6I` exactly, so `K = (I - h/sqrt6)/2` in `Q(sqrt6)` with `tr K = 32`.

> **`K_AA = K_BB = I/2` exactly on all three objects.** This holds because `sgn(h)` is off-diagonal in the sublattice decomposition when `h` is, and it
> is why the even corners' occupations are independent fair coins: the even-sublattice marginal is `2^-|A|` on every pattern. It is the hinge of Lemma
> 4, and it removes the matrix inversion from the torus computation, since a set `T` of formed even corners has `K_TT = I/2` and so `M_TT = I/2`.

## T2 — Single-site formation: one binary menu and two forced singletons

On the cube the census is complete: all `12` sites and all `3^11` conditions on the other eleven edges, `2105028` valid conditions in all, `12 / 264 /
2640 / 15840 / 63360 / 177408 / 354816 / 506880 / 506880 / 336384 / 122880 / 17664` by the number `k` of prior records. Over every site and every
condition there are exactly **three** menus — `{P0,P1}`, `{P0}`, `{P1}` — and **129** distinct odds vectors. No singleton menu occurs through `k = 7`;
the first forced record is at `k = 8`.

PR #7919's control reproduces exactly: nonzero record blocks `1 / 24 / 264 / 1760` at `k = 0..3`, the odds at a free edge `1/2` for `k <= 2` and the
five values `{5/18, 1/3, 1/2, 2/3, 13/18}` at `k = 3`, and its witness — records `0` on edges `0..6` and `8` lock edge `9` — giving support `{P1}` and
odds `[0, 1]`.

Two facts about the carrier follow. Nearest-neighbour records never move a site's odds off `1/2`: every condition whose records lie on the four edges
sharing a corner with the site gives the single odds vector `[1/2, 1/2]`, by particle-hole symmetry `p(n) = p(1-n)`, invariance of the record law
under a perfect matching, and `p(00) = p(11)` on an adjacent pair. Yet fixing the whole nearest-neighbour pattern and letting the far records vary,
**all `192` (site, NN pattern) pairs carry several odds values**, with spread `1` — the same NN pattern completes to conditions whose odds are
`[0,1]`, `[1,0]` and everything between. The odds a forming record receives are a function of records at distance two and beyond, and are not a
nearest-neighbour function on the edge-site lattice at all.

On the slab, over all conditions with `k <= 4` at every site, all nearest-neighbour conditions and all whole-class conditions, there is one menu
`{P0,P1}` everywhere with `73` odds vectors and no forcing.

## T3 — The joint units

**Cube corner star** (three records, domain `2^3`), complete over all `3^9` conditions at all eight corners: **69** menus of sizes `{4: 8, 5: 24, 6:
28, 7: 8, 8: 1}` — **never three** — and **1329** odds vectors, with exactly **one** full basis. `37` of the `69` menus carry several odds vectors, up
to `849` on the full basis. The eight size-4 menus are four complementary pairs. Restricted to nearest-neighbour conditions there are `5` menus of
sizes `{6: 4, 8: 1}` and `27` odds vectors.

**The cube's even-class tick**, all `24` orders and every prior outcome, step by step: menus `1 / 1 / 13 / 32`, odds vectors `1 / 1 / 18 / 32`,
uniform odds vectors `1 / 1 / 0 / 0`. Steps 1 and 2 offer the full basis at `1/8` for every condition; step 3 closes one odd corner and step 4 the
remaining four.

**Slab units, declared sub-families.** T2's minimal eigen-sets are the classes `{4}, {7}, {0,2}, {9,11}` and their odd partners. Restricted to the
class tick's own conditions the column pair realises `421` menus of sizes `{19, 25, 31, 32, 44, 56, 60, 64}` with `423` odds vectors and exactly one
uniform, and the degree-4 star `285` menus of sizes `5` to `16` with `501` odds vectors and one uniform. The source computation's complete censuses
over all `3^14` and all `3^16` conditions — `11405` menus and `95631` odds vectors for the pair, `1093` menus and `358125` odds vectors for the star —
run over millions of conditions and are **quoted, not recomputed here**. The slab class tick, all `24` orders: menus `2 / 2 / 166 / 960`, odds vectors
`2 / 2 / 192 / 1152`, uniform `2 / 2 / 0 / 0`.

**Closure, exactly.** On all `32` distinct (prior classes, unit) steps of the cube's even-class tick and all `32` of the slab's, the menu is the full
basis with uniform odds **iff** the event closes no corner of the other sublattice — Lemma 4, verified step by step. On the `6^3` and `8^3` tori the
classes carry `162` and `384` records and the pure-`F2` closure counts are `0, 0, 27, 108` and `0, 0, 64, 256`, so there too the first two events are
the uniform full menus `2^-162` and `2^-384`.

**Coarse-grainings are readings.** A grouping of a menu's outcomes — the blocks `{w : n_v(w) = 0}` and `{w : n_v(w) = 1}` of a star's eight outcomes,
say — is a set of projectors of rank above one in the record basis. No formation event realises one: by Lemma 1 every realised possibility is
rank-one, each edge site's record being locked individually. The corner occupations are therefore **readings** of the records — "a readout value is
determined by record content alone" — never formation alternatives, and their determinantal law is the sea's corner law read off the records rather
than a menu the tick offers.

## T4 — The `4^3` torus, ground twist sector, six-record star

Every corner is its own class here and the unit is one corner star of **six** records, domain `2^6 = 64`. The conditional law is the closure marginal
with the Schur-complement kernel; because the formed corners lie in one sublattice, `M_TT = I/2` exactly and no inversion enters. Over the declared
even-corner families:

| family | closes | condition classes | menus | sizes | odds vectors | full basis |
|---|---|---|---|---|---|---|
| T0: none | — | 1 | 1 | 64 | 1 (`1/64` each) | 1 |
| T1: `N(+x)` formed | 1 | 64 | 5 | 48, 64 | 12 | 1 |
| T2: `N(+x), N(-x)` | 2 | 2048 | 25 | 32, 48, 56, 64 | 200 | 1 |
| T2: `N(+x), N(+y)` | 2 | 2048 | 25 | 32, 48, 56, 64 | 200 | 1 |
| T3: `N(+x), N(+y), N(+z)` | 3 | 32768 | 141 | 20, 32, 40, 48, 56, 60, 64 | 4096 | 1 |
| T6 sub-family, exact | 6 | 312 | 193 | 7, 20, 23, 63 | 257, all rational | 0 |

T0 through T3 are exact and complete over every condition class of the family. The full T6 census — all six odd neighbours closed, `2097152` condition
classes of which `2097088` are valid, `21656` menus with sizes from `7` to `63` and no full basis — is float64 in the source computation and is
**quoted**; its exact declared sub-family agrees with it on `312` of `312` classes and to `3.9e-16` on every odds value. A mixed-parity nearest-neighbour
condition, one odd neighbour's star formed first, gives one menu of `32` with two non-uniform odds vectors of values `{5/192, 7/192}`.

## T5 — The Born test on the realised families

**(G) The global clause is refuted by the supports.** For each family the incidence system `sum_{w in M} g_w = 1` over the realised menus is solved
exactly over `Q`. On every family realised by more than the first two tick events **no normalised grading exists at all**, Born or not: the system's
rank is below the rank of its augment. The certificate is that rank gap; read out, it says that two disjoint realised menus each sum to `1` while
the full basis, realised too, sums to `1`. Such a pair is available at every unit: the site's two forced singletons; the star's complementary size-4
pair `{0,1,2,4}` and `{3,5,6,7}`; disjoint size-19 menus on the slab pair, size-5 on the degree-4 star, size-32, size-20 and size-7 on the torus.
Ranks: site `2`, cube star `8`, slab pair `64`, slab degree-4 star `16`, torus T1 `4`, T2 `8`, T3 `16`, T6 `64`, and `64` on the `353` pooled torus
menus. This is a stronger refutation than PR #7919's five odds on one menu, which also appears here: `37`, `5437` and `949` menus carry several odds
vectors, up to `266133` on one. Where the family is a single menu — the site through `k = 7`, the torus at T0 — the system is consistent, the sum is
pinned to `1`, and every normalised grading on that menu is a diagonal state, so the Born form is unforced in the opposite sense: it says nothing.

**(F) The fibred clause is an identity, and it forces nothing.** `p(w|n) = <w|sigma(n)|w>` holds to `3.7e-15` over PR #7931's complete control family
and over the complete site and star censuses; no fibre carries two menus — `0` exceptions over `175419` site conditions and `19619` star conditions,
and the source computation reports the same over all twelve sites and all eight stars. The per-fibre solution space therefore has dimension `|M| - 1`,
and the uniform-on-support grading `g(w) = 1/|M|` is menu-independent, normalised, and **differs from the Born vector on every fibre with non-uniform
odds**: `126` of `129` site fibres, `1324` of `1329` star fibres, `95630` of `95631` pair fibres and `4765` of `4766` torus fibres. It coincides with
Born exactly where the odds are already uniform — at the first two class events on every object.

**(K) The effect census.** Every realised possibility is a rank-one projector of the one record basis: every menu's odds live on its own support and
sum to `1` exactly, and the realised menus cover the basis. At a site the realised effects are `P_0` and `P_1` and nothing else — no `cP(n)` with `c <
1`, no direction other than the record axis, no balanced ternary, no coin, no collinear ternary, no mixed coin ternary, no four-outcome collinear
menu. In the joint-domain sense **no realised menu has three outcomes at any unit**: the minimum sizes are `4` on the cube star, `19` on the slab
pair, `5` on the degree-4 star and `7` on the torus star, and the only four-outcome menus anywhere are the cube star's eight, which are four
complementary pairs of rank-one projectors of one frame. So none of PR #7950's killing menus appears in either sense, and the homogeneity question is
void, all scales being `1`.

## Corollary — the abundance item is unpaid, and what would pay it

> Every formation event of the designed matter law offers a subset of **one** orthonormal frame, the record
> basis of the unit's edge sites, with odds the diagonal of the conditioned sea. The family it supplies
> therefore contributes **zero abundance** in the Born line's sense. The fibred clause is satisfied identically
> and forces nothing. A positive forcing at any unit would need registrations in a **second frame** — menus not
> commuting with the record basis — and no tick of this law produces one.

The missing item is not a theorem to import. It is a change of the designed law's record alphabet: the property PR #7926 names "abundance is a
property of the law" and supplies by fiat in `L_CONT`, whose continuum alphabet is the one on record. Against PR #7950's re-pricing the reading is
unchanged in form and sharper in content — the price stays **fibred clause plus abundance with collinear menus**, or **fibred clause plus abundance
plus homogeneity** — and the matter law does not pay it. Nothing here says the Born form is false, and nothing here derives it; what is settled is
which of the two clauses this particular family can bear.

## Disagreements with the brief, stated plainly

1. **There is no six-record star and no twelve-record column pair in the corpus.** Those are `Z^3` objects of
degree six. On the cube the corner star has **3** records, on the slab the column pair has **6** and the degree-4 star **4**. The `2^6` domain is
realised by the slab pair and by the torus star; no `2^12` unit exists on any object computed.
2. **The sea-preserving tick's first two events carry no state information.** Their menus are the full basis at
uniform odds, identical for every condition, on the cube, the slab, `6^3` and `8^3` alike. Admissibility's "varies with the nearest-neighbor
conditions" is exercised at this unit only through closure.
3. **PR #7931's `172` fibres reproduce only with the site in the key.** Keyed by `(rho_00, rho_11, |rho_01|)`
and pooled over sites there are `21`; with the site in the key there are `172`. The condition, pair and check counts `9969 / 82116 / 164232` reproduce
exactly.
4. **A criterion conjectured mid-run was wrong.** "Uniform iff the unit's incidence columns lie in `L_F`" holds
at no step of any tick computed — the unit's own corner is touched by no free edge — and closure is the correct predictor. Both are checked side by
side.

Two smaller corrections: the refutation of the global clause is by supports, not by odds, which is stronger than expected; and family T6 on the torus
has essentially every condition class distinct (`2093568` odds vectors on `2097088` classes), so an exact census of it is out of reach and only a
declared sub-family is exact.

## Reading, not theorem

If a rule hands out odds over the alternatives a single event offers, and it always offers alternatives drawn from one and the same list of mutually
exclusive readings, then asking whether its odds are the quantum ones is asking a question the rule cannot answer. It can be checked for consistency,
and it fails that check immediately: the rule sometimes offers the whole list and sometimes offers two halves of it, and no single assignment of
numbers to entries can make all three add to one. Restricting the question to one situation at a time makes it consistent again, but then it is empty
— the answer is whatever the situation's own numbers are, and a flat "one over the number of live entries" does just as well nearly every time. What
is missing is a second, incompatible list of readings, and the law being studied never writes one down. That is a property of what the law records,
not of how big a piece of it forms at once.

## Executable claim block

```text
objects: 2x2x2 cube; 2x2x3 slab; 4^3 torus twist (1,1,1); 6^3 and 8^3 tori, closure counts only
record_law: P(w) = 2^-g p(Aw); cube D = 144, values {1/144,1/48,1/36,1/16}, support 1984, sea agreement 3.5e-18
slab_law: 804 nonzero corner patterns, D = 8192, 392 with a sqrt2 part, support 411648 = 512 x 804
sublattice: K_AA = K_BB = I/2 exactly on the cube, the slab and the 4^3 torus; even marginal 2^-|A|
single_site_cube: 2105028 conditions complete; 3 menus {P0,P1},{P0},{P1}; 129 odds; first forcing k = 8
markov: NN-only conditions give one odds vector [1/2,1/2]; all 192 (site, NN pattern) pairs vary, spread 1
cube_star: 69 menus, sizes {4:8,5:24,6:28,7:8,8:1}, never 3; 1329 odds; one full basis; 37 menus multi-odds
cube_class_tick: menus 1/1/13/32, odds 1/1/18/32, uniform 1/1/0/0; record blocks 1/24/264/1760 at k = 0..3
slab_subfamilies: pair 421 menus / 423 odds / 1 uniform; degree-4 star 285 / 501 / 1; tick 2/2/166/960 menus
slab_quoted: complete pair census 11405 menus and 95631 odds; complete star census 1093 and 358125
closure: uniform full menu iff no other-sublattice corner closes, on 32 cube and 32 slab steps; 6^3 0,0,27,108, 8^3 0,0,64,256
torus_exact: T0/T1/T2/T3 give 1/5/25/141 menus and 1/12/200/4096 odds vectors; one full basis each
torus_quoted: T6 float census 2097088 valid classes, 21656 menus, no full basis; exact sub-family 312/312
global_clause: inconsistent at every unit; ranks 2, 8, 64, 16, 4, 8, 16, 64, 64 pooled; disjoint-menu witness
fibred_clause: identity to 3.7e-15; one menu per fibre, 0 exceptions; per-fibre dimension |M| - 1
uniform_rogue: menu-independent, normalised, non-Born on 126/129 site, 1324/1329 star, 95630/95631 pair fibres
effects: all rank-one in one frame; no three-outcome menu at any unit; min sizes 4 / 19 / 5 / 7
killing_menus: none of PR #7950's appears in the qubit-domain or the joint-domain sense; all scales are 1
arithmetic: exact rational and Q(sqrt2), Q(sqrt3), Q(sqrt6); no seed; floats only where labelled
runner_result_required: zero failed checks
```

## Interfaces

**PR #7919.** Its three-item price is what the Corollary re-reads at a formation unit; its control table `1 / 24 / 264 / 1760`, its five odds at `k =
3` and its edge-9 witness are reproduced here exactly, and its "nearest-neighbour law with a finite record alphabet" is not what this carrier
realises. **PR #7926.** Its `L_CONT` is the continuum alphabet against which the missing item is priced; nothing here says the framework's law is that
one. **PR #7931.** Its fibred clause is the clause verified here as an identity; its `172` fibres reproduce with the site in the key. **PR #7950.**
Its killing menus and its exact rank instrument are used directly; none of the menus is realised. **PRs #7947 and #7968.** They supply the tick and
the formation unit: the sea-preserving unit is a whole superlattice class, and the class tick's step tables here are computed on their objects. **The
determinantal record statistics.** The conditional corner law used throughout is theirs.

## Proof boundary

The `2x2x2` cube (complete: every condition at every site and every star), the `2x2x3` slab (single sites: `<= 4` records, all nearest-neighbour
conditions, all whole-class conditions; class units `{0,2}`, `{9,11}`, `{3,5}`, `{6,8}`, `{4}`, `{7}`, `{1}`, `{10}`: complete over every condition on
the other edges; the class tick in every order), the `4^3` torus in its ground twist sector (star of `v = 0`; declared even-corner families T0-T3
exact, T6 float64 with an exact declared sub-family; one nearest-neighbour condition), and the `6^3`, `8^3` tori for the closure count only; the
staggered sector at half filling; PR #7876 Model A. Menus are supports of the sea's conditional record law, which is the tick's law exactly on
eigen-set prefixes and the `tau = 0` law otherwise, and the two mixed-parity rows are labelled so. Not covered: other fillings or flux sectors,
interacting laws, the relaxation tick of PR #7895, units that are not unions of stars, single-site conditions with more than four records on the slab,
T4-T5 and the full T6 on the torus, any census on `6^3` or `8^3`, and any law whose records register anything but `Z_e`.

Where this note's runner reduces the source computation's complete censuses, it says so and quotes: the slab column pair over all `3^14` conditions,
the slab degree-4 star over all `3^16`, and the torus family T6 over `2097152` condition classes are each replaced by a declared sub-family that the
runner computes exactly and in full — the class tick's own conditions for the two slab units, and the `312`-class family for T6.

## Honest-auditor read

Audit this as a bounded statement about a supplied family of menus. What is proved is that the formation events of this designed law, at four declared
unit sizes on three objects, realise only subsets of one record frame; that on that family the global menu-independence clause is inconsistent by an
exact rank certificate; that the fibred clause holds identically and leaves an explicit non-Born grading standing; and that the abundance item of the
Born price is therefore unpaid by the tick. Do not audit it as a claim that the Born rule fails, that the Born form is derived or refuted anywhere,
that the axioms say anything about which menus form, or that any law outside the `Z_e` record alphabet has been examined.

## Imports and claim boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| cluster, superfast encoding, staggered sector, half filling | declared setting | stipulated here | physical eligibility open |
| the tick (Lueders formation, `exp(-i tau H_R)` between events) | declared dynamics | PR #7876 Model A, open | one tick among several |
| the formation units (site, star, pair, class) | declared units | PRs #7947, #7968, open | no unit is foreclosed |
| menu, grading, menu-independence, fibred clause, abundance | declared definitions | PRs #7919, #7931, #7950, open | the Born line's own terms |
| the continuum record alphabet `L_CONT` | named comparison | PR #7926, open | supplied by fiat there |

## Review record

The probe behind this note asked whether this tick meets the Born price on its own and the answer is no, so the title says that and no more. The exact
instruments are the ones PR #7950 used — rank certificates over `Q` — turned on the family this law actually realises, and the census that feeds them
is complete on the cube and declared where it is reduced. Three of the source computation's censuses are quoted rather than recomputed, and the note
marks each. It does not advance current-surface physical Born closure: the cluster, the tick, the units and the Born line's definitions are all
supplied, and no axiom content is derived here.

Independent audit remains required before the repository may assign any effective claim status.
