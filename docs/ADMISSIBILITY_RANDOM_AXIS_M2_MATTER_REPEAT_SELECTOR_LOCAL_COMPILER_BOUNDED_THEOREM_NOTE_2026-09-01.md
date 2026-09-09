---
claim_id: admissibility_random_axis_m2_matter_repeat_selector_local_compiler_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "Conditional on the Block-35 affine/covariant binary response class, the Block-36/37 source-bound randomizer and single-front compiler, a record-faithful pure M2 successor-state attachment, and exact operational repeatability of a second use of the same local axis/effect kernel with no direct first-Record parent, the displayed random-axis measure-and-prepare instrument uniquely selects lambda=1. Its signed-axis pushforward is exactly the Block-37 Haar response, and one radius-one finite-rate local extension realizes the attachment and second use while preserving confluence, covariance, archive screening, and arbitrary-finite active-cut induction. Repeatability and the physical attachment typing are not derived from the four minimal axioms."
runner: scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_corrected_2026_09_09.py
actual_current_surface_status: conditional-support
authority: none
audit_required_before_effective_retained: true
review_loop_used: false
---

# Random-axis M2 matter/repeat selector local compiler
**Correction date:** 2026-09-09

[current axiom memo](MINIMAL_AXIOMS_2026-06-29.md); [corrected Block 37](ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_BOUNDED_THEOREM_NOTE_2026-09-01.md).

All measures, program interfaces, local tables, active quotients and formation rates used below are explicitly supplied mathematical data. The current axiom memo supplies the framework boundary, not these choices. Ordinary expectations and event probabilities here do not restore scalar Record-collection additivity. The original status snapshots, broad mutation counts and prior-campaign claims are historical evidence only. Exact original notes, runners, caches, planning, intermediate versions and referenced inputs are preserved in [the recovery history](../.claude/science/physics-loops/eta-affine-repeat-correction-20260909/HISTORY.md).



**Primary runner:** `scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_corrected_2026_09_09.py`

**Date:** 2026-09-01

**Type:** bounded_theorem

**Classification:** `RANDOM_AXIS_MATTER_REPEAT_SELECTOR_EXACT` on the declared
affine binary-qubit, atomless-Haar-axis, source-bound single-front sector.

**Constitutional effect:** none. This candidate has `conditional-support`; it
has not received an independent retained-grade audit. There is no axiom or
primitive update, no obligation retirement, and **no TOE percentage movement**.
The original pre-landing review history is archived; this correction receives separate affected-source review.

## Result up front

This block constructs a specific conditional *joint local realization* that
the previous three blocks did not construct separately. It starts with one
recorded Haar axis, maps the first binary branch to a candidate qubit successor
under stipulated Record-faithful attachment, and sends that successor—not the
old outcome Record—through a second use of the same axis and the same response
kernel before the active cut closes. This narrows Block-37 seams W1/W6; it does
not retire them.

For a Bloch vector `s`, a Haar axis `a`, a label `b` in `{+1,-1}`, a response
parameter `lambda` and successor-state sharpness `kappa`, define

```text
rho_s                 = (I + s.sigma)/2,
E_b^lambda(a)         = (I + b lambda a.sigma)/2,
I_(a,b)^(lambda,kappa)(rho)
                      = Tr(E_b^lambda(a) rho) rho_(kappa b a).
```

On the full square `|lambda|<=1`, `|kappa|<=1`, these branches form a
normalized covariant completely positive measure-and-prepare instrument. If
the signed output direction is `n=b a`, then forgetting the latent pair
`(a,b)` gives exactly

```text
T_s^lambda(dn) = (1 + lambda n.s) mu(dn),
```

where `mu` is normalized atomless Haar measure on the sphere. Thus the
`lambda=1` member is not merely similar to the Block-37 outcome law; it is its
same measure after the explicit signed-axis factorization.

The candidate successor under the stipulated attachment is
`rho_(kappa b a)`. A second interrogation of that state using the same axis
and same `lambda` kernel has

```text
Pr(b2=b1 | a,b1,successor) = (1 + lambda kappa)/2,
Pr(b2!=b1 | a,b1,successor) = (1 - lambda kappa)/2.
```

The attachment type is fixed independently of those probabilities: the pure
outcome Record `n=b a` denotes the corresponding pure qubit possibility
`rho_n`. Record-faithful attachment therefore gives `kappa=1`; it rejects the
opposite-orientation `kappa=-1` corner. If an independent operational
calibration then requires exact same-label repeatability, the second formula
forces `lambda=1`.

