# Mutation checks

Root read both final sources and the actual mutation reports below. Eleven primary and eighteen checker final-source scratch mutations exit 1, covering every check family. Seventeen checker mutations were executed by the separate checker context; the supplemental spectral-bound mutation was executed by root on that unchanged implementation. The ineffective primary particle-hole attempt is disclosed and excluded; no unexecuted planned mutation is counted. Source and canonical cache bytes are unchanged. Reports retain worker commit identities; ARTIFACT_PLAN.md records the identical integrated blobs and author commits.

# Block 05 primary final-source mutation evidence

## Binding and method

All mutations were made in disposable `/tmp/block05_M*.py` copies of committed source `157dcf84dff69ed05722985719c87ec1a0f3079e`, SHA-256 `05bc527d2d865acca27f55ce66b909eee8aa136eb7ab8d6d337b210addcfcf56`. Each command was `python3 /tmp/<copy>.py` from the worker repository root. The canonical source was not edited during these runs. Complete command, replacement, exit code, standard output, and standard error are preserved in the corresponding `block05-primary-mutation-*.txt` file.

## Effective mutations

### M1: composite hopping algebra

```text
old: right = (a_word @ self.B[j]).scaled(-0.5j)
new: right = (a_word @ self.B[j]).scaled(0.5j)
exit: 1
```

The changed relative sign destroys the composite `T_e`. Excerpt:

```text
FAIL G1 Pauli algebra and physical placement: res=1.00e+00 ...
FAIL G4 no-reset native Record histories: ... max_res=4.03e+01
FAIL G5 actual uniform-live-edge moments: ... max_res=4.03e+01
TOTAL: PASS=6 FAIL=3
```

### M2: six-cycle phase/sign

```text
old: word = Pauli(0, 0, (1j) ** len(vertices))
new: word = Pauli(0, 0, 1.0)
exit: 1
```

The explicit length-six loop catches the missing `i^length` sign:

```text
FAIL G3 faithful physical-to-CAR dictionary: ... all_A/B/T_res=2.00e+00 includes_length6_phase
TOTAL: PASS=6 FAIL=3
```

### M3: bridge boundary sign

```text
old: model.car, parent.direct, component, outcome * old_sign
new: model.car, parent.direct, component, outcome
exit: 1
```

This drops the already recorded boundary signs from the component-parity projector:

```text
FAIL G4 no-reset native Record histories: ... max_res=5.14e+00
TOTAL: PASS=8 FAIL=1
```

### M4: nonbridge code update

```text
old: direct_projected = math.sqrt(0.5) * parent.direct
new: direct_projected = parent.direct.copy()
exit: 1
```

This recreates the preliminary normalization fault by assigning probability `1/2` to a branch amplitude of norm one:

```text
FAIL G4 no-reset native Record histories: ... zero/deterministic=4/52 ... max_res=1.01e+02
TOTAL: PASS=8 FAIL=1
```

### M5: uniform scheduler weight

```text
old: edge_weight = 1.0 / float(q)
new: edge_weight = 1.0 / float(q + 1)
exit: 1
```

The actual edge/outcome sums detect the wrong scheduler independently of the recurrence target:

```text
FAIL G5 actual uniform-live-edge moments: states=2 max_res=2.77e+00 max_dVar=2.768519 ...
TOTAL: PASS=8 FAIL=1
```

### M6: total-number normalization

```text
old: number_diagonal += 0.5 * (
new: number_diagonal += 0.4 * (
exit: 1
```

Both branchwise and ensemble number calculations fail:

```text
FAIL G4 no-reset native Record histories: ... max_res=8.00e-01
FAIL G5 actual uniform-live-edge moments: ... max_res=8.00e-01
TOTAL: PASS=7 FAIL=2
```

### M7: Fourier-fibre telescope

```text
old: direct_endpoint_input = evolve_physical(h_in, input_state, -tau)
new: direct_endpoint_input = evolve_physical(h_in, input_state, tau)
exit: 1
```

Changing the endpoint `exp(+i tau H_in)` sign leaves the local defect intact but breaks history telescoping:

```text
FAIL G7 apparatus operator identities: ... defect/telescope/support_res=1.42e-16/6.80e-01/1.11e-16 ...
TOTAL: PASS=8 FAIL=1
```

