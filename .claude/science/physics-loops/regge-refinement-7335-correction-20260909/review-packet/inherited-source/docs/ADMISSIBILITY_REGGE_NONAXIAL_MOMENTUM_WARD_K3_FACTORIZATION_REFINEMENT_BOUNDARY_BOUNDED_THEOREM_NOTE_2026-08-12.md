---
claim_id: admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "For the repository's actual four-dimensional Kuhn/Coxeter Regge-plus-deficit-square action at alpha=1/1024, exact cyclic phase quotients s=n.x mod L retain all fifty hinge classes and 240 simplex-hinge incidences per phase site for the nonaxial face-diagonal winding n=(1,1,0,0) and body-diagonal winding n=(1,1,1,0). Conserved static and Lorentz-null transverse source polarizations are solved in the complete eleven-dimensional flat nongauge quotient at fixed metric-response amplitude. On three increasing odd periods per orbit, the generated second-harmonic force has a bounded nonzero norm, its contraction with the linear displacement-generator term is O(|k|^2), inclusion of the quadratic generator term cancels that leading coefficient and leaves O(|k|^3), and the exact complex Ward vector divided by |k|^3 stabilizes. All four fitted exact-Ward powers lie between 2.94 and 3.04 with normalized-coefficient spread below four percent. This removes the simplest axial-artifact objection to Block 59 and resolves the executed k^3 order as a two-stage Ward cancellation. It is not a generic-momentum theorem, uniform all-L/refinement bound, nonlinear branch theorem, observable-decoupling theorem, full-Z3 construction, selected source/action law, nonlinear Lorentzian stability theorem, axiom amendment, audit verdict, or TOE percentage movement."
upstream_dependencies:
  - minimal_axioms
  - admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_bounded_theorem_note_2026-08-12
  - admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_2026_08_12.py
---

# Regge Nonaxial-Momentum Ward `k^3` Factorization And Refinement Boundary

**Date:** 2026-08-12

**Type:** `bounded_theorem`

**Role:** test whether Block 59's infrared Ward softening is merely an axial
one-dimensional artifact, and isolate the local order mechanism before any
further refinement or action-replacement work.

**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_2026_08_12.py](../scripts/admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_2026_08_12.py)

**Repository dependencies:** the current
[minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md), the
[Block-59 increasing-period result](ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_INCREASING_PERIOD_PSEUDOCONSTRAINT_SCALING_BOUNDED_THEOREM_NOTE_2026-08-12.md), and the
[Block-53 causal two-TT update](ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md).

## Result Up Front

Block 59 found

```text
||W(2k)|| = eta^2 O(|k|^3)                          (1)
```

on axial odd-period families. That was high-value route evidence, but it did
not rule out a special cancellation tied to one lattice axis.

This block uses two genuinely nonaxial cubic momentum orbits,

```text
n_face = (1,1,0,0),       k = (2 pi/L) n_face,
n_body = (1,1,1,0),       k = (2 pi/L) n_body.       (2)
```

For a local edge anchored at `a`, its cyclic phase shift is exactly

```text
Delta s = n.a  (mod L).                              (3)
```

Equation (3) is not a directional truncation of the local action. It is the
exact quotient of one Bloch plane wave: all fifteen edge classes, all fifty
hinge classes, and all 240 simplex-hinge incidences per phase site are rebuilt
with their actual four-dimensional anchors. Only superpositions with momenta
outside the cyclic subgroup are absent.

The source polarizations are

```text
face static: e_t tensor e_t,
face null:   (e_z+e_t) tensor (e_z+e_t),
body static: e_t tensor e_t,
body null:   ((e_x-e_y)/sqrt(2)+e_t) tensor itself.  (4)
```

Each vector in (4) is transverse to its Euclidean Bloch momentum; the two
null vectors have zero Lorentz norm with coordinate three read conditionally
as time. The edge source is the minimum-norm metric pullback, and the response
solves the complete eleven-dimensional flat nongauge quotient.

The retained tails are:

| momentum orbit | source | periods | fitted power | maximum relative fit residual | spread of `W/|k|^3` |
|---|---|---|---:|---:|---:|
| face diagonal | static | `49,97,145` | 2.988411 | 0.00168 | 1.01221 |
| face diagonal | null | `49,97,145` | 2.997559 | 0.00042 | 1.00255 |
| body diagonal | static | `97,145,193` | 2.987628 | 0.00085 | 1.00841 |
| body diagonal | null | `97,145,193` | 2.970265 | 0.00208 | 1.02032 |

The body-null family is the slowest pre-asymptotic control. Moving its tail to
larger periods is necessary: a short-period fit would understate its order.
On the retained tail, all four log fits have maximum relative residual below
`0.6%`.

