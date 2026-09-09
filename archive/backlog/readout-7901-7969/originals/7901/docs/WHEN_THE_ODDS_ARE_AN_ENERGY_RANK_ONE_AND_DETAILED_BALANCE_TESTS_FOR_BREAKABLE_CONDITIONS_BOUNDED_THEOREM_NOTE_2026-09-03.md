---
claim_id: when_the_odds_are_an_energy_rank_one_detailed_balance_tests
claim_type: bounded_theorem
claim_scope: "On the coarse torus Z_L^3 at L = 8 with nearest-neighbour adjacency, 512 sites and coordination 6, carrying groups of n <= 3 records -- the dimer and the bent trimer {(0,0,0), (1,0,0), (1,1,0)} -- and on the classical record-pattern chains of PR #7899, under FOUR STIPULATED TABLES OF LOG-ODDS declared here in full and derived from nothing. A PROPOSAL is (which record shifts, one of the six unit directions d); the target is t = source + d; a target carrying a record makes the tick null; otherwise the shift is registered with odds (1/n) p_prop(d) min(1, e^{-w(c, D)}). D = dB = B(new) - B(old) = A(old) - A(new) is the configuration change, with A(S) the adjacent record pairs and B(S) = (n-1) - A(S), exact for n <= 3; writing A(others) for the bond the two records that do not shift already carry, A(old) = A(others) + m_s and A(new) = A(others) + m_t, so D = m_s - m_t exactly. The NEIGHBOURHOOD CONDITION c has four declared coordinates: m_t, records other than the mover adjacent to the target; m_s, records adjacent to the mover's source before the shift; s = +1 for d = +x, -1 for d = -x, 0 otherwise; and a = (x+y+z) mod 2 of the mover's source site, the declared two-sublattice ACTIVITY. THE FOUR TABLES, with g0 = 1, mu = 1/2, nu = 1/4 and g, h, kappa swept, all rational: A, separable, w = beta(c) D with beta(c) = g0 (1 + mu m_t)(1 + nu a) and a uniform proposal -- rank one by construction, the control; B, exactly PR #7899's BR(g, h, 1), w = g D with the field in the PROPOSAL, p_prop(d) = e^{h[d = +x]}/(5 + e^{h}); C, non-separable with the crowding switch on the TARGET, w = g D + kappa D^2 1[m_t >= 1] + h s, uniform proposal so the field sits in the odds; C', the same family with the switch on the MOVER's own neighbourhood, w = g D + kappa D^2 1[m_s >= 2] + h s, declared in response to a computed degeneracy of C on the bent trimer and not fitted to a target. The matrix under test is M_rel(c, D) = max(0, w(c, D)) - max(0, w(c, 0)), the extra log-odds of separating at the same neighbourhood; the raw -ln of the odds carries the additive ln p_prop, which makes it rank >= 2 for every table with no energy content, so the D = 0 column is subtracted throughout. (T1) [exact over Q] THE RANK-ONE TEST. Over the complete enumeration of the torus -- the dimer's 18 occurring (m_t, s, a, D) cells over 12240 unblocked proposals and the 3-record group's 36 cells over 4672620 proposals from all 130305 {0,x,y} representatives, with 9 conditions (m_s, s) for C' -- M_rel has EXACT RANK ONE over Q for table A on both groups at h = 0 and h = 1 (sigma_2/sigma_1 <= 1.302410e-16) with the exact temperature ladder T(c) = 1, 4/5, 2/3, 8/15, 1/2, 2/5, and for table B on both groups at both h (<= 4.602077e-17) with the same beta = g at all 18 conditions, so a single T = 1/g; table C is rank 1 on the dimer but EXACT RANK 2 on 3-record groups at h = 0 (sigma_2/sigma_1 = 3.411710e-02, rank-one residual 3.409726e-02) and rank 4 at h = 1 (1.426295e-01); table C' is EXACT RANK 2 (5.018675e-02 at kappa = 1/2, 1.304845e-01 at kappa = 1) and rank 4 at h = 1 (2.224582e-01). In all 9 rank-one cases the factorisation in the gauge E(D = +1) = 1 gives E(D) = max(0, D), a ONE-SIDED BARRIER and not the configuration energy. TWO TRAPS are measured: a dimer cannot run this test, since D in {-1, 0, +1} makes D^2 = |D| and table C comes out exactly rank one there (0.000000e+00) with a plausible T = 1, 2/3; and with ln p_prop left in even table C gives 4.032337e-02. (T2) [exact] KOLMOGOROV'S CYCLE CRITERION on four chains: all 56454 distinct 4-cycles of the 1022-state even-translation dimer chain, all 1524 of the 511-state relative chain, all 504 winding cycles of length L = 8, and a declared finite subgraph of 1620 trimer 4-cycles on absolute configurations. Table A fails by exactly nu = 1/4 on the dimer and trimer chains, its winding cycles clean, and its stationary law misses pi ~ e^{-g B} by 1.199957e-01; table B at h = 0 passes on all four chains to machine zero and is exactly Gibbs (1.5e-14); table B at h = 1 is still rank one and still exactly Gibbs (2.4e-14) yet fails by exactly 4h on the dimer chain and L h on the winding cycles -- a DRIVEN steady state with a Gibbs internal coordinate; table C at h = 0 passes every cycle and is exactly Gibbs (1.5e-14) while its odds matrix is rank 2, the symmetric kappa D^2 barrier cancelling in every ratio; table C' fails by exactly 4 kappa, independently of g. THE LUMPING TRAP: at h = 1 the translation-reduced relative chain and the declared trimer subgraph both PASS to 1e-16 while the unlumped chain fails by 4h, because lumping discards the parity label the witness cycle turns on. (T3) [exact] ARRHENIUS / VAN 'T HOFF on the bent trimer's 18 proposals, splitting 4 null, 2 at D = 0, 8 at D = +1 and 4 at D = +2: table B carries the common slope a(D)/D = g on both break channels at g = 1, 2, 4; table C' has a(1) = g on the end records (m_s = 1) and a(2) = 2g + 4 kappa on the centre record (m_s = 2), so a(2)/2 - a(1) = 2 kappa exactly at every coupling, a gap that cannot be absorbed into g, and the trimer's lifetime becomes 18/(8 e^{-g} + 4 e^{-2g - 4 kappa}) = 5.967579958344 against PR #7899's 5.165916817967 at g = 1, kappa = 1/2. The exact relation between the two discriminators is CYCLE DEFECT = 4 kappa = 2 x VAN 'T HOFF GAP. A NULL RESULT is recorded: table C keyed to the target is Arrhenius on the bent trimer at every kappa, because all 12 of its breaking proposals land on a site with no occupied neighbour (m_t = 0), so its rank-2 signature lives in the re-binding moves alone -- which is why C' was declared. (T4) [exact] CONSISTENCY: table B reproduces PR #7899's closed forms to 2.22e-16 relative for the dimer lifetimes 2 e^{g}(5 + e^{h})/(9 + e^{h}) and e^{g}(5 + e^{h})/(4 + e^{h}), to 1.94e-16 for the intact fraction 6/(6 + 505 e^{-g}) at every h, and to 1.78e-15 for the trimer's 18/(8 e^{-g} + 4 e^{-2g}), with the 1/n record-choice factor and the sign convention D = B(new) - B(old) both as declared. This note declares four tables of odds and computes with them; nothing is derived from any axiom, no axiom is amended, no status is set, no registry entry is created, and no claim is made about which of these tables, if any, the framework's own law resembles."
upstream_dependencies: []
runner: scripts/when_the_odds_are_an_energy_rank_one_detailed_balance_check_2026_09_03.py
---

