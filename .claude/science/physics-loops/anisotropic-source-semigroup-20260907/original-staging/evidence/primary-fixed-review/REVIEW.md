# Independent block26 review: fixed anisotropy and iterated powers

Reviewed immutable DERIVATION.md SHA8363d46a6bfc02b22a94d3959dc338c0d79254c3761a7f1d650487f814c348e1. I did not execute the author's checker or read its separate simultaneous-limit attempt. Root's graph certificate and the native distinct-tree covariance agreement are supporting inputs, not claimed as my new graph reconstruction. Six independently recalculated scalar identities are in SCALAR_CONTROLS.json. A rejected reviewer numerator typo is preserved in CONTROL_CORRECTION.md.

Verdict: mathematical PASS for the explicitly iterated, fixed-n beta-first limit. Add the source-compression composition clarification below before canonical publication. There is no proved identification with a longer physical slab.

## Oscillator normalization checked independently

For sigma_plus=30 and sigma_minus=6(4k+5)/(4k²+6k+1), r²=sigma_minus/30. The identity 1-r²=2k(10k+13)/[5(4k²+6k+1)] establishes 0<r<1 for k>0. The Gaussian exponent coefficients satisfy 4a²-b²=1/(sigma_plus sigma_minus). Thus omega=1/sqrt(sigma_plus sigma_minus) and the Mehler ratio is (1-r)/(1+r). At k=1 this gives omega=sqrt55/90 and the earlier theta.

The eight-dimensional coordinate Jacobian for w=sqrt(omega)X is dX=omega^-4 dw. Therefore D_omega f=omega^-2 f(w/sqrt(omega)) is unitary, with precisely the exponent in the source. The transformed ground is exp(-|w|²/2). Hermite degree m has normalized eigenvalue theta^m. The compact conjugation action commutes with the oscillator and Hermite decomposition, so restricting to its invariant subspace gives exp(-t_k N), N=(-Delta+|w|²-8)/2, without changing eigenvalues or inserting a Weyl factor. The invariant polynomial degrees 2a+3b include the odd cubic mode; no even-only restriction is made.

## Actual powers and order of limits

Let B_beta=A_beta/||A_beta|| and C_beta=P B_beta P. Both have norm at most one. The off-chart bound from the structural parent, divided by a norm asymptotic with positive leading coefficient, gives ||B_beta-C_beta||->0 exponentially for fixed k. The telescoping product identity needs no commutation and bounds ||B_beta^n-C_beta^n|| by n||B_beta-C_beta|| for every fixed n. Since U_beta*U_beta=P, the conjugated C_beta power equals the power of its conjugated compression exactly. This makes the theorem about genuine powers of the finite source operator rather than insertion of an uncontrolled additional chart projection.

After applying D_omega, for each fixed n the beta limit is exp(-n t_k N). Now choose k_n=4n²/(5t²). The exact covariance gives k r_k²->1/5, so n*2artanh(r_k_n)->t. For a_n=n t_k_n and every nonnegative spectral value m, the mean-value theorem bounds |exp(-a_n m)-exp(-tm)| by |a_n-t| m exp(-min(a_n,t)m), whose supremum is |a_n-t|/[e min(a_n,t)]. The number operator has nonnegative spectrum, so this proves the asserted outer operator-norm convergence. No estimate uniform in n is needed in this iterated order. It supplies no simultaneous sequence beta_n, rate, or interchange of limits.

## OU invariant generator and domain

Direct differentiation of h=const exp(-|w|²/2) gives -h^-1Nh=(1/2)Delta-w.grad. For q=TrW² and c=TrW³, orthogonal projection onto traceless matrices gives grad c=3(W²-qI/3), while grad q=2W. Therefore gradq.gradc=6c, |gradc|²=9(TrW4-q²/3)=3q²/2, and Delta c=0 by invariance (there is no nonzero invariant linear polynomial). Also Delta q=16 and |gradq|²=4q. The chain rule then gives exactly

    2q Fqq+6c Fqc+(3q²/4)Fcc+(8-2q)Fq-3c Fc.

The mixed coefficient is 6c, not3c or12c. The traceless characteristic identity TrW4=q²/2 and discriminant q³/6-c²=Delta(eigenvalues)²/3 check exactly. The operator is the restriction of the full eight-dimensional ground-transformed process on invariant L2(h²dw). Finite invariant Hermite sums (equivalently invariant polynomials, with the Gaussian measure) form a core through spectral truncation. This construction fixes the quotient boundary behavior; the displayed differential expression alone is not used to select a boundary extension at the discriminant cusp.

## Required composition-scope clarification

The phrase 'actual normalized n-step operator' is mathematically correct only when it denotes powers of the already compressed source operator A. In general, if A=I*TI for a source embedding I, then A²=I*T(II*)TI, whereas the source compression of a two-step full transfer is I*T²I. They agree only with an additional invariance/intertwining premise. No such premise is proved here. Insert this explicit distinction in the source: repeated source compression/reset composition is supplied, and the operator-power theorem does not identify the compression of a longer full slab, physical elapsed time, a formation clock, or full slab dynamics. The existing final paragraph excludes physical time but does not yet state this load-bearing distinction.

No other mathematical correction is required for the frozen iterated theorem. This review does not approve the unreviewed simultaneous-limit extension.
