# Prospective local-moment / structure-factor pilot — not launched

## Purpose and domain

Test whether the variance reduction is computationally useful in an actual larger RK configuration sampler, and test fixed-momentum finite-volume effects separately from a lower-momentum observation. This is not a detuned calculation, a gap fit, a mixing proof or a photon-phase test. Use the exact supplied H_RK=N_f-A, geometric plaquette moves, and the component reached from n_a(r)=r_a mod2. Never enumerate the L4 Hilbert space.

Proposed volumes L2 and L4. Modes: L2 harmonic1 and L4 harmonics1,2, all six momentum-axis/transverse-polarization pairs. L2,h1 and L4,h2 both have q=π in lattice units; L4,h1 has q=π/2 and is a distinct point, not a matched continuation. No physical continuum length or speed is inferred.

## Configuration sampler and measured quantities

Use the existing exact RK random-plaquette transition: one uniformly proposed geometric plaquette per step, flip if flippable, M=3L³ steps per sweep. No branching, importance weights, forward suffix or descendant population. Thirty-two independently seeded chains start at the stated configuration. Compare separate burn32 and128-sweep protocols; take256 post-burn measurements per chain, one per sweep. All chains/seeds and both protocols are retained.

For each configuration and mode record complex O, |O|², the positive d=qhat² N_f^(ab)/(2Volume), and |L O|² where L O=-sum_flippable Delta O using the signed physical update. Also record all three orientation counts, total N_f, Gauss constraint and electric flux. There is no unknown ground-amplitude oracle at RK. Uniform measure is the stationary law on the sampled component; finite burn lengths are not assumed to sample it exactly.

The primary estimates are S=<|O|²>, mu1=<d>/S and mu2=<|LO|²>/S, with numerator/denominator covariance retained. Thirty-two chain means provide an independent-chain SE; within-chain16-sweep block statistics and lag correlations diagnose unresolved dependence. Estimate means of O as a symmetry diagnostic. Do not replace a failed mixing comparison with a larger error bar and call convergence established.

## Calibration and mixing diagnostics

Before L4, reproduce L2 exact S=5/12, mu1=8/5, mu2=16/5 under the same newly implemented local-observable code; compare both burn protocols and all six modes with4 chain-SE+1e-8. Validate each computed Delta O against an actual flipped configuration on all L2 moves and a fixed collection of visited L4 moves. The signed update includes the state-dependent sign; squared-only checks do not suffice. Include wrong staggering/orientation as genuine small adverse controls.

For L4, compare burn32 versus128 with4 combined chain-SE, first/second sampling halves, and16-sweep block versus chain uncertainty. Report discrepancies and autocorrelation estimates without choosing a burn after outcomes. Passing these checks is finite diagnostic evidence only; there is no quantitative spectral-gap/mixing bound for this L4 component in the proposed calculation. It does not establish the full zero-flux ground among other components.

The matched q=π comparison reports finite-volume changes in S, orientation flippability density and moment quotient. Equality across volumes is not a pass requirement: these are interacting finite systems. The lower q=π/2 result may provide an additional variational upper bound only insofar as the stationary expectations are controlled; two momenta cannot determine a dispersion exponent or pole weight.

## Actual computational-effectiveness comparison

On the same saved configurations compare the one-uniform-plaquette numerator with all-plaquette conditioning and the simplified orientation-count formula. Time their measurement kernels separately on fixed snapshots so Markov update cost and measurement overhead are exposed. Report numerator and ratio-influence variance times measured wall cost, not just the96/7 iid variance factor. This may show that summing flips is slower per effective estimate; that would be a useful failure. Reusing an incrementally maintained orientation count is a separate implementation choice that must be source-reviewed before execution, not assumed free.

## Proposed bounded authorization envelope

No job has started. First implement/review the observable extension and run a <=30second L2 microbenchmark. Then four volume/burn cells, each <=120seconds and384MiB, with total new execution<=510seconds including the microbenchmark; one BLAS thread and scratch-only caches. Stop rather than silently shrink a failed cell. The proposed32 chains ×256measurements ×M local updates is a finite workload, not a performance guarantee. Existing L2 timings motivate feasibility but do not certify L4 cost. Preserve every raw mean/covariance, timing and failed control. A root review of this proposal is required before using the new larger-volume scope.

Implementation freeze before any production: seeds1400000+100000L+100burn+chain,32 distinct chains. The within-chain influence autocorrelation diagnostic uses lags1..64 and sums until first nonpositive correlation, with within-chain centering; this is not a confidence bound or a certified ESS. Primary ratio SE uses32 chain-mean influence values. Split-half differences are paired within chains. Benchmark proposals use a separate RNG on saved snapshots. Code and analysis hashes were sent for independent pre-production review before running the four cells.
