---
claim_id: native_weak_electric_defect_density_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied full native H_U=H_0+UD, U>=0, cubic L=4M with M>=32: ground mean local-defect density at most (102400/387)U/h and thermal density at most800U/h plus explicit terms. No contour stability, phase, nonzero-U spectral gap or Hamiltonian selection."
upstream_dependencies:
  - native_uniform_cubic_flux_defect_stiffness_note_2026-09-08
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_endpoint_note_2026-09-08
runner: scripts/native_weak_electric_defect_density_2026_09_08.py
---

# Weak electric penalty preserves a bound on mean flux-defect density

**Type:** bounded_theorem  
**Status:** conditional-support

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied full native Hamiltonian H_U=H_0+UD, U>=0, exact dictionary and certified U=0 stiffness; finite-dimensional variational and quantum relative-entropy mathematics."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Result and prerequisites

Use the [certified uniform cubic stiffness](NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md), [full native electric dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), and [zero-penalty endpoint](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md). Work on the full physical carrier, without a low-charge projection. The auxiliary hopping unit is h=2|g lambda|>0. U>=0 is the coefficient of the actual positive electric operator D=sum_v(deg_v-3)^2. Let K_def count noncanonical elementary magnetic plaquettes, N=L^3 and L=4M with M>=32.

Every ground-state density operator of H_U obeys

    <K_def>/N <= (102400/387)*(U/h).

For the full physical Gibbs state at beta*h>=200, put c=3*beta*h/800. Then

    <K_def>/N <= 800*(U/h)+2*log(8)/(c*N)
                    +6*log(1+exp(-c/2))/c.

Both bounds may be capped by3, the total number of elementary faces per vertex. They are useful density bounds when their right sides are small. They neither exclude every defect nor prove contour stability, a phase, a uniform spectral gap or pure-winding selection. No commutation of D with H0 is assumed; D in fact changes magnetic flux. The proof avoids the shrinking finite-size gap condition entirely.

## Complete derivation and source history

The full independently reviewed derivation follows. Its initial400 ground bound is a valid conservative intermediate bound; the later sharpened coefficient102400/387 is the theorem stated above. Its scratch-source references are historical provenance, with the canonical load-bearing sources linked above. No numerical Gibbs or perturbed-ground-state computation is used.

# A volume-uniform weak-electric defect-density bound without a spectral gap

This is a new analytic consequence, not a nonzero-U phase theorem. Sources read: final canonical uniform stiffness note bed02a2a089591081fbd72c855eb7b4dfc3ffc5b60e709e621e148e7ead00163, the full native dictionary's electric/low-domain distinction, zero-penalty endpoint's parity and static-sector discussion, and native-zero-penalty-spectator-lifting/DERIVATION.md electric expansion. The supplied full carrier and H_U=H_0+U D are retained; U>=0. No low-charge projection is added.

## Exact electric input and the surviving observable

On the six-valent graph D=sum_v (sum_(e incident v) n_e-3)^2 =3N/2+(1/2)sum_v sum_(e<f incident v) Z_e Z_f. Thus 0<=D<=9N on the FULL carrier. Let K_def=sum_p (1-S_p)/2 with the canonical sign absorbed so that it counts defective plaquettes. These commuting projectors remain a well-defined observable at U>0, although their sectors cease to be invariant.

Every nonconstant electric pair flips two distinct incident link-X signs. On these cubic tori that pair is not a gauge cut. Consequently it maps each fixed magnetic flux orbit to an orthogonal orbit. For every density operator block diagonal in magnetic orbit, its expectation is zero. In particular <D>_rho0=3N/2 for the U=0 Gibbs state at any beta, and <D>=3N/2 for a chosen canonical-flux ground state. This statement does not require a spectator choice or an active gap. It is not the assertion that D is scalar as an operator.

## Ground-state density: a positive result independent of winding gaps

Suppose the zero-temperature local stiffness is kappa_g>0. The fixed-orbit energy bound upgrades to the FULL operator inequality

    H_0 >= E_0 I + kappa_g K_def.

Indeed H_0 and K_def are simultaneously block diagonal in flux, and the bound holds for the lowest energy in every block; higher active states only increase it. It remains valid on arbitrary coherent superpositions of flux blocks. Pure winding blocks have K_def=0 and create no contradiction.

Use a canonical ground state as a variational trial for H_U. Then

    E_U <= E_0+(3/2)U N,
    kappa_g <K_def>_(ground,U) <= (3/2)U N.

The second inequality follows from positivity of U D, without perturbation series, a unique ground state or any gap. It holds for every H_U ground-state density operator. At M>=32 the accepted delta_inf>=3/50 and quadrature loss give delta_(ground,L)>3/100; conservatively kappa_g=3h/800 is available. Hence

    <K_def>/N <= 400 U/h.

This is useful when U/h is small; it is a bounded-density result, not exact absence of defects. The existing small-size argument supplies an existential all-cubic positive kappa_g, but no explicit numerical minimum is assigned to it here.

## Thermal density by quantum relative entropy

Let rho_U and rho_0 be the FULL physical Gibbs states at the same beta. Gibbs variational principle, using rho_0 as trial, gives F_U-F_0<=U<D>_0=(3/2)UN. Therefore

    S(rho_U||rho_0)=beta(F_U-F_0-U<D>_U) <= (3/2)beta U N.

Because K_def commutes with H_0, the variational entropy inequality for s K_def is particularly direct:

    s <K_def>_U <= S(rho_U||rho_0)+log Tr(rho_0 exp(s K_def)).

