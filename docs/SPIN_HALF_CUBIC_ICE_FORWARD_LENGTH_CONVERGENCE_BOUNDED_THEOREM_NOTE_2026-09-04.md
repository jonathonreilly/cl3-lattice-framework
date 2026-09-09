# Historical paired forward-length diagnostics at fixed volume

**Date:** 2026-09-04; source correction 2026-09-09.

**Claim type:** bounded_theorem

**Runner:** [scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py](../scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py)

**Current diagnostic receipt:** [logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt](../logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt)

**Premise boundary:** [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md). The Hamiltonian, state/readout, Born weighting and imaginary-time sampling protocol used here are supplied model choices. They are not derived primitives or a physical Record formation law. Formal audit is deferred by the owner; this source applies no audit status.

## Data and finite decision rule

The original forward receipts, including the failed 6/2 join and later reanalyses, are preserved without retrospective relabelling. The higher-statistics L=8, V=.95 receipt uses F=6,8,10,12,14,16,20. In windows 2--6 and 8--14 the printed F=12,14,16,20 raw-gap fits are .230080 +/- .001412 and .232216 +/- .005219, with raw spans 1.04% and 2.35%. The current primary recomputes its eight original predicates from the authenticated historical data, strengthening the covariance gate to positive definiteness.

The covariance is a jackknife estimate from nonlinear fitted gap vectors. It is not an exact covariance from a Gaussian-vector sample. The original thresholds 16.766 and 2.262 are retained as fixed nominal Hotelling/Student diagnostics, without an exact confidence-coverage claim. Shared trajectory contrasts must use their joint covariance. The matched RK-subtracted excess carries the same RK-reference variance across all forward lengths. The current raw-gap span test is not an excess-span test: the corresponding excess spans are about 5.31% and 12.04%, and must not be advertised as below five percent.

A valid covariance must be finite, symmetric and positive semidefinite, consistent with its printed errors within the explicitly implemented rounding tolerance. Inversions require positive definiteness on the used subspace. Genuine RK identity rows can have rank-one covariance with zero forward contrasts; singularity there is not evidence of a failed RK identity. Detuned contrast inversions require positive contrast covariance.

## Scope

Agreement on these finitely many forward lengths is a finite diagnostic. It does not prove an infinite-forward/population limit or eliminate projection bias at larger volume. Nominal significance, finite span, ancestry-label counts and physical readout are distinct issues. No physical Maxwell mismatch is established because the historical magnetic product is not an identified physical target. All larger-volume/time/continuum and corrected-production conclusions remain held.

## Recovery and evidence status

The [complete original note](../.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md) and [complete original receipt](../.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt) are immutable dated history. All original program bodies, seeds, budgets, checks, tables and failures are retained in the same archive and authenticated by the [historical receipt index](../data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json). Earlier claims are not current authority. Current successful checks certify only the explicitly bounded diagnostics above. Historical production remains unvalidated under the corrected source; unavailable long-run evidence is held rather than restamped.
