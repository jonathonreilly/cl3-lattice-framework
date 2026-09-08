# Local electric oscillator strength and finite spectral moments at RK

## Result and model scope

The same supplied spin-half ice Hamiltonian admits a positive local ring-flip estimator for the transverse first spectral moment at RK. Exact enumeration gives a numerator variance reduction of96/7 relative to a uniformly proposed single-plaquette estimator at equal independent configuration count. It requires no late imaginary-time product or descendant genealogy. The corresponding moment/Ritz construction bounds the lowest observable-supported energy from above, but does not determine a photon pole or its residue. The detuned extension requires the unknown positive ground amplitude and a pure, not mixed, sampling measure.

This is conditional physics of the current Cartesian ice source dictionary E_b(r)=(-1)^sum(r)(n_b(r)-1/2), H=V N_f-A. It does not derive that dictionary, Hamiltonian, equilibrium preparation or occupation readout from Admissibility. It is not the earlier BKSF fermion carrier. The current Cartesian source note and TARGET_REPORT explicitly leave physical electromagnetic identification, component selection, thermodynamic stiffness and static-dynamic Maxwell equality open. The corrected source's warning about a two-vector Ritz value missing a lower sector is respected here.

The finite domain is the864-state L2 component reached from n_a(r)=r_a mod2, with24 geometric plaquettes and6912 directed moves. No other component or volume is enumerated. Source and input hashes are recorded separately.

## Local source dictionary gives a positive oscillator-strength observable

Let O(q,b)=|Lambda|^(-1/2) sum_r exp(i q.r) E_b(r), with q along a and b different from a. A flippable plaquette in the ab plane changes E_b at its two ends by opposite signs. Therefore

    Delta_p O = epsilon_p exp(i q.r) [1-exp(i q_a)]/sqrt(|Lambda|),
    |Delta_p O|² = qhat_a²/|Lambda|,
    qhat_a²=4 sin²(q_a/2).

Plaquettes in the other planes make zero change for this transverse mode. This follows from the actual staggered occupation update, including the parity sign at the displaced endpoint. It is not a continuum curl approximation. The six L2 transverse modes and all41472 corresponding directed move cases independently verify this identity.

At RK, H=L=N_f-A is the symmetric move-graph Laplacian and its ground vector on the connected component is uniform. The pure configuration measure is therefore uniform. For any diagonal observable with zero ground mean, define its positive spectral measure by the normalized vector O psi0. Its first moment is

    mu1 = <O,L O>_uniform / <|O|²>_uniform
        = <d(x)>_uniform / S(q),
    d(x)=1/2 sum_flips |O(y)-O(x)|²
        = qhat_a² N_f^(ab)(x)/(2|Lambda|),
    S(q)=<|O(q,b)|²>_uniform.                         (1)

Thus a simple orientation-resolved flippability count supplies the numerator. It is a diagonal configuration observable, compatible with the supplied link-occupation dictionary; no long-time product is needed. Incremental maintenance of orientation counts is a possible implementation improvement, not implemented or cost-certified here.

For the real L2 mode, the same identity is the finite double-commutator sum rule

    <[O,[H,O]]>/2 = <O(H-E0)O>.                       (2)

The six complete finite matrices verify (2). This ties the moment to the actual ring interaction and source-induced electric update; it is not a free oscillator fit. For complex modes, the Dirichlet identity remains valid with absolute squares; equation(2) as written is used only for Hermitian O.

## Exact variance reduction, with its correct sampling meaning

At a uniform RK configuration X, choose one of M plaquettes uniformly. Set Y=(M/2)|Delta_p O|² if it is flippable, zero otherwise. Then E[Y|X]=d(X). Total variance gives

    Var(Y)=Var(d(X))+E[Var(Y|X)] >= Var(d(X)).

For independent identically distributed configurations and a known S, both sample-mean numerators are unbiased, and the variance reduction is exact. This is standard conditional-expectation variance reduction. It is not a proof of equal computational cost: summing/checking all plaquettes can cost more than one proposal. Nor does it establish mixing or MCMC asymptotic variance ordering for arbitrary correlated samplers.

For exact arithmetic we use O_integer=sqrt(32) O. On the frozen L2 component,

    mu1=8/5, mu2=16/5, spectral variance=16/25,
    Var(Y_integer)=32768/9,
    Var(d_integer)=7168/27,
    Var(Y_integer)/Var(d_integer)=96/7.

In physical O units the two numerator variances are32/9 and7/27. Here S=5/12 and <d>=2/3. If S is also estimated on the same configurations, its covariance must be retained. The independent-sample delta-method ratio influence is Y-mu1 O² versus d-mu1 O², divided by S. Its exact configuration variance is numerically25.4634667 versus6.4768, a factor3.9314888. This is the leading ratio variance for independent samples, not a finite-sample unbiasedness theorem for the nonlinear ratio. The decrease remains substantial but is smaller than96/7; ignoring the shared denominator would overstate it.

## Spectral moments, upper bounds, and held-out failures

All normalized RK moments through order8 are computed by repeated integer sparse multiplication before revealing the full eigensystem:

    (1, 8/5, 16/5, 80/9, 568/15, 2144/9,
     28592/15, 784576/45, 7890176/45).

Moment2 is the configuration mean |LO|² divided by S. It has no late-time noise, but its local integrand still fluctuates and its estimation would need uncertainty control. On this finite model the nonzero variance16/25 rigorously excludes a single exact spectral level for O psi0.

