# Focused independent check: finite-patch Record spectral battery

This is a bounded scientific source check, with one material finding on the
frozen initial source. It is not a formal audit and applies no verdict, grade,
retention status, or ledger change. No repository files were edited.

## Source binding and applicable instructions

Repository: `/Users/jonreilly/Projects/Physics-worktrees/toe-campaign-20260907`.
Frozen main and initial HEAD: `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`.
The two candidate files were untracked, so their byte hashes, rather than HEAD
alone, bind this check:

| Source | SHA256 |
| --- | --- |
| `docs/NATIVE_RECORD_BATTERY_FINITE_PATCH_LOCALITY_NOTE_2026-09-07.md` | `de7ec27441c5690af8f07018ad0bfce598d4f84cf69ee2e918cfcac4d7ebdaed` |
| `scripts/native_record_battery_finite_patch_locality_2026_09_07.py` | `b8c14302200be820a6d14357939bd7a35c19a0602192c80df0669ad8241d4a41` |

I read the checkout's `AGENTS.md` pointer, the cached
`origin/ai/execution:AGENTS.md` at `8eb102f8fe545b458ede8f1a63121d9bfde103a4`,
and `docs/ai_methodology/SCIENCE_WORKFLOW.md`. These agree with the supplied
bounded read-only check and explicitly separate independent checking from
formal audit. I did not invoke a full review/audit skill or pipeline, fetch
moving refs, inspect external literature, or treat procedures as science
premises. The task's explicit restrictions control the output paths and scope.

## Finding F1 — P2: Eq. (6) uses the wrong Heisenberg time orientation

**Locations:** original note lines 112–124, especially Eq. (6), lines 116–118.
The author runner's real spin-chain fixture at lines 368–387 does not expose
this failure.

Equation (5) correctly gives

`C'(tau) = i alpha_{-tau}^{H-h}(h) C(tau)`.

Consequently, for positive `tau`, variation of constants supplies

`||C(tau)-C_P(tau)|| <= integral_0^tau a_P(-s) ds`,

with `a_P` as originally defined. The displayed source instead integrates
`a_P(+s)`. Those functions need not agree for the allowed complex Hermitian
Hamiltonians. The remark about replacing Hamiltonians by their negatives does
not make the displayed positive-time inequality true for the original fixed
Hamiltonians.

A simple admissible counterexample already has a nontrivial Record and a
proper radius-one buffer. Take a three-site chain `0–1–2`, `X={0}`, `P={0,1}`,
`r=R=1`, and Pauli operators

```text
h = X_0
A = H'_P = -Z_0 X_1 + 2 Y_1 - Z_0 Z_1
B = H_ext = 3 Z_1 X_2
H = A+B+h
Q_z = (I+z Z_0)/2.
```

All remaining named terms commute separately with both `Q_z`, the supports
have range at most one, and `[B,h]=0`. At `tau=0.4`:

| Quantity | Value |
| --- | ---: |
| Actual `||C-C_P||` | `0.1377215580103315` |
| Original Eq. (6) right side, `integral a_P(+s) ds` | `0.0561256439169221` |
| Correct `integral a_P(-s) ds` | `0.1379557284830106` |
| Correct symmetric integral, `integral max(a_P(s),a_P(-s)) ds` | `0.1379557284830106` |

The violation is not a quadrature-edge artifact. A single matrix-column norm
already lower-bounds the left side by `0.1349023403281219`. A 1024-cell
midpoint calculation bounds the positive-time integral above by
`0.0567427527023114`, using the analytic Lipschitz remainder
`(4 sqrt(6)+6) T^2/(4*1024)`. Matrix arithmetic remains ordinary double
precision; this is not an interval-certified matrix computation. The gap is
about `0.078`, far larger than floating-point errors here.

**Minimal correction:** for nonnegative `s`, define

```text
a_P(s) = max_{sigma=+/-1}
         ||alpha_{sigma s}^{H-h}(h)-alpha_{sigma s}^{H'_P}(h)||,

a_P(s) <= integral_0^s sum_cross max_{sigma=+/-1}
          ||[h_f,alpha_{sigma u}^{H'_P}(h)]|| du.
```

