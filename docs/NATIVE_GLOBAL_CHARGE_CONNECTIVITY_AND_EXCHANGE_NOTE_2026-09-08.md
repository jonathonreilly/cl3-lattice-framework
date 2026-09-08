---
claim_id: native_global_charge_connectivity_and_exchange_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Finite even cubic tori with all extents at least four and the supplied full low-charge native carrier: hopping-only connectivity of the entire one-positive/one-negative D2 configuration space, conditional uniqueness of its finite ground state for nonzero hopping, and an explicit globally supported D4 exchange loop. No D4 connectivity, transport rate, thermodynamic gap or selected physical dynamics."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_rk_charge_stability_note_2026-09-08
runner: scripts/native_global_charge_support_2026_09_08.py
---

# Global charge connectivity and a supported exchange loop

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

Every configuration with one positive and one negative charge can be reached from every other by permitted native hopping in the supplied finite model. The proof includes charge positions and the full edge configuration. A separate four-charge witness supports the native same-sign exchange algebra globally and shows why the two-charge sign convention does not extend automatically.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite results under the supplied full low-charge carrier and Hamiltonian."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Premises and operators

The [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) supplies the ambient edge Pauli algebra, its exact fermion–$Z_2$ Gauss representation, and low-charge hopping. The [charge stability note](NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08.md) supplies the ordered signed-hole frame and ring sign used below. These are provisional science dependencies, not audit-ratified physical premises.

Let the graph be $C_{L_1}\square C_{L_2}\square C_{L_3}$ with each $L_a$ even and at least four. It is simple and six-regular. All edge configurations in the supplied low-charge domain are available; no fixed winding or magnetic-cycle constraint is imposed. Define

\[
n_e=\frac{1-Z_e}{2},\qquad \epsilon_v=(-1)^{v_1+v_2+v_3},\qquad
G_v=\sum_{e\ni v}n_e-3,\qquad Q_v=\epsilon_vG_v,\qquad D=\sum_vQ_v^2,
\]

and restrict to $|G_v|\le1$. The sector $D=2$ has precisely one $Q=+1$ and one $Q=-1$, since the total signed charge vanishes. Write $p,m$ for their positions. Orient an edge $v\to w$ when $\epsilon_v(2n_e-1)=+1$. Its outdegree is $3+Q_v$.

For ascending local neighbor orders, the native convention is

\[
B_i=\prod_{e\ni i}Z_e,\quad
A_{ij}=X_{ij}\prod_{k<_i j}Z_{ik}\prod_{l<_j i}Z_{jl}\quad(i<j),\quad
A_{ji}=-A_{ij},\quad T_{ij}=\frac{i}{2}A_{ij}(B_i-B_j).
\]

A permitted low-charge hop moves a positive charge along an electric arrow, or a negative charge against it, to a neutral neighbor. It toggles that edge and has modulus-one amplitude. The argument concerns this actual support; it never discards phases to infer matrix-element existence.

## Six-edge cuts and charge-position reachability

Every nonempty proper vertex set has at least six cut edges. To see this, count crossings separately along the three coordinate directions. A mixed periodic fiber crosses an even number of times, at least twice. If all three direction counts are positive, their sum is at least six. If one direction has zero crossings, membership is constant along each fiber in that direction. Every crossing in a perpendicular direction repeats in at least four translated fibers, and each such mixed fiber contributes at least two crossings. Thus the total is at least eight. Some crossing exists by connectivity. A singleton attains six.

Delete the negative vertex $m$ and let $R$ be vertices reachable from $p$ along arrows. Suppose the remaining complement $B$ is nonempty. There is no arrow from $R$ into $B$. Every vertex of $B$ is neutral, so its total divergence is zero. Incoming edges to $B$ can come only from $m$, which has outdegree two. The number of outgoing edges equals the number incoming, making its cut at most four, a contradiction. Hence $p$ reaches every vertex except $m$.

Choose a directed simple path. Flipping its edges successively moves the positive charge along it, leaving the negative fixed. Simplicity ensures the next edge was not changed earlier. Every prefix remains in $D=2$. Reversing the arrows and charge signs gives the negative-charge version. Each path has at most $|V|-2$ edges.

Any requested ordered pair of distinct positions is therefore reachable in at most three such operations. If the desired positive position is the current negative position, first move the negative to a spare vertex, then move the positive and finally the negative to their targets. Otherwise two operations suffice. This is a finite support statement, not a shortest-path or mixing bound.

## Reversing a directed cycle using only hopping

We prove by induction on length that any directed simple cycle can be reversed while restoring both charge positions and every off-cycle edge.

If the cycle avoids the negative charge, move the positive along a directed access path avoiding the negative, stopping at its first cycle vertex. The access path is internally disjoint from the cycle. Traverse the cycle forward and retrace the reversed access path. Net change is precisely the cycle reversal. If the cycle avoids the positive, use the negative with arrows reversed.

For a cycle with a chord joining nonconsecutive vertices $a,b$, write its arcs as $P:a\to b$ and $Q:b\to a$. Suppose the chord points $a\to b$. First reverse the shorter directed cycle consisting of the chord and $Q$. Now reverse the shorter cycle consisting of $P$ and the reversed chord. Induction applies in each current orientation and restores the signed positions after each operation. The chord is reversed twice, while every original cycle edge is reversed once. The opposite chord direction uses the complementary order. Both subcycles are strictly shorter because the endpoints are nonconsecutive.

