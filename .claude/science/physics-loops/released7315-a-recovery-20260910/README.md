# Released #7315-A recovery packet

This packet preserves the source history replaced by the corrected Blocks
153--156 and 158--159. It is recovery material, not a manifest, theorem,
audit result, or premise registry.

`ORIGINAL_OCCURRENCES.json.gz.b64` contains every one of the 31 original
base-to-head changed-path occurrences for #7011, #7015, #7016, #7021, #7029,
and #7032. Repeated generated-manifest states remain separate occurrences.
The archive also contains the two distinct successor bodies that are not
otherwise represented by those originals:

- the exact-rational successor primary for #7029;
- the successor append to the #7032 campaign handoff.

`ORIGINAL_OCCURRENCES_INDEX.json` records the source revision, path, byte
count, and SHA-256 for each body without expanding the payload. Run

```bash
python3 .claude/science/physics-loops/released7315-a-recovery-20260910/verify_original_archive.py
```

to verify the base64 envelope, deterministic gzip payload, occurrence counts,
and every decoded body hash. Pass `--extract DIRECTORY` to recover bodies under
their PR number, revision kind, and original relative path.

The canonical corrected notes and primaries import only the bounded helper
`scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py`.
That helper records the historical AST provenance of its copied constructors
and imports the current finite Block 105 fixture closure. Historical caches in
this archive do not certify the corrected sources; fresh caches may be created
only by the separately authorized one-shot producer run.

The authorized evidence sequence preserved its two failed attempts outside the
repository, reused the fresh Block 153 and 154 caches from the successful part
of attempt 02, and produced fresh Block 155, 156, 158, and 159 caches in attempt
03. Each of the six canonical caches is bound to its corrected runner and
literal input closure and ends with its expected zero-failure total. This is
bounded execution evidence, not a formal audit or a claim about Block 157,
Block 160, or any later transfer.
