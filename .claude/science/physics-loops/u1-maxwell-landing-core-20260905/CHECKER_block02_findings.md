# CHECKER block 02 — independent refuting check of the dynamics-class adjudication

**Verdict: FIX FIRST**

The mathematics survives a from-scratch attack. I rebuilt the compilation with my
own sign conventions, re-derived the spectra by a different route, brute-forced the
classification without assuming any character theory, solved the nullspace theorem
in a strictly more general form than the primary does, and re-verified all ten
witnesses. Eighty independent checks, zero mathematical failures: **no verdict in
the seven-row table is refuted.** Three mutations planted in the primary's runner
were all caught.

What must be fixed before landing: two quotations attributed to open PRs are not in
those PRs (CK-01, CK-02); one classification sentence is an incomplete enumeration
and, read literally, trips the note's own falsifier list (CK-03); and the note's
falsifier claim that every witness property "is checked exactly" is false — three
witness properties are asserted in runner check labels but never tested (CK-04).

Object under attack: `docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md`
(770 lines, read complete), `scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py`
(1,148 lines, read complete), `logs/runner-cache/u1_dynamics_class_axiom_adjudication_2026_09_05.txt`,
`GOAL_block02.md`.

Framework refresher read first, complete: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233
lines — four axioms Lattice/Qubit/Admissibility/Record, the Qualification, the
"Admissibility is not a dynamics axiom" boundary, the open-gates list, and the
2026-08-13 Record revision paragraph); `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`;
`docs/audit/data/axiom_premise_nodes.json` (four canonical nodes: `minimal_axioms`,
`scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`).
The note's primitive-registry paragraph is accurate: none of the three primitives is
classified as a wall, an import, or a source of bounded status, and none supplies an item.

Disjoint machinery: `/private/tmp/claude-502/b02check/` (`indep.py`, `classify.py`,
`classify2.py`, `classify3.py`, `witness.py`, `logic.py`, `mut/m1..m3.py`). Nothing
from the primary's runner is imported. My `d0` carries the opposite sign convention;
my curl signs are derived from a Levi-Civita symbol (`C[f,e] = s * eps(k,m,a)`)
rather than a hand table; multiplicities come from an exact Fourier
block-diagonalisation over the coarse momenta, cross-checked against numpy
eigenvalues and an exact rational rank.

---

## CK-01 — material — a quotation attributed to PR #7917 is not in PR #7917

**Attacked sentence** (note, section 1, line 100): Its own boundary: "The
classification does not derive that dynamics class from the axioms" — and the same
string in the machine block, `target_blocker_text` (line 76), and in
`GOAL_block02.md` V1, which calls it a "quote at scope".

**Evidence.** I fetched the live PR body (`gh pr view 7917 --json body`) and the
full note on its head branch
(`docs/U1_MINIMAL_PHYSICAL_NEIGHBOR_CONSERVATIVE_GAUGE_DYNAMICS_UNIQUELY_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-03.md`,
538 lines) and searched both with whitespace normalised. The string does not occur;
the substring "does not derive" does not occur anywhere in that PR at all. The PR's
actual boundary sentences are:

- "That is a conditional selection theorem, not an axiom derivation." (line 342)
- "The four axioms do not currently select that class. In particular, they do not
  state real linear first-order evolution, energy conservation, minimal `(E,B)`
  payload, or continuous time." (lines 66-68) — this second one **is** quoted
  verbatim by the note and is correct.

A repo-wide search shows where the string does come from: the campaign's own
science-record summary
(`.claude/science/physics-loops/u1-maxwell-landing-core-20260905/inputs/light_lane_science_records.json`
and `archive/campaigns/pr-densify-wave2-20260905/all_verdicts.json`), i.e. a
machine-written précis of the PR, not the PR. The YAML's
`source_of_blocker_text: frontier_question` is also not right for that provenance.

This matters because the note's stated contract forbids treating the PRs as
authority and requires quoting them "at their own scope"; presenting a précis in
quotation marks as the PR's own words is exactly the failure mode that rule exists
to prevent. The note's substance is unaffected — the PR does concede the point.

**Narrowest fix.** Replace the quoted string in section 1 with one of the two real
sentences above (the second is already quoted, so the first suffices), and set the
machine block's `target_blocker_text` provenance honestly (it is a lane
science-record summary, not a PR quote and not a frontier question). Same string in
`LANDING_CORE.md` line 205 and `docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md`
line 253 — outside this block's file set, flagged for the supervisor.

