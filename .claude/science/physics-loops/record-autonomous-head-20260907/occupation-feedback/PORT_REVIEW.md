# Cold portable occupation-feedback review

Reviewed staged primary0403cafafc0123ae78398fe906defc89d3a000f6de7614bf0dc94a8634545737
and orbitaleb042088d2750055f4f3435a328e7713495779320df3f72ac581d617beace7e6.
Reviewer authored the independently frozen scratch70d calculation, but did not
author this port, its live binding or the independent orbital implementation.
This is independent review of that portable delta, not a fresh cold derivation
of the original mathematics. No source was edited.

## Positive findings

Primary45rows, summary, census, traps, initialQoccupation weights/moments,
292configuration records and mutation controls are EXACTLY equal to immutable
primary scratch output. No formula, fuel or parameter drift was found. The
conditionalQ ledger remains separately computed; it is not replaced by the
unconditional initial energy. Scope correctly identifies fiber occupations in
the emitted normal output. All45poststates,292configuration-prefix records,
46trap-prefix aggregates and complete reach/terminal mass are genuinely live
compared. The independent checker imports no primary helper. No saved JSON,
scratch path or stale literal source hash is used as live evidence.

A fresh staged-primary --json invocation passes with residual1.258e-12 in8.76s,
102.8MiB; pure JSON parsed successfully. Six built-in corruption controls pass.
The current-threshold margin.0010624 safely exceeds comparison error.

The orbital temporary-array repair changes only frequency columns into batches
of8; quadrature nodes, weights, orders and cell counts stay unchanged. Against
the immutable orbital raw result, all physics and convergence fields differ
by at most9.77e-15. No180MiB ceiling was relaxed; recorded orbitalRSS is97.97MiB.

## Interface findings requiring narrow repair

1. Scope and exact types are incompletely enforced. Replacing scope with a
   contradictory bare-occupation/nondecreasing-battery claim passes. Resource
   blas_threads=True and floating basis bits also pass via Python equality.
   Require exactSCOPE, integer basis/resource/discrete certificate fields.
2. Time-certificate coverage is not bound to all used rate pairs. The live
   checker emits46certificates, but dropping45 and retaining only the first
   passes. Derive the required canonical rate-pair tuples from every row's
   rate_groups; compare the exact certificate key set and reject duplicates.
3. Reported convergence/residual aggregate fields are not tied to their rows.
   Setting max_ledger_residual=99 passes while the per-row residuals remain
   valid. Recompute all supplied max_* summaries from the corresponding rows,
   and enforce their intended nonnegative tolerances/types.
4. Per-initial-occupation terminal decompositions are checked only to sum1,
   not against the exact configuration census. Changing the first occupation's
   terminal depth to12 passes, even though this law's maximal depth is5.
   Reconstruct the exact terminal(depth,class)->Fraction distribution for each
   initial bits value from the already compared configuration records and
   terminal rate-zero condition. Reject duplicate/missing/incorrect per-initial
   entries; normalization alone does not certify the reported distribution.

These are demonstrated validation-contract gaps, not observed errors in the
actual scientific outputs. The292exactconfiguration records and46aggregate
trap rows already agree. Repair should touch only the interface and add each
reproduced mutation; no numerical or resource-threshold change is needed.

Evidence: port-review-live.json in this directory; previous immutable source
and result artifacts remain unchanged. No recommendation to retune physics,
repeat the feedback experiment or broaden its scientific claims follows.

## Authorized repair (not independent self-review)

Root subsequently authorized the staged-primary-only interface repair. Exact
scope and resource/basis integer types are enforced; all46 ordered rate-pair
certificates must match the set derived from the compared row rate groups,
without duplicates. Row maximum residual/convergence summaries are tied exactly
to their source rows. Per-initial terminal distributions are now reconstructed
with exact Fractions from the already matched configuration records and actual
zero-rate traps, including exact depth and dark class. Sixteen mutation controls
include the reproduced scope/type/missing-certificate/false-summary failures,
duplicate/invented time certificates, and depth12/duplicate/omitted terminal rows.

All45physics rows, summaries, census, traps, initialQ weights/moments,292records,
controls, fixture and law are exactly unchanged from the pre-repair live output.
Root must inspect this repair delta independently; this author does not label
its own fix an independent final review. Evidence port-fixed-live-final.json
is separate from the original immutable port receipt/history.
