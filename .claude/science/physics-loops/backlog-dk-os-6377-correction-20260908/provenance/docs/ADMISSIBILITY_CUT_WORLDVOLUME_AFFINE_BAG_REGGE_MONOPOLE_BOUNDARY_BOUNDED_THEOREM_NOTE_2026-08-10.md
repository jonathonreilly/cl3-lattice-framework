---
claim_id: admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "On a supplied finite 3+1 tick extension, the binary cut has an explicit local four-coframe worldvolume action whose static restriction is the Block-11 spatial cut action times tick length. Its exact flat derivative adds a positive tick/tick metric source to the two spatial tangential sources. On the actual supplied cubic-Coxeter edge carrier, a Kuhn-triangulated unit hyperface has the same homogeneous metric derivative. For one static unit-cell tube, the centered four-volume improvement with pressure p=4 tau is uniquely fixed by homogeneous spatial stationarity and gives exact flat metric source T_bag(0)=tau e_tau e_tau^T. After an explicitly named metric-transverse projection, the actual Regge response obeys |k|^2 h_tau_tau -> 2 tau across four spatial directions, hence has the open-boundary 1/r monopole shape. A wrapping plane is exactly compatible with all nonzero-momentum Regge null modes. The unprojected localized bag is not an exact finite-lattice dust solution: a generic mixed-mode gauge remainder scales as k^3, its extra-null overlap scales as k^2, and the nonzero k=0 source is incompatible with the bare finite periodic Hessian. No history law, physical action family, pressure mechanism, mass identification, Regge/action selection, coupling, sign, Lorentzian continuation, infrared ensemble, nonlinear completion, axiom necessity, or adoption is proved."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py
---

# Cut Worldvolume, Affine Bag Source, And Regge Monopole Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** weak-field bridge and axiom-consequence map
**Scope:** supplied finite `Z^3 x Z_tau` binary histories, one explicit
worldvolume/volume family, and the supplied flat cubic-Coxeter Regge Hessian.
No physical history or geometry law is inferred.
**Audit-status authority:** independent audit lane only. This source authors
no audit verdict and predicts none.
**Primary runner:**
[admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py](../scripts/admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py)

## Result Up Front

Block 11 derived the spatial coframe response of the compatible binary cut but
left its temporal extrusion and lapse source open. This block constructs both
at model level and then tests them against the repository's actual Regge
carrier.

On a supplied finite four-dimensional tick complex, let `x_z in {0,1}` and
define the signed jump, cut indicator, and endpoint share on every four-axis
`mu` by

    j_z,mu=x_(z+e_mu)-x_z,
    chi_z,mu=j_z,mu^2,
    m_z,mu=[chi_z,mu+chi_(z-e_mu),mu]/2.

For an orientation-preserving local four-coframe `E_z`, define

    A_z,mu(E_z)=|cof(E_z)e_mu|.

The supplied worldvolume action is

    S_W[x;E]=tau sum_(z,mu) m_z,mu A_z,mu(E_z).       (1)

At `E=I`, equation (1) is `tau` times the four-dimensional cut. For a static
history `x_(i,n)=x_i`, no tick-normal faces occur. If
`E=diag(F,lambda_tau)`, then every spatial-normal three-volume is
`lambda_tau` times the corresponding Block-11 two-area. Thus

    S_W[static;diag(F,lambda_tau)]
      =N_tau lambda_tau S_cut[x;F].                  (2)

This is the requested temporal extrusion, not a relabeling of the spatial
action.

The exact flat four-coframe derivative is

    Pi_z=tau[(Tr Q_z)I_4-Q_z],
    Q_z=sum_mu m_z,mu e_mu e_mu^T.                  (3)

For a static face normal to spatial axis `a`,

    Pi_face=tau(I_4-e_a e_a^T).                     (4)

Equation (4) contains the two Block-11 spatial tangential entries and one new
equal tick entry. With metric perturbation `h=delta(E^T E)`, the metric source
is one half of each diagonal coframe entry. A static cut therefore has a
derived tick/lapse source; setting it to zero is not the static extrusion of
the same area action.

The actual edge-carrier check is stronger. Triangulate one unit cut
hyperface by the six tetrahedra induced by the supplied Kuhn/Coxeter complex
and differentiate its true three-volume with respect to its edge lengths.
At flat geometry all diagonal-edge derivatives cancel. The total derivative
is one on each of the three tangent axial edge classes. Projection through the
actual line-averaged Regge metric map gives exactly

    t_face,mu_nu(0)
      =[delta_mu_nu-delta_mu,a delta_nu,a]/2.        (5)

In particular, a spatial cut face has `t_tau_tau=1/2`.

