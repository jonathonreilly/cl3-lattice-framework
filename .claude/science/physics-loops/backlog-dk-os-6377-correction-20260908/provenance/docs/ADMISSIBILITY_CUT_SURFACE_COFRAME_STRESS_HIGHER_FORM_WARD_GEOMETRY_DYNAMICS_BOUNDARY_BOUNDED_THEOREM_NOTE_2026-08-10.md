---
claim_id: admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "On a supplied finite periodic cubic binary sector, the code-symmetric cut action admits an explicit positive local-coframe Gibbs family. Local cofactor-column areas weight the cut faces and reduce at the identity coframe to the Block-10 action. The exact flat first variation is the tangential surface response P_i=tau[(Tr Q_i)I-Q_i], not the normal cut tensor Q_i. Pullback to a centered displacement coframe gives an exact periodic virtual-work identity and global translation Ward identity; local divergence vanishes only on a supplied geometry equation, with planar and singleton fixtures separating on-shell and forced surfaces. The signed cut is the boundary of the occupied dual-cube chain and therefore has an independent exact off-shell higher-form Ward identity. The full finite log-partition Hessian contains both connected covariance and same-family coframe seagull terms. No physical coframe selection, action unit, projective family, geometry dynamics, curvature action, field equation, coupling, stress-energy identification, gravity, axiom necessity, or adoption is proved."
upstream_dependencies:
  - minimal_axioms
  - scale_reference_primitive
  - admissibility_code_swap_cut_area_local_source_improvement_metric_response_axiom_boundary_bounded_theorem_note_2026-08-10
  - observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21
  - universal_gr_stress_ward_transverse_seagull_bounded_theorem_note_2026-06-08
runner: scripts/admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_2026_08_10.py
---

# Cut-Surface Coframe Stress, Higher-Form Ward Identity, And Geometry-Dynamics Boundary

**Date:** 2026-08-10
**Type:** bounded theorem and axiom-consequence map
**Scope:** supplied finite periodic cubic binary sectors and one explicit
local-coframe source family. No physical geometry or dynamics is inferred.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_2026_08_10.py](../scripts/admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_2026_08_10.py)

## Result Up Front

Block 10 proved that the code-symmetric compatible binary action is exactly a
cut-area functional. This block constructs the missing off-background family
rather than only naming it.

Let `x_i in {0,1}` on a finite periodic cubic quotient. For the positive edge
from `i` in axis `a`, define the signed jump and cut indicator

    j_i,a=x_(i+e_a)-x_i,
    chi_i,a=j_i,a^2=|j_i,a|.

At each site supply an orientation-preserving local coframe `F_i`. Its
`a`-normal face-area factor is

    A_i,a(F_i)=|cof(F_i)e_a|.

Share each cut edge between its two endpoint coframes:

    m_i,a=(chi_i,a+chi_(i-e_a),a)/2.

For statistical surface coefficient `tau`, the geometry-indexed action is

    S_cut[x;F,B]
      =tau sum_(i,a) m_i,a A_i,a(F_i)+<B,J>.          (1)

Here `J` is the signed oriented dual surface with face coefficient `j_i,a`,
and `B` is an optional supplied real dual two-form source. At `F_i=I` and
`B=0`, equation (1) is exactly

    S_cut=tau C_X.

Taking `tau=(log B_code)/2` recovers the Block-10 compatible action. For every
finite `F,B`, normalization of `exp[-S_cut]` gives one positive joint law.
Its one-site conditional is local and is derived from the same action; static
compatibility is therefore built in on this finite surface.

The flat coframe derivative is exact. Let

    Q_i=sum_a m_i,a e_a e_a^T.

Then

    P_i=tau[(Tr Q_i)I-Q_i].                           (2)

For one cut face normal to `e_a`, its contribution is

    tau(I-e_a e_a^T),

the tangential surface projector. This corrects an important possible
misidentification: `Q_i` records face normals, while the area derivative
responds tangentially. `P_i` is a fully derived coframe response of (1), but it
is not a physical stress-energy tensor until the coframe family and action
unit are physically licensed.

Now pull the coframe source back to a centered displacement field:

    F_i[u]=I+D^0 u_i,
    (D^0_a u)_i=[u_(i+e_a)-u_(i-e_a)]/2.

For the full nonlinear coframe response
`P_i=partial S_cut/partial F_i`, periodic summation by parts gives

    delta S_cut/delta u_i=-div^0 P_i.                (3)

