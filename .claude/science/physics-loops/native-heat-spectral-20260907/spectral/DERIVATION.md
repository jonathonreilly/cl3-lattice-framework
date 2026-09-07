# Conditional heat-side coefficient and a closed quadrature lemma

The proposed coefficient is algebraically and domain-wise correct. The continuum-kernel quadrature introduces no h² top-eigenvalue correction: it has an O(h4) sampled-eigenvector residual. A full second-order expansion of the parent step-function embedded operator is nevertheless false because its cell-projection error is order h. These statements must remain distinct.

## Conditional coefficient and domains

Write h=beta^-1/2. The formal discrete heat symbol coefficient is L²/4 for the time-one heat and L²/8 for each half-time factor. Conditional on the necessary weighted reflected-heat remainder, this gives the candidate

    T2=S M_W2 S+(L²T0+T0L²)/8.

The heat factors make these bounded operators: L²S is bounded by spectral calculus; T0L² initially defined on DomL² has bounded extension S M_W(SL²), adjoint to L²T0. Moreover phi=mu^-1S(W Sphi) lies in DomL^n for every n because L^nS is bounded. Thus the Perron quadratic form is legitimate and

    <phi,T2phi>/mu
       =d0/mu+3+||Lphi||²/4.

The independently proved virial identity gives E_nuQ=3/2+kappa, kappa=-<phi,Lphi>, and d0/mu=[Var_nu(Q)+kappa²-4kappa-33/4]/4. Therefore

    <phi,T2phi>/mu
       =[Var_nu(Q)+kappa²-4kappa+15/4+||Lphi||²]/4
       >=[2(kappa-1)²+7/4]/4 >=7/16.

Cauchy–Schwarz supplies ||Lphi||²>=kappa². This bound concerns the conditional FULL coefficient; its positivity is compatible with the negative exact-versus-discrete-saddle coefficient d0. It is not a numerical value or a claim that the heat expansion was already proved by the earlier multiplier theorem.

## Why the original embedded operator expansion fails

Let Pi_h be cell-average projection onto the parent piecewise-constant embedding. Every embedded discrete operator has range in RanPi_h. For a nonconstant smooth Gaussian-decaying function v,

    ||(I-Pi_h)v||²/h² -> (1/12) integral(|dxv|²+|dyv|²).

This follows by cell Taylor expansion and the variance h²/12 of each coordinate; dominated summation is valid for such v. The Perron vector phi is smooth with Gaussian decay, since phi=mu^-1S(Wpsi), psi=Sphi is bounded and W has a Gaussian envelope. It is nonconstant and nonzero. Hence any Ahat_h with that cell range obeys

    ||Ahat_h-T0|| >= mu||(I-Pi_h)phi|| = Omega(h).

Consequently Ahat_h=T0+h²T2+o(h²) in operator norm cannot hold under this embedding. This is a failed formulation, not an obstruction to eigenvalue asymptotics. No embedding is silently changed below.

## Exact continuum sampled kernel and its Perron vector

Use B=M_sqrtW e^L M_sqrtW, with normalized Perron vector u=sqrtW psi/sqrtmu, psi=Sphi. Let k(x,y)=sqrtW(x)s_1^C(x,y)sqrtW(y). At right-endpoint nodes x_p=h(p+1), define the positive trace-class sampled matrix

    (B_h)_(p,q)=h² k(x_p,x_q),
    (u_h)_p=h u(x_p).

The kernel is positive definite, so B_h is positive; its finite trace follows from the heat diagonal bound and the summability of W. This is the sampled CONTINUUM kernel, not yet the discrete recurrence heat kernel.

The finite-reflection heat formula gives uniform bounds on every fixed-order spatial derivative of psi=Sphi: apply Cauchy–Schwarz to derivatives of each free Gaussian kernel, whose L² norms are uniform in the endpoint. It also gives smooth extension to the chamber walls and zero boundary values for psi and s_1^C(x,·). Thus

    k(x,y)u(y)
      =sqrtW(x)s_1^C(x,y)W(y)psi(y)/sqrtmu

