---
claim_id: formation_rate_ruler_evades_cancellation_constant_mode_fixes_kappa_one
claim_type: bounded_theorem
claim_scope: "Smooth conditional rate algebra, Q-ratio selection without physical constant-mode symmetry, uniform scalar energy response/iteration, and finite packet acceleration comparisons in explicitly supplied lattices."
upstream_dependencies: []
runner: scripts/formation_rate_ruler_constant_mode_fixes_kappa_one_check_2026_09_04.py
---

# Smooth rate dressing and uniform scalar response in a finite supplied lattice model

The useful result is conditional algebra: a smooth symmetric rate dressing adds
`kappa*nu` to the linear hopping weight. A particular ratio of logarithmic
responses selects `(kappa,nu)=(1,1)` when two conditions are imposed. It does
not establish invariance of the physical system under a constant potential.

**Original date:** 2026-09-04. **Correction date:** 2026-09-09.
**Author scope:** finite conditional support; no audit verdict is assigned.

## Supplied definitions and evidence boundary

All scientific objects used here are defined in this note and its runner.
Use coarse integer coordinates with signed nearest-neighbor hopping `M`,
`eta_x=1`, `eta_y=(-1)^x`, `eta_z=(-1)^(x+y)`, and
`Gamma_vv=(-1)^(x+y+z)`. The Hamiltonian is
`H0=M+m Gamma`. A supplied field family multiplies a bond by
`1+alpha*(Phi_v+Phi_j)/2` and its mass term by `1+beta*Phi_v`.
The reference covariance fills negative energies and half fills exact zero
modes; it is a spectral projector only away from the half-occupied zero modes.
`E_v=sum_j H_vj(P-I/2)_jv` is counted from half filling, not normal ordered
against the sea itself. Occupations and these matrix energies are supplied
model observables. Neither their Born/record realization nor a physical
six-record carrier or total-energy readout has been established here.

Use an open `2x2x3` box (924-dimensional half-filled Fock sector), periodic
`4^3` box, **all-open** `16x4x4` box, and `192x16x4` slab open in x and
periodic in y,z. The earlier small-slab periodic-boundary description was
wrong. The ramp, interior mask, packet masses, widths32/44, and field strengths
are declared in the runner. The largest dense matrix is924x924. Sparse packet
propagation bounds each actual field Hamiltonian by its absolute row sum;
this also covers nonlinear rate dressing, for which a linear-family bound
alone would be insufficient.

No historical supplier note is consumed as physical authority. In particular,
the archived emergent carrier, clock, gravity and cosmological interpretations
are not premises of this finite model. No axiom, scale reference, vacuum choice,
formation dynamics, Einstein equation, or source law is derived.

## T1 — smooth dressing and a projection that does not imply cancellation

Stipulate `r_v/r0=1+kappa*Phi_v>0` and a symmetric homogeneous function
`g(x,y)` of degree `nu`, nonzero at equal positive arguments. Differentiability
there gives Euler's identity `g_1=g_2=nu*g/(2*r0)` and hence

```text
(1+Phibar)*g(r_v,r_j)/g(r0,r0)
  = 1+(1+kappa*nu)*Phibar+o(||Phi||),    beta=1.
```

A locally C2 function yields an O(||Phi||²) remainder. Without differentiability,
`g=max(x,y)` is a symmetric degree-one counterexample: at `(1+e,1-e)` its
increment is `|e|`, while the proposed mean linear term is zero. The runner
checks this counterexample. The arithmetic and geometric power dressings are
smooth on the positive domain, and their **quadratic coefficients** differ by
`nu*kappa²*(Phi_v-Phi_j)²/8`; their full difference also has an O(||Phi||³)
remainder. The tested weighted homogeneous family is not an ordinary arbitrary
weighted power mean. The original sparse AM/GM comparison is retained
(approximately4.2e-7 and8.4e-8 relative residual on its two fields).

On a bipartite bond, writing a site response as `S_v+eps_v*T_v` gives
`(S_v+S_j)/2+eps_v*(T_v-T_j)/2`. Cancellation requires equal endpoint T;
a sublattice-even component can still vary in space. There is no theorem that
a supplied formation rate must be spatially constant or even.

The original six all-open slab rows are retained: occupation **regression**
coefficients near2.2e-14 and energy coefficients approximately1.000–1.947.
They are contractions against the ramp, not pointwise bond averages. For the
actual m1,H(2,1),g=.001 fixture the direct control has maximum interior bond
occupation derivative about**.0875482** and site-fit residual about**.0250834**
despite the near-zero projected coefficient. This defeats the old claim of
pointwise cancellation and the physical parity-based route rejection.

## T2 — constancy of Q is not physical constant-mode invariance

The AM and GM logarithmic-response ratio around uniform `Phi=c` is
`Q(c)=1+nu*kappa*(1+c)/(1+kappa*c)` on its positive-rate, nonzero-denominator
domain. Imposing both `kappa*nu=1` and Q constancy selects `(1,1)`.
This is a conditional algebraic selection, with both requirements supplied.

At that point the **actual** Hamiltonian is
`H(c)=(1+c)² M+(1+c)m Gamma`. Dividing by its hopping coefficient leaves
mass `m/(1+c)`; it is not generally a scalar multiple of H0. The actual
all-open slab m1,c=.1 control gives best scalar approximately1.1912766 with
maximum residual .0912766. A zero-mean Poisson convention neither proves a
physical constant-shift symmetry nor derives the selected rate parameters.

