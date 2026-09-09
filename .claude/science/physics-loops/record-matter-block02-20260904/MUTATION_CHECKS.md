# Block-02 primary runner mutation checks

Date: 2026-09-04
Committed source: `scripts/cubic_repulsive_flux_fixed_half_2026_09_04.py` at `6f3bb0c331cbe3a637939913662b3f3f92deea4b`
Source SHA-256: `46de4dbe218d9e847c5697b866707237741e4155c3b02d408aafe85446ee1dd3`

## Method

Section 6 of `docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` requires one load-bearing scratch mutation per changed check family and requires the affected check to fail. Each probe below copies the committed runner to `/tmp/block02-primary-mutations-20260904-pr-refresh`, applies the recorded exact replacement only to that copy, runs it directly, and requires a nonzero exit plus the named computed `FAIL` row. Repository source and cache files are not edited by these probes.

Six load-bearing mutations were run, including separate reflection and centering probes for the physical cube family.

## 1. Polar inequality and required conjugation

Scratch copy: `polar_missing_conjugation.py`

Exact replacement:

```diff
-    reflected = 0.5 * (trace_energy(left, a, a.conj(), couplings)
-                       + trace_energy(right, b.conj(), b, couplings))
+    reflected = 0.5 * (trace_energy(left, a, a, couplings)
+                       + trace_energy(right, b, b, couplings))
```

Command:

```bash
python3 /tmp/block02-primary-mutations-20260904-pr-refresh/polar_missing_conjugation.py > /tmp/block02-primary-mutations-20260904-pr-refresh/polar_missing_conjugation.out 2>&1; rc=$?; printf 'exit_code=%s\n' "$rc"; rg '^FAIL |^TOTAL:' /tmp/block02-primary-mutations-20260904-pr-refresh/polar_missing_conjugation.out; test "$rc" -ne 0; rg -Fq 'FAIL polar fixed-half q=0 inequality:' /tmp/block02-primary-mutations-20260904-pr-refresh/polar_missing_conjugation.out
```

Computed excerpt:

```text
exit_code=1
FAIL polar fixed-half q=0 inequality: cases=120 min_margin=-0.578489669
FAIL polar q=+-1 algebraic observation: cases=120 min_margin=-0.495323171; no off-half flux claim
TOTAL: PASS=13 FAIL=2
```

## 2. Physical cube reflection

Scratch copy: `cube_reflection_sign.py`

Exact replacement:

```diff
-        reflected_left[np.ix_(right, right)] = -hll
-        reflected_right[np.ix_(left, left)] = -hrr
+        reflected_left[np.ix_(right, right)] = hll
+        reflected_right[np.ix_(left, left)] = hrr
```

Command:

```bash
python3 /tmp/block02-primary-mutations-20260904-pr-refresh/cube_reflection_sign.py > /tmp/block02-primary-mutations-20260904-pr-refresh/cube_reflection_sign.out 2>&1; rc=$?; printf 'exit_code=%s\n' "$rc"; rg '^FAIL |^TOTAL:' /tmp/block02-primary-mutations-20260904-pr-refresh/cube_reflection_sign.out; test "$rc" -ne 0; rg -Fq 'FAIL CAR fixed-half reflection inequality:' /tmp/block02-primary-mutations-20260904-pr-refresh/cube_reflection_sign.out
```

Computed excerpt:

```text
exit_code=1
FAIL CAR fixed-half reflection inequality: cases=48 dim=70 min_margin=-1.0061529
TOTAL: PASS=14 FAIL=1
```

## 3. Physical cube centering

Scratch copy: `cube_centering.py`

Exact replacement:

```diff
-            occupations -= 0.5
+            occupations -= 0.4
```

Command:

```bash
python3 /tmp/block02-primary-mutations-20260904-pr-refresh/cube_centering.py > /tmp/block02-primary-mutations-20260904-pr-refresh/cube_centering.out 2>&1; rc=$?; printf 'exit_code=%s\n' "$rc"; rg '^FAIL |^TOTAL:' /tmp/block02-primary-mutations-20260904-pr-refresh/cube_centering.out; test "$rc" -ne 0; rg -Fq 'FAIL CAR centered/uncentered N=4 shift:' /tmp/block02-primary-mutations-20260904-pr-refresh/cube_centering.out
```

Computed excerpt:

```text
exit_code=1
FAIL CAR centered/uncentered N=4 shift: shift=-3V max_matrix_residual=1.20e+01
FAIL fixed-N versus full-Fock centering: cube shifts N=2:0, N=4:-3 max_res=2.54e+00
TOTAL: PASS=13 FAIL=2
```

## 4. Torus flux, Bloch spectrum, and gap

Scratch copy: `torus_flux.py`

