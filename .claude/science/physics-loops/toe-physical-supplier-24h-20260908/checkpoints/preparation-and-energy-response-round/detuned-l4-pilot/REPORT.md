# L4 detuned first-moment reference pilot

All nine frozen cells completed. The primary estimates are0.75337998±0.00262435 replicaSE at q=pi/2 and1.44894222±0.00636812 replicaSE at q=pi. These are finite-stencil, finite-population, finite-forward reference estimates. There is NO exact L4 consistency PASS, pure-denominator certificate, spectral pole, gap or continuum claim.

## Executed protocol and resources

The supplied component starts at n_a(r)=r_a mod2. L4 has64 vertices,192 links and192 geometric plaquettes; no Hilbert-space enumeration occurred. All source coefficients use the reviewed staggered electric dictionary. V=.93,.95,.97, derivative h=.02 only. The three groups are P512/burn160, P1024/burn160 and P1024/burn320, eight paired replica indices each. The final group is primary. All use20 classical sweeps, the existing final40-sweep energy window, four origins and cloned F12/F24 suffixes. The recorded origin complex means are MIXED diagnostics; they are neither labelled pure nor subtracted.

There are72 coupling-specific preparations, organized into24 independent paired replica vectors,96 center origins and192 suffixes. Origins, modes, window samples and paired V values are not additional independent uncertainty samples. The two harmonics share their kinetic numerator and center origin data; their influence covariance is retained.

All nine cells exited0 with all binary/count/Gauss/zero-flux postconditions true. Production wall time119.6287seconds, internal measured sum118.7507seconds, maximum RSS144.703MiB. Including the one2.3962second microbenchmark, charged execution is122.0250seconds of the600second envelope. Maximum cell wall time27.3799seconds. No cell, seed, population, burn or forward window was replaced or escalated. No job remains running.

Root reviewed the full wrapper and independently reconstructed all2304 complex Fourier coefficients with zero residual. The current pilot is df9f7c0a..., with explicit failure guards tested under optimize2. The unchanged producer/preparation/raw-measurement bodies retain their previously reviewed hashes. The microbenchmark and original assert-based source remain preserved.

## Estimates and finite controls

For each harmonic, mu_hat=qhat² B_hat/(64 sum6 S_hat), where B_hat=.95[E(.97)-E(.93)]/.04-E(.95). F24 results are:

|P|burn|kinetic B|kinetic SE|q=pi/2 moment|SE|q=pi moment|SE|
|---:|---:|---:|---:|---:|---:|---:|---:|
|512|160|51.65810783|.03280645|.74971737|.00362241|1.46103595|.01879561|
|1024|160|51.63172050|.02344690|.76119280|.00263414|1.43529977|.01274288|
|1024|320|51.64598179|.02282528|.75337998|.00262435|1.44894222|.00636812|

In the primary group, summed F24 structure factors are2.1422615051 (q=pi/2) and2.2277450562 (q=pi). The corresponding F12 moments are.75173216±.00431184SE and1.44409798±.01177181SE. All twelve harmonic/group/forward rows meet the prospectively declared nominal precision diagnostic4SE<=10% of the positive estimate. No exact-value consistency test was defined or added.

The matched-burn population shifts (512 minus1024 at burn160) are-.0114754±.0044789SE at pi/2 and.0257362±.0227081SE at pi. The matched-population burn shifts (160 minus320) are.0078128±.0037183SE and-.0136424±.0142455SE. Primary paired F12-minusF24 shifts are-.0016478±.0045537SE and-.0048442±.0118898SE. None exceeds the declared4SE+1e-8 sensitivity threshold. The nine first/second20-sweep energy-window comparisons also do not exceed that threshold. With eight independent vectors per group these are limited diagnostics, not proof of convergence; the pi/2 population shift is about2.56SE and must not be described as exactly zero.

## Reference meaning and unresolved errors

L4 harmonic2 and L2 harmonic1 both have lattice q=pi. The L2 primary estimate was1.66088±.00256SE, while this L4 primary is1.44894±.00637SE. The difference is a finite-volume reference observation under different finite-population/burn/forward protocols, not a certified thermodynamic trend. L4 harmonic1 has q=pi/2 and cannot be treated as a matched L2 continuation. No power-law or dispersion exponent is fitted from these two momenta.

No L2 F6 guarantee or tiny L2 energy-window bias is transferred. L4 derivative truncation at h=.02 is unresolved; no h=.01 cells were run. Population control, projection equilibration, finite F and nonlinear ratio biases remain separate from replica SE. The lack of a detected control shift is not a uniform error bound. S is the uncentered diagonal |O|² source weight; no mixed source mean was silently used as a pure mean. Possible ground/elastic contributions are not excluded by such mixed-mean diagnostics.

NOISY_SECANTS.json preserves the planned raw energy-concavity diagnostics. For the primary group these are[.75106,.75570] at pi/2 and[1.44448,1.45341] at pi. They are noisy endpoints, not certified bounds or confidence intervals. The earlier L2 failure of raw secants to contain the exact value was ordinary uncertainty propagation, not failure of mathematical concavity. Without controlled pure inputs these stochastic ratios are not rigorous supported-energy upper bounds.

## Analysis history

The estimator/analysis was frozen before opening outcomes. Its first JSON serialization failed because a NumPy boolean in the half-window flag was not a Python bool. analyze_BEFORE_JSON_REPAIR.py and the actual stderr are preserved. The only repair wraps that comparison in bool(); no estimator, threshold, sample, covariance or failed scientific test changed. The nine raw cell files and pilot source were untouched. The planned raw secant diagnostic was subsequently computed from the preserved mean energies and F24 denominators, without sorting or asserting enclosure.

This completes the capped reference pilot. A source-tilted comparison can use these literal finite estimates and raw covariance data, but must match the component, momenta, normalization and finite controls rather than treating this result as an exact pure-state oracle.
