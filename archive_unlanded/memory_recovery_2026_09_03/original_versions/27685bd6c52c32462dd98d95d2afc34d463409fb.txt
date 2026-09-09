# L3c Record-tick raw recovery

This directory is a byte-preserving copy of the surviving L3c campaign source
and principal output. It is historical evidence, not a retained runner.

The original source inserted an absolute scratch path before importing
`l3_core`. A copy of that dependency is preserved under `dependencies/`.
On a checkout where the old scratch path does not exist, run:

```bash
PYTHONPATH=dependencies python3 l3c_theorem.py
```

The recovered theorem probe was rerun from this archived layout on 2026-09-03
and reproduced the preserved output. `l3c_out.txt` and the omitted
`run.log` were byte-identical; the omitted `run.err` was empty.

`grid_counts.npy.b64` is the base64 representation of the recovered NumPy
array. Decode it to `grid_counts.npy` before checking `SHA256SUMS`.