## CK-02 — material — a quotation attributed to PR #7913 is not in PR #7913

**Attacked sentence** (note, section 1, line 118): This is the doubled incidence
declared in the open PR `#7913` ("exactly eight translated parity-role sectors on
even tori").

**Evidence.** Fetched
`docs/U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md`
on PR #7913's head branch. The phrase is absent (whitespace-normalised search). The
closest real text is line 134: "On an even periodic torus the result closes around
every cycle, giving exactly eight sectors." The words "translated" and "parity-role"
are the note's, not the source's.

**Narrowest fix.** Either quote the real sentence or drop the quotation marks and
paraphrase without them.

## CK-03 — material — "every such transformation law is induced from a character of the site stabilizer" is incomplete on the supplied payload; I exhibit a counterexample

**Attacked sentences** (note, section 3, lines 212-216): "Every such transformation
law is induced from a character of the site stabilizer (a `D_4` of proper rotations
about the site, all named by the Lattice axiom) ... This gives sixteen laws." And
the `claim_scope`: "under all sixteen signed-permutation representations".

**What I confirmed first.** Brute-force enumeration, no character theory assumed
(`classify.py`): the sector-preserving group on the side-4 torus has order 192
(8 even translations x 24 proper rotations); it is transitive on the 24 edge sites
and on the 24 face sites; each site stabiliser has order 8; `Hom(stabiliser, {+-1})`
has exactly 4 elements in each case, and the four induced reps are pairwise distinct.
So **sixteen isomorphism classes is right**, and in the compilation's own sign basis
the tensor-transport realisation reproduces every downstream claim exactly
(`classify3.py`): dimension 4 for the eight laws whose vector/scalar bits agree and 2
otherwise; exactly 8 coupling-admitting laws; exactly **4 distinct couplings — no
fifth**; the four one-face stencils are exactly
`{(1,1,-1,-1), (1,1,1,1), (1,-1,-1,1), (1,-1,1,-1)}`, each shared by a parity-twist
pair; exactly the vector/vector law and its parity twist are gauge- and
chain-compatible, with the oriented curl as their coupling. The existence rule is
confirmed to be `alpha_E == alpha_B`, and the note's gloss is accurate: on the
in-plane 180-degree flip the edge-along-`j` character value is `(-1)^alpha_E` and the
face value is `(-1)^alpha_B`. The hand stencil map is confirmed by hand and by
nullspace: the only vector fixed by `(a,b,c,d) -> (-d,a,-b,c)` is a multiple of
`(1,1,-1,-1)`.

**The break.** "Induced from a character" classifies laws **up to isomorphism** — up
to a diagonal sign change of basis. On the *supplied* payload (a fixed real number at
each site, with the compilation's fixed `d_0`, `d_2`), there are strictly more than
sixteen signed-permutation laws with the same site action. Concretely (`logic.py`
section 8c), let `D` negate the payload at every `z`-normal face site and set
`rho' = D rho_(vector,vector) D`. Then `rho'` is verified to be

- a genuine group representation with the same site action, and a signed permutation
  on every generator (24 rotations + 26 even translations);
- **not equal to any of the sixteen** tensor-transport laws (checked against all 16);
- its unique covariant nearest-neighbour coupling is `D C`, which satisfies
  `D C d_0 = 0` but `d_2 (D C) != 0`.

So under `rho'` the generator `[[0, -(DC)^T],[DC, 0]]` keeps items 1, 3, 4, 7 and
**fails item 5** — which is precisely a "fifth transformation law of a real
one-component payload by site permutation" in the sense of the note's own falsifier
list (section 13, first bullet).

**Why the verdicts nevertheless stand.** Section 4's nullspace theorem is
representation-free: any nearest-neighbour face row with `L d_0 = 0` and `d_2 L = 0`
is a lattice-wide multiple of the curl (I re-proved this in full generality, below).
That already delivers "only the curl is gauge- and chain-compatible" without any
enumeration of transformation laws. And OL as the note *defines* it pins the sign
basis — "the same convention the compilation uses for its oriented link value" — so
`rho'` is excluded by OL. The defect is in the stated mechanism and its scope, not in
the conclusion.

**Narrowest fix.** Two clauses. (1) In section 3 write "up to a diagonal sign
relabelling of the payload, every such law is induced from a character ...; the
compilation's own sign basis is part of the supply, and OL names it", and mirror that
in `claim_scope`. (2) Add one sentence saying the item-5 conclusion does not depend on
the enumeration at all, because section 4's nullspace theorem is representation-free
— that also removes the falsifier-list exposure. Optionally add the `D`-twist as the
explicit witness that OL's convention clause is load-bearing rather than decorative
(at present the note's only OL witness is the unoriented law `S`, which is a
*different* character, not a sign twist, and so does not exhibit this failure mode).

## CK-04 — material — "each is checked exactly" is false: three witness properties are asserted in check labels but never tested

**Attacked sentence** (note, section 13, sixth falsifier bullet): "a witness law that
fails one of the items it is claimed to keep (each is checked exactly)".

**Evidence.** Three runner checks assert properties in the label that the boolean
predicate does not evaluate:

- line 1127-1128, complex law: the label says "real-linear, nearest-neighbor,
  gauge-compatible"; the predicate is `dot_q(...) == 0 and theta != 0` — conservation
  only (and `theta != 0` is a constant).
- line 1115-1116, nonlinear law: the label says "nearest-neighbor and
  gauge-compatible"; the predicate is `dE2 != [2*x for x in dE]` — non-homogeneity
  only. The note (section 6) additionally claims the nonlinear law "is nearest-neighbor,
  covariant and gauge-compatible"; covariance is nowhere tested.
- the finite tick: the note (section 6) claims "each shear reads one site and four
  opposite-role neighbors" and that the tick carries "items 1, 3, 4, 5, 7", i.e.
  covariance; the runner checks reversibility, the Gauss rows, the modified energy and
  the not-`exp(hG)` fact, and neither the shear support radius nor covariance.

**I verified all three independently and they are all true** (`witness.py`): the
complex law's real generator on side 6 (324 = 2 x 162 real components) is exactly
antisymmetric, has support radius exactly 1, is covariant under all 24 rotations in
the doubled oriented representation, and its edge-to-face block is exactly `C`; the nonlinear law's
edge-to-face map is exactly `C`; the tick's shear operator has radius 1 and is
covariant. So this is a coverage-and-wording defect, not a false claim about the
physics — but the falsifier bullet as written is not true of the shipped runner.

**Narrowest fix.** Either add the three assertions to the runner's predicates (each
is a one-line addition using existing helpers `support_radius`, `is_covariant`, and
the `d0`/`d2` products), or soften the falsifier parenthetical. Adding the checks is
better: it is the falsifier that most directly protects the ten witnesses.

## CK-05 — material — item 4's "with no orientation premise at all" is representation-relative

**Attacked sentences** (note, results table row 4 and section 4): "DERIVED-CONDITIONAL-ON(items
1, 3, 5, 6, 7) with no orientation premise" and "the result is covariant".

