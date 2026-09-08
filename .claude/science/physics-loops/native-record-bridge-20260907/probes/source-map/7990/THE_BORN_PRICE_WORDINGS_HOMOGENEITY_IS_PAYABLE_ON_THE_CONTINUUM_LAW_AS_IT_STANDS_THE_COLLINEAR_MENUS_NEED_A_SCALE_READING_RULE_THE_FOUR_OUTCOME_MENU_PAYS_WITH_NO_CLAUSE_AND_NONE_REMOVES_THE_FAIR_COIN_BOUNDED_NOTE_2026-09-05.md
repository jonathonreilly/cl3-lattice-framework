---
claim_id: born_price_wordings_homogeneity_collinear_menus_four_outcome_fair_coin_2026_09_05
claim_type: bounded_theorem
claim_scope: "Exact rational one-site algebra under a Z^3 nearest-neighbour law on the continuum record alphabet {cP(n)} u {cI} of PR #7926, plus one labelled float64 recomputation of PR #7973's string-mode count. SUPPLIED, none of it read out of any axiom: the alphabet; the record-echo law L_CONT of PR #7926 under PR #7973's reading R1 (a cI record carries no Bloch direction); the modifications M1, M2, M3 declared here and the symmetric-mean reading in M2; the lattice-dipole class map, L_FIB and its tilt t = 2/3; a record-value class map and its tilt; PR #7950's definitions of menu, grading, menu-independence and the families, and its direction-measurability clause where used; the named elementary theorem that a bounded additive function on an interval is linear; PR #7973's L_HYB, relaxed vortex, declared flip patterns, M_0 and plane size. (T1) Complete over all 21^6 = 85766121 conditions of a declared 21-letter alphabet (230230 multisets), L_CONT realises exactly {I, binary, coin, balanced ternary}; the collinear ternary, the mixed coin ternary and the four-outcome collinear menu never occur, and L_CONT is scale-blind on every condition. The smallest covariant modifications that read the record scales on the collinear conditions are M1 (one record, collinear ternary at a = c), M2 (an antipodal pair, mixed coin at c = (c1+c2)/2) and M3 (an equal-direction pair, four-outcome menu); L_A = L_CONT + M1 + M2 differs from L_CONT on exactly 17496 + 43740 conditions and L_4 = L_A + M3 on exactly 29160 more. Both keep the echo lemma, the bulk I record on all 18^6 = 34012224 fully recorded conditions, covariance on 684024 checks with 0 mismatches, and PR #7926's abundance; the new menus sweep all grid scales at 1840/1840, 529/529 and 253/253. The lattice dipole's coordinate sum is the recorded-slot count mod 2, so a two-record menu reaches the fibre e_x only with an I-record pad. (T2) Without homogeneity, on the radius grid j/24 and all angle modes k <= 12: L_CONT's family has nullity 13, 3, 1, 2, 1 and alternating 2/1 thereafter, carrying the counting rogue and 11 free coin values; L_A's family has nullity 0 at every mode except k = 1, where the kernel is exactly the homogeneous Born vector h_1(c) = c, and pins u(c) = c without the ternary coin, under PR #7950's direction-measurability clause; L_4's family, per point on a ray with no ansatz, has 23 collinear and 132 four-outcome rows on 24 unknowns of rank 23 and nullity 1 with kernel W(c) = cW(1), so homogeneity is forced, bounded additivity extends it to real scales, and the 52-direction stage of rank 50 with kernel span{x, y} closes the Born form with no clause. (T3) The bulk fibre is rho = I/2 by an exact rank-3 certificate; for every state the +m members of any collinear-type menu total tr(rho P(m)), the binary's odds, so a collinear ternary at a bulk site registers a scale and not a sign; the bulk sign odds are 1/2, 1/2, re-registration costs 2^-N^2 unchanged, and a record-value map of tilt t biases the coin without fixing it since the antipode stays in the support and t < 1. PR #7973's flip-density-1/2 row is recomputed at 0 core modes in labelled float64. (T4) Homogeneity is satisfied by L_FIB, violated by the counting rogue, and insufficient without abundance on L_BIN; its status is a clause on L_CONT's family, a measurability-conditional theorem on L_A's, and an exact theorem on L_4's. No axiom is changed, no status is set, and no axiom-side Born forcing is claimed."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/born_price_wordings_homogeneity_collinear_four_outcome_fair_coin_check_2026_09_05.py
---

