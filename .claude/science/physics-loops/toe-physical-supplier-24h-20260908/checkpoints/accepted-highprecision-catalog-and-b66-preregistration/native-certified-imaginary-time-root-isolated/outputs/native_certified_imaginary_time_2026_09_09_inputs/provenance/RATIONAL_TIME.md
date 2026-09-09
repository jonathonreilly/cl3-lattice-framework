# Shared rational displacement and stable impurity imaginary time

A theoretical computational bridge, not a executed propagation or cost claim. The supplied infinite pi-flux bath and actual two-link impurities are unchanged. This uses the separately frozen quantitative pair-vacuum chart b6ce4a68 (currently under independent review), the exact local resolvent identities, and their trace-class prerequisites. No physical matrix, integral, eigensolver or kernel is evaluated here.

## 1. Propagate in the impurity vacuum chart

Let Omega_A be the normalized impurity vacuum, with positive reference overlap a_A, and let H_A,+ be its positive one-particle excitation operator. Its spectrum lies in[0,6h]: the signed nearest-neighbor hopping has six entries of magnitude h per row, so the Schur bound applies even after the two flips. The impurity vacuum energy relative to the reference is the finite scalar E_A, not an extensive separately subtracted vacuum energy.

Express the initial reference vacuum in the impurity annihilator frame as

 Omega0=a_A exp[(1/2) f_A^dagger Z_A f_A^dagger] Omega_A.

The real bipartite frame permits Z_A real skew; its singular values are the same as those of the reverse stationary chart. The quantitative lemma gives ||Z_A||<=sqrt(347/349)<1 and ||Z_A||_HS²<87. The latter follows from the fourfold projector singular-value multiplicity: 2sum tan²(phi_j)<=4sum sin²(phi_j)/(1+1/348)<87.

Quadratic evolution then gives exactly

 Z_A(t)=exp(-t H_A,+) Z_A exp(-t H_A,+^T),
 exp(-t D_A)Omega0=a_A exp(-t E_A) exp[(1/2)f_A^dagger Z_A(t)f_A^dagger]Omega_A.   (1)

Both one-particle factors are contractions. Hence ||Z_A(t)|| never exceeds the stationary chart bound. No negative-band exponential is evaluated. The unnormalized scalar can be kept as

 log ||exp(-tD_A)Omega0||=-tE_A
   +(1/4)Tr log(I+Z_A(t)^dagger Z_A(t))
   -(1/4)Tr log(I+Z_A^dagger Z_A).                       (2)

All trace terms are finite and nonextensive. E_A still requires a certified finite impurity-energy enclosure if an actual unnormalized kernel is wanted; the lower gap bound alone does not supply its value. Positive a_A fixes the initial phase, and the real pairing evolution fixes it continuously. Cross-impurity kernels still require shared signed contractions.

## 2. One shared chain of seeds, not a chain per rational orbital

Let U collect the seven center/neighbor seeds and R0(z)=(h0-z)^-1. Every actual impurity Delta_A has range in span U. Thus

 h_A R0(z)U=U+z R0(z)U+Delta_A R0(z)U.

Let P_A,+ be the EXACT positive-band projector. Since it commutes with h_A, the space W0 spanned by P_A,+R0(z)U over any finite pole set satisfies

 h_A W0 subset W0+span(P_A,+U).                        (3)

Consequently W_m=W0+span{h_A^j P_A,+U:0<=j<m} contains h_A^j W0 for j<=m, and

 dim W_m<=dim W0+7m.                                  (4)

The actual rank may be smaller. Covariance closure or two impurities may enlarge the union further; they cannot be silently counted as a single7m increment. Chebyshev polynomials in2h_A/(6h)-I can replace powers without changing the span and are bounded on the positive spectrum. This avoids interpreting enormous monomial moments as well-conditioned coordinates.

The positive projector is essential. Applying exp(-t h_A) to merely approximately positive orbitals would amplify negative-band leakage. Raw P0 projection is insufficient. Equation(3) uses the true P_A,+ even though its numerical representation will be approximate and certified.

## 3. Positive Galerkin and an a posteriori residual

Choose an exact orthonormal isometry V onto W_m inside range P_A,+. Put A=V^dagger h_A V>=0 and R=(I-VV^dagger)h_A V. For an initial vector Vx,

 exp(-t h_A)Vx -V exp(-tA)x
 =-integral_0^t exp(-(t-s)h_A) R exp(-sA)x ds,           (5)

where the first exponential acts only in the positive invariant subspace. Thus the error is bounded by the integral of ||R exp(-sA)x||, or crudely t||R||||x||. Its finite residual matrix is exactly

 R^dagger R=V^dagger h_A² V-A².                         (6)

This identity supplies a meaningful certificate from Gram/moment intervals. It is not an assumption that the raw Gram is well conditioned. With a skew initial pairing matrix Z in the V coordinates, the pairing error is at most

 2 integral_0^t ||R exp(-sA) Z||_HS ds.                 (7)

A bound on the relevant orbitals can be much sharper than t||R||||Z||_HS. Interval uncertainty and any initial pairing truncation error must be added separately.

If a computed symmetric matrix Atilde is within eta of exact A, then Ahat=Atilde+eta I is nonnegative and differs from A by at most2eta. Contractive Duhamel comparison bounds its semigroup error by2t eta. Arbitrarily clipping an uncertified spectrum is not an alternative. Certified orthogonalization requires a strictly positive Gram pivot or a declared stall.