Now take one occupied spatial cell, extruded through the tick direction. Its
boundary has six timelike hyperfaces. Add the centered, flat-law-preserving
volume improvement

    S_p[x;E]
      =-p sum_z (x_z-1/2)[V_z(E)-1].                (6)

Equation (6) vanishes for every binary configuration at flat geometry, so it
does not alter the Block-11 flat law. It is covariant under simultaneous code
swap and pressure reversal. Its geometry derivative is nevertheless nonzero.

Homogeneous spatial stationarity of the unit tube fixes the pressure; it is
not fitted to a target:

    2tau-p/2=0
      => p_*=4tau.                                  (7)

With (7), the six-face surface derivative and four-volume derivative give

    T_bag(0)=tau e_tau e_tau^T.                     (8)

All three spatial stresses and all shifts cancel exactly, while the tick
source remains positive. The active control `p=3tau` leaves spatial source
`tau/2` and does not reproduce (8).

Feed the same local face/volume derivatives into the actual cubic-Coxeter
Regge Hessian. For the exact wrapping plane, every sampled nonzero normal
momentum annihilates all four gauge zero modes and the extra non-metric zero
branch; the linear edge equation is solvable modulo its null space. For the
localized bag, center the cell phase. Its metric source is

    T_bag(k)=tau e_tau e_tau^T+O(k^2).               (9)

On the explicitly projected metric-transverse sector, the actual action gives

    |k|^2 h_tau_tau -> 2tau                         (10)

in the raw Regge orientation, independently across axial, face-diagonal,
generic mixed, and body-diagonal spatial directions. Since

    Fourier^-1[1/|k|^2](r)=1/(4 pi r),              (11)

equation (10) is a genuine leading `1/r` monopole **shape** on an open or
infinite boundary. The runner derives (11) with an exponential regulator:

    integral_0^infinity exp(-epsilon k) sin(kr)/k dk
      =atan(r/epsilon) -> pi/2.

This does not fix Newton's constant, the physical sign, or the conversion from
the Euclidean tick component to a Lorentzian potential.

Two finite-lattice residuals remain and are kept separate:

1. At a generic three-component spatial momentum, the unprojected bag's gauge
   force is nonzero and scales as `O(k^3)`.
2. Its overlap with the extra Regge zero branch is nonzero and scales as
   `O(k^2)`.

At `k=0`, the source overlaps the constant-metric zero modes, so the bare
finite periodic linear equation has no solution. Open boundaries, fixed
global strain/lapse, background counterstress, a lifted non-metric branch,
other local improvements, and a dynamical worldvolume all remain live. No
universal no-go is claimed.

The construction therefore reaches farther than Block 11: it produces a
conditional lapse monopole and the correct weak-field radial shape from an
actual geometry action. It is not an exact finite-lattice dust solution and
not a selected physical mass.

No canonical axiom is edited, and the fixed TOE percentages do not move.

## Machine Status And Trace

~~~yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 3+1 cofactor extrusion, Kuhn-hyperface source, affine pressure p/tau=4, flat tick-only source, wrapping-plane Regge compatibility, long-wave lapse pole, radial 1/r consequence, and distinct finite-lattice residual orders are computed. Physical history/action selection, exact localized conservation, geometry-law normalization, infrared ensemble, and axiom adoption remain open."
trace_class: upstream_support
target_claim_id: admissibility_cut_worldvolume_to_physical_regge_newton_source_bridge
target_blocker_text: "select one physical geometry-indexed history action and joint matter-geometry update whose localized source is exactly conserved on the chosen edge carrier, fixes the infrared zero-mode ensemble, and licenses the Regge orientation/coupling and Lorentzian weak-field readout"
source_of_blocker_text: derived_here
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "construct an exact finite-lattice local improvement or dynamical history that removes the O(k^3) gauge and O(k^2) extra-null residuals without projecting the source by hand"
conditional_surface_status: "one explicit static worldvolume family yields an exact flat tick source and the actual Regge metric sector yields the 1/r monopole shape; exact localized finite-lattice conservation and physical selection remain supplied"
hypothetical_axiom_status: "the geometry-indexed history/action amendment below is sufficient but neither adopted, proved necessary, nor claimed minimal"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## Exact Target Contract

