# CHECKER — block 04 (two-site block criterion), independent refuting seat

## 1. VERDICT

**FIX FIRST.**

The note's **conclusion survives** (the two-site block criterion is silent at
`(3,1,2)`, `(5,2,4)`, `(7,3,5)` for every coupling: `B_V > 2` at all three).
But the **inequality that carries it, and the three headline numbers, are
false**, and I have the counter-computation, not just an objection.

Fix list, in order of severity:

1. **BLOCKER — Theorem N's consequence step is invalid, and its numbers are
   above the true `B_V`.** Note lines 184–185: "the supremum over pairs at a
   slot gives `b_V(z) ≥ ρ_z + ρ'_z`". `ρ` and `ρ'` are two **separate** suprema
   over the instance space (note lines 110–117). Theorem N gives, per instance,
   `W_1 ≥ TV(m_x) + TV(m_y)`; taking the supremum gives
   `b_V(z) ≥ sup_ω [TV(m_x) + TV(m_y)]`, and `sup(f+g) ≤ sup f + sup g`. The
   step used is the wrong direction of that inequality. It is not repairable
   by inspection: the two maximizers are **different boundary instances** at
   all three silent triples (table in §2), and I show below that the claimed
   bound is **numerically false**, not merely unproved.
2. **BLOCKER — the three headline numbers `3.2457…, 2.4323…, 2.4470…` are
   larger than `B_V` itself.** They appear at note lines 48, 163, 193, 257–259
   (table column "`B_V` lower"), 351 (N7), 374 (Falsifiers) and in the YAML
   `claim_scope` (line 5). The correct exact values (§2, §3) are
   `B_V = 3.1703426260…, 2.2445769309…, 2.3756972997…`, all still `> 2`.
3. **`W_1` *is* exactly computable here — the note's "`W_1` is not computed
   exactly" (line 121) and "`W_1` is bounded, not computed" (line 387) are
   conservative but they hide that the lower bound is attained.** I prove and
   verify `W_1(μ_V^ω, μ_V^{ω'}) = TV(m_x) + TV(m_y)` exactly for every
   `x`-slot change (§3), so `b_V(z)` and `B_V` are exact, not an interval.
4. **N7 (line 351): the three per-site numbers are in the wrong order** —
   `10(ρ+ρ')/2` is `1.62, 1.22, 1.22` in the note's own triple order, printed
   as `1.22, 1.22, 1.62`. With the corrected quantity the numbers are
   `1.5851713130, 1.1222884655, 1.1878486498`, still `> 1`; the steelman's
   answer therefore stands after the fix.
5. **Theorem M's "iff" (heading line 214, line 229, obligation line 164) is a
   one-sided result stated two-sided.** The displayed inequality is an upper
   bound on `E[U']`; `B_V < 2` is proved *sufficient* for contraction, nothing
   proves it necessary. Say "contracts if `B_V < 2`".
6. Cosmetic: the `ρ/c_1` column (lines 257–262) truncates where it should
   round (`0.9992 → 0.9993`, `0.9885 → 0.9886`, `0.9618 → 0.9619`), while D1
   (line 279) rounds (`1.6123` for `1.612281`). One convention, please. The
   contract `GOAL_block04.md` prints the rounded forms, so note and contract
   currently disagree digit-for-digit.
7. Cosmetic: note line 225, "For sites `x` with `x ± e ∈ Λ`, `κ_x = 2`" — the
   correct condition is `x − e ∈ Λ` alone (`a = x` always covers `x`).

Everything else I attacked held: `c_1`, `ρ`, `ρ'`, the maximizing instances,
Theorem O, the symmetry claim, both line scans, all fences, all forbidden
phrases, the author-name rule, the runner and 12 mutations.

---

## 2. CK table — exact numbers

