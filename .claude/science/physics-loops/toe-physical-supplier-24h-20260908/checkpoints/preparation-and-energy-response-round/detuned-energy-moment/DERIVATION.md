# Detuned pure oscillator strength from mixed-energy response

Conditional positive estimator design, 2026-09-08. No stochastic production has been run in this directory. This is the supplied spin-half ice source, not the native fermionic carrier or a physical Maxwell identification.

## What is new relative to the inspected sources

The current-main finite-detuning projector note proves E0=(V-1)<Nf>mixed and the exact G=I-H/M kernel. The spectral-moments KINETIC_SUM_RULE_ADDENDUM identifies an orientation-specific pure kinetic expectation through a derivative with respect to that plane's hopping amplitude. It explicitly leaves such an estimator unimplemented. The present route varies only the already supported V parameter; it needs no altered transition kernel, off-diagonal walker observable, or pointwise psi ratio. It supplies a pooled transverse first moment, not an individual orientation's moment without further information.

On a fixed finite connected mobile component, H(V)=V N-A is real symmetric with irreducible nonpositive off-diagonal entries. Its lowest eigenvector is strictly positive and simple for every finite V. Normalize psi in L2. Differentiating H psi=E psi and using normalization gives the standard Hellmann-Feynman identity

 E'(V)=psi^T N psi,
 B(V):=V E'(V)-E(V)=psi^T A psi.