| Contract field | Block-12 value |
|---|---|
| target statement | extend the exact spatial cut into a spacetime source, derive rather than assume its lapse component, couple it to the actual Regge Hessian, and determine its weak-field monopole and exact finite-lattice residuals |
| quantifiers/domain | finite supplied `Z^3 x Z_tau` binary histories and positive four-coframes; static unit hyperfaces and one-cell tubes for the actual edge action; small nonzero static momenta for the weak-field limit |
| allowed premises | Block-11 cut action, approved equal-form tick graining, elementary cofactor and simplex-volume algebra, and the supplied actual 3+1 Regge action/Hessian |
| forbidden weakenings | inserting `T_tau_tau` by hand, fitting pressure to a Newton target, hiding a source projection, calling periodic zero-mode subtraction automatic, identifying a statistical action with physical mass, or treating the Regge action/sign/coupling as axiom-selected |
| required edge cases | static reduction, tick stretch, all four hyperface normals, code complement/pressure reversal, wrong pressure, wrapping plane, localized unit tube, axial and generic mixed momentum, extra Regge zero branch, and `k=0` |
| completion witness | explicit worldvolume family, exact four-coframe derivative, exact Kuhn edge derivative, derived affine pressure, tick-only flat source, actual-Regge lapse pole, radial transform, and measured residual orders |
| outcomes not counting as closure | a spatial stress with `T_tau_tau=0`, a target operator inserted as the update, a projected source presented as exact, a finite periodic Green solve with silent zero-mode deletion, or candidate axiom wording alone |

## 1. Four-Dimensional Cut Worldvolume

Let the finite supplied history lattice be

    Lambda=(Z/LZ)^3 x (Z/N_tau Z).

The tick coordinate is a supplied history coordinate in this construction.
The approved kinetic-isotropy primitive grants only that its graining has the
same form as a spatial edge; it supplies no history law or dynamics.

For `x:Lambda->{0,1}`, use the definitions preceding (1). The four-dimensional
cut size is

    C_4=sum_(z,mu) chi_z,mu.

Equation (1) is local, complement even, and positive for positive `tau`. On a
finite history lattice it defines a positive normalized Gibbs family if one
chooses to sum over histories. That probability interpretation is conditional;
the current Admissibility axiom specifies spatial nearest-neighbor
distributions and does not select a tick-neighbor history law.

### Static restriction

For `x_(i,n)=x_i`, `chi_z,tau=0`. With

    E=diag(F,lambda_tau), lambda_tau>0,

four-dimensional cofactor factorization gives

    |cof(E)e_a|=lambda_tau |cof(F)e_a|

for every spatial `a`. This proves (2). At `F=I`, `lambda_tau=1`,

    C_4=N_tau C_3,
    S_W=N_tau tau C_3.

Thus one spatial cut face becomes one timelike three-face per tick. No
independent tick energy has been appended.

### First variation and source typing

For `E=I+H`, in four dimensions,

    delta[cof(E)]_(I)=Tr(H)I-H^T,
    delta A_mu=Tr(H)-H_mu,mu.

This yields (3). At flat geometry `Pi` is symmetric. If

    h=delta(E^T E)=H+H^T,

then

    delta S_W=(1/2) sum_z Pi_z:h_z.

In a ten-component symmetric-metric coordinate vector, diagonal source entries
are `Pi_mu,mu/2` and offdiagonal entries are `Pi_mu,nu`. Equation (4) therefore
gives `tau/2` in each tangent diagonal. The tick source is fixed relative to
the spatial tangential source by the same worldvolume action.

For a static cut with `C_3` faces and `N_tau` ticks,

    sum_z Pi_tau,tau=tau N_tau C_3,
    sum_z t_tau,tau=(tau/2)N_tau C_3.                (12)

Equation (12) is a Euclidean action derivative. It is not yet physical energy.

### Four-dimensional virtual work and higher-form current

Any declared displacement pullback `E[u]` gives a corresponding virtual-work
identity. A centered pullback repeats the Block-11 summation by parts in four
directions:

    delta S_W/delta u_z=-div^0 Pi_z.

Local conservation is again an on-shell matter/history condition. Separately,
the occupied dual four-cells form a four-chain `U_4`; their signed interface
is the three-current

    J_3=partial U_4,
    partial J_3=0.

The higher-form closure is off shell. It does not imply stress-energy
conservation.

## 2. The Actual Kuhn/Coxeter Edge Source

The four-coframe result does not by itself specify how a dual cut surface
couples to the actual Regge edge variables. This section constructs one local
edge representative on the supplied path complex.

Take a unit hyperface normal to axis `a`. Its eight vertices carry the six
Kuhn tetrahedra obtained by ordering the three tangent axes. For a tetrahedron
with Gram matrix `G`,

    V_3=sqrt(det G)/6,
    delta V_3=(V_3/2) Tr(G^-1 delta G).              (13)

The runner evaluates (13) with exact rational arithmetic at flat geometry,
maps every tetrahedron edge to its actual Coxeter edge class and anchor, and
sums the cover.

The exact result is:

- the six tetrahedron volumes sum to one;
- every diagonal-edge derivative cancels in the complete cover;
- the surviving axial-edge weights sum to one for each tangent direction and
  zero for the normal direction.

