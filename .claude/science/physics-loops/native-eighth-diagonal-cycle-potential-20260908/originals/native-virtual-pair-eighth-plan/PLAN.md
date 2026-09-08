# Prospective bounded eighth-order diagonal plan — no execution

Same supplied native low-charge Hamiltonian, U>0, uniform real magnitudes, simple even cubic periods>=4. Fix the canonical direct-rotation effective Hamiltonian, not an arbitrary coupling-dependent basis within ice. The target is only its degree-eight diagonal, with no promise to compute all H8 or determine a phase.

## Exact coefficient extraction

Physical Z_e covariance makes each diagonal entry even in each independent coupling. Degree eight has multiplicity partitions8;6+2;4+4;4+2+2;2+2+2+2. Hence at most four active edges suffice. Set other couplings to zero, keep actual fixed exterior ice bits and the low projector, and extract degree eight before restoring uniform magnitude. Inclusion-exclusion over proper subsets isolates terms supported on all active edges. For four edges, the all-supported degree-eight term necessarily has each edge twice, so uniform-coupling inclusion-exclusion identifies that monomial without multivariate differentiation. Smaller subsets supply all their degree-eight terms together; no need to pretend they have only one monomial.

Vertex-disconnected active components factor, so their connected contributions vanish. Connected sets of four edges on this triangle-free graph are three trees (four-star, length-four path, and the degree-three/degree-two fork) or a four-cycle. Smaller connected forests are also required for subtraction. An inactive chord between vertices of an active tree does not spoil unique-ice leaf induction, but its presence matters when counting embeddings globally.

For forests the fixed-exterior ice subspace is one-dimensional. Exact rational eigenvector recursion with energy feedback therefore yields the canonical diagonal, including folds, as in order six. Enumerate all initial active-bit patterns that admit exterior ice completion; using all patterns locally is harmless only if the global embedding filter is separately supplied.

## The cycle requires a different argument

For an alternating four-cycle, fixed exterior occupation at every cycle vertex is two. There are TWO ice states, related by toggling the whole cycle. Scalar nondegenerate recursion around either one is invalid. Use the exact two-dimensional P projector and a formal Riesz-projection/direct-rotation expansion through order eight, or a rigorously equivalent symmetry shortcut.

Candidate shortcut to prove before using: the native cyclic product S commutes with each active A_e because each has two incident anticommuting neighbors; the full-cycle toggle maps each degree deviation to its negative when the exterior degree is two. It therefore preserves H0 and the low domain. S exchanges the two P basis vectors. Covariance of the canonical direct rotation would make its two diagonal entries equal. Each is then half the trace of the two-band effective Hamiltonian, equivalently half the sum of its two low eigenvalues. A contour-resolvent trace expansion can extract this sum rationally without choosing eigenvectors or confusing the order-four splitting with a diagonal term. Establish all these symmetry statements with actual orientation/phases first. Nonalternating cycle inputs have only one ice state and can use scalar recursion.

## What is needed before claiming an F potential

A nonzero connected cycle difference between alternating and nonalternating patterns is not by itself the full lattice potential. Four-edge trees may have configuration-dependent local coefficients whose embedding sums cancel, reinforce, or produce another observable. Compute the complete local table, then reduce the global sum using degree-three ice identities and explicit motif incidence. At order six the alternating-path table was nonconstant but its lattice sum was constant; that failure mode must be retained.

A defensible intermediate result is an exact local cluster table and its canonical convention, not a statement that the lattice has an RK partner. To establish a coefficient multiplying sum F_p, prove a decomposition of the complete diagonal into a scalar plus that observable (or list the additional independent local observables). Test any proposed identity on distinct globally completed ice backgrounds with differing flippability, but do not treat a finite fit as proof. Period-four winding cycles are distinct active cycles at the same order and must be retained or the graph restricted prospectively to periods>4. Uniform coupling signs disappear from diagonal terms, but do not disappear from offdiagonal rings.

## Bounded controls and stopping points

Each active cluster has at most16 edge-bit states, before low projection. Exact rational arithmetic and finite symbolic series should suffice under180 seconds/384MiB per command. No full L4 Hilbert enumeration or stochastic job is contemplated. Freeze formulas and expected symmetry before execution. Adverse controls should remove energy feedback, replace native phases by bare X, and incorrectly use a rank-one cycle P; each must be tested against a predicate it can actually affect. If the two-band canonical extraction or global motif reduction is not closed, stop with that named obligation rather than reporting a potential from an unfixed effective basis.

No computation has been performed under this plan.
