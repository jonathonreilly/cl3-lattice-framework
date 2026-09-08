---
claim_id: admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the supplied Block-12 four-coframe/Kuhn-Regge construction, a signed range-one isolated-defect selector multiplies a centered line-minus-bag geometry improvement that vanishes identically at flat geometry for every binary neighborhood. On an isolated static occupied unit tube it replaces the complete affine-bag edge source by one actual axial tick-edge source s_line=2 tau e_tau-edge, with the coefficient fixed uniquely by the already-derived homogeneous T_tau_tau=tau normalization. At k_tau=0 this actual edge source annihilates the four exact vertex-gauge columns analytically and maps exactly to pure T_tau_tau=tau. Direct eigenspace and pseudoinverse checks find full five-null-mode compatibility and unprojected edge-equation solvability on every one of 1,281 nonzero static modes of the periodic spatial tori L=3 through L=8. The actual unprojected Regge metric response obeys |k|^2 h_tau_tau -> 2 tau in four spatial directions and retains the open-boundary 1/r Green shape. The improvement is zero on the wrapping-plane fixture and changes the bag metric source only at O(k^2). A nonzero total tick charge remains incompatible with the bare periodic k=0 Hessian, and a fixed vertical line with k_tau nonzero is not gauge compatible. No physical action representative, mass identity, coupling, sign, infrared ensemble, dynamic history, nonlinear completion, axiom necessity, adoption, or universal static-momentum theorem is proved."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py
---

# Centered Tick-Edge Defect Improvement And Exact Static Regge Source Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** exact static-source improvement and axiom-consequence map
**Scope:** the supplied Block-12 binary tick history, local four-coframe/Kuhn
volume family, and the supplied flat cubic-Coxeter Regge Hessian. The exhaustive
full-null statement is restricted to the named finite tori and modes.
**Audit-status authority:** independent audit lane only. This source authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py](../scripts/admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py)

## Result Up Front

Block 12 constructed an affine-pressure unit bag with exact homogeneous metric
source

    T_bag(0)=tau e_tau e_tau^T,

and found the actual Regge `1/k^2` lapse pole after a disclosed metric source
projection. Its localized unprojected source retained an `O(k^3)` gauge
remainder and an `O(k^2)` overlap with the extra quadratic Regge zero branch.
This block gives an explicit local improvement that removes both residuals on
the static isolated-defect sector without projecting the source.

For one spatial cell `i`, let `B_i(E)` be the centered Block-12 geometric bag
deviation: the six timelike Kuhn-hyperface volumes, minus four times the Kuhn
four-volume, with every unit flat value subtracted. In the normalization used
below,

    B_i(E)
      =tau sum_(a=1)^3([V_i,a^-(E)-1]+[V_i,a^+(E)-1])
       -4tau[V_i^(4)(E)-1].                          (1)

Let `ell_i,tau(E)` be the actual axial tick-edge length at the same local
anchor, and define the centered tick line

    L_i(E)=2tau[ell_i,tau(E)-1].                     (2)

Both (1) and (2) vanish at the flat unit geometry. For the six spatial
neighbors `j~i`, define the signed range-one isolated-defect selector

    d_i
      =x_i product_(j~i)(1-x_j)
       -(1-x_i) product_(j~i)x_j.                    (3)

Thus `d_i=+1` only for an isolated occupied cell, `d_i=-1` only for an
isolated hole, and `d_i=0` on the other 126 binary radius-one neighborhoods.
Code complement reverses its sign. The local improvement is

    I_i=d_i(L_i-B_i),

or, in the exact runner-facing notation,

    I_iso=d_iso(L-B).                                (4)

At flat geometry, (4) is zero for every binary configuration. It therefore
does not change the Block-12 flat conditional law, its action zero, or any
flat-geometry probability. It changes only the declared off-background action
representative. On an isolated occupied unit tube, the bag plus (4) is exactly
the line:

    B_i+I_i=L_i.                                    (5)

The isolated-hole value is retained as a selector/complement control; its full
Block-12 source is not classified here. On a wrapping plane, every occupied
site has occupied in-plane neighbors and no site or hole is isolated; hence
`d_i=0` everywhere and the Block-12 plane source is untouched.

