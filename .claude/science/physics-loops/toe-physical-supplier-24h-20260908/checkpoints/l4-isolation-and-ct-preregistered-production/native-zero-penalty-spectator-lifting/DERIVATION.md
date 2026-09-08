# Delayed spectator splitting at the zero-penalty endpoint

Conditional theorem. Let the finite graph be a rectangular cubic torus with all three extents even and at least four. Use the full native dictionary, with no low-charge projection. Let H0 be the supplied U=0 Majorana hopping Hamiltonian. Assume an eigenvalue E0 of the FULL H0 has eigenspace P contained in one magnetic flux orbit and, in that orbit, consists of a unique full-rank active Majorana vacuum tensored with its allowed spectator parity space. Assume E0 is isolated from every other full-H0 eigenvalue. These are additional spectral hypotheses; flux optimization does not establish them. The small parameter here multiplies D and is not the large-charge-penalty expansion.

Under these hypotheses, the positive-overlap canonical effective Hamiltonian of H0+uD on P is scalar through order FIVE in u. In particular it is scalar through orders two, three and four requested initially. Order six is the first order at which the elementary support and parity rules permit a non-scalar contribution. No nonzero sixth-order coefficient or actual lifting is proved.

## Operator selection rule

In the full dictionary, D=3N/2+(1/2) sum_v sum_{e<f incident v} Ze^g Zf^g. Each nonconstant insertion toggles exactly two incident link-X signs and leaves the matter state unchanged before returning to a chosen gauge representative. H0 and all its resolvents are block diagonal in link-X configurations and involve only even products of active gamma Majoranas.

Take an ordered perturbation word, allowing reduced resolvents, unperturbed spectral projectors and powers thereof between insertions. Its final link toggle F is the mod-two sum of its electric pairs. Returning to the original magnetic orbit is equivalent to F=delta S for a vertex subset S. This equivalence uses the complete cycle fluxes: orthogonality to every cycle is exactly the cut space over F2.

Use an unreduced link-X representative along the word. No intermediate gauge choices are needed. On closing the orbit, the Gauss relation identifies the toggle delta S with the matter operator P_S=product_{v in S} P_v. Each P_v is, up to the fixed convention sign, i gamma_v bar-gamma_v. Therefore a returning word has spectator factor product_{v in S} bar-gamma_v and active factor comprising product_{v in S} gamma_v and even active resolvent functions. The active parity of this factor is |S| modulo two. Since the active vacuum has definite parity, every odd-|S| contribution vanishes after projection onto it. This conclusion does not require Gaussian factorization of a many-point correlator.

If S is empty, the projected active matrix element is a scalar and the spectator factor is identity. If S is the full vertex set, total physical matter parity is +1, so it is the same identity action. Complementary cuts give the same physical result. For other even S a spectator operator is permitted but its coefficient is not determined by this selection rule.

Reduced resolvents introduce no extra spectator operation. Within the starting orbit, the removed projector is the active vacuum projector extended by the identity on spectators and then restricted to even total matter parity. In other link sectors, the resolvent remains a function of an even active quadratic Hamiltonian. The argument thus also covers returns to the starting orbit in the middle of a word.

## Elementary small-cut classification

For a subset S write m_a for the number of coordinate-a circular lines containing both S and its complement. Each such line contributes at least two boundary edges, hence |delta S| >= 2(m_1+m_2+m_3).

Suppose |delta S| <= 10 and S is proper and nonempty. No m_a can be zero. Indeed, if m_a=0, S descends to a nonconstant binary function on the other two-coordinate torus. Such a function has at least two mixed coordinate lines in total: if only one direction varies, at least four parallel lines are mixed; otherwise each direction contributes one. Lifting multiplies this number by L_a>=4, contradicting sum m <=5.

Consequently all three m_a are positive, their sum is at most five, each is at most three, and at least one, say m_a, equals one. Slice in a different coordinate b, with remaining coordinate c. A nonconstant (a,c) slice must contain a mixed a-line: otherwise it is constant along a and any c variation would generate at least L_a>=4 mixed c-lines, exceeding m_c<=3. There is therefore exactly one nonconstant slice. There must be at least one because otherwise a nontrivial stack of constant slices gives m_b=L_a L_c>=16.

All constant slices have the same value; two opposite constant slices would again make every b-line mixed. Let T be the sites in the exceptional slice differing from that common value. Exactly those b-lines are mixed, so |T|=m_b<=3. Thus S or its complement has at most three vertices. A three-vertex subset has at most two internal edges (the graph is simple and triangle-free), and hence boundary at least 18-4=14. A two-vertex subset has boundary 12 unless adjacent, in which case it is 10. A singleton has boundary six.

This proves: every nontrivial cut of size at most ten is a singleton/complement cut or an adjacent-pair/complement cut. In particular every nontrivial even-cardinality cut has size at least ten. This proof does not use an assumed isoperimetric classification or a small-subset census in place of the arbitrary-subset argument.

## Orders and the fifth-order obstruction

At n insertions the toggle support has at most 2n edges. For n<=4, the small-cut classification leaves only empty/full S (scalar) or singleton/complement S (odd and vanishing). At n=5 the only additional possibility is the boundary of adjacent vertices v,w, containing ten edges.

To reach a ten-edge support in five two-edge insertions, every boundary edge must occur exactly once, with no repeated or internal edge. The ten boundary edges form two disjoint five-edge stars for purposes of incidence matching: no edge from one star shares an endpoint with an edge from the other, since adjacent vertices have no common neighbor in this triangle-free graph. Five edges at either star cannot be partitioned into incident pairs. Thus five allowed D insertions cannot realize this cut at all.

At six insertions this particular combinatorial obstruction disappears. At v pair the internal edge vw with one of its five external edges, and pair the other four external edges among themselves. Do the same at w. The six allowed electric pairs toggle all ten boundary edges once and the internal edge twice, giving delta{v,w}. The corresponding spectator factor is a bilinear and active parity is even. This establishes only an allowed support, not a surviving sum over resolvents or a nonzero coefficient.

## Canonical normalization and limitations

Finite isolated spectral perturbation theory supplies the contour projector Pi(u). Let A=P Pi(u) P and B=P (H0+uD) Pi(u) P. The positive-overlap canonical Hamiltonian is A^(-1/2) B A^(-1/2). Every coefficient of A and B is a finite sum of the words considered above. Up to degree five each is scalar on P. Formal power series multiplication and the analytic inverse-square-root expansion therefore remain scalar through degree five. Folded terms and normalization cannot manufacture an earlier spectator splitting. The scalar constant in D does not alter this conclusion.

This is not a claim that the isolated-eigenspace hypothesis holds for the flux-minimizing cubic model. A degenerate energy shared by distinct flux orbits requires including all those orbits in P; inter-orbit matrix elements are then not constrained to returning cuts, and the present theorem does not apply. Active zero modes likewise invalidate the unique-active-vacuum premise. No radius, coefficient, thermodynamic stability, spectator gap or phase is asserted.
