# Block 109 source-binding correction and attempt-02 freeze

This immutable record corrects one statement in `DRAFT_004`: the Block 109
axiom guard did not match at source commit
`956deb7c8e14e01086205bd6c688839602233e6b`. The draft's abbreviated displayed
hash was right, but the runner literal was only 62 characters:

```text
93af34cf6fcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753
```

The actual file SHA-256 is 64 characters:

```text
93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753
```

Attempt 01 finished without a wall or RSS kill. It recorded
`nonzero_exit`, `PASS=8 FAIL=1`: every science family passed and only
`A-source-input-closure` failed. Elapsed time was 87.33 seconds at the outer
wrapper, with sampled process-group peak RSS 110,968,832 bytes. The exact
preflight, execution JSON, stdout, empty stderr, and failed canonical cache are
preserved without overwrite under `producer-attempt01-109/`; its
`MANIFEST.json` SHA-256 is
`20c97656079d8814a10da8fb9a2334b8b7655ff50c11b81ce2a1e88088d9e16a`.

The literal-only correction is commit
`6af58b707f66d6f1bcad1c161525457658ebed68`. Before authorizing attempt 02,
an AST read compared all three fixed guard values directly to the current file
bytes, required each value to have length 64, and called the source-input
certificate without running the scientific `main()`; every equality was true.

Attempt-02 identities are:

- Block 109 runner SHA-256:
  `75482929c76a154eb21899022926b7e93f0d6bee990bd9ccab2d003c2f424987`
- Block 109 input fingerprint:
  `74996c17ee77a019ef7fe12bcf433cbb57e409b599eb2b7c837870d087f3af60`
- Block 110 runner SHA-256, unchanged:
  `6122f98192c94927c0096837e8d2ebbab88039188d2a650c5fcbf7f255113ffa`
- Block 110 input fingerprint after the imported-runner correction:
  `8c513feb186dda66ba7dd6aaa54cebcd60a366a572f43a0cbd9035221ddd37c5`

The coordinator authorized one corrected Block 109 attempt under the unchanged
180-second runner timeout, 195-second outer wall, 2 GiB process-group RSS cap,
and single-thread environment. The failed source bytes will not be retried.

