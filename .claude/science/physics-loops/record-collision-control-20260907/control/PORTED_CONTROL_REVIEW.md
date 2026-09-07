# Ported reduced-cell control review

Read-only2026-09-07 review of the block06 source and both canonical runners in /private/tmp/toe-collision-campaign-20260907. I authored the source draft and initial state-specific probe; this is a non-independent port/scope review. Root independently rederived the mathematics, primary supplied exact symbolic elimination/pulses, and native supplied independent matrices.

No blocking defect found. Fresh runs reproduce396 exact assertion calls,171 uniquely named state-specific matrix checks and8 native parent embedding residuals. The396 count includes actual executed assertions (including resource checks), not396 distinct theorems. The171 include sampled norm/energy/head checks plus complete cyclic-span invariance, polynomial/exponential and phase checks; the source describes this accurately. The8 parent residuals establish the displayed square boundary reduction and are not a full square simulation.

The exact primary checks [G1,q]=0 and [G1,K]Pq1=0 symbolically, and global energy commutation of all remaining pulses. Thus the continuum energy-distribution claim does not rely on45 time samples. The native helper independently checks the entire two-dimensional occupied cyclic subspace for every pulse. Its128-dimensional matrix folds fixed r and b0, and its operator norm2 for the first commutator is correctly distinguished from the512-dimensional scratch Frobenius norm22.627416997969522. They are not a failed cross-check.

Source quantifiers distinguish original Plegal-preserving workspace obstruction, expanded globally commuting two-site invariant, higher-support global transfer, and fixed-input two-site escape. Complete-graph pulse success is not declared success on the supplied nine-register nearest-neighbor line, and that line is not the original native square placement. The finite zero-energy ancillary extension retains its unchanged-K/global-two-site premises; no optimal cost or universal impossibility claim is made.

The actual accepted native branch amplitude1/sqrt(2) is explicitly distinguished from normalized unitary state transfer. The three-site phase i and state-specific phase+1 are consistent in symbolic and matrix implementations. No full accepted/refusal instrument, arbitrary-input energy conservation for G1, newly permanent Record formation or axiomatic control set is claimed.

Receipts: control-port-primary.json and control-port-native.json in this scratch directory. No repo edits or canonical caches authored.
