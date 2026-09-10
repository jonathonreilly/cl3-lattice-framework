# Correlated Ward gradients, dual residuals, and a sharp quadratic remainder

Unreviewed, source-only. No actual moments, nominal values, histories, scalar values or running witness outputs are read. The current numerical sign remains unknown. The three results below have distinct input requirements: the norm-only spectral remainder needs no new Wick contraction; the zero-dual gradient certificate needs three weighted Gram contractions; a nonzero dual certificate needs additional signed residual contractions and dual Gram matrices. None is being claimed numerically sufficient.

## Supplied problem and conventions

On the direct sum of15 native pair channels let H=diag(D_A)>=delta=h/4, x=-H^-1 Omega_vector and v=H^-1 J H^-1 Omega_vector, with J=diag(J_A), J_A=2i gamma(d_A). Thus J*=-J and ||J_A||=2sqrt2 h. Let T be the adjacency matrix of disjoint two-subsets of six labels, acting on the channel index. The common g=gamma(e0) is a self-adjoint unitary, commutes with T, and maps odd/even vectors into each other. Put B=Tg (this B is NOT the local impurity perturbation). More generally all identities use B*=g*T and need only ||B||=6.

The supplied exact observable is
 W=8alpha=Re(<x,Tx>-<x,Bv>).

Keep the original polynomial trials x0=-p(H)Omega and v0=qJp(H)Omega, with p of degree2 and channel-dependent fixed real constant q. Assume their independently certified errors ||x-x0||<=E and ||v-v0||<=F. Their coefficients, E,F, original nominal, scalar enclosures and all domain premises must be authenticated by any future protocol. No new choice of p or q is made here.

The native source explicitly uses x0=-pOmega and the stored nominal base+q*correction. Define Ccouple=-J, so Hv=Ccouple x and Ccouple*=J. This sign convention reproduces that stored nominal. Define e=x-x0, f=v-v0, r=-Omega-Hx0=He, s=Ccouple x0-Hv0=Hf-Ccouple e. Trial vectors and chosen duals lie in the common local-polynomial form core. The inner product is conjugate-linear in its first argument; all correction formulas below use real parts.

## 1. Exact dual residual identity

For arbitrary y,z in Dom(H), define
 a=2Tx0-Bv0-Hy+Ccouple*z,
 b=-B*x0-Hz,
 correction=Re(<r,y>+<s,z>).

Then the exact identity is
 W-W0-correction = Re(<e,a>+<f,b>)+R(e,f),
 R(e,f)=<e,Te>-Re<e,Bf>.                                      (1)

Indeed correction=Re<e,Hy-Ccouple*z>+Re<f,Hz>; subtracting this from the linear expansion of W gives(1). The coupling-adjoint sign is essential: Ccouple*=J, whereas J*=-J. Using x0=+p together with the stored plus nominal would give an incorrect signed correction. This uses no commutation of H with T or g, and no independence of residuals. In particular it does not replace a vacuum inverse by a full operator inverse.

Consequently a rigorous lower certificate is
 W >= W0+correction-E||a||-F||b||+L(E,F),                       (2)

where L below is a universal sharp lower bound for R. A safe upper certificate uses +E||a||+F||b||+6E²+6EF. Signed interval correction is retained before inflating the remaining error. Merely computing norms of y,z is insufficient: their two residual norms and signed correction are the required inputs.

Exact adjoint solves Hz=-B*x0, Hy=2Tx0-Bv0+Ccouple*z would eliminate both linear residuals. We do NOT assume these solves are available. They explain what a low-degree dual would approximate. Choosing y=z=0 is already a new computable estimator:

 W >= W0-E||2Tx0-Bv0||-F||B*x0||+L(E,F).                     (3)

This preserves cancellation inside the first gradient instead of replacing it by6(2||x0||+||v0||). It is not necessarily stronger for every input than the prior posterior bound; retain the maximum of independently valid lower certificates.

## 2. Sharp norm-only lower remainder using the exact Kneser spectrum

