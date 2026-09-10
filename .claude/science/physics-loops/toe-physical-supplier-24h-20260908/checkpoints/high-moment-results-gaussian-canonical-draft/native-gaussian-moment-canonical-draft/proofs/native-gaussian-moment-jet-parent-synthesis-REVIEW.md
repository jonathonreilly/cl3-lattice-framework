# Parent synthesis: native Gaussian moment jets

Source-only conditional PASS of the finite determinant identity, James's infinite-volume bridge, and Zeno's degree-filtered scalar table. No new native scalar or moment was evaluated. This is a source theorem under the supplied canonical Gaussian model, not an axiom selection or a numerical certificate.

## Native no-zero-atom hypothesis is grounded

The copied canonical dispersion note at commit aea1602ec35a045e5b06be563acef0c28dadcbd4 gives K=-2t sum D_a, D_a=eta_a(T_a-T_a*), eta_a(r)=(-1)^(sum_(b<a)r_b), with pairwise anticommuting D_a and D_a²=T_a²+(T_a*)²-2I. These identities extend directly to the infinite lattice on finitely supported functions and then by boundedness. Set h=2|t| and h0=iK/h in dimensionless units. Its square is sum_a(2I-T_a²-T_a*²), whose full-lattice Fourier multiplier is 4 sum sin²(k_a). This multiplier vanishes at finitely many torus points, a Haar-null set. If h0 f=0 then its square annihilates f; Fourier transformation forces f=0 in L2. No spectral gap follows. In magnetic-cell coordinates theta=2k the same multiplier is 6-2 sum cos(theta_a), as used by the scalar integral suppliers. The single-origin statement in those reduced coordinates must not be read as a single zero in the unfolded site Brillouin zone.

The copied thermodynamic note supplies the same canonical pure quasifree state and its positive normal-ordered GNS generator. This state and Hamiltonian remain supplied. Its uniform wrong-pair lower bound is unnecessary for the determinant identity itself; a later inverse certificate will need that separate imported inequality.

## Infinite bridge review

James's finite compression construction is sufficient. Uniformly bounded strong convergence of h_L to h0 and absence of a zero spectral atom yield strong convergence of spectral signs, by continuous approximation to sign on each vector's spectral measure. The possible finite zero eigenspaces vanish strongly. Even real-skew matrices have even nullity, so pure conjugation-paired half-fillings exist there; their choice changes the covariance only on a strongly vanishing subspace. This is not an assumption that finite compressions have a gap.

The bounded CAR interaction-picture field has a norm-convergent Dyson series locally uniformly in complex time. Its finite-volume expectations converge coefficientwise and locally uniformly using strong convergence of the one-particle vectors and covariance, with the uniform Dyson bound. For nonnegative real time the bounded perturbation identity identifies the expectation with exp[-t(H0+B)] on the vacuum; bounded iterated local commutators also establish the required power domains. This justifies interpreting the derivatives as actual native moments, rather than derivatives of a merely formal determinant.

Duhamel writes the one-particle relative exponential minus identity as an integral with one finite-rank V. Strong convergence of uniformly bounded exponentials becomes trace-norm convergence after multiplying V, uniformly on compact time sets. Multiplication by the bounded strongly convergent covariances preserves this trace-norm convergence. Continuity of the Fredholm determinant then transfers the squared finite identity. The branch at Z(0)=1 fixes the analytic germ; no global square-root choice across complex zeros is claimed. The factor two in V, half-log, and vacuum scalar subtraction remain essential.

## Degree and sign review

For n>=2, the part of U_n linear in V is -ad_h0^(n-1)(V)/n!, and its trace against P vanishes since [P,h0]=0. All other terms in the log coefficient have at least two V factors. Thus the total free h0 degree is at most n-2. Splitting each cyclic trace at V=F J F*, J=2i[[0,1],[-1,0]], leaves only ordinary or projected 2x2 moments with segment power at most n-2. This analytic deletion must happen before interval evaluation or input acquisition; numerical cancellation of high powers would not suffice.

Zeno's D_j and B_j tables have the consistent negative-band signs. In particular B0[a,d]=+ic/2 and Tr(PV)=2c, while the ordered Majorana contraction is -ic. Confusing these conventions reverses the mean. The O-pair spectral measure introduces two extra absolute powers; through m10 the sufficient new odd inputs are omega7 and omega9, with ordinary even moments through absolute degree10. The accepted omega5 supplier already contains dispersion moments E[X^3] through E[X^43], so its saved E[X^4] and E[X^5] can supply the absolute eighth and tenth moments without recomputing them. Different moment index conventions must be explicit in a future binding.

## Remaining numerical obligations

The finite parent synthetic tests (26 exact checks through order7), independent bridge tests (27), and degree-table controls (33) support separate source claims; they are not native evaluations. No proposed runtime has yet earned a cost or precision result. A source-reviewed implementation must enforce the total-degree cancellation, bound coefficient and interval growth, authenticate the new omega7/omega9 suppliers and inherited lower moments, and avoid replaying old native moments as comparison targets. The conditional infinite theorem is now adequate for designing that protocol. Actual higher moments, stronger trial states, alpha's sign, and physical model selection remain open.
