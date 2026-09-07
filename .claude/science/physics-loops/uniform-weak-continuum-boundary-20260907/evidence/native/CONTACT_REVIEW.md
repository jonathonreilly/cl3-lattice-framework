# Independent cold review of actual Haar contact sharpness proofs

Reviewed after freezing own40 proof0e93e579, whose independently derived contact construction used spacing2 rather than3. The completed contact proofs were not read before that freeze. Shared candidate exposure is acknowledged. Verdict PASS.

Targets:
- Root haar-contact-scaling/ROOT_DERIVATION.md SHA59f9ab2b355d4c85b0847998007dc37374f836589f00174a5e06a177b3eb232e.
- Primary haar-white-noise/DERIVATION.md SHAdb662cb65449029d3889aae8c1d942cc4a132af2bf0120385c563713a7059d5f.

The actual xy plaquettes at3k have disjoint link sets, including different z layers. Under the u=0 electric vacuum these sets are independent Haar variables. Each holonomy is Haar by invariance under multiplying any one independent Haar factor. No independence claim for arbitrary distinct overlapping plaquettes is used. With fine spacing ell=h/3 their anchor positions are exactly hk, so the Riemann measure h³ and field normalization h^(3/2) agree.

For chi=Tr U, the normalized field X=(chi+bar chi)/sqrt2 has mean0 and second moment1: nonneutral center powers have zero integral and Schur orthogonality gives integral chi bar chi=1. Its absolute bound3sqrt2 is correct. The root optional moments also check. The unique invariant alternating tensor in3 tensor3 tensor3 gives integral chi³=1. The mixed cubic terms have nonzero center charge; hence EX³=2/(sqrt2)^3=1/sqrt2. Since3 tensor3=6 plus bar3, character orthogonality gives integral |chi|⁴=2. Only the balanced fourth monomial survives center charge, giving EX⁴=6*2/4=3. The root uses this as an exact diagnostic, not a false claim of Gaussian one-cell statistics.

Primary's explicit logarithm constants are sound: B²=18 and |z|<=1/(2B) imply |phi(z)−1|<=z²(1/2+1/12)<=1/72. The logarithmic remainder is at most z⁴, yielding cubic remainder coefficient B/6+1/(2B)=7B/36<=B/4. The estimate E|X|³<=B EX²=B is valid. Root's larger M³/6 bound is also safe. For compactly supported real q, sum|h^(3/2)q(hk)|³=O(h^(3/2)); the uniform maximum tends to zero and the discrete quadratic form converges by Riemann sums. Exact independence then gives the joint Gaussian characteristic-function limit for every finite family of real test functions, including degenerate covariance matrices.

The optional root skew correction has the correct sign i³=-i and coefficient −i/(6sqrt2) sum b_k³. Bounded fourth moment gives the stated O(sum|b_k|⁴)=O(h³) remainder after the logarithm. It is deliberately an error relative to the discrete quadratic form; no rate is attached to the Riemann-sum error for arbitrary continuous functions. The exact fourth cumulant happens to vanish, but the coarser fourth-order remainder stated is valid and needs no change.

The field operator norm grows at most polynomially, while its smeared covariance tends to integral fg and is exactly zero for disjoint supports at every mesh. Thus this is a legitimate sharpness example for the narrow separated-correlation obstruction. Both target proofs correctly claim finite-dimensional distributions only, not tightness in a random-distribution topology, dynamical convergence, a propagating field or physical noise. Own40 wording was separately tightened to the same scope after primary review; its original bytes and exact correction are preserved. No correction requested for either target.
