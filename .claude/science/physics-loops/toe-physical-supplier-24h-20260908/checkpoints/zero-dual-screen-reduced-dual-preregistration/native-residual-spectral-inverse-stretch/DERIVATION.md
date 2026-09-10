# State-specific residual inverse norms from three spectral moments

Source-only, unreviewed. No native moments, scalar values, residuals or histories were read. The named target is ||D^-1 r||, for a specified residual vector r in a supplied wrong-flux channel D>=delta>0. No active bulk gap is assumed.

## Exact quadratic majorant

For tau>delta define

 A=(tau+2delta)/(delta² tau³),
 Q_tau(lambda)=(3tau-2lambda)/tau³+A(lambda-tau)².

The proposed formula is correct. Exact polynomial division gives

 Q_tau(lambda)-lambda^-2
 = (lambda-delta)(lambda-tau)²[(tau+2delta)lambda+delta tau]
   /(delta² tau³ lambda²).                                      (1)

Every factor has the required sign for lambda>=delta. Q interpolates lambda^-2 at delta and is tangent at tau. Thus Q>=lambda^-2>=0 throughout the full half-line, not just on a bounded spectral window.

If r belongs to Dom(D), put rho_j=<r,D^j r> for j=0,1,2, interpreting rho2=||Dr||². Spectral calculus gives

 ||D^-1 r||² <= U_tau(r)
 = A rho2 + B rho1 + C rho0,                                    (2)
 B=-2/tau³-2tau A,   C=3/tau²+tau² A.

This requires only the finite quadratic-form moment of D², not a bounded D or a bound on its largest eigenvalue. The exact form is nonnegative. B is negative: an interval implementation must charge the LOWER rho1 endpoint in an upper bound, or evaluate the complete signed expression outward. Substituting upper endpoints in all three terms would be invalid. A negative certified upper bound is a contradiction to be refused, not an inverse norm to square-root.

A deterministic proposed family is tau in{1,2,4,8,16} at delta=1/4. For any valid upper enclosures U_tau^U, also retain the old rho0^U/delta² and take their minimum. This cannot weaken the old certified bound. It does not promise strict improvement: Q grows quadratically at high energy. For a spectral vector supported exactly at delta and tau, (1) vanishes and the majorant is exact. For a vector concentrated at tau the inverse-square factor is1/tau², compared with the old1/delta²=16. These are explanatory spectral examples, not native outcomes.

## First residual for degree-one p

Let p(D)=p0+p1 D with fixed real rational coefficients and

 r=(I-Dp(D))Omega=Omega-p0 D Omega-p1 D²Omega.

Writing c=(1,-p0,-p1),
 rho_j=sum_(i,k=0)^2 c_i c_k m_(i+k+j),   j=0,1,2,              (3)
 m_n=<Omega,D^n Omega>.

Only m0..m6 are needed. The reviewed degree-(2,0) source represents D^nOmega for n<=3 by O0..O3 on a,d,Ka,Kd,K²a,K²d. Hence (3) uses exactly its c=mu/3,nu,omega5 scalar closure. Its local-polynomial domain argument supplies r in Dom(D). This imports the algebraic closure, not any accepted numerical omega5 or moment.

The error of the first trial is exactly
 ||D^-1Omega-p(D)Omega||=||D^-1 r||.

Call its new upper bound u_A (a norm, not a squared norm) after taking an outward root of the minimum of (2) and the old bound. Keeping norm/squared-norm notation separate avoids an extra factor delta.

## Inner constant-q residual

Let b=J p(D)Omega and t=(I-qD)b, with q real scalar. Define s_j=<b,D^j b>, j=0..4. Then

 xi_j=<t,D^j t>=s_j-2q s_(j+1)+q² s_(j+2),   j=0,1,2.          (4)

Applying (2) to xi gives a bound v_A>=||D^-1t||. The reviewed degree-(1,1) source supplies b,Db,D²b on the SAME six vectors, with at most cubic Clifford words and Wick words of length6. Thus s0..s4 again require only c,nu,omega5. The highest needed inner moment is s4, not s6. No new spatial covariance or seventh absolute moment follows at this degree from this construction.

## Return to the full Ward error, with the remaining operator estimate explicit

For x=D^-1Omega and xhat=p(D)Omega, let v=D^-1 J x and vhat=q J p(D)Omega (overall sign conventions do not affect these norms). The exact decomposition is

 v-vhat=D^-1 J(x-xhat)+D^-1(I-qD)b.

Consequently, with ||J||=j=2sqrt2 h,

 ||v-vhat|| <= (j/delta) u_A + v_A.                            (5)

The first term still uses the supplied operator bound ||D^-1||<=1/delta. It is NOT being treated as another known local spectral residual, since x-xhat contains the exact inverse. Closing a sharper state-specific estimate for that term would require additional information. There is no hidden replacement of a vacuum vector by a full resolvent operator.

For all15 channels set
 E_new²=sum_A u_A²,
 F_new²=sum_A[(j/delta)u_A+v_A]².

The same full-boundary Ward error theorem, or the reviewed posterior norm version, accepts these improved E,F with the original signed nominal. At h=1 the multiplicities are12P+3O. The degree-one all-q exclusion under the older residual-to-gap estimator does not apply to this NEW estimator. This observation supplies no sign or convergence claim.

A prospective implementation must freeze the five tau values, signed interval evaluation, moment provenance, coefficient identities, comparison with the old bound, cap/failure handling and full residual-error propagation. It must certify actual m0..m6 and s0..s4 from the scalar supplier; it cannot infer them merely from the205 degree10 events, which do not contain all those moments. No implementation or scientific evaluation is authorized by this source note.
