# Actual final-source mutation checks

The following reports record 27 isolated corrupted scratch runs. These are sensitivity evidence, not theorem proofs or effective audits.

# Block 04 primary scratch mutations

Canonical source was left unchanged. Every mutation was made in a separate `/tmp` copy after the final source commit and cache run.

- Canonical source: `/Users/jonreilly/Projects/Physics-worktrees/record-matter-block04-primary-20260905/scripts/repeated_record_matter_energy_apparatus_2026_09_05.py`
- Commit: `28d7c34df055e594b833b2ab18be604427205437`
- Canonical SHA-256: `a4da79a46cf490e67b50d5ccddb0a4c72493437d185516d91dc1795fb8fd5c0d`
- Execution environment for every case: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1`
- Interpreter: `/opt/homebrew/opt/python@3.13/bin/python3.13`
- Acceptance condition: the original string occurs exactly once, the corrupted copy exits nonzero, and stdout contains the named `FAIL` family plus `TOTAL`.

## M1: deterministic p=0 branch mislabeled as occupied

Expected family: `G0`. Exact-source match count: `1`.

Replaced:

```python
return probability_one, [(0, 1.0, deterministic)]
```

with:

```python
return probability_one, [(1, 1.0, deterministic)]
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m1.py`

Exit code: `1`. Output excerpt:

```text
FAIL G0 deterministic p=0/1 branches omit null outcomes: outcome_mask=2 count=1 no_zero_division=yes
TOTAL: PASS=14 FAIL=2
```

## M2: uniform deletion energy factor uses one incident-star copy

Expected family: `G1`. Exact-source match count: `1`.

Replaced:

```python
exact_target = (1.0 - 2.0 / live_count) * current_energy
```

with:

```python
exact_target = (1.0 - 1.0 / live_count) * current_energy
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m2.py`

Exit code: `1`. Output excerpt:

```text
FAIL G1 complex repeated Gaussian branches and uniform-live means: live=5 max_res=5.943e-02 max_branch_selection=0.457561
TOTAL: PASS=14 FAIL=2
```

## M3: remove the x-dependent eta2 sign from the cubic carrier

Expected family: `G2`. Exact-source match count: `1`.

Replaced:

```python
return -1.0 if x % 2 else 1.0
```

with:

```python
return 1.0
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m3.py`

Exit code: `1`. Output excerpt:

```text
FAIL G2 L6 pi-flux carrier and filled sea: sites=216 particles=108 gap=1.000000000 geometry=2.000e+00 projector=6.661e-16
TOTAL: PASS=15 FAIL=1
```

## M4: replace Hamiltonian phase evolution by an energy-basis permutation

Expected family: `G3`. Exact-source match count: `1`.

Replaced:

```python
in_energy_basis = phases[:, None] * in_energy_basis * phases.conj()[None, :]
```

with:

```python
in_energy_basis = np.roll(np.roll(in_energy_basis, 1, axis=0), 1, axis=1)
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m4.py`

Exit code: `1`. Output excerpt:

```text
FAIL G3 repeated ideal Gaussian occupation/deletion events tau=0.5: events=432 invariant_max=1.990e-13 identity_max=5.201e+00 min_excess=5.432e-02 p1_range=[0.3835,0.7085]
TOTAL: PASS=15 FAIL=1
```

## M5: reverse the battery translation in the finite CP apparatus

Expected family: `G4`. Exact-source match count: `1`.

Replaced:

```python
for q_in in range(battery_levels):
            q_out = q_in + shift
            if 0 <= q_out < battery_levels:
