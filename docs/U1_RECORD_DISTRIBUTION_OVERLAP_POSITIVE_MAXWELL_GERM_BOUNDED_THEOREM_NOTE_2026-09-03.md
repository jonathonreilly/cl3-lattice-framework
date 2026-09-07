# U(1) Record-Distribution Overlap Produces a Positive Maxwell Germ

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source note sets no audit
verdict, changes no TOE score, and claims no obligation retirement.
**Direct Fourier/registration parent:**
[`U1_REPRESENTATION_POSITIVE_REGISTRATION_KERNEL_TO_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_REPRESENTATION_POSITIVE_REGISTRATION_KERNEL_TO_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Continuum parent:**
[`COMPACT_U1_QUADRATIC_BASIN_SOURCE_FREE_MAXWELL_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-09-03.md`](COMPACT_U1_QUADRATIC_BASIN_SOURCE_FREE_MAXWELL_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Current axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Runner:**
[`scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py`](../scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_record_distribution_overlap_maxwell_germ_2026_09_03.txt`](../logs/runner-cache/u1_record_distribution_overlap_maxwell_germ_2026_09_03.txt)

## Claim scope

Supply a compact `U(1)` possibility coordinate and a nonuniform probability
density `p` on it. Assume `p>=0`, normalized against mass-one Haar measure,
and `p in H^2(U(1))`. Define the distribution-overlap kernel

```text
C(delta) = integral p(theta) p(theta+delta) dtheta/(2 pi).
```

Then:

1. `C` is a normalized, nonnegative, even `U(1)` probability density;
2. `C(delta)<=C(0)` for every `delta`;
3. every nonzero Fourier coefficient of `C` is a modulus square;
4. the normalized negative-log overlap

   ```text
   V(delta) = -log[C(delta)/C(0)]
   ```

   is finite and `C^4` near the identity; and
5. its identity curvature is exactly

   ```text
   V''(0)=kappa
          = ||p'||_2^2 / ||p||_2^2
          > 0.
   ```

This removes the positive-Lueders and Fourier-sign premises from the local
germ calculation. The input distribution may be asymmetric, may have drift,
and may have negative or complex Fourier coefficients. Its self-overlap is
automatically inversion symmetric and representation positive.

On an additionally supplied shifted conditional family

```text
p(theta | phi)=p_0(theta-phi),
```

Admissibility's genuine neighbor variation excludes exactly the uniform base
density, so it gives `kappa>0` on this bounded compact-phase realization.
Under a supplied repeatable ensemble protocol, Records make `p_0` and hence
`C` inferable from repeated finite-bin outcome frequencies. Exact point
coincidences are neither required nor asserted on a continuous possibility
domain.

The main boundary is physical ownership. The overlap is a derived statistic
of probability distributions. The four axioms do not state that this statistic
is a transition weight, action factor, or energy. If it is additionally the
factorized local transfer weight, its negative log lies in the continuum
parent's positive quadratic basin. If the same factor is then supplied on all
temporal and spatial plaquette orientations, the smooth zero-monopole branch
gives source-free Maxwell and two transverse local modes. A temporal overlap
kernel alone still lacks magnetic stiffness and is not Maxwell.

## 1. Autocorrelation theorem

Use normalized Haar inner product

```text
<f,g> = integral conjugate(f(theta)) g(theta) dtheta/(2 pi).
```

For a real probability density, the overlap is

```text
C(delta)=<p,tau_delta p>,
(tau_delta p)(theta)=p(theta+delta).
```

Nonnegativity is pointwise under the integral. Haar invariance gives

```text
integral C(delta) ddelta/(2 pi)=1.
```

A change of variables gives `C(-delta)=C(delta)`. Cauchy-Schwarz and
translation invariance of the norm give

```text
C(delta)<=|C(delta)|
        <=||p||_2 ||tau_delta p||_2
         =||p||_2^2
         =C(0).
```

