# Independent checker scratch mutation checks

These checks were run on 2026-09-07 against
`scripts/native_edge_record_shared_battery_transport_independent_check_2026_09_07.py`.
Each mutant was made in memory and executed as a separate Python process.  The
wide resource variants were disabled in the mutation subprocesses to shorten
runtime; the relevant validation path was unchanged.  No primary source or
cache was imported.

| Mutation | Observed failing validation family |
|---|---|
| Set the declared event count to four while retaining the five-event fixture | `fixture`, `topology` |
| Replace the final nonbridge edge 9 by bridge edge 1 | `topology` |
| Remove the phase pulse by setting its phase to zero | `preparation` |
| Rescale only the one-particle transfer difference in the overlap kernel | `reduction` |
| Compare first-pre against the undwelled state | `first-pre` |
| Remove the sine term from the analytic packet autocorrelation | `packet` |
| Reverse the energy-shift contribution in the battery-energy kernel | `packet`, `energy` |
| Offset one stored number trace by 0.1 | `number` |
| Set the declared execution time limit to zero | `envelope` |

All nine subprocesses exited nonzero and exposed at least one expected `FAIL`
line.  Harness summary: `MUTATIONS: PASS=9 FAIL=0`.
