---
claim_id: record_map_keeps_mass_fraction_vacuum_weightlessness_reference_choice
claim_type: bounded_theorem
claim_scope: "Rank-one occupation pinching on the original periodic odd Fock fixture, qualified even-torus mass expectations, and supplied read-coupling band algebra and finite packet accelerations; no physical source or cosmological conclusion."
upstream_dependencies: []
runner: scripts/record_map_keeps_mass_fraction_vacuum_weightlessness_check_2026_09_04.py
---

# Occupation pinching, mass expectations, and finite read-coupled acceleration

Rank-one pinching in a supplied occupation basis removes hopping and keeps
diagonal mass. This exact finite identity does not select the physical record
basis or a gravitational source. Coupling an external field specifically to
that pinched density gives a useful conditional acceleration calculation.

**Original date:** 2026-09-04. **Correction date:** 2026-09-09.
**Author scope:** finite conditional support; no audit verdict is assigned.

## Supplied setting and resource-equivalent fixture

Use a real symmetric KS nearest-neighbor hopping matrix M with signs
`eta=(1,(-1)^x,(-1)^(x+y))`, `Gamma=(-1)^(x+y+z)`, and `H=M+m Gamma`.
The covariance fills negative energies and half fills zero modes. Energies are
counted from I/2; this is not subtraction of the filled sea itself.
Stipulate W1: rank-one projectors onto **full occupation configurations**, so
`D(O)=sum_r |r><r|O|r><r|=diag(O)`. Stipulate separately a source/reference
convention and, for T3, coupling toD(H). A different decomposition, a partial
pinching, or a time/history readout is not covered. Born statistics, physical
record formation and a fine-lattice carrier are unaccepted bridges here;
`B_v=I-2n_v` is a model definition, not an established six-record realization.

The original Fock fixture is **periodic2x2x3**, dimension4096, with duplicated
wrapped bonds as implemented. Its odd periodic direction is not bipartite;
the even-torus anticommutator formula below is not applied to it. Every one
of its original bonds remains. Operators are sparse and pinching is diagonal
contraction. The corrected ground-state calculation uses sparse eigsh with
a deterministic starting vector, checks its residual and energy against the
independent sum of negative one-body levels. This is the same Fock Hamiltonian
as the old dense computation, not a smaller or bipartite replacement fixture.
No4096x4096 dense matrix or density matrix is allocated. The largest dense
matrices elsewhere remain1728x1728 for the original12^3 one-body fixture.

Other original fixtures remain periodic4^3,6^3,8^3,12^3 and a96x32x4 slab
open in x, periodic in y,z. All scientific premises are supplied definitions
here and in the runner; no historical carrier, source, or cosmological grade
is consumed.

## T1 — exact pinching identity in the chosen decomposition

A hopping term `c_v^dagger c_j`, j!=v, changes occupation configuration,
so its diagonal vanishes. Diagonal number operators are retained. Thus

```text
D(eps_hop_v)=0,
D(eps_total_v)=m*eps_v*(n_v-1/2)=-(m/2)*eps_v*B_v.
```

The sparse Fock checks retain exact floating zeros at all12 sites, and the
one-particle4^3 diagonal check agrees. The historical350.542437 Frobenius norm
is for **totalSUMHOP**, not each local density. Every occupation-diagonal
observable survives, while this hopping energy does not. That is a statement
about W1, not a theorem that all record maps erase all correlation energy.

## T2 — qualified even-torus formula and the dephased twin

On the bipartite even tori, `{M,Gamma}=0`, so
`H²=M²+m²I`. For m!=0 the gap makes
`P=(I-H/sqrt(H²))/2` a spectral projector. The diagonal hopping contribution
to sign(H) vanishes by bipartite block structure; consequently

```text
r_v=m*eps_v*(P_vv-1/2)
   =-(m²/2)*[(M²+m²I)^(-1/2)]_vv.
```

The inverse square root requires a gap. At m0 the diagonal mass operator is
zero directly; code returns zero without multiplying a singular inverse by
zero. The half-occupied zero modes are a covariance, not a projector.
Original8^3 masses.3,1,2,6 retain the1e-11 formula gate; representative
read densities are-.021413851,-.201703228,-.648782512,-2.781026670.
On12^3 m1 the density is approximately-.200917464424 per site. Uniform
**positive** H(1,1) rescaling preserves the sea covariance and yields
chi_read=r_v; at8^3 m1 it is about15.52percent of total response-1.299638.
This uniform statement does not apply to arbitrary fields or H(2,1).

