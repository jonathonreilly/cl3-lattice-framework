# U0 physical flux optimization through a half-filled hopping theorem

Status: conditional-support, pending independent bridge review. The supplied uniform native model and its exact constrained dictionary remain premises. This imports a mathematical flux theorem explicitly; it does not select the Hamiltonian from the axioms or establish any nonzero-U phase.

## Exact reduction of the physical sector objective

For an even vertex count N, the fixed magnetic-link flux orbit has the even-Fock Hamiltonian Hξ=(i/4)γ Kξ γ, with canonical i<j entries Kij=-2gλξij. Let the nonzero eigenvalues of iK be ±ωa, a=1..r, ωa>0. The independently derived endpoint result gives each active occupation pattern multiplicity2^(N-r-1). Consequently

 E_native(ξ)=-1/2 sum_a ωa,
 Z_native(β,ξ)=2^(N-1) product_a cosh(βωa/2).

Define a separate unconstrained spinless auxiliary Hamiltonian H_aux=Σij (iK)ij di†dj on N modes. Its one-particle spectrum is the same ±ωa with N-2r zeros. It is bipartite, so its unconstrained ground is attainable at exactly half filling, including an appropriate choice of zero occupations. Direct products give

 E_aux(ξ)=-sum_a ωa=2 E_native(ξ),
 Z_aux(β,ξ)=2^N product_a cosh²(βωa/2),
 Z_native(β,ξ)²=2^(N-2) Z_aux(β,ξ).

The last expression is the full auxiliary Fock trace at chemical potential zero, not a fixed-particle-number canonical partition function. The physical even-parity restriction has already been included via spectator multiplicity; it must not be imposed a second time on H_aux. The prefactor is independent of flux and rank. Thus minimizing the physical ground energy or fixed-flux free energy is precisely the same flux optimization as this auxiliary hopping problem. This is an equality of objectives, not a Hilbert-space/unitary equivalence between native and auxiliary systems.

## Explicit imported theorem and applicability

Macris and Nachtergaele, arXiv:cond-mat/9604043, Theorem1.4 with assumptionsA1/A2, prove that a canonical flux assignment minimizes the spinless hopping ground energy on the specified bipartite reflection graphs. A basic even circuit of length2m has canonical hopping holonomy(-1)^(m-1). Their finite-temperature remark extends the reflection inequality to the full Fock trace. The paper's hypercubic example and torus discussion include periodic winding circuits. Uniqueness of all energy minimizers is not proved. Lieb's original result is arXiv:cond-mat/9410025. These theorem statements are the only imported optimization step.

For the present rectangular periodic cubic graph take every extent La even and at least4, and all hopping magnitudes2|gλ| uniform and nonzero. Bipartiteness follows from coordinate parity, including seams. Choose C to contain every elementary square and every straight coordinate winding. It is generating: commute adjacent steps using square boundaries until each closed walk reduces to coordinate windings; winding loops at different roots differ by sums of squares. This integral cycle statement fixes all U(1) fluxes, not just Z2 parity.

For each axis a and integer s, reflection ra -> 2s+1-ra modLa has no fixed vertices and exchanges the two half-tori bounded by the two opposite cut planes. All edges/magnitudes are invariant. A square crossing a cut is fixed as an unoriented circuit, while a winding crossing a cut must run in axis a and is likewise fixed. All other circuits lie in one half. For each square choose a cut through one of its edges; for each winding choose its axis cut. This verifiesA2 for the generating C. An embedding can be made by placing each vertex reflection pair at opposite positions across a hyperplane; planarity is not required. Including all three winding directions resolves the abbreviated D-1 wording in the paper's hypercubic paragraph rather than treating plaquettes alone as a basic set.

## Canonical hopping flux belongs to the allowed native Z2 family

For a traversed cycle C of even lengthℓ let ηC multiply the signs comparing each step with canonical lower-to-higher vertex order. The normalized auxiliary hopping product is

 product_C [(iK)ij/(2|gλ|)] = (-i)^ℓ ηC product_e ξe.

A global sign of gλ cancels for evenℓ. Choose ξ_(r,a)=(-1)^(sum_(b<a)r_b). It is periodic for even extents. Every square has ξ holonomy-1 and η=+1, hence auxiliary holonomy-1, the canonical length4 flux. Every straight winding has ξ holonomy+1 and η=-1, hence auxiliary holonomy(-1)^(La/2+1)=(-1)^(La/2-1), exactly the canonical lengthLa flux. Thus an optimizing U(1) hopping configuration actually lies in the native allowed ξ=±1 family. A minimum over the larger U(1) family attained inside this smaller family is also its minimum. The resulting native sector has S-square eigenvalues-1 and straight magnetic winding eigenvalues+1, with the specified cycle convention.

The background minimizes each fixed-flux objective; the full physical ground energy is therefore the value in this sector. At finite temperature the full native partition function is still the sum over all flux sectors. Maximum individual sector weight does not make the entire Gibbs state equal to that sector, establish flux concentration or a phase, or give a flux excitation gap. No uniqueness or stability to U D is inferred. At gλ=0 every sector is tied, handled directly without the nonzero-hopping theorem.

The same sign background appears in the leading-H4 diagonal gauge, but those are distinct uses: here it specifies a magnetic sector at the U0 endpoint; there it is a phase transformation of electric ice configurations. This coincidence is not a proof that the two limits share a phase.
