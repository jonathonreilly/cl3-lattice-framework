# Finite Kernel Identities and a Radial-Ansatz Obstruction — Cycle 884

**Date:** 2026-08-04; corrected 2026-09-09

**Type:** bounded_theorem

**Claim type:** bounded_theorem

**Status:** bounded-support

**Authority:** none

**Audit:** unset; formal audit is deferred until the TOE is solid.

**Primary runner:**
[`scripts/frontier_cycle884_gbs2_kernel_window_2026_07_28.py`](../scripts/frontier_cycle884_gbs2_kernel_window_2026_07_28.py)

**Independent checker/helper:**
[`scripts/frontier_cycle884_gbs2_independent_check_2026_07_28.py`](../scripts/frontier_cycle884_gbs2_independent_check_2026_07_28.py)

**Cached primary receipt:**
[`logs/runner-cache/frontier_cycle884_gbs2_kernel_window_2026_07_28.txt`](../logs/runner-cache/frontier_cycle884_gbs2_kernel_window_2026_07_28.txt)

**Cached independent receipt:**
[`logs/runner-cache/frontier_cycle884_gbs2_independent_check_2026_07_28.txt`](../logs/runner-cache/frontier_cycle884_gbs2_independent_check_2026_07_28.txt)

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite Dirichlet identities, a conditional seven-point invariant-stencil count, explicit implication counterexamples, and a two-site algebraic obstruction on a stated nonzero-amplitude domain."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Select a physical gravity response operator, boundary condition, source coupling, and detector readout from retained framework content."
source_of_blocker_text: corrected_original_review
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Use these finite identities only after a physical operator and boundary supplier is established; keep window and sign selection open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the cubic
lattice and nearest-neighbour adjacency. They do not supply a scalar response
operator, a Poisson equation, a boundary condition, finite scalar readout
additivity, a source coupling, or a physical force-sign convention. Every
operator below is therefore an explicit mathematical input.

The exact original note, four original runners/caches and related receipts,
plus every selected intermediate Cycle-900 body are preserved outside the
active `docs/` discovery surface under
`.claude/science/physics-loops/time-kernels-6009-correction-20260909/`.

## 1. Exact finite zero-exterior model

For an integer `R>=1`, define

```text
Lambda_R = {x in Z^3 : ||x||_infinity <= R},
L_R = 6 I - adjacency,
L_R G_R = delta_0,
G_R(x) = 0 outside Lambda_R.
```

This is a supplied finite boundary problem. Exact rational elimination on
cubic-orbit classes finds a pivot in every column for `R=2,3,4`, verifies every
equation with zero residual, and gives positive values on each of those three
finite cubes.

### Theorem 884-F1

On each tested cube,

```text
G_R(0) - G_R(e_1) = 1/6.
```

The proof is local. Cubic symmetry puts the six neighbours of the origin in
one orbit, while the origin row of `L_R G_R=delta_0` is

```text
6 G_R(0) - 6 G_R(e_1) = 1.
```

The runner checks the full finite solve in addition to this identity. On the
radius-four cube it also finds
`G_R(3,0,0)-G_R(2,2,1) != 0`, even though both sites have Euclidean radius
three. This proves non-radiality for that finite zero-exterior model. It is not
an infinite-volume statement.

No conclusion about existence, uniqueness, decay, convergence, asymptotics or
transcendence on the infinite lattice is drawn from these finite pivots.

## 2. What cubic covariance says on a supplied seven-point stencil

Fix the support

```text
S = {0, +/-e_1, +/-e_2, +/-e_3}.
```

The 24 proper cubic rotations have two orbits on `S`: the centre and the six
neighbours. Therefore the invariant coefficient space on this supplied support
has dimension two: one centre coefficient and one common neighbour
coefficient.

