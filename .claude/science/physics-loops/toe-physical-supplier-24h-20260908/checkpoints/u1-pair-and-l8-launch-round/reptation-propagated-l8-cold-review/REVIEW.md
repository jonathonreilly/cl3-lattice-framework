# Final prospective L8 resumable-package review

PASS for freeze28529a43855747e35d786e79627e37e9685677e97e966b0a839505442915ced8, for the stated implementation and diagnostic scope only. Full producer, checkpoint, analyzer, analysis_core, launcher, protocol, proposal, freeze builder, roundtrip controls and smoke wrapper were read. Core6a15d889 and initializer704af3a3 are exact previously reviewed copies. All current local freeze hashes and199 declared runtime file hashes verify. Runtime metadata explicitly excludes a hermetic OS/framework guarantee.

## Trajectory and restart semantics

Each segment continues the same Path, head, direction, label ring, three states/NF/O caches and exact NumPy bit-generator state. The accumulator retains all nine partial batch sums, measured counters, full accepted-run history, unfinished run and tag extrema. Measurement batch index uses absolute attempted step minus burn, so an interrupted batch is continued rather than normalized early or discarded. Boundaries do not reseed or reinitialize. The final row divides by the full measured count and full batch width only after the full chain is complete.

The producer requires the immediately preceding receipt with matching config/freeze/segment, matching checkpoint hash and exact prior stop. The analyzer subsequently verifies the entire predecessor-hash chain and every segment interval/checkpoint hash, loaded dimensions, finite partial moments and accumulated attempt history. Final rows must equal the final saved accumulator exactly. This is source-bound provenance and consistency, not cryptographic proof that arbitrary supplied trajectories were sampled honestly. Segments/batches are not independent replicas.

A resource failure can leave a checkpoint without a receipt; it remains an explicit incomplete artifact. Neither launcher nor next invocation overwrites it or silently retries. The launcher requires a fresh output directory and stops on the first failed fixed job. Manual continuation exists only through the declared next-segment interface; this is not permission to replace a failed science segment.

## Actual predata repair

Found a fail-open NaN cache guard in the earlier loader: max(abs(NaN))>tolerance is false. The author preserved earlier bytes and repaired explicit finite complex caches, exact three-cache/label shapes, integer dtypes/binary states, integer metadata and expected L/n before allocation/advance. The corrected producer passes expected config into load. Independently injected NaN into the existing NPZ cache; final loader rejects it. No sampling was needed. Author five malformed controls and repeated4115-attempt exact roundtrip are preserved; the earlier179-attempt rejection-coverage failure remains historical. The new ledger includes a conservative two-second postreview control reserve.

## Statistics and comparisons

Independent synthetic complex-step differentiation reproduces all ten estimates and complete10-by-10 covariance; zero estimate residual and1.39e-17 covariance residual. Factors are qhat²=2-sqrt2,2 and volume512. Sixteen chain means determine SE. Cross-harmonic and residual/variance correlations are retained. Negative variances remain signed and disable the plugin bound. Nonpositive source denominators remain invalid rather than producing a false study pass. The finite projection and nonstationary initialization qualifications are explicit: observed R need not be an exact Rayleigh quotient until the target path law is justified.

Three arms and seeds are fixed, with128 segment jobs. A/C compares projection length at equal burn multipliers, not equal absolute attempts; B/C varies burn at long projection. The restored L4 baseline is hash-bound with its raw membership and independent post-review. Fixed L8A h2 versus L4B h1 and L8C h2 versus L4D h1 compare matched momentum at tau12 and36. Their D/R/correction errors combine independent-run SE, and these size contrasts are not agreement gates. The six within-study D precision gates, original-tag1% rule and12 within-study comparisons remain prospective nominal diagnostics, not convergence certification.

## Resources and review limits

The launcher reserves a full180 seconds from14400 minus recorded preproduction cost and elapsed wall time before each subprocess, using disk-backed stdout/stderr and immutable output checks. External timeout covers imports before the internal segment timer starts. Checkpoint write precedes receipt emission; missing receipt therefore cannot be mistaken for a complete job. Forecast10936.85 seconds and worst129.75-second job are planning estimates, not promises. Prior ledger7.226802541 seconds includes micro, controls, reduced smoke and conservative repair reserve.

No production, new stochastic micro or canonical edit was performed by this reviewer. Existing root literal L8 path reconstruction is separate evidence, not claimed as my own. The inherited path law and new restart machinery are reviewed; this does not predict favorable L8 outcomes, certify mixing, derive a photon or authorize production.