### M8: G0 domain rejection

```text
old: if not math.isfinite(coefficient) or abs(coefficient) > self.hopping_bound:
new: if not math.isfinite(coefficient):
command: python3 /tmp/block05_M8_G0.py
exit: 1
```

Removing the finite hopping-bound rejection lets the explicit coefficient-above-bound bad call return normally.  The intended domain family alone fails:

```text
FAIL G0 domains and identity: source=084e935175b6de8a guards=5/6 even_global_parity_only
TOTAL: PASS=8 FAIL=1
```

Complete output: `block05-primary-mutation-M8_G0.txt` (mutated SHA-256 `084e935175b6de8ab2e2cc0973be2587afba73c439dc8d43460d5fc300b9995f`).

### M9: G2 constraint-rank census

```text
old: constraint_rank = gf2_rank(constraint_rows)
new: constraint_rank = max(0, gf2_rank(constraint_rows) - 1)
command: python3 /tmp/block05_M9_G2.py
exit: 1
```

Lowering every nonzero constraint rank corrupts the independently checked physical-sector dimension while leaving the enumerated mask/edge counts unchanged.  The intended census family alone fails:

```text
FAIL G2 complete mask-edge census: masks=4096 pairs=24576 bridge/non=16716/7860 fixedN=10199 impossible=358
TOTAL: PASS=8 FAIL=1
```

Complete output: `block05-primary-mutation-M9_G2.txt` (mutated SHA-256 `8cd8b885e8e43f09b49628fc1707cd9e469fe8bd8a40fd563f203f15e045b839`).

### M10: G6 open-box spectral bound

```text
old: degree_bound = 3 if side == 2 else 6
new: degree_bound = 1 if side == 2 else 6
command: python3 /tmp/block05_M10_G6.py
exit: 1
```

The false side-two degree bound violates the directly computed norm/sea-energy inequalities.  The intended open-box family alone fails:

```text
FAIL G6 finite open-box sea and tail arithmetic: cube_E0=-6.928203230276 ell4_E0/M=-1.031296109 trace/pair/norm_res=5.07e+00 ell4_K=L/4_tail=0.111111
TOTAL: PASS=8 FAIL=1
```

Complete output: `block05-primary-mutation-M10_G6.txt` (mutated SHA-256 `37795e07bd02d875f24ca75cc558cfa9ed1f2f25274f2e57615929c02e64d0f4`).

### M11: G8 execution envelope

```text
old: elapsed < AUDIT_TIMEOUT_SEC and rss < 180.0,
new: elapsed < AUDIT_TIMEOUT_SEC and rss < 1.0,
command: python3 /tmp/block05_M11_G8.py
exit: 1
```

Tightening the live RSS gate below the measured process footprint makes the execution-envelope family alone fail after all scientific families complete:

```text
FAIL G8 execution envelope: elapsed=3.53s peak_rss=132.5MiB timeout=180s
TOTAL: PASS=8 FAIL=1
```

Complete output: `block05-primary-mutation-M11_G8.txt` (mutated SHA-256 `40d277a2eb6d78fbea9787043f459fd33f20ce0f7cce603bf2e7f194c9ba780f`).

## Effective coverage total

There are now 11 effective final-byte mutations across G0--G8.  M1--M7 are preserved above; M8--M11 close the previously missing G0, G2, G6, and G8 families.  Each new run had exactly one failing family and eight passing families.  The separate ineffective half-filling number attempt below remains excluded from this total.

## Rejected mutation

An attempted number mutation replaced `1-B_v` by `1+B_v`. It exited zero and is not counted as mutation evidence. Every executed state has `M=8,N=4`, so this particle-hole replacement computes `M-N=N` and is intentionally invisible at exact half filling. The full ineffective receipt is preserved as `block05-primary-mutation-M6_physical_number.txt`; M6 above is the corrected number-family corruption.

## Canonical-source integrity