The coefficient two in (2) is not fitted to Newton's law. The actual
line-averaged edge-to-metric map has

    partial ell_tau / partial h_tau_tau = 1/2        (6)

at flat geometry. The Block-12 bag already derived
`T_tau_tau(0)=tau`. Preserving that internally derived normalization requires
and uniquely fixes

    2tau(1/2)=tau.                                  (7)

At a static Fourier momentum `k=(k_x,k_y,k_z,0)`, the complete improved
isolated source is the actual edge row

    s_line(k)=2tau e_tau-edge.                       (8)

For the axial tick edge, the vertex-displacement gauge factor is

    [exp(i k_tau)-1]e_tau.                           (9)

Equation (9) vanishes identically at `k_tau=0`, so (8) annihilates all four
exact discrete gauge columns analytically. The same actual metric map gives

    s_line(k) M(k)=tau e_tau e_tau^T                 (10)

with zero spatial stress and zero shift for every static momentum. This is an
edge-source statement, not a continuum tensor inserted by hand.

The fifth, non-metric quadratic Regge zero branch is not removed by an analytic
assumption. The runner diagonalizes the actual `15 x 15` Bloch Hessian at every
nonzero spatial Fourier mode on each torus `L=3,4,5,6,7,8`. There are

    26+63+124+215+342+511=1,281                     (11)

such modes. Every Hessian has exactly five zero modes. Across the complete
inventory the maximum overlap of (8) with the full five-dimensional null space
is below `2e-13`, and the maximum residual of the unprojected actual edge solve
is below `5e-12`. No extra-null source projection is applied.

The long-wave metric response is likewise computed without a source
projection. With `H_h=M^dagger Q_R M`, solve

    H_h(k)h(k)+[s_line(k)M(k)]^*=0.                  (12)

Across axial, face-diagonal, generic mixed, and body-diagonal spatial
directions, the runner obtains

    |k|^2 h_tau_tau -> 2tau.                         (13)

The line-minus-bag correction changes the metric source only at `O(k^2)`, so
it preserves the residue already located in Block 12 while making the tested
edge source compatible before the solve. The inverse kernel remains

    Fourier^-1[1/|k|^2](r)=1/(4 pi r),              (14)

on the open or infinite static boundary. Equation (14) is a radial shape, not
a physical calibration or sign choice.

Two boundaries remain explicit. First, at `k=0` the actual Hessian has eleven
zero modes and a nonzero total tick charge lies outside its range. Therefore
the bare periodic k=0 equation has no solution. Second, if `k_tau` is nonzero,
the gauge factor (9) is nonzero: a fixed vertical edge is not a conserved
dynamic worldline. Open boundaries, fixed global lapse/strain, compensating
background charge, a curved or balanced torus, a combined geometry constraint,
and dynamic histories remain open.

This is an explicit action representative, not a selected physical mass. No
canonical axiom is edited, and the fixed TOE percentages do not move. No
universal no-go is claimed.

## Machine Status And Trace

~~~yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The radius-one selector and flat-law preservation are exact over all 128 neighborhoods; the line normalization, pure tick metric source, and static gauge identity are analytic; the complete Regge null-space and unprojected edge solve are exhaustive only on the named 1,281 finite-torus modes; the pole and Green tail are controlled long-wave checks. Physical and dynamic conclusions are withheld."
trace_class: upstream_support
target_claim_id: admissibility_exact_localized_physical_regge_source_and_dynamics_bridge
target_blocker_text: "physically select and license the improved joint history/action representative, identify its tick charge with mass/Record content, supply a conserved dynamic history and geometry equation, choose coupling orientation/sign and the infrared zero-mode ensemble, and establish nonlinear and realized-history completion"
source_of_blocker_text: derived_here
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "test whether a closed dynamic defect worldline supplies the required spatial edge segments and exact four-dimensional Ward identity, then couple that history to a declared open or balanced infrared ensemble without inserting an Einstein target"
conditional_surface_status: "one flat-law-preserving local defect improvement converts the isolated static affine bag to an actual axial tick-edge source with exact static gauge compatibility, exhaustive named-torus full-null compatibility, unprojected Regge lapse pole, and open-boundary radial tail"
hypothetical_axiom_status: "the existing Geometry-indexed history/action amendment is already sufficient to register this improvement; no broader candidate wording is needed, but the representative, mass typing, geometry update, coupling/sign, ensemble, and realized history remain unadopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## Exact Target Contract