# The continuum alphabet pays the grading-side wording of the Born price with its own formation events and the menu-side wording only once the support rule reads record scales; the four-outcome collinear menu makes homogeneity a theorem; and no wording removes the bulk fair-coin sign, which the class map alone sets

**Date:** 2026-09-05 | **Type:** bounded_theorem | **Audit:** unset; independent audit remains a separate lane
**Status authority:** independent audit only; this note authors no audit verdict and changes no axiom, primitive, registry, queue, or policy.
**Primary runner:** [`scripts/born_price_wordings_homogeneity_collinear_four_outcome_fair_coin_check_2026_09_05.py`](../scripts/born_price_wordings_homogeneity_collinear_four_outcome_fair_coin_check_2026_09_05.py)
**Runner cache:** [`logs/runner-cache/born_price_wordings_homogeneity_collinear_four_outcome_fair_coin_check_2026_09_05.txt`](../logs/runner-cache/born_price_wordings_homogeneity_collinear_four_outcome_fair_coin_check_2026_09_05.txt)
**Open sibling branches, none on main:** PR #7919 (menu-independence and abundance as separate items of the price); PR #7926 (the continuum record alphabet, `L_CONT`, `L_FIB` and the lattice-dipole class map); PR #7931 (the fibred menu-independence clause); PR #7950 (the two wordings of the price, Theorems A and B, and the counting rogue); PR #7969 (the matter law's own ticks in one frame); PR #7973 (the winding phase and the fair-coin sign). All six are open pull requests.

## Result Up Front

PR #7950 leaves the price of the Born form in two wordings: **(A)** a fibred menu-independence clause plus abundance enlarged to carry the collinear and mixed coin menus, or
**(B)** the same clause plus abundance plus a homogeneity clause on the grading. Which one a formation event on the continuum alphabet can realise, and at what cost, is settled
below.

The answer separates them. **(B) is payable by `L_CONT` exactly as it stands**: over a complete census its supports are `{I}`, binaries, coins and balanced ternaries and nothing
else, which is the abundance (B) asks for, so the homogeneity clause is the whole remaining cost. **(A) is not payable by any scale-blind rule**, and `L_CONT` is scale-blind on all
`21^6` of its conditions. The smallest covariant repair reads the record scale exactly where `L_CONT` is degenerate and gives `L_A`; under it (A) is payable up to PR #7950's
direction-measurability clause. One step further, at arity four, the four-outcome collinear menu makes homogeneity a **theorem** with no clause at all.

What no wording touches is the sign. In the bulk fibre the state is `I/2`, and for every state the outcomes of a collinear-type menu sharing the direction `+m` have total odds
`tr(rho P(m))`, exactly the binary's odds. A collinear ternary at a bulk site registers a **scale**, not a sign, and the fair coin of PR #7973 survives both wordings.

## Machine Status And Trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "The census is complete over a declared finite alphabet and the certificates are exact rational eliminations over Q on declared grids, but the family, the law, its modifications, the class map and the tilt are all supplied, the mode certificates carry PR #7950's direction-measurability clause, and one labelled float64 row is a model construction."
trace_class: upstream_support
target_claim_id: born_form_scaled_projector_arity_three_threshold
target_blocker_text: "prove ternary scaled-projector sufficiency or find a rogue"
source_of_blocker_text: frontier_question
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Decide whether any covariant nearest-neighbour rule on this alphabet realises the four-outcome collinear menu without reading two equal-direction record scales, or settle the regularity-free question left open on L_A's family."
conditional_surface_status: "exact rational algebra conditional on the supplied alphabet, the supplied laws L_CONT, L_A, L_4 and L_HYB, the supplied class maps and tilt, the declared rational grids, and — for the mode certificates only — direction-measurability at each scale"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

Work at one site with `H = C^2`. For a unit vector `n` write `P(n) = (I + n dot sigma)/2` and take the scaled domain `S = {cP(n) : 0 < c <= 1} union {cI : 0 < c <= 1}`. A **menu**
is a finite family of members of `S` summing to `I`; a **grading** is a map `w: S -> [0,1]` depending on the effect and not on the menu it appears in, written `W(c, n) = w(cP(n)) =
c/2 + K(cn)` and `u(c) = w(cI) = c + utilde(c)`, the Born form being `K(v) = gamma dot v`, `utilde = 0`. A **formation event** is one site, one record, the support a function of
the six nearest-neighbour records, the record locking one member of the support. Every load-bearing computation is exact over `Q`; no seed is used; the one float64 block is
labelled in its own output lines.

