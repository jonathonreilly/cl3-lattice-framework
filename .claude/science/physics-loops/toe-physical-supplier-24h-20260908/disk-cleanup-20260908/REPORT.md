# Read-only old-campaign cleanup inventory

Inspected31 named September7 campaign worktrees only. Total du allocation 15131000 KiB (about14.43GiB); ignored file payload totals 3139040641 bytes (about2.92GiB). No worktree, branch or file was removed.

Every listed checkout is clean for tracked and untracked files, and each local HEAD exactly matches its corresponding live origin branch HEAD from one git ls-remote query. Local origin-containing references are also retained, but their freshness is not assumed. All branches can be preserved when removing worktree checkouts; removal must not imply branch deletion.

No candidate cwd appeared in the lsof snapshot and no candidate path appeared in ps command text. This does NOT establish inactivity of other Codex threads, future source reads or open handles outside the cwd snapshot. Root should confirm ownership/inactivity and recheck status immediately before any removal.

Ignored files are overwhelmingly generated docs/audit data and Python bytecode. There are no ignored scientific outputs outside those categories. The one additional logs/physics_worker_lock.json in the spatial-weak-coupling checkout must be inspected before treating its owner as inactive. Raw ignored paths, bytes and SHA256 are preserved; identical-content groups identify duplicates. Unique generated audit caches are not new authority, but preserve them in an external archive if forensic provenance is desired before removal. Do not silently delete unique ignored files on the basis of the clean git status.

## Candidates, conditional on final ownership and ignored-file preservation check

| Worktree | KiB | Ignored bytes | Ignored files | Live branch exact |
|---|---:|---:|---:|---|
| /private/tmp/toe-anisotropic-source-campaign-20260907 | 487112 | 101225993 | 30 | True |
| /private/tmp/toe-autonomous-campaign-20260907 | 481332 | 101265768 | 36 | True |
| /private/tmp/toe-clock-campaign-20260907 | 482044 | 101137629 | 32 | True |
| /private/tmp/toe-collision-campaign-20260907 | 481628 | 101087410 | 31 | True |
| /private/tmp/toe-compact-cutoff-campaign-20260907 | 490724 | 101246584 | 30 | True |
| /private/tmp/toe-compact-gap-campaign-20260907 | 490240 | 101235252 | 30 | True |
| /private/tmp/toe-compact-hamiltonian-campaign-20260907 | 487360 | 101234920 | 31 | True |
| /private/tmp/toe-continuum-boundary-campaign-20260907 | 494604 | 101290217 | 30 | True |
| /private/tmp/toe-dimension-campaign-20260907 | 486052 | 101362807 | 31 | True |
| /private/tmp/toe-finite-pw-confinement-campaign-20260907 | 496728 | 101435395 | 30 | True |
| /private/tmp/toe-finite-pw-energy-campaign-20260907 | 495588 | 101299382 | 30 | True |
| /private/tmp/toe-finite-transporter-campaign-20260907 | 495100 | 101296062 | 30 | True |
| /private/tmp/toe-full-transfer-campaign-20260907 | 487004 | 101215666 | 30 | True |
| /private/tmp/toe-heat-campaign-20260907 | 483096 | 101073491 | 30 | True |
| /private/tmp/toe-infinite-static-campaign-20260907 | 494040 | 101282931 | 30 | True |
| /private/tmp/toe-local-observable-campaign-20260907 | 491700 | 101259393 | 30 | True |
| /private/tmp/toe-native-flux-campaign-20260907 | 486160 | 101321104 | 30 | True |
| /private/tmp/toe-native-flux-error-campaign-20260907 | 486340 | 101198168 | 30 | True |
| /private/tmp/toe-priority-formation-campaign-20260907 | 485856 | 101322028 | 30 | True |
| /private/tmp/toe-profile-tradeoff-campaign-20260907 | 485828 | 101322103 | 30 | True |
| /private/tmp/toe-record-campaign-20260907 | 479624 | 101699445 | 43 | True |
| /private/tmp/toe-spatial-area-campaign-20260907 | 492288 | 101265378 | 30 | True |
| /private/tmp/toe-spatial-correction-campaign-20260907 | 487996 | 101220470 | 30 | True |
| /private/tmp/toe-spatial-cubic-campaign-20260907 | 486680 | 101213666 | 30 | True |
| /private/tmp/toe-spatial-gaussian-campaign-20260907 | 486332 | 101207613 | 30 | True |
| /private/tmp/toe-spatial-weak-coupling-campaign-20260907 | 485852 | 101322179 | 31 | True |
| /private/tmp/toe-spatial-wilson-campaign-20260907 | 483336 | 101136437 | 30 | True |
| /private/tmp/toe-static-geodesic-campaign-20260907 | 492764 | 101270981 | 30 | True |
| /private/tmp/toe-static-uniform-campaign-20260907 | 493652 | 101277571 | 30 | True |
| /private/tmp/toe-volume-gap-campaign-20260907 | 491208 | 101253022 | 30 | True |
| /private/tmp/toe-wilson-campaign-20260907 | 482732 | 101061576 | 30 | True |