| CK | verdict | exact numbers |
|---|---|---|
| CK-01 `ρ`, `ρ'`, ratios, maximizers, symmetry | **CONFIRM** | see below |
| CK-02 Theorem O | **CONFIRM** | 476,280 exhaustive at `(3,1,2)` + 15,000 random: 0 violations |
| CK-03 Theorem N + exact `W_1` | **REFUTE (the consequence step and its numbers)** | see below |
| CK-04 Theorem M | **CONFIRM with one overstatement** | counts `κ_x=2`, 10 translates, coefficient `1−(2−B_V)/n` all re-derived correct; "iff" is one-sided |
| CK-05 line scans D1, D2 | **CONFIRM** | both crossings and both ratio thresholds reproduce |
| CK-06 numerals / fences / scope | **CONFIRM except 3 items** | N7 ordering; `ρ/c_1` truncation; `claim_scope` carries the false `B_V >= 10(rho+rho')` |
| CK-07 runner validity | **CONFIRM** | `TOTAL: PASS=21 FAIL=0`; stdout byte-identical to the cache; sha matches; 12/12 mutations fail in their declared family |
| CK-08 hidden wall / overclaim | **CONFIRM except CK-04's "iff"** | no "sharpest", no transition/several-laws language, larger blocks named "not attempted", the silence never leans on the `Z^3` step |

### CK-01 — recomputed from the definition (my own enumeration, 252 × 126 × 15)

Every literal in the note's table reproduced **exactly**:

| triple | `c_1` | `ρ` | `ρ/c_1` (exact float) | `ρ'` |
|---|---|---|---|---|
| `(3,1,2)` | `270/989` ✓ | `2168397/7948400` ✓ | `79427579/79484000` = 0.9992901590 | `1350/26077` ✓ |
| `(5,2,4)` | `8650000/40615109` ✓ | `271059507090000/1298168979740633` ✓ | `1100911142594662281/1122916167475647545` = 0.9804036797 | `1915425000/55627392667` ✓ |
| `(7,3,5)` | `6391462/29948925` ✓ | `239957740750/1121635870169` ✓ | `1496559013096875/1492897343194939` = **1.0024527272 > 1** ✓ | `856455908/27833079009` ✓ |
| `(2,1,2)` | `2/13` ✓ | `67715/446034` ✓ | `880295/892068` = 0.9868025756 | — |
| `(3,2,2)` | `2079/15566` ✓ | `1471549788/11145302999` ✓ | `19729667528/19957868161` = 0.9885658813 | — |
| `(5,4,4)` | `4000000/61385721` ✓ | `81847628000000/1305850357630907` ✓ | `1256068914229947/1305850357630907` = 0.9618781409 | — |

Maximizing instance of `ρ` at `(3,1,2)`: `∂y = (+x,+x,+x,+y,+y)`,
other four `∂x = (+x,+x,+x,−y)`, pair `+x ↔ −x` — exactly the note's (lines 264–268).
At `(5,2,4)` and `(5,4,4)`: all ten slots `+x`, pair `+x ↔ −x` — as the note says.

Symmetry claim (note lines 110–117): **CONFIRMED by a separate enumeration**
that varies a slot of `∂y` instead of `∂x` (function `rho_from_y_slot`, not a
symmetry argument). At all three silent triples,
`sup TV(m_y)` over `∂y`-slot changes `= ρ` and `sup TV(m_x)` over `∂y`-slot
changes `= ρ'`, as rationals.

### CK-02 — Theorem O

Exhaustive over all 476,280 `x`-slot instances at `(3,1,2)`: 0 violations of
`TV(μ_V) = TV(m_x)`. 3,000 random instances at each of the other five triples:
0 violations. Proof as written is correct.

**The `y`-slot case (the note does not state it).** For a change at a `y`-slot,
on 2,000 random instances per silent triple: `TV(μ_V) = TV(m_y)` in 2,000/2,000
and `TV(μ_V) > TV(m_x)` in 2,000/2,000, max gap `0.243163` at `(3,1,2)`. The
exact relation is the mirror one, `TV(μ_V^ω, μ_V^{ω'}) = TV(m_y^ω, m_y^{ω'})`,
and it does **not** factor through the `x`-marginal. Nothing in the note claims
otherwise; recording it because the spec asked.

### CK-03 — exact `W_1` by my own min-cost flow (integer transportation, SSP)

Method: scale both block laws to the common integer denominator `T·T'`, solve
the 36×36 integer transportation problem with cost `d_H ∈ {0,1,2}` by
successive shortest paths with full bottleneck pushes. Exact integers
throughout; no LP solver, no float, no import of the runner.

