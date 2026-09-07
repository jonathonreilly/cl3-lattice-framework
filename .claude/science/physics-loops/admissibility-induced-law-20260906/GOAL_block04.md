# Block 04 — the two-site block criterion: exact, and silent at the silent triples for every coupling (2026-09-07)

Branch `physics-loop/admissibility-induced-law-block04-two-site-block-criterion-20260907`, cut from block 03's tip `d61adbe4cb` (PR #8000); stacked PR. Supervisor-authored (Fable) with an Opus refuting checker; no primary seat: the mathematics is one page and every number is in the supervisor's controls `specs/supervisor_control_block04_two_site.py` and `specs/supervisor_control_block04_lines.py`.

## Why this block, and why it is small

Block 03 left the silent triples `(3,1,2)`, `(5,2,4)`, `(7,3,5)` and named the two-site block criterion as the cheapest sharper route. The control computed the block's sensitivities before any contract: the pair block's `x`-marginal is essentially as sensitive to an outer slot as a single site (`ρ/c_1 = 0.9993, 0.9804, 1.0025` at the three silent triples). Consequently the block sum, in every form, exceeds the block size there. The block therefore records this exactly, proves the obstruction for every coupling, and closes the route.

## Declared objects

- The pair block `V = {x, y}`, `y = x + e`; its boundary `∂V`: the five outer slots of `x` (`∂x`) and the five of `y` (`∂y`); `Z^3` is bipartite so no slot is adjacent to both. The block law with exterior records `ω`: `μ_V^ω(s_x, s_y) ∝ φ(s_x, s_y) Π_{z∈∂x} φ(s_x, ω_z) Π_{z∈∂y} φ(s_y, ω_z)`; its marginals `m_x^ω`, `m_y^ω`; the conditional `K^ω(s_y | s_x)` of `y` given `x` (independent of `ω_{∂x}`).
- Hamming distance `d_H` on `M^V`; `W_1(μ, ν) = min_π E_π d_H` over couplings (a minimum over a compact polytope; not computed exactly — bounded above and below).
- `b_V(z) = sup_{ω ~ ω' at z} W_1(μ_V^ω, μ_V^{ω'})`; `B_V = Σ_{z ∈ ∂V} b_V(z)`.
- `ρ = sup_{ω ~ ω' at z ∈ ∂x} TV(m_x^ω, m_x^{ω'})` (by symmetry the same for `z ∈ ∂y` and `m_y`); `ρ' = sup_{ω ~ ω' at z ∈ ∂x} TV(m_y^ω, m_y^{ω'})` (the second-order sensitivity); `c_1` from block 03.

## Theorems (all exact; every number in the controls)

**Theorem M (block-scan contraction on a finite window; proved).** For a finite window `Λ` and the random block scan that picks `a ∈ Λ` uniformly and resamples `V + a ∩ Λ` from its conditional law (the single site `a` when `a + e ∉ Λ`), coupled by a Hamming-optimal coupling at each step, the expected total disagreement `U = Σ_x P(η_x ≠ η'_x)` between two copies with the same exterior satisfies `E[U'] ≤ U − (1/n) Σ_x κ_x u_x + (1/n) Σ_z β_z u_z` with `κ_x` the number of updates covering `x` (two for interior sites) and `β_z` the sum of the update sensitivities to `z`; for interior `z`, `β_z = B_V`. Hence on the interior the scan contracts `U` iff `B_V < |V| = 2`. (Whether the contraction yields uniqueness on `Z^3` — the block analogue of Theorem I, which needs a per-site decay — is NOT proved here and is named as the obligation; the negative result below does not depend on it.)

