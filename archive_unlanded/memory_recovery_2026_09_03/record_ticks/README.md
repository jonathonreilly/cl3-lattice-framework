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

## Review caveats added 2026-09-09

The source and output are unchanged historical evidence. No retained or
verified label inside them grants current status. In particular:

- `l3c_theorem.py` tests the common kernel of Hamiltonian differences. An empty
  kernel excludes equal-action vectors, not all common eigenvectors or
  stationary pure density matrices. For example, `diag(0,1)` and `diag(2,3)`
  have invertible difference and share both coordinate eigenvectors. The
  script's broader invariance/no-tick conclusion is unsupported. Its asserted
  equivalence between unchanged finished probabilities and trivial action in
  every gap is also not established by these checks.
- The printed minimum of `||Q H_R g_b||^2` is zero. The output's claim that
  every site/value immediately destroys forbidden-subspace annihilation does
  not follow. Positive variance and averaged leakage are narrower observations.
- `l3c_run.py`, `l3c_main.py` and `l3c_out.txt` identify energy dephasing with
  the slow-formation limit at fixed tick interval without excluding resonances.
  Averaging a phase over geometric waiting times gives
  `q / (1 - (1-q) exp(-i theta))` for waits starting at zero. As `q` tends to
  zero, this retains coherences when `theta = tau(E_a-E_b)` is a multiple of
  `2 pi`. Unconditional dephasing in energy eigenspaces is therefore not
  justified for all fixed intervals.

The original 2026-09-03 rerun statement above is a historical report; no
campaign was rerun for this archival landing. A current theorem would require
a corrected argument and reproducible evidence at its exact finite scope.
