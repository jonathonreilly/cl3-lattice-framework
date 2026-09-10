# Native shared-center zero-energy scattering identity

This is an analytical route, not a computation of alpha. Use the actual bipartite one-particle matrix K=[0,B;-B^T,0], with the center in the first sublattice. Write b for its row, and b_A for that row restricted to a subset A of its six incident bonds. Reversing exactly those bonds gives B_A=B-2 e_0 b_A^T. Here b_A is a column when it occurs without transpose.

On a cubic fully antiperiodic even torus the reference B is invertible. Centered magnetic cubic symmetries permute all six incident bonds and preserve the AP holonomies. Their gauge factors cancel in the products b_j(B^-1)_(j,0). Consequently those six products are equal. Their sum is (BB^-1)_(0,0)=1, so each is exactly 1/6. This argument requires the centered magnetic symmetry, not a bare coordinate permutation of the signed matrix.

For k=|A|, the determinant lemma gives

 det(B_A)/det(B)=1-k/3.

For k !=3, Sherman–Morrison gives

 B_A^-1=B^-1+[2/(1-k/3)] B^-1 e_0 b_A^T B^-1.

In particular a two-bond defect has determinant ratio 1/3 and inverse coefficient 6. Its four-bond complement has ratio -1/3; the full six-bond star has ratio -1. The skew determinant ratio for a pair is therefore 1/9 at zero spectral parameter, agreeing with the independent scalar Green-function pair-gap formula. This does not give the many-body resolvent matrix element: the latter depends on the complete excitation spectrum and its vacuum contractions.

The same identity has a useful infinite-volume interpretation. The inverse reference operator applied to a finitely supported source is square summable in three dimensions: its Dirac singularity is O(1/|k|), whose square is locally integrable. Let w_A=(B^T)^-1 b_A, using this Fourier inverse. Its center value is k/6 by the AP limit of the identity above. Let q be a generalized zero-energy white-sublattice Bloch solution, B^T q=0, with q_0=1. Then

 q_A=q+[2/(1-k/3)] w_A

satisfies B_A^T q_A=0 and (q_A)_0=1/(1-k/3). For the actual pair, the center amplitude is exactly 3. All these statements concern generalized one-particle solutions; q is not an l2 CAR vector, and no bounded gamma(q) operator is asserted. The correction w_A is l2. The k=3 denominator is singular and this route must not be applied to it.

## Why this has not yet proved the node sign

A Ward manipulation using q_A must retain its bounded correction 6w_A. The defect-adapted zero-mode functional is not the original vacuum annihilator. Dropping that correction would discard precisely additional local-source contractions of the kind present in the reviewed three-resolvent formula. The positivity of the on-center factor 3 therefore does not establish positivity of alpha.

There is also an exact many-body complement identity. Conjugation by gamma_0 flips every center-incident quadratic term and leaves all other terms unchanged, hence gamma_0 H_A gamma_0=H_(A^c), and likewise gamma_0 R_A gamma_0=R_(A^c), using the same reference energy. Thus R_C gamma_0 R_A=gamma_0 R_(C^c) R_A. In the 90-word sum C and A are disjoint pairs, so A is contained in the four-leg set C^c. The expression is an ordered product of two distinct inverses. It is not a positive quadratic form just because both negative resolvents have positive negatives.

The next genuinely discriminating identity would express the fully summed soft Ward correction together with the direct term as a squared norm or a positive scalar multiple of an impurity overlap. Neither the one-particle determinant identity nor the complement relation supplies that factorization. The negative disjoint-pair channel established separately makes discarding the correction unjustified.

## Source and scope

Read actual NODE_REDUCTION.md, SOFT_LIMIT_AND_LAPLACE.md and UNIFORM_PAIR_GAP.md in native-infinite-star-node-stretch, together with the canonical bipartite convention carried by the 8063 thermodynamic-limit note. This derivation is independent algebra using that convention. It uses no finite-L4 extrapolation, no branch choice for a Gaussian determinant, no assumed positivity of a Laplace kernel, and no physical numerical evaluation. The newly reviewed h/6 gap can bound all inverse factors, but a norm bound cannot settle their signed sum.
