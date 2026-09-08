# CHECKER — BLOCK 01, refuting check of the U(1)/Maxwell landing core

**Date:** 2026-09-05
**Seat:** independent refuting checker (read-only; no git action taken; this is
the only file written).

**Framework refresher completed first, as required.** I read
`docs/MINIMAL_AXIOMS_2026-06-29.md` COMPLETELY (all 233 lines: the four named
axioms Lattice / Qubit / Admissibility / Record with the Admissibility reading
notes 1-3, the Qualification, Audit-Pipeline Treatment, Relation To Dynamics And
Kinetic Branch Selection, Relation To The Older Observable-Principle Parent,
Relation To The 2026-06-05 Record Wording, Open Gates Outside The Axioms, and the
2026-07-04 / 2026-08-05 / 2026-08-13 revision paragraphs in Historical Context).
I read `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` COMPLETELY (all
130 lines, including the generated baseline for the three approved primitives
`scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`).

**Ground truth read completely:** all 29 records in
`inputs/light_lane_science_records.json` and all eleven `inputs/PR*.md` files
(twelve member notes — #7952 has two). Comparator read: `BLIND_supplied_input_ledger_opus.md`
(used as comparator, not authority) and `REVIEW_HISTORY.md`.

**Method.** Every double-quoted attributed span in the three deliverables was
matched against its member source (203 spans: 137 in the meta note, 66 in the
ledger; the LANDING_CORE's 126 are a near-superset of the meta note's). Every
unquoted attributed restatement in the 90 member bullets was checked, and all 29
record `science` fields were diffed sentence-by-sentence against both prose
deliverables programmatically to catch dropped hypotheses.

---

## BLOCKER

### CH-01 — `#7945` is credited with a number it does not report (Check B)

- **file:line** `docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md:410-411`;
  identical text at `.claude/science/physics-loops/u1-maxwell-landing-core-20260905/LANDING_CORE.md:372-373`.
- **Primary's text:** "Both #7959 and #7945 report / 9,600 Gauss/ice states at
  `L = 2` and an 864-state zero-flux mobile component; / by their displayed
  formulas they are the same carrier at different values of / the supplied
  coupling (synthesis reading)".
- **Member's text:** `#7945` contains no occurrence of "9,600" or "9600"
  anywhere (verified by grep over
  `inputs/PR7945__SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md`:
  0 hits). Its single relevant sentence is line 188: "At `L=2`, the zero-flux
  mobile orbit has `864` configurations." The `9,600` figure at `L=2` belongs to
  `#7959` ("the `2x2x2` Gauss sector has dimension `9600`", note lines 5, 119,
  261) and to `#7937` ("exhausts all 9,600 L=2 ice states", record for PR 7937).
- **Why this is a blocker, not a slip.** The sentence is the sole factual
  evidence the note offers for the same-carrier identification, which is the
  hinge of the lane's declared open item (§6/§6.C). The note labels the
  *identification* a synthesis reading but presents its *premise* as a joint
  member report — so the honest label is undercut by a fabricated attribution.
  The note itself quotes the correct source three paragraphs later
  (meta:433 "#7937 ... exhausts all 9,600 L=2 ice states"), so the correct
  attribution was in hand.
- **Adjudication of Check B, exactly.** The identification of `#7959`'s and
  `#7945`'s carriers is *supportable but is a synthesis reading stated by no
  member*: it rests on (a) `#7945:188` "the zero-flux mobile orbit has `864`
  configurations" against `#7959:121` "the zero-winding class is `880 = 864 +
  16`: one flip component -- the ice configuration's, with `G_v = 0`"; (b)
  `#7945:107` "Inside one fixed three-of-six Gauss sector" against `#7959:5`
  "the fully periodic 2x2x2 torus (24 links, 8 vertices at z_v = 6 ... rho_v =
  0)"; and (c) the displayed Hamiltonians `#7959:99` `H = -lambda sum_f P_f`
  and `#7945:111-113` `H(V) = -sum_p(...) + V N_f`. Neither member states the
  identification. The primary's attribution **as written is not honest**: only
  the `864` is a joint report; the `9,600` is not `#7945`'s.
- **Fix:** "`#7959` reports 9,600 Gauss/ice states at `L = 2` (`#7937` reports
  the same count for the ice sector); `#7959` and `#7945` both report an
  864-state zero-flux / zero-winding component at `L = 2`."
