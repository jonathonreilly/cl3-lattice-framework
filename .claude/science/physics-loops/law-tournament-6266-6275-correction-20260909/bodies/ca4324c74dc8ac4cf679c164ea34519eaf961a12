---
claim_id: admissibility_record_worldline_conserved_stress_two_tt_lorentzian_cfl_locality_lstar_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "On a supplied straight self-avoiding Record path in Z3, each new site stores its incoming cubic direction in M2(C). Occupancy minus outgoing degree is a local decoder that cancels every permanent interior Record and leaves one active frontier source. One extension moves that source across one edge and yields a symmetric Lorentz-null rank-one stress whose four columns obey exact discrete continuity. Lorentzian trace reversal gives a nonzero temporal Ricci source for the x+t ray even though the inherited Euclidean trace reversal vanishes. For the Block-51 quadratic two-TT family, the direct unit-tick Lorentz recurrence is UV-unstable for r<1/6, marginal at r=1/6, and positive-energy stable for r>1/6 on the full cubic Brillouin zone. Every stable r>0 member has a dense temporal-block inverse, while r=0 is explicit finite-range but UV-unstable. A continuous-time r=0 local Hamiltonian is positive and stable but its time-one map is quasilocal and Record events need not be one-per-tick. Thus the straight conserved source exists, while current axioms select neither discrete implicit/action locality, continuous generator locality, nor an auxiliary finite-depth causal completion. This is not a no-go for other actions, QCA/splitting constructions, massive or accelerated sources, nonlinear gravity, axiom necessity/adoption, or TOE closure."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_permanent_record_formation_scheduler_lorentzian_time_constraint_selection_axiom_boundary_bounded_theorem_note_2026-08-11
  - admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_bounded_theorem_note_2026-08-11
  - admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_bounded_theorem_note_2026-08-11
  - admissibility_canonical_two_tt_positive_transfer_record_source_continuity_lstar_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_record_worldline_conserved_stress_two_tt_lorentzian_cfl_locality_lstar_boundary_2026_08_11.py
---

# Conserved Record Worldline / Two-TT Lorentzian CFL-Locality Boundary

**Date:** 2026-08-11

**Type:** `bounded_theorem`

**Role:** construct one explicit conserved Record source, then decide whether
the Block-51 positive transfer family also supplies a stable strictly local
Lorentzian one-tick update.

**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_record_worldline_conserved_stress_two_tt_lorentzian_cfl_locality_lstar_boundary_2026_08_11.py](../scripts/admissibility_record_worldline_conserved_stress_two_tt_lorentzian_cfl_locality_lstar_boundary_2026_08_11.py)

## Result Up Front

The Block-51 source-continuity repair can be realized by permanent Records,
but the repaired source exposes a separate causal-transfer decision.

First, a monotone Record history can encode **transport rather than charge
creation**. Supply an origin `x_0` and one cubic direction
`e in {+/-e_x,+/-e_y,+/-e_z}` as realized-state data. At step `n`, let

~~~text
x_m = x_0 + m e,
R_n = {x_0,...,x_n}.                                      (1)
~~~

The root uses the algebraic unit of `M_2(C)`. Every later site is an
**incoming-pointer Record** with content `-e.sigma`, pointing to its parent.
The six contents are Hermitian traceless involutions and transform as one
proper-cubic orbit. Every prefix is self-avoiding on `Z^3`, Records are only
added, and no site has more than one Record.

Define the source decoder locally by

~~~text
J_n(x) = 1_[x in R_n] - outgoing_degree_Rn(x).             (2)
~~~

For the path (1), **occupancy minus outgoing degree** cancels every old
interior Record and leaves

~~~text
J_n(x) = delta_(x,x_n).                                   (3)
~~~

When the path extends across `x_n -> x_(n+1)`, put unit flux `S_n` on that
edge. With the runner's incidence convention,

~~~text
Delta J_n + div S_n = 0.                                  (4)
~~~

