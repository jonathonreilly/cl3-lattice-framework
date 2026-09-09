# Independent Gaussian covariance-response review

Disposition: PASS for the current complete source, including two insertions and the Gaussian-filter node bound. Source SHA256 42f75a307d76a6eb9dda29472ee46cfbf41247a5e4b99b2a0c355793f28298e3. No physical simulation or Gaussian numerical kernel was run. I derived the insertion estimate independently before reading its added section, and it agrees.

## Wick differentiation and physical interpolation

The off-diagonal matrix C is purely imaginary antisymmetric, hence Hermitian, and I+C is the ordinary Majorana two-point matrix. Physical finite even quasifree covariances form a convex set (equivalently their real antisymmetric covariance has singular values at most1). Each linear covariance interpolation therefore defines a valid quasifree state, although not the convex mixture of endpoint density matrices. No pure-state interpolation is assumed.

With the stated Clifford derivative, partial_j partial_i(gamma_i gamma_j)=1 for i<j. More generally its removal signs match differentiation of every Wick pairing. Distinct ordered monomials span the finite Clifford algebra, proving the derivative identity for arbitrary U by linearity. There is no unproved operator expansion convergence in finite dimension.

For gamma_i U=U gamma(R_i), direct graded multiplication gives partial_j partial_i U=U[gamma(D_j)gamma(D_i)+2D_ij]/4. With the factor1/2 converting i<j to the full antisymmetric sum, the quadratic coefficient has factor1/8 and the scalar has factor1/4. Schatten inequalities give ||D^T DeltaC^T D||_trace <=epsilon||D||HS². The general complex-Majorana bound supplies the factor2 for its quadratic operator; trace duality handles the scalar. This reproduces equation(1), including its trace-norm rather than entrywise-norm convention.

The orthogonal cocycle displacement has trace norm at most the time integral of the rank-two generator trace norm, namely2beta times duration. Its Hilbert–Schmidt square is at most2 times its trace norm. The resulting(3/2)epsilon beta duration bound is correct. Box size enters only through a separately supplied covariance operator error.

## Two insertions and complete time integral

For B=gamma(f)gamma(g), the graded product rule produces four terms:
partial_j partial_i U B - partial_i U partial_j B + partial_j U partial_i B + U partial_j partial_i B.
After antisymmetric contraction the cross terms are
-U[gamma(D^T DeltaC f)gamma(g)-gamma(D^T DeltaC g)gamma(f)]/2.
Because DeltaC is purely imaginary and D,f,g real, each new coefficient is a scalar i times a real vector. Its CAR norm is its Euclidean norm; applying the generic sqrt2 bound here would be unnecessarily loose. The cross norm is at most epsilon||D||op||f||||g||. The derivative on B alone is f^T DeltaC g, bounded by epsilon||f||||g||. Together with equation(1), this proves equation(2). A reversed placement of the two insertions is reduced to this one by the real orthogonal conjugation, preserving their norms.

For total duration l=|t|+|s|, the overlap error is at most(3/2)epsilon beta l. The two soft-commutator insertion integrals have combined measure-weighted norm at most j l=(beta/2)l. Each insertion expectation error is at most epsilon[3+(3/2)beta l], using ||D||op<=2. Their sum is therefore bounded by epsilon[3beta l+(3/4)beta²l²]. Integrating against |w(t)w(s)| gives precisely equation(3), since integral l=2M0M1 and integral l²=2M0M2+2M1². The stated erfc Gaussian-filter absolute moments are correct. This step assumes the already supplied finite-soft-limit commutator representation, not an unbounded zero-mode operator.

## Independent control and limits

check.py implements a separate exact Fraction Clifford algebra on four Majoranas. It verifies the second derivative of a nontrivial rational Gaussian plane unitary for all16 index pairs, and the Wick derivative identity for all16 monomials plus three Gaussian/insertion operators along a physical covariance interpolation with rotated endpoint. All36 predicates pass. These are exact algebra controls, not physical data or the proof of a dimension-uniform estimate.

No correction requested. The result is chart-free and polynomial for real-time Gaussian unitaries and their two real-Majorana insertions. It is not automatically a bound for nonunitary imaginary-time products, arbitrary complex insertion vectors with the same constants, or mismatched finite/infinite operators. A common finite CAR subspace, covariance operator error, and separate evolution/locality errors remain mandatory. In the proposed cyclic compression, the correct state is the restricted infinite mixed covariance; substituting sign(K_m) would invalidate this application.
