---
claim_id: admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "For the supplied linear symmetric spatial tensor on Z3, the local Hamiltonian H=1/2 p^T p+1/2 h^T L_s h admits a staggered symplectic-Euler kick-drift factorization. One unit macro interval divided into N equal integer substeps is full-Brillouin-zone stable, with positive shadow energy on every nonzero mode, iff N>=2; N=1 is unstable at the cubic UV corner. N=2 is therefore the exact minimal equal-step depth. Its four algebraic Gaussian shears admit a fourteen-layer disjoint local-gate schedule; they are translation/proper-cubic covariant, strictly radius two per macro tick, preserve an exact positive local shadow energy, have physical group-speed norm at most one, and preserve the four trace/divergence constraints and exactly two TT coordinates. A Block-52 conserved null Record-frontier transition composes as one macro event split into equal substep source kicks while preserving the sourced constraint rows and remaining inside the radius-two cone. Depths 2,3,4,8 share the same static law and unit OS0 speed but have distinct finite-lattice energies, so causal feasibility does not select the depth, splitting order, event placement, or nonlinear law. This is a conditional linear causal candidate and minimality theorem within equal symplectic-Euler subcycling, not a unique update, radius-one QCA classification, massive/accelerated source, nonlinear gravity, axiom amendment, or TOE closure."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_bounded_theorem_note_2026-08-11
  - admissibility_canonical_two_tt_positive_transfer_record_source_continuity_lstar_boundary_bounded_theorem_note_2026-08-11
  - admissibility_record_worldline_conserved_stress_two_tt_lorentzian_cfl_locality_lstar_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py
---

# Two-TT Split-Step / Conserved-Record Causal Macro Update Boundary

**Date:** 2026-08-11

**Type:** `bounded_theorem`

**Role:** attack Block 52's explicit unit-tick stability/locality boundary with
the strongest live constructive route: a finite-depth local symplectic macro
update carrying the conserved Record frontier.

**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py](../scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py)

## Result Up Front

A stable finite-depth causal two-TT update exists. Block 52's tradeoff applied
to one direct recurrence, not to all local macro updates.

## Exact Target And Obligation Graph

**Exact target proved here:** within the supplied linear symmetric-tensor
Hamiltonian and the class of equal integer symplectic-Euler subcycles, prove
that two is the smallest substep count giving a full-zone stable finite-radius
macro update with positive shadow energy on every nonzero mode, exact two-TT
constraint preservation, unit physical group cone, and a composable conserved
straight Record-frontier source.

| obligation | status in this block |
|---|---|
| nearest-neighbor proper-cubic spatial symbol and unit OS0 normalization | supplied by the declared Hamiltonian and cited kinetic primitive |
| exact symplectic factorization and positive shadow form | proved here mode by mode and on the complete finite carrier |
| minimal equal integer substep count | proved here from the exact zone maximum `lambda=12` |
| four constraints and exactly two TT coordinates | proved here on every nonzero declared `L=9` mode |
| strict circuit cone and physical group cone | proved here by finite-carrier support and the analytic Cauchy bound |
| conserved straight Record-frontier current | cited from Block 52; its split source composition is proved here |
| unique physical update, event clock, and nonlinear completion | open and not part of the target |

The zero spatial mode has the expected semidefinite free-particle shadow form,
not strict positive energy. Odd finite tori do not admit the particular
axis-parity edge coloring used to count disjoint gates, although the algebraic
commuting kick and its finite-radius formula remain defined. Curved geometry,
accelerated or massive sources, arbitrary Record branching, boundaries, and
nonlinear constraint closure are outside the proved domain. The strongest
missing lemma is a derivation or uniqueness theorem selecting one exact joint
update and Record clock from the current axioms (or, failing that, an explicit
owner-approved extensional `L*` amendment).

Start from the local linear Hamiltonian

~~~text
H(h,p) = (1/2) p^T p + (1/2) h^T L_s h,                  (1)
~~~

where `L_s` is the nearest-neighbor cubic Laplacian. Split one unit macro
interval into `N` equal substeps `delta=1/N`. On each substep apply

~~~text
kick:   p <- p-delta L_s h,
drift:  h <- h+delta p.                                   (2)
~~~

