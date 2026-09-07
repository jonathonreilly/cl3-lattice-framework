# Separately derived structural consequences and top-Perron comparison

Use the notation and proved domains of DERIVED_EXTENSION.md. Let S=S_(1/2) on the Dirichlet chamber C, T0=S M_W S, f=Q(Q-7)W/4, and D=S M_f S. These consequences do not revise the original Omega preregistration and do not assert a full heat-side expansion.

## Indefiniteness and nonproportionality

The self-adjoint Dirichlet generator L has spectrum in(-infinity,0]. Spectral calculus gives S=exp(L/2) self-adjoint and injective, since exp(lambda/2)>0 at every finite spectral value. Consequently Ran(S) is dense: its orthogonal complement is ker(S*)=0. Boundedness, not invertibility with a bounded inverse, is used below.

W is strictly positive in the chamber. The continuous bounded f is strictly negative on the nonempty open set0<Q<7 and strictly positive on Q>7. Choose nonzero compactly supported test functions g_- and g_+ inside these regions. Their multiplier quadratic forms have strict opposite signs. Approximate each g by S u_n in L² using dense range. Since M_f is bounded, <S u_n,M_f S u_n> converges to <g,M_f g>. Thus <u_n,D u_n> is negative for some n and positive for some n. D is an indefinite self-adjoint trace-class operator. In particular it has at least one positive and one negative eigenvalue, by the compact self-adjoint spectral theorem.

If D=cT0, self-adjointness and T0 nonzero make c real. Then S M_(f-cW) S=0. Its sesquilinear form vanishes on Ran(S)xRan(S); boundedness and density extend this to all L² pairs. Hence f=cW almost everywhere. Since W>0 inside C, this would require Q(Q-7)/4 to be constant, which it is not: at(x,y)=(1,1) it is-3, while at(2,2) it is15. Therefore D cannot be any scalar multiple of T0. Indefiniteness already rules out real scalar proportionality, but the dense-range proof also identifies the exact multiplier obstruction.

Neither result determines <phi0,D phi0>, nor an excited/ground ratio coefficient. Positivity of phi0 or Sphi0 does not remove the sign-changing weight f from its integral.

## Uniform-gap top-eigenvalue comparison

Write Ahat_beta=U_beta A_beta U_beta*, Bhat_beta=U_beta B_beta U_beta*, and Dhat_beta=U_beta P_beta M_(f(x_p))P_beta U_beta*. The already proved statements are
 Bhat_beta ->T0 in operator norm,
 Dhat_beta ->D in trace norm, hence operator norm,
 Ahat_beta-Bhat_beta=beta^-1 Dhat_beta+Rhat_beta,
 ||Rhat_beta||<30/beta².
The first convergence follows from the parent's compact saddle sandwich proof and exp(3/beta)->1. The parent September2 section5 explicitly proves that T0 is nonzero compact positive semidefinite with strictly positive interior kernel, and hence has a simple top eigenvalue mu0>mu1. In particular mu0>0 and its spectral gap g=mu0-mu1 is positive. This is a displayed parent hypothesis/proof, not a numerically fitted eigenvalue assumption.

Operator-norm convergence gives, for sufficiently large beta, a top gap of Bhat_beta at least g/2. Its normalized top eigenvector phi_beta can be chosen to converge to phi0, by convergence of the isolated rank-one spectral projections. Let E_beta=Ahat_beta-Bhat_beta, so ||E_beta||=O(beta^-1). For large beta it is smaller than one quarter of the Bhat_beta gap.

An elementary block argument gives the uniform first-order perturbation estimate. Decompose a normalized top eigenvector of Bhat_beta+E_beta as a phi_beta+z with z perpendicular to phi_beta. Weyl's eigenvalue bound and the spectral gap make the reduced resolvent on the perpendicular space bounded by2/gap(Bhat_beta). Thus ||z||/|a|<=2||E_beta||/gap(Bhat_beta). The phi_beta component of the eigenvalue equation then implies
 |lambda0(Ahat_beta)-lambda0(Bhat_beta)-<phi_beta,E_beta phi_beta>|
 <=2||E_beta||²/gap(Bhat_beta).
All constants are uniform in sufficiently large beta; no derivative or rate for Bhat_beta itself is needed.

Multiplying by beta, using beta Rhat_beta->0, Dhat_beta->D and phi_beta->phi0, yields
 beta[lambda0(A_beta)-lambda0(B_beta)] -> d0:=<phi0,D phi0>.
The isometric embeddings preserve the nonzero top eigenvalues, so this statement is also on the original discrete spaces. Since lambda0(B_beta)->mu0>0,
 beta[lambda0(A_beta)/lambda0(B_beta)-1] ->d0/mu0.
The equivalent top-to-top logarithmic comparison has the same coefficient, if desired, because both top branches are positive. The number d0 and its sign remain undetermined by this argument.

This compares the exact native normalized packet with its exact beta-dependent sampled shifted saddle. It is not an expansion lambda0(A_beta)=mu0+d0/beta+O(beta^-2): the saddle's own convergence correction has not been computed. It also supplies no excited-eigenvalue coefficient without a separately established isolated simple branch, no ground/excited log-ratio sign, and no physical mass-gap statement.