is smooth as a function of y on the CLOSED quadrant despite sqrtW itself having fractional wall regularity. At either wall each of the three factors s_1^C, W and psi vanishes, so the product vanishes at least cubically. Its first normal derivative is zero. Every y derivative needed through order4 is bounded by sqrtW(x) times a fixed polynomial-Gaussian envelope in y, uniformly in x: heat-kernel derivatives and psi derivatives are uniformly bounded, while W and all its derivatives decay Gaussianly. No derivative of sqrtW(x) is needed for this estimate.

Similarly u(y)²=W(y)|psi(y)|²/mu is smooth, has cubic wall vanishing and derivative envelopes. Corners introduce no singularity; the underlying factors are smooth and all boundary conditions remain valid there.

## Euler–Maclaurin with a uniform residual

For a smooth half-line f with f(0)=f'(0)=0, vanishing derivatives at infinity and f^(4) integrable, right-endpoint Euler–Maclaurin gives

    |h sum_(n>=1)f(nh)-integral_0∞f|
      <=C h4 integral_0∞|f^(4)|.

One may take C=1/360 by bounding the B4 remainder and using |f'''(0)|<=integral|f4|. Only the order is needed. Apply this first in one coordinate and then the other. The error in the second application is sampled in the first coordinate, but its polynomial-Gaussian envelope has uniformly bounded Riemann sums for0<h<=1. The boundary zero/first-derivative conditions persist after integration in the other coordinate. Therefore

    |h² sum_q k(x,x_q)u(x_q)-mu u(x)|
       <=C h4 sqrtW(x),
    ||u_h||²=1+O(h4).

Since h²sum_p W(x_p) stays bounded, this gives the genuine quadrature-norm residual

    ||B_h u_h-mu u_h||_ell²=O(h4).

The cell-embedded sampled B_h converges to B in Hilbert-Schmidt norm by pointwise kernel convergence plus a two-sided polynomial-Gaussian domination. This is qualitative convergence, not a second-order embedded operator expansion. Its simple positive top eigenvalue is therefore eventually isolated near mu. The normalized residual identifies that branch and proves

    lambda_top(B_h)=mu+O(h4).

Thus the continuum-kernel sampling contributes NO h² top-eigenvalue term.

## Sufficient remaining heat input and assembly

Suppose the independently derived reflected discrete time-one kernel satisfies a uniform O(h4) remainder after

    beta K_beta(p,q)=s_1^C(x_p,x_q)
                     +(h²/4)L_x²s_1^C(x_p,x_q)+O(h4).

Two-sided sqrtW weights convert this uniform scalar remainder into an O(h4) Hilbert-Schmidt/operator remainder, because h²sum W is uniformly bounded. The sampled correction kernel C_h=h²sqrtW(x_p)[L_x²s_1^C(x_p,x_q)/4]sqrtW(x_q) converges qualitatively in HS norm to C=M_sqrtW L²e^L M_sqrtW/4, by the same dominated-kernel argument.

The simple-gap perturbation argument, the O(h4) baseline quadrature result and C_h→C then give the heat-only top correction <u,Cu>. Using u=sqrtW Sphi/sqrtmu and phi=mu^-1S(Wpsi),

    <u,Cu>=mu||Lphi||²/4.

Multiplication by the exact shifted-saddle factor e^(3h²) adds3mu. The previously proved native-versus-exact-discrete-saddle top difference adds d0. Under the displayed independently verified heat input, the native top eigenvalue therefore has

    lambda_top(A_beta)=mu
       +beta^-1[d0+3mu+mu||Lphi||²/4]+o(beta^-1).

The relative coefficient is at least7/16. No O(beta^-2) eigenvalue remainder follows from these qualitative correction/spectral convergence arguments. Until the independent reflected heat remainder is reviewed, this assembly remains conditional. It gives no individual excited branch, ground/excited ratio sign or physical mass-gap claim.
