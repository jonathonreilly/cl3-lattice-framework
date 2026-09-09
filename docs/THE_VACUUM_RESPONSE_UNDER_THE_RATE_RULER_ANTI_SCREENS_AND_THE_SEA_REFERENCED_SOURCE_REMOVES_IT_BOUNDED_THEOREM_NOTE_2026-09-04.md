---
claim_id: vacuum_response_rate_ruler_anti_screens_sea_reference_removes_it
claim_type: bounded_theorem
claim_scope: "Finite reference-dependent uniform and sampled nonuniform sea responses, a same-lambda off-axis counterexample, corrected-sign explicitly surrogate FFT feedback kernels, and no cosmological inference from P0."
upstream_dependencies: []
runner: scripts/vacuum_response_anti_screens_sea_reference_removes_it_check_2026_09_04.py
---

# Reference-dependent finite response and explicitly surrogate feedback kernels

Three reference conventions produce different finite response functions. The
fixed sea reference has a vanishing uniform linear response but a nonzero
nonuniform response. The field-dressed reference vanishes by its definition.
Axial samples do not determine the full lattice susceptibility.

**Original date:** 2026-09-04. **Correction date:** 2026-09-09.
**Author scope:** finite conditional support and labeled surrogate exploration;
no audit verdict is assigned.

## Supplied setting

All science inputs are the finite definitions here and in the runner, with no
physical carrier supplier consumed. Coordinates, KS signs, `Gamma`, the
nearest-neighbor real symmetric M and `H0=M+m Gamma` are supplied. The bond
weight is `1+alpha*(Phi_v+Phi_j)/2`; mass weight is `1+Phi_v`. The sea covariance
P fills negative energies and half fills zero modes. Gap/constant-rank
qualifications apply when P is called a projector. Covariance energies are
`diag(H*(P-P_ref))`, with reference I/2, fixedP(0), or field-dressedP(Phi).
These are model energy densities, not established physical record readouts.

The original fixtures remain: open2x2x3 half-filled924 Fock sector;
periodic4^3,8^3,12^3 sea matrices; response FFT tori16,24,32,64. Derivative
knobs are1e-5 (1e-4 for Fock derivatives), with O(g²) truncation error for
smooth dependence. The largest dense dimension is1728. No original primary
rerun is needed to interpret the historical cache; a new source/input-bound
cache records the corrected primary. No external matter source, clock,
cosmological note, or carrier grade supplies authority here.

## T1 — uniform response and an axial fitted surrogate

On the original periodic4^3 grid the energy is negative at every site for the
six declared masses. Representative `(m,E0,w_m,K2)` rows are
`(0,-1.12183644,0,2)`, `(.9,-1.24769456,.152931,1.847069)`,
`(1,-1.26960970,.178155,1.821845)`, `(6,-3.23760112,.860090,1.139910)`.
The exact uniform conditional identity is
`K(alpha)=alpha*(1-w_m)+w_m`, verified at the original tolerance. Uniform
positive H(1,1) rescaling gives K1=1. For `0<=w_m<=1,alpha>=1`, K>=1;
the formal zero `alpha=-w_m/(1-w_m)` needs w_m!=1 (at1 K=1).
The Fock uniform derivatives approximately-12.4083735 and-21.8731921 for
H(1,1)/H(2,1) agree with independently constructed one-body total derivatives.

The8^3 response samples are **axial** indices(0,0,0) through(4,0,0), with
lambda values0,.5858,2,3.4142,4. The full cubic-zone lambda range is0–12.
The first-three-sample least-squares fit has chi0 about-2.3979405 and c about
.1780893, max residual5.2e-4; the five-sample residual is about5.9e-3.
Sampled staggered/off projections are small. This does not prove isotropy,
exact scalar response for arbitrary fields, a continuum derivative expansion,
or an exact full-zone `chi=chi0+c*lambda` law.

If that fitted law is **stipulated as a surrogate**, and one independently
stipulates `Delta Phi=P0[rho+chi Phi]`, then

```text
L=-Delta,  ((1+c)L+chi0)Phi=-P0rho,
m_eff²=chi0/(1+c),  G_eff=1/(1+c).
```

The fitted values m_eff² approximately-2.035449/-1.192293 and factors
.848832/.917446 are retained. The surrogate negative-mode counts256,780,1892,
15352 on L16,24,32,64 are retained. Loss of positivity of a static quadratic
form does not mean noninvertibility except at an actual zero eigenvalue. It
does not imply a runaway without an evolution law. Negative fitted mass² has
no positive real Yukawa decay length, but does not remove every possible
length scale. The nominal inverse square root is about.701 lattice spacings.

## T2 — projector qualifications and a decisive off-axis control

Let P(t) be a differentiable constant-rank spectral projector of HermitianH(t),
commuting with H. From P²=P, `P Pdot P=0` and `(I-P)Pdot(I-P)=0`;
H is block diagonal in this decomposition, so **tr(H Pdot)=0**.
A spectral gap is sufficient. The identity is about a total trace, not each
site, and does not hold for an arbitrary moving projector or reference.
For fixed reference equal toP(0), the first-order total excess energy
vanishes. At the supplied uniform periodic fixture this also gives zero
uniform susceptibility. Nonuniform local responses need not vanish.

