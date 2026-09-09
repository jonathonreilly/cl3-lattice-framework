# Independent native node/soft-limit review

Disposition: PASS after the narrow adjacent-swap wording correction in PAIR_ORBITS.md. Alpha is not evaluated and no sign conclusion is supplied.

Reviewed complete NODE_REDUCTION.md, PAIR_ORBITS.md, SOFT_LIMIT_AND_LAPLACE.md (d9145e85d147b2b13bae236b892cc548d0de769f378939ee91993e5e5b8471d1), the earlier NODE_GAUSSIAN_REPRESENTATION.md for conventions, and the three small control sources. Current hashes are in READ_HASHES.json. Parent8062/8063 definitions were re-read for the exact 1/8 times90 creator, Gaussian extraction coefficient 1/2, thermodynamic cocycle and full-active wrong-pair gap. I previously independently reviewed those parent analytical constructions. No improved h/6 gap is imported here.

## Node and symmetry

The creator ambiguity has zero smooth node value: a smooth null symbol lies in the null space of the physical band projection on each approaching ray; opposite rays have complementary limiting projections. This does not choose a projector value at the singular node. A fixed smooth cell gauge equal to identity at zero preserves the conclusion. The given magnetic translations and site-centered reflections restore the oriented pi-gauge bonds. At the node their matrices force a scalar diagonal intertwiner. Bipartite anti-linear covariance then makes that scalar real. This uses invariance of the supplied Gaussian vacuum and the actual defect-family sum, not symmetry of eigenvalues alone. Nonzero finite one-particle norm would not determine this scalar.

My independent literal signed-edge control verifies translations, reflections and all coordinate permutations on the integer box [-2,2]^3. It found 160 failures of the single monomial gauge for the nonadjacent x/z swap. The author preserved the predecessor and corrected PAIR_ORBITS to adjacent swap generators and the composed general-permutation gauge; its new SHA is f0036658c448b3feaafae282f8448ec64ac3b7227bc589fb24bee6d9986acc82. The correct arbitrary-permutation gauge is the product over inversion pairs. It equals +1 at the origin and every even-coordinate site. Independently enumerating ordered disjoint pair actions gives sizes6,12,12,12,48, totaling90. No exchange of A and C or positivity is assumed. The correction repairs wording, not the orbit reduction.

## Exact soft identity and normalization

From [a,H]=omega a and L=[a,B], one has a(E-H-B)=(E-H-B-omega)a-L. Multiplying the inverses proves equation(1) with E MINUS omega and a plus R_minus L R term. Applying it first across R_C, then a gamma_v=phi(v)-gamma_v a, then across R_A gives all three terms and the minus sign in equation(2); aOmega=0 removes only the final rightmost annihilator. Defect inverses are never commuted through the vacuum.

A normalized cell annihilator has local anticommutator coefficients sqrt(2/n_cell)u. The stated sqrt(n_cell/2) rescaling therefore gives phi=u. Although its global norm diverges, only the local commutators enter the right side. At phi=q, L_A equals J_A/2, not J_A. Combining this with the parent's coefficient extraction and 1/8 word factor yields exactly equation(3). Complex finite spinors require merely a uniform local linear-CAR bound; the later real q insertion has ||J_A||=4sqrt(2)|t| as written.

The shift error is at most omega/delta² because both unshifted and downward-shifted spectral parameters lie below the same wrong-flux spectrum. Products with up to three inverses and fixed local insertions have finite-volume limits: expand the common integrable inverse filters, rewrite free evolutions into perturbation cocycles, apply compact-time local convergence, and dominate by their uniform norms. The small shift contributes a unit-modulus scalar exp(-i omega t). This is sufficient without any generalized-q operator or norm of its spatial cutoff.

At a chosen direction the limiting identity holds on the full rank-four annihilation-band subspace, not just a selected eigenvector. Opposite directions span the eight-dimensional cell space. Linearity consequently permits evaluating at e0 even though e0 is not itself an annihilation-band vector. The parent's smooth weighted-l1 coefficient symbol identifies the left limit. This is the essential logical step replacing the invalid generalized-Hermitian-annihilator argument; it is present and correct.

## Laplace signs and tail

R_A=-D_A^-1. The RC RA term has two negative signs. RC JC RC gamma RA has three; the final minus RC gamma RA JA RA has an additional minus. Defining Z_A(s) as the negative insertion integral gives exactly those signs in equation(4). Integrating the ordered insertion over s produces -D_A^-1 J_A D_A^-1. The integrand bound exp(-delta(t+s))[1+beta(t+s)/2] follows from the full-active impurity gap, without an active vacuum gap or any positivity of the signed scalar integrand.

The union of t>T and s>T gives equation(5): each half contributes exp(-delta T)[1/delta²+beta T/(2delta²)+beta/delta³]. My independent exact rational Taylor calculation verifies the claimed T=1024 and beta<3 tail below10^-6 with delta=3483/102400=6kappa in h=1 units. It does not use the provisional improved pair gap.

## Evidence and remaining obligations

The new independent check.py executes4509 integer/rational predicates, including the actual failed nonadjacent gauge formula, all five pair orbits and the conservative tail comparison. Supplier finite resolvent controls were read as algebraic fixtures, not treated as physical matrix elements or a proof of alpha's sign. No physical spectrum, inverse, Gaussian overlap or integration was evaluated here.

The bounded scalar representation is valid on the supplied Gaussian/domain premises. Numerical point evaluation still requires signed Gaussian overlaps/insertions, finite approximation and arithmetic errors, and treatment of overlap zeros/conditioning. Tail smallness alone is not feasibility or a nonzero-alpha certificate. The earlier real-time formal-q formula is not needed to justify the reviewed soft-limit route; its spatial-cutoff interpretation should not replace this safer route in a canonical proof.