**Theorem N (the obstruction; proved).** For any coupling `π` of `μ_V^ω` and `μ_V^{ω'}`, `P_π(η_x ≠ η'_x) ≥ TV(m_x^ω, m_x^{ω'})`, hence `W_1 ≥ TV(m_x) + TV(m_y)` and `b_V(z) ≥ ρ_z + ρ'_z`, `B_V ≥ 10(ρ + ρ')`. Executed: `ρ + ρ' = 0.32458…, 0.24323…, 0.24471…` at `(3,1,2)`, `(5,2,4)`, `(7,3,5)`, so `B_V ≥ 3.2458…, 2.4323…, 2.4471… > 2`. **The two-site block criterion is silent at the three silent triples for every coupling.** Upper bound (the sequential coupling: `x` first by the maximal coupling of the marginals, then `y` by the maximal coupling of `K^ω(·|s_x)`, `K^{ω'}(·|s'_x)`): `W_1 ≤ ρ_z (1 + c_1)` for `z ∈ ∂x` (since `K` does not depend on `ω_z`, the `y` values agree when the `x` values do, and disagree with probability at most `sup_{s ≠ s'} TV(K(·|s), K(·|s')) ≤ c_1` otherwise), so `B_V ≤ 10ρ(1 + c_1)`: `[3.2458, 3.4729]`, `[2.4323, 2.5327]`, `[2.4471, 2.5959]` at the three silent triples; at the region triples the upper bound is below `2` (`1.7518, 1.4966, 0.6676` at `(2,1,2)`, `(3,2,2)`, `(5,4,4)`).

**Theorem O (the whole-block sensitivity equals the marginal sensitivity; proved).** For `z ∈ ∂x`, `μ_V^ω = m_x^ω ⊗ K^ω` with `K^ω` independent of `ω_z`, so `TV(μ_V^ω, μ_V^{ω'}) = TV(m_x^ω, m_x^{ω'})`. Executed on every instance at `(3,1,2)`.

**Executed structure (G-type facts).** The exact `ρ` at the six triples (`2168397/7948400`, `271059507090000/1298168979740633`, `239957740750/1121635870169`, `67715/446034`, `1471549788/11145302999`, `81847628000000/1305850357630907`), `ρ'` at the three silent triples (`1350/26077`, `1915425000/55627392667`, `856455908/27833079009`), the ratios `ρ/c_1` (`0.9993, 0.9804, 1.0025, 0.9868, 0.9886, 0.9619`); along `(t,1,1)` and `(t,t,1)` (`t = 21/20 … 39/20`), the sequential bound `5ρ(1 + c_1)` crosses `1` in the same scan cell as `6c_1` (`(8/5, 33/20)` and `(29/20, 3/2)`), and `ρ/c_1` exceeds `1` beyond `t = 39/20` on `(t,1,1)` and beyond `t = 3/2` on `(t,t,1)`: the pair block is MORE sensitive than a single site at strong couplings.

## Forbidden
"non-unique", "several static laws", "phase transition", "the physical rule", "unique at (3,1,2)" etc. (block 03's list), "certified"; no uniqueness claim from Theorem M (the `Z^3` implication is not proved); the criterion's author's name only in Prior art/Imports.

## V1–V5 (advance)
V1 blocker: block 03's next question (the silent triples). V2 new: the exact two-site sensitivities, the obstruction for every coupling, the ratio structure. V3: not an audit-lane object. V4: non-trivial as an exact closure of the cheapest sharper route with a proof independent of the unproved implication. V5: not a variant of a landed note.

## Addendum after the refuting checker (supervisor, 2026-09-07; binding)

Theorem N's stated consequence "`b_V(z) ≥ ρ_z + ρ'_z`, `B_V ≥ 10(ρ + ρ')`" was wrong: `ρ` and `ρ'` are separate suprema attained at different boundary instances, so `sup (f + g) ≤ sup f + sup g`, not `≥`; the three numbers `3.2458, 2.4323, 2.4471` were false (the sequential coupling's own upper bounds lie below them). The checker proved, and the supervisor's control `specs/supervisor_control_block04_after_checker.py` reproduced, that `W_1 = TV(m_x) + TV(m_y)` exactly for a change at an x-slot (the disjoint-support coupling attains the lower bound), so `b_V(z) = σ := sup (TV(m_x) + TV(m_y))` and `B_V = 10σ` is exact: `152203860/48008647 ≈ 3.1703`, `124859962305/55627392667 ≈ 2.2445`, `14627647143900/6157201570091 ≈ 2.3756` at the silent triples (still `> 2`; Theorem N unchanged, Theorem N' added), and `74015/45047 ≈ 1.6430`, `314953560/211495159 ≈ 1.4891`, `≈ 0.6676` at the region triples. Theorem M is a sufficiency statement (contraction of the bound when `B_V < 2`), not an "iff". The N7 per-site figures are `B_V/2 = 1.5852, 1.1223, 1.1878`.
