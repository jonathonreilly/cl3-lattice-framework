# Adversarial cold review of frozen C=29 refinement

Reviewed orbital REFINED_BOUND.md, refined_certificate.py and its JSON after the independent Wilson coefficient derivation and original remainder audit had already been frozen. No refinement constants were coauthored or fitted during this review. I find the stated refinement valid on its declared domain, conditional on the exact parent recurrence/Fourier identity.

## Global H/Q bound and scalar maxima

Independently expanding sparse bivariate polynomials confirms exactly
 Q³-27H²=(x-y)²(x+2y)²(2x+y)²/4.
For x,y>=0, H>=0, so H<=Q^(3/2)/(3sqrt3). This is a global positive-chamber estimate, not an Omega-only interpolation. Maximizing q^r exp(-q) at q=r gives:
 Wmax²<=(3/2)^3 exp(-3)/27=exp(-3)/8;
 (QW)max²<=(5/2)^5 exp(-5)/27;
 (Q²W)max²<=(7/2)^7 exp(-7)/27.
The three displayed positive exponential-series inequalities imply respectively W<1/12, QW<1/6 and Q²W<1/2. These are strict global bounds, including chamber walls by continuity. Consequently |W2|<=3W+(7/4)QW+(1/4)Q²W<2/3, with coefficients summing exactly to2/3. Neither a sign assumption on W2 nor an unproved cancellation is used.

## Denominator fraction and ratio

The denominator correction remains NEGATIVE: D=D0(1-1/beta)+rD. With D0>14 and |rD|<=2618/beta², its lower bound for beta>=2048 is
 D/D0>=1-1/2048-2618/(14*2048²)=4192069/4194304.
This exceeds999/1000 by244913/524288000, so the claimed.999 fraction is safely valid. The bound is monotone in beta. The exact ratio subtraction is rN+D0 W2/beta²-rD(W+W2/beta); division by the lower denominator gives the stated sufficient coefficient
 76675625/2685312=29-1198423/2685312<29.
There is no denominator-sign error or missing D0 factor in that expression. The numerator uses171/D0<=171/14, the direct correction uses |W2|<=2/3, and the denominator residual uses2618/D0 times(1/12+(2/3)/2048).

## Spot checks of low/tail inputs

The enlarged a<=beta/2 ellipsoid remains inside the Fourier torus, since each coordinate square<=4a/3. Sum of sinc argument squares<=3/4 keeps the product-comparison factors positive. The revised squared-sinc coefficient1/16+1/10+1/80+1/1600 is below1/5. The sharper cosine remainder1/810 and u<=a/72 give damping23/72; the two revised cubic coefficients follow directly from the same product expansion. Numerator half-integer moments retain the correct Fourier/radial prefactor; bounding sqrt3/(2sqrtpi)<1/2 and alpha^-1/2<2 indeed leaves the displayed rational expression. The denominator moment factor uses the exact Delta² angular identity and has the correct1/5 prefactor ceiling.

For the exact high tail, global beta psi>=a/24 is unchanged. The coefficients sqrt3/(2pi)<1/3 and sqrt3/(18pi)<1/30 are conservative; the latter is the exact Delta² radial density after division by24pi², not its integrated Gaussian constant. The resulting beta-polynomial exponents are at most5, so monotonicity beyond2048>5*48 is correct. Approximation-tail polynomials(9/2)a4+a5/18 and5a5+a6/18 follow from beta<=2a and include the outside-torus Gaussian tail. Their exponential split at1024/6 is safe. These checks found no missing region or normalization term. Primary independently audits the detailed low-moment/tail arithmetic.

## Quantifiers and certificate execution

The statement concerns v_beta=beta^-3/2 c_p(beta)/c0(beta), x_p=(p+rho)/sqrtbeta, real beta>=2048 and p in N0² satisfying the declared Omega window. It does not replace this shifted variable by p/sqrtbeta or mix beta^-1 with a beta^-1/2 coefficient. Fourier remainder estimates are endpoint-uniform; the new multiplier maxima are global positive-chamber bounds and therefore cover every required moving-grid endpoint. Denominator estimates depend only on beta. No quadrature grid or fitted onset is required.

Live execution of refined_certificate.py passed its22 exact rational/positive-series checks and reproduced the frozen JSON. I separately verified the H/Q polynomial identity and final rational arithmetic without importing that script; receipts are refined-live-certificate.json and refined-independent-arithmetic.json. The script certifies displayed scalar arithmetic, while the accompanying analytic arguments supply the Fourier/domain premises; neither is misrepresented as proving a full operator or spectral expansion.

Verdict: no mathematical error found in the frozen C=29,beta>=2048 multiplier refinement. This does not transfer the coefficient to normalized physical convolution, a complete packet-operator expansion, a spectral-gap correction, or a physical mass-gap statement. The September3 diagonal-similarity sector remains separately scoped and cannot be used to discard the additional radial Wilson terms.
