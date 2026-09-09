---
claim_type: bounded_theorem
claim_scope: "Finite static Regge/Poisson comparisons on four momenta and an 8-cubed torus, gauge-dependent metric readouts, nonunique edge maps and conditional nonzero-mode exponent selection. The Poisson sign and bridge normalization are explicit; physical formation, curvature, global spectral and arbitrary-torus claims remain unestablished."
runner: scripts/formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.py
---

# Finite static Regge source response under a supplied endpoint-mean field

**Date:** 2026-09-09 source correction.
**Type:** bounded_theorem.
**Primary runner:** [formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.py](../scripts/formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.py).
**Runner cache:** [source-bound actual execution](../logs/runner-cache/formation_rate_defines_static_regge_edges_exactly_check_2026_09_03.txt).
**History:** [correction record and six exact original bodies](../.claude/science/physics-loops/regge-correction-20260909/CORRECTION_HISTORY.md).
The historical filename is a recovery key. This title and scope supersede its headline.

```yaml
actual_current_surface_status: bounded-support
trace_class: frontier_discovery
artifact_role: theorem
reachability_to_target: unknown_frontier
next_trace_action: "Keep finite diagnostics and conditional algebra separate from physical suppliers and unresolved global statements."
```

## Construction, premises and current interfaces

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select this action,
clock, source coupling, rate, metric readout or physical gravity interpretation.
A site has at most one permanent Record. A repeated tick or a local formation
rate is additional structure, not a count automatically supplied by Record.
The [kinetic-form primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) supplies c_t=c_s only.
Use a supplied Euclidean Z^3 x Z_tau path complex, edge lengths, action
S_R=sum_t A_t delta_t, its orientation and G. A later complex-frequency
continuation is a mathematical comparator, not an OS reconstruction theorem.

The actual unchanged R4 helper supplies the 24-simplex, 15-edge, 50-hinge
construction, area/angle derivatives and finite nonlinear box action. Its full
callable closure has no local grandchildren or external data. This primary's
precomputed rows, continued Q and batched maps are explicit local implementations;
old g1 probe names are copy provenance only, not required available files or
accepted parent campaigns. The [corrected spectral sibling](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md)
supplies the finite spectral/projection boundary, not a physical graviton theorem.
The older spatial/4D geometry notes describe the historical construction;
their broad conclusions and status rhetoric are not imported.

Let h_nu=Phi(-2nu,-2nu,-2nu,+2,0,...,0) in component order
xx,yy,zz,tt,xy,xz,xt,yz,yt,zt. The endpoint-mean map has
(M_AM h)_v=(v^T h v)/(2|v|) [1+exp(i k.v)]/2.
The line map replaces that last factor by (exp(i k.v)-1)/(i k.v).
The residuals are E=Q M h and E_h=M^dagger E at real static k.
Set khat^2=sum_i 4 sin^2(k_i/2), Delta=-khat^2, and exclude k=0 when dividing.

The optional reading r/r0=1+Phi, temporal length 1+Phi, spatial length
1-nu Phi and worldline action m sum l_tau is supplied. It does not follow
from the previous open #7925 package. In the [current density-ruler note](THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_AND_THE_HALF_FILLED_SEA_SUPPLIES_ZERO_BOUNDED_THEOREM_NOTE_2026-09-03.md),
kappa is a pointwise differentiable response, not an arbitrary regression slope;
a constant potential can change the hop-normalized mass ratio. With alpha=2,
beta=1 it is m(1+c)/(1+2c), not invariant under c shifts. Thus fixing a
zero-mean representative is an additional boundary convention.
If a symmetric differentiable homogeneous degree-one endpoint rule g is chosen,
g(a,a)=a and symmetry imply both partial derivatives at (a,a) equal 1/2.
Only its linearization is then the endpoint mean; these regularity/homogeneity
assumptions and a physical interpretation of g are not derived here.

## T1: finite provenance and continuation witnesses

