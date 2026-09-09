# Finite Screened Identities and the Corrected Radial-Ansatz Obstruction — Cycle 900

**Date:** 2026-08-04; corrected 2026-09-09

**Type:** bounded_theorem

**Claim type:** bounded_theorem

**Status:** bounded-support

**Authority:** none

**Audit:** unset; formal audit is deferred until the TOE is solid.

**Primary runner:**
[`scripts/frontier_cycle900_harmonic_repair_2026_07_28.py`](../scripts/frontier_cycle900_harmonic_repair_2026_07_28.py)

**Independent checker/helper:**
[`scripts/frontier_cycle900_harmonic_repair_independent_check_2026_07_28.py`](../scripts/frontier_cycle900_harmonic_repair_independent_check_2026_07_28.py)

**Cached primary receipt:**
[`logs/runner-cache/frontier_cycle900_harmonic_repair_2026_07_28.txt`](../logs/runner-cache/frontier_cycle900_harmonic_repair_2026_07_28.txt)

**Cached independent receipt:**
[`logs/runner-cache/frontier_cycle900_harmonic_repair_independent_check_2026_07_28.txt`](../logs/runner-cache/frontier_cycle900_harmonic_repair_independent_check_2026_07_28.txt)

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite screened origin identities, corrected multiquadratic norms on four axis conditions, safe interval semantics, and an exact normalization-stabilizer distinction."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Select a physical gravity response operator, boundary condition, source coupling, and detector readout from retained framework content."
source_of_blocker_text: corrected_original_review
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Treat the radial family as excluded only after supplying the screened nearest-neighbour equation; derive any physical kernel and boundary choice separately."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

This note builds on the corrected finite definitions in the
[Cycle-884 note](GBS2_KERNEL_WINDOW_ANATOMY_CYCLE884_BOUNDED_THEOREM_NOTE_2026-07-28.md).
The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select the
screened operator, a zero-exterior or periodic boundary problem, a source
coupling, or a physical readout. Those remain explicit inputs.

## 1. Finite screened origin identity

On the radius-three zero-exterior cube, supply `mu_squared>=0` and

```text
(6 I - adjacency + mu_squared I) G = delta_0.
```

Cubic symmetry makes all six nearest-neighbour values equal. The origin row is

```text
(6+mu_squared)G(0)-6G(e_1)=1,
```

and hence

```text
G(0)-G(e_1) = (1-mu_squared G(0))/6.                 (1)
```

### Theorem 900-F1

For `mu_squared>=0`, the displayed finite Dirichlet matrix is positive
definite. Its unique solution therefore inherits the cubic symmetry of the
operator, boundary and source, and equation (1) holds. Whenever `G(0)!=0`,
its left side equals `1/6` if and only if `mu_squared=0`.

Exact rational solves at `mu_squared=0, 1/100, 1/4, 1` verify the full finite
systems, the origin identity and positive `G(0)` in each tested model. These
examples do not select a physical mass or prove an infinite-volume limit.

## 2. Correct multiquadratic norm

An element of `Q(sqrt(p_1),...,sqrt(p_k))[epsilon]` is stored as a map from
radical basis keys to rational polynomials. Its field norm is computed by
multiplying the complete ring element under every sign character and reading
the rational component only after the full product. Thus

```text
N(1+sqrt(2))=(1+sqrt(2))(1-sqrt(2))=-1.
```

The historical primary and checker instead added the signed coefficient
polynomials inside each conjugate, dropping their radical basis keys; both
returned zero for this control. None of their old GCD certificates is used as
current evidence.

## 3. Screened nonzero radial ansatz

Supply, away from the source,

```text
sum_{y adjacent x} f(y) - (6+mu_squared) f(x) = 0,
f(x)=A/(|x|+epsilon),                              A != 0.
```

At the axis site `(n,0,0)`, define

```text
M_n(epsilon)=(n+epsilon)
  [1/(n-1+epsilon)+1/(n+1+epsilon)
   +4/(sqrt(n^2+1)+epsilon)].
```

The equation requires `M_n(epsilon)=6+mu_squared`. A solution on every
non-origin site must therefore make the four values `M_1,...,M_4` equal.

The domain excludes every zero denominator appearing in these four
conditions:

```text
epsilon in {0,-1,-2,-3,-4,-5,
            -sqrt(2),-sqrt(5),-sqrt(10),-sqrt(17)}.
```

### Theorem 900-F2

No `epsilon` in this domain and no value of `mu_squared` make the displayed
nonzero radial ansatz satisfy all four axis equations.

For the pairs `(1,2)`, `(1,3)`, `(2,3)`, `(1,4)`, clear denominators in
`M_n-M_m` and take the corrected multiquadratic norm. Their exact GCD in
`Q[epsilon]` is one. A common screened solution would make every pair
difference, and therefore every norm, zero. The unit GCD rules that out.

The primary proves this with explicit `Fraction` polynomial and
multiquadratic-ring arithmetic, retaining the six neighbour denominators
before clearing. The independent checker first combines the four equal
transverse terms, then eliminates radical generators with exact SymPy
resultants. These equivalent-on-domain clearings may report different norm
degrees and coefficients. Each route reports its own exact polynomials and a
unit common GCD, and both obtain `N(1+sqrt(2))=-1`.

The theorem is conditional on the supplied screened nearest-neighbour equation,
nonzero amplitude and stated domain. It does not prove that this equation is
the framework's physical gravity law. The zero-amplitude field is excluded
because it satisfies the homogeneous away-from-source equations trivially and
cannot represent the asserted nonzero source response.

## 4. Interval semantics

An enclosure that overlaps zero has unknown sign; it is not an exact root.
The independent control represents the single test element `sqrt(2)-7/5` in
the basis `{1,sqrt(2)}`, verifies from its two rational coefficients that it is
not exactly zero, encloses it coarsely across zero, and preserves an unresolved
bracket. No general root-isolation procedure is claimed or used in the GCD
proof.

This replaces the historical `cond_sign_at`/`isolate_root` branch that turned
an ambiguous sign enclosure into `(mid,mid)`.

## 5. Two distinct normalization operations

On the nonzero patch, the product stabilizer

```text
(lambda,sigma) -> (t lambda,sigma/t),              t != 0
```

leaves `lambda*sigma` exactly fixed. It therefore leaves both a fixed kernel's
raw sum and its amplitude-weighted sum unchanged. It cannot move a raw window
sum between kernel normalizations.

A separate kernel rescaling `K->cK` changes raw sums. Ratios
`K(x)/K(y)` cancel that independent amplitude when `c!=0` and `K(y)!=0`.
The primary checks both identities symbolically. Finite shape comparisons may
be quoted only for their stated finite boundary model; they are not a physical
normalization choice.

## 6. Boundary and physical scope

A zero-exterior Dirichlet cube and a periodic torus are different finite
boundary problems. Agreement of a local algebraic identity across them does
not select either as a physical Poisson supplier. Exact finite pivots prove
finite invertibility; they do not prove existence, uniqueness, decay,
convergence, transcendence, or an asymptotic coefficient on `Z^3`.

The current packet withdraws the historical claims of a physically forced or
unique harmonic repair, a complete 37-row consumer patch list, a physical
dimension reduction, `p=1` or `TOWARD` selection, and physical boundary or
Poisson selection. It preserves only Theorems 900-F1/F2, the corrected norm and
interval machinery, and the exact normalization distinction on their stated
mathematical domains.

No audit grade, TOE closure, Gate-B closure, reserved dependency, physical
Newton constant, or framework-level gravity law follows from this note.