## The Supplied Surface, Quoted

From `docs/MINIMAL_AXIOMS_2026-06-29.md` on main, the two clauses this note reads and never extends — Admissibility's support clause,

> The distribution is a probability measure on the local possibility domain; "available"/"admissible" denotes its support -- on finite menus, exactly the possibilities of nonzero
> probability.

and Record's one-possibility clause,

> When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent.

together with Admissibility's own variation clause, "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor
conditions." Nothing below is read out of either; both fix only what a menu and a formation event are.

From **PR #7926**, supplied whole: the continuum record alphabet; `L_CONT` — one record echoes as the binary of its own direction, three coplanar positively spanning records as
their ternary, two records as a coin, anything else `{I}` — the lattice-dipole class map `lambda(n)`, the sum of the recorded slot directions, and `L_FIB` with `rho` at `e_x` equal
to `(I + (2/3) sigma_x)/2`. From **PR #7973**: reading R1, `L_HYB`, the relaxed `24x24` vortex, the flip patterns and `M_0`. From **PR #7950**: menu, grading and menu-independence,
the families, the direction-measurability clause, and the two wordings, quoted verbatim,

> The price reads either **fibred clause plus abundance with collinear menus** or **fibred clause plus abundance plus a homogeneity clause**; the frame item is gone in both, and
> the count of supplied items does not grow in the first.

From **PR #7969**, supplied as context: on the matter law's own ticks every realised effect has scale 1 and the realised menus lie in one frame, so the abundance item is unpaid
there. M1, M2, M3 and the symmetric mean in M2 are supplied here and landed nowhere.

## T1 — What `L_CONT` Realises, Complete, And The Smallest Covariant Modification

**The census.** Declare 21 letters per slot: blank, `I`, `I/2`, and `cP(d)` for `c` in `{1, 1/2, 1/4}` and six directions `{m_1, m_2, m_3, -m_1, ±e_z}` with `m_1 = (1,0,0)`, `m_2 =
(-3/5, 4/5, 0)`, `m_3 = (-3/5, -4/5, 0)`. All three laws read the multiset of records, so the census runs over the **230230** multisets weighted by multiplicity and covers all
`21^6 = 85766121` conditions. By the number `kP` of direction-recorded neighbours:

| `kP` | `L_CONT` support | conditions |
|---|---|---|
| 0 | `{I}` | 729 |
| 1 | binary `{P(m), P(-m)}` | 26244 |
| 2 | coin `{aI, (1-a)I}`, else `{I}` | 284310 / 109350 |
| 3 | balanced ternary, else `{I}` | 87480 / 3061800 |
| 4, 5, 6 | `{I}` | 14171760 / 34012224 / 34012224 |

> **Proposition 1.** `L_CONT` realises exactly `{I, binary, coin, balanced ternary}`. The collinear ternary `{aP(n), (1-a)P(n), P(-n)}`, the mixed coin ternary `{cP(n), cP(-n),
> (1-c)I}` and the four-outcome collinear menu **never occur**, at any condition.

The structural reason is one line: **`L_CONT` is scale-blind.** On all `85766121` conditions the support is unchanged when every recorded scale is set to `1`. The only scalars it
reads are inner products of recorded directions — the coin's `a = (1 + m_1 dot m_2)/2` — and a scale-blind rule has no scalar to attach to a single direction, while each absent
menu needs exactly that.

**The modification.** Read the record scales on the collinear conditions, where `L_CONT` is degenerate.

| branch | condition | support |
|---|---|---|
| M1 | one record `cP(m)`, `c < 1` | `{cP(m), (1-c)P(m), P(-m)}`, the collinear ternary at `a = c` |
| M2 | antipodal `c_1 P(m), c_2 P(-m)` | `{cP(m), cP(-m), (1-c)I}` with `c = (c_1+c_2)/2`, the mixed coin |
| M3 (`L_4` only) | equal-direction `c_1 P(m), c_2 P(m)`, `c_1 + c_2 <= 1` | `{c_1 P(m), c_2 P(m), (1-c_1-c_2)P(m), P(-m)}` |

`L_A = L_CONT + M1 + M2`; `L_4 = L_A + M3`; every other branch is `L_CONT`'s. `L_A` realises exactly `{I, binary, coin, balanced ternary, collinear ternary, mixed coin}` and `L_4`
adds the four-outcome menu. `L_A` differs from `L_CONT` on exactly the one-record conditions with `c < 1` (**17496**) and the two-antipodal-record conditions (**43740**); `L_4`
differs from `L_A` on exactly the two-equal-direction conditions with `c_1 + c_2 <= 1` (**29160**). The new menus occur only where they must: under `L_A` the collinear ternary only
at `kP = 1` and the mixed coin only at `kP = 2`, and under `L_4` the four-outcome menu only at `kP = 2`.

