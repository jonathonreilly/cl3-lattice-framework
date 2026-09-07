# Field source block handoff

Allowed authored source files:

- `docs/SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md`
- `scripts/spin_half_cartesian_plaquette_source_2026_09_07.py`
- `scripts/spin_half_cartesian_plaquette_source_independent_check_2026_09_07.py`

The note is self-contained and conditional on the supplied carrier,
Hamiltonian, and electric map. It proves the all-local-domain source map,
gives an exact finite source discriminator, records corrected finite
continuous-source curvatures, and distinguishes the fully relaxed full-flux
endpoint from magnetic-flux-sector energy. Its affected-PR table uses frozen
heads. Raw electric/spectral/kernel statements are not invalidated by this
source-identification finding.

Actual checks: primary `19/0`, independent helper `55/0`; six response
values agree within `6.61e-15`. The exact independent Laurent-polynomial
second derivatives agree with the primary integer product-rule calculation.
Seven targeted scratch mutations all exited nonzero with scientific-check
failures. `verification.json` binds runner SHA-256 hashes and complete
commands; `primary/independent.json` and `.log` contain full evidence.
`INDEPENDENT_PROVENANCE.json` records the independent author's original
scratch code hash and packaging changes. The final note states that
same-checker confirmation of these final packaged files remains for root.

Reproduce baselines and mutation controls from the worktree root:

```bash
OPENBLAS_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-campaign-20260907/field/verify_and_mutate.py
```

The seven changed scripts under `mutants/` are deliberate scratch negatives,
not science source. No existing PR branch, main file, audit record, shared
planning pack, or another worker's files were modified. No commit, push,
PR/comment action, or formal audit was performed. Source scripts compile
without generating cache files. `git diff --check` was run but does not
inspect these untracked files; the final source review should inspect them
as additions.
