# Cold review: actual cube fixed-character limit

Verdict: PASS on the fixed finite-character-window scope. This review independently reconstructs the action count, missing-face control, Haar partition lower bound, global complex-character bound and normalized matrix estimate. It does not rerun or import the native support runner. The reviewed proof hash is recorded in HASHES.json.

## Actual observable and nonabelian cap

The normalized entry is the positive Gibbs expectation of conjugate(chi_lambda(W_output)) times chi_mu(W_input), with D00 equal to the same integral without either character. This is not division of individual link coefficients by their Weyl dimensions, and not normalization by the largest compressed eigenvalue. Ten spatial halfweights and twelve temporal weights give total exponent17beta and precisely the stated nonnegative deficit E.

I independently reconstructed the cap in cyclic edge orientations. Set three bottom cyclic edges and four vertical edges toI. Write the fourth bottom edge W and four top cyclic edges A,B,C,D. Side holonomies are Q0=A^-1,Q1=B^-1,Q2=C^-1,Q3=W D^-1 and top T=ABCD. Then

    Q3 Q2 Q1 Q0 T = W D^-1 C^-1 B^-1 A^-1 A B C D = W.

No commutations are made. The separately supplied native word U=S D^-1 T^-1 A B is the corresponding identity with positive-coordinate top-edge orientations. Unitariy telescoping and Cauchy-Schwarz therefore give squared missing-loop deviation <=5 sum of the five face deviations squared. Since each norm squared is6(1-J) and those spatial deficits carry factor1/2 in E, the bound60E is correct on each slice. Gauge transformations only conjugate the holonomies used in norm estimates.

An adverse control shows why all five faces matter: in my cyclic convention, omit the side Q0 weight, choose B=C=I,D=A^-1,W=A^-1 with A nonidentity. Every remaining side and the top isI, but W is notI. Thus generic concentration without the complete cap does not force the source loop to identity. The proof's geometry, not an assumption that all loops are weighted, closes this obligation.

## Partition lower bound and concentration

SU3 embeds isometrically for Frobenius distance into R18 on radius sqrt3. Disjoint radius r/2 ambient balls about an r-separated set lie inside radius sqrt3+r/2; comparing Euclidean volumes gives at most(1+2sqrt3/r)^18 centers. Maximality gives a covering of the group by r-balls. Translation invariance of Haar and the chord metric then gives volume >=[r/(r+2sqrt3)]^18 >=(r/5)^18 for r<=1. It is legitimate to use ambient dimension18 instead of intrinsic8; this weakens the constant rather than invalidating it. Compactness/radius limits handle open boundaries.

All24 link variables in that ball give a spatial product deviation<=4r and a temporal-gauge product deviation<=2r. Using the weaker4r for all factors yields E<=17(16/6)r²=136r²/3. For r=beta^-1/2, beta>=1, the partition is therefore at least e^-136/3 5^-432 beta^-216. This uses the exact24-variable temporal-gauge measure; no gauge-orbit volume is divided out.

For any u>=0, the unnormalized integral over E>=u is bounded by e^-beta u because the underlying product Haar has total mass1. Dividing by the partition and integrating min(1,e^(A-beta u)) gives (A+1)/beta, since A>0. With log5<2, the constant is136/3+864+1=2731/3. Also E<=34 is conservative and valid. Thus B_beta and min(34,B_beta) are correct. Neither the saddle dimension nor an asymptotic density coefficient is assumed. The bound can be numerically weak at moderate beta without affecting its asymptotic conclusion.

## Global complex character estimate

When ||I-U||op>=1, the elementary |chi-d|<=2d and Frobenius>=operator norm prove the global inequality immediately for m>=1. In the complementary regime, each principal eigenangle has absolute value<pi/3. Their sum lies in(-pi,pi); detU=1 therefore makes it0, not an undetermined2pi multiple. This supplies a traceless Hermitian logarithm X and avoids a hidden branch error near a nontrivial center element.

The (p,q) irrep embeds in p fundamental and q dual factors, so the represented Hermitian generator has norm <=m||X||op<=m||X||F. Its trace is0 because su3 is its own commutator algebra. For any real a, the integral Taylor remainder gives |e^(ia)-1-ia|<=a²/2; summing eigenvalues gives the stated d m²||X||F²/2 bound for the FULL complex character, not just its real part. The chord inequality |theta|<=pi|e^(itheta)-1|/2 and pi<4 give the conservative coefficient2. Thus the complex conjugation on the output character presents no problem.

Combining |chi_lambda|<=d_lambda with the two source-loop estimates gives120 d_lambda d_mu(m_lambda²+m_mu²) times the expected E. With b_lambda=d_lambda m_lambda², absolute entry domination by120(bd*+db*) bounds the matrix norm by240||b||2||d||2. Positivity is not needed for that domination, although the original compressed matrix is positive. For a fixed finite window, the bound vanishes, giving dd* and its eigenvalues. Labels growing with beta are not covered uniformly: both dimension and degree constants grow. No infinite-dimensional operator limit, physical mass gap or finite-beta diagonalization follows.

## Fundamental entry and scientific boundary

Complex conjugation of every link preserves the real action and Haar measure, so the fundamental expectation is real. The exact identity3-ReTr(W)=||I-W||F²/2 gives the deficit bound30 min(34,B_beta). The strict upper inequality R<3 follows from positive finite-beta density and a nonconstant loop holonomy. The lower inequality R>0 uses the separately reviewed spatial-reflection theorem; concentration alone would not imply it. No monotonicity is claimed or proved.

The result concerns the unchanged finite bare-Haar source compression at beta tending to infinity. It does not choose a physical beta, replace an environment-dressed source map, or establish any thermodynamic limit. Generic compact concentration is correctly acknowledged as prior work; the specific cap-controlled two-slice observable is the substantive additional conclusion. No mathematical correction is requested.
