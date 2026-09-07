# Cold review of root native port deltas

Reviewed repository integration diffs against the frozen ambient raw script and finite staging script. No repository edits were made. Both repository helpers were executed live with --json, and every scientific field was compared with frozen raw JSON after ONLY stripping runtime/source/dependency/resource/scope-format metadata and applying the documented trace-norm key renames. All remaining fields are bit-identical.

Finite helper SHA256 ffff92d5e7d0ea012d56e8176ea1714ab9a2ba0ac68d57250af60e7f5d29ce3e: 519 helper assertions, worst residual 2.37723e-14, 0.448 seconds, 122.5 MiB. The count does not include executing the imported carrier's main or full census. Original free A, irrational dimer coefficient, cap/grid, all three retained events, continuous reference, unsafe refusal and all six mutations are unchanged.

Ambient helper SHA256 1018e81fe6866b8110286a53a4078e49739af21cf9c5d83c6eaf73c584cc9fa9: 417 helper assertions plus 72 on-demand imported carrier assertions, 0.333 seconds, 167.73 MiB. The imported carrier main is not executed. All branch-restriction, individual-versus-sign-summed code-loss, merging-history probability, accumulated physical phase and coherent-history-addition controls are unchanged.

The added residual guards correctly reject NaN or infinite scalar maximum errors, rather than allowing NaN comparisons to pass. Portable sibling imports resolve the installed carrier; declared AUDIT_INPUT_PATHS and source/dependency hashes bind that carrier. Resource ceilings remain 180 seconds/180 MiB with one BLAS thread. The finite helper's allow_nan=False enforces strict JSON serialization. Trace-norm renames are mathematically correct: the finite retained error .490317785609 and ambient phase error .958851077208 are unhalved norms, not conventional trace distances.

One minor integration omission was reported to root: the ambient --json dump and default RESULT dump still use json.dumps without allow_nan=False. The current live result contains no nonfinite values, and this is not a scientific-output discrepancy, but adding strict serialization matches the declared integration intent. No other issue found in the reviewed deltas.

Live outputs are preserved at finite-ladder/integrated-result.json and ambient-generator/integrated-result.json. This review concerns the integration deltas and exact output preservation; it does not claim independent self-verification of the previously authored scientific internals.
