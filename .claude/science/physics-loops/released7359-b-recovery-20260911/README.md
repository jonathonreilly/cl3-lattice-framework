# Released #7359-B recovery packet

This packet preserves the source history replaced by corrected Blocks
180--183. It is recovery material, not a manifest, theorem, audit result, or
premise registry.

`ORIGINAL_OCCURRENCES.json.gz.b64` contains all 29 original base-to-head
changed-path occurrences for #7340, #7343, #7345, and #7347. The four
generated-manifest states remain separate occurrences. Block 180's nine
exercise/probe/frame bodies are preserved individually.

`ORIGINAL_OCCURRENCES_INDEX.json` records each PR, revision, path, byte count,
and SHA-256 without expanding the payload. Run

```bash
python3 .claude/science/physics-loops/released7359-b-recovery-20260911/verify_original_archive.py
```

to verify the base64 envelope, deterministic gzip payload, occurrence count,
and every decoded body hash. Pass `--extract DIRECTORY` to recover the bodies
under their PR number and original relative path.

The corrected canonical sources use one bounded helper and unchanged accepted
finite suppliers from current main. Historical caches in the archive do not
attest the corrected sources. Fresh corrected evidence remains pending an
explicit owner-authorized one-shot run.
