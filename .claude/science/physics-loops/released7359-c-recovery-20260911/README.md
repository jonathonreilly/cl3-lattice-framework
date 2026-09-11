# Released #7359-C recovery packet

This packet preserves all 26 original changed-path occurrences from PRs
#7350, #7351, #7353, #7355, and #7359. The occurrences consist of five
primaries, five notes, five ledgers, five successive states of the same
generated-manifest path, five historical caches, and the 354-line Block 188
check sidecar. They occupy 22 unique paths. Every occurrence is historical
evidence rather than current authority.

`ORIGINAL_OCCURRENCES.json.gz.b64` is a deterministic, lossless archive. Each
body is base64-encoded inside JSON; that JSON is gzip-compressed with an mtime
of zero and then base64-encoded for portable storage. The readable
`ORIGINAL_OCCURRENCES_INDEX.json` binds every PR, base, head, Git blob, path,
byte count, line count, SHA-256, finding set, and successor relationship.
`ORIGINAL_DELTA_VERIFICATION.json` binds the complete Git name-status and full
binary-diff identity for each of the five original base-to-head deltas.

Verify the envelope and every decoded body with Python's standard library:

```bash
python3 .claude/science/physics-loops/released7359-c-recovery-20260911/verify_original_archive.py
```

When the original Git objects are available, verify all head bodies, base
presence, successor relationships, and complete deltas too:

```bash
python3 .claude/science/physics-loops/released7359-c-recovery-20260911/verify_original_archive.py \
  --verify-git /path/to/Physics
```

Pass `--extract DIRECTORY` to restore each occurrence under its PR number and
original relative path. Repeated manifest versions remain separate by design.

`CLAIM_FAMILY_DISPOSITIONS.md` and `ORIGINAL_FINDING_DISPOSITIONS.json`
separate candidate canonical results from historical unreproduced material,
withdrawn claims, and open alternatives. In particular, the Block 188 B9
open-half construction is preserved as historical successful finite evidence:
it changes `D` and `Q` while retaining the three tested positive-semidefinite
Gram inertias. It is not discarded or promoted to uniqueness. The cited
campaign body and Block 186 check sidecar remain unavailable. The historical
16-dimensional census with nine nonreal roots is flagged unverified and
inconsistent with a real characteristic polynomial.

No file in this packet is a theorem, cache for corrected source, manifest,
audit result, premise, or physical interpretation.
