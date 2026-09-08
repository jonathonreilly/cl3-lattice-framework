# Final authorized worktree cleanup and recovery

All31 approved old September7 campaign checkouts were removed using ordinary git worktree remove, without --force. Zero candidates were skipped. Every local branch remains at its exact original HEAD, and that HEAD matched the live origin branch immediately before removal. No branch was deleted. Root confirmed no app task owned these paths; each candidate also passed fresh status/HEAD/open-handle/process checks.

Temporary gzip archives were then deleted only after matching their recorded hashes and classifying every archived path as generated audit cache, Python bytecode or stale lock metadata. No unique proof or raw scientific production appeared. Concise manifests and recovery mapping remain for root to publish remotely. The earlier archive-restoration instructions in REPORT.md are historical and superseded: those disposable archives no longer exist.

Removed checkout allocation: 12063200 KiB. Deleted temporary archives: 517915252 bytes. Observed df available rose58,655,236→71,844,108KiB, about12.58GiB; concurrent activity may affect this delta.

## Recovery mapping

| Original path | Preserved branch | Exact HEAD |
|---|---|---|
| /private/tmp/toe-anisotropic-source-campaign-20260907 | refs/heads/codex/anisotropic-source-semigroup-block26-20260907 | d57943620edd5098df7b6410f952d569730276f5 |
| /private/tmp/toe-autonomous-campaign-20260907 | refs/heads/codex/record-autonomous-head-block02-20260907 | 5bd7f234bd185eceaeb36e496a5b6bf4c69a1835 |
| /private/tmp/toe-clock-campaign-20260907 | refs/heads/codex/record-autonomous-clock-block08-20260907 | fcea79f576bd276004d33306a487cfb7577d418e |
| /private/tmp/toe-collision-campaign-20260907 | refs/heads/codex/record-collision-control-block05-20260907 | fb81c52351baea499c81f517a3d32ef8db10d065 |
| /private/tmp/toe-compact-cutoff-campaign-20260907 | refs/heads/codex/compact-cutoff-block32-20260907 | 4c3b9bd33bfbc2e03b9d91e05849607bc33ec70c |
| /private/tmp/toe-compact-gap-campaign-20260907 | refs/heads/codex/compact-gap-block30-20260907 | cf4eeb62cde4f3a812ae85ab1660232bc468a050 |
| /private/tmp/toe-compact-hamiltonian-campaign-20260907 | refs/heads/codex/compact-hamiltonian-block29-20260907 | 44964a9b72bccb9ae95d5d9b277007910ee86430 |
| /private/tmp/toe-continuum-boundary-campaign-20260907 | refs/heads/codex/continuum-boundary-block40-20260907 | 3dee7c038c60dd9aaddbcc186207f165367cc274 |
| /private/tmp/toe-dimension-campaign-20260907 | refs/heads/codex/dimension-divided-spectral-block16-20260907 | f29251ea68ba2bcd96c807881eae7bc8c6cfd48e |
| /private/tmp/toe-finite-pw-confinement-campaign-20260907 | refs/heads/codex/finite-pw-confinement-block43-20260907 | d041b83a507226feae9713662767dd34d2ffb4a8 |
| /private/tmp/toe-finite-pw-energy-campaign-20260907 | refs/heads/codex/finite-pw-energy-block42-20260907 | 91daeb27ebe4e840b1b0457ea30acfc3e333bd09 |
| /private/tmp/toe-finite-transporter-campaign-20260907 | refs/heads/codex/finite-transporter-block41-20260907 | 3756b77ab56aa397a7113082783c1c491d8d96ea |
| /private/tmp/toe-full-transfer-campaign-20260907 | refs/heads/codex/full-cube-transfer-block28-20260907 | 3b9c0ce91ca0cce5ed32689f95aa469e3fdc4551 |
| /private/tmp/toe-heat-campaign-20260907 | refs/heads/codex/native-heat-spectral-block13-20260907 | 6da2088d2c379839b2dca3977843b33264cd8e30 |
| /private/tmp/toe-infinite-static-campaign-20260907 | refs/heads/codex/infinite-static-block39-20260907 | c5f58f84246c7ee938152dcc317264f8b1384a3f |
| /private/tmp/toe-local-observable-campaign-20260907 | refs/heads/codex/local-observable-block35-20260907 | cf104c1e69c971f37bdca51f775a6165f9f57133 |
| /private/tmp/toe-native-flux-campaign-20260907 | refs/heads/codex/native-flux-record-block21-20260907 | 4aacc14450f2fa7877c25323b1ae25235bae91d5 |
| /private/tmp/toe-native-flux-error-campaign-20260907 | refs/heads/codex/native-flux-error-block25-20260907 | 99bf0f1984aff1a9cd1fde5cc1ef4f667a046544 |
| /private/tmp/toe-priority-formation-campaign-20260907 | refs/heads/codex/record-priority-formation-block18-20260907 | 11395e60ff268110e8d105ebb61ef4102cbf4b4a |
| /private/tmp/toe-profile-tradeoff-campaign-20260907 | refs/heads/codex/record-profile-tradeoff-block19-20260907 | 910fb7caa43ffc5df3d5f16d1c618cba4135fa69 |
| /private/tmp/toe-record-campaign-20260907 | refs/heads/codex/record-battery-transport-block01-20260907 | 707d7a9c7f929c1c2c16078dfed76acb786e5f3b |
| /private/tmp/toe-spatial-area-campaign-20260907 | refs/heads/codex/spatial-area-block36-20260907 | 08d312cdbb643ff661f2abd8b8489bcf0997ba7f |
| /private/tmp/toe-spatial-correction-campaign-20260907 | refs/heads/codex/spatial-wilson-correction-block24-20260907 | fa8cabc8b6f394a4acfcbc7c2be96c3e22ae6307 |
| /private/tmp/toe-spatial-cubic-campaign-20260907 | refs/heads/codex/spatial-wilson-cubic-block23-20260907 | 5680b56f4205536f746340d1f2070e243820981c |
| /private/tmp/toe-spatial-gaussian-campaign-20260907 | refs/heads/codex/spatial-wilson-gaussian-block22-20260907 | 2343266be6c4faf3ba9112ec1cab56b00c471c52 |
| /private/tmp/toe-spatial-weak-coupling-campaign-20260907 | refs/heads/codex/spatial-wilson-weak-coupling-block20-20260907 | fc49894fc09b33042752f69bf33d637955bee208 |
| /private/tmp/toe-spatial-wilson-campaign-20260907 | refs/heads/codex/spatial-wilson-mixing-block15-20260907 | 05f324c9fbfaaecc8f4038d6e9a6b037570e56d0 |
| /private/tmp/toe-static-geodesic-campaign-20260907 | refs/heads/codex/static-geodesic-block37-20260907 | ca0eebe4dffad7a53a201ad7773e804b8c89edef |
| /private/tmp/toe-static-uniform-campaign-20260907 | refs/heads/codex/static-uniform-block38-20260907 | 36843ba7b46901269911496f8dfdef6fd5f63cae |
| /private/tmp/toe-volume-gap-campaign-20260907 | refs/heads/codex/volume-uniform-gap-block34-20260907 | 1c814b95243c5f788f57bab57c67fdc542f1aab4 |
| /private/tmp/toe-wilson-campaign-20260907 | refs/heads/codex/native-wilson-second-order-block10-20260907 | 9450957fc039bf362bd2ca3d71d301d35d55cf40 |

To recover a checkout, use its preserved branch:

```sh
git worktree add /private/tmp/toe-anisotropic-source-campaign-20260907 codex/anisotropic-source-semigroup-block26-20260907
```

Every exact per-worktree recovery command is in WORKTREE_REMOVAL_RESULT.json. Generated caches can be regenerated from the preserved source as needed; deleted bytecode is recreated by Python. September8 checkouts, native-record-bridge source parent, raw probe directories, current/original user checkouts and Projects worktrees were excluded.

No GitHub or main mutation was performed by this worker. Root owns remote publication of this concise evidence log.
