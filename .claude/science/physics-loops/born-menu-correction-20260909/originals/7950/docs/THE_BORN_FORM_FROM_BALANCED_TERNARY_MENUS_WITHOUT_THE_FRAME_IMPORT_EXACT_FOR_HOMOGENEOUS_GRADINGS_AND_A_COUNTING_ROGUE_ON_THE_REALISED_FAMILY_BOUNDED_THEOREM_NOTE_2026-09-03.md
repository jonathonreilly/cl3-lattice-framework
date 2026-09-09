---
claim_id: born_form_from_balanced_ternaries_without_frame_import_2026_09_03
claim_type: bounded_theorem
claim_scope: "Exact rational one-site algebra on the 2026-08-09 scaled qubit domain. (i) A balanced ternary of scaled projectors resolves the identity exactly when the weights sum to 2 and the weighted directions sum to zero, so its side vectors close a triangle of perimeter 2 and every weight is automatically below 1; verified on 5200 exact rational balanced triples over a declared 52-point rational grid, with weights strictly between 1/21 and 696/697. (ii) Theorem A: for a grading homogeneous in the scale, the non-collinear balanced ternaries alone force the Born form on the whole qubit domain, with no continuity, measurability, boundedness beyond the range, countable additivity, ancilla lift or dimension-three frame theorem; the certificates are an untruncated 52-value circle system of rank 50 whose kernel is exactly the restriction of span{x, y}, a trigonometric system on modes 0 to 8 of rank 15 whose kernel is exactly cos t and sin t, and a degree-six sphere system of 49 unknowns and rank 46 whose kernel is exactly span{x, y, z}. (iii) On the menu family the continuum law of PR 7926 realises, the counting grading 1/3 on interior effects, 1/2 on projectors and 1/2 on coins is menu-independent, normalised on all 5271 realised menus and not Born, as is a one-parameter family containing it; both are killed by the collinear ternary and the mixed coin ternary, which lie in the parent note's low-arity family and are not realised by that law. (iv) Theorem B: on the parent note's family, without homogeneity, the coin menus force w(cI) = c by an exact rank-23 certificate, the mixed coin menus make the residual odd, and the angle-mode system on a 24-point radius grid with 44 perimeter-2 triangles has nullity 0 at modes 0, 3, 5 and 7 and nullity 1 at mode 1 with the vector h(c) = c, so with direction-measurability at each scale the Born form holds almost everywhere in direction. A regularity-free proof of homogeneity is not obtained. No axiom is changed, no axiom-side Born forcing is claimed, and the dimension-three frame theorem is neither used nor recomputed."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/born_form_from_balanced_ternaries_without_frame_import_check_2026_09_03.py
---

# The Born Form On The Qubit Domain From Balanced Ternary Menus Without The Three-Dimensional Frame Import: Exact For Homogeneous Gradings, For General Gradings Up To Direction-Measurability, And A Counting Rogue On The Realised Family

**Date:** 2026-09-03 | **Type:** bounded_theorem | **Audit:** unset; independent audit remains a separate lane
**Status authority:** independent audit only; this note authors no audit verdict and changes no axiom, primitive, registry, queue, or policy.
**Primary runner:** [`scripts/born_form_from_balanced_ternaries_without_frame_import_check_2026_09_03.py`](../scripts/born_form_from_balanced_ternaries_without_frame_import_check_2026_09_03.py)
**Runner cache:** [`logs/runner-cache/born_form_from_balanced_ternaries_without_frame_import_check_2026_09_03.txt`](../logs/runner-cache/born_form_from_balanced_ternaries_without_frame_import_check_2026_09_03.txt)
**Parent, on main:** [`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
**Open sibling branches, none on main:** `A_CONTINUUM_RECORD_ALPHABET_LIFTS_THE_ABUNDANCE_NO_GO_A_FIBRED_BORN_THEOREM_AND_A_FACTOR_OF_TWO_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-09-04.md` (PR #7926, the continuum alphabet and the fibred Born theorem);
`A_FIBRED_MENU_INDEPENDENCE_CLAUSE_NON_VACUOUS_ON_THE_CONTINUUM_LAW_DISCRIMINATING_ON_THE_CUBE_BOUNDED_THEOREM_NOTE_2026-09-04.md` (PR #7931, the fibred clause);
`MENU_INDEPENDENCE_IS_INDEPENDENT_OF_THE_AXIOMS_AND_INSUFFICIENT_WITH_THEM_THE_BORN_FORM_NEEDS_MENU_ABUNDANCE_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7919, menu-independence and abundance). All three are open pull requests.

