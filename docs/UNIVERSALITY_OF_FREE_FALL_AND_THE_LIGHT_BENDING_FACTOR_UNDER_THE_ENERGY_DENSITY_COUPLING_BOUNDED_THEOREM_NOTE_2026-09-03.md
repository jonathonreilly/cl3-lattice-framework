---
claim_id: universality_of_free_fall_and_the_light_bending_factor_under_the_energy_density_coupling_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite KS hopping plus staggered mass, supplied scalar potential and unitary dynamics. Exact energy regrouping and scalar-band Hamilton-equation identities at nonzero energy; finite Ehrenfest and width-extrapolation diagnostics. These are neither all-packet trajectory theorems nor a physical gravity or light-bending derivation."
upstream_dependencies: [minimal_axioms]
runner: scripts/free_fall_universality_light_bending_factor_check_2026_09_03.py
---

# Total-energy coupling: exact band-symbol acceleration and finite packet diagnostics

**Date:** 2026-09-09 source correction. **Type:** bounded_theorem.
**Primary runner:** [free_fall_universality_light_bending_factor_check_2026_09_03.py](../scripts/free_fall_universality_light_bending_factor_check_2026_09_03.py).
**Runner cache:** [actual source-bound execution](../logs/runner-cache/free_fall_universality_light_bending_factor_check_2026_09_03.txt).
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

## T1: the finite coupling and normalization

Define `H_Phi=H0+{Phi,H0}/2`, with real diagonal `Phi`.
A bond receives `1+(Phi_v+Phi_j)/2`; its staggered mass receives `1+Phi_v`.
For any normalized state, split each hop equally over its endpoints:
`eps_hop(v)=Re(sum_j psi_v^* M_vj psi_j)`,
`eps_tot(v)=eps_hop(v)+m Gamma_v |psi_v|^2`, and `n(v)=|psi_v|^2`.
Their sums are respectively `<M>`, `<H0>` and `1`. These are definitions of supplied
quadratic observables. They do not make hopping energy readable from occupation alone:
the two states `(1,1)/sqrt(2)` and `(1,-1)/sqrt(2)` have identical complete Z-outcome
probabilities but opposite expectation of the two-site hopping matrix.

Bipartiteness proves `H0^2=M^2+m^2 I`; the `8^3` torus tests the dispersion at
`m=0,.5,2`. For positive `1+Phi`, the alternative conjugation
`A H0 A`, `A=sqrt(1+Phi)`, replaces the arithmetic endpoint mean by its geometric
mean and differs at second order in the field. This is not equality at finite field.

## T2: exact scalar-symbol identities and their physical domain

For the supplied scalar Hamiltonian symbol `h(x,k)=E(q)+Phi(x) w(q)`, Hamilton's
equations at `Phi=0`, `partial_x Phi=g`, give
`a_x/g=-4 w E_xx+4 E_x w_x`. This is an exact identity for that symbol.
Applying it to a packet of the full matrix Hamiltonian requires a single-band,
slow-field approximation; it is not an exact quantum acceleration theorem for every state.

For `w=E`, `a_x/g=-4 cos p_x+8 sin^2(p_x)/E^2`.
At `p_x=0` and `E>0`, this is `-4` for every remaining momentum and mass.
For a massless longitudinal mode with `p_y=p_z=0`, it is `+4` for nonzero `E`.
For the hop-only weight `w=E0^2/E`, it is
`-4 (E0^2/E^2) cos p_x+8 sin^2(p_x)/E^2`.
The count weight `w=1` instead gives `-4[cos p_x-sin^2(p_x)/E^2]/E`.
All three follow by differentiation; the runner retains its fixed finite comparisons.

The hop fraction `chi=E0^2/E^2` is not the squared speed
`|v/c_L|^2=sum_a sin^2(p_a)/E^2` at finite lattice momentum.
They agree only at leading small momentum. A band-edge mode can have zero group
velocity and nonzero hop fraction. The exact longitudinal sign change is
`cos p_x=2 sin^2(p_x)/E^2`; `|v_x|/c_L=1/sqrt(2)` is only its continuum limit.
The continuum symbol gives `a=-c_L^2 grad Phi+2 v(v.grad Phi)` at this order,
not the exact finite-momentum vector law.

## T3: finite Ehrenfest data and uncertainty

The original fixtures are unchanged: `256x48x8` and `256x32x8` slabs, open in x,
periodic in y,z, `Phi=g(x-Lx/2)`, `g=.001`; finite windows and widths are literal
runner inputs. Gaussian/tanh energy filters prepare approximate bands, not exact
positive-energy projectors. The acceleration observable is the double commutator
`-<[H,[H,X]]>`. Its central field difference removes the field-independent part,
but retains `O(g^2)` bias: even `f(g)=g+g^3` gives derivative estimate `1+g^2`.

The two-width Richardson combination assumes a leading `1/sigma_x^2` error.
It has no proved remainder or complete error budget. Finite time, filters, interband
terms, boundaries, higher-width terms and field bias remain. Centroid fit covariance
is only that fit's diagnostic uncertainty. Packet mass dependence at fixed width
is measured model behaviour; the comparison does not prove that one width effect
exhausts it. Nor do the three approximately equal-energy packets have exactly equal energy.

The historical data are retained: transverse Richardson values near `-4`, a three-body
acceleration spread about `8e-5`, the count-source contrast, and the longitudinal
`(d<H0>/dt)/g` comparison with `-E v_x`. This last relation is a consequence of the
supplied coupling and clock, not a derived physical test-body or source law.

## T4: acceleration ratio is not a light-bending factor

The finite packet ratio near `1` compares massless transverse acceleration with a
slow massive reference. A ray's local transverse curvature is `a_perp/v_y^2`.
For a massless transverse mode with 0<p<pi, `v_y=2 cos(p/2)` and
`|a_perp|/v_y^2=|g|/cos^2(p/2)`. Thus the old finite-momentum ratios do not equal
a curvature factor. The three exact momenta `pi/8,pi/4,3pi/8` give curvature
multipliers `1.03957,1.17157,1.44646`, although their symbol acceleration ratio is one.
The packet fixture uses the original rounded decimal momenta, close to these values.
The continuum comparison is conditional on low momentum, an adiabatic ray and an
external metric interpretation; physical lensing and general relativity are not derived.

## T5: energy fork and open alternatives

A staggered mass changes the supplied total-energy density by `m Gamma_v n_v`.
Using hop energy alone therefore defines a different coupling, with a small response
near a gapped Dirac rest point. At `m=0` the two operators coincide. This exact fork
selects neither an admissibility law nor a physical source/readout. The two-weight
extension, dynamical field closure, clocks, alternative readouts, and more general
formation rules remain live conditional alternatives. No theorem rules them out.

The primary retains all 18 original checks and their numeric targets, with corrected
labels and new small controls for speed, curvature, finite-difference bias and readout.
Old caches are preserved as history; only the current fingerprinted cache is current execution.
Independent source review and coordinator landing checks are separate; formal audit is deferred.
