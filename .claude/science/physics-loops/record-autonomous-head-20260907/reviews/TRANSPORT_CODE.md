# Cold implementation review: autonomous event-epoch transport

Reviewed 2026-09-07. Read immutable scratch snapshots of the complete primary and orbital checker, and the primary's inherited CAR, spectral-group, packet-overlap and observable helper functions. Subsequently reviewed the exact source diff fixing head labels and binding live comparison. No source files edited. The native ladder checker is excluded from this review because I authored it.

## Verdict and concrete issue

No unresolved scientific calculation error found in the reviewed scope. One concrete metadata error was identified: the orbital snapshot placed the post-event head in both pre and post rows, and primary comparison did not inspect head. This would make a first-event pre row on edge 01 incorrectly say head 1 rather than head 0. Root independently identified the same issue. The final diff repairs orbital pre-head using the selected edge endpoints, independently reconstructs head from the completed prefix, and adds exact primary head and mask-convention comparison plus a head mutation. This resolves the reported issue. It did not affect the computed density/current/energy values.

Reviewed final source hashes:

- primary: c72bfb0f235e88a3a9f77eb8f9a7a3185e37661dcf3f05561356ec05c03c0fd2
- orbital: 18cc6560aea9d6dfc55ba0d755f77e4cc9b24f6a0d969ce39fdc54d4aee73bb7

## Math checks

1. Nonstationary input is retained. Primary sources are Pi_a psi for EVERY initial energy group after the local pulse; they are not probabilities or a diagonalized initial ensemble. The endpoint contraction keeps both initial energy indices coherently, with K(a-d-b+c). This gives the correct joint-battery reduction for arbitrary pure input at the same finite-system endpoint; mixed inputs extend linearly. The actual fixture remains the specified pulsed sea. Inherited grouping verifies projector completeness, eigenprojector residuals and group spread. An ungrouped output eigenbasis is legitimate even at degeneracy.

2. The telescoped shared lift uses the endpoint mask but keeps the full sum of j prior waits. Both j-pre and j-post therefore use j Laplace factors; j-pre has j-1 deletions/fuel translations. This is correct because total-Hamiltonian intertwining moves all previous dwells to the final side of that prefix. Free battery evolution leaves the reduced endpoint matter dynamics as exp(-i H_mask T) rho exp(+i H_mask T). The factor r/(r+i(b-c)) has the correct sign.

3. Primary EB is a direct joint moment contraction: for fixed output energy b its cross term is [48.5+(a+d)/2-b]K(a-d), then k Delta times trace is added. This is the analytic translated-packet first moment, not EB inferred from the ledger. Orbital EB independently integrates absolute squares of complete determinant amplitudes on battery energy intervals. Degenerate initial many-body groups are coherently summed; all groups and complex phases are retained. Fuel enters once as k Delta. The ledger then independently compares matter plus battery plus remaining fuel.

4. The orbital one-body reduction is valid without assuming the final state is Gaussian. For each Fourier fiber the initial Slater is propagated by a one-body unitary; integrating those fiber states yields a mixture of Slaters. Its covariance is the linear average implemented by the four-index kernel. The battery calculation separately uses all 70 determinant configurations and does not reconstruct a many-body state by pretending the averaged covariance is a pure/Gaussian state.

5. Physical coefficient and current conventions match. Orbital EDGES stores s=-h_uv; its 2*s*Im(C_vu) equals 2*h_uv*Im(C_uv), matching the inherited oriented current operator. The pulse signs exp[-i0.7(n0-n1)] match both implementations. Independently checked initial one-body spectrum: four eigenvalues -sqrt(3), four +sqrt(3), Fermi gap 2sqrt(3). Thus the many-body filled negative band is unique despite orbital degeneracy.

6. Exact graph path weights are products of reciprocal current live degree. All first-four paths have rate sequence (3,2,2,2); hence the orbital checker may use the common j-stage waiting density without averaging distinct rates. Primary additionally retains terminal graph mass. First-four connectivity ensures all native signs are nonbridges; sign multiplicity cancellation for these CAR observables is justified. The graph-only continuation does not extend the fair-sign assumption through later bridges.

7. Independently verified the orbital four waiting-density formulas and tail formulas against a transient phase-type generator matrix exponential at t=.001,.01,.09,.1,1,4,20 for each j. Maximum density discrepancy was 1.60e-14. At t=20, the j=4 tail is 9.724482890292394e-15, agreeing with the independent survival calculation. Numerical quadrature convergence is not itself a universal rigorous error certificate; the explicitly computed tail is separate and tiny at this fixture.

8. The broad cap enclosure from ||A_R||<=24 is sufficient: initial total support is inside [24,73], and any output system energy in [-24,24] gives battery support in [0,97]. The actual endpoint support uses complete initial/output spectral extrema plus k fuel shift and is conservative. Orbital support also includes zero-amplitude groups, which can overestimate support but cannot incorrectly certify a cap that truncates nonzero amplitude. No finite-ladder simulation is substituted for the continuous cap proof.

## Benchmark interpretation

The primary benchmark_failures fields count failed ROW SURFACES among the 90 path/event-side rows. The reported 71 support failures must not be described as 71 independent full trajectories or 71 statistical trials. Earlier prefixes recur across full trajectories, and pre rows are explicitly tagged with a future selected edge; this tagging is legitimate because edge choice is matter-independent and the repeated row weights sum correctly.

Support floor four is checked per surface using live-edge |J|>=0.02. The path front comparator is a different operation: max over the four selected-edge j-pre absolute currents >=0.05. Current source explicitly reports trajectory_front for the 24 full paths and all_pre_support_ok; the latter checks four pre surfaces, not all eight pre/post surfaces. Root's stated 24/24 trajectory-front passes and 0/24 all-pre-support passes are consistent in meaning and do not contradict 71 failed support surfaces. Do not equate the per-j summary front_max across different paths with a single trajectory front maximum.

## Review limits

This was a cold formula/code review plus an independent waiting-density diagnostic, not a rerun of all 90 primary/checker numerical rows or a new audit verdict. Final narrow diff was reviewed after the snapshots. The primary's live comparison binds all 90 observables, masks, rates, exact weights, fuel and now head. Runtime execution receipts remain owned by root and the implementing agents. No claim of spatially local implementation, Gaussian closure, universal transport success, or conditioned-sign battery monotonicity is inferred.