# When the odds are an energy: rank-one and detailed-balance tests for breakable conditions

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/when_the_odds_are_an_energy_rank_one_detailed_balance_check_2026_09_03.py`](../scripts/when_the_odds_are_an_energy_rank_one_detailed_balance_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/when_the_odds_are_an_energy_rank_one_detailed_balance_check_2026_09_03.txt`](../logs/runner-cache/when_the_odds_are_an_energy_rank_one_detailed_balance_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

`A_HIERARCHY_OF_NEIGHBOURHOOD_CONDITIONS_GLUED_BREAKABLE_AND_FREE_RECORD_GROUPS_UNDER_SHIFTING_TICKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7899) answered its owner's question affirmatively at the **breakable** level: the
cost **is** the odds, and what a suppression of `e^{-g}` per broken adjacency buys is a lifetime, `(6/5) e^{g}` for the dimer and `18/(8 e^{-g} + 4 e^{-2g})` for the bent trimer. This note takes the next step and asks what
more a law has to satisfy before the word **energy** is earned. The answer, on the tables declared below, is that **two** conditions must hold and **neither implies the other**: the odds must factorise into a part reading
only the neighbourhood and a part reading only the change, and every closed loop of changes must cost the same forwards as backwards. Both are exactly testable on a record history, and rules that pass one and fail the other
are easy to write down.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-object theorems -- the ranks over Q of every odds matrix by Fraction row reduction, the derived energy E(D) = max(0, D) and the exact temperature ladders, the complete cell census over all 130305 3-record translation-class representatives, the complete 4-cycle censuses of the 1022-state and 511-state dimer chains and of the 504 winding cycles, and the exact channel activations a(1) = g and a(2) = 2g + 4 kappa with their gap 2 kappa -- together with deterministic double-precision evaluations of exactly specified quantities at the thresholds printed in their tags. There is no sampling, no seed and no random number anywhere in the runner."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Route to its owner the one question this note raises and does not decide: whether the framework's own law-level odds, read at whatever object plays the part of a neighbourhood condition, factorise in the rank-one sense and close around cycles -- and, under the Record axiom's permanence, whether the same two tests are to be read on which values FORM together given recorded neighbours rather than on which groups come apart across a tick."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the four statements below, exactly the runner's check groups `A`-`D`: `T1` (`A`) the rank-one test; `T2` (`B`) Kolmogorov's cycle criterion; `T3` (`C`) the Arrhenius / van 't Hoff census;
`T4` (`D`) the reproduction of PR #7899's closed forms. Every group is **exact** -- integer or `Fraction` arithmetic, or a closed form checked against a complete enumeration at a printed threshold. Every chain is a
classical record-pattern chain; the only floating point enters the singular values, the cycle products, the stationary solves and the closed-form comparisons, each tagged with its threshold. There is **no sampling, no seed
and no random number anywhere in this runner**, and no line is a witness.

## Imports and authority

Imported scientific authority: none load-bearing. The Metropolis acceptance rule, Kolmogorov's cycle criterion for reversibility, the singular value decomposition, the Arrhenius and van 't Hoff readings of an activation, and
translation-class reduction are standard methodology; every object is redeclared here and the runner recomputes every statement, including the figures it compares against another lane. No observational value, no fitted
number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight:
`A_HIERARCHY_OF_NEIGHBOURHOOD_CONDITIONS_GLUED_BREAKABLE_AND_FREE_RECORD_GROUPS_UNDER_SHIFTING_TICKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7899 -- the breakable level, the chains reused here, and the two closed forms
`T4` reproduces), `SUPPORT_CONDITIONS_CONFINE_GROUPS_OF_SHIFTING_RECORDS_ENERGY_COSTS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7891 -- the cage and the rigid condition),
`SHIFTING_POSITION_RECORDS_EXACT_DIFFUSION_LAW_AND_THE_UNIFORM_ATTRACTOR_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7889 -- the stipulated shifting tick and the axiom cost that note names and hands to its owner),
`THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7893 -- a support condition as an emergent instance), and
`MINIMAL_AXIOMS_2026-06-29.md`, from which the axiom text in "Setting" is quoted verbatim. This note cites no grade of any of these and consumes no ledger row.

## Setting

The framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations
about each site." "No site is privileged." The lattice is physical. **Qubit / Site Possibility**: "Each site has a domain of local possibilities."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the
possibilities is determined by, and varies with, the nearest-neighbor conditions." Reading note (3), interpretive and non-governing, quoted verbatim and in full:

> The distribution is a probability measure on the local possibility domain; "available"/"admissible" denotes its support -- on finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may have zero singleton measure; Record locks a supported realization.

That sentence fixes one piece of vocabulary used below. A **support condition** is a **zero of the law-level odds** at a site given its neighbourhood: a configuration the odds give `0` is not admissible, so no record ever
locks it. It is a property of the **supplied law**, not an extra axiom and not a new primitive. Nothing in this note is a support condition: every table here is a **suppression**, finite at every argument.

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; **records are permanent**." "Only records are readable."

The owner's question, quoted on 2026-09-03, which PR #7899 answered at the level of the cost and this note takes one step further:

> "couldn't the cost just be the odds of separating neighborhoods? Low under most conditions but raised under some?"

and the two computations the panel ranked first and second in reply -- the **rank-one collapse** of the log-odds matrix, and **Kolmogorov's cycle criterion** on the tick graph -- which are exactly `T1` and `T2` below. The
panel's type correction stands and is carried, not dismissed: the framework's Admissibility odds are over *which value a forming record locks*, and the tables here are over *whether a multi-site pattern changes across a
tick*. These are **supplier tables**, and the note claims nothing about which of them, if any, the framework's law resembles.

**The axiom cost of the tick, named.** The Record axiom makes records **permanent**. Everything below that speaks of a record *shifting* is inside a **stipulated tick model**, declared as such, of exactly the kind PR #7889
declared and whose wording cost that note's corollary item 2 and its interfaces name and hand to its owner: at the physical sites a shift is a value change, so a shifting-record reading needs either a weakened
value-permanence or records read at the coarse cells. This note takes no position on that call and supplies no formation clause. A record **registers** a value at a site; it does not report one the site already had.

## The stipulated tables, declared in full

Four tables, all declared here, none derived. A lane proposing different ones inherits the obligations of `T1`-`T4` and none of these choices.

A **proposal** is (which record shifts, one of the six unit directions `d`); the target is `t = source + d`; a target carrying a record makes the tick **null**; otherwise the shift is **registered** with odds
`(1/n) p_prop(d) Acc(c, D)`, `Acc(c, D) = min(1, e^{-w(c, D)})`. The **configuration change** is `D = dB = B(new) - B(old) = A(old) - A(new)`, adjacencies broken minus made. The **neighbourhood condition** `c` has four
declared coordinates: `m_t`, the records other than the mover adjacent to the **target**; `m_s`, the records adjacent to the mover's **source** before the shift; `s = +1` for `d = +x`, `-1` for `d = -x`, `0` otherwise; and
`a = (x+y+z) mod 2` of the mover's source site, the declared two-sublattice **activity**. Constants `g0 = 1`, `mu = 1/2`, `nu = 1/4`; `g`, `h`, `kappa` swept. All four are **rational**, so every odds matrix below has an
**exact rank over Q**.

| table | `w(c, D)` | proposal | what it is for |
|---|---|---|---|
| **A** separable | `beta(c) D`, `beta(c) = g0 (1 + mu m_t)(1 + nu a)` | uniform `1/6` | rank one **by construction** -- the control |
| **B** breakable | `g D` | tilted, `p_prop(d) = e^{h[d = +x]}/(5 + e^{h})` | exactly PR #7899's `BR(g, h, 1)`; the field is in the **proposal** |
| **C** target crowding | `g D + kappa D^2 1[m_t >= 1] + h s` | uniform `1/6` | deliberately non-separable; the field is in the **odds** |
| **C'** mover crowding | `g D + kappa D^2 1[m_s >= 2] + h s` | uniform `1/6` | the same family, switch moved to the mover's own neighbourhood |

`C'` was **declared in response to a computed degeneracy** of `C`, not fitted to a target: out of a bent trimer every breaking proposal has `m_t = 0`, so a target-keyed switch never fires on a break and `C` reproduces `B`
there (`T3`). The **matrix under test** is `M_rel(c, D) = max(0, w(c, D)) - max(0, w(c, 0))`, the extra log-odds of separating at the same neighbourhood. The raw `-ln` of the odds carries the additive `ln p_prop`, which
makes it rank `>= 2` for **every** table with no energy content; the `D = 0` column is subtracted throughout, and `T1` reports what leaving it in would have done.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is precisely `P0`-`P4`.