Equation (3) is an exact virtual-work identity. It implies zero total force by
translation telescoping. It becomes local stress conservation only when a
geometry equation sets the left side to zero. The exact flat wrapping-plane
fixture has `div^0 P=0`; the singleton has nonzero local force but zero total
force. Thus the family supplies the stress map and its on-shell Ward shape,
while geometry dynamics remains a separate obligation.

There is also a stronger conservation law of a different type. The occupied
dual cubes form an oriented three-chain `U`, and their signed interface is

    J=partial U.

Therefore

    partial J=0.                                      (4)

Equation (4) holds for every binary configuration, without an equation of
motion. Equivalently, the primal signed jump is an exact one-cochain and has
zero integer plaquette curl. Consequently `<B,J>` is invariant under the
dual two-form gauge shift `B -> B+delta Lambda`. This is an off-shell
higher-form Ward identity for interface orientation. It is not energy-
momentum conservation and does not substitute for (3).

Finally, the geometry family fixes the contact terms that Block 10 could not
obtain from one background value. If `Psi=log sum_x exp[-S_cut]` and prime
denotes any coframe-source path, then

    Psi'=-E[S'],
    Psi''=Cov(S',S')-E[S''].                          (5)

The second term is the same-family coframe seagull. It is nonzero even along
an offdiagonal shear with zero first variation. The source family therefore
derives both the first insertion and its local contact term; no external
stress ansatz is needed on this conditional model.

This is a real constructive closure of the **existence** branch left by Block
10. It does not select this family physically, supply a geometry equation, or
derive gravity. No canonical axiom is edited, and the fixed TOE percentages
do not move. Finite normalization is established here; projective consistency
remains open.

## Machine Status And Trace

~~~yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The finite coframe Gibbs family, flat tangential response, exact virtual-work identity, global translation Ward identity, oriented-surface higher-form Ward identity, and connected-plus-seagull response formula are derived exactly; physical source/action licensing, projective consistency, geometry dynamics, curvature law, field equation, coupling, gravity, and axiom adoption remain open."
trace_class: upstream_support
target_claim_id: admissibility_cut_coframe_stress_to_physical_geometry_dynamics_bridge
target_blocker_text: "physically license one geometry-indexed probability family together with its local unnormalized action representative, geometry-dependent action zero, and action unit, then supply the geometry equation whose on-shell Ward identity couples the derived cut stress to a curvature or metric response"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Test whether a current model-level local action or a narrowly amended Lattice/Admissibility surface can select the coframe family and a local geometry action without inserting the target field equation by hand."
conditional_surface_status: "one explicit positive coframe-indexed cut Gibbs family now derives its tangential first variation, exact virtual-work identity, higher-form surface current, and local seagull; physical family selection and geometry dynamics remain supplied"
hypothetical_axiom_status: "an explicit geometry-family and dynamics amendment is sufficient to type this response physically; it is neither adopted, proved necessary, nor claimed minimal"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## Exact Target Contract

| Contract field | Block-11 value |
|---|---|
| target statement | construct one local geometry-dependent continuation of the exact cut action and derive its first variation, contact term, and precise conservation identities |
| quantifiers/domain | arbitrary binary configurations on finite periodic cubic quotients; arbitrary orientation-preserving local coframes for the action; centered displacement subfamily for virtual work |
| allowed premises | Block-10 cut theorem, elementary cubical chains, finite probability, cofactor algebra, exact finite differences, and explicitly supplied sources |
| forbidden weakenings | calling a source choice physical, treating a normalized probability family as fixing its geometry-dependent action zero, calling global telescoping local conservation, identifying the higher-form current with stress-energy, or inserting an Einstein/Regge equation as the update |
| required edge cases | identity and anisotropic coframes, complement, local flips, proper cubic rotations, uniform dilation, normal stretch, offdiagonal shear, wrapping plane, singleton, and oriented surface closure |
| completion witness | explicit normalized Gibbs family, exact flat Piola map, summation-by-parts identity, two conservation classes, seagull decomposition, and exact runner |
| outcomes not counting as closure | one arbitrary tensor insertion, a background-only covariance, an unsigned mod-two surface alone, a globally conserved but locally forced fixture, or candidate axiom wording |

## 1. Geometry-Indexed Cut Gibbs Family

