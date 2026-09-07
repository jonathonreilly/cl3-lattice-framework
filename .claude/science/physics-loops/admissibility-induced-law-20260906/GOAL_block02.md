# Goal — block 02: what the rule induces on an infinite window — the specification, an infinite-volume static law, and the exactly solvable row sweep (2026-09-06)

## Why this block

Block 01 (PR #7998) proved on finite windows that the formation law of a
nearest-neighbor product rule equals its static law exactly when every record
forms with at most one recorded neighbor, hence never on a window containing a
plaquette. Its N7 steelman left one obligation: an infinite-volume limit taken
along growing windows could wash out the normalizer history. The owner's gate
asks what the rule induces on the infinite lattice. This block answers at
scope: (i) the finite static laws with exterior records form a specification
and an infinite-volume static law exists (native proofs); (ii) on an infinite
strip of the lattice — an infinite window — the formation law along the row
sweep is exactly solvable (every row is the path's static chain; every
nearest-neighbor pair carries the single-edge law), while the static law of
the same strip has a different, exactly enclosed, nearest-neighbor pair
statistic. The normalizer history does not wash out. Uniqueness of the
infinite-volume static law on `Z^3` (the Dobrushin region) is the next block,
not this one.

Supervisor control computations (exact, `specs/supervisor_control_block02_*`):
row-law invariance `p0 P = p0` exact at `(3,1,2)` and `(5,2,4)` on the width-3
strip; horizontal and vertical nearest-neighbor pair-parallel probability
exactly `p/(p+q+4r)` (`1/4`, `5/23`); 8 row orbits under the 24 rotations and
the strip reflection; the quotient transfer matrix's characteristic polynomial
`λ^5 (λ^3 − 7312 λ^2 + 2578432 λ − 221134848)` at `(3,1,2)` (Perron root
`≈ 6945.3378`), degree 8 with a simple dominant root `≈ 179107.4288` at
`(5,2,4)`; the static infinite-strip center-row pair-parallel probability
`≈ 0.25611098728577869` and `≈ 0.21991516168701978`; second-eigenvalue ratios
`≈ 0.0325` and `≈ 0.0189` (numeric; the block makes these exact).

## Declared objects

- Menu, rotations, orbit weights `(p, q, r)`, product rule, records-only
  reading, static law with exterior records `ω`, formation law `μ_σ`: as in
  block 01's note (linked as the upstream dependency; its definitions are
  restated where used, never silently assumed). Declared triples `(3,1,2)`
  and `(5,2,4)`; the constant triple as the boundary.
- The one-edge kernel `K(a → s) = φ(s, a) / Z_1`, `Z_1 = p + q + 4r`:
  symmetric (`φ` symmetric) and doubly stochastic (rows sum to one; columns
  sum to one by transitivity), so the uniform law is `K`-invariant.
- Windows: the open `2×2×2` cube and the plaquette with exterior records
  (for the specification consistency); the strips `S_{W,n}` = the `W × n`
  grid of `Z^2` (rows of width `W`, `n` rows, nearest-neighbor edges, open
  boundary), `W ∈ {2, 3}` executed exhaustively and `W = 4` where the budget
  allows; the infinite strip `S_W` (rows indexed by `Z` or `N`) and the
  half-plane as proved objects.
- The row sweep `σ_row` on `S_{W,n}`: rows in order, each row left to right;
  under the records-only reading site `(i, j)` forms with recorded neighbors
  `(i, j−1)` (if `j > 0`) and `(i−1, j)` (if `i > 0`).
- Row states `ρ ∈ M^W`; the path static law `p_0(ρ) = (1/6) Π_{j≥1} K(ρ_{j−1} → ρ_j)`
  (block 01, Theorem B: the path swept from an end); the row-to-row formation
  kernel `P(ρ → ρ')`; the row transfer matrix `T(ρ, ρ') = V(ρ, ρ') A(ρ')` with
  `A(ρ) = Π_j φ(ρ_j, ρ_{j+1})` (row-internal edges) and `V(ρ, ρ') = Π_j φ(ρ_j, ρ'_j)`
  (vertical edges); the row symmetry group `G` = the 24 rotations acting
  diagonally, times the strip reflection `ρ ↦ ρ^{rev}`.

## Theorems (native proofs in the note; every finite statement executed)

