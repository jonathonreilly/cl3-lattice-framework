# Independent quadratic electric-perturbation density bound

PASS, conditional on the already supplied operator lower bound H0 >= E0 + kappa K, kappa>0, and existence of a normalized H0 ground state with expectation D=3N/2. Here K=sum_f P_f, P_f=(1-S_f)/2, counts the 3N elementary magnetic plaquette defects. U>=0. No uniqueness, gap of the perturbed Hamiltonian, or spatial homogeneity of its ground states is required.

For any density matrix rho and Hermitian unitary W anticommuting with S=1-2P, purify rho to a vector Psi. Decompose Psi into P and (1-P) parts. Anticommutation eliminates the two diagonal matrix elements of W. Cauchy-Schwarz and ||W||=1 give

|Tr rho W| <= 2 sqrt(p(1-p)) <= 2 sqrt(p), p=Tr rho P.

This proves the inequality for arbitrary mixed states, including arbitrary correlations; it is not a pure-state assumption.

On a cubic periodic graph with each extent >=4, every edge belongs to four distinct elementary plaquettes. Two perpendicular edges at a vertex share exactly one plaquette. Two opposite edges share none. This remains true at extent4: periodic wrap does not identify the two adjacent sites, or create a second common elementary square. Each pair term W=Z_e Z_e' therefore anticommutes with exactly6 or8 plaquette cycles, respectively. There are12N perpendicular and3N opposite pairs. For a fixed plaquette, each of its four edges participates in four perpendicular pairs at each endpoint, giving32 incidences; its four corner pairs were counted twice but commute with the plaquette, subtracting8, leaving24 affected perpendicular terms. Each edge has one opposite pair at each endpoint, yielding8 affected opposite terms, with no internal cancellation. These are local arguments valid also for mixed rectangular periodic extents >=4, not an extrapolation from finite tests.

Write D=3N/2+V, V=(1/2)sum_j W_j. For each term average the preceding inequality over its m_j affected faces. Triangle inequality then gives

|<V>| <= sum_f (24/6+8/8) sqrt(p_f)
          = 5 sum_f sqrt(p_f)
          <= sqrt(75 N <K>).

For any ground-state density matrix of H_U=H0+UD, the trial state implies E_U <= E0+3UN/2. Combining this with the operator lower bound and the preceding estimate yields

kappa <K> <= U sqrt(75 N <K>).

If <K>=0 the conclusion already holds; otherwise divide by its square root. Consequently

<K>/N <= 75 (U/kappa)^2.

Since D>=0, the same trial also gives <K>/N <= 3U/(2kappa). Finally K<=3N. Thus the simultaneous bound is min{75(U/kappa)^2, 3U/(2kappa), 3}. The quadratic term improves the linear term only for U/kappa<1/50. No finite-temperature claim follows from this ground-state variational argument. For U<0 the quadratic argument can be adapted with |U|, but the stated D>=0 linear comparison does not carry over; the present theorem explicitly assumes U>=0.

The exact helper independently reconstructs the actual edge/face incidence on4x4x4,4x4x8,4x8x8,8x8x8 and verifies every pair affected-face count and every face multiplicity. These checks support the local count; they are not the proof for all extents. No physical spectral or stochastic calculation was performed.
