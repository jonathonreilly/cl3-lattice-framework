# Post-execution validation

| Check | Result |
|---|---|
| primary exact runner | `75 PASS, 0 FAIL` |
| independent exact runner | `13 PASS, 0 FAIL` |
| preregistered mutation campaign | `30 killed, 0 survived` |
| Python compilation | pass |
| primary/independent cache freshness | fresh, input-fingerprint bound |
| primary cache size | 1,696 bytes; terminal `TOTAL` present |
| independent cache size | 409 bytes; terminal `TOTAL` present |
| forensic N5 readiness on synthetic current row | pass (`None` issue) |
| controlled-vocabulary lint | 0 violations |
| approved-premise purity | all four canonical nodes pass |
| repository invariants | pass; expected warn-only unacknowledged new graph node |
| whitespace/error check | pass |

The graph-manifest warning is intentionally not repaired on this branch:
`docs/audit/**` is audit-owned, and this backlog result has no authority to
stage generated audit state.