`P0` (declared here): the torus, the two groups, the four tables, the four coordinates of `c`, the gauge `M_rel`. `P1` (`A`): the rank-one test. `P2` (`B`): the cycle criterion. `P3` (`C`): the Arrhenius census. `P4` (`D`):
the reproduction of PR #7899.

## Definitions

A **group of records** is a finite set of occupied sites of the torus `Z_L^3` at `L = 8`, one record each; `A(S)` counts its adjacent pairs and `B(S) = (n-1) - A(S)`, exact for `n <= 3`. The two groups are the **dimer** and
the **bent trimer** `{(0,0,0), (1,0,0), (1,1,0)}`. Writing `A(others)` for the adjacency the two records that do not shift already carry, `A(old) = A(others) + m_s` and `A(new) = A(others) + m_t`, so **`D = m_s - m_t`
exactly**; this is the direct computation of `D` and not a shortcut.

The **chains**, all classical record-pattern chains, the largest object built anywhere being `1022 x 1022`: (1) the dimer **relative** chain, `511` states `r = v - u`, a valid reduction only for a fully translation-covariant
table -- table `A` reads the declared sublattice, so it is not one for `A`; (2) the dimer **full** chain reduced by **even** translations, state `(p, r)` with `p` the parity of record 1's site, `2 x 511 = 1022` classes, even
translations being an exact symmetry of every declared table, so every 4-cycle of the absolute chain is an even translate of one of these; (3) the **winding** cycles of length `L = 8` in chain (2), one record shifting `+x`
around the torus; (4) the **trimer** chain on **absolute** configurations, no lumping, in the declared finite subgraph of 4-cycles based at the bent trimer and at each of its one-tick successors.

