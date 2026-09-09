# Block31 preflight witnesses

Let `R=L+9f`, and let `d` range over the four unit directions perpendicular to
`f`.  Candidate output centers are `L+9d` and `R+9d`.  Their inward STATUS
samples are `L+5d` and `R+5d`.

For each candidate, copy the sample one step axially to `L+f+5d` or
`R-f+5d`; move the copy radially to `L+f+d` or `R-f+d`; then move it axially to
the comparator ports

`G_d=L+4f+d`, `H_d=L+5f+d`.

This uses one QND CNOT followed by seven SWAP layers per rail.  The 64 relay
sites are pairwise distinct and disjoint from the axial history and all eight
candidate 32-site block supports in an ephemeral enumeration.  The target
runner must recompute those facts and must verify every gate is one-site or
nearest-neighbor two-site after Toffoli decomposition/routing.

At the ports, the 16 ordered one-hot pairs partition into four equal, four
opposite, and eight perpendicular cases.  The exact `(g,h)` selector must be
retained for the future dispatch compiler because a three-class flag alone
does not identify which perpendicular Block30 route is required.

These are preflight witnesses only.  Gate counts, depth, covariance, cleanup,
the abstract projector specification, and route correspondence are target-
runner outputs, not preregistered facts.
