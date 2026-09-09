---
claim_id: continuum_alphabet_lifts_abundance_no_go_fibred_born_factor_two
claim_type: bounded_theorem
claim_scope: "Exact rational continuum-direction compiler, selected unit-dipole fibres and homogeneous finite ranks. The round affine-density fixed-cell obstruction is restricted; no full Record law, all-fibre abundance, two-circle positivity, or scale-free Born theorem is established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/continuum_alphabet_lifts_abundance_no_go_fibred_born_check_2026_09_04.py
---

# Continuum indexed-menu construction, homogeneous fibres and a restricted density bound

**Type:** bounded_theorem

Original date: 2026-09-04. Current correction: 2026-09-09.

[Primary runner](../scripts/continuum_alphabet_lifts_abundance_no_go_fibred_born_check_2026_09_04.py) · [current cache](../logs/runner-cache/continuum_alphabet_lifts_abundance_no_go_fibred_born_check_2026_09_04.txt)

## Conditional input/output model

L_CONT takes a partial map from the six signed unit **slots** to unit Bloch
vectors. These are bare direction inputs; a general scalar/scaled Record
payload is not decoded. One occupied slot emits (P(u),P(-u)); three emit their
unique positive rank-one ternary resolution if one exists, otherwise (I).
Two inputs emit (aI,(1-a)I), a=(1+u.v)/2, for 0<a<1, otherwise (I).
Other counts emit (I). This is a supplied indexed-menu compiler, not a full
iterated physical law on the original scaled effect/Record domain.

Every positive non-collinear rank-one ternary resolution is reconstructed by
placing its three directions in three slots: its positive weights are the
unique solution of sum c_i=2 and sum c_i u_i=0. Every rank-one binary is emitted by
one input. Every coin parameter 0<a<1 can be emitted by choosing a pair with
u.v=2a-1. **There is no mixed rank-one/scalar ternary branch.**

The original exact samples remain: 80 rational directions, 14 plane frames,
1764 ternaries; a rotation-closed 78-value sample, 1740 conditions, 41760
covariance comparisons and 228 distinct sorted indexed-menu keys. The
abundance probes include 80 binaries, 1200 ternaries and 77 coin values.
These finite probes support the explicit construction, not its physicality.
Duplicate effects retain multiplicity as explained under Domain below.

## Fibres and the corrected conditional implication

lambda(n) is the sum of the occupied slot directions, independent of values.
It is equivariant. For lambda=e_x, a one-slot pattern (+e_x) emits all binaries;
the three-slot pattern (+e_x,+e_y,-e_y) emits all non-collinear rank-one
ternaries. Rotations give the other five unit-direction fibres. This says
nothing comparable about every fibre: the empty input has lambda=0 and
emits (I). No two distinct signed-unit slots sum to e_x, so no coin branch
occurs in that unit fibre; no mixed ternary occurs anywhere.

The explicitly chosen Bloch state r_lambda=(2/3)lambda for a unit-direction
label and r_lambda=0 otherwise yields normalized, nonnegative indexed Born
grades. The sample has 83520 per-outcome covariance comparisons. This is a
constructed example, not a forced state assignment. Two ternaries with
coefficients (8/9,5/9,5/9), in the xz and yz planes, share (8/9)P(e_z) in
the e_x fibre and establish a nontrivial overlap.

The polynomial rows assume w(cP(u))=c(1+f(u))/2. They have 21 odd columns,
rank18/nullity3 and kernel x,y,z; the 36-column unrestricted version has
rank33/nullity3. They do not prove scale homogeneity. A correct sufficient
implication on an abundant fibre is **additionally homogeneous rank-one
grading**, in range and normalized on its full binary/non-collinear ternary
family; the self-contained homogeneous proof is supplied in the
[balanced-ternary note](THE_BORN_FORM_FROM_BALANCED_TERNARY_MENUS_WITHOUT_THE_FRAME_IMPORT_EXACT_FOR_HOMOGENEOUS_GRADINGS_AND_A_COUNTING_ROGUE_ON_THE_REALISED_FAMILY_BOUNDED_THEOREM_NOTE_2026-09-03.md). Its conclusion is rank-one Born form only.
Alternatively the frame-function theorem can be invoked only after its
**full** eligible menu family is supplied. Neither route is supplied by the
sentence “menu independence” or by this compiler in every fibre.

## Restricted round-density obstruction

With round measure dmu=dOmega/(4pi), density 1+r.u for |r|<=1 integrates to1,
and integral 2P(u)dmu=I. A fixed measurable cell A required to represent P(e_z)
for **every r** would need mu(A)=1/2 and integral_A u dmu=e_z/2. But for any
half-area cell, its moment norm is at most1/4: align its moment with z and
maximize integral_A u_z by choosing the upper hemisphere. The exact hemisphere
has area1/2 and moment e_z/4. This proves the factor-two obstruction only
for this round affine-density family and a state-independent cell valid for
all states.

It is not a classification of all continuum densities or protocols. For a
fixed frame the nonnegative density 1+r_z sign(u_z) gives its upper hemisphere
probability1/2+r_z/2. This density is discontinuous on a continuous domain;
no claim of continuity of the density is made. The affine density is strictly
positive for |r|<1, but vanishes at the antipode for |r|=1. Point probabilities
are still zero for this absolutely continuous measure. An exact-point Lüders
formula is a separately supplied conditional instrument, not conditioning an
event of positive measure or proof of physical Record locking.

## Other compilers, symmetry and circles

