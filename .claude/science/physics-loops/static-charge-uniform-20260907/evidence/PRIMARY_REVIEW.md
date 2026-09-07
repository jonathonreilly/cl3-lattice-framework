# Independent cold review: sector-restricted dressed static-source bounds

Verdict: PASS for both frozen proofs, conditional on the expressly imported quantitative dressed-coordinate estimate. The argument establishes a finite-graph/source-separation-uniform weak-coupling bound for the specified external probes. It is not obtained merely from the source paper's unlabelled spectral circles. No integration worktree was edited and no numerical test is substituted for this operator review.

Reviewed:

- Native `/private/tmp/toe-autonomous-native-ladder-20260907/static-charge-uniform/DERIVATION.md`, SHA256ad23675f5c7b723a50f9501f62f132187a5174f9e1540364b2149aabcc7b0e98.
- Root `/private/tmp/toe-campaign-20260907/static-charge-uniform/ROOT_DERIVATION.md`, SHA256e6b48a8fede8f5cff1a32b2878d0ad12084325b82e5f15276f3849b0f1a2755e.

I reviewed both only after they froze. The underlying static free-sector result was independently derived in primary37 before this review; the dressed-sector candidate and source-dimension concern were exposed by root/native and are not represented as independent discovery here.

## Direct primary-paper check

