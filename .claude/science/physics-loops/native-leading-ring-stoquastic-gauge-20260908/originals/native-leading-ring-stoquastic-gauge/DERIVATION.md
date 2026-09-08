# Explicit leading-ring diagonal gauge

Consider the supplied full native H4 on finite periodic cubic geometry with even extents at least4. The native A operators use the parent's canonical endpoint orientation and any fixed neighbor orders. The full W dictionary supplies d(x)=(-i)^|x|(-1)^q(x), q(x)=sum_(e<f)Mef x_e x_f, M_e=w_e XOR ell_e, where ell_e sums incidence rows of vertices from the lower endpoint up to but excluding the higher. M is symmetric off diagonal and has diagonal1. This dictionary is a phase-decorated basis bijection, not an arbitrary basis change.

Every ice string has exactly3N/2 occupied edges and n_v(x)=1 at every vertex. Thus W restricted to ice identifies it with the same electric bitstring and a fixed full matter occupation; its d phase is a constant times(-1)^q(x). Since W S_C W†=X_C, the ordinary electric-basis map U_d|x>=d(x)|x> sends S_C to the unsigned cycle flip. Equivalently d(y)/d(x) times the native S matrix element equals1 for y=x XOR C. Flippability is diagonal and unchanged.

Let eta_C be the product of the signs comparing the traversal direction of each edge with its lower-to-higher endpoint orientation. At length4, i^4=1 and reversal of the sequential native product crosses four anticommuting adjacent pairs, giving+1. Hence S_C=eta_C B_C, or U_d B_C U_d†=eta_C X_C. This step retains rather than discards the native oriented-cycle convention.

Choose coordinate axes0,1,2 and the static sign background

 xi_(r,a)=(-1)^(sum_(b<a) r_b).

It is periodic for every even extent. A plaquette in plane a<b has holonomy-1: changing r_a flips exactly the b-edge sign, while the other changes cancel. At a periodic seam the change1-L_a is odd and gives the same result. A straight winding cycle of length4 has holonomy+1 because the transverse exponent is repeated four times. For lexicographic vertex labels, every elementary plaquette has eta_C=+1, including seam plaquettes: each axis contributes one forward and one backward canonical sign, with paired wrapping signs. A straight extent-four cycle has three increasing edges and one decreasing wrap, hence eta_C=-1.

Define f(x)=product_e xi_e^x_e and U|x>=f(x)d(x)|x>. Then

 U B_C U†=eta_C product_(e in C)xi_e times X_C=-X_C

for every simple four-cycle on this domain. All simple four-cycles are elementary plaquettes or straight windings along extent-four axes. The explicit global bit formula on ice, after dropping the common(-i)^(3N/2), is

 U|x>=(-1)^[sum_(e<f)Mef x_e x_f + sum_(r,a)sum_(b<a)r_b x_(r,a)] |x>.

This single-valued diagonal phase proves consistency around every configuration relation automatically: phase ratios telescope. No assumed configuration connectivity or flux-only identification enters. Any reordering of native stars changes the supplied quadratic phase, not the result. The map preserves each exact support component and every diagonal observable.

With the parent's H4 coefficient +g^4 lambda^4/(2U^3) sum_C B_C (uniform positive native coefficients), the transformed leading nonconstant operator is -J sum_C X_C, J=g^4 lambda^4/(2U^3), plus the unchanged scalar. For arbitrary fixed real coupling signs at uniform magnitude, absorb their edge product into f as an additional linear bit sign. This still maps every leading cycle term to the same negative adjacency. It does not remove H6's closed-loop obstruction; its six-cycle terms transform too and retain that invariant negative product.

If every extent>=6, C4 consists only of elementary plaquettes, so this is exactly the supplied ordinary pure-kinetic plaquette Hamiltonian V0, up to scalar and time/energy scale, on the same ice component. If an extent is4, the full H4 also contains straight winding4 flips. The gauge makes those negative as well, but it does not remove them. Therefore the full L4 H4 is not identical to a numerical target that includes only elementary plaquettes. Removing winding terms would be an additional supplied modification. L2 is outside this simple-graph domain.

This is an exact leading-coefficient operator identity in the canonical convention, not equality of the full finite-coupling Hamiltonian, a selected action, a locality claim for the quadratic diagonal unitary, a ground-state result, or a Coulomb-phase inference. It does identify the precise leading supplied V0 comparison at L6 and larger even extents without pretending H6 remains stoquastic.