The kick is a product of **commuting nearest-neighbor kick** gates because all
terms depend only on the mutually commuting `h` coordinates. The drift is an
**onsite drift**. Each is an exact symplectic Gaussian shear.

At a spatial mode with Laplacian eigenvalue `lambda=kappa^2`, one substep is

~~~text
M_(delta,lambda)
 = [[1-delta^2 lambda, delta],[-delta lambda,1]],
det M = 1.                                                (3)
~~~

It preserves the exact shadow form

~~~text
Q_(delta,lambda)
 = [[lambda,-delta lambda/2],[-delta lambda/2,1]],         (4)
~~~

whose determinant is `lambda(1-delta^2 lambda/4)`. Therefore every nonzero
mode has positive energy and unit-circle roots iff

~~~text
delta^2 lambda < 4.                                      (5)
~~~

The cubic zone has `lambda<=12`. For equal integer subcycling, (5) becomes

~~~text
12/N^2 < 4,        hence N>=2.                            (6)
~~~

Depth one is UV unstable. Depth two is strictly stable and is the exact
**minimal integer depth is two** result within this equal symplectic-Euler
class. No fitted parameter or excluded high-momentum sector is used.

One depth-two macro update contains four algebraic shear factors,

~~~text
kick(delta=1/2), drift(1/2), kick(1/2), drift(1/2).        (7)
~~~

Because each kick has spatial radius one and each drift zero, the macro matrix
has strict spatial radius two. On the complete `L=5` phase-space carrier its
entries vanish exactly beyond graph distance two. For a conventional circuit
schedule in which gates in one layer have disjoint supports, color the cubic
edges by axis and base-coordinate parity. The six colors are matchings; hence
each kick takes six edge-gate layers and each drift one onsite layer. Equation
(7) is therefore **fourteen disjoint local-gate layers**, not an artificially
declared depth-four overlapping-gate circuit. It is still finite depth,
unlike Block 52's dense implicit inverse and unlike the quasilocal continuous
time-one exponential.

The macro frequency is

~~~text
E_N(k) = N arccos[1-kappa^2/(2N^2)].                      (8)
~~~

It has `E_N=kappa+O(kappa^3/N^2)`, so the leading OS0 speed is one. Its group
velocity satisfies

~~~text
|v_g|^2
 = sum_i sin^2(k_i) /
   {N^2 [kappa^2/N^2][1-kappa^2/(4N^2)]}
 <= 1,                                                    (9)
~~~

where the last step is the **Cauchy inequality**
`(sum s_i)^2<=N^2 sum s_i^2` for `s_i=sin^2(k_i/2)` and `N>=sqrt(3)`.
Thus the physical group cone stays inside one spatial edge per unit macro
time, even though the strict circuit support is radius two.

The same scalar shear acts on all six symmetric spatial tensor coordinates.
Trace plus three lattice-divergence constraints commute with `L_s`, so if both
`h` and staggered `p` obey them, every layer preserves them. On every nonzero
`L=9` momentum the constraint rank is four and the state has exactly two TT
coordinates.

Block 52's conserved Record source also composes. Let one Record path extend
across one edge during the macro interval. Its frontier increment and flux
obey

~~~text
Delta J + div S = 0.                                     (10)
~~~

Insert its Lorentz-null spatial stress as a local momentum kick. Evolve the
four contracted row values with the same kick/drift formulas; they agree
exactly with applying the rows after each physical update. The source also has
a nonzero TT projection. On `L=5` the full response to one endpoint kick stays
within the radius-two macro cone. This supplies one coherent reading:

~~~text
two unrecorded internal substeps per unit macro interval,
one Record event per macro tick.                           (11)
~~~

Equation (11) is a candidate clock convention, not a derivation. Stable
members remain distinct:

~~~text
E_2(0.4)=0.397995029,
E_3(0.4)=0.397629658,
E_4(0.4)=0.397502205,
E_8(0.4)=0.397379513.                                    (12)
~~~

**Depth two and depth three** share locality, positive energy, static response,
proper-cubic covariance, exactly two TT modes, unit OS0 speed, and group cone,
but differ physically at finite momentum. The **current axioms do not select**
the depth, kick/drift ordering, source-kick placement, macro-to-Record event
relation, or nonlinear completion.

