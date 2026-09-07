# Integrated validation

Pipeline d43d962285e8 completed against pinned main e6a50983b4d4b40ff4faf63a6d5edb0545a769ac with all seven native Wilson/heat/dimension claims present. Strict lint reports OK: no errors; exactly seven affected rows have forensic_evidence_ready true with no evidence or control failures. All seven generated rows have bounded_theorem type, unaudited status and nonempty source dependencies. Receipts were captured before generated cleanup.

```sh
python3 docs/audit/scripts/run_citation_graph_build.py
python3 docs/audit/scripts/write_citation_graph_manifest.py
git add docs/audit/data/citation_graph_manifest.json
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
python3 docs/audit/scripts/check_changed_audit_evidence.py --base e6a50983b4d4b40ff4faf63a6d5edb0545a769ac --include-worktree --json
```

The two new primary canonical runners preserve45 and19 checks; the independent wall helper preserves47 checks and21 rows. Every scientific payload matches frozen receipts. Hash-specific independent mathematical reviews and root final port review pass. Parent source/runner provenance is reused for the unchanged five claims; this one combined pipeline covers the seven-claim candidate. No independent audit verdict is assigned.

Main advanced to e043c95b37 during publication, adding separate apparatus/charged-source units. Subsequent synchronization must be identified separately from this pinned validation and preserve all seven science source/runner bytes.
