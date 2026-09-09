# L1h half-filling interaction raw recovery

This directory is a byte-preserving copy of the surviving L1h campaign source
and text output. It is historical evidence, not a retained runner.

The original `mb.py` inserted an absolute scratch path before importing
`common`. A copy of that dependency is preserved under `dependencies/`.
On a checkout where the old scratch path does not exist, run a probe with:

```bash
PYTHONPATH=dependencies python3 part6_sweep.py
```

The recovered `part6_sweep.py` was rerun from this archived layout on
2026-09-03 and reproduced its preserved census.

`part2_out.pkl.b64` is the base64 representation of the recovered serialized
object. Decode it to `part2_out.pkl` before checking `SHA256SUMS`.