| instance | `TV(m_x)` | `TV(m_y)` | lower `TV(m_x)+TV(m_y)` | **exact `W_1`** | sequential `E d_H` | upper `TV(m_x)(1+c_1)` |
|---|---|---|---|---|---|---|
| `(5,2,4)` **ρ-maximizing** (all ten `+x`, pair `+x↔−x`) | 0.2088014051 | 0.0098919172 | `283900887090000/1298168979740633` = 0.2186933223 | **0.2186933223** | 0.2296294815 | 0.2532708698 |
| `(5,2,4)` I2 (`∂y=(+x,+x,+y,−y,−z)`, `∂x_o=(+x,+y,−y,+z)`, `+x↔−x`) | 0.1872261243 | 0.0209457655 | `47818650/229707527` = 0.2081718898 | **0.2081718898** | 0.2154338495 | 0.2271005950 |
| `(5,2,4)` I3 (`∂y=(+x,−y,−y,+z,−z)`, `∂x_o=(−x,−x,+y,−z)`, `+y↔+z`) | 0.1394049502 | 0.0159260068 | `1152595/7420253` = 0.1553309570 | **0.1553309570** | 0.1573090144 | 0.1690947097 |
| `(5,2,4)` I4 (`∂y=(+x,+x,+x,+y,+y)`, `∂x_o=(+x,+x,+x,+y)`, `+x↔−x`) | 0.1971057505 | 0.0120415724 | `53046945384/253634350445` = 0.2091473229 | **0.2091473229** | 0.2188001986 | 0.2390843339 |
| `(3,1,2)` **ρ-maximizing** | 0.2728092446 | 0.0280516834 | `2391363/7948400` = 0.3008609280 | **0.3008609280** | 0.3129753779 | 0.3472869959 |
| `(7,3,5)` all ten `+x`, `+x↔−x` | 0.2132707151 | 0.0192924533 | `17665382830381930/75959503613253117` = 0.2325631684 | **0.2325631684** | 0.2371203314 | 0.2587852594 |

Plus 900 further random instances (300 per silent triple) and 3,600 more in a
second sweep — **5,406 exact transport solves, and in every single one
`W_1 = TV(m_x) + TV(m_y)` exactly.** The sequential coupling equalled `W_1`
in only 27 of 900 random instances (11 / 9 / 7 at `(3,1,2)` / `(5,2,4)` /
`(7,3,5)`): **the sequential coupling is not optimal in general**, and it is
never worse than the note claims (`lower ≤ W_1 ≤ seq ≤ upper` held in all).

**Why the equality holds (proof, so this is not a numerology claim).** For a
change at an `x`-slot, Theorem O gives `μ = a ⊗ K`, `ν = b ⊗ K` with the *same*
kernel. Build the coupling: take the maximal coupling of `a, b` on the
`x`-coordinate; on the common part (mass `1 − TV(a,b)`) set `x = x'` and draw
`y = y'` from `K(·|x)` — cost 0. On the residual (mass `TV(a,b)`, and `r_a`,
`r_b` have **disjoint supports**, so `x ≠ x'` there) couple the two residual
*joint* laws by any coupling whose `y`-marginals form a maximal coupling of
`r_aK/TV` and `r_bK/TV` (draw `(y,y')` from that maximal coupling, then `x`
and `x'` from their conditionals given `y`, `y'` independently — marginals are
correct). Since `a − b = r_a − r_b` as signed measures, `aK − bK = r_aK − r_bK`,
so the `y`-disagreement is `½‖r_aK − r_bK‖₁ = TV(m_y, m'_y)` exactly. Total
`E d_H = TV(m_x) + TV(m_y)`, which meets Theorem N's bound. ∎

Hence `b_V(z) = sup_ω [TV(m_x) + TV(m_y)]` **exactly**, and `B_V = 10 b_V(z)`.

**The counter-computation.** I computed that supremum exactly over the full
252 × 126 × 15 instance space:

| triple | `sup [TV(m_x)+TV(m_y)]` (exact) | `= B_V/10` | **true `B_V`** | note's claimed lower bound `10(ρ+ρ')` | `> 2`? |
|---|---|---|---|---|---|
| `(3,1,2)` | `15220386/48008647` | 0.3170342626 | **3.1703426260** | 3.2457900342 ✗ | yes |
| `(5,2,4)` | `24971992461/111254785334` | 0.2244576931 | **2.2445769309** | 2.4323453078 ✗ | yes |
| `(7,3,5)` | `1462764714390/6157201570091` | 0.2375697300 | **2.3756972997** | 2.4470666107 ✗ | yes |

The maximizers of `ρ` and of `ρ'` are different instances, which is exactly why
the note's step fails:

| triple | argmax `ρ` | argmax `ρ'` | argmax of the sum |
|---|---|---|---|
| `(3,1,2)` | `∂y=(+x,+x,+x,+y,+y)`, `∂x_o=(+x,+x,+x,−y)` | `∂y=(+x,+x,+x,+y,−y)`, `∂x_o=(+y,−y,+z,−z)` | `∂y=(+x,+x,+x,+y,−y)`, `∂x_o=(−x,−x,−x,−x)`; there `TV(m_x)=0.2700289804 < ρ`, `TV(m_y)=0.0470052822 < ρ'` |
| `(5,2,4)` | `∂y=(+x)^5`, `∂x_o=(+x)^4` | `∂y=(+x)^5`, `∂x_o=(+y,−y,+z,−z)` | `∂y=(+x)^5`, `∂x_o=(+y,−y,+z,−z)`; `TV(m_x)=0.1900245675 < ρ` |
| `(7,3,5)` | `∂y=(+x,+x,+y,+y,+z)`, `∂x_o=(+x)^4` | `∂y=(+x,+x,+x,+x,+y)`, `∂x_o=(+y,−y,+z,−z)` | `∂y=(+x,+x,+x,+y,−y)`, `∂x_o=(−x)^4` |

**Independent confirmation that the note's bound is false, not merely
unproved** (this one does not use my `W_1` equality proof at all): the note's
*own* sequential coupling gives `b_V(z) ≤ sup_ω [sequential E d_H]`, and I
computed that supremum exactly over the same full instance space —

| triple | `sup_ω [sequential E d_H]` (exact) | so `B_V ≤` | note claims `B_V ≥` |
|---|---|---|---|
| `(3,1,2)` | `1728802/5326557` | **3.2456275226** | 3.2457900342 |
| `(5,2,4)` | `1964883079712097648/8530198812860508875` | **2.3034434751** | 2.4323453078 |
| `(7,3,5)` | `155739611010/637009609081` | **2.4448549722** | 2.4470666107 |

Margins: `1.6×10⁻⁴` at `(3,1,2)`, `0.129` at `(5,2,4)`, `2.2×10⁻³` at
`(7,3,5)`; all three strict. So `B_V < 10(ρ + ρ')` at all three silent triples: the note's inequality is
**false**, and the number in the "`B_V` lower" column exceeds `B_V`.

**Does a different cost evade the obstruction (N7 steelman)?** Answered
honestly at the scope it claims, once the numbers are fixed. The per-site
figure a criterion of that shape inherits is `B_V/2 = 5·sup[TV(m_x)+TV(m_y)]`
= `1.5851713130, 1.1222884655, 1.1878486498` — all above `1`, so the silence
survives for any per-slot cost dominating Hamming. A cost *below* Hamming
(e.g. a weighted Hamming with weights `< 1`) is genuinely outside the reply,
and the note is right to name it as a different theorem rather than dismiss it.

### CK-04 — Theorem M, step by step (re-derived independently)

- Hamming-optimal coupling exists: couplings of two laws on a finite set form a
  compact polytope, `E_π d_H` linear. ✓
- `W_1` is a metric (min over couplings of a metric cost), so the triangle
  inequality along one-slot boundary changes gives
  `W_1 ≤ Σ_{z∈∂W} b_W(z) 1[η_z ≠ η'_z]`. ✓ (`b_W(z)` is a sup over *all*
  one-slot pairs, so each interpolation step is covered.)
