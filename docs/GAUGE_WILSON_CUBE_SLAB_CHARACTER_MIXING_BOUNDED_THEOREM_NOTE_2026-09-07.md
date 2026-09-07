---
claim_id: gauge_wilson_cube_slab_character_mixing_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
upstream_dependencies:
  - gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10
  - gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_note_2026-06-07
runner: scripts/gauge_wilson_cube_slab_character_mixing_check_2026_09_07.py
claim_scope: "For the explicitly supplied finite two-slice SU(3) cube Wilson action and constant-spectator Haar source embedding, stripping both marked spatial halfweights leaves a source operator with nonzero trivial/fundamental character mixing. Strict positivity holds for every positive spatial and temporal coupling on this finite slab; the earlier exact small-coupling results remain independent support. No framework-selected physical beta6 environment, dressed-environment, thermodynamic or continuum identification is claimed."
---

**Type:** bounded_theorem
**Status:** proposed_retained

# Actual Wilson cube-slab character mixing

The exact two-slice source compression in this note has **strictly positive trivial/fundamental character mixing for every s,t>0**, including the mathematical isotropic value s=t=6 on this finite model. A spatial-reflection quadratic form proves this all-coupling statement. Earlier independent small-coupling calculations remain below as support: the isotropic expansion begins with b^5/(12^5·81). The supplied constant-spectator Haar source embedding and open slab are part of the theorem; no framework-selected physical beta6 environment is identified.

