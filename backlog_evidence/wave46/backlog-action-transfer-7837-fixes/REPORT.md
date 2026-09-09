# PR #7837 bounded correction report

Author disposition: `READY_FOR_ORIGINAL_REVIEWER_CONFIRMATION`. This author does not issue the focused-review verdict, and no formal audit was run.

The corrected packet retains the positive-transfer determinant theorem, the exact same-qubit and orthogonal-blank constructions, and the conditional `4/9` versus `1/2` race. It repairs the three adversarial findings:

- zero first moment now supports only the half-trace identity; unique neutral-input inference requires a spanning menu, with an explicit signed-`z` coherence counterexample;
- `gamma_*>0` and the scalar `W=cI` exponential null case are explicit;
- physical/full-framework wall independence is withdrawn; the five labels are only separately supplied inputs within this packet;
- Route B is checked on all nine matrix units, all four Record-sector units, both coherence blocks, a rotated Kraus basis, semigroup composition, and a completeness-preserving Record-phase negative control;
- the primary imports and declares the separately executable helper, and both pin the canonical note and current Minimal Axioms memo;
- dated novelty, panel, and old `48/48` forced-Boolean claims are preserved only as attributed history.

Final frozen execution:

- primary: `TOTAL: PASS=8 FAIL=0`, cache elapsed 0.64 s, `/usr/bin/time` real 0.75 s, max RSS 68,911,104 bytes;
- independent helper: `TOTAL: PASS=9 FAIL=0`, cache elapsed 0.66 s, `/usr/bin/time` real 0.76 s, max RSS 67,928,064 bytes;
- both declare a 30-second timeout and have fresh source/input-bound canonical caches;
- actual citation-graph APIs discover the note as `bounded_theorem`, resolve the primary and imported helper, and resolve the current Minimal Axioms citation.

Attempt history is explicit. Attempt 1 for each runner reached its earlier checks and stopped nonzero at the same SymPy `.column` API typo. Those source-bound cache bodies and resource receipts are preserved as `*_FAILED_RUN_1.*`. Commit `a51bb2abb9` changes only `.column` to `.col` and repins the helper SHA. Attempt 2 is the successful final execution above; neither successful cache was rerun.

Source chain:

- W45/main landing base: `a917b8f7422bb420e599b37e3562505e77de1da5`;
- reconstructed original commits: `e1880fa282`, `32d3e34d3e`, `9bfe7e5599` (original PR head `07bf3d389b`);
- substantive correction and exact archive: `fc25c707e8`;
- narrow runtime API fix: `a51bb2abb9`;
- cache-only final delta: `5313a51746`;
- final tree: `a153373d5edcf1b05bfc10691ad48c61d862a547`.

All 29 original selected bodies and all three raw commit patches are exact in the repository archive. The current campaign copies carry historical banners. Obligation retirement and TOE percentage movement remain zero; audit status remains unset.
