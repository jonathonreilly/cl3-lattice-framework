# Lower Cubic-Ice Momenta Restore Maxwell Compatibility but Expose an Early-Time RK Control Boundary

**Date:** 2026-09-04

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Parent localization:**
[`SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md`](SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Primary runner:**
[`scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py`](../scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py)

**Primary cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt)

**Supporting runners and receipts:**

- infrared stochastic ladder: [`script`](../scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py), [`receipt`](../logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt);
- preregistered strict join: [`script`](../scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py), [`receipt`](../logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt);
- conditional health-boundary join: [`script`](../scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py), [`receipt`](../logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt).

## Result up front

The new `L=16,18` axial data materially change the finite-volume Maxwell
comparison. When joined to the source-pinned `L=8,10,12,14` ladder, the two
preselected `q^2+q^4+q^6` excess fits give

```text
window 2--6:  c^2 = 0.02086578 +/- 0.00613427,
window 8--14: c^2 = 0.00143067 +/- 0.00919872,
static target: U K = 0.01228909 +/- 0.00116899.
```

The respective target distances are `1.373` and `1.171` combined reported
errors. Fixing the leading coefficient to the independently measured central
`U K` value gives chi-squared values `6.2559` and `3.5127`, below the
predeclared `9.488` four-residual-degree threshold. The corresponding
one-parameter penalties are `1.9548` and `1.3934`, below `3.841`. A constant
squared-mass term is unresolved, a `q^8` extension does not significantly
improve either target fit, and removing either new infrared volume leaves a
coefficient compatible with the full six-volume result.

This is positive finite-volume evidence that the previous normalization
mismatch was a high-momentum truncation effect rather than a demonstrated
failure of `c^2=U K`. It is not a retained determination of that equality.
Two independently visible execution boundaries prevent that stronger claim:

1. The preregistered stochastic ladder is `TOTAL: PASS=2 FAIL=1`. Exact
   counts, Gauss charge, zero electric flux, effective-population fraction,
   forward genealogy, correlator positivity, and imaginary residual all
   satisfy their checks, but the minimum number of distinct origins surviving
   to `tau=16` is `18`, below the declared floor of `40`.
2. The conditional numerical join is `TOTAL: PASS=10 FAIL=1`. Its sole failed
   physics control is an early-window RK direct-spectrum coefficient
   `-0.00192094 +/- 0.00049902`, or `-3.849` reported errors from zero. The
   three later windows are consistent with zero.

The strict join correctly refuses the non-green ladder and is preserved as a
nonzero receipt. The conditional join was added after the result; it accepts
only this exact `2/1` health signature and then executes the original
preregistered numerical fit without changing its models or thresholds. Its
`10/1` status is also preserved. The green primary runner is only a
source-pinned localization of that failure; its `3/3` checks certify input
coverage and finite arithmetic, not physical acceptance.

## 1. New infrared measurements

The stochastic runner measures the same staggered transverse observable and
the same four fitted-time windows as the parent ladder. It adds two lower
lattice momenta at the detuned point `V=0.95` and at the RK control `V=1.00`:

| coupling | `L` | `tau=2--6` | `tau=6--12` | `tau=8--14` | `tau=10--16` |
|---:|---:|---:|---:|---:|---:|
| 0.95 | 16 | `0.084514 +/- 0.003244` | `0.086122 +/- 0.004536` | `0.081119 +/- 0.004585` | `0.077796 +/- 0.007371` |
| 0.95 | 18 | `0.066003 +/- 0.004320` | `0.068902 +/- 0.003290` | `0.065730 +/- 0.003097` | `0.064071 +/- 0.004577` |
| RK | 16 | `0.046070 +/- 0.000380` | `0.046677 +/- 0.000399` | `0.046648 +/- 0.000423` | `0.047072 +/- 0.000347` |
| RK | 18 | `0.036044 +/- 0.000274` | `0.037248 +/- 0.000252` | `0.037106 +/- 0.000337` | `0.037170 +/- 0.000372` |

The detuned gaps fall from about `0.0845` at `L=16` to about `0.0660` at
`L=18`. This is the downward infrared bend required by the parent
high-momentum localization. The data are generated by independent outer
populations, not by extending or refitting the parent trajectories.

