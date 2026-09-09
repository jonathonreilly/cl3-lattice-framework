# Eta lineage bounded correction report

Original PRs: #7853, #7854, #7855, #7856  
Author base: `fdfa10937a5bd0fad3e9ad73a65174aec10c534e`  
Frozen scientific source: `f1c43beedb1629efe6f88df22556df7149279cfd`  
Final source-and-cache commit: `96522dabefab305a0cebbea376257399859784d0`  
Final tree: `b7d92911fc97091d8863f620d4cb49a403c109a3`

## Result

The four controller-heavy historical units have been replaced by four small,
self-contained finite theorem packets with named independent checkers. The
correction retains the valid operator, ready-set, curl, compatible-extension,
carrier, and fixed-frame cylinder mathematics while resolving all five
findings from the sealed original review.

- Block 03 now treats its affine domain, Schur baseline, resolvents, norm
  bounds, gap, and cubic coefficient as supplied data. Its explicit
  resolvent telescoping proves only the stated conditional positivity interval;
  spectral inequivalence independently supplies the useful family result.
- Block 04 separates the general ready-set theorem and finite compatibility
  count from any claim that the completions are reachable events.
- Block 05 states the square-curl obstruction only for positive `t != 1` and
  limits the nonzero cubic germ consequence to a sufficiently small punctured
  neighborhood. The constant-only compatible-extension theorem remains exact.
- Block 06 proves the finite two-sector carrier and multiplicity-trace facts,
  retains the fixed-frame cylinders, and exhibits the failed branch
  intertwiner. The enlarged register is supplied model data; its spatial
  encoding and physical readout bridge remain open.

The old unconditional mutation totals were removed. The current Block 06
primary executes three concrete operand changes: a rescaled Kraus operator,
an explicit reset to `I4/4` between events, and opposite detector-direction
branch effects. Its checker independently executes the reset and branch
checks.

## Execution evidence

All final executions used a 30-second inner timeout, a 35-second outer
process-group watchdog, a 2 GiB summed process-group RSS ceiling, and one BLAS
thread. Every final cache is fresh and binds both runner source and declared
inputs.

| Unit | Primary | Checker | Primary time / peak RSS | Checker time / peak RSS |
|---|---:|---:|---:|---:|
| Block 03 | 5/0 | 4/0 | 0.50 s / 91.9 MB | 0.31 s / 90.9 MB |
| Block 04 | 4/0 | 3/0 | 0.14 s / 48.2 MB | 0.04 s / 26.1 MB |
| Block 05 | 5/0 | 4/0 | 1.82 s / 89.7 MB | 0.32 s / 88.4 MB |
| Block 06 | 7/0 | 5/0 | 0.88 s / 96.2 MB | 0.66 s / 93.5 MB |

The first Block 03 attempt is preserved separately. Its four scientific
predicates passed, while one literal scope token failed because Markdown
wrapped the phrase across a line. The sole repair normalized note whitespace
for that gate; the successful affected retry and every untouched producer were
then run once.

## Custody and integration boundary

The candidate has 272 paths: four active notes, four primaries, four checkers,
eight current caches, four correction metadata files, and 248 exact historical
review files. The archived review tree is byte-identical to the sealed external
review tree at SHA-256
`5bb164cd782a84e4673d06cf50f2321cf6c8a42720fc81bfee4974de90ef1076`.
That packet accounts for all 12 original commits, 122 endpoint changes, 98
union paths, and 123 distinct nonzero endpoint blobs.

At final validation, current main was
`8bb429a53d8df04502a06d6d8b09f6db320b533b`; its 733 paths since the author
base had zero intersection with this candidate's 272 paths. Root owns final
composition, manifest regeneration, repository gates, landing, and GitHub
disposition.

No formal audit was run. This packet does not claim physical realization,
whole-stencil covariance, obligation retirement, reservation release, or a
TOE.
