# Independent Preregistration Attack

The independent attack read only the frozen Block-16 goal, witnesses, and
parent authorities.  It did not inspect a Block-16 implementation and edited
no files.

## Verdict before implementation

The registered trace-and-prepare family is a valid candidate CP/TP
proper-cubic-covariant instrument on the declared effective direct-sum
Record algebra.  No counterexample was found to that finite-channel existence
target.

One exact support defect was found in the original preflight wording.  For
`f=e_x` and next candidate `2f`, the controller sources are

```text
(3,0,0), (2,+/-1,0), (2,0,+/-1),
```

which lie in the 43-site writer block.  The corresponding destinations are

```text
(4,0,0), (3,+/-1,0), (3,0,+/-1),
```

which do not.  Across all six directions they contribute 30 distinct external
sites.  The writer therefore has 43-site support, while direct composition has
73-site support and five external destination conditions per branch.

The attack also separated the direct and inherited blocked counts:

```text
direct generated Block-16 components       = 6*31 = 186
direct generated frontier evaluations             = 5,166
inherited Block-15 regression components   = 6*16*31 = 2,976
inherited frontier evaluations                    = 171,936
```

The correction was frozen at commit
`d51484274ff001cec0e4bb6753eedaf88e3adff2` before result adjudication.

## Algebraic checks that survived

- the common writer block is exactly `1+18+24=43` sites;
- `r_f=-(143/256)f`, with density eigenvalues `113/512` and `399/512`;
- the packet at `2f` is the exact `M=0` hybrid shell;
- the six Record masks are distinct and orthogonal only in the declared
  Record-mask direct sum;
- the six blank effects sum to one and STOP covers every nonblank sector;
- proper-cubic covariance is exact;
- the same-one-site-marginal product model gives valid mass
  `5^15/6^18`.

The product probability is a probability for classical preparation labels
containing exact Bloch possibilities.  It is not a Born probability for
perfectly distinguishing the nonorthogonal density matrices.

## Interpretation boundary

The effective instrument removes `f` and the cap from the input surface at a
conditioned selected center.  It nevertheless imports the six complete target
states through its trace-and-prepare table.  The blank detector, Record-sector
ontology, reset environment, selected center, atomic write, external
destination conditions, and nearest-neighbor compiler remain supplied or
open.
