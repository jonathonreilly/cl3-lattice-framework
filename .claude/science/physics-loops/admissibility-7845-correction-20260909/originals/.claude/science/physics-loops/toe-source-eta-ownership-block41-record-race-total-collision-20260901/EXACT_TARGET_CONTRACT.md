# Exact target contract

## State and generator

The state domain is the set of finite, well-typed Block-38 `Carrier` maps on
`Z^3`, including arbitrary unions, overlaps, mixed frames, turns, spent
archives, and states with no active transaction. Records are permanent.

Every ungranted `H` determines the finite set of sites that one complete
Block-38 trial would write. A head is grant-ready exactly when that footprint
is blank and no already-recorded `T` grant owns an intersecting footprint. It
contributes the unchanged deterministic `H -> T` row at rate one. A `T`
carrier is a grant only when its reconstructed source `H`, frame, and protocol
match literally.

For every grant, evaluate the unmodified Block-38 proposal function only on
the Record restriction to that owner's head and footprint. Admit a returned
row only at the source-declared next site inside that footprint. A row
contributes one generator term at its inherited rate with its complete source-
declared normalized measure. Let

```text
Gamma(C) = number of ready ungranted heads
           + number of admitted owner-filtered continuation rows.
```

For `Gamma(C)>0`, the embedded jump law is the rate-weighted mixture over all
grant and continuation rows. For `Gamma(C)=0`, the state is absorbing. No
enumeration order, random tape, claimant sidecar, auxiliary lease, owner id, or
synchronous phase is part of the state or law. Ownership is reconstructed
from ordinary permanent `H/T` Records and the declared footprint map.

## Completion witnesses

- exact singleton equality with the imported Block-38 trigger and every
  continuation row through one full trial;
- an explicit two-head overlapping-footprint race with distinct trigger sites,
  followed in both winner branches to permanent loser absorption and an
  unchanged full winner transcript;
- exhaustive head-pair overlap census across all 24-by-24 frame pairs and every
  relative displacement whose finite footprints intersect;
- chain, clique, same-trigger, distinct-trigger, turn, and mixed-protocol
  components of multiplicity greater than two;
- exact rejection of every cross-front hybrid parent proposal;
- exact normalization of every enumerated row and the arbitrary-finite
  exponential grant-race identity;
- covariance of footprint graphs, grants, rates, and output measures under all
  24 proper-cubic rotations and nonzero translations;
- permutation/order independence and no-overwrite checks;
- separated-component generator decomposition;
- an explicit conservative linear rate bound `Gamma(C) <= B |C|`, one Record
  per jump, and the resulting pure-birth nonexplosion proof;
- normalized finite path/cylinder densities and prefix marginalization;
- the same construction for several exact `lambda` values, proving collision
  totalization does not select the response parameter.

## Forbidden weakenings

- do not replace literal Block-38 rows by a different entanglement-breaking
  law or finite six-axis law;
- do not supply the claimant subset, lease family, priority order, or collision
  weights to the runner;
- do not STOP every collision, overwrite a site, erase/modify old Records, or
  allow parents from two transaction owners to create one row;
- do not call a finite motif census the total theorem without the generator
  formula and nonexplosion proof;
- do not call first-grant absorption elastic scattering or lineage survival;
- do not claim the axioms select the rate, `lambda`, occurrence semantics, or
  physical time unit;
- do not claim audit, owner adoption, source/gravity closure, obligation
  retirement, or TOE percentage movement from an author-side result.