**Theorem C (the specification and an infinite-volume static law).**
(C1, consistency, executed) For a finite window `Λ` with exterior records `ω`
and a sub-window `Δ ⊂ Λ`: the static law `μ_Λ^ω` conditioned on the records
on `Λ ∖ Δ` equals `μ_Δ^{ω'}` with `ω'` the records on `∂Δ` (exterior of `Λ`
or interior of `Λ ∖ Δ`); executed on the cube (sub-windows: a face, an edge,
a site) and the plaquette (an edge, a site), both triples, every configuration
of `Λ ∖ Δ`. Proof: direct cancellation, as Theorem A of block 01.
(C2, existence, proved) The family `{μ_Λ^ω}` is a specification with finite
range one; `M^{Z^3}` with the product topology is compact (a diagonal
argument on a finite menu — no choice principle); any exhausting sequence of
windows with any boundary records has a subsequence along which the
finite-volume static laws converge on every cylinder set; the limit satisfies
the finite-window conditional identity (C1) for every finite `Δ` (the
conditional kernels are local, so they pass to the limit). Averaging over
translations of a finite box of shifts and taking a further subsequence gives
a translation-invariant limit. Nothing about uniqueness is claimed.

**Theorem E (the row sweep is exactly solvable).** For the product rule on a
strip `S_{W,n}` (any `W ≥ 1`, any `n ≥ 1`) under `σ_row` and the records-only
reading:
(E1) the two-neighbor normalizer is the two-step kernel:
`Z_2(a, b) = Σ_s φ(s, a) φ(s, b) = Z_1^2 (K^2)(a, b)`;
(E2) the row-to-row kernel is
`P(β → α) = K(β_0 → α_0) Π_{j=1}^{W−1} K(α_{j−1} → α_j) K(α_j → β_j) / (K^2)(α_{j−1}, β_j)`
and the first row has law `p_0`;
(E3, invariance) `p_0 P = p_0`: summing `p_0(β) P(β → α)` over `β_0, β_1, …`
in turn telescopes — `Σ_{β_0} K(β_0 → β_1) K(β_0 → α_0) = (K^2)(α_0, β_1)`
cancels the `j = 1` denominator, leaving `K(α_1 → β_1)`; then
`Σ_{β_1} K(α_1 → β_1) K(β_1 → β_2) = (K^2)(α_1, β_2)` cancels the `j = 2`
denominator; and so on to `Σ_{β_{W−1}} K(α_{W−1} → β_{W−1}) = 1` — leaving
`(1/6) Π_j K(α_{j−1} → α_j) = p_0(α)`. Hence every row of the formation law
has exactly the law `p_0`, on every finite strip and on the infinite strip
and half-plane (the induction over rows needs no limit);
(E4, nearest-neighbor pairs) the joint law of `(α_0, …, α_{j−1}, β_j)` is
`(1/6) Π_{l<j} K(α_{l−1} → α_l) (K^2)(α_{j−1}, β_j)`, so every vertical pair
`(β_j, α_j)` and every horizontal pair `(α_{j−1}, α_j)` has the single-edge
law `(1/6) K` (pair-parallel probability `p/(p+q+4r)`), for every row `i ≥ 0`
and column `j`.
Executed: widths 2 and 3 (all `6^W` row states; `p_0 P = p_0` exactly; the
pair laws exactly) at both triples; width 4 if the `1296 × 1296` kernel fits
the budget (say so either way); the E1 identity symbolic; the constant-rule
boundary (`K` uniform) and an asymmetric-weight control (E3 fails).
What is NOT claimed: the same for any three-recorded-neighbor sweep (the
cubic sweep's normalizer `Z_3` is not a product of two-step kernels); the
plane's static law.

**Theorem F (the static infinite strip, exactly enclosed).** For `W = 3` (and
`W = 2`) at both triples:
(F1, symmetry reduction) `T` commutes with `G`; the Perron vector is
`G`-invariant; the quotient matrix `Q_{O,O'} = Σ_{ρ' ∈ O'} T(ρ, ρ')` (any
`ρ ∈ O`) on the row orbits (8 orbits at `W = 3`) has the same Perron root and
its Perron vector lifts to `T`'s;
(F2, Perron–Frobenius for a positive matrix, re-proved at scope) a matrix with
all entries positive has a simple positive eigenvalue `λ_1` strictly greater
in modulus than every other eigenvalue, with a positive eigenvector, unique up
to scale (Wielandt's argument: maximize `min_i (Tv)_i / v_i` over the simplex;
strict dominance from positivity);
(F3, the limit law) for the `n`-row strip the center-row law is
`∝ (A · T^c)(ρ) (T^{n−1−c} 1)(ρ)` and converges as `n → ∞` to
`w(ρ) ∝ A(ρ) ρ_1(ρ)^2` where `ρ_1` is the right Perron vector (the left
Perron vector is `A · ρ_1` because `V` is symmetric); the convergence is
geometric with ratio `|λ_2 / λ_1|`;
(F4, exact enclosure, executed) the characteristic polynomial of `Q` (exact
integers), its factorization, the Perron root's minimal polynomial and an
exact rational isolating interval (Sturm); the Perron vector of `Q` as
rational functions of `λ_1` (exact linear algebra over `Q(λ_1)`); the
center-row pair-parallel probability `s_∞ = Σ_ρ A(ρ) ρ_1(ρ)^2 [ρ_0 = ρ_1] / Σ_ρ A(ρ) ρ_1(ρ)^2`
as an algebraic number: its minimal polynomial by a resultant, an exact
rational isolating interval, and the identification of the correct real root
(a derivative bound on the rational function over the `λ_1` interval); the
enclosure excludes `p/(p+q+4r)`; the finite-`n` center-row values for
`n ≤ 13` converge into the enclosure; an exact rational bound on `|λ_2/λ_1|`
from the root isolation of the characteristic polynomial (all other roots'
moduli bounded above by a rational number below the Perron interval — use
Sturm on the real roots and a Cauchy/Fujiwara-type bound or the
`|λ|^2` real polynomial for complex pairs; report what was achieved exactly
and what remains numeric);
(F5, the separation, the block's headline at infinite scope) on the infinite
strip `S_3` the formation law's row marginal is `p_0` (Theorem E) with
nearest-neighbor pair-parallel probability exactly `p/(p+q+4r)`, and the
static law's center-row law is `w` with pair-parallel probability `s_∞`
inside an exact rational interval not containing `p/(p+q+4r)`: the two laws
differ on an infinite window; the normalizer history does not wash out along
the sweep.

## Named readings and premises (carried from block 01; nothing new adopted)

The records-only reading; positivity; the extensional reading of the
variation clause restricted to the declared menu (`(p, q, r)` not all equal);
the formation order as an unsupplied input (here the declared sweep). Theorem
E's exact solvability is a property of the two-recorded-neighbor sweep on a
two-dimensional window; no order is selected as physical.

## Quantifiers / domain

Theorem C1 executed on the declared windows; C2 proved for the finite menu on
`Z^3`. Theorem E proved for every strip width and every length including the
infinite strip and the half-plane; executed at widths 2, 3 (and 4 if it
fits). Theorem F executed at widths 2 and 3 with exact enclosures; proved via
F2 for positive matrices. No statement about the plane's static law, about
`Z^3`'s infinite-volume uniqueness, about any three-recorded-neighbor sweep,
about the physical formation order, the Born form, the bridge, or the gravity
action. This block does not fire wake condition 1 of
`docs/repo/DEFERRED_DECISIONS.md` entry 1.

## Forbidden

Floating point anywhere in the runner (numeric eigenvalues may be printed
ONLY as labelled non-load-bearing diagnostics computed by exact rational
iteration, never as evidence — prefer none); any sentence selecting the sweep
as the physical order; "the normalizer history washes out" or its negation
beyond the strip's scope; any Dobrushin or uniqueness claim on `Z^3`; the
words "certified", "closed", "complete", "global", "the law" outside their
exact finite meaning.

## Value gate (supervisor, in advance)

V1: the block-01 note's N7 obligation and the owner's infinite-lattice gate
(named consumer: the parked bridge decision material, not fired; the
record-matter lane's formation-order supply). V2: new — the specification and
existence on the finite menu (native), the exactly solvable sweep (E1–E4 with
the telescoping proof), the exact algebraic enclosure of the static
infinite-strip statistic, the infinite-window separation; sweep recorded in
`ROUTE_PORTFOLIO.md` (block 02 section). V3: the existence proof is standard
machinery, re-proved at scope because it is used; Theorem E's solvability
needs the menu's transitivity and the product rule's `Z_2 = Z_1^2 K^2`
identity, which the audit lane does not have; Theorem F's enclosure is a
framework computation. V4: non-trivial — E3 is a theorem about an infinite
object with an exact proof; F5 is an exact separation on an infinite window.
V5: not a variant of block 01 (finite windows, inequality only) nor of
anything landed (no note computes a formation law on an infinite window or a
transfer-matrix enclosure for this rule).