This block therefore closes causal feasibility but earns **zero TOE percentage
points**. The next genuine closure step is no longer “make gravity propagate.”
It is select one exact joint update, derive its selection if possible, and
extend it to nonlinear geometry and general conserved matter. No canonical
axiom is edited.

## Inputs And Non-Imports

| input | used here | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | spatial `Z^3`, nearest-neighbor adjacency, proper cubic covariance, Records and explicit dynamics boundary | Hamiltonian, canonical momentum, update layers, clock, source, or Record event rate |
| [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | the leading unit space-time kinetic form | substep depth, ordering, shadow energy, exact dispersion, or event cadence |
| [Block 46 joint-law cut](ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the exact instrument/clock/constraint/source law target | a selected `L*` |
| [Block 51 two-TT transfer](ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the symmetric-tensor quotient, static kernel, positive-state target, and source-continuity repair | this split update or a claim that `r` is physical |
| [Block 52 Record worldline/CFL boundary](ADMISSIBILITY_RECORD_WORLDLINE_CONSERVED_STRESS_TWO_TT_LORENTZIAN_CFL_LOCALITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the straight incoming-pointer Record path, conserved Lorentz-null stress, signature-aware source, and family-scoped causal cut | subcycling, event placement, massive/accelerated stress, or nonlinear connection |

The linear Hamiltonian, canonical momentum, equal substeps, kick-first order,
finite carriers, straight null source, macro-event placement, and shadow-energy
reading are supplied mathematical structures. No observation, fit, arbitrary
realized history, nonlinear action, gauge-fixed graviton quantization, massive
matter, audit verdict, `review-loop` result, or axiom amendment is imported.

## 1. Local Symplectic Factorization

Write

~~~text
K_delta = [[I,0],[-delta L_s,I]],
D_delta = [[I,delta I],[0,I]],
M_delta = D_delta K_delta.                                (13)
~~~

Both factors preserve the canonical symplectic form exactly. In real space,
`K_delta` reads only the site and its six nearest neighbors; `D_delta` reads
only the same site. The product `M_delta^N` therefore has radius at most `N`.
For `N=2`, the `L_s^2` term is nonzero at distance two, so the radius is
exactly two.

No checkerboard edge coloring is required for the linear kick: the elementary
potentials are functions of the commuting configuration variables. A quantum
Gaussian implementation uses commuting phase gates for all spatial edges,
then onsite Fourier/shear gates for the drift.

Equation (4) follows by direct multiplication

~~~text
M_delta^T Q_delta M_delta = Q_delta.                      (14)
~~~

It is local as a quadratic form:
`p^T p + h^T L_s h-delta h^T L_s p`. Positivity is precisely (5). The zero
spatial mode remains a free homogeneous mode and has semidefinite energy, as
expected; no zero-mode boundary state is inferred.

## 2. Minimal Equal-Step Depth And Physical Cone

At `N=1`, the corner `k=(pi,pi,pi)` has `lambda=12`; equation (3) has a real
reciprocal eigenvalue pair with spectral radius greater than one and (4) is
indefinite. At `N=2`, the corner has `delta^2 lambda=3`, strictly below four.
Every larger integer depth is also stable. This proves (6) for the whole zone,
while the runner evaluates all `4,913` grid momenta at depths one through six.

For the group cone, put `s_i=sin^2(k_i/2)`, so `kappa^2=4 sum s_i` and
`sin^2 k_i=4s_i(1-s_i)`. Differentiating (8) gives

~~~text
|v_g|^2
 = [sum s_i(1-s_i)]/[sum s_i (1-sum s_i/N^2)].            (15)
~~~

The inequality `|v_g|^2<=1` reduces to

~~~text
(sum_i s_i)^2 <= N^2 sum_i s_i^2,                         (16)
~~~

which follows from Cauchy and `N^2>=3`. The limit at zero momentum is one, so
the bound is sharp. Circuit support radius and physical group velocity are
different useful causal notions; both are reported.

## 3. Exact Two-TT And Sourced-Constraint Update

Let `C(k)` contain the trace row and three divergence rows. Since
`L_s(k)=kappa^2 I_6`,

~~~text
C p' = C p-delta kappa^2 C h+delta C f,
C h' = C h+delta C p'.                                   (17)
~~~

Thus the **sourced constraint state** evolves under exactly the same two-by-two
shear as the physical tensor, with force rows `C f`. Applying (17) twice gives
the macro update. The runner starts off constraint as a hostile control and
checks that the separately propagated rows agree with recomputation from all
six components; it does not merely initialize the residuals to zero.

On the homogeneous source-free fiber, `rank C=4` at every nonzero declared
mode, leaving two TT positions and two TT momenta. The local Lorentz-null
stress force projects nontrivially onto that quotient at generic momentum, so
the same event affects both the constraint and radiative sectors.

Equation (17) is the linear contracted Bianchi intertwiner. It is not a
nonlinear discrete diffeomorphism theorem or proof that the shadow energy is
the selected physical gravity Hamiltonian.

## 4. Record Event Composition

The incoming-pointer path source distinguishes persistent state from an event:
the frontier exists throughout the macro interval; extension is the transition
recorded at its end. A source kick may be placed at the first substep, second
substep, or symmetrically split. All three preserve (10) when the same
transition current is used; their finite-momentum responses differ.

The runner chooses equal half-kicks, one in each substep, and one registered
Record extension at the macro boundary. Its source image stays within the
same radius-two circuit cone. This realizes the interface but does not select
the placement convention.

The construction is straight and null. A bend changes the stress direction
and needs an interaction impulse; a massive path requires a rest/move cadence
and timelike normalization; pair creation requires a neutral branching
instrument. Those are the next source extensions, not assumptions hidden here.

## 5. Finite-Depth Fork And Exact `L*` Boundary

Equation (12) proves that consistency plus the leading kinetic primitive does
not select `N`. A proposed **minimal-depth principle** would choose `N=2`, but
that principle is new dynamical content unless derived from the existing
nearest-neighbor law. Likewise time reversal may prefer a symmetric Verlet
order, circuit architecture may prefer directional layers, and Record
semantics may choose a source placement.

The exact joint-law candidate now has a finite explicit referent:

~~~text
state:       permanent incoming-pointer Records, active frontier,
             (h_ij,p_ij) with four sourced rows and two TT pairs;
macro law:   N local kick/drift substeps with specified order;
source law:  signature-aware conserved stress kick from Record transition;
clock:       substep duration 1/N and one declared event instrument per macro;
causality:   strict circuit radius N and physical group cone <=1.             (18)
~~~

If retained work derives `N=2`, its ordering and source placement, the
constitutional cut can retire. If not, the honest amendment route is to
**retype Admissibility** around one exact extensional `L*` such as (18), after
owner selection. A sentence saying only “a local causal update exists” would
leave the physical fork intact. No canonical axiom is edited here.

## No-Go Discipline Gate

The narrow negative is now only that the one-substep equal symplectic-Euler
member fails full-zone positive energy. The positive depth-two escape prevents
any gravity or finite-depth causal no-go.

### N1 — Alternative Route Enumeration

| normalized route | attack and outcome | marker |
|---|---|---|
| equal subcycling | Two equal substeps satisfy the exact stability inequality and are constructed in full; this is the positive escape that narrows the negative to depth one. | ATTEMPTED |
| unequal-step formulation | **Unequal substeps** may alter error coefficients and source placement; they are outside the equal-depth minimality proof and remain live. | ATTEMPTED |
| reversible-order formulation | **Time-symmetric Verlet** can improve reversibility and changes the exact shadow form; its stability threshold is compatible with subcycling and remains an alternative law. | ATTEMPTED |
| axis-factorized formulation | **Directional splitting** replaces one cubic kick by axis kicks; they commute in the present linear scalar symbol but differ once nonlinear geometry is included. | ATTEMPTED |
| auxiliary-carrier formulation | A **radius-one QCA** with extra phase registers may achieve strict radius one per macro step; it is not classified or excluded. | ATTEMPTED |
| implicit-equation formulation | The Block-52 stable **implicit action** remains valid under action-local causality and need not use this circuit. | RULED OUT BY PRIOR |
| continuous-generator formulation | The Block-52 **continuous-time generator** remains finite range and positive; it uses asynchronous events and a quasilocal time-one map rather than a finite-depth macro circuit. | RULED OUT BY PRIOR |

The routes differ by substep weights, reversible composition, spatial
factorization, state carrier, implicit equation, and continuous generator.

### N2 — Wall-Independence Audit

After the causal feasibility repair, the remaining joint-law conditions are:

- `W_S`: select depth/order/source placement and the Record event clock;
- `W_M`: extend the straight null source to general conserved matter;
- `W_N`: extend the linear constraint/TT circuit to nonlinear geometry and an
  increasing-region physical phase.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `W_S`, `W_M` | no | no | yes |
| `W_S`, `W_N` | no | no | yes |
| `W_M`, `W_N` | no | no | yes |

Positivity, finite causal radius, two TT modes, and linear sourced-row
propagation are no longer counted as walls.

### N3 — Hidden-Wall Scan

The supplied canonical tensor/momentum, flat spatial Laplacian, linearity,
equal substeps, kick-first ordering, zero-mode exclusion from strict
positivity, finite carriers, straight null source, macro event placement, and
shadow-energy interpretation are explicit. “Canonical” describes phase-space
coordinates, not foundation status. No background reservoir, unnamed bridge,
standard-QFT premise, or assertion that the framework provides the
Hamiltonian/circuit is load bearing.

### N4 — Residual Matching

| witness | witness residual | residual used here | match? |
|---|---|---|---:|
| Block 46 | exact joint instrument/clock/constraint/source law unselected | equation (18) gives a concrete finite-depth candidate but not selection | yes |
| Block 51 | positive two-TT state/transfer feasible; finite law and source decoder open | reuse the same two-TT/static contract under a different causal construction | yes |
| Block 52 | direct unit-tick family cannot meet full-zone stability plus explicit finite radius; splitting/QCA remains live | construct the named split-step counterroute and retain QCA alternatives | yes |

The Block-50 OS obstruction is not cited against this independent canonical
circuit.

### N5 — Rhetoric And Resolution Audit

“Minimal” always means the smallest **integer number of equal symplectic-Euler
substeps** satisfying the full-zone strict positivity inequality; it does not
mean the unique causal law. Per element, all tensor/momentum/source and mode-
matrix entries are checked. Per site, the complete `L=5` phase-space circuit
and support cone are checked. Per mode, all `4,913` full-zone modes and all
`728` TT modes are checked. Per block, layers, energy, minimal depth,
constraints, cones, source, and selection fork are separate. Lattice-wide,
finite-radius translation-covariant formulas extend to `Z^3`; nonlinear
geometry, arbitrary matter/history, and uniqueness do not. The cache lands all
five resolution lines.

### N6 — Partial-Closure And Primitive Scan

The kinetic-isotropy primitive supplies only the leading unit speed, which all
depths share. It does not select depth or event cadence. Equations (4)-(10)
retire causal feasibility, positivity, and source-composition walls without an
axiom edit. A derived minimal-circuit theorem, reversible-order theorem, or
physical hardware/circuit equivalence could retire `W_S` downstream. Therefore
no new-axiom necessity is claimed.

### N7 — Steelman

The strongest hostile response is that the chosen kick-first circuit is merely
one symplectic integrator. A radius-one QCA with auxiliary staggered phase
registers might realize two TT modes, full-zone positivity, exact constraints,
and the same Record current while eliminating the depth-two strict support and
changing dispersion (12). Its terminal obligations are explicit: give the
local cell unitary/symplectic matrix, prove positive physical quotient and
constraint intertwining over the full zone, and identify/eliminate auxiliary
modes. That route would defeat any global minimality claim. Accordingly this
note proves only minimal equal-substep depth and keeps the QCA route live.

### N8 — Cross-Cycle Echo

Block 52 explicitly listed operator splitting and auxiliary QCA as repairs;
this block executes the first rather than repeating the obstruction. Earlier
two-step transfer work sometimes treated blocking depth as merely numerical;
here depth is a physical causal circuit choice with exact energy and cone
certificates. Prior selection walls have been retired by derived minimality
theorems, so the minimal-depth-principle route is preserved for the next block
instead of being labeled axiom necessity.

**Status: PASS.** The depth-one negative and depth-two positive construction
survive N1-N8. Unequal/symmetric/directional splitting, radius-one auxiliary
QCA, implicit action, continuous generators, general matter, nonlinear
geometry, derived selection, and exact joint-law adoption remain live.

## Reproduction

Run from the repository root:

~~~bash
python3 scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py
~~~
