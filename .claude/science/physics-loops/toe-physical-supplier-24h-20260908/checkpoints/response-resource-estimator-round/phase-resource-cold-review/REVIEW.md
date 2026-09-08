# Independent phase-resource review

PASS for DERIVATION.md SHAed18418686844f2da6c90e9bae77136fa39a85d52c09b83a7b2d622a3e6ba42c within its stated finite, classical-history, real-ready resource domain. No blocking correction found. The estimate is necessary, generally loose, and is not an optimal native gate or physical work cost.

## Coverage and independent evidence

Read complete derivation, preregistration, check.py and RESULT.json. The dimer_input_copy.py is byte-identical to phase-preparation/check.py SHA c767cfad..., already completely reviewed with an independent CAR calculation earlier in this same campaign. Verified that identity again. Read complete boundary-preparation/DERIVATION.md used for the real-code premise; actual source native A/B/T/code dictionary and phase import were checked in preceding phase/source-action reviews. I did not rerun author check.py because it writes its copied dependency; no author files changed. SOURCE_HASHES.json records complete artifact coverage.

Directly consulted primary Wu et al. https://arxiv.org/html/2103.01805, definitions of squared fidelity/convex roof, Propositions3–5 and their relevant proofs. Pure formula, convex roof strong monotonicity and trace-norm robustness are prior art, as the author says. The native application below can also be verified from the direct finite arguments, with no implicit Onsager or thermodynamic import.

My independent.py imports no author code and passes14 exact controls. It uses a different5-dimensional imaginary-H Gibbs example with energies +/-1,+/-2,0, explicit optimal real-block ensembles, a different complete real instrument, a saturating single phase pulse, classical-versus-coherent flag phases, expected-cost adverse, and rational dimer constants. This finite evidence supplements, not proves, the general argument.

## Quadratic budget proof

For pure psi=a+ib after a global phase, a and b may be orthogonal with ||a||>=||b||. The largest real-vector overlap is ||a||² and Ig=||b||². For any real Kraus K, the candidate real direction Ka/||Ka|| gives a comparison overlap at least ||Ka||², even if Ka and Kb are not orthogonal. Summing over complete Kraus effects bounds average output Ig by ||b||². Zero Ka terms are simply omitted. Convex-roof refinement establishes the mixed-input result. Tracing a real environment and coarse-graining successful outcomes are legitimate real instruments/channels; therefore the success probability factor cannot be dropped.

A real density has a real finite purification. Real Kraus instruments have real isometric dilations with outcome/environment flags retained. Because declared histories never coherently recombine, each controlled branch pulse may be recentered by its own scalar without changing any conditional density or probability. One may select this centered dilation for the proof; it need not match a hypothetical coherent source-control experiment. My explicit two-flag control confirms that those phases would matter if coherently recombined, so that exclusion is load-bearing.

At layer l the centered block-diagonal controlled generator has norm at most max_branch gamma_l. Its unitary moves every purified vector through Fubini–Study angle at most that value. Comparing consecutive hybrid circuits with common remaining unitaries preserves angle; real isometries also preserve it. The triangle bound then compares the full output to a real vector at angle <=Theta. For Theta<=pi/4 this implies Ig<=sin²Theta, and Ig<=1/2 covers the remainder. This justifies the exact clipped expression. No independent branch phases or environment resources have been charged twice.

This proof uses sum of layer maxima. It does not establish substitution by a maximum path sum or an expected path sum. Identity padding makes the chosen layering explicit, not canonically optimal. The reported rare-branch counterexample correctly defeats the mean-square replacement. Many individually small pulses can have finite summed angle, so the bound cannot exclude that route.

## Native Gibbs value and fidelity convention

On a real invariant code with H*=−H and the fixed scalar zero, a real orthogonal block transformation gives imaginary2-by-2 skew blocks and zeros. Each normalized Gibbs pair has Bloch y=tanh(beta E). Every pure qubit ensemble has average y fixed, and convexity of g(y)=(1−sqrt(1−y²))/2 gives the lower bound. Two pure states with that y and opposite real Bloch coordinates attain it. Real block measurement plus ensemble assembly proves exact additivity over these flagged blocks, including zero modes and odd code dimension. Consequently Ig=(1−d/Z)/2.

Equivalently rho rho*=P/Z², so ROOT fidelity Tr sqrt(sqrt(rho)rho*sqrt(rho))=d/Z. The literature's fidelity itself is the square of this quantity. The author variable rootF is correctly named and used; substituting squared fidelity would be wrong. My independent5-dimensional example has Z31/4, root fidelity20/31 and Ig11/62, with a matching explicit ensemble. Native dimer Ig32/289 and weighted value32/625 check exactly. The arbitrary scalar shift caveat is essential, because H*=−H would fail after that shift although the normalized Gibbs state is unchanged.

The d here is the dimension of the represented real invariant ready/code sector, not total unconstrained physical dimension and not an incorrectly doubled Fock space. The prior parity-reservoir identification supplies the path's full matter functional; that conditional source result is not newly derived by the resource bound. beta0/nonzero-H and zero-mode cases are correctly scoped.

## Expected robustness and approximation

R=.5||rho−rho*||1 is strongly monotone under a flagged real instrument by trace-norm contraction on Hermitian differences. Splitting U rho U† minus U* rho* Uᵀ first yields R(rho), and the remaining half trace norm is bounded by the distinguishability of relative unitary U†U*=exp(2i theta D). Its spectral arc gives sin(2gamma) through gamma<=pi/4 and the trivial bound1 thereafter. Weighted node increments telescope along the actual adaptive tree, yielding the stated linear expected budget, with actual reach probabilities. This argument does not invoke quadratic expected-angle control.

Ordinary trace distance epsilon changes R by at most2epsilon. For a pure state R=2sqrt(Ig(1−Ig)); convexity of R and concavity of that function applied to an optimal convex-roof ensemble imply Ig>=g(R) for mixed states. Thus the approximate-output substitution is valid but can be loose. It does not assert unproved continuity or optimality of the convex roof.

## Disposition

All claims survive independent scrutiny under the real input/real ancilla, supplied phase pulse, complete real instrument, finite classical adaptive-history and explicit layer-budget assumptions. They do not select h, beta, phase controls, Born values, occurrence or energetic implementation. No stronger pathwise budget, native compiler optimality, physical work lower bound or universal quantum-control obstruction follows.