For the same periodic2x2x3 Fock ground state g, `rho_D=D(|g><g|)` has exactly
the same **full occupation distribution** `|g_r|²`; therefore every function
of that instantaneous occupation configuration has the same expectation.
Total energies differ: historical values approximately-19.750491965 versus
-1.680186677, difference-1.505859 per site, all from hopping. The sparse
replacement measures the same quantities and independently validates the
ground energy. The equality of the two copied probability vectors is a
consequence of the definition, not an independent scientific test.
It follows that this one distribution cannot reconstruct total energy for
all states. Other record decompositions, correlations encoded in other
observables, or time/history readouts remain open.

The original6^3 relation `<n_v>_{-m}=1-<n_v>_m` remains tested for
m0,.5,1,2; maximum offsets from half filling are approximately
0,.106445405,.198338711,.323427762. It follows from the qualified even-torus
formula for nonzero m, with the chosen symmetric zero-mode convention at m0.
The separate sea mass-fraction rows return the same mass density twice and
are explicitly definition checks, not independent evidence for a source law.

## T3 — supplied read coupling, lattice speed, and finite packets

**Additionally stipulate** `H_Phi=H0+sum_v Phi_v*D(eps_total_v)`.
This is alpha0,beta1 in the supplied family; W1 alone does not require that
coupling. On an even bipartite lattice, for a normalized energy eigenvector
with E!=0, `{H,Gamma}=2mI` gives `m<Gamma>=m²/E`.
The original nine12^3 checks select three positions in the positive-energy
list at each mass. They are not three specified momenta. Identifying this
quantity with a Lorentz scalar or stress-tensor trace requires extra
continuum and stress-tensor premises, absent here.

In the supplied band description
`E²=m²+sum_a(2-2cos p_a)`, with coarse coordinate spacing2,
`v_a=2sin(p_a)/E` and limiting c=2. The parameter
`chi=1-m²/E²` is generally **not** v²/c². The original table is relabeled
sqrt(chi), with its values and computations preserved; its chi0 endpoint
at fixed nonzero transverse momentum uses the stated large-mass limit.

Under the stipulated leading-band acceleration expression
`a_x/g=-4*w*E_xx+4*E_x*w_x`, taking `w=m²/E` gives
`a_x/g=-4*m²*cos(p_x)/E²` for E>0. The two independently coded formula
forms still agree on the original12x4 momentum/mass grid. At p0,m>0 the
result is-4; at p_x0 it is-4(1-chi). This is not the exact GR velocity law.
A direct lattice counterexample fixes m=sqrt2,p_x=p_z0 and chooses p_y=pi/3
or pi/2: **both have v/c=.5**, but acceleration is **-8/3 versus-2**.
The runner evaluates the actualdispersion and acceleration functions for both.
At m0 this particular coupling has dH/dPhi=0; no conclusion about physical
photons or a curvature/light-deflection factor follows.

The original slab computation remains: gradient2e-4, widths10/14/20, time0–10
in.25 increments, Chebyshev propagation, and the Ehrenfest double commutator.
The central derivative has O(g²) error for smooth dependence. Its final
Richardson combination uses widths14/20 and assumes a leading1/sigma²
expansion. Historical extrapolated read/tot values are approximately
-3.908944/-3.996371 at m1,p_y0, -.871052/-3.995122 at m.4,p_y=.7854,
and0/-3.993629 at m0,p_y=.7854. The largest read discrepancy about.091056
remains under the original.1 gate. Finite momentum spread is plausible but
its contribution has not been isolated from filtering, boundary, field,
propagation and width-expansion errors. No all-mass universality or exact
finite-packet band law is proved. Deterministic inputs do not imply bitwise
cross-platform reproducibility.

## T4 — no cosmological inference from reference subtraction

The original separate arithmetic `3/R²>0` for finiteR>0 is retained at
R1,3,10,1e3,1e6,1e12, with limitzero asR tends to infinity. If an Einstein
vacuum equation and a de Sitter radiusR are independently supplied, a geometric
Lambda=3/R² identity follows; an independently supplied roundS3 has the
corresponding spectral identity. This finite Newtonian model supplies neither.

P0 removes any additive constant source, so zero sea-referenced vacuum excess
cannot determine the cosmological Lambda or radius and cannot exclude a
de Sitter solution. The old conclusion that this subtraction 'evacuates the
antecedent' is withdrawn. Both nonzero model densities remain printed; no
geometric or physical vacuum conclusion is read from their magnitudes.

Physical source selection, record-carrier realization and any physical
massless deflection are open. The finite positive pinching/algebra/packet
results are retained without a broad rejection of readability-based theories.

## Evidence and next use

Primary: [`scripts/record_map_keeps_mass_fraction_vacuum_weightlessness_check_2026_09_04.py`](../scripts/record_map_keeps_mass_fraction_vacuum_weightlessness_check_2026_09_04.py). Current evidence: [source/input-bound
runner cache](../logs/runner-cache/record_map_keeps_mass_fraction_vacuum_weightlessness_check_2026_09_04.txt); this cache records actual finite results, not a
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
