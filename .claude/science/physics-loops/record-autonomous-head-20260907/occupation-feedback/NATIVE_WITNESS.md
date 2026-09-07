# Native finite-ladder occupation-feedback witness

Run `python3 check_feedback.py` in this directory. The script imports only the accompanying immutable copy of the independently authored native carrier, plus NumPy/SciPy. It does not import the full-cube feedback primary or checker. The carrier copy digest is reported on every run; no old frozen repository source was modified.

The native square has edges 01,12,23,03, Hamiltonian T01+T23, four fuel latches with gap one, and battery levels 0 through 33. Source head0 has directed jumps on both incident live edges. The initial native code is the cycle+ sector. The negative-drift witness uses N=2 occupation configurations x0=(1,0,0,1) and x1=(0,1,0,1), with x1=T01 x0 fixing the relative phase. Take chi=-sin(pi/8)x0+cos(pi/8)x1 and embed it at exact total energy20 by the explicitly constructed spectral battery-index map. This correlated normalized state has drift (1-sqrt(2))/2. Head edge03 is blocked on both configurations; T23's drift contribution cancels. The full actual joint battery adjoint, including its anticommutator, gives the displayed 2x2 compression rather than merely testing a scalar ledger.

The second legal source sector records Z01=+1 and places head1 at vertex1. Directed bridge12 is active and its post-hop outcome has the correct deterministic parity (Z12=+), with old Record and N preserved. Actual finite lifted matrices intertwine independently constructed Htotal blocks. Full energy spectral indicators satisfy the summed GKSL adjoint identity even on battery-boundary inputs. No refusal channel is introduced.

A separate 2-state commensurate model uses source A=[[1,1],[1,1]], target A=0 and J=|01><10|. An equal mixture of an active exact-Q10 fiber state and a dark exact-Q20 fiber state has unconditional mean Q15; its eventual first-event probability is1/2 and selected Q10. The code constructs the actual joint ladder states and jump matrix. This is a selection counterexample, not an assertion of a frozen full-cube numerical outcome.

Result: 120 new checks plus40 native carrier checks passed, maximum residual1.112e-14, runtime0.345s, peakRSS99.5MiB. Three explicit mutations fail their target: replace matter rate by graph degree, complete the directed branches to identity using fake refusal, omit the battery anticommutator. The result JSON includes discrepancies and exact source hashes.

Finite square/ladder evidence supports the supplied feedback generator algebra. It does not compute the full cube, prove local physical realization, or establish renewal.
