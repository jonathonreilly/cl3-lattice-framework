# Original #6017 Cycle-947 correction history

This packet preserves the original H0-discharge campaign and replaces its
active authority with a small self-contained statement of the implications
that survive the focused review.

## Original boundary

- Original head: `526acddf6295b4df6bfec3d41f3066d7b9725cfd`.
- Raw authored parent: `b0626d59ac9baf9f7047f2a4aa3a4ea6f5074614`.
- Author repair base: `e97ff2fd204611f4091c4b664664dba7c263da65`.
- Original review report SHA-256:
  `f3072f3d493136dba28b372e8e7cc09e3c4575412209206caca70c3cb91ab63d`.
- Original review receipt SHA-256:
  `a2d8af743475dae5034d289efca5177fd8d3458d068937f8c08a9356288db807`.

The complete 106-file review directory is copied byte for byte under
`review-packet/`. Its 105 receipt artifacts, eight original endpoint bodies,
twelve intermediate bodies, six raw commits and patches, and 57 recovered
input blobs remain historical evidence. `SOURCE_PRESERVATION.json` verifies
those identities. The scoped Git attribute marks only the exact raw patch
copies as binary for diff presentation; it does not alter their bytes.

## Review corrections

The replacement applies all five findings.

- H1: bitwise lane locality is retained as a compiler-grammar implication.
  A lane is an independent bit coordinate, not a forced physical lattice
  site. The accepted statement `c[1] ^= c[0]` explicitly shows coupling
  between wire components inside one lane.
- H2: a proper-cubic box-isometry search is only a result about that supplied
  subgroup and an explicitly supplied injective lane/site map. An identity
  rule commuting with one local flip on all eight three-bit states refutes the
  inference that covariance determines the full automorphism group.
- H3: trajectory independence is conditional on fixed external choice words.
  A four-point external seed gives a lane-local update whose output
  probability changes exactly from `1/4` to `3/4` with a neighboring
  condition. No cross-lane deterministic gate is logically required for that
  distributional dependence. A Bernoulli menu has two supported outcomes only
  for `0 < mu < 1`.
- H4: static control-to-target reachability is an overapproximation. The
  program `x ^= y; x ^= y` has a graph path from `y` to `x` and no net
  dependence on `y` on any Boolean input. No minimal semantic cone or local
  screening theorem is retained.
- H5: the obsolete 719/import/AST-lift campaign, moving axiom read, historical
  numerical census, and contradictory append-splice summary are not restored
  as current evidence. Equal gate multisets are shown by a self-contained
  two-CNOT example not to determine an ordered composed map.

The finite facts do not identify lanes with physical sites, choose an external
probability law, supply a one-site domain/action bridge, establish a universal
symmetry classification, or select a unique successor. The original clause
count is preserved as historical bookkeeping and is not a progress measure.

## Current evidence plan

The primary and checker use the two original runner filenames but no legacy
imports. The primary has no repository inputs. The checker independently
recomputes the finite implications and reads only the exact primary source and
its fresh cache. Each final entrypoint runs once under a 30-second, 2-GiB
process-group bound with one-thread BLAS-family environment variables.

No original controller campaign is replayed. No current Cycle-878 source,
axiom, reserved dependency, planning surface, GitHub state, main branch, audit
data, or audit verdict is changed by this author worktree.