```

with:

```python
for q_in in range(battery_levels):
            q_out = q_in - shift
            if 0 <= q_out < battery_levels:
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m5.py`

Exit code: `1`. Output excerpt:

```text
FAIL G4 four-mode N=2 finite apparatus energy and CP completion: max_res=2.000e+00 refusal=-0.000000 kappa=1.000000 C=1.000000 bound=4.000000
TOTAL: PASS=15 FAIL=1
```

## M6: coherently combine success and refusal instead of recording status

Expected family: `G4`. Exact-source match count: `1`.

Replaced:

```python
status_kraus.extend([success_embed, refusal_embed])
```

with:

```python
status_kraus.append(success_embed + refusal_embed)
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m6.py`

Exit code: `1`. Output excerpt:

```text
FAIL G4 four-mode N=2 finite apparatus energy and CP completion: max_res=8.839e-02 refusal=0.250000 kappa=1.000000 C=1.000000 bound=4.000000
FAIL G4 explicit status readout removes success-refusal coherence: coherent_vs_read=0.000000 read_cross=8.839e-02 normalized_choi_distance=0.349349 (not_diamond_bound)
TOTAL: PASS=14 FAIL=2
```

## M7: omit the intermediate matter dwell from the total ideal history

Expected family: `G5`. Exact-source match count: `1`.

Replaced:

```python
w_total = w2_history @ unitary_mid @ w1
```

with:

```python
w_total = w2_history @ w1
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m7.py`

Exit code: `1`. Output excerpt:

```text
FAIL G5 two events reuse one correlated battery and telescope to total lift: max_res=1.612e-01 Schmidt_rank=3 support_margin=22 declared_margin=24 levels=57
TOTAL: PASS=15 FAIL=1
```

## M8: use epsilon instead of sqrt(epsilon) in the shared width

Expected family: `G6`. Exact-source match count: `1`.

Replaced:

```python
shared_width = 2.0 * np.pi * system_bound / np.sqrt(epsilon)
```

with:

```python
shared_width = 2.0 * np.pi * system_bound / epsilon
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m8.py`

Exit code: `1`. Output excerpt:

```text
FAIL G6 sine, margins, and fresh/shared error-budget arithmetic probes: max_res=1.825e+04 overlap=0.159154943 fresh=(err=0.080,ref=0.040) shared=(err=0.006,meanE=26742.900)
TOTAL: PASS=15 FAIL=1
```

## M9: replace uniform live-site selection by increasing site weights

Expected family: `G1`. Exact-source match count: `1`.

Replaced:

```python
uniform_weights = np.ones(live_count, dtype=float)
```

with:

```python
uniform_weights = np.arange(1.0, live_count + 1.0, dtype=float)
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m9.py`

Exit code: `1`. Output excerpt:

```text
FAIL G1 phase-rotated uniform-live E, N, and H^2 laws after previous Records: phases=3 live=5 prior_records=2 max_res=8.313e-02 H2_res=8.313e-02 star_square_bound=1.046806
TOTAL: PASS=15 FAIL=1
```

## M10: replace the local deleted-star in the H-squared identity by a sum

Expected family: `G1`. Exact-source match count: `1`.

Replaced:

```python
star = hamiltonian - post_hamiltonian
```

with:

```python
star = hamiltonian + post_hamiltonian
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m10.py`

Exit code: `1`. Output excerpt:

```text
FAIL G1 phase-rotated uniform-live E, N, and H^2 laws after previous Records: phases=3 live=5 prior_records=2 max_res=2.817e+00 H2_res=2.817e+00 star_square_bound=11.617209
TOTAL: PASS=15 FAIL=1
```

## M11: omit the occupied-branch conditioning rank update

Expected family: `G1`. Exact-source match count: `1`.

Replaced:

```python
outcome_one[np.ix_(keep, keep)] = block - np.outer(column, column.conj()) / probability_one
```

with:

```python
outcome_one[np.ix_(keep, keep)] = block
```

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /opt/homebrew/opt/python@3.13/bin/python3.13 /tmp/block04_primary_m11.py`

Exit code: `1`. Output excerpt:

```text
FAIL G1 complex repeated Gaussian branches and uniform-live means: live=5 max_res=6.742e-01 max_branch_selection=0.297461
FAIL G1 phase-rotated uniform-live E, N, and H^2 laws after previous Records: phases=3 live=5 prior_records=2 max_res=1.995e-01 H2_res=1.216e-02 star_square_bound=1.046806
TOTAL: PASS=11 FAIL=5
```

## Result

All eleven corrupted scratch copies exited `1` and emitted the appropriate `FAIL` family. They cover deterministic Gaussian branches, the exact uniform energy factor, cubic sign geometry, nontrivial dwell phases, finite battery energy translation, explicit status dephasing, same-battery history composition, shared resource arithmetic, uniform scheduler weights, the energy second-moment star term, and the occupied-branch conditioning rank update. M11 makes both G1 gates fail after the post-live particle expectation is read directly from the corrupted conditioned covariance.

These are sensitivity checks on the finite primary runner. They do not establish the theorem or validate an independent checker.


# Block 04 independent checker mutation evidence

Date: 2026-09-05

Final source-only commit tested: `cc3a11925e5e794a7532e48215ab489e2318fb15`

All mutations were made one at a time in separate directories under
`/tmp/block04-independent-mutations-v4`. The committed checker in the worktree
was never changed. Each replacement matched the stated source occurrence,
every mutated run exited with status 1, and every run retained a final `TOTAL`
line.

## Conditional-event sign

```text
predicted_jump = -star_mean + covariance / probability
predicted_jump = star_mean + covariance / probability
```

```text
FAIL fixed_number_process: CheckFailure: signed branch jump failed n=0
TOTAL: PASS=7 FAIL=1
```

## Uniform live-site weighting

```text
contribution = pinching(evolved, projectors[site]) / live_count
contribution = pinching(evolved, projectors[site]) / 4
```

```text
FAIL uniform_clock_laws: CheckFailure: uniform event blocks lost probability
TOTAL: PASS=7 FAIL=1
```

