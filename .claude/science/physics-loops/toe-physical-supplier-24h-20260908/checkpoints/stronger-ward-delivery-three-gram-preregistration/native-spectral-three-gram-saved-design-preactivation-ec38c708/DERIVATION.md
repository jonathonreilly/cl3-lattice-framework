# Closed degree10 joint-form saved certificate (h=1)

This specializes the independently reviewed zero-dual theorem298c/eaf0 to the SAME accepted degree10 polynomial trials with the newly accepted spectral E,F. It does not change p,q or acquire any physical moment. Degree20 and nonzero duals are outside this protocol.

Write u_A=p0_A,w_A=p1_A,V_A=4w_A, B_A=i gamma(a)gamma(d_A), J_A=2i gamma(d_A). For the signed local two-neighbor vectors, a·d_A=0, d_C·d_A=n_CA=|C intersect A|, kappa(a,d_A)=-c and kappa(d_C,d_A)=0. Thus <B_A>=c and B_C B_A=gamma(d_C)gamma(d_A), whose expectation is n_CA. Also J_A B_A=4 gamma(a). The exact trial conventions are x0_A=-(u_A+w_A B_A)Omega and v0_A=q_A(2iu_A gamma(d_A)+V_A gamma(a))Omega.

The three real ordered kernels therefore are
 X_CA=u_Cu_A+c(u_Cw_A+w_Cu_A)+n_CA w_Cw_A,
 Y_CA=q_Cq_A[4n_CA u_Cu_A+V_CV_A+2c(u_CV_A+V_Cu_A)],
 Z_CA=-q_A[2u_A(cu_C+n_CA w_C)+V_A(u_C+cw_C)].

They equal Re<x0_C,x0_A>, Re<v0_C,v0_A>, and Re<x0_C,g v0_A>. The minus sign in Z is mandatory. For disjoint pairs X-Z exactly equals the existing source degree10.word; this is an algebraic sign check, not a rerun of its saved nominal. No disjoint-only covariance table is used for overlapping pairs: the exact overlap n is included explicitly.

Use all15 lexicographic pairs of labels0..5; kindO means the two labels have equal integer quotient by2, otherwiseP. Assign T² weights6 on the diagonal,1 on disjoint pairs,3 on distinct intersecting pairs. Sum each kernel over225 ordered pairs per choice. Both retained residual/variational choices require at most450 pairs and1350 kernel values. This is NEW joint-form arithmetic, not a reproduction of the old nominal, Wick source moments or scalar suppliers. No Wick recursion is needed: only the same saved c, fixed p0,p1,q, nominal, and certified spectral E,F are inputs.

Let G0,G1,G2 be these weighted sums, u²=G0 and w²=4G0+G1-4G2. Outward upper roots provide ||Tg*x0|| and ||2Tx0-Tg v0||. All expressions use the original c interval and exact rational coefficients; G2 is subtracted with its lower endpoint in the upper bound. A negative norm upper is refused. Use the sharp L(E,F) from298c:
 L=-3E²-3EF if F<=2E;
 L=-6E²-3F²/4 if2E<=F<=4E;
 L=6E²-6EF if F>=4E.

Then W>=W0-E*w-F*u+L. The safe upper is W<=W0+E*w+F*u+6E²+6EF. Divide by8 and intersect with the ALREADY accepted spectral/posterior alpha interval; never claim automatic improvement or substitute the newer interval if intersection is empty. The prior estimator remains an alternative.

## Necessary screen, before any joint-form arithmetic

The specific computed zero-dual lower bound is at most W0+L because its two gradient penalties are nonnegative. Thus if the exact rational screen W0_upper+L(E_upper,F_upper)<=0, this particular zero-dual certificate using these chosen certified errors cannot produce a strictly positive lower endpoint for ANY subsequent Gram values. Return ZERO_DUAL_POSITIVE_CERTIFICATE_EXCLUDED and retain the old accepted alpha interval. Do not compute any pair kernels in that branch. This is not an exclusion of truealpha, smaller true errors, a new certified E/F, or a nonzero signed-dual correction. It also makes no new negative-sign claim.

The branch is fixed prospectively and evaluated independently for BOTH retained choices. If the screen is positive, all225 pairs for that choice are evaluated once with no adaptive selection. Arithmetic refusal is recorded as INDETERMINATE_ARITHMETIC; it does not trigger a retry. The result distinguishes zero completed pair kernels by the screen from a numerical Gram completion.