The **cycle defect** of a chain is `max` over its cycles of `|ln(product of forward odds / product of backward odds)|`; `0` is detailed balance. The **activation** of a break channel is `a(D) = -ln` of the mean acceptance in
that channel; **Arrhenius** holds exactly when `a(D)/D` is the same for every channel, and the **van 't Hoff gap** is `a(2)/2 - a(1)`.

## Theorem 1 -- the rank-one test: which tables have an energy, and which energy

**Conclusion.** `[exact over Q]` Over the complete enumeration of the `L = 8` torus -- the dimer's **18** occurring `(m_t, s, a, D)` cells over **12240** unblocked proposals, and the 3-record group's **36** cells over
**4672620** proposals from all **130305** `{0,x,y}` representatives, with **9** conditions `(m_s, s)` for `C'` -- the gauge-fixed matrix `M_rel` has **exact rank one over Q** for **table A** on both groups at `h = 0` and
`h = 1` alike (`sigma_2/sigma_1 <= 1.302410e-16`), with the exact temperature ladder `T(c) = 1/beta(c) = 1, 4/5, 2/3, 8/15, 1/2, 2/5`; and for **table B** on both groups at both `h` (`<= 4.602077e-17`), with the **same**
`beta = g` at all `18` neighbourhood conditions, hence a single `T = 1/g`. A field in the **proposal** never enters the cost matrix at all. **Table C** is rank one on the dimer but **exact rank 2** on 3-record groups at
`h = 0` (`sigma_2/sigma_1 = 3.411710e-02`, best rank-one relative residual `3.409726e-02`) and rank `4` at `h = 1` (`1.426295e-01`); **table C'** is **exact rank 2** (`5.018675e-02` at `kappa = 1/2`, `1.304845e-01` at
`kappa = 1`) and rank `4` at `h = 1` (`2.224582e-01`). **Which energy.** In all `9` rank-one cases the factorisation in the gauge `E(D = +1) = 1` gives

> **`E(D) = max(0, D)`** -- `E(-2) = E(-1) = E(0) = 0`, `E(+1) = 1`, `E(+2) = 2`.

**Two traps, both measured.** (i) A **dimer cannot run this test**: `D` lies in `{-1, 0, +1}`, so `D^2 = |D|` and every even function of `D` is absorbed into the one-sided gauge -- table `C`, non-separable by construction,
comes out **exactly rank one** on the dimer (`sigma_2/sigma_1 = 0.000000e+00`) and reports a perfectly plausible ladder `T = 1, 2/3`. (ii) With `ln p_prop` left in, even table `C` reports `4.032337e-02`, so the `D = 0`
column must be subtracted before the singular values mean anything.

**Proof.** The occurring cells are collected by complete enumeration over the torus, every representative, parity, mover and direction, with blocked targets dropped; `D` is computed as `m_s - m_t`, which is `A(old) - A(new)`
because the two records that do not shift keep whatever bond they had. Every entry of `M_rel` is a `Fraction`, so the rank is obtained by exact row reduction over `Q` and the singular values are a float cross-check, not the
statement. The factorisation is read off the `D = +1` column with the stated gauge and then compared entrywise against `max(0, D)`.

**Reading, not theorem.** This is the first half of the answer. If the odds of a group coming apart split into a part that depends only on the surroundings and a part that depends only on the change, then the second part is
an energy and the first is one over a temperature, and both can be read straight off a record history. Two things are worth saying about the energy that comes out. It is **not** the configuration energy: it is that energy's
positive part, a one-sided barrier, because a rule that accepts every downhill change outright carries no information about the downhill half of the move set -- any `E` agreeing uphill fits equally well. And the test needs
`D` to take at least three values, so it needs groups of at least **three** records; on two records it cannot fail, and it will hand back a plausible temperature for a rule that has none.

## Theorem 2 -- the cycle criterion: which tables are reversible, and where the defect lives