The latter follows from `max_sigma integral <= integral max_sigma`, and the
same symmetric LR bound controls both signs without adding a factor of two.
Thus the stated elementary bounds, `F1/F2` constants, cutoff estimates,
channel estimates, and resource rates survive this correction. Add this
complex-Pauli fixture to the author controls so the original sign mistake
cannot silently recur. Root's proposed correction in the session matches
these formulas. This initial report does not yet confirm changed source bytes.

Reproducer: [time_orientation_counterexample.py](time_orientation_counterexample.py).
Actual results: [time-orientation-counterexample.json](time-orientation-counterexample.json).

## Other checked obligations

No other material issue was found within the dispatched scope.

1. **Full-energy defect and domain, original lines 129–139.** Expanding
   `(H'+E_B) W C_P - W C_P(H+E_B)`, with `E_B=-i d/dtau`, gives
   `W(H'C_P-C_PH-iC'_P)=W[H_ext,C_P]`. The sign is correct. Fourier
   multiplication by `C_P` preserves `H1` because it is continuously
   differentiable and both it and its derivative are uniformly bounded;
   specifically `||C'_P||<=delta`. Boundedness alone would not justify the
   general domain assertion, but the needed derivative bound is established
   here. A finite product with the allowed dwells has the same domain property.

2. **Duhamel/LR integrations and constants, original lines 124–206.** For
   `A=H'_P`, `B=H_ext`, differentiating
   `alpha_{s-u}^{A+B}(alpha_u^A(h))` gives the single commutator integral.
   Independently, differentiating `C_P^* B C_P` gives one such integral for
   the energy defect; varying the cocycle generator gives a second integral
   for channel localization. Hence `F1=integral_0^u (exp(lambda v)-1)dv`
   and `F2=integral_0^u (u-v)(exp(lambda v)-1)dv`, exactly the displayed
   expressions. The time-sign repair above is necessary in the intermediate
   formula, but these uniform symmetric bounds and constants are unaffected.
   The interaction-chain sum is bounded by `|X| kappa^k exp(-mu d)`:
   the `|S|` activity factor pays for successive intersection choices. No
   exponential-weight convolution assumption is needed.

3. **Cubic boundary, original lines 185–221.** Every crossing support has an
   inside site `x` with `d(x,X)>r-R`; choosing a nearest point of `X` places
   it in one of `|X|` translated integer annuli. Overcounting both sites and
   indexed interactions is harmless. Summing incidence norms gives the stated
   `g|X|[V3(r)-V3(r-R)]`. Clipping the volume only removes possible sites.
   An independent enumeration used clipped volumes, non-singleton `X`,
   repeated two-site supports, and three-site interactions.

4. **Fourier tail and cutoff, original lines 225–249 and 352–369.** Deriving
   the sine transform as a difference of two sinc terms reproduces the
   rational density including its two removable values. The normalization,
   `tau^2` moment, and tail constant `128pi/(27 w^3 T^3)` are consistent.
   No fourth or exponential moment is needed. With
   `lambda(T+D)=mu(r-R)/2`, the short-time errors are
   `O(r^2 exp(-mu r/2))`; the joint tail is `O(w^-3/2 r^-3/2)` and the
   boundary-weighted energy tail is `O(w^-3 r^-1)`. These are the claimed
   rates for fixed finite event count and duration.

5. **Shared battery, dwell shifts, correlations, original lines 275–350.**
   In energy space a retained wavefunction can be written
   `exp(-i D E) sum_s v_s beta(E-s)`. Applying a spectral shift `u`
   changes a coefficient by `exp(i D u)` and its shift to `s+u`.
   This independent recursion gives precisely the cumulative Fourier
   arguments `tau+s_j` after removing the final common translation.
   At each such fiber the full history operator is an isometry, so the
   unconditioned norm measure is still the single original `p_w`; it is
   not a product of reduced channels. Product telescoping bounds the
   joint isometry difference, and telescoping the energy-intertwining
   identities bounds the unconditional mean without taking the norm of an
   extensive Hamiltonian. An arbitrary untouched reference does not alter
   these operator estimates. The stated exclusion of normalized rare-history
   guarantees is necessary and present.