**What is kept.** The echo lemma — every rank-one direction in every support is a recorded direction or its antipode — holds for all three laws with **0** failures; all `18^6 =
34012224` fully direction-recorded bulk sites are `I` records under all three; every realised support resolves `I_2` exactly; covariance holds on **684024** checks with **0**
mismatches for `L_A` and `L_4`. PR #7926's abundance is kept whole: every binary (**160/160**), every non-collinear balanced ternary of three declared planes (**756/756** at unit
and at `1/3` record scales), the coin branch at **77** distinct exact `a`. The new menus sweep the grid: the collinear ternary **1840/1840** over 23 scales `j/24` and 80
directions, the mixed coin **529/529** with **45** distinct `c`, the four-outcome menu **253/253**.

**A parity fact about the fibres.** The lattice dipole's coordinate sum equals the number of recorded slots mod 2, so without an `I`-record pad a two-record menu sits in an even
fibre and a one- or three-record menu in an odd one, and `e_x` is reachable unpadded only by the odd family — binary, collinear ternary, balanced ternary. With one `I` record in a
third slot, reading R1, every menu type reaches both `e_x` and the invariant fibre `0`; witnesses are `{+x: (1/3)P(m_2), +y: (1/2)P(-m_2), -y: I}` for the mixed coin, the same with
equal directions for the four-outcome menu, `{+x: (1/3)P(m_2)}` for the collinear ternary. In that collinear ternary two of the three outcomes share the direction and differ only
in scale, `1/4` and `3/4`: the record registers the sign of the axis and, on the echoed sign, a scale. Under `L_CONT` that scale is readable by Record and conditions no support
anywhere; under `L_A` it conditions the support on 61236 conditions.

## T2 — The Rank Certificates, With No Homogeneity Assumed Anywhere

Write `F_CONT`, `F_A` and `F_4` for the families the three laws realise, and `M_all` for PR #7950's arity-three family with the ternary coin, which no law here realises. The
unknowns are the values of a menu-independent grading; homogeneity is assumed in no row of any system below.

