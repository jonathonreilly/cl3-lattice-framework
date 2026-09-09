# Postexecution validation

The source- and input-pinned primary runner returned:

```text
TOTAL: PASS=12 FAIL=0
```

It checks source custody, the finite cubic two-design, marked-flux
normalization, the constant-determinant biconditional, scalar-shift controls,
the exact Route-Q first-jump weights/filtering/survival/re-jump boundary, the
Route-B marked operation and absorbing semigroup, the narrow carrier theorem,
the parity-safe three-qubit escape, both race laws, Record-only filtration,
axiom custody, N1--N8 scope, and all five N5 resolution classes.

The independent self-contained implementation returned:

```text
TOTAL: PASS=7 FAIL=0
```

It independently recomputes the finite moments, determinant/rate theorem,
same-qubit filter, orthogonal-blank writer, parity embedding, `4/9` versus
`1/2` race, and delayed-exposure/scalar-shift controls. It imports no function
from the primary runner.

The final hostile mutation sweep returned:

```text
KILLED=48 SURVIVED=0 EXPECTED=48
```

Additional checks:

- both runners compile with `py_compile`;
- primary stdout is 3,063 characters and independent stdout is 696, both below
  the 6,000-character limit;
- the canonical primary cache is fresh and forensic N5 readiness reports no
  issue;
- `repo_invariants_check.py --check` passes;
- path-scoped vocabulary lint reports zero violations;
- the four premise documents pass the premise-clean check;
- strict audit lint over the freshly materialized 4,897-row view reports no
  errors after effective-status computation (only pre-existing
  warnings/notices); the generated audit row was deliberately not staged or
  treated as an audit verdict;
- `git diff --check` passes; and
- a fresh main/PR check found no scientific overlap and no gravity-file touch.

These are mathematical and repository checks, not observational evidence or
an independent audit verdict.
