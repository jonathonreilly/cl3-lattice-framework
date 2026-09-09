# It happens constantly and is never read: the third pair's shadow derived, and RC-3 measured open — Cycle 930

Date: 2026-08-05

Authority: none

Audit: unset

Status: bounded worked result (owner-directed T-lane closure,
window 2b; no axiom surface touched). Cycle 922's two benched opens
are executed, with one closing and one measured decisively open.
THE THIRD PAIR: the answer is not "it cannot happen" — the pair
(h_f(b), r(b-1)) occurs 2,698 times at register level over B=4..8
and reaches the full reading configuration 34 times, with ZERO
episodes everywhere. The asymmetry is DERIVED: sorted by station
index, a bank's eight rows contain exactly ONE consecutive unit gap
— r(b-1) - h_r(b) = 1 — so every crossing of the third pair's
terminal is preceded, one tick earlier and by the same token, by
that token's crossing of ANOTHER row of the same bank: the terminal
is SHADOWED (exhaustive over 253 cells, B=3..24; closed forms
validated against the kernel's emitted program). The zero itself is
measured-and-sealed, not derived — stated at that grade. RC-3: the
equal-width discriminator DOES NOT CLOSE — it is neither necessary
(156 firing episodes carry no equal-width pair) nor sufficient (the
b = B-2 failing cell presents the full configuration 8 times and is
refused every time), and the binding refusal component is a TAIL
fact — the terminal 2P+1 ticks are not P-exact — which is exactly
891's declared dynamical boundary. The realization law therefore
stays open at RC-3, now MEASURED to sit on the dynamical boundary
rather than being any function of (B, b).

Claim type: bounded_theorem

Runners:

- [`frontier_cycle930_third_pair_rc3_2026_07_28.py`](../scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py)
- [`frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py`](../scripts/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py)

Receipt:

- [`third_pair_rc3_cycle930_receipt_2026_07_28.json`](../outputs/third_pair_rc3_cycle930_receipt_2026_07_28.json)
- [`third_pair_rc3_independent_check_cycle930_receipt_2026_07_28.json`](../outputs/third_pair_rc3_independent_check_cycle930_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). One worker over-claim was caught by
the block's own gate and corrected on the record: the first TP-3
claimed uniqueness properties that fail on 105 cells; the published
TP-3 carries the exception. SEAL HONESTY beyond the spec's ask:
B=8 is NOT a holdout (922's receipt publishes the zero on all six
B=8 rows, read before the seal) and B=9 is NOT blind (922's checker
receipt publishes the B=9 shape lists) — the first genuinely blind
tier is B >= 10, which no one has built; recorded in the gate and
receipt, and the B=10 spot-check did not fit the runtime budget and
is left undone, disclosed. Independent audit still required.

## Q1 — the third pair: shadowed, not forbidden

Register-level truth first: the pair occurs in 19 of 20 cells
(2,698 occurrences; 34 full configurations; the checker's widened
hunt — ANY two P-separated run starts, not just consecutive —
raises occurrences to 4,576 and still finds ZERO firing episodes,
including on B=9). Every refusal of a full configuration fails the
SAME component: the terminal ticks are not P-exact (34/34).

The derivation (TP-1..TP-3, pure station arithmetic, exhaustive
B=3..24 at zero disagreements):

- **TP-1 (the unit gap):** bank b's eight rows, sorted by index,
  have exactly one consecutive gap of 1: r(b-1) - h_r(b) = 1. A
  token advances one station per tick, so every crossing of
  r(b-1) is immediately preceded by the same token crossing
  h_r(b) — another row of bank b.
- **TP-2:** of RC-1's three pairs, exactly one terminates on
  r(b-1) — the third; the other two pairs' terminals have
  non-bank predecessors. All three FIRST stations are unshadowed.
- **TP-3 (with its exception carried):** h_r(b) has no P-preimage
  among the rows and sits one station below the third pair's
  terminal; the three first stations are the only P-shift-fixed
  rows EXCEPT on cells b = floor((B-1)/2), where exactly one
  reverse row becomes a fourth — and those exception cells are
  precisely Cycle 922's label-theft cells, reached here from the
  geometry side (at odd B the fourth fixed row IS the third
  pair's own terminal).
- **TP-4 (the zero itself): measured and sealed, not derived** —
  the seal covers B=9..12 with a holdout-free build log,
  independently recomputed by the checker from the primary's text
  alone; only B >= 10 is genuinely blind.

## Q2 — RC-3 does not close (both readings run)

**Reading A (the discriminator as stated, on attributed entry-gap
pairs): neither necessary nor sufficient.** Not necessary — B7.b3
fires 20 episodes while ALL 548 of its equal-width-carrying
stretches are refused, and 156 firing episodes across the corpus
carry only unequal-width pairs. Not sufficient — five cells
present configurations and fire nothing, including B8.b3 (258
presentations) and the flagged B8.b6; inside firing cells the
over-prediction is severe (544 presented / 8 fired at B7.b5).

**Reading B (on the P-exact stable region): a theorem of the
detector** — the stable region satisfies S[t] = S[t+P] by
definition, so run widths match unless tail-truncated (3,707
equal; all 266 unequal explained by truncation; zero unexplained).
Vacuous as a criterion; reported as such.

**The failing cell, answered exactly:** B8.b6 (P=8, the b = B-2
cell) presents the full configuration 8 times — width equality,
w <= P-1, clean ticks, stretch length all satisfied — and is
refused every time (R3 x6, R6 x2). NOT ONE component of the named
measurement is what fails. The refusal decomposition over all
presented configurations: ACCEPT 3,311 / R3 3,328 / R2 252 /
R6 98 — the binding component is the tail's P-exactness, i.e.
WHICH word the stretch carries at its end: 891's declared
dynamical boundary. **RC-1 derived; RC-2 fitted-then-sealed
(untouched); RC-3 open, and now measured to live on the dynamical
boundary rather than in (B, b) arithmetic.** No retro-prediction
for higher-B b = B-2 cells is claimed.

## Checker findings (adopted on the claim surface)

Status SUPPORTED_WITH_FINDINGS; zero refutations of the anatomy or
the derivations; two findings the primary did not report, both
adopted: (1) the primary's named statistic is NOT the best simple
discriminator — both_widths <= 3 outscores equal_width (F1 0.5642
vs 0.5574, with equal_width's precision at 0.40) — which
STRENGTHENS "does not close" and belongs on the record; (2) the
"binding component" claim survives as a refusal DECOMPOSITION and
not as a PREDICTOR (F1 0.13) — the weaker reading is the supported
one and is the one this note states.

## Gates, teeth, scoping

Primary: 10/10 gates, 458 s; the restriction gate against the
pinned 922/891 bytes has ZERO failed checks (the full B=4..7 clock
census, the 14 per-cell rows, the six B=8 holdout rows, the P=32
totals and bank lists, the 40/48 residual counts); deterministic
double-run. Checker: 10/10 gates, 678 s, on the lane-parallel
bit-slice generator validated tick-for-tick against the kernel's
own controller step (disclosed as the same posture as 922 — the
only route inside budget); B=5/6/7 recounted at zero
disagreements; blind-tier B=9 rebuilt and agreeing with the pinned
922 checker on all 7 rows; the widened hunt; the seal recomputed
independently. Teeth 20/20 across both runners. Declared scoping:
primary B=4..7 all clocks + B=8 bank clocks only (every restricted
B=8 quantity is bank-clock-only in the pinned source by
construction); the B=8 class-count rows are NOT recomputed and NOT
restricted against — stated, not hidden; anatomy dumps capped at
6 rows per (bank, shape) with exhaustive aggregate counts.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "Cycle 922's two benched opens: the never-firing third entry-gap pair (geometrically present at every B, zero episodes, no rule) and RC-3 sufficiency (the equal-width discriminating measurement, named, not forced)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the third pair's asymmetry is DERIVED (the unit-gap shadow: its terminal is always preceded one tick earlier by another row of the same bank; the zero itself sealed at measured grade — first blind tier B>=10, unbuilt); the shadow's exception cells ARE 922's label-theft cells, reached from geometry; RC-3 DOES NOT CLOSE — the discriminator is neither necessary nor sufficient, the best simple statistic is the checker's both_widths<=3 (F1 0.56, still weak), and the binding refusal is the tail's P-exactness = 891's dynamical boundary (which word a stretch carries) — the realization law's sufficiency side is a STRETCH-DYNAMICS question, not (B,b) arithmetic; T-LANE TERMINAL AT WINDOW SCOPE: k-run law + complement mechanism + RC-1/RC-2 + the shadow derived, RC-3 honestly open on the named boundary"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "TP-1..TP-3 are derivations (exhaustive B=3..24 with kernel-validated closed forms); TP-4 (the zero) is measured-and-sealed with only B>=10 genuinely blind (unbuilt, disclosed); the RC-3 verdict is at the measured corpus (B=4..8 primary tiers + the checker's B=9) under both readings of the spec's discriminator; the binding-component claim is a refusal decomposition, not a predictor (the checker's qualification adopted); declared tier scoping as listed"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the shadow derivation is station arithmetic verified on 253 cells and against the kernel's emitted program; the zero survives the checker's widened hunt (4,576 occurrences, zero episodes, including blind-tier B=9); the RC-3 negative carries exhaustive presentation/refusal tables with every component identified and the failing cell's 8 refused presentations itemized; the restriction surface reproduces at zero failures; both checker findings are adopted rather than argued"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 922 package (the restriction authority and the benched
  opens), the 891 package (the census and the dynamical-boundary
  language), the 889/881/879 packages and the pinned Cycle-719
  kernel exactly as inherited; nothing else.

### Derived

- the unit-gap shadow theorem (TP-1..TP-3, with the exception
  carried and its identity with the label-theft cells);
- the register-level anatomy of the third pair (occurs constantly,
  never read; every refusal the same tail component);
- the RC-3 double-reading negative with the full
  presentation/refusal decomposition and the failing cell's
  itemized refusals;
- the discriminator ranking (the checker's, adopted).

### Open

- RC-3 itself — now located ON the dynamical boundary (which word
  a stretch carries): closing it means predicting stretch tails,
  which 891 deliberately declined; nothing in this lane's
  arithmetic can close it;
- the B >= 10 blind verification of the third-pair seal (cheap,
  unbuilt);
- the RC-2 model-degeneracy band (922's, untouched).

## Verdict

The pair that never fires turns out to be the busiest silence in
the machine: it forms thousands of times, reaches the full reading
posture dozens of times, and is refused on every single occasion —
because its terminal station lives one tick downstream of another
row of its own bank, so the machine has always just read something
else. That shadow is arithmetic, derived once and checked across
two hundred fifty-three cells, and its only exceptions sit exactly
on the cells where the old classifier was caught stealing labels —
two anomalies closing into one geometry. The sufficiency question
took the opposite path: measured all the way down, the celebrated
discriminator fails in both directions, the best statistic anyone
can build from widths is mediocre, and the thing that actually
decides is the one thing this lane's arithmetic was never going to
decide — which word the dynamics leaves in a stretch's tail. The
lane ends its window where honest lanes end: everything arithmetic
derived, everything dynamical named, and the boundary between them
drawn in the right place. Independent audit still required.