## Result Up Front

The parent note obtains the Born form on the scaled qubit domain by lifting the two- and three-member menus to
orthonormal bases of `C^3` and applying the dimension-three frame theorem; that import is the third item of the
readout price PR #7919 states. This note asks whether the balanced ternary menus force the Born form on their own.
They do, and the price for saying so is exact and small. For a grading homogeneous in the scale, the non-collinear
balanced ternaries alone force the Born form with no regularity at all — no continuity, no measurability, no
countable additivity — by a graph-plane lemma on each great circle and a gluing lemma on the sphere. On the
parent's full low-arity family, without homogeneity, the same conclusion holds up to one clause: the grading is
measurable in the direction at each scale. Between those readings sits a plain correction — homogeneity is not
supplied by the menus the continuum law of PR #7926 realises, and on that family an explicit counting grading is
menu-independent, normalised and not Born.

## Machine Status And Trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "The dictionary, the two lemmas and Theorem A are exact for all functions with no regularity hypothesis, and the rank certificates are exact rational eliminations over Q on declared grids. Theorem B carries a direction-measurability clause that is not discharged here, and the whole result concerns a supplied menu family and a supplied grading, not the axioms."
trace_class: upstream_support
target_claim_id: born_form_scaled_projector_arity_three_threshold
target_blocker_text: "prove ternary scaled-projector sufficiency or find a rogue"
source_of_blocker_text: frontier_question
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Settle whether a bounded, direction-non-measurable, non-Born grading exists on the parent's low-arity family, or find a scale-free amplification giving homogeneity without regularity."
conditional_surface_status: "exact rational algebra conditional on the supplied menu family, the supplied grading clause, the declared rational grids, and — for Theorem B only — direction-measurability at each scale"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

Work at one site, with `H = C^2`. For a unit vector `n` write `P(n) = (I + n dot sigma)/2`, and take the parent's
scaled domain `S = {cP(n) : 0 < c <= 1, |n| = 1} union {cI : 0 < c <= 1}`. A **menu** is a finite family of
nonzero members of `S` summing to `I`; a **grading** is a map `w: S -> [0,1]` whose value depends on the effect
and not on a menu containing it. The map `cP(n) |-> v = cn` identifies the scaled rank-one effects with the
punctured unit ball; write `W(v) = w(|v| P(v/|v|))`, `u(c) = w(cI)`.

Two menu families are in play. `M_all` is the parent's family: every two- or three-member menu of `S`. `M_CONT` is
the family the continuum law `L_CONT` of PR #7926 realises as supports — every binary rank-one menu, every
non-collinear rank-one ternary, every coin. `M_CONT` is a proper subfamily: the collinear ternary `{aP(n),
(1-a)P(n), P(-n)}`, the mixed coin ternary `{cP(n), cP(-n), (1-c)I}` and the ternary coin `{aI, bI, (1-a-b)I}` are
in `M_all` and are not realised by that law, whose ternary branch reads three coplanar positively spanning
records. Every computation below is exact over `Q` with `fractions.Fraction`; no floating point enters any
load-bearing check and no seed is used. The runner prints one `PASS` line per verification; six recorded arguments
print with `ARG:` and are not counted.

## The Supplied Surface, Quoted

The parent states the family this note works over as its second conditional input,

> **Low-arity eligibility.** Every two- or three-member menu is normalized: `sum_j w(E_j)=1`.

