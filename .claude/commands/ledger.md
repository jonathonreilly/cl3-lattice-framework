# /ledger — Claim Status Lookup

Verify a claim's audit-ratified status before citing it as retained. In-file
`Status:` headers, note prose, and session memory can be stale; use the tracked
claim shards and `ledger_meta.json` at a named `origin/main` revision.

## Invocation

```text
/ledger <claim-id | note filename | keyword>
```

## Procedure

1. Attempt `git fetch origin main` when network use is allowed. Record whether
   it succeeded. If it fails, use the existing `origin/main` snapshot and report
   that remote freshness is unverified. If that ref is absent, use committed
   `HEAD` only as an explicitly local, non-authoritative fallback.
2. Freeze the selected revision and read its shards in memory. Do not clear or
   reuse a shared temporary directory, materialize audit outputs, or mix rows
   from different revisions:

   ```bash
   python3 - '<query>' <<'PY'
   import io, json, subprocess, sys, tarfile
   query = sys.argv[1].lower()
   resolved = subprocess.run(
       ['git', 'rev-parse', '--verify', 'origin/main^{commit}'],
       capture_output=True, text=True)
   fallback = resolved.returncode != 0
   revision = (subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True)
               if fallback else resolved.stdout).strip()
   print('snapshot:', revision)
   print('source:', 'local HEAD fallback; not current-main authority'
         if fallback else 'origin/main; fetch freshness must be reported separately')
   payload = subprocess.check_output([
       'git', 'archive', revision, 'docs/audit/data/ledger',
       'docs/audit/data/ledger_meta.json',
       'docs/audit/data/axiom_premise_nodes.json'])
   rows, premises = {}, {}
   with tarfile.open(fileobj=io.BytesIO(payload)) as archive:
       for member in archive:
           if not member.isfile() or not member.name.endswith('.json'):
               continue
           with archive.extractfile(member) as source:
               data = json.load(source)
           if member.name.startswith('docs/audit/data/ledger/'):
               rows[data['claim_id']] = data
           elif member.name.endswith('/axiom_premise_nodes.json'):
               premises = data
   hits = [(cid, row) for cid, row in rows.items()
           if query in cid.lower() or query in (row.get('note_path') or '').lower()]
   if not hits:
       print('No matching row in this snapshot; no inference about seeding history.')
   for cid, row in sorted(hits):
       print(cid)
       print('  note:', row.get('note_path'))
       for field in ('claim_type', 'audit_status', 'effective_status'):
           print(' ', field + ':', row.get(field))
       for dependency in row.get('deps') or []:
           state = rows.get(dependency, {}).get('effective_status')
           print('  dep', dependency + ':', state or 'CHECK PREMISE REGISTRY / MISSING ROW')
   PY
   ```

3. Report each match's type, audit status, effective status, direct dependencies,
   snapshot SHA, and freshness limitation. For a dependency without a claim row,
   inspect its entry in the premise registry at the same revision before calling
   it missing; approved foundation nodes are not ordinary claim rows. If an
   archive/read fails, report lookup failure, never infer a negative result.

## Interpretation

- Retained-grade means `effective_status` in
  `{retained, retained_bounded, retained_no_go}`. Preserve the exact scoped
  hypotheses of bounded and no-go results; a retained label does not prove a
  broader statement.
- Missing ratification prevents claiming retained authority, but does not by
  itself refute the source proof or prevent explicitly provisional research.
- Approved axiom/primitive entries chain-satisfy only within their registered
  source boundaries. Read the registry and source before classifying them.
- A row absent from this snapshot is unverified here. It may be unseeded,
  renamed, excluded, or historical; absence does not establish its history.
- This command reads status only and writes no ledger, queue, or generated
  status surface. Authoring sessions may use validated applied-audit feedback
  to reproduce a repair target, but new science does not require a prior audit
  rationale. Restricted independent audit seats use their own clean-context
  tools and must not import prior rationales from this command.
- Status authority and mathematical correctness are separate: a reproducible
  proof defect in a retained source is evidence to route for repair/re-audit,
  not something to conceal because the label is retained.
