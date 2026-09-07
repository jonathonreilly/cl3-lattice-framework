---
claim_id: gauge_wilson_cube_slab_exact_covariance_central_gaussian_spectrum_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Exact rational covariance and central Gaussian spectrum of the supplied stripped cube slab, identified with its fixed-branch rescaled limit through the nonlinear saddle parent; no physical coupling or thermodynamic limit."
upstream_dependencies:
  - gauge_wilson_cube_slab_nonlinear_saddle_dilated_kernel_bounded_theorem_note_2026-09-07
runner: scripts/gauge_wilson_cube_slab_exact_covariance_central_gaussian_spectrum_2026_09_07.py
---

**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; independent audit owns any verdict.

~~~yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
source_of_blocker_text: frontier_question
artifact_role: theorem
target_claim_type: bounded_theorem
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## Actual rescaled spectral conclusion

For the unchanged supplied finite bare-Haar cube operator A_beta=D_beta/D00, the [nonlinear saddle and dilated-kernel theorem](GAUGE_WILSON_CUBE_SLAB_NONLINEAR_SADDLE_DILATED_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-07.md) proves the Hilbert–Schmidt limit structurally for H and Sigma. This source computes those constants and diagonalizes the resulting central kernel. There is no circular dependency: the parent does not require the numerical covariance or spectrum derived here.

Writing ell0 and ell1 for the largest two eigenvalues of A_beta, the imported convergence and the exact simple Gaussian branches give

    beta^-4 ell0 -> sqrt3*pi [11/(6(32+3sqrt55))]^4,
    ell1/ell0 -> [(32-3sqrt55)/23]^2.

More generally every fixed nonzero Gaussian eigenbranch converges with its stated multiplicity. No uniform high-representation expansion, finite-beta onset, or physical mass-gap identification follows.

# Exact quadratic geometry and central Gaussian of the stripped cube slab

This calculation keeps the supplied32-link,16-vertex open four-cube and22weighted faces. The two xy faces at z=0, time0 and1 are omitted. Spatial weights are1/2 and temporal weights1. It does not replace the actual Wilson action by a commuting model. The rational calculation identifies its leading quadratic form; the declared nonlinear saddle parent supplies the analytical identification of an actual rescaled SU3 operator limit.

## Rational geometry

The frozen BFS tree has15edges, leaving17chords. Every positively oriented face contributes its four signed edge incidences. The22-by17 matrix B, diagonal weights W and two omitted-face rows S are retained in result.json with the graph and both gauge trees. Set H=B^T W B. Exact elimination gives

    det H=55/2,
    C=S H^-1 S^T=(1/11)[[64,46],[46,64]],
    C^-1=[[16/45,-23/90],[-23/90,16/45]].

An independent source-coordinate change stacks S with15coordinate rows. Its nuisance determinant is450, and its Schur complement is C^-1. Thus450 det(C^-1)=55/2. The second complete BFS tree gives the identical source covariance. All leading principal minors of H are positive; the topology also proves positivity through the complete-face flatness argument after the missing cap faces are restored by their disk identities.

Restoring both omitted face weights gives C_full=[[77,23],[23,77]]/60, strictly smaller. Incorrectly replacing all spatial halfweights by1 gives [[16,9],[9,16]]/5. Removing temporal weights leaves rank10 rather than17. Reversing one source orientation changes only the covariance cross sign. Full face incidence annihilates every vertex-gradient cochain. These controls distinguish the actual fixture from a full-action or diagonal-source substitute.

The first attempt at the second-tree control used a one-shot reversed iterator in the BFS neighbor loop, leaving an incomplete tree. Its inverse failed before any result was emitted. The original code and traceback are preserved. Materializing the axis order and asserting15tree edges fixes that implementation control; the primary graph, weights and scientific choices are unchanged.

## Eight-color leading covariance

