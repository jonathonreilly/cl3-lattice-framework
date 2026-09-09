# Original #5951 Cycle-891 correction history

This packet repairs the current evidence and provenance for original PR
`#5951` without reviving its historical corpus mechanism or holdout claims.

## Boundaries

- Original head: `ff333ef2285617a6ac6fdcb1fe0c623db786b896`.
- Raw authored parent: `2d3f825736e57b0dda2e9ee619064cbbc94d739b`.
- Author repair base: `e95f5d76d7d2a0595b6e5ef0d5782ee84fe48daa`.
- Original review report SHA-256:
  `b9f37f462e4b1f25ede9542fbbac25209d8a17ace85b308c7d3cfe1f755cf544`.
- Original review receipt SHA-256:
  `f12fcab0208c322dfa9e58db19f889e2c23c3ee52111a5033a3e0727064cf0d0`.

The full sealed review packet is copied byte for byte under `review-packet/`.
It contains the eight original endpoint bodies, the eight current bodies that
existed before this repair, three distinct intermediate bodies, all raw
seven-commit patches and messages, the sixteen recovered historical direct
inputs, and the review's decisive controls. `SOURCE_PRESERVATION.json` binds
the copy to the review receipt.

## Current scientific surface

The current note and primary remain self-contained. They retain only:

- the integer identities implied by `N=8B-5`,
  `delta=8B-13-8e`, and `b=B-2-e`;
- the cyclic mismatch-set formula for the longest good run, including its
  all-good case and even-cardinality fact;
- finite declared sweeps, distinct seeded comparisons, and a breaking
  perturbation control.

The checker's wording now says exactly what its code does: it checks selected
`CLAIMS_JSON` fields used by its predicates. It does not independently
reconstruct or compare the complete science digest.

The original review's exhaustive direct enumeration of all `3,586` binary
word/period cells for `N=1..8` is preserved as review evidence. It is not
relabelled as a new author execution.

## Evidence replacement

The two active caches and three active output receipts predate the current
self-contained runners. They are preserved under `review-packet/current/`
before replacement. The original reviewer also preserved the unchanged
current checker attempt that exited with `1 PASS / 5 FAIL` because those stale
pins and claims were present; that failure is not rerun.

The correction runs the final primary once under a 30-second, 2-GiB external
bound, pins the checker to that exact primary and cache, then runs the final
checker once under the same bound. Runner-written receipts replace the stale
mechanism/check receipts. The block receipt is rewritten as a bounded current
source/evidence inventory with no `SEALED`, blind-holdout, corpus-acceptance,
retained-grade, or audit claim.

The historical 299-second and 577-second corpus programs are not rerun. No
premise, reserved dependency, audit verdict, TOE closure, main branch,
planning document, or GitHub state is changed by this author worktree.