Thus cumulative Record number grows while active source number stays one.
Record permanence and source conservation are compatible once the source is a
boundary/frontier functional of the Record history rather than its raw count.

The same path carries an exactly conserved stress. Put

~~~text
k^mu = (1,e),
T^(mu nu) = rho k^mu k^nu,
rho = 1/(2 sqrt(2)).                                      (5)
~~~

At each step `T^(0 nu)` is supported at the frontier and `T^(i nu)` is the
corresponding edge flux. Equation (4) then holds for all four `nu`. The tensor
is symmetric, rank one, and null under `eta=diag(-1,1,1,1)`. Updating each
contracted connection flux by minus the stress flux preserves the **four
contracted constraints** exactly. At a generic spatial momentum the spatial
stress also has a nonzero projection onto the exact two-dimensional TT
quotient, so it can drive radiation rather than only a constraint field.

This corrects an important signature ambiguity. For the same `x+t` ray, the
Block-49 Euclidean trace reversal gives

~~~text
T_00 - (1/2) delta_00 Tr_E(T) = rho-rho = 0,               (6)
~~~

whereas Lorentzian null stress has `Tr_eta(T)=0` and hence

~~~text
T_00 - (1/2) eta_00 Tr_eta(T) = rho.                       (7)
~~~

Block 49 was explicit that its source map was Euclidean and conditional, so
(7) does not contradict it. It proves that the Lorentzian joint law needs a
**signature-aware source decoder**; the Euclidean diagonal value cannot be
carried unchanged into physical source semantics.

Second, positivity is not yet causality. For the Block-51 action family, write

~~~text
A_r(k) = 1+r kappa^2,
kappa^2 = sum_i 4 sin^2(k_i/2).                            (8)
~~~

The direct unit-tick Lorentz equation is

~~~text
A_r (h_(n+1)-2h_n+h_(n-1)) + L_s h_n = 0.                 (9)
~~~

A mode `exp(-i omega n)` obeys

~~~text
4 sin^2(omega/2) = lambda_r(k),
lambda_r(k) = kappa^2/(1+r kappa^2).                       (10)
~~~

The cubic Brillouin zone has `0<=kappa^2<=12`. Consequently:

~~~text
r < 1/6:  some lambda_r > 4, so omega is not real;
r = 1/6:  lambda_r=4 at the corner, a double -1 root with
          only semidefinite mode energy;
r > 1/6:  0<lambda_r<4 at every nonzero mode, giving a
          positive conserved mode energy and unit-circle roots.             (11)
~~~

But solving (9) explicitly for the next slice uses

~~~text
h_(n+1) = 2h_n-h_(n-1) - (I+rL_s)^-1 L_s h_n.             (12)
~~~

For `r>0`, on a connected periodic cubic carrier,

~~~text
(I+rL_s)^-1
 = [1/(1+6r)] sum_(m>=0) [r Adj/(1+6r)]^m.                (13)
~~~

Every pair of sites is joined by some walk, so every inverse entry is
strictly positive. Equivalently, the nonconstant symbol has no
**finite-range Laurent inverse**. Thus the stable members `r>1/6` are local as
implicit spacetime actions but not finite-radius explicit one-slice maps. The
`r=0` map is explicit nearest-neighbor but fails (11) at high momentum.

This is a scoped locality/stability boundary for family (8), not a gravity
no-go. A clean repair exists if causal evolution is continuous. The local
Hamiltonian

~~~text
H_cont = (1/2) p^T p + (1/2) h^T L_s h                  (14)
~~~

has positive energy, stable frequencies `omega=kappa`, and a finite-range
generator. Its exact time-one map has quasilocal tails from the exponential
series, not strict finite radius. Under that reading, Record formation is an
event instrument superposed on continuous evolution: **asynchronous Record
events** need not occur once per time unit, and a stationary source can persist
without continually creating Records.

The exact constitutional decision is therefore among at least three live
causal meanings:

1. **implicit action-local** discrete time with `r>1/6`;
2. **continuous generator-local** evolution with a quasilocal time-one map;
3. an **auxiliary finite-depth circuit** or QCA whose extra state/substeps
   achieve exact finite-radius unitary evolution.

Current axioms and the kinetic-isotropy primitive select none. The straight
worldline solves one source obstruction, but no canonical axiom is edited.
This block earns **zero TOE percentage points** because no causal joint law is
adopted.

## Inputs And Non-Imports

| input | used here | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | `Z^3`, proper cubic covariance, `M_2(C)`, permanent one-per-site Records, and the explicit dynamics boundary | a clock, Hamiltonian, formation site/rate, source, stress, or geometry update |
| [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | the leading unit space-time kinetic ratio | discrete leapfrog stability, a transfer coefficient, strict microcausality, or event cadence |
| [Block 45 Record/time boundary](ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | monotone formation and the unresolved Record-clock map | the straight path, rate, or source current |
| [Block 46 joint-law cut](ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the extensional Record-instrument/clock/source target | a selected `L*` |
| [Block 49 curvature/source boundary](ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the Euclidean `x+t` value in (6) and exact Ricci/trace-free split | a Lorentzian continuation of the source decoder |
| [Block 51 positive transfer/continuity boundary](ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the family (8), two-TT quotient, positivity, and transition-current target | the direct Lorentz recurrence, causal semantics, or selected `r` |

The origin, direction, straight self-avoiding domain, pointer code, null
normalization, source/stress identification, flat linear constraint field,
quadratic action family, finite carriers, and causal comparator definitions
are supplied mathematical structures. No observed constant, empirical fit,
arbitrary realized history, massive source, acceleration force, nonlinear
geometry, audit verdict, `review-loop` result, or axiom amendment is imported.

## 1. Permanent Path Records And A Local Active Source

The root content is the central unit, distinguished by the supplied algebraic
structure rather than by a spatial frame. A nonroot content is

~~~text
c_e = -e_x sigma_x-e_y sigma_y-e_z sigma_z,
c_e^dagger=c_e,    c_e^2=I,    Tr c_e=0.                  (15)
~~~

Signed axis permutations of determinant `+1` act on the Bloch vector and
carry (15) into the same six-element orbit. Translations move the whole path.
No origin or direction is selected by the law-shaped construction: both are
realized initial data. The runner exhausts all 24 proper frames, six
directions, and prefix lengths zero through six.

The parent of a nonroot site is recovered from its content. Its outgoing
degree is therefore a nearest-neighbor function of the Record configuration.
For a simple path, every old vertex except the frontier has one child. Equation
(2) is consequently exact at every prefix, including the one-Record initial
state.

This decoder is not the Record axiom's additive scalar readout. It is a new
candidate physical source functional on a supplied path domain. That type
separation is essential: finite additive readout counts permanent evidence;
the conserved source identifies the active boundary of that evidence.

## 2. Four-Column Stress Continuity And The Source Signature

Let the edge incidence column have `+1` at its source and `-1` at its target.
One extension has

~~~text
Delta J = delta_target-delta_source,
div S   = delta_source-delta_target.                       (16)
~~~

Multiplying both terms by `rho k^nu` proves the four identities

~~~text
Delta T^(0 nu) + div T^(i nu) = 0,     nu=0,1,2,3.         (17)
~~~

Because the spatial flux direction is `e_i`, the combined tensor is exactly
`rho k^mu k^nu`; symmetry is not imposed after the fact. If `E_(i nu)` denotes
the four contracted connection/constraint fluxes, then

~~~text
div E_n = T_n^(0 nu),
E_(n+1) = E_n - T_n^(i nu)                                (18)
~~~

preserves all four equations by (17). This is the discrete Bianchi/Gauss
intertwiner at the contracted linearized level.

It is not yet a complete nonlinear Einstein update. In particular, bends in
the path change `k` and require a compensating impulse/stress exchange; a
massive path requires a timelike cadence rather than one axis displacement per
unit tick; and the absolute flat periodic constraint requires a compatible
zero mode or boundary geometry. Those are explicit remaining obligations.

For the spatial tensor quotient at generic momentum, the TT projector of
`rho e_i e_j` is nonzero. The source can therefore be paired with the Block-51
two-mode oscillator while (18) carries the four constraint components. A full
same-field symplectic reduction and nonlinear connection remain open.

## 3. Exact Discrete Stability Threshold

For state `(h_n,h_(n-1))`, equation (9) has transfer matrix

~~~text
M_lambda = [[2-lambda,-1],[1,0]],       det M_lambda=1.    (19)
~~~

It preserves

~~~text
Q_lambda = [[1,-(2-lambda)/2],[-(2-lambda)/2,1]].          (20)
~~~

The eigenvalues of (20) are `1 +/- |2-lambda|/2`; both are positive exactly
when `0<lambda<4`. At `lambda=4`, (20) has a zero eigenvalue and (19) has a
double `-1` root with a linearly growing generalized solution. Real frequency
at the corner is therefore only marginal, not a positive-energy full-zone
closure.

Since `lambda_r` increases monotonically with `kappa^2`, its maximum is

~~~text
lambda_max(r) = 12/(1+12r).                               (21)
~~~

Equations (20)-(21) prove (11) without relying on a grid. The runner also
checks all `4,913` points of a full-zone grid, including every corner, for
`r=0,1/12,1/6,1/4,1`.

The Euclidean Gaussian/OS transfer stays positive for every `r>=0`; that was
Block 51. Equation (11) is a distinct direct-Lorentzian stability condition.
One may choose OS reconstruction instead of analytic continuation, but that
choice is itself the physical clock/transfer map the current foundation leaves
open.

## 4. Why The Stable Discrete Update Is Not Explicitly Local

On an `L^3` periodic carrier,

~~~text
L_s = 6I-Adj,
A_r = (1+6r)I-r Adj.                                      (22)
~~~

The adjacency spectral radius is six, so the series (13) converges for every
`r>0`. Connectedness makes some walk count `(Adj^m)_(xy)` positive for every
pair `x,y`; hence `(A_r^-1)_(xy)>0` at every separation. The runner confirms
this on the complete `L=5` matrices for `r=1/4` and `r=1`, including unit row
sums.

The same statement on `Z^3` follows from the Laurent-polynomial unit test. A
finite-range convolution inverse would make the nonconstant Laurent symbol
`1+r kappa^2(z)` a unit, but the only Laurent-polynomial units are nonzero
monomials. It is not one for `r>0`.

This distinction prevents a word game:

- equation (9) is **local as an implicit spacetime field equation**;
- equation (12) is **not a finite-radius synchronous update**.

Neither notion is automatically “the” causal meaning of the framework. The
joint law must say which is physical and how Record precedence is embedded.

## 5. Continuous-Time Repair And Remaining Choice

Equation (14) is local because `L_s` has only onsite and six-neighbor entries.
For every nonzero mode its time-one map is

~~~text
[h(1)]   [cos kappa       sin(kappa)/kappa] [h(0)]
[p(1)] = [-kappa sin kappa       cos kappa] [p(0)],        (23)
~~~

which preserves the symplectic form and positive energy
`kappa^2 h^2+p^2`. The generator is finite range and has exact unit small-
momentum speed. The exponential series reaches arbitrary graph distance at
finite time with factorial suppression, so (23) is quasilocal rather than a
strict finite-depth circuit.

This is a viable physical reading if causal locality attaches to the generator
and Records are sparse events. It also fixes a conceptual error exposed by
Block 51: a stationary gravitating object need not form one new permanent
Record on every evolution tick. The source persists as state; Records log
selected transitions.

It is not derived here. A different spacetime action, an operator splitting
with substeps, or an auxiliary QCA can potentially give a stable strict circuit
while respecting the leading kinetic ratio. Those constructions remain live
and must be tested before any broader no-go.

## 6. Exact `L*` / Axiom Decision Boundary

The next extensional joint-law candidate must now bind all of the following:

~~~text
state:          (Record configuration, active source, geometry phase space),
Record step:    a monotone extension instrument and precedence rule,
source map:     a signature-aware conserved T^(mu nu)[R,R'],
constraints:    the four-column intertwiner (17)-(18),
radiation:      exactly two positive TT coordinates,
causality:      one selected meaning among action-local, generator-local,
                or finite-depth circuit-local evolution,
clock:          the map between evolution parameter and Record events.       (24)
~~~

The straight path plus continuous Hamiltonian is the most economical current
candidate, but it is not a derived selector and it does not cover massive or
accelerated matter. The current axioms contain no dynamics from which to infer
(24), while the kinetic primitive supplies only the leading graining ratio.

If a downstream theorem constructs and uniquely identifies (24), the axiom
cut retires. Otherwise the honest governance surface is an exact adopted `L*`
referent, not a generic sentence saying “evolution is causal.” No canonical
axiom is edited in this block.

## No-Go Discipline Gate

The only negative is family-scoped: within (8)-(12), a unit-tick member cannot
be both strictly finite-radius as an explicit slice map and positive-energy
stable on the full cubic Brillouin zone. The source result is constructive.
No claim is made against all gravity or all causal lattice updates.

### N1 — Alternative Route Enumeration

| normalized route | attack and outcome | marker |
|---|---|---|
| clock-ratio route | A **smaller time step** with `a_t/a_s<1/sqrt(3)` stabilizes the `r=0` leapfrog; it changes the declared unit graining and therefore remains a live clock/primitive revision rather than a counterexample within the unit-tick scope. | ATTEMPTED |
| band-limited route | An **infrared band restriction** `kappa^2<4` keeps `r=0` real and positive; it closes an EFT sector but not the claimed full-zone transfer. | ATTEMPTED |
| implicit-action route | Choosing `r>1/6` gives stable positive mode energy; equations (13) and (22) prove its explicit slice inverse has all-distance support, so it succeeds only under action-local causality. | ATTEMPTED |
| continuous-generator route | The **continuous-time Hamiltonian** (14) is finite-range, stable, and positive; it defeats a gravity no-go and remains the preferred repair, while its time-one map is quasilocal rather than strict finite depth. | ATTEMPTED |
| split-step route | **Operator splitting** can compose local substeps and may change the CFL polynomial; no exact two-TT Record-faithful construction is supplied here, so this route is explicitly unclosed. | ATTEMPTED |
| auxiliary-circuit route | An **auxiliary QCA** can store staggered fields or substep phases and may realize a stable strict circuit; that changes the state carrier and is the strongest live attack on the family-scoped result. | ATTEMPTED |
| alternate-action route | A **different spacetime action** with additional fields or temporal range may avoid (10); it lies outside family (8) and is not excluded. | ATTEMPTED |

The routes differ in clock ratio, spectral domain, implicit equation, continuous
generator, factorized update, enlarged carrier, and action family. They are not
multiple phrasings of one coefficient change.

### N2 — Wall-Independence Audit

After collapsing downstream consequences, three open conditions remain:

- `W_R`: extend the straight path into a general Record instrument with
  massive/accelerated conserved stress;
- `W_C`: select the clock and causal-locality meaning in (24);
- `W_G`: identify the connection/TT direct sum with one complete nonlinear
  geometry law and coupling.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `W_R`, `W_C` | no | no | yes |
| `W_R`, `W_G` | no | no | yes |
| `W_C`, `W_G` | no | no | yes |

The signature correction and straight four-current close parts of `W_R`; the
three fields above are the collapsed remaining set.

### N3 — Hidden-Wall Scan

The supplied origin/direction, straight path, null velocity, pointer alphabet,
source normalization, flat connection field, TT projection, quadratic family,
unit tick, full Brillouin zone, periodic inverse controls, and three causal
definitions are explicit. “Background” appears only in the excluded-boundary
sense; no reservoir is used. “Canonical” refers only to the prior constrained
phase-space construction. No standard-QFT assertion, unnamed bridge context,
or statement that the framework provides stress, geometry, or a Hamiltonian is
load bearing.

### N4 — Residual Matching

| witness | witness residual | residual used here | match? |
|---|---|---|---:|
| Block 45 | Record formation, scheduler, and Lorentzian clock are unselected | path is one supplied instrument; cadence remains open | yes |
| Block 46 | one exact joint Record/clock/constraint/source law is missing | equation (24) refines that same law object | yes |
| Block 49 | Euclidean contracted source is conditional and `x+t` gives zero | compare exactly that signature-dependent diagonal value | yes |
| Block 51 | positive TT transfer exists but source continuity and selection remain open | construct one conserved source and test the direct Lorentz update of the same family | yes |

No earlier Euclidean Gram obstruction is used as evidence for the CFL or
finite-range-inverse results.

### N5 — Rhetoric And Resolution Audit

The phrase “no stable strictly local update” is never used without the exact
qualifiers “explicit one-slice,” “unit tick,” “full cubic Brillouin zone,” and
“family (8).” Per element, every path pointer, tensor/current entry, TT
coordinate, and transfer entry is checked. Per site, complete `L=5`
incidence/Laplacian and inverse rows are checked. Per mode, all `4,913` grid
points and the analytic corner bound are checked. Per block, source,
constraints, stability, locality, and continuous repair are separate. Lattice-
wide, the path formula extends on `Z^3` and the Laurent proof excludes finite-
range inverse for this symbol; arbitrary actions, paths, nonlinear phases, and
histories are not inferred. The cached runner prints all five resolution lines.

### N6 — Partial-Closure And Primitive Scan

The premise registry confirms that kinetic isotropy grants only `c_t=c_s` at
OS0, not a discrete update, causal definition, Hamiltonian, or Record clock.
The minimal axioms explicitly supply none of them. The continuous-time repair
can retire the stability wall without a new axiom if a downstream theorem
derives generator-local causality and the event instrument. A smaller-time-step
convention would instead require reconciling the stated unit graining. An
auxiliary circuit theorem could retire both. Therefore no axiom necessity is
claimed.

### N7 — Steelman

The strongest hostile response is an explicit finite-depth symplectic QCA with
auxiliary staggered registers: its substeps could be individually local and
unitary, reproduce two TT modes at OS0, carry the conserved path stress, and
avoid solving `(I+rL_s)^-1`. The terminal obligation is concrete—write its
one-tick matrix, prove full-zone positive norm and four constraint intertwiners,
then eliminate or physically identify auxiliaries. Such a construction would
evade the family (8) tradeoff completely. It is not supplied here, so the
negative remains family-scoped and the QCA route is the next adversarial
alternative if continuous time is not selected.

### N8 — Cross-Cycle Echo

Earlier transfer blocks repeatedly showed that Euclidean roots, OS positivity,
and Lorentzian physical update are separate obligations. Block 51 positively
closed OS/canonical feasibility but did not test direct unit-tick stability.
This block supplies that missing test and a continuous repair. Earlier Record
work treated formation count and clock together; the frontier decoder now
demonstrates that a conserved source can persist while Record count grows.
Prior dynamics walls have been retired by exact Hamiltonian or circuit
bridges, so both mechanisms are preserved rather than mislabeled as new-axiom
necessity.

**Status: PASS.** The straight conserved source and the family-scoped
unit-tick locality/stability boundary survive N1-N8. Smaller ticks, IR-only
theories, implicit action locality, continuous local Hamiltonians, operator
splitting, auxiliary QCA, different actions, massive/accelerated sources,
nonlinear gravity, and exact joint-law adoption remain live.

## Reproduction

Run from the repository root:

~~~bash
python3 scripts/admissibility_record_worldline_conserved_stress_two_tt_lorentzian_cfl_locality_lstar_boundary_2026_08_11.py
~~~
