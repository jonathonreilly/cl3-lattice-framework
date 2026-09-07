# Prospective finite spectral check contract — block33

Read parent cutoff proof SHA256 f3a2a22c4f0284d98c751a37987282d5bb56416ff946faf501216cb6ac9da47f. This contract is frozen before new matrix calculations. The analytical candidate was sketched before this contract, and that timing is disclosed.

Assume a nonnegative self-adjoint compact-resolvent H=K+V, 0<=V<=M, finite orthogonal P commuting with K, and QKQ>=gQ with g>0. Work on the full or exact physical reducing Hilbert space. Set A=PHP, B=PVQ, D=QHQ and b any proved bound on ||B||. For E<g, the Feshbach complement A-E-B(D-E)^(-1)B* should yield Ritz eigenvalue bounds, with indices counted with multiplicity and excluded-state counts explicit. No global spectral approximation or invented compact-model physical input is intended.

Targets: prove E_j<=mu_j and mu_j-E_j<=b²/(g-E_j) when E_j<g; derive computable lower endpoints and two-sided first-gap interval, retaining ground subtraction. Test whether positivity improves b<=M/2. Prove a threshold eigenvalue-count bracket and exhibit its unresolved boundary band.

Frozen exact controls: two-dimensional K=diag(0,g), V=[[1,1],[1,1]], g=10, giving an actual nonzero Ritz error; diagonal uncoupled controls with one excluded level to expose index misuse above g; a three-dimensional K=diag(0,1,10), V=outer((1,1,1),(1,1,1)) with P first two coordinates for gap/ground-subtraction checks; g=1/4 two-dimensional counterpart to exhibit a vacuous positive-gap bound, rather than hide it. Exact symbolic eigenvalues or certified rational sign inequalities only. These are abstract operator controls, not substitutes for Haar plaquette calculations. Preserve any failing candidate and do not tune parameters.

No repo edits. Derive the form-domain Schur inertia statement and finite-rank index conditions before claiming a theorem. Root owns publication and other workers' results.