Q_grid, Q_an, M_line and QEH match the actual R4 functions at the declared real
momenta, with errors below 1e-15. The three K_DISP fixtures at magnitudes .5,1,2
have relative singular-value nullities seven at the proposed scalar dispersion
and five at frequency 1.05 times it. This is the actual three-row observation,
not a complete spectral proof. All ranks throughout are thresholded numerical
ranks. R4 has a seeded random main fixture (seed 5), although this primary does
not call R4.main; its own declared momenta and box perturbation are fixed.

## T2: the static finite identity and its sign

At the four K_STATIC values (.37,-.81,.22), (1.9,.4,-2.3), (2.9,2.7,-3),
(.013,.007,-.02), with k_tau=0, the original tests give

```text
M_AM^dagger Q M_AM h_1(Phi=1) = -khat^2 e_tt
Q M_AM h_1(Phi=1) = -2 khat^2 e_tau
Q delta_l = +2 Delta Phi e_tau.
```

The plus sign in +2 Delta is essential. The last relation is the position-space
reading of the tested symbol relation, not the old erroneous -2 Delta claim.
The maximum four-point residual is 5.4e-15. The unchanged 8^3 FFT test uses
Phi(k)=-1/khat^2 for all 511 nonzero modes and Phi(0)=0, and yields
(Q delta_l)_tau=2(delta_x0-1/N) within 1.3e-16, other classes within 2.8e-16.
Linearity supports superpositions of modes on this same tested grid to numerical
precision. No exact Laurent-coefficient identity for arbitrary real k or every
torus is proved by four points plus a finite grid. Those stronger claims remain open.

