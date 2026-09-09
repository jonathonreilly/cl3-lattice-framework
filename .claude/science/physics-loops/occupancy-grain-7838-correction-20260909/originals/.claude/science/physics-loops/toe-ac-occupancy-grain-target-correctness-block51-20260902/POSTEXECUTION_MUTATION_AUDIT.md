# Post-execution mutation audit

The primary runner lists exactly the thirty mutations preregistered in
`MUTATION_PLAN.md`.  Each mutation was executed separately and required a
nonzero result.

```text
MUTATION_TOTAL=30
MUTATION_KILLED=30
MUTATION_SURVIVED=0
```

Coverage includes orbit counts, support degrees, global-versus-local copying,
Pfaffian/realification typing, current Record scope, removed scalar Record
content, PR/TOE overclaim, canonical/audit-file mutation, source drift, graph
metadata, and N1/N5/partial-closure omissions.