Exact replacement:

```diff
-    value = (1, (-1) ** x, (-1) ** (x + y))[axis]
+    value = (1, 1, (-1) ** (x + y))[axis]
```

Command:

```bash
python3 /tmp/block02-primary-mutations-20260904-pr-refresh/torus_flux.py > /tmp/block02-primary-mutations-20260904-pr-refresh/torus_flux.out 2>&1; rc=$?; printf 'exit_code=%s\n' "$rc"; rg '^FAIL |^TOTAL:' /tmp/block02-primary-mutations-20260904-pr-refresh/torus_flux.out; test "$rc" -ne 0; rg -Fq 'FAIL KS plaquettes and Wilson loops:' /tmp/block02-primary-mutations-20260904-pr-refresh/torus_flux.out
```

Computed excerpt:

```text
exit_code=1
FAIL KS plaquettes and Wilson loops: fields=18 plaquettes=7584 loops=1416 residual=2.000e+00
FAIL KS direct/Bloch spectra: all8twists=4^3,6^3 max_residual=2.000e+00
FAIL canonical finite-volume gap: sizes=4^3,4x4x6,6^3,4x6x8 min_gap=0.870263933 formula_res=1.24e+00
TOTAL: PASS=12 FAIL=3
```

## 5. Reflection geometry closure

Scratch copy: `geometry_closure.py`

Exact replacement:

```diff
-            c[axis] = (1 - c[axis]) % lengths[axis]
+            c[axis] = (2 - c[axis]) % lengths[axis]
```

Command:

```bash
python3 /tmp/block02-primary-mutations-20260904-pr-refresh/geometry_closure.py > /tmp/block02-primary-mutations-20260904-pr-refresh/geometry_closure.out 2>&1; rc=$?; printf 'exit_code=%s\n' "$rc"; rg '^FAIL |^TOTAL:' /tmp/block02-primary-mutations-20260904-pr-refresh/geometry_closure.out; test "$rc" -ne 0; rg -Fq 'FAIL finite reflection/cycle geometry:' /tmp/block02-primary-mutations-20260904-pr-refresh/geometry_closure.out
```

Computed excerpt:

```text
exit_code=1
FAIL finite reflection/cycle geometry: sizes=4 cycles=2028 cut_cycles=1620
TOTAL: PASS=14 FAIL=1
```

## 6. Constructor and theorem-domain guards

Scratch copy: `domain_guard.py`

Exact replacements:

```diff
 def ks_hopping(lengths: tuple[int, int, int], twists: tuple[int, int, int]) -> np.ndarray:
-    validate_domain(lengths, 0.0)
     volume = int(np.prod(lengths))

 def geometry_certificate(lengths: tuple[int, int, int]) -> tuple[bool, int, int]:
-    validate_domain(lengths, 0.0)
     coords = list(itertools.product(*(range(n) for n in lengths)))
```

Command:

```bash
python3 /tmp/block02-primary-mutations-20260904-pr-refresh/domain_guard.py > /tmp/block02-primary-mutations-20260904-pr-refresh/domain_guard.out 2>&1; rc=$?; printf 'exit_code=%s\n' "$rc"; rg '^FAIL |^TOTAL:' /tmp/block02-primary-mutations-20260904-pr-refresh/domain_guard.out; test "$rc" -ne 0; rg -Fq 'FAIL domain guards:' /tmp/block02-primary-mutations-20260904-pr-refresh/domain_guard.out
```

Computed excerpt:

```text
exit_code=1
FAIL domain guards: rejected=1/5 (KS/geometry odd,length2; V<0)
TOTAL: PASS=14 FAIL=1
```

## Result

All six scratch copies exited nonzero, and every named check family emitted a computed `FAIL`. The unmodified committed runner and its staged certified cache were not changed or executed during these mutation probes.


---

# Block 02 independent checker mutation probes

Date: 2026-09-04

## Final-source and cache envelope

- Canonical checker: `scripts/cubic_repulsive_flux_fixed_half_independent_check_2026_09_04.py`
- Final source commit before recertification: `985ea72d28`
- Final source SHA-256: `4773f060f980ac3fe680894637d25f990000479491ba2a7e526610ede2e49c78`
- Declared and executed timeout: 180 seconds
- Canonical cache header: `runner cache v1`; `exit_code: 0`; `elapsed_sec: 0.77`; `status: ok`
- Canonical cache SHA-256: `ffaa1e928fb088ec0726cd2736b85f2892f7889c2b8e12ccddc41f8525f4e172`
- Canonical stdout terminal: `TOTAL: PASS=6 FAIL=0`

The probes below run one disposable external copy per mutation. Each replacement must occur exactly once in the final source. A successful probe requires a nonzero process exit, the named check-family `FAIL` line, and a terminal total with at least one failure. No mutated copy is imported by or written into the repository.

