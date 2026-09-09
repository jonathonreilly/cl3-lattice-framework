# Rank-one real polar transversality: qualitative argument

Let B0 and B_lambda,0<=lambda<=1, be bounded real operators between the two sublattice Hilbert spaces, with zero kernels for both operators and their adjoints. Their polar factors U0,U_lambda are therefore real orthogonal onto maps even if the singular spectrum accumulates at zero. Write B0=U0 S, B_lambda=U_lambda T_lambda, with bounded positive injective S,T_lambda. Suppose B_lambda-B0 has rank at most one, and U_lambda-U0 is trace class, continuous in trace norm along lambda. Put R_lambda=U0^T U_lambda.

The eigenspace E=ker(R_lambda+I) has dimension at most one. Indeed U0^T B_lambda=S+u v^T=R_lambda T_lambda. If dim E>=2, there is a nonzero real x in E with v^T x=0. Then

 x^T Sx=x^T(S+u v^T)x=x^T R_lambda T_lambda x=-x^T T_lambda x,

contradicting strict positivity of the two quadratic forms. T need not preserve E. No bounded inverse of S or T was used.

R_lambda is real orthogonal and I+trace class. Its Fredholm determinant is real and equals (-1)^m, where m is the finite multiplicity of -1: the other nonreal eigenvalues occur in conjugate unit-circle pairs with product one. The determinant is continuous in trace norm and starts at1. For completeness, continuity follows by the absolutely convergent exterior-power expansion and its bound |det(I+A)-det(I+B)|<=||A-B||_1 exp(1+||A||_1+||B||_1). Hence m is even. Combining m<=1 with evenness gives m=0.

Because R_lambda-I is compact normal, absence of the eigenvalue -1 also excludes -1 from the spectrum: nontrivial eigenvalues can accumulate only at1. Thus I+R_lambda has a bounded inverse for each lambda. Trace-norm continuity and compactness of the parameter interval give a common finite inverse bound, but this argument supplies no useful numerical value.

## Actual native premises

For the actual two-link defect, B_lambda=B0-2lambda e0 b_A^T and b_A contains the two original signed center-neighbor couplings. Both bare inverse columns B0^-1 e0 and B0^-T b_A lie in l2 by the local inverse-square Green bounds. Moreover b_A^T B0^-1 e0=1/3. If B_lambda x=0, substitution into the bare inverse gives (1-2lambda/3)b_A^T x=0; hence x=0. The transpose argument is identical. This proves the required zero-kernel statements without a uniform spectral gap.

The reviewed trace-class impurity projector proof5654417a gives P_lambda-P0 in S1, continuous in lambda. The offdiagonal sublattice block of the sign function is the polar factor, so it gives the stated S1 continuity of U_lambda-U0. These are actual native premises, not an assumed general gap or parity selection rule.

## Why determinant positivity alone gives no numerical angle margin

A nonnative2x2 family illustrates the limit. Set S_n=diag(6n²,1) and

 D_n=[[-6n²,4n],[-4n,7/3]].

D_n-S_n has rank one and det(S_n+lambda(D_n-S_n))/det S_n=1-2lambda/3 throughout the path. Yet the relative polar rotation has cosine

 (7/3-6n²)/sqrt((7/3-6n²)²+64n²),

which tends to -1. Scaling both matrices by6n² bounds their norms without changing their polar factors. An orthogonal left multiplication can turn the rank-one update into a single-row update. This remains a synthetic example, not a native cubic counterexample. Its weighted perturbation size is10/3, violating the stronger native metric bound proved separately. It only shows that the determinant ratio and bounded operator norms alone do not quantify the chart.