| Contract field | Block-13 value |
|---|---|
| target statement | construct a local flat-law-preserving source improvement that removes Block 12's localized static gauge and extra-null residuals on the actual Regge carrier while preserving the derived tick source and `1/k^2` pole |
| quantifiers/domain | all 128 binary radius-one spatial neighborhoods for selector algebra; one isolated static occupied tube and its complement; every nonzero static Fourier mode on periodic spatial tori `L=3` through `L=8`; four named small-momentum directions for the pole |
| allowed premises | the Block-12 bag and its internally derived homogeneous source, the approved equal-form tick graining, elementary local Boolean algebra, and the supplied actual axial edge, metric map, and Regge Hessian |
| forbidden weakenings | projecting the edge source, fitting its coefficient to Newton's law, deleting `k=0` silently, importing a conserved continuum stress tensor, treating a finite-mode numerical inventory as an all-momentum symbolic theorem, or treating action selection as current-axiom content |
| required edge cases | all 128 neighborhoods, code complement, isolated occupied cell, isolated hole, wrapping plane, generic bag residual control, two separated sources, all named torus modes, four pole directions, `k=0`, and `k_tau!=0` |
| completion witness | explicit (4), exact (5)--(10), exhaustive five-null-mode and edge-solve certificate on (11), unprojected (12)--(13), and separated compact/dynamic controls |
| outcomes not counting as closure | metric-transverse projection alone, a continuum dust tensor inserted by hand, a single sampled momentum, a periodic solve with implicit neutralization, or candidate axiom wording without physical selection |

## 1. Local Action Construction

### 1.1 The inherited centered bag

Block 12 used the complete Kuhn covers of each unit hyperface and four-cell.
At flat geometry all diagonal-edge volume derivatives cancel, and only actual
axial edge classes remain. For an isolated static occupied tube, its six
spatial-normal hyperfaces and centered pressure `p=4tau` give (1). The
homogeneous metric derivative is pure tick:

    delta_g B_i|_(k=0)=tau delta h_tau_tau.          (15)

At nonzero generic static momentum its centered finite stencil has the
correct leading metric source but retains the two residuals measured in Block
12. No claim in this block rewrites those measurements.

### 1.2 Radius-one defect selector

Equation (3) depends on the center and its six nearest spatial neighbors. Its
classification follows directly:

- `x_i=1` and all neighbors zero gives `d_i=+1`;
- `x_i=0` and all neighbors one gives `d_i=-1`;
- every other one of the 128 assignments gives `d_i=0`.

Under `x -> 1-x`, the two terms exchange and `d_i -> -d_i`. Proper cubic
rotations merely permute the six neighbor factors. Thus the selector is
range-one, complement odd, and proper-cubic scalar.

### 1.3 Flat-law preservation

Both bracketed geometric deviations in (1)--(2) are exactly zero at the flat
unit geometry. Hence

    I_i[x;I]=0                                      (16)

for all local bit assignments, including those on which `d_i` is nonzero.
Equation (16) is stronger than equality after normalization: the unnormalized
flat action representative is unchanged configuration by configuration.

The improvement is nevertheless visible under geometry variation. This is
precisely why the candidate action amendment must register geometry-dependent
improvements rather than only the normalized flat law.

### 1.4 Sector action

On the isolated occupied sector, (5) is an identity of local geometry
functionals, not just their leading metric derivatives. On a static wrapping
plane the selector vanishes at every site, so the exact Block-12 plane action
and its null compatibility remain untouched. For separated isolated defects,
the linearized source is a sum of translated copies of (8); at fixed static
momentum translation supplies only scalar phases. Gauge and full-null
compatibility therefore compose linearly on the tested carrier.

This note does not claim that (4) is unique among local improvements, nor that
the current axioms select the isolated-defect sector as matter.

## 2. Exact Static Source Identities