**Evidence.** Covariance is not a property of a matrix; it is a property of a matrix
*relative to a representation*. I tested the derived generator `c[[0,-C^T],[C,0]]`
against all sixteen laws: it is covariant under exactly
`[((1,0),(1,0)), ((1,1),(1,1))]` — the vector/vector law and its parity twist — and
under no other (my `classify3.py` shows the scalar/scalar covariant space is
`span{onsite, onsite, S, S^T}`, which does not contain the curl, and the eight mixed
laws admit onsite terms only). The primary's own runner makes the same move: the
check at line 1001-1002 that "item 4 is implied by the other items" evaluates
`is_covariant(maxwell, p)` against `perm6 = field_rotation(comp6, rot, ORIENTED, ORIENTED)`
— i.e. it verifies item 4 *using the orientation law*.

The note is aware of this and says so in section 4 ("the oriented structure enters
through `d_0` and `d_2` inside item 5 itself"), which makes the claim defensible under
an existential reading ("there is a transformation law under which the derived
generator is covariant"). But that reading is never stated, and "with no orientation
premise at all" is repeated three times (results table, section 4 verdict, section 9
table) in a stronger-sounding form.

**Narrowest fix.** One clause in the results table and section 9: "…with no
orientation premise beyond the oriented `d_0`/`d_2` that item 5 itself names; the
covariance is exhibited for the oriented representation."

## CK-06 — minor — R1's reversibility parenthetical is not executed, and is false for the sweep

**Attacked sentence** (note, N1 route R1): "reversibility is not conservation: the
harmonic sampler is reversible with respect to its measure while its conditional-mean
map strictly decreases the energy (runner section G)".

**Evidence.** Runner section G tests exactly two things: that one Gauss-Seidel sweep
of single-site conditional *means* strictly decreases `(1/2) A^T C^T C A` (I
reproduce: `1292.4756 -> 132.3083` on my own random rational field), and that the
collapsed edge-only map has radius 2 with `diag(Q) = 4`. It never tests reversibility
of any sampler. Moreover, a *single-site* Gibbs update is reversible with respect to
`pi`, but the systematic-scan sweep that section G actually forms is a composition of
such updates and is **not** reversible with respect to `pi` in general. As written the
sentence attaches a property of the single-site kernel to "the harmonic sampler" and
cites a section that establishes neither.

**Narrowest fix.** "each single-site conditional update is reversible with respect to
`pi`, while the sweep of conditional means strictly decreases the energy (runner
section G)" — and drop the section-G citation from the reversibility half.

## CK-07 — minor — one runner PASS is a tautology

**Attacked line** (runner 1133-1134, section M): the predicate is
`real_dim_m2c == 8 and max(1, 1, 2, 1) <= 8 and 9 > real_dim_m2c` where
`real_dim_m2c = 2*2*2` is a literal three lines above. Nothing about the compilation,
the payloads, or any witness is evaluated; the check cannot fail for any input. It
contributes 1 of the 95 PASSes. The `and theta != 0` conjunct in the complex-law check
is the same pattern.

**Narrowest fix.** Either derive the witness component counts from the constructed
generators (e.g. assert the complex generator's dimension is `2*(ne+nf)` and the
vertex law's is `nv+ne+nf`) or drop the check and restate the count as 94.

## CK-08 — minor — the side-6 nullspace theorem is proved in reduced form only, though the full form holds

**Attacked scope** (note, section 4: "side 6 after the per-face reduction"; runner
lines 988-1000, which solve only the 81 face-coefficients `q_f` *after assuming* each
face row is a multiple of its own curl).

**Evidence.** I solved the side-6 system in full generality — all 324 free
coefficients (81 faces x 4 boundary edges), imposing `L d_0 = 0` and `d_2 L = 0` with
no per-face reduction — and the nullspace is exactly **1-dimensional and spanned by
the oriented curl** (`classify3.py`). Side 4 in full generality (96 unknowns)
reproduces the primary's result. So the note is entitled to the stronger, unreduced
statement at side 6 and currently under-claims.

**Narrowest fix.** Extend the runner's `system4` construction to side 6 (it is the
same code with `comp6`) and drop "after the per-face reduction" from section 4.

---

## Attacks that FAILED to break the note (recorded as defended)

These are the places I expected to find a hole and did not.

1. **Compilation rebuild.** With my own `d_0` sign and Levi-Civita-derived curl
   signs, on sides 4, 6, 8: the role census (`n^3/8`, `3n^3/8`, `3n^3/8`, `n^3/8`),
   the shell census, the absence of any same-role nearest-neighbour pair, the parity
   theorem (edge-face distances all odd, same-role all even), `C d_0 = 0`,
   `d_2 C = 0`, `(+1,+1,-1,-1)` in every curl row and column, and every curl entry a
   physical nearest-neighbour pair — all reproduce exactly.
2. **Multiplicities by a different route.** Exact Fourier block-diagonalisation over
   the 27 coarse momenta of the side-6 torus: the curl symbol is
   `-[d]_x` with `d_a = 1 - e^{i k_a}`, so `Chat^† Chat = |d|^2 I - d d^†` with
   eigenvalues `{0, |d|^2, |d|^2}` and `|d|^2 = 3 x (number of nonzero coarse
   components)`. This gives `{0:29, 3:12, 6:24, 9:16}` — matching the note — and the
   Hodge symbol is `|d|^2 I`, giving `{0:3, 3:18, 6:36, 9:24}`. Confirmed again by
   numpy eigenvalues and by exact rational rank. `29 = 26 + 3` and `52 = 2 x 26` check.
3. **No fifth coupling.** In the compilation's sign basis, over the full 240-coefficient
   per-site nearest-neighbour generator space on side 4 (no translation-covariant
   pattern basis assumed), all 16 laws give exactly 4 distinct couplings and every
   coupling direction is rank 1.
4. **The nullspace theorem, strengthened.** Full generality at side 4 (96 unknowns)
   *and* side 6 (324 unknowns): dimension exactly 1, spanned by the curl.
5. **The item-5 constraint-surface attack failed.** I asked whether "preserves the
   magnetic Gauss row" needs `d_2 L = 0` exactly or only invariance of the constraint
   surface. Imposing only `d_2 L v = 0` for `v` in `ker(d_0^T)` (dimension 17 of 24 at
   side 4) gives the **same** one-dimensional space — because `L d_0 = 0` already
   kills `L` on `im(d_0)`, and `im(d_0) + ker(d_0^T)` is everything. The weaker
   reading is equivalent here. The note is safe and could say so.
6. **The item-4 chain is complete.** Given items 1, 3, 5, 7 (face rows `= q C`), I
   solved the conservation system over 145 unknowns (`q`, 24 free edge onsite
   coefficients, 96 free edge-from-face coefficients, 24 free face onsite
   coefficients) for three different positive weight pairs `(w_E, w_B) = (1,1),
   (2,3), (1/5, 7)`. In every case the solution space is exactly 1-dimensional, **all**
   onsite terms are forced to zero, and the reverse block is forced to
   `-(w_B/w_E) q C^T`. Item 6 does do the work the note assigns it.
7. **All ten witnesses hold every property claimed.** damped (radius 1, covariant
   under 24 rotations and 26 even translations, gauge/chain-compatible face block,
   trace `-54`); overdamped (trace `-162`, per-mode polynomial
   `lambda^2 + gamma lambda + gamma s^2`, own series gives slow root
   `-s^2 - s^4/gamma + O(s^6)`); same-sign (exactly symmetric, real eigenvalue `3 > 0`,
   trace 0); unoriented `S` (conservative, covariant under the scalar law, *not*
   covariant under the oriented law, `S d_0 != 0`, `d_2 S != 0`, rank-3 image of the
   three constant edge fields while the curl annihilates them); anisotropic `(1,2,3)`
   (radius 1, conservative, `L d_0 = 0`, not covariant, `d_2 L != 0`);
   site-privileging (conservative, radius 1, gauge-compatible, not translation
   covariant); improved curl at side 8 (exactly antisymmetric, `L d_0 = 0`,
   `d_2 L = 0`, covariant, radius exactly 3); vertex scalar (`dH/dt = 0`, covariant,
   and **every** coupling at physical distance 1 — a vertex's six neighbours really
   are its six edges, so the note's "nearest-neighbour" claim for it is correct — plus
   the Hodge multiplicities and the two-speed member); finite tick; nonlinear;
   complex.
8. **The "no positive form of any kind" claims are sound.** For the damped and
   overdamped witnesses the argument is trace-based: `M G + G^T M = 0` with `M > 0`
   forces `G` similar to `-G^T`, hence `tr G = 0`; traces are `-54` and `-162`. For the
   same-sign witness `G` is *exactly* symmetric (I checked entrywise, not via an
   eigensolver) with a real eigenvalue `3 > 0`, and a real growing eigenvector forbids
   any conserved positive form. Note the primary's runner only samples nine diagonal
   weight pairs for this; the note's prose arguments are stronger than the runner's
   predicate, and correct.
9. **The leapfrog invariant, rederived by hand.** With `alpha = 1 - h^2 s^2/2`,
   `beta = h s`, `gamma = 1 - h^2 s^2/4`, the kick-drift-kick map is
   `E1 = alpha E0 - beta B0`, `B2 = alpha B0 + beta gamma E0`, and the cross terms in
   `B2^2/2 + gamma E1^2/2` cancel identically while
   `alpha^2 + gamma beta^2 = 1 - t + t^2/4 + t - t^2/4 = 1` with `t = h^2 s^2`. So
   `H_h = |B|^2/2 + |E|^2/2 - (h^2/8)|C E|^2` is exact — and the coefficient is
   uniquely `1/8`: I checked `1/6` and `1/10` both fail. Positivity holds since
   `max spec(C^T C) = 9 < 4/h^2 = 16` at `h = 1/2`. The nonlinear law's quartic energy
   is exactly conserved.
10. **Radius-3 scope is exact.** `C C^T C` satisfies both chain constraints, has
    support radius exactly 3, and is not a multiple of `C` — so the gauge-plus-chain
    space genuinely grows the moment radius 3 is allowed, and the note's
    nearest-neighbour scope statement is tight. No edge sits at physical distance 2
    from a face, so "radius one or at least three" is exact.
11. **Sourced facts.** The 14 axiom sentences the runner needles are verbatim in the
    memo, including the 2026-08-13 revision sentence, and I checked every
    double-quoted span in the note that is attributed to the memo or to a primitive
    note — all resolve (the one ellipsis, in the "choose a Hamiltonian or transfer
    operator ... define a time metric" quote, is honest). The PR #7886 quote "The
    factorized transfer interpretation is an explicit premise" is verbatim on that
    PR's head branch. The N4/N6/N8 claim types and statuses all match the ledger
    shards: `dynamics_nontriviality_selection_firewall_2026-06-06` = `no_go`/`unaudited`;
    `record_classical_semigroup_boundary_2026-06-06` = `bounded_theorem`/`unaudited`;
    `dynamics_form_from_record_preservation_..._2026-06-05` = `bounded_theorem`/`unaudited`;
    `single_clock_axis_selection_..._2026-06-11` = `no_go`/`unaudited`;
    `index_pairing_not_forced_..._2026-06-08` = `no_go`/`unaudited`;
    `dynamics_axiom_minimal_nontriviality_branch_proposal_2026-06-29` = `meta`.
    The note carries exactly three markdown links — the landed axiom memo and its own
    co-landing runner and receipt. **No link points at an unlanded surface**; every
    open PR is referenced as a backticked id only.
12. **No circularity in the verdict table.** Items 4 and 5 are marked
    DERIVED-CONDITIONAL-ON sibling items, never DERIVED, and the note states plainly
    that they are mutually redundant so that only one of the two may be dropped
    (section 10, N2 last row). That is an internal-redundancy statement, not a
    derivation from the class, so the GOAL's circularity bar is not tripped.
13. **N1-N8 negative-claim discipline holds.** Every negative is scoped to "not forced
    by the four axiom sentences plus the supplied compilation, on the finite compiled
    tori and by the stated size-free arguments". N7 explicitly refuses the broader "no
    route" claim and names the live reflection-positivity route, and the gate result
    says the note does not ship any "no route exists" or "a new axiom is required"
    claim. I found no hidden "no route" sentence. CK-06 is the only N1-N8 wording
    defect.
14. **The 2026-08-13 paragraph is read faithfully.** The memo removes `I`, finite
    additivity and `I(empty)=0` from Record, and separately says rows requiring those
    structures "must likewise cite a separate retained authority or remain
    conditional/open". The note's reading — no additive scalar of any kind in current
    Record; a supplied additive scalar is not forbidden as downstream structure; the
    revision is silent on conservation, which is dynamical — matches both passages.
    Its "item 6 needs three things" decomposition is sound.

---

## Mutation-probe table

Three defects planted in scratch copies of the primary runner
(`/private/tmp/claude-502/b02check/mut/`, `ROOT` repointed at the worktree; the repo
copy was not touched). All three caught; every mutant exits 1.

| mutation | caught? | by which check |
|---|---|---|
| M1: `face_stencil` sign flipped for the `z`-normal orientation only (`(shift(x,i,1), 1)` -> `-1` when `k == 2`) | **yes** — `PASS=65 FAIL=30` | first at section C, "side 4: C d0 = 0 and d2 C = 0 over the integers" and "every face row and every edge column ... has entries (+1,+1,-1,-1)"; then cascades through the covariant classification (E), the Gauss rows and the `Q(Q-3)(Q-6)(Q-9)` spectrum (F), and the vertex-payload dimension count |
| M2: `is_covariant` returns `True` unconditionally for sign-free permutations, i.e. for every translation | **yes** — `PASS=94 FAIL=1` | section I only, "site-privileging law (one face row doubled): ... but NOT translation covariant". Note this is the sole check that notices; the positive-direction translation-covariance conjunct at line 1002 goes vacuous without complaint. Thin but fail-closed. |
| M3: modified-energy coefficient `h^2/8` -> `h^2/6` | **yes** — `PASS=94 FAIL=1` | section L, "finite tick: conserves the modified energy `H_h = |B|^2/2 + |E|^2/2 - (h^2/8)|C E|^2` exactly" |

---

## Recommended disposition

Land after CK-01 through CK-05 are applied. CK-01 and CK-02 are two-line edits.
CK-03 is two clauses plus (optionally) one extra witness. CK-04 is three one-line
runner predicates. CK-05 is one clause. CK-06 to CK-08 are cosmetic or
strengthening and can ride along. The seven-row verdict table, the mutual
redundancy of items 4 and 5, the five-wall collapse, and every existence witness
survive the attack unchanged.
