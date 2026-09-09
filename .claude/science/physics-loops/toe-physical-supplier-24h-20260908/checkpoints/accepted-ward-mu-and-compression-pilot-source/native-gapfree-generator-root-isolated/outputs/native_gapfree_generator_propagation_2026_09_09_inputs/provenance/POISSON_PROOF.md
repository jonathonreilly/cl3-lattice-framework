# Logarithmic gap-free propagation control from a Poisson integral

Source-only theorem, root authored. No native leakage, matrix, propagator or scalar calculation. This strengthens the reviewed first-action generator closure b3bcb bound while retaining every exact-isometry and physical excitation premise.

Let H,L be bounded self-adjoint operators on the SAME Hilbert space and delta=||H-L||. For t>0, scalar contour integration at the pole it gives

 e^(-t|x|)=(t/pi) integral_R cos(sx)/(t^2+s^2) ds.

For x>0 close the contour for exp(isx) in the upper half plane; the residue at it is exp(-tx)/(2it). The large semicircle vanishes. At x=0 integrate the elementary Cauchy density; x<0 follows by evenness. The integrable weight and bounded functional calculus then give the same identity in operator norm for H and L. This does not require a spectral gap, positivity of H, or an operator-Lipschitz theorem for absolute value.

Unitary Duhamel gives ||exp(isH)-exp(isL)||<=|s|delta. Averaging positive and negative s gives ||cos(sH)-cos(sL)||<=min(2,|s|delta). Split the Poisson integral at S>0. Therefore

 ||e^(-t|H|)-e^(-t|L|)|| <= (t delta/pi) log(1+(S/t)^2) + (4/pi) arctan(t/S).

For delta>0 choose S=2/delta, z=t delta. Using arctan(z/2)<=z/2 gives

 E(z) <= (z/pi)[log(1+4/z^2)+2].

Also E<=2 trivially. For delta=0 the operators coincide and the error is0; t=0 likewise. This is a modulus of continuity O(z log(1/z)), not a false dimension-independent Lipschitz assertion for |H|. No differentiation of spectral projectors occurs.

## Rational certificate without transcendental evaluation

Choose S=2^m t with integer m>=0. On [0,t], integral s/(t^2+s^2) ds=log2/2. On [t,S], it is <=m log2; above S, integral 1/(t^2+s^2) ds<=1/S. With log2<7/10 and pi>3 the error is bounded by

 B_m(z)=z*(7/30+7m/15)+4/(3*2^m).

Both constants admit elementary proofs: the positive exponential series at7/10 already exceeds2 through its fourth term, so log2<7/10; an inscribed regular hexagon gives pi>3. B_m is a rational upper bound for any chosen m; it need not be optimized from data. This makes a future bound check exact rational arithmetic with a predeclared m.

At t<=100/h and delta<=h/10^6 take m=15,z<=1/10000. Then B15<765/10^6<1/1000. The previous square-root estimate required delta<=h/120000000000 for the same one-particle target. This is a relaxation of a sufficient CONDITION by over100000, not an achieved native leakage or time kernel.

For the more stringent z<=1/10^7, m=25 gives B25<123/10^8. On an at-most398-particle sector,398*B25<1/1000. Thus t<=100/h, delta<=h/10^9 is a sufficient propagation-only condition at that particle cap. This numerical example does not prove the actual state has that cap; initial-state and particle truncation tails must already be independently established. No claim about a399-mode frame's physical occupancy is inferred.

## Actual compressed frame

For exact isometry V, Pi=VV*, L=Pi H Pi+(I-Pi)H(I-Pi), A=V*HV and R=(I-Pi)HV, the off-diagonal two-block matrix gives ||H-L||=||R||=delta. The block diagonal functional calculus gives e^(-t|L|)V=V e^(-t|A|). Hence the same Poisson error bounds

 ||e^(-t|H|)V - V e^(-t|A|)||.

Apply this to the native H_A only after certifying the actual common coordinates and first-action leakage Gram. A numerical midpoint frame is not the exact V premise. The previous first-generator closure supplies the necessary local inputs including mu but not their conditioning or attained leakage. Positive-band excitation identification, impurity vacuum, scalar energy, insertion vectors and initial pairing errors remain separate. A positive contraction e^(-t|A|) does not turn arbitrary real frame vectors into actual excitation modes.

On a specified n-particle exterior sector, telescoping contraction tensor powers multiplies the one-particle bound by at most n; restriction to antisymmetry has norm1. On a direct sum of sectors up to n take the maximum. For pairing matrices, the Hilbert-Schmidt propagation discrepancy is at most2 E ||Z||_HS, plus independent initial/source errors. Ground-state energy factors and normalized determinant conditioning remain outside this estimate.

This removes an unnecessarily severe square-root leakage requirement using the same actual first-action data. It leaves an empirical/mathematical task to certify delta and all state-identification premises. Alpha remains uncomputed.