It remains to handle an induced cycle containing both charges. The positive vertex has four outgoing edges, exactly one on the cycle. Because the cycle has no chord, its other three outgoing neighbors lie outside the cycle and are neutral. Park the positive charge along one of those edges. The cycle itself is unchanged. The negative charge can now traverse the entire cycle backwards, returning to its original vertex and reversing the cycle. The parked positive returns along its reversed temporary edge, which the traversal never touched. This restores that edge and the positive position. Every prefix remains a legal two-charge configuration.

This completes the induction, including noncontractible cycles. No ring move or extra phase operation is required.

## Full configuration connectivity and finite sector ground state

After aligning charge positions, compare two configurations. Orient every edge on which they differ as in the first configuration. Equal full outdegrees imply that this difference subgraph has equal incoming and outgoing degree at every vertex. It decomposes into edge-disjoint directed simple cycles. Reverse these successively by the construction above. Each completed operation changes only its requested cycle, so all remaining difference cycles retain their orientation. The result is exactly the target edge configuration. Thus the entire supplied $D=2$ hopping graph is connected.

For the supplied Hamiltonian

\[
H=\sum_p J_p F_p(I-S_p)+UD+tT_{\rm low},\qquad J_p\ge0,
\]

the parent ordered signed-hole frame makes every allowed $D=2$ hopping entry negative for $t>0$, and the ring off-diagonal entries are nonpositive. For $t<0$, the position phase $\epsilon_p\epsilon_m$ reverses all hopping signs and preserves the rings. With $t\ne0$, connectivity makes $cI-H$ nonnegative and irreducible for sufficiently large finite $c$. The finite Perron theorem therefore gives a simple lowest eigenvalue and a strictly positive ground vector in this frame, within $D=2$. This imports the checked sign frame; connectivity alone would not justify Perron positivity. There is no uniqueness conclusion at $t=0$, for the full all-charge Hamiltonian, or inside an additional fixed-winding restriction.

## A globally supported four-charge exchange witness

Use the complete periodic $4^3$ graph: 64 lexicographically ordered vertices, 192 sorted undirected edges and ascending neighbor lists. Set

\[
i=(0,0,0),\ j=(1,0,0),\ k=(0,1,0),\ l=(0,0,1).
\]

Place positive charges at $j,l$ and negative charges at $(2,2,0),(2,0,2)$. Fix $n_{ij}=0,n_{ik}=1,n_{il}=0$. The four charged vertices all require degree two; all others require degree three. An exact bipartite integral flow with residual degree capacities constructs the remaining bits. Flow 93 saturates every demand. The delivered bitstring is then directly checked against all 64 degree equations; validity does not rest on a solver's status alone.

Both sequences

\[
A:\ i\leftarrow j,\ k\leftarrow i,\ i\leftarrow l,
\qquad
B:\ i\leftarrow l,\ k\leftarrow i,\ i\leftarrow j
\]

are nonzero at every step, stay in the full low-charge domain with two charges of each sign, and finish in the identical 192-bit configuration. Literal native endpoint strings and the neutral-target/charged-source factor $T_{ab}=-iA_{ab}$ give route amplitudes $-i$ and $+i$. Route $A$ followed by the reverse of $B$ is therefore a six-hop loop with product $-1$. Complementing all bits gives the opposite-signed template, also checked. Bitstrings in the output put edge zero at the right; the full edge list and all intermediate charge vectors are retained.

A diagonal unit-modulus change of basis multiplies each hopping amplitude by an endpoint phase ratio. These cancel around a closed loop. The negative six-hop product therefore excludes a diagonal rephasing making all hopping entries nonnegative real on its containing component. It also excludes making all entries negative real, since six negative factors have positive product. This is only a diagonal-phase obstruction for the delivered component. It neither proves full $D=4$ connectivity nor excludes a non-diagonal unitary or a different supplied domain. It resolves the global extendibility of this particular local exchange template, not every possible local boundary pattern.

## Evidence, provenance and remaining physical questions

The paired runner executes three finite helpers: 328177 reachability predicates, 78 full-cycle predicates and 102 exchange predicates, totaling 328357. Reachability checks include a complete two-dimensional cut analogue, selected three-dimensional cuts and 33368 directed paths across stated finite neighborhoods, not a complete $D=2$ census. The cycle fixtures construct full $4^3$ configurations with a four-cycle requiring parking (six hops) and a chorded six-cycle (eight hops), checking every global intermediate and exact final cycle XOR. The exchange helper retains complete bitstrings and native phases. Finite controls check these constructions; the general theorem is the proof above.

Original proofs, protocols, raw outputs and independent reviews are preserved in the [research packet](../.claude/science/physics-loops/native-global-charge-support-20260908/HANDOFF.md). The original reachability proof explicitly left full connectivity open. Its separate extension preserved that history; root supplied the same chord/parking idea before the author's extension was frozen, so it is not presented as a blind discovery. Independent proofs and an independent CAR/dictionary replay of the exchange phases are separate evidence.

Graph cycle decomposition and the finite Perron theorem are standard mathematics. No historical novelty of these tools is claimed. The new supplied-model conclusions do not select the low-charge projector, relaxed cycle domain, couplings, physical preparation or native occurrence law. They do not establish a transport rate, a thermodynamic gap, deconfinement, a photon, continuum statistics or a completed theory.