**Part 1, angle modes on the radius grid `j/24`, every mode `0 <= k <= 12`.** PR #7950's instrument, extended to all modes and to the four families, on the **48** perimeter-2 grid
triangles (its 44 with `s_1 < s_2` plus the 4 isosceles ones its `combinations` omitted). Triangle rows alone reproduce PR #7950's control nullities `3, 3, 2, 2, 2` at `k = 0, 1,
3, 5, 7`.

| family | k = 0 | k = 1 | k = 2 | k = 3 | k = 4 | ... | k = 12 |
|---|---|---|---|---|---|---|---|
| `F_CONT` | 13 | 3 | 1 | 2 | 1 | alternating 2/1 | 1 |
| `F_A` | 0 | **1** | 0 | 0 | 0 | 0 | 0 |
| `F_4` | 0 | **1** | 0 | 0 | 0 | 0 | 0 |
| `M_all` | 0 | **1** | 0 | 0 | 0 | 0 | 0 |

`F_CONT`'s nullity 13 at `k = 0` carries the counting rogue `h_0(c) = c - 2/3` on the interior with `h_0(1) = 0`, and **11** of the 13 are free coin values: on the family `L_CONT`
realises, the coin grading is constrained by nothing beyond `u(a) + u(1-a) = 1`.

> **Proposition 2.** On `F_A` the mode-`k` system has nullity **0** at every mode `k <= 12` except `k = 1`, where the kernel is exactly `h_1(c) = c`, the Born vector, homogeneous
> in the scale. The counting rogue is not in the `k = 0` kernel, and the radius `1/24` that PR #7950 reported uncovered is covered by the collinear row `h(1/24) + h(23/24) - h(1)`.
> `F_4` and `M_all` agree with `F_A` mode by mode, so the ternary coin adds nothing that the collinear and mixed coin menus have not already added.

Under PR #7950's clause — the angle-Fourier coefficients of `K(c n(phi))` exist at each scale, direction-measurability — `F_A` forces `W(c, n) = c(1/2 + gamma dot n)` almost
everywhere in direction at each scale and `u(c) = c`: Theorem B of PR #7950 on a family a law realises, **minus the ternary coin**. With `h_0(1) = 0` from the binary and `h_0(a) =
-h_0(1-a)` from the collinear ternary, the triangle rows with one side `1/2` make `phi(x) = h_0(x + 1/2)` additive with `phi(1/2) = 0`, hence zero. A regularity-free proof on `F_A`
is not obtained, as it was not in PR #7950.

**Part 2, `F_4` with no ansatz at all.** Per-point unknowns `W(c)` on one ray: **23** collinear rows and **132** four-outcome rows on 24 unknowns have rank **23**, nullity **1**,
kernel exactly `W(c) = c W(1)` — **homogeneity is forced on the grid**. The collinear rows alone, `F_A`'s whole ray content, leave nullity **12**, which is why `F_A` needs the mode
argument and its clause. For real scales the four-outcome menu, the collinear ternary and the binary give `W(an) + W(bn) = W((a+b)n)` for `a, b > 0` with `a + b <= 1`, and `W` has
range `[0,1]`; a bounded function additive on an interval is linear — a named elementary theorem, not recomputed — so `W(cn) = c W(n)` exactly, and the mixed coin gives `u(c) = c`
exactly.

**Part 3, the Theorem A stage.** PR #7950's untruncated circle certificate, recomputed: **52** grid directions, **5200** non-collinear balanced ternaries, per-direction unknowns,
rank **50**, nullity **2**, kernel exactly `span{x, y}`. With homogeneity from Part 2, the balanced ternaries alone give `f(n) = 1/2 + beta dot n` on the circle and PR #7950's
Lemma 2 glues the circles.

> **Proposition 3.** On `F_4` the Born form follows with no homogeneity assumption, no frame theorem and no regularity clause. On `F_A` it follows up to direction-measurability at
> each scale. On `F_CONT` it does not follow: the counting rogue survives.

The fibred version is unchanged: the fibre `e_x` contains all of `F_A` and `F_4` with `I`-padding, so each per-fibre grading meets the same certificates, and covariance restricts
`rho_{e_x} = (I + t sigma_x)/2` with `t` free. The tilt stays supplied.

## T3 — The Fair Coin Is Untouched By Either Wording

The class map reads slots, so every fully recorded condition has `lambda = (0,0,0)`; the stacked `R - 1` over the 24 proper cubic rotations has rank **3**, the invariant Bloch
space is `{0}`, and the bulk fibre carries `rho = I/2` under every support rule. In that fibre:

| condition | menu | odds |
|---|---|---|
| `{cP(m), five I}` under `L_A` | collinear ternary | `(c/2, (1-c)/2, 1/2)`; `+m` total `1/2`, `P(-m)` `1/2` |
| `{(1/4)P(m), (3/4)P(-m), four I}` under `L_A` | mixed coin | `(1/4, 1/4, 1/2)` |
| `{(1/4)P(m), (1/2)P(m), four I}` under `L_4` | four-outcome | `(1/8, 1/4, 1/8, 1/2)`; `+m` total `1/2` |
| six direction records | `{I}` | no direction, hence no sign, registered at all |

> **Sign lemma.** For every state `rho` and every menu of the new family, the total odds of the `+m` members equal `tr(rho P(m))`, the binary's odds — the `+m` members sum to
> `P(m)` as effects. Checked on 5 states across 7 scales for the collinear, four-outcome and mixed menus.

So the sign odds are a property of the fibre's state alone and no menu of `L_A` or `L_4` changes them: `1/2, 1/2` in the bulk, PR #7973's `23/30, 7/30` on the tilted circle
unchanged. **A collinear ternary at a bulk site registers a scale, not a sign.** One class tick therefore re-registers an `N x N` winding field unflipped with odds `2^-N^2 =
10^-173.4, 10^-308.3, 10^-693.6` at `N = 24, 32, 48`, identical to PR #7973. A record-value class map with a supplied tilt `t` gives the field's own sign odds `(1+t)/2` and the
antipode `(1-t)/2`; the antipode is in the support, so by Admissibility's support clause `t < 1` strictly and the flip density `(1-t)/2` is positive for every admissible tilt — the
sign is a biased coin, never definite, and at `t = 2/3` the unflipped path costs `(5/6)^N^2 = 10^-45.6, 10^-81.1, 10^-182.4`. In labelled float64 with PR #7973's own helper code,
the relaxed `24x24` vortex is an `L_HYB` fixed point at residual `9.9e-15` over 960 unpinned sites, and the declared flip pattern at density `1/2` leaves **0** core modes while no
flips, density `1/9` and about `1/6` keep 2 each; the input to that count, the per-site flip odds, is exactly `1/2` under `L_A` and `L_4` as under `L_CONT`.

## T4 — Homogeneity As A Clause, In The Axioms' Register

> **The clause.** Within a class, the odds the law assigns to a possibility scale with the possibility: where one admissible possibility is a fraction of another admissible
> possibility of the class, its odds are that fraction of the other's.

The register is possibility, odds, admissible and class, as in PR #7931's fibred wording. It compares two conditions of one class, so it is not the per-condition sentence PR #7919
found vacuous under Admissibility. Three facts fix its status.

- `L_CONT` with `L_FIB` **satisfies** it: in the fibre `e_x`, `w(cP(n))/c = w(P(n))` on all **126** `x`-`y`-plane ternaries and their binaries, every ternary summing to 1.
- The counting rogue **violates** it, `w(P/2)/(1/2) = 2/3` against `w(P) = 1/2`, while staying normalised on all 126: on `L_CONT`'s realised odds the clause is non-vacuous.
- Homogeneity alone **does not pay abundance**. On `L_BIN`, whose supports are binaries only, `w(cP(u)) = c(1 + u_z^3)/2` is homogeneous, menu-independent, normalised on every
  binary and not Born (`64/125` against `4/5`); on the matter law of PR #7969 every realised scale is 1, so the clause is vacuous while the supports lie in one frame. Wording (B)
  needs abundance as its own item, and `L_CONT` pays it with its own events.

> **Status by family.** `F_CONT` — homogeneity is a **clause**. `F_A` — a **theorem under direction-measurability**. `F_4` — a **theorem with no clause**. Wording (B) supplies as a
> clause exactly what the four-outcome menu supplies as a support.

## Corollary — The Two Wordings, Priced Against Actual Formation Events

**Wording (B), the fibred clause plus abundance plus homogeneity, is payable by `L_CONT` unmodified.** Its formation events — binaries at `kP = 1`, balanced ternaries at `kP = 3` —
are exactly the abundance (B) asks for, its own events, needing no support rule that is not already there; with the homogeneity clause the Born form follows with no regularity and
no frame theorem. The price is a supplied clause on the grading that the realised menus do not force: on `F_CONT` the counting rogue is menu-independent, normalised and not Born.

**Wording (A), the fibred clause plus abundance with the collinear menus, is payable only after the scale-reading modification.** No scale-blind rule offers those menus at any
condition, and `L_CONT` is scale-blind everywhere. `L_A` is the smallest covariant repair: it reads the record scale on the one-record and antipodal-pair conditions and changes
nothing else, keeping the echo lemma, the bulk `I` record, covariance and PR #7926's abundance. Under `L_A` the Born form follows **up to direction-measurability at each scale**,
with `u(c) = c` obtained without the ternary coin; PR #7950's regularity-free residue stays open.

**The four-outcome collinear menu pays with no clause at all.** As a formation event it needs `L_4`, which reads two equal-direction record scales and has arity four, outside the
arity-three surface; in exchange homogeneity becomes a theorem on the grid and, through bounded additivity, for real scales, and the 52-direction stage then gives the Born form
outright.

**Neither wording removes the fair-coin sign.** It is set by the class map's fibre, which no support rule touches: the bulk fibre is `rho = I/2` by an exact rank-3 certificate, and
the sign lemma makes every collinear-type menu carry the binary's sign odds for every state. A collinear ternary at a bulk site registers a scale, not a sign, so a menu family
cannot buy the sign back; a directed record-value class map biases it, and the antipode stays in the support, so the bias is never a certainty.

The honest price of the Born form, in one sentence: **the Born form costs a fibred menu-independence clause with a directed class map and a supplied tilt, plus either a homogeneity
clause on the grading (payable by `L_CONT`'s own formation events, exactly) or a support rule that reads record scales (payable by `L_A`'s events up to direction-measurability, by
`L_4`'s events at arity four exactly), and in every version the bulk sign of a registered direction is a coin set by the class map, which no support rule changes.**

## The Six Disagreements With The Expectation, Stated Plainly

1. A collinear ternary at a bulk site does **not** give the bulk a director with a definite sign: it registers a scale, and its sign odds equal the binary's for every state.
2. Wording (B) needs **no modification** of `L_CONT`: (B)'s formation events are already realised, (A)'s are not, and (A) requires `L_A`.
3. The mixed coin ternary shares a fibre with the binaries and balanced ternaries only with an `I`-record pad — a parity obstruction absent from PRs #7926 and #7950.
4. `F_A` pins `u(c) = c` **without** the ternary coin `M_all` used; and on `L_CONT`'s family the coin grading is essentially free, 11 free grid values.
5. Under `L_A` two antipodal unit records give the binary, not `{I}` as under `L_CONT` — a side effect of the mean reading in M2, flagged and not load-bearing.
6. PR #7973's string-mode count, 0 modes at flip density `1/2`, is recomputed here rather than only quoted; its input is exact and unchanged by either modification.

## Reading, Not Theorem

There are two ways to say what quantum odds cost, and they sound like the same sentence. One says: let the rule be told that half of an alternative gets half the odds. The other
says: let the alternatives on offer include the ones where an alternative is split in two along the same direction. The rule this alphabet actually gives you already offers
everything the first sentence needs and nothing the second needs — it reads which way its neighbours point and never how much of them there is, so it can never put a scale on a
single direction. Teach it to read that scale on the one kind of neighbourhood where it currently has nothing to say, and the second sentence comes true too; let it read two such
neighbours and the scaling rule stops being something you say and becomes something that follows. None of this reaches the sign. Which way the direction a site records points is
settled by the coarse label the site sits under, and in the bulk that label is blind to direction, so the answer is a coin toss. Splitting an alternative finer tells you more about
how much, and nothing about which way.

## Executable claim block

```text
alphabet: 21 letters per slot -- blank, I, I/2, cP(d) for c in {1, 1/2, 1/4} and 6 exact rational unit directions; 230230 multisets, complete over 21^6 = 85766121 conditions, not reduced
L_CONT realised menus: {I, binary, coin, balanced ternary}; collinear ternary, mixed coin ternary, four-outcome menu never occur; scale-blind on 85766121 of 85766121
L_A = L_CONT + M1 + M2: differs on 17496 + 43740 conditions; L_4 = L_A + M3: differs on 29160 more
kept: echo lemma 0 failures; bulk I on 18^6 = 34012224; covariance 684024 checks 0 mismatches; binaries 160/160; ternaries 756/756 at unit and 756/756 at 1/3; 77 exact coin values
new sweeps: collinear 1840/1840; mixed coin 529/529 with 45 distinct c; four-outcome 253/253; dipole parity = recorded-slot count mod 2, e_x unpadded only for odd arity
mode nullities, grid j/24, 48 triangles, k <= 12: F_CONT 13 3 1 2 1 ...; F_A = F_4 = M_all 0 1 0 0 ... with kernel h_1(c) = c
ray certificate: 23 collinear + 132 four-outcome rows, 24 unknowns, rank 23, nullity 1, kernel W(c) = cW(1); collinear alone nullity 12
Theorem A stage: 52 directions, 5200 balanced ternaries, rank 50, nullity 2, kernel span{x, y}; homogeneity satisfied by L_FIB on 126 ternaries, violated by the counting rogue, insufficient alone on L_BIN (64/125 against 4/5)
fair coin: invariant fibre rank 3, rho = I/2; sign lemma on 5 states x 7 scales; bulk odds 1/2, 1/2; 2^-N^2 = 10^-173.4, 10^-308.3, 10^-693.6; tilt gives (1+t)/2 and (1-t)/2 > 0, so t < 1 strictly, and 10^-45.6, 10^-81.1, 10^-182.4 at t = 2/3
labelled float64: relaxed 24x24 vortex residual 9.9e-15 over 960 sites; flip density 1/2 leaves 0 core modes, none/1-9/~1-6 keep 2
arithmetic: exact rational (fractions.Fraction) on every load-bearing check; no seed anywhere; one labelled float64 block; runner_result_required: zero failed checks
```

## Interfaces

**PR #7919.** Its three-item price is what the Corollary re-prices; its finding that the per-condition sentence is vacuous under Admissibility is why the homogeneity clause here
compares two conditions of one class. **PR #7926.** `L_CONT`, `L_FIB`, the class map and the abundance construction are taken whole; the census states completely what that law
offers, and `L_A` and `L_4` keep every property it was built for. **PR #7931.** Its fibred clause is untouched and supplies the register in which the homogeneity clause is written.
**PR #7950.** Its two wordings are the object priced here, its Theorems A and B are used on families a law realises, its mode tables are extended to every mode `k <= 12` and to the
new families, and its uncovered radius `1/24` is covered on `F_A`. **PR #7969.** Its one-frame result shows homogeneity vacuous where every scale is 1, so abundance is a separate
item. **PR #7973.** Its R1, `L_HYB`, flip patterns and fair-coin result are supplied; the sign lemma extends its bulk binary statement to every menu of the new families.

## Proof boundary

Proved, on the declared families and grids: the complete census and Proposition 1; scale blindness; the exact difference sets of `L_A` and `L_4`; the echo lemma, the bulk `I`
record, the resolution of every support and covariance for both modified laws; abundance kept and the three new grid sweeps; the dipole parity fact and the padded fibre witnesses;
the mode nullities of the four families and Proposition 2; the ray certificate and Proposition 3's `F_4` reading up to the named additivity theorem; the 52-direction stage; the
invariant-fibre rank, the bulk odds of each new menu, the sign lemma and the strict tilt bound; and the homogeneity clause on `L_FIB`, its violation by the counting rogue and its
insufficiency on `L_BIN`.

Boundaries, exactly: one `M_2(C)` site under a `Z^3` nearest-neighbour law; the declared 21-letter alphabet (6 directions x 3 scales, `I`, `I/2`, blank) for the complete census,
run whole and not reduced to a sub-census; the 80 stereographic directions; three declared planes giving 378 ternaries; the radius grid `j/24`; the 52 Pythagorean circle directions
giving 5200 ternaries; modes `k <= 12`; `L_A` and `L_4` with the symmetric-mean reading in M2 and reading R1; the lattice-dipole class map and `L_FIB` at `t = 2/3`; the `24x24`
open plane, `M_0 = 0.7` and PR #7973's declared flip patterns for the one float64 block, labelled as such in its own output lines.

Not covered: any law other than `L_CONT`, `L_A`, `L_4` and `L_HYB`; a regularity-free Born proof on `F_A`; arities above four; polynomial or Fourier content above mode 12 on the
mode certificates, the per-point ray and 52-direction certificates having no such bound; any class map other than the lattice dipole and the record-value map named; the infinite
lattice; many-body content. Nothing here is derived from the axioms: the alphabet, the laws, their modifications, the class maps, the tilt, the grading definitions and both clauses
are supplied, and no axiom-side Born forcing is claimed.

## Honest Auditor Read

Audit this as a bounded theorem about supplied laws and supplied menu families. Established: a complete census of what one declared law offers; that it offers wording (B)'s
abundance and cannot offer wording (A)'s menus at all; that a named smallest modification offers them while keeping every property the law was built for; exact certificates fixing
homogeneity's status on each family; and that the bulk sign odds are `1/2` under all of them. Do not audit it as a claim that the Born rule is derived, that homogeneity is proved
from the axioms, that `L_CONT`, `L_A` or `L_4` is the framework's law, or that the class map or the tilt is established beyond what is supplied.

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| continuum alphabet, `L_CONT`, `L_FIB`, lattice-dipole class map | declared law and map | PR #7926, open, not on main | one law and one map, not a classification |
| reading R1, `L_HYB`, flip patterns, `M_0`, plane size | declared reading and model construction | PR #7973, open, not on main | model constructions, not landed fields |
| M1, M2, M3 and the symmetric mean in M2 | declared modifications | stated here; landed nowhere | smallest covariant repair, argued not classified |
| menu, grading, menu-independence, the families, the two wordings | declared definitions | PR #7950, open, not on main | the object being priced |
| direction-measurability at each scale; bounded additive on an interval is linear | regularity clause where used; named elementary theorem | PR #7950; classical, quoted | not discharged; used once, not recomputed |
| homogeneity clause; the tilt `t` of any directed class map | grading clause when assumed; supplied parameter | stated here in PR #7931's register; PRs #7926 and #7973 | not supplied by `L_CONT`'s menus; bounded below 1 here |
| observations, fits, target probabilities | none | not used | not applicable |

## Review Record

This note prices two wordings of the Born price against actual formation events on a continuum record alphabet and separates them: one is payable by `L_CONT`'s own events
with a clause, the other only after the support rule is taught to read record scales, and a fourth outcome at arity four turns the clause into a theorem. It also reports, against
the expectation, that the new menus register scale and never sign, so the fair coin of PR #7973 survives every wording. It does not advance current-surface physical Born closure:
the alphabet, the laws, the modifications, the class map and the tilt are all supplied.

Independent audit remains required before the repository may assign any effective claim status.