- `κ_x`: `x ∈ W(a)` iff `a = x` or `a = x − e`, so `κ_x = 2` iff `x − e ∈ Λ`.
  ✓ (note's `x ± e ∈ Λ` is sufficient but stronger than needed — cosmetic).
- 10 translates adjacent to a slot: `z ∈ ∂(V+a)` iff (`a ~ z`, `a ≠ z−e`) — 5
  choices — or (`a+e ~ z`, `a ≠ z`) — 5 choices; the two sets are disjoint
  because `Z^3` is bipartite and `a`, `a+e` have opposite parity. Total 10. ✓
  Their sensitivities are the ten `b_V(z')`, `z' ∈ ∂V`, summing to `B_V`. ✓
- Coefficient of `u_z`: `1 − κ_z/n + β_z/n = 1 − (2 − B_V)/n`. ✓
- Single-site updates at `a + e ∉ Λ`: treated consistently — they still cover
  `a` (so `κ` is unaffected) and contribute the one-site sensitivity, and the
  interior is defined to exclude them. ✓
- **The "iff" is not proved.** The displayed relation is an upper bound on
  `E[U']`; `B_V ≥ 2` makes the *bound* useless but does not exhibit
  non-contraction. Heading (line 214), line 229 and the obligation row (line
  164) should read "if", not "iff"/"exactly when".
- What M does not give: the paragraph is honest and complete (no per-site
  decay, no `Z^3` claim, silence independent of it). One dependency: its last
  sentence, "at the silent triples the interior coefficient … is at least `1`",
  uses `B_V ≥ 2`, which after the fix rests on `B_V = 3.1703…, 2.2446…,
  2.3757…` — still true.

### CK-05 — the line scans, recomputed by my own code

`(t,1,1)`, `t = k/20`, `k = 21…39`: `6c_1` crosses `1` between `t = 32/20` and
`33/20`; `5ρ(1+c_1)` crosses `1` in the **same** cell `(8/5, 33/20)`; `ρ/c_1`
first exceeds `1` at `t = 39/20`. Sample points:
`t=8/5`: `6c_1 = 0.982788`, `5ρ(1+c_1) = 0.936631`, `ρ/c_1 = 0.982680`;
`t=33/20`: `1.070542 / 1.032174`; `t=35/20`: `1.237952 / 1.227425`;
`t=37/20`: `1.392860 / 1.423824`; `t=38/20`: `1.465293 / 1.517908`;
`t=39/20`: `1.534332 / 1.612281`, `ρ/c_1 = 1.004174`.

`(t,t,1)`: both cross in `(29/20, 3/2)`; `ρ/c_1 > 1` from `t = 3/2`. Samples:
`t=29/20`: `0.948289 / 0.913460`, `ρ/c_1 = 0.998168`; `t=30/20`:
`1.041232 / 1.020697`, `ρ/c_1 = 1.002381`; `t=32/20`: `1.214363 / 1.233717`;
`t=35/20`: `1.442574 / 1.546426`; `t=39/20`: `1.693528 / 1.931383`.

The note's D1 sub-numbers check: `0.9366` vs `0.9828` at `t = 8/5` ✓;
`1.6123` vs `1.5343` at `t = 39/20` ✓ (rounded; see finding 6).

The symmetry reduction I used for the scans (fixing the varied pair to one of
the two octahedral orbit representatives) was validated against the full
15-pair enumeration at `(32,20,20)`, `(39,20,20)`, `(29,20,20)`, `(30,30,20)`:
identical rationals.

### CK-06 / CK-08 — text

- All three fence sentences present verbatim (runner E1, and read directly).
- Forbidden phrases: 0 hits for `non-unique`, `several static laws`,
  `phase transition`, `the physical rule`, `certified`, `sharpest`.
- `Dobrushin`/`Shlosman` appear only at note lines 135 (Prior art) and 397
  (Imports); `Vaserstein` at 137 and 399. Rule satisfied.
- "we assume", "by construction", "as is standard", "naturally", "obviously",
  "canonical" occur exactly once each — all inside the N3 sentence that lists
  the scanned phrases, not as load-bearing text.
- Larger blocks are named "not attempted; obligation named" (N1 route 2), not
  claimed to fail. ✓ No sentence lets a reader infer uniqueness at the region
  triples: the region numbers are presented as an upper bound below 2, and the
  Boundaries section explicitly denies any `Z^3` uniqueness from M. ✓
- **`claim_scope` (YAML, line 5) is wider than what is proved**: it asserts
  "the block sum `B_V >= 10(rho + rho') > 2`". After the fix it should assert
  `B_V = 10 sup[TV(m_x)+TV(m_y)] > 2` (or, if the supervisor prefers not to
  adopt my equality proof, `B_V >= 10 sup[TV(m_x)+TV(m_y)] > 2`).
- Falsifiers (line 374) lists "`10(ρ + ρ') ≤ 2` at a silent triple" as a
  falsifier of the theorems. That test passes for the wrong reason and should
  be restated on the corrected quantity; the runner's C5 check has the same
  shape and would not have caught the error.

---

## 3. Findings, with severity

| # | note line(s) | what it says | correct statement | severity |
|---|---|---|---|---|
| F1 | 184–185 | "the supremum over pairs at a slot gives `b_V(z) ≥ ρ_z + ρ'_z`" | `b_V(z) ≥ sup_ω[TV(m_x)+TV(m_y)]`; `sup(f+g) ≤ sup f + sup g`, so the stated step is the wrong direction. In fact `b_V(z) = sup_ω[TV(m_x)+TV(m_y)]` exactly (proof in §2). | **blocker** |
| F2 | 5 (YAML), 48, 163, 193, 257–259, 351, 374 | `B_V ≥ 10(ρ+ρ') = 3.2457…, 2.4323…, 2.4470…` | `B_V = 3.1703426260…, 2.2445769309…, 2.3756972997…` (exact rationals `152203860/48008647`, `124859962305/55627392667`, `14627647143900/6157201570091`). All `> 2`, so the silence claim is intact. | **blocker** |
| F3 | 121, 387 | "`W_1` is not computed exactly … bounded, not computed" | `W_1(μ_V^ω,μ_V^{ω'}) = TV(m_x)+TV(m_y)` exactly for every `x`-slot change (proved §2; verified on 5,406 exact transport solves, 0 exceptions). `B_V` is exact, not an interval. | **major** (a correct-but-weaker claim that the block could simply have proved) |
| F4 | 351 (N7) | `10(ρ+ρ')/2 = 1.22, 1.22, 1.62` | wrong order for the note's own triple order, and the wrong quantity. Correct: `B_V/2 = 1.5851713130, 1.1222884655, 1.1878486498`. | **major** |
| F5 | 214, 229, 164 | Theorem M "iff `B_V < 2`" / "exactly when" | only "if" is proved: the relation is an upper bound on `E[U']`. | **moderate** |
| F6 | 257–262 vs 279 | `ρ/c_1` column truncated (`0.9992`, `0.9885`, `0.9618`), D1 rounded (`1.6123`) | one convention; rounded values are `0.9993`, `0.9804`, `1.0025`, `0.9868`, `0.9886`, `0.9619` (these match `GOAL_block04.md`, which the note currently contradicts). | cosmetic |
| F7 | 225 | "For sites `x` with `x ± e ∈ Λ`, `κ_x = 2`" | `κ_x = 2` iff `x − e ∈ Λ`. | cosmetic |

Nothing else I attacked broke. In particular Theorem N's *inequality* is
correct as stated and correctly proved (line 178–190) — only its "Consequently"
clause fails; Theorem O is correct and exhaustively executed; the `ρ`, `ρ'`,
`c_1` literals and both scans are exactly right; the maximizing instances are
right; the block law, the ten-slot boundary and the bipartite argument are
right.

---

## 4. Mutation runs (12, all four families)

Main run: `TOTAL: PASS=21 FAIL=0`, elapsed 59 s wall (58 s CPU). stdout
byte-identical to the pinned cache except one trailing newline.
`runner_sha256` recomputed = `8609e76702f123cf75f5f59615303fcc898b8285c62a3496619e5b5edc212089`
= the cache's value. (`input_fingerprint_sha256` is written by the audit
harness, not by the runner, so I could not reproduce it from the runner alone.)
`--list-mutations` returns the 16 declared mutations with their families.

