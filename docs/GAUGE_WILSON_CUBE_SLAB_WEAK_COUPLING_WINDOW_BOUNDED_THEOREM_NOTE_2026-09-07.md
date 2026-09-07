---
claim_id: gauge_wilson_cube_slab_weak_coupling_window_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_cube_slab_weak_coupling_window_check_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_cube_slab_character_mixing_bounded_theorem_note_2026-09-07
  - gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_note_2026-06-07
claim_scope: "For the supplied bare-Haar two-slice SU(3) Wilson cube slab, every fixed finite character window of D_beta/D_00 converges to the outer dimension vector with an explicit O(log(beta)/beta) bound. The fundamental ratio tends to3. The full-space normalized vacuum output norm diverges; no gap or physical coupling selection is claimed."
---

# Actual Wilson slab: normalized weak-coupling character windows

The actual stripped source matrix has a rank-one limit on every fixed finite character window, with entries d_lambda d_mu. This is a statement about the supplied finite Wilson slab, not the native diagonal coefficient packet. The same D00 normalization has an unbounded vacuum-output norm on the full character space, so the finite-window conclusion is not a bounded infinite-dimensional rank-one limit.

**Type:** bounded_theorem

## Status and direct dependencies

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
bodyType: bounded_theorem
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
```

Independent audit owns status authority.

- [Actual spatial mixing parent](GAUGE_WILSON_CUBE_SLAB_CHARACTER_MIXING_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the exact source map, full-space stripping,22face action, and strict positivity at all positive couplings.
- [SU3 coefficient/Schur bridge](GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE_NOTE_2026-06-07.md) supplies the representation conventions; dimensions are d_(p,q)=(p+1)(q+1)(p+q+2)/2.
- [Existing compact-Laplace endpoint source](GAUGE_VACUUM_PLAQUETTE_HIERARCHY_OBSTRUCTION_LEMMAS_BOUNDED_NOTE_2026-05-10.md) is prior-work context. Generic compact concentration is not claimed as new here; the quantitative proof below is explicit.

Primary exact support runner: [gauge_wilson_cube_slab_weak_coupling_window_check_2026_09_07.py](../scripts/gauge_wilson_cube_slab_weak_coupling_window_check_2026_09_07.py). It reports per_word_checks2, per_arithmetic_checks10, per_adverse_checks4, TOTAL16. These are exact freegroup/arithmetic checks, not numerical Haar or spectrum certification. The analytical concentration and representation estimates remain load bearing.


The finite action and bare-Haar source embedding are exactly those of the cube-slab mixing construction. This is not the supplied diagonal coefficient packet. Let s=t=beta≥1. There are24integrated spatial links in temporal gauge, ten unmarked spatial face halfweights, and twelve temporal weights. The two marked xy faces atz0 remain stripped. Write J(U)=ReTr(U)/3 and

E=Σ_(10spatial faces)(1−J(U_P))/2 + Σ_(12temporal faces)(1−J(U_P)).

E≥0, and the total weight is exp(17beta)exp(-beta E). Define ν_beta as the normalized positive probability measure proportional to exp(-beta E) on the24link Haar product. Exact source compression gives

D_lambda,mu/D_00 = Eν[conjugate(χ_lambda(W_output)) χ_mu(W_input)].

Both D and D00 are unnormalized in this formula; any common positive temporal or partition normalization cancels. This is the precise complex-character convention.

## Missing-face control at every configuration

The other five faces of a spatial cube form a disk spanning the marked loop. Peeling the disk, or gauge-fixing a tree, writes its boundary holonomy as a product of five transported face holonomies (possibly inverted). Each transport is a conjugation. The identity follows by cancelling each internal oriented edge word; it is the nonabelian disk/Bianchi identity, not a commuting approximation.

The Frobenius norm is invariant under unitary left/right multiplication and conjugation. Thus

||I−W_missing||F ≤Σ_(five faces)||I−U_P||F,

||I−W_missing||F²≤5Σ||I−U_P||F²
 =30Σ(1−J(U_P))≤60E.

This holds for both omitted faces at every configuration. In particular every action maximum E=0 has BOTH marked holonomiesI, even though their action factors were removed. The5face geometry is inherited from the previous cube construction; no uniqueness of a flat gauge representative is needed.

## Explicit concentration without a nonabelian saddle

For0<r≤1, the normalized Haar measure of the Frobenius ball B_r(I) inSU3 is at least(r/5)^18. Here is an elementary conservative bound: regard SU3 as a compact subset of R18 lying on the sphere of radius sqrt3. A maximal r-separated set has at most(1+2sqrt3/r)^18 points, by packing disjoint ambient radiusr/2balls inside the ambient radius sqrt3+r/2ball. Its radiusrballs cover the group. Bi-invariance of Frobenius distance and Haar measure gives vol(B_r)≥1/N≥[r/(r+2sqrt3)]^18≥(r/5)^18. Open/closed endpoints are handled by an arbitrarily small radius enlargement/limit. The exponent18 is deliberately ambient, not the intrinsic dimension8.

If all24links lie within Frobenius distance r ofI, every spatial face product is within4r and every temporal-gauge two-link product within2r. We may use the conservative4r for all22faces. Therefore1−J(U_P)=||I−U_P||F²/6≤8r²/3 and E≤136r²/3. At r=beta^-1/2,

Z_beta:=∫exp(-beta E)dHaar
 ≥ exp(-136/3) 5^-432 beta^-216.

Consequently Pν(E≥u)≤min(1,exp[A_beta−beta u]),

A_beta=136/3+432log5+216logbeta.

Integrating this tail yields

Eν E ≤(A_beta+1)/beta
 ≤[216logbeta+2731/3]/beta =:B_beta,

where log5<2. Also E≤34 follows from1−J≤2 and total weight17, so min(34,B_beta) is valid. No fitted constant, Haar saddle expansion or small-return cancellation is used. The partition factor is bounded directly.

## Fixed-representation quadratic character control

For highestweight lambda=(p,q), let d_lambda be its dimension and m_lambda=p+q. Then globally onSU3,

|χ_lambda(U)−d_lambda| ≤2d_lambda m_lambda² ||I−U||F².  (1)

For the trivial representation both sides vanish. For nontrivial lambda, if||I−U||op≥1, the claim follows from|χ−d|≤2d and m≥1. Otherwise the principal eigenangles satisfy|theta_j|<pi/3, and detU=1 forces their sum0. Thus U=exp(iX) for traceless HermitianX. The representation occurs in the tensor product of pfundamentals and qantifundamentals, so its infinitesimal Hermitian generator A obeys||A||op≤m||X||F and TrA=0. The latter follows because a trace of a Lie representation vanishes on the commutator algebra su3. Hence

|Tr(exp(iA))−d|≤Tr(A²)/2≤d m²||X||F²/2.

The elementary chord bound gives||X||F²≤(pi²/4)||I−U||F²; pi<4 then proves(1). This is a finite-label bound, with explicit growth in m andd; no uniform claim over increasing highestweights is made.

Using|χ_lambda|≤d_lambda, (1) and the missing-face bound gives

|D_lambda,mu/D_00−d_lambda d_mu|
 ≤120 d_lambda d_mu(m_lambda²+m_mu²) min(34,B_beta).  (2)

Thus for every fixed finite character window, the normalized matrix converges entrywise and in matrix operator norm to the rank-one outer product dd*. For an explicit window norm bound, let vectorsd=(d_lambda) andb=(d_lambda m_lambda²). Then the norm difference is at most240||d||2||b||2 min(34,B_beta). This is O(logbeta/beta). The normalization is D00, not the largest eigenvalue; the limiting top window eigenvalue is||d||² and every other window eigenvalue tends0. This is not a statement about an untruncated infinite-dimensional transfer spectrum.

## Fundamental mixing ratio

For the trivial/fundamental entry, complex conjugation of all link matrices preservesν and conjugates the source trace, so R_beta=D03/D00 is real. Exactly

3−R_beta = Eν[3−ReTr(W_input)]
 = (1/2)Eν||I−W_input||F²
 ≤30 min(34,B_beta).

The all-positive-coupling reflection theorem already proves R_beta>0. For every finite beta>0 the Gibbs density is strictly positive on the full Haar product, and the missing holonomy is not identicallyI; therefore the displayed expectation is strictly positive and R_beta<3. Consequently

0<R_beta<3, and R_beta→3 as beta→infinity,

with the explicit upper deficit bound above forbeta≥1. This does NOT prove monotonicity in beta. It shows convergence to maximal dimension-scaled mixing in this fixed entry, not that every finite-beta increment increases it.

## Novelty and boundaries

Existing hierarchy-obstruction/reduction-existence sources already prove generic finite-volume Wilson compact-Laplace plaquette endpoints. That general concentration principle is not new here. The added statement is the stripped two-slice observable: two omitted plaquette holonomies are forced toI by the weighted five-face caps, giving the actual source-matrix outer-dimension limit and an explicit finite-window rate. The source search found no existing matching statement, without claiming exhaustive absence from every historical file.

No physical beta is selected. The supplied finite bare-Haar map is unchanged, and no environment-dressed embedding, infinite-volume limit, high-representation limit or physical mass gap is asserted. Restoring the8temporal links gives the same normalized ratios by the previous gauge-change proof, but the24variable temporal-gauge representation is used for the explicit volume bound.

## Explicit nonabelian disk word

Gauge-fix three bottom boundary edges and four vertical edges toI, a spanning tree of the spatial cube. Let U be the fourth bottom edge; source loop is U orU^-1. Let top edges in positive x/y orientations be A,B,C,D. The top face is T=A B C^-1 D^-1. The four side faces, up to inversion, are A,B,D and S=U C^-1. Exactly

U=S D^-1 T^-1 A B.

The freegroup cancellation in check.py verifies this without assuming commutativity. Each factor is an actual face holonomy or its inverse in this gauge. Unitariy triangle inequality thus bounds||I−U||F by the five actual face deviations. Gauge conjugation restores the gauge-independent missing-loop norm statement. This is a concrete implementation of the disk step in DERIVATION.md, not a scalar surrogate.

The original twelve word/arithmetic checks are preserved in the canonical runner; four separate side-removal controls were added. They do not replace the analytic Haar-volume, concentration or representation proof.

## Adverse geometry control

The complete cap is necessary for the stated missing-face implication. In the explicit tree gauge above, remove the S=U C^-1 side constraint in BOTH temporal slices. Set A=B=C=D=I and U=diag(-1,-1,1), identically at both times. All retained spatial faces and all temporal faces areI, but the source holonomy is nonidentity with squared Frobenius deviation8. Thus the weakened20face action has a maximum with a nonflat omitted source. This is an adverse control for the cap argument, not the theorem's22face fixture; removing just one temporal copy is not asserted to give this counterexample.


## Additional corollary (2026-09-07): no bounded untruncated limit under D00 normalization

This is derived after the fixed-window proof, with its frozen bytes unchanged. Let A_beta=D_beta/D00 on the full central-character Hilbert space. For each finite beta it is a bounded positive operator: I is an isometry, Menv is bounded on the compact link product, C_t is bounded, and D00>0. No uniform-in-beta bound follows from these facts.

For every fixed finite setF of representations, Bessel's inequality and the fixed-entry limit with input vacuum give

||A_beta χ0||²≥Σ_(lambda∈F)|<χ_lambda,A_beta χ0>|² → Σ_(lambda∈F)d_lambda²

in the following precise sense: the finite right-hand side tends to the displayed sum, hence the liminf of the left side is at least that sum. Since these sums grow without bound asF enlarges, ||A_betaχ0||→infinity. Consequently ||A_beta||→infinity as well.

Thus this D00-normalized family has no bounded strong-operator limit and no bounded operator-norm limit on the untruncated central-character space. This uses a single fixed vacuum vector, not an interchange of a growing representation cutoff with beta. It does not require the uniform boundedness principle. The formal outer-dimension matrix is not the matrix of a bounded rank-one operator because the dimension vector is not inell².

No untruncated eigenvalue ratio, physical gap, high-label uniform asymptotic or monotonic norm-growth rate is inferred. Finite-window rank-one convergence remains valid and is exactly the premise of this distinction. A different normalization or a rescaled embedding could have a different limit and is not excluded.

## Proof history and check scope

The [durable packet](../.claude/science/physics-loops/spatial-wilson-weak-coupling-20260907/PROOF_REVIEW.md) records N1–N8, the original frozen proof, its independent review, the noncommutative word supplement and the separate untruncated norm corollary. These are after-the-fact navigation indexes; the original preregistration and proof bytes are preserved. The runner checks twelve original identities and four adverse controls; it does not numerically establish Haar concentration or operator convergence.
