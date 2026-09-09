# Read/Reset Cadence and the Interference Channel — Bounded Theorem

**Date:** 2026-07-17

**Claim type:** bounded_theorem

**Status:** bounded claim candidate; audit unset

**Claim scope:** For a supplied finite-dimensional unitary, declared rank-one
instrument, squared-modulus transition weights, and read/reset schedule, this
note proves the exact cadence-defect identity and its all-time monomial closure
criterion. It does not derive an instrument, Record, occurrence rule, clock,
mass law, or axiom content.

**Primary runner:**
[`scripts/read_reset_cadence_interference_channel_bounded_2026_07_18.py`](../scripts/read_reset_cadence_interference_channel_bounded_2026_07_18.py)

## Imported surface

Let `U` be a supplied unitary and let `{R_a}` be a declared complete rank-one
projector family. Supply the dephasing map

```text
D_B(X) = sum_a R_a X R_a
```

and the frame weights

```text
K_t[a,b] = |<a|U^t|b>|^2.
```

Interpreting `K_t` as a transition kernel additionally supplies selective
read/reset semantics: after an outcome, the system is represented by that
rank-one state before the next interval. None of this structure is derived
from Record or Admissibility.

## Exact cadence-defect identity

Suppose the `n`-update interval acts first and the `m`-update interval acts
second. On inputs diagonal in the declared frame, the difference between one
read after `m+n` updates and a read/reset after each interval is

```text
Delta_mn = K_(m+n) - K_m K_n.
```

It is the diagonal representation of the channel

```text
D_B Ad_(U^m) (I-D_B) Ad_(U^n) D_B.
```

Entry by entry, `Delta_mn` is exactly the sum of the interference cross terms
between distinct intermediate frame paths. Every `K_t` is entrywise
nonnegative and doubly stochastic; every `Delta_mn` has zero row and column
sum. The runner verifies the matrix/cross-term identity independently on the
seeded Haar unitary whose induced `K_2` and `K_3` kernels do not commute,
fixing the interval order, and checks the all-time closure criterion on
monomial and finite-order nonmonomial controls.

## All-time closure criterion

For every positive `m,n`,

```text
K_(m+n) = K_m K_n
```

if and only if `U` is monomial in the declared frame: a permutation matrix
with arbitrary phases.

The forward implication for a monomial unitary is immediate. Conversely,
all-time closure gives `K_t=K_1^t`. Finite-dimensional unitary recurrence has
a subsequence `U^(t_j)` converging to the identity, hence `K_1^(t_j)` converges
to the identity. Therefore `|det K_1|=1`. The Hadamard determinant bound and
the unit column sums of the doubly stochastic `K_1` can saturate only when
each column has one unit entry. Doubly stochasticity then makes `K_1` a
permutation, and `U` is monomial.

Closure for one fixed interval pair can occur by cancellation and does not
satisfy this criterion.

The cadence-defect identity is an elementary channel expansion. The all-time
monomial closure criterion is proved here from finite-unitary recurrence and
the Hadamard bound, but no claim of literature novelty is made for either
statement.

## Boundaries

- The unitary, frame, squared-modulus rule, reset/repreparation, and schedule
  are supplied.
- A nonselective ensemble dephasing is not a selected realized trajectory.
- The result derives no Record formation, permanence under all lawful
  continuations, Born frequency, event trigger, rate, or clock normalization.
- It makes no mass-spectrum, gravity, measurement-solution, TOE, or no-go
  claim.
- It has no constitutional effect and supports no axiom conclusion.

## No-Go Discipline Gate

**Status: `FAIL / DO NOT SHIP` for any negative inference from the scoped
artifact.** The cadence-defect identity and all-time monomial criterion under
the declared imports remain positive bounded results. The candidate negative
tested was:

> The objects constructed in this note and its paired runner do not by
> themselves define a physical Record, occurrence rule, probability law, or
> clock.

The sentence is an import inventory for the displayed construction, not a
claim that those bridges are impossible in the framework. Because the route
outcomes below are current tests without per-route retained authority, it is
not shipped as a no-go.

### N1 -- alternative routes

| attempted route | marker | result against the scoped boundary |
|---|---|---|
| identify the integer exponent of `U` with duration | `ATTEMPTED` | the exponent orders supplied updates but carries no duration unit or calibration |
| identify the unistochastic kernel with a probability law | `ATTEMPTED` | squared-modulus weights and selective reset semantics are declared inputs; occurrence and frequency are absent |
| identify dephasing with Record formation | `ATTEMPTED` | the channel deletes coherences but locks no site/content pair, selects no outcome, and proves no permanence |
| identify kernel-semigroup closure with a physical clock | `ATTEMPTED` | the monomial criterion concerns composition in update count only and supplies no trigger, rate, or metric |
| identify the cadence defect with force, mass, or energy | `ATTEMPTED` | the defect depends on a supplied unitary and frame and contains no source-response or resource bridge |
| absorb the frame into notation | `ATTEMPTED` | passive relabeling preserves the construction, while changing the physical read frame changes the instrument being declared |

The [minimal framework axioms](MINIMAL_AXIOMS_2026-06-29.md) supply neither
the missing instrument semantics nor a time metric. The paired runner tests
the finite algebraic identities and does not assert those bridges.

