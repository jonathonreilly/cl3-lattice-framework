# Preflight Support Correction

This correction was frozen after an independent preregistration-only attack
and before adjudicating or committing the Block-16 primary result.  It narrows
one sentence in `PREFLIGHT_WITNESSES.md` without changing the registered
43-site writer, its six outputs, its weights, or the Block-15 controller.

The sentence "No branch needs a site outside it" applies only to each writer
output `sigma_f`.  It does **not** apply to the subsequent Block-15 transport
controller.  At the generated candidate `2f`, that controller has global
source sites

```text
3f and 2f+e for the four e perpendicular to f
```

and global destination sites

```text
4f and 3f+e for the four e perpendicular to f.
```

The five sources are in the common writer block `B`; the five destinations are
outside `B`.  Across all six signed fronts, the external destinations are six
sites of type `4f` and 24 sites of type `3f+e`.  They are mutually distinct and
disjoint from `B`, so the common support counts are

```text
writer support B                         = 43 sites
external controller destinations         = 30 sites
writer-plus-controller extension         = 73 sites
external destination conditions/branch    = 5 sites
```

Accordingly, the registered `2,688 = 6*14*32` direct controller maps must be
interpreted on a 73-site tensor extension carrying those post-writer
destination conditions.  The Block-16 generated length-two seeds directly
contribute `6*31 = 186` nonempty-obstacle components and 5,166 complete
frontier evaluations.  The `2,976 = 6*16*31` components and 171,936 frontier
evaluations remain legitimate frozen Block-15 regression coverage over trail
lengths 2 through 17; they are not all newly generated Block-16 components.

This support correction does not falsify the registered effective writer or
its direct composition.  It does forbid any claim that the complete composed
controller acts inside `A_B`, and it makes the already-open locality and
nearest-neighbor compilation obligations more explicit.
