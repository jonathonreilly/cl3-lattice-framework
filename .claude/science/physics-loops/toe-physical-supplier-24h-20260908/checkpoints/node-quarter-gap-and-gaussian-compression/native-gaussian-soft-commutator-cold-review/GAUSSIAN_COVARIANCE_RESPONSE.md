# Chart-free covariance response of a real-time Gaussian unitary

New derivation for independent review, not a certified node algorithm. This avoids the generic exponential-in-volume conversion in QUANTITATIVE_FILTER.md. It concerns real-time Gaussian unitaries, not nonunitary imaginary-time products with large norms.

Let gamma_i be2m Majoranas. Let omega_0,omega_1 be even quasifree states on this finite algebra and C_ij=omega(gamma_i gamma_j) for i!=j, C_ii=0. Put epsilon=||C_1-C_0||op. Let U be an even Gaussian unitary with U*gamma_i U=sum_j R_ij gamma_j and real orthogonal R. Set D=R-I.

Claim:

 |omega_1(U)-omega_0(U)|
 <= epsilon/4 [||D||HS²+||D||1].                         (1)

Here ||.||1 is matrix trace norm, not entrywise sum. No overlap determinant inverse, nonvanishing chart, or square-root phase choice occurs.

Proof. Define graded Clifford derivatives partial_i O=(gamma_i O-(-1)^parity(O)O gamma_i)/2. The Wick expansion, differentiated along the physical covariance interpolation C_s, gives

 d/ds omega_s(O)=sum_(i<j) DeltaC_ij omega_s(partial_j partial_i O)
              =(1/2)sum_ij DeltaC_ij omega_s(partial_j partial_i O).

This can first be checked on an ordered Majorana monomial: each removed pair is precisely one differentiated Wick contraction. It then holds for every operator by linearity in the finite Clifford algebra. Covariance interpolation remains a valid quasifree covariance, although the interpolated states are not generally the linear mixture of endpoint states.

For U, gamma_i U=U gamma(R_i), so

 partial_j partial_i U
 =U[gamma(D_j)gamma(D_i)+2D_ij]/4.

Consequently the derivative is one eighth of a quadratic Majorana contraction plus a scalar contraction. The quadratic coefficient matrix is D^T DeltaC^T D, whose trace norm is <=epsilon||D||HS². For a general complex matrix M, ||sum_ab M_ab gamma_a gamma_b||<=2||M||1: apply its singular-value decomposition and ||gamma(z)||<=sqrt(2)||z||. The scalar contraction is <=2epsilon||D||1 by trace duality. Together they give (1), after integration over s. Antisymmetric covariance differences eliminate diagonal derivative terms automatically.

For a real-time local-impurity cocycle the one-particle orthogonal path has rank-two generator of norm beta, hence trace norm2beta. Unitary invariance and Duhamel give

 ||R-I||1 <=2beta |t|,  ||R-I||HS²<=2||R-I||1,

because ||R-I||op<=2. For a product of two such cocycles use |t|+|s|. Thus (1) is at most (3/2)epsilon beta(|t|+|s|), independent of the number of modes in the box. This is a potentially useful rank-two replacement for the generic2^m covariance conversion. If only entrywise covariance error eta is known on the box, epsilon<=2m eta is safe, still polynomial rather than exponential.

The bound immediately applies to the even overlap term in the Gaussian-filter node formula. The local Majorana insertion terms require extending the graded-derivative calculation to U gamma(f)gamma(g) and integrating their insertion times; that is finite-degree algebra, but its constants are not asserted here without deriving them. Likewise a quantitative finite-box covariance estimate and a practical locality radius remain necessary. Equation(1) by itself does not certify a physical integral or node value.

## Explicit two-Majorana insertion extension

For real f,g (external complex scalar phases are harmless), the same calculation yields

 |omega_1(U gamma(f)gamma(g))-omega_0(U gamma(f)gamma(g))|
 <=epsilon ||f||||g|| [1+||D||op+(||D||HS²+||D||1)/4].       (2)

To see the constants, use the graded product rule twice. The second derivative on U contributes the coefficient in(1) times ||f||||g||. Since partial_j(gamma(f)gamma(g))=f_j gamma(g)-g_j gamma(f), the two cross terms combine under antisymmetric DeltaC into a contraction bounded by epsilon||D||op||f||||g||. The second derivative on the insertion contributes f^T DeltaC g, bounded by epsilon||f||||g||. In the cross term DeltaC is purely imaginary and D,f,g are real, so the resulting Majorana coefficient vector is a common imaginary phase times a real vector: its norm is exactly its Euclidean norm, without an extra sqrt2. Thus (2) uses the actual real-time Majorana setting, not arbitrary complex insertion vectors.

For the node functional, a commutator with a Gaussian unitary is an integral of a local linear J insertion of norm j=beta/2. Each term then has two real Majoranas up to a common scalar phase. After collecting Gaussian factors into one unitary, its trace displacement is <=2beta(|s|+|t|), independently of the insertion time. Equations(1)-(2) therefore give the complete Gaussian-filter covariance error bound

 (90/8) epsilon [6beta M0 M1+(3/2)beta²(M0 M2+M1²)],         (3)

where M0=2sqrt(T)/sqrt(pi), M1=T, M2=8T^(3/2)/(3sqrt(pi)). Both commutator terms are included. For a truncated time integral, the full moments are conservative upper bounds. This is a polynomial, volume-independent conversion from covariance operator error ON THE COMMON FINITE BOX to the complete node functional's expectation error. It does not bound the covariance error itself or remove spatial truncation error. All statements in this supplemental section remain newly derived and await independent review.