The declared health summary is

```text
minimum effective-population fraction = 0.939055,
minimum distinct tau=16 origins        = 18,
minimum forward descendants            = 92.
```

The effective-population threshold is `>0.85` and the two genealogy floors
are `>=40`. Thus the aggregate check fails only because `18 < 40`. The
receipt does not identify which of the four rows owns that minimum, so the
conditional analysis must not silently promote any late-time result to a
green stochastic determination.

## 2. Source-pinned Maxwell comparison

For each volume and fitted-time window, the joined response is

```text
y(q) = omega_0.95(q)^2 - omega_RK(q)^2,
q = 2 sin(pi/L).
```

The target is parsed from the independent source-pinned charge/flux and
magnetic-twist receipts:

```text
U K = 0.01228909 +/- 0.00116899.
```

It is not copied from the spectral fit. The six-volume excess results are:

| window | free `q^6` `c^2` | free chi-squared | fixed-`UK` chi-squared | fixed penalty |
|---:|---:|---:|---:|---:|
| `2--6` | `0.02086578 +/- 0.00613427` | `4.3010` | `6.2559` | `1.9548` |
| `6--12` | `0.02493498 +/- 0.00746873` | `2.4121` | `5.2790` | `2.8669` |
| `8--14` | `0.00143067 +/- 0.00919872` | `2.1193` | `3.5127` | `1.3934` |
| `10--16` | `0.00025721 +/- 0.01212239` | `2.5157` | `3.5008` | `0.9851` |

The first and third rows are the preselected target windows. Both retain a
positive central coefficient, are compatible with `U K`, pass the fixed
central-target fit and penalty checks, and are compatible with one another.
The two unselected windows are reported to show the time dependence rather
than used to replace either target.

The mass and higher-order controls for the target windows are:

| window | `mass^2` | mass improvement | `q^8` improvement |
|---:|---:|---:|---:|
| `2--6` | `0.00132101 +/- 0.00345865` | `0.1459` | `0.8063` |
| `8--14` | `-0.00184519 +/- 0.00495484` | `0.1387` | `0.0093` |

Neither extension crosses the predeclared one-parameter improvement
threshold. This rules out neither a still-higher correction nor a much more
precise mass; it shows only that neither is selected by this finite receipt.

Removing `L=18` gives target-window coefficients
`0.02412701 +/- 0.00761187` and `0.00618925 +/- 0.01553405`. Removing `L=16`
gives `0.01542554 +/- 0.00761080` and
`0.00183443 +/- 0.00949805`. Each is compatible with its corresponding full
fit. The lower-momentum-only `L=12,14,16,18` coefficients are broad and have
negative central values, so the present data establish compatibility, not a
precise positive infrared estimate.

## 3. Why the conditional join remains non-green

The original join includes a direct-spectrum control in addition to the RK-
subtracted excess. At `V=0.95`, the target-window direct coefficients are

```text
window 2--6:  0.01978718 +/- 0.00602777,
window 8--14: 0.00107589 +/- 0.00914656.
```

Both are positive centrally and compatible with `U K`. At RK, where this
direct `q^2` coefficient should be unresolved around zero, the same fits give

```text
window 2--6:  -0.00192094 +/- 0.00049902  (-3.849 errors),
window 6--12:  0.00007516 +/- 0.00051839  (+0.145 errors),
window 8--14: -0.00001313 +/- 0.00077901  (-0.017 errors),
window 10--16: 0.00033588 +/- 0.00115100  (+0.292 errors).
```

Only the earliest window is anomalous. Fixing its RK `q^2` coefficient to
zero costs `delta chi^2=14.8180`. Adding a `q^8` term changes the coefficient
to `-0.00328434 +/- 0.00113686`; fixing that coefficient to zero still costs
`8.3460`. Thus a single added momentum order does not absorb the early-time
effect.

The early-window leave-one-volume-out values are:

| removed volume | RK `c^2` | reported-error distance from zero |
|---:|---:|---:|
| `L=8` | `-0.00256840 +/- 0.00069627` | `-3.689` |
| `L=10` | `-0.00206007 +/- 0.00051327` | `-4.014` |
| `L=12` | `-0.00201126 +/- 0.00053441` | `-3.763` |
| `L=14` | `-0.00160660 +/- 0.00055654` | `-2.887` |
| `L=16` | `-0.00185480 +/- 0.00051656` | `-3.591` |
| `L=18` | `-0.00142927 +/- 0.00091471` | `-1.563` |