and obtains the Born form from it by the lift whose two load-bearing sentences are

> `F` is a nonnegative normalized frame function on `C^3` with no continuity, measurability, differentiability, or
> countable additivity premise added.

> By the named dimension-three frame theorem, there is a unique positive operator `R on C^3` with `Tr(R)=1` and
> `F(u)=<u|R|u>`.

Those two sentences are exactly what drops. The runner reads both from the parent on disk and from this note, and
uses neither.

## T1 — The Dictionary: A Balanced Ternary Is A Perimeter-2 Triangle

Taking traces and traceless parts of `sum_i c_i P(n_i) = I` gives the exact equivalence

> `sum_i c_i P(n_i) = I` **iff** `sum_i c_i = 2` and `sum_i c_i n_i = 0`,

so the `v_i = c_i n_i` are the side vectors of a closed triangle of perimeter 2, and the balanced weights of three
non-collinear coplanar directions are unique, `c_i/2` being the barycentric coordinates of the origin in the
triangle `n_1 n_2 n_3`. Two consequences are automatic rather than extra hypotheses. First, `c_1 = |c_2 n_2 + c_3
n_3| <= c_2 + c_3 = 2 - c_1`, so `c_1 <= 1`, with equality only when `n_2 = n_3`; the runner checks the strict
inequality through `|c_2 n_2 + c_3 n_3|^2 < (c_2 + c_3)^2` iff `n_2 dot n_3 < 1`, on all **1326** pairs of the
declared grid. Second, a **projector never enters a non-collinear balanced ternary**: a side of length 1 forces
the other two to sum to 1, hence to be parallel. On the declared grid of **52** rational unit directions from the
Pythagorean parametrisation with `m <= 5` there are **5200** non-collinear balanced ternaries; each satisfies `sum
c_i = 2` and `sum c_i n_i = 0` exactly, every weight lies strictly between **1/21** and **696/697**, and none is a
projector.

## T2 — Theorem A: Homogeneous Gradings, Exactly, With No Regularity

Assume homogeneity in the scale, `w(cP(n)) = c f(n)`, and put `F = f - 1/2`. Normalisation on a non-collinear
balanced ternary reads `sum_i c_i F(n_i) = 0`.

> **Lemma 1 (great circle).** Let `C` be a great circle and `F: C -> R` **any** function with `sum_i c_i F(n_i) =
> 0` on every balanced non-collinear triple in `C`. Then `F(n) = beta_C dot n` on all of `C`, for one in-plane
> `beta_C`. **Lemma 2 (gluing).** If `F: S^2 -> R` is linear on every great circle, then `F(n) = beta dot n` for
> one `beta` in `R^3`.

*Proof.* For a balanced triple the lifted vectors `(n_i, F(n_i))` in `R^3` satisfy `sum_i c_i (n_i, F(n_i)) = 0`
with every `c_i` nonzero, so they are dependent; no two members are antipodal, so `n_1, n_2` are independent and
the three lifted vectors span the plane through the first two, the graph of a linear form. Parametrising `C` by
`t`, a triple is balanced exactly when all three gaps are below `pi`, so a fixed pair `(0, delta)` completes to
balanced triples throughout `(pi, pi + delta)`; chaining pairs from that arc carries the one `beta_0` over the
circle bar two points, and a restart from `(delta/2, 3delta/2)` agrees at two independent points and covers those.
For Lemma 2, with `a_i = F(e_i)`, `m = (x, y, 0)/r` and `r = (x^2 + y^2)^{1/2}` nonzero, the equator gives `F(m) =
(a_1 x + a_2 y)/r` and the circle through `e_3` and `m` gives `F(n) = r F(m) + z a_3 = beta dot n`. ∎

> **Theorem A.** Let `w: S -> [0,1]` be menu-independent, homogeneous on the rank-one effects, and normalised on
> every non-collinear balanced ternary. Then there is a unique density matrix `rho` with `w(cP(n)) = tr(rho,
> cP(n))` for every `c` in `(0,1]` and every `n`. No continuity, measurability, boundedness beyond the range
> `[0,1]`, or countable additivity is used; no ancilla, no lift, no dimension-three theorem.

