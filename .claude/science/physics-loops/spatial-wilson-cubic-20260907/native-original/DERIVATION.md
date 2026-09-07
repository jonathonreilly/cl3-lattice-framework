# Vanishing first odd correction of the actual two-source cube marginal

This is a separate extension of structural proof SHA86be606d, under preregistration SHA364fdb27. It keeps its supplied action, adapted literal-source coordinates and central embedding. Constants below are finite but unspecified. No finite-beta accuracy at beta=6 is asserted.

## 1. Actual cubic color structure

Write each chord U_e=exp(i X_e), with Hermitian traceless X_e, and expand the real trace of each ordered plaquette word. Linear terms vanish. The cubic terms from one exponential or from a twice-repeated factor have real traces before multiplication by i^3 and hence give zero real contribution. For three distinct factors, Re(i^3 Tr ABC)=Im Tr ABC=Tr(A[B,C])/(2i). Thus every cubic term is a real multiple of the alternating invariant tensor f_abc contracted against three edge-color coordinates. Signs from inverse edges and ordering change coefficients only. There is no symmetric d_abc term in the real action. This argument also applies directly to any plaquette word in the adapted tree, where tree factors are identities.

Consequently, in the 136 real adapted coordinates z,

    E(epsilon z)/epsilon^2 = Q2(z) + epsilon E3(z) + O(epsilon^2 |z|^4),
    Q2(z)=(1/6) sum_color z_color^T H z_color,
    E3(z)=sum_edge_triples c_efg f_abc z_ea z_fb z_gc.

Normalized Haar in exponential coordinates is even under X -> -X by Haar inversion invariance, so its density has no linear term. Product Haar has the same property.

## 2. Conditional Gaussian cancellation

The two sources are literal chord variables (possibly with a fixed inverse sign), not nonlinear functions of nuisance chords. Condition the centered Gaussian exp(-Q2) on these two source vectors X,Y. For every nuisance edge e its conditional mean is m_e=A_e X+B_e Y, and every conditional covariance has the form C_ef delta_ab. The same statement includes deterministic source edges with zero conditional covariance.

Wick's formula for a cubic monomial gives a product of three means plus three mean-covariance contractions. Contracting the first with f gives f(m_e,m_f,m_g)=0 because all three means lie in span{X,Y}. Each remaining contraction contains f_abc delta_ab (or an index permutation), hence vanishes. Therefore

    E_Gaussian[E3 | X,Y] = 0

identically for all X,Y. The unconditioned cubic integral also vanishes, either by this identity or by oddness. This is specific to at most two independently fixed Lie-algebra source vectors; it is not asserted for three or more sources.

## 3. Uniform weighted remainder, not just formal expansion

Choose nested compact-closure exponential charts as in the structural proof, and a smooth cutoff chi equal to one on the smaller full 17-group chart and supported inside a chart where E(w)>=c|w|^2. Set epsilon=beta^-1/2. On scaled coordinates define

    F_epsilon(z)=chi(epsilon z) exp[-E(epsilon z)/epsilon^2] J(epsilon z),

where J is the product local Haar density. Extend by zero outside the support. At epsilon=0 the expression is exp(-Q2(z)) j0^17. Smoothness and the Taylor formula for E at its critical point give, uniformly when epsilon z lies in this compact chart,

    |partial_epsilon [E(epsilon z)/epsilon^2]| <= C |z|^3,
    |partial_epsilon^2 [E(epsilon z)/epsilon^2]| <= C |z|^4.

These bounds follow by writing E(w)=integral_0^1 (1-t) D^2E(tw)[w,w] dt and differentiating; bounded third/fourth derivatives suffice. Derivatives of J and chi add fixed polynomial factors in |z|. The same quadratic lower bound holds at every intermediate parameter between zero and epsilon. Thus for a fixed polynomial P,

    |partial_epsilon^2 F_epsilon(z)| <= C P(|z|) exp(-c' |z|^2).

Derivatives of the cutoff are supported in its chart annulus and satisfy the same estimate. Taylor's theorem yields the integrable pointwise bound

    |F_epsilon-F_0+epsilon j0^17 E3 exp(-Q2)|
       <= C epsilon^2 P(|z|) exp(-c' |z|^2).

Integration over 120 nuisance coordinates gives a polynomial times a Gaussian in the 16 source coordinates. The linear term vanishes identically by Section2. The normalized partition integral has nonzero constant term and zero linear term, so division preserves the O(epsilon^2) weighted remainder.

Removing the cutoff costs exponentially small terms: on the compact excluded part E has a positive gap. Uniform source-fiber bounds multiply this by at most beta^68 before normalization, or beta^60 in scaled marginal coordinates. For sources still in the chart these terms can be absorbed into a weaker source Gaussian exactly as in the structural proof; outside the source chart the squared density integral remains polynomial times exp(-c beta). Neither weak convergence alone nor a probability-tail estimate is used to infer a kernel bound.

Accordingly, if p_beta is the normalized scaled two-source Lebesgue density and g is its limiting Gaussian, then on the expanding source chart

    |p_beta(X,Y)-g(X,Y)| <= C beta^-1 P(|X|+|Y|) exp[-c(|X|^2+|Y|^2)]

up to exponentially small terms with the same weaker Gaussian envelope. In particular its L1 and L2 errors are O(beta^-1). This is an asymptotic bound with finite model-dependent constants, not an explicit numerical certificate.

## 4. Central operator and fixed spectral consequences

The dilated kernel of beta^-4 A_beta is the central average of p_beta divided by sqrt(j(X/sqrt(beta))j(Y/sqrt(beta))). Haar evenness makes this denominator j0+O(beta^-1(|X|^2+|Y|^2)) in the fixed chart; its derivatives and reciprocal are bounded there. Angular averaging contracts L2 and preserves radial Gaussian envelopes. The off-chart operator is exponentially small in Hilbert-Schmidt norm by the prior structural proof. Therefore the actual central operator, extended on the common Lie-algebra space as specified there, satisfies

    || beta^-4 U_beta P A_beta P U_beta^* - K_infinity ||_HS = O(beta^-1),
    beta^-4 ||A_beta-P A_beta P||_HS = O(exp(-c beta) beta^m).

The shrinking chart complements in the limiting Gaussian also have exponential tails. Compact self-adjoint eigenvalue perturbation then gives each fixed isolated nonzero eigenvalue with absolute error O(beta^-1) after scaling. In particular, since the reviewed Gaussian ground and first central branch are simple and lambda0>0,

    lambda_1(A_beta)/lambda_0(A_beta) = theta^2 + O(beta^-1).

The implied constants and onset are not supplied. This does not determine the beta^-1 coefficient or its sign. Computing that coefficient would require the conditional expectation of E3^2/2-E4 plus the quadratic Haar term and partition normalization; none is replaced by a Gaussian proxy here.
