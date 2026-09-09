# Explicit node error for restricted-state cyclic compression

New analytic derivation; no physical action. Use the reviewed exact local-J node formula and the Gaussian inverse filter w_T. Assume exact cyclic space/projection and exact restricted covariance at first. All finite compressed CAR operators are embedded in the original algebra for comparison; the infinite vacuum expectation of them equals their finite mixed quasifree expectation.

Let E_m(L)=2exp(WL)(WL)^m/m!. It bounds the propagated-field error relative to the norm of ANY vector in the seven-seed span, uniformly for |time|<=L. For B=(i/2)gamma_v gamma(d), ||d||=beta, its interaction-picture generator differs by at most beta E_m(L). For J=(i/2)gamma(d), ||J||=j=beta/2, the propagated insertion error is at most j E_m(L). The central gamma error is E_m(L).

A product of interaction cocycles along a piecewise real-time contour of total length L has operator-norm error <=beta L E_m(L), by Duhamel and unitary telescoping. Absolute free propagation times on the contour are <=L. A term with one J and one central gamma has error <=j[beta L+2]E_m(L): the cocycle segments contribute beta L, and the two fields each contribute one. This bound is uniform in the J insertion time.

The overlap term plus BOTH soft correction terms therefore have total integrand error <=

 [beta L+j L(beta L+2)]E_m(L)
 =[2beta L+(beta²/2)L²]E_m(L), L=|s|+|t|.          (1)

The insertion integration lengths add to L. No commutator with a generalized q_m is evaluated; J is the supplied local insertion transported by the compressed free dynamics. This avoids an artificial compressed free-boundary contribution.

On |s|,|t|<=R, use E_m(2R). Integrating absolute filter weights gives the complete90-word compression error

 Ecomp <=(90/8) E_m(2R)
          [4beta M0M1+beta²(M0M2+M1²)].          (2)

Here M_p are full absolute filter moments, conservatively bounding their truncated versions. Scalar impurity phases and signed gauge transports are retained in the cocycles; compressing the state does not change the reference energy convention.

If the actual computed finite covariance differs from the exact restricted covariance by operator norm epsilon, the independently reviewed Gaussian response42f75/8c310172 gives in addition

 Ecov <=(90/8)epsilon
         [6beta M0M1+(3/2)beta²(M0M2+M1²)].      (3)

No pure-vacuum substitution, inverse-overlap chart bound, or exponential-in-dimension state conversion occurs. Arithmetic errors in the Gaussian kernels, cyclic frame, and compressed generator are not included in(2)-(3); they require their own certified budgets.

## A concrete sufficient, but not presently practical, parameter set

Set h=1, delta=1/6, beta<3, W=2sqrt3<4. Choose T=1024, R=384. The already reviewed inverse error is <=585630 exp(-256/9)<3*10^-7. The time-truncation bound is <=(90/8)*598016 exp(-36)<2*10^-9.

Take m=12288, so W*2R<3072 and

 E_m(2R)<=2 exp(3072)(3/4)^12288
         <=2 exp(-3072/7),

using e<3 and log(4/3)>=2/7. Thus compression error from(2) is negligible compared with10^-6. The exact rational coefficient upper bounds follow by using M0<=64, M1=1024, M2<=262144/3 and beta<=3. With Ccov denoting that rational coefficient in(3), taking epsilon<=10^-6/(4 Ccov) budgets at most2.5*10^-7 to covariance error. The saved exact arithmetic file records these constants. A remaining budget is available for frame and kernel arithmetic, but none is certified here.

The dimension bound is <=86016 real modes, about43008 complex modes (plus a harmless parity-padding mode if required). This replaces an enormous cubic spatial box, but dense covariance storage alone at binary64 is tens of gigabytes, outside384MiB; dense Gaussian evaluation is therefore NOT licensed by this sufficient parameter set. A substantially sharper polynomial approximation or structured moment/kernel representation is needed for affordable computation. This is a cost consequence of the proved sufficient bound, not a proof that smaller m fails or that the cyclic route is impossible.

The reference covariance moments contain Gamma_infinity and are not finite-walk moments alone. Ill-conditioned raw Krylov Gram matrices can invalidate a floating orthogonalization even when the abstract dimension estimate is true. Those two numerical obligations remain explicit.