Use the already proved U=0 global moment bound, valid for 0<s<beta kappa_beta:

    <K_def>_U/N <= [(3/2)beta U +log(8)/N
       +3 log(1+exp(-(beta kappa_beta-s)))]/s.

With s=beta kappa_beta/2 this is

    <K_def>_U/N <= 3U/kappa_beta
       +2log(8)/(beta kappa_beta N)
       +6 log(1+exp(-beta kappa_beta/2))/(beta kappa_beta).

For M>=32,beta*h>=200 the accepted theorem permits kappa_beta=3h/800. The weak-U contribution is then800 U/h. This is volume-uniform apart from an explicitly vanishing finite-size term; no claim of a spectral gap or convergence of perturbation theory enters. It proves small mean local-defect density in the supplied perturbed Gibbs model. It does not transfer native reflection positivity to U>0.

The entropy inequality can be proved without an external concentration theorem: form sigma=exp(log rho_0+sK_def)/Z_s, use S(rho_U||sigma)>=0 and rearrange. Commutation makes Z_s the stated classical flux moment. All states are finite-dimensional and rho_0 is faithful at finite beta.

## What fails, and the next discriminating obligation

A global isolated-ground perturbation theorem would require U||D|| small relative to a finite-size isolation gap. Here ||D||<=9N, the active gap closes and wrong winding gaps are O(h/L), so that sufficient route has a shrinking U window. Failure of that sufficient condition is not proof of instability. The density estimates above avoid it entirely.

The entropy argument cannot preserve the contour tail at fixed U: its relative-entropy cost is extensive, so a binary event estimate can spend O(beta U N) on one local event. Neither the U=0 orbitwise free-energy penalty nor the global moment bound implies a uniform exterior-conditioned repair inequality. D mixes flux blocks, hence a fixed-flux free-energy comparison is no longer a sector decomposition of H_U.

A concrete next target is a local insertion bound for the imaginary-time expansion of U(D-3N/2), uniformly in volume: control connected flux-changing pair histories near a prescribed defect set, with denominator/time-integral decay priced by their defect energy and with cancellations/active bath treated explicitly. Such a bound must remain valid at repeated flux returns and arbitrary gapless active excitations; replacing each intermediate resolvent by the ground defect penalty is invalid on an unrestricted energy window. No such local bound is assumed here. The exact inequalities above are already positive tractable support; contour stability remains a sharper separate obligation.

## Sharper explicit ground coefficient and proof of the electric selection rule

At zero temperature and M>=32, delta_(ground,L)>=3/50-4*(3*pi²/(8*M²)). Using pi²<10 gives delta_(ground,L)>3/50-15/1024=1161/25600. Hence kappa_g=1161*h/204800 is a safe lower bound and

    <K_def>/N <= (102400/387)*(U/h).

The preceding400 bound remains valid but is weaker. The thermal800 coefficient is unchanged because its temperature budget is different.

Here is a direct all-size proof that the electric pair has zero diagonal flux block. Every edge of a cubic torus with extent L>=4 belongs to four distinct elementary plaquettes. Two distinct incident edges share at most one elementary plaquette: perpendicular directions share one when compatible, and collinear edges share none. This is true also at L=4, since the forward and backward neighbor are distinct and no elementary square repeats an edge. Thus some elementary plaquette contains exactly one edge of the pair. Z_e Z_f anticommutes with that plaquette's magnetic loop. A gauge cut intersects every cycle evenly, so the pair cannot be a cut. This proves its vanishing expectation in every orbit-block-diagonal state, with no chosen gauge representative. It also proves D mixes flux; the identity <D>=3N/2 cannot be promoted to D=(3N/2)I.

## Why the factor eight is exact as an overcount

For the periodic cubic cell complex, a link Z2 gauge class with prescribed elementary plaquette products, if consistent, has exactly eight possibilities distinguished by the three independent winding Wilson loops. The ratio of two solutions is a flat1-cochain; quotienting by vertex coboundaries gives H¹(T³;Z2)=(Z2)^3. This includes all flat winding sectors; no parity or spectator factor removes them. Each compatible assignment with k defects therefore contributes at most8 times the reference weight exp(-beta*kappa*k). Bounding compatible assignments by all subsets of the3N faces yields

    Tr rho0 exp(s K_def) <= 8*(1+exp(-(beta*kappa-s)))^(3N).

The denominator is bounded below by ONE canonical orbit's weight. The factor8 is deliberately not canceled against an unproved equality of winding weights. This overcount is safe for nonzero s and includes the canonical zero-defect term. The expectation of D in rho0 uses block diagonality, not an assumption that only the minimizing winding orbit occurs.

## Full quantum entropy derivation and precise imports

For finite-dimensional faithful rho0=exp(-beta H0)/Z0 and rhoU=exp(-beta HU)/ZU, direct logarithms give

    S(rhoU||rho0)=Tr rhoU(log rhoU-log rho0)
                 =beta(FU-F0-U Tr rhoU D).

The Gibbs variational principle follows from nonnegativity of quantum relative entropy, with no commutation of D and H0. Its trial rho0 gives FU-F0<=U Tr rho0D. For s>0 define sigma_s=exp(log rho0+sK_def)/Tr exp(log rho0+sK_def). Nonnegativity S(rhoU||sigma_s)>=0 gives the variational entropy bound used above. Since [K_def,H0]=0, the normalizing trace equals Tr rho0 exp(sK_def). No Golden–Thompson reversal, classicalization of rhoU, or commutation of HU with K_def is used. Quantum relative entropy nonnegativity and the finite-dimensional Gibbs variational principle are standard imported mathematics; the new content is their application to the native electric selection rule and certified flux moment.
