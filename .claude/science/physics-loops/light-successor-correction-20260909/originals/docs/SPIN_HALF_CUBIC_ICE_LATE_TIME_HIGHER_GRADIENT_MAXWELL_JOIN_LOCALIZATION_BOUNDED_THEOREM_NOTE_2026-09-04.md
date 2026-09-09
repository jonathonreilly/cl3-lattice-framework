# Late-Time Spin-Half Cubic-Ice Spectroscopy Localizes the Maxwell Join to Higher-Gradient Resolution

**Date:** 2026-09-04

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct magnetic-response parent:**
[`SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md`](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md)

**Direct transverse-spectrum parent:**
[`SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py`](../scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt)

## Result up front

The weak-detuning spin-half cubic-ice Maxwell comparison is not repaired by
projecting the transverse correlator to later imaginary time. Its apparent
tension is removed, at the resolution of the tested finite-volume ladder, by
including the first omitted symmetry-allowed momentum correction.

Matched `V=0.95` and RK populations on `L=8,10,12,14`, extended through
`tau=16`, give the two-term excess fit

```text
omega_0.95(q)^2 - omega_RK(q)^2 = c^2 q^2 + b q^4.
```

Its inferred coefficient does not fall with projection time:

```text
tau window 2--6:  c^2 = 0.032685 +/- 0.003233,
tau window 8--14: c^2 = 0.040114 +/- 0.006483,
tau window 10--16: c^2 = 0.045545 +/- 0.006673.
```

The early and primary late values differ by only `1.03` combined errors, and
the two late windows agree. Fixing the two-term fit to the independently
measured static value

```text
U K = 0.012289 +/- 0.001169
```

costs `Delta chi^2=18.42` in the primary late window. Drift with the fitted
time window is therefore not the explanation of the original comparison on
this finite matrix. This statement holds at the fixed six-sweep forward
projection used here; it does not remove the separate finite-forward-length
systematic described below.

The same four points also show why that conclusion need not be a normalization
failure. With the next analytic term included,

```text
omega_0.95(q)^2 - omega_RK(q)^2
    = c^2 q^2 + b q^4 + d q^6,
```

fixing `c^2=U K` gives in the primary late window

```text
b =  0.171837 +/- 0.022559,
d = -0.251040 +/- 0.057066,
chi^2 = 1.646 for two residual degrees of freedom.
```

The fixed-static three-term fit is acceptable in all four projection windows
and never costs `Delta chi^2 >= 4` relative to a free three-term fit. If `c^2`
is instead left free, the primary late result is

```text
c^2 = 0.014883 +/- 0.021486,
```

which is compatible with `U K` but not independently resolved.

Thus the previous finite-volume tension is absorbed at this resolution by the
first omitted analytic correction: the `q^2+q^4` truncation was being asked to
identify an infrared coefficient over momenta where a `q^6` shape is already
visible conditional on fixed `U K`. The calculation removes evidence for a
static-dynamic inconsistency. It does **not** yet establish the equality
`c^2=U K`, because the current momenta cannot separate `c^2`, `q^4`, and
`q^6` precisely when all three float.

The shortest remaining positive test is lower momentum, not longer imaginary
time: extend the matched ladder to `L=16,18` or constrain the higher-gradient
coefficient independently. A high-statistics forward-length control must then
test that the inferred infrared coefficient is stable as the descendant
projection grows. No axiom edit is justified.

## 1. Question and decision logic

The magnetic-response parent measured a positive relaxed `K` on the same
coupling where the charge-flux parent measured `U`. Their product predicts a
Maxwell velocity. The first transverse-spectrum fit returned a larger
coefficient, with a `2.729`-error difference at `V=0.95`.

There were two cheap and physically distinct explanations:

1. the projected correlator had not reached its lowest transverse state; or
2. the available momenta were outside the range where two gradient terms
   isolate the coefficient of `q^2`.

They make different predictions. Explanation 1 requires the effective gap and
inferred `c^2` to move systematically at later time. Explanation 2 permits a
stable gap but requires the first omitted analytic term to absorb the
finite-momentum curvature without changing the independently fixed `U K`.

