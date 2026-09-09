---
claim_id: native_gapfree_generator_propagation
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
runner: scripts/native_gapfree_generator_propagation_2026_09_09.py
---
# Signed native generator closure and gap-free propagation

For the supplied infinite native model, the first signed-generator action on a common pole/Ward carrier closes after adding the local seven-star space and its reference-covariance partners. Its Gram requires the existing A,A′,B,B′,a0,c_minus data and the additional scalar mu=E sqrt(X). If an exact finite common isometry has certified leakage delta, its positive finite generator |A| approximates the actual one-particle semigroup with a gap-free Poisson error of order t delta log(1/(t delta)). Neither a leakage value nor a propagated native state is computed here.

The physical premises are the [finite-excitation Ward realization](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md), the [certified imaginary-time theorem](NATIVE_CERTIFIED_IMAGINARY_TIME_NOTE_2026-09-09.md), and the [local Green scalar definitions and enclosure methods](NATIVE_CERTIFIED_LOCAL_GREEN_SCALARS_NOTE_2026-09-09.md). Their supplied-model and common-reference-frame qualifications remain in force. No scalar acceptance is inferred from the existence of an oracle or an output filename. Full source derivations and independent research reviews are preserved in the paired provenance directory; their research execution descriptions are historical, not new results from this runner.

Use h=2|t_hop|>0, H0=iK, Gamma0=i sign(H0). Thus Gamma0=-K/|H0| and Gamma0 K=|H0|; the opposite sign is incorrect. Displayed local formulas below use h=1. The general propagation theorem allows arbitrary bounded self-adjoint operators on a common Hilbert space. The native application additionally requires actual Gram enclosures, an exact isometry and a certified leakage norm.

## 1. A finite algebraic action closure

For y_sigma(v)=-i(H0-i sigma s)^-1 v=-(K-sigma s)^-1v,

 K y_sigma(v)=sigma s y_sigma(v)-v.

For the actual Ward vector w_A, H0 w_A=i d_A, hence K w_A=d_A. Also K e0=d_all=sum of all three signed opposite-neighbor pairs. K commutes with Gamma0, so the same action identities hold for all reference-complex-structure partners.

A two-link flip changes K by
 DeltaK_A=2(e0 d_A^T-d_A e0^T).

Its action on any vector is determined by the two bare overlaps. Thus if F contains the common resolvent columns, e0,w_A,w_C and their Gamma0 partners, every K_A F column belongs to span(F,L,Gamma0 L), where L is the finite local seven-star space (one can reduce this to the actual d_A,d_C,d_all support span). No higher spectral moment is needed for the FIRST generator action and its norm Gram. This is an exact infinite-Hilbert-space identity, not an assertion that span(F) is invariant.

To compute F^T K_A F and (K_A F)^T(K_A F), it suffices to certify the common Gram enlarged by bare local star columns and Gamma0 partners, with the same phase and scale. All balancing coefficients sigma*s and sqrt(alpha) must be propagated; do not replace a weighted column by an unweighted source silently. Existing scales1/2 on the Ward insertions are exact.

## 2. Exactly one additional scalar for this first-action closure

The Ward-only stationary catalog A,A',B,B',a0,c_minus does not supply every bare-neighbor projected overlap. The missing scalar is mu=E sqrt(X), already the separate reference-energy integral in the campaign; it must be bound to its actual acceptance, not inferred from c_minus.

For local real star columns u,v use the literal seven-star I,O,T,N matrices of the parent. Put D=(1-s²A)/6. The bare-pole overlaps are

 <u,y_sigma(v)>=u^T[ sigma*s*(A I+(A-D)O)+D T ]v,
 <u,Gamma0 y_sigma(v)>=u^T[ B N-(mu-s²B)O/6-sigma*s*B T/6 ]v.

The mu O term canceled in stationary pole-pole divided differences but does NOT cancel in this single-resolvent boundary. Center rows have O=0, explaining why the previous center append did not need mu. The signs agree with the existing center Ward API.

Bare-bare Euclidean overlaps are literal local coordinates; local reference covariance is

 U^T Gamma0 U=-(mu/6)T.

For example K Gamma0=|H0| on the diagonal fixes this sign and coefficient: at center sum over six neighbors gives mu. Cubic symmetry makes the six contributions equal. Same-sublattice entries vanish and no star nearest-neighbor links other than center-neighbor occur.

Ward-bare Euclidean entries vanish for bare neighbors and equal1/3 for e0. The parent gives

 <w_A,Gamma0 e_j>=d_A^T[c_minus N-mu O/6]e_j.

Ward-Ward entries use only a0 and the exact O geometry, as already reviewed. Together these formulas certify the full enlarged action Gram using A,A',B,B',a0,c_minus,mu and literal geometry. No newly evaluated lattice moment beyond mu is required. General h follows by restoring the parent h factors and K-action coefficients; this note's displayed overlaps use h=1.

The closure is only first-action. Repeated powers introduce progressively more distant local sources; their covariance moments are not automatically contained in this seven-star catalog. Therefore this argument does not by itself supply the896 Krylov directions of the degree128 positive-band theorem.

## 3. Exact signed compression and leakage

Let V be an EXACT isometry onto a finite common real subspace built from the enlarged data, with Pi=VV^T. Set A=V^*H_A V (complex Hermitian) and R=(I-Pi)H_A V. Then

 R^*R=V^*H_A²V-A².

The two terms come from the first-action Gram above. Interval Gram conditioning, unknown exact nullspace, coordinate normalization and coefficient rounding must be certified before using this equality numerically. A midpoint or PSD-shifted factor is not automatically this exact V. The existing equivariant dilation theorem can provide an actual nearby V only with its stated factor error and common-source embedding; those errors must be propagated into A,R.

For the actual signed nearest-neighbor operator, ||H_A||<=6h by the degree-six Schur bound, including the flipped signs. No active gap is needed. A small leakage norm is a quantitative question, not a consequence of algebraic closure or small stationary-projector error.


## Poisson propagation theorem

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

## Supporting verification and remaining obligations

The paired runner performs small exact rational operator identities, signed-resolvent fixtures, PSD leakage identities and the displayed rational error comparisons. Wrong-sign alternatives are explicit synthetic algebra discriminations, not mutations of a native solver. It evaluates no native generator, matrix, leakage, integral or semigroup. The analytic Poisson proof, rather than those fixtures, establishes the operator theorem.

The stated sufficient leakage condition delta<=h/10^6 at t<=100/h yields a one-particle error below.001; it is not an achieved leakage certificate. At delta<=h/10^9, the stated398-particle conditional bound also requires an independently justified particle cap and truncation tail. Actual coordinate conditioning, positive-band identification, impurity scalar/vacuum and insertion errors remain separate. Repeated generator powers require additional source data, so higher Krylov closure is still open. Alpha and its sign are uncomputed.

The optional approximate stationary-complex-structure route satisfies ||(Gamma_A-Gammahat_A)K_A||<=6h eta when its operator error iseta. Gammahat_A K_A need not be Hermitian or positive; it supplies only approximate matrix elements until further structure is certified. This route supplies no alternate automatic semigroup certificate.
