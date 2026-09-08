# Frozen #7894/#7897 author handoff

All twelve findings have implemented corrections awaiting original-session independent confirmation. No author scientific PASS is granted.

- Worktree: `/Users/jonreilly/Projects/Physics-worktrees/fix-backlog-symmetry-hartree-7894-7897-20260908`
- Base: `0221e4865fd37cad773137467dc42af92d655ba9`
- Final staged source tree: `eba06697df80475300fb7ed42e679d29d13ed4d4`
- Exactly seven additions: both original note/runner/cache triples and one outside-docs correction history. All 28,803 base paths are preserved.
- `candidate.patch` SHA-256: `f5ea6b7e3207cd33d7da2ee00e0ee75351cc20e7ac1d7c5c670a86a57fc8987b`
- `author-correction.patch` SHA-256: `84298778630f2851139c1fdb5c355e0122524d4c7c5844719bbdaf75814639f9`
- Original independent reviewer: `/root/backlog_draft_triage`; original receipt SHA-256 `a5ba8a16d5f98279776adee41326e5b19421565b6c74f7ab8462c557155dc237`.

`REPORT.md` explains the corrections and boundaries. Final genuine caches are 37/0 and 28/0; all 56 original check IDs, original computational functions and numerical table rows survive. Seven actual source mutants and sixteen adverse input/source cases reject. The failed authored Hartree 27/1 attempt and its numerical sparse-zero correction remain preserved. No source changes are pending.

Root should compose this exact source on current main, generate and bind the manifest, then return the combined source/manifest to the original reviewer once. The current-main supplement is `LATER_MAIN_BINDING.json` for `efa1126d20be562976ef8e06a6be16a4e22575e9`; its eight-path advancement is disjoint. This packet does not modify or approve the separate walls unit.

Key schemas for verification:

- `FINAL_RECEIPT.json`: source/base/tree/patch binding, original review binding, execution summary and `artifacts` list of `{path, sha256, bytes}` for every external evidence file except the receipt itself.
- `FINAL_SOURCE_INVENTORY.json`: object with `paths` list (seven rows), each containing `path`, `mode`, `type`, `blob`, `sha256`, `lines`, `original` and `final_disposition`; summary counts and empty deletion lists are top-level.
- `COMPLETE_ORIGINAL_CURRENT_FINAL_MAP.jsonl.gz`: 30,096 JSONL rows with `path`, `raw_parent`, `head7894`, `head7897`, `author_current_main`, `original_selection`, `final`, `disposition`.
- `FINDING_DISPOSITIONS.json`: twelve-row list retaining `original_finding`, `author_disposition`, `correction`, `controls`, and hashed `final_anchors`.
- `FINAL_CLAIM_DISPOSITIONS.json`: twelve-row list retaining each original section and its final line range, section hash and scope disposition.
- `FINAL_PUBLICATION_INPUT_PREFLIGHT.json`: object with two `rows`; actual IDs/primaries, types, both helper APIs, citations, declared input paths/hashes, live guard and readiness.
- `FINAL_EXECUTIONS.json`: two-row list with actual command/environment, resource guard, full result/stdout, cache status and equal complete `pre_identity`/`post_identity`.
- `INPUT_CONSUMER_CONTROLS.json`: eighteen-row list: two successful actual consumer/cache cases and sixteen adverse drift/removal/omission/source cases.
- `SEMANTIC_MUTANTS.json`: seven-row list with exact substitutions, source hashes, actual commands, nonzero exits, failed checks and totals.
- `READ_LEDGER.json`, `ORIGINAL_CHECK_PRESERVATION.json`, `ORIGINAL_FUNCTION_AND_TABLE_PRESERVATION.json`: full read and original test/computation/data preservation evidence.

The authoritative full correction is `author-correction.patch`; intermediate and failed-attempt patches remain provenance. `final-source/` is the final seven-body snapshot; `frozen-source/` predates final cache completion and is not the final inventory.
