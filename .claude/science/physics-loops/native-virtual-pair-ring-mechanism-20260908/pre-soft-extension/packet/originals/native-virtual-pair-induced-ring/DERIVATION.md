# Virtual native pairs induce a ring term, but not its RK diagonal partner at fourth order

## Supplied model and perturbation convention

Use the full low-charge native carrier on a finite even periodic cubic graph with extents at least four, relaxed magnetic-cycle constraints and no winding restriction. The exact native dictionary at PR8038 head86e03ef9 fixes sorted-edge Hermitian A_e, which flip their own edge bits and anticommute precisely when distinct edges meet. The physical low domain is |Q_v|<=1, D=sum Q_v². Let P be its ice subspace D=0 and Q=I-P. This Q projector is unrelated to the indexed signed charges Q_v.

The candidate Hamiltonian is supplied:

    H(g)=H0+g V, H0=U D, U>0,
    V=sum_e lambda_e P_low A_e P_low,

with real fixed lambda_e and a formal small dimensionless parameter g. No coupling, perturbation or preparation law is derived from axioms. This is a finite-volume perturbative calculation, not a uniform-volume convergence theorem. All denominators below retain the actual intermediate D, and A is never silently replaced by X.

## Exact Schur reduction and folded term

PVP=0. On Q the unperturbed energy is at least2U. For small enough g at any fixed finite graph, the inverse of Q(H(g)-E)Q exists near E=0. Solving the Q component of the eigenvalue equation gives the exact P-space Schur equation

    E p = -g² P V Q [Q(H0+gV-E)Q]^-1 Q V P p.

Put R=Q H0^-1 Q and C=sum lambda_e². Every one-edge flip from ice is low-admissible and creates D=2. A two-step return to ice uses the same edge, with A_e²=I. Therefore

    P V R V P = C/(2U) P,
    P V R² V P = C/(4U²) P.

The second-order effective operator is the constant -g² C/(2U). Odd P-to-P words vanish: all ice strings have exactly3|V|/2 occupied edges, whereas each perturbation flips the parity of the total occupied-edge count. This argument also applies inside the Schur expansion with intermediate Q projectors.

Expanding the finite inverse and using E=-g² C/(2U)+O(g⁴), the fourth-order coefficient is

    H4 = -P V R V R V R V P + C²/(8U³) P.

The second term is the folded/reducible contribution, not an optional convention. The scalar second-order and normalization operators make the coefficient unambiguous under the usual P-space orthonormalization through this order. Equivalently the displayed Schur equation itself yields the low-energy eigenvalues of g²H2+g⁴H4 through order g⁴. Its remaining finite-volume terms are O(g⁶): the P-space Schur kernel is even in g, including its E dependence. No numerical onset, system-size-independent remainder or nonperturbative equivalence is claimed.

## Fourth-order diagonal

An ice-to-itself four-step word must toggle each edge an even number of times. For a single edge repeated four times, the intermediate return after two steps is removed by R. Its only fourth-order contribution is the folded lambda_e⁴/(8U³).

For an unordered pair e,f, the words starting with ee or ff are likewise reducible. Four words remain: efef, effe, feef, fefe. If the edges are disjoint, every one has energies2U,4U,2U and positive amplitude. Their irreducible contribution is -lambda_e²lambda_f²/(4U³), cancelling the cross term in C²/(8U³).

If the edges meet and their initial bits agree, the second distinct flip would make |G|=2 at their common endpoint, and the low projection refuses all four words. If their bits differ, all four are allowed with energies2U,2U,2U. Native anticommutation gives amplitudes -1,+1,+1,-1, whose sum is zero. In either case the surviving coefficient is just the folded +lambda_e²lambda_f²/(4U³). Thus the entire diagonal is configuration independent, even for unequal lambda:

    H4,diag = [sum_e lambda_e⁴/8
               + sum_{unordered adjacent e,f} lambda_e²lambda_f²/4] P/U³.

For uniform lambda, |E|=3|V| and the number of adjacent edge pairs is15|V|, giving33|V|lambda⁴/(8U³). Projected A operators were not assumed to anticommute globally: the anticommutation was used only for the paths whose intervening low-support checks pass.

## All24 orderings of a four-cycle

