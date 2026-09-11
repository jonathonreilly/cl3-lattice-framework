# Released 7753 proposed bounded runtime

The historical cache reports approximately 51.83 seconds for 45 exact-rational 24 x 24 environments. The repaired source retains that central workload and adds only cheap byte guards and three Gram-status booleans derived from already-computed exact ranks.

Proposed canonical run after source review:

- producer cap: 120 seconds;
- outer cap: 150 seconds;
- peak RSS cap: 2 GiB;
- wrapper: the repository's established cached runner wrapper;
- exact child command: `python3 scripts/cached_runner_output.py --refresh --timeout-sec 120 scripts/admissibility_dirac_kahler_joint_pin_order_extended_alphabet_2026_08_27.py`;
- inspected one-shot watchdog: `execute_once.py` in the external draft-003 handoff (it writes only to sibling `producer-01/`);
- precondition: create `logs/runner-cache/.in-progress/` before the wrapper captures source/input identity, so first-use log-directory creation cannot invalidate the run;
- run count before a source change: one;
- mutation sweep: defer until the corrected baseline is frozen and passes; claim mutations are guard checks rather than independent scientific reconstructions.

The supervising reviewer approved one execution under these bounds. Its exact command, source/input hashes, resource measurements, and result are recorded in `PRODUCER_EXECUTION.json`; no automatic retry was performed.
