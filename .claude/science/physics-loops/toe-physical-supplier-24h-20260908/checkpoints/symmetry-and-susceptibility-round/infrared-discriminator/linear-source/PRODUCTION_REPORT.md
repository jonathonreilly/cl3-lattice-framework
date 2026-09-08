# Authorized linear-source population pilot: precision failure

All14 frozen cells completed, with16 replicas each:224 coupling-specific preparations,32 independently seeded seven-source replica vectors. No replacements, extra samples, source-step selection or L4 escalation occurred. Primaryh=.01 unchanged. Hash verification preceded launch. Raw files, full paired vectors and7×7 covariance matrices are preserved.

Actual subprocess wall time 10.448868083s; inclusive charged total 14.009400666s of1800, including3.560532583s conservative prior micro charge. Maximum cell wall 0.874988625s; maximum RSS 133.203125MiB. All raw binary/count/Gauss/flux/cache/window/resource postconditions passed. Original500s forecast failure and prospective revised envelope remain preserved: actual execution was far faster than conservatively scaling first-call compilation repeatedly. This observation was not used to change the samples.

| Population | h | susceptibility | replica SE | precision |
|---|---|---|---|---|
| 128 | 0.01 | 5.492923048 | 14.382124165 | FAIL |
| 128 | 0.005 | -19.483692339 | 44.353594971 | FAIL |
| 128 | 0.0025 | -10.317842915 | 190.011505039 | FAIL |
| 256 | 0.01 | -2.379600096 | 5.778176217 | FAIL |
| 256 | 0.005 | -17.579663255 | 22.434483995 | FAIL |
| 256 | 0.0025 | 5.867226958 | 96.317627044 | FAIL |

Exact finite-step references at h=.01,.005,.0025 are .560114229654074,.5600967326779838,.5600923584481166. All six nominal4SE consistency tests pass only because errors are enormous. All six precision tests fail; four estimates are negative. Negative values were retained without clipping. Population and paired-step compatibility within4SE does not establish absence of bias: these tests lack power here. No stochastic burn-sensitivity test was performed; only the earlier deterministic80/last40 reference propagation was checked.

Primary P256h=.01 gives−2.379600096±5.778176217 SE; primary P128 gives5.492923048±14.382124165 SE. These cannot supply a useful positive inverse moment or harmonic spectral bound. The exact susceptibility identity remains valid; the finite population energy-curvature estimator has failed its declared measurement precision target. Smaller h amplifies noise as expected. Common random numbers did not make the second response sufficiently precise, and no guaranteed covariance gain is claimed.

The energy used is the local mixed estimator−.05Nf+ξF. Stored shifted_energy is merely this estimator minusΛ, an algebraic transform, NOT independent accumulated-weight growth data. The analysis checks that transform, frozen source hashes, all40 sample windows and their physical-energy means before calculations.

Disposition: preserve as a negative calibration result; stop this production protocol. A future susceptibility route would need a different validated variance-reduction or response estimator and a new preregistered cost/precision test, not more seeds silently appended here. No finite-size photon, exponent, gap or source-support inference follows from this noisy pilot.
