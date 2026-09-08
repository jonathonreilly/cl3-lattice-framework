# Post-execution PR check

Two directly relevant PRs appeared after the Block 43 preregistration commit
and before packaging. They are bound here rather than silently rewritten into
the frozen prior-art expectation.

## PR #7831

Observed head: `ff8573cf054125db0dd0fcf07dba131280b6b736`.

The one-site graded Record cell forces the Lüders effect only under the
separately declared operational premise that outcome Kraus operators are
parity-even. On a two-mode cell the same note exhibits a four-real-dimensional
effect family and two complete even instruments with the same output but
different effects.

Impact on Block 43: the two-mode writer remains a valid exact construction,
but it is an existence repair, not an instrument-selection theorem. Block 43
must not say that grading, evenness, or Record permanence uniquely forces its
fair-complement instrument.

## PR #7832

Observed head: `9301c509842ea4835def91ad50f41bfd4f80ab1c`.

Under the declared grading, arbitrary directional one-site cubic response is
not parity-even; requiring even-faithful rank-one one-site response kills the
vector coefficient. The first-order structure relocates to even hopping
channels, where cubic equivariance leaves a six-dimensional family and no
Clifford relation is selected.

Impact on Block 43: this independently confirms that the compatibility issue
is architectural rather than confined to one measurement formula. Global
grading has a real migration cost, and the two-mode repair does not close the
separate hopping-channel or dynamics selector.

## Novelty decision

Neither PR states the complete cross-PR decision packet. However, the
post-execution repository search found the projector-span and commutant facts,
the even two-mode logical carrier, the ordinary/graded product twins, and
closely related preparation channels already distributed across prior work.
The surviving novelty is the conditional application, the particular
fair-complement writer, the common axiom kernel, and the owner migration
matrix. That is useful architecture-decision work but not a new retained hard
result. The independent hostile audit therefore assigns `BACKLOG`, with
`hard_impact_gate: FAIL` and `shipping_decision: BACKLOG_NO_PR`; see
`POSTEXECUTION_NOVELTY_AUDIT.md`.