The lemmas give `f(n) = 1/2 + beta dot n`; the range at `c = 1`, `n = ± beta/|beta|` forces `|beta| <= 1/2`, so
`rho = (I + 2 beta dot sigma)/2` is a density matrix with `c(1/2 + beta dot n) = tr(rho, cP(n))`, unique by the
Bloch correspondence, and homogeneity gives `u(c) = c` on the coins.

**Certificates (exact rational), in increasing truncation.**

| system | unknowns | rows | rank | kernel |
|---|---:|---:|---:|---|
| one free value per grid direction, no truncation at all | 52 | 5200 | **50** | exactly the restriction of `span{x, y}` |
| trigonometric polynomials, modes 0 to 8 | 17 | 400 | **15** | exactly `{cos t, sin t}` |
| all polynomials of degree `<= 6` on `S^2`, 12 rational great circles | 49 | 168 | **46** | exactly `span{x, y, z}` |

The first is the sharp one: with one independent unknown per grid point and no polynomial or Fourier truncation
whatsoever, the balanced-triple rows already leave nullity exactly 2 — Lemma 1 certified on the grid, which the
degree-truncated computations of the open sibling PRs could not say. A **fibred corollary** follows: if a fibre
realises only the ternaries of one great circle `C`, then `f` on `C` is exactly `1/2 + beta_C dot n`, Born odds on
the realised support with `rho` fixed up to the Bloch component normal to `C`, and two non-parallel circles pin
`rho` — PR #7926's one-circle proposition with the degree bound and the regularity both removed.

## T3 — The Counting Rogue On The Realised Family

`M_CONT` has a structural feature `M_all` does not: **arity is a function of the effect**. Every interior effect
`cP(n)` with `c < 1` occurs only in ternaries, every projector only in binaries, every coin only in binaries. So
`1/arity` is a menu-independent grading.

> **Proposition 3.** `w(cP(n)) = 1/3` for `0 < c < 1`, `w(P(n)) = 1/2`, `w(aI) = 1/2` is menu-independent, has
> range in `[0,1]`, is continuous in the direction and is normalised on **every** menu `L_CONT` realises —
> **5271** of them on the declared grid: 5200 ternaries, 52 binaries, 19 coins — and it is **not** of Born form,
> since `tr(rho, cP(n))` is homogeneous in `c` while `w(P)/1 = 1/2` against `w(P/2)/(1/2) = 2/3`.

The rogue is not isolated: the family `W(v) = (1/2 + lambda)|v| - 2 lambda/3 + beta dot v` is normalised on **all
5200** non-collinear ternaries identically in `lambda` and `beta`, its three coefficient conditions being exactly
`sum |v_i| = 2`, `sum v_i = 0` and `sum |v_i|/2 = 1`; its range is in `[0,1]` exactly for `lambda` in `[-3/2, 0]`,
and only `lambda = 0` is Born. On the projector boundary it is worse still: projectors never enter a non-collinear
ternary, so on `M_CONT` the values `w(P(n))` are constrained by nothing beyond `w(P(n)) + w(P(-n)) = 1`, and the
dimension-two frame freedom survives there verbatim. What kills the rogue is exactly the two menus `M_all` has and
`M_CONT` lacks: the collinear ternary `{aP(n), (1-a)P(n), P(-n)}` at `a = 1/4` sums to **7/6** on it, and the
mixed coin ternary `{cP(n), cP(-n), (1-c)I}` at `c = 1/2` sums to **7/6**. Either family, or a homogeneity clause
on the grading, restores the Born conclusion on the interior.

## T4 — Theorem B: `M_all` Without Homogeneity

