# Reference inverse-square-root moment from the accepted catalog

Units h=1. X=6−2Σcosθ on the normalized folded3-torus,0≤X≤12. Define c_minus=E X^(-1/2). Tonelli gives c_minus=(2/pi)∫_0^∞ A(t)dt, A(t)=E(X+t²)^(-1). The isolated zero of X has integrable inverse square root in3D. This is a new integral using saved scalar certificates, not a claim that earlier B contraction already evaluated it. For general h, c_minus(h)=c_minus(1)/|h|.

For z=u+iv with u>0, the exact identity
 |x+z²|²−(u²/|z|²)(x+|z|²)²=(v²/|z|²)(x−|z|²)²≥0
implies |A(z)|≤sec(arg z) A(|z|). On the Bernstein ellipse rho=5/2 over[a,2a], center c=3a/2, semiaxes29a/40,21a/40. The maximal squared tangent is (21/40)²/((3/2)²−(29/40)²)=441/2759, so sec²=3200/2759<(27/25)². Together with the reviewed A(0)≤17/60, this gives |A(z)|<153/500<1/3. Also |z|Re z≥(31a/40)², giving |A(z)|≤1600/(961a²)<4/c². Thus the same panel envelope M=min(1/3,4/c²) used in the reviewed uniform transform applies directly to A, without differentiating A or invoking a B integrand.

The fixed accepted geometry has26-point Gauss-Legendre nodes on67 dyadic panels j=-64..2, a=2^j, and160-bit root/weight intervals. The standard analytic Gauss bound used by the pinned parent is (20/3)a M rho^(-52) per panel. The full dyadic sum Σ a min(1/3,16/(9a²))≤20/9: for a≤2, sum a≤4 and contribution≤4/3; for a≥4 the reciprocal sum≤1/2 and contribution≤8/9. Therefore total quadrature error≤(400/27)(4/25)^26. Monotonicity A'(t)≤0 encloses each actual root value between saved upper-endpoint lower A and lower-endpoint upper A. Positive weight intervals already include a/2; no second mapping factor is applied.

The omitted low interval[0,2^-64] contributes between0 and2^-64/3. For t≥8 the exact finite geometric identity gives
 A(t)=Σ_(n=0)^25 (-1)^n E[X^n]/t^(2n+2) + E[X^26/(t^52(t²+X))].
The integrated remainder lies in[0,12^26/(53*8^53)]. Moments are exact integer multinomial sums Σ_(a+b+c=n) n!/(a!b!c!) binom(2a,a)binom(2b,b)binom(2c,c), since each independent2−2cosθ has central-binomial moments. Interval operations outward-round to192 bits; Machin32/10 supplies the multiplier2/pi. No cancellation in a machine floating sum is assumed.

One fixed target width2e-19 is prospective. Whether accepted endpoint and weight uncertainty achieves it is determined by the once-only worker, retaining the complete interval even if INDETERMINATE. No numerical c_minus, accuracy success, projector, Ward value or new physical conclusion is asserted by this source preparation.
