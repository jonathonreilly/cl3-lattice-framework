# Local L4 h1+h2 production protocol: preproduction review PASS

This reviews the complete candidate, not only the earlier sampler core. Final PRODUCTION_FREEZE.json12af2b728c89c75a68da3fcca0325a4f01d234d5b369e31ceb2243497085e8eb was verified against every listed file. Core fcd0956ce5719731825afe2ef92b27c512b90d9024d60e45229e3c63ee110268, producer83c451a9a57bb0eb5486e74e6d599d288f8fd7ec0ef10afa89efae11701eb475, final analyzer85bf6a0ed06f9f7ae67aa0f91b7005cd94088079f36f5b94f536498ec04c4e24 and launcher07b7469a45b7932aecbb57c99fe5c8f8b5a39a11a2bce68dba0679b857c01aed were read completely. Original freezes, micro and covariance-field failure history remain preserved. No stochastic production was run by this reviewer. Root controls authorization and the proposed resource envelope.

## Core and harmonic extension

The prior actual local transition review is reused. The h1+h2 change leaves count, legal, flip, change and step ASTs unchanged; it extends coefficient rows and constructor arguments. The final additional guard limits L to2 or4. I independently reconstructed all2304 L4 coefficients using exact powers of i: rows0..5 are h1, rows6..11 h2, each ordered transverse pair and normalization1/8. Maximum floating discrepancy is below1e-15. On the three saved endpoint/midpoint configurations,576 actual forward-and-inverse change calls reproduce both harmonic caches and Nf. HARMONIC_DELTA_RESULT.json records this new coverage; the earlier9264 deterministic transition controls are not rerun or relabeled as new.

The only runtime local scientific dependency of production is core.py. The diagnostic exact L2 graph is not imported. The constructor produces the same alternating ice seed; positive even n is checked. All production cells use declared L4,V=.95 and harmonics1,2. No arbitrary odd-L domain is implied.

## Readout and finite projection

For each measured step the producer uses the midpoint Nf, squared norms of the two six-component complex source vectors, and E=-.05(Nf_left+Nf_right)/2. Both real and imaginary source contributions enter vdot; it does not use an origin mixed mean or silently subtract a ground mean. The four quantities are accumulated together into sixteen contiguous batch vectors.

At the stated stationary finite path law, the ratio is qhat²(.95<Nf_mid>-<E_endpoint>)/(64<S_h_mid>), with qhat²=2 for h1 and4 for h2. The source mode is qpi/2 for h1 and qpi for h2. n=384tau gives one-sided tau=n/(2M), M=192. This is a finite G-power Dirichlet quotient, not an exact exponential-time estimator or necessarily a ground spectral centroid. The source protocol explicitly retains this limitation and has no exact L4 oracle or ground/pole consistency gate.

## Sampling and uncertainty

The six fixed cells are tau4,12,36 each with burns8n/32n; warm32n is primary. Each has32 independent chains, measured64n updates, divided into sixteen batches4n. Two-chain shards are a resource partition, not additional independent observations. Seed202609160000+32cell+2shard+rep is unique over all192 chains and separate from the measurement micro. All chains start from the same seed/self path, so comparisons are finite initialization diagnostics, not proof of equilibration. Batches and overlapping paths are not treated as independent replicas.

The analyzer computes ratios from the grand mean and propagates the full four-observable chain covariance through paired influence vectors. Independent cells' difference variances add; within-cell h1/h2 covariance is retained. During review I found that the original field joint_ratio_covariance held influence covariance rather than estimator covariance. The final source now emits explicitly named chain influences, their covariance and joint_ratio_estimator_covariance=Cov(influences)/32. It checks the diagonal against SE². Means, ratios, SEs and gates were unchanged by this reporting repair.

A complete synthetic96-shard dataset was passed through the actual analyzer before and after repair under PYTHONOPTIMIZE=1. All six joint covariance diagonals now equal the reported SE²; all estimates and comparisons remain identical. Actual malformed source hash, NaN, seed, count and zero-RSS inputs reject. Duplicate JSON and explicit nonfinite parsing guards were read. Raw means/batches are finite and mutually consistent, metadata/seeds/source hashes and counts are checked. Invalid aggregate numerator/denominator prevents ratio promotion; underlying four-vector means and nonpositive S counts remain available. Ten-percent four-SE precision and four-SE comparison flags are nominal, not simultaneous coverage or certified intervals.

## Resource and failure contract

The measured measurement-micro hot time is .0494622500264seconds and total .0910384999879seconds, not the informal alternative hot-time message. It includes the actual readout accumulation. The frozen forecast uses threefold update/readout time plus10seconds per shard, totaling4848.919946seconds, maximum106.154615seconds. This is planning extrapolation, not guaranteed runtime. Initialization/path length, diagnostics and platform variation can still defeat it.

The proposed launcher binds the full freeze, refuses output replacement, uses disk-backed outputs, stops on any failure and reserves a full180seconds before each of96 shards from5400 minus the measured micro and elapsed wall time. Producers also check180seconds/384MiB, finite JSON and final caches; subprocess timeout covers imports as well. A cap failure must remain a partial failed execution, not trigger reduced coverage, replaced seeds or favorable cell selection. No new production was launched during review and no budget is authorized by this memo.

Disposition: PASS for the frozen numerical protocol and its stated finite-projection scope. No blocker remains after covariance repair. This does not establish burn sufficiency, tau convergence, a gap, a pole, RK/off-RK scaling or a physical source-selection law.