Three exact reductions, none needing regularity. **Coins:** the binary coin gives `u(a) + u(1-a) = 1` and the
ternary coin `u(a) + u(b) + u(1-a-b) = 1`, so `u` is additive, and on the radius grid `j/24` the **144** coin rows
have rank **23** and nullity **1**, with kernel exactly `u(c) = c` normalised by `u(1) = 1`. **Oddness:** the
mixed coin ternary gives `W(cn) + W(-cn) = 1 - u(1-c) = c`, so `K(v) := W(v) - |v|/2` is odd on the punctured
ball, `|K| <= 1`. **Additivity on perimeter-2 pairs:** since `sum_i |v_i| = 2` on every balanced ternary,
normalisation is exactly `K(v_1) + K(v_2) + K(v_3) = 0`, that is `K(u + v) = K(u) + K(v)` whenever `|u| + |v| +
|u+v| = 2`, and Born is `K(v) = gamma dot v`. The graph-plane argument gives a `gamma_T` per triangle; two
perimeter-2 triangles never share two side vectors, so Lemma 1's chaining has no analogue, and that is where
homogeneity was doing work.

**The angle modes.** In a plane with `v = c n(phi)`, suppose `phi |-> K(c n(phi))` is integrable at each scale,
with angle-Fourier coefficients `h_k(c)`. Rotating a triangle shape and taking the `k`-th coefficient gives `sum_i
h_k(c_i) e^{i k alpha_i} = 0` for every perimeter-2 triangle, and with `alpha_2 - alpha_1 = pi - A_3`, `alpha_3 -
alpha_2 = pi - A_1` this makes `(h_k(c_1), h_k(c_2), h_k(c_3))` proportional to `(sin kA_1, sin kA_2, sin kA_3)`;
even `k` vanish by oddness and `k = 0` by the mixed coin menu. At `k = 1` the law of sines makes `sin A_i`
proportional to `c_i`, so `h_1(c)/c` is constant on each triangle, any two lengths in `(0,1)` summing above 1
share a triangle, and chaining gives `h_1(c) = lambda c` with `h_1(1) = lambda` from the collinear ternary at `a =
1/2`: **mode 1 is the Born vector and it is homogeneous.** For odd `k >= 3` a triangle with `A_1 = pi/k` and `sin
kA_2` nonzero forces `h_k(c_1) = 0` over `(m_k, 1)`, `m_k = 2 sin(pi/2k)/(1 + sin(pi/2k))`, and a second triangle
carries that zero to every length: **every mode `k >= 2` is killed.**

> **Theorem B.** Let `w` be menu-independent and normalised on `M_all`, with `n |-> w(cP(n))` measurable on `S^2`
> at each scale. Then `w(cP(n)) = c(1/2 + gamma dot n)` for almost every `n` at each `c`, with `|gamma| <= 1/2`,
> and `w(cI) = c`. Continuity in the direction at each scale, or homogeneity, upgrades this to every effect.

**Certificate on the 24-point radius grid, 44 perimeter-2 grid triangles.**

| rows | k = 0 | k = 1 | k = 3, 5, 7 |
|---|---|---|---|
| `M_CONT` only | nullity **3**: uncovered `1/24`, the rogue `(c - 2/3)` on the interior, `h(1)` free | nullity **3**: uncovered, Born `c`, `h(1)` free | nullity **2**: uncovered, `h(1)` free — interior killed |
| `M_all` | nullity **0** | nullity **1**, the vector `h_1(c) = c` including `h_1(1) = 1` | nullity **0** |

The radius `1/24` is covered by no grid triangle and is reported as a grid artefact, not a kernel direction. The
reading is sharp: modes `k >= 3` are killed by the non-collinear ternaries alone, so all the collinear and mixed
coin menus add is the scale coupling at mode 0 and the projector boundary — exactly the homogeneity content.

## The Correction To The Three Open Sibling PRs

