# Off-Axis Cubic-Ice Spectroscopy Retains One Leading Kernel and Localizes the Maxwell Mismatch to the Highest Momentum

**Date:** 2026-09-04

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Exact tensor parent:**
[`SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md`](SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md)

**Spectral parent:**
[`SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md`](SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md)

**Forward-projection control:**
[`SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md`](SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py`](../scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt)

**Supporting runners and receipts:**

- first individual-mode scout: [`script`](../scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py), [`receipt`](../logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt);
- cubic-orbit scout: [`script`](../scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py), [`receipt`](../logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt);
- corrected staggered scout: [`script`](../scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py), [`receipt`](../logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt);
- production ladder: [`script`](../scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py), [`receipt`](../logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt);
- preregistered join: [`script`](../scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py), [`receipt`](../logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt).

## Result up front

The physical spin-half cubic-ice branch shows no resolved need for different
leading quadratic coefficients along axial, face-diagonal, and body-diagonal
directions. A covariance-aware fit to complete cubic momentum orbits on
`L=8,10,12,14` gives

```text
common c^2 = 0.049253 +/- 0.005510,
common chi^2 = 5.051,
four-independent-c^2 chi^2 = 1.708,
improvement for three added coefficients = 3.343 < 7.815.
```

The independently fitted family coefficients are

```text
axis      0.045741 +/- 0.007543,
face out  0.052759 +/- 0.019288,
face in   0.019401 +/- 0.020471,
body      0.075377 +/- 0.031645.
```

The two face polarizations differ by `0.977` combined reported errors. A
common mass is unresolved, adding family-specific eighth-order momentum terms
does not cross the four-parameter improvement threshold, and removing either
`L=8` or the body family leaves a statistically compatible common
coefficient. These are positive finite-volume tests of the one-coefficient
quadratic tensor structure forced by proper cubic covariance plus gauge
transversality.

They do not yet measure that coefficient reliably. The preregistered
`q^2+q^4+q^6` join rejects the independent static target

```text
U K = 0.0122891 +/- 0.0011690
```

by `6.563` reported errors and gives fixed-target `chi^2=48.117`. That join is
preserved as `TOTAL: PASS=11 FAIL=2`.

The immediate influence test localizes this mismatch to the highest-momentum
`L=8` block. Removing only `L=8` gives

```text
L=10,12,14 common c^2 = 0.031583 +/- 0.015021,
distance from U K = 1.281 reported errors,
fixed-U K chi^2 = 2.763 for four residual degrees of freedom.
```

Removing `L=10`, `L=12`, or `L=14` instead leaves target distances of
`3.030`, `6.578`, and `3.975` reported errors and fixed-target chi-squared
values above the corresponding `9.488` threshold. Removing the body family
from the lower-momentum set also leaves `U K` compatible. Thus the current
data support one leading direction-independent kernel, while the scalar
normalization is underresolved because the highest accessible momentum lies
outside the demonstrated three-gradient range.

This is not a positive determination of `c^2=U K`. The lower-momentum estimate
is broad, the covariance comes from eight outer populations per block, and
the production observable uses a four-sweep forward suffix. The decisive
next evidence is the independent `L=16,18` axial infrared ladder already
specified by the parent campaign, followed by a paired forward check at those
larger volumes.

## 1. Exact tensor question versus physical carrier question

The companion exact calculation starts from all `36` coefficients of a real
symmetric homogeneous-quadratic three-component kernel. Proper cubic
covariance leaves dimension three, gauge transversality leaves dimension six,
and their intersection has dimension one:

```text
K_ij(q) proportional to q^2 delta_ij - q_i q_j.
```

That theorem does not prove that a finite lattice spectrum is analytic,
gapless, or already in its quadratic regime. Off-axis spectroscopy is needed
to test those physical premises. Direction-dependent corrections at fourth
and higher momentum order are compatible with the exact theorem; a second
direction-dependent coefficient at quadratic order is not.

The production fit therefore assigns one common `q^2` coefficient and allows
separate `q^4` and `q^6` coefficients for the four measured families. It
compares that model with four independent leading coefficients, rather than
placing equal finite-momentum gaps into the ansatz.

## 2. Correct staggered electric observable

The microscopic state stores link occupation as zero or one. The ice electric
field used by the axial parent is the centered occupation multiplied by the
bipartite site sign. The off-axis coefficient row must therefore contain

```text
(-1)^(x+y+z) exp(i k dot (x + e_axis/2)) polarization_axis.
```

The link-center phase makes the lattice divergence proportional to
`q_axis=2 sin(k_axis/2)`. Each longitudinal coefficient row then vanishes on
every sampled ice state to machine resolution.

The first scout omitted the bipartite sign in the coefficient passed to the
inherited centered-occupation evaluator. Its separate longitudinal check
inserted the sign explicitly, so that control passed while the transverse
correlators failed. The receipt remains `TOTAL: PASS=3 FAIL=1` with the
resulting non-finite gaps.

The second scout tested whether complete cubic-orbit averaging alone repaired
the signal. It did not, and its `TOTAL: PASS=3 FAIL=1` receipt is also
preserved. The corrected scout applies the missing sign to the same orbit
table and returns `TOTAL: PASS=4 FAIL=0`. The production runner independently
implements that corrected table rather than mutating either failed receipt.

## 3. Cubic-orbit production matrix

For each first-harmonic momentum family, the runner averages the complete
signed-permutation orbit before extracting a decay:

- six axial momenta with two transverse polarizations;
- twelve face-diagonal momenta, retaining the out-of-plane and in-plane
  polarizations as separate families; and
- eight body-diagonal momenta with two transverse polarizations.

There are `52` transverse modes in total. Both momentum signs are present, so
the cubic-family average is not a selected ray or phase convention.

The measured gaps are:

| coupling | `L` | axis | face out | face in | body |
|---:|---:|---:|---:|---:|---:|
| 0.95 | 8 | `0.233088` | `0.409818` | `0.400154` | `0.574926` |
| 0.95 | 10 | `0.161074` | `0.281294` | `0.280681` | `0.379979` |
| 0.95 | 12 | `0.125753` | `0.213750` | `0.217458` | `0.283860` |
| 0.95 | 14 | `0.103163` | `0.170241` | `0.167853` | `0.229134` |
| RK | 8 | `0.174141` | `0.346208` | `0.355045` | `0.516266` |
| RK | 10 | `0.116942` | `0.231126` | `0.231094` | `0.344247` |
| RK | 12 | `0.080968` | `0.160624` | `0.163109` | `0.245058` |
| RK | 14 | `0.060039` | `0.120196` | `0.120755` | `0.180493` |

Every coupling and volume has eight independent outer populations. The
runner emits the full four-family delete-one-population jackknife covariance
for each block. Every covariance is positive definite and full rank; the
largest condition number is `2.46 x 10^2`. The minimum effective-population
fraction is `0.970996`, the minimum fitted-time origin diversity is `172`, and
the minimum forward-endpoint diversity is `247`. Counts, sectors, phase
residuals, and all five declared production checks pass.

## 4. Fits and localization controls

The fit response is the matched squared-gap excess

```text
y_f(q) = omega_0.95,f(q)^2 - omega_RK,f(q)^2,
```

with the detuned and RK covariance propagated through the subtraction. The
static target is parsed from the source-pinned charge/flux and magnetic-twist
receipts; it is not inserted as a comparison to itself.

The full common model has sixteen observations and nine coefficients: one
common `c^2`, plus `q^4` and `q^6` coefficients for each family. Its seven
residual degrees of freedom are sufficient to test the fit. The independent
model adds three leading coefficients. Their nominal improvement threshold is
derived for three added parameters.

The post-result localization keeps every datum and covariance fixed. It
repeats the common fit after removing one volume at a time. Only removal of
the largest lattice momentum, `L=8`, changes both target decisions from fail
to pass. The lower-momentum result also survives removal of the body family:

```text
axis plus both face families, L=10,12,14:
c^2 = 0.029163 +/- 0.016899,
target distance = 0.996 reported errors,
fixed-target chi^2 = 2.017 for three residual degrees of freedom.
```

A diagnostic fit allowing a separate `q^8` coefficient for every family on
the full matrix gives

```text
c^2 = 0.017016 +/- 0.027542,
fixed-target chi^2 = 0.758 for four residual degrees of freedom.
```

It does not cross the four-parameter model-improvement threshold and leaves
`c^2` less than one reported error from zero. It is therefore evidence of
model-order underresolution, not a selected determination. With only three
free residual degrees of freedom, that diagnostic cannot replace new lower-
momentum data.

The covariance decisions use nominal likelihood-ratio thresholds while each
block covariance is estimated from eight populations and the gap is
nonlinear. That finite-sample limitation weakens any sharp rejection; it does
not create the observed fact that only removing `L=8` restores target
compatibility.

## 5. Forward and time limitations

The off-axis production matrix uses the early `tau=2--6` window and a fixed
four-sweep forward suffix. The separate axial forward receipt contains an
`F=4` value near its longer results, but its declared held-out decisions begin
at `F=6`; it does not certify `F=4`. No paired off-axis forward ladder has yet
shown that every direction family shares the longer-suffix stability. The
present result therefore supports the spatial tensor comparison at the tested
estimator settings; it does not close the forward systematic at larger
volumes or for every off-axis family.

Likewise, the late-time axial parent found no coherent fitted-window drift,
but this production run does not repeat the full off-axis orbit matrix at late
time. Lower momentum has higher leverage than multiplying the current
high-momentum time windows, provided the larger-volume forward control is
retained.

## 6. Program and axiom consequence

The exact theorem and the production result now separate two questions that
were previously entangled:

```text
leading quadratic tensor structure:
  unique exactly and not contradicted by the off-axis family comparison;

scalar coefficient c^2:
  incompatible with U K in the full three-gradient finite-q fit,
  compatible but underresolved after the unique highest-q block is removed;

remaining positive decision:
  add genuinely lower momenta and retain a paired projection control.
```

No axiom edit follows. Cubic covariance comes from Lattice, while the gauge
null, analytic expansion, gapless phase, and coefficient matching are derived
properties of this supplied carrier. Writing isotropy or `c^2=U K` into the
axioms would assume the physics being tested.

No official TOE score moves until independent classification. The scientific
advance is that a possible directional failure of the light branch has been
tested across complete cubic orbits and is not resolved, while the remaining
normalization question has been localized to finite-momentum model order
rather than mislabeled as anisotropy.

## Falsifiers

This bounded result fails if an independent replay finds any of:

- a production receipt other than `TOTAL: PASS=5 FAIL=0`;
- a localization receipt other than `TOTAL: PASS=11 FAIL=0`;
- a significant three-parameter improvement from independent family leading
  coefficients;
- incompatible face-diagonal leading coefficients;
- failure of positive-definite full-rank covariance or declared genealogy
  floors;
- a lower-momentum `L=10,12,14` coefficient more than two combined reported
  errors from the source-pinned `U K` target;
- failure of the fixed-target lower-momentum fit; or
- restoration of the same target compatibility by removing `L=10`, `L=12`,
  or `L=14` instead of `L=8`.

Run:

```bash
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py --check-only
python3 scripts/cached_runner_output.py scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py --check-only
```
