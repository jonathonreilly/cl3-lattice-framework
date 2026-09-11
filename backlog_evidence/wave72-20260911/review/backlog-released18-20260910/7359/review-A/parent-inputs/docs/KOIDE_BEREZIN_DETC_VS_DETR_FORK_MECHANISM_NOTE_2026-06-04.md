---
claim_id: koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04
claim_type_author_hint: bounded_theorem
claim_scope: >
  Under POLARIZATION-SELECT, this note proves the exact four-cell det_C-vs-det_R
  fork algebra on R[Z_3] = R (+) C, yielding real => r = 1, Q = 1 and
  holomorphic => r = 1/2, Q = 2/3 while preserving the unconditional boundary
  that no route here selects the polarization.
---

# Koide Berezin det_C vs det_R Fork Mechanism

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** bounded_theorem (conditional mechanism / route-pruning support)
**Status:** source-only bounded conditional theorem. This note does not approve
a new axiom, primitive, admission, or verdict. It records exact conditional
algebra for a tested four-cell fork: real versus holomorphic polarization,
crossed with Gaussian versus Berezin statistics.
**Primary runner:** [runner][runner]
**Cached log:** [runner cache][cached-log]

[runner]: ../scripts/berezin_detc_detr_fork_2026_06_04.py
[cached-log]: ../logs/runner-cache/berezin_detc_detr_fork_2026_06_04.txt
[lever-note]: KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md
[block-count-note]: KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md

## Safe Statement

The bounded claim is conditional. On the generation algebra
`R[Z_3] = R (+) C`, once POLARIZATION-SELECT supplies either the real or the
holomorphic polarization, the four modeled cells compute exact branch
consequences. The fork separation is that polarization, not Gaussian versus
Berezin statistics, decides the doublet slot count.

This note does not decide which polarization is physical.

## Named Conditional Premises

```text
POLARIZATION-SELECT (named conditional premise): a polarization for the
generation doublet is SUPPLIED: either real (the doublet counts as two real
slots) or holomorphic (the doublet complex structure J is chosen and the
doublet counts as one complex slot). Not derived: no landed route selects a
polarization; this note's four-cell mechanism shows the choice is not made by
moving between Gaussian and Berezin statistics.
```

## Exact Identities

The runner works on the generation algebra `R[Z_3] = R (+) C`. It verifies the
real and complex block decompositions, the doublet projector `P_d`, and the
doublet complex structure `J` with `J^2 = -P_d`.

The determinant/block-count identities recorded here are exact:

- Real determinant count: `det_R(alpha P_s + beta P_d) = alpha beta^2`.
- Holomorphic block count: choosing `J` counts the doublet as one complex slot.
- Real Gaussian doublet weight: two real modes.
- Holomorphic Gaussian doublet weight: one complex mode.
- Holomorphic Berezin count: one complex mode gives `det_C`.
- Real Majorana Berezin count: two real modes give the Pfaffian real-slot count.

The `Q = (1 + 2r) / 3` lever is the upstream algebra identity from
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md).
That upstream note remains the cited authority for this lever.

## Conditional Chain

Under POLARIZATION-SELECT, the exact per-branch consequences are:

```text
real => r = 1, Q = 1
holomorphic => r = 1/2, Q = 2/3
```

The four modeled cells are:

| action family | polarization | doublet count | result |
|---|---|---:|---|
| real Gaussian | real | 2 real slots | `r = 1`, `Q = 1` |
| Majorana Berezin | real | 2 real slots | `r = 1`, `Q = 1` |
| holomorphic Gaussian | holomorphic | 1 complex slot | `r = 1/2`, `Q = 2/3` |
| holomorphic Berezin | holomorphic | 1 complex slot | `r = 1/2`, `Q = 2/3` |

The tested mechanism is that the `r = 1/2` cell follows from holomorphic
polarization: choosing the doublet complex structure `J` and counting the
doublet as one complex slot. It is not supplied merely by changing from a
Gaussian action to a Berezin action, because the real Majorana Berezin cell
lands on the real-slot count.

