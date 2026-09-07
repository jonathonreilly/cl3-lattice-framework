# #8002 initial-head transition addendum

**Resolved: the initial snapshot scope is fully accounted for.** The original frozen seven-landing report is unchanged; this addendum distinguishes the cutoff head from the later reviewed/closed head.

- Initial254 snapshot at `2026-09-07T13:10:39.143955+00:00`: **`be102438f655dd18019634fa46ab7aba8b1a14d9`**.
- Reviewed and closed head: **`726bafb889a85efadc62dbd81d51efb66c2cdf90`**.
- Actual original delta base: `d61adbe4cb0bcb245235b6525b6ff577cafb6bb1`.
- Accepted landing: `a8f84aaad75fdcb790ba6ba094e4275e237d9a5a`; checked current main: `7887b4481feae2800c04c7c42ddac9554f2c2b9f`.

Actual Git proves that the reviewed head is the **direct child** of the initial head. The single intervening commit adds **36 lines to four existing campaign files**: HANDOFF.md, OPPORTUNITY_QUEUE.md, STATE.yaml and TRACE_GATE.md. All four changes are append-only with unchanged modes. There are no deletions, renames, mathematical note changes, runner changes, cache changes or manifest changes. Every other tree path retains its exact mode/blob.

The initial authored delta has **12 paths**, all byte/mode-identical at the later reviewed head. Each of those twelve paths is already in the accepted sixteen-path #8002 disposition map. Thus its mathematical statement, runner, original cache, gravity probe and original history/control payload were included in the source review, with the same accepted corrections and qualifications previously recorded. The note’s original reversed-suprema/boundary scope and unsupported Gaussian/gravity transfer were corrected or withdrawn; this addendum does not reapprove the original wording.

The four added close-out surfaces also were **already included in the original full review**. In particular the review’s findings 7 and 8 explicitly cite the newly appended queue’s “Exactly computable block criteria are closed,” its Gaussian twin, and the matching state wording; the final confirmation narrows these and distinguishes source handoff from landing. They are not unreviewed extra physics smuggled into a cutoff identity. Their exact original/reviewed/accepted/current dispositions are in `TRANSITION_PATH_DISPOSITIONS.json`.

The preserved remote #8002 branch points to `726bafb889a85efadc62dbd81d51efb66c2cdf90` according to the fresh branch check bound in the seven-landing report. Its direct parent `be102438f655dd18019634fa46ab7aba8b1a14d9` is therefore also recoverable. Existing original objects and the complete initial authored map are independently available locally; no branch mutation or fetch was necessary.

**Count consequence:** #8002 remains one original PR whose complete initial science scope was disposed and landed. This head mismatch does not change otherwise verified 27/20 PR or science-coverage totals; other constituents of those totals are outside this bounded addendum. The correct join is “116 exact snapshot-head matches plus one verified #8002 head transition,” not “all117 closure heads equal the cutoff snapshot.” At the source-record level, the frozen seven-landing inventory has 233 records at reviewed closure heads; using the initial #8002 head gives **229** records, still **167** distinct touched paths because those four campaign paths were already present in earlier constituents. Neither distinction changes the number of PRs.

`INITIAL_AUTHORED_SCOPE.json` binds all twelve original paths by base/initial/reviewed/accepted/current mode, blob and SHA256. `TRANSITION_PATH_DISPOSITIONS.json` binds all four additions and their existing review disposition. `initial-to-reviewed.diff` is the complete actual diff. `TRANSITION_RECEIPT.json` binds source identities, ancestry, recoverability and existing acceptance evidence. No new proof review, gate, formal claim audit, source/GitHub/planning change or action was performed.
