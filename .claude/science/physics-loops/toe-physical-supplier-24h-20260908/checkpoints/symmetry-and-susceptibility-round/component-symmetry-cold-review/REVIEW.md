# Independent component-symmetry cold review

PASS for DERIVATION.md3d0bcc08b196de13704a5004d92e21a857e8a557d9a4d5fa21d7902f064594cc and check.pya96be1a2 (full hash bound in RESULT.json). Complete proof, preregistration and executable read; raw path/result inspected. This is a constructive theorem about the supplied even-periodic binary ice component, not an axiomatic Record theorem or an ergodicity result across zero-flux components.

## Independent construction

For translation axis j choose k=(j+1) mod3 and remaining l. Use plane(j,k), with root parity layers (r_j,r_k,r_l)=(0,1,0),(0,1,1),(1,1,0),(1,1,1). This is derived directly from occupations rather than importing the author's BFS paths. In the first two layers the j=0 links toggle0→1 and the k-links at k=1 toggle1→0. The last two layers toggle j=1 links1→0 and toggle those k-links a second time back to1. The endpoint therefore changes every j-link and no other link, exactly tau_j seed.

Within one layer all roots have fixed parity. Sharing a unit-face edge would require a root separation by one coordinate step in its plane (or equality), which cannot occur between distinct same-parity roots on an even torus; transverse separation also gives distinct edges. The layer has(L/2)^3 faces. Each layer boundary is2-periodic, so all faces have the same four-bit legality as its L2 representative. Edge disjointness preserves legality throughout arbitrary sequential execution. This proves4(L/2)^3 legal flips for every even L, not merely tested sizes.

Own check.py implements this direct four-layer prescription in array coordinates, with no BFS or L4 enumeration. It checks all three axes at L2,4,6,8, every face legality, disjointness, intermediate2-periodicity, translated/reflected target equality, final degree3 and actual staggered plane flux0. This extends finite diagnostic sizes but is not used as a substitute for the preceding general proof.

## Symmetry and operator action

Translation sends legal paths to legal paths. Since translated seeds are connected to the seed, translating any state/path in C_L stays in C_L. The inverse translation gives equality. This explicitly closes the otherwise missing step from full-Hamiltonian symmetry to restricted-component symmetry.

With undirected-link reflection, (R_j n)_b(r)=n_b(R_j r-delta_bj e_j). On the parity seed this toggles only direction j, the same target already constructed. Reflection and coordinate permutations preserve the legal face graph, so their component actions are valid. No spin-orientation sign was silently substituted for the actual occupation permutation.

Changing variables in the Fourier sum gives O_ab(tau_j n)=-exp(iq delta_aj)O_ab(n). Even L makes stagger periodic, and allowed torus momentum makes the seam phase consistent. A transverse j!=a has character-1 even at q=pi, whereas the longitudinal character at pi is+1. Thus a longitudinal-only argument would fail precisely at that endpoint. Own direct controls on fixed legal-path configurations verify translation and reflection actions for q0,qmin,qpi. The reflection equation for a!=b is O_ab(R_j n)=(-1)^delta_bj O_ab(n), with complex conjugation additionally when j=a. A nonzero qpi witness is checked, avoiding a zero-observable phase test.

## Elastic conclusion and limits

For finite C_L the hopping adjacency is connected and off-diagonal matrix elements of H are nonpositive. cI-H is nonnegative irreducible for sufficiently large c, giving a unique normalized strictly positive lowest vector. This holds for finite real V and translation-invariant real diagonal source; the proof does not require V<=1, which is instead a particular stochastic-kernel constraint. A component translation is a basis permutation commuting with H, so it fixes that unique positive vector. The transverse character-1 then forces the pure mean exactly zero. At RK the same argument applies to the uniform component state.

Consequently raw |O|² has no ground-state elastic mass in this finite supplied component and invariant source family. If its weight is nonzero, its exact first spectral moment is an upper bound on the minimum supported positive excitation energy. This is not an equality, a pole, a global-across-components gap, or a statement that finite stochastic ratios are certified bounds. Translation-breaking sources/preparations and other components remain outside the conclusion. The frozen L4 report's earlier elastic caution was appropriate before this proof; it should not be rewritten as if this symmetry had been established before its run. No correction to the author proof is requested.
