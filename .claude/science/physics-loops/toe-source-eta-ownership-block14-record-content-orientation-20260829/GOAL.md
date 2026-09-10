# Goal

Source/Eta Block 14 attacks the exact reflection ambiguity left by Block 13.
The all-or-none five-cell controller is safe for every static obstacle pattern,
but identical Record flags alone select both ends of a finite straight trail.
This block tests whether the **signed front already present in locked Record
content** supplies the missing local arrow through one fixed covariant coarse
decoder, without an 84-entry codebook or host direction.

This is an effective framework-level Record-readout target.  It does not claim
that the current full-rank nonorthogonal one-qubit representatives are perfectly
distinguishable by an ordinary POVM.  Microscopic pointer/control, seed
generation, concurrent fronts, occurrence rate/time, and gravity remain
separate unless explicitly constructed.

## Frozen Record code and decoder family

Keep the Block-12 code unchanged:

```text
g = 9/16,
epsilon = 1/256,
r_(f,b) = -g f + epsilon s_b,
```

where `f` is one of six signed coordinate axes and `s_b` is one of fourteen
axis/corner outcome directions.  Freeze the coarse decoder

```text
D(r) = the unique d in {+/-e1,+/-e2,+/-e3} with d^T r < -1/2,
```

returning `None` unless exactly one such `d` exists.  Runtime may call this
fixed half-space functional only on locked Record content.  It may not call or
construct the Block-12 `(f,b)` codebook, compare against 84 targets, receive
`f` or `b` from the host, or decode the old outcome.

The runner must prove exact robustness, not sample it:

- for the true front, `f^T r_(f,b) <= -143/256 < -1/2`;
- for every other signed axis, the negative component is either absent or has
  magnitude at most `1/256`;
- the decoder is unique for all 84 contents and covariant under all 24 proper
  cubic rotations;
- every threshold `tau` with `1/256 < tau < 143/256` gives the same decoder on
  the registered code, while runtime remains frozen at `tau=1/2`.

This derives decoder stability from the constructed code.  It does not claim
that the minimal Record axiom uniquely selects this downstream readout law.

## Content-oriented eligibility

For a no-Record candidate site `x`:

1. require exactly one nearest-neighbor Record at a site `p`;
2. compute `f=D(c(p))` from that Record's locked content;
3. require `p=x-f`, so the decoded arrow agrees with predecessor displacement;
4. require a Record at `x-2f`;
5. require the other five nearest-neighbor sites to be no-Record.

The probability stage then receives the actual six neighboring `M2` contents
and uses the unchanged fourteen-way Block-09 law.  The decoded `f` is geometry
for eligibility and guarded transport; the old outcome never enters the
probability or controller.

## Frozen obstacle controller

Retain Block 13's five destination pairs and all-or-none guard verbatim.
Conditioned on formation and realized outcome:

- write `r_(f,b)` at `x`;
- if all five destination Record flags vanish, execute all five disjoint
  nearest-neighbor SWAPs;
- otherwise execute identity on every source/destination content;
- never move a pre-existing Record and never partially transport the packet;
- assign blocked probability mass to the local terminal `(b,STOP)`.

No public runtime input supplies `f`.  The post-stage must consume only the
front produced internally by content-oriented eligibility.

## Exhaustive target

The primary runner must cover:

- all 84 Record contents and 24 proper-cubic frames;
- all six fronts, all fourteen left-end and right-end outcome contents, and
  trail lengths two through nine (`6 x 14 x 14 x 8 = 9408` trail cases);
- the complete no-Record frontier adjacent to every registered trail, proving
  exactly one eligible forward candidate and rejection of the reflected and
  every lateral candidate;
- all `6 x 14 x 14 x 32 = 37632` guarded controller cases with exact clear
  successor, blocked identity/permanence, fixed packet size, and normalized
  continue-or-STOP mass;
- after each of the 31 blocked patterns, the complete local frontier of the
  trail plus new Record plus obstacle layer.  If a candidate has a unique
  obstacle predecessor, exhaust all six possible decoded directions for that
  obstacle.  Require zero eligible continuation sites in that local component;
- source/AST scans excluding a codebook, host front/outcome, role, epoch, site
  ID, scheduler, global time, target fixture, or same-event probability
  feedback.

The structurally independent checker must import neither the Block-14 primary
nor the Block-13 primary and must use a longer trail range.

## Prospective adjudication

Exactly one terminal must be returned:

- `CONTENT-ORIENTED-SAFE-FRONT`: the fixed decoder is exact/covariant and
  outcome-independent; every unblocked finite trail has exactly one oriented
  tip; every guarded clear/blocked case is safe and normalized; and every
  blocked registered local frontier has zero eligible continuation;
- `EFFECTIVE-ORIENTATION-ONLY`: the algebra works only by importing an exact
  content functional, codebook, host front, supplied endpoint selector, or
  noncovariant chart beyond the frozen fixed decoder;
- `CONDITIONAL-HALO`: any reflected/lateral continuation survives, any blocked
  local frontier remains eligible, or safety still needs an external
  scheduler/clearance oracle;
- `NO-MEMBER`: the fixed half-space decoder fails on the registered 84-state
  code or cannot compose with the frozen guarded map.

Even `CONTENT-ORIENTED-SAFE-FRONT` is an effective single-lineage result from a
supplied oriented two-Record seed.  It is not microscopic pointer closure,
simultaneous-front confluence, a rate/clock, gravity, or TOE completion.

## Hard falsifiers

- flip any decoded direction by changing the outcome label;
- produce two decoder directions or none for any registered content;
- fail proper-cubic covariance or threshold-margin inequalities;
- accept the reflected endpoint or a lateral candidate;
- use an `(f,b)` dictionary, old outcome, or host front in runtime;
- leave any registered local continuation eligible after a blocked event;
- move one occupied Record, execute a partial packet, or lose STOP mass;
- claim perfect ordinary one-site POVM readout, generated seed, microscopic
  control, interacting-front confluence, site/rate/clock, gravity, an axiom
  amendment, obligation retirement, or TOE movement.

## Frozen authority

- Block-13 delivery `96d25272f5b09a4a2743836f7a1a6d14e2b99771`;
- Block-13 science result `88cd67d464c9da93fbb025c1f9943d14376ad267`;
- observed `origin/main` `3cc632921c36aa90266c5c62e56816577ce59a0a`;
- minimal-axiom blob `bc23300becfe4e4db57153c0e94cfcdf2338da71`;
- Block-13 note/primary/independent/primary-cache/independent-cache blobs
  `bfcd86b9a6c5f60c151b8f4addc94efd00f33f11` /
  `ab7f5fb3ddde7ff81f754a04ad5ac0a95f68a6f4` /
  `2b4e89f591d5fce52e0a5ff6999b2f189cb18f7a` /
  `acb7550bbb793ac492e5853eb334f7b6823312e8` /
  `b333bfe59b40f49dfbe884db18a8e5296d803588`;
- Block-13 panel and N1--N8 blobs
  `1017524fb02f47e5bd80c39b264de875504c8e74` /
  `9b75b26d7541a80bf32aede51ac6d967b31e4612`;
- latest inspected connection PR `#7799`, head
  `6a28cea23935c254fe070fb27027217b40cf9c91`, retained as portfolio context
  only and not a proof input.

## Accounting

This preregistration authorizes no minimal-axiom edit.  Formal obligation
retirement and TOE percentage movement remain zero unless a later independent
audit ratifies an applicable closure.
