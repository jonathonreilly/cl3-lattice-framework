# Independent Checker Return

The structurally independent checker:

- imports only the Python standard library and imports neither the Block-16
  nor Block-15 primary runner;
- reconstructs the writer, external destinations, and 73-site support with
  sparse integer-coordinate sets;
- uses exact `Q(1/sqrt(3))` Bloch arithmetic and positive-functional/state
  factorization rather than SymPy density/Choi matrices;
- represents the channel by symbolic blank/nonblank central effects;
- reconstructs the flag front by directed Record-edge extrapolation;
- independently rebuilds all controller maps and blocked frontiers;
- uses a separate `6x43` preparation-label array for the joint-law result;
- tests positive local Born overlaps while explicitly rejecting a Born
  distinguishability reading.

Return:

```text
primary:     10/10, mutations 58/58
independent:  7/7, mutations 64/64
terminal: COVARIANT-CONDITIONAL-CAP-PACKET-INSTRUMENT
```

Exact independent counts:

```text
writer sites                         43
external controller destinations    30
composition extension               73
branches                              6
proper cubic rotations               24
controller maps                    2,688
generated blocked              186 / 5,166 frontier evaluations
inherited blocked            2,976 / 171,936 frontier evaluations
```

Both implementations agree exactly on every branch Record mask and Bloch
content, the seven composition counts, and
`P_prod(valid)=30517578125/101559956668416=5^15/6^18`.

After whitespace/comment normalization and unique-line reduction, the sources
share 112 lines in a 2,075-line union (`5.40%`).  Their five exact top-level
function AST matches are only the four elementary coordinate helpers
`add/subtract/scale/dot` and mutation-sweep boilerplate; they share zero exact
nontrivial science-function ASTs.

Root read the complete 1,630-line implementation and replaced no result.  The
checker preserves the selected-center, atomic-event, effective-mask,
preparation-label, locality, concurrency, occurrence/rate/time, gravity,
axiom, retention, obligation, and TOE boundaries.