The supplied Regge complex has one axial tick edge per cell with direction
vector `v=e_tau`. Its gauge and metric rows are, directly from the source-bound
maps,

    G_tau,nu(k)=[exp(i k_tau)-1]delta_tau,nu,        (17)

    M_tau,h_tau_tau(k)
      =exp(i k_tau/2)sinc(k_tau/2)/2,               (18)

with every other entry of this metric row zero. At `k_tau=0`, equations
(17)--(18) prove (9)--(10) exactly.

There is no spatial-momentum approximation in these two identities. Their
scope boundary concerns the extra non-metric zero branch: its orthogonality to
the tick-edge row is checked over the finite inventory rather than proved as a
symbolic identity for every point of the continuous Brillouin zone.

For two isolated sources at positions `a` and `b`,

    s_2(k)=2tau[exp(i k.a)+exp(i k.b)]e_tau-edge.    (19)

Thus any finite static collection inherits (17), and it inherits the tested
extra-null orthogonality mode by mode. Equation (19) does not solve the compact
zero mode when the total signed charge is nonzero.

## 3. Full-Null And Edge-Solve Inventory

For each named Fourier mode, the runner forms the actual Hermitian Regge Bloch
Hessian `Q_R(k)`, diagonalizes it, and defines the numerical null space by
`|lambda|<1e-8`. It then checks

    ||N(k)^dagger s_line(k)^*||,                    (20)

and solves the unprojected edge equation

    Q_R(k)delta ell(k)+s_line(k)^*=0                (21)

with the Moore-Penrose pseudoinverse. A solve counts only if the direct
residual of (21), not the pseudoinverse return code, is small.

The inventory contains every nonzero triple in the standard Fourier index
range for each `L=3,...,8`, giving (11). Every one of the 1,281 Hessians has
exactly five numerical zero modes: the four vertex-gauge modes and the one
extra quadratic branch described by the supplied Regge theorem. The cached
runner reports the worst gauge overlap, full-null overlap, and direct solve
residual.

This is exhaustive over the named finite fixtures. It is not an analytic
classification for arbitrary lattice size or arbitrary continuous momentum.

## 4. Unprojected Pole And Open-Boundary Tail

Because (10) is already transverse to the static continuum metric gauge
columns, the metric solve in (12) needs no projector. At `epsilon=0.025`, the
four checked directional coefficients are approximately

| direction | `|k|^2 h_tau_tau/tau` |
|---|---:|
| axial | `2.0001042` |
| face diagonal | `2.0000347` |
| generic `(1,0.7,0.4)` | `2.0000149` |
| body diagonal | `1.9999884` |

For every direction, halving `epsilon` from `0.05` reduces the error from two.
These values establish the controlled long-wave response of the supplied
quadratic carrier, not an exact equality at finite momentum.

The regulated radial kernel used for (14) is

    G_epsilon(r)
      =atan(r/epsilon)/(2 pi^2 r)
      ->1/(4 pi r).                                 (22)

No Newton constant, attractive sign, Lorentzian potential, nonlinear
completion, or empirical calibration follows from (13)--(22).

## 5. Controls And Exact Boundaries

### 5.1 The old bag is an active residual control

At the normalized generic static momentum along `(1,0.7,0.4)`, the runner
first recomputes the Block-12 bag's nonzero gauge and extra-null overlaps. It
then adds the explicit line-minus-bag row and verifies that the result is (8)
to machine precision. This distinguishes cancellation by a local action
stencil from a hidden source projection.

The metric source of the counter-improvement scales as `O(k^2)` under
momentum halving. Consequently the constant monopole source in (10) is
preserved.

### 5.2 Compact zero mode

At `k=0`, `Q_R(0)` has eleven zero modes. The source (8) has nonzero overlap
with that null space, and the direct pseudoinverse residual is nonzero. The
narrow conclusion is only

    no solution for nonzero total tick charge
    in the bare unmodified periodic quadratic equation.               (23)

Open or fixed-boundary problems, fixed global lapse, a compensating source,
background subtraction, and a different on-shell geometry remain outside
(23). The phrase “bare periodic k=0 equation” always means this exact scope.

### 5.3 Dynamic Fourier control

For `k_tau!=0`, equation (17) is nonzero. The runner's mixed momentum control
also has nonzero overlap with the fifth branch. A physical worldline can add
spatial segments, vertices, endpoint forces, or a joint geometry equation;
none is present in the fixed vertical-line fixture. The theorem is static.

