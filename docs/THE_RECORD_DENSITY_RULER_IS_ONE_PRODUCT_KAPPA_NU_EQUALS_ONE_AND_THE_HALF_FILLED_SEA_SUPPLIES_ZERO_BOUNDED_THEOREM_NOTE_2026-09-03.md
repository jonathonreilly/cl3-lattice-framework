---
claim_id: the_record_density_ruler_is_one_product_kappa_nu_equals_one_and_the_half_filled_sea_supplies_zero_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional pointwise differentiable density dressing gives alpha=1+kappa*nu and beta=1. The uniform-amplitude one-dimensional t=1 toy has -1/8<=nu<0 for positive coupling, proved globally. Gapped massless bipartite seas have flat occupation; massive finite slabs have numerically near-zero fitted slopes but nonzero local bond response and regression residual. No physical formation/readout or general local-density no-go is derived."
upstream_dependencies: [minimal_axioms]
runner: scripts/record_density_ruler_kappa_nu_sea_supplies_zero_check_2026_09_03.py
---

# A supplied density dressing: the product condition, a global toy bound and local sea-response limits

**Date:** 2026-09-09 source correction. **Type:** bounded_theorem.
**Primary runner:** [record_density_ruler_kappa_nu_sea_supplies_zero_check_2026_09_03.py](../scripts/record_density_ruler_kappa_nu_sea_supplies_zero_check_2026_09_03.py).
**Runner cache:** [actual source-bound execution](../logs/runner-cache/record_density_ruler_kappa_nu_sea_supplies_zero_check_2026_09_03.txt).
**History:** [dated correction and all exact original bodies](../.claude/science/physics-loops/gravity-ruler-correction-20260909/CORRECTION_RECORD.md).
The original filename is a recovery key; this title and current scope supersede its older headline.

```yaml
actual_current_surface_status: bounded-support
trace_class: frontier_discovery
artifact_role: theorem
reachability_to_target: unknown_frontier
next_trace_action: "Keep the supplied model identities, finite diagnostics and unresolved physical suppliers distinct."
```

## Supplied model and current authority

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select the
Hamiltonian, scalar potential, clock, Born law, vacuum, energy readout, formation
site/rate or physical gravity interpretation used here. All are supplied model
conditions where invoked. The historical fermion supplier's marker rule reads a
`5x5x5` window; its adjacent-sites-only realization was explicitly open. Its title,
Git ancestry and old status do not derive the present hopping model from the axioms.
No scalar Record-additivity or current audit status is inferred.

The finite coarse graph has real nearest-neighbour KS hoppings `M` with
`eta_x=1`, `eta_y=(-1)^x`, `eta_z=(-1)^(x+y)` and diagonal grading
`Gamma_v=(-1)^(x+y+z)`. On the bipartite fixtures, `{M,Gamma}=0`.
The supplied one-particle Hamiltonian is `H0=M+m Gamma`, with `t=1` and
coarse-site position `X`. Its dispersion, near the chosen corner `q=pi+p`, is
`E^2=E0^2+m^2`, `E0^2=sum_a (2-2 cos p_a)`. The cell has two coarse sites:
`q=2k`, `v_a=2 sin(p_a)/E`, and the small-momentum massless speed is `c_L=2`.
All formulas dividing by `E` require `E>0`; the gapless zero is excluded.
The fine-site encoding and a physical identification of these modes are not proved here.

## T1: a pointwise dressing condition, with hypotheses

Use the [corrected two-weight family](THE_SPATIAL_HALF_OF_THE_METRIC_IS_ONE_DECLARED_WEIGHT_ON_THE_HOP_TERM_FREE_FALL_AND_LIGHT_BENDING_AT_FACTOR_TWO_BOUNDED_THEOREM_NOTE_2026-09-03.md) and separately stipulate
`rho_b=rho0(1+kappa Phi_b)+o(Phi_b)`, `rho0>0`, and dress only each hop by
`f(rho_b)/f(rho0)`. Here `Phi_b=(Phi_v+Phi_j)/2`.
Assume f is differentiable and positive near rho0. Then
`nu=rho0 f'(rho0)/f(rho0)` and the already present factor `1+Phi_b` gives
`alpha=1+kappa nu`, `beta=1`, to first order. Thus alpha=2 iff `kappa nu=1`.
A second-order remainder requires correspondingly stronger second-order hypotheses;
it does not follow from differentiability alone. The exact power-law version additionally
requires `1+kappa Phi_b>0`. These are pointwise response assumptions, not a fit definition.
The ratio alpha/beta is a scalar-symbol acceleration coefficient ratio under the earlier
hypotheses, not a finite-lattice light-bending factor.

## T2: global bound for one explicitly supplied toy

For the uniform-amplitude dangling-mode toy with t=1 and s=g0^2 n>0,
its Bloch matrix `[[-2 cos k,sqrt(s)],[sqrt(s),0]]` has eigenvalues `-cos k +/- sqrt(cos^2 k+s)`.
This definition is the one used from
`RECORD_DENSITY_SLOWS_LR_FRONT_OPTICAL_METRIC_TOY_BOUNDED_THEOREM_NOTE_2026-06-09.md`;
only this rederived dispersion is consumed. Its wider historical timing/Record claims
and periodic-dilution tables are not accepted or rerun here.
Let `v_F(s)=max_k |dE/dk|`, and identify f with v_F only for this conditional calculation.
For the maximizing branch take `u=-cos k` in (0,1) and
`r=u/sqrt(u^2+s)` in (0,1). Its speed is `sqrt(1-u^2)(1+r)`.
The endpoint speeds are 1 and 0, while small positive u gives speed greater than 1;
reflection gives a larger speed than the other cosine half. Hence the maximum is interior.
Stationarity gives

