# Additional adverse ground-subtraction control

Frozen before running the matrix checker. Add K=diag(0,1,10), V=[[1,0,1],[0,1,0],[1,0,1]], P first two coordinates. The analytic expectation is that lowering only the first retained mode makes the exact first gap larger than the finite Ritz gap. This is a prospectively checked discriminator against treating the finite gap as an upper bound, not an independently discovered numerical result.

Clarify the original g=1/4, rank-one-P fixture: it can test failure of the mu<g hypothesis and a vacuous lower endpoint, but it has no second Ritz eigenvalue and therefore cannot by itself supply a finite gap. The checker must report that missing index rather than manufacture it.