## Motivation Exhibit

This section is evidence only; not load-bearing; no value below is consumed by
any claim.

The runner keeps a motivation-tier randomized replay of the
`Q = (1 + 2r) / 3` identity to catch implementation mistakes. That replay is
not proof and is not consumed by the bounded theorem. The load-bearing content
is the exact algebra in the preceding sections.

Any nearest-rational scan, live mass value, literature number, fitted selector,
or imported comparator attached to this fork is quarantined here as
motivation-tier evidence only. No PDG values, fitted parameters, or literature
comparators are consumed by this claim.

## Unconditional Boundary

The unconditional boundary is this note's own demotion record from the
review-loop no-go gate, summarized below; it carries no audit verdict or
publication status of its own:

> It does not claim that no future native route can derive `J`, and it does not
> claim that the complex structure is an axiom or primitive.

## No-Go Discipline Disposition

The submitted branch tried to phrase this as a broader negative claim:
`det_C` is not forced by first-order structure alone. That broad negative did
not pass the review-loop no-go gate as submitted: its N1 section listed four
routes, while the repo rule requires at least five before a no-go can ship.

This landed note is therefore demoted. It does not claim that no future native
route can derive `J`, and it does not claim that the complex structure is an
axiom or primitive. It records only the tested four-cell mechanism and leaves
the positive route open: derive a native polarization selector, or show that
the readout functional factors through the doublet complex-slot quotient.

### 2026-07-07 Recut

This recut re-types the row from `open_gate` to `bounded_theorem`. Any matched
selector value formerly used as route evidence is re-typed as a supplied
premise under POLARIZATION-SELECT, not as a derived or preferred landing.
The conditional algebra above is now the load-bearing claim.

The unconditional boundary is unchanged: no landed route selects a
polarization here, and no closed no-go against future native `r = 1/2`
derivations is claimed.

## Residuals / Open Derivation Targets

- Derive a native polarization selector for the generation doublet, if one
  exists.
- Show whether a readout functional factors through the doublet
  complex-slot quotient.
- Close neither target by changing Gaussian statistics to Berezin statistics
  alone.
- Preserve the open possibility of a future native route to `r = 1/2`.

The related doublet-counting pin is discussed in the
[real-rep block-count note][block-count-note]; this note does not use that
related note as closure, only as context for the same open complex-structure
question.

## Citation Contract

Citation is audit-gated. This source note does not set a verdict, landing, or
publication status.

The upstream authority for the lever `Q = (1 + 2r) / 3` remains
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md).

The safe downstream use is narrow: this note may be cited to say that the
tested action-side fork separates polarization from statistics, and to use the
fork separation result and the per-branch conditional `(r, Q)` values under
POLARIZATION-SELECT. It may cite only these conditionals:

```text
real => r = 1, Q = 1
holomorphic => r = 1/2, Q = 2/3
```

It may not be cited as a closed no-go against all future `r = 1/2` derivations.

## What This Does Not Claim

- It does not adopt the holomorphic polarization.
- It does not establish a charged-lepton mass prediction.
- It does not use PDG values, fitted parameters, or literature comparators.
- It does not assert that `Q = 2/3` is impossible to derive natively.
- It does not classify the doublet complex structure as an axiom or primitive.
- It does not edit generated ledger, queue, or publication-status files.
- It does not derive or prefer a polarization; POLARIZATION-SELECT may not
  be cited as decided or derived.

## Verification

Run:

```text
python3 scripts/berezin_detc_detr_fork_2026_06_04.py
```

The runner is deterministic and offline. Load-bearing checks determine the exit
code and final `TOTAL` line. The seeded randomized replay is printed only under
the motivation-tier banner and cannot affect exit status.

Expected clean stdout closes with:

```text
LOAD-BEARING CHECKS: PASS=35 FAIL=0
MOTIVATION-TIER (non-load-bearing; does not affect exit status)
MOTIVATION: PASS=1 FAIL=0
TOTAL: PASS=35 FAIL=0
```
