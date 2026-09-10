# Completing the weighted projector arithmetic budget

Prospective sufficient construction for the fixed66-node sign quadrature, h=1. No physical matrix or scalar is evaluated. This closes explicit *targets*, not their achievement. The error below compares the represented unrounded finite-rank Q with the exact quadrature Q. It is not a claim that a subsequently rounded pure projector is within the same error of the true impurity projector.

## Scalar balancing removes the matrix-square-root obligation

At node j write alpha_j=35 w_j/(2pi), X_j=[R(is_j)U,R(−is_j)U], and

 Y_j=sqrt(alpha_j) X_j,
 J_j=[[0,T_j/35],[T_j*/35,0]].

Then Q=sum Y_j J_j Y_j* exactly and ||J_j||<=1. This is scalar balancing, not the spectral absolute-value factorization of C. It has precisely the same bounds used by the reviewed B ledger: Tr M<318 after reference-covariance closure, and maximum alpha_j<12. No A-dependent matrix square root or inverse Gram is needed. Covariance closure embeds J with zeros in the extra block and preserves these facts. The signed coefficient is retained, not replaced by an arbitrary contraction.

## Fixed geometry and scalar gates

The exact POLES brackets must verify s in[1/128,16], distinct positive-pole separations >=2^-11, w in[2^-11,2], sum exact weights <16, and midpoint pole/weight errors <=2^-140. The first four bounds hold for the existing rational geometry ledger; the last two are to be checked against its exact brackets. Pi must be enclosed with midpoint error <=2^-140. If a gate fails, refine geometry under a new predata source version or report an unmet target; do not silently use the constants below.

For A and A′ require midpoint error <=eta_A=10^-30 at the chosen pole midpoints. Root-bracket widening must either be included in this eta or separately charged by the physical displacement estimate below. The planned accepted oracle full width1e-30 has spare factor two for its tiny bracket widening, but the actual widened intervals must be checked. Require B and B′ midpoint radii <=10^-19 as in the reviewed sufficient B ledger. Coefficient arithmetic is separate.

## A-dependent raw Gram entries

The actual seven-source formula is C_sigma(s)=sigma*s*(A N−D O)+D T, D=(1−s²A)/6. Signed two-neighbor seeds multiply entry bounds by at most4. With A,A′ errors <=eta_A, the coefficient and derivative error multipliers are bounded by

 g(s)=4[s+(s+1)s²/6],
 g1(s)=4[(1+s)+(s²+(s+1)(2s+s²))/6].

Nonconfluent Gram entries have error <=[g(s)+g(t)]eta_A/|sigma*s+tau*t|; confluent entries have error <=g1(s)eta_A. On the frozen geometry both are <2^24 eta_A. The264-row raw Gram therefore has operator error <2^33 eta_A; scalar balancing and covariance closure give epsilon_A<2^37 eta_A.

Apply the reviewed conditioning-free factor comparison separately to this error: after symmetry twirl and PSD shift, trace operator discrepancy <=2sqrt(318*1056 epsilon_A)+1056 epsilon_A <10^-6. This uses the same fixed reference coefficient-space comparison as the B ledger; it does not identify shifted ghost modes with a physical state.

## A-dependent signed coefficient

For T=(V^-1+G)^-1, ||T||<=35. Holding the pole fixed, the native2x2 G error obeys

 ||Delta G|| <=[2s+(1+s)s²/3]eta_A <1500 eta_A.

The resolvent identity gives ||Delta T||<=1225||Delta G||/(1−35||Delta G||). Thus ||Delta J||<=70||Delta G|| whenever35||Delta G||<=1/2. Its trace operator effect is <=Tr M ||Delta J|| <318*105000*eta_A <10^-10. This avoids any derivative of a matrix absolute value. The actual numerical2x2 inverse must certify its residual separately; no binary64 accuracy assumption is made.

## Pole, weight and pi displacement

For s>=1/128, ||X_j||HS<=sqrt(17/10) and ||dX_j/ds||HS<=sqrt6*128². Moving all columns by at most rho while keeping their coefficients fixed costs at most

 (35*16/6)[2sqrt(17/10)*sqrt6*128²*rho+6*128^4*rho²]

in trace norm, less10^8 rho for rho<=2^-140. The additional coefficient movement can be bounded directly: ||dG/ds||<=||U||²/s²<=32768 and hence ||dT/ds||<=1225*32768. Its total contribution is less 2*10^8 rho. Using3*10^8 rho is therefore sufficient for all pole movement. This is a physical resolvent bound, independent of divided-difference conditioning.

Weight perturbations contribute <=(35/6)(17/10)sum|Delta w|<10*66 rho_w. Pi perturbations contribute <=(35*16/2)(17/10)*|Delta(1/pi)|; with pi>3 and |Delta pi|<=rho_pi this is <53 rho_pi. All three terms together are far below10^-10 under the frozen geometry precision gates.

These physical displacement terms are not charged again through scalar root widening: choose and record either exact-pole intervals throughout, or midpoint data plus this displacement allocation. The latter is the construction used here.

## Actual matrix-arithmetic stopping targets

Use outward rational/dyadic interval arithmetic for scalar alpha square roots, the2x2 T matrices, and all weighted Gram entries. No eigensolver is needed to certify these intervals. Require the additional *matrix arithmetic only* operator-radius bound epsilon_num<=2^-60, obtained for example by528 times the largest absolute entry rounding radius. Root/pi/input radii already charged above must not be counted as mere rounding or dropped. The corresponding factor-comparison error is <2*10^-6.

Require additional signed coefficient operator error <=2^-40, verified from the actual2x2 interval entries or inverse residual; its trace contribution is <318*2^-40<10^-9. A conservative entry criterion per2x2 block is radius<=2^-42 per real/imaginary component. Scalar sqrt operations may be enclosed by exact rational squared-endpoint comparisons. Their induced Gram entry widths belong to epsilon_num, rather than an unsupported condition number estimate.

Combining the previously reviewed B allocation .003001 with A10^-6, matrix rounding2*10^-6, and coefficient/geometry allocations of10^-9+2*10^-10 gives a bound below .003005, hence below1/200. More than .001995 remains unused; this is not a license to omit another error class. The initial quadrature error is separately bounded by the fixed p6/Jlo7/Jhi4 theorem. No use is made of ||Q||1 to bound a factor trace.

## Purification remains an explicit subsequent operation

This ledger supplies a sufficient complete input/arithmetic target for the unrounded quadrature representative. Its exact physical spectral rounding is still defined by the reviewed contour or polynomial construction. For the exact quadrature candidate, eight cubic purification steps have scalar truncation <=(2/7)(7/8)^256 and trace error <=528 times that quantity. Actual polynomial arithmetic must propagate its interval errors, and a midpoint Gram must not be substituted as the native Gram. This stage is not included by relabeling the initial .005 budget as a final pure-state error.

The decisive future implementation can now report each of: B input contribution, A Gram contribution, T contribution, pole/weight/pi contribution, weighted-entry rounding radius, and2x2 coefficient residual. It must stall if any frozen target fails. Actual A66/B66 enclosures and the528-dimensional matrix remain uncomputed here.
