# Independent local-observable cutoff review

Reviewed primary DERIVATION.md SHA1244c9ebbe748387b0ab8784efc82db9aebbb0655a3475ddc2d393f5734957c5, without reading root's parallel sharper-tail proof. Direct primary source inspected: Nachtergaele–Sims, arXiv:1410.8174v1, Proposition2.1, Lemma2.2 and Theorem3.1 proof, especially equations71–73. This review did not rerun the author's29-control checker or claim independent verification of its internals.

Assessment: the finite-volume/local-observable theorem and its constants are mathematically sound. Two narrow source clarifications were sent to the author: identify the density-operator difference's trace norm explicitly, and specify a fixed infinite interaction family for the optional thermodynamic-limit sentence. Neither changes the finite estimate.

## Strong topology and propagation

The cited proof explicitly repairs the unbounded-onsite domain issue. The actual local spaces are separable; finite sums of bounded plaquette operators become bounded strongly continuous interactions under the onsite/support-adapted picture. Arbitrary bounded A need not preserve the kinetic domain. The review therefore uses the paper's strong-integral recursion rather than differentiating [K,A]. Its recurrence is applicable without importing a numerical velocity or a finite-dimensional truncation. The final general F-norm bound is not needed: direct face counting in the recurrence supplies the present constant.

Every cubic link belongs to at most4 elementary faces. The first face of a chain has at most4|X| choices and each successor at most4*4=16, with deliberate overcounting of shared/repeated faces. Thus a_n<=4|X|16^(n-1)v^n. The prefactor2 in the commutator series gives (|X|/2)||A||||B|| times the tail of exp(32vT). A chain of n mutually intersecting successive faces connects its endpoint links in at most n clique-graph steps, so terms below d(X,Y) vanish. Multiplying each term by exp(n-d)>=1 gives the bound exp(32e vT-d). The stated relaxed prefactor2|X| is therefore safe. At overlap, the trivial2||A||||B|| bound is sufficient. At v=0 the exact disjoint chain sum vanishes, as the proof separately retains.

The finite-volume iteration remainder is controlled by the same factorial majorant, so increasing onsite kinetic strength does not introduce another propagation constant. Removing plaquettes only reduces the chain collection.

## Boundary and region geometry

Decoupling the C crossing plaquettes changes the Hamiltonian by a bounded operator on the same free domain. Its strong interaction-picture Duhamel comparison leaves only commutators of the crossing terms with the inside dynamics. The exterior-only Hamiltonian commutes with A and contributes no error. This avoids any need for an unbounded commutator of A itself.

A crossing face has an outside link at distance at least ell+1. All links of a face are adjacent, so its nearest link has distance at least ell. This proves the stated boundary exponent, including the ell=0 overlap case. Summing the C norm-v terms and integrating for timeT gives precisely2|X|vCT exp(32e vT-ell).

Adjacent links have tail coordinates differing by at most1 in each coordinate. A ball is therefore covered by |X| coordinate cubes with at most3(2ell+1)^3 links each. Four face-link incidences per internal face and at most4 faces per link give F<=N. Every crossing face has at least one inside link, giving C<=4N. Combining these establishes the stated24|X|² polynomial prefactor. A degree-only exponential ball bound would not establish the intended spatial convergence; the proof correctly avoids it.

The optional infinite-volume norm-Cauchy sentence needs one explicit hypothesis: the finite volumes must restrict one fixed infinite retained-plaquette interaction. The finite statement allows arbitrary subsets, but toggling a plaquette near X between successive volumes would invalidate a common limit. This is a family-consistency condition, not a defect in the finite comparison. It was sent to the author for clarification.

## Energy, reference systems and normalization

The energy E is that of rho_B under H_B and is conserved only during the isolated inside evolution used for the cutoff comparison. The argument does not assume the actual time-dependent local energy in the global evolution is conserved. The global-to-local boundary step is an operator-norm estimate and hence requires no state energy or product-state assumption.

Any purification of a density operator with Tr(rho_B H_B)<infinity is in the form domain of H_B tensor I. The cutoff commutes with the kinetic operator and obeys H_B>=g_r(I-P). Consequently the omitted norm along isolated evolution is at most sqrt(E/g_r). The cross term is only PV(I-P), bounded by M=2vF. The reference is inert, so the form-domain projected Duhamel estimate survives purification unchanged. Normalizing the projected vector adds exactly1-sqrt(p), with p>=1-E/g_r. If E>=g_r, positivity of p must be supplied separately; the proof retains that condition.

For normalized pure vectors xi,eta, the trace norm |||xi><xi|-|eta><eta|||_1 is at most2||xi-eta||. Contractive partial trace and the expectation bound using that trace norm give the displayed coefficient2. The proof's phrase 'trace distance' should be replaced by 'trace norm of the difference of the normalized density operators': conventional trace distance includes an additional factor1/2. The numerical constant in the theorem is already correct.

The trivial cap2 is legitimate because the target state after successful normalized preparation and the exact state are both normalized and ||A_r||<=||A||. It would not apply in the same way to an unnormalized projected target, but that is not the theorem's final comparison. Exterior correlations disappear exactly under the reduced-state identity for inside-only dynamics; they are not thrown away by a product approximation.

## Physical boundary sectors

The full matrix-coefficient cutoff commutes with every endpoint gauge action. A globally invariant density reduces to a density commuting with induced boundary actions, which need not be supported on invariant vectors. The stated full tensor carrier is therefore essential.

A concrete analytic check is a normalized fundamental Wilson-loop wavefunction on one plaquette. Across a cut isolating one link, Schur orthogonality gives nine equal Schmidt coefficients1/3 in its fundamental matrix-coefficient block. The reduced single-link density is I_9/9 on that block, not the trivial-link vacuum. It commutes with both endpoint actions but has no boundary-singlet vector support. Thus imposing a separate singlet projector on the cut region would destroy a legal physical input. The author's formulation correctly avoids this error.

No hardware compilation, all-energy diamond estimate, uniform whole-state approximation, physical time selection or spatial-continuum statement follows. The finite proof is independent of the small-coupling stability theorem and permits any supplied finite v, with the displayed radius/time cost.