If `r_a(k)` is this edge-source row and `M(k)` is the actual line-averaged
metric map, then at zero momentum

    r_a(0)M(0)=t_face(0),                            (14)

with `t_face` given by (5). Equation (14) independently recovers the cofactor
derivative using the true edge-length variables.

The fixed Kuhn diagonal makes the individual real-space edge-weight stencil
frame dependent away from the affine sector. This source does not silently
average over unavailable diagonals. The homogeneous tensor (14) is proper-
cubic covariant; an all-frame exact edge carrier would require the co-present
frame construction or another selected triangulation rule.

### Exact plane compatibility

For a wrapping plane normal to spatial axis `a`, tangential translations force
`k_b=0` for every `b!=a`. Equation (13) then reduces to the unit source on the
three tangent axial edge classes. Each such edge `v` has `k dot v=0`, so the
actual Regge gauge row

    G_v,rho(k)=[exp(i k dot v)-1]v_rho/|v|

is annihilated exactly. The runner also diagonalizes the actual `15 x 15`
Hessian at twelve nonzero momenta and finds that the plane source annihilates
its fifth, non-metric zero branch to machine precision. The pseudoinverse
equation has residual below `4e-12`.

This is an exact nontrivial combined source/action solution class: a planar
domain wall can source the nonzero normal-momentum Regge response without a
Ward repair. It is extended, not a localized mass.

## 3. A Flat-Law-Preserving Unit Bag

The one-cell spatial tube has two hyperfaces for each of the three spatial
normals. At homogeneous flat geometry their total metric source is

    t_surface=diag(2tau,2tau,2tau,3tau).             (15)

The unit four-volume has metric derivative

    t_volume=(1/2)I_4.                              (16)

Use the centered improvement (6). The subtraction by one makes the term zero
on the entire flat law, not merely on the selected bag. Centering `x-1/2`
gives exact covariance

    (x,p)->(1-x,-p).

The pressure is a source parameter and changes sign with the chosen phase. It
is not Record's scalar readout.

Every localized bag source below is the response difference between the
one-cell tube and the empty reference history. The uniform `-1/2` background
in (6) therefore cancels exactly, leaving the occupied-cell volume derivative
used in (15)--(16). Under code swap the corresponding reference is the full
history. No uniform background source is silently included in the localized
Fourier row.

Stationarity under any homogeneous spatial diagonal strain demands that each
spatial entry of `(15)-p(16)` vanish. All three equations coincide and give
(7). The tick entry then becomes

    3tau-(4tau)/2=tau,

which proves (8). More generally, in `d` spatial dimensions a unit hypercube
would give the affine relation `p/tau=2(d-1)`; `4` is the derived `d=3` value,
not a numerical fit.

The construction is a pressure-balanced **affine bag candidate**. At the
identity source it has the stress pattern of static dust. It is not a selected
physical mass because:

- the history/worldvolume family is supplied;
- the volume improvement is one allowed off-background continuation, not
  selected by the flat probability law;
- the pressure mechanism and code phase are supplied; and
- the physical action unit and tick-to-energy reading are open.

The distinction between the flat action value and its geometry derivative is
load bearing. Because `(V-1)` vanishes at flat geometry, the improvement can
change the lapse derivative while leaving every flat Gibbs weight untouched.
This is a concrete instance of the Block-11 action-family ambiguity, not an
additive constant independent of the binary configuration.

## 4. Regge Weak-Field Response

Let `s_bag(k)` be the Fourier edge-source row obtained from the six
hyperfaces minus four times the unit four-volume derivative. Remove the phase
of the cell center. Direct projection through the actual metric map gives

    s_bag(k)M(k)
      =tau e_tau e_tau^T+O(k^2),                    (17)

with no offdiagonal metric source. The runner measures the exponent `2` rather
than assuming it.

The supplied Regge note independently establishes on its metric sector

    Q_h(k)=-1/2 Q_EH(k)+O(k^4).                     (18)

For static momentum, `h_tau_tau` is invariant under the linear metric gauge
shift because `k_tau=0`. Project the small finite-lattice longitudinal source
piece explicitly, solve

    Q_h h+T_transverse=0,                           (19)

and keep the projection visible. Four spatial directions give

| direction | `|k|^2 h_tau_tau/tau` at `|k|=0.025` |
|---|---:|
| axial | approaches `2` |
| face diagonal | approaches `2` |
| generic `(1,.7,.4)` | approaches `2` |
| body diagonal | approaches `2` |

The runner computes the values and requires their maximum error from `2` to be
below `2e-4`. Halving momentum reduces every error, consistent with the
`O(k^2)` correction implied by (17)--(18).