- **Severity: blocker.**

---

## MATERIAL

### CH-02 — the meta note computes, after declaring that it does not

- **file:line** `META:14-15` against `META:631-632` (same defect at
  `LANDING_CORE:594`).
- **Primary's text:** "**Runner:** none. Nothing is computed here; every number
  below is quoted from / a member note or record." Then: "the later members'
  static target `U K = 0.012289` is (by this / note's arithmetic) the product of
  the static parents' `U(0.95) = 0.162638`, / as quoted in #7945, with #7946's
  relaxed `K`".
- **Member's text:** the product (0.162638 x 0.075561 = 0.0122891) is stated by
  no member. `#7952` (late-time) and `#7963` quote `U K` as an imported target
  (`#7952:53`, `#7963:118` "It is not copied from the spectral fit"); neither
  factorizes it.
- The arithmetic is disclosed and is correct, but the header assertion is
  falsified by the body. Fix the header ("no runner; the only arithmetic is the
  one product marked in §6.C") or drop the product.
- **Severity: material.**

### CH-03 — a synthesis inference presented as a member-imposed narrowing

- **file:line** `META:627-634` (`LANDING_CORE:589-596`).
- **Primary's text:** "Three further narrowings the members impose on each
  other, each at scope. / (1) ... so #7945's 36% and 61% figures / are measured
  against a magnetic number the lane's later members replaced."
- **Member's text:** `#7946`'s record says only "It distinguishes the relaxed
  curvature from the older 0.2598 variational upper cost". No member says the
  0.2598 was *replaced*, and no member states the `U = 0.162638`, `K = 0.075561`
  factorization of `U K`. The note's own rule (`META:26-27`) is: "Where this note
  adds a reading of its own it is marked 'synthesis reading'; every other
  sentence about a member is a quote or a restatement at that member's own
  scope." Item (1) is a reading, unmarked, and is filed under a heading that
  says the members impose it. (The blind seat's C03 reaches the same reading
  independently, so the reading is not wrong — the *label* is.)
- The same unmarked-reading defect applies to the F-B1 conclusion at
  `META:225-229` ("So at #7886's and #7887's scope, the positive spatial
  (magnetic) curvature ... is a supplied orientation completion") and to
  narrowings (2) and (3) at `META:635-648`. F-B1's reading is correct and
  well-evidenced (`#7886:60-62`, `:237`; `#7887` record; `#7915:59`, `:570`);
  only the labelling is at fault.
- **Fix:** mark (1)-(3) and the F-B1 conclusion "synthesis reading", or rename
  the heading.
- **Severity: material.**

### CH-04 — ledger row 4 / D2: the Gauss-as-support lever, adjudicated

The primary flagged D2 for a refuting check. **Partly refuted; the derivability
rating must come down.**

- **file:line** `SUPPLIED_INPUT_LEDGER.md:228-237` (row detail), `:40` (summary
  table, "partial, high"), `:440-444` (D2), `:474` ("Row 4 ... is the natural
  block 03").
- **Primary's text:** "*Partial, high.* ... On the role-compiled lattice a
  vertex-role site's six physical nearest neighbors are its six edge-role sites,
  so *the admissible vertex possibilities are those compatible with the six
  neighboring link records* is exactly the shape of the Admissibility sentence
  ... **#7893 already words Gauss's law that way.**"
- **Member's text:** `#7893` (record): "Gauss operators that commute with the
  coupled law and are implemented as order-independent **site-level support
  forcing among corner records**."
- **Three refutations.**
  1. **Direction.** `#7893` forces the support *among the corner (link)
     records*, indexed by site. The primary restricts *the vertex site's own
     possibility menu*. These are different objects, and the claim "#7893
     already words Gauss's law that way" is not supported by `#7893`'s text.
  2. **The vertex carries nothing.** In every member that uses this constraint
     the vertex-role site has no dynamical payload — `#7959:97` "`rho_v` = a
     STATIC background charge (no matter, so no `n_v`)", `#7959:100` "`rho_v = 0`
     on every torus"; `#7917` item 7 "no vertex, cube, extra coin, or hidden
     time payload participates". Admissibility shapes the distribution over a
     site's *own* possibilities; applied at an empty vertex it forbids no edge
     configuration. Read the other way — the vertex record equals `div E` — the
     rule becomes a determinate map that admits every edge configuration, and
     Gauss's law reappears only once the background `rho_v = 0` is supplied,
     which the row concedes is supplied.
  3. **The shape match is content-free and inherits a tier-A supply.** What the
     axiom sentence gives is "support at a site determined by nearest-neighbor
     conditions" — satisfied by *any* nearest-neighbor rule. None of the Gauss
     content (which signed combination, the background) follows, as the row
     itself says. The lever is also conditional on the role compilation, which
     this ledger's own row 3 rates tier-A **genuine supply**; the row does not
     record that inheritance, whereas the blind ledger's R13 does ("partly
     derivable in form; supplied in application; **inherits R02**").
- **What survives.** D2's compatibility claim against blind R19 is correct: the
  sector/component start is registered data under `realized_state_primitive`
  (its source note: "A value that would change under a different law-admissible
  realized state is registered data, not derivation output"), and the rule's
  *form* is Admissibility-shaped. That is all.
- **Fix:** downgrade to "partial, shape only — the axiom sentence gives a
  nearest-neighbor support rule and nothing of Gauss's content; conditional on
  the supplied role compilation (row 3)"; delete or correct "#7893 already words
  Gauss's law that way"; reconsider "natural block 03".
- **Severity: material.**

### CH-05 — "What feeds the terminal" attributes dependencies no member states

- **file:line** `META:691-697` (`LANDING_CORE:654-660`).
- **Primary's text:** "What feeds the terminal, by member: ... the positive
  magnetic curvature `kappa` from #7886 and #7887 ...; the quadratic kernel's
  uniqueness under cubic covariance plus transversality from #7952 (a statement
  about the kernel class, independent of the dynamics class)."
- **Member's text:** (a) `#7952`'s kernel note is dated 2026-09-04, one day
  *after* `#7917` (2026-09-03); its declared parent is
  "SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE...";
  it never mentions `#7917`, and `#7917`'s front matter names only `#7915`
  (direct parent) and `#7913` (role compiler). Listing it "by member" under what
  feeds the terminal is a dependency no member states, and the parenthetical
  ("independent of the dynamics class") contradicts the list it sits in.
  (b) At `#7917`'s own scope `kappa` is not load-bearing for the uniqueness at
  all: `#7917:290-296` "The direct parent's Record-overlap curvature **can be
  assigned** `beta=kappa, alpha=1/kappa`, giving `c=1`" — it fixes the one
  remaining speed *after* the class has already selected the generator. The
  note's own Imports section gets this right ("Reciprocal coefficients ... Role:
  normalization", `META:738-740`); §7 overstates it.
- **Fix:** drop `#7952` from the list (or move it to a separate "adjacent, not
  upstream" line), and say `kappa` fixes the speed after selection.
- **Severity: material.**

---

## MINOR

### CH-06 — §0's one-paragraph chain elides the split its own §3 makes load-bearing
`META:56-58`: "A supplied Record registration or overlap law forces the local
plaquette potential's quadratic germ to be strictly positive". `#7886:60-62`:
"A temporal registration kernel by itself supplies only the electric/temporal
quadratic block. It has no magnetic restoring block and is not Maxwell." The
note's F-B1 (`META:217-229`) says exactly this; §0, the paragraph most likely to
be read alone, does not carry the temporal/spatial qualifier. **minor.**

### CH-07 — section heading in the deriving voice
`META:129` "## 2. The Maxwell germ forced (link ii)". Defensible (it mirrors the
member titles `#7886` "representation-positive Record kernels force a Maxwell
germ", `#7887` "Record-distribution overlap forces a positive Maxwell germ") but
the heading alone drops "supplied", which the body restores. This is the only
place in either prose deliverable that reads as the framework deriving Maxwell;
everywhere else continuum Maxwell is used strictly as the comparator. **minor.**

### CH-08 — branch-name provenance dropped from the meta note
`LANDING_CORE:415` and `:533` disclose that the `#7959` and `#7963` branch names
were "looked up with `gh pr view` on 2026-09-04; not in `inputs/`"; `META:453`
and `META:571` state them flatly. Two consequences: the meta note asserts two
addresses that no pack input supports, against its own "every number below is
quoted from a member note or record"; and the LANDING_CORE's own caveat wording
is itself wrong — `inputs/PR7959__*.md` and `inputs/PR7963__*.md` *are* in
`inputs/`; it is the branch names that are not. **minor.**

### CH-09 — `#7932` scope compressions
`META:394-397`: "In the no-wrap window (`|div E| < K/2`, exhaustive at `K=32`,
`|m|<=2`) modular Gauss is exactly additive; electric errors fall as `K^-2`; the
quadratic tangent on the cubic torus has ..." — `#7932` gives `|m|<=2` for the
*electric-cosine error table* (K=16..128) and `K=32, |div E|<=12<K/2` for the
*exhaustive no-wrap check*; the parenthetical blends two distinct conditions.
And `#7932`: "**At every nonzero momentum on `L=3,4,5,7`**, its curl kernel has
one gauge-null direction and exactly two degenerate transverse branches" — the
named finite tori are dropped in favour of "the cubic torus". **minor.**

### CH-10 — `#7955`'s own qualification dropped from the `c^2 = U K` sequence
`#7955` record: "L=10,12,14 accepts U K only with a broad, underresolved
coefficient." Carried nowhere in either deliverable (`META:561-569`, `:614-617`).
It is the member's own version of the caveat the note *does* carry at `#7963`'s
scope ("broad and have negative central values"), so the sequence is not
misleading — but the member's sentence should be there. Also dropped: "The
result remains finite-volume early-time spectroscopy with a four-sweep forward
suffix". **minor.**

### CH-11 — cross-merge mapping is internally inconsistent
`SUPPLIED_INPUT_LEDGER.md:417-420`: `R16` is mapped twice ("R13-R17 into row 1"
and "R16, R19, R21, R24, R25 into rows 11-12"), and `R19` is mapped into rows
11-12 while D2 (`:440-444`) adjudicates `R19` against row 4. **minor.**

### CH-12 — ledger row 3: the realized-state slot does not obviously host a role pattern
`:39` / `:196-201`: "at most a feature of a realized state (registered data)".
Per the axiom memo's Qualification, "A state is a configuration of records"; a
period-two vertex/edge/face/cube role pattern is not a record configuration, so
the realized-state slot is not an available home for it. The row's primary
argument (Lattice "No site is privileged" ⇒ a law-level role assignment
privileges sites ⇒ genuine supply) is sound and does not need the second clause.
**minor.**

### CH-13 — ledger row 2 is a computation row inside a derivation ranking
`:16-24` ranks "by the value to the chain of a **successful derivation**"; `:474`
then says "Row 2 is a computation block, not a derivation block". Disclosed, but
the tier-A placement mixes categories. Related and also disclosed: row 1 is
tier A because a *full* derivation would move the terminal, while the block-02
sub-target the ledger actually selects (items 3, 4, role-level 5) is by the
ledger's own §1 reasoning the part that cannot move it — "the block's honest
product may be a sharpened residual rather than a derivation" (`:470-472`).
**minor, disclosed.**

### CH-14 — small restatement drifts
- `LANDING_CORE:198` "the class `M_min` (M1-M6 plus continuous time)" — continuous
  time is *inside* `#7917`'s M2 ("no memory, second time derivative, external
  clock variable, or finite-step inverse"; N3: "Continuous time is supplied").
- `META:694-695` "the two-branch spectrum from #7915 (which #7917 inherits rather
  than re-derives)" — `#7917:286-288` does recompute it ("The runner rechecks
  every momentum on `L=3,4,5,7`") while saying "This is not a new photon count
  beyond the direct parent".
- `SUPPLIED_INPUT_LEDGER.md:207` "approach the photon frequency **only** at
  `K = 128, 256, 512, 1024`" — `#7932` lists those as the tested values, not as a
  limit.
- `META:653-655` "no member computes a same-detuning electric stiffness for the
  ring-exchange-alone law" — an absence claim over 31 PRs, 20 of which the pack
  carries only as two-sentence records. True on the evidence in `inputs/`; should
  be scoped to it.
**minor.**

---

## PASSES

**Check A — quote fidelity.** PASS apart from CH-01 and the minors above. All
203 quoted spans resolve to their member's own text at that member's own scope;
the eleven full member notes were checked line by line and the 29 records
diffed sentence-by-sentence. The terminal (`#7917`) and the photon split
(`#7959`, `#7945`, `#7963`, `#7952` x2, `#7955`) were checked exhaustively.
Spot list of exact matches verified: `#7917`'s seven class items and the
uniqueness statement (verbatim, `#7917:26-47`); `#7959`'s "NOTHING IS PROVED FOR
ANY L^3 TORUS WITH L >= 4 ..." and the `k < pi/6` not-decided sentence
(verbatim, `:5`, `:207`); `#7945`'s `c_V^2` pair, `gamma`, 5.1/6.0 sigma, 36%/61%,
`c_RK^2 = 0.000138 ± 0.000674` (all verbatim); `#7963`'s six fitted numbers,
both PASS/FAIL signatures, and "early-time estimator boundary with some L=18
leverage" (verbatim); `#7886`'s rank-one / "does not derive kappa_s>0 or
kappa_s=kappa_t" / gauge-action-isotropy sentences (verbatim); `#7921`'s six
class items and the kinetic-isotropy interpretation-boundary paragraph
(verbatim); `#7884`'s supplied list and "This is a supplied-action theorem"
(verbatim); `#7915`'s three-time-rule table and N3 "Supplied" list (verbatim).

**Check C — self-containment.** PASS on all three sub-checks.
- Exactly one markdown link in the whole note (`META:9`), to the landed
  `MINIMAL_AXIOMS_2026-06-29.md`. No link to any unlanded note. No member is
  presented as landed or audited; every member entry carries "open PR, unlanded".
- The machine-status block (`META:36-52`) has **exactly 15 fields**, with the
  spec's exact names and exact values: `actual_current_surface_status: open`,
  `target_claim_type: meta`, `trace_class: upstream_support`,
  `target_claim_id: null`, `target_blocker_text` verbatim,
  `source_of_blocker_text: frontier_question`, `reachability_to_target:
  supports`, `artifact_role: theorem`, `next_trace_action` (one sentence naming
  the ledger-selected target, consistent with `SUPPLIED_INPUT_LEDGER.md:463-475`),
  `conditional_surface_status: null`, `hypothetical_axiom_status: null`,
  `admitted_observation_status: null`, `claim_type_reason` verbatim,
  `audit_required_before_effective_retained: true`, `bare_retained_allowed: false`.
- No authority vocabulary is applied to any member. "retained" occurs only inside
  the two mandated field names; "audited" only in the negation at `META:780`;
  "landed" only as "unlanded" / "none landed" / "No member is landed".

**Check D — ranking of the top three rows.** PASS at the members' own scopes.
Row 1 is supported by `#7917`'s own "The four axioms do not currently select
that class. In particular, they do not state real linear first-order evolution,
energy conservation, minimal `(E,B)` payload, or continuous time" and its two
program choices. Row 2 is supported by `#7959`'s "what is missing for a Maxwell
photon is a stiffness" and `#7945`'s "Admissibility permits but does not select
them". Row 3 is supported by `#7959`'s "The link role is designed, not derived"
and `#7893`/`#7903`/`#7913`/`#7932`'s "declared". Within-tier ordering (levers
before genuine supply) is applied consistently. See CH-04, CH-12, CH-13 for the
qualifications. Cross-merge D1, D4, D5, D6 are fair characterizations of blind
R04, R01/R05, R03, R07 respectively; the "supervisor-checked 8/8 quotes" claim
matches `REVIEW_HISTORY.md`.

**Check D, item D3 — CONFIRMED in the primary's favour.** `#7959`'s "A
Rokhsar-Kivelson potential term moves the coupling **toward** `z = 2`, not away
from it" (`:214-215`) and `#7945`'s `c_V^2 = gamma |V-1|` at `V = 0.95, 0.90`
(`:246`) are consistent in direction: `V N_f` at `V < 1` is a *weaker* RK term
than at the RK point `V = 1`, so `#7945`'s motion toward linear is motion away
from `z = 2`, which is `#7959`'s statement read in the other direction. The blind
ledger's C01 ("a direct clash") misreads `V < 1` as "adding such a term". The
primary's reading is the better one, it records both at scope, and it correctly
locates the residual tension in the uncomputed interval `0 < V < 0.90` — where
`#7945` itself declines to extrapolate ("a response test, not an exact
perturbative identity at these finite detunings", `:274-275`).

**Check E — the photon item.** PASS (with CH-03 and CH-10). The split is stated
OPEN at every point: `META:73` "which of these is the lane's photon is open";
`META:407` heading "the lane's open item"; `META:592` "### 6.C The split, stated
as open"; `META:654-655` "is the lane's open item. This note decides nothing
about it"; `META:786` "No resolution of the two-branch photon split". The
`c^2 = U K` sequence `#7945 -> #7952 -> #7955 -> #7963` is carried member by
member at scope (`META:608-618`) with every verdict flip intact, including
`#7955`'s 6.563-error disagreement and its `L=8` localization. `#7963`'s
`-3.849` sigma early-window RK coefficient is carried twice, in the member entry
(`META:586-589`) and in the cross-member paragraph (`META:618-625`), together
with the `PASS=2 FAIL=1` genealogy failure, and is explicitly folded into the
open item ("That estimator boundary is part of the open item"). Nothing is
resolved.

**Check F — the terminal.** PASS (with CH-05 and one gap). All seven declared
class items are quoted verbatim at `META:661-673` against `#7917:26-35`; the
uniqueness statement and its "There is no second stencil, mass term, damping
term, orientation coefficient, or same-role nearest-neighbor term inside the
class" are verbatim against `#7917:37-47`; the boundary is verbatim ("The
classification does not derive that dynamics class from the axioms, and exact
finite local tick selection remains open"; "If equal lattice kinetic
normalization is applied to this already selected class, `c=1` in lattice
units"; "That is a conditional selection theorem, not an axiom derivation").
M5's load-bearing role is stated at `#7917`'s scope in the ledger (row 1 item 6,
`:97-114`: the diagonal blocks force `u=v=0`, the cross block forces the
weighted negative adjoint, and `#7917`'s "energy conservation excludes the
dissipative sampler"). **Gap:** the meta note carries M5's mechanical role
(`META:240-241`) but not that sentence, so a reader of the meta note alone
cannot connect M5 to the three-way time fork the note presents at `META:206-215`.
Recommend one clause in §7.

**Own-voice physics.** No sentence in either prose deliverable asserts that the
framework derives Maxwell or light; the honest terminal paragraph (`META:75-79`)
states the opposite. Continuum Maxwell is used only as the members' comparator
(`META:24-25`, `:771-774`, `:792-793`) and never as a premise. The primary's
own-voice content is confined to: the marked synthesis readings (`META:125-127`,
`:186-189`, `:411-413`), the unmarked readings of CH-03, the one arithmetic
product of CH-02, and the ledger's derivability estimates — which the ledger
correctly declares up front ("Every estimate is this synthesis's reading, not a
member claim", `:31`).

---

VERDICT: FIX FIRST | One blocker and four material findings stand between this pack and landing. The blocker is a fabricated attribution at the hinge of the lane's declared open item: both prose deliverables say `#7959` and `#7945` "report 9,600 Gauss/ice states at `L = 2`", and `#7945` reports no such number — it reports only the 864-state orbit — while the note quotes the true source (`#7937`) correctly twenty lines later; because that sentence is the evidence offered for the same-carrier identification, the "synthesis reading" label it carries is undercut by a false premise, and the fix is a one-line reattribution plus an explicit statement that the identification is stated by no member. The four material findings are all correctable in place: the note declares "Nothing is computed here" and then multiplies two members' numbers; three cross-member readings (including the "replaced" verdict on `#7945`'s 0.2598 comparator) are filed under a heading that says the members impose them, against the note's own labelling rule; ledger row 4's Gauss-as-support lever — which the primary itself flagged for this check — reverses the direction of `#7893`'s "support forcing among corner records", applies Admissibility to a vertex that every member gives no payload, and does not record that it inherits the tier-A supplied role compilation, so "partial, high" and "natural block 03" must come down to "partial, shape only"; and §7's "What feeds the terminal, by member" lists `#7952`'s kernel note (written a day after `#7917`, cited by neither) as upstream while in the same breath calling it independent, and promotes `kappa` from a post-selection speed normalization to a terminal input. Against that, the checks that matter most for a docs note all pass cleanly: self-containment is exact (one link, to the landed axiom memo; exactly the fifteen mandated status fields with the mandated values; no authority word touching any member), the photon split is stated open at six separate points with `#7963`'s `-3.849` sigma control boundary and genealogy failure carried in full and resolved nowhere, the terminal's seven class items and boundary are verbatim, and the primary's D3 disagreement with the blind seat is the correct reading. Fix CH-01 through CH-05, add one clause carrying `#7917`'s "energy conservation excludes the dissipative sampler" into §7, and the pack lands.
