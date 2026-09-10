# Corrected zero-mode Ward identity with all tails retained

Use the actual native definitions and normalization in SOFT_LIMIT_AND_LAPLACE.md. Let w_A=(B^T)^-1 b_A for a two-link pair and set W_A=6 gamma(w_A). This is a bounded Hermitian CAR operator, unlike the generalized original node mode. The rank-one identity gives (w_A)_0=1/3, hence {W_A,gamma_0}=4.

The generalized corrected mode q+6w_A solves K_A(q+6w_A)=0. Its rigorous bounded consequence is

 [W_A,D_A]=-J_A,
 [W_A,R_A]=-R_A J_A R_A.                         (1)

One may establish the first equation directly on the finite-particle core using the linear CAR commutator: K_A w_A is finitely supported by the defining inverse equation. The result extends as a bounded commutator. It does not require forming gamma(q), an impurity vacuum, or a unitary implementing a change of vacuum. The second identity follows from the bounded inverse commutator, with R_A=-D_A^-1.

Substituting (1) into the already reviewed soft identity, and using {W_C,gamma_0}=4, gives the exact bounded formula

 8 alpha = sum_(A,C disjoint) [
  3 <R_C R_A>
 + (1/2)<R_C gamma_0 (W_A-W_C) R_A>
 - (1/2)<W_C R_C gamma_0 R_A>
 - (1/2)<R_C gamma_0 R_A W_A> ].                (2)

All brackets remain in the ORIGINAL canonical Gaussian vacuum. In particular the last two terms must not be removed by an impurity-annihilation assertion. The derivation is simple operator algebra: the two middle terms of the expanded commutators combine as W_C gamma_0+gamma_0 W_A=4+gamma_0(W_A-W_C). This is where the native factor3 appears, with its exact normalization.

This removes one inverse from each correction, replacing its local numerator by a bounded spatial tail. It is a sharper structural target than a bound using beta/delta cubed. It does not make the direct overlap positive: <R_C R_A> is an off-diagonal Gram entry, and the disjoint-pair sum is indefinite. Pair reversal makes the full sum real but does not cancel the (W_A-W_C) term; its adjoint is exactly the reversed-pair term.

## Actual tail norms from the native scalar Green function

The pair-gap derivation defines A(0)=<e_0,(-K^2)^-1 e_0> and D(0)=1/(6h^2). Its normalized signed two-neighbor vector u has <u,(-K^2)^-1u>=A(0) for perpendicular pairs and D(0) for opposite pairs. Since ||b_A||=sqrt(2)h,

 ||w_P||^2=2h^2 A(0) <=17/30,
 ||w_O||^2=2h^2 D(0)=1/3.

Thus ||W_P||<=sqrt(102/5), and ||W_O||=sqrt12. These are real CAR vectors, so the operator norm equals their Euclidean norm. They use the actual Green-function bound, not a flat-spectrum L4 approximation. The difference vector has zero center component; its trivial norm bound is still at most the sum of the two norms.

For one ordered pair, the absolute value of the three correction terms in (2) is bounded by

 [ ||W_A-W_C|| + ||W_C|| + ||W_A|| ] /(2 delta^2)
 <= (||W_A||+||W_C||)/delta^2.

Even the opposite-pair norm is larger than the onsite coefficient3. Moreover no strictly positive lower bound for the direct disjoint Gram sum follows from the available gap. Consequently this rigorous estimate does not close a positivity proof, including with the improved h/6 gap. It does avoid the former extra inverse power, so it can improve an eventual certified approximation of the scalar target.

## Precise remaining opportunity

A sign proof must control correlations between W_A Omega and R_C gamma_0 R_A Omega, not merely the tail norms. The actual reference Gaussian relation fixes W_A Omega as a one-particle vector; it does not annihilate it. A usable next identity would evaluate or bound these cross contractions jointly with the disjoint-pair Gram channels through the actual quadratic scattering data. Formula (2) narrows that task to two inverses and explicit l2 sources. No impurity-vacuum implementer or determinant square-root sign has been supplied or used. Alpha remains unevaluated.