Equations (10)--(11) follow. In the raw normalization the leading radial tick
response is

    h_tau_tau(r) ~ tau/(2 pi r),                    (20)

before the geometry-action coefficient, coupling, orientation, and physical
signature are supplied. Only the `1/r` shape and relative source channel are
derived here.

### What this does and does not retire

| Obligation | Block-12 status |
|---|---|
| temporal extrusion of the cut | constructed exactly as (1)--(2) |
| tick/lapse derivative of the same area action | constructed exactly as (3)--(5) |
| local actual-edge source at flat | constructed exactly from Kuhn volumes |
| one affine dustlike source | constructed with uniquely stationary `p_*=4tau` |
| nonzero-momentum plane/Regge compatibility | exact on sampled plane family, including extra null branch |
| leading localized metric source and lapse pole | `T_tau_tau=tau+O(k^2)` and `|k|^2h_tau_tau->2tau` |
| weak-field radial shape | `1/r` on an open/infinite boundary |
| exact localized finite-lattice conservation | open; explicit `O(k^3)` gauge and `O(k^2)` extra-null residuals |
| physical family, pressure, mass, Regge action/sign/coupling | open |
| finite periodic `k=0` equation | requires a declared infrared ensemble or compensator |

## 5. Exact Finite-Lattice Boundaries

### Gauge remainder

At generic mixed spatial momentum, the source is not exactly transverse on the
fixed Kuhn stencil. The runner measures

    ||s_bag G_edge||=O(k^3).                        (21)

One nonzero counterexample is enough to rule out presenting the bare bag as an
exact all-mode Ward solution. Equation (21) does not rule out an improved
stencil or a dynamical matter history.

### Extra non-metric zero branch

The actual quadratic Regge Hessian has a fifth zero branch outside the metric
sector. The bag-source overlap obeys

    ||Z_extra^dag s_bag||=O(k^2).                   (22)

Thus the full edge equation retains a finite-lattice residual even after the
leading metric source is dustlike. Projecting (22) away is a named comparator
operation, not an exact local field equation. A higher-order geometry action,
an alternative triangulation, or a source improvement could lift or decouple
this branch.

### Periodic zero mode

At `k=0`, the supplied Hessian has ten constant-metric zero modes plus the
extra branch. The bag edge source has nonzero projection on that null space.
Consequently

    Q_R(0) ell(0)+s_bag(0)=0                       (23)

has no solution on the bare finite periodic linearized system. This is the
usual compatibility condition for a source on a compact massless operator,
here checked on the actual `15 x 15` Hessian rather than asserted by analogy.

Equation (23) is scoped to the bare periodic ensemble. An open or infinite
boundary removes the constant normalizable mode and is already the domain used
for (11). Fixing global lapse/strain, adding background counterstress, moving
to a curved background, or imposing a compensating total source are distinct
live routes.

## 6. Exact Axiom And Convention Consequence Map

The mathematical construction needs no canonical edit if it is declared as a
downstream model. Full autonomous physical typing would require the current
axioms to say more than they do. The missing obligations are now specific.

### Level A — downstream convention, no axiom edit

A model can declare:

1. a finite binary tick history;
2. equations (1) and (6), including the pressure-source transformation;
3. the actual edge-volume representative and its fixed triangulation;
4. the Regge action coefficient, orientation, and coupling; and
5. an open boundary or zero-mode constraint.

Every positive and negative result in this note then follows without changing
Lattice, Qubit, Admissibility, or Record. The source remains model input.

### Level B — candidate foundation amendment

One sufficient, deliberately explicit wording is:

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

This is sufficient wording, not adopted wording. It is not proved necessary
or minimal. It could be split among amendments to Lattice, Admissibility, and
Record rather than introduced as a fifth named axiom. It can also remain a
downstream source/action convention.

### Level C — still required after the amendment

Even Level B does not derive a particular worldvolume family, pressure
mechanism, or Regge action. A completed physical route must still prove or
select:

- why (1), (6), or another exact finite-lattice family is realized;
- a local matter/history equation that removes (21);
- a carrier law that removes or lifts (22);
- the geometry-action normalization, sign, and Lorentzian continuation;
- the infrared ensemble in (23); and
- the physical identification and calibration of the monopole charge.

The approved kinetic-isotropy primitive already supplies the equal-form tick
graining. It is not a wall and is not enlarged here. It supplies none of the
items above.

## 7. Consequence For The TOE Lanes

