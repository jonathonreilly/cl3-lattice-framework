# Released #7315-D recovery packet

This packet preserves the source history replaced by corrected Blocks 171--173.
It is recovery material, not a manifest, theorem, audit result, or premise
registry.

`ORIGINAL_OCCURRENCES.json.gz.b64` contains all 15 original base-to-head
changed-path occurrences for #7202, #7203, and #7204: three notes, three
primaries, three caches, three ledgers, and the three historical generated
manifest states. The generated manifests are archived only and are never
written to the live manifest by this packet.

`ORIGINAL_OCCURRENCES_INDEX.json` records each revision, relative path, byte
count, and SHA-256 without expanding the payload. Run

```bash
python3 .claude/science/physics-loops/released7315-d-recovery-20260911/verify_original_archive.py
```

to verify the base64 envelope, deterministic gzip payload, occurrence counts,
and every decoded body hash. Pass `--extract DIRECTORY` to recover the files.

The corrected primaries use the bounded helper
`scripts/admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11.py`.
That helper reconstructs the missing historical `b171_profile_table_v2.py`
table from the source definitions that produced it, records exact provenance,
and imports only the current finite Block 105 matrix closure. The historical
43-file dependency chain and historical caches remain recovery evidence; they
do not certify the corrected sources.

Fresh canonical caches remain pending independent source confirmation and a
separately authorized one-shot producer run. Formal claim audit remains
deferred.