## Exclusions

All September8 worktrees, the native-record-bridge September7 source parent, raw probe directories, user dirty checkouts and Projects worktrees were excluded. No cleanup recommendation is based solely on age. This inventory grants no automatic removal authorization and does not claim other ongoing threads have released these source paths.

## Preservation procedure for root

Recheck candidate status and live branch head; confirm no active owner. Hash/archive ignored files requiring preservation, especially any lock metadata or unique forensic output, then verify archive content before worktree removal. Keep the corresponding branch ref and remote branch. The current inventory contains exact HEADs and ignored-file hashes, but no archive was created by this read-only task.

Lock follow-up: the spatial-weak-coupling lock names PID87232 and expiry2026-09-07T20:08:23Z. A targeted ps query returned exit1/no such process. This supports treating that particular lock as stale, but does not prove all thread consumers are inactive. Ignored content hashing found833 distinct hashes,829 appearing in only one inspected checkout; many are generated/bytecode variants. Consequently these ignored bytes must not be called byte-identical duplicates without reference to the hash groups.


# Authorized cleanup completed

All31 worktrees and branches remain. Archived every unchanged inventoried ignored regular file in31 separate gzip tar archives under /private/tmp/toe-campaign-preserved-ignored-20260908. Every archive member payload was read back and SHA256/size verified before deletion; mode/uid/gid checked, timestamps preserved by tar/PAX and nanosecond source metadata recorded in manifests. Full archive hashes and exact member metadata are in CLEANUP_RESULT.json and per-worktree manifest files. No archive is inside a Git worktree.

Removed 892 verified ignored regular files, 3139040369 bytes. Compressed archives total 517915252 bytes; net logical payload saving2,621,125,117 bytes (about2.44GiB). There were 63 conservative skips: lock/guard metadata was archived but left in place. Every source hash, mtime, ignored classification, HEAD and clean status was checked again; active path-reference snapshots found none. Every checkout remains tracked/untracked clean afterward. No worktree, tracked/untracked file, raw science directory or branch was removed.

Filesystem free space changed from56,520,800KiB to59,072,832KiB in the observed df snapshots (about2.43GiB increase). Other concurrent activity can affect df, so the exact removed/archive byte accounting is the attributable payload measure.

## Restoration

Restore first into a fresh external directory to avoid overwriting regenerated cache files:

```sh
mkdir -p /private/tmp/toe-ignored-restore-review
tar -xpf /private/tmp/toe-campaign-preserved-ignored-20260908/toe-anisotropic-source-campaign-20260907.tar.gz -C /private/tmp/toe-ignored-restore-review
```

Use that archive's ARCHIVE_MANIFEST.json to verify each relative file's SHA256 before selectively restoring to its original worktree path. The same command pattern applies to every exact archive path recorded in CLEANUP_RESULT.json. Do not blindly overwrite newly generated files; source metadata in the manifests allows a deliberate restoration.


## Superseding final authorization
All31 candidate worktrees were subsequently removed with branches preserved, and disposable temporary archives deleted. See FINAL_CLEANUP_REPORT.md and WORKTREE_REMOVAL_RESULT.json; earlier archive restoration instructions are historical, not current.
