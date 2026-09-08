# Exact global witness against a scalar-plus-flippability eighth diagonal

## Source coverage and independent reconstruction

Read complete root check.py SHA4cf2d62afb714b3a3211cdf73a5749065d2301dbae2c193d7517228b20f487ca. Its nonbacktracking path enumeration, fork/star multiplicities, periodic cycle conventions, deterministic legal-successor selection and feature extraction are consistent with the frozen combinatorial proof. It does not fit a physical coefficient. The original541533 count is the author's count, not repeated here as independent predicates.

The new helper independently builds the coordinate graph and enumerates four-step neighbor-slot tuples iteratively, without importing or executing the root checker. It stores all192/648 edge bits at each of the first three states, legal flip edge IDs/endpoints and pre-flip bits. Full degree-three legality is checked at every state and transition. State SHA hashes match the three corresponding root snapshots exactly. This is independent implementation verification after source reading, not blind candidate discovery.

## Narrow obstruction

Write the proven diagonal as a scalar plus

Q(x)+(3559/14400) F(x),
Q=−209 d(x)/28800+1769 P(x)/216000,

where d is total cycle domain walls, P the sum of four-edge sigma products, and F total cycle flippability. A scalar+aF representation would force Q to be affine in F on every ice state, even if the scalar and a were allowed to depend on volume.

On L4, counting all simple four-cycles including winding cycles, the three exact feature triples (F,P,d) are

(144,240,576), (136,208,576), (130,192,576).

The affine determinant (F1−F0)(Q2−Q0)−(F2−F0)(Q1−Q0) is −1769/3375, nonzero. The two successive legal flips are winding cycles with edge IDs[0,48,96,144] and[1,13,25,37] in the declared coordinate edge order.

On L6, where every simple four-cycle is an elementary plaquette, the triples are

(324,648,1296), (320,624,1304), (317,612,1310).

The determinant is −1769/9000, again nonzero. The successive legal plaquette flips have edge IDs[0,125,15,17] and[1,558,541,540]. Some cross a periodic coordinate seam; they are ordinary elementary plaquettes, not length-four winding cycles. Translation can place each such plaquette away from a coordinate seam, which is only a coordinate convention.

All three states in each witness are connected by legal alternating cycle flips. The obstruction therefore persists even on that particular ring-connected component, not merely across disconnected ice sectors.

## What follows

For the supplied full-carrier perturbation and the specified canonical direct-rotation convention, the eighth-order diagonal is not a scalar plus a multiple of total four-cycle flippability. L6 shows this failure without extent-four winding contributions. This is an exact finite counterexample to that claimed functional identity. It does not prove a phase statement, compute the full eighth-order offdiagonal operator, preclude other independently supplied interactions, or exclude special tuning in a different model. It also does not establish any thermodynamic magnitude or continuum inference.

The witness uses the frozen local coefficient table and the global connected-motif reduction as mathematical dependencies. The finite state reconstruction independently checks admissibility, features and the determinant; it does not independently rederive all perturbative coefficients. No canonical files changed.
