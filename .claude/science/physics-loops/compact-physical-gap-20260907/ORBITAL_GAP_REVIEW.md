# Independent cold review: compact physical gap proofs

Verdict: PASS for both stated finite-cube results. No mathematical correction requested. This review did not rerun the finite support/center census; it checks its role and the analytic proof, with the reported exhaustive census retained as finite evidence.

Reviewed exact source hashes:
- /private/tmp/toe-autonomous-primary-20260907/compact-electric-gap/DERIVATION.md: fa74bb78510e060b54bb114a82d539a34339ee6d2281179d246cb5c3850de594
- /private/tmp/toe-autonomous-primary-20260907/compact-all-coupling-gap/DERIVATION.md: dc8bbdbf39a8fab146aaaa2bc312195f1e85491c1c21cfe2c734726149459414

## Block30

The all-representation lower bound is valid: every nontrivial edge costs at least4/a, and physical support has no degree-one vertex. Cube girth forces four edges; equality yields exactly fundamental/antifundamental face loops. Schur matching excludes a mixed-representation four-cycle. A five-edge support cannot avoid a leaf on this bipartite simple cube. At six edges a non-cycle minimum-degree-two support would require a theta graph with paths of lengths at least1,3,3, hence at least7 edges. Thus six-edge admissible supports are cycles. The reported count16 supplies multiplicity32; the interacting bound does not need that multiplicity.

Character orientation and conjugation are consistent. Pair Schur integrals are1; the cubic invariant in3 tensor3 tensor3 is the unique epsilon, giving integral chi³=1. Center selection is used only to remove terms, not to assign surviving Haar integrals. The moments12 and12 give lower Ritz entry35v/6 and off-diagonal -v/sqrt3. Min-max E1(H)>=16/a and ground Ritz upper bound yield the stated gap. The determinant (8x/3)(13x-35) proves the exact positivity interval, without identifying it with actual gap closure.

The isolated free ground and level16 cluster justify bounded analytic perturbation locally. Ground second coefficient -(1/3)/16=-1/48; conjugate-face blocks give slopes35/6 and37/6. The excited multiplicity is only first-order, as explicitly stated. No all-v perturbative conclusion is made.

## Block31

The tail bound is correct with the stated normalization. For shell m>=2, E>=4m and d<=(m+2)^3/8; f2=16/243, ratio bound (4/3)(5/4)^6/54<1/10, tail<=160/2187. Together with18e^-4<1/3 this yields889/2187<1/2. Absolute convergence permits a continuous heat kernel whose uniform half/three-half bounds are valid on the entire group, not only near identity.

Twelve-link products and normalized gauge averaging preserve the bounds. Bounded V gives the positive-cone semigroup comparison, explicitly not Loewner order. Positivity improving plus compact self-adjointness gives a unique strictly positive ground; gauge commutation makes it physical. The ratio bound3^12 exp(12av) cancels E0 and integral phi correctly.

The ground transform is domain-safe: smooth positive phi and reciprocal are bounded on the compact carrier, preserving Sobolev form domains. Gauge averaging preserves smooth-core density. Weighted variance is bounded using an infimum over constants, not a false equality of Haar and weighted means. The two density bounds produce exactly (minphi/maxphi)^2, yielding16/a times3^-24 exp(-24av). This is a strictly positive finite-volume physical gap for finite parameters, with no uniform-volume or continuum claim.

The constants are conservative but do not depend on unverified numerical exponential evaluations. Source claims accurately separate the exact algebra runners from the analytic tail, domain and all-representation arguments.