Thus the identity is a global maximum without assuming that the original
density is centered or symmetric.

Write

```text
p(theta)=sum_(n in Z) p_hat_n exp(i n theta).
```

Then Parseval gives

```text
C(delta)=sum_(n in Z) |p_hat_n|^2 exp(i n delta)
        =1+2 sum_(n>=1) |p_hat_n|^2 cos(n delta).
```

Every nontrivial representation coefficient is a modulus square. This places
`C` inside the positive-character class proved in the direct parent even when
`p_hat_n` itself is negative or complex.

The `H^2` hypothesis gives
`sum n^4 |p_hat_n|^2<infinity`, so `C` has four termwise derivatives. Since
`C(0)=||p||_2^2>0`, continuity gives a neighborhood in which its logarithm is
finite and `C^4`. Zeros of `C` away from that neighborhood become hard
barriers and do not affect the local theorem.

Differentiation and periodic integration by parts give

```text
C'(0)=integral p p'=0,
C''(0)=integral p p''=-integral |p'|^2.
```

Therefore

```text
V''(0)=-C''(0)/C(0)=||p'||_2^2/||p||_2^2.
```

A periodic `H^1` function has zero weak derivative exactly when it is constant
almost everywhere. Since `p` is nonuniform, the numerator is strictly
positive. This proves the sign and nondegeneracy.

## 2. What Record does and does not supply

The minimal Record axiom says that records form, lock one supported local
possibility, persist, and are the only readable objects. The Admissibility
axiom supplies the neighbor-conditioned probability distribution but not its
extensional form or numeric values.

Supply a repeatable sampling protocol whose frequencies are consistent for
each fixed partition. Use `N` equal Haar-width cyclic bins
`B_i=[2 pi i/N,2 pi(i+1)/N)` and their limiting masses `p_i`.
The discrete statistic is

```text
C_N(s)=N sum_i f_i f_(i+s),       delta_N=2 pi s/N,
```

with indices modulo `N`. First let the supplied sampling limit give
`f_i -> p_i` for fixed `N`. Then take `N -> infinity` with
`delta_N -> delta`. The equal-bin density approximation converges to `p`
in `L^2`; continuity of translations and Cauchy-Schwarz give
`C_N(s) -> integral p(theta)p(theta+delta)dtheta/(2 pi)`.
A joint sampling/refinement limit needs its own error control and is not
proved here. Arbitrary unequal refining bins do not justify the factor `N`
or the cyclic shift's physical meaning.

The original runner check uses deterministic integer rounding at fixed
256 equal bins using midpoint-sampled probabilities and increasing count
totals. It checks that finite-bin
approximation, not a stochastic sampling law or partition refinement.
A separate correction witness integrates `1+0.25 cos(theta)` exactly over
equal bins at `N=32,64,128,256` and fixed shift `pi/4`; it also shows the
unweighted statistic fails for unequal refining bins at zero shift.

This is the precise sense in which the overlap is Record-inferable. The
theorem does not claim that a continuous exact point has nonzero probability,
that one run reveals a probability distribution, or that unread possibilities
are directly measured. It also does not derive repeatability, independence,
the formation site, or the formation rate from Record.

Most importantly, calculability from records does not make a statistic a law
of motion. Record supplies data from which `C` can be inferred; an additional
physical bridge must establish that Nature uses `C` as the local transition or
configuration weight.

## 3. Admissibility variation on a compact shift orbit

Suppose a supplied compact-phase neighboring condition `phi` acts by shifts:

```text
p(theta|phi)=p_0(theta-phi).
```

If `p_0` is uniform, the conditional distribution is identical for every
condition. If it is nonuniform, some pair of shifts gives different
distributions. Therefore, within this shift-covariant family,

```text
Admissibility variation
iff p_0 is nonuniform
iff ||p_0'||_2^2>0
iff kappa>0.
```

For two neighboring conditions `phi_1,phi_2`, their distribution overlap is