**Conclusion.** `[exact]` On all **56454** distinct 4-cycles of the `1022`-state even-translation dimer chain, all **1524** of the `511`-state relative chain, all **504** winding cycles of length `L = 8`, and the declared
finite subgraph of **1620** trimer 4-cycles on absolute configurations. **Table A fails by exactly `nu = 1/4`** on the dimer chain (`2.500000000000001e-01`) and on the trimer chain (`2.500000000000001e-01`), its winding
cycles being clean (`2.2e-16`), and its stationary law -- which exists, `|pi P - pi| = 1.0e-17` -- misses `pi ~ e^{-g B}` by `1.199957e-01`. **Table B at `h = 0` passes on all four chains** to machine zero and its stationary
law is exactly `pi ~ e^{-g B}` (`1.5e-14`). **Table B at `h = 1`** is still rank one (`T1`) and still exactly Gibbs (`2.4e-14`), and **still fails by exactly `4h`** on the dimer chain and by `L h` on the winding cycles.
**Table C at `h = 0`, `kappa = 1/2`, passes every cycle** on all four chains and is exactly Gibbs (`1.5e-14`) while its odds matrix is **rank 2**. **Table C' fails by exactly `4 kappa`** -- `0`, `1`, `2`, `4` at
`kappa = 0, 1/4, 1/2, 1` -- and the defect is **independent of the coupling**, `2.000000000000` at `g = 2` as at `g = 1`. **The lumping trap:** at `h = 1` the translation-reduced relative chain **passes** (`2.2e-16`) and so
does the declared trimer subgraph (`3.3e-16`), while the unlumped chain fails by `4.000000` and the winding cycles by `8.000000`.

**Proof.** Each chain is built edge by edge from the declared table, with the `1/n` record-choice factor and the proposal odds in place, so every row is stochastic and the diagonal absorbs null ticks and unregistered
proposals. The 4-cycle censuses are complete enumerations of the closed walks on four distinct states, deduplicated over the eight rotations and reflections of a 4-cycle. The winding cycles track the mover's source parity,
so table `A` is read with its declared activity rather than with the activity discarded. The stationary law is a linear solve with the normalisation replacing one equation, refined three times so the small entries are solved
rather than recovered by cancellation, and its residual is printed.

**Reading, not theorem.** Rank one does **not** give a Gibbs state. Table `A` factorises to machine zero, hands back a clean temperature ladder, and has no Gibbs law at all -- and the reason is as simple as it is general: on
a bipartite lattice a move and its reverse sit on **opposite** sublattices, so a condition keyed to which sublattice the mover started on takes a different value going and coming, and the inverse temperature that suppresses
a move is not the one that suppresses its undoing, however cleanly the odds factorise. Detailed balance does **not** give rank one either: a symmetric `kappa D^2` term is a barrier, it costs the same both ways, it cancels
in every ratio and changes the rate and not the resting law -- so table `C` at zero field sits in exactly the Gibbs law it would have had without the barrier while its odds refuse to factorise. And a Gibbs-looking resting
law is **not sufficient**: with a field in the proposal, table `B` keeps its rank one and keeps its Boltzmann law and is nevertheless not reversible at all, because a current runs round the torus while the internal
coordinate sits in its Boltzmann distribution. Finally, the test has to be run on the chain one actually has: lumping by translation closes the witness cycle, and on a torus part of the defect lives only on the cycles that
wind.

## Theorem 3 -- what a record history would show: Arrhenius, van 't Hoff, and a null result

**Conclusion.** `[exact]` Out of the bent trimer the `18` proposals split **4 null**, **2 at `D = 0`**, **8 at `D = +1`** (an end record leaves) and **4 at `D = +2`** (the centre record leaves, both bonds go). **Table B**
carries the **common slope** `a(D)/D = g` on both break channels at `g = 1, 2, 4`. **Table C'** does not: every `D = +1` break is an **end** record (`m_s = 1`, not crowded) so `a(1) = g`, and every `D = +2` break is the
**centre** record (`m_s = 2`, crowded) so `a(2) = 2g + 4 kappa`, giving the **van 't Hoff gap**

> **`a(2)/2 - a(1) = 2 kappa` exactly**, `1.000000000000` at `g = 1, 2, 4` for `kappa = 1/2` and `2.000000000000` for `kappa = 1`,

the **same** gap at every coupling, so it cannot be absorbed into a redefinition of `g`. The trimer's lifetime becomes `18/(8 e^{-g} + 4 e^{-2g - 4 kappa})`, matched by the enumerated proposals to `0.0e+00`:
`5.967579958344` against PR #7899's `5.165916817967` at `g = 1`, `16.474505674194` against `15.571677528219` at `g = 2` and `122.693773845084` against `121.731046628774` at `g = 4`. **The exact relation between the two
discriminators:** for the same declared `kappa` the **cycle defect is `4 kappa`** and the **van 't Hoff gap is `2 kappa`**, so `defect = 2 x gap` -- `2.000000000000` against `2 x 1.000000000000` at `kappa = 1/2` and
`4.000000000000` against `2 x 2.000000000000` at `kappa = 1`. **The null result.** Table `C`, keyed to the **target's** crowding, is Arrhenius on the bent trimer at **every** `kappa` (`a(1) = a(2)/2 = 1.000000000000` at
`kappa = 0, 1/2, 1` alike), because all `12` of its breaking proposals land on a site with no occupied neighbour -- `m_t = 0` in every one of them -- so the crowding switch never fires on a break, and `C`'s rank-2 signature
lives in the **re-binding** moves alone.

**Proof.** The channel census enumerates the bent trimer's `18` proposals, records `(m_s, m_t)` for each breaking one, and reports the activation as `-ln` of the mean acceptance in the channel; the `(m_s, m_t)` sets are
compared against `{(1, 0)}` for `D = +1` and `{(2, 0)}` for `D = +2`, which is the exact reason for `a(1) = g` and `a(2) = 2g + 4 kappa`. The lifetime is the reciprocal of the summed break odds over the same enumerated
proposals and is compared with the closed form; the summation direction is the one in which the small weights are added rather than differenced.