The order is resolved more strongly than a norm-only fit. Let `F_2(k)` be the
quadratic action-gradient coefficient at the generated second harmonic, after
dividing out `eta^2`. Expand the exact vertex-displacement map as
`Gamma(2k)=Gamma_1(2k)+Gamma_2(2k)+...`, where `Gamma_j=O(|k|^j)`. The
executed calculation gives

```text
||F_2(k)||                                  = O(1),
||Gamma_1(2k)^dagger F_2(k)||               = O(|k|^2),
||(Gamma_1(2k)+Gamma_2(2k))^dagger F_2(k)|| = O(|k|^3),
||Gamma(2k)^dagger F_2(k)||                 = O(|k|^3),
W(2k)                                       = eta^2 O(|k|^3).  (5)
```

Within each orbit and polarization, `||F_2||` varies by less than four
percent, `||Gamma_1^dagger F_2||/|k|^2` by less than seven percent, and
`||(Gamma_1+Gamma_2)^dagger F_2||/|k|^3` by less than six percent. The latter
to former contraction ratio decreases monotonically from below `0.30`, and
the first-to-last exact complex normalized Ward vectors align above `0.995`.
Halving the analytic complex-direction field amplitude preserves the two
hostile normalized Ward coefficients within half a percent.

The important conclusion is bounded: the simplest nonaxial and cubic-diagonal
attacks do not break the emergent-infrared route. Fixed Regge remains rejected
as an exact microscopic first-class law. It remains a viable emergent
candidate whose next missing theorem is uniform angular/refinement control and
physical observable decoupling.

## Why The `k^3` Order Is Plausible

There are two resolved Ward cancellations, not a naive `k^2` force times a
`k` generator.

First, the exact displacement map is

```text
Gamma_e^mu(k) = [exp(i k.v_e)-1] v_e^mu/|v_e|,       (6)
```

so its Taylor orders are known algebraically for every direction. The full
generated edge-force tends to a nonzero norm, but the linear generator term
annihilates its leading constant contribution: its contraction begins at
`|k|^2`, not `|k|`. The quadratic generator term then cancels that `|k|^2`
coefficient, leaving the exact contraction at `|k|^3`.

Every constant positive metric defines another flat Kuhn lattice. The
runner executes a nontrivial off-identity constant metric and finds both
deficit and action gradient zero to numerical precision. The action is local
and analytic near this positive metric family. This supplies the continuum
metric-family identity behind the first cancellation; the second is the
finite-spacing expansion of the same nonlinear Ward/Bianchi structure on the
executed plane-wave jets.

The generator series and constant-metric flatness are algebraic/numerical
anchors. Their complete coefficient cancellation is an executed local order
resolution, not yet a symbolic multivariable Taylor theorem for every
direction. That distinction is why (5) remains bounded evidence rather than a
uniform refinement theorem.

## What Changed Scientifically

Before this block there were two materially different interpretations of
Block 59:

1. the `k^3` result is an axial cancellation and fixed Regge still requires
   immediate exact repair or replacement; or
2. it is the local higher-derivative order of the pseudo-constraint defect,
   making controlled infrared closure the shortest route.

The face- and body-diagonal controls reject the first interpretation on the
two most symmetric nonaxial cubic orbits. This is significant route progress:
the campaign should not spend its next deep block on an automatic perfect
action or source-specific cancellation.

It is still zero TOE score movement. Observable decoupling remains unproved,
as do a uniform angular bound, an explicit refinement map and norm, increasing
regions, a physical state quotient, nonlinear constraint propagation, and a
selected Record/gravity law.

## Axiom Issue Exposed

The present minimal axioms do not state whether gravity must be exact at the
microscopic lattice scale or may be defined by a controlled emergent limit.
An attached law cannot close this ambiguity with the phrase “approximately
covariant.” It must choose one of two contracts:

1. **Microscopic contract:** an exact joint source-geometry Noether identity
   and exactly first-class finite-spacing constraint law.
2. **Emergent contract:** a specified refinement map, norm, admissible source
   class, physical observable/state quotient, convergence rate, and nonlinear
   Lorentzian propagation statement.

This block supplies evidence toward the second contract. It does not select,
adopt, prove necessary, or prove minimal either contract. No axiom is amended.

## No-Go Discipline Packet

The surviving negative statement is narrow:

> The fixed action is not exactly first class on the executed sourced
> finite-spacing branches, and the present nonaxial tails do not by themselves
> prove uniform refinement or physical decoupling.

### N1 -- Alternative Route Enumeration