## Planned exact replacements

### M1 — Pauli CAR/centering family

Remove the Jordan--Wigner parity string.

```text
OLD: return [kron_all([Z2 if k < j else LOWER if k == j else I2 for k in range(modes)]) for j in range(modes)]
NEW: return [kron_all([I2 if k < j else LOWER if k == j else I2 for k in range(modes)]) for j in range(modes)]
EXPECTED: FAIL pauli_car_centering
```

### M2 — exact polar/bar family

Drop both reflected complex conjugations in the exact witness.

```text
OLD: reflected = (energy(vec, sy, sy.conjugate()) + energy(vec, (-sy).conjugate(), -sy)) / 2
NEW: reflected = (energy(vec, sy, sy) + energy(vec, -sy, -sy)) / 2
EXPECTED: FAIL exact_polar_mutations
```

### M3 — physical particle--hole/reflection family

Drop the minus sign in the right-half one-body particle--hole map.

```text
OLD: right = local_hamiltonian(-hr.T, coupling, ledges)
NEW: right = local_hamiltonian(hr.T, coupling, ledges)
EXPECTED: FAIL fixed_half_reflection
```

### M4 — centered canonical-cube diagnostic family

Delete the `y` staggering from the `z`-direction hopping sign.

```text
OLD: eta = 1 if axis == 0 else (-1) ** x[0] if axis == 1 else (-1) ** (x[0] + x[1])
NEW: eta = 1 if axis == 0 else (-1) ** x[0] if axis == 1 else (-1) ** x[0]
EXPECTED: FAIL centered_ground_diagnostic
```

### M5 — canonical torus seam/gap family

Force every allowed even length to use a periodic seam.

```text
OLD: return -1 if length % 4 == 0 else 1
NEW: return 1
EXPECTED: FAIL canonical_torus
```

### M6 — domain/import-firewall family

Admit the excluded length-two periodic multigraph.

```text
OLD: if length < 4 or length % 2:
NEW: if length < 2 or length % 2:
EXPECTED: FAIL guards_import_firewall
```

## Results

All six replacements occurred exactly once. Every mutated runner exited with code 1, emitted the intended family `FAIL`, and ended with a nonzero failure total. The temporary directory was removed automatically after execution.

### M1 result

```text
M1 EXIT=1 REPLACEMENT_COUNT=1 PROBE_OK=True
FAIL pauli_car_centering CAR=2.0e+00 centering_N2,4,6=1.8e-15 dimN4=70
TOTAL: PASS=4 FAIL=2
```

The missing parity string is shared infrastructure, so it also trips one downstream family; the required CAR-family failure is explicit.

### M2 result

```text
M2 EXIT=1 REPLACEMENT_COUNT=1 PROBE_OK=True
FAIL exact_polar_mutations local=-8/5 drop_bar_margin=-8/5 polar_margin=2 KT=-1 Kdag=1 q_to_Q0=True
TOTAL: PASS=5 FAIL=1
```

### M3 result

```text
M3 EXIT=1 REPLACEMENT_COUNT=1 PROBE_OK=True
FAIL fixed_half_reflection cases=12 spec=5.7e-01 herm=0.0e+00 N/Q=0.0e+00 polar_Q0=1.2e-15 norm=3.3e-15 margins=(1.486e-01,2.653e-01)
TOTAL: PASS=5 FAIL=1
```

### M4 result

```text
M4 EXIT=1 REPLACEMENT_COUNT=1 PROBE_OK=True
FAIL centered_ground_diagnostic diagnostic_only centered_full_vs_N4=1.3e-14 plaquette=2.0e+00
TOTAL: PASS=5 FAIL=1
```

### M5 result

```text
M5 EXIT=1 REPLACEMENT_COUNT=1 PROBE_OK=True
FAIL canonical_torus bandgaps=(4, 4, 4):0.000000/(1, 1, 1);(4, 4, 6):2.000000/(1, 1, 1);(6, 6, 6):3.464102/(1, 1, 1) formula=2.4e+00 h2=0.0e+00 clifford=0.0e+00 herm=0.0e+00 wrong4_gap=6.1e-17
TOTAL: PASS=5 FAIL=1
```

### M6 result

```text
M6 EXIT=1 REPLACEMENT_COUNT=1 PROBE_OK=True
FAIL guards_import_firewall domain_rejections=2/3 imports=ast,numpy,sympy,time local_imports=0
TOTAL: PASS=5 FAIL=1
```

## Verdict

The final checker is mutation-sensitive in every reported check family. These probes establish checker teeth for the bounded implementations; they do not enlarge the mathematical scope beyond the theorem note's proof-carried hypotheses.
