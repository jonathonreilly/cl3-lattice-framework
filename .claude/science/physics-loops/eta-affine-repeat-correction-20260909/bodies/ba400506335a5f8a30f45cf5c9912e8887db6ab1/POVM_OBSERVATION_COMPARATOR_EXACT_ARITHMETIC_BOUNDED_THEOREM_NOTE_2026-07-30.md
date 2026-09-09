# Exact rational comparison for a supplied six-effect qubit POVM

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_povm_observation_comparator_exact_arithmetic_2026_07_30.py`](../scripts/frontier_povm_observation_comparator_exact_arithmetic_2026_07_30.py)

Independent reconstruction:

- [`frontier_povm_observation_comparator_independent_check_2026_07_30.py`](../scripts/frontier_povm_observation_comparator_independent_check_2026_07_30.py)

Load-bearing sources:

- [`POVM_OBSERVATION_COMPARATOR_INPUT_CONVENTION_META_NOTE_2026-07-30.md`](./POVM_OBSERVATION_COMPARATOR_INPUT_CONVENTION_META_NOTE_2026-07-30.md)
- [`BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md`](./BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md)
- [`MINIMAL_AXIOMS_2026-06-29.md`](./MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This package changes no axiom, primitive,
registry, policy, audit result, or audit status. Its authority is `none`; the
bounded theorem remains unaudited until the independent audit lane evaluates
it.

## Conditional result

Adopt exactly the finite inputs and associations in the convention note. Let

```text
rho = (I + r_x X + r_y Y + r_z Z)/2,
r = (21/100, -32/100, 41/100),
E_(a,s) = (I + s sigma_a)/6.
```

Then `|r|^2=1573/5000<1`, so `rho` is a positive trace-one matrix. Each
`E_(a,s)` has eigenvalues `{0,1/3}`, and summing the positive and negative
effects on all three axes gives `I`. The supplied trace comparator evaluates
exactly to

```text
q_(a,s) = Tr(rho E_(a,s)) = (1 + s r_a)/6.
```

In the order `(x+,x-,y+,y-,z+,z-)`, this is

```text
q = (121, 79, 68, 132, 141, 59)/600.
```

For any positive integer `M` and any exhaustive, mutually exclusive
nonnegative count vector `n` with `sum_i n_i=M`, exact normalization gives
`f_i=n_i/M`, `f_i>=0`, and `sum_i f_i=1`. This is a conditional rational
simplex identity under the supplied exposure convention.

The matching synthetic profile therefore agrees in all six slots. The
counterfactual profile

```text
(120, 80, 68, 132, 141, 59)/600
```

agrees in four slots and disagrees in `x+` and `x-`. Across the two declared
profiles the exact comparator census is ten agreements and two
disagreements.

## Proof-obligation graph

```text
supplied Bloch vector with |r|^2 < 1
  + supplied Pauli-axis six-effect POVM
      -> positive rho, positive effects, sum_i E_i = I
      -> exact q_(a,s) = (1 + s r_a)/6

positive exposure M
  + exhaustive exclusive nonnegative counts with sum_i n_i = M
      -> exact f_i = n_i/M in the rational simplex

exact q and exact f
      -> slotwise equality/disagreement census
```

Every association on the left is an explicit condition. The theorem does not
derive the input convention or claim that it is the unique way to represent a
comparator.

## Independent reconstruction

The primary runner uses the closed-form Pauli trace identity. The independent
checker instead constructs `rho` and all six effects as exact rational complex
`2x2` matrices, multiplies them entry by entry, and takes the trace. It imports
neither the primary runner nor the Cycle-317 module. Only after completing
that reconstruction does it run the primary as a clean black-box subprocess.

The Cycle-317 file is read as text, pinned at SHA-256
`e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10`,
and parsed to confirm the provenance of the supplied Bloch literal and held
trace expression. It is never imported or executed by either runner, so its
transitive apparatus modules and repository-state checks are not runtime
premises of this result.

## Import and support boundary

- The convention note supplies the outcome order, effects, Bloch literal,
  exposure rule, row schema, and both synthetic profiles.
- The linked Born-form theorem is mathematical context for a conditional
  trace-functional surface. This package does not import its audit status as
  proof authority and reproduces the finite matrix identity used here.
- The linked minimal axioms delimit the Record vocabulary. `ObservationRow`
  is not a framework Record, and no Record formation or occurrence
  identification is used.
- Pauli matrices, rational arithmetic, matrix multiplication, positivity of a
  `2x2` Hermitian matrix, and finite counting are zero-input mathematical
  machinery.
- There are no measured, fitted, observational, phenomenological,
  cosmological, or literature-derived numerical inputs.

## Claim boundary

This is a finite conditional algebraic theorem and a synthetic comparator
fixture. It is silent about physical occurrence, Record formation, realized
history, probability-law selection, repeated-process convergence, and
empirical calibration. The supplied trace functional is not promoted to a
selected physical law.

The earlier module-wide receiver census, universal eight-component interface,
and categorical mutation-safety statements are outside this result. This
sentence records removed scope only.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 scripts/frontier_povm_observation_comparator_exact_arithmetic_2026_07_30.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 scripts/frontier_povm_observation_comparator_independent_check_2026_07_30.py
```

The paired runner-cache logs are reproducibility aids only. No claim-status
receipt or self-certificate is part of this package.