6. **Caps and global comparator, original lines 251–271.** Successive local
   spectral shifts sum within the declared local allowance; both dwells
   preserve energy-coordinate support. A finite interval cap does not turn
   the continuum battery into a finite-dimensional apparatus. The distinction
   from global spectral support is real: for `H=X_0+X_1+4 Z_0 Z_1`,
   `h=X_0`, `P={0}`, and `Q_z=(I+zZ_0)/2`, a sufficient local offset is
   one. The global lift has a nonzero shift `-8.59524158061724`, with
   transition norm `0.0771572093456713`; the same input can reach negative
   comparison-battery energies. The note correctly does not assert that
   the local allowance makes this comparator positive.

7. **Physical tensor BKSF placement, original lines 373–417.** Endpoint-star
   supports at the doubled midpoints have at most 11 edge factors, midpoint
   radius two, diameter four, and incidence at most 11. A direct geometric
   enumeration on a `4x4x4` vertex cube attains all these maxima, without
   importing a CAR map. The algebraic explanations of termwise `Z_e`
   commutation and number conservation are correct: only the named edge
   flips, and `(B_i-B_j)(B_i+B_j)=0`. Cycle-code projection statements remain
   conditional on the supplied BKSF representation. Localizing sums of the
   same terms preserves the number and surviving Record/cycle relations.
   The note explicitly does not infer physical locality of the shared battery,
   a transport law, or an autonomous nearest-neighbor implementation.

## Independent execution and limits

[independent_controls.py](independent_controls.py) imports no candidate code.
Its principal control uses a different four-qubit Hamiltonian with unequal
couplings and an initial matter/reference state with Schmidt values
`0.8218879263, 0.5696492225`. It propagates the retained battery by its actual
energy-coordinate spectral translations, directly integrates the final joint
wavefunction, and separately reconstructs fibers for controlled, mixed, and
all-free dwells.

- Energy-coordinate and fiber amplitudes agree within `3.08e-15`.
- Omitting the free shifts gives errors `0.1602044` and `0.2627051` in the
  mixed and all-free cases.
- Total probabilities agree with one within `1.4e-15`.
- Direct full matter-plus-battery energy drifts are
  `-0.0014768673`, `0.0136340886`, and `0.0193288280`, each inside the
  applicable theorem bounds.
- Independent centered differentiation checks the defect identity within
  `2.04e-10`; direct commutator integration checks both Duhamel orders.
- Final independent control summary: `TOTAL: PASS=7 FAIL=0`. This does not
  override F1: the time-asymmetric counterexample is a separate later control.
- The original author runner was additionally reproduced unchanged:
  `TOTAL: PASS=19 FAIL=0`.

Exact principal commands, all outputs inside this directory:

```sh
python3 /Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/matter-independent-check/independent_controls.py
python3 /Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/matter-independent-check/time_orientation_counterexample.py
python3 /Users/jonreilly/Projects/Physics-worktrees/toe-campaign-20260907/scripts/native_record_battery_finite_patch_locality_2026_09_07.py --json-output /Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/matter-independent-check/author-reproduction.json
```

The actual runs redirected stdout/stderr to the corresponding `*-stdout.txt`
files. Environment: Python 3.13.5, NumPy 2.4.4, SciPy 1.17.1. BLAS/OpenMP
thread counts were set to one. The calculations used at most 16-dimensional
matter matrices for independent dynamical controls, 128-dimensional matrices
in the separately reproduced author runner, and sparse geometric enumeration
for the cubic support check. No large simulation or full repository pipeline
was run. Quadrature estimates are diagnostic, not interval certificates.

Two scratch-only failures are preserved rather than hidden. The first native
geometry control incorrectly demanded saturation of the bound 11 on a
`3x3x3` vertex cube, which has only one degree-six interior vertex and attains
10; changing the fixture to `4x4x4` supplies adjacent interior vertices. The
original script/results/stdout are saved with `.first-run` suffixes. The first
counterexample serialization encountered a NumPy boolean JSON error; its
trace is saved in `time-orientation-counterexample-first-run-error.txt`, and
an explicit `bool` conversion fixed only that scratch-output error.

Initial conclusion: repair F1 and check the changed bytes before substantial
reuse. The other scoped implications survive the independent attacks above.
No formal scientific status is assigned.
