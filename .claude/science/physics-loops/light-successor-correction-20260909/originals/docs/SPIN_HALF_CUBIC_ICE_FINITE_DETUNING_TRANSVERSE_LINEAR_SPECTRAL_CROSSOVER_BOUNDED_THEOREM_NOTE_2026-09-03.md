# Finite-Detuning Spin-Half Cubic Ice Has a Transverse Linear Spectral Crossover

**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct static-response parent:**
[`SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Finite-detuning projector parent:**
[`SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Finite-qubit photon parent:**
[`SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py`](../scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt`](../logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt)

## Result up front

The same spin-half cubic-ice Hamiltonian whose finite-detuning topological
flux tower and fixed-charge response share one electric stiffness also has a
directly measured transverse imaginary-time spectral crossover.

The measured observable is the cubic-orbit average of the six first-momentum
transverse electric modes. On periodic boxes, write

```text
q_L = 2 sin(pi/L).
```

The runner estimates the normalized ground-state correlation

```text
C_L(tau) = <0| E_T(-q_L) (G/g_0)^(3 L^3 tau)
                       E_T(q_L) |0>
             / <0|E_T(-q_L)E_T(q_L)|0>,

G = I - H/(3 L^3).
```

One fixed interval, `tau=2,...,6`, supplies the reported finite-volume decay
`omega_L`. The adjacent intervals `1,...,4` and `3,...,8` are controls, not
alternative selections.

At the exact Rokhsar-Kivelson point, the measured ladder follows

```text
omega_RK(q)^2 = a^2 q^4
```

over `L=6,8,10,12,14`. This is the expected special `z=2` RK dynamics and is
the campaign's null control.

At both finite detunings,

```text
V=0.95 and V=0.90,
```

the excess over that directly measured RK ladder is instead described by

```text
omega_V(q)^2 - omega_RK(q)^2
    = c_V^2 q^2 + b_V q^4.
```

The fitted `c_V^2` is positive at more than three reported standard errors
at each detuning. A joint fit with

```text
c_V^2 = gamma |V-1|
```

is accepted, and the coefficient grows monotonically between the two tested
detunings. Pure linear and pure quadratic laws are both rejected relative to
the two-term crossover on the declared finite matrix.

This is the first repo-native calculation on this carrier to see the
finite-detuning transverse dynamics rather than infer it only from static
Maxwell ingredients or primary literature. It is direct positive movement on
the light lane.

The result is not a thermodynamic photon-pole theorem. A three-term fit

```text
omega^2 = m^2 + c^2 q^2 + a^2 q^4
```

does not resolve `m^2` at two standard errors and does not improve the fit by
the two-sigma one-parameter threshold. That means no mass is detected on the
tested volumes; it does not prove `m=0` at infinite volume. The retained
claim is therefore a **finite-volume transverse linear spectral crossover**.

## 1. Microscopic Hamiltonian and positive projector

Inside one fixed three-of-six Gauss sector and electric-flux sector, the
Hamiltonian is

```text
H(V) = - sum_p (|clockwise><counterclockwise| + h.c.)
       + V N_f.
```

At `V=1`, this is the RK graph Laplacian. At `V<1`, the exact Green kernel

```text
G = I - H/M,  M=3L^3,
```

is entrywise nonnegative. Its row sum at a configuration with `N_f`
flippable squares is

```text
B = 1 - (V-1) N_f/M.
```

The runner samples this kernel by the same fixed-population stochastic
reconfiguration used by the direct finite-detuning parent. It does not use
the parity-conserving pair update studied in open PR #7942. Every accepted
move is one elementary square-ring flip. Consequently the full Gauss array
and electric flux are preserved exactly.

The calculation remains component-scoped. It neither crosses nor classifies
all square-move components. Three nonlocal zero-flux starts give independent
component controls at `L=8`.

## 2. The transverse operator

For the staggered electric field on the positive-axis link from `x`,

```text
E_i(x)=(-1)^(x_1+x_2+x_3) [n_i(x)-1/2],
```

choose momentum axis `a` and a distinct polarization axis `b`. The measured
mode is

```text
E_(a,b)(q)=L^(-3/2) sum_x E_b(x) exp(i q x_a),
q=2 pi/L.
```

There are six ordered pairs `(a,b)`. Axis permutations act transitively on
this set. The runner checks that the measured mode set, the three square
orientations, and the symmetric ice start are closed under every permutation
of the cubic axes.

The reported correlator averages the complete six-mode orbit before fitting.
This is an exact symmetry average, not six statistically independent
measurements. Raw single-mode spreads and a diagonal-error diagnostic are
printed, but neither is promoted to a separate polarization-degeneracy
measurement. This distinction matters on the largest detuned boxes, where
individual descendants are noisy while the invariant average remains clean.

## 3. Forward-walking estimator

With a constant trial vector, an equilibrated projector population represents
the positive right ground vector. At an origin configuration the runner
attaches `E_T(q)`, propagates for `tau` sweeps, attaches `E_T(-q)`, and then
propagates for `F` further sweeps. Descendant labels implement the left
ground-state projection without changing the nonnegative state evolution.

Every `tau` cohort receives the same forward length. This avoids the ancestry
collapse found in the first scout, where early cohorts were accidentally
carried to one common final time. The retained calculation uses `F=4` and
directly compares `F=0,2,4,6`.

For an exponential decay per sweep `lambda`, the exact finite-step conversion
to an energy difference is

```text
omega=(M-E_0) [1-exp(-lambda/M)].
```

No continuum-time approximation is needed in the reported gaps.

At `L=2`, the zero-flux mobile orbit has `864` configurations. The runner
constructs the complete sparse Hamiltonian, diagonalizes its ground state,
and applies the exact finite-step Green kernel to the transverse vector. Six
independent populations with four measurement origins reproduce both the
exact ground energy and normalized correlator through `tau=4`.

## 4. Finite matrix and fixed analysis

The primary matrix is

| coupling | volumes | outer populations | walkers | origins per population |
|---:|---|---:|---:|---:|
| `V=1.00` | `6,8,10,12,14` | 4 | 384 | 4 |
| `V=0.95` | `6,8,10,12` | 4 | 512 | 6 |
| `V=0.90` | `6,8,10,12,14` | 4, with a second 4-population `L=12` family | 512; `1024` at `L=14` | 6; 4 at `L=14` |

Every finite-detuning population receives `80` uniform-RK warmup sweeps and
`140` projector burn sweeps. The RK control receives `80+100` uniform
sweeps. Consecutive measurement origins are separated by the full
`tau_max+F` trajectory plus two additional sweeps.

Errors are standard errors over outer populations after averaging origins
within each population. Origins are not counted as independent replicas.
The second `V=0.90,L=12` seed family is retained in full; it was added after
the first four populations left the mass discriminator underresolved.

The fit variable is the lattice momentum `q_L`, not `2 pi/L`. The RK and
detuned ladders are fitted separately before their squared ratios are
subtracted. The RK errors propagate into every excess point.

## 5. Dispersion and model controls

The cached primary matrix is:

| `V` | `L=6` | `L=8` | `L=10` | `L=12` | `L=14` |
|---:|---:|---:|---:|---:|---:|
| 1.00 | `0.305382 +/- 0.005596` | `0.177396 +/- 0.003236` | `0.115131 +/- 0.001273` | `0.082160 +/- 0.000745` | `0.060182 +/- 0.000455` |
| 0.95 | `0.348953 +/- 0.009472` | `0.219052 +/- 0.004497` | `0.157502 +/- 0.007376` | `0.118248 +/- 0.004007` | not run |
| 0.90 | `0.414570 +/- 0.006725` | `0.256693 +/- 0.007673` | `0.203678 +/- 0.016318` | `0.152398 +/- 0.010326` | `0.106267 +/- 0.004225` |

The RK fit gives

```text
c_RK^2 = 0.000138 +/- 0.000674,
a_RK^2 = 0.092002 +/- 0.002658.
```

Thus the RK infrared intercept is unresolved while its `q^4` coefficient is
positive. Subtracting this measured control gives

| `V` | excess `c_V^2` | errors above zero | residual `q^2` slope | `chi^2` |
|---:|---:|---:|---:|---:|
| 0.95 | `0.027162 +/- 0.005322` | 5.1 | `0.001829 +/- 0.010332` | 0.190 |
| 0.90 | `0.032683 +/- 0.005489` | 6.0 | `0.046609 +/- 0.009647` | 4.267 |

The common detuning fit is

```text
gamma = c_V^2/|V-1| = 0.372286 +/- 0.048788,
chi^2 = 7.721.
```

The mass fits return

```text
V=0.95: m^2=-0.000022 +/- 0.005503, Delta chi^2=0.000,
V=0.90: m^2=-0.004345 +/- 0.004963, Delta chi^2=0.766.
```

Neither is a two-sigma result and neither earns the one-extra-parameter
threshold. The checks enforce the following facts:

1. Every `C_L(tau)` used by the fit stays positive through `tau=6`, while the
   cubic-average imaginary residual stays below `0.06`.
2. Every decay is more than five reported errors above zero.
3. The three predeclared time windows agree within `25%` on every row.
4. The RK ladder selects positive `q^4` in `omega^2` and no resolved `q^2`
   intercept.
5. Each finite detuning selects a positive excess `q^2` intercept at more
   than three errors.
6. The crossover beats a pure `omega proportional q` law and a pure
   `omega proportional q^2` law at both detunings.
7. Adding `m^2` gives neither a two-sigma coefficient nor a `Delta chi^2=4`
   improvement.
8. One common positive `gamma` multiplying `|V-1|` fits both detunings.

The last condition is a response test, not an exact perturbative identity at
these finite detunings. Higher-order changes in the `q^4` term remain
allowed.

## 6. Testing the static-dynamic Maxwell triangle

The static parent measured the independent electric stiffnesses

```text
U(0.95)=0.162638,
U(0.90)=0.321114.
```

The RK magnetic-flux response measured

```text
K_RK approximately 0.2598.
```

For a quadratic Maxwell mode,

```text
c^2=U K.
```

The runner therefore forms the non-refitted comparison

```text
K_dyn(V)=c_V^2/U(V).
```

Both values are positive. At `V=0.95`, `K_dyn` is about `0.167`, within `36%`
of the independent RK magnetic coefficient. At `V=0.90`, `K_dyn` is about
`0.102`, roughly `61%` below it. Because this is not a same-detuning
magnetic-twist measurement, the latter does not falsify the dynamic result;
it prevents a quantitative static-dynamic closure claim at the stronger
detuning. This is the first executed dynamic normalization test joining:

```text
topological electric tower
    -> fixed-charge Coulomb response
    -> transverse propagation speed
    -> nearby magnetic response.
```

No electromagnetic unit or empirical fine-structure constant is assigned.

## 7. Robustness controls

The runner additionally executes:

- `F=0,2,4,6` forward windows on `V=0.95,L=8`;
- a doubled `1024`-walker, longer-burn `V=0.95,L=8` population;
- three nonlocal zero-flux starts, one for each cubic axis;
- exact recounting of `N_f` in every final population;
- exact Gauss and flux checks on every final walker;
- minimum effective-population and descendant-survival thresholds;
- all six transverse axis-polarization modes; and
- two independent `V=0.90,L=12` seed families.

The forward windows agree within `12%`; the population control agrees within
`12%`; and the three start families agree with the primary result within
`20%`.

The genealogy control uses quantities that measure statistical support
directly: effective population must remain above `85%`, every four-sweep
forward cohort must retain at least `16` distinct labels, and every fitted
`tau=6` origin must retain at least `10` distinct original lineages. Fractions
and absolute minima are printed in the receipt.

These controls bound the implemented estimator. They are not a rigorous
finite-population or autocorrelation theorem.

## 8. Program consequence and axiom boundary

The light stack now contains, on one finite local carrier:

```text
exact Gauss constraint and local ring dynamics
 -> static transverse RK tensor and positive magnetic response
 -> positive finite-detuning topological electric stiffness
 -> charge Coulomb response with the same U
 -> direct finite-detuning transverse linear spectral crossover.
```

That is substantial TOE-facing progress because the photon-phase bridge no
longer depends only on importing the existence of linear dynamics from the
spin-liquid literature. The shortest remaining light-sector physics test is
now the thermodynamic continuation of this measured crossover, not another
static Maxwell identity.

The source does not identify this emergent gauge boson as the empirical
electromagnetic photon. It does not derive the cubic Hamiltonian from
Admissibility, compile the coarse link/ring representation into the final
homogeneous physical-site law, couple this carrier to the repo's dynamical
matter realization, or supply Record-formation probabilities.

No axiom edit follows. The lattice, ice constraint, ring Hamiltonian,
couplings, sector starts, and observable are supplied model content.
Admissibility permits but does not select them; Record is not used.

## 9. Prior-art and contribution boundary

The cubic spin-half model, RK point, dual Maxwell description, and stable
adjacent `U(1)` Coulomb phase are due to M. Hermele, M. P. A. Fisher, and
L. Balents,
[“Pyrochlore Photons: The U(1) Spin Liquid in a S=1/2 Three-Dimensional
Frustrated Magnet”](https://arxiv.org/abs/cond-mat/0305401) (2004).

This source makes no priority claim for the model, the forward-walking
method, or the expected crossover form. Its repo-specific contribution is
the reproducible joined calculation: exact small-orbit calibration, direct
RK null ladder, two finite detunings, `L` through `14`, fixed-window spectral
fits, mass and pure-law controls, static-dynamic coefficient comparison, and
population/component/forward-projection checks on the same carrier used by
the static stack.

## 10. Executable evidence

The paired runner must finish with zero failures. It prints:

- exact and projected `L=2` correlations;
- every `omega_L` and its outer-population error;
- all three time-window estimates;
- raw polarization spread and phase-leakage diagnostics;
- RK and finite-detuning crossover coefficients with covariance errors;
- mass coefficient and `Delta chi^2`;
- the joint detuning coefficient;
- `K_dyn=c^2/U`;
- forward-length, population, and component controls; and
- the final `TOTAL: PASS=... FAIL=0` line.

## No-Go Discipline Gate

This positive finite-volume result sits next to a tempting thermodynamic
claim. The gate keeps the executed crossover separate from an unexecuted
infinite-volume masslessness theorem.

### N1 — Alternative route enumeration

| Route | Outcome |
|---|---|
| exact `L=2` Green correlator | **Positive calibration.** |
| RK `L=6,...,14` dynamical ladder | **Positive control:** `z=2`, `omega proportional q^2`. |
| finite-detuning forward walking | **Positive:** resolved transverse decays. |
| `omega^2=c^2q^2+a^2q^4` | **Selected finite-volume crossover.** |
| pure linear or pure quadratic law | **Tested negative on the declared matrix.** |
| positive mass term | **Not resolved:** less than two sigma and insignificant fit gain. |
| real-time continuation | **Open.** |
| larger-volume/thermodynamic pole | **Open.** |
| same-detuning magnetic twist | **Open.** |

### N2 — Wall-independence and collapse audit

The remaining light-phase wall combines larger-volume dynamics,
thermodynamic control, and same-detuning magnetic response. It does not
collapse the independent physical-site compiler, matter coupling,
Admissibility selection, Record formation, or empirical identification
walls. A larger dynamic lattice would not select the law; a compiler would
not prove a massless spectrum.

### N3 — Hidden-condition scan

The supplied cubic graph, even periodic volumes, zero-flux component starts,
Hamiltonian, detunings, constant trial vector, walker counts, warmup/burn
times, measurement origins, forward lengths, time windows, momenta, and fit
families are explicit. Outer populations, not repeated origins, set the
reported errors. The square-move components above `L=2` are not classified.

No physical time unit, light speed, electric charge, or experimental field
normalization is supplied.

### N4 — Residual matching

| Surface | Residual there | Match here |
|---|---|---|
| finite-detuning stiffness parent | direct transverse dynamics open | **direct partial resolution:** finite-volume spectral crossover |
| static charge parent | dynamical pole absent | **direct partial resolution:** `c^2>0` and `c^2/U>0` |
| RK photon parent | linear dynamics imported | **reduced dependence:** direct two-detuning measurement |
| QMC connectivity PR #7942 | update is component-restricted | **matched boundary:** independent projector and three start controls, still component-scoped |
| minimal axioms | law selection absent | **unmatched:** Hamiltonian remains supplied |

### N5 — Rhetoric and resolution audit

“Linear spectral crossover” means a positive `q^2` term in `omega^2` after
the measured RK `q^4` control is subtracted. It does not mean exact linearity
at every tested momentum. “No mass detected” means the stated two-sigma and
fit-improvement tests fail to resolve `m^2`; it does not mean an exact
masslessness theorem. “Photon” is used only for the conditional emergent
gauge mode, not empirical electromagnetism.

The five-resolution certificate is:

```text
per_element: every elementary square transition and branch factor;
per_site: Gauss charge and final link occupations;
per_mode: six first-momentum transverse modes and their cubic average;
per_block: exact L=2 plus projector L=6,8,10,12,14;
lattice_wide: finite periodic boxes, not the thermodynamic limit.
```

### N6 — Partial-closure paths and primitive boundary

No axiom or approved primitive is added. Positive continuations are:

- extend the low-momentum ladder beyond `L=14` with independent populations;
- use a loop/cluster or gauge-reduced method to reduce ancestry noise;
- measure a same-detuning magnetic twist and compare it directly to
  `c^2/U`;
- couple mobile charges and measure the matter-photon continuum; and
- compile the carrier into the homogeneous physical-site law.

### N7 — Steelman

A hostile reviewer can correctly say that a sum of exponentials fitted over
`tau=2,...,6` need not equal the exact lowest eigenvalue, that descendant
ancestry becomes sparse on the largest boxes, and that five momenta cannot
prove an infinite-volume pole. They can also note that the individual
largest-volume polarizations are noisy and that the magnetic comparison uses
nearby RK `K`, not same-detuning `K`. These are why the theorem is bounded.

The strongest positive reply is also limited: the exact small orbit, RK null
ladder, two detunings, fixed windows, `L=14` extension, two `L=12` seed
families, and estimator/component controls all point to the same crossover.

### N8 — Cross-cycle echo and failed-attempt ledger

The first scout propagated every `tau` cohort to one common endpoint. That
left only a few percent of early ancestors and produced noisy plateaus. The
retained algorithm gives every cohort the same forward length and explicitly
reports survival.

The first production pass then failed two overstrong interpretation checks.
A raw polarization-spread cut treated six correlated symmetry images as
independent estimates. It was replaced by an exact cubic-orbit closure check,
while raw spreads remain printed. A nonnegative fit was required to choose
exactly `m^2=0`; this was replaced by the statistically meaningful questions
of whether `m^2` reaches two sigma or improves `chi^2` by four. Neither does.

The first cached expanded run also failed a percentage-only genealogy check:
the `L=14` effective population was about `87%` against an arbitrary `90%`
cut, and a spot check found `12` to `14` fitted-time lineages. The check was
corrected to retain the original `85%` effective-population floor and test
explicit absolute survivor counts. The next complete cache then exposed a
worse `L=14` block with only `12` forward labels and `6` fitted-time origins.
Those floors were not lowered: the retained `V=0.90,L=14` calculation doubles
the population to `1024` walkers. This changes no seed, correlator definition,
fit, or physics threshold.

No failed result was discarded. The first `V=0.90,L=12` family remains in the
final average, a second independent family was added, and the ladder was
extended to `L=14` together with its RK control. Those changes narrow the
claim from “direct thermodynamic photon pole” to the retained finite-volume
linear spectral crossover.

## Falsifiers

This bounded claim fails if the cached runner does not reproduce its final
zero-failure line, or if an independent implementation finds any of:

- the exact `L=2` correlator mismatch exceeds the declared bound;
- Gauss charge or flux changes under an accepted transition;
- the RK ladder does not retain its quadratic decay;
- either finite detuning loses its positive excess `q^2` coefficient;
- a mass term becomes resolved by the declared test;
- forward length, population, or nonlocal starts move the `L=8` gap outside
  the declared tolerances; or
- larger controlled volumes flatten to a positive mass rather than continue
  toward zero.

Run:

```bash
python3 scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py
```
