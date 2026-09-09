# d = 3 Bar-Window Measurement: Frozen Protocol Delta

**Date:** 2026-07-11
**Status:** design delta only; no measurement or derivation — FROZEN
2026-07-11 at supervisor authorship. This memo inherits the complete
route-C protocol of
[`docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md`](D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md)
(the parent frozen memo, protocol hash
`c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e`)
and changes ONLY what is stated here. Nothing else in the parent
protocol — geometry, Hamiltonian form, preparation, fragment
partition and tensor orders, the four certification gates with the
trajectory-t0 excess anchor, the pair subgrid, the lazy X rule, the
theta map, the doublet control-and-diagnostic role, machinery
tolerances, checkpoint/resume/report identity — is altered.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege
the Z basis, by construction.

No formation rule.

Sets no audit status.

## Why this delta exists (measured basis, declared)

The 2026-07-10 bar-location run
([`docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md`](D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md),
PR #5144) measured that the comparator has TWO physical quantities
where the parent protocol assumed one: the bar location
(theta* ~ 0.50, insensitive to lambda and delta where certification
fires) and a certification WINDOW in the transverse field (the
opposite-pair conditional dependence crosses the 0.02-bit
independence gate between lambda = 0.10 and 0.20; measured trend
C_55 = 0.005 / 0.017 / 0.060 at the content peak). The parent's
every-lambda completeness gate conflates the two. This delta makes
both first-class: certify where independence permits, gate on a
predeclared minimum window, and report the closure as a measured
boundary. The lambda set is extended DOWNWARD with 0.02 as the
strongest available test that theta* is a threshold in theta rather
than a clock reading: weak field changes the exterior scrambling rate
while leaving the J-scale write mechanism alone, so a stable theta*
under that change is evidence the bar is load-bearing. lambda = 0.20
REMAINS commissioned and is allowed to fail lawfully — its failure
mode is this protocol's boundary measurement, not a missing cell.

## Delta 1 — commissioned lambdas

`lambda in {0.02, 0.05, 0.10, 0.20}` (four traces). All grids,
subgrids, deadlines, tolerances, and the headline delta = 0.10 are
inherited unchanged. The dt-halving machinery trace stays at
lambda = 0.10 on `Jt = 0:0.05:1.10` with the inherited gate
(no-event-on-both passes as physics absence; event mismatch fails).

## Delta 2 — the certified window and the completeness gates

Define the **fully certified set**

`W_full = { lambda : at EVERY delta in {0.05,0.10,0.20} the trace has
a first certification-subgrid hit with R_ind >= 2 by Jt <= 1, AND the
headline (delta = 0.10) event persists >= 3 consecutive certification
samples }`.

- **CHECK-03 (window existence and locality).** Requires
  `|W_full| >= 2`; the shell causal ordering
  `t_face <= t_edge <= t_corner` at every commissioned lambda
  (vacuously true where nothing crosses); and the inherited
  requirement that every fired headline event name its witness pair
  and pass the drift gate. Fewer than two fully certified lambdas is
  physics absence: **BAR-NOT-PINNED**.
- **CHECK-04 (tolerance and field stability inside the window).**
  Over `W_full` only: for each delta, the median theta* must be
  finite and positive, and
  `max_delta median / min_delta median < 1.5`; ADDITIONALLY the
  headline theta* values over `W_full` must satisfy
  `max/min < 1.5` (field stability — new). Any failure:
  **BAR-NOT-PINNED**.
- **CHECK-05 (bar location and boundary report).** At headline delta,
  print theta* for each lambda in `W_full`, their median and range,
  and the inherited `inside` / `BAR-BELOW-WINDOW` label per event
  (flag, never a verdict class). ADDITIONALLY print the **boundary
  report**: the certified window `W_full` as a list; the boundary
  bracket `(max certified lambda, min non-certified commissioned
  lambda above it)`, or `not-bracketed-above-0.20` if every
  commissioned lambda certifies; and, if `W_full` is not contiguous
  in the commissioned ladder, the flag `NONCONTIGUOUS-WINDOW`
  (reported, not gated). The boundary is a measured OUTPUT; no gate
  consumes it.

Verdict wiring is inherited: machinery or CHECK-01 failure is
MACHINERY-FAIL (exit 2); CHECK-02, CHECK-03, or CHECK-04 failure is
BAR-NOT-PINNED (exit 1); otherwise BAR-DERIVED-EFFECTIVE (exit 0)
with the window, boundary bracket, theta* median, and flags on the
TOTAL line. Physics absence is never MACHINERY-FAIL. No lambda,
delta, deadline, or tolerance may be dropped or reweighted after any
physical row is inspected.

## Delta 3 — cost model and preflight recalibration (declared)

The exact frozen schedule: main Z rows `4 x 101 = 404` at `3.5u`;
pair-subgrid rows `4 x 17 = 68` at `7.5u`; dt-halving `23 x 3.5u`
plus `23 x 7.5u`; X demolition worst case `4 x 11 = 44` at `10u`;
Z and X doublet baselines `4 x 2 x 21u`. Total **2785u**.

The parent's planning unit (`21.33 s`, the 2026-07-09 pilot cadence)
is superseded by the MEASURED realization of this exact machinery:
the 2026-07-10 run completed its frozen 2152u schedule in 17,818 s,
i.e. **8.28 s per unit**. The preflight keeps the parent's live
mechanics — time one k=4, one k=5, and each q=9,10,11 gather on the
live cube state, calibrate the unit as the maximum of the measured
per-weight times and the declared floor — with the floor recalibrated
to `8.28 s`. Projection at the floor: `2785 x 8.28 s + 0.7 h reserve
= 7.1 h`. The refusal gate is inherited unchanged: projected wall
<= 13.5 h and projected RSS <= 8 GiB or `--full` refuses as
MACHINERY-FAIL; the live 10 GiB RSS guard and the 14 h wall cap are
unchanged.

Validation wall allowance is raised to **30 minutes** (declared): the
new campaign cache directory starts cold and the four ground-doublet
Lanczos builds (including the new lambda = 0.02, whose doublet is the
most degenerate) dominate the first validate. The lambda = 0.02
doublet is deliberately built and gated in validate, BEFORE launch,
so an eigensolver convergence problem surfaces as a pre-launch
machinery failure, never mid-run.

## Delta 4 — artifacts

Runner: `scripts/d3_bar_window_measurement_2026_07_11.py`, a FORK of
the parent runner
[`scripts/d3_bar_location_measurement_2026_07_10.py`](../scripts/d3_bar_location_measurement_2026_07_10.py)
carrying exactly the deltas in this memo and nothing else — the
review surface is the diff between the two runner files. The parent
runner file is not modified (its committed streams and caches remain
byte-reproducible for PR #5144 review).

Cache directory: `logs/runner-cache/d3_bar_window_checkpoints/`.
Streams: `lam_0p02_...`, `lam_0p05_...`, `lam_0p10_...`,
`lam_0p20_observables.jsonl` and `dt_half_lam_0p10_observables.jsonl`.
Ground caches: `ground_doublet_3x3x3_lam_0p02.npz` (and the three
inherited names) in that directory. Schema literals:
`d3-bar-window-observable-v1`, `d3-bar-window-checkpoint-v1`,
`d3-bar-window-ground-doublet-v1`,
`d3-bar-window-preflight-v1`. `protocol_hash` = SHA-256 of THIS
frozen memo's UTF-8 bytes; the parent memo's hash is additionally
recorded in every artifact as `parent_protocol_hash`. The six-line
stdout contract, the three boundary sentences on every surface, JSONL
append+fsync, atomic checksummed checkpoints, resume refusal on any
identity mismatch, and `--report` regeneration are inherited
unchanged, with the TOTAL line extended by
`window=[...] boundary=(...)`.

## Risk signatures (inherited plus one)

The parent's five risk signatures are inherited unchanged. One is
added:

6. **Window noncontiguity.** If lambda = 0.02 fails full
   certification while larger lambdas pass (e.g. the weak-field
   dynamics is too slow for the Jt <= 1 deadline at some tolerance),
   `W_full` is noncontiguous or bounded below. The exact observables
   are the per-delta first-hit times and the per-lambda gate ledger
   at lambda = 0.02. This is reported with the NONCONTIGUOUS-WINDOW
   flag and both brackets; it does not change the verdict class by
   itself (CHECK-03/04 still decide). A slow-write signature at
   lambda = 0.02 (content rising but late) is quoted as measured; no
   deadline extension is permitted.

## What a positive and a negative buy

Positive (BAR-DERIVED-EFFECTIVE): the registration bar's effective
location on Z^3 in this declared comparator, theta* with median and
range, tolerance- and field-stable across a MEASURED certified
window, with the window's noise boundary bracketed — the
protocol-complete successor to the 2026-07-10 existence result.

Negative (BAR-NOT-PINNED): the certified window is smaller than two
commissioned lambdas, or theta* is tolerance- or field-controlled —
either of which demotes the 2026-07-10 theta* ~ 0.50 reading from
"location candidate" to "single-window observation" and names the
next obstruction exactly.

## Boundaries

Inherited verbatim from the parent memo, including: conditional on
the standing quantum-Darwinism record reading; all comparator inputs
declared, none derived; not basis-neutral; finite volume,
finite-time persistence only; no formation rule; sets no audit
status.