```text
integral p(theta|phi_1)p(theta|phi_2)dtheta/(2 pi)
 = C(phi_1-phi_2).
```

It depends only on their relative condition, is even under exchange, and has
the positive germ above. The runner checks this identity for every pair in an
explicit three-condition set.

The compact `U(1)` coordinate and shift action remain supplied. A general
neighbor-conditioned family can vary by changing shape rather than by group
translation; this theorem does not turn that larger class into a convolution
kernel. Deriving the compact orbit from `M_2(C)` or identifying a physical
subgroup is a separate carrier/dictionary problem.

## 4. Strict improvement over a sign-selected kernel

Consider the positive normalized density

```text
p(theta)=1-0.6 cos(theta).
```

Its raw identity is a minimum. If one incorrectly used `p` itself as a
transition weight around zero, the negative-log curvature would be

```text
[-log(p(theta)/p(0))]''_(theta=0)=-3/2.
```

Its overlap instead is

```text
C(delta)=1+0.18 cos(delta),
V''(0)=0.18/1.18>0.
```

Thus the overlap construction does real work: it repairs a valid positive
probability density outside the direct parent's representation-positive
class. It is not merely the same premise renamed.

For an asymmetric density with sine components, the complex phases of
`p_hat_n` also disappear in `|p_hat_n|^2`. The overlap does not select the
distribution's center or drift; it intentionally measures translation-
invariant similarity. Whether physical drift must survive in another sector
is outside this theorem.

The uniform mutation gives `C=1` and `kappa=0`. Admissibility variation is
therefore load-bearing on the supplied shift orbit rather than decorative.

## 5. Conditional action and Maxwell corollary

If local overlap factors are supplied as a conditionally factorized weight,

```text
P[path or configuration] = product_p C(delta_p),
```

then ordinary multiplication gives the additive negative-log functional

```text
-log[P/C(0)^N] = sum_p V(delta_p).
```

This algebra does not assume finite scalar additivity as Record content. It
does assume that the overlap factors are the physical joint-law factors;
arbitrary local conditional distributions do not establish that premise.

The autocorrelation theorem supplies exactly the continuum parent's local
hypotheses:

```text
V(0)=0,             V is even and C4 near zero,
V''(0)=kappa>0.
```

If `delta_p` is additionally identified with compact plaquette curvature and
the same factor is present on every orientation, smooth principal-branch
refinement gives

```text
S -> (kappa/4) integral F_mu_nu F_mu_nu d^4x,
partial_nu F_nu_rho=0,
dF=0
```

on the zero-monopole branch. Distinct input distributions change `kappa` and
finite-angle corrections, but after curvature normalization their vacuum
equations converge to the same source-free Maxwell operator.

The runner follows three inputs—including a signed and an asymmetric Fourier
family—through six fixed-volume refinements. It independently rechecks the
compact Bianchi identity and the all-momentum gauge spectrum.

## 6. Temporal-only boundary and spatial target

An overlap between a link distribution on neighboring Record-time layers can
supply a temporal/electric plaquette kernel. It does not create spatial
plaquette factors merely because its germ is positive.

With temporal curvature `kappa_t=kappa` and no spatial curvature
`kappa_s=0`, the quadratic gauge block at nonzero spatial momentum has rank
one. With an isotropic spatial completion `kappa_s=kappa`, it has rank three
before removing the gauge direction and exactly two transverse local modes
after Gauss reduction. An unequal completion changes the infrared cone.

This locates the next construction target:

```text
Record-inferred U(1) distribution overlap
 -> positive temporal/electric germ             proved conditionally here

local cell/plaquette ownership of the same overlap
 -> positive spatial/magnetic germ              open

one physical spacetime law equating the germs
 -> isotropic source-free Maxwell completion    open
```

The existing “directions compare; cells weigh corners” H1 result is an
operator factorization on a different fixed source. It does not by itself
identify its corner weights with this `U(1)` overlap or supply spatial gauge
plaquettes. A direct composition must prove those type identifications rather
than rely on the similar wording.

