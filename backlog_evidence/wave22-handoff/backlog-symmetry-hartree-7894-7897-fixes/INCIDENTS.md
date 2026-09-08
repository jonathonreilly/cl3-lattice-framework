# Preserved attempts and execution limits

The original reviewer ran the two original baselines once (33/0 and 23/0); the author did not repeat them. Both original caches and the independent false-negative controls remain unchanged under `original-review/` and `original-source/`.

The first final authored Hartree execution genuinely returned 27/1 in 9.149632 seconds. Its new R5 check required `.nnz == 0` on a sparse commutator that was mathematically zero but stored 70 explicit zeros in DIA form. Its actual entries were all zero; conversion to CSR gave numerical maximum zero, whereas the hopping commutator's maximum was one. Source, own-note input, cache, raw execution and wrapper are preserved in `failed-first-final-hartree/`; `SPARSE_ZERO_DIAGNOSIS.json` records the actual matrix observations.

Only the new predicate was changed to test the actual CSR numerical maximum. The same bounded repair also clarified that selected originals, rather than an unselected parent campaign, were preserved; the own-note pin changed accordingly. `failed-control-correction.patch` is the exact delta. One genuine Hartree refresh then produced 28/0. The earlier final symmetry 37/0 cache remains identical. No failed condition was suppressed and no original check was replaced by a hash.

The first external diagnosis tried `.max()` on a DIA matrix and raised `AttributeError: 'dia_matrix' object has no attribute 'max'`. This occurred before any source edit; the failed diagnosis program remains `repair_failed_control_first_attempt.py`. The CSR diagnosis succeeded. Its traceback was visible in the tool output; this statement records that incident rather than claiming a separately captured traceback file.

External control preparation initially had an `else120` syntax error, preserved in `controls_first_syntax_failure.py` and its log. A subsequent command used the incorrect `/opt/homebrew/opt/python3.13` path and exited 127; `controls_wrong_python_path.log` preserves it. Neither attempt ran scientific source. The corrected command used `/opt/homebrew/opt/python@3.13/bin/python3.13 -B`; `controls.log` and per-case receipts preserve the actual successful control execution.

Final cache runs used the current real cache executor with real child environment capture, thread limits of one, 90/120-second declared caps, an RSS watchdog and bounded output capture. No unchanged baseline or parent production campaign was repeated. These computational outcomes support the stated finite checks; they are not an independent scientific verdict.
