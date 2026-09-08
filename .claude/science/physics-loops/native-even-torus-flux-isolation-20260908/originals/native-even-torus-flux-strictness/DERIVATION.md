# Strict flux selection on finite even rectangular cubic tori

Candidate theorem for independent review. On the supplied finite cubic torus with all extents even and>=4, uniform nonzero hopping magnitude, the canonical flux assignment is the UNIQUE minimizing flux orbit at U=0. The statement concerns flux orbits, not uniqueness of the native ground vector with its spectator degeneracy. No volume-uniform gap, finite-penalty stability, physical coupling selection or phase follows.

Inputs imported explicitly: the full CAR/Z2 native dictionary and its auxiliary energy identity, and the Macris–Nachtergaele reflection representation/inequality for the declared canonical basic circuits (cond-mat/9604043 Section2). The strict equality/control argument below is additional, not attributed to their theorem. The previously established canonical dispersion is used only to describe the auxiliary vacuum; the stronger faithfulness lemma itself does not require a spectral calculation.

## 1. The exact reflection tensor form

Choose a coordinate cut into equal half-tori of m=L_a/2 layers. Its two boundary layers are paired with their reflected counterparts by single crossing bonds. The MN half-Fock/Jordan-Wigner and right particle-hole transformations, followed by a local gauge, give

H(A,B)=A⊗I+I⊗B−sum_mu C_mu⊗C_mu.

A,B are Hermitian number-conserving half hopping quadratics (right particle-hole changes its hopping sign/conjugation). Every C_mu is a positive real multiple of a boundary annihilator or creator in a real occupation-basis CAR representation. Both members of each adjoint pair occur with the same positive weight. Therefore the sum is Hermitian. Vectorization sends the interaction to -sum C_mu X C_mu^T=-sum C_mu X C_mu†. The distinction between transpose and adjoint is harmless ONLY because these channel matrices are real. Complex phases remain in A,B, not in C_mu.

The half tensor identification does not introduce a missing entangling transformation: the d-generators on the left differ from its usual CAR representation by a unitary within the left matrix algebra, and the right generators form its independent CAR algebra. Right particle-hole and phase changes are also half-local. All statements about rank or gauge intertwining are made in these explicitly specified tensor coordinates.

## 2. Every positive reflected ground matrix is strictly positive

Consider H(A,bar A). A positive semidefinite coefficient matrix X of a normalized ground vector satisfies

A X+X A−sum_mu C_mu X C_mu†=E X.

Such a nonzero positive ground matrix exists by the same matrix modulus inequality used in MN: replace any ground coefficient matrix by its left/right positive moduli; their averaged energy cannot increase, hence each is also a ground vector.

For v in kerX, sandwich the eigenmatrix equation with v. The A terms and right side vanish, leaving sum_mu ||X^(1/2) C_mu†v||²=0. Thus each C_mu† preserves kerX. Adjoint pairing means all boundary creation AND annihilation operators preserve it, so their algebra reduces kerX. Applying the eigenmatrix equation to v now makes every interaction term vanish and yields X A v=0. Hence A also preserves kerX; A is Hermitian, so this is a reducing subspace.

Boundary CAR together with A generate the FULL half CAR algebra. Start with both outer layers. For a known site x on the inward frontier, [A,c_x] is a linear combination of neighboring annihilators. All transverse neighbors and the outward neighbor are already known; there is exactly one inward unknown neighbor y until the fronts meet. Its nonzero hopping coefficient allows solving for c_y. Adjoint gives c_y†. Peel whole layers successively. For m=2 every site is boundary already. This proves generation for every m>=2, irrespective of interior hopping phases. The irreducible full Fock CAR algebra has no proper reducing subspace. Since X is nonzero, kerX is not the whole space and must be zero.

Thus EVERY nonzero PSD ground coefficient matrix of a reflected half Hamiltonian has full rank. Neither uniqueness of that ground nor a no-zero-mode assumption was needed. This is stronger than the earlier canonical Slater rank certificate; that certificate remains a separate verified L6 illustration.

