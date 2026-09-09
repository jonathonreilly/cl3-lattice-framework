# Efficient certified mixed transition inverse and logarithm

Prospective finite-matrix arithmetic method, no native propagation or matrix evaluation. Inputs must already be certified real-skew pairings in one legitimate common CAR frame. Their approximation to infinite native pairings, HS tails and frame errors are separate obligations. A Gram-shift ghost representation is not admitted merely because the matrices below are invertible.

Let E=Z_C Z_A, ||E||<=q<1, M=I−E, and g=1−q. For the exact native disk q=9801/10000 and g=199/10000. For approximate finite inputs use a certified common qbar bounding their actual products; do not assume the exact disk automatically applies to approximate matrices. Then sigma_min(M)>=g and ||M||<=1+q. The positive mixed determinant branch is supplied by the independently proved real Gaussian overlap theorem.

## Eleven doubling steps

Set P_1=E and S_1=I. Given P_n=E^n and S_n=sum[k=0..n−1]E^k, compute

 S_2n=S_n+P_n S_n, P_2n=P_n P_n.

Eleven steps give2048 terms with22 matrix products, not2048 products. The last power product can be omitted if only the sum is wanted. In exact arithmetic ||P_n||<=q^n and ||S_n||<1/g, so no exact intermediate magnitude grows exponentially. The inverse tail is q^2048/g<10^-15. No normality or spectral-eigenvector assumption is used.

Floating or approximate products are candidates only. A fresh certified residual rho>=||I−M Shat|| gives

 ||M^-1−Shat||<=rho/g.

If the residual is computed for a matrix Mhat with certified ||M−Mhat||<=eta, use rho<=rhohat+eta||Shat||. Directed interval residual loops or an independently proved roundoff bound are required; a vendor multiplication result alone is not a certificate. This residual can replace lengthy forward propagation through all doubling products. Finite intermediate checks and a failed residual gate must stop the fixed attempt, not silently increase precision or iterations.

For optional forward enclosures, if power/sum errors at n are ep,es and new product/addition roundoff envelopes are dp,ds, then

 ep_next <=2 q^n ep+ep²+dp,
 es_next <=(1+q^n)es+ep(1/g+es)+ds.

These are sufficient, not claims that binary64 automatically meets a target. The fresh residual remains preferable. Transition F,B,C errors follow the previously reviewed two-/three-factor telescoping bounds.

## LU candidate and certified log determinant

Suppose a real LU candidate, including its row permutation Pi, defines the exact dyadic matrix B=Pi^-1 L U. Require finite stored entries and nonzero pivots. Unit diagonal L must actually be represented as unit, or its diagonal product must also be included. Build a certified residual bound eta>=||B−M|| with eta<g. Matrix-input error is included in eta, not omitted from the reconstruction residual.

Every M+t(B−M) is invertible because its least singular value is >=g−t eta. Its real determinant cannot change sign. Since det M>0, det B>0. The exact sign from permutation and diagonal factors must agree; a disagreement means the candidate/residual certificate failed. No numerical determinant square-root branch is selected.

The exact determinant differential gives

 |log det B−log det M| <=−N log(1−eta/g).             (1)

Indeed integrate |Tr[(M+tDelta)^−1 Delta]|<=N eta/(g−t eta). This works for nonsymmetric, nonnormal M. If a trace-norm residual tau>=||Delta||1 is available, the alternative bound tau/(g−eta) is valid. For eta/g<=1/2, the simple rational sufficient bound2N eta/g avoids evaluating the logarithm in(1). Thus a target delta_log may use eta<=g delta_log/(2N), with eta<=g/2. This is a dimension-dependent finite determinant bound, not a determinant continuity assertion based only on operator error in infinite dimension.

The computed scalar log det B also needs enclosure; summing unproved libm logarithms is insufficient. Each |Lii| or |Uii| is an exact positive dyadic. Write x=2^k y with1<=y<2 by integer comparisons. For z=(y−1)/(y+1),0<=z<1/3,

 log y=2 sum[j=0..m−1]z^(2j+1)/(2j+1)+R,
 0<=R<=2 z^(2m+1)/((2m+1)(1−z²)).

Use z=1/3 for log2. Combine all k into one signed integer before multiplying its log2 enclosure; then sum the remaining log y intervals outward. This certifies log|det B| directly without multiplying enormous/small pivots. The determinant sign is accounted for separately as above. Scalar interval widths and residual bound(1) are added.

## Normalized overlap and separate infinite-input error

The finite normalized log overlap is

 ell=½log det(I−Z_A Z_C)−¼log det(I+Z_A^T Z_A)−¼log det(I+Z_C^T Z_C).

Using I−Z_CZ_A instead gives the same determinant. The two anchors have least singular value>=1 and norm<=1+r², so the same backward-certificate method works with g=1 (or certified Cholesky plus its residual). Add half the mixed log error and one quarter of each anchor log error. Positive overlap follows from the theorem, not an amplitude floor. An ell interval yields multiplicative error exp(±delta); a separate outward scalar exponential is needed only when an amplitude is requested.

For true infinite pairings approximated by these finite matrices, first add the reviewed HS input bound with q_* controlling BOTH actual and approximate products. This is essential: finiteN LU error does not control omitted HS tails. Zero-padding a valid common finite CAR frame adds determinant1 and changes no state, while inventing numerical ghost modes is not justified. Relative gauges/frames and unnormalized evolution scalars remain separately bound.

## Prospective cost and outputs

Candidate inverse: at most22 doubling matrix products plus one fresh residual. Candidate log determinant: one real LU and one certified product residual per determinant, plus O(N) scalar log enclosures. These operation counts replace a2048-product narrative; no measured runtime or memory target is claimed. A later contract should save pairings/source hashes, qbar, inverse residual, exact pivot/permutation signs, LU residual, scalar log intervals and all HS/input allocations. No alpha or inserted-kernel sign conclusion follows.
