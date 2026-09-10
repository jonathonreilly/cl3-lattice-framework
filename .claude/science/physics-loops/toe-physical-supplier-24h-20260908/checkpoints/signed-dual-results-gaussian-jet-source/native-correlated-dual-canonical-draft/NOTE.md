# Correlated residual certificates for the native Ward observable

Claim type: bounded_theorem.

Status: source-reviewed conditional theorem with two accepted bounded calculations; canonical assembly and independent canonical review pending. Full pipeline, current-main combined verification, changed-audit readiness and formal audit: UNRUN.

The signed-dual calculation narrows the two retained alpha intervals, but both still contain zero. The earlier zero-dual screen excludes only that particular positive certificate. Neither result establishes alpha's sign, nonvanishing, or law selection.

## Supplied identity and the signed residual correction

We retain the original infinite native model, reference vacuum and Ward boundary identity supplied by the preceding canonical hierarchy. Set h=1. On the direct sum of the15 two-neighbor channels, H=diag(D_A)>=delta=1/4, J_A=2i gamma(d_A), C=-J, C*=J. The common g=gamma(e0) is self-adjoint unitary; T is adjacency of disjoint two-subsets of six labels and commutes with g. Write B=Tg; this B is distinct from the local impurity B_A=i g gamma(d_A).

For the exact states x=-H^-1 Omega_vector and v=H^-1 J H^-1 Omega_vector, the supplied observable is W=8alpha=Re(<x,Tx>-<x,Bv>). The inner product is conjugate-linear in its first argument. Keep the same degree1 polynomial trials x0=-p(H)Omega and v0=qJp(H)Omega and certified direct-sum errors ||e||<=E, ||f||<=F. All scalar, domain and source-family premises remain those of the accepted trials.

For arbitrary polynomial dual vectors y,z define r=-Omega-Hx0=He, s=Cx0-Hv0=Hf-Ce and correction=Re(<r,y>+<s,z>). Direct expansion gives

W-W0-correction = Re<e,2Tx0-Bv0-Hy+C*z> + Re<f,-B*x0-Hz> + R(e,f),

where R=<e,Te>-Re<e,Bf>. Thus a signed correction shifts the center, while two residual norms bound the remaining linear error. No commutation of H with T or g, independence of residuals, or replacement of a vacuum inverse by an operator norm is assumed.

## Sharp quadratic remainder and the zero-dual boundary

Let N be the6-by15 vertex-edge incidence matrix of K6. Since NN*=4I+J6 and T=J15+I-N*N, the eigenvalues of T are6,-3,1 with multiplicities1,5,9. Hence T²<=3T+18I. Put a=||e|| and m=<e,Te>/a². Minimizing a²m-aF sqrt(3m+18) over -3<=m<=6 and0<=a<=E yields

L(E,F) = -3E²-3EF for F<=2E;
L(E,F) = -6E²-3F²/4 for2E<=F<=4E;
L(E,F) = 6E²-6EF for F>=4E.

These branches agree at their boundaries and decrease as either nonnegative error bound increases. Equality can be attained by vectors in the6 and-3 eigenspaces with appropriately aligned gf, so this is sharp given only these norm premises. It is not a statement that native errors attain the worst case.

With zero duals, the lower bound is W0-E||2Tx0-Bv0||-F||B*x0||+L. Since both norm penalties are nonnegative, W0_upper+L(E_upper,F_upper)<=0 rules out a strictly positive lower endpoint from this fixed zero-dual certificate. It does not rule out smaller certified errors, nonzero dual corrections or a nonzero physical alpha.

The completed screen returned this limited exclusion for both fixed modes, with zero pair kernels computed. The original spectral interval was retained. The accepted screen is not retroactively relabeled a sign result.

## Closed kernels and reduced action data

Write u_A=p0_A,w_A=p1_A,V_A=4w_A. The trials are x0_A=-(u_A+w_A B_A)Omega and v0_A=q_A(2iu_A gamma(d_A)+V_A g)Omega. For n=|C intersect A| and the same c=<B_A>, the real kernels are

X_CA=u_Cu_A+c(u_Cw_A+w_Cu_A)+n w_Cw_A,
Y_CA=q_Cq_A[4n u_Cu_A+V_CV_A+2c(u_CV_A+V_Cu_A)],
Z_CA=-q_A[2u_A(cu_C+n w_C)+V_A(u_C+cw_C)].

