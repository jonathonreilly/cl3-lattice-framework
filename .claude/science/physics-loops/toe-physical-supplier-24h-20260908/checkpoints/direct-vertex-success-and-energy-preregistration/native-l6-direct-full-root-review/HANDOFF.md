# Fixed direct full run handoff — no launch performed

Topology: one stdlib root monitor plus one worker at a time. No bootstrap interpreter. Production4060, contract62f0, replay2956 are fixed. Exactly four direct candidates once, original thresholds. Prior14; production180/internal175; replay150/internal145; whole root remaining346, watchdog345.5, total360. Aggregate tree384MiB includes root itself; perPID sampled peaks and external worker highwaters retained. No retry/replacement.

Run root preflight first with the pinned interpreter-I-B-S run_once.py preflight. Root must complete cold review and remote checkpoint before the launch command below. ROOT_AUTHORIZATION was prepared only as explicitly requested; this agent has not launched either physical stage.

External shell command, executed once by root from this directory:

`/usr/bin/time -lp /Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -B -S run_once.py launch > ROOT_SHELL.stdout 2> ROOT_SHELL.stderr`

Root independently reconciles real elapsed<346 and maxRSS<=384MiB from this shell receipt, then charges14prior. Internal COMPLETE remains shell-pending. This shell captures interpreter startup/final teardown that the Python timer cannot see. LAUNCH_STARTED is an exclusive marker; output is fixed fresh sibling native-l6-direct-full-run-4060. Any failure retains all logs/partials and prevents replay or success.

The root verifies both source/runtime sets, loadedstdlib origins, exact production authorization and contract; streaming hashes avoid fullfile buffers. Every stage uses/usr/bin/time-lp and a new process group, bounded ps polling, group+known descendant cleanup on exceptions/time/RSS. Production output must have exactly11NPY files, seven raw bitbridges with parsedNPY headers, source-bound COMPLETE and Echi success. Replay gets fixed RESULT/COMPLETE/source/contract binding. Entire production membership/hashes are unchanged afterward; all particle bounds/Echi and replay bindings agree. Both source sets and authorization are checked again at completion.

Source-only controls exercise actual time-receipt parser and adversarial missing/invalid fields. No numerical array/control or worker is executed by these controls. Independent root approval, review and outer shell remain required for actual execution.
