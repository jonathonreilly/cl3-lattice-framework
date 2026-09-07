# Local Auxiliary-Face Conditionals Realize the Gauge Measure Without Postselection

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source note sets no audit
verdict, changes no TOE score, and claims no obligation retirement.
**Direct parent:**
[`U1_RECORD_FACE_LIKELIHOOD_SPATIAL_GAUGE_AND_PHOTON_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_RECORD_FACE_LIKELIHOOD_SPATIAL_GAUGE_AND_PHOTON_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Overlap parent:**
[`U1_RECORD_DISTRIBUTION_OVERLAP_POSITIVE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_RECORD_DISTRIBUTION_OVERLAP_POSITIVE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Current axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Runner:**
[`scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py`](../scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.txt`](../logs/runner-cache/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.txt)

## Claim scope

Let `G=Z_N` and let `T:G->R_{>0}` be a strictly positive, even compact
plaquette weight. The Record-overlap examples of the parents supply such a
`T` on every finite cyclic refinement. On the doubled cubic incidence pattern,
put a link possibility `ell_e in G` at every edge-role site. At every face-role
site put an auxiliary possibility

```text
h_f in {star} union G^4.
```

The four entries of a non-universal `h_f` are ordered by the four edge sites
in that face site's nearest-neighbor star. Choose

```text
epsilon = (1/2) min_(g in G) T(g),
```

and define one local nonnegative face factor

```text
F_f(star; ell_boundary) = epsilon,

F_f(a; ell_boundary)
 = T(curl a)-epsilon       if a=ell_boundary,
 = 0                       otherwise.
```

Then on every finite periodic incidence complex:

1. **Exact unconditional marginal.** Summing the auxiliary at each face gives

   ```text
   sum_(h_f) F_f(h_f;ell_boundary)=T(Phi_f),
   ```

   so the normalized joint distribution

   ```text
   mu(ell,h) proportional to product_f F_f(h_f;ell_boundary)
   ```

   has link marginal

   ```text
   mu_link(ell) proportional to product_f T(Phi_f).
   ```

   No special Record outcome is conditioned on and no auxiliary outcome is
   discarded before the weight is produced.

2. **Nearest-neighbor full conditionals on support.** At a face, conditional
   on its four neighboring links, exactly two possibilities have positive
   probability:

   ```text
   Pr(star|ell_boundary)=epsilon/T(Phi),
   Pr(ell_boundary|ell_boundary)=1-epsilon/T(Phi).
   ```

   At a link, the only relevant conditions are its adjacent face auxiliaries.
   If all are `star`, the link is uniform on `G`; if any carries a tuple, its
   incident component fixes the link. All tuple demands agree on the joint
   support. A conflicting zero-probability neighbor context may be assigned a
   covariant fallback without changing `mu`.

3. **Compatibility and uniqueness.** The universal state has positive weight.
   From any supported state, turn every face to `star`, change links one at a
   time, and turn any desired faces back to their matching tuples. Thus the
   single-site support graph is connected. The displayed local full
   conditionals determine `mu` uniquely on that support, and their random-scan
   heat-bath chain is reversible.

4. **Gauge and cubic covariance.** A gauge transformation acts simultaneously
   on the links and on every matching tuple; `star` is fixed. Curl and `T` are
   unchanged. Proper cubic rotations permute faces and tuple slots; orientation
   reversal sends `Phi` to `-Phi`, which evenness removes.

This is a finite constructive theorem for any strictly positive `T`, not only
the runner's example. The runner exhausts the parent's `Z_4` Record overlap
`T=(85,50,40,50)` on a one-face support and on all `65,536` link
configurations of a `2 x 2` periodic gauge lattice. It also follows a strictly
positive trigonometric Record density through `Z_N`,
`N=8,16,32,64,128,256`, and verifies convergence of the discrete curvature to
the parent's positive `U(1)` curvature.

This removes the direct parent's **postselection and joint-compatibility
caveat for the finite candidate law**. The plaquette measure is now an
unconditional marginal of one compatible local-conditional system. It does
not derive this local rule from the axioms' unspecified distribution, provide
a Record-production history, or finish the internal role/readout compilation.
It also does not prove a continuous compact interacting photon or identify the
field with electromagnetism.

## 1. The two-state decomposition at one face

Fix the four neighboring link values

```text
a=(a_1,a_2,a_3,a_4) in G^4,
Phi(a)=a_1+a_2-a_3-a_4.
```

Only two auxiliary values contribute:

```text
F(star;a)=epsilon,
F(a;a)=T(Phi(a))-epsilon.
```

Because `epsilon=(1/2)min T`, both are strictly positive and every other tuple
has weight zero. Their sum is exactly `T(Phi(a))`. This is an identity for
every boundary tuple, not an asymptotic or a fitted normalization.

The half-minimum choice removes a free scalar from this construction. Other
values `0<epsilon<min T` give the same link marginal but different readable
auxiliary statistics. The runner checks `epsilon=1`, the canonical value `20`,
and `39` for `T=(85,50,40,50)`. At `epsilon=0`, the universal state has zero
weight and cannot connect tuple sectors. At an endpoint
`epsilon>=min T`, at least one matching state loses strict positivity. These
are controls on this decomposition, not a claim that every possible auxiliary
decomposition must use the half-minimum.

For a normalized overlap `q=T/T(0)`, multiplying every local factor by the
same positive constant changes only the finite-volume partition function.
The induced link probability and its negative-log action are unchanged.

## 2. Global marginal without a selected outcome

Given the links, different `h_f` variables occur in different factors. Hence
finite distributivity gives

```text
sum_h product_f F_f(h_f;ell_boundary)
 = product_f sum_(h_f) F_f(h_f;ell_boundary)
 = product_f T(Phi_f).
```

Unlike the all-success likelihood in the direct parent, this equation sums
**all** auxiliary possibilities and still leaves the plaquette weight. The
reason is that `F` is an unnormalized factor of the joint measure, not a
normalized descendant probability whose outcomes sum to one before the joint
normalization.

After the global partition function is applied, however, `F` yields ordinary
normalized local full conditionals. The construction therefore avoids the
parent's normalization trap without pretending that a normalized binary
child can reweight its parent when forgotten.

For the `Z_4` Record histogram `(8,4,2,1)/15`, direct pair counting gives

```text
T=(85,50,40,50),       epsilon=20.
```

The runner enumerates all `4^8=65,536` link configurations on the `2 x 2`
periodic lattice. For each it sums all `2^4=16` supported universal/matching
face masks and obtains exactly the target four-plaquette product. The local
one-face identity is also checked on all `4^4=256` ordered boundaries for all
three interior epsilon choices.

## 3. The local full conditionals

### Face site

Condition on the four link neighbors. The normalization is the one-face
marginal `T(Phi)`, so

```text
Pr(h=star | a)=epsilon/T(Phi(a)),
Pr(h=a    | a)=[T(Phi(a))-epsilon]/T(Phi(a)),
Pr(h=b    | a)=0 for b!=a.
```

These probabilities depend only on the face site's nearest-neighbor edge
conditions. They normalize exactly and vary with `Phi` whenever `T` is
nonconstant.

### Edge site

Condition on every other variable in a supported joint state. A neighboring
face in state `star` contributes the same factor `epsilon` for every candidate
link value. A neighboring tuple state contributes only when the candidate
equals its incident tuple component. Therefore

```text
Pr(ell_e=g | adjacent h)
 = 1/N                    if every adjacent h=star,
 = 1 at the common demand if at least one h is a tuple,
 = 0 otherwise.
```

The other three links around an incident face do not enter this conditional
on support: their equality with the stored tuple is already fixed in the
conditioning event. If tuple demands conflict, the conditioning event has
zero `mu` probability and the full conditional is mathematically arbitrary;
a fixed uniform fallback makes the candidate rule total without changing the
joint measure.

Thus both nontrivial site roles have distributions determined by their
nearest-neighbor incidence conditions. This is stronger than merely writing a
four-link action and declaring it local on a coarse face.

The construction is still conditional on a supplied role sector. Vertex and
cube roles, genesis of the role pattern, and a single microscopic rule table
covering every possible malformed role neighborhood are not compiled here.

## 4. Connected support makes the joint law determined

Hard matching constraints can hide arbitrary weights in disconnected support
components. The positive universal state is included to remove that problem.

Take any supported `(ell,h)`. Each face may change from its matching tuple to
`star` with positive conditional probability `epsilon/T(Phi)`. Once all faces
are universal, each link conditional is uniform, so any target link
configuration can be reached by single-site changes. Finally each target face
may remain universal or change to its matching tuple with positive
probability. The support graph is connected.

Now let `mu` and `nu` be two normalized joint distributions on this support
with the same displayed full conditionals. Along every allowed single-site
edge `x<->y`, the conditional ratios give

```text
mu(y)/mu(x)=nu(y)/nu(x).
```

Connectivity makes `mu/nu` constant on the whole support, and normalization
makes that constant one. Thus the local full conditionals select the joint
measure uniquely at finite volume.

On the one-face `Z_4` model the support has `2 x 4^4=512` states. The runner
builds its entire single-site graph, visits all states, and checks every face
and link heat-bath balance equation for the three epsilon choices. At
`epsilon=0`, the 256 matching-tuple sectors cannot communicate, which is the
explicit disconnected-support control.

The heat-bath chain proves static compatibility and uniqueness. It is not
identified with physical time or with a process that changes permanent
Records.

## 5. Gauge and proper-cubic covariance

Around a square with vertices `0,1,2,3`, take positive link orientations
`a_1:0->1`, `a_2:1->2`, `a_3:3->2`, and `a_4:0->3`. Then

```text
Phi=a_1+a_2-a_3-a_4.
```

Under `a_xy -> a_xy+lambda_y-lambda_x`, all four vertex phases cancel from
`Phi`. Transform a matching auxiliary tuple by the same four link maps;
`star` remains `star`. Equality and the factor weight are preserved. The
runner checks all 256 boundary tuples against all 64 based `Z_4` gauge
transformations.

The eight square relabelings either preserve the oriented sum or reverse it.
Since the Record overlap is even, `T(-Phi)=T(Phi)`. The runner checks all eight
images of every boundary tuple. On the three-dimensional incidence complex,
proper cubic rotations permute these face rules; the direct parent separately
checks all 24 rotations of the spatial plaquette product.

The tuple slots must transform with their incident edge directions. This is
an exact abstract covariance rule. Realizing that slot action through a
specific internal `M_2(C)` automorphism or a spatial composite remains part of
the microscopic compiler interface.

## 6. Capacity inside the one-site possibility algebra

The full one-site possibility domain has algebraic presentation `M_2(C)`.
At the level of distinct possibilities, the face alphabet fits explicitly:
for `zeta=exp(2 pi i/N)`, map

```text
(a_1,a_2,a_3,a_4)
 -> [[zeta^a1,zeta^a2],
     [zeta^a3,zeta^a4]],

star -> [[0,0],[0,0]].
```

This is injective for every finite `N`, and the same formula embeds
`U(1)^4` as a subset of `M_2(C)`. The runner verifies distinctness for all
`1+4^4=257` and `1+8^4=4097` labels.

This algebraic capacity is not an orthogonal-readout theorem. If every
auxiliary label must be perfectly distinguishable as an orthogonal quantum
record, a composite needs at least

```text
ceil(log2(1+N^4))
```

qubits: `5,9,13,17` at `N=2,4,8,16`. The runner derives those costs. The
framework may instead use nonorthogonal possibility content in the local law,
but a physical readable-slot interpretation must decide which standard is
required.

## 7. Finite cyclic route toward the compact overlap germ

Use the strictly positive density

```text
p(theta)=1+0.25 cos(theta)+0.15 sin(2 theta).
```

Sample and normalize it on `Z_N`. Its cyclic autocorrelation is strictly
positive at every shift, so the auxiliary theorem applies at every tested
`N`. Normalize the overlap at zero and use

```text
kappa_N = -2 log q_N(2 pi/N)/(2 pi/N)^2.
```

The runner verifies monotonically shrinking error through
`N=8,16,32,64,128,256`, ending below `2e-5` from the parent's analytic

```text
kappa=||p'||_2^2/||p||_2^2>0.
```

Thus the exact finite local laws approach the same positive compact curvature.
This is not yet a theorem interchanging the group refinement, spatial
continuum, thermodynamic, and quantum limits. It supplies a concrete sequence
on which that stronger analysis can be run.

## 8. What changes in the TOE route

The action/compatibility stack now has the following constructive sequence:

```text
neighbor-varying Record distribution on a compact shift orbit
 -> positive even overlap kernel                         parent #7887
 -> nearest-neighbor spatial face likelihood             parent #7906
 -> unconditional gauge marginal from local conditionals this note
 -> positive magnetic germ and two weak-field modes       parent #7906
```

The new step is not a synonym for the previous one. Parent #7906 required an
all-success Record event to turn normalized face probabilities into a
plaquette posterior. Here every auxiliary outcome is summed and the plaquette
weight remains, while the resulting joint measure has compatible local full
conditionals and connected support.

What remains explicit:

- selection of this auxiliary conditional family from the unspecified
  Admissibility distribution;
- the full rotation-covariant internal/role compiler on physical sites;
- the Record formation/history process, if static full conditionals are not
  taken as the complete probability law;
- the electric/time law and relative propagation normalization;
- the physical electromagnetic dictionary; and
- simultaneous compact, thermodynamic, interacting, and quantum continuum
  control.

No axiom update is requested. This is a candidate law inside the room the
minimal axioms deliberately leave for the extensional distribution.

## 9. Executable evidence

The runner reports `TOTAL: PASS=19 FAIL=0`. It verifies:

- reconstruction of the finite Record overlap rather than insertion of its
  four output weights;
- all 257 auxiliary values on all 256 face boundaries for three interior
  epsilon splits;
- exact marginalization, positivity, normalization, and neighbor variation;
- every based `Z_4` gauge transformation and every square relabeling;
- the complete 512-state one-face support graph and all local heat-bath
  balance equations;
- every `2 x 2` link configuration and every one of its 16 supported face
  masks at the canonical split;
- local edge conditional composition on every incidence mask;
- the zero-universal and endpoint controls;
- injective `M_2(C)` labels and orthogonal composite costs; and
- six cyclic refinements approaching the positive `U(1)` curvature.

The single-face marginal identity, finite distributivity, conditional formulas,
support path, conditional-ratio uniqueness proof, and covariance equations
prove the general finite theorem. Exhaustive runs test every element of the
declared `Z_4` blocks; the refinement sequence is a convergence check, not a
proof of all simultaneous limits.

## No-Go Discipline Gate

This positive theorem contains three narrowed negative boundaries: normalized
descendant probabilities cannot reweight a forgotten parent in the no-feedback
model of #7906; the zero-universal version of this auxiliary construction has
disconnected support; and the finite cyclic sequence is not itself a proof of
the full continuous interacting theory. The gate below stress-tests only
those statements and asserts no permanent impossibility.

### N1 — Alternative route enumeration

| Family | Object / mechanism / terminal obligation | Marker and outcome |
|---|---|---|
| `selected_face_event` | Normalized binary face outcomes / condition on all successes / obtain the plaquette posterior. | **ATTEMPTED:** positive in #7906, but retains a selected-event condition. |
| `forgotten_descendant` | Normalized face outcomes / sum every outcome / obtain an unconditional parent reweighting. | **ATTEMPTED:** fails in the declared no-feedback model because each sum is one. |
| `matching_only_auxiliary` | Hard matching tuples / exact face marginal / obtain locally connected support. | **ATTEMPTED:** marginal is exact but `epsilon=0` leaves disconnected tuple sectors. |
| `universal_plus_matching` | One universal plus one matching tuple / positive overlap split / obtain both exact marginal and connected support. | **ATTEMPTED:** positive; this is the theorem. |
| `full_conditionals` | Supported incidence graph / local conditional ratios / determine a unique finite joint measure. | **ATTEMPTED:** positive; connectivity and every one-face heat-bath equation pass. |
| `one_site_algebra` | Explicit four-entry matrix label / inject the face alphabet into `M_2(C)` / meet possibility capacity. | **ATTEMPTED:** positive as an algebraic injection; orthogonal readout remains separate. |
| `cyclic_refinement` | Strictly positive sampled Record densities / `Z_N -> U(1)` curvature / preserve the Maxwell germ. | **ATTEMPTED:** positive through six refinements; simultaneous continuum control remains open. |

The failed matching-only and forgotten-descendant routes are not generalized
beyond their displayed constructions. Positive feedback, other auxiliary
factorizations, direct continuum specifications, and spatial composites remain
live.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: microscopic role and rotation-covariant internal compiler.
- W2: selection of this auxiliary conditional family.
- W3: physical formation/history interpretation if static law is insufficient.
- W4: electric/time dynamics and relative normalization.
- W5: electromagnetic field/readout dictionary.
- W6: compact interacting and simultaneous-limit control.

| Pair | First closure implies second? | Second closure implies first? | Independence established? |
|---|---|---|---|
| W1, W2 | unresolved | unresolved | no |
| W1, W3 | unresolved | unresolved | no |
| W1, W4 | unresolved | unresolved | no |
| W1, W5 | unresolved | unresolved | no |
| W1, W6 | unresolved | unresolved | no |
| W2, W3 | unresolved | unresolved | no |
| W2, W4 | unresolved | unresolved | no |
| W2, W5 | unresolved | unresolved | no |
| W2, W6 | unresolved | unresolved | no |
| W3, W4 | unresolved | unresolved | no |
| W3, W5 | unresolved | unresolved | no |
| W3, W6 | unresolved | unresolved | no |
| W4, W5 | unresolved | unresolved | no |
| W4, W6 | unresolved | unresolved | no |
| W5, W6 | unresolved | unresolved | no |

The table withdraws the earlier blanket independence assertion; no
conditional hypothesis is removed. Concrete examples elsewhere in this note
apply only to the relationships they test.

### N3 — Hidden-wall scan

“Supply” and “supplied” mark the cyclic group, role sector, local factor,
fallback on zero-probability contexts, and any dynamics. The displayed
`M_2(C)` map is an algebraic injection, not a claim of orthogonal readability.
“Canonical” appears only in the parent's separately supplied weak-field
quantization and is not used in this factor theorem. No “as is standard,”
“the framework provides,” “naturally,” or “obviously” phrase carries a proof
step. The global normalization, support, and finite-volume condition are
explicit.

### N4 — Residual matching

| Cited surface | Its residual | Residual treated here | Match and use |
|---|---|---|---|
| `U1_RECORD_FACE_LIKELIHOOD_SPATIAL_GAUGE_AND_PHOTON_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md`, lines 90-96 and 375-385 | product joint and postselection are supplied | unconditional auxiliary marginal with connected compatible full conditionals | **yes**, direct target |
| `U1_RECORD_DISTRIBUTION_OVERLAP_POSITIVE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md`, lines 251-269 and 326-350 | overlap factorization/ownership remains supplied | one explicit finite local joint-law realization | **partial**, candidate ownership but not law selection |
| `G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`, lines 1-35 and 190-220 | marginals do not choose a coupling | explicit joint coupling and unique full-conditionals measure | **yes** in mathematical shape; no audit grade imported |
| historical PR #7901 | energy tests on record-shift chains | reversible full-conditionals chain on a gauge factor graph | **partial**, context only |
| historical PR #7903 | finite truncated interacting photon remains uncomputed | static factorization of a magnetic measure | **no**, dropped as witness and not claimed closed |

The proof stands after dropping both historical-PR pointers. They route future
composition only.

### N5 — Rhetoric and resolution audit

“The zero-universal construction has disconnected support” is tested on every
one-face state; it is not extended to all auxiliary designs. “A forgotten
normalized child does not reweight its parent” is an exact per-face identity
and lattice product in #7906's no-feedback model; feedback is explicitly
outside that sentence. “Finite cyclic convergence is not the full interacting
continuum” states an unexecuted scope rather than a negative theorem.

The cached stdout carries the five-resolution certificate:

```text
per_element: every Z4 boundary tuple, auxiliary state, gauge transform, and square relabeling is checked
per_site: face and edge full conditionals are normalized and depend only on incidence neighbors on support
per_mode: checked and not executed — this factorization changes no parent Hessian eigenvalue or momentum mode
per_block: all 512 one-face support states and three epsilon splits are checked for balance and connectivity
lattice_wide: every 2x2 Z4 link configuration and all 16 auxiliary masks are marginalized exactly
```

### N6 — Partial-closure paths and primitive check

The current primitive registry and all three source notes were reread. The
scale-reference primitive supplies units only. The kinetic-isotropy primitive
supplies structural `c_t=c_s` graining, not this factor, a gauge Hamiltonian,
or formation. The realized-state primitive supplies pointwise evaluation, not
a state, measure, probability, or selector. They are premise nodes with their
declared scopes and are neither walls nor expanded here.

Live partial-closure routes are concrete:

- compile the tuple-slot transformation through an explicit spatial composite
  or an allowed internal action on the displayed `M_2(C)` injection;
- prove a direct continuous mixed auxiliary measure instead of approaching it
  only through `Z_N`;
- treat the static compatible full-conditionals law as the probability theory
  and derive predictions without adding a record-changing tick;
- or build a fresh-site formation history whose event conditionals equal this
  static law.

Adopting a candidate extensional law would be downstream model selection, not
a new axiom. Deriving the law from a smaller consistency class would be the
preferred import-retirement path.

### N7 — Steelman

A hostile reviewer can argue that the supposed microscopic compiler wall is
nearly gone: `M_2(C)` has four complex entries, this note gives an explicit
injective `U(1)^4` label, and the face site already has exactly the four edge
neighbors the tuple describes. The remaining work may be a routine covariant
slot permutation rather than new physics. That route is credible, so this
note does not declare a compiler no-go. Its exact terminal obligation is to
write one proper-cubic-covariant rule on every physical role and show that its
Record-readable interpretation preserves the abstract full conditionals.
Likewise, if physical predictions are exhausted by a static conditional
probability law, no extra formation dynamics may be needed. The theorem leaves
both stronger positive readings open.

### N8 — Cross-cycle echo

The repository search found the same marginal-versus-joint distinction in
`G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`.
That note isolated the joint coupling as an open formation atom; this theorem
does not dismiss it, but supplies and uniquely characterizes one coupling for
the finite gauge model. The Record-occurrence axiom update retired an older
absence-of-occurrence statement while preserving the concrete formation-rule
residual; the applicable lesson is to keep the static law/formation distinction
explicit. Open PRs #7900 and #7902 show that one joint-formation unit succeeds
on flat-band blocks and fails to generalize automatically, so they motivate a
compiler test rather than a general negative conclusion.

**Gate result:** PASS for the three scoped boundaries. Seven materially
different routes were executed, the hard-matching failure was repaired by a
positive universal state, the pairwise wall relations are explicitly unresolved, and both the
continuous and microscopic steelman routes remain open.

## Falsifiers

The finite theorem fails if any of the following occurs:

- the universal and matching weights do not sum to `T(Phi)` for some boundary;
- the canonical half-minimum split is not strictly positive;
- the link marginal differs from `product_f T(Phi_f)` after every auxiliary is
  summed;
- a supported face or edge full conditional depends on a non-neighboring site;
- the positive-universal support graph is disconnected;
- two distinct normalized measures on that connected support share all the
  displayed full conditionals;
- a gauge transformation or square relabeling changes a local factor;
- the finite auxiliary alphabet does not inject into `M_2(C)` as displayed;
  or
- the declared positive-density cyclic sequence fails its stated curvature
  convergence check.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=19 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A selected framework-derived electromagnetic law and physical field/readout bridge remain open; the eventual physical consumer is not yet established."
source_of_blocker_text: "review_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Use the conditional result with its stated inputs; establish the missing physical consumer and selection bridge before claiming framework closure."
conditional_surface_status: "Finite cyclic links, positive plaquette weights, epsilon-positive universal-plus-matching auxiliaries and the stated finite support."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The written derivation establishes only the declared conditional mathematical claim; finite checks and source review grant no retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original September 2–3 source and receipts are preserved at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. This revision supplies current
source status, explicit timeout/input-bound evidence and written boundary
checks. The conditional scope is stated in the status record above.
Independent source confirmation and current-main integration validation are
separate; no audit verdict or effective retained status is asserted.