Let `V=(Z/LZ)^3`, with `L>=3`, and take every positive oriented nearest-
neighbor edge once. Define

    j_i,a=x_(i+e_a)-x_i,
    chi_i,a=j_i,a^2.

The unsigned cut size is

    C_X=sum_(i,a) chi_i,a.

For a local coframe `F_i in GL^+(3,R)`, define its cofactor face vectors and
areas

    n_i,a=cof(F_i)e_a,
    A_i,a=|n_i,a|>0.                                 (6)

The `a`th cofactor column is the cross product of the other two coframe
columns. Thus (6) is the area of the corresponding local parallelogram face.
This is a declared corner/coframe source family. Away from affine fields it is
not claimed to be a unique embedding of a curved hexahedral complex.

Use the symmetric endpoint share

    m_i,a=(chi_i,a+chi_(i-e_a),a)/2.                 (7)

Then the area part of (1) has two exactly equal forms:

    S_area=tau sum_(i,a)m_i,a A_i,a
          =tau sum_(i,a)chi_i,a [A_i,a+A_(i+e_a),a]/2.  (8)

Equation (8) counts each cut edge once and assigns it the mean area of its two
endpoint coframes. Endpoint symmetrization is what makes the local site
carrier transform cleanly under signed proper-cubic axis rotations.

At `F_i=I`, every `A_i,a=1`; hence

    S_area=tau C_X.                                  (9)

With `tau=t/2`, `t=log B_code`, equation (9) is exactly the Block-10
code-symmetric action.

### Positive joint law and exact local conditionals

For any finite real two-form source `B`, define

    pi_(F,B)(x)=Z[F,B]^-1 exp[-S_cut[x;F,B]].         (10)

The state space is finite and every weight is positive, so (10) exists and is
normalized. If an empty site `i` is changed to occupied, only its six incident
cut edges change. Write the mean endpoint area on edge `<ij>` as
`Abar_ij`. Then

    Delta_i S_area
      =tau sum_(j~i) Abar_ij(1-2x_j).                (11)

The one-site odds are `exp[-Delta_i S_cut]`. They are therefore local full
conditionals of the single joint law (10), not separately specified kernels.
At the flat source with `tau=t/2`, equation (11) becomes

    Delta_i S=t(3-k_i),
    odds=B_code^(k_i-3).

Thus the geometry family continues the compatible count law rather than
replacing it with an unrelated stress ansatz.

There is a necessary normalization distinction even on this finite model. The
replacement

    S_cut -> S_cut+c(F,B)

by any configuration-independent function leaves `pi_(F,B)` unchanged, but
it shifts the first and second derivatives of the unnormalized action and of
`Psi`. Therefore a normalized law alone does not determine its absolute
coframe response. This block explicitly declares the local representative
(1), including its geometry-dependent additive zero. A physical source law
would have to license that representative or an equivalent normalization,
not only `pi_(F,B)`.

This finite construction does not prove a projectively consistent family
under changes of region, an infinite-volume phase selection, or a temporal
update process. Projective consistency remains open.

## 2. Exact Flat Coframe Derivative

Let `F=I+H` infinitesimally. The cofactor identity gives

    delta[cof(F)]_(F=I)=Tr(H)I-H^T.

Taking the norm of its `a`th column at the unit vector `e_a` gives

    delta A_a=Tr(H)-H_aa.                            (12)

Define the local normal-area tensor

    Q_i=sum_a m_i,a e_a e_a^T.                      (13)

Using (12),

    delta S_area
      =sum_i P_i:H_i,

with

    P_i=tau[(Tr Q_i)I-Q_i].                          (14)

Equation (14) is the complete flat first variation of the declared coframe
family. It is not chosen by representation matching.

For one face with normal `n=e_a`, its contribution is

    P_face=tau(I-n n^T).                             (15)

It has zero normal traction, two tangential eigenvalues `tau`, and trace
`2tau`. Equation (15) is the discrete surface-tension response expected from
area variation. The tensor `Q_i` from Block 10 was a normal/orientation
carrier; the metric/coframe response is its tangential complement.

At the flat background, `P_i` is symmetric. Away from it, the derivative with
respect to `F_i` is a first-Piola-type mixed tensor. Converting it to another
stress convention requires an explicit geometry/volume convention and is not
done silently here.

### Proper-cubic covariance

For a proper cubic signed permutation `R`, transform

    x_i -> x_(R^-1 i),
    F_i -> R F_(R^-1 i) R^T.