**Reading, not theorem.** The two tests are not just formal: each has a signature a record history would carry. A law whose odds do not factorise shows up as **break channels with different slopes** -- here the group's end
records and its centre record part at activations that differ by a fixed amount, no matter how the coupling is tuned. A law that is not reversible shows up as a **loop that costs more one way round than the other**. On these
tables the two are the same number up to a factor of two, which is a convenience and not a theorem. The null result is the practical warning: a non-separable law can be completely undetectable in the lifetimes of the very
group whose separation it governs, and still be rank 2 in the odds. Which of the two tests sees it depends on which coordinate the condition is keyed to, so run both.

## Theorem 4 -- consistency with the parent

**Conclusion.** `[exact]` With the `1/n` record-choice factor and the sign convention `D = B(new) - B(old) = A(old) - A(new)` both as declared, **table B reproduces PR #7899's closed forms**: the dimer lifetimes
`2 e^{g}(5 + e^{h})/(9 + e^{h})` aligned and `e^{g}(5 + e^{h})/(4 + e^{h})` transverse over six `(g, h)` cells to `2.22e-16` **relative** -- both `(6/5) e^{g}` at `h = 0` -- the intact fraction `6/(6 + 505 e^{-g})` to
`1.94e-16` **at every `h`** (`|pi P - pi| <= 6.0e-17`), and the bent trimer's `18/(8 e^{-g} + 4 e^{-2g})` to `1.78e-15`, namely `5.165916817967`, `15.571677528219` and `121.731046628774` ticks at `g = 1, 2, 4`.

**Proof.** The dimer figures come from the same `511`-state relative chain used in `T2`, the lifetime as the reciprocal of the summed break odds out of the intact vector and the intact fraction from the refined stationary
solve; the trimer figure comes from the same `18`-proposal census used in `T3`. Both are compared against the closed forms as written in PR #7899.

**Reading, not theorem.** This theorem carries no new content and is here for one reason: the three tables that are **not** PR #7899's are tested against a reproduction of PR #7899's own numbers on the same code path, so a
difference reported in `T1`-`T3` is a difference between the declared tables and not between two implementations. Two conventions are load-bearing and were both fixed before any table was compared -- the `1/n` factor for
choosing which record shifts, and the sign of `D` on the trimer.

## Corollary -- when the odds are an energy

Within the setting declared above, on the `L = 8` torus, for groups of `n <= 3` records and for the four stipulated tables alone:

1. **The two tests are logically independent, and each fails without the other.** Rank one does not give a Gibbs state (table `A`: rank one to machine zero, a clean temperature ladder, cycle defect exactly `nu`, and a
   stationary law `12 %` off Boltzmann). Detailed balance does not give rank one (table `C` at `h = 0`: every cycle product `1`, exactly Gibbs, odds matrix rank `2`). And a Gibbs stationary law is not sufficient for either
   reading (table `B` with a field: rank one, exactly Gibbs, and not reversible). **Only both together license the sentence "these odds are an energy and a temperature".**
2. **Where the odds are an energy, the energy is a one-sided barrier.** What comes out of Metropolis-type odds is `E(D) = max(0, D)`, the positive part of the configuration change, not the configuration energy itself; the
   odds carry nothing about the downhill half of the move set.
3. **A bipartite lattice puts a parity defect into any sublattice-dependent activity.** A move and its reverse start on opposite sublattices, so a law whose odds read which sublattice a record sits on is never in detailed
   balance, however perfectly separable it is -- and the defect is exactly the activity coefficient `nu`.
4. **A field is a driven steady state, not a hotter one.** With the tilt in the proposal the internal coordinate stays exactly Gibbs and the intact fraction is unmoved at every `h`, while the cycle products fail by exactly
   `4h` on a 4-cycle and `L h` around the torus. A resting law that looks thermal is not evidence of reversibility.
5. **The measurable discriminator on a record history is a pair.** Bin every registered change by `(c, D)`, subtract the `D = 0` column and take the singular values -- `sigma_2/sigma_1 = 0` is the energy; then take every
   4-cycle of the **unlumped** history and every cycle that winds -- `0` is detailed balance. A third check comes free, the van 't Hoff gap between break channels, which here is exactly half the cycle defect.
6. **Two traps for anyone repeating this.** A dimer cannot run the rank-one test, because `D^2 = |D|` when `D` has three values and a non-separable table comes out rank one with a plausible temperature. A
   translation-reduced chain cannot run the cycle test, because the witness cycle is closed in the reduced chain and open in the real one. Both were walked into and measured here.

## Reading, not theorem -- the whole thing in plain words

When can the odds of a group coming apart be read as an energy divided by a temperature? Two things must both hold, and neither implies the other: the odds must split into a part that depends only on the surroundings and a
part that depends only on the change, and going round any closed loop of changes must cost the same forwards as backwards. Rules that pass the first and fail the second, or the reverse, are easy to write down, and so is a
rule that is perfectly thermal in its resting statistics yet not reversible at all because a steady push runs through it. So "the cost is the odds" is right, but "the odds are an energy" is an extra property that a law may
or may not have, and there is an exact test for it on record histories.

## Interfaces named for other lanes, not settled here

- **The framework's actual law.** Every table here is supplied. Whether the framework's own odds, read at whatever object plays the part of a neighbourhood condition, factorise in the rank-one sense and close around cycles
  is a question about the law and is asked, not answered, here.
