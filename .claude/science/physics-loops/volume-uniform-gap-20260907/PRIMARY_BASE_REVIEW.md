# Independent applicability review: volume-uniform electric-dominated gap

Verdict: PASS for the clarified native proof and the independent root proof, in their stated fixed-lattice, sufficiently small supplied av scope. This is an independent mathematical applicability review, not an audit verdict or a reconstruction of the imported stability theorem. No finite-cutoff extension is reviewed here.

Reviewed files:

- Native DERIVATION.md SHA256 `23de61b434e797d65a11c1404105bae7908fd791d80f476b30bdedcd8213f991` in `/private/tmp/toe-autonomous-native-ladder-20260907/volume-uniform-gap/`.
- Root ROOT_DERIVATION.md SHA256 `5d896bf767fbc700784048a09c0f4dabacc523e902960b3ce74acc8d3c6ae861` in `/private/tmp/toe-campaign-20260907/volume-uniform-gap/`.
- Native original a8921b35 version is preserved as DERIVATION_BEFORE_ALL_LABEL_CLARIFICATION_a8921b35.md. I inspected its explicit diff. The clarified all-label argument closes the omitted-representation justification; the corrected interpretation of a is appropriate. This verdict binds the clarified version, not silently the original wording.

## Primary theorem inspection

I opened the primary [Yarotsky paper](https://arxiv.org/pdf/math-ph/0411042) directly and inspected printed pages2–4 and section2 beginning on printed page6, also checking the saved PDF (SHA256 b0f7c876b690f0fdc7730a88100c5b841352ed339369fe57fa9497c53d6019f3). The hypotheses explicitly allow infinite-dimensional site Hilbert spaces and unbounded nonnegative self-adjoint onsite operators, with unique vacuum and gap at least1. Perturbations are bounded self-adjoint operators supported in shifts of one fixed finite set. Translation invariance is introduced only after Theorem3 for the subsequent quasiparticle results. Thus inhomogeneous perturbations are permitted here. Equation(3) is whole-range inclusion; boundedness preserves the free finite-volume operator domain. Theorem1 gives shape-dependent constants and the centered spectral gap; Theorems2–3 supply the state limit and weak-resolvent GNS limit with that gap. The paper attributes Theorems1–3 to references[1,10,23]; section2 reviews them and directs detailed proof to[23]. The claimed import and attribution are accurate. No quasiparticle assumption is needed.

## Independent mapping checks

Every positively directed cubic link belongs to exactly its tail cell. Three links per cell therefore give L2(SU3^3), with no class-function truncation or Gauss projection at a cell. For F(p,q)=p²+pq+q²+3p+3q, increasing p changes F by2p+q+4>0; increasing q gives p+2q+4>0. All nonzero labels dominate (1,0) or(0,1), where F=4. Hence the unique three-link constant vacuum has scaled gap1 for h_x=(a/4)K_x, with all labels covered. Compact resolvent is valid but not needed for the stability import.

The ij plaquette uses tail cells x,x+e_i,x+e_j. Grouping its three choices at x fits {0,e1,e2,e3}. Because each normalized real trace has modulus at most1, the centered group norm is at most3av/4. This is a local bound; using a global norm would fail uniformly with volume. Removing constants affects no gap. Multiplying the imported centered bound by4/a gives at least2/a under the disclosed existential smallness condition. No numerical threshold is inferred.

The whole-range rule is not conventional individual-face inclusion: side length2 gives3 grouped faces versus6 individually supported faces. Outgoing links reaching outside the cell set cause no problem: their endpoint gauge actions are included, and every retained face still closes. The proof explicitly retains this boundary convention for the thermodynamic construction.

The finite-graph padding lemma is valid independently. Give all missing links free kinetic factors, choose a sufficiently large complete-cell volume, and set unwanted plaquette terms to zero. Each nonzero group remains bounded by3av/4 and uses the same allowed shape. Exact factorization into the desired finite graph and extra free link Hamiltonians implies the desired gap is no smaller than the enlarged-system lower bound. Site-dependent perturbations are allowed by the primary theorem. No infinite-volume theorem is applied to the graph-dependent family.

## Physical sector and domains

Finite bounded real potentials preserve positivity improvement of the compact elliptic heat semigroup, so the unique normalized positive ground is gauge invariant. Restricting a reducing subspace containing that ground preserves the lower gap; it need not preserve the exact first eigenvalue.

For infinite volume, finite-support gauge automorphisms preserve the limiting state. Their canonical GNS unitaries fix the cyclic vector. Applying the imported weak-resolvent matrix-element limit to transformed local A,B passes finite covariance to the limiting resolvent. The joint fixed space is consequently closed and reducing and inherits the gap. This argument avoids applying an unbounded Hamiltonian directly to arbitrary local bounded-observable vectors, and needs no infinite Haar projector.

The optional normality argument also checks. Remove one onsite term and at most four incident perturbation groups. Comparing the exact ground with a vacuum-at-that-site trial state yields <h_x> <=8epsilon. For any finite set, its summed onsite Hamiltonian has compact resolvent. The bound makes local density matrices trace-norm tight (the off-diagonal truncation error is controlled by the square root of the omitted mass). Their bounded-observable limit is therefore normal. Local normality yields strong continuity of finite gauge actions in GNS: first on dense local-observable vectors using normality on a larger finite region, then by uniform boundedness. Averaging a local observable over its finitely many incident vertex groups preserves its link support. The resulting vector is the group average of the original GNS vector; for an invariant target this contraction cannot worsen the approximation. This justifies the optional fixed-space/cyclic-invariant identification. It is not needed for the minimal fixed-space gap claim.

## Scope and adverse checks

The conclusion uses an external mathematical theorem and supplied action, couplings and lattice. It does not select a physical coupling, identify a with a spatial continuum parameter, establish arbitrary-coupling stability, classify all infinite ground-state representations, or prove a continuum Yang–Mills/QCD gap. The constants are existential and depend on the fixed interaction shape. No finite-dimensional simulation proves the theorem. No runner rerun was needed for this proof review; the geometry and normalization were checked directly above.

No correction is required to the reviewed clarified proofs. Preserve the original all-label/parameter clarification history and the boundary adverse case in any canonical package.