The fibred Born theorem of PRs #7926 and #7931 and the kernel computations of PR #7919 are computations **inside
the homogeneous ansatz**, and say so in their own words — PR #7926, "In the normal form `w(cP(u)) = c(1 +
f(u))/2`", and PR #7919, "Take the polynomial sector `w(c P(u)) = c(1 + f(u))/2`" — while both runners build each
menu row by multiplying a direction-only vector by the scale, at `menu_row` in #7926 and at the same place in
#7919:

```text
row = [r + c * v for r, v in zip(row, f_row(n, a_mons, b_mons))]
row = [row[t] + coefficient * vals[t] for t in range(len(row))]
```

Under that ansatz every conclusion of those notes stands, and Theorem A makes their great-circle proposition
exact. What does not stand is the unqualified reading: **the realised menus do not supply homogeneity**, and
Proposition 3 is an explicit menu-independent non-Born grading on every menu `L_CONT` realises. The same ansatz is
why PR #7919 correctly found the mixed ternary rows vanishing identically — inside homogeneity that menu reduces
to the binary condition — while without it that menu is one of the two that kill the rogue. So the fibred Born
conclusions of #7926 and #7931 hold **as theorems about homogeneous gradings**, and menu-independence plus
normalisation on the realised balanced ternaries alone is insufficient.

## Corollary — The Readout Price

Against the three items PR #7919 prices — a fibred menu-independence clause, abundance, and the frame import:
**(1) the frame import drops**, exactly for any homogeneous grading (Theorem A) and up to the direction-regularity
clause on `M_all` (Theorem B), neither using `C^3`, an ancilla, or the dimension-three theorem; **(2) the fibred
clause stays and is sharpened** — one great circle of realised ternaries gives Born odds on the support exactly,
with no degree truncation and no regularity, and two non-parallel circles pin the state; **(3) abundance stays
and, on the continuum law, must be enlarged** — the realised family lacks the collinear and mixed coin ternaries,
and without them the counting rogue is menu-independent and non-Born on every realised support, so either those
menus join the abundance clause or homogeneity becomes a clause of the grading. The price reads either **fibred
clause plus abundance with collinear menus** or **fibred clause plus abundance plus a homogeneity clause**; the
frame item is gone in both, and the count of supplied items does not grow in the first.

## The Honest Residue

A regularity-free proof of homogeneity from `M_all` was **not obtained**. Gleason's bounded-implies-continuous
lemma works in dimension three because the frame condition is scale-free on the sphere; the perimeter-2 family is
not scale-free, and no amplification argument replacing it was found. Whether a bounded, direction-non-measurable,
non-Born grading exists on `M_all` is **open** here: none is exhibited and none is excluded. The parent's lift
needs no regularity at all, so on that one point the import still buys something, and Theorem B's clause is the
honest measure of what. The four-outcome collinear menu `{aP(n), bP(n), (1-a-b)P(n), P(-n)}` would give bounded
additivity in the scale and hence homogeneity exactly, but it has arity four: outside the parent's surface and the
realised family alike.

## Reading, Not Theorem

If a rule assigns odds to a scaled alternative without regard to the list it appears in, and the three-way
alternatives are all available, then the odds are the quantum ones — and to see it one needs nothing about a third
dimension, an extra system, or any smoothness in the rule. The catch is a scaling question that sounds too simple
to matter: does half of an alternative get half the odds? If the rule is told that it does, the argument is
complete and exact. If it is not told, the three-way alternatives the continuum rule offers can be answered by
counting how many alternatives there are, which is not the quantum answer; two further three-way alternatives,
both ordinary, remove that.

## Executable claim block

```text
grid_circle_directions: 52 rational unit vectors, Pythagorean parametrisation m <= 5; 68 at m <= 6; 12 great circles
balanced_ternaries: 5200 non-collinear balanced triples; weights in (1/21, 696/697); c_i <= 1 automatic
untruncated_circle_certificate: 52 unknowns, 5200 rows, rank 50, nullity 2, kernel = span{x, y} restricted
truncated_certificates: circle modes 0..8, 17 unknowns, 400 rows, rank 15, kernel {cos t, sin t}; sphere degree <= 6, 49 unknowns, 168 rows, rank 46, kernel span{x, y, z}
realised_menus: 5271 = 5200 ternaries + 52 binaries + 19 coins; the counting rogue is normalised on all
rogue_family: (1/2+lambda)|v| - 2lambda/3 + beta.v, range in [0,1] iff lambda in [-3/2, 0]; lambda = 0 is Born
rogue_killers: collinear ternary at a = 1/4, mixed coin ternary at c = 1/2, both summing to 7/6 on the rogue
coin_certificate: 144 rows, 24 unknowns on the grid j/24, rank 23, nullity 1, kernel u(c) = c; 44 perimeter-2 triangles, 1/24 covered by none
mode_nullity: M_CONT 3, 3, 2, 2, 2 at k = 0, 1, 3, 5, 7; M_all 0, 1, 0, 0, 0, mode 1 giving h_1(c) = c
arithmetic: exact rational throughout, fractions.Fraction; no float, no seed, no numpy, no sympy
import_boundary: the dimension-three frame theorem is quoted from the parent and never used; runner_result_required: zero failed checks
```

## Interfaces

**The parent, on main.** Its low-arity family is the family `M_all` here; its lift and frame step are quoted and
not used, and Theorems A and B reach the same conclusion on a smaller hypothesis set, neither refuting it. **PR
#7926.** Its `L_CONT` fixes `M_CONT`; Theorem A sharpens its fibred theorem and Proposition 3 qualifies it. **PR
#7931.** Its fibred clause is untouched and inherits that qualification. **PR #7919.** Its three-item price is
what the Corollary re-prices.

## Proof boundary

Proved: the dictionary and the automatic weight bound; Lemmas 1 and 2 and Theorem A, exact for **all** functions
with no regularity hypothesis; the fibred corollary; Proposition 3 and its one-parameter family; the two killing
menus; the exact coin rank certificate and the oddness reduction; the mode identities and the four exact rank
certificates on the declared grids. Not proved: any axiom-side derivation of the Born form; homogeneity without a
regularity clause; whether a bounded, direction-non-measurable, non-Born grading exists on `M_all`; anything at
arity four or above; and any claim that the continuum law of PR #7926 is the framework's law. Boundaries: the
qubit domain only, one site; the rational grids as declared — 52 and 68 circle directions, 36 per great circle, 12
great circles from four rational orthonormal frames, and the radius grid `j/24`; polynomial degrees `<= 8` on the
circle and `<= 6` on the sphere, bounding the truncated certificates only, since Lemmas 1 and 2 and Theorem A are
exact for all functions and the untruncated 52-value certificate has no degree bound. Nothing here is derived from
the axioms — family, grading and menu-independence are all supplied.

## Honest Auditor Read

Audit this as a bounded theorem about a supplied menu family: for a homogeneous grading the balanced ternaries
force the Born form exactly and without any regularity; for a general grading on the parent's family they force it
up to direction-measurability; on the family the continuum law realises they force neither, with an explicit
rogue. Do not audit it as a claim that the frame import is gone unconditionally, that homogeneity is proved, or
that the Born form follows from the four axioms.

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| scaled domain `S` and the family `M_all` | declared family | 2026-08-09 parent note, on main | physical eligibility remains open |
| `M_CONT`, the realised family | declared family | PR #7926, open, not on main | one law among several |
| homogeneity in the scale | grading clause, when assumed | stated here as a hypothesis | not supplied by any menu |
| direction-measurability at each scale | regularity clause for Theorem B | stated here as a hypothesis | not discharged |
| dimension-three frame theorem | quoted from the parent, never used | 2026-08-09 parent note | absent from both theorems |
| observations, fits, target probabilities | none | not used | not applicable |

## Review Record

The parent obtains the Born form here through a one-ancilla lift and the dimension-three frame theorem; this note
obtains it twice without either — exactly under homogeneity, and up to direction-measurability on the parent's own
family — reports a correction the three open sibling PRs need, and exhibits the menu-independent non-Born grading
that makes the point concrete. It does not advance current-surface physical Born closure: the family, the grading
clause and the law are supplied.

Independent audit remains required before the repository may assign any effective claim status.
