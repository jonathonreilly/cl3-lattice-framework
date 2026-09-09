# Finite-Detuning Spin-Half Cubic Ice Joins Charge Coulomb Response to Its Flux Stiffness

**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct finite-detuning parent:**
[`SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**RK and finite-qubit parent:**
[`SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**First-order stiffness parent:**
[`SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py`](../scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt`](../logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt)

## Result up front

On the same finite-detuning spin-half cubic-ice components whose topological
flux tower fixes an electric stiffness `U`, a fixed opposite unit-charge pair
has a Coulomb-family interaction with the same coefficient to the stated
finite-population accuracy.

The calculation uses the complete finite Hamiltonian at

```text
V=0.95 and V=0.90,
```

not a first-order expansion around the Rokhsar-Kivelson point. Directed
alternating paths create exactly one charge `+1` and one charge `-1`, with no
other Gauss defects. Square-ring projection then holds their positions fixed
while sampling the charged mobile component.

For axial separations `r=1,...,L/2` on `L=4,6,8`, a joint fit with one core
intercept per volume gives

| `V` | charge-fit `U` | flux-tower `U` | relative difference |
|---:|---:|---:|---:|
| 0.95 | 0.160609 +/- 0.015345 | 0.162638 | 1.2% |
| 0.90 | 0.301440 +/- 0.026769 | 0.321114 | 6.1% |

The charge predictor is the exact periodic cubic-lattice Coulomb coordinate
for the path's fixed harmonic sector,

```text
C_L(d)=G_L(0)-G_L(d)+|d|^2/(2 L^3),

G_L(d)=1/L^3 sum_(k != 0) cos(k.d)
       / [4 sum_i sin^2(k_i/2)].
```

The first two terms are the longitudinal lattice Green-function energy. The
last term is the energy coordinate of the uniform harmonic field carried by
the declared directed path sector. In quadratic Maxwell theory the pair
energy is

```text
E_pair(L,d)=E_core(L)+U C_L(d).
```

The fitted `U` is resolved above zero at both detunings and agrees with the
independent topological-flux `U` within the runner's `25%` threshold.

A raw continuum fit

```text
E_pair(L,r)=E_core(L)-A/r
```

is nearly degenerate with the periodic predictor at these short volumes. Its
amplitude agrees within `25%` with the coefficient-free Maxwell prediction

```text
A=U/(4 pi).
```

The raw amplitudes are `27%` and `21%` above that asymptotic normalization;
the runner treats `30%` as its finite-volume diagnostic. The data therefore
resolve the Coulomb family and its shared normalization at that accuracy,
but do not select periodic-lattice corrections over raw `1/R`.

Both Coulomb forms beat linear-distance string growth,
quadratic-distance growth, and a within-volume constant response by the
declared controls. Every volume and detuning also passes a simpler sign test:
the charge energy rises from one-link separation to `L/2`. Thus the result is
not only a positive charge-creation gap.

Off-axis pairs at displacements `(2,1,0)`, `(2,2,0)`, and `(2,2,1)` provide a
second geometry test at `V=0.90`. They give

```text
U_charge=0.272689 +/- 0.029369,
U_flux=0.321114,
```

and continue to reject string growth. Path-order and cubic-rotation controls
to the same endpoints agree within four reported errors.

This is a meaningful photon-phase advance: the topological sector tower and
the static force law no longer carry unrelated fitted coefficients. One
microscopic qubit Hamiltonian supplies both, and they meet at the Maxwell
normalization. The result remains bounded by finite volume, finite projector
population/time, unclassified disconnected components, and the absence of a
direct dynamical photon pole.

## 1. Directed paths make only endpoint charges

Use the parent's staggered electric field on the positive-axis link from `x`:

```text
E_i(x)=(-1)^(x_1+x_2+x_3) [n_i(x)-1/2].
```

The initial ice state is

```text
n_i(x)=x_i mod 2.
```

Flipping one link changes its electric field by exactly `+1` or `-1`. Regard
the sign as an arrow on that link. A path that follows these arrows has one
outgoing unit at its start, one incoming unit at its end, and one incoming
plus one outgoing unit at every internal vertex. Consequently

```text
div E=+1 at one endpoint,
div E=-1 at the other,
div E=0 everywhere else.
```

The runner builds axial paths and the off-axis paths

```text
(2,1,0), (2,2,0), (2,2,1).
```

It verifies the complete charge array before projection and after projection
for every final walker. It rejects path segments that oppose an alternating
arrow or reuse a link.

The elementary square flip changes a closed circulation, so it preserves the
entire charge array. The charges are external fixed sources in this theorem;
their motion and matter backreaction are not claimed.

## 2. The periodic Coulomb coordinate

On the periodic cubic lattice the positive scalar Laplacian has nonzero-mode
symbol

```text
lambda(k)=4 sum_i sin^2(k_i/2).
```

Its zero-mode-removed Green function is the finite sum displayed above. For
charges `+1` and `-1` separated by `d`, minimizing

```text
(U/2) sum_links E^2
```

at fixed divergence gives the longitudinal energy

```text
U [G_L(0)-G_L(d)].
```

The directed path also fixes a harmonic sector. If its unwrapped displacement
is `d`, the sum of its added electric field is `d`. Its uniform component is
therefore `d/L^3`, whose energy is

```text
(U/2) L^3 |d/L^3|^2 = U |d|^2/(2L^3).
```

Longitudinal and uniform fields are orthogonal. Adding the two gives `U C_L`.
No coefficient is tuned in this coordinate.

The runner verifies that `C_L` is unchanged by axis permutations and sign
reversals on `L=4,6,8`. Its comparison value `U_flux` is the mean topological
stiffness already produced by the direct parent's independent flux-sector
calculation:

```text
U_flux(0.95)=0.162638,
U_flux(0.90)=0.321114.
```

These are comparison data, not refitted to the charge energies.

## 3. Exact charged-sector calibration

At `L=2`, one adjacent opposite-charge component contains exactly `508`
basis configurations. For each detuning the runner constructs its complete
square-move graph and diagonalizes

```text
H(V)=H_RK+(V-1)N_f.
```

The exact charged ground energies are

| `V` | exact `E_0` | projector estimate |
|---:|---:|---:|
| 0.95 | -0.349861309 | -0.350107486 +/- 0.000109301 |
| 0.90 | -0.706280403 | -0.706326091 +/- 0.000283532 |

Direct eigenvector evaluation also verifies the constant-trial mixed-estimator
identity

```text
E_0=(V-1)<N_f>_mixed
```

to `1e-9`. The independent `2048`-walker populations reproduce both exact
energies inside the declared stochastic bound.

This calibrates the charged projector itself. It does not turn the larger
graphs into exact diagonalizations.

## 4. Finite projector protocol

The axial `L=4,6,8` matrix uses:

```text
walkers                 384
uniform-RK warmup       120 attempted sweeps
projector burn          200 attempted sweeps
projector samples       400, one per attempted sweep
```

One attempted sweep is `3L^3` exact positive Green-function steps per walker.
Ten time blocks supply the internal errors. The parent note proves the
projector transition and mixed estimator; this runner independently checks
their charged-sector exact controls.

Off-axis and path-order controls use `256` walkers with `100/150/300`
warmup/burn/sample sweeps. The `L=8`, `V=0.90`, `r=1,4` population control
uses `768` walkers with `150/250/500` sweeps.

Every final population satisfies:

- the original full charge array, not merely total charge zero;
- recomputed and incrementally maintained `N_f` equality;
- minimum effective population above `90%` of nominal; and
- at least `25%` distinct final walkers for every `L>=4` run.

The `768`-walker long-distance energy rise is positive and agrees within
`30%` with the `384`-walker value. This bounds one population sensitivity; it
does not remove population bias rigorously.

## 5. Fit and control hierarchy

The primary fit uses every axial separation on every volume, with one
independent intercept `E_core(L)` and one common response coefficient per
detuning. The intercept absorbs the local source-core energy and its finite
volume dependence. It cannot absorb separation dependence within a volume.

At `V=0.95`, the unweighted residuals are

```text
periodic Coulomb       0.00003535
raw 1/R                0.00003263
linear distance        0.00010862
quadratic distance     0.00015186
constant               0.00018761.
```

At `V=0.90`, they are

```text
periodic Coulomb       0.00022624
raw 1/R                0.00019146
linear distance        0.00047988
quadratic distance     0.00070220
constant               0.00100906.
```

The periodic residual is `8%` and `18%` above raw `1/R`, respectively. The
runner permits at most `25%`. It does not declare the finite-periodic
correction selected. Both forms are Coulombic, and both are separated from
the confining/string and flat controls.

The stronger discriminator is normalization. The periodic coefficient is
compared directly with `U_flux`, while the raw `1/R` coefficient is compared
with `U_flux/(4 pi)`. The periodic comparisons pass within `25%`; the raw
asymptotic comparisons are `27%` and `21%` high and pass the stated `30%`
finite-volume diagnostic.
The two detunings therefore test not only a shape but the scaling of its
coefficient as the microscopic electric stiffness changes.

Short-distance irrelevant operators, periodic images, harmonic-sector choice,
and projector noise can all move the small-volume curve. The theorem does not
fit those corrections with extra free parameters.

## 6. Off-axis and path controls

The off-axis set adds three displacement shapes on each of `L=6,8` at
`V=0.90`. Its periodic-Coulomb coefficient is positive, remains within `30%`
of `U_flux`, and has smaller residual than linear- or quadratic-distance
growth. It is not required to beat raw radial `1/R` because the present sample
does not resolve the small cubic-lattice angular correction.

Two further pairs target implementation artifacts:

1. `(2,2,0)` is reached by `x` then `y` and by `y` then `x`; the paths differ
   by closed square circulations but have the same endpoints and sector.
2. `(2,1,0)` and its cubic rotation `(1,2,0)` are built with compatible
   directed orders.

Their projected energies agree within four combined internal errors. This
tests path-order and axis coding without claiming a complete orbit average.

## 7. Program consequence and remaining target

The finite-qubit light chain now has the following coefficient-level join:

```text
topological electric flux
        -> U from Phi^2/L
        -> same U in periodic charge response
        -> U/(4 pi) in raw long-range 1/R normalization.
```

This is more informative than two independent positive fits. A single
coefficient controls a global sector energy and a local-source response, as
Maxwell theory requires.

The result still does not directly see a photon in time. The highest-value
remaining phase diagnostic is an imaginary-time transverse correlator whose
lowest pole scales as `|k|` rather than `k^2` or a nonzero mass. That would
join the static coefficient pair to the dynamical mode.

Separate program walls also remain:

- classification or stronger sampling of disconnected mobile components;
- a controlled thermodynamic limit and a finite interval in `V`;
- finite-detuning magnetic-twist stiffness;
- mobile dynamical charges and matter-field backreaction on this carrier;
- an orthogonal one-qubit-per-physical-site compiler;
- Admissibility-law selection; and
- empirical electromagnetic identification.

No axiom update is proposed. The source positions, Hamiltonian, detunings,
component starts, and projector are supplied model content.

## 8. Prior-art and contribution boundary

The cubic spin-half model, RK point, first-order spinon potential, dual Maxwell
description, and stable adjacent `U(1)` phase are due to M. Hermele,
M. P. A. Fisher, and L. Balents,
[“Pyrochlore Photons: The U(1) Spin Liquid in a S=1/2 Three-Dimensional
Frustrated Magnet”](https://arxiv.org/abs/cond-mat/0305401) (2004).

This source makes no priority claim for the model, Coulomb law, Green-function
projector, or phase. Its repo-specific contribution is the reproducible join:
two finite detunings, exact charged-orbit controls, every axial separation on
three volumes, off-axis and path-order checks, population doubling, and a
coefficient comparison to the independently computed topological stiffness.

## 9. Executable evidence

The runner reports `TOTAL: PASS=15 FAIL=0`. It checks:

- axial and off-axis paths leave exactly two opposite unit charges;
- periodic Coulomb coordinates are cubic- and inversion-invariant;
- the complete `508`-state charged graph obeys the mixed-estimator identity;
- two charged projector energies reproduce exact diagonalization;
- every final walker preserves its full charge array and `N_f` count;
- population weight and state-diversity controls;
- resolved positive pair-creation energy at all separations;
- positive one-link-to-half-box energy rise on all six volume/detuning rows;
- positive periodic-Coulomb coefficient at both detunings;
- Coulomb-family preference over string, quadratic, and constant controls;
- periodic-response `U` agreement with flux-tower `U`;
- raw `1/R` amplitude tracking of `U/(4 pi)` within `30%`;
- the off-axis coefficient and non-string control;
- path-order and cubic-rotation agreement; and
- a doubled-population long-distance-rise control.

## No-Go Discipline Gate

This positive join includes a deliberately unresolved distinction between the
finite periodic kernel and raw `1/R`. The gate prevents that finite-resolution
boundary from being inflated into either a unique-kernel claim or a negative
phase verdict.

### N1 — Alternative route enumeration

| Route | Outcome |
|---|---|
| exact charged graph | **Positive control:** `508` states and two exact detunings. |
| axial periodic Green response | **Positive:** resolved coefficient matches `U_flux`. |
| raw continuum `1/R` | **Positive and near-degenerate:** amplitude matches `U/(4 pi)`. |
| off-axis displacement family | **Positive:** keeps coefficient sign/magnitude and rejects string growth. |
| linear or quadratic string growth | **Tested negative for this data:** larger residuals. |
| constant separation response | **Tested negative for this data:** larger residuals and endpoint rise. |
| moving dynamical charges | **Open:** fixed sources here do not move. |
| transverse imaginary-time pole | **Open:** direct dynamical photon diagnostic. |

The two Coulomb parameterizations are retained as one unresolved family, not
counted as competing TOE walls.

### N2 — Wall-independence and collapse audit

The remaining phase wall contains thermodynamic control, a finite-detuning
magnetic response, and the dynamical photon pole. The periodic-versus-raw
Coulomb distinction is a finite-size correction question inside that wall.

Independent walls are the physical-site compiler, mobile matter coupling,
law selection, Record formation/readout, and empirical identification.
Neither a static force law nor a compiler derives the other. A dynamic pole
would not choose the Admissibility law. Matter backreaction would not prove a
thermodynamic photon phase.

### N3 — Hidden-condition scan

The supplied cubic graph, periodic even volumes, fixed charge positions,
directed paths, harmonic sectors, component starts, Hamiltonian, detunings,
populations, projection times, seeds, per-volume intercepts, and five fit
families are explicit. The charges are external and immobile. The graph
components are not classified exhaustively above `L=2`. Internal block errors
are not a rigorous population-bias or autocorrelation bound.

No experimental charge, electric unit, speed, or fine-structure constant is
identified. No Record-formation probability or physical time is used.

### N4 — Residual matching

| Surface | Residual there | Match here |
|---|---|---|
| finite-detuning stiffness parent | direct charge law open | **direct partial resolution:** charge response carries the same `U` |
| first-order parent | finite-detuning response unexecuted | **resolved on two finite points, not an interval** |
| finite-qubit RK parent | first-order `1/R` imported | **new finite-detuning projector evidence** |
| primary spin-liquid source | stable phase and first-order spinon potential | **independent bounded match, not a replacement proof** |
| minimal axioms | no Hamiltonian or law value selected | **unmatched:** supplied model remains supplied |

The charge result depends on the direct parent's formulas and files on this
stack, not on an audit grade assigned to that parent.

### N5 — Rhetoric and resolution audit

“Coulomb response” means the finite data support periodic and raw inverse-
distance forms while rejecting the named confining/flat controls. It does not
mean the periodic correction is resolved. “Same coefficient” means agreement
inside `25%` with reported stochastic errors and controls, not exact equality.
“Long range” is not used as an infinite-volume claim.

The five-resolution certificate says:

```text
per_element: directed path links and square flips are checked;
per_site: two fixed charges and the full Gauss array are preserved;
per_mode: periodic Coulomb plus harmonic and raw 1/R are fitted;
per_block: exact L=2 and projector L=4,6,8 are combined;
lattice_wide: finite-volume static response, not an infinite-volume theorem.
```

### N6 — Partial-closure paths and primitive boundary

No axiom or approved primitive is added. Positive continuations are:

- extract a transverse imaginary-time pole at multiple momenta and volumes;
- extend charge response to `L>=10` with independent populations;
- classify or sample additional mobile components with nonlocal loop starts;
- compute the magnetic twist coefficient at the same detunings; or
- promote the coarse carrier only after an orthogonal physical-site compiler.

The kinetic-isotropy primitive neither selects this Hamiltonian nor turns
projector steps into physical time.

### N7 — Steelman

A hostile reviewer can correctly say that `L<=8`, fixed populations, short
separations, and per-volume core intercepts cannot prove an asymptotic
potential. They can note that raw `1/R` has a slightly smaller residual than
the full periodic coordinate and that disconnected mobile components may
exist. These points are why the claim is bounded.

They do not erase the exact charged calibration, positive endpoint rise on
all six rows, rejection of string growth, two-detuning coefficient tracking,
off-axis control, or agreement with independently measured `U`. The honest
outcome is a positive finite-volume coefficient join with the kernel
distinction unresolved.

### N8 — Cross-cycle echo

The RK parent explicitly declined to claim its short direct charge run and
cited the primary first-order `1/R` result. The finite-detuning parent then
named charge response as one of two next phase diagnostics. This source
executes that opening with the positive Green-function projector already
calibrated there. It does not recycle the flux data as charge data: source
separations, charged components, path controls, and fits are new observables.

Open PR #7942 appeared while this result was being packaged. It independently
finds `937` square-flip components on `L=2` and a parity obstruction for a
different stochastic-series pair-update sampler. This source does not use
that pair update, quote a full-sector excitation gap, or cross components: its
exact positive projector and every claimed energy are explicitly
component-scoped. The new comparison reinforces rather than resolves the
stated component-classification boundary.

**Gate result:** PASS. Eight routes are separated, the two Coulomb forms are
kept as one unresolved family, confining controls are bounded only on the
tested data, and the coefficient join is preserved without a thermodynamic or
dynamical overclaim.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- a directed path leaves any charge beyond its two unit endpoints;
- a square move changes the fixed charge array;
- periodic `C_L` fails cubic or inversion covariance;
- the exact `508`-state graph or mixed estimator is miscounted;
- the charged projector misses either exact `L=2` energy beyond tolerance;
- any separated pair lacks a resolved positive creation energy;
- any half-box endpoint fails to rise above one-link separation;
- either Coulomb coefficient is unresolved or nonpositive;
- periodic response differs from raw `1/R` beyond the declared residual
  tolerance;
- Coulomb response fails a named string, quadratic, or constant control;
- periodic `U_charge` differs from `U_flux` by at least `25%`;
- raw `1/R` amplitude differs from `U_flux/(4 pi)` by at least `30%`;
- off-axis response loses its positive flux-matched coefficient or its
  non-string control;
- path-order or cubic-rotation energies disagree beyond four errors; or
- population doubling reverses or changes the endpoint rise beyond `30%`.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=15 FAIL=0
```