For the supplied linearized equation Q delta_l=8 pi G P0 rho e_tau, the
relation gives Delta Phi=4 pi G P0 rho. The [weak-field bridge](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
defines phi=(-Delta)^(-1)P0 rho, positive for a positive isolated source in its
large-distance convention, and test response 1-phi. Thus the required conversion
is **Phi=-4 pi G phi**, with test response 1+Phi after the same coupling
normalization. Phi and the bridge's phi are not the same variable. The constant
mode is removed; a single nonneutral periodic source is not solvable without
that background. A -Gm/r asymptotic additionally needs an infinite-volume/Green
kernel theorem and its limit order, not the present 8^3 calculation.

## T3: when the exponent is selected

E_h(nu) is affine because h_nu is affine. On the four tested modes its tt slot
is -nu khat^2; changing nu does not affect only the spatial slots. Write
E_h(nu)=E_h(1)+(nu-1)D. In the spatial slots E_h(1)=0 on the tested identity,
and the measured max spatial |D|/khat^2 is at least .338. Therefore, conditional
on that identity and a mode with Phi(k) nonzero and at least one spatial
D_ij(k) nonzero, demanding zero spatial source gives
0=Phi(k)(nu-1)D_ij(k), hence nu=1. This short linear argument does not apply
to k=0, a zero field, vanishing D, or a supplied spatial stress that balances D.
The explicit constant-field control has Q(0)M_AM(0)h_nu approximately zero
for nu=0,1,2: a constant field cannot select nu. The two small-k comparisons
retain the 3.1e-4 deviation from the continuum tidal comparator; they do not
prove the global coefficient identity or its asymptotic remainder.

## T4: solution classes and representative-dependent readouts

The source e_tau lies in the numerical range of Q at the four momenta and all
511 nonzero grid modes; residuals are 6.1e-12 and 3.3e-14. The numerical kernel
dimension is five there. The pseudoinverse solution and the rate ansatz with
M=sigma/2 agree modulo the **full** kernel, with relative residual 1e-11 on
the four points and position-space residual 2.1e-16 on the grid. This is useful
finite linear algebra, not uniqueness of an edge representative.

The old routine name gauge_invariants is retained for source compatibility;
it actually applies pinv(M_AM), then Phi_read=h_tt/2 and
Psi_read=-P_ij h_ij/4 using P built from 2 sin(k_i/2). These readouts are not
invariant under the full vertex-displacement gauge family. At
k=(1.9,.4,-2.3,0), adding Gamma e_x leaves Q delta_l unchanged to about
3.1e-15 but changes Phi_read by -.015790282065 i and Psi_read by
+.061356662840 i. The gauge vector's distance from im M_AM is about .2802.
The original six smallest axial grid readouts, Psi_read/Phi_read=1 and
Phi_read khat^2=-1/2, remain properties of that chosen pseudoinverse
representative only. They are not lattice gauge observables or a metric slip theorem.

## T5: two named rules and a nonunique family

The retained comparison gives line-map residuals .0071,.48,4.5,2.7e-9 at the
four points, and torus source coefficients .90025 versus 1.00000 for endpoint
mean. It distinguishes these two named maps on these tests. It does not derive
a unique edge rule. Whenever Q Gamma=0, M'=M_AM+Gamma B has the same Q M,
and at real k the same M'^dagger Q M'=M_AM^dagger Q M_AM (Q is Hermitian).
For static k the temporal row of Gamma is zero. The explicit real B with
B[x,tt]=.3 changes the map by norm .2458628 at (.37,-.81,.22,0), preserves
the temporal row and both residual operators within 1e-14. This is a family
of gauge-related alternatives, not a claim that all inequivalent maps work.

## T6: time-dependent residuals and continuum TT comparisons

The two retained real Euclidean 4-momenta yield nonzero spatial/mixed residuals;
the smaller has continuum-comparator error below 5e-3. This falsifies a vacuum
solution for those ansatz fixtures. Calling the residual a physical stress or
momentum density adds a source interpretation. No complete time-dependent
no-go is proved. At the three continued frequency fixtures the rate direction
has |Q u|/|u|=.340,1.601,5.960, while two additional singular values are small.
Its zero algebraic dot products with h_xy and h_xx-h_yy are continuum TT
comparisons for k along z; they are not overlaps with all finite-k null modes.
The count 10-4=6 is an off-shell metric-component quotient at a nonzero momentum,
not six propagating physical degrees of freedom. Neither its remaining five
directions nor the two approximate spectral directions are identified as a
physical graviton here.

The [current two-weight note](THE_SPATIAL_HALF_OF_THE_METRIC_IS_ONE_DECLARED_WEIGHT_ON_THE_HOP_TERM_FREE_FALL_AND_LIGHT_BENDING_AT_FACTOR_TWO_BOUNDED_THEOREM_NOTE_2026-09-03.md) calls alpha/beta a scalar-symbol
transverse acceleration-coefficient ratio under its hypotheses. The optional
identification alpha=1+nu,beta=1 gives two when nu=1; it is not an exact finite
light-bending or ray-curvature factor. Its isotropic metric comparison requires
low momentum and the supplied Hamiltonian. No physical acceleration or curvature
is computed by this Regge runner.

## T7: the actual endpoint and action checks

The position-space endpoint-mean field matches its Fourier map at every site
and class on the 8^3 box at k=2pi(1,2,0)/8 within 1.8e-15. On the 3^4 box,
one cosine rate direction at k=(2pi/3,0,0,0) with central-difference step 1e-4
has S_R''=-243.000674 versus Bloch -243.000000 and the tested source-identity
prediction -243.000000; S_R(flat)=3.3e-12. This preserves the numerical
normalization check. One direction and one step do not validate every tensor
coefficient, prove equality, or attribute all error to an O(step^2) remainder.

## Evidence and remaining suppliers

All thirteen original predicates, IDs and numeric parameters remain with
corrected scope labels. Four new checks enforce the signed response, actual
gauge-readout counterexample, gauge-shifted map and constant-field exception.
Own note, the corrected sibling, actual helper, memo, kinetic declaration and
three used current bridge/interface notes are guarded inputs. Exact original
notes/runners/caches remain history outside active discovery. The finite and
conditional results survive without a physical rate interpretation. No action,
orientation, G, tick, source rule, Record-length law, OS reconstruction,
nonlinear solution, universal edge-rule exclusion or route quota is derived.
Formal audit remains deferred.
