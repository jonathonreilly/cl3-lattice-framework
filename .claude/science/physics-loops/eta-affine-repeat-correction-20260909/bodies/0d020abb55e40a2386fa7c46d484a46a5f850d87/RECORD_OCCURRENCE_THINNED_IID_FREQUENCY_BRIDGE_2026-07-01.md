# Record Occurrence Thinned-IID Frequency Bridge

**Date:** 2026-07-01
**Type:** bounded_theorem — bounded support theorem / finite sparse-record normal form
**Claim-strength label:** bounded support theorem for a supplied occurrence
kernel and supplied IID reset/preparation protocol
**Primary runner:**
[`scripts/record_occurrence_thinned_iid_frequency_bridge_2026_07_01.py`](../scripts/record_occurrence_thinned_iid_frequency_bridge_2026_07_01.py)
**Cached output:**
[`logs/runner-cache/record_occurrence_thinned_iid_frequency_bridge_2026_07_01.txt`](../logs/runner-cache/record_occurrence_thinned_iid_frequency_bridge_2026_07_01.txt)

This is not an audit verdict. It does not run audit workers, edit registries,
change axioms, or add a primitive.

## Claim

Sparse record production is compatible with ordinary finite-frequency algebra
when no-record attempts are represented as an explicit outcome.

Given a finite value set `A`, an activation probability `a`, a conditional
selection law `p(v)` on `A`, and IID reset/preparation for repeated attempts,
the one-attempt outcome set is:

```text
{bot} union A
```

with probabilities:

```text
q(bot) = 1 - a
q(v)   = a p(v),  v in A.
```

For `N` repeated attempts, histories have product weights on
`({bot} union A)^N`. Attempt-level frequencies concentrate around `q`, while
recorded-only frequencies concentrate around `p` after conditioning on the
number of produced records.

The theorem does not derive `a`, `p`, the physical instrument/trigger, IID
reset/preparation, a clock/rate, objectivity, or empirical measurement
semantics. It proves only the finite frequency law once those operational
surfaces are supplied.

## Finite Theorem

Let `A` be finite and let:

```text
K(bot) = 1 - a
K(v)   = a p(v),  v in A,
```

where `0 <= a <= 1`, `p(v) >= 0`, and `sum_v p(v)=1` when `a>0`. For `N`
independent repetitions of the same kernel, a history

```text
w = (w_1, ..., w_N) in ({bot} union A)^N
```

has product weight:

```text
P(w) = product_i K(w_i).
```

Let:

```text
N_bot = #{i : w_i = bot}
N_v   = #{i : w_i = v}
M     = N - N_bot = sum_v N_v.
```

The joint count law is multinomial:

```text
P(N_bot=n_bot, {N_v=n_v})
  = N! / (n_bot! product_v n_v!)
    (1-a)^n_bot product_v (a p(v))^n_v.
```

Therefore the attempt-level frequencies

```text
F_bot = N_bot/N
F_v   = N_v/N
```

satisfy:

```text
E[F_bot] = 1-a,
Var(F_bot) = a(1-a)/N,

E[F_v] = a p(v),
Var(F_v) = a p(v) (1 - a p(v)) / N.
```

The total record count is binomial:

```text
M ~ Binomial(N,a),
E[M/N] = a,
Var(M/N) = a(1-a)/N.
```

Conditional on `M=m>0`, the recorded values are multinomial with probabilities
`p(v)`. The recorded-only frequency

```text
G_v = N_v/M
```

satisfies:

```text
E[G_v | M=m] = p(v),
Var(G_v | M=m) = p(v)(1-p(v))/m.
```

The zero-record case has probability:

```text
P(M=0) = (1-a)^N.
```

So if `a>0`, repeated attempts eventually produce records with probability
approaching one, but no finite attempt count is guaranteed to contain a record.

## Explicit Witness

Take:

```text
A = {0,1},
a = 1/4,
p(0) = 3/5,
p(1) = 2/5.
```

Then:

```text
q(bot) = 3/4,
q(0)   = 3/20,
q(1)   = 1/10.
```

For `N` repeated attempts:

```text
E[F_bot] = 3/4,
E[F_0]   = 3/20,
E[F_1]   = 1/10,
E[M/N]   = 1/4.
```

Among histories with exactly `m>0` records, the recorded-only frequencies
recover the conditional selection law:

```text
E[G_0 | M=m] = 3/5,
E[G_1 | M=m] = 2/5.
```

At `a=1`, the theorem reduces to the ordinary IID frequency law on `A`. At
`a=0`, there are no records and no recorded-only frequency is defined.

## Boundary

This is a finite algebra bridge, not a record-production theorem.

The following remain separate supplied premises or open physical bridges:

- the record-writing instrument or trigger;
- the activation law `a`;
- the conditional selection law `p`;
- IID reset/preparation between repeated attempts;
- clock/rate normalization if attempts per unit time are claimed;
- local objectivity or redundant broadcast if multi-observer records are
  claimed;
- the physical observable/context being sampled.

Rows that count only recorded tokens may use recorded-only frequencies only
after conditioning on `M>0` or otherwise supplying the sampling convention.
Rows that count attempts, including no-record attempts, should use the
attempt-level law over `{bot} union A`.

## Non-Claims

This note does not claim:

- record occurrence is derived from the axioms;
- every trial records;
- every site records;
- every available possibility eventually records;
- finite counts derive probabilities;
- IID reset/preparation is derived;
- activation and selection are independent physical mechanisms;
- a clock, rate, reset cost, pointer coupling, source/action coefficient,
  theta sector, metric, physical observable, or empirical comparator is
  derived;
- measured constants, fitted values, lattice-MC values, beta=6 values, or a
  new primitive are used.

## No-Go Discipline

The result narrows a residual without pretending to close the production
problem. It rules out only one overcorrection: sparse records do not force a
total-record model. The hard physics remains the supplied occurrence kernel and
the supplied IID reset/preparation protocol.

Live paths remain:

- derive a physical instrument/trigger supplying `a` and `p`;
- derive IID reset/preparation from a preparation or instrument theorem;
- derive a local Markov/transfer process whose discrete attempts reduce to the
  thinned kernel;
- state rates or objectivity only after a clock/broadcast bridge is supplied.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/record_occurrence_thinned_iid_frequency_bridge_2026_07_01.py
```

Expected result:

```text
TOTAL: PASS=65 FAIL=0
```
