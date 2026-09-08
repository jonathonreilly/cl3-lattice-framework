# Uniform native virtual-pair diagonal remains constant through sixth order

## Exact scope and effective-basis convention

Use the same supplied finite low-charge carrier and H=UD+sum_e g_e A_e, where each A is the actual sorted-edge native operator sandwiched by the low projector, U>0, and P is the full ice projector. All periodic extents are even and at least four. The new result concerns only the diagonal sixth-order coefficient for uniform |g_e|=g. It does not calculate sixth-order off-diagonal rings, prove an RK point or give a volume-uniform perturbation radius.

Fix the canonical direct-rotation effective Hamiltonian on P. For the small low-energy spectral projection P(g), define Q=I-P, Q(g)=I-P(g) and

    W(g)=[P(g)P+Q(g)Q] [I-(P(g)-P)^2]^-1/2,
    H_eff=P W(g)† H(g) W(g) P.

At any fixed finite graph, sufficiently small real couplings preserve the initial gap2U separating this band; the finite Riesz projection and the displayed near-identity inverse square root are analytic. The formula maps P unitarily onto P(g). It fixes a convention: an arbitrary additional coupling-dependent unitary within P can change later diagonal coefficients. No basis-independent potential assertion is made beyond this specified natural effective basis.

## Why finite forest energies determine the full diagonal coefficient

Conjugation by physical Z_e changes only g_e to -g_e, preserves H0 and P, and conjugates P(g), W(g) and H_eff covariantly. Consequently each diagonal ice matrix element is an even analytic function of each individual g_e. A total-degree-six diagonal monomial therefore has support at most three edges, with multiplicities6,4+2, or2+2+2.

Set every other coupling to zero to extract such a monomial. Exterior edge bits are then conserved by H, both spectral projections, the direct rotation and H_eff. Any set of at most three edges is a forest, because this simple bipartite cubic graph has no triangles. For fixed exterior bits taken from an ice configuration, that forest has exactly one ice state: a leaf's degree condition fixes its active edge, then induction removes leaves. Hence the relevant P block is one-dimensional and the effective diagonal is exactly the ordinary nondegenerate ground energy of this finite active-edge matrix. This proves the connection to the global coefficient, not merely a numerical cluster analogy. All folded and reducible terms are automatically included in that scalar energy expansion.

For vertex-disconnected active sets, native ordered-star strings contain no active edge from another component. H0 and the low constraint also factor across the disjoint endpoint sets. The finite Hamiltonian is a tensor sum up to irrelevant fixed exterior signs, so its ground-energy series is additive. Inclusion-exclusion therefore removes every disconnected cluster. This is an actual factorization proof of the linked contribution.

Native phase conventions within a fixed forest may be replaced by A_j=X_j times Z on earlier incident active edges for calculating scalar energies. Both conventions have squareI and the same incident-edge anticommutators. Their edge-toggle phase ratio has trivial product around every elementary hypercube square and around backtracking, giving a diagonal unitary between them. This preserves H0, all low-support refusals and the initial basis vector up to phase. It does not replace A by bare X or remove fermionic signs. Full-background controls below independently use the original native strings.

## Local coefficients, including folded terms

Set U=1 and every active magnitude to g temporarily. Write E(g)=sum_n E_n g^n and use intermediate normalization psi_0=|0>, <0|psi_n>=0 for n>0. With R the inverse positive unperturbed energy on nonzero active states,

    E_n=<0|V psi_(n-1)>,
    psi_n=-R Q [V psi_(n-1)-sum_(j=1)^(n-1) E_j psi_(n-j)].

This exact recursion includes the energy feedback responsible for folded terms.

For one edge, two incident edges, or three edges forming a star, anticommutation cancels every allowed two-distinct-edge path from |0>. Equal-bit intermediate paths are refused in both orders; opposite-bit paths cancel. Thus V²|0>=k|0> for k=1,2,3, and the invariant bright subspace has unperturbed energies0,2 and coupling g sqrt(k). Its exact low eigenvalue is1-sqrt(1+k g²), giving E6=-k³/16. Removing all proper subcluster contributions gives

    one edge: -1/16;
    incident pair: -3/8;
    three-edge star: -3/8.

