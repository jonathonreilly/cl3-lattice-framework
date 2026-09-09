# The other half of the clock: complements belong to banks, and the law learns to count runs — Cycle 891

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed campaign-5, successor to
Cycle 889; no axiom surface touched). Both of Cycle 889's named open
questions are CLOSED: the even complement family has a derived
mechanism with a SEALED holdout verification, and the non-two-run
dirt has an exact k-run law of which 889's law is the two-run
sub-case. One carrier-level holdout miss and two 2-episode residuals
are reported as the partial results they are.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle891_complement_mechanism_2026_07_28.py`](../scripts/frontier_cycle891_complement_mechanism_2026_07_28.py)
- [`frontier_cycle891_complement_independent_check_2026_07_28.py`](../scripts/frontier_cycle891_complement_independent_check_2026_07_28.py)

Receipt:

- [`complement_mechanism_cycle891_receipt_2026_07_28.json`](../outputs/complement_mechanism_cycle891_receipt_2026_07_28.json)
- [`complement_independent_check_cycle891_receipt_2026_07_28.json`](../outputs/complement_independent_check_cycle891_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted; substitution disclosed). Checker
independence is cross-context and algorithmic (interval-algebra
detector — the primary's bitmask never formed; independent program
reconstruction; the controller's own step function as a second tick
generator). The worker's first mechanism hypothesis was WRONG and was
corrected mid-block from measurement (disclosed below); the checker's
first run was an HONEST_FAIL on its own coverage gate (disclosed
below). Independent audit still required.

## The transport anatomy (measured, then derived)

A per-station attributed kernel trace shows that inside a closed
quiescent stretch, the ONLY stations that move a bank's dirt are the
four ordered rows of an incident edge — the two RELAY_SWAP rows AND
the two HANDOFF rows (the worker's first hypothesis said RELAY_SWAP
alone; the measurement said otherwise; the published statement is the
corrected one). Twenty-six transitions in eighteen audited stretches:
zero charged to a non-transport station, zero touching a bank off the
edge. Each station is crossed twice per orbit (leader, follower sigma
ticks later), giving the exact bookkeeping identity
s2 - s1 = Delta_t + (p2 - p1) (mod N), which classifies EVERY
readable period.

## The complement mechanism (Q1, derived not fitted)

Exhaustively over B = 3..8: the ring-complement-valued separations
between incident transport stations take exactly three shapes —
same-edge (N - DELTA); the ENTRY GAP 8(B - 1 - b); and 8(B - 1),
which is alignment-forbidden at every B. Zero rows disagree with the
derivation. The structural fact: **DELTA is a property of one EDGE;
its complement is a property of one BANK** (b = B - 2 - e). Full
incidence tables at B=4 and B=5 (ledgers summing to the corpus, every
clock classified; the pinned 889 episode spectra reproduced exactly).
Co-occurrence is REAL: single clocks read both a DELTA and a
complement at different stretches (6 clocks at B=4, 153 at B=5, 247
at B=6, 306 at B=7 — recomputed, checker-reproduced row for row).

**The holdout.** The derive/holdout split (derive at B=4/5, predict
B=6/7) was SEALED — a digest computed and printed before any holdout
corpus existed, with the build log at seal time published and
holdout-free, byte-identical after. B=6: predicted {8, 16, 24} =
observed, exact, all three carriers verified as the predicted
entry-gap bank. B=7: predicted {8, 16, 24, 32}, all four present at
value level; carriers verified for three; **the P=32 carrier
prediction FAILED** — 32 fires only through the edge-complement
class, never the entry gap. Two residuals (40, 48) at 2 episodes each
out of 3,711 — statistically marginal, real, horizon-closed, fully
anatomized. The value-level holdout is exact; the carrier-level
holdout is 3/4 at B=7; both facts are the result.

[Qualification 2026-08-05, Cycle 922: the VALUE-level holdout
stands untouched; the CARRIER-level labels need clock-local
reading. This note's classifier is value-based with entry-gap
priority, so wherever a bank's entry gap coincides with its own
edge complement the ENTRY_GAP label is stolen: clock-locally the
B=6 P=24 carrier has ZERO bank-owned entry-gap episodes (it is the
same-edge complement of edge 2), B=8 P=32 likewise, and B=7 P=24
splits (20 true entry-gap episodes; the rest complement). Also:
the entry-gap census here was restricted to the two RELAY_SWAP
rows per edge — Cycle 922's RC-1 derives that the entry-gap value
is realised by exactly THREE ordered pairs, with the
handoff-carrying pair f(b)->h_r(b-1) the dominant carrier at
several B. The P=32 miss itself is predicted by the short-arc
condition 2P < N (fitted-then-sealed grade), and the 40/48
residuals are ordinary same-edge complements readable only
stretch-locally (2P >= N) — not a fourth shape. See the Cycle-922
note.]

## The k-run law (Q2, the named open question closed)

For a word with ANY dirty-run structure W:

    I_max(P) = (max cyclic gap of W symmetric-difference (W - P)) - 1

(N - 1 when the bad set is a single residue; unbounded when empty),
reading requires I_max >= P + 1 — plus the FINITE form for bounded
stretches (the same symmetric difference intersected with the
stretch's admissible offsets). Verified: 2,996 randomized ring cells
and 599 finite cells with zero mismatches, and **all 580 of Cycle
889's cells recovered exactly — 889's law is the k = 2 sub-case.**
The checker attacked it on primes and composites unrelated to the
8B-5 family, up to 9 runs, non-contiguous dirty sets, periods to 5N:
2,553 cells, zero mismatches, with a +1 perturbation breaking on all
381 controls.

**The B=7 anomalies resolve.** The four named-open periods (35, 40,
43, 48) are stretch-local readings: the finite form is exact on every
witness (50/50, 45/45, 51/51, 66/66) while the ring form would have
refused all four — the closed stretch simply does not carry the
orbit-periodic run pattern whose forbidden zones would kill the
period. Register-level event lists are published for all four
(including a genuine five-run word at P=40). Honest boundary, stated
exactly: the law is exact for any run structure, but it is a law
about a WORD — which word a given stretch carries is a dynamical
fact, measured per witness, not derived.

## Process disclosures (the honesty layer)

- The worker's first mechanism hypothesis (RELAY_SWAP-only transport)
  was refuted by its own instrumentation and corrected; gates reflect
  the corrected fact.
- The checker's first full run HONEST_FAILed its own declared
  coverage threshold (1,337 attack cells vs 1,500 declared, zero
  mismatches) and had a register-comparison bug; both fixed in a
  dedicated commit and re-run; the verdict block never changed.
- One disclosed optimization: OR-folded residue counting, proven
  equivalent to the pinned semantics on 4,000 randomized words inside
  a gate, with the checker deriving residues a third way.

## Checker

10/10 gates PASS; `findings_the_primary_did_not_report` EMPTY.
Independent program reconstruction (zero disagreements, B=3..8);
interval-algebra detector validated against a literal per-tick
definition on 2,500 cases; B=4/5 recomputed in full with row-for-row
agreement; **the holdout audit recomputed both predictions and both
carrier maps from the rule's STATED TEXT alone** — the text is
determinate, the seal-time build log is holdout-free, the rule-source
digest agrees. All four witness anatomies verified register by
register with a second, independent tick generator. Teeth 7/7
(tampered pin, dropped clock family, hardcoded incidence row, leaked
census answer, holdout violation, fake anatomy, perturbed law).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "Cycle 889's two named open questions: the even complement family's mechanism (observed, law-admissible, underived) and the non-two-run episode dirt at B=7 (35/43 outside the two-run law's scope)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "both questions closed; carry the k-run law (with its finite form) as the standing period instrument — 889's law is its k=2 sub-case; the P=32 carrier miss and the 40/48 two-episode residuals are the named remaining anomalies (value-level understood, carrier-level open); the edge-vs-bank ownership split (DELTA/complement) should be carried wherever clock families are consumed"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the mechanism is measured at register level then derived with an exhaustive separation census (0 disagreeing rows); the holdout was cryptographically sealed before the holdout corpora existed and independently audited from the rule text alone; the k-run law is exact on 6,148 verified cells including 889's full cell set as a sub-case; every partial miss and residual is reported with its anatomy"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- fourteen pins: the 881 primary/receipt/caches, the 889
  primary/checker/receipts/caches, the 879 primary, and the Cycle-719
  kernel pair exactly as 889 pinned them; only the kernel imported
  (the substrate under test), zero firewall hits.

### Derived

- the transport anatomy (four rows of an incident edge; HANDOFF
  transports) and the bookkeeping identity;
- the three complement shapes and the edge-vs-bank ownership split;
- the complete B=4/5 incidence tables and the co-occurrence counts;
- the sealed-holdout verification at B=6/7 with its honest carrier
  miss;
- the k-run law (ring and finite forms) with 889's law as sub-case;
- the resolution of all four B=7 anomalies as stretch-local readings.

### Open

- the P=32 carrier mechanism at B=7 (value predicted, carrier class
  wrong);
- the 40/48 two-episode residuals (anatomized; no rule yet);
- which word a stretch carries (the dynamical fact the law
  deliberately does not cover).

## Verdict

Cycle 889 left two questions standing; this block answers both and
pays for the answers with discipline: the complement family turns out
to be the bank's own signature (where DELTA was the edge's), predicted
into unseen corpora from a rule sealed before those corpora existed —
and where the prediction partly missed, the miss is in the note, not
under it. The law that replaced the dead conjecture now counts runs
instead of assuming two, swallows its predecessor as a special case,
and explains every anomaly it was born from — while declining, on the
record, to predict the one thing that is genuinely dynamical.
Independent audit still required.
