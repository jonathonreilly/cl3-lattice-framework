# Rational-coordinate certification for the adjacent sixth-order DP

This is a concrete alternative certification interface, not a coefficient result or authorization to scan prefixes. The supplied exact rational orthogonal black columns r_i and d_i=r_i^T r_i>0 come from the frozen frame construction. Their common span and the canonical K matrices are the earlier design inputs. We retain t=1, full vacuum complement offset and the unreduced initial-parity convention. Root requested an independent route; checker concurrently constructs an orthonormal interval implementation. No completed solver output was used here.

## Remove the frame radicals by a diagonal similarity

Put omega=2sqrt6, B_i=r_i/sqrt(d_i), C_i=-K0 r_i/(2sqrt6 sqrt(d_i)). For each prefix define the exact rational ten-by-ten matrix

q_ij=-r_i^T K_F K0 r_j/12.

Then M_ij=(B^T K_F C)_ij=sqrt6 q_ij/sqrt(d_i d_j). On occupation bits b define s_b=product_i d_i^(b_i/2), S=diag(s_b), W=S²=diag(product_i d_i^b_i). Coordinates represent physical vector S z. In the even512-dimensional block,

S^-1 H_F S=sqrt6 J_F,

where J is entirely rational. Its diagonal is sum_i(q_ii/d_i)(b_i-1/2). For i<j and a=b XOR2^i XOR2^j its entry is

J_ab=sign(b;i,j)/2 [q_ji(1-2b_i)-q_ij(1-2b_j)] d_i^(b_i-1) d_j^(b_j-1),

with sign=(-1)^(popcount(b below i)+popcount(b below j)), exactly the original Fock convention. This follows because s_b/s_a divided by sqrt(d_i d_j) equals the displayed rational powers. Hence WJ=J^T W. The similarity is not unitary in ordinary Euclidean coordinates; omitting W would invalidate residual/error norms.

The reduced starting energy is -5omega=-10sqrt6. Thus H_F-E0,reduced =sqrt6 S A_F S^-1, A_F=J_F+10I rational. No exact extension larger than Q(sqrt6) is necessary, and scaling away sqrt6 makes each linear system rational. At the base q_ij=2d_i delta_ij and J has energy2(popcount(b)-5), which independently checks the vacuum offset.

## Exact residual certification without exact inverses

At levels k=1..5 let z_k=(sqrt6)^k S^-1 x_k, where x_k is the actual partially summed DP vector after k inverses. With electric insertion factor1/2 and R=(E0-H)^-1, the recurrence is

A_s z_s = -1/2 sum_(predecessors) z_prev.

The target has no final resolvent: z_target=1/2 sum z_5. All exact target coordinates are rational. Approximate candidates can be obtained by any floating solver, then converted to exact dyadic rationals; correctness does not depend on that solver or its frame being accurate. Form A and the residual using exact Fraction/integer arithmetic. This removes frame, matrix-assembly, BLAS residual and floating-summation uncertainty from the certificate itself. It does not make an approximate solve exact.

Use ||z||_W²=z^T Wz. If the already proved physical denominator bound is delta_s>0, then ||A_s^-1||_W <= sqrt6/delta_s. Choose a fixed rational upper u6 with u6²>6 and u6>0. If incoming certified coordinate error is e_in and the exact rational residual is r=b_hat-A_s z_hat, the coordinate error obeys

e_s <= (u6/delta_s)(e_in + upper_sqrt(r^T Wr)).

The incoming error is one half the sum of predecessor errors; signs cannot increase that bound. At the target it is likewise half the predecessor sum. This is a valid but potentially pessimistic bound; if it cannot resolve the coefficient, report indeterminate rather than claiming cancellation or increasing tolerances.

Square roots of positive rational p/q can be bounded outward by integers: for chosen D, find n with n²q>=pD² and (n-1)²q<pD²; n/D is an exact upper bound. No floating sqrt is required. Gap certificates and dyadic candidates are source-bound data. A singleton-cut prefix still uses its separately proved initial-parity gap, not the unrestricted ground-distance certificate.

Exact rational inversion is optional. Dense512 rational inverses may be expensive and need not be attempted. Exact residuals use the sparse zero/two-bit transition structure. A floating candidate may be computed in the better-conditioned orthonormal frame and converted to rational coordinates; any conversion error is automatically included when the resulting dyadic vector is checked against the exact A.

## Closing bra and rational coefficient scale

For adjacent black v and white w, define c_wj=-(K0r_j)_w/2, rational. The ordered gamma_v gamma_w has coefficients r_i(v)c_wj/(sqrt6 sqrt(d_i d_j)) multiplying a_i b_j. Therefore

L=-i sqrt6 S^-1 gamma_v gamma_w S

is a real rational matrix. Its vacuum row ell=e0^T L is the actual closing bra in scaled coordinates, not an unweighted physical row copied from another basis. For the fixed ordered adjacent pair, ||ell||_(W^-1)²=6 because gamma_v gamma_w is norm-preserving and e0 has W norm1. The finite control independently verifies this identity on the actual frame.

Five resolvents and the one closing factor give

<vac|gamma_v gamma_w x_target>= i (ell z_target)/6³.

Thus, with the fixed Gauss/cut ordering of the parent and spectator operator i bar_gamma_v bar_gamma_w, the associated real coefficient is rational at t=1. All six factors1/2 and five negative resolvent signs remain in the DP. A different ordered spectator convention changes the corresponding orientation sign; this formula does not license dropping it. For coefficient evaluation a coordinate error e gives absolute error at most u6 e/216. Exact rational evaluation of ell z_hat introduces no new roundoff. Summing bridge families requires retaining their actual closing orientation and adding their certified errors. Nonadjacent-cut classification is outside this packet.

## Bounded controls and limits

check.py verifies the supplied rational Gram directly, independently reconstructs full canonical64 K, and builds one actual512 rational prefix matrix. It checks WJ=J^T W entrywise, base energies, similarity-factor identities and the actual closing-row dual norm6.3357 predicates pass in0.419s22.66MiB. A supplied dyadic test vector yields an exact rational residual without solving. No prefix scan or coefficient computation occurred.

The metric ranges125/1296 to1327104 on this frame, so numerical conditioning must be measured rather than assumed benign. Exact Fraction residual cost and accumulated bounds remain unprofiled. This route is implementable and mathematically certifying if its bound excludes zero, but it has not yet demonstrated that exclusion or exact cancellation. It complements, rather than validates, the checker's independent interval implementation.