- **The form-together reading under permanence.** Records are permanent. Read that way, the two tests apply to which values are admissible to **form** at a site given its recorded neighbours, with `D` reading the change in
  the neighbourhood pattern; the matrices and the cycle products are the same objects and the wording changes. Which reading the framework intends is the owner's call, the same call PR #7889's corollary item 2 hands over.
- **Amplitude ticks.** Every chain here is classical. PR #7889's `M2` kernel -- a pre-record amplitude running for a time `tau`, the odds being its weights conditioned on the admissible set -- is a different object, and what
  either test says about it is untouched here.
- **Larger groups.** The censuses stop at `n <= 3`, where `B = (n-1) - A` is exact and `D` takes five values. At `n >= 4` a group can carry more than `n-1` adjacencies, `D` takes more values, and both tests get sharper; none
  of that is computed.
- **Non-Metropolis acceptance rules.** `Acc = min(1, e^{-w})` is a declared convention and it is what makes the derived energy one-sided. A smooth acceptance rule -- Glauber, or any strictly positive function of `w` --
  would return an `E` determined on both halves of the move set, and what the two tests then measure is not computed here.

## Remaining live routes

1. Whether the exact factor of two between the cycle defect and the van 't Hoff gap survives beyond a single switched `D^2` term, or is an accident of this family.
2. Whether a positive stationary law that passes the cycle test but fails the rank-one test admits a **local** energy at all -- the Hammersley-Clifford question, untouched here.

## Executable claim block

The canonical machine-bound restatement of the four theorem conclusions.

```text
setting: the coarse torus Z_L^3 at L = 8, 512 sites, coordination 6, bipartite; groups of n <= 3 records, the dimer and the bent trimer {(0,0,0),(1,0,0),(1,1,0)}; A(S) adjacent record pairs, B(S) = (n-1) - A(S) exact for n <= 3. Axioms quoted from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading note (3) quoted in full
tables: STIPULATED, derived from nothing. Proposal = (which record shifts, one of 6 unit directions); null tick on a blocked target; otherwise registered with odds (1/n) p_prop(d) min(1, e^{-w(c,D)}). D = B(new) - B(old) = A(old) - A(new) = m_s - m_t. c = (m_t, m_s, s, a) with a = (x+y+z) mod 2 of the mover's SOURCE. g0 = 1, mu = 1/2, nu = 1/4. A: w = g0 (1 + mu m_t)(1 + nu a) D, uniform proposal. B: w = g D, p_prop(d) = e^{h[d=+x]}/(5+e^{h}) -- PR #7899's BR(g,h,1). C: w = g D + kappa D^2 1[m_t >= 1] + h s, uniform. C': w = g D + kappa D^2 1[m_s >= 2] + h s, uniform. Gauge M_rel(c,D) = max(0,w(c,D)) - max(0,w(c,0)). Records are PERMANENT; every shifting statement is inside a stipulated tick model whose axiom cost PR #7889 names
T1_rank_one [exact over Q]: cells by complete enumeration -- dimer 18 (m_t,s,a,D) over 12240 unblocked proposals, 3-record 36 over 4672620 from all 130305 {0,x,y} representatives, 9 conditions (m_s,s) for C'. A rank 1 on both groups at h = 0 and 1 (sigma_2/sigma_1 <= 1.302410e-16), ladder T(c) = 1, 4/5, 2/3, 8/15, 1/2, 2/5; B rank 1 on both groups at both h (<= 4.602077e-17), beta = g at all 18 conditions, T = 1/g; C rank 2 on 3-record at h = 0 (3.411710e-02, residual 3.409726e-02) and rank 4 at h = 1 (1.426295e-01); C' rank 2 (5.018675e-02 at kappa = 1/2, 1.304845e-01 at kappa = 1), rank 4 at h = 1 (2.224582e-01). In all 9 rank-one cases E(D) = max(0, D) EXACTLY in the gauge E(+1) = 1. TRAPS: C is rank one on the dimer (0.000000e+00, T = 1, 2/3) since D^2 = |D| there; with ln p_prop left in C gives 4.032337e-02
T2_cycles [exact]: 56454 4-cycles of the 1022-state even-translation dimer chain, 1524 of the 511-state relative chain, 504 winding cycles of length 8, 1620 declared trimer 4-cycles on absolute configurations. A fails by exactly nu = 1/4 on the dimer and trimer chains, winding clean, stationary law off Gibbs by 1.199957e-01 (|pi P - pi| = 1.0e-17); B at h = 0 passes all four to machine zero, exactly Gibbs 1.5e-14; B at h = 1 rank one and exactly Gibbs 2.4e-14 yet fails by exactly 4h on the dimer chain and L h on the winding cycles; C at h = 0, kappa = 1/2 passes all four and is exactly Gibbs 1.5e-14 while rank 2; C' fails by exactly 4 kappa (0, 1, 2, 4 at kappa = 0, 1/4, 1/2, 1) and g-independently (2.000000000000 at g = 2). LUMPING TRAP: at h = 1 the relative chain (2.2e-16) and the trimer subgraph (3.3e-16) PASS while the unlumped chain fails by 4.000000 and winding by 8.000000
T3_arrhenius [exact]: the bent trimer's 18 proposals split 4 null, 2 at D = 0, 8 at D = +1, 4 at D = +2. B: common slope a(D)/D = g at g = 1, 2, 4. C': a(1) = g on end records (m_s = 1), a(2) = 2g + 4 kappa on the centre record (m_s = 2), van 't Hoff gap a(2)/2 - a(1) = 2 kappa EXACTLY at every g; lifetime 18/(8 e^{-g} + 4 e^{-2g - 4 kappa}) matched to 0.0e+00, 5.967579958344 vs 5.165916817967 at g = 1 kappa = 1/2, 16.474505674194 vs 15.571677528219, 122.693773845084 vs 121.731046628774. RELATION: cycle defect 4 kappa = 2 x van 't Hoff gap 2 kappa. NULL RESULT: C is Arrhenius on the bent trimer at every kappa (a(1) = a(2)/2 = 1.000000000000) because all 12 breaking proposals have m_t = 0
T4_consistency [exact]: table B reproduces PR #7899 -- dimer lifetimes 2 e^{g}(5+e^{h})/(9+e^{h}) and e^{g}(5+e^{h})/(4+e^{h}) to 2.22e-16 relative over six (g,h) cells, both (6/5) e^{g} at h = 0; intact fraction 6/(6 + 505 e^{-g}) to 1.94e-16 at EVERY h (|pi P - pi| <= 6.0e-17); trimer 18/(8 e^{-g} + 4 e^{-2g}) to 1.78e-15, i.e. 5.165916817967, 15.571677528219, 121.731046628774 at g = 1, 2, 4. The 1/n record-choice factor and the sign D = B(new) - B(old) are declared conventions fixed before any comparison
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=21 FAIL=0
```