All six route outcomes are current source analysis. None has a per-route
retained-authority citation closing the physical alternatives. **N1 therefore
fails**, and the negative disposition is `partial-narrowing`; only the exact
finite identity and monomial criterion are submitted for independent audit.

### N2 -- wall independence

For a physical read/reset interpretation, the imports collapse to three
independent groups.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| supplied unitary/frame / selective reset semantics | no | no | yes |
| supplied unitary/frame / schedule-to-clock bridge | no | no | yes |
| selective reset semantics / schedule-to-clock bridge | no | no | yes |

Only the first two groups enter the bounded algebraic theorem. The third is
named solely to prevent update count from being overread as physical time.

### N3 -- hidden-wall scan

Every use of `supplied` or `declared` refers to the unitary, rank-one frame,
squared-modulus weights, dephasing map, or reset semantics listed under
Imported surface. No phrase such as “the framework provides,” “naturally,” or
“standard QFT” carries an additional premise. The proof uses only finite
unitary recurrence, determinant multiplicativity, and the Hadamard bound.

### N4 -- residual matching

| cited witness (exact path and line) | residual there | residual used here | match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:65,105-113,164-168` | Record supplies no update law, probability rule, or time metric | the construction does not inherit those objects from Record | yes; approved source boundary only |
| `scripts/read_reset_cadence_interference_channel_bounded_2026_07_18.py:100-181` | finite channel/kernel identities, order control, and monomial/nonmonomial checks | exact positive theorem scope | yes; current unaudited compute, so it cannot make N1 pass |

No prior no-go, historical application, or campaign is used as supporting
authority for the canonical claim.

### N5 -- rhetoric and resolution audit

The exact identity is matrix-wide for finite dimension and all positive
interval pairs. The runner checks a five-dimensional generic control and a
four-dimensional monomial control. It does not classify lattice-wide
instruments, physical histories, field modes, or continuum clocks. Every
negative sentence is therefore restricted to the objects actually displayed.

### N6 -- partial-closure paths

A retained instrument theorem could derive the rank-one read/reset semantics;
a retained occurrence/Record bridge could type selected outcomes; and an
independent clock theorem could calibrate lawful update order to duration.
Each would retire a named import without changing the algebraic identity. The
registered scale-reference, kinetic-isotropy, and realized-state primitives do
not supply these bridges.

### N7 -- strongest steelman

A future local law could derive the instrument, make read/reset events into
Records, and calibrate its update order against the independently derived time
lane. Then the same cadence defect could become a physical observable rather
than a declared-frame diagnostic. That live route defeats any broad no-go and
is why this note claims only the finite conditional theorem.

### N8 -- cross-cycle echo

The repository echo search covered `cadence`, `dephasing`, `Record`,
`unistochastic`, `update count`, `time metric`, `Born`, `no retained
primitive`, and `requires new axiom`.

| prior surface | similar wall | retired mechanism/status | application here |
|---|---|---|---|
| `docs/READ_TWICE_PACKET_DERIVE_FIRST_UNIFICATION_BOUNDED_NOTE_2026-07-13.md` | finite copying and Hilbert pairing were overread as Record, probability, or time | current bounded candidate; negative gate failed and physical bridges remain open | no pointer-copy or weight result is imported as a cadence law |
| `docs/ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md` | an availability menu was overread as successor dynamics | current bounded candidate; finite append witness does not select the physical rule | the declared read/reset schedule remains an import |
| `docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md` | update order was overread as rate or metric duration | order/axis separated from calibration; unaudited | integer exponents are not called physical time |
| `docs/READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md` | finite additivity was overread as a probability representation | FRAME-EXT remains conditional and unaudited | squared-modulus/reset semantics stay declared imports |

No listed wall has a retained retirement mechanism omitted here. A naming
change cannot supply an instrument, occurrence, or clock calibration, so the
negative gate remains `FAIL`.

## Primary comparisons

The instrument, unistochastic-kernel, process-history, and decoherent-walk
background is prior work; see Davies and Lewis,
<https://doi.org/10.1007/BF01647093>; Ozawa,
<https://doi.org/10.1063/1.526000>; Życzkowski, Kuś, Słomczyński, and Sommers,
<https://doi.org/10.1088/0305-4470/36/12/333>; Benoist, Cuneo, Jakšić, and
Pillet, whose rank-one von Neumann instruments give unistochastic Markov
outcome measures, <https://doi.org/10.1007/s10955-021-02725-1>; Pollock et al.
for the process-tensor framework and its operational Markov condition,
<https://doi.org/10.1103/PhysRevA.97.012127> and
<https://doi.org/10.1103/PhysRevLett.120.040405>; Kendon and Tregenna for
decohered walks, <https://doi.org/10.1103/PhysRevA.67.042315>; and
Chandrashekar for periodically measured quantum walks,
<https://doi.org/10.1103/PhysRevA.82.052108>.

## Reproduction

```bash
python3 scripts/read_reset_cadence_interference_channel_bounded_2026_07_18.py
```

Expected summary:

```text
TOTAL PASS=10 FAIL=0
```
