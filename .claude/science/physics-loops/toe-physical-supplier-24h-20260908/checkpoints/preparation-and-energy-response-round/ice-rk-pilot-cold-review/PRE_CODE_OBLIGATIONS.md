# Prospective independent code-review obligations

Proposal read: LARGER_RK_PILOT_PROPOSAL.md, frozen before production. This is not a code approval; implementation has not yet been delivered.

For momentum along a and polarization b, O=V^-1/2 sum_r epsilon(r) exp(i q r_a)(n_b(r)-1/2). An ab plaquette at r changes the root b occupation by1−2n_b(r) and the displaced b edge oppositely after staggering. Therefore Delta O=epsilon(r)(1−2n_b(r)) exp(i q r_a)(1−exp(iq))/sqrt(V). This root-polarization expression works for either ordering of a,b. L O is minus the sum of these actual changes over flippable geometric squares, not the sum of absolute values. d is half the sum of squared absolute changes. The L4,h1 complex mode must be directly compared with flipping configurations; L2 real-only checks cannot validate its imaginary sign.

Each plane includes V geometrical faces, total3V; duplicate endpoints, if any, must retain individual geometric contribution. Fourier O carries1/sqrt(V); d carries qhat²/(2V), and |LO|² carries its squared normalization. Preserve complex means and both real and imaginary source updates. Neither taking only real(O) nor replacing LO by qhat² times a count is valid.

Independent chains are the uncertainty units. Six symmetry-related modes and256 correlated samples within a chain must not become independent replicates. For ratio mu=mean(A)/mean(S), retain chain covariance through influence A−mu S; distinguish this from mean of chain ratios. Split-half comparisons within a chain require paired differences, not independent-half SE. Blocks diagnose correlation but cannot certify equilibration from common deterministic starts. Both burn protocols must survive regardless of outcomes.

Microbenchmark must include compilation accounting separately, warm timing repeats, update time, and measurement time. If randomized single-face measurements consume the dynamics RNG, expose the change of sampled trajectory or preferably use independent preselected face randomness for timing/variance comparisons. All-pairs shared-snapshot covariance must remain paired. Variance times cost is descriptive for the measured stationary-design proxy; no effective-sample claim follows without autocorrelation correction.

Check exact L2 signed moves exhaustively. L4 visited-move checks should include complex phases and every orientation, and fail actual wrong-stagger/wrong-orientation mutants. Preserve no-flip cases. The120second per-cell/384MiB limit and fixed32x256 schedule must not be shrunk after seeing runtime/results. No matrix or L4 Hilbert-space enumeration.
