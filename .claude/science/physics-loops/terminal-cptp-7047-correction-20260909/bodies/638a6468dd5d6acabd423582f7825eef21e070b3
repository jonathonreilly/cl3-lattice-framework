# Record Markov-Generator Embeddability Boundary

**Date:** 2026-06-06
**Claim type:** no-go / exact-support boundary
**Status:** branch-local source note awaiting independent audit handling.
**Primary runner:**
[`scripts/frontier_record_markov_generator_embeddability_boundary_2026_06_06.py`](../scripts/frontier_record_markov_generator_embeddability_boundary_2026_06_06.py)
with cached output
[`logs/runner-cache/frontier_record_markov_generator_embeddability_boundary_2026_06_06.txt`](../logs/runner-cache/frontier_record_markov_generator_embeddability_boundary_2026_06_06.txt).

## Result

The production-kernel boundary separates realized post-record append/count
dynamics from a probability kernel. This note adds the next dynamics gate:

```text
a discrete stochastic production kernel is not yet a continuous-time rate law.
```

Some stochastic kernels are embeddable as

```text
P(t) = exp(Q t)
```

for a finite Markov generator `Q`. Others are not. Even when a kernel is
embeddable, the rate and clock interval are extra data: the same finite
transition matrix can fix only a product such as `rate * time`, not the
separate physical rate and time unit.

## Exact Checks

The runner uses column-stochastic convention.

### Positive embeddable example

The lazy two-state kernel

```text
P_lazy = [[3/4, 1/4],
          [1/4, 3/4]]
```

is generated at `t=1` by

```text
Q = [[-r, r],
     [ r,-r]],       r = log(2)/2.
```

This is a valid continuous-time Markov generator once the rate and clock
interval are supplied.

### Negative determinant obstruction

The swap kernel

```text
P_swap = [[0,1],
          [1,0]]
```

is stochastic and is a perfectly valid discrete producer. But

```text
det(P_swap) = -1.
```

No finite real generator can satisfy `P_swap = exp(Q t)` at finite `t`, because

```text
det(exp(Q t)) = exp(t tr(Q)) > 0.
```

So a valid discrete record-production kernel need not be a continuous-time
Markov step.

### Singular reset obstruction

The reset/write-zero kernel

```text
P_reset = [[1,1],
           [0,0]]
```

is stochastic but singular. A finite matrix exponential is always invertible,
so exact finite-time reset is not produced by a finite bounded Markov generator.
This is the stochastic-producer analogue of the finite-time reset semigroup
boundary in the record stack.

### Clock-rate normalization

The same `P_lazy` is also generated with

```text
r = log(2)/4,      t = 2.
```

Thus even the embeddable case fixes a product `r t`, not the physical rate and
clock interval separately.

## Dynamics Implication

The typed dynamics stack is now:

```text
post-record append/count layer
  consumes realized atoms

production kernel
  assigns probabilities over next atoms

Markov generator + clock
  supplies continuous-time rates when embeddability and normalization hold
```

Each layer is a separate gate. Record can host realized updates; a stochastic
kernel can describe possible next records; a continuous rate law needs still
more structure.

## Boundaries

- Does not derive a production kernel.
- Does not derive a Markov generator.
- Does not derive transition rates, a clock metric, or Born probabilities.
- Does not select a Koide/generation dial location.
- Does not update repo-wide authority surfaces.

## Runner Summary

Expected scorecard:

```text
PASS=19 FAIL=0
```