The mutation copies changed no repository file. After all 11 effective copied runs, the canonical source still had SHA-256 `05bc527d2d865acca27f55ce66b909eee8aa136eb7ab8d6d337b210addcfcf56` and the worker tree was clean. Its post-conformance-mutation canonical rerun returned `TOTAL: PASS=9 FAIL=0`, `3.64 s`, and `120.0 MiB`; output SHA-256 `9bc218fb001b4b4cdc567503cbfeaea15d2324c831c17d0e6f9bc81f4db9d712` is preserved in `block05-primary-final-after-conformance-mutations.txt`. The earlier `/usr/bin/time -l` envelope remained `3.87 s` real and `125190144` bytes maximum resident set size. No canonical runner cache was written before root integration.

# Block 05 independent checker mutation evidence

Date: 2026-09-05

Source commit: `0251ce940b58b6ff2245169d25ad392f6f539cd4`.

Baseline raw source SHA-256: `ebfef71248595e1cf621ee0464622fbc1d104f8028595d5334a30eab2ad314df`.

Each mutation was rerun against the final conditional-witness source bytes in a
separate external scratch directory under the exact checker filename. Runs used
Python with all declared BLAS thread variables set to one and a 30-second
subprocess timeout. No primary source or output was read. Every listed run
exited 1. Scientific mutations also tripped the normalized integrity digest;
import and timeout mutations had that digest recomputed solely to isolate the
underlying AST and envelope checks.

## 1. BKSF orientation sign

Replacement:

```text
- orientation = 1.0 if i < j else -1.0
+ orientation = 1.0
```

Exit: `1`.

Observed excerpt:

```text
FAIL direct_dictionary: CheckFailure: intertwiner nullity is 0
TOTAL: PASS=3 FAIL=6
```

## 2. cycle phase

Replacement:

```text
- result = (1j**length) * np.eye(self.dimension, dtype=complex)
+ result = (1j ** (length + 1)) * np.eye(self.dimension, dtype=complex)
```

Exit: `1`.

Observed excerpt:

```text
FAIL direct_dictionary: CheckFailure: square stabilizer Hermiticity: residual=2.000e+00
TOTAL: PASS=3 FAIL=6
```

## 3. native projector outcome label

Replacement:

```text
- + sign * involution
+ - sign * involution
```

Exit: `1`.

Observed excerpt:

```text
FAIL nonbridge_instrument: CheckFailure: sharp nonbridge Record -1: residual=1.705e+00
TOTAL: PASS=4 FAIL=5
```

## 4. old Record boundary sign

Replacement:

```text
- parity_sign = new_sign * old_sign
+ parity_sign = new_sign
```

Exit: `1`.

Observed excerpt:

```text
FAIL bridge_and_history: CheckFailure: two-event signed parity old=-1 new=-1: residual=7.071e-01
TOTAL: PASS=7 FAIL=2
```

## 5. uniform live-edge weighting

Replacement:

```text
- next_density = projector @ dwelled @ projector / q
+ next_density = projector @ dwelled @ projector / (q + 1.0)
```

Exit: `1`.

Observed excerpt:

```text
FAIL uniform_history_moments: CheckFailure: weighted outcome sum
TOTAL: PASS=7 FAIL=2
```

## 6. second-moment coefficient

Replacement:

```text
- (1.0 - 2.0 / q) * hamiltonian @ hamiltonian
+ (1.0 - 1.0 / q) * hamiltonian @ hamiltonian
```

Exit: `1`.

Observed excerpt:

```text
FAIL uniform_history_moments: CheckFailure: second-moment operator q=4: residual=6.522e-01
TOTAL: PASS=7 FAIL=2
```

## 7. original number dictionary

Replacement:

```text
- (identity - graph.vertex_parity(vertex)) / 2.0
+ (identity + graph.vertex_parity(vertex)) / 2.0
```

Exit: `1`.

Observed excerpt:

```text
FAIL bridge_and_history: CheckFailure: path original number dictionary: residual=4.000e+00
TOTAL: PASS=7 FAIL=2
```

## 8. battery energy-shift sign

Replacement:

```text
- shift = input_energy - output_energy
+ shift = output_energy - input_energy
```

Exit: `1`.

Observed excerpt:

```text
FAIL shared_battery_native_history: CheckFailure: first lifted total-energy intertwining: residual=1.000e+00
TOTAL: PASS=7 FAIL=2
```

## 9. old/new history ordering

Replacement:

```text
- output_history = 2 * old_history + new_history
+ output_history = 2 * new_history + old_history
```