## Status and dependencies

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
bodyType: bounded_theorem
conditional_surface_status: conditional-support
trace_class: upstream_support
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review the exact reflection identity and strict averaged half-amplitude for the actual bare-Haar slab."
audit_required_before_effective_retained: true
bare_retained_allowed: false
admitted_observation_status: null
hypothetical_axiom_status: null
```

Independent audit owns status authority. This note does not assign an effective verdict.

- [Temporal-gauge mixed Wilson kernel](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md) supplies the linkwise temporal-kernel convention for a supplied Wilson action.
- [Wilson coefficient positivity](GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE_NOTE_2026-06-07.md) supplies the representation-ring positivity and Schur contraction convention. Here c_lambda is the coefficient in w=Σc_lambdaχ_lambda, not the dimension-divided coefficient.
- [Distinct-shell exact geometry](GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_EXACT_CORE_NARROW_THEOREM_NOTE_2026-05-29.md) already records the five-face cube cap. Its geometry is not claimed as new here.
- [Supplied-diagonal source factorization](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md) and [conditional residual packaging](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md) delimit the older supplied-D algebra. This note calculates an actual operator instead of supplying a diagonal input.

Primary exact support runner: [gauge_wilson_cube_slab_character_mixing_check_2026_09_07.py](../scripts/gauge_wilson_cube_slab_character_mixing_check_2026_09_07.py). It checks 973017 signed subsets and four rational controls; necessary center-flux selection is not counted as an actual Haar integration proof. The proof below supplies that contraction. Independent helper: [native_gauge_transfer_spatial_wilson_cube_slab_f3_check_2026_09_07.py](../scripts/native_gauge_transfer_spatial_wilson_cube_slab_f3_check_2026_09_07.py). Its separately constructed full affine F3 system has rank17 and nullity5, enumerates all243 solutions, and confirms unique minimum support5 with next support9. Its fifteen named checks and5832 component congruences are supporting exact arithmetic, not a substitute for the Haar proof.


Spatial Wilson action and anisotropy are explicit inputs. The isotropic supplement below is a separate calculation on the same defined operator.

## Exact finite model

Take the twelve positively oriented edges of one spatial cube with vertices in{0,1}³, at two open temporal slices. The marked face is xy at z=0. Write s,t>0, a=s/2 and w_b(G)=exp[b ReTr(G)/3]. Each spatial face has halfweight w_a at each time, and each of the twelve temporal plaquettes has weight w_t. Temporal gauge sets the eight vertical time links to identity. The link Hilbert space is L²(SU(3)^12) with normalized product Haar; If=f(Wbottom) is an isometry from central class-function L². The environment multiplier Menv contains the other five spatial halfweights; M0 contains the marked one. C_t has kernel product_e w_t(V_e U_e^-1). Define D03=<χ0,D_(s,t)χ3>, where χ3 is the fundamental character, not its normalized trace.

## Full class-function stripping identity

Define S_s on the full central class-function L² space as multiplication by w_(s/2)(W). Let M0 be the corresponding marked-face multiplier on the full link Hilbert space. For the exact Haar isometry If=f(Wbottom), M0 I=I S_s and I* M0=S_s I*. Both S_s and S_s^-1 are bounded because the group is compact and the weight is strictly positive. Therefore, with the actual full transfer T=M0 Menv C_t Menv M0,

I* T I=S_s D_(s,t) S_s,

D_(s,t)=S_s^-1 I* T I S_s^-1=I* Menv C_t Menv I.

This identity uses full multiplication before any character-window compression. It is not an identity obtained by replacing S_s with the exponential of a finite compressed recurrence J_N. A finite-window matrix element is taken only after the displayed full-space stripping; inversion and compression are not interchanged.

Independent graph support: [gauge_wilson_cube_slab_reflection_geometry_check_2026_09_07.py](../scripts/gauge_wilson_cube_slab_reflection_geometry_check_2026_09_07.py) reconstructs the actual32links,24faces,22remaining faces, matching-forest cuts, reduced source words and the10crosscouplings. Its47 geometry/action checks include every reflected cross-pair endpoint and orientation and the complete coupled-pair set excluding exactly the two omitted source pairs. They do not numerically prove positivity. Strict positivity follows from the analytic Haar and Peter–Weyl argument below. The older973017-subset and243-affine-solution runners remain specifically perturbative certificates.

## All-positive-coupling proof: gauge restoration and change of reflection plane

Restore one temporal link at each of the8spatial vertices. The resulting full open four-dimensional hypercube has16vertices and32links. Its24plaquette faces are weighted except the2marked xy faces at z=0, at the input and output times. Spatial faces carry a and temporal faces carry t. Sourceχ3 is the input marked loop; its action weight remains absent.

Integrate every link against normalized Haar. Gauge-transform the upper-time vertices, leaving lower-time vertices fixed, to set the8temporal links to identity. These links form a matching forest, so there is no periodic holonomy constraint. The remaining spatial variables change by left/right Haar translations with unit Jacobian, and every face weight and the source trace is gauge invariant. The8temporal Haar integrations contribute1. The integral is exactly the original temporal-gauge D03, not a new measure or transfer model.

Instead fix the8links parallel to spatial x to identity, by gauge-transforming the x=1vertices with x=0vertices fixed. These links are another matching forest. The same normalized-Haar argument is exact. Remaining variables form two identical12link halfcubes in(y,z,time), one at each x. Each half has six internal face factors: two yz spatial faces with a and four temporal faces with t. Let their common real positive product be M(H).

Every crossface with axes(x,j) reduces to H_j,right H_j,left^-1, up to inversion/conjugation which does not change w. There are12potential matching halfedges. The two missing source face weights remove exactly the crosscouplings on the yedges at z=0 at the two times. Of the10remaining crosscouplings, six carry a and four carry t. Thus their kernel is a tensor product of10actual central Wilson convolutions. There is no added coupling on an omitted face.

## Exact reflection quadratic form

Let U be the omitted yedge at input time and V the omitted yedge at output time within either halfcube. The source trace after x gaugefix is

Tr(U_right U_left^-1)=Σ_(i,j) (U_right)_(i,j) conjugate((U_left)_(i,j)).

The two half-actions are identical, since x reflection does not exchange space and time. Define F_ij(H)=M(H) U_ij. Let P integrate U and V against independent normalized Haar, leaving a function of the10coupled halfedges. Fubini's theorem (all functions continuous on compact groups) gives exactly

D03=Σ_(i,j) <P F_ij, C_cross P F_ij>,

where C_cross is the tensor product of six C_(w_a) and four C_(w_t). Depending on the initial source-loop orientation the displayed scalar is conjugated; the real positive quadratic form proves the same value. No factor1/3 appears in the character source: it is an unnormalized trace.

Each Wilson convolution has strictly positive Peter–Weyl eigenvalues c_lambda(b)/d_lambda for b>0. Strict coefficient positivity follows from the actual representation-ring expansion: every SU3 irrep occurs in a tensor product of fundamental and antifundamental representations, whose exponential coefficients are positive. Thus C_cross is a bounded positive injective operator. It need not have a positive uniform spectral lower bound. Nevertheless <f,C_cross f>>0 for every nonzero L² function f, by its full orthogonal Peter–Weyl expansion.

## Nonzero projected half-function

It remains essential to prove PF is nonzero; reflection positivity alone would only give nonnegativity. Set the10coupled halfedges to identity. Of the six half-faces, the two spatial ones reduce to w_a(U),w_a(V), one temporal face reduces to w_t(UV^-1), and the other three temporal faces give e^(3t). Hence

(PF_ij)(identity)=e^(3t)∫∫ U_ij w_a(U)w_a(V)w_t(UV^-1)dU dV.

The matrix integral is scalar by simultaneous conjugation. Let

I(a,t)=∫ χ3(U)w_a(U)(w_a*w_t)(U)dU.

Then (PF_ij)(identity)=δ_ij e^(3t) I(a,t)/3. Central convolution gives

(w_a*w_t)(U)=Σλ [c_lambda(a)c_lambda(t)/d_lambda]χ_lambda(U).

All coefficients are nonnegative. Expand the other w_a and use the nonnegative integer multiplicities in character products. The trivial convolution term and the antifundamental coefficient of w_a alone give

I(a,t)≥c0(a)c0(t)cbar3(a)>0.

Absolute uniform convergence is justified by Σλ d_lambda c_lambda(b)=e^b and standard character bounds; alternatively expand finite positive representation sums and pass to the uniform Wilson limit. Thus at least the diagonal PF_ii is nonzero at identity. PF_ii is continuous, so it remains nonzero on an open set of positive product Haar measure. It is genuinely nonzero in L², not merely at a measure-zero configuration.

Combining this with the strictly positive quadratic form proves D03>0 for ALL s,t>0.

## Normalization, controls and limits

Dividing the temporal kernel by c0(t)^12, or dividing the complete finite integral by any positive partition scalar, preserves strict nonzero mixing. The proof supplies no useful uniform numerical lower bound at6; injectivity is not a coercivity estimate. An algebraic finite-character residual obtained by left multiplying by a positive invertible diagonal also retains this off-diagonal entry.

The matching-forest gauges rely on open two-slice geometry. Periodic temporal boundary conditions would introduce a holonomy constraint and are not included. The five-face cap geometry is inherited from the previous construction; the new ingredient is reflection across spatial x and the strict projected-amplitude argument. The source map remains f↦f(Wbottom) with constant spectators, and no generic source embedding or physical infinite-volume environment is substituted.

At t=0 or s=0 the strict coefficient argument changes; the already proved t=0 positive-s result and untouched-edge vanishing families are separate controls. No claim of all-parameter positivity is made outside s,t>0. The existing small-coupling isotropic series remains an independent check, not an input to this proof.

## Earlier small-coupling construction and independent controls

The following calculations were frozen before the reflection extension. They retain their original scope and provide independent checks of the same operator.

## Actual operator and source map

Let E be the twelve edges of one cube and H=L²(SU(3)^E,dU). Let W0 be its bottom loop. I:L²central(SU3)→H sends f to f(W0). Product Haar makes I isometric. This image is gauge invariant; all Wilson factors and temporal convolution commute with local gauge transformations, so restricting to the gauge-invariant Hilbert space makes no change to the matrix elements below.

Write J(G)=(χ3+χbar3)/6=ReTr(G)/3, w_b=e^(bJ). Let C_t have kernel ∏_(e∈E) w_t(V_e U_e^-1). Let M0 be multiplication by w_(s/2)(W0), and Menv by the product of the other five face halfweights. The true two-slice transfer is M0 Menv C_t Menv M0. Since M0 I=I m0, its source compression is m0 D_(s,t) m0, where

D_(s,t)=I* Menv C_t Menv I.

Thus multiplication by m0^-1 strips the marked faces EXACTLY on the full source class space. No finite-section exponential or prescribed D enters. C_t is positive semidefinite by the nonnegative Wilson character expansion, and D is positive self-adjoint. Positivity does not imply character diagonality.

## Five-face disk Haar integration

Fix the bottom boundary holonomy W. Conditional integration over the other eight links gives g_s(W)=I* Menv 1. The five environment faces form a disk with boundary the marked loop. Gauge-fix a tree consisting of three bottom edges and four vertical edges. Seven normalized Haar gauge integrations give one; the remaining four top edges are independent Haar variables, while the fourth bottom edge is W (or its inverse). The five face words now form the usual disk gluing integral.

The exact elementary identity, from matrix-index Schur orthogonality, is

∫ χλ(A X) χμ(X^-1 B) dX = δλμ χλ(AB)/dλ.

Successive gluing of five disk faces gives four factors1/dλ. Equivalently, after the above tree gauge, integrate the four free top links successively. Orientation reversals are harmless since w_b(G^-1)=w_b(G). If w_(s/2)=Σλ cλ(s/2)χλ, then

g_s(W)=Σλ cλ(s/2)^5/dλ^4 χλ(W).

All steps can first be made for finite character polynomials and then passed to the Wilson exponential: its representation-ring expansion has nonnegative coefficients and Σλ dλ cλ=e^(s/2), ensuring absolute uniform convergence and permitting the Haar integrations. This is actual disk integration, not a definition of a coefficient vector.

The cube geometry itself is old: docs/GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_EXACT_CORE_NARROW_THEOREM_NOTE_2026-05-29.md proves the distinct five-face cap. It does not prove this two-slice off-diagonal. The old tensor-transfer Perron source lines12–13,73–74,450–451 explicitly leave static-to-two-slice operator identification open. Here the static marginal is used only through the exactly rank-one temporal kernel at t=0.

## Exact off-diagonal at zero temporal coupling

C_0=|1><1| on the full link space. Consequently D_(s,0)=|g_s><g_s|, and conjugation symmetry gives

<χ0,D_(s,0)χ3>=c0(s/2)^5 c3(s/2)^5/81.

For s>0 this is strictly positive. More explicitly, positivity of representation-ring coefficients in exp[(s/12)(χ3+χbar3)] gives c0≥1 and c3≥s/12, so

<χ0,D_(s,0)χ3>≥s^5/(12^5·81).

This is not a claim about an inverse local convolution at t=0, where nontrivial local eigenvalues vanish.

## Explicit strictly positive temporal coupling

Because |J|≤1, the product temporal kernel satisfies pointwise

|∏_(12edges)w_t(V_eU_e^-1)−1|≤e^(12t)−1.

The ten environment halfweights in the two-slice integrand have product at most e^(5s); |χ3|≤3. Product Haar has mass1. Therefore

|<χ0,[D_(s,t)−D_(s,0)]χ3>|≤3e^(5s)(e^(12t)−1).

This is a direct integral estimate, not a numerical continuity inference. As a derived explicit member of the preregistered positive-t interval, choose s=1 and t=10^-12. Since e5<149 and e^x−1≤2x for0≤x≤1/2,

|difference|<10728/10^12 < 1/(12^5·81)=1/20155392.

Thus this actual finite Wilson slab has a strictly nonzero character off-diagonal at strictly positive spatial AND temporal couplings. The extreme anisotropy is disclosed; it proves existence and does not approximate a physical beta6 or isotropic slab. The rational choice is made after deriving the analytic bound, not presented as the original preregistered numeric fixture.

For t>0 the normalized one-link convolution eigenvalues aλ(t)=cλ(t)/(dλ c0(t)) are strictly positive. If one further defines the historical algebraic residual R=(Dloc)^-1D with Dloc=diag(aλ^4), its 0,3 entry remains nonzero (a0=1). Multiplying by any positive normalization scalar likewise cannot restore diagonality. This is a statement on finite character matrix elements; no bounded all-weight inverse is asserted.

## Controls and boundaries

With Menv=I, direct linkwise Schur integration gives diagonal compression c0(t)^8 [cλ(t)/dλ]^4, or aλ(t)^4 after dividing by c0(t)^12. This derives the four-link packet for the explicitly constant spectator embedding in the no-spatial-environment model. It does not derive the same form after five spatial faces are inserted.

If a source edge is absent from every remaining spatial factor at both slices, its Peter–Weyl isotypic projectors commute with Menv and C_t. Iχλ belongs to the λ (or dual, depending orientation) sector on that edge. Orthogonality then forces off-diagonal source entries to vanish for different labels. This explains why a two-plaquette toy is an inadequate falsifier. The five-face cap avoids that condition on every source edge.

The new result rejects universal diagonality for this explicit actual Wilson/Haar source compression. It does not claim that every physically chosen environment embedding, boundary state, geometry or parameter is non-diagonal. In particular an environment-dressed embedding is a different map and would need its own definition and proof.

## Isotropic result: exact fifth-order mixing

The preregistered exact center-flux enumeration tested973017 signed subsets of the22actual action faces through size5. There are no successful subsets at sizes0,1,2,3,4 and exactly one at size5: the five spatial cap faces on the INPUT slice, with their consistent oriented signs. Runtime0.267seconds,28.985MiB. Raw graph,24link incidence vectors, all counts and the unique signed solution are retained in isotropic_center_selection.json. This is necessary center selection, not a claim that any flux-balanced graph automatically has nonzero Haar integral.

Why repeated factors are covered: a degree n monomial of the Wilson exponential is a product of n fundamental or antifundamental plaquette traces. For each face reduce its signed count modulo3 to0,±1. The number of nonzero residues is at most n. Independent center multiplication of each of the24Haar links forces the resulting signed face incidence to cancel the input source loop modulo3. Therefore no degree below5 survives. At degree5 every surviving residue support must have size5, forcing exactly one trace factor on each of those five faces. There are no repeated insertions, neutral pairs, triple insertions or temporal insertions at that degree.

The unique cap is evaluated by actual Schur disk gluing, rather than by its center condition. Its four1/3gluing factors give1/81. Every spatial halfweight contributes b/12. The other slice contributes its constant term. Hence, with s=t=b in the exact frozen source operator,

<χ0,D_(b,b)χ3> = b^5/(12^5·81) + O(b^6).

The finite compact-group integral is entire in b, so this strictly positive leading coefficient proves nonzero mixing for all sufficiently small positive ISOTROPIC b. This result is distinct from the previously frozen anisotropic proof and does not establish anything at beta6.

An optional explicit derived positive point requires no fitted remainder. Write the two-slice integrand as χ3(Winput)exp[b A(U,V)]. There are ten spatial halfweights and twelve temporal weights, so |A|≤5+12=17 and |χ3|≤3. Its degree≥6 Taylor remainder is bounded by

3 e^(17b)(17b)^6/6!.

At b=10^-14, e^(17b)<2, so remainder≤17^6 b^6/120. This is strictly smaller than b^5/(12^5·81), as verified by an exact rational comparison. Thus a fully positive isotropic parameter exists explicitly, with the extreme small value disclosed. The parameter is a derived corollary, not part of the original pre-computation fixture.

This refutes character diagonality for the specified actual cube-slab Wilson/Haar compression and source map even at isotropic coupling. It does not identify a dressed-environment source map or claim the historical multi-link physical target has supplied this exact map. The graph geometry was already known in the distinct-shell exact-core note; the new ingredient is the actual two-slice off-diagonal, including the24link SU3 center rule and its coefficient.

## Normalization and applicability

All displayed absolute Taylor and perturbation bounds apply to D as defined, with UNNORMALIZED temporal Wilson product. Dividing C_t by c0(t)^12 normalizes its trivial product-link channel. This is a positive scalar, so it preserves the off-diagonal sign. On the isotropic line c0(b)=1+O(b²), hence the normalized operator retains the same fifth-order coefficient, but the displayed absolute remainder bound is not asserted unchanged after division. A further positive finite partition-function normalization also preserves nonzero mixing; its numerical leading coefficient must be adjusted if its value at zero is not one.

The source map is exactly f↦f(W_bottom) with constant spectators. A source map dressed by an environment state is different and not analyzed. The result therefore rejects unconditional character-diagonality of the declared actual compression, including at small isotropic coupling; it does not close all historical physical environment targets or identify a physical beta6 observable. No Wilson-action selection from framework axioms, TOE closure, infinite-volume result or continuum mass gap is asserted.

The native coefficient packet uses c_lambda/c0, whereas a normalized one-link Wilson convolution uses c_lambda/(d_lambda c0). Neither replacing one coefficient sequence by the other nor applying abstract Schur uniqueness would remove the actual off-diagonal found here. The untouched-edge criterion explains a genuinely vanishing family; low-order zeros alone are never promoted to diagonality.


The [campaign provenance and N1–N8 discipline](../.claude/science/physics-loops/spatial-wilson-mixing-20260907/NO_GO_DISCIPLINE_CHECKLIST.md) preserve the supplied physical-model imports and heavy negative-packet NOT PASS.
