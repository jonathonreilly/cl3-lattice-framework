# Released 6515 Recovery Correction Record

This directory preserves the source surfaces of original PR 6485 followed by
PR 6515 while the live notes, runners, and ledgers are corrected on a clean
checkout of main `1157173587fde42555d36659954e71c544e23312`.

## Immutable original bodies

`ORIGINAL_SOURCE_BODIES.json` contains ten body versions across nine distinct
paths. Each body is base64-encoded from its exact Git blob. The two versions
of `docs/audit/data/citation_graph_manifest.json` are included for recovery
only and have no current authority. Base64 preserves every byte of the two
historical cache files, including trailing whitespace.

The bundle was generated from:

- PR 6485 base `8afe8dff5ccf531208238af0aaaec1f547d73874`, head
  `ad84cfcc857a65285389ba93b47cd7b718589be5`;
- PR 6515 base `ad84cfcc857a65285389ba93b47cd7b718589be5`, head
  `d6761278fca9cac617200792473a8f4da3a6cfff`.

Run the read-only verifier from the repository root:

```bash
python3 .claude/science/physics-loops/released6515-recovery-20260910/build_original_source_recovery.py --check
```

It decodes each body, checks its byte count and SHA-256, reconstructs its Git
blob identifier, and compares the bytes to `git cat-file`. The immutable JSON
bundle has SHA-256
`6bdc3acc51eab5ea973c2c5110c7b6be7e974b5f4c2c6fdb447d8fb6ed917afa`.

## Corrections applied to the live surfaces

1. The actual spatial block span is `I_4,D_x,C+C^T,C-C^T`; `D_x` is not
   circulant.
2. Historical claims about a 37-dimensional subspace, 666/8,646 pair scans,
   and gamma extensions are demoted as unexecuted. The 132-dimensional
   linear-space certificate remains live at both fixtures. The positive
   fiber is claimed only for the executed `c=5/13` fixture.
3. The finite `Q`, step profile, and rational fixtures are declared chosen
   algebraic data, with no action-derived physical selection.
4. The signature obstruction is limited to pure-odd Grams. It does not
   exclude mixed even/odd involutions.
5. The Fourier blocks are declared coupled through shared coefficients and
   reality constraints.
6. The anticommutant result is identified as a rank-14/nullity-2 calculation
   in a 16-dimensional trial space of `16 x 16` Gram-side matrices at the
   primary fixture. It is not a `32 x 32` anticommutant of `A_star` inside
   the 132-dimensional dressing class.
7. The 48-coordinate permutation support is reported as linear rank 47 and
   nullity 1, followed by a one-parameter Groebner basis `{1}`. The four
   directed supports separately have full ranks 12 or 24.
8. Live source binding no longer relies on moving Git refs, absent historical
   notes, or stale caches. Block 109 constructs its matrices inline and
   declares its note, the minimal axioms, premise registry, and corrected
   supplier note. Block 110 declares its note, the Block 109 note, and the
   Block 109 runner that it actually imports.

## Cache and authority boundary

The released caches are stale and remain recoverable only from the JSON
bundle. No live citation manifest, planning file, audit result, or GitHub
surface is written by this recovery unit.

The first corrected Block 109 producer attempt at source commit
`956deb7c8e14e01086205bd6c688839602233e6b` recorded `PASS=8 FAIL=1` and
`nonzero_exit`. All eight science families passed; the source-input guard
failed because the typed axiom SHA-256 literal omitted two characters. The
attempt completed in 87.33 seconds without a resource kill, at sampled
process-group peak RSS 110,968,832 bytes. Its cache and complete wrapper
evidence are preserved under the external correction-evidence directory
`producer-attempt01-109/`, whose manifest SHA-256 is
`20c97656079d8814a10da8fb9a2334b8b7655ff50c11b81ce2a1e88088d9e16a`.
Those source bytes were not retried.

The source-binding literal alone was corrected from the actual axiom bytes in
commit `6af58b707f66d6f1bcad1c161525457658ebed68`. The coordinator authorized
one corrected Block 109 attempt under the same caps. It produced the live
cache with `PASS=9 FAIL=0`, `status: ok`, elapsed 90.73 seconds, runner
SHA-256 `75482929c76a154eb21899022926b7e93f0d6bee990bd9ccab2d003c2f424987`,
input fingerprint
`74996c17ee77a019ef7fe12bcf433cbb57e409b599eb2b7c837870d087f3af60`,
and cache SHA-256
`f527e0d46eafbb5aacf6a5e98a945b12c58725739b6a1049cc112159fc5f30a6`.
The outer wrapper completed in 90.84 seconds with sampled process-group peak
RSS 117,063,680 bytes and no limit kill.

Block 110 then ran once. Its live cache records `PASS=8 FAIL=0`, `status: ok`,
elapsed 42.48 seconds, runner SHA-256
`6122f98192c94927c0096837e8d2ebbab88039188d2a650c5fcbf7f255113ffa`,
input fingerprint
`8c513feb186dda66ba7dd6aaa54cebcd60a366a572f43a0cbd9035221ddd37c5`,
and cache SHA-256
`8c86a0bf3541902a46b29ca439596154c40bd165d8ef5c336a113442702bf6c7`.
The outer wrapper completed in 42.68 seconds with sampled process-group peak
RSS 115,310,592 bytes and no limit kill.

Both successful runs used a 180-second runner timeout, a 195-second outer
wall, a 2-GiB process-group RSS cap, and single-thread environment variables.
Pre/post source identities matched. This correction record is not declared in
either runner's `AUDIT_INPUT_PATHS`, so recording these results does not alter
either cache fingerprint.