## Independent-clock exponent

```text
expected_energy = initial_energy * math.exp(-2.0 * gamma * final_time)
expected_energy = initial_energy * math.exp(-1.0 * gamma * final_time)
```

```text
FAIL uniform_clock_laws: CheckFailure: constant-clock exponential energy law failed
TOTAL: PASS=7 FAIL=1
```

## Hypergeometric live count

```text
== remaining_particles
== remaining_particles + 1
```

```text
FAIL uniform_clock_laws: CheckFailure: live-number hypergeometric law failed k=0 r=1
TOTAL: PASS=7 FAIL=1
```

## Complex adjoint

```text
star[other, site] = np.conjugate(one_particle[site, other])
star[other, site] = one_particle[site, other]
```

```text
FAIL fixed_number_process: CheckFailure: Hermitian expectation acquired an imaginary part
FAIL uniform_fibre_identities: CheckFailure: live incident stars do not sum to twice H_R; residual=6.9282
FAIL local_defects: CheckFailure: local defect sign D=-WV failed; residual=4
TOTAL: PASS=5 FAIL=3
```

## Omitted live vertex in fibre average

The first of the two source occurrences was changed:

```text
for selected_site in live_sites:
for selected_site in live_sites[:-1]:
```

```text
FAIL uniform_fibre_identities: CheckFailure: uniform fibre energy identity failed R=0000 tau=0.137
TOTAL: PASS=7 FAIL=1
```

## Second-moment correction sign

```text
+ second_correction
- second_correction
```

```text
FAIL uniform_fibre_identities: CheckFailure: uniform fibre second-moment identity failed R=0000 tau=0.137
TOTAL: PASS=7 FAIL=1
```

This distinguishes the `V_i^2` correction from the first-moment identity.

## Local-defect sign

```text
require_small(defect + W @ V, "local defect sign D=-WV failed")
require_small(defect - W @ V, "local defect sign D=-WV failed")
```

```text
FAIL local_defects: CheckFailure: local defect sign D=-WV failed; residual=9.79796
TOTAL: PASS=7 FAIL=1
```

## Battery translation direction

```text
shift_amount = frequency
shift_amount = -frequency
```

```text
FAIL shared_battery_two_events: CheckFailure: swap extension does not conserve energy; residual=27.7128
TOTAL: PASS=7 FAIL=1
```

## Shared-battery correlation retention

```text
second_input = intermediate
second_input = np.kron(np.ones(12, dtype=complex) / math.sqrt(12.0), packet)
```

```text
FAIL shared_battery_two_events: CheckFailure: shared correlated battery composition failed; residual=1.22228
TOTAL: PASS=7 FAIL=1
```

## Direct battery-energy sign

```text
battery_hamiltonian = data["spacing"] * np.diag(np.arange(length, dtype=float))
battery_hamiltonian = -data["spacing"] * np.diag(np.arange(length, dtype=float))
```

```text
FAIL shared_battery_two_events: CheckFailure: direct matter plus battery ledger does not equal total energy
TOTAL: PASS=7 FAIL=1
```

## Old Record retention

```text
W2 = np.kron(np.eye(2), W_site2)
W2 = np.kron(np.array([[0, 1], [1, 0]], dtype=complex), W_site2)
```

```text
FAIL shared_battery_two_events: CheckFailure: second lift changes the old Record; residual=12.1655
TOTAL: PASS=7 FAIL=1
```

## Stationary-history battery reset

```text
actual_final_joint = S2 @ actual_first_joint
actual_final_joint = S2 @ np.kron(ideal_first_state, packet)
```

```text
FAIL stationary_input_statistics: CheckFailure: ground stationary history did not reuse the correlated battery; residual=0.765367
TOTAL: PASS=7 FAIL=1
```

This discards the correlated first-event output and supplies a fresh product
battery before the second event. It is caught by the sequential-versus-direct
shared-history comparison.

## Status dephasing

```text
dephased_physical = status_dephase(physical_reduced)
dephased_physical = physical_reduced
```

```text
FAIL status_readout_correction: CheckFailure: status-readout cap distance is not p
TOTAL: PASS=7 FAIL=1
```

## Dense-resource cap

```text
DENSE_MATRIX_LIMIT = 600
DENSE_MATRIX_LIMIT = 200
```

```text
FAIL shared_battery_two_events: CheckFailure: dense matrix exceeds 200: (312, 312)
TOTAL: PASS=7 FAIL=1
```

## Import firewall

```text
import ast
import ast
import json
```

```text
FAIL source_contract: CheckFailure: forbidden import roots: ['json']
TOTAL: PASS=7 FAIL=1
```

These finite sensitivity probes do not prove the continuous battery bound, the
general variance recursion, or the stationary-input corollary beyond the tested
fixture.
