# Postexecution validation

Runner class: exact deterministic.

An independent SymPy implementation, sharing no runner functions, recomputed
the matrix identities and finite stochastic kernels:

| Check | Result |
|---|---|
| Gibbs density normalization and positivity | PASS |
| distinct `Z/X` resolutions and distributions | PASS |
| distinct ensembles with common barycenter | PASS |
| two functionals agreeing on one PVM but separating another effect | PASS |
| same effects with different instrument outputs | PASS |
| two covariant varying neighbor-count laws | PASS |
| equal conditional content with unequal hazards; active Record commutator | PASS |

```text
INDEPENDENT_TOTAL: PASS=7 FAIL=0
```

Derive-vs-assert check: the runner computes every rational matrix, probability,
Kraus effect/output, law family, kernel row, and commutator. Its scope
mutations are explicitly identified as rhetoric/custody firewalls rather than
physics countermodels.

Edge cases: all seven neighbor counts `n=0,...,6` are full-support and
normalized; both rank-one PVMs sum to identity; both formation hazards are
strictly between zero and one; Record rows are absorbing.

Overall mathematical confidence: high for the finite witnesses. Scientific
promotion confidence: low, because current main already owns the component
results and no physical action-to-law compatibility condition is newly solved.