A nontrivial fourth-order ice-to-ice edge change consists of a simple alternating four-cycle. Four distinct changed edges must balance their bit increments at every vertex, and a simple cubic graph has no shorter cycle. For an alternating four-cycle every ordering of its four flips is low-admissible. After the first and third flips D=2. After two flips D=2 for adjacent edges and D=4 for opposite edges. There is no intermediate ice state, so the folded term cannot contribute to this off-diagonal entry.

Number the edges in directed cyclic order0,1,2,3, but let each A_e use its canonical sorted orientation. Relative to their cyclic product, the16 adjacent-first orderings have eight positive and eight negative signs and cancel with their common denominator8U³. The eight opposite-first orderings all have negative relative sign and denominator16U³. The sum before the overall Schur minus is therefore -1/(2U³) times the canonical cyclic product.

For a directed cycle C=(v0,v1,v2,v3,v0), set

    eta_C = product_a sign(v_(a+1)-v_a),
    S_C = i⁴ A_(v0v1) A_(v1v2) A_(v2v3) A_(v3v0).

Then S_C=eta_C times the canonical cyclic product. Consequently

    H4,off = sum_{unoriented simple four-cycles C}
              [eta_C product_(e in C)lambda_e/(2U³)] P S_C P
           = sum_C [eta_C product lambda_e/(2U³)] F_C S_C on ice.

Each cycle is counted once; reversal or cyclic reindexing leaves eta_C and S_C unchanged here. F_C is its alternating-support projector. For lexicographically labeled elementary geometric plaquettes eta_C=+1, including seams. On an extent-four straight winding cycle eta_C=-1. Such winding cycles occur at the same fourth order and must not be omitted on L4. When every extent exceeds four, only geometric plaquettes have length four.

## Bare-X adverse model and relation to RK

Replacing A by bare X while retaining the same low-charge support gives no sign cancellation. Its fourth-order alternating-cycle coefficient is

    -(16/8+8/16) product lambda/U³ = -5 product lambda/(2U³).

For adjacent repeated-edge pairs its diagonal coefficient is +(lambda_e²lambda_f²)/(4U³) for equal initial bits and the negative of this for unequal bits. With uniform lambda, every ice vertex has six equal-bit and nine unequal-bit edge pairs, so this bare-X diagonal is again constant, but equals -3|V|lambda⁴/(8U³), not the native result. This is a different perturbation, not a licensed approximation to native A.

For positive canonical lambda and standard lex elementary plaquettes the native induced coefficient is positive relative to the fixed source S_p, whereas the conventional positive-J RK term J F_p(I-S_p) has negative ring coefficient. This sign is not a basis-invariant no-go. Conjugating by a product of physical Z_e changes the individual A_e signs, preserves H0 and correspondingly changes S_C. Supplied edge signs can change the relative displayed coefficient. For even cubic periods the coordinate-edge choice sigma_x=(-1)^(y+z), sigma_y=(-1)^z, sigma_z=1 has product -1 on every elementary plaquette; it can be incorporated as a supplied lambda sign pattern. This observation does not select that pattern physically.

Even after arranging the negative ring sign, the native fourth-order diagonal is a scalar, not the matching J sum F_p. The actual L4 ice backgrounds in the controls have respectively96,92,89,86 alternating plaquettes, so sum F_p is not constant and cannot be absorbed in that scalar. Thus this perturbation supplies a leading ring kinetic mechanism but does not supply the RK equality of diagonal and kinetic coefficients at fourth order. Higher orders or additional supplied interactions are not ruled out. No photon, mobile deconfinement, continuum or physical action selection follows from the calculation.

## Exact finite evidence and provenance

PREREGISTRATION.md was written before execution. Root supplied the model and independently warned about edge-sign/gauge conventions after the preliminary permutation calculation; this clarification was adopted before this final proof. Orbital's independent frozen result was announced before this freeze, but its proof and implementation have not yet been read.

The literal full L4 helper executes55576 explicit predicates under -OO in4.70s31.72MiB. It checks363 alternating plaquettes across four full ice backgrounds with all24 orderings; every intermediate D is computed from the full192-bit configuration. One complete24-order native phase/bit tape is retained. All18336 unordered edge pairs are checked for irreducible/folded diagonal coefficients, including actual low refusals. Every single-edge second-order return and folded-only fourth word is checked. A straight winding four-cycle is separate. Full background bits, graph dictionary, per-plaquette coefficients and every diagonal pair are retained. These finite controls support the general word classification and source conventions; they are not a full Hilbert census or convergence certificate.
