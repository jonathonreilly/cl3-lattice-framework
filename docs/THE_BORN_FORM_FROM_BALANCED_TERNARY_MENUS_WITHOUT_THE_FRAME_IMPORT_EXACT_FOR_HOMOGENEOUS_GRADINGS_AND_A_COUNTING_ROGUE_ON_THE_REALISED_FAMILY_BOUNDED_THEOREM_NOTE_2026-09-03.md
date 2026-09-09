---
claim_id: born_form_from_balanced_ternaries_without_frame_import_2026_09_03
claim_type: bounded_theorem
claim_scope: "Self-contained homogeneous rank-one theorem, exact finite angle/radius certificates and a repaired indexed counting rogue. Scalar identity grades need separate coin hypotheses. The former import-free all-scale measurable Theorem B remains unestablished."
upstream_dependencies:
  - minimal_axioms
runner: scripts/born_form_from_balanced_ternaries_without_frame_import_check_2026_09_03.py
---

# Homogeneous rank-one Born form, a counting rogue and finite scale certificates

**Type:** bounded_theorem

Original date: 2026-09-03. Current correction: 2026-09-09.

[Primary runner](../scripts/born_form_from_balanced_ternaries_without_frame_import_check_2026_09_03.py) · [current cache](../logs/runner-cache/born_form_from_balanced_ternaries_without_frame_import_check_2026_09_03.txt)

## A — homogeneous rank-one theorem

Let F:S^2->[−1,1], and assume w(cP(n))=c(1+F(n))/2 for0<c<=1.
Suppose every non-collinear positive rank-one ternary resolution of I is
normalized (and binary normalization is allowed). Then F(n)=r.n for a unique
|r|<=1, so w(cP(n))=Tr(rho cP(n)), rho=(I+r.sigma)/2. This statement
covers rank-one effects only. Rank-one homogeneity does not determine
w(cI); scalar grades require the additional coin equations described below.

Here is an algebraic proof, without a frame theorem or regularity premise.
On any great-circle plane define g(v)=|v|F(v/|v|), g(0)=0. For independent
u,v, the triangle (u,v,-u-v) can be rescaled to perimeter2; strict triangle
inequalities put each resulting coefficient in(0,1). Normalization gives

    g(u)+g(v)+g(-u-v)=0.

Set h(v)=g(v)+g(-v). Adding the equations for (u,v) and(-u,-v) gives
h(u+v)=-h(u)-h(v), and replacing v by -v gives the same for h(u-v).
The pair u+v,u-v is independent, so
h(2u)=-h(u+v)-h(u-v)=2h(u)+2h(v).
Positive homogeneity also gives h(2u)=2h(u), hence h(v)=0. Thus g is odd.
It is additive for independent arguments by the first equation and for
collinear arguments by real homogeneity. Hence it is a real linear
functional on the plane. Using the xy-plane and each plane spanned by e_z
and a direction of the xy-plane glues one common r on the sphere. The bound
|F|<=1 in every direction forces |r|<=1. This proves A pointwise without
measurability. It does not prove scale homogeneity itself.

On one circle the same proof gives a linear restriction with coefficient
norm<=1 and at least one density extension. Two nonparallel circles agreeing
on their intersection give a unique trace-one Hermitian representer, with
positivity only if its full |r|<=1. The functions y on xy and z on xz give
r=(0,1,1), whose smaller eigenvalue is(1-sqrt(2))/2<0. Thus two-circle
positivity is an additional compatibility condition.

## Exact certificates and the hypothesis they test

The52-point rational grid yields5200 non-collinear ternaries. Their weights
include both extrema1/21 and696/697 and lie in the **closed** interval between
them, within(0,1). No non-collinear ternary contains a projector: a side of
length1 forces equality in the remaining triangle inequality and collinearity.
All1326 grid pairs verify the strict inequality away from equal directions.

Finite ranks remain:52 free grid values/5200rows rank50; modes0..8 with
17columns/400rows rank15; four rational frames give12 great circles; degree<=6
sphere sections have49columns/168rows rank46. The kernels are respectively
the sampled two plane coordinates, cos/sin, and x,y,z. These finite results
are diagnostics; the proof above supplies the untruncated homogeneous claim.

The earlier notes explicitly used the hidden scale assumption:
“In the normal form `w(cP(u)) = c(1 + f(u))/2`” and
“Take the polynomial sector `w(c P(u)) = c(1 + f(u))/2`”. Their row expression
`row = [r + c * v for r, v in zip(row, f_row(n, a_mons, b_mons))]`
is already homogeneous. Those ranks cannot establish that assumption.