I opened [Yarotsky0411042](https://arxiv.org/pdf/math-ph/0411042) and directly reread Section2, equations8–15 and their definitions. Equation8 controls H_(I,0)v_I, not just vector norm. The finite creation operators commute; overlapping products vanish, and their logarithmic coordinates are unique. Equations9–13 identify the dressed-coordinate Hamiltonian. Equation14 is a linear column bound on arbitrary input coefficient u_I, with an auxiliary decay weight and factor |I|. Fixing that decay parameter below1 and dropping weights gives the claimed unweighted estimate. The paper's preliminary hypotheses allow infinite onsite spaces, unbounded onsite operators and inhomogeneous bounded interactions. Constants depend on fixed range; no later quasiparticle assumption is needed. The source attributes this machinery to earlier work. It remains a mathematical import rather than a claimed new proof of generic stability.

## Correct identification and covariance of S

The coordinate map really is the stated S: for a bare coefficient u_I, its creation operator commutes with every ground-state creation operator, so S hat u_I Omega0=hat u_I S Omega0=hat u_I Omega_tilde. Thus the paper's coefficient expansion is exactly the bounded finite-volume similarity asserted in the proofs.

Every full gauge assignment factors over tail cells even though individual vertices act on several cells. Within each cell it is a tensor product of left/right link translations and fixes the product constant. Therefore all excitation projectors Q_I commute with gauge action. The unique interacting neutral ground can be vacuum-overlap normalized. Gauge covariance and invariance of Omega0 force its phase to1. Conjugating its creation exponential produces the same ground vector with transformed coefficients; uniqueness of the creation logarithm then fixes each v_I separately. This proves S commutes with the gauge action, which is substantially stronger than ground-state invariance alone. Tensoring S with identity on external colors preserves combined covariance.

For finite volume the nilpotent creation sum has a finite exponential and inverse. These are bounded, though their norms can grow with volume. Equation8 supplies v_I in Dom H_(I,0). Since the bra vacuum has zero free energy, [H0,hat v_I] is the bounded rank-one-on-I operator with ket H_(I,0)v_I, tensored with identity outside. The outside free terms commute. Consequently each creation operator and both finite exponential polynomials preserve Dom H0. The bounded perturbation has that same domain. This makes the similarity an operator identity, not a formal vacuum relation or a quadratic-form comparison under a nonunitary map.

## Actual graph and ghost-vacuum restriction

Completing three outgoing links per cell is valid only with the additional ghost-vacuum restriction. Both proofs include it. The enlarged Hamiltonian factorizes because no retained face uses a ghost. Its exact neutral ground is the actual ground times all ghost constants. Bare excitation projections commute with every ghost constant projector. Projecting the product ground and recursively forming its finite creation logarithm therefore leaves each coefficient in the ghost-vacuum subspace. Equivalently, phase rotations on the ghost complement fix the ground and vacuum, and uniqueness of the logarithm enforces that property. For ghosts inside I, both ket and bra of hat v_I are in vacuum; outside I it acts as identity. Thus S and its inverse commute with every ghost projector, not merely preserve one ground vector.

Ghost vacuum is also invariant under all endpoint gauge transformations, including at added dangling vertices. The joint fixed-space/ghost-vacuum restriction is exactly the original graph's charged carrier with all original boundary Gauss constraints. It cannot route charge through unused completion links. The centered scalar and the exact neutral vacuum energy cancel together, leaving precisely (a/4)(H_actual-E_vac+K_ghost). There is no extensive unpriced difference of independently approximated vacuum energies.

## Source amplification and block threshold

The external space has dimension9. Writing one coefficient as sum_alpha u_alpha tensor e_alpha and using triangle inequality gives the column sum at most c delta |I| sum_alpha||u_alpha||. Cauchy–Schwarz bounds that last sum by3||u||. This is a valid fixed factor; no complete-boundedness claim is assumed. Summing over I and using H_(I,0)>=|I| gives the relative l1 estimate kappa=3c delta.

Each Q_I commutes with the combined gauge and ghost restrictions. Therefore a vector in the joint sector decomposes into joint-sector coefficient blocks. Within each block, the all-representation occupied-component argument applies unchanged: a lone fundamental endpoint cannot be neutralized in a component, so occupied actual links connect the sources and cost at least d in scaled energy. This is a spectral lower bound on every restricted self-adjoint block, not only on a selected path vector or on an expectation averaged over blocks. In particular the vacuum coefficient block vanishes for distinct independently gauged endpoints.

## Restricted inverse and spectral conclusion

On the finite direct sum with norm sum_I||u_I||, H0's restricted resolvent acts blockwise. For 0<=z<d its graph-norm factor is at most d/(d-z); for z<0 at most1. The bounded operator F(H0-z)^(-1) consequently has norm<1 below (1-kappa)d. The inverse is ordered correctly: (H0-z)^(-1) times the Neumann series. Its first factor maps into Dom H0 with graph norm. The series acts on the coefficient Banach space; each finite-volume l1/Hilbert equivalence and bounded similarity suffices to obtain a Hilbert-space inverse. Neither equivalence constant needs to be uniform to infer absence of spectrum for each volume with the same excluded interval.

Similarity preserves spectrum, not positivity of forms. Since the original restricted operator is self-adjoint, the excluded real half-line proves the lower bound. F may mix excitation blocks but preserves their total joint sector, which is all this step requires. The proof would fail if one retained only global spectral circles; both sources correctly establish the additional sector structure before using the resolvent.

## All-coupling upper trial

For any finite v the neutral compact-group ground exists, can be chosen positive and is gauge invariant. Multiplying it by a simple shortest open transporter, with normalized source trace, gives a normalized vector in the specified charged carrier. Scalar multiplication potential has exactly the same expectation. The kinetic product rule has cross term proportional to Tr(U_P†D_(e,A)U_P)=0 because the inserted generator is traceless, for both link orientations. The extra sum of derivative squares is8/3 in the trace convention; multiplying by3/(2a) gives4/a per traversed link. A shortest path has no repeated links. Smooth bounded transporter multiplication preserves the form domain, so approximation from smooth vectors justifies the identity for the ground form vector. The resulting variational energy is exactly E_vac+4d/a. Nonnegativity of the difference also follows independently from restriction of H tensor I. No spatial-loop expectation or temporal-loop identity is used.

## Scope

No blocking mathematical gap was found in these frozen arguments. The constants are existential and geometry-dependent; static endpoint spaces, the compact Hamiltonian, couplings and time scale are supplied. The lower bound is a genuine linear finite-volume energetic separation cost in this weak-coupling model. It does not establish a unique infinite-volume potential, a charged thermodynamic state, temporal Wilson-loop reconstruction, numerical physical string tension, dynamical quark masses, continuum limit or axiom selection. The quantitative coordinate estimate and the full boundary/ghost restrictions must remain explicit in any canonical claim.