Use Hermitian traceless generators with Tr(T_a T_b)=delta_ab, and U_e=exp(i beta^-1/2 sum_a z_ea T_a). The action deficit has leading beta E=(1/6)sum_a z_a^T H z_a. Thus each of the eight color vectors has covariance3H^-1, and the two TREE-FRAME source logarithms have

    Sigma=3C=(1/11)[[192,138],[138,192]],
    det Sigma=1620/11, correlation=23/32.

The aligned matrix coordinates are gauge-fixed quantities. Their cross-covariance is not a gauge-invariant observable for independently conjugated source holonomies. The central source space requires angular projection, as below.

Write X,Y in the eight-dimensional Euclidean Lie algebra. The normalized joint Gaussian Lebesgue density is

    g(X,Y)=(2pi)^-8(11/1620)^4
       exp[-a(TrX²+TrY²)+b Tr(XY)],
    a=8/135, b=23/270.

The inverse covariance has diagonal2a and offdiagonal−b. This is a correlated positive Gaussian, not the diagonal coefficient packet used in the separate one-link model.

## Actual normalized Haar constant

Let normalized Haar nearI be j(X)dX in the trace-orthonormal coordinates. Its leading constant is

    j0=1/(16sqrt3 pi5).

Here is an independent normalization derivation. The normalized SU3 Weyl formula on eigenangles theta1,theta2,theta3=−theta1−theta2 has factor1/[6(2pi)²]. NearI its Weyl determinant is Delta(theta)², with Delta=(theta1−theta2)(2theta1+theta2)(theta1+2theta2). A small supported Gaussian exp[−TrX²/2] in scaled coordinates gives the local eigenangle integral

    integral_R2 Delta² exp[−(theta1²+theta1 theta2+theta2²)] dtheta1 dtheta2
       =24pi/sqrt3.

Indeed theta1=u−theta2/2 diagonalizes the exponent. Delta=2u³−(9/2)u theta2²; independent Gaussian moments with variances1/2 and2/3 give the squared-polynomial mean12, and the Gaussian mass is2pi/sqrt3. Comparing the Weyl result divided by6(2pi)² with the full eight-dimensional Gaussian integral(2pi)^4 yields j0 above. A cutoff in a sufficiently small identity chart and dominated convergence justify using only this local Weyl expansion. No fitted group-volume constant enters. The real dimension8 gives Haar scaling beta^-4 for EACH source group.

## Correct dilation and central projection

For the source operator A_beta=D_beta/D00, the local unitary from group functions to Lie-algebra functions is

    (U_beta f)(X)=beta^-2 sqrt[j(X/sqrtbeta)] f(exp(iX/sqrtbeta)).

It is an isometry only on the fixed group chart, extended byzero into the expanding Lie-algebra ball. If the actual normalized two-source density has the proved scaled Gaussian limit, the transformed kernel of beta^-4 A_beta tends to g/j0. One power beta^-4 arises from the one-source Hilbert-space integration measure; the joint density itself scales beta8. Neither beta^-8 A_beta nor an unscaled operator limit is the correct normalization.

On central functions the limiting kernel is

    K(X,Y)=j0^-1 integral_SU3 g(X,Ad_h Y) dh,

equivalently the independent double Ad average. The Gaussian commutes with simultaneous orthogonal transformations, so its operator commutes with the Ad projection. This is its restriction to invariant functions, extended byzero on the noninvariant complement. The integral cannot be omitted when displaying a kernel intended to be individually conjugation invariant.

## Exact spectrum of this Gaussian operator

Put omega=sqrt(4a²−b²)=sqrt55/90 and

    theta=b/(2a+omega)=(32−3sqrt55)/23.

The eight-dimensional Hermite generating transform diagonalizes the unaveraged Gaussian. Its degreeN eigenvalue is lambda0 theta^N, with ground eigenfunction exp(−omega TrX²/2), and

    lambda0=[(2pi)^-8(det Sigma)^-4/j0] [pi/(a+omega/2)]^4
           =sqrt3 pi [11/(6(32+3sqrt55))]^4.