Let N be the6-by15 unsigned vertex/edge incidence matrix of the complete graphK6 and Jall the15-by15 all-ones matrix. T=Jall+I-N*T N. Since N N*=4I+J6, T has eigenvalues6 on constants, -3 on the five-dimensional zero-sum incidence range, and1 on the nine-dimensional kernel of N. This is an elementary finite graph identity, not an imported physical gap. In particular
 T²<=3T+18I, and T²=3I-2T+3Jall.                              (4)

Set hvec=gf. For a=||e||>0 and m=<e,Te>/a² in[-3,6],
 R>=a²m-F||Te||>=a²m-aF sqrt(3m+18).

Minimizing the scalar expression over m and then0<=a<=E gives

 L(E,F) = -3E²-3EF,              0<=F<=2E;
          -6E²-3F²/4,           2E<=F<=4E;
           6E²-6EF,             F>=4E.                       (5)

For E=0 set L=0. The interior minimum occurs at sqrt(3m+18)=3F/(2a); outside that range it is at m=-3 or6. In each branch the minimized expression decreases as a increases over the applicable range, so a=E gives the global minimum. Formula(5) is continuous at both boundaries and is nonincreasing in both nonnegative E,F; certified upper errors can safely be used. Sharpness follows by choosing e in the span of the6 and-3 eigenspaces with the required mean m and hvec parallel to Te with normF. No strictly stronger universal lower bound can follow from only E,F,T and unitary g. This is a precise obstruction to further norm-only improvement; it is not a native sign obstruction.

The identities in sections1–2 allow arbitrary h with consistently scaled states and errors. Sections3–5 below specialize the native table and implementation counts to h=1: equivalently use dimensionless K/h and the corresponding dimensionless d and absolute moments before restoring units. In particular Ka=sum b_j and the displayed mu,nu,omega5 tables are not asserted with unscaled K at arbitrary h.

## 3. Minimal new acquisition: three T²-weighted trial contractions

Because g is common to all channels and commutes with T, put
 G0=<x0,T²x0>, G1=<v0,T²v0>, G2=Re<x0,T²g v0>.

Then ||B*x0||²=G0 and ||2Tx0-Bv0||²=4G0+G1-4G2. The second expression must be evaluated as a signed correlated interval and refused if its purported upper bound is negative. Replacing G2 by its upper endpoint in an upper gradient norm would be wrong; its LOWER endpoint is needed. This is a joint trial covariance estimator, not a product of separate trial norms.

Exactly(T²)_CA is6 for C=A,1 for disjoint C,A, and3 for distinct intersecting C,A. Thus the required scalar kernels are
 Re<x0_C,x0_A>, Re<v0_C,v0_A>, Re<x0_C,g v0_A>
 with those fixed weights. There are15 diagonal,90 ordered disjoint and120 ordered intersecting pairs. The existing degree20 source compute.py records cross_wick_raw.base and correction for the five disjoint classes; these are usable only after exact coefficient/orientation authentication. It does NOT record the v-v family, nor the intersecting and diagonal x-g-v families. The diagonal x-x and v-v norms can be recovered from existing source_moment_raw index0 and q because J*J=8h²I. The original nominal alone cannot separate these three weighted contractions.

A conservative NEW computation, reusing those saved disjoint base/correction (with G2=-q times the stored correction) and diagonal norms without rerunning them, needs at most:
 -120 ordered intersecting x-x kernels;
 -210 off-diagonal v-v kernels;
 -135 diagonal/intersecting x-g-v kernels.
Total465 new ordered kernels PER polynomial choice. Both retained residual/variational choices require at most930 kernels,14880 Wick words and223200 naive pairing terms before caching. Each p2 trial has at most four Clifford monomials of length<=2, because O2=2-kd-av and O1=B_A. Each v trial has at most four monomials of length<=3. Thus each requested kernel expands into at most16 Wick words, of length<=6, for at most7440 Wick word evaluations. A naive perfect-pairing expansion at length6 has15 pairings, giving at most111600 pairing terms before scalar interval arithmetic. These are safe symbolic counts, not measured native runtime or interval-width guarantees. Hermitian/orbit caching can reduce work but is not assumed in this count.

