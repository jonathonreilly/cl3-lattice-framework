# Owned but never read: the P=32 miss derived from the short arc, a label theft exposed, and the residuals dissolve — Cycle 922

Date: 2026-08-05

Authority: none

Audit: unset

Status: bounded worked result (owner-directed T-lane closure,
window 2b; no axiom surface touched). Cycle 891's honest carrier
miss is CLOSED, and on the way the block finds something larger
than it was sent for. The anatomy: bank 2 OWNS the value 32 at B=7
through all three entry-gap row pairs — the geometry is fully
intact — but no clock containing bank 2 READS period 32 anywhere
in the corpus; every one of the 276 P=32 episodes is a same-edge
complement (bank 4) or a cross-token reading (bank 0), exhaustively
accounted. The larger finding: 891's classifier is VALUE-based with
entry-gap priority, so wherever a bank's entry gap coincides with
its own edge complement the ENTRY_GAP label is STOLEN — two of
891's carrier labels are corrected (B=6 P=24 and B=8 P=32 are
clock-locally same-edge complements) and one is split (B=7 P=24 is
part entry gap, part complement). The realization condition —
2P < N, the SHORT-ARC condition — is stated with its honest
epistemic status (FITTED-THEN-SEALED, not derived), predicts a
sealed B=8 map and a fully blind B=9 map with necessity NEVER
violated on 27 cells and sufficiency failing on exactly the two
b = B-2 cells flagged in advance, and strictly dominates 891's own
rule. And the 40/48 residuals are NOT a fourth shape: they are
ordinary same-edge complements whose 2P >= N makes them readable
only stretch-locally — which is why they come in ones and twos.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle922_p32_carrier_2026_07_28.py`](../scripts/frontier_cycle922_p32_carrier_2026_07_28.py)
- [`frontier_cycle922_p32_carrier_independent_check_2026_07_28.py`](../scripts/frontier_cycle922_p32_carrier_independent_check_2026_07_28.py)

Receipt:

- [`p32_carrier_cycle922_receipt_2026_07_28.json`](../outputs/p32_carrier_cycle922_receipt_2026_07_28.json)
- [`p32_carrier_independent_check_cycle922_receipt_2026_07_28.json`](../outputs/p32_carrier_independent_check_cycle922_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Two dated qualifications to the Cycle-891 note are executed
on the blockT5 branch (the post-ship-edit pattern; below).

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). The spec's alignment-forbidden guess
was declared a non-premise and is FALSIFIED — the entry-gap
geometry at (7, 2) is intact; the failure is blunter. SEAL HONESTY,
disclosed in full: during scoping the worker saw 891's LABEL-level
output at B=8 before the condition was written; the condition was
fitted only to clock-local B=4..7 incidence, and its B=8/B=9
predictions were pre-registered by SHA-256 BEFORE any clock-local
B=8 attribution was computed — the prediction CONTRADICTED the 891
label on two of six cells and the clock-local truth vindicated it
on one and refuted it on the other, so no retro-fit was possible
(the pre-registration also recorded the (8,6) risk in advance).
B=8 is therefore a partially-informed holdout at the label level
and blind at the clock-local level; B=9 is blind on every level
(the primary NEVER builds a B=9 corpus; the checker builds it).
The checker's first run rebuilt B=8 independently but broke the
900 s cap (1237 s, 9/9 PASS, reproducing the primary's B=8 row
including the sufficiency failure); it was re-scoped and re-run at
792 s, with the over-budget run's rows and stdout digest preserved
in the receipt as superseded, disclosed as not-the-shipped-run.
Independent audit still required.

## Q1 — the anatomy, and the finding above it

**The miss:** `any_clock_containing_bank2_reads_P32 = false`. All
276 P=32 episodes at B=7: bank 4 (90 episodes, sigma 5, the
same-edge complement r(3)->f(3)); bank 0 (2 episodes, sigma 19,
cross-token N - sigma = 32); pair clocks inherit (92 + 184 = 276).
Member banks over all reading clocks: {0, 4, 5, 6} — bank 2 never
appears, while owning the value through all three of its entry-gap
row pairs. The bookkeeping identity checked on 407 attributed
run-start pairs, zero violations.

**The label theft (the larger finding):** 891's
`classify_separation` scans every swap station in the machine
(value-based) and gives RELAY_ENTRY_GAP top priority — so wherever
8(B-1-b) coincides with the bank's own edge complement (b = (B-1)/2
or (B-2)/2), the ENTRY_GAP label is stolen regardless of what
produced the reading. Redone clock-locally: **B=6 P=24 — zero
bank-owned entry-gap episodes** (it is the same-edge complement of
edge 2); **B=8 P=32 — zero** (the same, edge 3; 891's label said
ENTRY_GAP with 22 episodes); **B=7 P=24 — split** (20 episodes are
the true entry gap; the rest are bank 3's own complement).

**RC-1 (derived, exhaustive, B=3..12, zero disagreeing rows):**
among a bank's own eight incident transport rows the entry-gap
value is realised by exactly THREE ordered same-token pairs — and
the handoff-carrying pair f(b)->h_r(b-1) carries MOST of the
episodes at several B. 891 reported one pair because its census
was restricted to the two RELAY_SWAP rows per edge; its swap-only
inventory would have missed the dominant carrier. (Also derived:
N-3 is realised by two pairs.)

## The realization condition, with its honest status

**RC-2, SHORT-ARC NECESSITY: a bank-owned entry-gap reading occurs
only if 2P < N** (equivalently b >= floor(B/2)). At B=7 this cuts
the family at P in {8, 16, 24}, excluding 32 — **891's carrier
miss, predicted by the condition**. Fit: 14/14 cells at B=4..7.

**Status: FITTED-THEN-SEALED, NOT DERIVED** — stated plainly in
the runner, the receipt, and here. The mechanism sketch (the entry
gap must be the short arc of the bank's own two dwell residues;
at 2P >= N the stable region must close on a residue the bank does
not own) is a derivation for the single-token orbit word ONLY;
with two tokens a bank can carry more residues — which is exactly
why the same-edge-complement shape IS readable at 2P > N (bank 4
reads 32 with 2P = 64 > 51) while the entry-gap shape is not.
RC-1 is derived; RC-2 is fitted; RC-3 (sufficiency) is a declared
boundary, not claimed.

## Q2 — the sealed prediction

Seal: a digest of the condition text plus its pure-function output
at B=8..12, computed and printed before any holdout corpus
existed, with the seal-time build log published and holdout-free;
byte-identical after. **B=8 (full map, 532,176 stretches):
necessity 6/6; sufficiency fails on one cell** — b=6 (P=8), which
sits at b = B-2. Against the same tier 891's own rule is wrong on
two cells; RC-2 on one; **RC-2 strictly dominates**. **B=9 (fully
blind; built only by the checker): predicted firing {4,5,6,7};
measured {4,5,6}; necessity violations NONE; the one sufficiency
failure is b=7 (P=8) — the exact cell the primary flagged as
marginal IN THE SEALED BLOCK.** Across all 27 cells: necessity
never violated; sufficiency fails on exactly the two b = B-2 / P=8
cells, both flagged in advance.

**Model degeneracy, reported not argued away:** three rival closed
forms fit the corpus exactly as well (2P < N; 2P < N+4;
b >= floor(B/2) — the third algebraically identical to the first)
— the entry-gap values are multiples of 8 and N grows by 8 per
bank, so no threshold inside one 8-wide band is distinguishable by
this corpus. For contrast on the same cells: P <= 24 is wrong on
6; **891's ring-alignment rule is wrong on 7**.

## Q3 — the residuals dissolve

The four B=7 residual episodes (P=40 x2, P=48 x2) are the
SAME-EDGE COMPLEMENT shape on banks incident to the edge (bank 4
via r(4)->f(4) = N - DELTA(7,4); bank 6 via r(5)->f(5) =
N - DELTA(7,5)) — 891 did NOT mis-bin them (its label was
correct); it had no rule for the route. Their rarity is the same
short-arc fact: 2P >= N for both, so no ring-periodic reading can
close and only stretch-local finite-form readings survive —
precisely 891's own finding that the ring form refuses both
witnesses while the finite form is exact on them. **A complement
value with 2P >= N is readable only stretch-locally, and therefore
only in ones and twos.** Unchanged and open: WHICH stretch carries
the truncated word (891's declared dynamical boundary).

## The corrections executed (post-ship-edit pattern)

Two dated qualifications on the Cycle-891 note (blockT5 branch,
pin refreshed): (1) the carrier-level labels at value-coincidence
cells (B=6 P=24 and B=8 P=32 are clock-locally same-edge
complements; B=7 P=24 splits) — the VALUE-level sealed holdout is
untouched; (2) the entry-gap census was swap-row-only — RC-1's
three-pair inventory supersedes it, with the handoff pair the
dominant carrier.

## Gates, teeth, checker

Primary: 10/10 gates PASS, 540 s; the restriction gate against
891 has ZERO failed checks (B=4/5 complement source classes,
carrier banks, completeness ledgers, co-occurrence counts, B=6/7
episode counts, the 32 -> {} carrier verification, residual
counts, stretch counts); double-run byte-identical modulo the
runtime field. Checker: SUPPORTED_WITH_PART_REFUTATION, 9/9 gates,
792 s, 10/10 teeth — own tick generator validated tick-for-tick
against the pinned kernel's own gate semantics (three tiers, zero
mismatches); a third-route detector on tick-index SETS (both prior
routes avoided), validated on 1200 randomised cases; the rule
re-derived from the primary's stated text alone (three phrasings,
determinate on all 55 cells). The checker CONFIRMS the bank-2
silence, the residual anatomy, and the B=7 cells row for row; its
PART-REFUTATION (the B=9 b=7 sufficiency failure) and the
three-way model degeneracy are reported above as results, not
softened. Anatomy dumps are capped at 8 stored rows per
(bank, period) — every episode is CLASSIFIED and the aggregate
counts are exhaustive; the register-level dump is a sample.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "891's P=32 carrier miss at B=7 (value predicted, carrier class wrong) and the 40/48 two-episode residuals (anatomized, no rule)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the miss is derived-at-fitted-grade (SHORT ARC: bank-owned entry-gap readings need 2P < N; necessity unviolated on 27 cells incl. a fully blind B=9; sufficiency fails only at the flagged b=B-2/P=8 cells — RC-3's discriminating measurement is named: equal-width runs w <= P-1 with >= 8 clean stable ticks); the LABEL THEFT corrects two 891 carrier labels (value-priority classifiers must be read clock-locally — carry this wherever 891's carrier claims are cited; the value-level holdout stands); RC-1's three-pair inventory supersedes the swap-only census (the handoff pair dominates); the 40/48 residuals dissolve into stretch-local complements (2P >= N); named cheap successor: the never-firing third pair h_f(b)->r(b-1) (geometrically present at every B, zero episodes anywhere, no rule); the model degeneracy (an 8-wide indistinguishable band) needs a corpus with N not congruent to 3 mod 8 if anyone ever wants the threshold's exact form"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "RC-2 is FITTED-THEN-SEALED, not derived (the single-token mechanism sketch does not extend to two-token words — stated); the B=8 holdout is label-informed/clock-locally-blind and B=9 fully blind (disclosed with the pre-registration digest); three rival forms fit equally within an 8-wide band (model degeneracy reported); the shipped checker rebuilds B=7 and B=9 only (the over-budget run that also rebuilt B=8 is preserved as superseded); anatomy dumps sampled at 8 rows per cell with exhaustive classification"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the anatomy is exhaustive (276/276 episodes classified; the bookkeeping identity at zero violations); RC-1 is an exhaustive derivation B=3..12 with zero disagreeing rows; the sealed predictions carry printed pre-registration digests with holdout-free build logs, and the blind B=9 tier was built only by the independent checker; the label-theft correction is exhibited clock-locally against 891's own labels; the checker's part-refutation and the model degeneracy are carried on the claim surface"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 891 package (the restriction authority — zero failed
  checks), the 889/881/879 packages and the pinned Cycle-719
  kernel exactly as 891 pinned them; nothing else.

### Derived

- the exhaustive P=32 anatomy (owned-but-never-read) and the
  bank-2 silence;
- the label-theft correction with the clock-local re-attribution
  (two labels corrected, one split);
- RC-1 (the three-pair inventory; the dominant handoff carrier);
- RC-2 at fitted-then-sealed grade with the 27-cell record and
  strict dominance over 891's rule;
- the 40/48 dissolution (stretch-local complements; the
  ones-and-twos law);
- the model-degeneracy band.

### Open

- the never-firing third pair (the named cheap successor);
- RC-3 sufficiency (the equal-width discriminating measurement,
  named, not forced);
- the threshold's exact form inside the 8-wide band (needs a
  different-N corpus);
- WHICH stretch carries a truncated word (891's dynamical
  boundary, unchanged).

## Verdict

The miss that survived a sealed holdout turns out to have been
telling the truth twice: the bank really does own the value — its
geometry is perfect, all three doors in place — and the machine
really never walks through any of them, because the period is too
long for the short arc the reading requires. On the way to that
answer the block caught the classifier doing something no one had
looked for: handing the entry-gap label to readings the complement
produced, whenever the two values collide — so two of the old
holdout's carrier verdicts change hands while its value-level
record stands untouched. The residuals stop being residuals the
moment the same condition is read backwards: too long for the
ring, they live only in stretches, and stretches deal in ones and
twos. What the block declines to claim is as visible as what it
claims — the condition is fitted and sealed, not derived; three
siblings fit inside a band the corpus cannot split; and the one
pair that never fires anywhere is left on the bench, named, for
whoever comes next. Independent audit still required.
