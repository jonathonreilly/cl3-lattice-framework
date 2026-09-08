# RK inverse moment from actual Markov correlations and geometric lags

This is an independent finite-component route after reading the orbital infrared-discriminator report. Its RK comparison value was exposed before our calculation and is not a fit. The elementary Markov kernel and six-source dictionary are reconstructed from actual binary plaquettes here. No tilted kernel or linear-source implementation is reused or changed.

## Exact elementary-time identity

On the declared connected RK component, H=Nf-A and P=I-H/M, M=3Vol. P is exactly the uniform geometric face proposal, flipping every flippable face and otherwise staying. It is symmetric stochastic, with stationary uniform component law. The parity seed has Nf=M/2, hence P(seed,seed)=1/2. Connectivity and this self-loop make the finite chain irreducible and aperiodic. Thus its nonconstant eigenvalues p lie strictly between-1 and1; one must NOT infer that they are all nonnegative from entrywise positivity.

For centered diagonal Hermitian channels F_j, or equivalently real and imaginary parts of complex O, set S=sum_j <F_j²> and C_k=sum_j <F_j,P^k F_j> in the uniform inner product. For the translation-invariant seed component the separately reviewed constructive symmetry proof makes these source means exactly zero, including qpi. Otherwise centering is a separate premise. The positive normalized spectral measure nu of H gives C_k/S=integral(1-omega/M)^k dnu(omega). Finite aperiodicity permits summation:

 m_-1 = integral omega^(-1)dnu = [1/(M S)] sum_(k=0)^infinity C_k.

If tau_int means1/2+sum_(k>=1) C_k/C_0, then m_-1=(tau_int+1/2)/M. If the convention instead uses tau_two=1+2sum_(k>=1)rho_k, then m_-1=(tau_two+1)/(2M). Omitting the extra equal-time half is an actual finite-step error. These formulas use elementary proposals, not one sweep as a unit-time continuous semigroup.

Negative p can make individual odd-lag correlations signed. Truncating an elementary sum is not automatically a lower bound without a spectral-sign premise. For each fixed finite component the infinite sum converges, but that fact supplies no usable uniform lag cutoff or stochastic error bound.

## Why sweep sampling is not the same inverse moment

One sweep is Q=P^M. Its normalized lag sum is

 I_sweep=integral [1-(1-omega/M)^M]^(-1)dnu,

not integral1/omega. Even replacing P^M by exp(-H) leaves a discrete quadrature correction; continuous time is not produced by renaming a sweep. When p lies in[0,1), let S_M(p)=1+p+...+p^(M-1). Since S_M<=M and [M-(M-1)p]S_M=M+sum_(k=1)^(M-1)p^k-(M-1)p^M>=M,

 0 <= 1/(1-p^M)-1/[M(1-p)] <= (M-1)/M.

Hence m_-1 belongs to[I_sweep-(M-1)/M,I_sweep] under that extra spectral premise and with the COMPLETE sweep sum. This is generally a broad interval. Finite sampled lags leave an additional unresolved tail.

For even M, p and-p give identical sweep eigenvalues. The two-state symmetric stochastic kernels with nonconstant eigenvalues+.5 and-.5 illustrate exact aliasing: at M24 all sweep correlations coincide, but inverse energies are1/12 and1/36. This is an abstract Markov counterexample to inference from sweep data alone, not an assertion that both measures occur in the ice component. The actual L2 calculation has minimum p=.1425063>0; no unproved extension of that fact to L4 is made.

## A bounded resolvent target from random elementary time

Choose alpha>0, q=M/(M+alpha), and independent K with P(K=k)=(1-q)q^k, k>=0. For a stationary origin X_0, evolve the ACTUAL P for K proposals. Then

 r_alpha := integral1/(omega+alpha)dnu
          = E[sum_j F_j(X_0)F_j(X_K)]/(alpha S).

This follows because (H+alpha)^(-1)=(M+alpha)^(-1)sum q^kP^k and1-q=alpha/(M+alpha). For complex channels the real product sum is Re sum conjugate(O_j(X_0))O_j(X_K), including both Cartesian components, not a real-part square or complex absolute product. Expected elementary cost is E K=M/alpha, or1/alpha sweeps. No source-energy finite difference or forward descendant measure enters this RK identity. Uniform stationarity on the chosen component is the remaining sampling premise.

Unbounded K is incompatible with a strict deterministic runtime limit. Instead retain zero contribution when K>Kmax, preserving its probability mass as zero rather than resampling a shorter K. This is an unbiased estimator of the TRUNCATED resolvent numerator, not of the full target. By stationarity and Cauchy–Schwarz |C_k|<=S, the normalized absolute tail is at most q^(Kmax+1)/alpha. Set Kmax=ceil(log(alpha epsilon)/log q)-1 for epsilon=.001. The deterministic tail statement does not require a spectral gap or positive p. Finite-chain ratio uncertainty and stationarity error remain separate.

The regularizer is not an innocuous numerical step: r_alpha increases to m_-1 as alpha decreases to0, but a finite alpha supplies no upper bound on m_-1 without controlling a weak soft tail. Even perfect r_alpha cannot automatically resolve that tail. Nonetheless exact r_alpha gives the supported-energy upper bound Delta_supported<=1/r_alpha-alpha, by monotonicity of1/(omega+alpha). It gives no lower gap or pole. No uncontrolled stochastic estimate is promoted to that rigorous bound.

## Independent actual L2 check

check.py independently builds864 states and6912 directed geometric moves, six sources and H. A full floating eigensystem and a separate constrained linear solve (H+Pi_constant)u=F agree on m_-1; no earlier saved graph or target is imported.21 named checks pass in.135seconds/89.36MiB. Raw energies/weights are retained; this is not interval certification.

S=2.5, m1=1.6, m_-1=.7225489282737988, reciprocal1.383989320126796. The full H maximum20.57984797 is below M24 for this fixture. The complete sweep sum is1.33011974697, exceeding the actual inverse moment by.60757081869. Even the common sweep trapezoid subtraction1/2 would give.83011974697, still wrong. The elementary sum through lag256 gives.72254715288, with actual floating error-1.77539e-6; this finite-fixture success is not an L4 lag guarantee.

|alpha|r_alpha|difference from m_-1|mean proposal count|Kmax|rigorous stationary normalized truncation bound|
|---|---|---|---|---|---|
|.25|.6045545920|-.1179943363|96|800|.00099348|
|.5|.5206792479|-.2018696804|48|368|.00099241|
|1|.4088385924|-.3137103358|24|169|.00096852|

The regularization error is much larger than the selected tail bound. It must remain visible rather than being renamed an inverse moment. Exact finite geometric sums agree with the resolvent formula; direct repeated P application checks all fixed elementary lags0,1,4,16,64,256. The wrong-sweep and alias examples are explicit adverse algebraic controls, not purported native source mutants.

## Comparison with curvature and remaining obligation

Linear-source curvature gives the same unregularized static susceptibility at RK, but a second difference amplifies energy noise by source_step^(-2). The random-lag product instead has an explicit1/alpha normalization and expected path length1/alpha sweeps. Neither observation alone proves a lower total variance or useful inverse-moment precision. Endpoint products may be signed; small alpha raises both cost and stochastic variance, and the regulator-to-zero tail remains unbounded without further information. Russian-roulette infinite sums could be unbiased only with an appropriate integrability/variance analysis; they are not silently used under a hard cap.

A useful next pilot therefore estimates the three DECLARED regularized targets, calibrates at L2, and compares their cost/uncertainty with the pending curvature method. It does not claim to have retired the zero-regulator spectral tail. The proposal is separate; no L4 micro or production has run.