The runner tests both on the same stochastic populations and reports both
outcomes. It does not choose a fit after seeing only one time window.

## 2. Matched late-time estimator

The calculation reuses the exact positive Green projector and transverse
first-harmonic operator from the spectral parent. It measures four time origins
per population, propagates each origin six forward sweeps to control
mixed-estimator bias, and follows the correlator through `tau=16`. Statistical
errors are taken across independent populations rather than treating those
within-population origins as independent.

The forward length is fixed at six sweeps. The spectral parent separately
reported the lower-statistics `L=8` sequence

```text
F=0: 0.234663, F=2: 0.214491, F=4: 0.219052, F=6: 0.240189.
```

Its twelve-percent span passed that parent's bounded stability check but is
not negligible compared with the normalization question here. The present
larger-population `F=6` value, `0.227459 +/- 0.002105`, lies inside that span.
This note therefore isolates fitted-time drift and finite-momentum model
order; it does not claim a forward-length extrapolation.

The finite matrix is

```text
V=0.95 and V=1.00 (RK),
L=8,10,12,14,
windows 2--6, 6--12, 8--14, and 10--16.
```

At `V=0.95`, the `L=8,10,12` rows use six independent populations of `2048`
walkers and `L=14` uses four populations of `3072`. The matched RK control
uses half those populations. Errors are delete-one-population jackknife
errors, not time-slice regression errors.

For each length the runner subtracts the matched RK squared gap before fitting:

```text
y(q) = omega_0.95(q)^2 - omega_RK(q)^2,
q = 2 sin(pi/L).
```

This removes the directly measured RK `q^4` carrier contribution without
assuming its coefficient or extrapolating it from another volume set.

## 3. Late-time spectrum

The reported gap ladder is:

| coupling | `L` | window `2--6` | window `6--12` | window `8--14` | window `10--16` |
|---:|---:|---:|---:|---:|---:|
| 0.95 | 8 | `0.227459 +/- 0.002105` | `0.225571 +/- 0.005920` | `0.212142 +/- 0.013521` | `0.200953 +/- 0.015134` |
| 0.95 | 10 | `0.166280 +/- 0.001541` | `0.165382 +/- 0.003382` | `0.175927 +/- 0.007154` | `0.170540 +/- 0.012352` |
| 0.95 | 12 | `0.122942 +/- 0.002131` | `0.123095 +/- 0.004222` | `0.127920 +/- 0.004748` | `0.127187 +/- 0.004562` |
| 0.95 | 14 | `0.103678 +/- 0.004344` | `0.103133 +/- 0.001913` | `0.105330 +/- 0.002852` | `0.104357 +/- 0.002551` |
| RK | 8 | `0.177175 +/- 0.001295` | `0.175196 +/- 0.000501` | `0.173903 +/- 0.003220` | `0.175827 +/- 0.005392` |
| RK | 10 | `0.116420 +/- 0.000780` | `0.115841 +/- 0.001432` | `0.115427 +/- 0.001709` | `0.114165 +/- 0.001761` |
| RK | 12 | `0.082318 +/- 0.000478` | `0.081900 +/- 0.000480` | `0.082161 +/- 0.000786` | `0.082688 +/- 0.001188` |
| RK | 14 | `0.060838 +/- 0.000154` | `0.060587 +/- 0.000435` | `0.060326 +/- 0.000346` | `0.059544 +/- 0.000840` |

There is no coherent downward drift across sizes. The noisiest row, `L=8`,
does fall at the last window, but `L=10,12,14` do not reproduce that direction.
The fit-level coefficient is correspondingly stable within errors rather than
approaching `U K`.

The minimum effective-population fraction is `0.972682`. At `tau=16` every
population retains at least `91` origin genealogy labels, and every
forward-walked endpoint retains at least `352`. All local recounts, Gauss
sectors, and zero-electric-flux checks pass.

## 4. Two-term versus three-term gradient fits

The two-term results are:

| time window | free `c^2` | free `b` | free `chi^2` | fixed-`U K` `chi^2` | fixed penalty |
|---:|---:|---:|---:|---:|---:|
| `2--6` | `0.032685 +/- 0.003233` | `0.005493 +/- 0.007651` | `5.150` | `44.959` | `39.808` |
| `6--12` | `0.034553 +/- 0.003708` | `0.001131 +/- 0.011768` | `1.040` | `37.092` | `36.051` |
| `8--14` | `0.040114 +/- 0.006483` | `-0.009954 +/- 0.023455` | `3.149` | `21.569` | `18.421` |
| `10--16` | `0.045545 +/- 0.006673` | `-0.040520 +/- 0.026256` | `1.460` | `26.299` | `24.839` |

Those numbers make the original tension more stable, not less, when the model
is held to two terms.

The three-term results are:

| time window | free `c^2` | free `chi^2` | fixed-`U K` `b` | fixed-`U K` `d` | fixed `chi^2` | fixed penalty |
|---:|---:|---:|---:|---:|---:|---:|
| `2--6` | `0.015247 +/- 0.011928` | `2.842` | `0.109810 +/- 0.010901` | `-0.121782 +/- 0.019883` | `2.904` | `0.062` |
| `6--12` | `0.033354 +/- 0.011838` | `1.028` | `0.137576 +/- 0.015095` | `-0.176992 +/- 0.032208` | `4.195` | `3.167` |
| `8--14` | `0.014883 +/- 0.021486` | `1.632` | `0.171837 +/- 0.022559` | `-0.251040 +/- 0.057066` | `1.646` | `0.015` |
| `10--16` | `0.026676 +/- 0.024251` | `0.805` | `0.176122 +/- 0.021874` | `-0.290682 +/- 0.058792` | `1.157` | `0.352` |

The fixed-`U K` fit has two residual degrees of freedom. The free fit has one.
The reported fixed-fit coefficient errors propagate both spectral errors and
the independent `U K` uncertainty. At both late windows the fixed fit resolves
positive `b` and negative `d` by more than three reported errors. This
establishes that the first omitted
analytic shape is visible conditional on the independently measured `c^2`.
It does not establish a universal value of `b` or `d`, and their drift across
windows warns against treating either as an asymptotic coefficient yet.

Likewise, the free three-term `c^2` is compatible with `U K` but broad. Four
momenta can test the fixed prediction, but they cannot precisely estimate
three correlated coefficients. Lower momentum is required to turn
compatibility into a measured equality.

## 5. Program and axiom consequence

This is positive TOE-facing progress because it changes the scientific choice
at the light frontier:

```text
later fitted-time window: tested and deprioritized,
two-term normalization discrepancy: not supported,
higher-gradient finite-q correction: directly resolved at fixed U K,
remaining decisions: lower-q isolation of c^2 and forward-length stability.
```

The light carrier now has separately measured electric response, Coulomb
charge response, relaxed magnetic response, and transverse dynamics with no
remaining demonstrated inconsistency among them. What remains is a positive
end-to-end equality test in the infrared, plus the thermodynamic and
Lorentz/continuum limits already declared by the parent stack.

A companion exact certificate,
[`SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md`](SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md),
shows that proper cubic covariance and gauge transversality leave only the
quadratic Maxwell tensor. The live spectral question is therefore whether
this carrier reaches that analytic infrared regime and with which scalar
coefficient, not whether a second cubic quadratic speed can be fitted.

No axiom edit is justified. The result concerns how a supplied local
Hamiltonian approaches its long-wavelength effective theory. Adding the
finite-volume correction or the equality `c^2=U K` to the axioms would assume
the supplier physics that this campaign is meant to derive.

No official TOE score moves until independent classification. The scientific
advance is a falsified explanation, a removed apparent inconsistency, and a
sharply cheaper next experiment.

## 6. Structured wall audit

### N1 — Alternative routes

The campaign compared three routes: later projection, lower momentum, and an
expanded analytic gradient model. Later projection was the cheapest possible
repair and was tested first. The expanded model uses the already available
four-volume data and identifies whether lower momentum is actually needed.
Direct `L=16,18` projection remains the decisive next route.

