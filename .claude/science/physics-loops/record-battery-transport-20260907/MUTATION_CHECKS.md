# Mutation and independent-check record

These are source-side verification records, not audit verdicts. Historical
executions retain their own source identities. No old receipt is relabeled
after source changes.

## Primary mathematical implementation

Frozen experiment source:
`ab0ae23cfdbd084dd3d6043c9bc94560d7b8160925d39a9083dcd8a9f3be4750`.
Final mutation probe:
`410644a929ade4f241fd7673c8430c98c0466abc13b125947a00d2eeb066a6cd`.
Raw probe output:
`94e6d313be36c7ace9453e8587a70ac43572f59548d38dd70f64adf239683a86`.

| Corruption | Detection |
|---|---|
| Omit the sine-overlap term | Direct interval integral disagrees |
| Shift grouped spectral energy | Spectral resolution residual |
| Change the edge order | Local-port/path check |
| Reverse the matter dwell phase | Sequential/endpoint and first-minus controls |
| Split a degenerate spectral value | Grouped versus individual eigenstate contraction |
| Reverse battery energy shift | Direct battery moment and total-energy drift |
| Remove initial energy coherences | Large independent state/observable change |
| Reset a fresh battery at each event | Distinct later currents and state |
| Reverse free endpoint phase | Endpoint residual 0.4075 and dwell residual 0.1468 |
| Swap incoming/outgoing free phase | Endpoint residual 0.1733 and dwell residual 0.0336 |
| Use frozen width-one mean for wide packet | Energy drifts 62 and 129.5 |
| Use frozen cap for wide packet | Full spectral support exceeds the cap |
| Use width-one kernel at widths 125/260 | State disagreement about 0.756/0.757 and changed benchmark outcomes |
| Corrupt state normalization or energy diagnostic | Density/energy checks reject |

The incorrect free-phase models still have self-consistent energy ledgers.
The timing and independent-state checks detect them; conservation alone is
not used as their validation. Runtime-envelope mutation is explicitly a
predicate check, not new evidence about physics or a real memory-stress test.

## Independent checker and rational certificate

The original independent checker source
`71784b76a1a52a5301f31d19eac1a91856750d14ff2796503d419f30821838e2`
was written without reading the primary or its caches. Nine mutations
tested fixture count, topology, pulse preparation, one-particle transfer
kernel, first-pre timing, packet overlap, battery moment, number trace and
execution envelope. Every mutant exited nonzero in the intended family.
The wide runs were disabled for those mutation subprocesses; this limitation
is recorded in `independent/MUTATION_CHECKS.md`.

The exact-rational certificate source
`1d4ab304a51c8bf3095499e5f1fde8e934a4623b9e1de6e312b6c6a468680ec5`
had fourteen rejected mutations spanning signed hopping, norm bound,
square-root bracket, Hermiticity, path connectivity, current/density/energy
enclosures, Taylor precision, front margin, both width inequalities and
the memory predicate. These rejection tests supplement the root and cold
reviewers' independent proof checks of the error-enclosure formulas.

## Final live-comparison interface

Final primary:
`50d8a0f9812fd0b0d67b2735b133b396f75c819b10a375ebdba2e47727a05fea`.
Final checker:
`d88004e1311a87181bb3e5c336778d24c2c2d023834d4b15b58c9cc1822f4529`.
Only the comparison interface and reporting contract changed from the
mathematically reviewed versions; no scientific formula or parameter changed.

The primary compares all forty surfaces with a live checker subprocess,
requiring exact discrete/resource/schema fields and finite numerical
agreement within 5e-8. A primary-only dwell-map corruption gives a measured
disagreement 7.693e-4 and fails. Malformed JSON, child exit 7 and a false
checker validation status also fail. The author and cold reviewer exercised
missing/extra keys, missing surfaces, changed support, float/bool support,
resource drift, NaN/Inf, duplicate JSON keys and timeout: all were rejected.

The primary's validation is 13 PASS / 0 FAIL; the three unmet width-one
physical thresholds remain explicit benchmark FAIL outcomes. The original
experiment source and machine-written nonzero receipt are preserved under
`primary/historical/` and in commit `c1b7b95e8a`.

## Parent memory implementation repair

The full 4096-by-128 isometry is bitwise equal to the original implementation;
all residual fields and scientific stdout agree exactly. All 128 columns and
26 generator/stabilizer comparisons remain covered. Final-column corruption
raises every affected comparison residual; a forced 181 MiB measurement
still fails the unchanged 180 MiB envelope. See reviews/MEMORY_REPAIR.md.
The historical primary probes target the preserved ab0ae23c experiment source.
To replay them, use a scratch tree and put primary/historical/experiment_source.py
at the primary runner path, retaining both probe scripts; never overwrite the
current primary in a review worktree. These are historical verification tools,
not the current canonical runner or a new comparison-validation receipt.
