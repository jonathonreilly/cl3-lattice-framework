# Cubic Covariance and Gauge Transversality Uniquely Fix the Quadratic Maxwell Kernel

**Date:** 2026-09-04

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Physical carrier parent:**
[`SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py`](../scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt)

## Result up front

Consider the most general symmetric three-component kernel whose entries are
homogeneous quadratic polynomials in spatial momentum. It has `36` real
coefficients before constraints. Exact linear algebra gives

```text
proper cubic covariance only:  dimension 3,
gauge transversality only:      dimension 6,
both conditions together:       dimension 1.
```

The unique joint basis, after one normalization choice, is

```text
K_ij(q) = q^2 delta_ij - q_i q_j.
```

Therefore a symmetric, analytic, gapless gauge branch on a proper-cubic
carrier has a unique quadratic spatial kernel. Its two transverse
polarizations share one direction-independent leading coefficient. Cubic
anisotropy may reappear at fourth and higher momentum order, but it cannot
enter as a second quadratic light-speed coefficient.

This is an exact algebraic reduction, not a numerical fit. It sharpens the
off-axis spectroscopy campaign: that calculation tests whether the physical
spin-half branch reaches the assumed analytic transverse regime and measures
its one coefficient. It is not being asked to infer leading isotropy from a
few directions when the symmetry and gauge conditions already force it.

## 1. Declared kernel class

Let `K(q)` be a real symmetric `3 x 3` matrix. Each of its six independent
entries is an arbitrary homogeneous polynomial of degree two in
`q=(q_0,q_1,q_2)`. The six monomials are

```text
q_0^2, q_1^2, q_2^2, q_0 q_1, q_0 q_2, q_1 q_2,
```

so the unrestricted coefficient space has dimension `6 x 6 = 36`.

The claim is deliberately confined to this class. It assumes a quadratic
Taylor term exists. It does not prove analyticity, exclude a mass or a
nonanalytic direction-dependent term, or show that the microscopic carrier
actually has a thermodynamic pole.

## 2. Proper cubic covariance

The runner constructs all `24` orientation-preserving signed permutation
matrices `R`. For every one it imposes the polynomial identity

```text
K(R q) = R K(q) R^T.
```

Coefficient matching over the exact polynomial ring gives rank `33`, leaving
a three-dimensional cubic-covariant quadratic kernel space. Cubic symmetry by
itself is therefore insufficient. This control matters: it prevents the
argument from silently replacing the proper cubic group by continuous
rotational symmetry.

## 3. Gauge transversality

Independently, the runner imposes

```text
K(q) q = 0
```

as an exact polynomial identity. This is the momentum-space null direction
required by the gauge redundancy. Applied without cubic covariance, it gives
rank `30` and leaves six quadratic kernels. Gauge transversality by itself is
also insufficient.

Stacking the two exact constraint matrices gives rank `35`. Its nullspace is
one-dimensional, with normalized representative

```text
[[q_1^2 + q_2^2,      -q_0 q_1,      -q_0 q_2],
 [     -q_0 q_1, q_0^2 + q_2^2,      -q_1 q_2],
 [     -q_0 q_2,      -q_1 q_2, q_0^2 + q_1^2]].
```

This is exactly `q^2 delta_ij - q_i q_j`. On the plane perpendicular to
`q`, it acts as the scalar `q^2`. Both transverse polarizations therefore
have the same quadratic dispersion coefficient for every direction.

## 4. Physical consequence and remaining test

The spin-half cubic-ice carrier has an exact local ice constraint and proper
cubic covariance. Its finite-volume spectral work already finds a positive
transverse crossover. The theorem shows that, if this branch has an analytic
gapless thermodynamic continuation, leading spatial isotropy is not an extra
fit choice. The one remaining quadratic coefficient is the quantity compared
with the independently measured electric and magnetic responses.

The off-axis production ladder still has essential work to do. It can expose
any of the following failures of the theorem's physical premises:

- a nonzero mass within the accessible volume range;
- a failure to reach the analytic small-momentum regime;
- polarization splitting inconsistent with higher-gradient suppression;
- an incorrectly identified transverse observable; or
- finite-momentum corrections large enough that the common coefficient is
  not yet measurable.

The numerical ladder must therefore retain family-specific fourth- and sixth-
order corrections while testing one common quadratic coefficient. Agreement
would support the physical realization of the exact theorem; disagreement
would localize the missing premise rather than create an independent cubic
quadratic speed.

## 5. Axiom boundary

The Lattice axiom supplies proper cubic rotations of the underlying lattice.
It does not by itself supply a gauge field, a symmetric analytic kernel, a
gapless phase, or the identification of lattice momentum with a physical
long-wavelength excitation. In this application gauge transversality comes
from the supplied ice constraint and carrier construction.

No axiom edit follows. Adding the Maxwell kernel to the axioms would assume
the carrier physics. The theorem instead states exactly which derived carrier
properties are sufficient to force it.

The result also does not equate the emergent Hamiltonian time with Record
time, fix the numerical light speed, derive Lorentz boosts, couple the mode to
matter, or identify it with empirical electromagnetism.

## 6. Independence and mutation controls

The two partial solution dimensions are retained as load-bearing controls:

| retained constraints | exact dimension |
|---|---:|
| proper cubic covariance | `3` |
| gauge transversality | `6` |
| both | `1` |

Dropping either condition enlarges the answer. Thus neither condition is
decorative, and the unique Maxwell basis is not placed into the calculation
as the only starting ansatz. The runner begins from all `36` coefficients and
derives the nullspace.

The calculation uses exact symbolic coefficients. It contains no stochastic
sample, fitted tolerance, external numerical comparator, or embedded target
coefficient.

## 7. Prior-art boundary

The group-theoretic fact that cubic symmetry constrains low-rank tensors and
the gauge-theory form of the transverse Maxwell kernel are standard. No
priority is claimed for either. The repo-specific contribution is the exact
intersection calculation in the full symmetric quadratic kernel class and
its use to separate a forced leading tensor structure from the live
spin-half-carrier spectroscopy questions.

## Falsifiers

This bounded theorem fails if an independent exact implementation finds any
of:

- other than `24` proper signed-permutation rotations;
- a cubic-only solution dimension other than `3`;
- a transverse-only solution dimension other than `6`;
- a joint solution dimension other than `1`; or
- a joint basis not proportional to `q^2 delta_ij - q_i q_j`.

Its application to the spin-half carrier fails if that branch is not
analytic and gapless in the infrared, does not inherit the declared cubic
covariance, or does not satisfy the required gauge null direction.

Run:

```bash
python3 scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py
```
