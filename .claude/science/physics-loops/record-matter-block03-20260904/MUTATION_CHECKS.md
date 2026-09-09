# Block 03 primary runner mutation checks

**Date:** 2026-09-04
**Canonical source commits:** `7fac0dc80b` (source-only commit before the first v1 certification), `7c0419e8c79a785d6de31d488bbcd9cd25cdd248` (display-only signed-zero normalization), then `9dac0e31f5f93baf25e66d681be7aa0edab6ce59` (finite-weight domain hardening)
**Canonical source:** `scripts/local_record_quench_energy_and_ground_overlap_2026_09_04.py`
**Final source SHA-256:** `331ff5335e1dd99000a04dbaf21420cb3979fdb12aadcbf53b6d6508dc256394`
**Final cache SHA-256:** `e8f3c9271726870c1f3e837716c9486f64aacfec9eef11ea16190d26ce66ecbb`
**Canonical certification:** runner cache v1 is fresh for the final source, exits `0`, reports `PASS G0 constructor domains: rejections=10/10`, and ends `TOTAL: PASS=14 FAIL=0`.
**Method:** Each case copies the committed canonical source to a fresh `/tmp` path, requires one exact source string to occur once, replaces it once, and executes that scratch copy from the block-03 worktree. The canonical source is never modified. A mutation passes this exercise only when the corrupted copy exits nonzero and emits a `FAIL` in the intended substantive family. All six cases were rerun against final commit `9dac0e31f5`; the excerpts below are the final rerun outputs.

## G1 — Gaussian conditioning / closed comparator

- Exact replacement: `lower += (0.5 - float(outcome)) * np.outer(row.conj(), row)` → `lower += (0.5 + float(outcome)) * np.outer(row.conj(), row)`.
- Command: `python3 /tmp/block03_mutation_g1.py > /tmp/block03_mutation_g1.out 2>&1`.
- Exit: `1`.
- Computed excerpt:

```text
FAIL G1 all iterative occupation branches: max_res=4.000e+00 subsets=empty/full/nonreducing outcomes=21
TOTAL: PASS=13 FAIL=1
```

## G2 — energy and reduced fixed-number ground subtraction

- Exact replacement: `ground_formula = -float(np.trace(b_matrix).real)\n            particle_number = target_number` → `ground_formula = +float(np.trace(b_matrix).real)\n            particle_number = target_number`.
- Command: `python3 /tmp/block03_mutation_g2.py > /tmp/block03_mutation_g2.out 2>&1`.
- Exit: `1`.
- Computed excerpt:

```text
FAIL G2 branch energy and fixed-N ground subtraction: max_res=1.320e+01
FAIL G2 bounds and diagonal-K control: max_violation=1.320e+01 diagonal_jump=1.300000 diagonal_delta=2.665e-15
TOTAL: PASS=12 FAIL=2
```

## G3 — staggered cubic geometry

- Exact replacement: `plaquette_residual = max(plaquette_residual, abs(product + 1.0))` → `plaquette_residual = max(plaquette_residual, abs(product - 1.0))`.
- Command: `python3 /tmp/block03_mutation_g3.py > /tmp/block03_mutation_g3.out 2>&1`.
- Exit: `1`.
- Computed excerpt:

```text
FAIL G3 staggered cubic geometry: max_res=2.000e+00 boundary_twists=-1,+1,-1
TOTAL: PASS=13 FAIL=1
```

## G4 — singleton resolvent quadrature

- Exact replacement: `return (2.0 / np.pi) * x_value * x_value * variance / mean` → `return (1.0 / np.pi) * x_value * x_value * variance / mean`.
- Command: `python3 /tmp/block03_mutation_g4.py > /tmp/block03_mutation_g4.out 2>&1`.
- Exit: `1`.
- Computed excerpt:

```text
FAIL G4 singleton resolvent quadrature: max_abs=3.645e-02 values=0.000000000,0.027161812,0.036451708
FAIL G6 scalar momentum and finite-grid quadratures: identity_max=1.776e-15 actual_max=3.645e-02 diagnostic_only=no_limit_proof
TOTAL: PASS=12 FAIL=2
```

## G5 — overlap counts and leakage

- Exact replacement: `ell_expected = l_scalar / 2.0 + alpha / 4.0` → `ell_expected = l_scalar / 2.0 - alpha / 4.0`.
- Command: `python3 /tmp/block03_mutation_g5.py > /tmp/block03_mutation_g5.out 2>&1`.
- Exit: `1`.
- Computed excerpt:

```text
FAIL G5 particles holes zero mode and leakage: max_res=3.849e-02
TOTAL: PASS=13 FAIL=1
```

## G6 — scalar momentum and finite-grid quadratures