## 6. Exact Axiom And Convention Consequence Map

The construction itself needs no canonical edit when declared as downstream
model content. The result changes which scientific obligation is open, not
the authority of the current axioms.

### Level A — downstream convention, no axiom edit

A model may declare:

1. the Block-12 finite tick history and actual Kuhn-Regge carrier;
2. the improved local action `S_13=S_12+sum_i I_i`;
3. the isolated-defect interpretation and tick-edge source unit;
4. an open, fixed-lapse, neutralized, or background-balanced ensemble; and
5. the geometry-action orientation, coupling, and readout.

All positive and negative mathematical statements above then follow without
changing Lattice, Qubit, Admissibility, or Record. The physical declarations
remain model inputs.

### Level B — candidate foundation amendment

The candidate wording from Block 12 remains sufficient and is intentionally
not broadened:

> **Geometry-indexed history/action amendment.** For every finite causal
> history region and declared boundary condition, the framework supplies one
> joint history law on the spatial lattice and its registered tick extension.
> Record permanence is enforced on that history. The law belongs to one
> registered local geometry-indexed family with a fixed unnormalized local
> action representative `S[history;geometry]`; the representative fixes every
> geometry-dependent state term and improvement, including terms that vanish
> at the flat source, and fixes one physical action unit. Its flat spatial
> restriction is the Admissibility law, and the family is covariant under
> spatial translations and proper cubic rotations. Local lapse, shift, and
> spatial matter sources are the first variations of that same spacetime
> action. The Lattice structure also registers one local geometry carrier and
> the map between its coframe, metric, and edge variables. Geometry has one
> specified local action or causal update, including its orientation and
> matter coupling. Conservation is the Ward identity of the combined
> matter-history-plus-geometry equations. Each model declares its open,
> boundary-fixed, background-subtracted, or globally constrained zero-mode
> ensemble.

The phrase “fixes every geometry-dependent state term and improvement” already
covers (4). No new axiom category is exposed by this construction. The wording
is sufficient, hypothetical, unadopted, not proved necessary, and not claimed
minimal. It may instead remain a downstream convention followed by an
import-retirement audit.

### Level C — still required after the amendment

Block 13 retires the specific Block-12 static nonzero-mode source residual on
the named finite carrier. It does not select or derive:

- why (4), rather than another flat-law-equivalent improvement, is physical;
- why an isolated binary defect is mass or which Record content carries it;
- a dynamic conserved worldline and one realized history;
- the geometry action's orientation, coupling magnitude, and Lorentzian sign;
- the compact infrared ensemble or compensating sector in (23);
- nonlinear/projective geometry and strong-field behavior; or
- the independent Born functional, effect program, and occurrence law.

The approved kinetic-isotropy primitive supplies equal-form tick graining only.
It is a registered dependency, not a wall, and is not enlarged here.

## 7. Consequence For The TOE Lanes

| Lane | Exact Block-13 advance | Still open |
|---|---|---|
| operational quantum / records | the action carrier can distinguish an isolated local defect while preserving the complete flat law | physical defect/Record identification, action unit, and occurrence |
| causal time | the static tick-edge source is exact and the `k_tau!=0` failure is now localized | dynamic worldline, causal update, rate, and realized history |
| inertia / matter | the isolated source has a pure tick density on the actual carrier rather than an affine bag contaminated by spatial/null residuals | mass typing, dressed inertia, motion, and interaction law |
| gravity / source / resources | the Block-12 static nonzero-mode gauge/null residual is cancelled by an explicit local improvement; the actual unprojected Regge pole and open tail survive | action selection, coupling/sign, compact ensemble, dynamics, nonlinear and Lorentzian field law |
| Born probability / realized history | flat conditional weights are unchanged configuration by configuration | functional/program selection and one realized history |

This is high-value gravity/source progress, but the science block is not yet
landed, audited, or adopted. No canonical axiom is edited. Under the fixed
campaign rubric, the fixed TOE percentages do not move.

## 8. Relation To Existing Sources