Because `cof(RFR^T)=R cof(F)R^T`, the areas permute by unsigned axis and

    S_area[Rx;RFR^T]=S_area[x;F],
    P_(Ri)[Rx]=R P_i[x] R^T.                         (16)

This is exact covariance under the current Lattice symmetry group. It is not
continuous local Lorentz symmetry or lattice diffeomorphism invariance.

## 3. Virtual Work And The On-Shell Ward Boundary

To obtain a source variation generated by a site field, restrict to the
centered displacement subfamily

    F_i[u]=I+D^0u_i,
    (D^0_a u_b)_i
      =[u_(i+e_a),b-u_(i-e_a),b]/2.                 (17)

Only displacement fields for which every resulting `F_i` remains in
`GL^+(3,R)` belong to this subfamily.

Let the nonlinear first Piola response of (8) be

    P_i,ba=partial S_area/partial F_i,ba.

For an arbitrary virtual displacement `v`, the chain rule and periodic
summation by parts give

    delta_v S_area
      =sum_(i,b,a)P_i,ba(D^0_a v_b)_i
      =-sum_(i,b)(div^0 P)_i,b v_i,b,               (18)

where

    (div^0 P)_i,b
      =sum_a[P_(i+e_a),ba-P_(i-e_a),ba]/2.

Therefore

    delta S_cut/delta u_i=-div^0 P_i.               (19)

Equation (19) is the exact local virtual-work identity promised in (3).

Three conservation statements must be separated:

1. **Global translation Ward identity.** Constant `v` has `D^0v=0`, and
   periodic telescoping gives

       sum_i div^0P_i=0.                             (20)

   This is off shell and exact.
2. **Local on-shell force balance.** If `u` is a dynamical geometry variable
   and its source-free equation is `delta S_total/delta u_i=0`, then (19)
   contributes `div^0P_i` to that equation. For the matter action alone,

       div^0P_i=0                                   (21)

   is an on-shell condition, not an identity for every cut.
3. **Forced interface.** A nonstationary binary surface has a local force

       f_i=div^0P_i=-delta S_area/delta u_i.

   Its total is still zero by (20).

The exact wrapping-slab fixture has two flat interfaces and satisfies (21) at
every site. The singleton has nonzero local `f_i` but zero total. This is the
precise point at which a geometry action or dynamics is needed. Equation (19)
is not a lattice diffeomorphism theorem, and (20) is not enough to call every
configuration locally conserved.

The centered derivative in (17) is one explicit proper-cubic choice. It has
the familiar alternating/sublattice null directions of a centered lattice
gradient. Selecting a different discrete coframe derivative changes the
source family and must be stated as a different model; no uniqueness claim is
made.

## 4. Off-Shell Higher-Form Ward Identity

The cut has a second, topological conservation law that does not require
geometry dynamics.

Let `c_i^*` be the oriented dual cube centered on primal site `i`. Define the
occupied dual three-chain

    U=sum_i x_i c_i^*.

Its oriented boundary is

    J=partial U
     =sum_(i,a) j_i,a f_i,a^*,                       (22)

up to one fixed global orientation convention for dual faces. Since the
boundary operator squares to zero,

    partial J=partial^2 U=0.                         (23)

In primal coordinates, (23) is the exact integer plaquette identity

    j_i,a+j_(i+e_a),b-j_(i+e_b),a-j_i,b=0.          (24)

This strengthens the unsigned mod-two closure in Block 10 to an oriented
integer-chain statement.

For a supplied dual two-form source `B`, the source term is `<B,J>`. Under

    B -> B+delta Lambda,

Stokes' identity gives

    <delta Lambda,J>=<Lambda,partial J>=0.           (25)

Thus the action, partition function, and all gauge-invariant responses obey
an exact off-shell higher-form Ward identity.

Under code swap, `J->-J` while `|J|` and the area action stay fixed. The
two-form source transforms as `B->-B` if code swap is to remain a covariance
of the sourced family. At `B=0`, the original code-swap symmetry is exact.

The current `J` counts oriented interface. It is not energy, momentum, mass,
or stress. Its conservation does not imply (21). This distinction prevents a
topological closed-surface theorem from being relabeled as gravitational
stress conservation.

## 5. Full Same-Family Hessian And Seagull

Let `F(s)` be any differentiable coframe path and write

    Psi(s)=log sum_x exp[-S_cut(x;s)].

