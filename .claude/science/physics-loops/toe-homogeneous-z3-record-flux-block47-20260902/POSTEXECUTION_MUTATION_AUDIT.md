# Postexecution mutation audit

Baseline execution returns `TOTAL: PASS=9 FAIL=0`.

All `31` preregistered mutations exit nonzero and end in a well-formed
`TOTAL` line with exactly the intended certificate red. No mutation survives.
The final harness contains no branch that merely assigns `ok=False`.

Twenty-one mutations alter executable link fields, Hamiltonians, square
targets, path/Bessel coefficients, claimed probability bounds, protocol data,
exterior/gated links, pulse claims, rotation link data, source hashes, or bare
translation claims. Ten are intentionally labeled coverage/type/scope
firewalls: dropping a parity coordinate, replacing an all-time proof by a
low-order one, substituting an odd torus for infinite `Z3`, mistyping
coordinate bits or the source, and injecting the five prohibited promotion
claims. They test claim custody, not hostile alternative physics.

Independent panel review forced three repairs before this result was accepted:

- the Bessel endpoints are now derived from exact series terms and two
  independently constructed polynomial expressions for
  `4(m+1)(m+2)=8+4m(m+3)`;
- `break_rotation_gauge_covariance` flips one actual link ratio and produces a
  non-flat cocycle rather than merely reducing rotation coverage; and
- the perfect-transfer mutant is contradicted by the certified strict upper
  probability bound, not by an unrelated lower endpoint.

Result: `31` killed, `0` survived. Scope guards are not advertised as
mathematical countermodels.