The ordered minus sign in Z is essential. T² weights are6 for equal pairs,1 for disjoint pairs and3 for distinct intersecting pairs. Summing gives G0,G1,G2, with ||B*x0||²=G0 and ||2Tx0-Bv0||²=4G0+G1-4G2. The lower endpoint of G2 is used in an upper bound on the latter norm.

Nonzero duals require additional signed data. For each channel set U=B*x0 and V=2Tx0-Bv0. Using [H0,gamma(f)]=i gamma(Kf), H0Omega=0, g²=1 and ||d_A||²=2 reduces the vectors V,HV,JU,HJU to scalar/quadratic Clifford words, while U is linear and HU at most cubic. The first residual is at most quadratic and the inner residual linear. These are identities on the polynomial vacuum vectors, not arbitrary-state commutator replacements.

The complete action formulas are preserved in the reviewed proof snapshot. Their finite bank lies in (a,d,k,e,Kd,Kk,Ke), omitting e,Ke for opposite pairs. With neighbor combinations f=sum f_j b_j,h=sum h_j b_j, n=sum f_j h_j and m=sum f_j h_(j xor1), the dots are <f,h>=n, <Kf,Kh>=6n+m, <a,Kf>=-sum f_j; the nonzero covariances are kappa(a,f)=-(c/2)sum f_j and kappa(Kf,h)=3cn+(nu/6-3c)m. Antisymmetry and parity supply the remaining entries. Thus these new contractions need only the already authenticated c and nu; E,F retains its separate full spectral provenance.

Acquire the real4-Gram of(V,HV,JU,HJU), real2-Gram of(U,HU), and c0=Re<r,V>,c1=Re<r,JU>,c2=Re<s,U>. These13+3 entries support y=s0(V-tJU),z=-tU. The residual coefficient vectors are(1,-s0,-t,s0t) and(-1,t); the signed correction is s0c0-s0t c1-t c2. Certified interval quadratic forms and outward roots give the two norms. Negative norm uppers or empty certificate intersections refuse rather than manufacture success.

## Fixed proposals and five scales

Midpoint Rayleigh ratios propose t and then s0, clamped to[0,4] and rounded down to2^-64. Nonpositive denominators or arithmetic refusal use the predefined zero fallback. The midpoint is never treated as a PSD or optimizer certificate: all bounds use the original interval entries at the chosen exact dyadics.

For lambda in(0,1/2,1,3/2,2), scale both dual vectors uniformly. The coefficients become(1,-lambda*s0,-lambda*t,lambda*s0*t),(-1,lambda*t), and correction lambda times the unscaled correction. Replacing both parameters by their scaled values would incorrectly introduce lambda². All scales reuse the same contractions. Intersect their valid alpha intervals with the prior accepted interval; this cannot widen that prior interval, but need not establish a sign. The zero-dual screen cannot suppress these signed candidates.

## Accepted outcome and its limits

The reduced signed-dual study completed once in4.65 seconds externally, with82,706,432-byte external RSS and119,488,512-byte sampled whole-tree peak. Its763 events and nine output files retain both modes,15 channels per mode and all five scales. Complete covariance/operator signatures allow exact reuse:684 expanded Wick words were evaluated versus5130 logical uncached words. These are distinct from recursive Wick-state counts.

For both modes lambda=1 supplies both final endpoints. Descriptive rounded intervals are:

| Mode | Prior spectral interval | Accepted signed-dual interval |
|---|---|---|
| Residual | [-734.76773,826.14955] | [-489.19594,665.70731] |
| Variational | [-737.70476,890.22488] | [-441.59020,696.19304] |

Lambda1/2 and the zero dual also improve on the prior interval, but less than lambda1. Lambda3/2 and2 do not improve either endpoint beyond lambda1. This describes the retained candidates; it is not a continuous optimization claim. Both final statuses remain INDETERMINATE_SIGN.

The worker's raw covariance and Wick correctness were independently source-reviewed. The root independently reconciled proposals, quadratic forms, signed corrections, scales and intersections, while explicitly inheriting raw Wick/scalar truth. The compact supporting checker authenticates this evidence boundary and tests synthetic algebra; it does not replay any native contractions.

Exact bytes, compressed event-stream recovery and original paths are in INVENTORY.json. Remote89 head8c202703bfd600147e7a27d146594859191ba610 supplies preregistration provenance; the later archive containing completed outputs remains a parent delivery dependency. Historical bytecode/membership preparation and retention/transient-bound repairs remain preserved in scratch and must receive exact remote recovery links before canonical delivery. No audit or integration success is implied by this draft.
