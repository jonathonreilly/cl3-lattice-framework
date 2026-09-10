# A finite-moment certificate for the full Ward sum

Source-only extension of COMMON_CENTER_REWRITE d0d1 and the independently reviewed direct Q>160 bound. No native scalar, moment array, resolvent, or accepted numerical output was evaluated. This is a convergent certificate mechanism, not a completed sign certificate or a claim of practical degree.

## Common-center correlations, with exact boundaries

Put a_A=R_A Omega, b_A=R_A g Omega, z_A=R_A C R_A Omega, C=[H0,g]. All b,z,g a are odd vectors in the SAME original Fock representation. Taking the expectation of the common-center identity and pairing reversed ordered edges gives

 8 alpha = Re sum_(C disjoint A) <b_C-z_C, g a_A>.                 (1)

The sign follows from C*=-C: <Omega,R_C C R_C g R_A Omega>=-<z_C,g a_A>. The second correction is its reversed-edge conjugate. Equivalently z_A=b_A-g a_A+v_A, where v_A=R_A J_A R_A Omega, since [R_A,g]=R_A(C-J_A)R_A. Thus (1) is exactly Q-Re<x,T g v>, not a positivity replacement. The five orbit sums of the two real correlations in (1) are a finite exact target, but their values are not supplied by the diagonal moments of g Omega alone. Cauchy bounds retain the large inverse-gap factors. In particular the previously certified centerless estimate5525/h² still cannot be absorbed by Q>160/h².

## Explicit polynomial residual certificate

Let delta=h/4, j=2 sqrt2 h=||J_A||, and choose real polynomials p_A and q_A. Define

 uhat_A=p_A(D_A)Omega, xhat_A=-uhat_A,
 bhat_A=J_A uhat_A, vhat_A=q_A(D_A)bhat_A.

The actual v_A=D_A^-1 J_A D_A^-1 Omega has positive overall sign from the two negative inverses. Define the finite polynomial residual norms

 r_A=||(I-D_A p_A(D_A))Omega||,
 t_A=||(I-D_A q_A(D_A))J_A p_A(D_A)Omega||.

Then e_A=r_A/delta bounds ||x_A-xhat_A||, and

 f_A=(j e_A+t_A)/delta bounds ||v_A-vhat_A||.                    (2)

Proof: D_A^-1 is bounded by1/delta; insert and subtract D_A^-1 J_A uhat_A. No commutation of J_A with D_A is used. In particular replacing t_A by a scalar diagonal moment of Omega would be invalid.

Set E=(sum e_A²)^1/2, F=(sum f_A²)^1/2, X=sqrt15/delta, V=j sqrt15/delta². Compute the finite polynomial Ward number

 W_hat=<xhat,T xhat>-Re<xhat,T g vhat>.

Using ||T||=6 and the original vectors gives

 |8 alpha-W_hat| <=6 [ E(2X+E)+E V+(X+E)F ].                    (3)

Therefore W_hat greater than the right side proves alpha>0; its negative counterpart proves alpha<0. Alternatively Q>160/h² can be kept exact: an upper certificate for Re<x,T g v> below160/h² suffices. Equation(3) makes all approximation error explicit without a coordinate-width gate, Gaussian determinant branch, or impurity-vacuum substitution.

Every r_A² is a finite diagonal moment combination through degree2deg(p_A)+2. Every t_A² and W_hat is a finite ordered mixed moment of the actual D_A,J_A,g and Omega. Cubic covariance reduces repeated instances but does not remove signs or imply mixed moments positive. All must be evaluated or enclosed consistently with the native reference covariance; this document does not assert they follow just from EX and EX².

## Why this is an actual convergent native hierarchy

The reference one-particle energy is bounded by6h. A quadratic B_A maps the at-most-m-particle subspace into the at-most-(m+2)-particle subspace and has norm sqrt2 h. Consequently, for a vector psi supported in particle sectors at most m,

 ||D_A^n psi|| <= h^n product_(k=0)^(n-1) [6(m+2k)+sqrt2] ||psi||. (4)

This follows one factor at a time from the particle-sector restriction of H0 and the bounded perturbation; it does not claim D_A itself bounded. In particular Omega and J_A p_A(D_A)Omega are analytic vectors with a nonzero exponential spectral moment. J_A is a bounded linear Majorana field and increases the particle cutoff by at most1.

For any such source psi, polynomials are dense in L2(x² dmu_psi): the exponential moment makes a function orthogonal to all polynomials have an analytic Laplace transform vanishing near zero, hence vanishing Fourier transform and zero measure. Since x>=delta, 1/x belongs to this weighted L2 space. Thus polynomials p can make ||(I-D_A p(D_A))psi|| arbitrarily small. First choose p_A to make all e_A small; then for the resulting fixed analytic source bhat_A choose q_A to make t_A small. This proves E,F can tend to zero, so (3) converges to the actual full alpha.

The sequence need not stop if alpha=0, and the proof gives no affordable degree. Even when alpha is nonzero, finite stopping exists abstractly but may require many new half-moment/covariance suppliers. The elementary third moment bound alone has NOT closed the correction. The genuine remaining obligation is a signed mixed-moment enclosure meeting(3), not an unspecified replacement vacuum or an assumption of kernel positivity.
