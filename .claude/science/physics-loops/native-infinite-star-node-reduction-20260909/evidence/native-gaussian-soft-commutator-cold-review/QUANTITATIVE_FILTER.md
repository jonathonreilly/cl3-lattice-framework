# Quantitative filter and finite-box feasibility stretch

New analytic partial, not independently reviewed. No physical evaluation. Set h=1 for the numerical parameter examples; restore times by h^-1 and Gaussian parameter T by h^-2.

The convention f_T(x)=integral w_T(t) exp(itx)dt gives exactly

 w_T(t)=sign(t) erfc(|t|/(2sqrt(T)))/(2i).

Integration by parts in the sine transform verifies f_T=(1-exp(-Tx²))/x. In particular

 M_p=integral |t|^p |w_T(t)|dt
    =(2sqrt(T))^(p+1) Gamma((p+2)/2)/((p+1)sqrt(pi)),
 M_0=2sqrt(T)/sqrt(pi), M_1=T.

For a symmetric time truncation |t|<=R, the omitted zeroth moment is <=2sqrt(T)/sqrt(pi) exp(-R²/(4T)); the omitted first moment is <=2T exp(-R²/(4T)), using erfc(x)<=exp(-x²). The latter controls the soft commutator tail because the real-time insertion identity has norm <=j|t|. Thus this time truncation also controls the node functional, not only f_T in operator norm.

Using the conservative replacements j<=3/2, delta=1/6 and1/sqrt(2e)<=1, choose T=1024. The complete90-word inverse-approximation error is <=585630 exp(-256/9)<10^-6. This follows directly from epsilon0=6 exp(-256/9), epsilon1<=4278 exp(-256/9). There is no numerical node value in this estimate.

For example R=512 gives q=R²/(4T)=64. With M0<=64, M1=1024, tail0<=64 exp(-64), tail1<=2048 exp(-64), telescoping the three node products bounds the complete time-truncation error by (90/8)*598016 exp(-64). Both full and truncated F have norm <=M0 and commutator norm <=jM1, so no spectral-gap property is needed for the truncated F here. The bound is well below10^-6.

A rigorously elementary propagation estimate already exposes a cost problem. For a vector initially supported inside a box with padding r, compare full K and its open-box compression K_B. Their powers on that vector agree for n<r, and both norms are <=W. Hence

 ||(exp(tK)-exp(tK_B))v|| <=2 exp(W|t|)(eW|t|/r)^r ||v||.

If W|t|<=r/(4e), the right side is <=2 exp(-r)||v||. For the two-filter product, free propagation times up to2R occur; sufficient padding is r>=8eWR. With W=2sqrt3 h<4h and e<3, the displayed R=512/h gives sufficient r=49152 sites. Duhamel comparison of local quadratic cocycles adds only time/support polynomial factors to this exponential estimate. Soft derivatives introduce finitely many local J insertions and require those same comparisons, rather than a norm of the generalized plane wave. This is a convergence route, but this coarse radius is utterly impractical for a direct full box. It is not a lower bound on the radius actually needed or an obstruction to better Gaussian methods.

The covariance step must also be quantitative. One safe but impractical elementary bound is as follows. On m complex modes, let the two physical Gaussian covariance matrices differ entrywise by at most epsilon. Along their convex covariance interpolation every Pfaffian minor is a physical monomial expectation of modulus <=1. Differentiating a2n-Majorana Pfaffian therefore bounds its change by n(2n-1)epsilon. Expanding a norm-one observable in the orthonormal Majorana monomial basis and using Cauchy-Schwarz gives expectation error <=2^m m(2m-1)epsilon. Thus merely proving entrywise covariance convergence, with this generic conversion, is not a practical finite-box certificate. Gaussian-specific trace-distance/overlap estimates or a direct determinant response comparison are needed to avoid the exponential conversion. This observation is about a crude proof bound, not an actual divergence of Gaussian states.

Conclusion: Gaussian approximation and time truncation are explicitly controllable at a declared error. The currently elementary spatial/covariance estimates do not certify an attainable full finite-box computation. A kernel pilot should not interpret empirical finite-box convergence as satisfying these missing quantitative bounds.
