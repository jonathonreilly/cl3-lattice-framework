# The gauge breaks at second order: GBW1b priced at seven, and the same clause that hid the window exposes it — Cycle 892

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed gravity axiom-up ladder;
no axiom surface touched). GBW1b — the kernel-window joint obligation
Cycle 885 split off — is now PRICED, and its central question is
answered by a theorem with an exhibited mechanism: the window extent
that the linear readout cannot see (Cycle 887's gauge theorem) is
SEEN by the quadratic normalization, because the barrier expels
amplitude from the records. The entire verdict is conditional on the
barrier identification B(R) = supp(R), inherited from Cycle 885 and
tested by neither cycle — named below as the one open route to
collapse.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle892_gbw1b_pricing_2026_07_28.py`](../scripts/frontier_cycle892_gbw1b_pricing_2026_07_28.py)
- [`frontier_cycle892_gbw1b_independent_check_2026_07_28.py`](../scripts/frontier_cycle892_gbw1b_independent_check_2026_07_28.py)

Receipt:

- [`gbw1b_pricing_cycle892_receipt_2026_07_28.json`](../outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json)
- [`gbw1b_independent_check_cycle892_receipt_2026_07_28.json`](../outputs/gbw1b_independent_check_cycle892_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted; substitution disclosed). One lineage
deviation disclosed: the Cycle-887 artifacts landed on a sibling
branch, so the two pinned files were checked out VERBATIM from the
887 ship commit with both digests verified against the spec before
use — vendored, never reconstructed (commit 7c11e5ab97). Checker
independence is cross-context and algorithmic (DFS path enumeration
vs the primary's layered DP). Independent audit still required.

## Q1 — the extent is NOT gauge at quadratic order

Over the 12-configuration family, six theta values, and the nine
containment-holding admissible windows from the 885/887 catalogues —
648 exact cells — the single linear readout class splits into
**8 quadratic classes**: 35 of 36 window pairs separate in Z, and the
one non-separating pair is set-identical on this family, so **Z is
exactly as fine as the window set itself**. Separation appears on
10/12 configurations at every theta. The annular chart SEES the
separation (8 profiles, 0 blind pairs) but does not DETERMINE Z (51
witnesses where equal (a2, b2) with different sets give different Z).

Before any of this: the restriction gate reproduced Cycle 885's
boundary-locus rows value-for-value, its degenerate control 0/12, and
Cycle 887's readout-gauge 9/12 with matching members, against their
pinned receipts.

## The mechanism (proved, not sweep-only)

**C892-T1 (amplitude expulsion).** The barrier B(R) = supp(R) blocks
the walk ON the barrier, so propagated amplitude is EXPELLED from the
records: reach intersect supp(R) is empty on 12/12 configurations,
the amplitude inside supp(R) is exactly the seed, and five
configurations freeze outright (every neighbour of the source is a
record).

**C892-T2 (the exact criterion).** Z is window-monotone with the
exact difference formula Z(W') - Z(W) = the amplitude mass on
W' minus W (26 nested pairs, zero violations; the support window is
the unique minimum). Corollary: the extent is gauge at quadratic
order IFF every admissible containment-holding window carries the
same mass on the reachable set — and the support window carries NONE
of it, so the gauge break has an exhibited witness, not just a
catalogue.

**C892-T3 (the kernel's exact role).** Z(theta) =
sum over d of M_d * T_d(cos phi) with cos phi = (1 - theta^2) /
(1 + theta^2), degree bounded by walk depth, M_d rational and
theta-free — 648 exact checks. The kernel contributes EXACTLY ONE
SCALAR (cos phi).

**C892-T4 (parity selection).** Odd interference orders appear iff
the source set spans both lattice parities — zero mispredictions.

The structural summary: the SAME axiom clause ("only records are
readable") hides the window at first order and exposes it at second —
it pins the linear readout to the records, and the barrier pushes the
quadratic weight off them, onto loci only the window choice selects.

## Q2 — the obligation map: GBW1b prices at SEVEN dimensions

- **(a) the window: LOAD-BEARING, does not collapse** — one
  convention (the structuring-set choice from Cycle 887, now with
  quadratic consequences). Supplying theta does NOT collapse it:
  windows separate at every theta.
- **(b) the kernel: one scalar** (cos phi, by C892-T3).
- **(c) the interface: five named requirements** the composed-record
  event-space step must supply (the Cycle-878 artifacts are ABSENT
  from this lineage — tracked-file scan, 0 hits, never
  reconstructed). Derived from computed Z facts only (the checker's
  needle scan confirms zero Born-rule vocabulary in the premises):
  IF1 is the sharpest — the barrier puts the linear readout and the
  quadratic weight on essentially DISJOINT loci, so no pointwise
  identification exists; IF3 — total box mass moves with theta on
  7/12 and normalizing by it leaves 7/12 still theta-dependent; IF5 —
  Z vanishes on 42 containment-holding cells; IF2 (finite additivity)
  comes for FREE and is banked; IF4/IF6 complete the set in the
  receipt.
- **(d) residual: 7** (1 + 1 + 5), with residual scenarios computed
  for all five supply combinations.

## Conditionality (the one open route to collapse)

Every result above is conditional on the barrier identification
B(R) = supp(R) — inherited from Cycle 885's derivation chain and
tested by neither cycle. A different barrier relocates amplitude and
could invert Q1. This is the named next question for any GBW1b
consumer, and it is the same identification premise the 885/887
residuals already carry.

## Process disclosures

Two real defects found and repaired in the open: the checker's first
run reported C892-T2 REFUTED with 42 violations — a phantom (its
sweep fingerprint dict was shared across configurations, comparing Z
from different records); per-config keying gives zero violations on
the same 7,192 windows. And the primary's science digest drifted
between cold runs — the census counted the cycle's own artifacts
(Cycle 885's repair-log item 9 recurring); fixed with a published
exact-path exclusion, two cold runs now digest-identical.

## Checker

Fully independent machinery; the partition reproduced identically.
Three windows the primary never evaluated (rank/threshold filter,
morphological closing, union map), each given a C892-T2 prediction
RECORDED BEFORE Z was computed — 3/3 land where predicted (the union
map joins its predicted class exactly). Adversarial hunt for a
collapse witness: all four constructions survive, including a sweep
of 7,192 generated containment-holding windows with zero violations
of T2. Teeth 8/8, including planted-difference blindness (the
partition provably can see a gauge break — so a collapse verdict
would not have been a blind spot either) and a blind-structural-
predictor mutation. All 11 pins match the committed tree.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "GBW1b — the terminal normalization as a kernel-window joint obligation (Cycle 885's split, carried through 887's gauge theorem)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "GBW1b is priced (7 dims: window convention + cos-phi + five interface requirements); the window convention is now load-bearing at the Born interface — carry the quadratic gauge break wherever the extent convention is consumed; the one open collapse route is the barrier identification B(R)=supp(R) (untested by 885 or here); the interface requirements IF1/IF3-IF6 are the exact demand sheet for any future event-space composition"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the gauge break is a theorem with an exhibited mechanism (expulsion + the exact difference formula), not a catalogue fact; the kernel reduction to one scalar is an exact Chebyshev-form identity on 648 cells; the interface requirements are derived from computed Z facts with a needle gate against Born vocabulary; the restriction gate reproduces both parent receipts value-for-value; the conditionality on the barrier identification is stated at the top, not buried"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 885 primary + receipt and the 887 primary + receipt (887 pair
  vendored verbatim from its ship commit, digests verified); the 885
  checker; the axiom memo and both Gate-B notes — eleven pins under
  hard-fail preflight;
- the barrier identification B(R) = supp(R) (the conditional
  premise, named).

### Derived

- the 8-class quadratic partition (Z exactly as fine as the window
  set) with the annular-chart sees-but-does-not-determine result;
- C892-T1..T4 (expulsion; the exact difference formula and collapse
  criterion; the one-scalar kernel form; parity selection);
- the 7-dimension GBW1b obligation map with all supply scenarios;
- the five interface requirements derived from Z's computed
  structure.

### Open

- the barrier identification (the one route to collapse — untested);
- the event-space composition meeting IF1/IF3-IF6 (next campaign's
  door);
- the Cycle-887 no-interaction and structuring-set conventions, now
  with quadratic consequences attached.

## Verdict

The ladder's last obligation had a question at its centre and the
question had a clean answer: no, the freedom does not stay free —
the window the linear world cannot see is exactly what the quadratic
world weighs, because the records expel the amplitude their own
readability clause pins to them. What is left of GBW1b is a demand
sheet: one convention the owner already holds, one scalar the kernel
was always going to charge, and five requirements addressed to an
event space that this lineage has never met. The whole bill is
conditional on one identification that nobody has yet audited — and
that identification is now the single most valuable open question on
the gravity side. Independent audit still required.
