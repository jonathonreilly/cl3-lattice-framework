# Native star form factor: exact target and conditional resummation

Source read completely: native-third-order-hybridization/DERIVATION.md (410b proof), plus native-third-vertex-interpretation/DERIVATION.md. The first proof supplies the actual energy-dependent operator, not a quadratic approximation:

 O_v(E0)=(1/8) sum_{A,C disjoint two-edge subsets of star(v)} R_C gamma_v R_A,
 R_A=(E0-H_A)^(-1).

There are 90 ordered terms. Every A is a wrong-flux pair, so both parity resolvents are bounded by the defect stiffness. This is an actual operator definition on the finite full carrier in the declared window. Its vacuum vector has odd active particle number and the physical vertex is -i O_v beta_v. The finite L4 identity and finite L6 multiparticle evidence do not determine its large-volume infrared form factor.

## What symmetry and positivity do, and do not, determine

Magnetic covariance makes O_v transform in the same vertex representation as gamma_v. It therefore permits a constant nonzero one-particle form factor: the family gamma_v itself has that covariance. It also permits a vanishing form factor: the family [Hactive,[Hactive,gamma_v]] transforms identically and multiplies one-particle amplitudes by omega(k)^2. Both are odd Hermitian families. Hence covariance alone cannot choose between node nonvanishing and vanishing. This is a concrete pair of symmetry-compatible alternatives, not a claim that either equals the native O_v.

Nor is a simple resolvent-positivity argument sufficient. Each -R_A is positive, but R_C gamma_v R_A is an odd transition operator, not a positive quadratic form. Even the incidence matrix selecting disjoint pairs is indefinite: on the 15 two-element subsets of six objects its eigenvalues are 6, -3 and 1. A direct -3 eigenvector is x_A=1_{1 in A}-1_{2 in A}; for A containing 1 but not 2, exactly three disjoint C contain 2, and conversely. Thus replacing the signed transition expression by a sum of positive Gram terms is not licensed by the six-positive-neighbor count. This does not refute a more subtle native positivity identity.

The exact unresolved datum is a_v(k)=<k|O_v(E0)|Omega>. A useful analytic result must either derive its leading value/vanishing at a node or control the full operator-valued connected return without that reduction. A finite set of momenta, the total one-particle norm, and an upper bound on inverse gaps cannot decide this limit. The definition contains flux-defect resolvents; replacing them by stationary free resolvents would change the question.

## Conditional quadratic model, with exact normalization

Only if an independently controlled reduction gave -i alpha u^3 sum_v gamma_v beta_v as the relevant quadratic vertex, the Majorana matrix would be

 K_eff = [[K, -2 alpha u^3 I], [2 alpha u^3 I, 0]].

Put m=2 alpha u^3. For an active frequency omega>=0, the two positive frequencies of this diagnostic are

 nu_+ = (sqrt(omega^2+4m^2)+omega)/2,
 nu_- = (sqrt(omega^2+4m^2)-omega)/2.

They satisfy nu_+ nu_-=m^2 and nu_+-nu_-=omega. At a Dirac point both equal |m|; for fixed positive omega, nu_-=m^2/omega+O(m^4/omega^3). If the active bandwidth is bounded by W and m is nonzero and momentum independent, the one-particle gap is at least (sqrt(W^2+4m^2)-W)/2, uniformly in volume. Its small-m scale is m^2/W, not the larger Dirac-point scale |m|. This statement is exactly about this quadratic matrix. Physical even-parity many-body level counting requires the separate vacuum-parity check.

This is not an approximation theorem for H_U. The actual O_v has higher odd pieces; other zero-return terms, the 648 mixed-middle orders, energy dependence and canonical normalization remain. Contributions of the same order as the tiny ultraviolet minimum can change the conclusion. A formal gap in this matrix therefore supplies neither a native bulk gap nor a phase claim.

## A possible CAR improvement over an absolute spatial majorant

An inverse-frequency one-particle kernel behaves as 1/|k| near a three-dimensional node if its numerator is bounded and nonzero. Its spatial l1 norm cannot be uniform (the Fourier multiplier is unbounded), as shown in the main derivation. However its row l2 norm CAN be uniform: Parseval reduces its squared row norm to a normalized sum bounded by constant times sum_k 1/omega(k)^2, and the same shell proof bounds this in three dimensions. This assertion requires a uniformly bounded form factor; that native property has not yet been proved here.

For real coefficients t_w and distinct Hermitian Majoranas beta_w, CAR gives the exact identity (sum_w t_w beta_w)^2=(sum_w t_w^2)I. Hence its operator norm is the row l2 norm. In particular a local commutator of a quadratic spectator Hamiltonian with beta_v can be controlled by l2, even when an l1 interaction estimate diverges. This removes one overly strong absolute-value obstruction, but does not by itself construct a local interacting ground state, a Lieb-Robinson estimate, or the joint-defect recursion. It suggests that preserving CAR cancellations in a resummed reference is more plausible than a scalar absolute-history expansion. The necessary native form-factor bound and higher connected operator bounds remain explicit obligations.