## B — repaired counting rogue on the smaller indexed family

Set w(P(n))=1/2, w(cP(n))=1/3 for0<c<1,
w(cI)=1/2 for0<c<1, and **w(I)=1**. Every binary antipodal projector tuple,
non-collinear rank-one ternary, binary coin and singleton(I) is normalized.
Repeated I/2 payloads remain two indices until pushforward aggregation.
The existing continuum compiler emits these types; it does not emit mixed
rank-one/scalar or collinear rank-one ternaries. The finite retained test
has5271 menus:5200 ternaries,52 binaries,19 coins; the current additional
guard covers the previously omitted singleton(I). This is one grade on
abstract effect payloads for indexed menus, not a physical unindexed law.

The rogue is not homogeneous: w(P)=1/2 but w(P/2)/(1/2)=2/3.
A collinear tuple (aP,(1-a)P,P(-n)) at a=1/4 sums7/6; the mixed tuple
(cP(n),cP(-n),(1-c)I) at c=1/2 also sums7/6. These lie outside the smaller
family and show how adding menus can reject the rogue.

The algebraic interior family

    W(cn)=(1/2+lambda)c-2lambda/3+beta.(cn)

sums1 on a balanced ternary for any parameters, since sum c=2 and sum cn=0.
It is not generally a probability grading. **For beta=0 only**, range[0,1]
on every0<c<1 holds exactly for lambda in[−3/2,0]: the endpoint limits are
−2lambda/3 and1/2+lambda/3, and the function is affine. With beta=e_x,
lambda=0,c=3/4,n=e_x the value is9/8. The current code tests that boundary;
it does not advertise the beta-free lambda condition for arbitrary beta.

## C — full-family conditional implication and unresolved import-free proof

From binary and ternary scalar coins, u(c)=w(cI) is additive for positive
arguments summing below1, monotone by nonnegativity, and u(1)=1; rational
squeezing gives u(c)=c. Mixed menus then imply W(cn)+W(-cn)=c. These are
additional hypotheses, not consequences of A's rank-one homogeneity.

The parent states, verbatim:

> **Low-arity eligibility.** Every two- or three-member menu is normalized: `sum_j w(E_j)=1`.

> `F` is a nonnegative normalized frame function on `C^3` with no continuity, measurability, differentiability, or countable additivity premise added.

> By the named dimension-three frame theorem, there is a unique positive operator `R on C^3` with `Tr(R)=1`

Under that full family and the named frame theorem the conditional trace-form
implication remains available. The original advertised **import-free
all-scale/measurable Theorem B is unestablished here**. Its Fourier proof
omitted the reflected-triangle constraint, did not prove zero propagation
through all radii, and did not justify passage from surface measurability to
arbitrary great-circle restrictions. No theorem or cache PASS is assigned to
those missing steps; no counterexample to the full parent family is claimed.

The finite results are retained exactly: on24radii j/24, coin rows144 have
rank23/kernel c. There are44 declared perimeter-two triangles. For the smaller
family, mode0 and1 nullities are3, modes3,5,7 nullities2; radius1/24 is
uncovered, and the projector boundary remains free. The covered mode0
interior carries c-2/3; mode1 carries c; higher tested modes vanish there.
With the additional full-family rows the24-column ranks are24 for modes
0,3,5,7 and23 for mode1 (111rows), kernel c. This is a finite scale/mode
certificate and supplies neither missing all-mode proof nor physical
eligibility. All original ARG IDs remain as explicit unresolved or bounded
argument records, excluded from machine totals.

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

The homogeneous theorem is PROVED under its extra hypothesis. The nonhomogeneous counting rogue on the smaller family is ATTEMPTED and survives; the full mixed/collinear family rejects it. The import-free all-mode route remains OPEN because its missing proof steps are not repaired by finite ranks.

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

The parent full-family frame theorem closes a conditional mathematical representation step with a named import; it does not certify the advertised import-free proof or the physical compiler. The current memo supplies the constitutional comparison only;
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

A rigorous all-radius argument with correct reflected equations and measure restrictions could establish a larger import-free theorem. Nothing in the retained finite nullspaces rules this out. This route remains open; the scoped counterexamples do not close it.

### N8 — cross-unit correction

#7912/#7919/#7926 homogeneous matrices motivated A, while the repaired rogue corrects their attempted scale-free inference. Historical statements are preserved as provenance rather than counted
as independent corroboration. The present dispositions replace those claims.
