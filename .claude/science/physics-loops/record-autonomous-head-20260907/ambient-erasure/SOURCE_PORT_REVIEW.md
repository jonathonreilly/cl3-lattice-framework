# Cold review: ambient generator source and portable native witness

Reviewed 2026-09-07, independently of the source author, read-only. Inputs: repo ambient-generator theorem note and runner; frozen native scratch ambient-generator/check.py and REVIEW.md; my prior ambient-generator-review.md and locality derivations. No repo changes.

## Verdict

No blocking mathematical defect found in the common ambient generator, capped sign-summed code invariance, or CPTP chronological-copy erasure statement. One narrow factor-of-two terminology correction is needed. The portable code retains the frozen scientific computation, with only the declared metadata/output and finite-residual guard changes.

## Finding: trace distance convention

The note at lines 227–228 says “trace distance 2sin(0.5)”; the runner's `distinct_time_state_trace_distance` field stores 0.9588510772084062. The calculation is the trace norm ||rho-sigma||_1, whereas conventional trace distance is one half of that norm, sin(0.5). The nonzero timing-phase witness is valid. Rename this quantity “trace-norm distance” in prose and metadata (or explicitly define the unconventional normalization); no scientific recomputation is needed. The same terminology originated in the scratch witness, so this is not a port regression.

## Mathematical review

The local bare seed uses the whole native hopping and the supplied fuel/head registers. J=T n_v(1-n_w), with Q applied after J, is the appropriate physical directed operator; the bridge action is not assigned an extra fair-coin factor. The unrestricted physical head tensor has the destination-empty factor, and the note limits its simplification to the prepared one-head sector. N conservation and old-Record preservation follow termwise from the declared native algebra.

The refusal uses source eligibility E_vw rather than an unrestricted identity, so ineligible sectors do not acquire fake refusal jumps. On the stated one-head sector its effect is positive and energy commuting. Individual capped sign effects need not preserve the code; the proof correctly requires the sum over signs. Commutation of target energy projectors with the newly recorded Z and sum_z Q_z Pi_b Q_z=Pi_b supply that cancellation. Functional calculus then supplies the refusal square root. The witness checks refusal effects, and the source accurately calls them effects rather than claiming a separate numerical square-root amplitude test.

The erasure map C(rho)=sum_s W_s rho_ss W_s† is CPTP even when different W_s have overlapping output ranges: its input history blocks are orthogonal. Separate history-resolved jump labels give the appropriate recycling sum. The loss and free-term intertwinings give the stated generator intertwining. This does not identify arbitrary coherent additions of different chronological amplitudes. The source explicitly keeps their environmental distinction and the timed-probability correction: equal accumulated time gives equal normalized states for the complete safe witness, while dwell-weighted hazards determine their generally unequal norms. Feedback and unsafe-cap extensions are not inferred from that special normalized-state statement.

Exact energy-lift conservation and bounded finite-volume capped GKSL scope are stated separately from physical bath/locality realization. Bare local support is not misrepresented as a finite-range exact energy lift. The proof supplies head/fuel placement and reservoir roles rather than deriving them. The finite square/dimer witness is not presented as a full cube or infinite-lattice computation.

## Port and resource review

A direct diff against the frozen scratch source confirms no change to the scientific computation: added Path/AUDIT_INPUT_PATHS and dynamic dependency SHA, explicit rejection of nonfinite comparison residuals, and default/JSON reporting. The declared dependency is the actual imported native-ladder helper. No saved result is substituted for computation. All numerical comparisons are on demand, and the output explicitly says the parent's full main/census is not rerun.

Fresh `python3 ... --json` run succeeded. Receipt: ambient-port-review-result.json in this scratch directory. Checks 417; imported carrier checks 72; maximum residual 3.553069838302329e-15; individual loss leakage 0.35355339059327395; summed leakage 4.2117038240549247e-16; timed ratio 0.7408182206817174. Runtime reported 0.33147 s and peak RSS 149.46875 MiB, below 180 s/180 MiB. BLAS variables are set to one before numerical imports. Runner SHA 89c6f4fcc3bd55c08dc8cae67da855a2f1b1600a7a1a4a54b14e5465e27b4766; imported helper SHA fa24c6eee30f27387030640d1331f5379981013719c13b10ac5e6f97af3421af.

Two nonblocking robustness qualifications: elapsed time begins after imports, so it is computation time rather than whole-process startup time; JSON serialization still permits nonfinite values in principle (`allow_nan=True` default), though the new comparison guard rejects nonfinite residuals and this fresh payload is finite. Using allow_nan=False would make serialization defense explicit. Neither qualification changes this successful finite receipt or the mathematical witness.
