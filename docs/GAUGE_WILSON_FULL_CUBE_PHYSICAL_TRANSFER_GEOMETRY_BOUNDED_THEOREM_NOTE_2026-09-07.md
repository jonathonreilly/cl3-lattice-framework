---
claim_id: gauge_wilson_full_cube_physical_transfer_geometry_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_full_cube_transfer_geometry_check_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_cube_slab_character_mixing_bounded_theorem_note_2026-09-07
  - gauge_wilson_cube_slab_exact_covariance_central_gaussian_spectrum_bounded_theorem_note_2026-09-07
claim_scope: "Actual full24face SU3 physical transfer, onto gauge coordinates, exact five-mode covariance and simultaneous-Ad Gaussian spectrum; no physical action/time selection."
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

This source treats the FULL physical boundary space of the supplied finite SU(3) cube, with all24 two-slice faces retained. Tree gauge fixing is onto that physical space, so its transfer powers glue complete intermediate boundaries. The earlier22-face marked-loop source compression is not used here.

The [physical supplied full-transfer definition](GAUGE_WILSON_CUBE_SLAB_CHARACTER_MIXING_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the Wilson action and its full T before marked-source stripping. The [normalized Haar convention](GAUGE_WILSON_CUBE_SLAB_EXACT_COVARIANCE_CENTRAL_GAUSSIAN_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies j0=1/(16sqrt3 pi^5). No two-source cubic-cancellation result, first spectral correction or compressed-source composition theorem is imported. The action and physical scale remain supplied.

# Full gauge-invariant cube transfer: exact geometry, gluing and Gaussian modes

This is a different declared supplied model from the22-weighted-face marked-loop compression. All24 faces are present. The original source already defines the full transfer T=M0 Menv C Menv M0; here Msp=M0 Menv includes all six spatial halfweights. The calculation does not strip a marked face or insert the constant-spectator source map I. Canonical source consulted: GAUGE_WILSON_CUBE_SLAB_CHARACTER_MIXING_BOUNDED_THEOREM_NOTE_2026-09-07.md, full-T definition and source-compression equations; its hash is in result.json. Preregistration preceded the independent integer-graph computation. No root result or alternative geometry raw was read.

## 1. Exact physical Hilbert space and full transfer

On an oriented spatial cube let U=(U_e) be12 SU3 links with normalized product Haar. The gauge group SU3^8 acts by U_e -> g_tail U_e g_head^-1. Let Hphys be the invariant subspace of L2(SU3^12). Pick a seven-edge spanning tree rooted at vertex0. Recursive tree gauge sends its links toI; every chord becomes its based fundamental-loop holonomy X_i, i=1,...,5. A change of root frame conjugates all five X_i simultaneously.

Gauge-invariant f is therefore determined by a function F(X_1,...,X_5) invariant under ONE simultaneous SU3 conjugation. Conversely every such F gives an invariant f. The recursive changes of link variables are left/right Haar translations; the seven tree integrations contribute1. Thus the correspondence is an exact onto isometry

 Hphys = L2(SU3^5, product Haar)^simultaneous Ad.

This is not five independent class-function spaces. Generic mixed traces, such as Tr(X1 X2), are admissible and cannot be removed by independent conjugations of X1 and X2.

For w_b(U)=exp[b ReTr(U)/3], define Msp(U)=product_(six faces) w_(beta/2)(U_face), and C_(k beta)(V,U)=product_(12 edges) w_(k beta)(V_e U_e^-1), k>0. The bounded positive operator T=Msp C Msp preserves Hphys: multiplication by face weights is gauge invariant, and central link convolution commutes with the gauge action. Positivity follows from positive Wilson convolution, not only pointwise positivity of a kernel. No additional source projection is made when restricting T to this reducing subspace.

Restoring eight temporal links is exact in gauge-invariant matrix elements. Those links form a matching forest and can be gauged toI by transformations on the upper boundary; central physical boundary functions are unchanged. Their normalized Haar integrations contribute1. Alternatively fix the15-edge tree consisting of the seven spatial tree edges on each boundary and one temporal edge at the roots. Its remaining17 chords are exactly5 left,5 right and7 temporal-nuisance variables. The based source functions involve all five boundary chord variables; independent conjugation averaging at each endpoint gives the physical kernel, with the SAME conjugation applied to all five variables at that endpoint.

## 2. Exact powers glue without environment reset

For finite beta,k the group is compact and the kernels are continuous/bounded. Iterated Haar integration is justified directly. The kernel of T^n integrates over all12 intermediate spatial links at every time. Each internal slice carries Msp², i.e. a full spatial Wilson weight beta; only the two external slices carry halfweights. Every adjacent slice pair carries all12 temporal weights k beta. This is exactly the longer slab action in temporal gauge.

Because T commutes with the gauge projection P, (T restricted Hphys)^n=T^n restricted Hphys. The tree-coordinate isometry is onto Hphys, so its coordinate transform has exactly the same power property. There is no I I* inserted between steps and no reset of omitted spectator modes. By contrast, (I* T I)^n generally inserts I I* and need not equal I* T^n I. This closes the reset distinction for the FULL physical transfer under the supplied action; it does not prove that the action is physically selected.

## 3. Independent exact spatial geometry and temporal elimination

The checker labels vertices0,...,7 with coordinate axes in bits0,1,2 and positive edges v -> v xor2^a whenever bit a is0. A greedy spanning tree is frozen by this ordering. Let D be the8-by12 vertex-edge incidence, Dt its rooted seven-by-seven tree block, and Dc its chord block. The five fundamental-cycle rows C have chord block I5 and tree block (-Dt^-1 Dc)^T. Thus DC^T=0 and C J=I, where J embeds chord coordinates into links with tree links zero.

Let F be the six oriented spatial face rows. Since each face is a cycle, F=B C where B=F[:,chords]. Define

 M=(C C^T)^-1,  K=B^T B.

Both are positive definite. For two boundary tree-chord coordinates x,y, the temporal quadratic form is k||J(x-y)+D_root^T z||², where z contains the seven remaining temporal Lie variables. Minimizing over z projects onto the cycle subspace. With Pcycle=I-D_root^T(D_root D_root^T)^-1 D_root,

 J^T Pcycle J = (C C^T)^-1 = M.

The minimized temporal term is k(x-y)^T M(x-y). Adding the two six-face halfweights gives the boundary Hessian

 Hboundary = [[K/2+kM, -kM],[-kM,K/2+kM]].

For Tr(TaTb)=delta_ab the action is(1/6)sum_color q^T H q. Therefore the per-color boundary covariance is3 Hboundary^-1. The checker separately constructs the complete24-face17-chord Hessian with five left/five right/seven temporal variables, and verifies this Schur complement symbolically in k. It also verifies the cycle projection identity independently. These are not comparisons between two encodings of the already assumed reduced formula.

## 4. Exact generalized modes and Gaussian normalization

Whiten the cycle metric with z=M^(1/2)x. The spatial precision becomes L=M^-1/2 K M^-1/2. Its spectrum equals the nonzero spectrum of F F^T, since F=BC. Orient faces outward: each has four edges and shares one oppositely oriented edge with each adjacent face. Hence F F^T is the Laplacian of the octahedral dual graph K_(2,2,2), up to orientation conjugation. This graph has Laplacian spectrum0 once,4 three times and6 twice. The exact five-dimensional determinant calculation independently gives det(K-lambda M)/det M=(4-lambda)^3(6-lambda)^2.

After metric whitening and a real orthogonal mode change, each color of a spatial mode with lambda in{4,6} has plus/minus covariance

 sigma_plus=6/lambda,  sigma_minus=6/(lambda+4k).

The normalized plus/minus coordinates are(zL+zR)/sqrt2 and(zL-zR)/sqrt2. The original tree-coordinate statements are Cov_plus=6K^-1 and Cov_minus=6(K+4kM)^-1; confusing these with scalar mode covariances would omit metric factors.

The scalar Gaussian kernel for one color/mode has exponent

 -A(x²+y²)+Bxy,
 A=(lambda+2k)/12, B=k/3.

Thus omega=sqrt(4A²-B²)=sqrt(lambda(lambda+4k))/6. With r=sqrt(lambda/(lambda+4k)), its Mehler ratio is

 theta=B/(2A+omega)=(1-r)/(1+r),
 t_lambda=-log theta=2 asinh(sqrt(lambda)/(2sqrt k)).

Dividing the Gaussian transfer by its top eigenvalue gives exp(-sum_j t_lambda(j) N_j), with eight oscillator colors in each of the five spatial modes. The metric/mode and oscillator-width coordinate changes are unitary after including their ordinary Jacobian factors. All these spatial-linear changes commute with simultaneous AdSU3, so they preserve the physical invariant subspace. Absolute normalization is fixed in the added Haar-metric section below. It is unnecessary for the normalized eigenratio, but its fixed Jacobian must not be omitted if absolute amplitudes are stated.

## 5. Global singlets and the first excitation

The five oscillator species each transform in the eight-dimensional adjoint representation of SU3. The ground Gaussian is invariant and unique. There is no linear invariant because su3 has zero center. The invariant bilinear on the adjoint is unique up to scalar: an invariant bilinear identifies an intertwiner of the complexified simple adjoint with itself, hence is proportional to the trace/Killing form. It is symmetric. Therefore every pair of spatial species admits the scalar color contraction sum_a x_(i,a)x_(j,a), with the Gaussian constant subtracted on diagonal species. Invariant degree-two states form Sym² of the five-dimensional species space, not merely five radial polynomials.

For k>0, t4<t6. The lowest singlet excitation uses two quanta from the three lambda4 species and has excitation exponent2t4, eigenratio theta4², and multiplicity dim Sym²(R3)=6. The three diagonal excitations and three offdiagonal contractions are linearly independent. There is no single-quantum singlet; any degree>=3 costs at least3t4>2t4, and using a lambda6 quantum increases the two-quantum cost. Five independent class-function restrictions would discard the offdiagonal contractions and falsely report only three lowest states.

Set k_n=n²/t² for a fixed positive parameter t. Then n t_lambda(k_n) -> t sqrt(lambda). After the stated oscillator-width identifications, the Gaussian n-step normalized eigenvalues tend to exp[-t sum_j sqrt(lambda_j)N_j]. Its lowest singlet excitation energy is4 with multiplicity6: two frequency2 quanta. All other two-quantum possibilities cost2+sqrt6 or2sqrt6>4; degree>=3 costs>=6. This is a Gaussian family statement, not a uniform actual-Wilson double-scaling theorem.

## 6. Controls, limitations and unresolved analytic work

The checker uses exact rational/symbolic arithmetic and no fitted eigenvalues. It verifies covariance at k=1/3,1,5/2 plus the symbolic full Schur identity. Removing one actual spatial face changes the generalized characteristic polynomial. Leaving the boundary link gradients ungauged produces seven zero curl modes. Replacing global Ad by independent class functions loses exactly the three mixed lowest quadratic invariants. The first run failed only because SymPy could not order a radical eigenvalue expression; the preserved repair uses exact Sylvester minors without altering inputs.

For fixed k, the restored full24-face action has a unique flat tree-gauge minimum and positive Hessian by the same elementary simply-connected flatness argument. A full actual kernel theorem, especially uniform as k grows with n and beta, is NOT inferred from the exact Hessian alone. The companion full-transfer limit theorem supplies that separate analytic obligation. The supplied full action and full physical boundary space differ from the22-face one-source model; its previous covariance, central single-mode spectrum and beta^-4 scaling cannot be carried over. Here each boundary has40 real chart coordinates; any prospective D00-normalized full-kernel dilation has the dimensional amplitude beta^-20, not beta^-4. The dimensional count is the input to the separately proved full marginal bound. No physical action selection, continuum spacetime, thermodynamic limit or finite-beta accuracy claim is made.

## Absolute normalized Haar metric factor

In the original five tree-chord variables, local boundary Haar is j0^5 dx, with eight Euclidean color coordinates for each chord. For z=M^(1/2)x, the linear Jacobian is J_M=(det M)^4 because the five-dimensional map is repeated for eight colors. Thus dx=J_M^-1 dz, and the leading Haar density in z coordinates is j0^5/J_M.

The boundary unitary is f(x) -> J_M^-1/2 f(M^-1/2 z). Equivalently, the original normalized two-boundary density satisfies g_x=J_M^2 g_z; the transformed integral kernel has one net inverse J_M from its two unitary factors and integration measure, leaving J_M g_z/j0^5. Therefore the absolute ground eigenvalue is

    lambda0_full(k)=(det M)^4 product_(j=1)^5
      [16sqrt(3)pi/(sqrt(sigma_plus,j)+sqrt(sigma_minus,j))^8].

This factor is fixed, positive and independent of k. The frozen exact orbital metric has det M=1/384, independently checked by rational determinant and inverse-cycle-Gram equality. Therefore the prefactor is384^-4. Neither independent fivefold Ad projection nor a residual gauge-volume factor belongs in this formula. Projection onto the single simultaneous-Ad invariant subspace retains the positive Gaussian ground, so it does not change the leading eigenvalue.

This absolute factor is not needed for the normalized semigroup beyond a uniform positive lower bound, but it fixes the actual Haar normalization if absolute amplitudes are stated. The calculation reads frozen orbital matrices and does not claim an independent second geometry enumeration.

## Canonical finite interface and five reporting scopes

The [exact geometry helper](../scripts/gauge_wilson_full_cube_transfer_geometry_check_2026_09_07.py) retains all28 original scientific checks and adds three separately prospective checks of detM=1/384, its eight-color Jacobian and the136/80/56/40 dimensions. TOTAL31 counts those named scientific checks; resource and strict-output guards are additional execution checks. All original matrices and scientific values match the frozen raw result. The helper reads the actual existing physical-parent source to bind its SHA; this is a declared runtime audit dependency, not a new source to publish in this package.

N5 per_element: exact12edge spatial cube and32edge full slab; no marked-face stripping.
N5 per_site: seven boundary tree edges leave five cycles; full17chords split5+5+7.
N5 per_mode: eight colors carry one global Ad action; generalized spatial frequencies are4×3 and6×2.
N5 per_block: exact temporal Schur, metric and dimension checks support the analytical nonlinear proof rather than replacing it.
N5 lattice_wide: finite supplied action, unspecified uniform constants/onset and no selected physical time, continuum spacetime or thermodynamic claim.

## Durable proof and review packet

The [block28 packet](../.claude/science/physics-loops/full-cube-transfer-20260907/PROOF_REVIEW.md) preserves the independent full geometry, uniform kernel proof, root derivation, actual matrices, metric checks, failed control history and source-bound reviews. It records the original28 checks and three prospective supplements without portraying finite algebra as numerical certification of analytic uniform constants. This is a retrospective evidence index; audit authority remains separate.