### N2 — Wall independence

The late-time conclusion uses raw correlator evolution and does not depend on
the static `U K` value. The higher-gradient compatibility does depend on the
independent static measurement, but its fit coefficients do not reuse the
magnetic populations. A failure of the static parent would remove the
quantitative join, not the late-time spectral result.

### N3 — Hidden-wall scan

The main risks are population genealogy collapse, a drifting RK subtraction,
one noisy time window, finite forward projection, correlated fit parameters,
and post-selected gradient order. The runner retains four predeclared windows,
matched RK populations, outer-population jackknives, explicit genealogy
floors, and both the failing two-term and successful three-term fits. The
parent's forward-length spread is reported above rather than folded into the
statistical error. The `q^6` term is the first analytic cubic-symmetric
correction omitted from the tested one-dimensional momentum ray; terms beyond
it remain uncontrolled.

### N4 — Residual matching

The residual is no longer a demonstrated difference between static and dynamic
normalizations. It is the inability of the current momentum range to estimate
`c^2` independently once the visible higher-gradient curvature is admitted,
together with the unextrapolated forward length. The next campaign must add
lower `q` or independently constrain the correction, then vary the forward
projection; more fitted-time samples at the same sizes do not match either
residual.

### N5 — Rhetoric audit

“Localizes” does not mean “closes.” “Compatible” does not mean “derived” or
“confirmed.” “Resolved corrections” refers only to the fixed-`U K` three-term
fit on this finite matrix. This note claims neither a thermodynamic photon pole
nor Standard Model electromagnetism.

### N6 — Partial-closure path

Even without a lower-momentum run, the campaign removes fitted-time drift as
the leading explanation and prevents the program from treating a misspecified
two-term fit as an axiom or normalization problem. The full late-time ladder
and its matched RK control remain reusable for other spectral estimators; the
forward-length systematic remains explicit rather than being hidden in its
statistical errors.

### N7 — Steelman

A hostile reviewer can say that one additional parameter predictably improves
a four-point fit, that `q^6` may merely emulate still higher terms, and that
the fixed-static coefficient imports uncertainty not sampled jointly in the
fit. Those objections prevent a closure claim. They do not restore the
two-term rejection as evidence of inconsistency: the first allowed omitted
term fits all windows at the independently declared central `U K`, with low
absolute chi-square and small penalty relative to a free coefficient. The
honest conclusion is under-resolution of the infrared coefficient.

### N8 — Cross-cycle echo and failed-attempt ledger

The campaign began with the explicit hypothesis that a longer projection
would lower the weak-detuning coefficient. A single `L=14` scout appeared to
support it: its terminal gap fell from about `0.1040` to `0.0847`. That result
was not promoted. Four full `L=14` populations returned
`0.104357 +/- 0.002551`, and the complete ladder falsified the hypothesis.

The first production runner therefore ended with three failed checks. Its raw
result was preserved and analyzed rather than discarded or made to pass by
loosening thresholds. The first omitted `q^6` term was then added uniformly to
all four already declared windows. It restored compatibility without changing
any population, seed, gap, error, momentum, or static target. Both the failed
two-term comparison and the reported higher-gradient comparison remain in the
final receipt.

No failed or interesting result was discarded.

## Falsifiers

This bounded claim fails if the cached runner does not reproduce its final
zero-failure line, or if an independent implementation finds any of:

- a local recount, Gauss-law, or electric-flux failure;
- genealogy below the declared floors;
- a coherent late-time decrease hidden by the population jackknife;
- a changed conclusion under the same matched data and stated weighted fits;
- a significant penalty for fixed `c^2=U K` after the `q^6` term is included;
- loss of the visible higher-gradient correction under increased populations;
- a forward-length ladder that moves the inferred infrared coefficient beyond
  the stated statistical compatibility; or
- a reanalysis of the declared ladder in which fixed `U K` plus `q^4+q^6`
  carries a significant fit penalty.

Run:

```bash
python3 scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py
```