```text
u^2 = r(1-r)/(1+r-r^2)
s(r) = (1-r)^2(1+r)/[r(1+r-r^2)]
s'(r) = (r-1)(3r+1)/[r^2(r^2-r-1)^2] < 0.
```

The limits of s(r) are infinity and zero, so each positive s has exactly one
stationary maximum and its envelope is differentiable. Envelope differentiation gives
`nu=d log v_F/d log n=-r(1-r)/2`; therefore
`1/8+nu=(2r-1)^2/8>=0`. The global bound is `-1/8<=nu<0`, attained at
`r=1/2`, `u^2=1/5`, `s=3/5`, `v_F=3/sqrt(5)`.
This proof, not the retained grid or 40-digit stationary calculation, supplies globality.
If this f is selected and kappa nu=1 is required, then kappa<0 and `|kappa|>=8`.
It is not a bound on other registration classes or a physical record-production law.

## T3: finite occupations, zero modes and the nonzero local response

The finite calculation is ordinary Fock space on 12 modes, with a supplied quadratic
Hamiltonian and Born occupation measurement. Its 924-dimensional N=6 block agrees
with the one-body sea projector on the gapped fixtures. It is not a construction of
the fine-edge BKSF code or an identification of occupation with permanent physical Records.

For an invertible massless bipartite H, `Gamma P_- Gamma=P_+` and `P_-+P_+=I`,
so `(P_-)_vv=1/2`. With zero modes the correct identity is
`(P_-)_vv=(1-(P_0)_vv)/2`. The mixed convention assigning weight one half to every
zero mode restores flat density; an arbitrary pure half-filled zero-mode ground state
need not. For H=0 on two modes, the one-particle state at the first mode has occupations
(1,0). The runner makes its zero-mode convention explicit and checks the many-body
fixtures are gapped before comparing a selected pure ground state to P_-.

At nonzero mass, the original uniform-field examples have zero mean and a staggered
response. The `16x4x4` open-x, periodic-yz slab has eight original ramp fixtures.
Their least-squares projected coefficient onto the ramp is near zero, but their
pointwise endpoint-averaged response is not. At m=1,(alpha,beta)=(2,1),g=.001,
`max_b |d rho_b/dg|=0.1183863716`; the four-column fit on
`(Phi_b/g, Gamma_v, Gamma_v(Phi_v-Phi_j)/g, 1)` leaves max residual
`.0431215807` and RMS `.0122289170`. Its fitted kappa has magnitude below `1e-12` in that control.
The residual disproves the old claim that the whole response is the fitted staggered
gradient. These values are finite central-difference diagnostics, not exact derivatives.

Only a genuinely pointwise zero response allows substituting kappa=0 into T1.
That is justified for the stated gapped massless bipartite occupation model, or the
explicit half-zero-mode mixture convention. A vanishing massive global projection
cannot make this substitution. The massive local-density feedback question remains open.

## T4: constant modes and the restricted locality observation

For a spatially uniform Phi=c with positive hop scale, dividing H by `1+alpha c`
gives the hop-normalized mass ratio `m_eff=m(1+beta c)/(1+alpha c)`.
Its derivative at zero is `m(beta-alpha)`, equal to -m at (2,1).
This is a dimensionless ratio after a rescaling, not a proved change in physical rest mass.
A chosen neutral inverse `G0 P0` fixes a zero-mean potential representative;
constant sensitivity then signals a required normalization/boundary convention,
not a contradiction in that fixed representative.

If one separately supplies `-Delta Phi=P0 rho`, a response pointwise proportional
to that source vanishes where Delta Phi=0 even when Phi is nonzero.
The interior of the open linear ramp illustrates this ansatz mismatch only.
It is not a no-go for all local response laws, boundary-dependent responses,
propagated fields, other observables or formation dynamics.

## T5: finite dressed-packet diagnostics

The unchanged 192x16x4 slab compares (1,1),(2,1), and the stipulated dressing
at (kappa,nu)=(-1,-1) or (-8,-1/8), with the original fields and widths.
They retain the near-two transverse acceleration ratios and the finite-field
nonlinearity at kappa=-8. They measure acceleration ratios, not ray curvature.
Central field differences retain O(g^2) bias; two-width Richardson has no certified
remainder. The nonlinear power domain is checked, and propagation uses at least the
actual absolute-row-sum bound of its Hermitian matrix, rather than assuming a
linear-weight bound also certifies the nonlinear dressing.

All 15 original check identities and numeric targets are retained; C5 gains an actual
residual condition. New controls distinguish global from local response, zero-mode
fillings, the global toy proof and propagation/domain bounds. The assumed Hamiltonian,
state, readout, density response, dressing and physical clock remain supplied.
The scalar record-density law is not derived; alternatives are not excluded.
Own note, the used sibling definition, toy definition and memo are guarded inputs.
Original source/cache bodies remain explicit history; formal audit is deferred.