L_COIN emits only scalar coins; L_BIN emits only antipodal rank-one pairs
or (I). Their menu-map covariance samples each have9600 comparisons. The
fixed f(u)=u_z^3 is odd, in range, and non-Born on binaries, but **not cubic
covariant as a global odds assignment**: f(e_z)=1 and f(e_x)=0. Covariance of
a compiler and covariance of its associated grading are separate conditions.

For a supplied equivariant Bloch-state assignment, the full cubic group fixes
only0; the order-four stabilizer of e_x fixes span(e_x). Thus an invariant
label under that particular action has maximally mixed state. A nontrivial
G-set can carry nonzero states; it need not literally be a direction-valued
physical Record or be supplied by the axioms.

On the z=0 circle the original2470 homogeneous rows have global nullity17;
Fourier modes1,3,5 have rank4/nullity2. f=u_z^3 vanishes there and fails1506
of1764 rows across14 planes. The full homogeneous one-circle theorem follows
from the balanced-ternary proof: bounded f is linear in the two plane
coordinates and has a density extension. Two nonparallel circles agreeing on
their intersection determine a unique trace-one **Hermitian** representer;
it is a density only with the extra compatibility |r|<=1. Indeed f=y on xy
and f=z on xz glue to r=(0,1,1), giving eigenvalue(1-sqrt(2))/2<0. No
independent wall count or minimal three-price conclusion remains.

## Domain, authority and evidence

The [current minimal-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) is the
constitutional authority. Its local possibility presentation, probability
law and permanent Record boundary do not identify physical outcomes with
scaled effects, create an indexed menu compiler, or select a density matrix.
This note makes no canonical axiom edit. It derives no physical formation,
occurrence, frequency, clock, or nearest-neighbour Born law.

For a unit vector n, P(n)=(I+n.sigma)/2. The scaled domain is
S={cP(n),cI:0<c<=1}; zero can be adjoined with grade zero for the full
parent theorem.

A menu here is an **indexed finite tuple** of nonzero effects whose operator
sum is I. Its probabilities are on indices. When equal effect payloads are
reported without their indices, their probabilities must be **summed**.
For example, (I/2,I/2) has two indexed probabilities 1/2; its pushforward has
one payload I/2 of probability 1, and that distinct-payload set sums to I/2.
An indexed resolution is therefore not literally the support of a probability
measure over unindexed Record contents. This interface is supplied mathematics,
not an extension of the physical Record alphabet or permission to overwrite
permanent records. No iterated input/output closure is asserted.

The [frame-lift note](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md) is read for its stated conditional
mathematical family and quoted formulas only. The implication using its
standard dimension-three frame-function theorem is conditional on that named
theorem and **every** binary/ternary scaled menu, including repeated/collinear,
mixed and coin menus. The smaller family of non-collinear rank-one ternaries
does not satisfy that hypothesis. Historical parent Record-additivity,
physical-campaign, and audit-status passages supply no authority here. No
parent runner or campaign is executed or accepted by a quote check.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
artifact_role: theorem
reachability_to_target: advances
next_trace_action: "Resolve the stated mathematical or physical supplier boundary; formal audit is deferred until a solid TOE."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Independent audit remains required before any effective retained status;
formal audit is deferred under the current owner directive. Source checks and
cached PASS counts are execution evidence, never audit grades or proof of
physical realization. Exact rational certificates and float64 diagnostics
are distinguished below. All original notes, runners and caches, including
incorrect claims and both earlier corrected note versions, remain immutable
outside active discovery in the dated correction packet.


## No-Go Discipline Gate

### N1 — actual alternatives

The finite alphabet obstruction is evaded by the displayed continuum input compiler (ATTEMPTED). The round affine-density cell fails (ATTEMPTED); the fixed-frame sign-density alternative succeeds outside that affine family (ATTEMPTED). A physical typed Record interface remains OPEN.

These are the actual examined alternatives, not an exhaustive route count.
No procedural packet PASS or arbitrary route quota is claimed.

### N2 — implication boundary

The model's typing, grade functionality, menu eligibility and physical
realization are not claimed to be pairwise independent. Their implication
relations remain unresolved. Rank-one homogeneity is an additional sufficient
mathematical hypothesis; it does not follow from the smaller menu family.
There is no proved minimal three- or four-price count.

### N3 — hidden premises

Indexed effects, the declared input alphabet, supplied state/conditioning,
finite volume and numerical tolerance are explicit premises. Menu-map
covariance does not prove odds covariance, physical admissibility, or Record
formation. Quoted parent source is not a fresh theorem or campaign result.

### N4 — residual matching

The hemisphere moment closes only the round affine fixed-cell residual. The homogeneous circle proof concerns rank-one grading, not all-scale or coin forcing. The current memo supplies the constitutional comparison only;
it is not evidence that every constructive physical route is impossible.

### N5 — resolution

The runner reports per_element, per_site, per_mode, per_block and lattice_wide
scope. Finite rows do not certify unsampled scales/modes, and finite cube
conditioning does not certify an infinite or nearest-neighbour physical law.
The negative statements apply only to their displayed families and witnesses.

### N6 — partial closure

The exact finite calculations and conditional positive theorem remain useful.
A typed physical outcome interface, an actually realized larger menu family,
or an additional proved regularity/scale relation could close further gaps.
No new primitive or axiom is required or proposed by inference here.

### N7 — strongest counter-route

Changing the density family or supplying an actual larger indexed instrument can defeat broad per-condition rhetoric without changing the verified hemisphere integral. This route remains open; the scoped counterexamples do not close it.

### N8 — cross-unit correction

#7919 supplies the finite-domain comparison; #7950 corrects the hidden scale hypothesis and the two-circle positivity boundary. Historical statements are preserved as provenance rather than counted
as independent corroboration. The present dispositions replace those claims.
