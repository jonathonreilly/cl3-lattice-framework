# Finite-excitation Ward synthesis: independent review pending scalar correction

The principal-angle/Fock, unnormalized propagation and raw-rank Ward parts are sound under the declared actual CAR premises. The initial scalar sourcee6779882 has an underexplained regularized-absolute-value endpoint passage: uniform operator convergence is not by itself trace-norm convergence. Root and author are correcting that step. No unconditional synthesis PASS is issued on those original bytes. Initial source hashes are retained separately.

## Fock multiplicities, phase and domains

A paired Bogoliubov block uses two reference fermion modes and four doubled one-particle singular directions, all of projector-difference singular value sin(theta). Its mean excitation count is2sin²(theta), and squared HS projector difference4sin²(theta). An exceptional occupied mode contributes one particle and two singular values1. Thus<N>=||P-Q||HS²/2, as stated. The local skew pairing matrix, rather than independent one-mode rotations, gives the correct physical multiplicity.

The infinite ordered product converges because the omitted squared sines are summable. Choosing the cosine factors nonnegative fixes approximation phases relative to the original state; it does not assume a nonzero overlap with the impurity vacuum. All finitely many exchanged modes must be retained. Norm-continuity of the physical projection path and local paired charts preserve relative parity; no claim based solely on a complex Fredholm index is needed.

The count distribution is a finite integer plus twice independent Bernoulli variables of summable means. Its variance and second moment are finite, hence the vacuum lies in Dom N, not merely in the quadratic-form domain of N. Bounded one-particle dispersion then puts it in Dom H0. The bounded physical impurity does not change that domain. The polarization map can be extended from its vacuum to a unitary between Fock spaces by applying the new CAR creation operators: irreducibility makes their cyclic span the whole representation. The scalar-generator comparison is therefore legitimate once the scalar itself is identified correctly.

## Raw rank to finite excitation

A rank-k nuclear approximation implies the singular tail after k is at most eta. Within degeneracies one may choose canonical particle-hole blocks first. Completing the one final intersected block adds at most three singular directions. All value1 exceptions are included when eta<1. Hence the carrier has at most k+3 doubled directions and floor((k+3)/2) fermion modes. This is an existence statement about the true principal vectors, not the singular vectors of the raw approximate Q.

The omitted paired angles have4sum sin(theta)<=eta. The weaker bound used by the source, sum sin²(theta)<=eta², is safe and gives Fock error<=sqrt2 eta. Discarded pairs have even parity. This does not claim a cheap extraction of the exact principal angles.

## All Ward sources and propagation

Exact positive impurity evolution contracts the unnormalized error by exp(-delta t). The left-boundary source is W_C Omega and the right-boundary source W_A Omega; each is approximated by applying the same bounded W to the appropriate approximated original vacuum before propagation. They are not dropped or commuted through the evolution. A linear CAR field applied to a finite carrier adds at most one new creation orbital; its annihilation part acts inside the retained carrier.

Telescoping the two propagated vectors yields the stated per-word coefficient delta^-2[3+(||WA-WC||+||WA||+||WC||)/2](epsilon_A+epsilon_C). Thus the complete coefficient with||W||<=4.6 is correct. The normalized-quench counterexample correctly explains why no norm-independent normalized-state guarantee follows.

The rank2352 example supplies Fock-state error<8.1e-7, NOT alpha error<1e-6. At delta1/4, a safe total alpha state-error coefficient is6588 times raw eta, using sqrt2<=3/2. A raw eta<=1/(6588*10^6) suffices for a1e-6 state-compression contribution. The same explicit rank construction with Jlo39,Jhi36,p17 gives rank<=5100. Exact arithmetic is in WARD_BUDGET.json. None of these are total numerical-error or runtime certificates.

## Direct alternative justification for the relative trace

For bounded hA,h0 with finite-rank difference, the norm-convergent functional calculus identity gives

 |hA|-|h0|=(2/pi)integral_0^infinity s²[(h0²+s²)^-1-(hA²+s²)^-1]ds.

The integrand is trace-norm integrable: near zero its norm is <=s C0 by expressing the squared resolvents through their +/-is differences and the supplied uniform local-column bound; at infinity the resolvent identity with trace-class hA²-h0² bounds it by||hA²-h0²||1/s². Thus trace may be taken under this integral without invoking operator-Lipschitzness of absolute value.

For the actual self-dual determinant d(s), its logarithmic derivative is s times the trace of the squared-resolvent difference in the opposite order. Hence the trace integral is-(2/pi)integral s (log d)' ds. Integration by parts, using bounded log d near zero and O(s^-2) or better at infinity, gives(2/pi)integral log d. Combined with the independently justified normal-ordering formula c=-Tr(|hA|-|h0|)/4, this identifies the actual scalar. This is a possible repair; the final author source will be reviewed before issuing a synthesis verdict.
