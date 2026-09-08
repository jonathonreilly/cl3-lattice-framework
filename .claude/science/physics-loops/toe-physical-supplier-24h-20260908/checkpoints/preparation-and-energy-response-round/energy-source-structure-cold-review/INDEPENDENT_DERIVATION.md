# Independent derivation before author code exposure

For each of six ordered transverse pairs(a,b), a!=b, O_ab=Volume^(-1/2) sum_r epsilon(r) exp(i q r_a)(n_b(r)-1/2). The diagonal bound |O_ab|<=sqrt(Volume)/2 gives0<=X=sum|O_ab|²<=3Volume/2. It requires the same Fourier normalization and six channels; it does not presume independent modes. H=V Nf−A+lambda X has off-diagonal −1 per geometric flippable face (summed if endpoints coincide). Put M=3Volume, Lambda=|lambda|3Volume/2 and b=1+[(1−V)nf+Lambda−lambda X]/M. For V<=1, b>=1.

One offspring's transition proposes a uniform geometric face and flips only if flippable and accepted with probability1/b. Thus bP(y|x)=multiplicity(x,y)/M off diagonal, and diagonal b−nf/M=1−Vnf/M+(Lambda−lambda X)/M. Therefore bP=I−(H−Lambda I)/M exactly. Null proposals and rejected flippable proposals both stay put. This needs branch acceptance1/b, not b, and all geometric multiplicities. Positive entries alone do not prove a finite-population estimator unbiased. On a connected finite component Perron positivity identifies the lowest-energy vector; population replacement and finite projection time still require separate checks.

The shifted eigenenergy E'=E−Lambda must be restored as E=E'+Lambda at EACH source value before differentiation. Lambda has a cusp at0; a symmetric first difference of the exact symmetric Lambda cancels, but relying on that accident obscures one-sided derivatives and energy baselines. Mixed local energy may directly use the original H; otherwise explicitly restore Lambda. Differentiation applies to a simple branch within the declared component, not an unverified switch between components.

For a ground vector and each channel, the exact Dirichlet first numerator is qhat²<A_plane>/(2Volume). This remains true under diagonal lambda X since diagonal potentials commute with O. Six channels count each of three planes twice, so the ratio of SUMMED numerators to SUMMED raw weights is

  mu_sum=qhat²<A>/(Volume<X>)
        =qhat²[V E_V+lambda E_lambda−E]/(Volume E_lambda).

At lambda=0 this reduces to the proposed expression. All six momenta must have the same qhat². This is a weight-averaged moment, not the arithmetic mean of six individual normalized moments. E_lambda=<X> is a pure-state expectation by Hellmann–Feynman; it does not require forward walking as a mathematical identity. An energy estimator has its own stochastic bias and source-response errors.

If <O> is nonzero, <|O|²> includes elastic ground-state weight. The formula remains the first moment of that raw spectral measure, whose support includes zero. It is then not an upper bound for the first strictly positive excitation. To infer a connected spectral centroid use sum(<|O|²>−|<O>|²), requiring independent mean information or a proved symmetry in the actual sampled component. Cubic/translation symmetry of the full Hamiltonian alone does not prove the chosen component carries all those symmetries.

Central finite differences incur O(h²) truncation on a smooth simple branch; derivative noise scales roughly1/h and finite-population biases need not cancel. A ratio with E_lambda in the denominator adds ratio bias and covariance requirements. Use matched-source covariance if common random numbers are introduced, not independent-error formulas by default. L2 exact agreement can validate operator/source conventions but cannot establish larger-L projector population convergence.
