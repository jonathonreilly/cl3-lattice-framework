# Goal — block 03: the exact uniqueness region — where the rule induces exactly one static law on the cubic lattice (2026-09-06)

## Why this block

Block 02 (PR #7999) proved that an infinite-volume static law exists on `Z^3`
for the finite menu and left open whether it is unique. The owner's gate asks
what the rule induces on the infinite lattice; "an action, and one law or
several" is the honest shape of the answer. This block gives the exact
region of couplings in which the answer is "exactly one static law", by
re-proving the classical one-site contraction criterion at scope (a coupling
argument on finite windows, then the corollary on the lattice) and computing
the criterion's coefficient exactly for the covariant product rule. Outside
the region the criterion is silent: nothing is claimed about several laws.

Supervisor controls (exact; `specs/supervisor_control_block03_*`,
`specs/supervisor_control_block02_dobrushin_strip.py`): the one-neighbor
interdependence coefficient `c_1` of the covariant product rule on the
six-neighbor shell — `270/989` at `(3,1,2)` (`6c_1 = 1620/989`),
`8650000/40615109` at `(5,2,4)` (`6c_1 ≈ 1.278`), `2/13` at `(2,1,2)`
(`6c_1 = 12/13`), `2079/15566` at `(3,2,2)` (`6c_1 = 6237/7783`),
`4000000/61385721` at `(5,4,4)`, `98241110000/4544062780611` at
`(11,10,10)`; `c_1(p,q,r) = c_1(q,p,r)` on the whole grid; with the
orthogonal weight fixed at 4, `6c_1 < 1` exactly on the diamond
`{(2,4),(3,3),(3,4),(3,5),(4,2..6),(5,3..6),(6,4),(6,5)}` of `(p,q)` in
`1..12`; along the line `(t,1,1)` the crossing `6c_1 = 1` is at the second
real root of `t^7 − 2t^5 + 5t^4 − 8t^3 − t^2 − 4` (`≈ 1.60970232778585`) with
the maximizing shell pattern three `+x`, two `−x` and the flipped neighbor
`+x ↔ −x`; along `(t,t,1)` at the second real root of
`4t^7 − 8t^5 + 5t^4 − 8t^3 − t^2 − 1` (`≈ 1.47753945492135`), pattern three
`+x`, two orthogonal, flipped `+x ↔` orthogonal; along `(1,1,t)` at the
second real root of `t^7 + t^5 + 8t^4 − 5t^3 + 8t^2 − 4` (`≈ 0.676800877749306`),
same pattern. On the `3×3` planar window the finite-window comparison bound
holds with room: exact center-site total-variation sensitivity to one flipped
exterior slot `0.0090109` against the bound `1/56` at `(2,1,2)`, `0.0073929`
against `1971216/114898033` at `(3,2,2)`, `0.0016901` against
`100000000/30049760881` at `(5,4,4)` (the window's own four-neighbor
coefficients `1/8`, `1404/11431`, `10000/175641`).

## Declared objects

- Menu, rotations, orbit weights `(p, q, r)`, product rule, positivity, the
  static law of a finite window with exterior records `ω`, the specification
  and the existence of an infinite-volume static law: as in blocks 01 and 02
  (linked as upstream; definitions restated where used). Declared triples:
  the region triples `(2,1,2)`, `(3,2,2)`, `(5,4,4)`, `(11,10,10)` and the
  silent triples `(3,1,2)`, `(5,2,4)`; the constant triple as the boundary.
- A configuration `η` of the six-neighbor shell of a site `x`; the one-site
  conditional `r_x(· | η)`; for a neighbor direction `y`, the
  **interdependence coefficient**
  `C_{xy} = sup { TV(r_x(·|η), r_x(·|η')) : η, η' differ only at y }`,
  `TV = (1/2) Σ_s |·|`; for the covariant rule `C_{xy} = c_1(p,q,r)` for
  every neighbor `y` and `0` otherwise, and `α = Σ_y C_{xy} = 6 c_1`.
- A finite window `Λ` (a finite graph with declared exterior slots; the
  interior interdependence matrix `C_Λ` restricted to `Λ`); the influence
  series `D_Λ = Σ_{n≥0} C_Λ^n`, convergent when every row sum of `C_Λ` is at
  most `α_Λ < 1`; for two exterior assignments `ω, ω'` the vector
  `b_y = Σ_{z exterior, z ~ y} c_1 [ω_z ≠ ω'_z]`.
- Windows executed: the plaquette with its eight exterior slots (the
  one-step coupling inequality); the `3×3` planar window with its twelve
  exterior slots (the comparison bound by row transfer, four-neighbor
  coefficient); the `Z^3` shell (the coefficient `c_1`).

## Theorems (native proofs in the note; every finite statement executed)

**Theorem G (the coefficient, exactly).** (G1) For the covariant product
rule `C_{xy}` is the same number `c_1(p,q,r)` for all six neighbors (proper
rotations) and zero for non-neighbors (the conditional depends on the shell
only); `α = 6 c_1`. (G2) `c_1(p,q,r) = c_1(q,p,r)`: the relabeling
`s ↦ −s` of the forming site's value exchanges the parallel and antiparallel
orbits and leaves the total variation invariant. (G3) `c_1 = 0` iff
`p = q = r` (the constant rule; otherwise some one-neighbor conditional
varies). (G4, executed) the exact values at the six declared triples and at
the constant triple; the grid with `r = 4`, `p, q ∈ 1..8` (or `1..12` if it
fits) with the `6c_1 < 1` cells; the maximizing shell pattern and flipped
pair at each declared triple. (G5, executed) along each of the three lines
`(t,1,1)`, `(t,t,1)`, `(1,1,t)`: the maximizing pattern at the crossing, the
displayed rational function `6·TV(t) − 1` at that pattern (sign pattern of
the six differences fixed on the isolating interval — executed), the unique
positive root `t*` of its numerator isolated to width `10^{-20}` (Sturm), and
the exact verification at the two rational endpoints of the isolating
interval that the displayed pattern attains the supremum over all `7776 × 15`
pattern-and-pair choices and that `6c_1 − 1` changes sign across `t*`; the
threshold is stated as that root, with the sign change as the executed
content.

**Theorem H (finite-window comparison by coupling; re-proved at scope).**
Let `Λ` be a finite window with exterior assignments `ω, ω'`, and let
`μ = μ_Λ^ω`, `μ' = μ_Λ^{ω'}` be the static laws (unique with their full
conditionals, block 01 Theorem A). Suppose the row sums of `C_Λ` are at most
`α_Λ < 1`. Then there is a coupling of `μ` and `μ'` whose disagreement
probabilities `u_x = P(η_x ≠ η'_x)` satisfy `u ≤ D_Λ b` entrywise, hence for
every function `f` on `M^Λ`, `|μ(f) − μ'(f)| ≤ Σ_x δ_x(f) (D_Λ b)_x`, where
`δ_x(f)` is the oscillation of `f` in its `x` argument.
*Proof (all steps finite).* (H1, one step) Consider the random-scan
single-site update: choose `x ∈ Λ` uniformly, resample `η_x` from
`r_x(· | η, ω)`. Couple two chains (`η` with `ω`, `η'` with `ω'`) by choosing
the same `x` and using a maximal coupling of the two one-site conditionals,
which agree with probability `1 − TV`. Changing one site at a time along a
path from `(η, ω)` to `(η', ω')` and using the triangle inequality,
`TV(r_x(·|η,ω), r_x(·|η',ω')) ≤ Σ_{y∈Λ, y~x} C_{xy} [η_y ≠ η'_y] + b_x`.
Hence, writing `u_x` for the disagreement probability at `x` before the
step and `u'_x` after it, `u'_x ≤ (1 − 1/|Λ|) u_x + (1/|Λ|) ((C_Λ u)_x + b_x)`
(the site `x` is chosen with probability `1/|Λ|`, in which case the
disagreement at `x` is at most the total variation just bounded, in
expectation over the other sites' states; otherwise it is unchanged).
Executed on the plaquette with exterior records: the one-step inequality
`TV ≤ Σ C [differ] + b` for a declared family of configuration pairs and one
flipped exterior slot (exact integers), and the maximal-coupling agreement
identity `P(agree) = 1 − TV` on the same instances. (H2, the fixed point)
The map `u ↦ (1 − 1/|Λ|) u + (1/|Λ|)(C_Λ u + b)` is monotone and, from
`u^0 = 1`, its iterates decrease to the least fixed point `u* = D_Λ b`
(the Neumann series converges since `‖C_Λ‖_∞ ≤ α_Λ < 1`); executed on the
`3×3` window: `D_Λ` by exact inversion, `u*`, and the monotone iterates.
(H3, stationarity and the limit) Start both chains in their stationary laws
`μ` and `μ'` under any coupling; the coupled dynamics keeps the marginals
stationary (each chain is a Markov chain with `μ`, resp. `μ'`, invariant:
the single-site resampling preserves a law with the right full conditionals
— the static law's, by block 01 Theorem A). The disagreement vector after
`t` steps is bounded by the `t`-th iterate from `u^0 = 1`, which tends to
`u*`; the joint laws live on the finite set `M^Λ × M^Λ`, so a subsequence
converges to a coupling of `μ` and `μ'` with `u ≤ u*`. The bound on
`|μ(f) − μ'(f)|` follows by writing `f(η) − f(η')` as a telescoping sum of
single-site changes. ∎ Executed on the `3×3` window at the region triples:
the exact center-site marginals for the base exterior assignment and for one
flipped exterior slot (row transfer, integers), their total variation, and
the bound `(D_Λ b)_{center}`; the inequality holds at each triple with the
exact values above; at `(3,1,2)` the window's row sum exceeds one and the
window bound is not asserted (recorded, not used).

**Theorem I (uniqueness on the lattice in the region; corollary).** If
`α = 6 c_1 < 1` then the specification of the covariant product rule on
`Z^3` has exactly one infinite-volume static law. *Proof.* Let `μ, ν` be two
static laws (Gibbs measures for the specification; block 02 Theorem C2
gives at least one). For a local `f` with support in a box and the box `Λ_L`
of side `2L + 1` around it, the conditional identity of block 02 (C1 in the
limit) gives `μ(f) = ∫ μ_{Λ_L}^{ω}(f) μ(dω)` and likewise for `ν`, so
`|μ(f) − ν(f)| ≤ sup_{ω, ω'} |μ_{Λ_L}^ω(f) − μ_{Λ_L}^{ω'}(f)|`. By Theorem H
with `b_y ≤ 6 c_1 [y adjacent to the exterior]`, this is at most
`Σ_{x ∈ supp f} δ_x(f) Σ_{y ∈ ∂_in Λ_L} (D_Λ)_{xy} · 6c_1`. Since
`(C_Λ^n)_{xy} ≤ c_1^n N_n(x, y)` with `N_n` the number of nearest-neighbor
paths of length `n` from `x` to `y` inside `Λ`, and `Σ_y N_n(x,y) ≤ 6^n`,
`Σ_{y ∈ ∂_in Λ_L} (D_Λ)_{xy} ≤ Σ_{n ≥ L − ℓ} (6 c_1)^n = α^{L−ℓ}/(1 − α)`
(`ℓ` the radius of the support of `f`), which tends to zero as `L → ∞` when
`α < 1`. Hence `μ(f) = ν(f)` for every local `f`, and `μ = ν`. ∎ Executed:
the path-count bound's arithmetic `α^L/(1 − α)` as exact rationals for
`L = 1..12` at the region triples (a table), and the exact identity
`Σ_y N_n(x,y) = 6^n` on `Z^3` for `n ≤ 4` by enumeration.

**The region, stated.** For the covariant product rule at
`(2,1,2)`, `(3,2,2)`, `(5,4,4)`, `(11,10,10)` the rule induces exactly one
static law on `Z^3`; on the line `(t,1,1)` for every rational `t` strictly
between `1` and the isolating interval's lower endpoint of `t*`, and
likewise on the other two lines (executed at a declared list of rational
points on each line, each with its own exact `c_1`). At `(3,1,2)` and
`(5,2,4)` the criterion is silent: no statement about one law or several.

## Named readings and premises (carried; nothing new adopted)

Records-only reading (it enters only through blocks 01–02's definitions,
not this block's theorems, which concern the static laws); positivity; the
extensional reading of the variation clause restricted to the declared menu.
No formation order enters this block.

## Quantifiers / domain

Theorem G executed at the declared triples, grid and lines; G1–G3 proved.
Theorem H proved for every finite window; executed on the plaquette and the
`3×3` planar window. Theorem I proved on `Z^3` for `α < 1`; executed as
arithmetic. No statement about the silent triples beyond "silent"; no
statement about several static laws anywhere; no sharper criterion
attempted (named as leads: the two-site Dobrushin–Shlosman condition,
disagreement percolation); no formation law; no plane; no bridge, Born or
gravity statement; this block does not fire wake condition 1 of
`docs/repo/DEFERRED_DECISIONS.md` entry 1.

## Forbidden

Floating point anywhere in the runner; "non-unique", "phase transition",
"several static laws" as claims; "the physical rule"; any uniqueness claim
at the silent triples; any claim that the silent triples are outside every
criterion; "certified", "closed", "complete", "global", "the law" outside
their exact meaning; naming the criterion after its author in a claim
sentence (the author's name may appear once in the prior-art line as a
reference re-proved here).

## Value gate (supervisor, in advance)

V1: the owner's infinite-lattice gate ("one law or several") and block 02's
named next target; consumers: the parked bridge decision material (not
fired), the gravity lane's action question (the static law is unique in the
region — the object the lane's Gaussian analogy would need). V2: new — the
exact coefficient of the covariant rule, the exact region and thresholds,
the coupling re-proof of the finite-window comparison bound executed on
exact windows, the corollary on the lattice; sweep recorded in
`ROUTE_PORTFOLIO.md` (block 03). V3: the criterion is classical (referenced
and re-proved); its coefficient for this menu, the maximizing patterns and
the exact thresholds are framework computations the audit lane does not
have; the only in-repo use of the criterion (`WILSON_STAGGERED_*`,
2026-07-12) is on a different carrier and quotes the theorem as authority.
V4: non-trivial — the region is an exact algebraic object; the thresholds
are degree-7 algebraic numbers with the maximizing patterns identified.
V5: not a variant of blocks 01–02 (existence and formation) or of anything
landed.

## Addendum after the contract refuter lens (supervisor, 2026-09-06; binding on the note and runner)

The Opus contract refuter lens (`scratchpad/panel3/L4_block03_refuter.md`, twelve exact scripts) reproduced every control number in this contract — the seven coefficients, the direction independence, the `p ↔ q` symmetry, the diamond, the three polynomials with their sign changes, the three window comparisons with `D_Λ`, the path-count identity — and found seven defects in the contract's statements, three false as written. Each is verified by the supervisor's control `specs/supervisor_control_block03_after_lens.py` and corrected here; the note and runner follow this addendum where it differs from the text above.

**A1 (D1). "The second real root" is false.** Each of the three polynomials has exactly three real roots (executed), two negative and one positive; the threshold is the **unique positive real root**. The runner prints the real-root count.

**A2 (D2). Each line crosses `6c_1 = 1` twice; the region on a line is a bounded interval.** Exact: on `(1,1,t)`, `6c_1(1,1,36/25) = 110854656/112222201 < 1` while `6c_1(1,1,29/20) = 12731058/12618923 > 1`; on `(t,1,1)`, `6c_1(47/100,1,1) = 31800/31009 > 1` while `6c_1(1/2,1,1) = 12/13 < 1`. So on each line the set where `6c_1 < 1` is a bounded open interval `(t_low, t_high)` with both endpoints algebraic, and the contract's "the crossing" was an overclaim: read as a half-line it would silently state uniqueness at `(1,1,2)` where `6c_1 ≈ 1.959`. The second thresholds, with their maximizing patterns and polynomials, are:
- `(t, 1, 1)`: on the descending scan `t = 1 − k/40` the crossing lies in `(19/40, 1/2)`; the maximizing pattern is `(+x, +x, −x, +y, −y)` with the flipped neighbor `+z ↔ −z` (60 tied copies); the numerator of `6·TV − 1` is `−(t^2 + 10t − 5)`, so the second threshold is `t_2 = √30 − 5 ∈ [0.47722557505166113456, 0.47722557505166113458]`; `6c_1 > 1` below it.
- `(t, t, 1)`: crossing in `(27/40, 7/10)`; pattern five `+x` with the flipped neighbor `+y ↔ +z` (72 copies); numerator `−(t^5 + 7t − 5)`, one real root, `t_2 ∈ [0.69167061103656469380, 0.69167061103656469382]`; `6c_1 > 1` below it.
- `(1, 1, t)`: on the ascending scan `t = 1 + k/20` the crossing lies in `(7/5, 29/20)`; the same pattern (72 copies); numerator `5t^5 − 7t^4 − 1`, one real root, `t_2 ∈ [1.44577488770465582773, 1.44577488770465582774]`; `6c_1 > 1` above it. This line is the `(t, t, 1)` line under scale invariance (`c_1(1,1,t) = c_1(1/t,1/t,1)`), and both of its polynomials are the reciprocals of the `(t, t, 1)` polynomials — executed.
- The certificates of A5 and A6 use the Lipschitz lemma along a line: with every weight `t` or `1` the one-site weights are monomials `t^{k_s}`, `0 ≤ k_s ≤ 6`, so `Σ_s |a_s'(t)| ≤ 6/t` and `c_1` is Lipschitz with constant `6/u` on `[u, v]`; the region certificate bisects on `c_1` itself at dyadic midpoints (`2395`, `1782`, `1715` subintervals on the three lines, ~65 s), and the competitor sweep on each isolating interval certifies every shell-multiset-and-pair choice below or identifies it as a copy of the maximizer (`30, 288, 288` copies at the first thresholds, `60, 72, 72` at the second; no distinct choice uncertified). Supervisor controls: `specs/supervisor_control_block03_after_lens.py` (the lens's counterexamples, the second crossings, the sweeps with a crude Lipschitz bound) and `specs/supervisor_control_block03_certificates.py` (the `6/t` lemma prototype with timing).
Theorem G5 is restated: **on each of the three lines the set `{t > 0 : 6c_1 < 1}` contains the open interval between the two displayed algebraic thresholds and excludes both thresholds' outer neighborhoods on the declared scan; the region on the line is stated as that interval.** (Scale invariance `c_1(λp,λq,λr) = c_1(p,q,r)` is stated and executed; it relates the lines and the diamond and explains why the second crossings exist.)

**A3 (D3). `b` and `C_Λ` are defined from the window's own conditional, not from `c_1`.** On a window where a site has `d < 6` conditions (the plaquette, the planar `3×3`), the one-slot sensitivity of its conditional is the `d`-slot coefficient `c^{(d)}`, and `c_1 = c^{(6)}` is **not** a safe substitute: `c^{(4)}(2,5,3) = 14250/59251 > c_1(2,5,3) = 1629375/6780002` (executed). Declared objects are corrected: `C_{yz}` = the supremum, over that window's shells at `y` differing at slot `z` only, of the total variation of `y`'s conditional; `b_y = Σ_{z exterior, z ~ y} C_{yz} [ω_z ≠ ω'_z]`. For the covariant rule `C_{yz} = c^{(deg y)}`; on the boxes `Λ_L ⊂ Z^3` of Theorem I every site has six conditions and `C_{yz} = c_1`, so Theorem I is unchanged. The executed window numbers already used `c^{(4)}`; the runner adds the `(2,5,3)` row so the inversion sits next to the corrected definition.

**A4 (D4). H2's "the iterates decrease from `u^0 = 1`" is false under H's hypothesis.** Counterexample: the one-site window at `(3,1,2)` with all six exterior slots flipped has `α_Λ = 0` and `b = 6c_1 = 1620/989 > 1`, so `T(u) = b` and the iterates increase. Corrected proof step: `T(u) = (1 − 1/|Λ|) u + (1/|Λ|)(C_Λ u + b)` is monotone and a `‖·‖_∞`-contraction with modulus `1 − (1 − α_Λ)/|Λ| < 1` (its linear part has `‖C_Λ‖_∞ ≤ α_Λ`), hence has the **unique** fixed point `u* = D_Λ b` with `T^n(v) → u*` from every `v`; since `u^{n+1} ≤ T(u^n)` and `u^0 ≤ 1`, monotonicity gives `u^n ≤ T^n(1) → u*`, so `limsup u^n ≤ u*`. "Least fixed point" is dropped (the fixed point is unique). On the `3×3` window `T(1) ≤ 1` does hold at the region triples (executed), so the decreasing iterates are shown there as an executed illustration, not as the proof.

**A5 (D5). Endpoint dominance does not by itself make the threshold the displayed root.** The corrected G5 obligation, executed in the runner for each of the six thresholds: on the isolating interval `[a, b]` of the displayed polynomial's positive root, for **every** shell-multiset-and-pair choice (252 × 15), either the exact values `6·TV − 1` at `a` and at `b` are negative and an exact Lipschitz bound `L` on `[a, b]` (the lemma of the last bullet above: constant `6/a` on `[a, b]`) gives `max(6·TV(a), 6·TV(b)) − 1 + 6L(b − a) < 0`, or the choice's rational function (with the sign pattern at `a`) is **identical** to the displayed one. Then `6c_1 − 1 = max_i (6 g_i − 1)` crosses zero on `[a, b]` exactly where the displayed function does, i.e. at the root. The identical-function count is recorded (30 on `(t,1,1)` at the first threshold: the symmetric copies of the maximizer).

**A6 (D6). "Every rational `t` between …" becomes an executed certificate on an explicit interval, per line.** For each line the runner certifies `6c_1(t) < 1` for **all** real `t` in `[u, v]`, where `u` is the upper end of the lower threshold's isolating interval and `v` the lower end of the upper one, by the same exact Lipschitz-bisection certificate applied to every shell-multiset-and-pair choice (adaptive bisection; the number of subintervals is recorded). Together with A5 this proves the region on the line is exactly the open interval between the two thresholds, up to the isolating intervals. The three geometries are stated separately; "likewise on the other two lines" is dropped.

**A7 (D7). "Paths" reads "walks".** `(C_Λ^n)_{xy} ≤ c_1^n N_n(x, y)` with `N_n` the number of nearest-neighbor **walks** of length `n` from `x` to `y` (repeats allowed); `Σ_y N_n(x, y) = 6^n` is a walk count.

**A8 (D8). "Static law on `Z^3`" is pinned to the full finite-window conditional identity.** Declared objects: a static law on `Z^3` is a probability measure on the product space whose conditional law on every finite `Δ`, given the records outside `Δ`, is the finite-window static law `μ_Δ^ω` with exterior records — the property block 02's Theorem C2 proves for its constructed limit. Theorem I's first step uses exactly this for `Δ = Λ_L`; no single-site-to-volume lemma is needed under this definition, and the note says so.

**A9 (D9). The maximizer is not unique.** The runner records the tie count over shell-multiset-and-pair choices at each declared triple (`(3,1,2)`: 12; `(5,2,4)`: 6; `(2,1,2)`: 60; `(3,2,2)`: 30; `(5,4,4)`: 30; `(11,10,10)`: 30) and the note says "a maximizing pattern (the maximizer is not unique; tie count recorded)".

**A10 (D10). The last step of Theorem I** adds the clause: cylinder events form a π-system generating the product σ-algebra, so `μ(f) = ν(f)` for every local `f` gives `μ = ν`.

**A11 (lens confirmations recorded as executed content).** The silent triple `(7,3,5)` with all weights distinct, `c_1 = 6391462/29948925`, `6c_1 ≈ 1.2805`, is added to the coefficient table; direction independence holds for all 720 slot permutations (the conditional is a product over the shell), stronger than the rotation argument, and the note says so; Theorem H's expectation step needs nothing about how the other sites are coupled (the one-step bound holds pointwise on the joint state; only linearity of expectation is used) and the note states this explicitly; Theorem I uses no translation invariance (only the site-homogeneity of `c_1` from the one fixed covariant rule) and therefore covers every static law on `Z^3`, translation-invariant or not — the note says so; the finite menu is load-bearing (compactness in H3, finite maxima, `δ_x(f) < ∞`, block 02's existence) and is declared.
