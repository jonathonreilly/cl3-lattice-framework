# Independent U0 flux-objective bridge review

Disposition: PASS for the stated finite, uniform, even rectangular torus, with the imported mathematical theorem explicit. No fatal parity, trace, or reflection obstruction found. This is a source-specific conditional review, not an audit verdict or a phase theorem.

Reviewed complete root DERIVATION.md a54fddac4ac8962e7ddfa55de140e056664812c42fc5106a115f6924bfeed643, check.py b066614ac8169cdfef280db5403f6349c85744d13dd69c429d0a42bd0352ff53, preregistration, source receipt, result and freeze. The author's 6962 predicates test finite objective/reflection fixtures, not the imported theorem. No author module was imported by my controls.

## Primary-source coverage

Read Macris–Nachtergaele, https://arxiv.org/pdf/cond-mat/9604043, printed pp.4–6 (A1/A2, definition and Theorem 1.4), pp.7–15 (Fock tensorization, right particle-hole transformation, cross-plane gauge, reflection inequality, canonical-count improvement and finite-temperature remark), and pp.18–21 (torus, integral generating circuits, hypercubic example). The proof acts on the tensor product of the two full Fock spaces; its finite-temperature trace extension therefore supports chemical potential zero, rather than a fixed-number thermal trace. Its canonical assignment is a minimizer; uniqueness of minimizers is explicitly left unresolved. The example's D−1 wording does not replace verification of A2 for the three-dimensional torus.

## Independently checked bridge

Enumerating all N ordinary occupation bits with even total parity gives each active r-pattern exactly 2^(N-r-1) realizations. At least one spectator pair remains for the present even N, including maximal active rank. Thus rank changes do not alter the prefactor after writing the answer as a product of coshes. Enumerating the auxiliary full Fock occupations independently gives Z_native squared = 2^(N-2) Z_aux at the SAME beta. Its minimum energy is twice the native minimum. At exactly N/2 auxiliary particles the minimum is still attainable by filling negative energies and enough zero modes; the fixed-number thermal partition function is different. The controls explicitly distinguish those traces.

For A2, each crossing bond in the chosen half-torus cut joins a vertex to its reflection, and no vertex has two crossing bonds when every extent is at least four. This additional fact licenses the independent cross-plane gauge operation used in the paper's proof. Squares crossing a cut have precisely two crossing edges and one reflected half-path; straight axial windings do likewise. Other basic circuits stay in one half. The full set is reflection-stable. Each target circuit can be crossed by a suitable cut. A symmetric abstract embedding suffices; a planar embedding is not required.

The integral generation claim follows by reducing a lattice walk with square commutations in the universal cover; its remaining displacement is a sum of coordinate periods. Including all winding directions kills those residual generators. This is stronger than a mod-two cycle-space statement and addresses U(1) fluxes.

The supplied ordered-edge eta factor must remain in the auxiliary hopping flux. For a square it is +1, while a straight winding has one descending seam and eta=-1. With the stated periodic xi background the resulting auxiliary flux is canonical for lengths divisible by four and for lengths two modulo four, including mixed extents. Global coupling sign cancels around every even circuit. Consequently the U(1) optimizer lies in the allowed native Z2 subset.

My check.py passed 6590 predicates: independent parity-constrained occupation enumeration for N=2,4,6,8 and every possible active rank, matching ground minima including half filling, a fixed-number-trace adverse distinction, independent crossing-edge matching on mixed tori, and frozen input hash checks. These are finite support controls; the general reflection and cycle-generation arguments above carry the theorem application. I did not rerun the author's control suite.

Scope remains U=0 and supplied uniform real coupling. The full thermal trace sums all native flux sectors; an individually maximal sector weight proves neither concentration nor a gap. This does not settle uniqueness, nonzero-U stability, phase continuity with the large-U ring model, or physical selection of the Hamiltonian.