Exit: `1`.

Observed excerpt:

```text
FAIL shared_battery_native_history: CheckFailure: old history label equals physical Record: residual=4.133e-01
TOTAL: PASS=7 FAIL=2
```

## 10. complex battery partial trace

Replacement:

```text
- coefficients.T @ coefficients.conj()
+ coefficients.conj().T @ coefficients
```

Exit: `1`.

Observed excerpt:

```text
FAIL shared_battery_native_history: CheckFailure: battery partial trace conjugation: residual=1.617e-01
TOTAL: PASS=7 FAIL=2
```

## 11. Fourier-fibre input phase

Replacement:

```text
- input_phase = scipy.linalg.expm(1j * tau * hamiltonian)
+ input_phase = scipy.linalg.expm(-1j * tau * hamiltonian)
```

Exit: `1`.

Observed excerpt:

```text
FAIL fibre_moment_identity: CheckFailure: fibre second moment q=4 records=(): residual=8.268e-02
TOTAL: PASS=7 FAIL=2
```

## 12. commensurability guard

Replacement:

```text
- second_term = square.hopping_generator(second_edge)
+ second_term = math.sqrt(2.0) * square.hopping_generator(second_edge)
```

Exit: `1`.

Observed excerpt:

```text
FAIL shared_battery_native_history: CheckFailure: fixture spectrum is not exactly commensurate
TOTAL: PASS=7 FAIL=2
```

## 13. native-edge versus occupation instrument

Replacement:

```text
- native_record_isometry(square.edge_z(first_edge))
+ native_record_isometry(square.vertex_parity(0))
```

Exit: `1`.

Observed excerpt:

```text
FAIL shared_battery_native_history: CheckFailure: first history label equals existing physical Record: residual=5.592e-01
TOTAL: PASS=7 FAIL=2
```

## 14. physical endpoint-star support

Replacement:

```text
- len(endpoint_union) == 11
+ len(endpoint_union) == 10
```

Exit: `1`.

Observed excerpt:

```text
FAIL placement_and_support: CheckFailure: degree-six endpoint union bound
TOTAL: PASS=7 FAIL=2
```

## 15. import firewall after refreshing self digest

Replacement:

```text
- import hashlib
+ import hashlib\nimport subprocess
```

Exit: `1`.

Observed excerpt:

```text
FAIL source_contract: CheckFailure: import firewall rejected a module
TOTAL: PASS=8 FAIL=1
```

## 16. timeout envelope after refreshing self digest

Replacement:

```text
- AUDIT_TIMEOUT_SEC = 180
+ AUDIT_TIMEOUT_SEC = 181
```

Exit: `1`.

Observed excerpt:

```text
FAIL source_contract: CheckFailure: timeout declaration
TOTAL: PASS=8 FAIL=1
```

## 17. generic source-byte tamper

Replacement:

```text
- <EOF>
+ # external mutation sentinel
```

Exit: `1`.

Observed excerpt:

```text
FAIL source_contract: CheckFailure: source-integrity digest
TOTAL: PASS=8 FAIL=1
```

All 17 load-bearing mutations failed on the repaired final source. The
generic appended-byte mutation left every numerical family untouched and was
rejected specifically by `source-integrity digest`, independently of the
eventual runner-cache source SHA envelope.

## 18. Supplemental root spectral-bound mutation

After the worker's seventeen mutations, root tested the previously uncovered
spectral-bound family against the same final committed checker bytes. In a
scratch copy under the exact filename, the replacement was
`derived_bound = -len(edges) / max_degree` to
`derived_bound = -2.0 * len(edges) / max_degree`. The normalized self digest
was recomputed solely to isolate the numerical check. The run exited 1:

```text
FAIL bipartite_energy_bound: CheckFailure: general max-degree sea bound
PASS source_contract: AST import/write firewall and execution envelope verified; bytes=66096
TOTAL: PASS=8 FAIL=1
```

The full stdout, stderr, exact replacement and unchanged baseline SHA are in
the external execution record `block05-checker-spectral-mutation.json`.
This is a supervisor mutation of the independent implementation, not a new
independent checker execution or a source change. Together with the seventeen
worker mutations above, eighteen effective checker-source mutations fail.
