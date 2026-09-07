# Final focused confirmation

The single material finding F1 in [REPORT.md](REPORT.md) is resolved on the
source bytes below. No unresolved material finding remains within this
bounded independent check. The conditional theorem's final error bounds and
resource rates are unchanged. This confirmation grants no formal audit
verdict, grade, retention status, or TOE completion claim.

## Confirmed source

Frozen main: `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`.

| File | Final SHA256 |
| --- | --- |
| `docs/NATIVE_RECORD_BATTERY_FINITE_PATCH_LOCALITY_NOTE_2026-09-07.md` | `69aa65235a59a81cd33d37610ad950bec8c6c8c75c1cddd7ec6a73199fed9904` |
| `scripts/native_record_battery_finite_patch_locality_2026_09_07.py` | `f8cfd87e8c7e72b9ab97cc105204c89968db39ea964e2f74601b2edd0024f883` |

Exact copies of these source bytes are saved here with `confirmed-` filename
prefixes. [FINAL_SOURCE_BINDING.json](FINAL_SOURCE_BINDING.json) records their
absolute source/snapshot paths, verification time, and hashes. The initial
report and initial reproduction evidence were preserved.

## Why the repair resolves F1

Final note lines 118–126 define `a_P(s)` as the maximum over both signs of
Heisenberg time and carry the signed maximum inside the commutator sum and
integral. For either sign, Duhamel comparison gives its own integral bound.
Taking the maximum and then moving it inside the integral/sum gives exactly
the corrected (7). Variation of constants for the cocycle, whose generator
uses negative time, is now covered explicitly by (6).

Both the elementary commutator estimate and the LR estimate depend on
`|s|`, so the same bound controls each element of the maximum. No additional
factor of two is required. The stated `F1`, `F2`, spectral-energy defect,
shared-battery telescoping, sine-tail cutoff, cubic-shell estimate, cap
distinction, and physical BKSF support conclusions therefore retain the
constants checked in the initial report.

Final note lines 480–487 preserve the original failure and its admissible
three-site fixture rather than concealing it. The runner at lines 402–430
checks the nontrivial Record premise, verifies that the old positive-time
integral is violated, and verifies the repaired symmetric integral. The
note's final execution count was also corrected from 19 to 20.

## Exact final verification

1. Reproduced the final candidate runner, with its JSON and stdout/stderr
   written to `final-author-reproduction.json` and
   `final-author-reproduction-stdout.txt`: exit 0,
   `TOTAL: PASS=20 FAIL=0`.
2. Reran the independently implemented
   [time_orientation_counterexample.py](time_orientation_counterexample.py):
   exit 0. The actual cocycle difference is `0.1377215580103315`; the invalid
   positive-time integral is `0.0561256439169221`; the valid negative/symmetric
   integral is `0.1379557284830106`. Its direct matrix-column lower bound
   still exceeds the positive-time integral's Lipschitz-controlled midpoint
   upper bound. See `final-independent-sign-stdout.txt` and
   `time-orientation-counterexample.json`.
3. Copied the final author runner into this scratch directory and changed
   exactly `max(difference(u,1),difference(u,-1))` to `difference(u,1)`.
   The actual mutant execution exited 1 with `TOTAL: PASS=19 FAIL=1`.
   Only `both_Heisenberg_time_directions_required` failed. This directly
   demonstrates that the added regression rejects the original time-sign
   defect. Source: `final-sign-regression-mutant.py`; result:
   `final-sign-regression-mutant.json`; log:
   `final-sign-regression-mutant-stdout.txt`.
4. Rechecked the final note and runner hashes against the declared values
   above and saved exact source snapshots. No repository file was edited
   by this reviewer.

The final runner command was:

```sh
python3 /Users/jonreilly/Projects/Physics-worktrees/toe-campaign-20260907/scripts/native_record_battery_finite_patch_locality_2026_09_07.py --json-output /Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/matter-independent-check/final-author-reproduction.json
```

The independent and mutation commands used the corresponding absolute
script paths in this directory. All executions retained one BLAS/OpenMP
thread. No full repository pipeline, large simulation, formal audit,
repository edit, commit, push, PR, or external message was performed by
this reviewer. Numerical integration and matrix results remain diagnostic
double-precision checks, with the scope and analytic arguments recorded
in the initial report.
