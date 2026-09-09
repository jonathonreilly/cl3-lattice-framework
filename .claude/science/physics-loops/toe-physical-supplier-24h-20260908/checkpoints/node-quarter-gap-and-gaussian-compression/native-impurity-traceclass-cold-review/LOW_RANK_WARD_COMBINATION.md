# Raw nuclear approximation to uniform unnormalized Ward accuracy

Inputs: LOW_RANK_PROJECTOR_CERTIFICATE.md source943237a3cabc4346fd8c7d9191833e77ea14a4dda249195b632eb92f86aa062a, independently reviewed in native-impurity-lowrank-cold-review/REVIEW.md; the explicit Fock product and bounded Ward identities in this campaign. This is a mathematical combination, not a numerical extraction of principal angles.

Suppose D=P_A-P0 has a rank-k approximation Q with ||D-Q||1<=eta<1. Best rank-k approximation in nuclear norm gives sum_(j>k)s_j(D)<=eta. This can be proved by compressing onto the orthogonal complement of the k-dimensional output of Q and using the singular-value variational principle. No rounding of P0+Q is needed for this inference.

Choose canonical particle-hole principal blocks ordered by decreasing angle and retain every block intersecting the first k singular directions. A paired creation block has four singular directions with common value sin(theta), and uses two fermion modes. A fully swapped mode has two singular directions of value1 and uses one mode. Within a degenerate eigenspace choose these canonical blocks first; there is no need to retain the entire accidental spectral degeneracy. Completing the final intersected block adds at most three directions. Thus the retained one-particle dimension is at most k+3, and its fermion-mode count is at most floor((k+3)/2). For k2352 the safe bound is1177 fermion modes. All swapped modes are retained because any omitted singular value1 would contradict eta<1. This is a principal-angle carrier, distinct from the quadrature-column carrier and not a recipe for obtaining its basis cheaply.

The omitted paired angles obey 4 sum_tail sin(theta)<=eta, in particular sum_tail sin(theta)<=eta. Therefore sum_tail sin²(theta)<=eta² and the explicit product construction gives the safe bound

 ||Omega-Omega_r||<=sqrt(2)eta = epsilon.         (1)

(The multiplicity4 permits a stronger constant, but no downstream estimate here uses it.) Parity is preserved, and phase is fixed by the original-state product overlap, not by a possibly zero impurity-vacuum overlap. The rank and error are theoretical consequences of the raw Q certificate; they do not claim that Q's singular vectors themselves are the exact principal vectors of D.

## All terms of the two-inverse Ward observable

Use the independently rederived identity

 8alpha=sum_disjoint [3<RC RA> +1/2<RC gamma0(WA-WC)RA>
 -1/2<WC RC gamma0 RA> -1/2<RC gamma0 RA WA>].

For each impurity choose a normalized Omega_rA satisfying (1). Propagate Omega_rA under its exact DA. For the left boundary term also propagate WC Omega_rC under DC; for the right boundary term propagate WA Omega_rA under DA. These odd source states differ from the exact ones by at most ||WA||epsilon_A. Applying a single linear CAR field to a finite-mode state adds at most one additional orbital to its excitation carrier; an annihilation term changes coefficients but does not require an infinite set of new orbitals. All such sources are propagated unnormalized.

Semigroup contraction and integration give, for one ordered pair, a total Ward error at most

 delta^-2 [3 + (||WA-WC||+||WA||+||WC||)/2]
             (epsilon_A+epsilon_C)
 <=delta^-2(3+||WA||+||WC||)(epsilon_A+epsilon_C).

This uses ||gamma0||=1 and normalized original/approximant vacua; source norms are bounded by the relevant W norm. With ||WA||,||WC||<=4.6, epsilon_A,epsilon_C<=sqrt2 eta, the full90-word alpha error is at most

 (90/8) * (61/5) * (2sqrt2 eta) /delta².        (2)

No inverse-cube error appears. This is only the state-compression error: errors in scalar impurity energies, orbital propagation, principal-angle extraction, W tails, and common-representation overlaps must be added separately. The bound can use whichever impurity gap has actually been certified; it does not infer a finite-volume gap from an infinite one.

At eta=2287839703834313821/4000000000000000000000000 and k2352, formula(1) is below8.1e-7. The rank increases only through the reviewed polylogarithmic quadrature choice as eta decreases. Thus there is a rigorous polylogarithmic EXISTENCE bound for a finite-excitation approximation with uniform unnormalized propagation error. It is not a polynomial-time or384MiB representation: a generic state on1177 fermion modes would be enormous. A Gaussian/wedge representation, certified angle extraction, and phase-consistent cross-impurity evaluation remain essential computational obligations. No physical matrix, spectrum, or quench was evaluated here.