| mutation | family | exit | check that failed | in family? |
|---|---|---|---|---|
| `block_law_factorization_broken` | B | 1 | B1 | ✓ |
| `coupling_marginals_broken` | B | 1 | B2 | ✓ |
| `lower_bound_lemma_forged` | B | 1 | B3 | ✓ |
| `sequential_upper_bound_forged` | B | 1 | B4 | ✓ |
| `rho_literal_off` | C | 1 | C2 | ✓ |
| `rho_prime_literal_off` | C | not run (budget) | — | — |
| `c1_literal_off` | C | 1 | C1 | ✓ |
| `ratio_bounded_by_one_claimed` | C | 1 | C3 | ✓ |
| `silent_lower_bound_below_two` | C | 1 | C5 | ✓ |
| `region_upper_bound_forged` | C | 1 | C6 | ✓ |
| `crossing_cell_wrong` | D | 1 | D1 | ✓ |
| `ratio_beyond_one_denied` | D | 1 | D2 | ✓ |
| `claim_nonunique_at_silent` | E | 1 | E2 (`hits: ['non-unique']`) | ✓ |

Every mutation run produced exactly one FAIL (`PASS=20 FAIL=1`) in its declared
family. E4 (the float self-scan) passes: 0 floating-point literals or
conversion calls in the runner source.

