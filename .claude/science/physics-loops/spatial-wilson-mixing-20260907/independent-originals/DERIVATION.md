# Independent untouched-edge criterion and actual cube-cap compression

Status: bounded source-grounded analysis, scratch only. Graph/action/embedding were frozen before computation in PREREGISTRATION.md. This is a supplied finite SU(3) Wilson slab, not a derivation of the framework's physical environment or action. The source seam is the open target in GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_FINITE_BOX_CONVOLUTION_REALIZATION_UNIQUENESS_NARROW_NOTE_2026-05-17.md:141–148, with the independent central temporal link kernel from GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md:27–65 and138–165. The older source-sector factorization note supplies typed D only; it is not used as a Wilson operator here.

## Exact sufficient untouched-edge criterion

Let E chi_lambda(U)=chi_lambda(W_source(U)), with the source a simple oriented four-edge loop. It is an isometry from Haar class functions, because the product of independent Haar edge variables is Haar. On an oriented source edge e, E chi_lambda lies entirely in the Peter–Weyl edge isotypic sector lambda, or its dual if that edge occurs inversely. This follows by expanding the loop trace in the matrix entries of that single link, with all other links as coefficients.

Let P_lambda,e denote that isotypic projector on the full link Hilbert space. Every independent central temporal link convolution commutes with all these projectors. If an edge e is absent from every remaining spatial multiplier at BOTH time slices, those multipliers act as identity on its variable and commute with P_lambda,e too. Thus the actual stripped transfer R_full=M_F C M_F commutes with P_lambda,e. It follows immediately that
< E chi_mu, R_full E chi_lambda>=0 for mu!=lambda.
This is sufficient for character diagonality, even when the remaining factors couple arbitrarily many other links. It is stronger and more precise than a pictorial assertion that some plaquette is missing.

The criterion requires absence from both slices after stripping; absence on only one side does not generally suffice. It also requires that no boundary state, noncentral temporal kernel or other factor consumes that edge. In representation terms, the exact sufficient condition is preservation of its isotypic sectors. Spatial touching is a test for failure of this criterion, not a proof that mixing must occur.

Vertex gauge transformations act by left/right translations on an edge and preserve its isotypic projectors. A Gauss-law projection therefore also commutes with them. It cannot spoil the above diagonality conclusion, nor does it impose character diagonality once the criterion fails: distinct source-loop characters are already gauge singlets.

## Actual stripping and scope of compression

The marked face spatial halfweight is a function m(W_source). Exactly M_marked E=E M_m and E* M_marked=M_m E*. Hence the full source compression has the form M_m [E* M_F C M_F E] M_m, and stripping the marked halfweights gives R_(s,b)=E* M_F C_b M_F E. This is an actual Wilson Haar compression for the supplied finite slab. It does not use a supplied abstract diagonal D. Stripping is done on the full class-function space before taking any finite character box; inverse finite compressions need not reproduce this operation.

## Cube cap and its gauge tree

The cube's five non-source faces form a disk spanning all four source edges; every source edge is touched by one side face. Let bottom vertices be A,B,C,D cyclically, top vertices A',B',C',D'. A gauge tree is the bottom edges AB,BC,CD and four vertical edges AA',BB',CC',DD'. Set its seven links to identity by Haar-preserving vertex transformations. The remaining source edge carries W up to orientation/conjugation, and the four top edges are a,b,c,d. Normalized Haar factors from the gauge tree integrate to1. There is no hidden charged boundary state.

With w(g)=exp[(s/6)ReTr g], inversion symmetry and centrality permit the conditional five-face integral to be written

g_s(W)=integral w(a)w(b)w(c)w(W d^-1)w(abcd) da db dc dd.

Expanding the final factor in characters and integrating a,b,c using the matrix-coefficient Schur identity multiplies chi_lambda(d) by(c_lambda/d_lambda)^3. Integrating d against w(Wd^-1) adds one more c_lambda/d_lambda. Consequently

g_s(W)=sum_lambda c_lambda(s/2)^5/d_lambda^4 chi_lambda(W),

where c_lambda(s/2) means the character coefficient of exp[(s/6)ReTr], matching the native author's convention w_eta=exp[(eta/3)ReTr]. Orientation reversal replaces lambda by its dual, whose coefficient is equal here. Thus the normalization and fifth power/four dimension divisors are exact. At s0 the result is1, providing a trivial-channel check.

This explicit gauge tree also shows why a collection of four side plaquettes with an unfilled top behaves differently: after removing the top weight, free top-edge integration kills all nontrivial character dependence. Touching all four source edges alone is not enough; the closed five-face disk is the crucial nontrivial contraction in this cube fixture. It is the minimal complete cap among subsets of the cube's other five faces. No global minimality over all graphs/boundary identifications is claimed.

## Actual off-diagonal element and strictly positive temporal coupling

At b0 all twelve temporal Wilson factors equal1, so C0 is the projection onto the constant full-link function. Therefore
R_(s,0)=|g_s><g_s|.

Writing 0 for the trivial representation and3 for the fundamental, the exact off-diagonal element is
R_(s,0)[0,3]=c_0(s/2)^5 c_3(s/2)^5/81>0 for s>0.
Both external characters are gauge invariant, so Gauss projection leaves this calculation unchanged. The positivity follows without numerical integration: exp[(s/12)(chi3+chibar3)] has a uniformly convergent tensor-character series with nonnegative multiplicities; hence c0>=1 and c3>=s/12. Thus the off-diagonal is at least a_s=(s/12)^5/81.

This b0 calculation is not the final positive-coupling claim. For the actual finite Haar integral, the ten spatial halfweights have total bound exp(5s), twelve temporal factors obey |C_b-1|<=exp(12b)-1, and |chi3|<=3. Therefore
|R_(s,b)[0,3]-R_(s,0)[0,3]|<=3exp(5s)[exp(12b)-1].
It follows that the off-diagonal remains nonzero whenever the right side is less than a_s. Division by a positive trivial-channel scalar for temporal normalization does not change nonvanishing.

The native author's proposed concrete s1,b=10^-12 passes independently: exp5<149, and exp(12b)-1<=24b because12b<=1/2. The perturbation is at most10728/10^12, strictly below1/(12^5*81). Thus the real part of the off-diagonal remains strictly positive. A positive Taylor sum plus geometric remainder certifies exp5<149; the exact rational comparisons are reproduced in check.py without importing the author's calculation.

## Interpretation

This supplies a concrete genuine spatial-Wilson off-diagonal mechanism on a fixed finite graph and positive couplings, invalidating any universal inference of diagonal residuals from central independent temporal links plus gauge invariance alone. It does not establish non-diagonality for every environment, every coupling (including isotropic coupling), or a framework-selected slab. It does not replace the untouched-edge criterion by its converse. The separate wall-uniform dimension-divided one-link asymptotic is a different question and was not computed here.