## T3 — uniform energy response

For a differentiable constant-rank negative-energy projector, differentiating
the total sea energy gives `tr(P*dH)`; the `tr(H*dP)` term vanishes.
The uniform periodic model therefore yields
`K=alpha*(1-w_m)+beta*w_m`, with `w_m=E_mass/E_total`.
For the stated nonpositive hopping/mass contributions and nonzero total energy,
`0<=w_m<=1`, so K lies **inclusively** between the weights; equality occurs
at m0 or equal weights. This is not an arbitrary spatial-response formula.

The retained independent open-cube Fock check gives total-energy/occupation
agreement around5e-15/2e-15 at m.7 and the original ramp. Uniform H(1,1)
positive rescaling gives K1=1 on4^3. The original five masses and four alpha
values still test K against the formula at the original2e-6 tolerance.
A sea-energy density and a stipulated Poisson matter source are different
objects; no source identification follows from these numbers.

## T4 — uniform scalar iteration and external-field comparison

If one **stipulates the uniform scalar** update
`alpha_next=1+nu*K(alpha)`, its fixed point is
`(1+nu*w_m)/(1-nu*(1-w_m))` when the denominator is nonzero.
Tuning to alpha2 requires `nu=1/(2-w_m)` and slope
`(1-w_m)/(2-w_m)` in[0,1/2], including1/2 at m0. At nu1,w_m0 the map is
`alpha_next=1+alpha` and has no fixed point. The retained200 iterations per
mass use the computed uniform response and approach2 within the declared
1e-5 gate. This does not solve a spatial self-consistent rate-density equation.

The original small-slab energy comparison takes a maximum **over its interior
mask**: approximately2.850e-4 and7.135e-5 at gradients.004 and.002, ratio3.99.
It compares two supplied external-field Hamiltonians; it is not closure of a
local energy-tracking loop. The uniform K2-K1 shift about.821845 at m1 is
retained. A feedback equation requires a further source choice. Under the
separately stipulated convention `Delta Phi=P0[rho+chi Phi]`, `L=-Delta`,
the correct equation is `(L+chi)Phi=-P0rho`; no positive Yukawa mass follows
from a negative sea susceptibility.

## T5 — finite packet acceleration measurements

The original sparse Hamiltonian comparisons and all packet rows remain.
For the declared AM(1,1) packet, the historical rest/massless accelerations
are approximately-4.03702/-8.04940, ratio1.9939; GM gives the same rounded
ratio, linearH(2,1) gives1.9891 and H(1,1) gives.9997. Rest packet rows at
m=.5,1,2 are approximately-4.06370,-4.03702,-4.01127, with retained original
.09 tolerance and a printed comparison against matched linear-family packets.
The ratio mismatch decreases from about.00478 to.00033 on a fourfold field cut.
These are useful finite comparisons, not exact curvature, light-deflection,
universal-free-fall, or error-mechanism results.

Central differentiation has O(g²) error for smooth dependence: even terms
cancel in its numerator, but cubic terms leave g² error after division. The
two-width Richardson combination assumes a leading1/sigma² expansion that
these two widths do not independently establish. The residual's cause is not
isolated. Deterministic parameters do not imply bitwise cross-BLAS identity.
For `E²=m²+sum(2-2cos p_a)` physical coarse-coordinate group velocity is
`v_a=2sin(p_a)/E`, c=2. The parameter `chi=1-m²/E²` is not v²/c² at finite
momentum; replacing one with the other cannot turn these rows into exact GR.

## T6 — local tick arithmetic remains a declaration

If one stipulates `a_tau(v)=1/[(1+Phi_v)M*c]`, then `r/r0=1+Phi` and its
value at-.1 is.9. The runner retains this arithmetic only. No local tick,
physical clock rate, mass normalization, or independent agreement with a gauge
principle is proved. A future physical formation rule and its coarse hopping
law remain open; neither historical clock grades nor carrier suppliers are used.

## Evidence and next use

Primary: [`scripts/formation_rate_ruler_constant_mode_fixes_kappa_one_check_2026_09_04.py`](../scripts/formation_rate_ruler_constant_mode_fixes_kappa_one_check_2026_09_04.py). Current evidence: [source/input-bound
runner cache](../logs/runner-cache/formation_rate_ruler_constant_mode_fixes_kappa_one_check_2026_09_04.txt); this cache records actual finite results, not a
physical validation or audit grade. The original note/runner/cache are preserved
exactly in [the historical inventory](../archive/backlog/gravity-7925-7929-7938/HISTORY.md).
Historical paths retain old titles for provenance; this corrected body is the
authoritative author scope at the active path. All runtime scientific helpers
and fixture parameters are inline. The runner binds this exact note as its
only repository input; no physical premise is imported from historical links.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
artifact_role: conditional_model_calculation
conditional_surface_status: conditional-support
next_trace_action: use the finite identities with their supplied assumptions; establish an actual carrier and source law before physical promotion
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Formal audit is deferred under the owner's campaign decision. Landing review
checks this finite source scope and evidence binding; it assigns no audit grade.