The source vectors for this minimal stage are a,d_A,d_C,Ka,Kd_A,Kd_C: powers of K no greater than1. Their general overlapping-pair covariance must be generated explicitly; the existing disjoint-only cross_table must NOT be applied unchanged. No new scalar beyond mu=3c and nu is required by the seven-star covariance identities below. Existing omega5 is needed for the certified degree20 residual bounds but not these additional gradient contractions. A future worker must preserve actual interval correlations/provenance and freeze all new overlapping tables, count caps and gates. Nothing here authorizes an actual evaluation.

## 4. Optional small nonzero dual family and its larger input boundary

Write u=B*x0 and w=2Tx0-Bv0. Choose fixed real t,s0 and z=-t u, y=s0(w-t Ccouple*u). This does not increase the degree of the physical p/q trials. Then
 a=w-s0 Hw-t Ccouple*u+s0t HCcouple*u,
 b=-u+t Hu,
 correction=s0 Re<r,w>-s0t Re<r,Ccouple*u>-t Re<s,u>.              (6)

For this family the complete new data are the real4-by4 Gram matrix of(w,Hw,Ccouple*u,HCcouple*u), the real2-by2 Gram matrix of(u,Hu), and the three signed contractions displayed in(6). No original saved degree20 event contains this entire set. Direct interval quadratic forms then produce ||a||²,||b||² and the signed correction for any prospectively fixed finite t,s0 family. The zero pair is always retained.

These vectors require at most one new H action on the displayed low-degree words, which differentiates K^0/K^1 sources to K^1/K^2 and multiplies by the local quadratic impurity. The local-polynomial core supports this action. A conservative expansion has at most48,192,24,120 monomials for the four a-vectors and24,96 for the b-vectors, with degree<=6. The r and s trial residuals have at most13 and20 monomials. Therefore one full15-channel implementation could require at most1,714,680 Wick words, some length12 (10395 naive pairings each). This is NOT a cheap ready-to-run stage; it needs symbolic reduction/caching and a separately justified cost before any protocol. The minimal gradient stage above avoids that larger workload.

## 5. Explicit finite covariance closure for the optional dual

Let b_j=epsilon_j e_j for the six signed neighbor sites, so Ka=sum_j b_j. The entire new bank is contained in {K^i a,K^i b_j:0<=i<=2}; linear relations can reduce its nominal21 columns. Dots are exact finite-support lattice algebra. For the real antisymmetric vacuum covariance kappa, [K,Gamma0]=0 gives
 kappa(K^i f,K^j g)=(-1)^i kappa(f,K^(i+j)g).

Bipartite parity makes the inappropriate color pairs zero. The nonzero base entries needed up to total power4 are:
 kappa(a,b_j)=-mu/6;
 kappa(a,K²b_j)=nu/6;
 kappa(a,K⁴b_j)=-omega5/6;
 kappa(a,Ka)=-mu, kappa(a,K³a)=nu.

For neighbor blocks M_l(i,j)=kappa(b_i,K^l b_j), l=1,3, the matrices are symmetric. Their diagonals are -mu and nu. Their signed pair quadratic forms for d_A=b_i+b_j are M1[d_A]=-e_A, M3[d_A]=e3_A, where
 e_P=2mu, e_O=nu/3; e3_P=2nu, e3_O=omega5/3.
Hence each off-diagonal is recovered as one half of the corresponding pair form minus the two diagonal contributions. These are precisely the reviewed six-vector degree11/20 identities, now polarized across arbitrary pairs. They determine all required overlapping covariance entries with only mu,nu,omega5. One must preserve these signs; in particular J*=-J and kappa(d,Kd)=-e_d.

This proves a scalar closure, not availability of a numerical Gram certificate or an acceptable runtime. Full interval implementation of the new tables, independent source review and a NEW bounded computation remain necessary. The current failed/indeterminate protocols and their scopes stay unchanged.
