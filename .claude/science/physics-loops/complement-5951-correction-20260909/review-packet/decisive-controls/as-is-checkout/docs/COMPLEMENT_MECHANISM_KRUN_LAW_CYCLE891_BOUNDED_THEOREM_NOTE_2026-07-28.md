# Bank/edge identity algebra and the cyclic k-run alignment law; the corpus mechanism and holdout story as stipulated history — Cycle 891

Date: 2026-08-04 (revised 2026-08-08, review loop iteration 1)

Authority: none

Audit: unset

Status: bounded worked result, SELF-CONTAINED after review. The
identity algebra and the k-run alignment law are recomputed from
scratch in-file; the corpus-scoped mechanism census and the
derive/holdout story are provenance context only — their inputs
(Cycle-879/881/889 artifacts) are not landed on origin/main and are
absent from this tree.

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

## Review record (review loop iteration 1, Sol reviewer, 2026-08-08)

Two review findings drive this revision. First, the original note
called its derive/holdout split "SEALED — a digest computed and printed
before any holdout corpus existed". The seal was created AT RUNTIME
from the final rule source and the in-memory build log, inside the same
reviewed file that contains the deterministic corpus generator; the
post-holdout check re-hashed the same final rule text. That proves one
invocation did not mutate the rule function after building the holdout
corpora — an in-process precomputation/order guard. It does not prove
the author had not inspected or fit to those deterministic outputs
before committing the final source; no prior commit, tag, or external
timestamp binds a pre-holdout digest. The "sealed"/blind-holdout
language is WITHDRAWN. Second, the runner's own preflight hard-fails in
this tree: its Cycle-879/881/889 inputs are unlanded and absent, so the
committed green cache certified a different, fuller checkout. The
corpus-scoped results are therefore stipulated history here, and both
runners were replaced by self-contained fail-closed programs computing
only the cores below. The old framing must not be cited as a passed
gate.

## Result 1 — bank/edge identity algebra (exact, exhaustive)

For bank count `B` and edge offset `e` (with `b = B - 2 - e`):

    N = 8B - 5
    DELTA = 8B - 13 - 8e
    N - DELTA = 8(e + 1)
    entry gap = 8(B - 1 - b) = 8(e + 1) = N - DELTA

verified exhaustively over `B = 3..8` and every valid `e` (primary),
and over `B = 3..60` with finite-difference coefficient cross-checks
(checker). These are the stated signs and normalizations of the
recorded transport bookkeeping, certified as pure algebra.

## Result 2 — the cyclic k-run alignment law (exact, controlled)

For a cyclic word of length `N` with dirty residue set `W` and period
`P`, the longest run of positions `i` with `dirt(i) == dirt(i + P)`
equals

    (max cyclic gap of W symdiff (W - P)) - 1

with the edge cases handled: an empty mismatch set gives the whole
ring (`N`), and the mismatch set always has even cardinality (equal
cardinalities of `W` and `W - P`; verified). Verified against a
literal ground-truth scan on 3,000 randomized cells (primary) and
2,500 cells with an independent single-pass ground truth on a
different seed (checker); a `-2` perturbation of the formula breaks on
every applicable control cell. This is the law of which the recorded
two-run law is the `k = 2` special case — that historical
correspondence (the 580 recorded cells) is provenance context below.

## Provenance context (non-load-bearing)

The original block's corpus-scoped content — the per-station transport
anatomy (four ordered rows of an incident edge), the B=4/5 incidence
tables, the co-occurrence counts, the derive-at-B=4/5 /
predict-at-B=6/7 exercise with its exact value-level hits, the P=32
carrier miss (predicted entry-gap carrier; observed edge-complement
carrier), the 40/48 two-episode residuals, and the recovery of the
recorded Cycle-889 cells as the k=2 sub-case — was computed on the
unlanded Cycle-879/881/889 stack plus the landed Cycle-719 kernel.
None of it is certified by this package; it is recorded history from
an uncertified fuller checkout. The honest description of the
historical B=6/7 exercise is: an in-process precomputation guard
ordered the rule construction before the holdout corpora were built
within one invocation, and the recorded value-level predictions
matched while one carrier-level prediction failed. If the stack lands,
the corpus census can be re-run and certified in its own package.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the recorded even-complement family's mechanism and the recorded non-two-run episode dirt (the two open questions of the recorded Cycle-889 history)"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "carry the k-run alignment law (ring form, literal-ground-truth verified, perturbation-controlled) as the standing period instrument at algebra level; carry the bank/edge identity algebra; every corpus-scoped statement (transport anatomy, incidence tables, holdout predictions, carrier classes, residuals) is recorded history awaiting the unlanded stack"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "Result 1 is pure integer algebra over its declared sweep; Result 2 is a combinatorial law verified against a literal ground truth on randomized cells with controls; neither certifies any statement about the recorded corpus, its mechanism, or its holdout predictions"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exhaustive integer sweeps, two independent ground-truth implementations on distinct seeds, a breaking perturbation control, and an even-parity structural check; no corpus input is read"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, stipulated definitions, open

### Stipulated definitions (declared scope inputs)

- the declared identity sweep ranges (`B = 3..8` primary; `B = 3..60`
  checker);
- the declared randomized k-run cell family.

### Imports

- none. The input closure contains no repository file beyond the
  paired runner/cache pins.

### Derived (conditional on the stipulations)

- the four bank/edge identities with the entry-gap equality;
- the cyclic k-run alignment law with edge cases, parity fact, and
  perturbation control.

### Open

- the corpus mechanism question in full (transport anatomy, incidence
  tables, co-occurrence, the carrier classes) — waiting on the
  unlanded stack;
- the recorded P=32 carrier mechanism and the recorded 40/48
  residuals — history, uncertified;
- a genuinely pre-registered (externally timestamped) holdout
  protocol, if the prediction exercise is ever to carry blind-holdout
  force.

## Verdict

The algebra and the law survive on their own: four identities that
hold everywhere they are defined, and a run-counting formula that a
literal scan confirms on every randomized word, with the perturbed
formula failing exactly as a control should. The story around them —
banks owning complements, predictions into unseen corpora, a seal —
was computed on artifacts this tree does not contain and, in the case
of the seal, claimed a cryptographic property the code never had. The
story is kept as history; the mathematics is kept as mathematics.
Independent audit still required.
