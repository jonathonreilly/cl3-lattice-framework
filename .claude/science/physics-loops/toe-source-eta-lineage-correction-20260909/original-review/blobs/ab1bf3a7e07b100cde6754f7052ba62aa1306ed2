# PR Backlog

Both exact runners, identity-bound caches, the bounded N1-N8 note, fresh
adversarial audit, and citation-graph refresh are complete.  The result PR is
backlogged because the mandatory full pipeline does not currently pass on the
proposed tree:

- stage 7 raises `ScienceFingerprintError` before adjudicating the new row;
- on current `origin/main`, `build_citation_graph.py` hashes to `24b88666d52a`
  while its dependency-policy manifest pins `235e8b82fd46`;
- on stacked base PR 7787, the same source hashes to `c58180b642cb` while its
  manifest pins `20698263cbf6`;
- Block 03 changes neither the governed source nor the epoch manifest, so an
  author-lane refresh would be an unauthorized policy edit, not a science fix.

The source note also records the independent checker as a co-load-bearing
`packet_helper_runner`; the corresponding claim-scoped mapping is a reviewed
hard landing condition and is deliberately not applied on this author branch.
Formal retained-audit status remains unset.

After the governance repair lands, retry:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/check_changed_audit_evidence.py --base origin/main
python3 docs/audit/scripts/audit_lint.py --strict
python3 docs/audit/scripts/repo_invariants_check.py --check --enforce-links
```

If all pass, open the draft stacked on Source/Eta PR 7787 with the title
`[physics-loop] source-eta-03 — bounded_theorem — conditional-support Record join`.
Do not use `review-loop`.
