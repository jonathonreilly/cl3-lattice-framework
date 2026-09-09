# Direct Gaussian resolvent candidate: distinct unlaunched route

The closed CG attempt is not retried. This design changes the algorithm and requires its own reviewed source/cost/contract. No physical array/action is executed. The exact fresh-residual certification remains the acceptance mechanism; a floating SVD is only a candidate generator.

## Actual real CAR convention and quadratic matrix

In the reviewed kernel A_j is real symmetric with A_j²=I. B_j is real antisymmetric with B_j²=−I and the factor (2n_j−1) on its input column. Thus A_j B_j=2n_j−1 and B_j A_j=1−2n_j. This sign is load-bearing. All distinct generators anticommute. Let a be the center B coefficient vector and b the sum of the two neighbor A coefficient vectors weighted by their native k=-2. The actual pair operator is

 Hpair = sum_j omega_j n_j + B(a) A(b)
       = c I − (1/2) sum_ij M_ij B_i A_j,
 c=(1/2)sum omega_j,    M=diag(omega)−2 a b^T.

The perturbation of the 21 by21 real matrix is rank one. No onsite Hamiltonian or extra physical pulse is introduced: this is classical computation of the already supplied operator's inverse candidate.

Choose oriented singular decomposition M=U diag(sigma) V^T with U,V in SO(21), allowing signed singular values. Starting from ordinary orthogonal SVD U0,S,V0, multiply their last columns by det(U0),det(V0); the last signed singular value becomes det(U0)det(V0) times its nonnegative value. This preserves M exactly and keeps both rotations even-implementable. Zero singular values cause no difficulty for the algebra, but inverse denominators must be checked in the selected parity sector rather than assumed positive from an unrestricted vacuum.

Define B'_j=sum_i U_ij B_i and A'_j=sum_i V_ij A_i. Then Hpair=c−(1/2)sum_j sigma_j B'_j A'_j. In the rotated occupation basis its energies are

 E(n)=delta+sum_j sigma_j n_j,
 delta=(sum_j omega_j−sum_j sigma_j)/2.

Keeping signed sigma is essential. Replacing them by absolute values without an accompanying parity relabeling can choose the wrong physical sector. SO rotations preserve total active parity; selected even/odd parity is the one used by the existing first/second resolvents. The certified proper-prefix gap gives positivity on that sector; it is not inferred from an approximate SVD.

## Real Spin rotations and application order

For p!=q, both A_p A_q and B_p B_q are real antisymmetric, square−I and preserve parity. Hence exp(theta A_p A_q/2)=cos(theta/2)I+sin(theta/2)A_p A_q, and similarly for B. Their conjugations have opposite signed plane conventions because A²=+I and B²=−I:

 e^(theta AA/2) A_p e^(−theta AA/2)=cos(theta)A_p−sin(theta)A_q,
 e^(theta AA/2) A_q e^(−theta AA/2)=sin(theta)A_p+cos(theta)A_q;
 e^(theta BB/2) B_p e^(−theta BB/2)=cos(theta)B_p+sin(theta)B_q,
 e^(theta BB/2) B_q e^(−theta BB/2)=−sin(theta)B_p+cos(theta)B_q.

A generators' bilinears commute with B generators' bilinears. SO decompositions into plane rotations therefore give a real orthogonal parity-preserving Spin matrix W with W A_j W^T=A'_j and W B_j W^T=B'_j, provided the plane sign conventions above are respected. Hpair=W Hdiag W^T. The direct inverse candidate is W [Hdiag^-1 (W^T rhs)]. Apply inverse rotations to rhs, divide each compressed occupation coordinate by delta+sum sigma_j n_j, then apply forward rotations in reverse sequence. Overall double-cover sign cancels. No dense Fock matrix is formed.

Each bilinear maps an occupation to the one with p,q toggled, with the product of the actual input-column CAR signs. The two-state rotation must update both amplitudes from saved old values; an in-place sequential overwrite is wrong. Diagonal p=q is never a Givens generator. The omitted top bit is reconstructed from the fixed parity, exactly as in the reviewed kernel. A source-bound implementation must test A and B rotation signs separately, all pairs including top-bit pairs, and forward/inverse action against small dense CAR matrices with non-dyadic angles.

## Resource and certification boundary

Generic SO(21) decomposition requires at most210 planes per factor,420 total. Transforming into and out of the diagonal frame takes at most840 plane passes per inverse, plus one diagonal pass. Four representatives could require3360 passes, with additional source/final transport work. This may be slower than expected: rank-one M does not automatically imply a short Spin circuit. One real vector plus bounded pair scratch can replace CG's x,r,p,Ap collection, materially changing peak storage. A measured plane-pass cost and complete live-memory accounting are required before proposing a physical run.

Approximate SVD/rotation errors need not be trusted as a physics certificate. After constructing x, certify the true fixed operator residual by the existing exact norm/envelope method and gap1/3; a bad decomposition or denominator causes a failed certificate. Guard all floating denominators, finite values and magnitude ceilings. If signed-spectrum cancellation makes delta inaccurate, compute it at higher precision or use an interval, but still certify the true residual. No fallback/retry schedule is selected here.

## Potential smaller first-source space

For a first solve with vacuum rhs and rank-one perturbation B(a)A(b), a sufficient invariant complex one-particle space is the smallest space closed under the baseline frequency matrix and containing a and b. Since the baseline has four distinct frequencies, span{P_lambda a,P_lambda b} has dimension at most8. It is number-preserving relative to the baseline vacuum. The corresponding Fock space, vacuum outside it, is invariant under Hpair because both linear factors lie in that space and H0 preserves it. Thus the first-source resolvent can be solved on at most8 complex modes (128-dimensional fixed even parity), with exact embedding back into21 modes.

This is an upper-bound theorem, not a demonstrated dimension or free embedding cost. Second sources are sums of transported first solutions and need not belong to the same eight-mode space. Projecting them into it without proof would change the operator problem. A useful next source-only step is exact rank/basis construction for the two first-source spaces using the rational adapted sectors, followed by a tiny oriented-SVD/Spin implementation. No physical-cost or solve authorization is implied.