Finite differentiation yields

    Psi'=-E[S'],
    Psi''=Cov(S',S')-E[S''].                         (26)

The covariance term is the connected response of the first insertion. The
second term is the local same-family contact or seagull insertion. Because
both come from (1), their relative normalization is fixed.

### Uniform-dilation algebra and exact parent-action coefficient cross-check

For `F(s)=(1+s)I`, every face area is `(1+s)^2`. Hence

    S'(0)=2tau C_X,
    S''(0)=2tau C_X.

With `tau=t/2`,

    Psi''(0)=-t E[C_X]+t^2 Var(C_X).                 (27)

As an exact coefficient cross-check against the Block-10 parent action, apply
the same common area multiplier to its degree-six `K_7`, `B_code=4` fixture.
Then

    E[C_X]=3948/4663,
    Var(C_X)=122288880/21743569.

Equation (27) therefore gives exact rational coefficients for both the
seagull and connected pieces. `K_7` is not a cubical coframe geometry and is
not used as one: this fixture checks only the finite Gibbs-response algebra.
All geometric covariance and local-force claims above are checked on periodic
cubic lattices.

### Exact offdiagonal shear fixture

Take

    F(s)=I+s e_1 e_2^T.

For a face normal to `e_1`,

    A_1(s)=sqrt(1+s^2),
    A_1'(0)=0,
    A_1''(0)=1,

while the other two face areas have zero first and second derivative on this
path. Thus a flat action can have zero offdiagonal first insertion and a
nonzero offdiagonal seagull. On the 24-rotation orbit of the `L=3` wrapping
line, `E[C_1]=4`, so this shear response is a pure exact contact term.

This closes the full first/second source derivative for the declared coframe
family. It does not prove that the family is the unique or physical metric
source of the framework.

## 6. What The Construction Retires And What It Does Not

The Block-10 residual had four walls. This construction changes their status:

| Wall | Block-11 status |
|---|---|
| existence of an off-background local geometry family | **constructed exactly** for one coframe family |
| same-family first variation and contact terms | **constructed exactly** as (14) and (26) |
| conservation identity | **split exactly** into off-shell global translation, on-shell local force balance, and off-shell higher-form surface conservation |
| physical family/action-representative selection, including its geometry-dependent additive zero | open |
| geometry dynamics or curvature action | open |
| physical action unit, field equation, coupling, and regime | open |

The result is therefore stronger than another candidate clause: there is now
a complete finite model to accept, reject, or compare. What remains is not
algebraic existence but physical selection and dynamics.

No no-go claim ships. Other coframe discretizations, metric variables,
Regge/edge actions, source conventions, improvement terms, kinetic carriers,
and continuum completions remain live.

## 7. Exact Axiom/Convention Consequence Map

Three governance levels must remain separate.

### Level A — downstream model convention, no canonical edit

A model may declare (1), (10), and the source-derivative convention locally.
Then all theorems in this note follow without changing the four canonical
axioms. The price is that the coframe family and its physical interpretation
remain model inputs.

### Level B — geometry-family and dynamics amendment

One sufficient foundation-level wording is:

> **Geometry-family and dynamics amendment.** The fixed cubic combinatorics
> admits registered local coframe sources `F`. For every finite region and
> boundary condition, Admissibility supplies one positive joint-law family
> `pi_F` and one registered local log-weight representative `S_F`, with
> `pi_F=Z_F^-1 exp(-S_F)`, whose local conditionals are restrictions of that
> same law. The source convention fixes any geometry-dependent additive shift
> of `S_F`. The family reduces to the flat Admissibility law at `F=I` and is
> covariant under lattice translations and proper cubic rotations. With one
> fixed physical action unit `s_*`, local matter stress/source is
> `partial[s_* S_F]/partial F`; the connected generating response includes
> the second variation of that same `S_F`. Physical geometry has a separately
> specified local action or update law, and any conservation statement is the
> proved Ward identity of the combined matter-plus-geometry equation.

This wording could be expressed as amendments to Lattice and Admissibility
rather than a fifth named axiom. It is sufficient to type the construction
physically once a particular `pi_F` and geometry law are selected. It is not
adopted, proved necessary, or claimed minimal.

### Level C — field-law completion

Even Level B does not select `S_geometry[F]`. To obtain a gravitational field
equation one must additionally specify or derive:

    delta[S_geometry+s_* S_cut]/delta u=0,           (28)

