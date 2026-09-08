# Fixed L4 complex-source RK calibration

All16 fixed cells completed. Charged time including frozen micro: 218.477seconds, below600. Maximum child RSS158.953MiB. No replacements, additional cells or production-source changes. Each population has8 independent paired8-source vectors;128 source-replica records are not128 independent derivative replicas.

Aggregate nominal gate: **True**. This includes the prospectively retained stricter paired half-window criterion. Full covariance, individual replica derivatives and every flagged comparison are retained in ANALYSIS.json. No automatic detuned stage follows either verdict.

|Population|harmonic|step|derivative ± paired-replica SE|independent RK reference|consistency|precision|half-window|
|---|---|---|---|---|---|---|---|
|512|1|0.02|2.274207878 ± 0.002127711|2.257110596|True|True|True|
|512|1|0.01|2.278306580 ± 0.001119799|2.257110596|True|True|True|
|512|2|0.02|2.276807404 ± 0.002580479|2.282562256|True|True|True|
|512|2|0.01|2.275928116 ± 0.002928045|2.282562256|True|True|True|
|1024|1|0.02|2.275774765 ± 0.001084115|2.257110596|True|True|True|
|1024|1|0.01|2.275049686 ± 0.001418614|2.257110596|True|True|True|
|1024|2|0.02|2.278613663 ± 0.001656785|2.282562256|True|True|True|
|1024|2|0.01|2.275823212 ± 0.001984984|2.282562256|True|True|True|

References are32 independent finite-chain means from the unchanged L4 burn128 RK pilot, with full two-harmonic covariance. They are not an exact stationary oracle. Same seeds pair source cells within each new population; populations and reference chains are independent. Nominal4SE tests are diagnostics, not coverage or mixing theorems. A positive source derivative does not establish a photon or isolate a pole. Source-step and finite-population biases remain possible even when comparisons do not flag.

The source is X_h=sum six complex Fourier absolute squares. Physical energy=lambda X_mixed is recorded separately from its shifted value. The exact component-symmetry proof removes stationary elastic means for this symmetric finite-component target; finite-chain means and stationarity errors still require statistical control. The new kernel remains a supplied nonlocal source probe.

The actual cost falls below the hot-based forecast with50% allowance. The original cold-as-hot1632second failure remains in MICRO.json; FORECAST.json records the separately justified hot decomposition. No claim of general scaling or guaranteed future runtime follows.

## Serialization repair disclosure

The frozen analyzer9a46fd18 completed statistical calculations but failed JSON serialization of a NumPy precision boolean. Original source and stderr are preserved. The sole fix wraps that existing comparison in bool(...); final analyzer SHA f300d54d7a66007343b741f53b8b0fb05d07a24e882e28982bfc42f3ad527b01. JSON_BOOL_FIX.diff records the exact one-expression change. No statistic, criterion, replica or production output changed. The original production freeze remains historical and is not rewritten to imply this repair preceded data.
