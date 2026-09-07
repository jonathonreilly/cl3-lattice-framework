# Postexecution contract amendment

The core star and cube targets survived, but frozen item 9 did not survive as
written. Independent execution review found two distinct defects:

1. The star parameter is `C=cosh(beta_star sqrt(6))`, whereas the diagonal
   unequal/equal weight of a unit two-site hop is
   `E=cosh(beta_edge)`. Reusing `C` at one common beta was false.
2. A blank/no-Record neighbor cannot simultaneously mean an explicit third
   condition and an unobserved binary neighbor. Independent binary
   marginalization does not cancel remote interactions.

The corrected execution therefore retains only the complete binary
full-conditional edge law and adds a separately declared ternary
Record-snapshot model for all blank conditions. On a binary cube at `E=5/4`,
one fixed zero neighbor and all other sites unobserved give the exact center-one
probability `54875/98523`, not `5/9`; the runner makes that counterexample
load-bearing.

Three further scope refinements were forced during execution:

- the cubic sharpness control is an on-lattice square plaquette (`h^4`), not an
  off-lattice leaf triangle;
- the primary literal Record is the same-site occupation PVM followed by a
  supplied incident-edge gate; a three-level pointer is only an optional
  dilation requiring an extra carrier; and
- perfect transfer is proved on an isolated eight-vertex cube. Boundary
  isolation is supplied and explicitly mutation-tested.

These are target corrections, not silent passes. The final status is a
corrected bounded theorem, not successful execution of frozen item 9 verbatim.