## 7. Premise ledger and physical boundary

At axiom scope, this note uses only:

- Admissibility's existence of a genuinely neighbor-varying probability
  distribution; and
- Record's readable, locked outcomes as the data from which a distribution
  may be inferred across a supplied ensemble protocol.

The following remain supplied or open:

- a compact `U(1)` possibility orbit inside the one-site or composite
  `M_2(C)` structure;
- shift covariance of the conditional family;
- repeatable comparable Record ensembles and their sampling relation;
- physical ownership of distribution overlap as a transition/action weight;
- factorization or another compatible global-law construction;
- link and plaquette geometry, including spatial magnetic factors;
- equality of temporal and spatial curvature in physical units;
- the electromagnetic dictionary, charged sources, coupling normalization,
  quantum continuum, and strong-field/topological sectors.

No binary Record capacity, positive Lueders instrument, exact Wilson shape,
Hamiltonian, Born selector, action, time metric, or physical photon identity is
read into the four axioms.

## 8. Executable evidence

The runner reports `TOTAL: PASS=31 FAIL=0`. It verifies:

- normalization and positivity of three input densities with positive,
  negative, and asymmetric/complex Fourier data;
- direct quadrature equality with the squared-Fourier overlap formula;
- normalization, nonnegativity, evenness, periodicity, identity maximality,
  positive curvature, and the Sobolev norm identity;
- 32 deterministic signed asymmetric eight-harmonic families and an
  asymmetric non-polynomial von Mises mixture;
- raw-wrong-sign and uniform-distribution mutations;
- pairwise shifted-condition overlap and finite integer Record-histogram
  convergence;
- factorized negative-log additivity, second-order action and operator
  refinement, and microscopic-shape independence after curvature
  normalization;
- exact zero-monopole compact Bianchi closure;
- every nonzero Fourier momentum on `L=3,4,5` for the isotropic completion,
  gauge null, and transverse quotient; and
- temporal-only and anisotropic spatial controls.

The analytic Cauchy-Schwarz, Parseval, integration-by-parts, and periodic
zero-derivative arguments prove the universal statement. The finite suites are
falsification controls, not an empirical extrapolation.

## No-Go Discipline Gate

The note contains the negative boundary that Record-inferability alone does
not make the overlap a physical action and that a temporal kernel alone is not
Maxwell. The N1-N8 gate below restricts those statements to missing ownership
and magnetic-block proofs; it asserts no permanent impossibility.

### N1 — Alternative routes and same-cycle evidence

These attempts were checked analytically or by the paired runners in this
47-path review unit. Positive and partial constructions remain positive or
partial; none is recast as a failed route to satisfy a count. Named check
labels, rather than old ordinal numbers, identify the evidence. Cross-note
comparisons below are scope tests, not extra premises of this note.

| Route | Actual attempt and evidence | Result within the stated scope |
|---|---|---|
| Fourier autocorrelation | **ATTEMPTED:** Square the complete complex Fourier coefficients (§1; direct-overlap and modulus-square checks). | A nonuniform H2 density gives a positive germ without a sign assumption on its coefficients. |
| Real-space norm identity | **ATTEMPTED:** Use Cauchy-Schwarz and integration by parts; compare the independent density derivative integral with curvature. | The maximum and norm-ratio formula agree. |
| Raw density as kernel | **ATTEMPTED:** Use the explicit negative-cosine density before autocorrelation (raw-instability check). | That raw identity germ is unstable; the overlap repairs it. |
| Binned observation | **ATTEMPTED:** Test deterministic counts at fixed bins, exact uniform-bin refinement, and unequal-bin refinement (§2). | Only the stated uniform-bin and consistent sampling limit justifies density inference. |
| Factorized action | **ATTEMPTED:** Multiply the supplied transition factors and take their logarithm (path probability/action check). | Additivity follows for that chosen product; action ownership remains supplied. |
| Temporal-only germ | **ATTEMPTED:** Build the temporal-only Hessian (temporal-only check). | Two magnetic directions are absent in that block. |
| Spatial completion and anisotropy | **ATTEMPTED:** Assemble the full orientation-completed Hessian and vary spatial curvature (last Fourier controls). | The supplied isotropic completion works and an unequal completion changes the cone. |