That last sentence is conditional. **Record permanence does not imply repeat certainty.**
The local process executes and exposes the repeat experiment, but
the four [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not require its
answer to be one. This block therefore identifies the remaining decision
cleanly: adopt/derive the physical attachment and repeatability condition, or
leave the affine parameter unselected.

## 1. Exact instrument theorem

For a unit axis, the two effect eigenvalues are

```text
(1+lambda)/2, (1-lambda)/2,
```

and the successor-state eigenvalues are

```text
(1+kappa)/2, (1-kappa)/2.
```

The Choi matrix of a branch is

```text
J(I_(a,b)^(lambda,kappa))
  = rho_(kappa b a) tensor (E_b^lambda(a))^T.
```

Its four eigenvalues are the pairwise products of the two spectra above.
Each is separately affine on the closed `(lambda,kappa)` square and is
nonnegative at all four corners, hence nonnegative everywhere by bilinear
interpolation. The runner checks all 32 exact spectrum/corner cases and a
1,500-case exact Choi/effect/state sweep including pure, mixed, aligned,
anti-aligned, zero, interior, and endpoint controls.

Moreover,

```text
E_+^lambda(a) + E_-^lambda(a) = I,
```

so branch traces sum to `Tr(rho)`. Rotating state, axis, effect, and successor
together conjugates every branch. The runner separately solves the proper-
cubic affine response constraints: the constraint matrix has rank 14 and its
one-dimensional nullspace is the dot product. This is the finite exact
covariance audit of the displayed all-rotation identity, not a replacement for
the analytic identity.

## 2. Haar factorization and convex preparation

Conditioned on `a`, the first branch mass is

```text
p_lambda(b|a,s) = (1 + b lambda a.s)/2.
```

For every bounded measurable test function `f`, antipodal invariance of Haar
measure gives

```text
sum_b integral p_lambda(b|a,s) f(b a) mu(da)
  = integral (1 + lambda n.s) f(n) mu(dn).
```

The runner checks the exact density, normalization, first moment, and fourth
moment. In particular, Haar has fourth coordinate moment `1/5`, whereas the
six-axis cubature has `1/3`. The six directions used to exhaust the finite
rewrite graph are therefore typed only as structural controls. The actual
axis row carries a separate normalized atomless Haar source-measure object,
and a non-cubature point `(3/5,4/5,0)` is bound through the literal downstream
rows. The exact fourth moments distinguish the six-axis control from the Haar law; the original label-only mutation verdict supplies no additional evidence.

For `s=p s0+(1-p)s1`, direct expansion gives

```text
T_s^lambda = p T_s0^lambda + (1-p) T_s1^lambda.
```

Multiplying by the same second-use factor proves the corresponding joint
two-use intertwiner. Thus the parent barycentric `M` survives the factorization
without answer-defining a new quotient. The positive normalized nonlinear
twin `1+(n.s)^3` fails this preparation-affinity test by the exact midpoint
gap `-3/8`; aligned endpoint agreement alone is insufficient.

## 3. What selects the endpoint—and what does not

The two-use calculation gives exact repeatability precisely when
`lambda*kappa=1`. On the closed square that has two same-sign corners:
`(+1,+1)` and `(-1,-1)`. The Record-to-matter orientation is therefore
load-bearing. A first Record whose physical content is the direction `n=b a`
is record-faithfully attached to `rho_n`, which fixes `kappa=+1` rather than
`-1`. Conditional exact repeatability then leaves only `lambda=+1`.

This ordering prevents a circular proof:

1. the effect family and successor family are kept symbolic;
2. the physical Record-to-state orientation is declared and checked without
   using the response probability;
3. the second local read uses the retained state and axis with the same
   symbolic kernel;
4. only the observed/calibrated repeat condition is set to one; and
5. `lambda=1` is solved, rather than inserted.

The independent control evaluates the actual second-read row at selected
and nonselected parameters. Its unchanged repeat-certainty predicate accepts
`lambda=kappa=1` and rejects the nonzero mismatch at interior parameters.
The original imported/singleton/answer-defined mutation labels do not establish
alternative physical processes. Nonselection and supplied attachment remain
explicit assumptions, as above.

The older [autonomous calibration nonselection note (historical)](../.claude/science/physics-loops/eta-affine-repeat-correction-20260909/bodies/a497717d101cfbc197f42393800e845283b155af/AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md)
remains relevant: a same-map or absorbing-Record condition alone does not
calibrate blank-sector formation. Block 38 does not claim otherwise.

The missing direct first-Record parent is a causal-interface property. The successor state encodes the first outcome, so no statistical independence of the two reads is claimed.

## 4. Literal local extension

For one relational proper-cubic frame with forward vector `d`, transverse
vector `t`, and head `H_j=H_0+8j d`, the occupied sites are

```text
T = H-t,     G = H+d-t,  R = H+d,    P = H+2d,
A = H+3d,   F = H+4d,   M = H+5d,   B2 = H+6d,
C = H+7d,   Q_r = H+r d+t (r=1,...,8),
H_next = H+8d.
```

The source-bound active quotient grows as

```text
H -> T -> G
H + G -> R -> P -> A -> F -> M -> B2 -> C -> H_next
          \-> Q1 -> Q2 -> Q3 -> Q4 -> Q5 -> Q6 -> Q7 -> Q8
                              \____/   \____/   \____/   \____/
                                 F        M        B2       H_next
```

`G` is the inherited Block-37 Gaussian/PIT selector pushforward; its parent
continuous normalization and partition are content-pinned and rechecked.
`A` is a Record of the actual Haar axis. `F` records axis plus first outcome
direction. `M` is a separate candidate `M_2(C)` successor carrier containing
the retained axis and Bloch state under the stipulated Record-faithful
attachment; this block does not independently establish it as retained matter.
`B2` is the second result. `C` is value-blind, and the protocol rail—not either
outcome—forms the next active head.

Every displayed causal bond is one lattice edge. The second-read target has
parents exactly `M` and `Q6`. The permanent first Record `F` is two lattice
steps away and is not a parent. The non-cubature actual-axis bind executes

```text
H ... P + Q8 -> A(a) -> F -> M -> B2
```

pointwise for a lawful Haar-source point and reproduces both exact branch
kernels. The hostile `record_relay` changes the second row to read `F` at
radius two and fails its designated causal-firewall gate.

Finite role information and seven real payload coordinates occupy one direct
eight-real `M_2(C)` carrier. Protocol carriers store `(u0,p,u1)` losslessly;
`F` stores `(axis,direction)` and `M` stores `(axis,state)`. The runner checks
912 reachable carrier instances across the codec and rejects an absent or
mixed successor state.

## 5. Generator, confluence, covariance, and history

Every ACTIVE blank target carries one rate-one local term. Continuous source
semantics and finite graph controls are distinct:

- the inherited Gaussian/PIT selector source is normalized by the pinned
  parent source theorem;
- the actual axis source is normalized atomless Haar measure;
- finite Gaussian-bit and six-axis atoms are structural representatives used
  only for exhaustive reachability, diamonds, and codec checks; and
- the first and second binary rows use their exact state-dependent masses.

The reachable one-trial control graph has:

```text
652 states
1,075 directed weighted edges
248 co-enabled action diamonds
0 diamond failures
0 premature dead ends
48 terminal control states
0 source-row normalization/type failures.
```

All legal local event orders therefore give the same terminal control law.
This is exhaustive confluence of the finite six-axis control quotient, not an
enumeration of the atomless continuum. Continuum coverage is the analytic Haar
measure/pushforward theorem plus the typed source schema and non-cubature
pointwise bind.
The analytic source rows are locally owned, and the non-cubature pointwise bind
checks that the actual atomless jump maps into the same downstream schema. The
runner re-executes 1,248 terminal rows across all 24 proper-cubic frames and
two nonzero translations; every localized distribution agrees. It checks 576
nearest-neighbor causal bonds.

The active close projects away axis/outcome/state values from the next head.
Two unequal permanent first-trial archives produce exactly the same
48-row next-trial transcript distribution. The generated support is
`18N+1`; at `N=64` it has 1,153 Records with only the intended shared cut
between consecutive trials. Since the next head has the same protocol type
and the archive is screened, ordinary Markov-kernel induction preserves the
parent arbitrary-finite-history interface. No old Record is erased.

This is a single-front theorem. Multi-front collision/scattering totalization
is not executed, and no lattice-wide result is claimed.

## 6. Current controls and historical mutation evidence

The original eighteen-label controller and transcript are archived unchanged.
`host_schedule` formerly corrupted the verifier's reverse distribution while
leaving the local table unchanged; singleton/imported/answer-defined switches
also manufactured failures without the claimed process change. Those counts
are withdrawn as scientific sensitivity evidence. The corrected verifier
compares the actual forward and reverse two-action distributions.

The primary retains the complete clean finite baseline: the rank-14 class,
1500 CP samples, symbolic Choi spectra and 32 corners, continuous Haar and
joint-affinity identities, actual non-cubature source bind, local second-read
firewall, 652-state/1075-edge/248-diamond graph, 48 terminal transcripts,
1248 covariance rows, 912 codec cases and unequal-archive screening. Cubic
covariance is the encoded role/frame action inherited from corrected Block 37,
not unitary conjugation of a full role-coded M2 payload. The physical qubit
instrument separately has its ordinary conjugation covariance.

The companion's named faults change actual operands/source with clean baseline
conditions. These are scoped controls, not a replacement hostile-count quota.

## 7. Prior-art boundary

Closest repository results supply complementary pieces:

| prior result | supplied there | Block 38 delta |
|---|---|---|
| [Block 35 affine boundary](ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md) | the public affine/covariant response-class boundary | actual random-axis instrument and repeat compiler |
| [Block 36 renewal](ADMISSIBILITY_GAUSSIAN_FAIR_RECORD_MIDPOINT_AFFINITY_HAAR_EDGE_FACTOR_FRESH_PORT_RESET_BOUNDED_THEOREM_NOTE_2026-09-01.md) | fair local randomizer/reset and Haar factor context | candidate successor attachment and same-kernel reuse |
| [Block 37 local compiler](ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_BOUNDED_THEOREM_NOTE_2026-09-01.md) | actual single-front local generator with derived `M/S` | recorded latent axis and matter/repeat extension |
| [physical-state attachment cut (historical)](../.claude/science/physics-loops/eta-affine-repeat-correction-20260909/bodies/6bcca990308cacc2ec32c3c7a8547089cb8bc133/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md) | branch-first CP attachment boundary | joint atomless-axis pushforward and local repeat test |
| [Kraus/isometry bridge (historical)](../.claude/science/physics-loops/eta-affine-repeat-correction-20260909/bodies/259d10937fd1b346cb2ca6f85035e3829acaaa5e/RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md) | supplied controlled-copy/QND realization | no universal selector; different supplied context |
| historical static repeatability results preserved in recovery | exact repeat collapses a supplied binary menu | repeat experiment is compiled into the same source-bound local process |

No novelty is claimed for qubit effects, measure-and-prepare channels, Haar
antipodal pushforwards, repeatability lemmas, or local rewrite confluence in
isolation. The bounded advance is their exact joined bridge under the frozen
parent interfaces.

## 8. Exact consequence and remaining decision

Within the declared candidate class, the block establishes:

- a normalized covariant CP instrument for the full parameter square;
- the exact atomless signed-axis pushforward to `T_s^lambda`;
- preservation of randomized/direct convex preparation and joint two-use `M`;
- an independently typed pure candidate `M_2(C)` successor carrier under the
  stipulated Record-faithful attachment;
- a causally independent same-axis, same-kernel second read;
- conditional unique selection of `lambda=1` from record-faithful attachment
  plus exact operational repeatability;
- a radius-one finite-rate local extension with exhaustive finite-control
  confluence, analytic/pointwise atomless-source coverage,
  proper-cubic/translation covariance, archive screening, and arbitrary finite
  active-cut induction; and
- exact rejection of 18 targeted shortcuts.

It does **not** establish:

- that the four axioms derive the pure Record-to-matter attachment;
- that Record formation or permanence derives repeatability;
- that Nature selects this response family or the repeat condition;
- a total multi-front/full-`Z^3` interacting theory;
- one realized infinite history or an empirical frequency theorem;
- source normalization, units, reciprocal gravity response, or a continuum
  gravity limit;
- an independent audit verdict, obligation retirement, or TOE closure.

Those are live scope boundaries, not a universal no-go. The scientific choice
is now narrower than before: either find a physical derivation/measurement
principle for the attachment and repeat condition, or record them honestly as
additional candidate-law input. More compiler plumbing without that decision
would not select the law.

## Reproduction and current inputs

The corrected primary has a distinct filename and a static, actual import of
the corrected Block 37 helper. Both helper-discovery APIs therefore see the
runtime dependency. Its input union includes both notes, the parent runner,
corrected Block 36 and the current axiom memo, with fail-closed hashes.
Existing accepted original-basename helpers and their consumers remain exact.
The primary and separate companion report only the checks genuinely executed
on their frozen current source; the old historical cache is never restamped.

**Standalone affected-fault checker:** [actual fine-cell, projection and repeat controls](../scripts/audit_companion_eta_affine_repeat_corrected_2026_09_09.py). It imports definitions only and is run separately; this link does not claim automatic companion registration.