This elementary specialization is proved by the displayed differentiation; Hellmann-Feynman is established theory (Feynman, Forces in Molecules, Phys.Rev.56,340,1939, https://journals.aps.org/pr/abstract/10.1103/PhysRev.56.340; primary abstract read for provenance only). The ground energy is concave as the infimum of affine Rayleigh quotients. For h>0 this gives

 [E(V+h)-E(V)]/h <= E'(V) <= [E(V)-E(V-h)]/h.

At V>0 these directly bracket B. No third-derivative estimate, finite-volume gap lower bound, or fitted truncation order is needed for that bracket. Floating eigensolver endpoints below are NOT certified interval endpoints. Genuine energy enclosures would turn this into a genuine kinetic enclosure; ordinary replica SE bands do not do so automatically.

By contrast, multiplication of the eigen-equation by the all-ones bra gives

 E(V)=(V-1) [1^T N psi/(1^T psi)].

The bracket is mixed flippability m(V), not pure. Its derivative enters E'=m+(V-1)m'; simply substituting m for E' is false at detuning. Applying this exact identity to a finite population has sampling, population-control and burn biases, none of which differentiation removes.

## Orientation aggregation without a symmetry assumption

Use the six sources O(q along a,polarization b), a!=b, all with the same lattice momentum magnitude and the actual staggered electric dictionary. Write S_ab=<|O_ab|^2>pure (or the corresponding centered quantity if the source has nonzero mean). The local source identity gives

 numerator_ab=<O_ab†(H-E)O_ab>=qhat^2 <A_plane(ab)>/(2 Volume).

Each of the three planes occurs twice in the six-mode sum. Therefore the pooled positive spectral measure, formed by adding the six unnormalized measures and then normalizing, has first moment

 mu_pool = qhat^2 B(V)/(Volume * sum_(a!=b) S_ab).

This is a structure-factor-weighted mean of the six individual moments, not generally their arithmetic mean and not one chosen plane's moment. It needs no cubic symmetry inside a selected component. On this particular L2 component the six S values coincide numerically, and all source means vanish; that observation is not used in the aggregate formula. At q=0 or vanishing summed structure factor the ratio is not defined and no moment claim is made. The current target is q=pi,Volume8.

The structure factors remain PURE observables. Existing forward descendant C0 estimates tend to them as forward time and population control are appropriately controlled; mixed C0 is not substituted. The kinetic-energy derivative route removes unknown pointwise wavefunction ratios from the numerator, not the remaining forward/pure-denominator obligation.

## Frozen exact calibration

The independently reconstructed actual L2 component has864 states,24 geometric plaquettes,6912 directed arcs. All geometric moves are retained. At V=.95:

 E=-.40273650590973076,
 <Nf>pure=8.108812016122437,
 <Nf>mixed=8.054730118194623,
 <A>pure=8.106107921226045,
 S_ab=.405873687668263 approximately,
 mu_pool=1.6643330522761663.

Direct six-source H-E quadratic forms agree with the energy-response numerator. The frozen second-order central stencil h=.02 gives mu=1.664314709258024, bias -1.8343018e-5; h=.01 gives1.6643284666767533; h=.005 gives1.664331905886. The five-point h=.02 value1.664333055562704 is an exact-data accuracy comparison, not a reason to replace the prospectively chosen noisier-stencil design. None of the step sizes was selected after looking at stochastic output.

The h=.02 concavity bracket maps to [1.6601430218903446,1.6684863966257042] for the moment using exact pure S. It is useful even though much wider than the central-stencil error: it does not infer a bias bound from agreement of two stencils. At h=.01 and .005 the corresponding intervals are also reported. The stationary F6 C0 value differs from pure S by4.37293e-9 on this L2 fixture, from deterministic matrix propagation. This is finite floating support, not a volume-uniform or interval-certified forward-error theorem.

Twenty executed finite checks cover graph, eigensystem residuals, pure/mixed energy identities, source normalization, adverse mixed substitution, and concavity brackets. The full exact protocol and all point energies are in RESULT.json. No stochastic sample is counted here.

## Bias and uncertainty accounting

For the primary central stencil define B_h=V(Eplus-Eminus)/(2h)-Ecenter. If the energies have deterministic error bounds eps_minus,eps_0,eps_plus, then its added error is at most V(eps_plus+eps_minus)/(2h)+eps_0. Differentiation amplifies population and statistical error just as it amplifies deterministic error. An observed h-versus-h/2 agreement does not independently bound those errors.

For paired independent replica vectors e_r=(Eminus,Ecenter,Eplus), coefficient vector c=(-V/(2h),-1,V/(2h)), the estimated variance of the replica mean B_h is c^T sampleCov(e_r)c/R. Shared seeds are allowed but must be retained in this covariance; they do not guarantee beneficial correlation after accept/reject and resampling paths diverge. Seeds are independent across replica index. Sweeps, walkers, modes and origins within a replica are not extra independent replicas.

For a jointly estimated T=sum6S, the pooled ratio uses mean B/mean T. Its leading replica influence is (qhat^2/Volume)/meanT times [(B_r-meanB)-(meanB/meanT)(T_r-meanT)]. This retains numerator/denominator and all orientation correlations. It is a delta-method SE, not finite-sample unbiasedness or a rigorous confidence interval. Negative or zero denominator estimates are failures, not repairable by absolute values.

Population bias, energy sampling-window transients, finite forward time and ratio bias must be reported separately. The inspected prepare_population averages counts over its final min(40,burn_sweeps) sweeps; at burn40 that includes the initial projector transient. A tiny ENDPOINT transient alone does not validate this energy average. The proposed burn80 leaves40 projector sweeps before its40-sweep averaging window; its exact infinite-population window target should be checked before stochastic production. This is a measurement protocol choice, not a kernel change.

## Conclusion and limits

There is a useful positive route: existing mixed-energy estimates at neighboring V and existing forward diagonal structure factors can infer the pure pooled first moment, with a transparent finite-difference/concavity and covariance contract. It does not assert mixed=pure, identify a pole or gap, or establish a thermodynamic dispersion. The exact L2 calibration is favorable; statistical usefulness still awaits the fixed protocol in STOCHASTIC_PROTOCOL.md and root review before any execution.

Supplementary deterministic propagation evaluates the specified last40-of80 energy window after20 classical sweeps at all five proposed V values. Maximum absolute floating window-energy residual is8.66e-15 (BURN_WINDOW_RESULT.json). This resolves the window-versus-endpoint bookkeeping on L2, not finite-population bias. An actual source mutant replacing pure Nf by mixed Nf fails pure_FH_algebra; its output is preserved.
