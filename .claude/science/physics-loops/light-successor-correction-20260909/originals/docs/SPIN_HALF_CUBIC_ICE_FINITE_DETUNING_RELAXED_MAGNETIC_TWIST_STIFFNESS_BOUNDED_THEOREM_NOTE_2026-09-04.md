# Finite-Detuning Spin-Half Cubic Ice Has Positive Relaxed Magnetic-Twist Stiffness

**Date:** 2026-09-04

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct transverse-dynamics parent:**
[`SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Static charge-flux parent:**
[`SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**RK carrier parent:**
[`SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py`](../scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt)

## Result up front

The finite-detuning spin-half cubic-ice carrier has a directly measured,
positive relaxed magnetic response on the same couplings where the parent
calculations measured electric stiffness, Coulomb charge response, and a
transverse linear spectral crossover.

For one cubic plaquette orientation, put a phase `theta` on every directed
ring move and let `E_0(theta)` be the lowest energy in the fixed Gauss and
zero-electric-flux sector. The finite-volume relaxed response is

```text
K_L = (1/L^3) d^2 E_0(theta)/d theta^2 at theta=0.
```

The direct calculation finds, over `L=4,6,8,10`,

```text
V=0.95: K = 0.075561 +/- 0.000915,
V=0.90: K = 0.076589 +/- 0.001155.
```

Every individual size and both continuation radii give a resolved positive
coefficient. A doubled-population calculation reproduces the result, and
three independently sampled plaquette orientations give one cubic response.
The response is already present at the RK point and changes by less than ten
percent over the two finite detunings.

This resolves the immediate magnetic question positively: the microscopic
finite-qubit carrier has a relaxed, same-detuning magnetic cost rather than
only a bare phase-twisted trial-state cost.

It also corrects an important normalization ambiguity. The RK parent reported

```text
J n_f approximately 0.2598
```

from the expectation value of a phase-twisted equal-amplitude state. That is
a valid positive variational upper cost. It is not the relaxed ground-energy
curvature. The present calculation finds the latter equal to
`0.073357 +/- 0.000881` on the tested RK volumes. The two numbers answer
different questions and must not be
substituted for one another in `c^2=U K`.

Using the newly measured same-detuning `K`, the static-dynamic Maxwell
comparison is not yet quantitatively closed on the finite matrices. The
stronger detuning is statistically compatible at the declared resolution;
the weak detuning retains a greater-than-two-error tension. This is positive
localization of the remaining light-sector work, not a no-photon result. The
shortest next test is to extend the transverse spectrum farther into the
infrared and ask whether its fitted `c^2` approaches the independently fixed
`U K`.

This note does not claim a thermodynamic helicity modulus, an infinite-volume
photon pole, or a Standard Model electromagnetic normalization.

## 1. Carrier and physical twist

The carrier is the same one-qubit-per-link cubic ice model used throughout the
parent stack. In a fixed three-of-six Gauss sector and electric-flux sector,

```text
H(0) = - sum_p (|clockwise><counterclockwise| + h.c.) + V N_f.
```

For a chosen plaquette orientation `mu nu`, assign each flippable directed
move a sign `s_p(x)=+/-1`. Reversing the move reverses the sign. The Hermitian
twisted Hamiltonian is

```text
H(theta)_(x,y) = -exp(i theta s_p(x))
```

when `x` and `y` differ by that oriented plaquette flip. Other orientations
retain matrix element `-1`, and the diagonal remains `V N_f(x)`. Because the
reverse matrix element is the complex conjugate, `H(theta)` is Hermitian.

The fully relaxed curvature is

```text
K_L = E_0''(0)/L^3.
```

It includes both the direct ring-energy curvature and the state relaxation
induced by the twist. This distinction is why it can be smaller than the
expectation value in one fixed phase-twisted trial state.

For a uniform magnetic flux quantum, `theta=2 pi/L^2`, so a positive stable
`K_L` produces the Maxwell finite-volume scaling

```text
Delta E = 2 pi^2 K_L/L + higher powers.
```

The runner measures the zero-angle curvature. It does not simulate a whole
quantized-flux ladder.

## 2. Sign-free analytic continuation

Direct stochastic projection at real `theta` has a phase problem. The runner
uses the analytic continuation

```text
theta = i eta.
```

Then the target off-diagonal weights are real and positive:

```text
exp(-eta s_p(x)).
```

The continued matrix is non-Hermitian, but its Green matrix is positive and
has a Perron eigenvalue. Moreover,

```text
H(-i eta) = H(i eta)^T,
```

so the two signs have exactly the same spectrum. Analyticity around zero gives

```text
E_0(i eta) = E_0(0) - (K_L L^3/2) eta^2 + O(eta^4).
```

Thus

```text
K_L(eta) = -2 [E_0(i eta)-E_0(0)]/(eta^2 L^3)
```

approaches the physical Hermitian curvature. The runner averages independent
`+eta` and `-eta` populations and repeats the measurement at `eta=0.10` and
`eta=0.16`.

### Exact continuation control

The complete connected `L=2` orbit is diagonalized twice: once at real
`theta=0.02` and once at `theta=i 0.02`. At all three tested couplings,

```text
V=1.00, 0.95, 0.90,
```

the continued curvature reproduces the physical Hermitian curvature to
better than `10^-4` relative. The stochastic `L=2` results then reproduce the
same exact curvatures within the declared population errors.

This test establishes the sign of the continuation rather than assuming it.

## 3. Exact positive projector

Let `M=3L^3` be the number of square moves. The runner uses

```text
G_eta = I - H(i eta)/(1.5 M).
```

For every sampled state, its exact row sum is

```text
b_eta(x) = 1 + [W_eta(x)-V N_f(x)]/(1.5 M),
```

where

```text
W_eta(x) = sum over flippable p of exp(-eta s_p(x))
```

on the target orientation and unit weight on the other two. A random
plaquette proposal is accepted with the exact normalized Green weight.
Fixed-population stochastic reconfiguration samples the positive left Perron
vector. Its local row-energy estimator is

```text
E_local(x)=V N_f(x)-W_eta(x).
```

At `eta=0`, this reduces to the already verified constant-trial identity

```text
E_local=(V-1)N_f.
```

The runner updates both `N_f` and `W_eta` only on the exact affected
plaquettes after each ring move, then independently recounts them in every
final walker. It also checks the three-of-six Gauss law, zero electric flux,
transition-probability bounds, effective population, and final-state
diversity.

This is an exact Green-kernel representation followed by a finite-population,
finite-projection stochastic estimate. It is not exact diagonalization above
`L=2`.

## 4. Declared finite matrix

The primary matrix uses

```text
V = 0.95 and 0.90,
L = 2,4,6,8,10,
eta = 0, +/-0.10, +/-0.16.
```

The reported volume summaries omit `L=2`, which is retained as the exact
calibration. They average the `L=4,6,8,10` estimates after combining the two
continuation radii. Errors conservatively take the larger of propagated
within-run uncertainty and the standard error across volumes.

Additional controls are:

- an RK ladder at `L=2,4,6,8,10`;
- independent samples of all three cubic orientations at `V=0.90,L=6`;
- doubled `L=8` populations at both finite detunings; and
- exact real-versus-imaginary twist diagonalization on `L=2`.

The two continuation radii are a truncation control. Their agreement does not
prove the absence of every higher-order effect outside the tested interval.

## 5. Finite-detuning result

The final cached values are inserted from the identity-pinned runner receipt.
The runner reports `TOTAL: PASS=13 FAIL=0` and gives

| coupling | relaxed `K`, `L=4,6,8,10` | `K_L` at `L=4,6,8,10` |
|---:|---:|---|
| 0.95 | `0.075561 +/- 0.000915` | `0.076864, 0.077237, 0.073327, 0.074815` |
| 0.90 | `0.076589 +/- 0.001155` | `0.079733, 0.075228, 0.076852, 0.074541` |

At each coupling:

1. every `K_L(eta)` is more than three internal errors above zero;
2. `eta=0.10` and `0.16` agree within twenty percent;
3. the combined `L=4,6,8,10` spread is below ten percent;
4. doubled populations reproduce the primary `L=8` value within eight
   percent; and
5. all exact counts, Gauss sectors, electric fluxes, and transition bounds
   remain intact.

These statements establish positive finite-volume relaxed response. Four
large but finite boxes do not establish a nonzero thermodynamic limit.

The doubled `L=8` populations return `0.076116 +/- 0.000736` at `V=0.95`
and `0.075662 +/- 0.000900` at `V=0.90`. The three independent orientation
controls return `0.077130`, `0.073878`, and `0.075619`. The minimum effective
population fraction over the complete retained matrix is `0.946030`.

## 6. RK variational cost versus relaxed response

The earlier RK calculation evaluated the original Hamiltonian in a specified
phase-twisted equal-amplitude state. If `n_f` is its flippability density,

```text
Delta E_trial = J n_f L^3 [1-cos(theta)].
```

It measured `J n_f` near `0.2598`. By the variational principle, this is a
positive upper cost for that trial state. Allowing the state to relax can
lower the curvature through the current-response term. The present runner
does allow that relaxation by taking the Perron eigenvalue at each continued
twist.

The direct RK ladder gives

```text
K_RK,relaxed = 0.073357 +/- 0.000881
```

over `L=4,6,8,10`, strictly positive and well below `0.2598`. Its four values
are `0.075488, 0.072042, 0.072466, 0.073433`. The finite-detuning coefficients
remain within ten percent of it. Therefore:

```text
positive bare twist cost: retained,
positive relaxed twist cost: newly measured,
equality of the two: rejected on the tested finite systems.
```

This is a correction of interpretation, not a retraction of the earlier
positive variational calculation.

## 7. Static-dynamic Maxwell join

The direct parents measured

```text
U(0.95)=0.162638,
U(0.90)=0.321114,
```

and transverse crossover coefficients

```text
c_dynamic^2(0.95)=0.027162 +/- 0.005322,
c_dynamic^2(0.90)=0.032683 +/- 0.005489.
```

For one quadratic Maxwell normalization,

```text
c^2=U K.
```

The runner performs this comparison without refitting `U`, `K`, or the
dynamic ladders. The static predictions are

```text
V=0.95: U K = 0.012289 +/- 0.001169,
V=0.90: U K = 0.024594 +/- 0.002083.
```

The strong-detuning comparison differs by `1.378` combined reported errors.
The weak-detuning comparison differs by `2.729`. The direction is the same at
both couplings: the finite-volume spectral fit returns a larger `c^2` than the
static product.

This does not negate the positive transverse crossover. The spectral parent
explicitly did not claim an asymptotic pole, and at `V=0.95` its lowest tested
momenta sit near the crossover between the RK `q^4` term and the emergent
`q^2` term. A two-term finite-volume fit can therefore assign curvature to
the `q^2` coefficient before the true infrared regime is cleanly isolated.

The comparison makes the next decision test concrete:

```text
extend V=0.95 to lower q and test c^2 = U K as a fixed prediction.
```

If the fitted coefficient moves toward `U K`, the light normalization closes.
If controlled lower momenta preserve the discrepancy, the effective
Hamiltonian normalization or measured operator assignment must be revised.

## 8. Program and axiom consequence

The light stack now reads

```text
finite local qubits and exact Gauss constraint
 -> local ring dynamics and RK Coulomb tensor
 -> positive finite-detuning electric stiffness
 -> charge Coulomb response with the same U
 -> direct transverse linear spectral crossover
 -> positive same-detuning relaxed magnetic response.
```

This is meaningful TOE-facing progress: the magnetic ingredient has moved
from a fixed trial-state expectation to a relaxed response on the same finite
carrier. The remaining light issue is no longer “does the carrier have a
magnetic stiffness?” It is the quantitative infrared join among three
independently measured coefficients.

No axiom edit is justified. The four axioms permit the carrier and its local
dynamics but do not fix this supplier Hamiltonian, its coupling, or its
continuum normalization. The current discrepancy is inside the supplied
physics and its finite-size extraction. Writing it into the axioms would hide
rather than solve the calculation.

No official TOE score moves until independent classification. The science
position improves because one named ingredient is now directly positive and
the remaining closure test is sharper.

## 9. Structured wall audit

### N1 — Alternative routes

The campaign considered four routes to the same-detuning magnetic coefficient:

1. reuse the RK flippability expectation;
2. evaluate a finite-detuning phase-twisted ground-state trial vector;
3. sample the real-twist Hamiltonian directly; and
4. extract the fully relaxed curvature by sign-free analytic continuation.

Route 1 changes the coupling and does not include relaxation. Route 2 gives
only a variational upper cost. Route 3 has a phase problem. Route 4 is retained
because its continuation sign and normalization can be checked by exact
diagonalization.

### N2 — Wall independence

The positive magnetic result does not depend on the transverse spectral fit:
it uses only the local Hamiltonian, exact twist definition, and Perron
eigenvalue. Conversely, the observed Maxwell-join tension depends on comparing
independent static and dynamic calculations. Removing the dynamic parent
removes the comparison, not the positive magnetic theorem.

### N3 — Hidden-wall scan

The main hidden risks are finite population, finite projection time,
continuation-radius truncation, cubic-axis bias, and confusing a variational
expectation with a relaxed eigenvalue. The runner attacks them with doubled
populations, two radii, exact `L=2`, all three orientations, and an explicit
separation of the two response definitions.

### N4 — Residual matching

What remains unclosed is exactly the residual measured here:

```text
c_dynamic^2 - U K_relaxed.
```

It is not relabeled as an axiom issue, a missing magnetic term, or evidence
against the carrier. The next campaign must reduce the spectral momentum or
find a normalization change that quantitatively explains this residual.

### N5 — Rhetoric audit

“Stiffness” in the title means finite-volume relaxed twist curvature. It does
not mean an audited thermodynamic phase theorem. “Correction” refers to using
the old variational number as a relaxed coefficient; the old calculation
itself remains positive and reproducible.

### N6 — Partial-closure path

Even if the static-dynamic equality remains unresolved, the positive relaxed
magnetic response is independently useful. It closes the existence question,
provides a direct target for larger-volume spectroscopy, and supplies a
quantitative response for comparison with other carriers.

### N7 — Steelman

A hostile reviewer can say that a non-Hermitian continuation may encounter an
exceptional point, fixed-population Perron sampling is biased, two finite
radii do not determine a derivative, and four volumes do not prove a limit.
They can also say that the greater-than-two-error weak-detuning discrepancy
uses uncertainties from separate stochastic pipelines and therefore should
not be called a sharp rejection.

The bounded reply is that exact `L=2` continuation fixes the local sign and
curvature, `+/-eta` transpose symmetry is exact, the two radii agree, cubic
orientations agree, doubled populations agree, and the volume ladder is
stable. These controls justify the finite-matrix positive result and the word
“tension,” not a thermodynamic theorem or no-go.

### N8 — Cross-cycle echo and failed-attempt ledger

The first scout used one continuation radius and one population. It found a
positive coefficient near `0.08` but underestimated the exact `L=2` value in
some seeds. Raising the `L=2` population through `512`, `1024`, and `2048`
converged onto exact diagonalization. The retained runner therefore includes
an exact stochastic calibration and a doubled-population large-volume
control.

The first production ladder showed one noisy `V=0.95,L=8,eta=0.10` point.
It was not deleted or used to select another radius. A second radius was
already declared, and a doubled-population `L=8` calculation independently
returned the common `K` near `0.075`. Both primary radii remain in the final
summary.

An efficiency-tuned full pass then reduced every primary population to `512`.
It failed two declared quality checks: the cheap `V=0.90,L=4` point lifted the
four-volume spread above ten percent, and one population reached effective
weight fraction `0.8255` against the retained `0.85` floor. Neither threshold
was lowered. The retained calculation increases only the `L=4` population and
sampling length, and resamples weights twelve rather than eight times per
plaquette sweep. The physical volume set, two continuation radii, estimator,
and response thresholds remain unchanged.

The initial interpretation compared `c^2/U` to the RK flippability number
near `0.260`. The present relaxed calculation showed that comparison joined
different observables. The distinction is retained explicitly, and the
same-detuning relaxed value is used instead.

No failed or interesting result was discarded.

## Falsifiers

This bounded claim fails if the cached runner does not reproduce its final
zero-failure line, or if an independent implementation finds any of:

- real and imaginary exact `L=2` twist curvatures disagree at quadratic order;
- the Green transition weights fail to reproduce `I-H(i eta)/(1.5M)`;
- `+eta` and `-eta` have different Perron eigenvalues;
- local recounting changes `N_f` or the weighted flippability sum;
- any accepted move changes Gauss charge or electric flux;
- doubled populations or cubic orientations move the response outside the
  declared controls;
- controlled larger volumes drive the relaxed curvature to zero; or
- lower-momentum spectroscopy preserves the current discrepancy after every
  operator and normalization factor is matched.

Run:

```bash
python3 scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py
```
