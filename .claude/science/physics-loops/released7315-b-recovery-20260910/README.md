# Released #7315-B recovery packet

This packet preserves the source history replaced by corrected Blocks
160--166. It is recovery material, not a manifest, theorem, audit result, or
premise registry.

`ORIGINAL_OCCURRENCES.json.gz.b64` contains all 36 original base-to-head
changed-path occurrences for #7042, #7046, #7051, #7052, #7056, #7071, and
#7083. The seven generated-manifest states remain separate occurrences, and
the Block 166 campaign-handoff append is preserved byte for byte.

`ORIGINAL_OCCURRENCES_INDEX.json` records each PR, revision, path, byte count,
and SHA-256 without expanding the payload. Run

```bash
python3 .claude/science/physics-loops/released7315-b-recovery-20260910/verify_original_archive.py
```

to verify the base64 envelope, deterministic gzip payload, occurrence count,
and every decoded body hash. Pass `--extract DIRECTORY` to recover the bodies
under their PR number and original relative path.

The corrected canonical sources use one bounded helper and the unchanged
current Block 159/105 finite definitions. Historical caches in the archive do
not attest the corrected sources. The separately authorized one-shot run of
the seven corrected primaries produced 44 passes and no failures; the fresh
canonical caches travel with the source candidate.

`CORRECTION_RECORD.json` maps every original path occurrence and substantive
claim family to its disposition, binds the 22 frozen candidate source bodies,
and records the fresh cache and bounded-execution identities. Its status is a
source candidate pending main composition and final confirmation. It does not
record a landing, audit verdict, premise adoption, or retained status.
