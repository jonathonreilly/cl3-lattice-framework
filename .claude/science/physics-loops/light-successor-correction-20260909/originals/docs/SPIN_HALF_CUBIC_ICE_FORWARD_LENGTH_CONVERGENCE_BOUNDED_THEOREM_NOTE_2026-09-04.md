# Fixed-Volume Forward Projection Converges for the Spin-Half Cubic-Ice Transverse Gap

**Date:** 2026-09-04

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct spectral parent:**
[`SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md`](SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**

[`scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py`](../scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py)

**Cached receipt:**

[`logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt)

**Supporting data and correction runners:**

- [`scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py`](../scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py)
- [`scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py`](../scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py)
- [`scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py`](../scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py)
- [`scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py`](../scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py)

**Supporting cached receipts:**

- [`logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt)
- [`logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt)
- [`logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt)
- [`logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt)

## Result up front

At fixed `L=8` and `V=0.95`, the projected transverse gap is stable when the
forward-walking suffix grows from six through twenty sweeps. The higher-
statistics, predeclared plateau test uses ten independent outer populations,
`3072` walkers per population, and the paired covariance among seven forward
lengths. It gives

```text
time window 2--6:
  F=12,14,16,20 plateau = 0.230080 +/- 0.001412,
  Hotelling statistic = 5.239 < 16.766,
  raw plateau span = 1.04 percent.

time window 8--14:
  F=12,14,16,20 plateau = 0.232216 +/- 0.005219,
  Hotelling statistic = 2.045 < 16.766,
  raw plateau span = 2.35 percent.
```

Every held-out `F=6,8,10` contrast lies below the predeclared two-sided
Student threshold of `2.262` reported errors. The largest contrast is `1.059`
in the early window and `0.846` in the late window. The matched squared-gap
excess over the RK control passes the same plateau and held-out-contrast
tests.

This removes inadequate forward projection as a supported explanation of the
finite-momentum Maxwell mismatch at the tested volume. It strengthens the
spectral parent's localization: lower momentum and gradient-order resolution,
not a longer descendant suffix at `L=8`, are now the live tests.

The result is deliberately not an infrared or thermodynamic statement. The
projection scale may worsen as the gap falls with increasing `L`. A paired
forward-length control at the largest infrared volumes is therefore still
required before the coefficient comparison can be closed.

## 1. Why paired forward lengths are required

The positive Green-function estimator samples a population at a common time
origin and then follows its descendants for a chosen number of sweeps before
measuring the transverse endpoint. Different forward lengths taken from the
same trajectory are strongly correlated. Treating them as independent would
inflate the apparent information and could manufacture either convergence or
drift.

Both data runners therefore retain all requested endpoints from each shared
trajectory. Statistical covariance is estimated across independent outer
populations after the nonlinear gap extraction. The decision runners use the
full paired covariance for plateau tests and for comparison with held-out
shorter suffixes.

The first receipt sampled

```text
F = 2,4,6,8,10,12,
six outer populations,
2048 walkers at V=0.95,
1024 walkers at RK.
```

The independent extension sampled

```text
F = 6,8,10,12,14,16,20,
ten outer populations,
3072 walkers at V=0.95.
```

Both use four time origins, follow the correlator through `tau=16`, and keep
the local recount, Gauss sector, electric-flux sector, effective-population,
origin-genealogy, and forward-survival controls.

## 2. Preserved failed controls and their correction

The first data receipt intentionally remains nonzero:

```text
TOTAL: PASS=3 FAIL=1
```

Its failed check required a full-rank long-forward covariance block at both
couplings. At RK, however, `delta V=0` makes every projector weight uniform.
Systematic resampling is then the identity, so extending the forward suffix
does not alter any endpoint on the shared trajectory. Every RK gap is exactly
the same for every `F`, and its paired covariance has rank one. That is a
structural control of the estimator, not missing stochastic information. The
receipt is preserved rather than rewritten around the outcome.

The first decision runner also remains nonzero:

```text
TOTAL: PASS=6 FAIL=2.
```

It used the asymptotic two-degree-of-freedom chi-squared cutoff `5.991` for a
covariance estimated from only six outer populations. The early raw and
matched-excess statistics were `7.300` and `7.354`; the late statistics were
`0.139` and `0.137`. Raw motion was already small, but the nominal early gate
failed.

The finite-sample reanalysis was specified separately and consumes the
unchanged failed receipt. For two contrasts and six populations, it uses the
Hotelling-to-`F` threshold

```text
p (n-1) / (n-p) F_(p,n-p;0.95) = 17.361,
```

and a two-sided `t_5` threshold `2.571` for the fixed `F=6` contrast against
the equal-weight long mean. Both early statistics pass that finite-sample
threshold, both late statistics pass, and all four fixed contrasts pass. The
correction runner reports `TOTAL: PASS=7 FAIL=0` while retaining both original
failures as inputs.

Because the gap is a nonlinear statistic and its covariance is a delete-one-
population jackknife estimate, the finite-sample calibration is a bounded
multivariate-normal approximation rather than an exact distribution-free
theorem. The higher-statistics extension tests whether the conclusion
survives more populations and a longer plateau instead of relying on that
single correction.

## 3. Higher-statistics forward ladder

The complete high-statistics gap rows are:

| time window | `F=6` | `F=8` | `F=10` | `F=12` | `F=14` | `F=16` | `F=20` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `2--6` | `0.228115` | `0.227437` | `0.229851` | `0.230452` | `0.229702` | `0.230172` | `0.228056` |
| `6--12` | `0.222228` | `0.220860` | `0.220360` | `0.220330` | `0.218599` | `0.215523` | `0.219383` |
| `8--14` | `0.225793` | `0.230206` | `0.232127` | `0.229389` | `0.227894` | `0.229114` | `0.233340` |
| `10--16` | `0.251305` | `0.261075` | `0.257236` | `0.258276` | `0.263066` | `0.267766` | `0.261222` |

The runner reports `TOTAL: PASS=4 FAIL=0`. Its minimum effective-population
fraction is `0.994933`; the minimum `tau=16` origin diversity is `516`, and
the minimum forward-endpoint diversity is `413`. Both predeclared covariance
blocks are full rank.

The result decision was not made in that data runner. The separate join had
already declared the long set `F=12,14,16,20`, the two windows `2--6` and
`8--14`, the finite-sample calibration, the held-out shorter lengths, and the
five-percent raw-span bound.

For three contrasts and ten outer populations its Hotelling threshold is
`16.766`; its two-sided `t_9` threshold is `2.262`. The results are:

| quantity | window `2--6` | window `8--14` |
|---|---:|---:|
| raw plateau | `0.230080 +/- 0.001412` | `0.232216 +/- 0.005219` |
| raw Hotelling statistic | `5.239` | `2.045` |
| maximum held-out contrast | `1.059` | `0.846` |
| raw long-set span | `1.04%` | `2.35%` |
| squared-gap excess | `0.020680 +/- 0.000688` | `0.020860 +/- 0.002710` |
| excess Hotelling statistic | `5.264` | `2.076` |
| maximum excess contrast | `1.059` | `0.841` |

All eight declared decisions pass. The high-statistics `F=6` gaps also
reproduce the first receipt within two combined reported errors. The result is
therefore not an artifact of selecting only one population count, one
forward-length triplet, or one fitted-time window.

## 4. What the result does and does not settle

The direct conclusion is

```text
fixed L=8, V=0.95 transverse gap:
forward suffix F=6,...,20 is statistically plateaued at current resolution.
```

It rules against the specific suggestion that the previously observed
`F=6` spectrum was displaced because descendants had not been propagated far
enough at `L=8`. It does not prove an unbiased infinite-population estimator,
and it does not transfer automatically to `L=14,16,18`, where the physical gap
is smaller and the needed projection length can grow.

The result also does not make the finite-`q` two-term coefficient equal to the
independent static target. The stable `L=8` gap still contains the higher-
gradient curvature localized by the spectral parent. Projection convergence
and infrared model order are separate questions; this receipt closes only the
former at one volume.

The next decisive measurement is a paired shorter-versus-longer forward
control on the largest lower-momentum volumes, combined with the already
declared `q^2+q^4+q^6` Maxwell comparison. It should be run before interpreting
any lower-`q` coefficient shift as physical.

## 5. Axiom boundary

No axiom edit follows. The forward suffix is part of the numerical estimator
for a supplied local Hamiltonian, not a new primitive of Lattice,
Admissibility, Record, or the neighbor-mediated update law. Its convergence
supports the reliability of this carrier calculation at one finite volume;
it neither supplies a universal dynamics rule nor identifies Hamiltonian
imaginary time with Record time.

No official TOE score moves until independent classification. The positive
scientific advance is narrower: one live systematic explanation has been
tested with paired data, corrected finite-sample statistics, and an
independent higher-statistics extension, and it does not account for the
finite-momentum Maxwell comparison.

## Falsifiers

This bounded result fails if an independent replay finds any of:

- a high-statistics data receipt other than `TOTAL: PASS=4 FAIL=0`;
- a high-statistics join other than `TOTAL: PASS=8 FAIL=0`;
- a long-forward raw Hotelling statistic at or above `16.766`;
- a held-out fixed contrast at or above `2.262` reported errors;
- a raw long-forward span at or above five percent;
- a failure of the high-statistics `F=6` result to reproduce the first paired
  receipt within two combined reported errors; or
- a count, sector, genealogy, or finite-correlator health failure.

Run:

```bash
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py --check-only
```
