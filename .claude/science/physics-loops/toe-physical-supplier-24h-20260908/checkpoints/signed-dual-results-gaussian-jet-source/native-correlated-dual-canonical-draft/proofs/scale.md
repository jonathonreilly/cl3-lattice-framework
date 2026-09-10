# A fixed uniform dual-scaling family

Source-only extension of the reviewed reduced degree10 dual proof625f. The original primal trials, certified E,F, H>=delta, signed coupling C=-J and all domain assumptions remain fixed. No new contraction or actual numerical evaluation is performed.

Write U=B* x0 and W=2T x0-B v0. For any already chosen local polynomial duals y,z define D=Hy-C*z and V=Hz. The exact residual identity for the scaled duals lambda y,lambda z is

 W_actual-W0-lambda correction = Re<e,W-lambda D>+Re<f,-U-lambda V>+R(e,f).

Here correction=Re<r,y>+Re<s,z>. Scaling does not alter the sharp quadratic remainder L(E,F), because the primal errors e,f are unchanged. Consequently for every fixed real lambda,

 lower(lambda)=W0_lower+(lambda correction)_lower-E*A_lambda-F*B_lambda+L(E,F),
 upper(lambda)=W0_upper+(lambda correction)_upper+E*A_lambda+F*B_lambda+6E²+6EF,

where A_lambda and B_lambda are certified upper bounds on the direct-sum residual norms. Divide both endpoints by8 for alpha. All interval directions apply to the original intervals, not midpoint surrogates.

## Same sixteen contractions

For each channel the existing proposal is y=s(W-tJU), z=-tU. With the four-Gram ordered as (W,HW,JU,HJU) and the two-Gram as (U,HU), the uniformly scaled residual coefficient vectors are exactly

 a_lambda=(1,-lambda*s,-lambda*t,lambda*s*t),
 b_lambda=(-1,lambda*t).

The signed correction is lambda*(s*c0-s*t*c1-t*c2). Thus the existing13 upper-triangle Gram entries and3 signed contractions suffice for every lambda. There is no new Wick evaluation, source vector, covariance or supplier. There are only additional small interval quadratic forms and roots.

A separate multiplier is essential: substituting s'=lambda*s and t'=lambda*t into the original nested parameterization changes the last coefficient to lambda²*s*t and does not represent uniform dual scaling. Equivalently the general independent coefficients y=aW+bJU, z=cU must scale (a,b,c) together. The nested proposal selects (s,-st,-t); it does not constrain all legitimate duals to remain on that nonlinear surface after scaling.

## Fixed prospective schedule and retention

Use the literal ordered family (0,1/2,1,3/2,2), with the same lambda across channels while retaining their individual t_A,s_A. The proposal itself remains unchanged. Lambda0 gives the zero dual and lambda1 gives the reviewed sequential proposal, so this family includes both earlier candidates. Lambda>1 is allowed: the bound t<=4 or s<=4 just describes the unscaled Rayleigh-ratio proposal; it is not a validity restriction on arbitrary polynomial dual vectors.

For each scale evaluate all full original interval forms, sum squared norm upper bounds across channels, and use outward roots. Negative certified norm upper bounds or empty intersections signal inconsistent certificates and must not be clipped into success. A lower squared-norm endpoint may be intersected with zero only using the established true-norm nonnegativity premise. Finite arithmetic caps and retention of each scale's inputs/forms/roots/correction before its final gate remain required. Arithmetic resource refusal yields an explicitly unavailable candidate, never an invented interval.

Intersect all successfully certified alpha intervals with the already accepted spectral/posterior interval. Because all contain the same actual alpha, a nonempty intersection cannot be wider than that prior interval and cannot worsen its endpoints. This is a conditional correctness statement, not a guarantee that finite arithmetic succeeds or that the width strictly improves. An empty intersection is a hard discrepancy; do not silently select whichever sign is preferred. Keep the prior interval as a separately identified accepted result even if the new study refuses. Do not use the zero-dual necessary screen to skip lambda>0: the signed correction may make those candidates useful.

## Added work

Per channel and scale, evaluate10 upper-triangle terms for the four-form and3 for the two-form, plus the three already saved signed terms. At15 channels, five scales and two primal modes this is at most1950 Gram-entry terms and450 signed-entry terms, plus at most20 global outward roots. Existing sequential proposal divisions are not repeated. These are operation counts excluding rational bit growth, interval endpoint operations and durable output overhead; they are not a measured runtime forecast. The5130 Wick-word acquisition bound is unchanged. The five-scale schedule and any updated runtime cap must be frozen and independently reviewed before actual data evaluation.