An arbitrary local marginal does not specify a joint formation mechanism.
Spatial-cell realization, correlated joint laws and effective isotropization
remain construction problems, not routes declared impossible here.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: compact orbit realization.
- W2: shift-covariant conditional family.
- W3: consistent ensemble sampling.
- W4: physical ownership of the overlap weight.
- W5: joint compatibility or factorization.
- W6: spatial plaquette construction.
- W7: temporal-spatial gauge equality.
- W8: electromagnetic identification.
- W9: charged coupling.

| Pair | First closure implies second? | Second closure implies first? | Independence established? |
|---|---|---|---|
| W1, W2 | unresolved | unresolved | no |
| W1, W3 | unresolved | unresolved | no |
| W1, W4 | unresolved | unresolved | no |
| W1, W5 | unresolved | unresolved | no |
| W1, W6 | unresolved | unresolved | no |
| W1, W7 | unresolved | unresolved | no |
| W1, W8 | unresolved | unresolved | no |
| W1, W9 | unresolved | unresolved | no |
| W2, W3 | unresolved | unresolved | no |
| W2, W4 | unresolved | unresolved | no |
| W2, W5 | unresolved | unresolved | no |
| W2, W6 | unresolved | unresolved | no |
| W2, W7 | unresolved | unresolved | no |
| W2, W8 | unresolved | unresolved | no |
| W2, W9 | unresolved | unresolved | no |
| W3, W4 | unresolved | unresolved | no |
| W3, W5 | unresolved | unresolved | no |
| W3, W6 | unresolved | unresolved | no |
| W3, W7 | unresolved | unresolved | no |
| W3, W8 | unresolved | unresolved | no |
| W3, W9 | unresolved | unresolved | no |
| W4, W5 | unresolved | unresolved | no |
| W4, W6 | unresolved | unresolved | no |
| W4, W7 | unresolved | unresolved | no |
| W4, W8 | unresolved | unresolved | no |
| W4, W9 | unresolved | unresolved | no |
| W5, W6 | unresolved | unresolved | no |
| W5, W7 | unresolved | unresolved | no |
| W5, W8 | unresolved | unresolved | no |
| W5, W9 | unresolved | unresolved | no |
| W6, W7 | unresolved | unresolved | no |
| W6, W8 | unresolved | unresolved | no |
| W6, W9 | unresolved | unresolved | no |
| W7, W8 | unresolved | unresolved | no |
| W7, W9 | unresolved | unresolved | no |
| W8, W9 | unresolved | unresolved | no |

### N3 — Hidden-wall scan

The density's `H^2` regularity, mass-one Haar reference, compact shift action,
repeatable ensemble interpretation, and any factorized use are explicit. The
Maxwell corollary separately supplies compact links, plaquette identification,
a four-dimensional refinement, orientation completion, and a smooth zero-
monopole branch. No continuous singleton probability, binary menu, preferred
possibility, or action selector is hidden in Record.

### N4 — Residual matching

The direct parent left the positive-Lueders registration class and physical
kernel ownership as load-bearing inputs. This note removes the former from
the mathematical sign theorem by an independently defined distribution
overlap, but retains the latter. The continuum parent left realization of an
isotropic positive action basin open. This note reaches only a conditional
temporal germ and does not relabel spatial realization as closed.

### N5 — Rhetoric and resolution audit

“Not automatically an action” means no axiom or theorem cited here equates the
overlap statistic with Nature's transition/configuration weight. “Temporal
alone is not Maxwell” means its displayed quadratic block lacks two magnetic
restoring directions. Neither phrase excludes a cell law, compatible joint
law, emergent action, or larger composite route. The cached stdout prints:

```text
per_element: every Fourier component of each input density is squared analytically in the overlap kernel
per_site: shifted neighbor-conditioned distributions and finite Record histograms are compared directly
per_mode: every nonzero Fourier momentum on L=3,4,5 is checked after orientation completion
per_block: raw-sign, uniform, temporal-only, isotropic, and anisotropic blocks are contrasted
lattice_wide: fixed-volume action/operator refinements and zero-monopole cube identities run on four-lattices
```

### N6 — Partial-closure paths and primitive check

The current axiom registry was reread. Admissibility supplies distributions
and their neighbor variation, not values, action, factorization, or a transfer
operator. Record supplies readable outcomes, not a repeatable protocol or a
rule turning an analyst's statistic into dynamics. The kinetic-isotropy
primitive addresses a kinetic graining form, not gauge-action equality; the
scale and realized-state primitives supply neither missing block.

Partial closure can proceed by proving that a local face/cell Record rule has
this overlap as its likelihood factor, by deriving a compatible joint law from
the local full conditionals, or by obtaining the same kernel as an effective
action after eliminating explicit local auxiliaries. Any one could establish
physical ownership without changing the autocorrelation theorem.

### N7 — Steelman

The strongest objection is decisive against an overclaim: one may compute
infinitely many functions of a measured probability distribution, and most
are not physical laws. Autocorrelation is special mathematically—it is
positive, symmetric, and stable—but those virtues do not prove that the
framework uses it to weight histories or spatial curvature. Moreover, an
actual law might preserve drift information that overlap intentionally
removes. This blocks TOE or Maxwell promotion from this note alone. It does
not defeat the theorem that the overlap, if physically owned, lies in the
positive Maxwell basin.

### N8 — Cross-cycle echo

Earlier Record work repeatedly separated an inferred ensemble law from an
individual realized Record and separated a registration/readout kernel from a
continuous dynamics. This theorem keeps both distinctions. Earlier gauge work
separated temporal reflection-positive kernels from spatial Wilson factors;
the temporal-only rank control keeps that distinction. The result advances
the route by removing Fourier-sign and exact-action choices, not by reviving
the old identification shortcuts.

**Gate result:** PASS for both scoped boundaries. The positive overlap theorem
stands, physical ownership and spatial completion remain live construction
routes, and no broader no-go ships.

## Falsifiers

The theorem fails within scope if any of the following occurs:

- a nonuniform normalized nonnegative `H^2(U(1))` density has an overlap
  coefficient that is not a modulus square;
- its overlap is larger away from identity than at identity;
- `V''(0)` differs from `||p'||_2^2/||p||_2^2` or is nonpositive;
- an asymmetric or negative-Fourier density retains an odd or negative
  representation component after self-overlap;
- finite Record histograms cannot approximate the overlap statistic under the
  stated supplied sampling protocol;
- curvature-normalized overlap potentials fail to approach the common smooth
  Maxwell operator when used as plaquette factors; or
- the temporal-only quadratic block already contains the magnetic transverse
  stiffness stated to be absent.

## Verification

Run:

```text
python3 scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=31 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A selected framework-derived electromagnetic law and physical field/readout bridge remain open; the eventual physical consumer is not yet established."
source_of_blocker_text: "review_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Use the conditional result with its stated inputs; establish the missing physical consumer and selection bridge before claiming framework closure."
conditional_surface_status: "Supplied nonuniform H2 Haar density; action ownership and spatial completion remain supplied, and histogram inference requires uniform bins and a consistent sampling limit."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The written derivation establishes only the declared conditional mathematical claim; finite checks and source review grant no retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original September 2–3 source and receipts are preserved at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. This revision supplies current
source status, explicit timeout/input-bound evidence and written boundary
checks. The conditional scope is stated in the status record above.
Independent source confirmation and current-main integration validation are
separate; no audit verdict or effective retained status is asserted.
