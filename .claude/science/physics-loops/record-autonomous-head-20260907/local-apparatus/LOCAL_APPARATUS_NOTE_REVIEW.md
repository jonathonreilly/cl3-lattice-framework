# Cold source-only review: local-quench and finite-ladder note

Reviewed the2026-09-07 repo note against my independent quench/global-energy derivations and the primary safe-cap proof. No repo changes. Known pending malformed-control count and unused-code extension edits are excluded from findings.

## Verdict

No blocking mathematical or scope defect found. The note correctly separates legal native-CAR locality, full-line local energy defect, whole-cube safe finite-battery approximation, and conditional storage. These are complementary results rather than a claim that one local finite apparatus inherits every exact property of all four.

## Specific checks

The echo orientation and negative Heisenberg time are correct. m=r+1 counts the first possible traversal of an omitted nonzero hopping, rather than only reaching its endpoint. Hence Taylor agreement holds for n<m, and the integrated tail begins at m+1. The whole-support physical geometry gives the stated conservative m>=floor(R/2)+1. Source parity, bridges and fixed N are correctly included as legal-code restrictions; the use of odd CAR norm identities does not claim physical locality of odd operators on the edge-qubit tensor. Fuel controls and physical erasure do not promote this to an unrestricted ambient norm.

The feedback factor J^-(tau) and extra4T_m term are correctly separated from the complete isometry law. No feedback finite-battery or support conclusion is smuggled into the complete-law theorem.

The exact defect and Hermitian drift formulas have the right signs. The g_R bound follows the omitted one-particle support distance, and the one-head Lambda avoids an extensive edge-rate sum. The unconditional Fourier translation is applicable to the full-line multiplier law with original free evolution, not selected trajectories. The sine tail integration and cutoff example support a volume-uniform bound on finite-volume energy-mean differences. The source explicitly forbids transferring that bound automatically to cap, rounding or changed free evolution.

The stronger safe enclosure0<=A<=24 is valid for this unit-gap/unit-hop ambient cube: each q_e(h_e+I) is positive and at most2q_e because the whole native hop has norm<=1. Thus Q in[48,73] and later battery in[24,73] follow; this strengthens rather than conflicts with the primary memo's looser norm-only enclosure. It does not require the projected approximate packet to retain Q safety.

The capped TWO-sign column and one source-eligibility refusal complement have equal completed effects to the exact law. Duhamel evaluates their difference on the exact safe flow. Cell restriction, free battery rounding and input projection are applied in the correct order. The stated diamond norm is over the fixed legal matter-input map with a fixed battery and arbitrary reference; it is not over arbitrary battery or coherent direct-sum inputs. The erratum is properly disclosed rather than reused as a premise.

For the whole finite cube, actual free A+EB_delta commutes with rounded conserved A_delta+EB_delta, despite not generally commuting with the jumps. Thus the exact rounded-energy statement and conservative original mean certificate are compatible. Composition of local fiber error with the safe-cap comparison grants a trace approximation; the text correctly withholds the whole-cube exact energy certificate from that composition. If this composition is expanded in a later source, its local rounded columns and control-sector definitions should be specified explicitly rather than inferred from the short paragraph.

The48-qubit count is clearly a conditional storage encoding, excluding collision ancillas, bath, clock, preparation and synthesis. The six-mode and native-square witnesses are not presented as48-qubit propagation or a fixed-time all-path cube transport result. Audit status and supplied axiomatic ingredients remain explicit. I have not independently rerun the newly stated native519-check witness in this source-only review; that numerical paragraph is within the separate native runner review lane.

## Highest-value next physical assumption

After the finite-horizon fresh-ancilla collision construction, the largest remaining hidden operation is implementation of the globally spectral rounded J_a couplings. A supplied clock is important, but making it autonomous before defining what physical coupling it switches risks merely concealing those matrices inside an even larger apparatus.

The next bounded target should therefore specify a physical interaction graph and bounded interaction-strength/gate set for the finite storage-plus-ancilla device, then quantify an explicit compilation of one rounded collision pulse (including eligibility and refusal) to that set, with retained-channel error and gate/time/workspace counts. A very large constructive upper bound would still retire more of the current global-coupling assumption than another fixture calculation. Clock scheduling/pulse accuracy must be counted as a supplied resource in that intermediate result. An autonomous finite clock can then be addressed against an explicit sequence of admissible local controls, rather than against unspecified spectral jumps. This is a proposed next target only, not a theorem established by the present note.