For Krylov trial space span{O,LO,...,L^(k-1)O}, the Gram and energy matrices are S_ij=mu_(i+j), B_ij=mu_(i+j+1). Rayleigh–Ritz gives an upper bound on the lowest energy in the observable's cyclic spectral support. It is not a lower bound, and not necessarily the full-component gap. The smallest Ritz values at k1,2,3 are

    1.6, 1.37998579552, 1.20926435972.

The held-out full eigensystem gives the lowest O-supported level1.16086551317, while the full-component first gap is .969623616795. The supported level has weight .704202846395. No discrepancy with the smaller full gap is hidden: the observable is blind to some sectors.

The k3 quadrature has nodes1.20926436,2.82464339,8.95154680 and weights .77102731,.22556837,.00340432. These are moment-matching Ritz/quadrature data, not measured poles. In particular the first weight .7710 is not the actual .7042 residue. Held-out moments6,7,8 differ from the exact moments by -37.6186,-1429.5334,-34068.6701. The four vectors O,LO,L²O,L³O have rank4, so the three-dimensional Krylov space has not closed. Calling the three nodes the complete spectrum fails an explicit held-out check.

A rigorous but weak contamination statement is available without the full spectrum. Graph degree gives support in[0,B], B=2 max N_f=32. With mean mu=8/5 and variance16/25, an interval [mu-r,mu+r], r1/4, can contain at most

    1 - (variance-r²)/(max(mu²,(B-mu)²)-r²)

of the spectral mass. Hence at least .000624934 lies outside that narrow interval. The exact held-out measure in fact has essentially all mass outside it. This contrast shows how weak low-order moment bounds can be; they do not identify a low pole or its weight. No fitted late-time slope enters these statements.

Equation(1) also supplies a conditional long-wavelength upper-bound mechanism: if on a specified volume family S(q) is independently bounded below and the orientation flippability density is bounded above, the variational supported energy is at most a constant times qhat²/S(q). For example a uniform positive lower bound on S gives an O(q²) upper bound. No such volume-uniform structure-factor premise is proved by this L2 calculation, and an upper bound alone supplies neither a dispersion law nor a positive pole residue. This is not a photon theorem.

## Detuned extension and a failed shortcut

For V.95 let psi>0 be the exact finite ground amplitude, E0 its energy. The ground-state-transformed local operator is

    L_psi O(x) = [(H-E0)(O psi)](x)/psi(x)
               = sum_y A_xy psi(y)/psi(x) [O(x)-O(y)].

Its measure is pi(x)=psi(x)², normalized. Consequently

    mu1=<O L_psi O>_pi/S_pi
       = [1/2 sum_xy A_xy psi(x)psi(y)|O(x)-O(y)|²]/S_pi,
    mu2=<|L_psi O|²>_pi/S_pi.

The positive local numerator uses ratios psi(y)/psi(x); these are not supplied by knowing only the local flippability count or a mixed fixed-population distribution proportional to psi. The independent full finite ground calculation gives

    mu1=1.66433305228, mu2=3.42186788633.

Replacing these by uniform RK moments gives1.6 and3.2, and even retaining the transformed operator but averaging with the mixed psi measure gives mu1=1.65676680883. Both shortcuts fail on the actual finite model. The exact psi is used here only as a held-out diagnostic import. No larger-volume ground-state ratio estimator, pure sampling procedure or new preparation is supplied.

## Evidence, preserved failures, and prior art

check.py executes17 finite assertion groups, including exact moments, variance identities and detuned-weighting controls. curl_check.py reuses that module and separately verifies41472 directed source-update cases and12 plane-count/commutator identities. Reuse is disclosed; these are not independent science implementations or independent sample counts. All commands stayed below one second of measured checker time and around104MiB RSS, below the declared bounds. Two actual mutants fail (remove Dirichlet half; substitute RK detuned moment).

The preregistered multiplicity-collapse control is non-discriminating here: every actual L2 adjacency multiplicity equals1, so collapsing them leaves this operator unchanged. It is not counted as a killed mutation. Geometric moves are still retained in the construction; a different model cannot inherit this simplification without checking.

The first output had a small exact-arithmetic reporting error in Var(Y): it converted a centered floating sum to an integer, truncating rounding noise. The original code/raw remain preserved. The repaired code computes E[Y²]-E[Y]² entirely as rational integer sums; only that variance receipt changed, from75497471/20736 to32768/9. A supplemental script initially had a syntax typo `else0`; the pre-fix source and parser error are preserved. No physical parameter or failed mathematical test was tuned away.

Variational/Krylov and conditional-variance principles are established mathematics, not new physics: Rayleigh–Ritz is derived directly above; for the relation between Krylov moments and variation see Fernández, Rayleigh–Ritz variation method and connected-moments polynomial approach, https://arxiv.org/abs/0807.1442. For conditioning see Blackwell, Conditional Expectation and Unbiased Sequential Estimation (1947), DOI10.1214/aoms/1177730497. The claimed increment is the actual staggered-electric/ring-flip numerator, its exact variance comparison and its constrained spectral interpretation on this supplied carrier.

The remaining hard obligation is a volume-capable pure-measure or ground-ratio estimator with controlled error, followed by uniform spectral information sufficient to establish a low-energy branch and weight. This result avoids a failed late-time fit for low moments; it does not establish physical electromagnetism or close that obligation.
