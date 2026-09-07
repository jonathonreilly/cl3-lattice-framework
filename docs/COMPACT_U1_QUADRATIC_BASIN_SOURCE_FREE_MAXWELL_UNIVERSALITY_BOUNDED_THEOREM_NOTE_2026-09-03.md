# Compact U(1) Quadratic-Basin Source-Free Maxwell Universality

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source note sets no audit
verdict and claims no effective obligation retirement.
**Direct parent:**
[`COMPACT_U1_WILSON_TO_SOURCE_FREE_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-02.md`](COMPACT_U1_WILSON_TO_SOURCE_FREE_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-02.md)
**Runner:**
[`scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py`](../scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.txt`](../logs/runner-cache/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.txt)

## Claim scope

On a finite periodic four-dimensional hypercubic carrier, supply compact
`U(1)` link variables and an isotropic one-plaquette action

```text
S_V[ell] = sum_(x,mu<nu) V(bar_theta_mu_nu(x)).
```

Assume that `V` is an even `2 pi`-periodic plaquette potential, finite and
`C^4` on a neighborhood of the flat point, and normalized there by

```text
V(0)=0,                 V''(0)=kappa>0.
```

Then every smooth principal-branch refinement family has the same leading
continuum physics:

1. the action converges to
   `kappa/4 integral F_mu_nu F_mu_nu d^4x`;
2. the exact lattice equation converges to the source-free Euclidean Maxwell
   equation `partial_nu F_nu_rho=0`;
3. the compact cube identity supplies `dF=0` on the smooth zero-monopole
   branch;
4. the flat-background quadratic kernel has one gauge null, a rank-three positive
   Euclidean quotient, and exactly two local transverse spatial modes after
   Gauss reduction; and
5. all higher derivatives of `V` affect only refinement corrections. Two
   potentials with the same `kappa` have the same normalized quadratic limit
   even when their exact finite-angle actions and equations differ.

Thus the exact Wilson cosine is sufficient but is not necessary for this
source-free classical Maxwell limit. The load-bearing microscopic condition
inside the stated one-plaquette class is a positive isotropic quadratic germ,
not the full finite-angle shape of the potential.

The potential may have additional minima or even hard (`+infinity`) barriers
away from that neighborhood; neither affects the smooth-sector statement.

This is a supplied-action theorem. It does not establish that the framework's
Admissibility law realizes a compact connection, an action in this basin, or a
physical electromagnetic dictionary. Charged sources, coupling normalization,
Record readout, interacting quantum electrodynamics, nonsmooth sectors, and
general multi-plaquette actions are outside the claim.

Positive curvature makes the flat connection a local stable background. The
claim does not require or assert that it is the unique global action minimum.

## 1. Compact connection and exact equation

Use the parent's orientation convention

```text
tilde_theta_mu_nu = Delta_mu^+ ell_nu - Delta_nu^+ ell_mu
                  = bar_theta_mu_nu + 2 pi n_mu_nu,
bar_theta_nu_mu = -bar_theta_mu_nu.
```

The principal angle may jump by `2 pi` under a change of lift, but the periodic
potential is unchanged wherever it is finite. Therefore every action in the
class is link-gauge invariant. Evenness makes the term independent of the
arbitrary choice between the two plaquette orientations.

Because the local germ is even and `C^4`, it has
`V'(0)=V'''(0)=0`. On any configuration contained in that smooth
neighborhood, variation of one link gives the exact lattice equation

```text
G_rho(y)
 = sum_(nu != rho)
     [V'(bar_theta_rho_nu(y))
      - V'(bar_theta_rho_nu(y-nu))]
 = 0.
```

This formula is not a linearized definition. The runner compares it with
independent finite differences for three distinct periodic potentials and
checks that it annihilates gauge directions.

## 2. Uniform quadratic-germ bounds

Let

```text
M_4(epsilon) = sup_(|t|<=epsilon) |V''''(t)|.
```

Taylor's theorem gives, for `|t|<=epsilon`,

```text
|V(t) - kappa t^2/2| <= M_4(epsilon) |t|^4/24,
|V'(t) - kappa t|    <= M_4(epsilon) |t|^3/6.
```

For `epsilon=max_p |bar_theta_p|` and

```text
Q_kappa = (kappa/2) sum_p bar_theta_p^2,
```

the full finite-lattice action therefore obeys

```text
|S_V-Q_kappa|
 <= M_4(epsilon)/24 sum_p |bar_theta_p|^4
 <= [M_4(epsilon) epsilon^2/(12 kappa)] Q_kappa.
```

In four dimensions at most six oriented face contributions meet the varied
link in the displayed equation, so the pointwise nonlinear remainder obeys

```text
|G_rho-kappa d^dagger bar_theta| <= M_4(epsilon) epsilon^3.
```

No finite list of candidate potentials is used to prove these inequalities.
They hold locally for every `V` satisfying the stated germ hypotheses. The
explicit globally smooth family in Section 5 challenges the theorem with
different microscopic shapes.

## 3. Smooth continuum limit

Let the physical four-volume be fixed, let the spacing `a` tend to zero, and
define each link phase by the exact edge integral of a `C^4` one-form `A`.
Once

```text
a^2 ||F||_infinity < pi,
```

Stokes' theorem places every plaquette on the principal branch:

```text
bar_theta_mu_nu = integral_plaquette F = a^2 F^a_mu_nu.
```

There are `O(a^-4)` plaquettes at fixed volume. The quadratic contribution is
finite, while the potential-dependent fourth-order remainder is `O(a^4)`:

```text
sum_p O(bar_theta_p^4) = O(a^-4 a^8) = O(a^4).
```

The face-average quadrature itself approaches the continuum integral, giving

```text
S_V -> (kappa/2) integral sum_(mu<nu) F_mu_nu^2 d^4x
     = (kappa/4) integral F_mu_nu F_mu_nu d^4x.
```

Likewise, divide the exact link equation by `kappa a^3`. The linear
codifferential has the usual smooth limit and the nonlinear bound above
vanishes under refinement. Hence

```text
partial_nu F_nu_rho = 0.
```

The parent's exact compact identity

```text
d bar_theta = 2 pi m,        m = -d n
```

is independent of the action. Every sufficiently fine smooth family has
`m=0`, so its limiting homogeneous equation is `dF=0`.

For the exact-edge test mode `A_1=A cos(x_2)`, write

```text
z = a A (1-cos a).
```

The nonlinear link operator is `2V'(z)/a^3`. Using
`z<=A a^3/2` and the Taylor bound gives the executable estimate

```text
|2V'(z)/(kappa a^3)-A|
 <= A a^2/12 + [M_4/kappa] A^3 a^6/24.
```

The runner verifies this bound at six refinements for all three representative
laws.

## 4. Universal quadratic kernel and modes

Allow temporal and spatial germs with positive curvatures `kappa_t` and
`kappa_s`. With the forward-coboundary momentum

```text
hat_k_mu = 2 sin(k_mu/2),
T = hat_k_0^2,
P = sum_i hat_k_i^2,
```

the flat-background Hessian is

```text
K_00 = kappa_t P,
K_0i = K_i0 = -kappa_t hat_k_0 hat_k_i,
K_ij = kappa_t T delta_ij
       + kappa_s(P delta_ij-hat_k_i hat_k_j).
```

Its exact spectrum at nonzero four-momentum is

```text
0,
kappa_t(T+P),
kappa_t T+kappa_s P,
kappa_t T+kappa_s P.
```

For the isotropic basin `kappa_t=kappa_s=kappa`, the three nonzero eigenvalues
are all `kappa(T+P)`. Eliminating `A_0` at `P>0` gives

```text
K_red = kappa(T+P)
        [I_3-hat_k_spatial hat_k_spatial^T/P],
```

whose projector has rank two. Every potential with the same curvature has
this same Hessian because its higher derivatives disappear at the flat
connection.

If a reflection-positive transfer interpretation is additionally supplied,
the parent calculation applies with `beta_s/beta_t` replaced by
`kappa_s/kappa_t`:

```text
4 sinh^2(E/2) = (kappa_s/kappa_t) P.
```

The infrared cone is isotropic when the temporal and spatial curvatures and
the corresponding spacings are equal. The approved kinetic-isotropy primitive
concerns the kinetic graining form; this theorem does not silently extend it
into a derivation of the gauge-action Hessian.

An overall positive `kappa` multiplies the source-free equation and therefore
cancels after division. It remains physically meaningful when sources,
coupling normalization, or quantum fluctuation weights are introduced.

## 5. Constructive non-uniqueness witness

For every `lambda>=0`, define

```text
V_lambda(t)
 = [(1-cos t) + (lambda/4)(1-cos 2t)]/(1+lambda).
```

Each member is even, positive, `2 pi`-periodic, and has

```text
V_lambda''(0)=1,
sup |V_lambda''''| <= (1+4 lambda)/(1+lambda).
```

For distinct `lambda` the values and slopes differ at finite plaquette angle,
so this is not Wilson rewritten by an overall constant. Nevertheless every
member has the same Maxwell action, equation, and flat-background mode content in
the smooth limit. The runner uses `lambda=0,1/2,2`, checks the Taylor
inequalities across the full principal interval, and follows all three through
the same refinement sequence.

Three mutations locate the hypothesis boundary:

- `V_quartic(t)=(1-cos t)^2` has zero quadratic curvature. Its fixed-volume action
  and scaled link equation collapse to zero under Maxwell refinement.
- A negative spatial curvature gives negative transverse Hessian directions.
- Unequal positive temporal and spatial curvatures preserve the gauge null but
  change the infrared cone by `sqrt(kappa_s/kappa_t)`.

These are constructive controls, not claims about every action outside the
stated class.

## 6. What this changes for the Maxwell route

The parent theorem established source-free Maxwell from the Wilson action.
This theorem removes the Wilson cosine's exact finite-angle shape from that
particular continuum obligation. For vacuum classical Maxwell, it is enough to
show that the realized compact-`U(1)` action lies in the positive isotropic
quadratic basin above.

The remaining science separates cleanly:

1. derive, or explicitly supply and classify, the compact-`U(1)` connection
   and a local gauge action with `kappa_t=kappa_s>0` from the actual
   Admissibility law;
2. derive the dictionary identifying that connection with the physical
   electromagnetic field;
3. couple the verified matter/charge sector and recover the sourced equations;
4. fix the physically meaningful coupling normalization and Record-readable
   observables; and
5. control quantum, monopole, and interacting continuum sectors.

Exact Wilson, heat-kernel, and Manton selection can still matter for
finite-lattice and strong-field predictions. This result says only that such
selection is not a prerequisite for the smooth source-free Maxwell equations.

## 7. Executable evidence

The runner reports `TOTAL: PASS=27 FAIL=0`. It verifies:

- evenness, periodicity, positivity, common curvature, and uniform Taylor
  bounds for the representative family;
- finite-angle separation between its exact actions and equations;
- exact gauge invariance, finite-difference variation, gauge-direction nulls,
  and finite-lattice quadratic bounds;
- fixed-volume second-order action and operator refinement, the explicit
  operator error bound, and the inherited zero-monopole compact Bianchi sector;
- exhaustive `L=3,4,5` Fourier spectra, gauge nulls, and Schur reductions; and
- zero-curvature, wrong-sign, anisotropic, and common-rescaling controls.

The analytic Taylor argument supplies the universal quantifier over the stated
function class. The finite family is a falsification suite, not an exhaustive
enumeration used in place of proof.

## No-Go Discipline Gate

The positive theorem contains one negative boundary: exact Wilson selection is
not necessary for its scoped source-free limit. The following N1-N8 check
stress-tests that boundary; it is not a permanent impossibility claim about
microscopic action selection.

### N1 — Alternative routes and same-cycle evidence

These attempts were checked analytically or by the paired runners in this
47-path review unit. Positive and partial constructions remain positive or
partial; none is recast as a failed route to satisfy a count. Named check
labels, rather than old ordinal numbers, identify the evidence. Cross-note
comparisons below are scope tests, not extra premises of this note.

| Route | Actual attempt and evidence | Result within the stated scope |
|---|---|---|
| Taylor germ | **ATTEMPTED:** Apply the C4 remainder bounds to an arbitrary supplied even positive-curvature germ (§§1–3; action/first-variation bound checks). | The common quadratic term survives; finite-angle equality is unnecessary. |
| Distinct microscopic actions | **ATTEMPTED:** Use the explicit harmonic-potential family and compare its finite-angle action and equation (distinct-law checks). | Different microscopic laws have the same germ; action selection is not derived. |
| Fixed-volume refinement | **ATTEMPTED:** Evaluate full action and Euler refinements with the analytic error bound (§3 and refinement checks). | Both converge in the supplied smooth family; no interacting limit is claimed. |
| Compact topology | **ATTEMPTED:** Use the exact cube identity and the smooth zero-monopole control. | The selected branch has zero local charge; other sectors are outside the theorem. |
| Anisotropic stiffness | **ATTEMPTED:** Split temporal/spatial curvature (anisotropic-curvature check). | The cone changes; isotropy is a hypothesis. |
| Degenerate or unstable germ | **ATTEMPTED:** Set zero curvature and wrong-sign spatial curvature (last control block). | The tested flat and unstable cases do not give the claimed stable germ. |
| Common normalization | **ATTEMPTED:** Rescale the common curvature (final sourceless-equation check). | It cancels from the source-free classical equation, not from all physical data. |

Nonlocal, nonsmooth, charged and general multi-plaquette actions remain
outside this theorem; none is ruled out by this list.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: realization of the supplied positive isotropic basin.
- W2: physical U(1) identification.
- W3: charged coupling.
- W4: Record readout.
- W5: quantum and strong-field control.

| Pair | First closure implies second? | Second closure implies first? | Independence established? |
|---|---|---|---|
| W1, W2 | unresolved | unresolved | no |
| W1, W3 | unresolved | unresolved | no |
| W1, W4 | unresolved | unresolved | no |
| W1, W5 | unresolved | unresolved | no |
| W2, W3 | unresolved | unresolved | no |
| W2, W4 | unresolved | unresolved | no |
| W2, W5 | unresolved | unresolved | no |
| W3, W4 | unresolved | unresolved | no |
| W3, W5 | unresolved | unresolved | no |
| W4, W5 | unresolved | unresolved | no |

### N3 — Hidden-wall scan

The supplied objects are explicit: a four-dimensional periodic hypercubic
refinement, compact `U(1)` links, one identical local plaquette potential, a
smooth principal branch, local `C^4` regularity, and positive isotropic curvature.
The Lorentzian dispersion additionally needs the parent's reflection-positive
transfer interpretation. No action, dynamics, source, physical dictionary, or
Record process is smuggled in as “canonical” or “standard.”

### N4 — Residual matching

The earlier action-form work distinguishes Wilson, heat-kernel, and Manton at
finite lattice scale. This theorem asks a different question—what survives a
smooth source-free `U(1)` refinement—and therefore does not erase their
finite-scale separation. The heat-kernel convolution-CLT route uses a supplied
stochastic evolution; this proof instead uses only the local action germ. No
prior residual is imported as a witness.

### N5 — Rhetoric and resolution audit

The negative sentence is supported by an explicit continuum family containing
multiple non-Wilson laws, not by failure to find a selector. Its resolution
certificate lands in the primary cached stdout:

```text
per_element: every representative potential is checked across the full principal-angle interval with analytic Taylor bounds
per_site: exact link gradients are checked against independent finite differences on a periodic four-dimensional lattice
per_mode: every nonzero Fourier momentum on L=3,4,5 is checked for the common spectrum and exact gauge null
per_block: temporal and spatial curvature blocks are Schur-reduced and challenged by anisotropic and wrong-sign controls
lattice_wide: fixed-volume refinement and exact zero-monopole cube identities are executed on periodic four-lattices
```

The conclusion is restricted to the stated one-plaquette smooth vacuum limit.

### N6 — Partial-closure paths and primitive check

The current axiom registry was checked directly. The minimal axioms supply a
nearest-neighbor probability-distribution law but no source/action or physical
observable bridge. The kinetic-isotropy primitive supplies kinetic graining
form, not a gauge-action Hessian; the scale primitive supplies units only; the
realized-state primitive supplies a pointwise evaluation slot only. Therefore
none is used to infer `kappa_t=kappa_s>0`.

A derivation of that basin condition from an actual Admissibility law, or an
explicitly classified bounded supplier law, would advance the route without
requiring exact Wilson selection. Physical identification and charged coupling
remain separate construction paths. No axiom amendment is proposed here.

### N7 — Steelman

The strongest objection is that “all reasonable lattice actions flow to
Maxwell” would be far broader than what was proved. A realized law could have
zero or anisotropic curvature, a parity-odd or mixed-plaquette quadratic term,
nonlocal interactions, a nonsmooth flat germ, or persistent topological
defects. Such a law can leave the stated basin and need not yield ordinary
Maxwell physics. This objection defeats the broad slogan but not the theorem,
whose exact action class and hypotheses are explicit. The next target is basin
membership for the actual framework law, not another arbitrary potential.

### N8 — Cross-cycle echo

A current-repo search found three relevant earlier shapes. The action-form
uniqueness note already observed leading-order agreement among named actions
but retained their finite-scale distinction. The heat-kernel CLT note obtains
universality from a stronger supplied stochastic-dynamics premise. The
record-preservation dynamics-form note conditionally narrows dynamics to a
gauge-invariant local class while leaving coefficients and truncation open.
This theorem neither treats those source notes as retained premises nor revives
their broad negative rhetoric. It supplies a self-contained `U(1)` Taylor,
compact-Bianchi, and mode theorem and leaves their live closure mechanisms
available.

**Gate result:** PASS for the scoped negative boundary. The positive theorem
and its explicit exclusions stand; no wider action-selection no-go is asserted.

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
conditional_surface_status: "Supplied even periodic C4 plaquette potential with positive isotropic curvature on a smooth zero-monopole branch."
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
