# A Role-Encoded Doubled Incidence Pattern Compiles the Gauge Measure Into One Nearest-Neighbor Site Law

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source note changes no
audit verdict, TOE score, axiom, or approved primitive.
**Direct parent:**
[`U1_AUXILIARY_FACE_LOCAL_CONDITIONALS_UNCONDITIONAL_GAUGE_MEASURE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_AUXILIARY_FACE_LOCAL_CONDITIONALS_UNCONDITIONAL_GAUGE_MEASURE_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Covariant-law comparison:**
[`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md)
**Internal/spatial-action boundary:**
[`COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md`](COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md)
**Runner:**
[`scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py`](../scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.txt`](../logs/runner-cache/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.txt)

## Result up front

Let `G=Z_N`, let `T:G->R_{>0}` be even, and use the universal-plus-matching
face factor of the direct parent. There is a finite role-and-payload alphabet
inside the one-site possibility domain and one site-independent conditional
rule with these properties:

1. Every physical site carries a role label `r in Z_2^3`. A candidate role is
   supported exactly when each of its two neighbors along axis `i` carries
   `r xor e_i`. The rule reads the six neighboring labels, not the site's
   coordinates.
2. The valid role configurations on an even periodic cubic lattice are
   exactly the eight translates

   ```text
   r_s(x)=x mod 2 xor s,       s in Z_2^3.
   ```

   Translation permutes them transitively. Proper cubic rotations permute
   their three role bits. Thus the law privileges no site or sector.
3. Hamming-weight-zero and Hamming-weight-three roles have a unit payload.
   Weight-one roles carry one oriented `Z_N` link value. Weight-two roles
   carry the parent's face auxiliary `star union Z_N^4`.
4. A face site's full conditional reads its four edge neighbors. An edge
   site's full conditional reads its four face neighbors. The remaining two
   neighbors only certify the role geometry. These are all physical
   nearest-neighbor sites.
5. In each role sector, summing every face auxiliary gives exactly

   ```text
   product_f T(Phi_f).
   ```

   The eight sectors have equal partition functions, so the finite covariant
   joint law is their equal mixture. No face outcome is selected.
6. The rule is covariant under translations, local `Z_N` gauge
   transformations, and all 24 proper cubic rotations. A rotation reverses
   an oriented link value when it reverses that link; evenness of `T` removes
   the induced face-orientation sign.

This closes the direct parent's **role geometry and physical nearest-neighbor
incidence interface** for finite cyclic models. It also gives a positive
answer to the possibility-state route left outside the two finite negative
classes in PR #7880: a field site can carry its changing payload and a role
label in the same local possibility. It does not contradict that PR. Its
value-reading class erased the role of every free code site, and its
state-reading class used a frustration-free projector kernel. This theorem
uses neither restriction.

The result remains a declared candidate Admissibility law. It does not derive
the choice of `T` or the role/payload alphabet from the four axioms, identify
the declared cubic relabeling with a canonical automorphism of `M_2(C)`, make
all labels orthogonally readable on one qubit, provide Record-formation
history, supply electric/time dynamics, or identify the gauge field with
electromagnetism.

## 1. The one-site alphabet

For every role `r in Z_2^3`, define its payload set by Hamming weight:

```text
|r|=0:             {unit}                 vertex role,
|r|=1:             Z_N                    edge role,
|r|=2:             {star} union Z_N^4     face role,
|r|=3:             {unit}                 cube role.
```

There are three edge orientations and three face orientations, so the total
number of finite labels is

```text
A_N = 2 + 3N + 3(1+N^4) = 5+3N+3N^4.
```

An explicit set-level injection into `M_2(C)` is obtained by enumerating the
labels `lambda_0,...,lambda_(A_N-1)` and sending

```text
lambda_k -> diag(k/A_N,1).
```

The matrices are distinct. This establishes possibility capacity, not a
canonical physical encoding. If every label must be mutually orthogonal and
readable, a composite needs at least `ceil(log2 A_N)` qubits: `6,10,14,18`
for `N=2,4,8,16`. If microscopic sites are smaller than the composite field
object, such an object may occupy many sites; the present one-site injection
is only the literal finite-support model.

The proper cubic group acts on the symbolic subalphabet by permuting role
axes, face slots, and edge orientations, with inversion of an oriented group
value when an axis reverses. The runner proves covariance under that declared
action. The current axioms constrain covariance of the rule but do not supply
an action tying spatial rotations to an internal `M_2(C)` automorphism. If a
stronger implementation requires the declared permutation to arise from a
specified algebra automorphism or an orthogonal spatial composite, that is a
remaining compiler obligation.

## 2. Roles arise from neighboring possibility labels

For adjacent sites `x` and `x+/-e_i`, impose the hard local condition

```text
r(x+/-e_i)=r(x) xor e_i.
```

Given a supported six-neighbor shell, there is exactly one central role that
satisfies these six equations. No absolute coordinate appears in the rule.
Starting from `r(0)=s`, propagation along lattice edges gives

```text
r(x)=s xor (x mod 2).
```

Path order does not matter because bit flips commute. On an even periodic
torus the result closes around every cycle, giving exactly eight sectors. On
an odd periodic axis, going once around flips one bit and demands
`r=r xor e_i`, so no valid periodic role field exists. That is a boundary
condition on this period-two construction, not an obstruction on `Z^3`.

Classifying by Hamming weight yields the doubled incidence geometry:

| central role | six-neighbor census |
|---|---|
| vertex | six edges |
| edge | two vertices and four faces |
| face | four edges and two cubes |
| cube | six faces |

This is the point missed by treating a dynamical edge site as merely a free
binary value. Its possibility is a pair `(role,payload)`. The payload may vary
while its role component continues to transmit the incidence structure to
both neighbors.

## 3. The physical face boundary is one nearest-neighbor star

Let a face role have ones on axes `i<j`. Its four edge-neighbor positions are
ordered

```text
x-e_j,  x+e_i,  x+e_j,  x-e_i.
```

They carry respectively the coarse oriented links

```text
a_i^-, a_j^+, a_i^+, a_j^-.
```

Therefore the face curl is

```text
Phi_f=a_i^-+a_j^+-a_i^+-a_j^- mod N.
```

All four sites are one physical lattice step from the face site. Conversely,
an edge role on axis `i` has exactly four adjacent face sites, at `x+/-e_j`
for the two `j!=i`. Thus every factor that changes when an edge value changes
is stored at one of that edge site's physical nearest neighbors.

No `5x5x5` observation window is used. The longer-scale gauge square is
represented by a radius-one incidence star because the physical lattice is
finer than the gauge object.

## 4. One fixed conditional rule

First solve the role equations from the six neighbor labels. On a supported
shell this gives one role. Apply the following payload branch:

- **vertex or cube:** the unit payload has probability one;
- **face:** use the direct parent's two supported probabilities

  ```text
  Pr(star|boundary)=epsilon/T(Phi),
  Pr(boundary|boundary)=1-epsilon/T(Phi),
  epsilon=(1/2)min T;
  ```

- **edge:** if all four adjacent face auxiliaries are `star`, use the uniform
  law on `Z_N`; otherwise the matching tuples require one common edge value,
  which has probability one.

Conflicting tuple demands and malformed role shells have zero probability in
the joint law below. A uniform distribution over the appropriate finite
alphabet defines a covariant total fallback there without altering any
supported conditional.

The rule is one conditional schema, not four coordinate-indexed laws. Which
branch applies is determined by the neighbor-carried role condition. It is
site-independent, reads only the six nearest neighbors, and varies in three
separate ways: different shells select different roles, face probabilities
vary with curl, and edge probabilities switch between uniform and fixed.

## 5. Compatible finite joint law

Let `C(r_x,r_y)` be one when adjacent roles differ in the bit for their edge
axis and zero otherwise. Define on an even finite torus

```text
mu(r,ell,h) proportional to
  [product_(nearest-neighbor pairs) C(r_x,r_y)]
  [product_(face-role sites f) F_f(h_f;ell_boundary)].
```

In a valid role sector, varying a face payload changes only its own `F_f`.
Varying an edge payload changes only the four `F_f` factors held by its face
neighbors. Varying a role away from the shell-determined value kills a local
`C` factor. The one-site full conditionals of `mu` are exactly the rule in
section 4.

For fixed roles and links, distributivity over the face auxiliaries gives

```text
sum_h product_f F_f = product_f T(Phi_f).
```

The direct parent proves connected payload support inside each role sector.
The eight role sectors are disconnected by one-site supported moves, but they
are related transitively by translations and have identical partition
functions. The normalized factor law above therefore gives them equal mass.
More generally, the displayed full conditionals determine the measure inside
each sector, and translation covariance fixes the eight relative constants.

In an infinite-volume limit, a pure translated sector may be selected as a
spontaneously broken phase. The finite law and its rule privilege none.

## 6. Symmetries

### Translation

Translating all sites by `a` maps sector `s` to `s xor (a mod 2)`. Link
orientations and boundary order are unchanged, so every face factor is
unchanged. The runner checks all 64 translations in all eight sectors on the
`4x4x4` physical torus.

### Gauge

An edge midpoint on axis `i` connects vertex-role sites `x-e_i` and `x+e_i`.
For a vertex potential `lambda`, set

```text
ell_i(x) -> ell_i(x)+lambda(x+e_i)-lambda(x-e_i).
```

The four vertex terms cancel around every face. Matching tuples transform
with their edge values and `star` is fixed. The runner checks every face of 64
sector-field pairs under two nonconstant local gauge transformations.

### Proper cubic rotation

A signed axis permutation sends an edge midpoint on old axis `i` to the new
axis and sends its value to `+ell` or `-ell` according to orientation. It
permutes a face's four slots. Its curl is the old curl or its negative, and
`T(-Phi)=T(Phi)`. The runner checks all 24 rotations in every sector, then
checks all `256` `Z_4` boundaries and all `257` face auxiliary labels under
each rotation. Both zero factors and the two supported factors covary.

## 7. Relation to the earlier two finite negatives

PR #7880 tested two narrower classes.

1. Its value-reading rule treated code sites as arbitrary binary values. To
   accept all intended code fillings, its maximal rule had to forget which
   free value occupied which role. Rival period-collapsed patterns then fit.
2. Its possibility-state rule was a frustration-free projector complement.
   The local kernel had to contain every intended role state and therefore
   contained linear superpositions that became global junk.

The present rule stores a classical role label alongside every changing
payload and uses conditional probabilities with hard adjacency support. A
code site is not role-free, and the accepted set is not a linear kernel. The
eight supported role fields are proved exactly by propagation from one site.
Accordingly this is a positive member of an open class named by #7880, not a
refutation of either theorem in that PR.

The scientific lesson is useful beyond this gauge model: information can be
carried through a site by its possibility state even when another component
of that possibility remains dynamical. “Free payload” does not imply “no
role information.”

## 8. What this changes in the TOE route

The constructive light/action chain is now

```text
neighbor-varying compact Record distribution
 -> positive even overlap kernel
 -> unconditional auxiliary gauge measure
 -> role-encoded physical nearest-neighbor conditional law
 -> positive magnetic Maxwell germ and two weak-field transverse modes.
```

Before this theorem, the third line lived on an abstract doubled edge/face
factor graph. It was open whether that graph could be made from the physical
site possibilities without a nonlocal coordinate-keyed rule. The role labels
and their six-neighbor propagation provide that finite compiler.

The former combined compiler wall should now be split:

- **closed here:** coordinate-free period-two role geometry, physical
  nearest-neighbor incidence, supported local full conditionals, translation
  and proper-cubic label covariance, and finite `M_2(C)` set capacity;
- **still open:** a canonical algebra-automorphism or orthogonal-composite
  implementation of the internal label action, if that stronger standard is
  required for physical readability.

The larger live walls are unchanged:

- why the physical Admissibility law selects this `T` and this auxiliary
  family rather than another allowed local distribution;
- how Records form from, and experimentally sample, the static law;
- the electric/time law and relative normalization;
- the electromagnetic dictionary; and
- compact interacting plus simultaneous thermodynamic, continuum, and
  quantum control.

No axiom update is requested by this result. The current Admissibility axiom
deliberately leaves its extensional distribution unspecified, so a declared
candidate law is allowed but not selected.

## 9. Executable evidence

The runner reports `TOTAL: PASS=23 FAIL=0`. It verifies:

- exactly eight period-two role fields on the even exhibit and unique
  propagation from the origin role;
- the odd-period frustration control;
- every role and every one of the `512` site shells on the `4x4x4` torus;
- the full `8+24+24+8` incidence census in all sectors;
- exact physical-face/coarse-curl equality for four complete link fields per
  sector;
- unconditional auxiliary marginalization and equal sector gauge products;
- all `256` face conditionals and `3,072` supported edge masks;
- gauge covariance, all `512` sector-translation pairs, all `192`
  sector-rotation pairs, and every auxiliary label under every rotation; and
- all `262,144` assignments of the six neighboring role labels, of which
  exactly eight admit one central role and all others invoke the total
  fallback; and
- the exact finite alphabet counts, `M_2(C)` injections, and orthogonal costs.

The general role classification is proved by path propagation, and the
general face marginal and within-sector compatibility are inherited from the
direct parent's finite theorem. The finite runner exhausts the declared local
and symmetry blocks rather than claiming an infinite interacting limit.

## No-Go Discipline Gate

This positive theorem carries four narrowed negative boundaries: an odd
periodic axis cannot support this parity construction; #7880's two classes do
not already contain this rule; local full conditionals alone do not fix
relative weights between disconnected role sectors without covariance; and a
set injection is not an orthogonal or algebra-automorphism compiler. The gate
below stress-tests only those statements.

### N1 — Alternative routes and same-cycle evidence

These attempts were checked analytically or by the paired runners in this
47-path review unit. Positive and partial constructions remain positive or
partial; none is recast as a failed route to satisfy a count. Named check
labels, rather than old ordinal numbers, identify the evidence. Cross-note
comparisons below are scope tests, not extra premises of this note.

| Route | Actual attempt and evidence | Result within the stated scope |
|---|---|---|
| Fixed coordinate roles | **ATTEMPTED:** Enumerate parity-origin exhibits and translate them (eight-sector and translation checks). | A fixed exhibit chooses an origin; carrying all sectors avoids making it the law’s preferred origin. |
| Role plus changing payload | **ATTEMPTED:** Propagate neighbor role flips and enumerate all supported and unsupported shells (§§1–3; propagation and fallback checks). | One covariant local rule realizes the stated finite role structure. |
| Unconditional auxiliary measure | **ATTEMPTED:** Sum the universal-plus-matching face payload (face-marginal and full gauge-product checks; auxiliary parent proof). | The supplied local conditionals realize the plaquette law without postselection. |
| Finite-set algebra encoding | **ATTEMPTED:** Inject every finite role/payload label into the M2(C) possibility domain (§1; distinct-injection checks). | This proves set capacity only, not an algebra automorphism or orthogonal readout. |
| Orthogonal spatial composite | **ATTEMPTED:** Count mutually orthogonal code dimensions for N=2,4,8,16 (§1; qubit-cost check). | The 6,10,14,18-qubit costs are a partial capacity result; a nearest-neighbor composite compiler is open. |

Homogeneous vertex storage, an internal algebra-action compiler and different
auxiliary factorizations remain live. Historical #7880 binary/kernel examples
are context for a change of alphabet, not retained authority excluding all
role encodings. The positive construction here is checked directly.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: extensional law selection.
- W2: strong internal/orthogonal implementation if required.
- W3: Record formation and sampling interpretation.
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

“Declared,” “candidate,” and “supplied” mark `G`, `T`, the finite alphabet,
the symbolic cubic action, and the off-support fallback. The role is carried
by a possibility label; it is not inferred from an unreadable Record. The
set injection is not called an orthogonal encoding. Equal sector mass follows
from the displayed finite factor law and translation symmetry, not from an
unstated ergodicity claim. No dynamics, canonical quantization, measurement,
or continuum interchange is smuggled into the compiler theorem.

### N4 — Residual matching

| Surface | Residual | Match here |
|---|---|---|
| direct parent | abstract link/face roles and physical compiler | **exact:** role geometry and physical nearest-neighbor incidence |
| PR #7880 | free-code value rules and projector state rules admit finite junk | **no contradiction:** this rule carries a separate role component and is not a kernel projector |
| minimal axioms | one covariant varying nearest-neighbor distribution, values unspecified | **shape match:** one explicit candidate law, no selection imported |
| covariant-Q8 comparison | finite-support laws can witness the Admissibility contract without becoming the physical law | **method match:** same bounded-model status |
| internal/spatial-action boundary | axioms supply no spatial action on `M_2(C)` | **exact residual:** symbolic covariance proved; canonical internal action not claimed |
| historical PR #7903 | finite matter/gauge join lacks an interacting photon | **no closure:** this theorem supplies a magnetic probability law, not that finite spectrum |

The proof stands after dropping both historical-PR comparisons.

### N5 — Rhetoric and resolution audit

“Exactly eight” is a classification of the displayed neighbor-bit equations
on an even torus. “No odd-period solution” is only for that parity
construction. “Nearest neighbor” names the physical radius-one incidence
shell actually enumerated. No general role-marking impossibility, unique
physical law, or full photon theory is claimed.

The cached stdout supplies:

```text
per_element: every finite role label, Z4 face boundary, and auxiliary label is checked under its declared transformations
per_site: all 512 supported physical shells and all 3072 edge masks use only six nearest neighbors
per_mode: checked and not executed — the compiler preserves but does not recompute the parent photon Hessian
per_block: all eight L4 role sectors, 64 translations, and 24 proper cubic rotations are checked
lattice_wide: four full link fields per sector are marginalized and compared across the 4x4x4 physical torus
```

### N6 — Partial-closure paths and primitive check

The current primitive registry and approved premise sources were checked. The
scale-reference primitive fixes units only. The kinetic-isotropy primitive
does not select this static factor law or compile its labels. The
realized-state primitive is pointwise evaluation, not a probability selector.

Live positive continuations are:

- build the orthogonal spatial-composite version and verify that every direct
  dependence remains nearest-neighbor;
- find a cubic-equivariant algebraic encoding for the symbolic label action;
- combine the same role compiler with temporal/electric local factors;
- derive the conditional table from a smaller consistency principle; or
- connect its static measure to a fresh-site Record-formation experiment.

### N7 — Steelman

A hostile reviewer can say the role label is simply the old coordinate parity
written into the state and therefore explains no physics. The exact answer is
that it is not coordinate-keyed by the law: all eight offsets are supported
equally, translations permute them, and the local shell determines every
role. It is a spontaneous period-two order parameter. The reviewer is still
right that selecting this ordered phase and this payload law is model input,
not an axiom derivation. That remaining selection wall is stated rather than
renamed.

The reviewer can also reject the set injection as too weak for a physical
qubit readout. The note accepts that stronger reading, reports the exact
composite cost, and leaves the covariant orthogonal compiler open.

### N8 — Cross-cycle echo

PR #7880 is the direct echo. Its own boundary explicitly leaves open rules on
pre-Record possibility states other than projector complements. This theorem
occupies that opening and preserves its two finite results. The separate
internal/spatial-action note warns that lattice symmetry does not itself
supply an internal `M_2(C)` action; this theorem therefore does not turn its
declared label permutation into axiom content.

**Gate result:** PASS for the four scoped boundaries. The listed materially
different routes were separated, the positive role-plus-payload route was
executed, the two earlier negatives were residual-matched rather than
generalized, and both stronger internal compilers remain live.

## Falsifiers

The finite compiler theorem fails if any of the following occurs:

- a valid six-neighbor shell admits zero or more than one central role;
- an even torus admits a role field outside the eight propagated sectors;
- a face or edge payload reads a site beyond its six physical neighbors;
- the physical boundary curl differs from the coarse plaquette curl;
- summing all face auxiliaries fails to recover `T(Phi)`;
- translated sectors have unequal gauge products or partition functions;
- a local gauge transformation changes a face curl;
- a proper cubic rotation changes a local factor after its declared label
  relabeling;
- the one-site finite alphabet does not inject into `M_2(C)`; or
- the displayed one-site full conditionals disagree with the finite joint
  factor law.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=23 FAIL=0
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
conditional_surface_status: "Even periodic role lattice and supplied finite role/payload conditional family; finite-set encoding supplies no orthogonal readout or algebra action."
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