| route | mechanism | disposition after this block |
|---|---|---|
| uniform analytic refinement | multivariable small-`k` bound in a named norm | open and ranked first |
| hostile angular/source family | irrational-direction approximation or less symmetric conserved tensor | open |
| observable quotient | soft displacement sector decouples from two TT and Record observables | open and required |
| nonlinear Lorentzian limit | constraint-preserving increasing-region update | open and required |
| dynamical matter source | exact mixed source-geometry cancellation | open fallback |
| improved/perfect action | refinement-improved exact or asymptotic law | open fallback |
| Pachner/tent dynamics | variable-complex canonical constraint propagation | open fallback |
| alternate connection carrier | exact local frame/connection Ward identity | open fallback |

No open route is counted as attempted or closed.

### N2 -- Wall-Independence Audit

The finite-spacing Ward lift and missing uniform-refinement theorem are not the
same wall. The former is an executed property of the fixed action. The latter
requires quantifiers over direction, scale, source class, norm, and observable
quotient. Observable contamination and nonlinear propagation are independent
again. They are not collapsed into one rhetorical “approximate covariance”
gap.

### N3 -- Hidden-Wall Scan

The calculation does not test arbitrary momentum, incommensurate angular
limits, simultaneous modes, general conserved stress, nonlinear solved
nonaxial branches, full `Z^3`, open boundaries, state positivity, or source
selection. The cyclic quotient is exact for the single Bloch wave but is not a
claim about arbitrary nonlinear fields.

### N4 -- Residual Matching

The new runner uses the same action, coefficient, edge carrier, metric map,
gauge map, and source normalization as Block 59. It changes only the momentum
orbit and the transverse polarization required by conservation. Thus it tests
the axial-artifact residual directly rather than replacing the problem with a
different action or projected metric surrogate.

### N5 -- Resolution And Rhetoric Audit

- `per_element`: all fifteen edge classes enter;
- `per_site`: all fifty hinges and 240 simplex-hinge incidences enter;
- `per_mode`: the fundamental response and generated second harmonic are
  separated on every executed period;
- `per_block`: two nonaxial orbits, two source polarizations, three tail
  periods per orbit, and two amplitude controls are executed; and
- `lattice_wide`: explicitly not executed.

No claim uses “generic,” “uniform,” “all-L,” “full lattice,” “observable,” or
“Lorentzian” beyond the stated boundary.

### N6 -- Partial-Closure Paths

Equation (5) is useful without completing a TOE: it reprioritizes fixed Regge
as an emergent candidate and gives the next theorem a precise norm/order
target. A uniform Ward bound could close before observable decoupling; a clean
hostile counterexample could instead retire the emergent route without saying
all gravity is impossible.

### N7 -- Steelman

The strongest objection is that two cubic symmetry orbits may share a hidden
cancellation and miss generic angles or multi-mode resonances. That objection
survives. The correct response is a symbolic/local angular bound or a hostile
less-symmetric family, not a universal success claim.

The opposing steelman also survives: exact cutoff constraints may be
unnecessary if every physical observable and state converges to the Einstein
constraint surface. The current calculation supports but does not prove that
position because observable decoupling remains unproved.

### N8 -- Cross-Cycle Echo

Earlier blocks overread affine projections, period-three aliases, and finite
momentum inventories. This block corrects the directional-resolution risk by
testing nonaxial phase anchors and by moving the slow body-null control into
its actual tail. The recurring lesson is to resolve the controlling order and
quantifier before replacing a carrier or declaring a no-go.

**N1--N8 status: `PASS`** for the two-orbit nonaxial order and narrow
finite-spacing/refinement boundary. A generic-momentum success, universal
Regge no-go, uniform continuum theorem, physical-state theorem, or TOE closure
claim would fail this gate and is not shipped.

## Reproduction

From repository root:

```bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
python3 scripts/admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_2026_08_12.py
```

Expected final line:

```text
TOTAL: PASS=7 FAIL=0
```

The runner supports `TOE_MUTATION=phase_shift`,
`TOE_MUTATION=infrared_order`, `TOE_MUTATION=factorization`, and
`TOE_MUTATION=note_boundary`; each mutation must fail its named gate.

## Conclusion

The axial-artifact objection has failed on the executed face- and
body-diagonal controls. The generated force remains bounded and nonzero, but
the first two displacement-generator orders cancel its potential `|k|` and
`|k|^2` Ward contributions, leaving `O(|k|^3)` on all four retained nonaxial
source families.

That is route progress, not TOE closure. The next high-value work is a uniform
angular/refinement theorem or a less-symmetric counterexample, followed by the
physical two-TT/Record observable quotient. More size scans are stopped.

No TOE percentage moves.