The pair coefficient includes both degree-six monomials using its two edges, evaluated at equal magnitudes. Disjoint pairs have zero connected coefficient.

For a three-edge simple path, label its edges1,2,3 in path order. Let a=1 if their initial bits alternate (010 or101), otherwise a=0. The simultaneous triple toggle is low-admissible exactly when a=1; it then has D=2. The two outer-edge toggle |d> is always allowed and has D=4. Adjacent double toggles may have D=2 or be refused, but their contributions cancel in V(|1>+|2>+|3>). Put |s>=|1>+|2>+|3>. In the convention A1=X1, A2=Z1X2, A3=Z2X3,

    V|0>=|s>,    V|s>=3|0>+2|d>,
    E2=-3/2,    psi1=-|s>/2,    psi2=|d>/4,
    E4=7/8,     <d|psi4>=-(7-a)/32.

The last equality follows from V|d>=|1>+|3>-a|123> and the recursion; the triple state's psi3 coefficient is a/8. Other adjacent-double coefficients do not enter <s|V psi4>=2<d|psi4>. Therefore

    E6=-(35+a)/32.

Subtracting three one-edge and two incident-pair contributions gives the connected three-path coefficient

    -(5+a)/32.

The exact local table covers every initial bit pattern, not only flippable plaquettes. In particular there is a configuration-dependent local alternating-path term. It must be summed before inferring a lattice potential.

## Summing all motifs on an ice state

Write N for the number of vertices and M=3N for edges. There are15N unordered incident edge pairs and20N three-edge stars. A simple three-edge path is uniquely counted by its middle edge and one other edge at each endpoint, giving25M=75N paths. Simplicity and bipartiteness ensure the two exterior vertices are distinct, including period-four tori. An additional inactive edge closing a square does not change this three-active-edge forest calculation.

For every middle edge, each endpoint has exactly three other edges whose bit is opposite to the middle bit, because an ice vertex has three occupied and three vacant edges. Thus exactly3*3=9 paths per middle edge are alternating, giving27N alternating paths independently of the ice configuration. Consequently the total sixth-order diagonal is

    H6,diag = -[3N/16 + 3(15N)/8 + 3(20N)/8
                 + (5(75N)+27N)/32] g^6/U^5
            = -(207N/8) g^6/U^5 times P.

Signs of individual couplings do not affect this diagonal, by the Z_e covariance. The assertion is for uniform magnitudes. Weighted alternating-path sums need not be constant with inhomogeneous magnitudes; they are not selected here. The diagonal at fourth order was already constant, and this sixth-order result shows that the desired flippability potential does not appear at this order either in the stated convention. Eighth order and higher, other perturbations and off-diagonal sixth-order corrections remain uncomputed. No full effective-Hamiltonian or phase claim is inferred from a diagonal coefficient alone.

## Exact controls and provenance

PREREGISTRATION.md predates calculations. The local helper uses exact rational eigenvector recursion on all active bit patterns for one edge, incident/disjoint pairs, stars, paths and a disconnected pair-plus-edge control. It keeps all low-support refusals. FULL_RESULT.json uses four actual complete L4 ice backgrounds from the preceding frozen fourth-order probe, reconstructs the entire graph, counts every star/path motif, and runs separate original-native-Pauli energy recursion on each represented bit pattern. All four backgrounds have the same diagonal total -1656 although their plaquette flippability counts differ. This supports the analytical incidence-count argument rather than substituting for it.

The preceding raw background input is hash-bound; no author implementation is imported. The present proof was frozen before reading orbital's independently assigned sixth-order work. Root supplied the target and received intermediate mechanism messages. General perturbative tools and finite linked coefficient extraction are standard mathematics. No canonical source, physical primitive or publication is changed.