The invariant polynomials on traceless Hermitian3-by3 matrices are the symmetric eigenvalue polynomials with trace0, freely generated by TrX² and TrX³. Averaging the complete Hermite decomposition commutes with the Gaussian and preserves its degree filtration; the invariant degree multiplicities are therefore the coefficients of1/[(1−z²)(1−z³)]. Polynomial density in Gaussian L2 and compact-group averaging give completeness on the invariant subspace. The spectrum there is

    lambda0 theta^(2a+3b), a,b>=0,

with multiplicity equal to the number of pairs at each degree. In particular the ground and first excited branch are simple, and their ratio is theta². This differs from the earlier central-character ONE-LINK Gaussian ratio. No physical mass gap is inferred by changing models.

The radial Weyl transform gives the same count: multiplication by the cubic Vandermonde sends invariant radial functions to antisymmetric functions on the two-dimensional Cartan plane. Their polynomial degrees are3+2a+3b. The two-dimensional oscillator contributes ground exponent1, so the first antisymmetric exponent is4, matching the eight-dimensional oscillator's ground exponent8/2. The odd-extension isometry uses1/sqrt6; its chamber kernel sums six signed images without another1/6 multiplier. There is no extra Weyl factor6 in the eigenvalues.

A proposed simplification of the absolute ground coefficient was rejected by the symbolic check: omega²/(2a+omega) is NOT2a−omega, whose product identity uses b² instead of omega². The original failed candidate/check are retained. The corrected coefficient above passes direct Gaussian integration; theta and the ratio were unaffected.

## Scope and current evidence

The covariance certificate has17actual checks and retains all rational matrices. The separate normalization certificate has8checks, including exact Haar and absolute Gaussian factors. Both are finite exact calculations, not by themselves a proof that the non-Abelian Wilson kernel converges. The declared independently reviewed nonlinear fiber-integration parent supplies that analytical step. No growing-highestweight expansion, thermodynamic limit, dressed sourceembedding, physical beta or formation mechanism is supplied here.

# Finite-beta sanity check for the leading absolute norm

For every finite beta, A_beta=D_beta/D00 is a bounded positive operator and the normalized vacuum character has norm1. Its exact Rayleigh quotient is1, so ||A_beta||>=1. The separately derived leading asymptotic norm is L_beta=beta4lambda0. At mathematical beta6,

    L_6=sqrt3*pi [11/(32+3sqrt55)]4
       < (11/2)(55/271)4
       =100656875/10787160962 <1/100.

The first bound uses pi<22/7, sqrt3<7/4 and sqrt55>37/5. Therefore the relative error against the actual norm is

    | ||A_6||-L_6 | / ||A_6|| = 1-L_6/||A_6|| >99/100,

and ||A_6||>100 L_6. This excludes a small-relative-error use of the leading TOP-NORM formula at6. It does not refute the beta→infinity theorem, does not quantify error of the first/top eigenvalue ratio, and does not select6 as a physical coupling. No actual spectrum was numerically fitted.

## Exact artifacts and limits

The [primary exact runner](../scripts/gauge_wilson_cube_slab_exact_covariance_central_gaussian_spectrum_2026_09_07.py) preserves the17 rational geometry checks and8 Gaussian/Haar checks, and adds3 separately preregistered beta6 sanity inequalities, for28 actual assertions. It emits all matrices, determinants and exact constants with `--json`, under180 seconds/180MiB with no external runtime file inputs. The [independent adapted-tree helper](../scripts/gauge_wilson_cube_slab_adapted_tree_saddle_check_2026_09_07.py) constructs a different gauge tree with source loops as exact chords. Analytic compactness, fiber bounds and central projection are proved in the parent; no finite checker replaces them. Original iterator and prefactor failures, preregistrations and independent reviews are preserved in the evidence packet.