| Lane | Exact Block-12 advance | Still open |
|---|---|---|
| operational quantum / records | one flat-law-preserving off-background improvement is explicit and code/pressure covariant | physical family selection, action unit, and Record/source identification |
| causal time | the spatial cut is explicitly extruded to a three-dimensional worldvolume with a derived tick source | selected history law, permanence-compatible update, causal propagation, and rate |
| inertia / matter | one unit tube has an exact affine dustlike source pattern rather than only spatial tension | exact finite-lattice equilibrium, physical mass identification, and dressed inertia |
| gravity / source / resources | actual edge-volume source, exact plane Ward compatibility, derived lapse monopole, Regge `1/k^2` pole, and open-boundary `1/r` shape | exact localized Ward/null completion, action/sign/coupling, infrared ensemble, nonlinear and Lorentzian field law |
| Born probability / realized history | the flat probability law can remain unchanged while the geometry derivative changes | selection of the off-background family and one realized history |

This is meaningful gravity/source progress, but it remains a conditional model
stack. No canonical axiom is edited and no independent audit has acted. Under
the campaign's fixed rubric, the fixed TOE percentages do not move.

## 8. Relation To Existing Sources

| Source | Exact use | Boundary preserved |
|---|---|---|
| [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | spatial cubic sites, local probability surface, and explicit statement that source/action and dynamics are outside the memo | no history, geometry, action, or gravity content imported |
| [Block-11 coframe stress](ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | spatial cut action, endpoint shares, cofactor response, action-family ambiguity, and on-shell Ward distinction | no temporal extrusion, mass, or geometry equation inherited |
| [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | equal-form tick graining only | no history law, dynamics, action, source, coupling, or Lorentz theorem imported |
| [Actual 3+1 Regge second variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) | actual edge classes, metric map, Hessian, gauge zeros, extra branch, and `Q_h=-Q_EH/2+O(k^4)` | edge/action selection, sign, nonlinear completion, and tick scale remain supplied |

The Cycle-576 source tournament is context only. It proved exact Ward
compatibility for a deficit source, not for this matter worldvolume. Its
metric-map and source-calibration boundaries agree with the distinct residuals
found here; none of its numerical source amplitudes or couplings are imported.

The older Gate-B weak-field interface used a supplied `1/(r+epsilon)` scalar.
This note instead derives the `1/k^2` pole from the actual Regge Hessian and the
`1/r` transform analytically. Gate B's detector, normalization, and generated-
connectivity residuals do not match this block's finite-lattice Ward/null
residuals and are not counted as witnesses.

## 9. No-Go Discipline Gate

The negative claim shipped here is deliberately narrow:

> The **bare fixed-Kuhn, affine-pressure, one-cell source** is not an exact
> all-mode source of the **unmodified quadratic Regge equation on a finite
> periodic lattice**. One sampled generic mixed mode has the nonzero residuals
> (21)--(22), and its nonzero `k=0` source violates (23).

The positive long-wave monopole theorem and the exact plane family are not
weakened by that scoped statement.

### N1 — alternative route enumeration

Approach families are normalized by object, mechanism, and terminal
obligation rather than by wording.

| Route | Attempt and result | Marker |
|---|---|---|
| open/infinite geometry | Replace the compact periodic inverse by the open-boundary Green problem; this removes the `k=0` compatibility condition and produces (11), but changes the infrared premise and therefore does not refute the scoped periodic statement. | ATTEMPTED |
| fixed global lapse/strain | Remove constant metric variations from the variational domain; this can close (23), but it is a declared constrained ensemble rather than the bare periodic equation. The Regge note explicitly identifies constant metric zero modes at `k=0`. | ATTEMPTED |
| metric-transverse source projection | Project the source before solving; this yields (10), but the projection is visible and nonlocal in Fourier space, so it does not make the unprojected local edge source exact. | ATTEMPTED |
| exact wrapping surface | Use a planar wrapping worldvolume; it annihilates every sampled Regge null mode exactly, proving that the carrier can accept some matter surfaces but not repairing the localized bag. | ATTEMPTED |
| local improvement or alternate triangulation | Add bending/corner terms, average frame sectors, or select another local edge representative to cancel (21)--(22); no exhaustive improvement classification is attempted, so this route remains live and the claim is not universal. Block 11 explicitly keeps other improvements and Regge/edge actions live. | ATTEMPTED |
| dynamical matter history | Vary the worldvolume history jointly so its equation supplies force balance; the present static binary tube has no such update. Block 11 identifies local conservation as on shell, and the current axioms state that Admissibility is not dynamics. | ATTEMPTED |
| lifted non-metric branch / nonlinear geometry | Add a higher-order or alternative geometry action that lifts the fifth Regge zero branch; the supplied quadratic note leaves that branch's higher-order behavior open, so this changes the geometry law rather than contradicting (22). | RULED OUT BY PRIOR as a premise of the current quadratic surface; live as a completion |
| compensating background source | Add a cosmological/background counterstress with zero total compact source; this can close (23) but is not present in the bare bag action and requires a separately licensed action representative. | ATTEMPTED |

There are more than five materially distinct routes. Several are viable under
changed premises. Therefore a framework-wide or permanent no-go would fail N1;
only the displayed bare-model statement passes.

### N2 — wall-independence audit

The collapsed open-condition set is:

- `W1`: physical history/worldvolume/action-family and pressure selection;
- `W2`: exact localized finite-lattice joint conservation and edge-carrier
  compatibility;
- `W3`: geometry action orientation, normalization, coupling, and nonlinear
  completion; and
- `W4`: infrared boundary/global-zero-mode ensemble.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| `W1,W2` | no; selecting a family does not prove its Ward/null equations | no; a mathematical conserved source need not be physically selected | yes |
| `W1,W3` | no; matter-family selection does not choose the geometry law | no; a Regge law does not select the matter history/action | yes |
| `W1,W4` | no; action selection does not choose compact/open constraints | no; a boundary choice does not select matter | yes |
| `W2,W3` | no; source conservation does not fix sign/coupling/nonlinear geometry | no; a geometry law alone does not put a supplied static source on shell | yes |
| `W2,W4` | no; nonzero-mode conservation does not remove `k=0` | no; zero-mode handling does not repair mixed-mode residuals | yes |
| `W3,W4` | no; local action normalization does not choose the global ensemble | no; boundary data do not fix action orientation/coupling | yes |

No raw wall follows automatically from another, and no extra “mass identity”
wall is counted separately: physical mass typing is included in `W1` and its
normalization/coupling in `W3`.

### N3 — hidden-condition scan

The source was scanned for `we assume`, `by construction`, `as is standard`,
`the framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit class | Classification |
|---|---|
| flat background / identity source | explicit theorem domain, not a hidden physical premise |
| supplied or registered tick, geometry, action, and boundary | explicit `W1`, `W3`, or `W4` condition |
| canonical axiom wording | governance statement bound to the current axiom memo; no scientific step follows from the label |
| standard Fourier/Green terminology | non-load-bearing name; the regulated transform is derived in-runner |
| Kuhn/Coxeter construction | explicit supplied Regge dependency, not asserted as axiom-selected |

No hidden condition was promoted after the scan; the four-wall count remains
unchanged.

### N4 — residual matching

| Witness | Witness residual | Block-12 residual | Match? |
|---|---|---|---|
| `ADMISSIBILITY_CODE_SWAP_...2026-08-10.md:496-502` | temporal extrusion, field equation, coupling, realized history open | equations (1)--(2) close only extrusion; `W1-W3` preserve the rest | yes |
| `ADMISSIBILITY_CUT_SURFACE_...2026-08-10.md:483-488` | action-representative selection, geometry dynamics, field equation/coupling | `W1-W3` | yes |
| `ADMISSIBILITY_CUT_SURFACE_...2026-08-10.md:572-575` | source calibration, action selection, full local index-shifting Noether bridge | `W1-W3`, especially (21) | yes |
| `CUBIC_COXETER_REGGE_3PLUS1_...2026-06-09.md:97-101` | edge/action selection, orientation, nonlinear completion | `W3` | yes |
| `CUBIC_COXETER_REGGE_3PLUS1_...2026-06-09.md:110-116` | extra zero branch beyond quadratic order and supplied metric map | (22) and carrier part of `W2` | yes |
| `PHYSICAL_DYNAMICAL_METRIC_SOURCE_...CYCLE576...md:213-215` | deficit Ward is not a matter Noether derivation | localized worldvolume Ward residual (21) | yes, as a boundary only |
| `GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE...md:58-71` | scalar core and normalization convention | localized Regge Ward/null residual | no; dropped as witness and retained only as contrast |

No mismatched Gate-B or older scalar-surrogate result is used to support the
finite-lattice claim.

### N5 — rhetoric audit

| Resolution | Executed statement | Scope not claimed |
|---|---|---|
| per element | exact tetrahedron/four-simplex volume derivative | no arbitrary curved simplex family |
| per site | one unit spatial cell tube and its affine strains | no arbitrary-size or arbitrary-shape equilibrium |
| per mode | twelve plane modes plus a generic mixed shrinking sequence | no exhaustive classification of every momentum/source stencil |
| per block | worldvolume -> pressure -> Regge metric projection -> Green tail | no selected physical theory or nonlinear completion |
| lattice wide | actual finite periodic `k=0` null projection | no open/infinite-boundary obstruction |

The primary cached stdout carries one substantive certificate line for each of
these five resolutions. Phrases such as “not an exact finite-lattice dust
solution” refer only to the bare fixed-Kuhn localized bag. No statement says
that a lapse monopole is not a framework fact at every resolution.

### N6 — partial-closure path scan

| Existing path | Status | What it could close |
|---|---|---|
| source-coupled local-action candidate | existing `open_gate`, not a new axiom | could house the derivative convention in `W1` downstream |
| Block-11 Level-A model convention | existing bounded construction | allows the worldvolume family to remain model content without foundation edits |
| approved kinetic-isotropy primitive | registered premise, not a wall | already supplies equal-form tick graining only |
| actual Regge second variation | supplied bounded theorem | supplies a concrete conditional `W3` action/Hessian but not its physical selection/sign |
| open/infinite Green problem | executed here | closes the periodic part of `W4` for the weak-field shape |
| owner choice of fixed-volume/background ensemble | unadopted convention route | could close compact `W4` without new local physics |

It would be incorrect to say “a new axiom is required.” The amendment in
Section 6 is a sufficient route for foundation-level autonomy, while
downstream conventions and import-retirement audits remain legitimate.

### N7 — steelman

A hostile reviewer should argue that the negative result is mostly a choice of
discretization: the same calculation already finds an exactly compatible
wrapping plane, the localized residuals vanish as `k^3` and `k^2`, the metric
sector has the correct monopole, and an improved corner/bending stencil or a
dynamical worldvolume could cancel the residuals. Moreover, the open-boundary
problem removes the compact zero mode and immediately yields `1/r`. This is a
strong, mathematically actionable objection to any broad no-go. It does not
contradict the narrow statement that the **unmodified fixed-Kuhn static bag on
the bare periodic quadratic Hessian** has the explicitly computed residuals.
The steelman is therefore adopted as the next construction target, and the
claim remains narrowed.

### N8 — cross-cycle echo

| Similar prior wall | Later mechanism / current lesson |
|---|---|
| Block 10 named temporal worldvolume extrusion as open | equations (1)--(2) retire that mathematical existence wall without axiom adoption |
| earlier matter-Hessian GR routes left the geometric route open | the actual Regge second-variation theorem later supplied the geometric operator; this block uses that same route rather than declaring GR impossible |
| P1/source-response was once phrased as an axiom-style admission | the existing source-coupled local-action candidate reframed it as a downstream convention; `W1` is likewise not automatically a new axiom |
| AC-phi labeling walls were later separated into derivation versus import-retirement paths | Section 6 keeps convention/adoption and new physics distinct rather than calling every selection issue axiomatic |
| prior action-form no-go packets were narrowed after alternative diffusion/action routes appeared | this packet likewise states a current-action residual with live improvement and action-selection routes |

The mechanisms that retired similar walls—explicit construction, downstream
convention, alternate geometry action, and boundary choice—are all considered
here. None is silently foreclosed.

**Gate status:** PASS for the narrowed bare finite-periodic fixed-Kuhn
statement; FAIL for any universal no-route, no-monopole, or “new axiom
required” reading.

## 10. Verification

Run:

    python3 scripts/admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py

The runner checks:

- current-axiom, Block-11, tick-primitive, and actual-Regge source boundaries;
- exact rational Kuhn tetrahedron and four-simplex volume derivatives;
- diagonal-edge cancellation and homogeneous coframe/metric matching;
- static worldvolume reduction and integrated tick source;
- unique affine pressure `p_*=4tau`, active wrong-pressure control, flat-law
  preservation, and code/pressure covariance;
- plane gauge/extra-null compatibility and actual edge-equation residuals;
- centered bag metric-source `O(k^2)`, gauge `O(k^3)`, and extra-null `O(k^2)`
  exponents;
- metric-transverse actual-Regge solve and four-direction lapse-pole limit;
- regulated `1/r` Green tail and bare periodic `k=0` incompatibility;
- N1--N8 and five-resolution execution-certificate surfaces; and
- canonical-axiom nonmutation and fixed-percentage boundaries.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The strongest honest chain is now

    compatible spatial cut
      -> explicit 3+1 worldvolume
      -> derived tick/lapse face source
      -> affine-pressure unit bag
      -> tick-only leading metric source
      -> actual Regge 1/k^2 response
      -> open-boundary 1/r monopole shape.

This is the first direct route in the campaign from the cut action to a lapse
monopole on the actual geometric operator. The exact plane family shows that
matter-source/Regge compatibility is attainable. The localized source still
has named `O(k^3)`, `O(k^2)`, and periodic-zero-mode residuals, so exact local
finite-lattice gravity is not claimed.

No history law, physical action, pressure mechanism, mass identity, coupling,
sign, Lorentzian continuation, nonlinear equation, or infrared ensemble is
selected. No canonical axiom is edited. No universal no-go is claimed. The
fixed TOE percentages do not move.