The sign survives every removal, and the anomaly remains resolved under five
of six removals. Its significance weakens when `L=18` is removed, so it is
not volume-independent. Combined with its disappearance in every later time
window, the narrow supported classification is an early-time estimator
boundary with some `L=18` leverage. The data do not support calling it a
failure of the long-wavelength Maxwell coefficient.

## 4. Alternative-route stress test

Before assigning that boundary, the retained data were challenged along the
available independent directions:

- **time route:** three later fitted-time windows make the RK `q^2` term
  consistent with zero;
- **model-order route:** adding `q^8` weakens but does not remove the earliest
  anomaly;
- **volume-influence route:** no single volume flips its sign, although
  removing `L=18` makes it unresolved;
- **mass route:** a constant squared-mass term is unselected in either target
  excess fit;
- **infrared-subset route:** `L=12,14,16,18` alone is too imprecise to select
  the leading coefficient but remains compatible with the full fit;
- **direct-versus-subtracted route:** the detuned direct spectrum and the
  subtracted excess are target-compatible, while the control issue is
  isolated to early-time RK;
- **genealogy route:** the failed `tau=16` origin floor independently prevents
  promotion of the late result; and
- **forward route:** only fixed `F=6` is present here, so no larger-volume
  paired forward-length conclusion is available.

These checks do not prove that imaginary-time contamination is the unique
cause. They do show that the live alternatives are narrower than a generic
failure of Maxwell matching.

## 5. Execution provenance

The expensive child completed in `26040.72` seconds. During execution, other
repo work changed only parent-directory filesystem metadata. The cache
wrapper therefore rejected the result under its strict pre/post execution-
identity check even though both content identities were identical:

```text
runner sha256:
80108851a3d3a77e8e2593502abfa17ee72eab7174ad7043f039afe2e5133867

declared-input fingerprint sha256:
535d78a5839e9248fddf6f57407fa898e16f5b6bb4362f041776b0e2c93b9672
```

The complete live stdout was copied before the wrapper resumed. The canonical
cache was reconstructed with those exact content identities, the original
`nonzero_exit` status, exit code `1`, and byte-for-byte identical stdout. Its
stderr records the recovery provenance. No failed check was edited or
discarded.

## 6. Program and axiom consequence

The light branch has made a real but bounded advance:

```text
previous state:
  full L=8,10,12,14 three-gradient fit rejected c^2 = U K;

new state:
  adding L=16,18 makes both target-window q^6 fits compatible with U K,
  and the fixed-U K model passes its declared fit and penalty tests;

remaining boundary:
  the infrared receipt misses its tau=16 origin-diversity floor,
  and the early RK direct-spectrum control carries a spurious q^2 term.
```

No axiom edit follows. The candidate Maxwell relation is a property to derive
for this supplied carrier, not an admissible primitive to insert into the
axioms. No official TOE score moves without independent classification.

The shortest positive follow-up is not another high-momentum orbit search. It
is a source-pinned `L=16,18` replay with enough origin diversity to satisfy the
existing `tau=16` floor, paired forward lengths at those same volumes, and a
declared late-time primary window. That one campaign can decide whether the
green late RK control and target-compatible excess survive the two remaining
estimator boundaries.

## Falsifiers

This bounded record fails if an independent replay finds any of:

- a live-log stdout different from the canonical infrared cache stdout;
- different runner or declared-input content hashes at launch and completion;
- an infrared receipt whose failure is not isolated to the declared genealogy
  check;
- any conservation, sector, positivity, or imaginary-residual failure hidden
  by the conditional parser;
- target-window `q^6` coefficients or fixed-target chi-squared values different
  from those reported above;
- a green conditional join rather than its preserved `TOTAL: PASS=10 FAIL=1`;
- an RK early-window anomaly that remains comparably resolved in the three
  later windows; or
- a localization receipt other than `TOTAL: PASS=3 FAIL=0`.

Run:

```bash
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py --check-only
```