or a local causal update whose stationary/continuum equation has that form.
Equation (28) would balance the matter force `div^0P` against the geometry
response. Calling the left term curvature, fixing its sign and nonlinear
completion, and matching a Newton/Einstein regime are independent tasks.

The approved scale primitive converts `a` to physical units. It supplies none
of `s_*`, `B_code`, `S_geometry`, the coupling sign, or the update law.

## 8. Consequence For The TOE Lanes

| Lane | Exact Block-11 consequence | Still open |
|---|---|---|
| operational quantum / records | sourced probability responses now come from one explicit joint family rather than unrelated insertions | physical code/family selection and Record occurrence |
| causal time | geometry force balance is separated from an update law, and the surface current is conserved on each supplied slice | geometry evolution, worldvolume history, rate, and causal propagation |
| inertia / matter | the cut has a derived tangential coframe response and an oriented higher-form current | physical matter/stress identity, energy, and dressed inertia |
| gravity / source / resources | exact local coframe family and action representative, tangential first variation, seagull, global translation Ward, and on-shell local force equation | physical action-representative license and additive zero, geometry action, curvature equation, coupling, and regime |
| Born probability / realized history | every sourced finite law is normalized and locally compatible by construction | selection of this law, continuous M2 lift, and realized history |

The construction retires a mathematical existence obligation but no current-
axiom physical or autonomous obligation. Its coframe and dynamics are supplied
model content. Under the campaign's fixed rubric, the fixed TOE percentages
do not move.

## 9. Relation To Existing Sources

| Source | Exact use | Boundary preserved |
|---|---|---|
| [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | fixed cubic combinatorics, translations, proper-cubic rotations, and local probability surface | no coframe source, action unit, joint geometry family, or dynamics imported |
| [Block 10 cut/metric boundary](ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | exact cut action, endpoint shares, and the fixed-background extension residual | no physical metric derivative inherited |
| [Source-coupled local-action candidate](OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md) | convention that same-action derivatives define insertions and connected responses | open gate, not canonical authority |
| [Stress-Ward/seagull packet](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md) | boundary requiring the full same-family metric Hessian and contact terms | its Dirac carrier and spin-two interpretation are not imported |
| [Scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) | physical units only | no dimensionless law, source selection, action unit, or coupling supplied |

The physical dynamical metric/source tournament and Regge packets construct
different supplied edge/hinge carriers. They leave physical source
calibration, action selection, and the full local index-shifting Noether bridge
open. This note neither imports their target operator nor conflicts with their
bounded constructions.

The older lattice-Noether route warns that a global or two-step translation
symmetry must not be presented as a locally conserved canonical momentum
density without deriving the actual variation. Equations (18)--(21) make the
variation, divergence convention, and on-shell condition explicit.

## 10. Verification

Run:

    python3 scripts/admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_2026_08_10.py

The runner checks:

- current axiom, Block-10, source-convention, stress-seagull, and scale
  boundaries;
- signed/unsigned cut relations and exact oriented integer surface closure;
- exact locality of the supplied two-form source and code-swap covariance
  under `B -> -B`;
- identity, anisotropic, and all-24-rotation cofactor-area covariance;
- endpoint-share/edge-area equality, flat cut recovery, code swap, and every
  local flip in the exact fixture set;
- cofactor first/second variations, the full flat tangential Piola map, and
  single-face tangential eigenstructure;
- stress and force covariance under all 24 proper cubic rotations;
- exact centered summation by parts, global translation telescoping, planar
  stationarity, and singleton force;
- exact `K_7` connected/seagull coefficients and offdiagonal shear contact;
  and
- source wording, physical boundaries, trace contract, and canonical
  nonmutation.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The missing off-background object from Block 10 now exists explicitly:

    compatible cut Gibbs family
      -> coframe area derivative
      -> tangential surface stress
      -> exact virtual work and same-family seagull.

The oriented surface also carries a distinct exact off-shell higher-form Ward
identity. Local energy-momentum conservation is different: it follows only
after the coframe is physically licensed and a geometry equation places the
combined system on shell.

This advances the gravity/source lane from “no selected derivative” to “one
complete conditional derivative family with a precise dynamics boundary.” It
does not derive a physical metric, curvature law, Newton coupling, causal
update, or gravity.

No canonical axiom is edited. No no-go claim ships. No percentage moves.
