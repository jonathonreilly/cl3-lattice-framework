# Bounded delivery orchestration review

Reviewed complete launcher run_probes.py SHA103ec4ac36254aa7d7a94c97711cd887c6670ec986ece52545a87205af38d230 and portable independent helper fa699d21a4e362dadad5e982b9fd62ac88e0f313ce01fa3519c8dcbf780f16d2 against preserved95d5d994e3e99f55216c976251c5cf7e33d7d301874dfc836c585c086eb66410. Complete diff is exactly one root-path assignment. Manifest reviewed c8f06b168db289d060222edf31c9b3b1111f55c006ab5900999bce9713b88161.

**Verdict: normal-environment orchestration checks PASS; one environment hardening fix required for reliable assertion execution.** No claim-audit verdict or proof certification.

Portable helper uses its sibling probability-family directory. Launcher copies probes to disposable storage, runs primary probability checker before independent helper, and overwrites copied result.json with FRESH stdout. Independent helper therefore checks1458 fresh probability rows and the current copied probability source hash. The old scratch absolute path is not used by the portable program. Seven programs produce166 named assertions; additional1458 rows are separately reported, not added as1458 named assertions. Raw source integrity is not mathematical validation, and scope output explicitly separates the analytical proofs.

Tests all use copies under this delivery-review directory; no original packet or math source edited:

1. Baseline: overallPASS,7programs,166 assertions.
2. Actual arithmetic mutation with corresponding temporary manifest hash updated: native square exp polynomial T² coefficient1/4→2/4. Child raises AssertionError, launcher exits nonzero; not a hash-gate rejection.
3. Explicit child exit7 with temporary manifest updated: launcher exits nonzero reporting exited7.
4. Remove square child and remove its manifest entry so the failure reaches execution: subprocess exits2, launcher fails. Missing manifest-bound files also fail before execution by read_bytes.

Preserved adverse SURVIVOR: first mutation altered the odd T coefficient−3/4→−2/4. It passed even though the operator exponential is wrong. The fixture traces are insensitive to the odd coefficient, so existing17 checks do not certify that full operator formula independently. The mathematical derivation still gives the correct formula. This is a substantive coverage limitation, not an orchestration failure or a reason to erase the first attempt. Its mutated copy/stdout/stderr and first test driver are preserved. Do not describe166 assertions as exhaustive operator correctness.

**Required narrow fix:** launcher copies os.environ and does not remove PYTHONOPTIMIZE. With PYTHONOPTIMIZE=1 the detectable T² mutation above returns overallPASS/166, because the original action helper's final assert and the independent helper's bare asserts are disabled. Reproduced in optimized_math_mutation.stdout. Remove PYTHONOPTIMIZE from the child env (or equivalently force optimization0) before subprocesses launch. This is an actual fail-open path, not hypothetical. The packet was not edited by this reviewer. A one-line delta review and repeat of this exact adverse case suffices; no math fixture change required.

Other limits: timeout180 is per subprocess, not aggregate; capture_output is not a memory quota; the manifest is byte integrity, not proof; output schema checking is purpose-built for these trusted frozen scripts rather than a generic hostile-JSON audit harness. These are acceptable research-checkpoint scope when reported honestly. No current claim of canonical audit eligibility should be inferred.