**Runner blind spot worth naming.** C5 checks `10(rho + rho') > 2`, i.e. it
tests the note's *stated* number rather than a `W_1` bound, so it cannot detect
F1/F2. No check in the runner computes `sup[TV(m_x)+TV(m_y)]` or any `W_1`. A
check that recomputes `sup_ω[TV(m_x)+TV(m_y)]` (cheap — 476,280 instances,
about 25 s per triple) would close it.

---

## 5. My scripts, and my own failures

All under
`/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-sync-science-task-0c8fac/3a5217b4-5b36-4906-8abe-d27fc3312603/scratchpad/checker04/`:

- `ck_core.py` — φ table, block law, marginals, exact TV on integer weight
  vectors, `c_1`, `ρ`/`ρ'` enumeration, maximal coupling, and an exact integer
  min-cost-flow transportation solver (`mincost_flow`, `w1_exact`). Written
  from the definitions; the runner is never imported.
- `ck_run1.py` → `ck_run1.out` — CK-01, CK-02, the independent `∂y`-slot
  symmetry check.
- `ck_run2.py` → `ck_run2.out` — CK-03 exact `W_1` on the named instances plus
  900 random ones.
- `ck_run3.py` → `ck_run3.out` — CK-05 both line scans + the symmetry-reduction
  validation.
- `ck_run4.py` → `ck_run4.out` — the `sup[TV(m_x)+TV(m_y)]` counter-computation
  and a wider `W_1 =` lower-bound test (3,600 instances).
- `ck_run5.py` → `ck_run5.out` — exact `sup_ω[sequential E d_H]` over the full
  instance space (the coupling-independent contradiction of F2).
- `runner_main.out`, `mut_*.out`, `mutlist.txt`, `cache_stdout.txt` — CK-07.

**My own failures, recorded:**

1. I shipped a wrong `ck_run5.py` on the first run: `TV` computed as `R/(2D)`
   instead of `R/D` (I double-counted the factor 2 already absorbed by summing
   only the positive part of the difference). It produced `sup seq = 0.1887` at
   `(3,1,2)`, which is *below* an instance value I had already computed
   (`0.3130`) — an internal contradiction I caught only because I had that
   cross-check in hand. Fixed (`tv = Fraction(R, D)`) and re-run; the corrected
   numbers are in §2.
2. I left a dead placeholder line in `ck_core.sequential_coupling_cost` in the
   first draft (a `maximal_coupling` call whose result was discarded); removed
   before use. `ck_run2.py`/`ck_run5.py` use their own `seq_cost`/`sup_seq`.
3. My first attempt to run the checker scripts used `timeout`, which is absent
   on this macOS host; the run aborted with exit 1 and cost one round trip.
4. I drafted this file before `ck_run5.py` finished `(7,3,5)` and shipped a
   placeholder row for it; the run then landed
   (`155739611010/637009609081 = 0.2444854972 < 0.2447066611`) and the row is
   now real. Flagging it because a reader of the first draft would have seen a
   gap where there is none.
5. `W_1 = TV(m_x) + TV(m_y)` is proved above for `x`-slot changes; I verified
   it numerically on 5,406 instances but did **not** verify the mirrored
   statement for `y`-slot changes by transport (only by the block's `x↔y`
   symmetry, which is exact).
