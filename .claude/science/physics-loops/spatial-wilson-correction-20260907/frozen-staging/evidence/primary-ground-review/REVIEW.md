# Cold review of the actual first ground coefficient

Verdict: PASS for native DERIVATION.md (full SHA in HASHES.json). My independently frozen different-tree calculation agrees exactly on Z1 and k0. This review checks the analytical coefficient interface rather than inferring it from that agreement. I read native coefficients only after freezing my own raw source/result; the chronology and different individual Taylor components are recorded in the independent comparison receipt.

## Uniform second-order kernel expansion

The prior cubic-cancellation proof controls two epsilon derivatives using the Hessian-integral formula for E(epsilon z)/epsilon². The extension by one derivative is valid: bounded fifth action derivatives give a C|z|5 bound on the third derivative of that quotient. Three derivatives of its exponential produce only fixed polynomial factors (up to degree9) times the same Gaussian lower-bound envelope. Haar and smooth cutoff derivatives through order3 are bounded on a smaller star-shaped compact chart. Taylor's theorem thus gives the stated O(epsilon³) polynomial-Gaussian remainder, uniformly on expanding scaled coordinates. Nuisance integration preserves its weighted L2 order. The compact complement and the omitted source-chart pieces remain exponentially small and therefore o(epsilon²).

The order-epsilon marginal kernel is identically zero by the separately proved two-vector f cancellation. This is stronger than its ground expectation being zero. Consequently there is no missing second-order resolvent term involving an order-epsilon operator. The common-space operator expansion really has the form K0+epsilon²K2+o(epsilon²). Simple isolated-eigenvalue perturbation gives the Rayleigh coefficient <phi,K2phi>, with eigenvector changes contributing at higher order. The beta-dependent local unitary and chart cutoff cause no extra coefficient: the source square-root Haar factors are included explicitly, and the Gaussian ground's omitted tail is exponentially small.

## Ground weighting and normalization

The ground on the eight-dimensional Lie algebra is radial exp(-omega|X|²/2). It has no Vandermonde factor in this representation; that factor belongs to a different unitarily equivalent radial chamber representation. Its two matrix-element factors add omega P_source, not2omega P_source, to the chord precision H/3. The proposed Gg is therefore correct. Literal source chords are essential to avoid additional nonlinear source-coordinate insertions.

The exponential Haar Jacobian has log(j/j0)=-sum_positive_roots alpha²/12+O(|X|4). On traceless SU3 diagonals the root-square sum is3TrX², giving- TrX²/4. Its Gaussian expectation is-2TrG. The transformed kernel divides by the square root of each source Haar density, so the half-back insertion is +(TrXu²+TrXv²)/8, whose expectation is Guu+Gvv. This yields the displayed Ng1 exactly. The partition expansion supplies subtraction of Z1, while the leading ground Gaussian integral cancels against lambda0. No unnormalized insertion or hidden source-volume factor remains.

The one-group control Z1=-1 follows from ETrX4=360 at G=3, E4=-360/72=-5 and Haar=-6. This tests the action and Haar conventions separately from the cube agreement.

## Independent algebra and gauge test

My explicit trace-orthonormal matrices give ImTr(TaTbTc) tensor norm12, equivalent to native's f' norm48 with its extra1/2. Both conventions give the same determinant Wick formula. The ordered fourth contractions64/3,-8/3,64/3 agree. My adapted tree omits a different edge from each source square and extends in reverse order; it produces different E3², E4 and Haar terms but exactly the same normalized Z1 and ground coefficient. Ground radiality and central Haar invariance make this an appropriate gauge-invariance check, not a demand that coordinate-dependent pieces match.

The exact positive coefficient is therefore supported both analytically and by the independent computation. It is a first asymptotic ground coefficient only: no specified finite-beta accuracy, first-excited/ratio coefficient, coupling selection, or infinite-volume mass gap follows from this source. No mathematical correction is requested.
