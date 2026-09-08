# Virtual ring mechanism from a soft charge penalty on the full native carrier

This extension changes an explicit premise. Take the entire native edge-bit Hilbert space, with relaxed fixed magnetic-cycle constraints, and H(g)=U D+g V, D=sum_v Q_v², Q_v=epsilon_v(deg_v-3), V=sum_e lambda_e A_e. There is NO P_low sandwich and no refusal of |Q_v|>1. The native A_e are the same sorted-edge Pauli strings as the full dictionary, with real lambda_e and U>0. The graph is an even finite cubic torus with every extent at least four. Its ice P still has D=0; the rest has D>=2 by signed neutrality. This supplies an energy penalty and interactions, not an axiomatic choice of either.

## Fourth-order operator survives removal of the hard projection

Every departure from ice has D=2; a two-step ice return repeats the edge. Thus H2=-(sum lambda_e²)/(2U) P and the fourth folded term is (sum lambda_e²)²/(8U³)P exactly as in the hard model. Odd P-to-P words vanish by total edge-bit parity.

All alternating four-cycle permutations already lay inside the old low domain, so their denominators, native phases and summed ring coefficient are unchanged. For diagonal repeated-edge words, the only new paths are two incident edges with equal initial bits. Their intermediate D is now6 instead of being forbidden. The four irreducible words have phases -1,+1,+1,-1 with the same denominator (2U)(6U)(2U), so they cancel. Opposite-bit incident and disjoint words are unchanged. Therefore the full fourth-order effective operator is exactly the earlier one:

H4_diag=[sum lambda_e^4/8 + sum_incident_unordered lambda_e²lambda_f²/4]P/U³,
H4_off=sum_unoriented_simple_four_cycles [eta_C product_C lambda_e/(2U³)] F_C S_C on ice.

The orientation eta_C and extent-four winding cycles must still be retained. There is no nonconstant fourth-order diagonal potential. This removes the hard low-charge projection from the virtual-ring supplier at this order; it does not supply the remaining Hamiltonian or its fine-lattice implementation.

## Sixth-order diagonal for uniform magnitudes

Use the same canonical direct-rotation effective Hamiltonian and physical Z_e covariance as the hard-model proof. Each diagonal entry is even in each individual coupling; degree-six monomials therefore have at most three active edges. These supports are forests. Fixing their exterior bits from an ice configuration leaves exactly one ice state, so their coefficients are ordinary nondegenerate ground-energy coefficients. Disconnected supports factor as tensor sums. Native incident anticommutation is retained throughout.

One-edge, incident-pair and star bright subspaces remain exactly two-dimensional without the projector: newly allowed equal-bit double paths cancel in pairs as well. Their connected sixth coefficients remain -1/16,-3/8,-3/8 in U=lambda=1 units.

For three active edges forming a path, the triple-toggle state is now always present. Its energy is

D_3=2+4 m, where m is the number (0,1,2) of equal-bit internal junctions.

The two exterior endpoints always contribute1 each; an equal-bit internal junction contributes4, and an opposite-bit junction contributes0. The exact intermediate-normalization recursion gives

E6_path=-(35+2/D_3)/32,
connected_path=-(5+2/D_3)/32.

For D_3=2 this agrees with the hard allowed triple. D_3=6,10 replace the previously refused contributions. Exact rational recursion over every active bit pattern confirms these formulas with the full native Clifford signs. No bare-X replacement is used.

For each middle edge of any ice configuration, each endpoint offers three opposite-bit choices and two same-bit choices. Hence the numbers of paths with m=0,1,2 are9,12,4. Their weighted sum of2/D_3 is9+12/3+4/5=69/5, independent of the ice configuration. Summing one edges, incident pairs, stars and paths on N vertices gives

H6_diag = -[3N/16+3(15N)/8+3(20N)/8+(5(75N)+3N(69/5))/32]g^6/U^5
        = -1053N g^6/(40U^5) times P.

The full-carrier sixth scalar differs from the hard-domain value -207N/8, as it must; the difference is -9N/20. Uniform magnitudes still produce no configuration-dependent diagonal ice potential through sixth order in this convention. No off-diagonal sixth coefficient or eighth-order statement is asserted.

## Controlled fourth-order approximation

The previously derived finite-volume Schur remainder argument applies verbatim after replacing the old Q complement by the full non-ice complement: the only required properties are its gap2U, ||V||<=sum|lambda|, PVP=0, scalar two-step kernels and odd-word parity. Every one holds on the full carrier. Therefore if a=|g|sum|lambda_e|<=U/4, every ice-descended low eigenvalue is within a^6/U^5 of the actual fourth-order Hermitian operator. This is a one-sided finite spectral-distance bound, not a volume-uniform statement or a guarantee about individual eigenvectors.

The restricted no-double two-species U1 dictionary is NOT thereby extended to the full carrier: |Q_v| can now exceed1, and the diagonal identity n_c=1-Q_v² fails there. Nor is the whole |Q|<=1 subspace an isolated energy band: many simultaneous unit charges can cost more than a higher-charge configuration. Only the ice-descended low-energy cluster is isolated by the stated small-norm argument. The existing full native CAR/Z2 dictionary remains the exact parent for the entire edge space.