## 3. Saturation forces boundary-fixed unitary equivalence

Let X=U Sigma V† be a ground coefficient matrix for H(A,B). Put Y=U Sigma U† and Z=V Sigma V†. Direct cyclic-trace expansion gives the energy defect

E_(A,B)(X)−[E_(A,bar A)(Y)+E_(bar B,B)(Z)]/2
 = (1/2)sum_mu ||Sigma^(1/2)(U†C_mu U−V†C_mu V)Sigma^(1/2)||_HS².

A/B terms cancel. The channel identity is the elementary weighted square identity; paired real channels ensure the original expectation is its real part. This establishes equality conditions without asserting that a many-body hopping matrix is entrywise positive.

If the original flux is a global minimizer, both reflected child energies equal that minimum by MN's inequality and global minimality. The displayed trial energies must also attain it, and all squares vanish. Y and Z are PSD reflected ground matrices, so Section2 implies Sigma invertible. Hence R=U V† commutes with EVERY boundary channel. Subtracting the right-child eigenmatrix equation from the original equation after multiplication by R† gives

(R† A R−bar B)Z=0,

therefore R† A R=bar B. This is exact, with no unknown energy scalar because both ground energies are the same. Consequently the original is equivalent to a reflected child by a half-system unitary fixing all boundary CAR generators.

## 4. That unitary is a site gauge, in any number of layers

Let R† A R=C be an equivalence between half hopping quadratics, where R fixes all boundary annihilators. Initially the known modes are those boundary modes. Double CAR commutators of A with two known modes recover their hopping entries, so the corresponding entries of C agree after the already-known site phases are accounted for.

At each inward-frontier site x, its hopping commutator has only one unknown neighboring mode y. Subtract known contributions and divide by the nonzero coefficient. One obtains R†c_y R=z_y c_y, where |z_y|=1 follows from the CAR and equal hopping magnitudes. All frontier sites at that layer determine their respective phases; any second determination is consistent because it comes from the same R. Incorporate those phases and iterate. Thus R acts by site phases on every mode. Irreducibility makes it equal to that gauge implementer up to a scalar. Its boundary phases are1, so it changes no cross-plane bonds. The original full hopping assignment is therefore gauge equivalent to the reflected child.

## 5. Unique canonical orbit

The reflected child has canonical flux through every basic circuit crossing the chosen reflection cut. Gauge equivalence means the original has these fluxes too. A minimizing original can be tested against EACH coordinate cut; every elementary square and every straight winding crosses an admissible such cut. Therefore all its basic fluxes are canonical. The established generating-set argument identifies one gauge orbit. This direct argument does not need to assume an arbitrary minimizer already has a faithful Slater state or to carry out a reflection sequence.

The canonical assignment exists in the native Z2 family and attains the larger U(1) minimum. Thus a native Z2 minimizer is also a minimizer of the larger phase problem, and the argument applies. For connected graph, two Z2 sign assignments related by a U(1) site gauge with all edge ratios±1 are also related by a Z2 site gauge after removing one global phase. Hence uniqueness is also exactly uniqueness of the native orbit.

The canonical auxiliary Slater vacuum is indeed unique: its all-antiperiodic magnetic momenta have no simultaneous zeros (in fact each sin factor is nonzero at finite even extent), so the one-particle spectrum has no zero. This agrees with, but is not necessary for, Section2. Native spectator multiplicity remains as in the full dictionary. At any fixed finite graph and nonzero uniform hopping, finitely many Z2 orbits plus strict uniqueness imply an EXISTENTIAL positive flux-sector separation. The proof supplies neither its value nor a volume-independent lower bound. At zero hopping every orbit ties and the theorem is inapplicable.

## Review boundary

The substantive points needing cold checking are the real-channel equality identity, the half-local tensor conventions and both layer-peeling inductions. No new numerical spectrum or flux scan substitutes for them. Existing L6 modular rank and rational equality fixtures remain historical independent checks. No claim of historical novelty is made; further primary-source comparison may identify this as a specialization of a known strict reflection-positivity argument.
