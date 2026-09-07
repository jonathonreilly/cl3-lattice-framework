# Minimal Physical-Neighbor Conservative Gauge Dynamics Is Maxwell Up to Orientation, Field Normalization and Speed

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.
**Direct parent:**
[`U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Role compiler:**
[`U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
**Runner:**
[`scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py`](../scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_minimal_maxwell_generator_uniqueness_2026_09_03.txt`](../logs/runner-cache/u1_minimal_maxwell_generator_uniqueness_2026_09_03.txt)

## Result up front

Declare the following weak-field dynamics class on the role-compiled physical
lattice:

1. one real electric component lives at each edge-role site and one real
   magnetic component at each face-role site;
2. evolution is real, linear, first order, and continuous in time;
3. a site derivative may use its own component and the dynamical components
   among its six physical nearest neighbors, but no farther site;
4. the law is translation- and proper-cubic-covariant;
5. the edge-to-face map is invariant under `A -> A+d_0 lambda` and preserves
   the magnetic Gauss row;
6. a positive, diagonal, proper-cubic field energy is conserved; and
7. no vertex, cube, extra coin, or hidden time payload participates.

Within this exact class, every nonzero generator is equivalent, after a possible
magnetic-field sign reversal and positive field rescaling, to

```text
dot E = -c C^T B,
dot B =  c C E,
```

where `C` is the oriented physical edge-to-face curl and `c>0` is one overall
speed. The two signs of the common coupling are related by `B -> -B`;
positive rescaling alone does not identify them. There is no second stencil,
mass term, damping term, independent face-orientation coefficient, or
same-role nearest-neighbor term inside the class.

The classification has four steps:

- gauge invariance on one face star leaves the one-dimensional stencil
  `(1,1,-1,-1)`;
- proper cubic covariance makes its coefficient equal on all face
  orientations;
- the period-two role geometry has no edge-edge or face-face nearest-neighbor
  pairs, so only edge-face blocks and real onsite scalars remain; and
- positive diagonal energy conservation kills the onsite scalars and fixes
  the reverse block to be the weighted negative adjoint.

After choosing the magnetic orientation, the remaining positive coefficients
are field normalization and a freely supplied speed. The reciprocal choice
`beta=kappa`, `alpha=1/kappa` gives `c=1` conditionally. The existing matter
kinetic-isotropy primitive does not identify these gauge coefficients with the
matter kinetic block. At nonzero momentum the classified generator carries
the two transverse Maxwell branches established in the direct parent.

This materially sharpens the time-selection issue. The conservative Maxwell
law is not merely one arbitrary local example: it is the only member of a
small, explicit, physically motivated class. The four axioms do not currently
select that class. In particular, they do not state real linear first-order
evolution, energy conservation, minimal `(E,B)` payload, or continuous time.
Those are now the exact assumptions requiring derivation, model selection, or
a narrowly considered primitive/axiom decision.

## 1. Exact declared class

Call the class `M_min`. Its field content and rule shape are fixed as follows.

### M1 — field content

Each edge role carries one real `E` component and each face role one real `B`
component. Vertex and cube roles carry no dynamical component. The finite
Record auxiliary and compact link payloads of the static parent may remain as
separate possibility data, but they do not enter this linear classification.

### M2 — locality and order

The time derivative at a physical site is a real linear function of its own
field and fields at the six nearest neighbors. It contains no memory, second
time derivative, external clock variable, or finite-step inverse.

### M3 — lattice symmetry

The same law is used at every site. Proper cubic rotations carry edge
orientation into edge orientation and face normal into face normal. No
orientation has an independent coefficient.

### M4 — gauge and chain constraints

The magnetic response to an edge potential is unchanged by an exact gradient,
and the edge-to-face response has zero cube divergence:

```text
L d_0=0,                  d_2 L=0.
```

### M5 — conservative metric

There is a positive diagonal energy

```text
H=(w_E/2)||E||^2+(w_B/2)||B||^2,
w_E,w_B>0,
```

with the same weight on all cubic images of a role. The generator preserves
`H` for every field.

### M6 — minimal payload

No additional vertex, cube, coin, duplicated configuration, or longer-range
field is allowed. This is a classification assumption, not an axiom claim.
Dropping it reopens several routes listed below.

## 2. Gauge invariance fixes one face stencil

Take one oriented square with vertices `0,1,2,3` and boundary links

```text
a:0->1,  b:1->2,  c:3->2,  d:0->3.
```

A general face response inside `M_min` is

```text
L_f(A)=x_a a+x_b b+x_c c+x_d d.
```

Under vertex gauge values `(lambda_0,...,lambda_3)`, the four links change by

```text
a -> a-lambda_0+lambda_1,
b -> b-lambda_1+lambda_2,
c -> c-lambda_3+lambda_2,
d -> d-lambda_0+lambda_3.
```

Requiring the coefficient of every `lambda_v` to vanish gives

```text
-x_a-x_d=0,
 x_a-x_b=0,
 x_b+x_c=0,
-x_c+x_d=0.
```

The integer constraint matrix has rank three and one-dimensional nullspace

```text
(x_a,x_b,x_c,x_d)=q(1,1,-1,-1).
```

This is the oriented curl. The result needs neither a continuum limit nor a
Fourier argument. The runner performs exact rational row reduction and also
enumerates all `5^4=625` coefficient vectors with entries from `-2` to `2`:
each gauge-invariant vector is a curl multiple, and every other one has an
explicit gauge residual.

## 3. Proper cubic covariance leaves one spatial coefficient

Applying the face calculation separately to the `xy`, `xz`, and `yz`
orientations initially leaves three scalars `(q_xy,q_xz,q_yz)`. The 24 proper
cubic rotations act transitively on the six oriented face normals. Covariance
therefore requires

```text
q_xy=q_xz=q_yz=q.
```

The combined exact constraint matrix has 12 stencil variables, gauge rank
nine, and two independent orientation equalities. Its nullspace is one
dimensional with basis

```text
(curl_xy,curl_xz,curl_yz).
```

An orientation-dependent coefficient is not a second covariant solution. It
is the anisotropy control and splits the transverse branches.

## 4. The role geometry removes same-role neighbor blocks

Every edge-role site has two vertex and four face neighbors. Every face-role
site has four edge and two cube neighbors. There are no nearest-neighbor
edge-edge or face-face pairs.

Under M1 and M6, a derivative may therefore contain only:

- an onsite real scalar multiplying the same field; and
- the four opposite-role components in its incidence star.

No general vector-valued onsite mixing is hidden here: the three cubic
components occupy three different physical sites. A complex onsite phase or
an internal multiplet would leave the declared real one-component class.

The runner checks every role shell on the side-six physical lattice. It then
assembles the unique local curl rows into the full `81 x 81` incidence matrix
and rechecks `C d_0=0` and `d_2 C=0` over integers.

## 5. Conservation fixes the reverse block

Write the most general remaining real generator as

```text
G = [[u I,  r C^T],
     [q C,  v I ]].
```

Energy conservation for every `(E,B)` is equivalent to

```text
G^T diag(w_E I,w_B I)+diag(w_E I,w_B I)G=0.
```

The diagonal blocks give

```text
2 w_E u=0,                2 w_B v=0,
```

so positivity forces `u=v=0`. The cross block gives

```text
w_E r+w_B q=0,
```

or

```text
r=-(w_B/w_E)q.
```

Thus the edge response is the weighted negative adjoint of the face response.
Let

```text
sigma=sign(q),            B_tilde=sigma B,
alpha=|q|,                beta=|r|.
```

For a nonzero generator `q` and `r` have opposite signs, so `alpha,beta>0`.
Conjugation by `diag(I,sigma I)` gives the displayed positive-orientation
system on `(E,B_tilde)`. Positive diagonal similarity alone cannot change
the sign of any nonzero matrix entry; in particular it cannot turn `-G` into
`G` at a fixed `c>0`. Now rescale the oriented fields by

```text
E'=sqrt(w_E)E,            B'=sqrt(w_B)B_tilde.
```

The generator becomes

```text
G' = c [[0,-C^T],[C,0]],
c=sqrt(alpha beta).
```

Every nonzero real coefficient choice is therefore the same positive-speed
generator after this possible sign reversal and positive field normalization,
with one remaining time scale `c`.

The runner checks four unequal positive coefficient pairs, conservation,
both Gauss rows, their spectra, and the explicit similarity transform. A
negative-coupling control checks the missing orientation reversal. A
same-sign adjoint mutation and a damping mutation both fail the metric-skew
condition.

## 6. Spectrum inherited by the unique class

For staggered Fourier symbol

```text
s_i=2 sin(k_i/2),
```

the unique curl has singular values `(0,|s|,|s|)`. Therefore the normalized
generator has

```text
spec(iG')=(-c|s|,-c|s|,0,0,+c|s|,+c|s|).
```

At nonzero momentum the electric and magnetic Gauss rows remove the two
longitudinal zero directions, leaving two positive-frequency transverse modes.
At zero momentum the whole block vanishes and the constant harmonic fields
survive Gauss; no two-mode claim is made for that sector. The
runner rechecks every momentum on `L=3,4,5,7`. This is not a new photon count
beyond the direct parent; it establishes that every member of `M_min` has the
same count and dispersion.

The direct parent's Record-overlap curvature can be assigned

```text
beta=kappa,               alpha=1/kappa,
```

giving `c=1` as a supplied reciprocal gauge normalization. Other positive
products `alpha beta` satisfy the same classification. The approved
kinetic-isotropy primitive fixes the matter kinetic-form ratio; identifying
it with this gauge family requires a further matter/gauge kinetic bridge,
which is open here. Class selection alone supplies no such identification.

## 7. Why an exact local tick remains open

The theorem classifies a continuous-time local generator. A finite tick has a
separate locality/unitarity tension:

- the explicit Euler map `I+dt G` retains radius one but satisfies

  ```text
  (I+dt G)^T(I+dt G)=I+dt^2 G^T G,
  ```

  so it is not exactly norm preserving;
- the Cayley map

  ```text
  (I+dt G/2)(I-dt G/2)^(-1)
  ```

  is exactly norm preserving, but the inverse spreads a one-tick row beyond
  the physical star.

On the full 162-variable runner block, every Cayley row has more than ten
nonzero entries at the declared tolerance. This does not prove that no exact
finite-depth local tick exists. Split-step edge-face rotations, Trotter
circuits, quantum cellular automata, and enlarged coins remain live.

This is now the sharpest dynamics compiler residual: the infinitesimal law is
unique inside M1-M6, while a strictly radius-one exact unitary tick has not
been selected or constructed.

## 8. What is and is not selected

The direct parent displayed three inequivalent time uses of the static
spatial kernel: conservative Maxwell evolution, a diffusive sampler, and a
two-reflection spectral lift. This theorem explains how a minimal physical
criterion separates them:

- energy conservation excludes the dissipative sampler;
- M6 excludes the doubled walk/coin space of the spectral lift; and
- real one-component physical-neighbor locality plus gauge invariance leaves
  the curl generator.

That is a conditional selection theorem, not an axiom derivation. The four
framework axioms state a local conditional probability distribution and
permanent Records. They do not require conservative continuous-time flow,
minimal dynamical payload, or linear weak-field evolution.

There are now two honest program choices:

1. treat M1-M6 as defining the candidate physical law and continue testing
   compact interactions, matter coupling, and phenomenology; or
2. seek a derivation of M1-M6 from a smaller principle, and if no existing
   premise can provide it, decide whether a conservative local-dynamics
   principle belongs in the approved primitive/axiom boundary.

No axiom edit is made here. The theorem supplies the exact language needed
for that decision without expanding Admissibility by implication.

## 9. Executable evidence

The runner reports `TOTAL: PASS=25 FAIL=0`. It checks:

- exact rational rank and nullspace of the one-face gauge constraints;
- every one of 625 small integer stencils and a sign mutation;
- the three-orientation gauge space and one-dimensional cubic subspace;
- the orbit of all six oriented normals under 24 proper rotations;
- every edge/face shell on the physical block and absence of same-role
  nearest neighbors;
- assembly of the global `81 x 81` curl and both chain identities;
- onsite exclusion, weighted-adjoint conservation, four coefficient pairs,
  both Gauss rows, field rescaling, and the complete mode spectrum;
- anisotropy, same-sign, damping, and missing-orientation controls; and
- local Euler versus norm-preserving nonlocal Cayley ticks.

## No-Go Discipline Gate

This note makes a uniqueness statement inside M1-M6 and two bounded tick
statements. The gate prevents those results from being generalized into a
claim that Maxwell dynamics is axiom-forced or that an exact local tick is
impossible.

### N1 — Alternative routes and same-cycle evidence

These attempts were checked analytically or by the paired runners in this
47-path review unit. Positive and partial constructions remain positive or
partial; none is recast as a failed route to satisfy a count. Named check
labels, rather than old ordinal numbers, identify the evidence. Cross-note
comparisons below are scope tests, not extra premises of this note.

| Route | Actual attempt and evidence | Result within the stated scope |
|---|---|---|
| Minimal conservative real class | **ATTEMPTED:** Solve the face gauge nullspace, cubic equality and weighted-energy adjoint conditions (§§2–5; exact classification checks). | The stencil is unique up to magnetic orientation, positive rescaling and speed. |
| Dissipative sampler | **ATTEMPTED:** Use the role-compiled note’s projected OU law and its rate/variance checks. | It is a positive static-law sampler outside conservation. |
| Two-reflection lift | **ATTEMPTED:** Use the role-compiled note’s explicitly executed two-reflection blocks. | Its extra walk payload lies outside the minimal class. |
| Explicit Euler tick | **ATTEMPTED:** Build I+hG on the full block (Euler norm check). | It is local but fails exact norm preservation. |
| Implicit Cayley tick | **ATTEMPTED:** Build the rational Cayley transform on the same block (Cayley support/norm check). | It preserves raw norm but the tested inverse has support beyond a star. |
| Finite-depth shear tick | **ATTEMPTED:** Replay the leapfrog sibling’s exact inverse, local metric and support controls. | It is a positive finite-depth escape from a one-layer reading, not a new generator class. |

Complex onsite phases, added vertex/cube payload, longer-range curls and
second-order formulations remain outside the class. No impossibility claim
is made about those enlarged objects.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: derivation or adoption of M1-M6.
- W2: exact finite local tick.
- W3: enlarged payload/internal implementation.
- W4: Record formation and measurement bridge.
- W5: compact nonlinear/interacting stability.
- W6: electromagnetic and matter-coupling dictionary.

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

The examples elsewhere in this note establish only their displayed positive
or negative cases. In particular, the leapfrog example changes both complete
map radius and energy metric; that single example does not establish those
restrictions’ independence. The strict radius-one sibling retains its own
explicit domain-relaxation table.

### N3 — Hidden-wall scan

“Declare,” “within,” and “conditional” mark M1-M6. “Unique” never appears
without that class. The fields are real and one-component per role. The energy
metric is positive, diagonal, and cubic. Continuous time is supplied. The
Cayley density check is a finite exhibit, not a theorem about every unitary
integrator. Gauge normalization remains supplied even after the dynamics class
is chosen; no matter/gauge kinetic identification is assumed.

### N4 — Residual matching

| Surface | Residual | Match here |
|---|---|---|
| direct dynamics parent | static law leaves a three-way time fork | **partial closure:** M1-M6 select the conservative edge-face branch |
| role compiler | physical edge/face incidence but no dynamics | **exact:** its neighbor graph is the classified stencil domain |
| minimal axioms | no dynamics, Hamiltonian, or tick | **no import:** M1-M6 remain downstream assumptions |
| kinetic-isotropy primitive | equal matter kinetic form | **no closure:** no identification with the gauge coefficient product is proved |
| historical PR #7903 | compact fermion/U1 Hamiltonian join | **future composition:** no finite interacting spectrum imported |
| historical PR #7911 | spin-half ring is gapped | **no conflict:** different payload and three-dimensional weak-field class |

The classification is self-contained after both historical-PR pointers are removed.

### N5 — Rhetoric and resolution audit

“No second stencil” means no second stencil inside M1-M6. “Onsite term is
killed” means a real scalar onsite term under positive diagonal conservation.
“Cayley spreads” is tested on the named finite block. No universal no-go for
complex fields, extra payloads, longer range, nonlinear laws, finite-depth
circuits, or discrete time is asserted.

The cached output carries:

```text
per_element: all 625 small face stencils and every exact gauge constraint row are classified
per_site: the full L3 role geometry excludes same-role neighbors and leaves four edge-face couplings
per_mode: every momentum on L=3,4,5,7 is checked for the unique two-branch spectrum
per_block: gauge, cubic, energy-adjoint, field-rescaling, Euler, and Cayley blocks are contrasted
lattice_wide: the global 81-by-81 curl and 162-variable generator are assembled from the unique stencil
```

### N6 — Partial-closure paths and primitive check

The approved primitive registry was reread. Kinetic isotropy supplies the
matter kinetic-form ratio, not this gauge coefficient product; scale reference
supplies units; realized-state evaluation supplies no dynamics. M1-M6, an
exact tick, and a matter/gauge kinetic identification remain separate supplied
choices or open derivations in this note.

The shortest live positive paths are:

- construct a finite-depth split-step unitary on the same edge-face stars and
  test whether its only infrared branches are the classified photons;
- derive conservation from a probability or reversibility principle without
  reintroducing the dissipative sampler;
- show the minimal payload follows from the one-site algebra or from an
  orthogonal spatial composite; or
- adopt M1-M6 as the candidate law and attack compact interacting stability.

### N7 — Steelman

A hostile reviewer can argue that M1-M6 were chosen precisely to describe
Maxwell, so uniqueness is circular. Gauge invariance does real work: before
it, one face has four independent coefficients; it reduces them to the curl.
Cubic symmetry reduces three orientation coefficients to one, and energy
conservation fixes the reverse map and removes damping. Nonetheless, choosing
real linear first-order conservative minimal fields is physical input. The
theorem narrows that input; it does not erase it.

The reviewer can also argue that a continuous generator is not the
framework's emergent tick. The Euler/Cayley control confirms the distinction,
and the tick remains an explicit top-priority residual.

### N8 — Cross-cycle echo

The direct parent exhibited multiple time laws with one static kernel. This
classification resolves that echo only after adding M1-M6. The kinetic-
isotropy source independently warns that equality of kinetic coefficients is
not a dynamics selector. Both boundaries survive unchanged.

**Gate result:** PASS for the scoped uniqueness and tick statements. The listed
routes were separated, the exact nullspaces and global generator were
executed, and every route outside M1-M6 remains open by name.

## Falsifiers

The conditional theorem fails if any of the following occurs inside M1-M6:

- a gauge-invariant one-face stencil is not proportional to
  `(1,1,-1,-1)`;
- proper cubic covariance permits unequal orientation coefficients;
- the role geometry contains a same-role physical nearest-neighbor pair;
- a nonzero real onsite scalar preserves a positive diagonal energy;
- conservation permits a reverse block not equal to the weighted negative
  adjoint;
- two allowed generators with the same speed are not related by a possible
  magnetic sign reversal followed by positive field rescaling;
- an allowed nonzero momentum lacks exactly two transverse branches; or
- the exact Euler or Cayley controls have the opposite locality/norm behavior
  on the named block.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=25 FAIL=0
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
conditional_surface_status: "Real linear continuous time, minimal edge/face payload, physical-neighbor stencil, gauge and cubic covariance, positive diagonal conserved energy; equivalence includes magnetic sign reversal."
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