- Exact replacement: `4.0 * sum(np.sin(value / 2.0) ** 2 for value in (qx, qy, qz))` → `3.0 * sum(np.sin(value / 2.0) ** 2 for value in (qx, qy, qz))`.
- Command: `python3 /tmp/block03_mutation_g6.py > /tmp/block03_mutation_g6.out 2>&1`.
- Exit: `1`.
- Computed excerpt:

```text
FAIL G6 scalar momentum and finite-grid quadratures: identity_max=3.000e+00 actual_max=9.767e-03 diagnostic_only=no_limit_proof
TOTAL: PASS=13 FAIL=1
```


All six corrupted scratch copies exited nonzero and named their intended family. No mutation was applied to the canonical source.

# Block 03 independent checker mutation record

Date: 2026-09-04

Canonical source commit: `5767cae37499fff5b4ec892ee6e5abd6d1305ded`

Canonical source SHA-256: `4c5069df7249ef613ee87a661884db3f5ef6e9ea8245a59344ea17c8f6222201`

Method: each probe copies the committed independent checker to a separate
external scratch directory while preserving its exact basename, performs one
literal replacement, and executes that copy. A probe passes this mutation
audit only if the process exits nonzero and stdout contains the intended
`FAIL <family>` line. Scratch copies are not repository artifacts.

## Results

All seven probes exited `1`; each emitted its intended failure family and a
nonzero final failure count.

### 1. Source/import firewall

Exact replacement:

```diff
 import math
+import os
```

Terminal excerpt:

```text
FAIL source_import_firewall: CheckFailure: forbidden import roots: ['os']
TOTAL: PASS=6 FAIL=1
```

### 2. Exact Fock projection and complex adjoint

Exact replacement:

```diff
-h_deleted[2:4, 0] = Q_T.conjugate().T
+h_deleted[2:4, 0] = Q_T.T
```

Terminal excerpt:

```text
FAIL exact_fock_projection: CheckFailure: deleted one-particle Hamiltonian is not Hermitian
FAIL leakage_squared_overlap: CheckFailure: deleted one-particle Hamiltonian is not Hermitian
TOTAL: PASS=5 FAIL=2
```

The second failure is expected because both families independently rebuild the
same exact complex Fock fixture.

### 3. Fixed-number energy and trace comparison

Exact replacement:

```diff
-delta = sp.simplify(trace_sqrt - sum(K[index, index] for index in kept))
+delta = sp.simplify(trace_sqrt)
```

This deliberately drops the post-quench energy subtraction and thereby
confuses a total ground-energy magnitude with the excess.

Terminal excerpt:

```text
FAIL fixed_number_energy_trace: CheckFailure: noncommuting multisite excess mismatch
TOTAL: PASS=6 FAIL=1
```

### 4. Leakage and squared overlap

Exact replacement:

```diff
-fidelity = sp.simplify(sp.conjugate(amplitude) * amplitude)
+fidelity = sp.simplify(abs(amplitude))
```

Terminal excerpt:

```text
FAIL exact_fock_projection: CheckFailure: squared Slater overlap mismatch n=0
FAIL leakage_squared_overlap: CheckFailure: squared Slater overlap mismatch n=0
TOTAL: PASS=5 FAIL=2
```

The first failure is expected because the exact Fock family also enforces the
squared-overlap identity before returning its fixture.

### 5. Singleton resolvent and scalar quadrature

Exact replacement:

```diff
-expected_g = (s + 5) / ((s + 1) * (s + 9))
+expected_g = (s + 4) / ((s + 1) * (s + 9))
```

Terminal excerpt:

```text
FAIL resolvent_scalar_quadrature: CheckFailure: singleton resolvent g sign/denominator mismatch
TOTAL: PASS=6 FAIL=1
```

### 6. Canonical antiperiodic integer grid

Exact replacement:

```diff
-q = 2.0 * math.pi * (np.arange(N, dtype=float) + 0.5) / N
+q = 2.0 * math.pi * (np.arange(N, dtype=float) + 0.0) / N
```

Terminal excerpt:

```text
FAIL canonical_integer_grids: CheckFailure: antiperiodic spectrum mismatch N=2
TOTAL: PASS=6 FAIL=1
```

### 7. Continuum constants and shell bound

Exact replacement:

```diff
-CUBE_DENOMINATOR = 32
+CUBE_DENOMINATOR = 31
```

Terminal excerpt:

```text
FAIL continuum_constants_shells: CheckFailure: cube Green bound mismatch
TOTAL: PASS=6 FAIL=1
```

These are detection tests only. Their mutated SHA values are intentionally not
cache inputs, and none of the scratch copies was staged or committed.