This conditional orbit count does not select either coefficient, require the
neighbour coefficient to be nonzero, select an inverse operator, or identify a
physical response law. The identity response is local, linear, translation
covariant and cubic covariant, yet a unit source has zero response at distance
two. Thus those properties alone do not force a nonzero power-law tail or
`p=1`.

## 3. Nonzero massless radial ansatz

Supply the massless discrete harmonic equation away from the source and the
radial ansatz

```text
f_epsilon(x) = A/(|x|+epsilon),       A != 0.
```

At `x=(1,0,0)` and `x=(2,0,0)`, division by the nonzero amplitude reduces the
two harmonicity conditions to

```text
R_1 = 1/epsilon + 1/(epsilon+2) + 4/(epsilon+sqrt(2))
      - 6/(epsilon+1) = 0,

R_2 = 1/(epsilon+1) + 1/(epsilon+3) + 4/(epsilon+sqrt(5))
      - 6/(epsilon+2) = 0.
```

Their domains exclude

```text
R_1: epsilon in {0,-1,-2,-sqrt(2)},
R_2: epsilon in {-1,-2,-3,-sqrt(5)}.
```

### Theorem 884-F2

No defined value of `epsilon` makes both equations hold.

One exact route rationalizes each summand separately and writes the resulting
cleared numerator as `U_i+V_i sqrt(D_i)`. In that representation the common
factors of `U_i,V_i` are

```text
h_1 = epsilon(epsilon+1)(epsilon+2),
h_2 = (epsilon+1)(epsilon+2)(epsilon+3).
```

Each factor divides the corresponding cleared denominator and consists of
actual pole values, so it is removed before interpreting roots. For this
term-by-term representation, the reduced quadratic norms
`U_i^2-D_i V_i^2` both have degree six and their exact monic GCD over
`Q[epsilon]` is one. Any simultaneous zero of the two original defined
residuals would be a common zero of these two norms, which is impossible.

The primary first cancels the rational-only part of each displayed residual,
then multiplies by its defined `epsilon+sqrt(D_i)` denominator. This gives a
shorter, coprime numerator representation and an independent unit GCD for its
two norms. The `Fraction` checker uses the term-by-term representation above.
The two routes therefore need not report the same intermediate factors or
degrees; each starts from the displayed residuals, keeps the full radical
component, and proves the same no-common-zero implication on the stated
domain.

This is a theorem about the supplied massless radial ansatz with `A!=0`. It
does not make the ansatz physically mandatory and does not classify
`epsilon`, screening, or any different kernel as physically inadmissible.

## 4. Window and sign implication checks

Finite additivity is absent from the current Record axiom. Even if a finite
additive scalar readout is separately supplied, it does not collapse arbitrary
site weights to an annulus or two boundary parameters. The independent runner
uses three shell weights `2/7, 5/7, 10/7`; their set-sum readout is exactly
additive and retains all three distinct weights.

Positive values of a supplied Green function likewise do not select a physical
source-coupling or `TOWARD` sign. Replacing a separately supplied coupling
`c` by `-c` reverses the interpreted response while leaving the positive
mathematical Green function unchanged. A physical sign requires an additional
source/action and observable bridge.

## Corrected disposition of the historical claims

The current packet retains the finite model identity, the conditional
seven-point orbit count, the explicit counterexamples, and Theorem 884-F2.
It withdraws the earlier claims that:

- Record currently supplies finite scalar additivity;
- additivity forces an annular sharp window or makes an outer boundary gauge;
- locality, linearity and cubic covariance select a nearest-neighbour inverse;
- continuum scaling weights are an exact lattice proof of `p=1`;
- Green-function positivity selects the physical `TOWARD` orientation;
- finite Dirichlet calculations establish an infinite decaying Green function;
- the enumerated chart classifications are complete physical dimension counts;
- the radial-ansatz obstruction eliminates a physical regulator or screened
  response without an independently supplied operator.

No audit grade, TOE closure, Gate-B closure, reserved dependency, physical
Newton constant, or framework-level gravity law follows from this note.