The retained12^3 fixed-reference uniform derivative is near1e-11. The next
two axial sample ratios chi/lambda are approximately-.00461 and-.00513;
their fitted slope near-.00532 gives a **surrogate** factor1.00534.
The maximum about.0100 concerns the original four axial8^3 samples only.
An actual same-lambda control on the **same8^3 sea** evaluates(4,0,0) and
(2,2,0): both have lambda4, but fixed-reference susceptibility is approximately
0 versus **-.02627384**, and half-reference susceptibility approximately
-1.66561612 versus-1.69188996. Thus chi is not a function of lambda alone,
and the claimed full-zone .010 bound and pure-Laplacian kernel are false.

For the field-dressed reference, `P(Phi)-P(Phi)=0` at every site by definition.
That zero is distinct from the fixed-reference trace identity and does not
establish that a physical source must choose this convention. Half-occupied
zero modes are covariances, not projectors; no gapless-projector proof is used.

## T3 — what P0 does and does not decide

For a zero-mean fieldPhi and a constantchi0, P0(chi0Phi)=chi0Phi. The original
inhomogeneousL16 control retains its approximately1e-18 mean/projection
residuals. But P0 also kills **any additive constant in rho**. A source with
zero vacuum excess and one with an arbitrary constant vacuum density produce
the same projected Newtonian field. It follows that neither this projection
nor sea subtraction determines a cosmological Lambda, a radius, or absence of
a de Sitter solution.

The original arithmetic3/R² at R1,3,10,1e3,1e6 remains a separate mathematical
illustration. It is positive for every finiteR>0 and tends to zero asR tends
to infinity. Conditionally, an independently assumed Einstein equation on a
de Sitter geometry of radiusR would give Lambda=3/R²; the roundS3 spectral
identity also needs that independently supplied geometry. Neither equation nor
geometry is supplied by P0. No cosmological ancestry is consumed here.

The uniform scalar rate algebra gives nu*=1/(2-w_m),kappa*=2-w_m, so
chi_uniform=E0*kappa*. The original all-mass numerical comparison is retained;
it does not solve a spatial rate loop or full feedback problem.

## T4 — corrected-sign surrogate kernels and limited calibration

The retained negative-mass **fitted surrogate** FFT kernels show sign changes
at selected distances and large ratios: onL64 representative ruler/bare values
are-.188,-.437,2.563,-1.436,12.570,50.556 at d1,2,3,6,8,16.
These exact finite inversions of a supplied surrogate are sensitive near poles.
An error in a fitted susceptibility can strongly change such numbers; they do
not show destruction of a physical two-body law.

The second surrogate interpolates the original four fixed-reference **axial**
samples as a function oflambda, sets its zero-mode value to zero, and uses a
proportional-to-lambda tail beyond the last sample. This continuation is a
model declaration, contradicted as an exact susceptibility by T2's control.
The earlier implementation used **lambda-chi**, inconsistent with the stated
field equation. The corrected implementation uses **lambda+chi**, and checks
the actual Fourier equation residual and a deliberately wrong-sign residual.
The active primary retains its original L16,24,64 distances and prints every
corrected ratio and their spread. Its
first distance list includes theL16 antipode d8; only its second list excludes
antipodes. No exact flat rescaling, unchanged rigid-copy ratio, or absence of
all length dependence is inferred.

The positive-mass² calibration keeps the original7 sampled values onL64 at
d1..8. The first sampled row below1percent is m²=1e-4 (nominal length100),
while1e-3 gives roughly5.7percent. This is not a necessary sharp threshold,
universal100-spacing requirement, or calibration for negative mass².

## T5 — normalization and distinct fit parameters

The supplied inverse unnormalized graph Laplacian has coefficient one in
lattice units. Its large-distance infinite-lattice continuum asymptotic is
1/(4pi*r); converting that to a physical Newton constant needs a separate
source, force, and unit bridge. Finite controls4pi*r*G at r=L/4 remain
approximately.3307/.3275 onL32/64, with near-sourceL64 values
1.0372,.9893,.9057,.8430 at d1–4.
The axial fitted c is not the mass fraction: at m0,c approximately.1881702
while w_m=0; at m2,c approximately.1504620 againstw_m=.413607.
These coefficients remain fitted finite data, not full-zone identities.

A full finite susceptibility action, a physical source/reference law and its
carrier realization remain open. No broad no-go against other vacua, record
maps, time-dependent sources, or nonlocal response has been established.

## Evidence and next use

Primary: [`scripts/vacuum_response_anti_screens_sea_reference_removes_it_check_2026_09_04.py`](../scripts/vacuum_response_anti_screens_sea_reference_removes_it_check_2026_09_04.py). Current evidence: [source/input-bound
runner cache](../logs/runner-cache/vacuum_response_anti_screens_sea_reference_removes_it_check_2026_09_04.txt); this cache records actual finite results, not a
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
