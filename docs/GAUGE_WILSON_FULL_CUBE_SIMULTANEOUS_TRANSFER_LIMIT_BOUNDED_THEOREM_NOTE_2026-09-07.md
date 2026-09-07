---
claim_id: gauge_wilson_full_cube_simultaneous_transfer_limit_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_full_cube_transfer_geometry_check_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_full_cube_physical_transfer_geometry_bounded_theorem_note_2026-09-07
claim_scope: "Uniform actual full-transfer error kappa49/sqrt(beta) and simultaneous n204 sequence on global singlets, with genuine layer gluing under the supplied action; constants/onset and physical time unselected."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

For the supplied FULL gauge-invariant cube transfer, choose kappa_n=n²/t² and beta_n=n^204. After actual norm normalization, n genuine transfer steps and the stated oscillator-coordinate identification converge in operator norm to exp(-t H_eff), where H_eff=2(N1+N2+N3)+sqrt6(N4+N5), restricted to simultaneous-Ad singlets. The first positive limiting singlet energy is4 with multiplicity6. No microscopic physical time or action is selected.

The [full geometry and Haar theorem](GAUGE_WILSON_FULL_CUBE_PHYSICAL_TRANSFER_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the exact24face graph, onto physical Hilbert-space identification, covariance and positive limiting norm. Unlike a marked-source compression, this full physical space reduces T, so its powers glue the supplied layers without an environment-reset premise. The proof below retains an uncancelled first marginal Taylor term; it does not use the special two-source cancellation theorem or any first spectral coefficient.

# Full gauge-invariant cube transfer: kernel identification and a polynomial simultaneous limit

This proof follows the prospective contract in PREREGISTRATION.md and was written without reading orbital's geometry calculation. The exact modal covariance below is supplied by the independently reviewed full geometry theorem. The full-boundary transfer here is different from the earlier22-face marked-source compression: ALL24 faces are retained, and the entire local-gauge-invariant boundary space is used.

## 1. Exact transfer and why its powers glue layers

Let the spatial cube have8vertices and12edges. Its kinematic boundary space is L2(SU3^12,dHaar), with the vertex gauge group acting by U_e -> g_tail U_e g_head^-1. Let P_G be the normalized Haar-average orthogonal projector onto its invariant subspace H_G. Supply the Wilson half-potential M_beta, multiplying by the six spatial plaquette halfweights, and the twelve independent central temporal convolutions C_beta,kappa. The full positive transfer is

    T_beta,kappa=M_beta C_beta,kappa M_beta.

The spatial multiplication commutes with every local gauge action because plaquette traces are conjugation invariant. The convolution kernel also commutes: applying the same endpoint gauge transformations to U_e and V_e sends V_e U_e^-1 to its conjugate at the tail, leaving the central Wilson weight invariant. Hence [T,P_G]=0 exactly. The restriction T_G=T|H_G is a reducing restriction, not a compression onto a smaller noninvariant source family.

Consequently(T_G)^n=(T^n)|H_G. Kernel multiplication integrates all12 spatial links at every intermediate slice. The two neighboring spatial halfweights multiply to the full spatial weight at an internal slice, with six halfweights left at each endpoint. The twelve temporal weights occur at every step. Thus these powers are the corresponding genuine multilayer transfer of the SUPPLIED lattice action. This is the precise invariance premise absent for a marked-plaquette source map. It does not derive that action or select its physical time scale.

Use A=T_G/<1,T_G1>. This positive scalar normalization does not change its eigenvectors, and A/||A||=T_G/||T_G||. Repeated normalized powers therefore differ from the supplied microscopic transfer only by a scalar normalization, not by resetting omitted boundary variables.

## 2. Boundary gauge coordinates and exact source kernel

Fix one spatial spanning tree of7edges. Gauge fixing it represents H_G isometrically as L2(SU3^5) invariant under ONE simultaneous global conjugation of the five based-loop variables. Successive normalized Haar changes of variables eliminate the seven tree links without a gauge-volume multiplier. The residual root gauge acts simultaneously on all five loops. It is not permissible to project each loop independently onto class functions.

For a two-slice matrix element between such invariant boundary functions, reinsert8temporal gauge links by normalized Haar averaging and the corresponding independent slice gauge changes. Gauge invariance of both boundary functions and the spatial halfweights makes this identity exact. The restored graph has32edges/16vertices. Choose the7left-tree edges,7right-tree edges and one root temporal edge as a15-edge spanning tree. The remaining17group variables are five literal left boundary chords, five literal right boundary chords and seven temporal nuisance chords.

The exact normalized two-boundary matrix-element kernel in these coordinates is the7-group fiber integral

    k_beta,k(U,V)=Z_beta,k^-1 integral_(SU3^7) exp[-beta E_k(U,V,Y)]dY.

Here U,V each denote five group variables, and E_k has twelve spatial halfweights and twelve temporal weights k. The source functions are invariant under simultaneous conjugation within each five-tuple. Accordingly the operator kernel is projected onto these two global-Ad invariant spaces. The aligned frame density may have colored correlations; the correct projection averages one group element per whole boundary, not five per boundary.

The original Wilson maximum factor is exp[(6+12k)beta]; it and all positive temporal normalization factors cancel in A=T_G/<1,T_G1>. There is no beta-dependent gauge-fixing determinant introduced by the tree-coordinate representation.

## 3. Uniform saddle geometry and dimensions

All24flat faces force a globally flat connection on the open four-cube; in tree gauge this is the unique identity tuple. For k>=1, E_k>=E_1, so fixed nested star-shaped product exponential charts have a k-independent positive quadratic lower bound and a k-independent compact-complement gap. Each fixed-order action derivative grows at most linearly in k.

The total logarithm dimension is17*8=136. Each boundary has5*8=40 coordinates, so the joint marginal has80 coordinates and the nuisance integration56. Its Gaussian partition scales beta^-68, nuisance scaling is beta^-28, each boundary Haar volume scales beta^-20, and the normalized operator must be scaled by beta^-20. These are dimensions in the invariant-function representation on the full Lie space; replacing40 by the generic orbit-space dimension would be incorrect, just as replacing the eight-dimensional Haar scaling by the Cartan rank is incorrect for one central group.

The temporal Hessian has rank12. Indeed, in the adapted gauge its seven spatial-tree temporal-face equations force the seven nonroot temporal variations to zero, and the five remaining temporal equations then equate the left/right chord variations. These twelve independent equations leave five common boundary variations. The spatial Hessian is positive on this kernel: all six cube-face equations kill the five spatial cycle variations. Thus H_k=H_sp+kH_temp is positive and

    c k^12 <= det H_k <= C k^12, k>=1.

One way to see the determinant power without an explicit determinant formula is to factor H1 and diagonalize H1^-1/2 H_temp H1^-1/2. It has exactly12positive eigenvalues and five zero eigenvalues; det H_k=det H1 product_(12)[1+(k-1)nu_j]. Therefore the full Gaussian partition Z0(k) is between positive constants times k^-48.

## 4. Conditional exact covariance and Gaussian singlet limit

The reviewed finite geometry import is a FIXED k-independent spatial metric and mode basis in which the five boundary modes have lambda_j=4,4,4,6,6 and source covariance eigenvalues

    sigma_plus,j=6/lambda_j,
    sigma_minus,j=6/(lambda_j+4k).

Any fixed metric Jacobian changes a positive normalization constant, not a power of k or beta. The common adjoint-color action commutes with these fixed mode transformations.

For each fixed k>0 the same finite-dimensional fiber Laplace argument gives the actual beta^-20-dilated operator limit, projected onto global-Ad singlets in L2((su3)^5). The Haar chart map U_beta has factor beta^-10 times the square root of the five-group Haar density. It is a unitary only from the fixed chart subspace onto its expanding coordinate window, extended by zero as a partial isometry; it is not a global group-to-Lie-algebra unitary. The transformed kernel equals the normalized scaled80-dimensional marginal divided by the two boundary square-root Haar densities. Each limiting mode has

    omega_j=1/sqrt(sigma_plus,j sigma_minus,j),
    theta_j=(1-r_j)/(1+r_j), r_j=sqrt(lambda_j/(lambda_j+4k)),
    t_k,j=-log theta_j=2 artanh r_j.

After the product oscillator-coordinate unitary, the limiting Gaussian divided by its ground norm is exactly

    exp[-sum_(j=1)^5 t_k,j N_j],
    N_j=(-Delta_(w_j)+|w_j|²-8)/2,

RESTRICTED TO THE SINGLE SIMULTANEOUS-AD SINGLET SPACE. It is not a tensor product of five separately projected central operators. The unrestricted Gaussian commutes with this compact-group action, so the restriction follows by orthogonal projection of its complete Hermite decomposition.

Its leading eigenvalue is a fixed positive metric/Haar constant times

    product_j (sqrt(sigma_plus,j)+sqrt(sigma_minus,j))^-8.

It is uniformly bounded below by a positive constant for k>=1. Its invariant Gaussian ground state is the unrestricted ground state, so no singlet projection changes that norm. The normalized Gaussian joint density g_k has ||g_k||L2<=C k^10: each of five covariance determinants contributes k^-1 per color pair, with eight colors and the L2 determinant exponent -1/4. Fixed polynomial-weighted L2 norms have the same bound because the largest source covariance eigenvalue is bounded uniformly.

## 5. Uniform first-order marginal bound: no cubic cancellation assumed

Let epsilon=beta^-1/2. For the fixed-chart cutoff density F_k,epsilon, its first derivative is bounded by

    |partial_epsilon F_k,epsilon(z)| <= C k P(|z|)exp(-c|z|²).

The full partition first derivative is zero by oddness of its cubic action term and evenness of Haar, so its second-order estimate remains Ck²/beta. In contrast, the conditional means now span TEN retained source vectors, so the previous two-vector alternating-tensor cancellation is not imported. We use the honest first-order marginal estimate.

Write n_beta,k for the unnormalized scaled80-dimensional marginal, n0,k=Z0(k)g_k, and Ztilde=beta^68 Zphysical. Uniform Taylor bounds give

    ||n_beta,k-n0,k||L2 <= C k/sqrt(beta),
    |Ztilde-Z0(k)| <= C k²/beta.

For beta>=C k^50, Ztilde>=Z0/2. The exact normalization identity then yields

    ||p_beta,k-g_k||L2
      <= C[k^49/sqrt(beta)+k^60/beta].

Under this partition threshold the second term is bounded by a constant times the first: its ratio is k^11/sqrt(beta), which is bounded for beta>=Ck^50. Thus the normalized marginal error is Ck^49/sqrt(beta).

The compact nuisance tail has amplitude at most C beta^28 exp(-g beta); on the scaled source chart its L2 norm is at most C beta^48 exp(-g beta), since that chart has80-dimensional volume O(beta^40). The full scaled partition tail is C beta^68 exp(-g beta). These are bounded by the displayed Taylor rates with constants independent of k. Gaussian tails have only polynomial k-amplitude and a uniform quadratic exponent. No probability-tail estimate is used as a substitute for a kernel norm bound.

Boundary Haar square-root corrections cost at most C k^10/beta and hence are smaller. Global-Ad averaging contracts L2. If either boundary is outside the fixed chart, k_beta,k<=C beta^68 k^48 exp(-g beta), so the beta^-20-scaled off-chart operator has HS norm at most C beta^48 k^48 exp(-g beta), again absorbed by C k^49/sqrt(beta).

Uniform positivity of the Gaussian ground norm stabilizes actual norm normalization when beta>=C k^98. Oscillator scaling is unitary and introduces no additional k loss. Thus the actual normalized full-transfer chart operator differs from the singlet Gaussian contraction by at most

    C k^49/sqrt(beta), beta>=C k^98,

with the same bound on the omitted full-operator chart part.

## 6. Simultaneous actual full-transfer powers

Fix a mathematical t>0 and choose

    k_n=n²/t², beta_n=n^204.

The normalization threshold holds for all sufficiently large n, since k_n^98=C_t n^196. Contractive telescoping bounds the n-step error by

    C n k_n^49/sqrt(beta_n)=C_t n^-3.

It also controls the difference between the true full-transfer power and repeated chart compression, so a chart reset is not silently substituted for the physical boundary transfer. The exact reducing-space identity in Section1 legitimizes actual layer composition before taking limits.

For each spatial mode,

    t_k,j=sqrt(lambda_j)/sqrt(k)+O(k^-3/2),
    n t_k_n,j=t sqrt(lambda_j)+O_t(n^-2).

Because the five commuting number operators have nonnegative spectra, the normalized Gaussian powers converge in operator norm, with O_t(n^-2) error, to

    exp(-t H_eff),
    H_eff=2(N1+N2+N3)+sqrt(6)(N4+N5)

on global-Ad singlets. For example split the difference of the five commuting exponential factors and bound each by |a-b|/[e min(a,b)]. Combining gives a simultaneous actual normalized full-transfer limit with O_t(n^-2) error after the specified n-dependent boundary Haar and oscillator unitaries.

More precisely, with B_n=T_G,beta_n,k_n/||T_G,beta_n,k_n||, chart projection P_n and oscillator unitary D_n, the operator on the common singlet oscillator space is

    D_n U_n P_n B_n^n P_n U_n* D_n* -> exp(-t H_eff).

The omitted-power bound is ||B_n^n-(P_n B_n P_n)^n||<=C_t n^-3. Thus the displayed partial-isometry comparison and its controlled complement, rather than a nonexistent global chart unitary, are the precise full-operator statement.

This uses the exact reviewed modal covariance import together with the nonlinear bounds above, not an inference from a Gaussian proxy. Its constants and onset are unspecified. The sequence204 is deliberately crude. The supplied lattice action, anisotropy tuning and mathematical time remain inputs; no physical clock or continuum spacetime interpretation follows.

## 7. A spectral consequence with the correct singlet domain

The unique ground is a singlet. There is no degree-one singlet in the adjoint representation. The smallest positive singlet energy is4: two quanta among the three frequency2 spatial modes can be contracted by the unique invariant color bilinear form. Their mode labels form a symmetric3-by3 matrix, yielding multiplicity6. All other combinations have larger total energy, since the remaining two modes have frequency sqrt6>2. This count uses simultaneous singlets and would be wrong if five separate class-function restrictions were imposed. It is a property of the limiting supplied Gaussian transfer, not a physical mass-gap identification.

## Canonical finite interface and five reporting scopes

The [exact geometry helper](../scripts/gauge_wilson_full_cube_transfer_geometry_check_2026_09_07.py) retains all28 original scientific checks and adds three separately prospective checks of detM=1/384, its eight-color Jacobian and the136/80/56/40 dimensions. TOTAL31 counts those named scientific checks; resource and strict-output guards are additional execution checks. All original matrices and scientific values match the frozen raw result. The helper reads the actual existing physical-parent source to bind its SHA; this is a declared runtime audit dependency, not a new source to publish in this package.

N5 per_element: exact12edge spatial cube and32edge full slab; no marked-face stripping.
N5 per_site: seven boundary tree edges leave five cycles; full17chords split5+5+7.
N5 per_mode: eight colors carry one global Ad action; generalized spatial frequencies are4×3 and6×2.
N5 per_block: exact temporal Schur, metric and dimension checks support the analytical nonlinear proof rather than replacing it.
N5 lattice_wide: finite supplied action, unspecified uniform constants/onset and no selected physical time, continuum spacetime or thermodynamic claim.

## Durable proof and review packet

The [block28 packet](../.claude/science/physics-loops/full-cube-transfer-20260907/PROOF_REVIEW.md) preserves the independent full geometry, uniform kernel proof, root derivation, actual matrices, metric checks, failed control history and source-bound reviews. It records the original28 checks and three prospective supplements without portraying finite algebra as numerical certification of analytic uniform constants. This is a retrospective evidence index; audit authority remains separate.
