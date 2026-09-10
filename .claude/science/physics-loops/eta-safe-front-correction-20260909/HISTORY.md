# Eta safe-front historical recovery

This directory is a portable byte-custody packet for original PRs #7867,
#7862, #7863, #7864, and #7865. It records 16 authored
commits, 132 raw endpoint changes, 120
historical paths (119 outside the generated
citation manifest), 133 distinct endpoint blobs,
124 constituent tip records, 182 input identity
rows, and 30 static import modules.

RECOVERY.json maps every nonzero old/new endpoint and every original input
identity to an exact SHA-256-addressed file under bodies/. Each row retains
the original revision, repository path, Git blob ID, mode, byte count, and
SHA-256 digest. Identical bytes are stored once.

SOURCE_DISPOSITION_TEMPLATE.json preserves all 124 original
constituent records and leaves the correction author's current disposition
fields blank. Filling those fields is semantic work for the author and
reviewer; this custody packet makes no recommendation or PASS determination.

The historical docs/audit/data/citation_graph_manifest.json bodies are present
only through the content-addressed history map. They are outside active
documentation discovery and must not be restored as current authority. The
sealed review still requires corrected-source confirmation. No numerical
producer, repository audit, main mutation, or scientific review was performed
while building this packet.

## Author correction record (2026-09-10)

The correction author preserved this custody packet and added a complete
source-side disposition against author base
`8bb429a53d8df04502a06d6d8b09f6db320b533b`.  The corrected scientific
source is frozen at commit
`ae4130778850e94ce4d7a9223582293c4cb08237`, tree
`0e65e7fba1858c0cf316d7005c9f98a5cf170eef`.

`SOURCE_INVENTORY.json` binds the ten runner modules and their transitive
declared inputs to 37 unique frozen paths.  The cheap pre-execution check
confirmed current imports, declared-path membership, timeout declarations,
scope predicates, and the corrected B12/B13 probability API contract without
calling any runner's `evaluated_checks` or producer entry point.

`SOURCE_DISPOSITIONS.json` accounts for all 124 constituent-tip records: 20
same-path corrected constituents, 89 byte-preserved historical constituents,
five generated citation-manifest rows that are not restored, and ten fresh
cache rows from the frozen source.  Historical caches were not reused.

Root executed each of the ten producers once under its declared wall ceiling,
a 2 GiB process-group RSS ceiling, and single-threaded BLAS.  All 83 reported
checks passed, source/stat identities remained fixed, and the canonical
`cached_runner_output.py --check-only` path validated every serialized cache
without a science rerun.  The fresh caches are frozen at commit
`cbf6e5ca0a05c153359fbb1ab1aec2b4bccb3459`, tree
`4021a2a8468588ebe0ced03fe9b476a9ba974ffa`.  Formal audit, correction
confirmation, status promotion, and landing remain separate owner/reviewer
steps.
