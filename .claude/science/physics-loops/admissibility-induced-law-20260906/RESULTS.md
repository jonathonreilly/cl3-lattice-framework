# Results — block 01, admissibility-induced-law-20260906 (primary seat, Fable, 2026-09-06)

## Headline

For a covariant positive product rule on the six-projector menu with orbit weights `(p, q, r)` not all equal on the menu, the formation law along an order equals the static law exactly when every site forms with at most one recorded neighbor (Theorem B, proved for every finite graph via the identity `μ_σ Π Z_k = μ Z_W` and the single-site variation lemma; executed exactly: path3 4/6, P4 8/24, star4 12/24, cycle4 0/24 orders; distinct laws 2/3/5/4). On every window containing a plaquette no order gives equality, and cube8's 40,320 orders all have a site with two or more recorded neighbors (in fact `max_k |A_k| = 3` for every order, since the last site to form sees all three neighbors). The static half is the landed binary compatibility theorem generalized to the finite menu with exterior records (Brook rank 215 with `μ` in the nullspace; the sum rule fails at rank 216 with `R(1/4) = 27/25`), and the six coincidence routes each force the constant rule or are not one fixed nearest-neighbor rule.

## Run record

| run | TOTAL line | elapsed | note |
|---|---|---|---|
| control reproduction (`S/control.py`, own code) | all seven control numbers reproduced | 0.6 s | path3 4/6, P4 8/24, star4 12/24, cycle4 0/24; laws 2/3/5/4; `Z_2` differences; `Z_1 = p+q+4r`; `R(1/4) = 27/25`; `219/866` |
| baseline 1 (note stub) | `TOTAL: PASS=53 FAIL=0` | 7.8 s | stdout 7,705 chars, over the cap |
| baseline 3 (after two trim passes) | `TOTAL: PASS=53 FAIL=0` | 7.8 s | stdout 5,834 chars |
| baseline 4 (real note, after part 3) | `TOTAL: PASS=53 FAIL=0` | 7.8 s | stdout 5,834 chars |
| pinned cache (`runner_cache.execute_and_write_cache`, timeout 600) | `TOTAL: PASS=53 FAIL=0` | 7.83 s | `status: ok`; runner sha256 `48272bc7…065b61`; input fingerprint `e65ebc4c…24e68` |
| mutation census (41 mutations, 4 parallel, one helper per mutation) | see table below | about 90 s wall | first pass 39/41 agreed; two runner defects fixed; second pass pasted below |

