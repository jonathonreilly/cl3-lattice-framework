# Source-energy stochastic calibration: all fixed cells completed

The new binary-configuration tilted kernel completed the exact authorized fourteen jobs without replacements, added seeds, source changes or forward suffixes. Primary population2048/source step.02 gives mu=1.6658056404 ±0.0026748461 independent-replica delta SE, versus exact finite-stencil1.6642623381. Both nominal consistency and5% precision criteria pass. This demonstrates a finite L2 calibration, not unbiasedness, a rigorous confidence level, a positive-excitation identity or a photon phase.

## Frozen provenance and resources

Production used kernel396c74a04271990477bcf2eb3f88dae967f8fb24f531071c3f436c9679487d21, driverdd47a50492354b532795eb4fdd70e8ebbd16267eb3d24073f991f786a8fd9bca, analyzer11349daeed5c2f1ac55cd4ee26184aec061f5fb54dc762f33654d8a7896b2118 and protocolac19207026950b1406551437bfc101e1cfbefae88399fbf805f63ce1303fbf70. Native independent full-code review preceded launch; root separately authorized600seconds production. No code changed after that review.

Production took 58.050197 seconds inside children, 59.443633 seconds with subprocess overhead; maximum RSS136.562MiB. Every job satisfied180seconds/384MiB and total remained below600seconds. Earlier deterministic verification4.539seconds/251.47MiB is separate, not counted as production. All224 source-replica records are retained, representing32 independent paired seven-source vectors, not224 independent response estimates. Each contains all40 Nf/X/physical-energy samples and source shift.

Every recorded energy obeys (V-1)meanNf+lambda meanX; the scalar shift is restored separately for every source. Every final state/count/Gauss/flux check passes. Cached Fourier drift against literal recalculation during each final40 window is zero in these runs. Minimum resampling-weight effective-population fraction is0.998162; this is NOT an energy ESS. Minimum initial-ancestor fraction after burn is0.240234. Neither diagnostic certifies estimator precision.

## All response estimates

|Population|source h|B ± SE|T=dE/dlambda ± SE|mu ± SE|exact finite-stencil mu|nominal consistency / precision|
|---|---|---|---|---|---|---|
|1024|0.02|8.10252983 ± 0.00548529|2.43641129 ± 0.00422243|1.66280009 ± 0.00264959|1.66426234|True / True|
|1024|0.01|8.10252983 ± 0.00548529|2.42887573 ± 0.00886996|1.66795891 ± 0.00625802|1.66430162|True / True|
|2048|0.02|8.10643360 ± 0.00410904|2.43318710 ± 0.00362241|1.66580564 ± 0.00267485|1.66426234|True / True|
|2048|0.01|8.10643360 ± 0.00410904|2.42692299 ± 0.00701656|1.67010524 ± 0.00459346|1.66430162|True / True|

All four nominal tests pass without changing the primary step. There are zero nonpositive replica source derivatives and zero negative replica B. The smallest T is2.35953369 (population1024,step.01). Positive derivatives still have sampling error; valid=True is not a guarantee. All raw per-replica B,T and source secants, including adverse secants, are explicitly preserved in REPLICA_RESPONSE_VECTORS.json.

Population1024 minus2048 primary difference is−.0030055459 with independent combined SE.0037649842, unflagged. The paired step differences are−.0051588140±.0072220390 and−.0042995996±.0054599894 at1024/2048. Non-detection is not convergence or a bound on population/step bias. In particular doubling population did not reduce the estimated primary SE in this finite set of16 replicas.

## Noisy secants remain adverse evidence

|Population|h|mean forward secant|mean backward secant|replicas with reversed endpoints|
|---|---|---|---|---|
|1024|0.02|2.425354004|2.447468567|6/16|
|1024|0.01|2.441491699|2.416259766|9/16|
|2048|0.02|2.429292297|2.437081909|8/16|
|2048|0.01|2.437129211|2.416716766|9/16|

Both mean step.01 intervals are reversed. These are noisy energy differences, not certified concavity bounds. The exact energy is concave and its exact secants bracket pure X, but ordinary stochastic endpoints do not inherit deterministic enclosure status. No endpoints were sorted, clipped or relabelled.

## Separate error sources and comparison

The exact source-step.02 denominator bias is7.66325e-5 and the combined fixed V/source stencil moment differs from pure1.6643330523 by−7.07142e-5. At source-step.01 the corresponding combined bias is−3.14354e-5. These finite-difference errors are distinct from stochastic and finite-population errors. The frozen deterministic last40-of80 window check is below5e-15 in floating arithmetic; it is not a finite-population claim. Ratio uncertainty uses full paired seven-dimensional energy covariance, not independent-source or independent-sweep SEs.

The earlier independent F6 denominator method reported population2048 moment1.660881897±.002557398 SE versus its different finite-stencil/F6 target1.664314691. This fresh two-response run has similar observed precision, but uses different seeds and fourteen rather than ten cells and a different diagonal probe kernel. This is descriptive context, not a paired improvement or an efficiency theorem. No earlier V samples were reused.

## What was gained and what remains

Both numerator and denominator are now inferred from ground-energy responses using actual binary transitions. No forward genealogy enters the denominator estimator, and no pointwise ground-wavefunction ratio is supplied. The price is a supplied nonlocal diagonal source and additional finite differences. Finite-population, burn, response and ratio errors still require control; larger volumes and spectral concentration are untested. The uncentered X can include elastic mass on other components. This packet authorizes no further job.
