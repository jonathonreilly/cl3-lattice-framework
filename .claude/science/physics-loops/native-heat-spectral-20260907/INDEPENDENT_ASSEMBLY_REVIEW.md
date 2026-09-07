# Independent adversarial review: full heat-side top coefficient

Review target was preregistered in REVIEW_PLAN.md before reading worker derivations. Reviewed orbital full-heat-second-order/DERIVATION.md and certificate.py, and primary DERIVATION.md (reported SHA7be320cf...). No floating spectral fit was used. The combined proof route is mathematically valid with the distinctions and domain details below retained. I found no missing uniformity step after checking the actual derivative-envelope argument.

## Reflected kernel and weighted remainder

The full-walk symbol gives exp(-ta/3)[1+t h²a²/36], hence correction(t h²/4)L². This is1/8 at time1/2 and1/4 at time1. The sixth-order cosine remainder, low cutoff a<=beta/2 and damping23t/72 are consistent. The low integrated bound scales as t^-3 and is maximal at1/2. Exact and Gaussian high-tail bounds include the outside-torus approximation and are decreasing on the stated beta interval. The live ten-check exact certificate passes.

Six exact Weyl images multiply the uniform full-walk error3h4 by six, including shifted near-wall endpoints; they do not require an unproved relative boundary estimate. The same-grid weighted Hilbert-Schmidt scaling is correct: entries of the heat remainder are at most18h6, so multiplying two square-summable weights gives18h4 times their two scaled ell² norms. The stated bound h²sum W<1 follows from the Gaussian and x³Gaussian Riemann-sum estimates. Thus the time-one sqrtW sandwich has a genuine uniform O(h4) HS/operator remainder. An unweighted operator estimate is not inferred.

## Exact eigenfunction regularity and quadrature

The crucial distinction is that u=sqrtW Sphi/sqrtmu is generally only normal^(3/2) at a smooth wall, so applying fourth-order Euler–Maclaurin directly to u would fail. The primary proof instead applies it to u²=W|psi|²/mu and to s1(x,y)W(y)psi(y), with psi=Sphi. These are smooth on the closed quadrant. Each wall contributes one zero from W, one from psi, and one from the reflected heat kernel (or two from psi for u²), giving at least cubic vanishing and zero first normal derivative.

The finite-reflection Gaussian formula gives bounded derivatives of every fixed order of psi, by Cauchy–Schwarz against the L² input phi. The bounds are uniform in the spatial endpoint. Kernel derivatives are uniformly bounded in both endpoints. Multiplication by W and its derivatives then supplies an integrable polynomial-Gaussian envelope for all derivatives through order4 in the quadrature variables. The constant for the kernel-applied-u integrand carries only the external sqrtW(x). No derivative of that fractional-regularity external factor is needed. The same smooth extensions handle the corner; no hidden corner contribution of orderh² survives.

The half-line Euler–Maclaurin bound with f(0)=f'(0)=0, decaying derivatives and f4 inL¹ is O(h4); the stated1/360 follows from the B4 remainder and |f'''(0)|<=||f4||1. The tensor argument uses Q1(Q2-I2)+(Q1-I1)I2, with Gaussian envelopes controlling the sampled first-coordinate error uniformly. Thus the infinite tails and the compact-region estimate are handled together, rather than exchanging an uncontrolled large-box limit with h→0.

This proves ||u_h||²=1+O(h4) and ||B_hu_h-mu u_h||ell²=O(h4). Two-sided Gaussian domination also proves qualitative HS convergence of the cell-embedded sampled continuum B_h to B. Its isolated simple top eigenvalue therefore has a uniform eventual gap. The normalized residual forces some eigenvalue withinO(h4) ofmu, and that gap identifies it as the top branch. No convergence rate for the embedded operator or a separate sampled-eigenvector derivative assumption is needed.

## Spectral assembly without a false operator expansion

Let C_h be the sampled kernel h²sqrtW(x)[L_x²s1(x,y)/4]sqrtW(y). Uniform bounded derivative kernels and two-sided Gaussian weights give qualitative HS convergence to C=(1/4)M_sqrtW L²e^L M_sqrtW. This, the O(h4) heat remainder, the O(h4) baseline quadrature eigenvalue error and the uniform top gap give
 lambda_top(sqrtW K_beta sqrtW)=mu+h²<u,Cu>+o(h²).
The nonzero spectrum of this carrier is exactly that of P_beta M_W P_beta. No square-root expansion of the actual Wilson multiplier is used.

The identity S sqrtW u=sqrtmu phi yields
 <u,Cu>=(mu/4)||Lphi||².
It is domain-safe: phi=mu^-1S(W Sphi) lies in DomL^n for every n since L^nS is bounded; L²e^L is itself bounded. Adding the exact scalar exp(3h²) contributes3mu, and the already proved native-versus-exact-saddle top comparison contributesd0. The resulting FULL TOP asymptotic is therefore
 lambda_top(A_beta)=mu+beta^-1[d0+3mu+(mu/4)||Lphi||²]+o(beta^-1).
Only a little-o remainder is justified at this stage, not O(beta^-2).

## Independent virial/domain check and sign

The dilation argument can avoid assuming phi lies in a dilation-generator domain. For (U_a f)(x)=a f(ax), the unitarily equivalent family is exp(a²L/2) M_W(x/a) exp(a²L/2). It is norm-differentiable near a=1: differentiated heat factors are bounded LS_a, and differentiated multipliers are bounded Gaussian polynomials. Its simple eigenvalue is constant. Differentiating its Rayleigh eigenvalue gives0=-2mu kappa+mu(2E_nu Q-3), hence E_nu Q=3/2+kappa, kappa=-<phi,Lphi>. All forms involving Lphi are legitimate by the smoothing observation above.

Substituting the variance identity for d0/mu and applying ||Lphi||²>=kappa² gives
 lambda2/mu=[Var_nu(Q)+kappa²-4kappa+15/4+||Lphi||²]/4
 >=(kappa-1)²/2+7/16 >=7/16.
This positive full coefficient is compatible with the negative d0 because they compare different objects. It does not determine an excited/ground ratio coefficient or any physical gap.

## Preserved failed formulation

The original step-cell embedding has range in RanPi_h, and for the smooth nonconstant Perron phi, ||(I-Pi_h)phi|| is orderh with coefficient determined by its nonzero gradient. Hence an embedded expansion T0+h²T2+o(h²) in operator norm is impossible for that embedding. The spectral/Nyström argument above never uses that false expansion. The full coefficient is an eigenvalue result obtained by a quasimode and isolated-gap argument, not a repaired claim about the entire embedded operator.

Verdict: the reviewed reflected-heat input closes the conditional premise in primary's top-eigenvalue assembly. Retain the full-Fourier source import, exact rho shift, two-sided weights, cubic-wall integrands, qualitative correction convergence, eventual simple gap and little-o scope explicitly in any source note. No numerical eigenvalue or eigenfunction is a proof input.