Machine clock at launch: 17:48 UTC (the supervisor's stated launch time was 18:25 UTC; elapsed times below are by the machine clock from 17:48).

## Defects found in my own drafts and fixed

1. `E4c` expected rank 6 for the `6×6` matrix `Z_2 = Φ²` at both triples (the contract's expectation); at `(3,1,2)` the exact rank is 4 because `det Φ = (p+q+4r)(p+q−2r)²(p−q)³` and `3+1−2·2 = 0`. Fixed to the true values (4, 6) with the determinant factorization checked symbolically; the route needs only rank ≠ 1, which the symbolic minors give whenever `(p,q,r)` are not all equal. This is a contract defect, reported to the supervisor.
2. `E6b` conditioned the marginal reading's chain on the recorded neighbors only; the chain rule needs the conditional given all earlier records (a partial record set is not screened by the Markov property). Fixed; both versions executed (24/24 vs 0/24 orders reproduce `μ`).
3. Mutation `marginal_chain_rule_broken` swapped the last chain step for the R-only rule, which is vacuous by Theorem A (the last site's conditional given everything is the rule). Fixed to swap the second step.
4. Mutation `claim_born_derived` did not fire: the forbidden-phrase scan lowercased the note but not the phrase list ("derives the Born"). Fixed: both sides lowercased.
5. Unmutated stdout was 7,705 characters; two trim passes brought it to 5,834.
6. Operating-rule miss: note part 1 was written in one call of 254 lines (cap 250; over by 4). Parts 2 and 3 and every runner append were within the cap.

## Could-not list

- The raw `sympy.solve` (and lex Gröbner basis) of the cycle4 absence-factor system `(a, b, c, p, q, r)` on the declared 46-configuration set did not finish inside the 10-minute line (the Gröbner basis alone took 69 s and has degree-20 elements; `solve` was still running after 20 minutes in the scratch directory). The runner instead executes an exact two-step route for that instance: the static site marginal is uniform (symbolic), the first-formed site's formation marginal `(ac, bc, ac, bc, c², c²)` forces `a = b = c`, a constant absence factor cancels, and the reduced declared-set system in `(p, q)` after `r = 1` gives `p = q = 1`; the solution is verified on every configuration (E4b). The path3 instance is executed raw (Gröbner in under a second; `solve` 14 s in scratch; the runner uses the basis membership test).
- The general converse of Theorem A and the infinite-volume specification are open by contract, not attempted.
- No exhaustive cube8 law (6^8 configurations): by contract the cube is executed on the declared configuration family and order family only.

## Modelling choices

- Menu order `P(+x), P(−x), P(+y), P(−y), P(+z), P(−z)`; reference value `P(+x)`.
- Windows as declared; cycle4 embedded as the plaquette `(0,0,0), (1,0,0), (1,1,0), (0,1,0)` and path3 on the `x`-axis for the absence-direction reading.
- Exterior assignments: cycle4 two exterior records per site `P(+e_x), P(−e_y)`; cube8 the exterior neighbor along axis `a` carries `P(+e_a)`.
- Cube configuration family: all configurations within two sites of the all-`P(+x)` reference (741) plus 300 draws of the LCG (seed 20260906, multiplier 1103515245, increment 12345, modulus `2^31`, taking `(state >> 16) mod 6` per site); no overlap between the two parts.
- Cube order family: identity, reverse, BFS from 0 `(0,1,2,4,3,5,6,7)`, DFS from 0 `(0,1,3,2,6,4,5,7)`, `(0,3,5,6,1,2,4,7)`, `(0,7,1,6,2,5,3,4)`; the varied site `y` is the smallest-index recorded neighbor of the first site with two or more recorded neighbors.
- Rank certificates by fraction-free (Bareiss) integer elimination throughout; sympy exact for symbolic identities.
- Asymmetric instance: `φ_asym(a,b) = φ_(3,1,2)(a,b) + [a < b]`, static law oriented by site index.

## Census of formation-law classes (D5; identical at `(3,1,2)` and `(5,2,4)`)

| window | orders | distinct laws | class sizes | orders equal to `μ` |
|---|---|---|---|---|
| path3 | 6 | 2 | 4, 2 | `(0,1,2), (1,0,2), (1,2,0), (2,1,0)` |
| P4 | 24 | 3 | 8, 8, 8 | 8 (the orders with every site formed next to at most one recorded neighbor) |
| star4 | 24 | 5 | 12, 6, 2, 2, 2 | the 12 with the center first or second |
| cycle4 | 24 | 4 | 8, 8, 4, 4 | none |

cube8: distribution of `max_k |A_k|` over all 40,320 orders is `{3: 40320}`.

## Exact absence-extension solution set (route 4)

- path3, order `(0,2,1)`, unknowns `(a,b,c,p,q,r)` normalized by `r = c = 1`: 8 distinct polynomial equations; lex Gröbner basis contains `(a−1)u, (b−1)u, (p−q)²u, (q−1)³u` with `u = (p+q+4)²`; solution set on the positive domain `{a = b = c, p = q = r}`; verified on all 216 configurations.
- cycle4, order `(0,1,2,3)`: solution set `{a = b = c, p = q = r}` by the two-step exact route above; verified on all 1296 configurations. Raw solve: could-not (above).
- Any factorized absence weight: rank `Z_2` = 4 at `(3,1,2)`, 6 at `(5,2,4)`; minors `(p−q)²(p²+2pq+q²+8r²)` and `((p−r)²+(q−r)²)(p²+2pr+q²+2qr+6r²)` symbolic.

## Exact order-mixture differences (route 5, cycle4, 24 orders)

`max_v |avg_σ μ_σ(v) − μ(v)|` = `899/2341664` at `(3,1,2)`; `3478458125/23066700436908` at `(5,2,4)`; control `1585133/10007780364` at `(2,3,5)` (the panel's value, reproduced).

## Marginal reading (route 6)

cycle4 at `(3,1,2)`, `v_1 = P(e_x)`: static one-neighbor conditional `(219/866, 71/866, 72/433, 72/433, 72/433, 72/433)` against the rule's `(1/4, 1/12, 1/6, 1/6, 1/6, 1/6)`; on path3 the two agree for every `v_1`. Chain rule given all earlier records: 24/24 orders reproduce `μ`; given recorded neighbors only: 0/24.

## Mutation census (second pass, final runner; observed family read from each raw per-mutation stdout in `S/mut/<name>.txt`)

Summary: agree 41 of 41; by family B: 6/6; C: 7/7; D: 14/14; E: 7/7; F: 7/7

| mutation | expected family | observed failing family (raw stdout) | TOTAL line | exit | failing checks |
|---|---|---|---|---|---|
| `absence_blind_nonconstant_passes` | E | E | TOTAL: PASS=52 FAIL=1 | 1 | E3 |
| `absence_extension_solution_forged` | E | E | TOTAL: PASS=52 FAIL=1 | 1 | E4a |
| `asymmetric_identity_holds` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D12 |
| `brook_cycle_sign_flip` | C | C | TOTAL: PASS=51 FAIL=2 | 1 | C8,C9 |
| `claim_action_identified` | F | F | TOTAL: PASS=52 FAIL=1 | 1 | F2 |
| `claim_axiom_amended` | F | F | TOTAL: PASS=52 FAIL=1 | 1 | F2 |
| `claim_born_derived` | F | F | TOTAL: PASS=52 FAIL=1 | 1 | F2 |
| `claim_gate_explained` | F | F | TOTAL: PASS=52 FAIL=1 | 1 | F2 |
| `claim_infinite_volume` | F | F | TOTAL: PASS=52 FAIL=1 | 1 | F2 |
| `claim_order_physical` | F | F | TOTAL: PASS=52 FAIL=1 | 1 | F2 |
| `claim_rule_selected` | F | F | TOTAL: PASS=52 FAIL=1 | 1 | F2 |
| `compat_rank_off_by_one` | C | C | TOTAL: PASS=52 FAIL=1 | 1 | C5 |
| `constant_rule_varies` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D10 |
| `distinct_law_count_wrong` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D5 |
| `edge_flip_not_in_group` | B | B | TOTAL: PASS=52 FAIL=1 | 1 | B9 |
| `exterior_factor_dropped` | C | C | TOTAL: PASS=52 FAIL=1 | 1 | C2 |
| `fj_factorization_wrong` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D6 |
| `fj_j4_wrong` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D6 |
| `formation_equals_static_on_cycle` | D | D | TOTAL: PASS=49 FAIL=4 | 1 | D1,D3,D4,D5 |
| `formation_identity_drop_Zk` | D | D | TOTAL: PASS=48 FAIL=5 | 1 | D1,D2,D3,D4,D5 |
| `formation_uses_all_neighbors` | D | D | TOTAL: PASS=48 FAIL=5 | 1 | D1,D2,D3,D4,D5 |
| `marginal_chain_rule_broken` | E | E | TOTAL: PASS=52 FAIL=1 | 1 | E6b |
| `marginal_reading_is_fixed_rule` | E | E | TOTAL: PASS=52 FAIL=1 | 1 | E6a |
| `menu_drop_projector` | B | B | TOTAL: PASS=51 FAIL=2 | 1 | B2,B4 |
| `menu_witness_varies_on_menu` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D11 |
| `one_neighbor_normalizer_wrong` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D7 |
| `orbit_census_wrong` | B | B | TOTAL: PASS=52 FAIL=1 | 1 | B2 |
| `order_mixture_equals_static` | E | E | TOTAL: PASS=52 FAIL=1 | 1 | E5 |
| `p4_census_wrong` | D | D | TOTAL: PASS=51 FAIL=2 | 1 | D4,D5 |
| `plaquette_lemma_skips_order` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D8 |
| `positivity_zero_entry_passes` | B | B | TOTAL: PASS=52 FAIL=1 | 1 | B10 |
| `psi_nonconstant_passes` | B | B | TOTAL: PASS=52 FAIL=1 | 1 | B7 |
| `psi_rank_deficient` | E | E | TOTAL: PASS=52 FAIL=1 | 1 | E2 |
| `rotation_improper` | B | B | TOTAL: PASS=52 FAIL=1 | 1 | B3 |
| `single_edge_sum_rule_inconsistent` | C | C | TOTAL: PASS=52 FAIL=1 | 1 | C7 |
| `single_site_variation_constant` | D | D | TOTAL: PASS=52 FAIL=1 | 1 | D9 |
| `static_conditional_uses_two_hops` | C | C | TOTAL: PASS=52 FAIL=1 | 1 | C1 |
| `static_mu_wrong_edge_weight` | C | C | TOTAL: PASS=52 FAIL=1 | 1 | C1 |
| `sum_rule_pretends_consistent` | C | C | TOTAL: PASS=52 FAIL=1 | 1 | C6 |
| `weights_collapsed_to_constant` | D | D | TOTAL: PASS=51 FAIL=2 | 1 | D4,D5 |
| `z2_rank_one` | E | E | TOTAL: PASS=52 FAIL=1 | 1 | E4c |

## Pinned baseline stdout (from the cache file; exit 0, elapsed 7.83 s)

```text
AUDIT_INPUT_PATHS:
  docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md
  docs/MINIMAL_AXIOMS_2026-06-29.md
AUDIT_TIMEOUT_SEC: 600
scope: finite windows, six-projector menu, exact arithmetic; no infinite-volume claim
mutation: none
PASS: A1 both declared audit inputs exist
PASS: A2 axiom memo contains: There is one fixed nearest-neighbor ad
PASS: A3 axiom memo contains: is determined by, and varies with, the
PASS: A4 axiom memo contains: Records form.
PASS: A5 axiom memo contains: records are permanent
PASS: A6 axiom memo contains: Only records are readable.
PASS: A7 axiom memo contains: A site with no record cannot be read.
PASS: A8 the note carries its claim id
PASS: A9 upstream binary note exists (presence only)
PASS: B1 six projectors Hermitian, idempotent, trace one (sympy exact)
PASS: B2 pair orbits by Tr(PP') in (1, 0, 1/2): census (6, 6, 24)
PASS: B3 24 proper signed axis permutations: det +1, closed, order 24
PASS: B4 every rotation permutes the menu; action transitive
PASS: B5 U_z spinor: P(e_x)->P(e_y), P(e_y)->P(-e_x), fixes P(+-e_z)
PASS: B6 U_3 = (I - i(sx+sy+sz))/2 unitary, cycles P(e_x)->P(e_y)->P(e_z)
PASS: B7 covariant site weight: solution space dimension 1 (constant)
PASS: B8 covariant symmetric pair weight: exactly three orbit values
PASS: B9 edge flip t_{e1} o R_{e2,pi} is in the group, swaps 0 and e1; phi(a,b) = phi(rho b, rho a) = phi(b,a) on 36 pairs
PASS: B10 positivity: every r(s | eta) > 0 for every partial eta at the declared triples
PASS: C1 Theorem A: full conditionals of the static law equal the rule on path3/P4/star4/cycle4 (all v, x, s; both triples)
PASS: C2 cycle4 with exterior records P(+e_x), P(-e_y): full conditionals equal the rule with exterior records
PASS: C3 cube8: full-conditional identity on the family (741 near-reference + 300 LCG), with and without exterior
PASS: C4 positive rule => positive static law on the declared windows (cube8 on its family)
PASS: C5 Brook uniqueness on path3 (3,1,2): 648x216 compatibility system, exact rank 215 (Bareiss), mu spans the nullspace, positive
PASS: C6 sum rule inconsistent on path3: compatibility rank (216, 216) = 216 at lambda 1/4, -1/8 (|lambda| < 1/deg)
PASS: C7 single edge: the sum rule is consistent (nullity 1, law (1 + lambda<s,t>)/36) at both couplings
PASS: C8 sum-rule Brook cycle: R(1/4) = 27/25, R - 1 = -4*lambda**3/((lambda + 1)**2*(2*lambda - 1)); lambda^2 divides, no other root in |lambda| < 1/6
PASS: C9 the same Brook cycle for the product rule with symbolic (p, q, r) is exactly 1
PASS: D1 B1 identity mu_sigma prod Z_k = mu Z_W for every order, v, window, triple
PASS: D2 every formation law sums to one
PASS: D3 consistency line Z_W = sum_v mu_sigma prod Z_k (not a theorem)
PASS: D4 B2: mu_sigma = mu iff max|A_k| <= 1; equal orders path3/P4/star4/cycle4 = (4, 8, 12, 0)
PASS: D5 B5 census of distinct formation laws path3/P4/star4/cycle4 = (2, 3, 5, 4); class sizes [4, 2]; [8, 8, 8]; [12, 6, 2, 2, 2]; [8, 8, 4, 4]
PASS: D6 f_j formulas and factorizations symbolic, j = 1..5; at p = q: 2(p-r)(p^j-r^j)
PASS: D7 one-neighbor normalizer p + q + 4r for every menu value (symbolic)
PASS: D8 cube8: all 40320 orders have some |A_k| >= 2; max|A_k| distribution {3: 40320}
PASS: D9 cube8 six declared orders: identity on the family; single-site variation: three values = const * prod f_j
PASS: D10 B4 constant rule (2,2,2): uniform under every 1- and 2-neighbor condition; mu_sigma = mu for all orders of path3, cycle4
PASS: D11 menu witness f(x) = 1 + x^2(1-x^2) at (1,-1,0,1/2) = ('1', '1', '1', '19/16'), x^2 = 1/2: 5/4; induced (1,1,1); mu_sigma = mu on cycle4
PASS: D12 asymmetric pair weight on path3: the identity fails for 5 of 6 orders
PASS: E1 route 1: the (3,1,2) rule varies between the conditions P(+e_x) and P(+e_y) on the menu; the constant rule does not
PASS: E2 route 2: non-constant psi breaks covariance; Z_2-constant system in psi has rank [6, 6] (both triples)
PASS: E3 route 3: a direction-blind absence factor is forced constant by covariance (dimension 1)
PASS: E4a route 4 path3 (0,2,1): 8 eqs, r=c=1; Groebner basis contains (a-1)u,(b-1)u,(p-q)^2u,(q-1)^3u, u=(p+q+4)^2: a=b=c, p=q=r; verified
PASS: E4b route 4 cycle4 (0,1,2,3): uniform static marginal vs first-site marginal (ac,bc,ac,bc,c^2,c^2) forces a=b=c; reduced 3 eqs give p=q=r; verified
PASS: E4c route 4 factorized: rank Z_2 = [4, 6] at (3,1,2),(5,2,4); det Phi = (p+q+4r)(p+q-2r)^2(p-q)^3; minors symbolic: rank >= 2 unless p=q=r
PASS: E5 route 5 cycle4 mixture: max |avg - mu| = 899/2341664 (3,1,2), 3478458125/23066700436908 (5,2,4); control (2,3,5) 1585133/10007780364
PASS: E6a route 6: static one-neighbor conditional = rule on path3, not on cycle4 (219/866, 71/866, 72/433 x4 vs 1/4, 1/12, 1/6 x4)
PASS: E6b route 6 chain rule on cycle4: given all earlier records mu_sigma = mu for 24/24 orders; given recorded neighbors only 0/24
PASS: F1 the note carries the four fence sentences verbatim
PASS: F2 the note contains no forbidden phrase (hits: [])
PASS: F3 runner source: no floating-point literal or conversion call (0 hits)
per_element: executed — every menu value, every configuration of path3/P4/star4/cycle4, every order, both triples, exact
per_site: executed — the full conditional at every site of every declared window; cube8 on the declared configuration family
per_mode: checked and not executed — no spectral decomposition in the theorem; det Phi factorization is symbolic
per_block: executed — every order's normalizer history block by block; cube8: 40320 orders combinatorially, six exactly
lattice_wide: checked and not executed — finite windows only; the infinite-volume specification is named, not computed
PASS: G1 the five N5 resolution lines are printed (each >= 40 characters)
TOTAL: PASS=53 FAIL=0

----- stderr -----

```
