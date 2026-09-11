# Released 7981→7988 Recovery Correction Record

This directory preserves the complete source surfaces of original PR 7981
followed by PR 7988 while the live Block 213 and Block 214 notes and runners
are prepared on correction source base
`1157173587fde42555d36659954e71c544e23312`.

## Immutable original bodies

The original graph is:

- PR 7981: `4e9931a970ded94f769553da9e6d77770d612f64` →
  `851aff9b3f950e5f08b0bd0878df2e1992bbe15b`;
- PR 7988: `851aff9b3f950e5f08b0bd0878df2e1992bbe15b` →
  `1dc2ae2557a22ef188f344665bc00edc2593d113`.

Their actual deltas contain 34 body occurrences across 28 unique paths. Six
weighted-packet paths occur in both deltas, and both historical states are
preserved. The recovery bundles use deterministic gzip followed by base64;
decoding preserves every original byte, including cache whitespace.

Four actually used historical helper sources are preserved separately:
Block 201's lane construction, Block 211's cell family, Block 209's exterior
corner machinery reached through Block 211, and the historical Block 105
Hodge assembler. They are recovery provenance. The live runners do not import
them or make their unexecuted parent claims current.

Run the read-only verifier from the repository root:

```bash
python3 .claude/science/physics-loops/released7981-7988-recovery-20260910/verify_original_source_recovery.py
```

## Correction boundary

The prior held checkpoint independently verified the supplied-matrix
17-variable determinant identity, with no source PASS. That unchanged
calculation is reused rather than repeated during author preflight.

Block 214's general `D07` congruence and Schur shift remain valid. The
congruence does not prove a general off-star-line branch rescaling: the exact
positive-definite counterexample
`H=I8+(E07+E70)/4+(E16+E61)/3`, `k=(1,2,3)` gives candidate
`224/15` but nonzero residual `528724036/455625`. The live branch result
is therefore restricted to the degree-diagonal/star-line specialization.
The general block determinant identity carries `(-1)^n`; its `n=4`
specialization has the positive sign used by this packet.

The finite cell forms, exterior differential, assemblies, and weighted kernel
are supplied algebraic objects. No action-derived physical selector, kernel,
metric, gravity, causal cone, propagator, dynamics, or continuum theorem is
adopted.

## Producer state

The corrected source freeze is commit
`2e60673f8d1668fd229f02096b79c78eda65de5f`. It has literal runner/input
hashes and parser-visible note citation edges. After explicit coordinator GO,
each producer ran exactly once, sequentially, through the reviewed process-group
watchdog; neither was retried.

- Block 213: all gate families `A`–`I` pass, `PASS=36 FAIL=0`; runner SHA-256
  `d80ce0e3168968fcc1a887e6737681e4cdfc31c82813813415f008a68507088d`,
  input fingerprint
  `017fc6165dab5e76aa6c23ab488235d2b7319aa02ff11dc7fc68abe47838ce28`,
  cache SHA-256
  `c7f7ca09ba51da62fd1283ea197466a75b88f0e24adad327a5b33c93584050f7`.
  The wrapper elapsed time was `64.033` seconds and sampled peak process-group
  RSS was `168919040` bytes.
- Block 214: all gate families `A`–`I` pass, `PASS=33 FAIL=0`; runner SHA-256
  `f0d70c67c5a13a53995698752276a10183dc77e46e7446617e10817603a74b91`,
  input fingerprint
  `6a450e183f05b54f4b4136ab5e1edb621146cc88fda29079f10366e6d94710da`,
  cache SHA-256
  `a6d83d53bc7f9ff415c0bc766d2b8b0b704b49068c3fac2cd734c3c6271d3a5e`.
  The wrapper elapsed time was `178.572` seconds and sampled peak process-group
  RSS was `106971136` bytes.

Both runs exited zero, wrote fresh canonical caches, preserved pre/post source
identity, produced empty wrapper stderr files, and incurred no wall-time or RSS
kill. External immutable preflight and execution receipts are under
`7981-7988/fixes/` in the owner campaign evidence directory.