## Proof boundary

Every statement above is proved on **declared finite objects**: groups of `n <= 3` records on the `L = 8` torus, the `1022`-state and `511`-state dimer chains, the `504` winding cycles, and a declared finite subgraph of the
trimer chain. Nothing is claimed for larger groups, for the thermodynamic limit, for other lattices, or for any table other than the four in "The stipulated tables".

**The four tables are stipulated in full and derived from nothing.** Reading note (3) makes support a property of the **supplied odds**, so stipulating a table here is stipulating a law, not amending an axiom; reading note
(2) is explicit that the axioms supply no formation site, probability or rate, and this note supplies none either. Table `C'` was declared in response to a computed degeneracy of `C` and is not fitted to any target. A lane
proposing different tables inherits the obligations of `T1`-`T4` and none of these choices. **Records are permanent**; every sentence in which a record *shifts* is inside a stipulated tick model declared as such, and the
axiom cost of that stipulation is the one PR #7889 names and hands to its owner.

**Every chain is a classical record-pattern chain.** PR #7889's amplitude kernel is not used, so nothing here bears on any amplitude tick.

**Complete enumeration where stated, bounded and declared where not.** Complete: the occurring `(c, D)` cells over all `130305` 3-record translation-class representatives and all `511` dimer relative vectors; all `56454`
4-cycles of the `1022`-state chain; all `1524` of the `511`-state chain; all `504` winding cycles; the bent trimer's `18` proposals. **Bounded and declared:** the trimer's `1620` 4-cycles are those based at the bent trimer
and at each of its one-tick successors, a finite declared subgraph and not the whole trimer chain -- so every trimer row is a **falsification** where it reports a defect and a **bounded** result where it reports none.

**`[exact]` versus `[numerical]`.** Exact, with no floating point in the statement: every odds matrix, its rank over `Q` by `Fraction` row reduction, the derived `E(D) = max(0, D)`, every `beta(c)` and `T(c)`, the identity
`D = m_s - m_t`, the channel activations `a(1) = g` and `a(2) = 2g + 4 kappa` and their gap `2 kappa`, and the cycle and proposal counts. Numerical: the singular values (a rank-one matrix returns `sigma_2/sigma_1` at or
below `1.31e-16`), the cycle products (every violation lands on its exact rational -- `0.25`, `1`, `2`, `4`, `8` -- to fifteen digits), the stationary vectors and the closed-form comparisons, each at the threshold printed in
its line. **There is no sampling, no seed and no random number anywhere in the runner**, and no line is a witness. The largest object built anywhere is `1022 x 1022`.

**Nothing is derived from the axioms.** No axiom is used, amended or invoked; no status is set; no registry entry or ledger row is touched. The panel's type correction is carried: the framework's Admissibility odds are over
which value a forming record locks, and these tables are over whether a multi-site pattern changes across a tick. **These are supplier tables, and the note claims nothing about which of them, if any, the framework's law
resembles.** No claim is made that any table is unreachable, and none of the results below rules out any construction: a rule that fails one test on these tables is a rule with a named, measured defect, not a route that is
closed.

**Not computed:** groups of `n >= 4`; the complete trimer cycle census; cycles of length other than `4` and `L`; acceptance rules other than `min(1, e^{-w})`; anything about continuum limits, gaps, or the link sector; and
whether a positive stationary law here admits a local energy.

## Review record

An honest auditor should come away with four declared tables of odds and two exact tests run on them, not a claim about what the framework's own law does; four exact finite-object theorems, three complete 4-cycle censuses,
one complete cell census over `130305` representatives, and exact ranks over `Q` throughout, with the numerical lines deterministic, unsampled and threshold-tagged; no Monte Carlo anywhere; the stipulation declared as
stipulated in the front matter, the setting, its own section, the claim block and the proof boundary alike; the axiom cost of the shifting tick named rather than absorbed; two methodological traps reported because this lane
walked into both of them, and a null result reported because it is the reason table `C'` exists; and a corollary written as an answer to its owner's question, with the question it cannot settle -- what the framework's own
odds do under these two tests -- handed back rather than settled.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions" and "The stipulated tables", no hypothesis is adopted, and the "Imports and authority" pointers are plain text carrying
no grade and no weight. Hard landing conditions are a fresh runner and cache pair at `PASS=21 FAIL=0`, runtime under the declared `150` seconds, a current zero-dependency citation-manifest entry, and passing pipeline,
strict-lint and changed-evidence gates; audit remains a separate lane.