| Source | Exact use | Boundary preserved |
|---|---|---|
| [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | spatial cubic locality, local probability surface, and explicit exclusions of dynamics and source/action identification | no history action, physical mass, geometry equation, or realized history imported |
| [Block-12 affine bag](ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | centered bag source, internally derived normalization, measured residual orders, actual-Regge pole, Green tail, and candidate amendment | the old residual is an active control; physical selections remain open |
| [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | equal-form tick graining only | no dynamics, source, mass, selector, or Lorentzian law imported |
| [Actual 3+1 Regge second variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) | axial edge, line-averaged metric map, Hessian, four gauge zeros, fifth branch, and long-wave metric action | edge/action selection, orientation, nonlinear completion, and physical tick scale remain supplied |

The older
`docs/G_NEWTON_WEAK_FIELD_RESPONSE_BOUNDED_CLOSURE_NOTE_2026-05-10_gnewtonG3.md`
identified the then-absence of a smooth metric tensor as a wall for its
proper-time route. That residual is not the present compact-zero-mode or
dynamic-current residual. Later coframe/Regge constructions have also retired
the relevant carrier-absence premise on this supplied model surface. The old
note is therefore provenance-only cross-cycle context, not a witness or
dependency for (23).

## 9. No-Go Discipline Gate

The negative content is deliberately split into two narrow statements:

1. a nonzero total tick charge is outside the range of the bare unmodified
   periodic quadratic Regge Hessian at `k=0`; and
2. a fixed vertical line at `k_tau!=0` does not satisfy the discrete gauge
   identity by itself.

Neither statement says that compact gravity, dynamic matter, or a physical
mass source is impossible.

### N1 — alternative route enumeration

Approach families are normalized by their primary object, mechanism, and
terminal obligation.

| Route family | Attempt and scoped result | Marker |
|---|---|---|
| open/infinite boundary | Replace the compact inverse by the open Green problem; this removes the normalizable constant mode and yields (14), but changes the boundary premise and therefore does not solve the bare periodic equation (23). | ATTEMPTED |
| fixed global lapse/strain | Remove the constant metric variation from the allowed variational domain; this can make the constrained equation compatible, but it is a fixed-global-mode ensemble rather than the bare Hessian domain named in (23). | ATTEMPTED |
| compensating/background source | Add an opposite total charge or background counterstress so the compact source sums to zero; this can close the global compatibility condition, but the compensator is absent from the isolated-source action. | ATTEMPTED |
| curved or balanced torus | Expand about an on-shell curved/background-balanced geometry instead of flat periodic OS0; the linear operator and source balance then change, so this is a live completion rather than a contradiction of the flat-Hessian calculation. | ATTEMPTED |
| combined geometry constraint or lifted branch | Vary matter and geometry jointly or modify the geometry action so the global constraint and fifth branch are handled on shell; the supplied quadratic Regge theorem leaves higher order open, so this changes the equation under test. | ATTEMPTED |
| closed dynamic worldline | Add the spatial segments, vertices, endpoint forces, or history variation needed for a conserved four-current; this directly attacks the `k_tau!=0` control but is not the fixed vertical line tested here. | ATTEMPTED |
| neutral defect pair | Use one occupied and one complementary isolated defect so the total signed tick charge vanishes; static modewise compatibility remains additive, but this proves a neutral sector rather than a single nonzero total charge. | ATTEMPTED |

There are at least five distinct live routes. They defeat any framework-wide
no-go, so only the two displayed bare-fixture statements may ship.

### N2 — wall-independence audit

The collapsed open-condition set is:

- `S`: selection and physical typing of the history/action representative,
  defect, action unit, and mass/Record carrier;
- `G`: geometry action/update, orientation, coupling, sign, and nonlinear law;
- `I`: infrared boundary/global-zero-mode ensemble; and
- `H`: dynamic conserved history and realized occurrence.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| `S,G` | no; selecting matter content does not fix its field equation | no; a geometry law does not identify which defect is mass | yes |
| `S,I` | no; a selected source can still violate compact neutrality | no; a boundary ensemble does not select matter/action content | yes |
| `S,H` | no; a selected static density does not supply motion or occurrence | no; a history law does not identify its charge as physical mass | yes |
| `G,I` | no; local normalization/sign does not choose global boundary data | no; a zero-mode prescription does not fix the local geometry law | yes |
| `G,H` | no; a geometry equation alone does not specify the matter worldline | no; a conserved history does not fix coupling or nonlinear geometry | yes |
| `I,H` | no; compact neutrality does not provide dynamics | no; local dynamics need not choose the global ensemble | yes |

The static nonzero-mode conservation residual is not retained as a fifth wall:
equations (8)--(21) retire it on the named Block-13 surface. Physical mass
typing is folded into `S`, and realized occurrence is folded into `H`.

### N3 — hidden-wall scan

The note was scanned for `we assume`, `by construction`, `as is standard`,
`the framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit class | Classification |
|---|---|
| flat background / supplied OS0 carrier | explicit theorem domain and `G`, not an axiom-selected premise |
| background source or balanced torus | explicit alternative route under `I`, not silently used in the positive proof |
| registered primitive or action language | source-bound dependency for the primitive; unadopted candidate wording for the action |
| canonical axiom statement | governance boundary only; no scientific identity follows from the label |
| line and bag defined by construction | explicit mathematical definitions (1)--(4), non-load-bearing as physical claims |

No hidden wall is added. The four-wall set remains collapsed.

### N4 — residual matching

| Witness | Witness residual | Block-13 residual or target | Match? |
|---|---|---|---|
| `ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_...2026-08-10.md:138-146` | localized bag has `O(k^3)` gauge, `O(k^2)` extra-null, and bare periodic `k=0` residuals | (4)--(21) target and retire the first two; (23) preserves the same `k=0` residual | yes |
| `CUBIC_COXETER_REGGE_3PLUS1_...2026-06-09.md:41-45` | four exact gauge modes, constant metric zero modes at `k=0`, and one extra quadratic branch | null inventory (20), periodic boundary (23), and dynamic gauge control | yes |
| `ADMISSIBILITY_CUT_SURFACE_COFRAME_...2026-08-10.md:483-488` | action-representative selection and combined on-shell geometry dynamics are open | `S`, `G`, and `H` | yes |
| `G_NEWTON_WEAK_FIELD_RESPONSE_...2026-05-10_gnewtonG3.md:319-326` | smooth metric/proper-time carrier was absent on its older surface | compact zero-mode and dynamic-current residuals | no; dropped as a witness |

The mismatched old metric-absence result is used only in N8 to check how prior
walls were retired.

### N5 — rhetoric audit

| Resolution | What is executed | What is not claimed |
|---|---|---|
| per element | actual axial tick-edge metric derivative, unique coefficient two, and exact static gauge factor | no arbitrary edge family or selected particle ontology |
| per site | all 128 radius-one neighborhoods, complement covariance, isolated replacement, and plane nonactivation | no classification of every larger-support improvement |
| per mode | every nonzero static mode for `L=3,...,8`, plus one dynamic hostile control | no symbolic theorem for every continuous momentum or lattice size |
| per block | bag-to-line action improvement through unprojected Regge pole and regulated Green tail | no nonlinear, Lorentzian, or empirical gravity theory |
| lattice wide | all 1,281 named nonzero modes and the separate nonzero-total-charge `k=0` obstruction | no obstruction for open, fixed-mode, neutralized, curved, or dynamic ensembles |

The primary cached stdout carries one substantive execution-certificate line
for every row. The negative phrases are restricted to the bare periodic
zero-mode equation and fixed vertical dynamic fixture.

### N6 — partial-closure path scan

The primitive registry was checked before treating any dependency as a wall.

| Existing path | Status | What it closes or could close |
|---|---|---|
| approved kinetic-isotropy primitive | registered premise, not a wall | supplies equal-form tick graining only |
| Block-12 Level-A action convention | existing bounded downstream path | can register (4) as model content without a foundation edit |
| Geometry-indexed history/action amendment | unadopted sufficient wording | would register the absolute representative, carrier, geometry update, coupling, and ensemble at foundation level |
| actual Regge second variation | supplied bounded theorem | supplies the conditional carrier and Hessian, not their physical selection |
| open/static Green problem | executed in Blocks 12--13 | closes the compact zero-mode issue for the open weak-field shape |
| fixed, neutralized, or background-balanced ensemble | unadopted convention route | could retire `I` without adding a new local physics axiom |
| dynamic worldline construction | live scientific route | could retire the fixed-line part of `H` by bound theorem followed by import-retirement audit |

It would be false to say that this result requires a new axiom. The existing
candidate wording is sufficient for autonomous registration, while a declared
downstream model convention is sufficient for the mathematics. Selection and
new dynamics remain physical work, not automatically a fifth axiom.

### N7 — steelman

A hostile reviewer should say that (23) is merely the compact Gauss-law
compatibility condition, not evidence against gravity: an open boundary,
fixed global lapse, neutral pair, background charge, or curved on-shell torus
can remove it. The `k_tau!=0` control is equally unsurprising because a vertical
edge is only one segment of a worldline; adding its spatial segments and
varying the combined matter-geometry action may restore the Ward identity.
Block 13 itself demonstrates how quickly the previous bag residual disappeared
once a different flat-law-equivalent local representative was considered.
This is a decisive objection to any broad no-go and supplies the next concrete
construction target. It does not contradict the two narrow algebraic facts
about the unmodified bare fixtures, so the source adopts the steelman and keeps
the negative claim at that scope.

### N8 — cross-cycle echo

| Similar prior wall | Retirement mechanism and current lesson |
|---|---|
| Block 12's localized gauge/extra-null residual | explicit local line-minus-bag improvement retires it on the named static surface; alternative representatives must stay live |
| the older G-Newton metric-carrier absence | later coframe and actual Regge constructions supplied a bounded metric carrier; an absence claim is epoch- and surface-specific |
| Block 11/12 action-selection language | Level-A downstream convention separated mathematical construction from foundation adoption; do not relabel every selector as a new axiom |
| periodic massless-operator zero-mode walls | open, fixed-mode, compensating, and background-balanced ensembles are explicit resolution mechanisms and all remain live here |
| static-source conservation walls | the combined on-shell matter-plus-geometry Ward route remains live; a fixed source failure is not a dynamic no-go |

Every known retirement mechanism relevant to this residual—new construction,
convention, boundary choice, compensator, and combined dynamics—is represented
in N1 or N6. None is foreclosed.

**Gate status:** PASS for the two narrow bare-fixture statements; FAIL for a
framework-wide compact-gravity, dynamic-matter, physical-mass, or universal
no-route reading.

## 10. Verification

Run:

    python3 scripts/admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py

The primary runner checks:

- current-axiom, Block-12, approved-tick-primitive, and actual-Regge source
  boundaries;
- all 128 radius-one binary neighborhoods and exact complement covariance;
- flat-law preservation, isolated bag-to-line replacement, and wrapping-plane
  nonactivation;
- actual tick-edge normalization, homogeneous source preservation, exact static
  gauge identity, and pure tick metric source;
- the old generic bag residual and its explicit line-minus-bag cancellation;
- `O(k^2)` counter-improvement metric neutrality;
- all 1,281 nonzero static modes on `L=3,...,8`, including zero-mode count,
  full-null overlap, and direct unprojected edge residual;
- separated-source additivity, four-direction unprojected lapse pole,
  convergence, and regulated `1/r` tail;
- bare periodic `k=0`, mixed dynamic, and proper-cubic controls;
- source-note N1--N8, governance, and five-resolution execution surfaces; and
- canonical-axiom nonmutation and fixed-percentage boundaries.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The strongest honest chain is now

    compatible binary cut
      -> explicit four-coframe worldvolume
      -> affine tick-only bag source
      -> flat-law-preserving isolated-defect improvement
      -> actual axial tick-edge source
      -> exact static gauge identity
      -> exhaustive named-torus full-null compatibility
      -> unprojected Regge 1/k^2 lapse pole
      -> open-boundary 1/r shape.

The specific Block-12 static nonzero-mode source residual is retired on the
named carrier. The compact nonzero-charge zero mode and fixed-line dynamic
control remain explicit. No history/action representative, mass/Record
identity, coupling, sign, Lorentzian continuation, infrared ensemble,
nonlinear field equation, Born functional, or realized history is selected.

No canonical axiom is edited. No universal no-go is claimed. The fixed TOE
percentages do not move.
