# Fixed-flux first-order electric penalty

Root supplied the candidate; this derivation verifies it. On the full cubic edge carrier, with degree6 and Q_v=epsilon_v(deg_x(v)-3),

 Q_v²=(1/4)(sum_(e incident v) Z_e)²=3/2+(1/2)sum_(e<f incident v)Z_e Z_f.

Thus D=3N/2+(1/2)sum_v sum_(e<f incident v) Z_e Z_f. No low-charge projection is present. The sign epsilon_v squares away. In a general simple graph the centered penalty (deg_x(v)-d_v/2)² has scalar sum_v d_v/4=E/2 and the same pair sum; that is not automatically the original cubic charge definition on a different graph.

In the full dictionary, Z_e is Z_e^g. Magnetic flux sectors are the orbits of link-X signs under vertex-star flips. An electric product Z_F toggles exactly the subset F of link-X signs and therefore sends flux character phi_C to (-1)^|F intersect C| phi_C for every cycle. It stays within a fixed flux sector if and only if F is a cut (mod2 coboundary). This is the standard cycle/cut orthogonality, also seen directly because a sign assignment is gauge equivalent to its toggled assignment exactly when the changed signs form a product of stars.

For the pair terms of D, F consists of two distinct incident edges. A connected cubic periodic graph with all even extents>=4 has no nonempty cuts of size1 or2 (proved below). Consequently every pair term maps to a distinct flux sector and

 Pi_phi D Pi_phi=(3N/2)Pi_phi

on the ENTIRE fixed-flux even-Fock sector, not just its U0 ground states. Distinct pair terms may reach the same other sector and interfere there; this does not affect the diagonal compression. It does not say D is scalar on the full carrier. Since D vanishes on actual ice states while its trace average is3N/2, it is manifestly not globally scalar.

A direct elementary proof of the needed no2-edge-cut fact avoids any external graph theorem. Given an edge in direction a, there are four length-three square detours between its endpoints, obtained by displacement +b,-b,+c,-c along the two other axes. For extents>=4 these detours are pairwise edge-disjoint and avoid the original edge. Any cut containing that edge must meet each detour, so it contains at least five edges. This lower bound suffices; claiming the sharper connectivity6 is unnecessary to this proof. Periodic seams do not change the distinctness of these translated detours.

For a general connected graph the precise exception is a pair of incident edges that itself forms a cut. Merely having some2-edge cut is not sufficient if its two edges are disjoint and never occur in the penalty sum. If F=delta(S), then on Gauss-invariant vectors product_(e in F)Z_e^g=product_(v in S)P_v^f. Hence its within-sector contribution is a generally nonscalar even matter-parity operator. S and its complement give the same operator because total matter parity is even. A bridge alone does not occur as a linear term in this centered-square penalty, although sums of two bridges can be an incident cut and contribute. Parallel-edge/L2 geometries require their actual incidence and cycle space; the simple cubic argument must not be transferred by collapsing labels.

For perturbation theory, let H0 denote the U0 Hamiltonian at fixed nonzero supplied g and coefficients, and let an eigenspace P_* lie wholly in one flux sector with eigenvalue E_*. If E_* is isolated from ALL other eigenvalues of the full finite H0 by a positive gap, then first-order degenerate perturbation by U D is scalar3NU/2 on P_*. Degeneracy within that flux eigenspace, including spectator degeneracy, is not split at first order. This requires excluding coincident-energy states in other flux sectors; if they exist, the full degenerate eigenspace can have nonzero off-flux D matrix elements at first order. Even with isolation, second and higher orders can couple virtual other-flux states. There is no claim of a cubic optimal flux, a uniform gap, nonzero-U solvability, or scalar correction on the globally degenerate ground manifold without those extra hypotheses.

## Exact bounded controls

The independent standard-library control checks all960 incident edge-pair removals on the actual L4 degree6 graph; each remaining graph is connected, so every term changes a magnetic flux. Small-graph fixed-flux gauge-parity compressions distinguish the hypothesis: on K4 (using its degree-centered penalty) the compression is3I but12 pair terms leave the sector; the full penalty is not scalar, since the all-zero electric state has value9. On a square, the incident pairs are cuts and the even-Fock diagonal values are4,2,2,2,2,2,2,0, a direct nonscalar exception. These are not cubic phase controls. The run passed964 predicates in0.028s, with no sampling or author imports. The general result rests on the cut selection rule and four disjoint detours, not the finite census.
