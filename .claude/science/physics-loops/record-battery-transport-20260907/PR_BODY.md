The fixed native Record transport fixture now has an explicit shared-battery calculation for its nonstationary phase-pulsed input. The physical outcome depends on the dwell operation: with the width-one battery, laboratory free evolution passes the original pre-event current test, while a supplied matter-only dwell does not. Both have some post-event surfaces below the added current threshold. Energy is evaluated from the joint battery state throughout.

The same block proves a dimension-independent observable error bound proportional to `1/w^2`. An independent exact-rational calculation of the ideal current, density and energy margins derives sufficient controlled-protocol widths **125** for the original tests and **260** when the added post-event current test is required. These widths were fixed before actual-width computations. Their initial means are **86.5** and **154**, with caps **173** and **308**; they are sufficient resource prescriptions, not fitted minima.

This is a **bounded_theorem** with actual status **conditional-support**. The carrier, preparation, event instrument, apparatus and schedule are explicit inputs. Spatially local autonomous realization and continuum matter remain constructive targets. No audit verdict or effective-status change is submitted.

This main-based PR carries the source dependencies from #7983 (`4248f6f8a7`) and #7996 (`2ca16ee74d7`) in its reviewed delta. Their conditional carrier, Record and apparatus algebra received an additional independent review. Narrow source-note corrections clarify current measurement timing, fresh versus historical execution results and helper registration. The parent branches remain unchanged. This avoids exposing thousands of unrelated latest-main audit changes against the older stack base. Independent scientific audit remains required for the proposed bounded theorems.

| Case | Pre-event current support | Post-event current support | Original test | Added post-event test |
|---|---|---|---|---|
| Controlled dwell, width 1 | 7,6,5,0,2 | 0,5,6,5,5 | FAIL | FAIL |
| Free battery dwell, width 1 | 7,6,5,4,5 | 0,5,7,1,4 | PASS | FAIL |
| Controlled dwell, width 125 | 7,6,4,6,7 | 6,5,4,6,6 | PASS | PASS |
| Controlled dwell, width 260 | 7,6,4,6,7 | 6,5,4,6,6 | PASS | PASS |

All four cases satisfy the declared density, number, negative-energy and cap checks. The final primary validates live agreement with an independently written checker on all 40 surfaces, with maximum numerical disagreement below `5e-13`. It continues to print the three width-one benchmark failures. The earlier experiment's exact source and machine-written `nonzero_exit` receipt remain in the historical packet; they were not relabeled.

Validation:

- Primary comparison validation: **13 PASS, 0 FAIL**, `physical_fail=3` explicitly retained.
- Independent eight-mode/70-dimensional checker: **9 PASS, 0 FAIL**.
- Exact-rational ideal-margin certificate: **15 PASS, 0 FAIL**.
- Independent Astra low proof/code reviews and a direct two-level joint-state energy integral found no blocking mathematical issue.
- Mutation checks cover wrong dwell phases, energy shifts, packet kernels/resources, rational enclosures, and failed/malformed independent-comparison output. Wrong free phases retain a self-consistent energy ledger but fail the separate timing/comparison controls.
- Final full pipeline and strict audit lint pass. All three changed claims are forensic-ready with every load-bearing helper registered; vocabulary, compilation, links and whitespace checks pass.
- Parent memory repair preserves the full isometry bitwise, all scientific outputs and all 26 physical generator/stabilizer checks. Final canonical native/local replays pass 9/8 checks at 103.5/102.2 MiB with unchanged 180 MiB caps. Original sources and failed pre-repair receipts remain in the packet; independent parent checkers pass 9/5 checks.

The helper registration is additive and claim-scoped. Its normalized governed builder fingerprint is unchanged. The citation manifest acknowledges the new note and its two intended parent dependencies. Audit-owned generated state will be excluded from the landing delta.

Review packet: [handoff](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/codex/record-battery-transport-block01-20260907/.claude/science/physics-loops/record-battery-transport-20260907/HANDOFF.md), [trace](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/codex/record-battery-transport-block01-20260907/.claude/science/physics-loops/record-battery-transport-20260907/TRACE_GATE.md), [review history](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/codex/record-battery-transport-block01-20260907/.claude/science/physics-loops/record-battery-transport-20260907/REVIEW_HISTORY.md), [mutation checks](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/codex/record-battery-transport-block01-20260907/.claude/science/physics-loops/record-battery-transport-20260907/MUTATION_CHECKS.md), [imports](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/codex/record-battery-transport-block01-20260907/.claude/science/physics-loops/record-battery-transport-20260907/ASSUMPTIONS_AND_IMPORTS.md), and [source note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/codex/record-battery-transport-block01-20260907/docs/NATIVE_EDGE_RECORD_SHARED_BATTERY_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-07.md). The note names all three load-bearing runners and their canonical caches.

Main synchronization: workflow commit f6f861e8f0 is integrated; the campaign now uses the owner-selected milestone cadence. This adds no scientific premise.