## 4. Explicit uniform polynomial gate at t<=100/h

For x in[0,6h], write y=2x/(6h)-1 and a=t(6h)/2<=300. On the Bernstein ellipse rho=3/2, cosh(log rho)=13/12, so

 |exp[-a(1+y)]|<=exp(a/12)<=exp25.

The degree m Chebyshev truncation therefore has uniform error

 delta_m<=6 exp25 (2/3)^(m+1)<6*3^25*(2/3)^(m+1).       (8)

At m128, the last quantity is strictly below10^-10 by an exact rational comparison saved in EXACT_BUDGET. No exponential library value is used in that check.

Because W_m contains all degree m polynomial images of W0, exact Galerkin polynomial action agrees on W0. The true and compressed semigroups on any orthonormal initial basis in W0 therefore differ in operator norm by at most2delta_m. For an initial pairing supported there, (1) then differs in HS norm by at most4delta_m||Z_A||_HS<4*10^-9. This is a truncation theorem under exact positive-band data, not an achieved total error. The added seed count is at most896 per impurity. Stationary-basis size, covariance/chiral completion, interval precision and actual dense matrix costs remain unmeasured.

For real skew pairings, the normalized Gaussian-vector differential has squared metric (1/2)Tr[(I+ZZ^T)^-1 dZ (I+Z^TZ)^-1 dZ^T], bounded by||dZ||_HS²/2. It follows by differentiating the normalized Gaussian overlap near equal arguments; the real positive-anchor frame has zero Berry connection. Integrating along the straight real-skew path gives a vector-error bound ||Delta Z||_HS/sqrt2. This conversion does not cover a separately approximated impurity vacuum or an unresolved phase/frame mismatch. Scalar logarithm errors in(2) obey |d lognorm_pair|<=||Z||_HS||dZ||_HS/2; energy error adds t|Delta E_A|.

## 5. What Gram data are actually required

The existing eight scalar values do not yet provide an exact positive-band basis. At minimum one needs interval bounds for

 W^dagger P_A,+ W, W^dagger P_A,+ h_A W, W^dagger P_A,+ h_A² W,

including the augmented seed-polynomial blocks. Here W denotes unprojected rational/seed columns. If P_A,-=P0+Q_A and Q_A has a certified finite-rank resolvent representation, these are free full/projected Grams plus finite coefficient contractions and the certified Q_A remainder. Cross terms are shared-source products, not one new bath integral per orbital. For example W^dagger Q_A W=(W^dagger Y_A) C_A (Y_A^dagger W). An S1 remainder epsilon gives entry error at most epsilon||w_i||||w_j||, which can be costly at low poles or ill-conditioned pivots.

Alternatively all seed moments can be read from the local matrix spectral measure of h_A, whose Stieltjes transform is the rank-two Woodbury update of the seven-source free Green function. The positive-energy restriction is load-bearing; unprojected moments alone do not supply it. Higher polynomial moments or stable block recurrence data must be certified before a degree128 calculation is executable. Products between the A and C positive-band bases require P_A,+P_C,+ cross contractions and a common CAR frame. They are not determined merely by separate Gram eigenvalues.

Thus(4) removes the multiplicative Krylov-chain dimension count, but does not claim that today's inputs already meet these conditioning/data requirements.

## 6. Chiral structure and a finite Cayley construction

Let Sigma be the bipartite grading. Since Sigma h0 Sigma=-h0,

 Sigma R0(z)e=-chi R0(-z)e when Sigma e=chi e.

The sum/difference of the two pole columns are exact chiral eigenvectors. Rephase them to real vectors. Gamma0 anticommutes with Sigma, so a paired pivot starting in one chiral eigenspace adds its Gamma0 partner in the other. This preserves both the reference covariance and the grading. The earlier raw-column greedy pilot did not enforce this and must not be relabeled a physical chiral-projector construction.

A Hermitian imaginary perturbation Q obeying Sigma Q Sigma=-Q gives Ptilde=P0+Q with both particle-hole and chiral complement identities. If its certified operator error from P_A,- is below1/2, spectral rounding about1/2 preserves both identities. In a reference-covariance and chiral-invariant finite subspace, the outside block remains P0. The resulting physical projector gives a real orthogonal polar block Rhat. Interval rounding and the absence of an eigenvalue at1/2 must be certified, not presumed.

For the exact R, set W=(R^T-I)/2. Equation(5) of the pair-chart proof gives ||W||<=q=sqrt(347/696)<1. The Cayley pairing is

 Z=-W sum_(n>=0)(-W)^n.

Truncating before n=N has S1 error at most(87/2)q^N/(1-q). Antisymmetrizing the truncated real matrix cannot increase its error from the exact real-skew Z. For an approximation Rhat with S1 error epsilon and ||What||<=q+epsilon/2<1, the degree N polynomial input error is at most

 (epsilon/2) sum_(n=0)^(N-1)(n+1)(q+epsilon/2)^n
 <=epsilon/[2(1-q-epsilon/2)²].                        (9)

This is an explicit finite contraction route from certified stationary projector data to pair coordinates. It does not bypass the need for chiral-preserving rounding or make the source Gram error vanish.

## Next decisive gate

A prospective implementation should first certify a small chiral/shared stationary basis and its positive-band Grams, then report actual minimum pivot and residual(6), before any long-time matrix exponential. If those data are available, the stable formulas(1)-(2), additive dimension(4), and exact polynomial bound(8) give a concrete attainable target. No such matrix job, budget or physical cost has been authorized or executed in this note.
