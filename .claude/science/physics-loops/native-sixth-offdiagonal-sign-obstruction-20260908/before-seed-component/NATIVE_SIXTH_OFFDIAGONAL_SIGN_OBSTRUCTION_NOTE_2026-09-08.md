---
claim_id: native_sixth_offdiagonal_sign_obstruction_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied full native carrier: complete canonical sixth coefficient for uniform magnitudes, and exact same-component L6 witness obstructing an all-nonpositive diagonal-phase gauge in an explicit coarse finite-volume coupling window, with a global canonical norm remainder. No arbitrary-basis or phase claim."
upstream_dependencies:
  - native_virtual_pair_ring_mechanism_note_2026-09-08
runner: scripts/native_sixth_offdiagonal_sign_obstruction_2026_09_08.py
---

# Sixth-order native hopping and a signed configuration loop

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

Virtual native pair fluctuations generate both corrected four-cycle hopping and six-cycle hopping. Their signs form an exact frustrated configuration loop on a globally valid L6 ice state: no diagonal change of basis can make all its transitions real nonpositive. This is a fixed-convention finite perturbative result, not an obstruction to arbitrary basis changes or a phase claim.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Canonical finite H6 with supplied Hamiltonian and exact diagonal-phase witness."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Complete coefficient and parent convention

Use the [full-carrier mechanism](NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md), [native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) and [instrument](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). All even periodic extents are at least four; there is no hard charge gate, fixed magnetic-cycle sector or omitted winding sector. For supplied $H=UD+g\sum_e\lambda_eA_e$, $U>0$, uniform $|\lambda_e|=\lambda$, the canonical direct-rotation coefficient is

\[
H_{\mathrm{eff}}^{(6)}=\frac{g^6\lambda^6}{U^5}\left[
-\frac{1053N}{40}P-\frac{43}{6}\sum_{C\in\mathcal C_4}B_C
-\frac38\sum_{C\in\mathcal C_6}B_C\right].
\]

$N$ is the vertex count, $P$ the ice projector, and $B_C$ is the explicitly signed sequential native cycle product defined below. Individual real coupling signs are included once in $B_C$; repeated signs square away. The parent sixth diagonal is expressly in this same canonical convention, so adding it to the complete offdiagonal support classification gives the full coefficient. This is a finite Taylor coefficient, not a volume-uniform perturbative convergence claim. No eighth-order offdiagonal result is used.


## Explicit finite-volume norm and sign window

The appendix gives an independent global analytic estimate for the exact canonical operator. Put $\mathcal L=\sum_e|\lambda_e|$ and $a=|g|\mathcal L$. For $a\leq U/8$,

\[
\|K_{\rm can}-K_6\|\leq\frac{2^{19}}3\frac{a^8}{U^7}.
\]

For the uniform model write $\epsilon=|g|\lambda/U$ and $E=3N$. The exact four-transition sign obstruction survives whenever

\[
0<\epsilon<\min\left\{\frac1{8E},\sqrt{\frac3{86}},\frac3{2^{23/2}E^4}\right\}.
\]

This deliberately coarse global bound scales with $\mathcal L^8$ and has an extremely restrictive volume-dependent window. It is not a practical threshold, a volume-free isolated band, or the parent's local dynamical theorem. Existing finite controls verify coefficients and witnesses; they do not test this analytic norm theorem.

## Scope and convention

Use the supplied full H=UD+g sum_e lambda_e A_e on a simple bipartite degree-six cubic torus of even extents at least four. There is no low-charge projection. The global formula below assumes uniform coupling magnitude, with individual real signs retained in the native product. All effective coefficients use the canonical direct rotation; this is not a transfer to an arbitrary local normal form.

For an unoriented simple even cycle C, choose a traversal e0,...,e_(k−1), and define B_C to act as the alternating-cycle indicator times the sequential product A_(k−1)...A_0, with any chosen actual canonical edge signs included. Its reversal has the same product for even k: reversal contributes (−1)^k from the k incident anticommuting pairs. A cyclic shift likewise crosses two incident neighbors and changes no sign. Thus B_C is well-defined independently of traversal start/direction, is Hermitian, and toggles the cycle only on alternating inputs. This is an explicit native-product convention; converting to the parent's oriented S_C requires retaining its orientation and i^k factor. No universal sign is inferred after discarding that conversion.

For all positive coefficients in this canonical-A convention, the sixth offdiagonal coefficient is

(g^6/U^5)[−(43/6) sum_(C4) B_C4 −(3/8) sum_(C6) B_C6].

For uniform magnitudes lambda and arbitrary signs, include lambda^6 times the product of the signs on the toggled cycle in each B_C. Repeated-edge signs square to one. The result concerns only offdiagonal entries between ice strings. It combines with the parent's sixth scalar only in this same canonical convention. No phase or thermodynamic conclusion follows.

## Completeness of transition support

Between two ice configurations the toggled edges have balanced occupied and empty incidences at each vertex. Their nonempty support is therefore an alternating Eulerian subgraph. At order six its size is even and at most six. A simple bipartite graph has no two-cycle or triangle; the minimum nonempty support is a four-cycle. A six-edge Eulerian support must be a simple six-cycle: any decomposition into more than one cycle would require at least eight edges. This argument also excludes repeated-vertex figure-eight transitions at this order.

Consequently, six distinct flips give a simple six-cycle. Four-cycle transitions have the four changed edges used oddly and exactly two additional uses: either one cycle edge is used three times, or an extra edge is used twice. All six-cycle geometries have the same abstract active cycle algebra and energy function. This includes planar rectangle perimeters, nonplanar hexagons, periodic winding examples and any other simple six-cycle; a geometrical list is unnecessary once all simple cycles are included. Inactive chords do not alter the fixed-exterior degree deviations or active-edge commutation signs.

An extra edge for a four-cycle is either incident to one cycle vertex or vertex-disjoint. It cannot connect two cycle vertices: adjacent endpoints would duplicate an existing edge, while opposite endpoints lie in the same bipartition. Each cycle vertex has four external incident edges, giving sixteen distinct spokes. On an alternating ice cycle exactly one occupied and one empty cycle edge meet each vertex; the four external edges comprise two occupied and two empty. The local spoke coefficient below is identical for either bit, so its embedding sum is uniform.

## Canonical two-dimensional recursion

For an alternating C4, with or without one spoke, let P project onto the two fixed-exterior ice states, Q=I−P and D_Q>0. Let chi: P→Q be the graph wave operator, with Omega=P+chi and P Omega=P. Invariance H Omega=Omega H_B gives, since PVP=0,

D_Q chi+g QVP+g QVQ chi−g chi PVQ chi=0,
H_B=g PVQ chi.

At coefficient n,

chi_n=−D_Q^-1[delta_(n1) QVP+QVQ chi_(n−1)−sum_(a+b=n−1;a,b>=1) chi_a PVQ chi_b].

The first term involving chi0 is omitted. This exact triangular recurrence includes the folded feedback terms. The isometry Omega M^-1/2 with M=I+chi†chi has positive P overlap, hence is the canonical direct-rotation column. Its effective Hamiltonian is

H_eff=M^1/2 H_B M^-1/2.

This direction follows directly from Omega†Omega=M and H Omega=Omega H_B; it is not guessed from Hermiticity. Exact binomial series through sixth order suffice. The finite helper separately checks the graph equation, inverse metric product and Hermiticity at every retained degree. At this order M2 is scalar, so these particular fixtures cannot discriminate the inverse similarity direction merely by their final sixth matrix; the algebraic isometry derivation supplies that obligation.

For an isolated alternating C4 the canonical matrices are H2=−2I, H4 with diagonal3/2 and offdiagonal1/2, and H6 with diagonal−5/2 and offdiagonal−3/2. With one spoke, either initial spoke bit gives H6 diagonal−97/24 and offdiagonal−89/48. Subtracting the isolated C4 result leaves the connected spoke correction −17/48. Other proper subsets cannot realize the same C4 transition, so no further offdiagonal inclusion-exclusion terms occur.

A vertex-disjoint edge factorizes from the cycle. The low isometry is the tensor product of the two positive-overlap canonical isometries, and its effective Hamiltonian is the sum of the factors. Thus mixed disconnected offdiagonal coefficients vanish, rather than producing an extensive correction to a local ring. Sixteen spokes then give −3/2+16(−17/48)=−43/6.

## Leading six-cycle coefficient

Any nonempty proper subset of a simple alternating cycle has an endpoint of degree one in the toggled support, and hence nonzero D. A six-distinct-edge history therefore never returns to P before its last step. Folded terms cannot contribute to this monomial. The amplitude is the sum over all720 permutations of the native product matrix element divided by the five negative full-D intermediate energies. The exact sum is −3/8 times the sequential cycle product. All proper-subset energies and phases are retained; no bare-X substitution is made.

The abstract cycle calculation applies to every actual simple six-cycle by diagonal gauge equivalence of the active flip hypercube: pairwise square holonomies are precisely the native incident anticommutation signs, while fixed exterior factors are edge-sign gauges. Ratios to the sequential product are invariant under that gauge. This proves geometry independence of the coefficient without replacing native phases by a bosonic model.


## Actual global sign witness

# A globally supported fourth/sixth native sign loop

Root proposed the three-face cube-corner route before this witness search. The initial coordinate seed failed; its exact script and failure are preserved. An exact integral bipartite degree-completion then found a full192-edge L4 ice bitstring. This is a deterministic existence certificate, not sampling or an ergodicity claim.

Each fixed cube assignment is tested for three successive alternating face flips. Remaining edge occupancies are a bipartite unit-capacity flow with prescribed residual degree three at every vertex. The returned full state and every subsequent state are checked directly against all64 degree constraints. Raw RESULT stores all four192-bit states. The cube lies in coordinates0/1 and no witness face wraps a periodic seam.

The legal three-face edge lists are [49,62,52,50], [3,52,15,4], [12,62,15,14]. Their combined toggle is the simple nonplanar six-cycle [3,50,49,12,14,4]. Reversing that six-cycle returns exactly to the original full state. Thus all four configurations belong to one explicitly exhibited legal ring component.

Native phases are evaluated directly using A_e=X_e times Z on earlier incident edges in the full coordinate edge ordering. Any alternative endpoint ordering is a diagonal gauge and preserves the closed product. Sequential native-product phases on the three faces and closing six-cycle are (−1,+1,+1,−1). The leading effective coefficients are +1/2 for each four-cycle and −3/8 for the six-cycle in that sequential-product convention. The resulting four transition signs are (−1,+1,+1,+1), with closed product−1.

A diagonal unitary phase change telescopes around a closed configuration loop and cannot alter its product. Four real nonpositive nonzero matrix elements would have positive product. Therefore the fourth-plus-sixth effective hopping cannot all be made nonpositive by a diagonal phase gauge on the component containing this witness. At sufficiently small nonzero real coupling on this fixed finite lattice, higher analytic orders cannot reverse these nonzero leading signs; the same narrow diagonal-gauge obstruction persists for the canonical effective operator. No uniform-in-volume radius is claimed.

This is not an obstruction under arbitrary non-diagonal basis changes, a phase theorem, or a statement that every approximate V0 calculation is invalid. It says that the leading stoquastic ring sign structure does not extend unchanged to this sixth-order native correction in the specified canonical convention. It depends on the separately derived H6 coefficients; independent source-bound review remains necessary before downstream reuse. No canonical files were edited.

# L6 same-local-pattern extension

The frozen L4 source and result remain unchanged. check_l6.py changes only lattice-dependent vertex/edge sizes and the output filename; the exact local cube assignment search and bipartite integral degree completion are retained. It delivers four complete648-bit states, each checked at all216 vertices. The three legal plaquettes are [109,128,112,110], [3,112,21,4], [18,128,21,20], and the closing six-cycle is [3,110,109,18,20,4]. All lie within the coordinate0/1 cube; none crosses a seam or winds.

Sequential native-product phases are again(−1,+1,+1,−1), hence the leading effective signs are(−1,+1,+1,+1) and the four-step product is−1. The exact same diagonal-gauge obstruction therefore exists on L6. The difference between the first and last state is precisely these six edges. At sixth order any contribution to that matrix element must flip those six edges exactly once, so a distinct winding support cannot contribute to this transition. This remains a fixed-finite-volume perturbative statement and does not claim a uniform analytic radius or a phase.

# Discriminating canonical metric-direction control

Supplemental generic finite matrix, not a new native model claim. Take D=diag(0,0,1,2), V off-block with QVP=[[1,0],[1,1]] and QVQ=PVP=0. The exact graph recursion gives

HB2=[[-3/2,-1/2],[-1/2,-1/2]], M2=[[5/4,1/4],[1/4,1/4]], HB4=[[2,3/4],[1/2,1/4]].

Their commutator [M2,HB2]=[[0,-1/4],[1/4,0]] is nonzero. The forward metric similarity gives H4=[[2,5/8],[5/8,1/4]], matching expansion of the normalized-column energy sandwich. The reverse similarity gives [[2,7/8],[3/8,1/4]], which is not Hermitian. Four explicit exact predicates confirm this direct alternative. It supplies a genuine direction discriminator absent from the native fixtures with scalar M2. No subprocess mutation or independent native coefficient derivation is claimed.

## Evidence and scientific limits

The live primary executes fresh coefficient, generic normalization and full L4/L6 witness helpers. Original coefficient and normalization counts are3653 and4. Original witness search guards were not assigned a count. The port adds nine explicit delivered-witness checks per lattice and seven absolute reviewed coefficient/history bindings, giving3682 predicates. No old uncounted checks are promoted retrospectively. Generic metric-direction controls are not native coefficient evidence.

Complete original proofs, raw bitstrings, the failed coordinate-seed search, independent Riesz-projector/late-edge-order reviews and the reviewer's failed modulo-index adaptation are preserved in the [packet](../.claude/science/physics-loops/native-sixth-offdiagonal-sign-obstruction-20260908/REVIEW_HISTORY.md). New actual subprocess mutations are recorded separately from original direct alternatives. No third-party PDF is included; canonical rotations and resolvent techniques are standard mathematics, not claimed historical inventions.

The Hamiltonian, geometry, couplings and ice carrier remain supplied. This does not establish an electromagnetic identification, deconfinement, a phase, a thermodynamic sign radius or impossibility under a general nondiagonal basis. The fixed finite exact sign product is the claimed obstruction. Final canonical source review remains separate from author verification and formal audit status.

## Appendix: complete finite-volume analytic remainder proof

# A coarse exact finite-volume canonical remainder after sixth order

Research proof. Supplied H(g)=UD+gV, with full native D>=0, P=1_{D=0}, D|Q>=2, U>0. Let L=sum_e |lambda_e|, so ||V||<=L. If L=0 the claim is exact. This is a GLOBAL finite-volume norm estimate, not the volume-independent local theorem. No physical coupling selection is implied.

## Analytic canonical Hamiltonian on the fixed ice carrier

Set r=U/(4L). For complex |g|<=r and z on the counterclockwise circle |z|=U, the unperturbed resolvent has norm at most1/U and the perturbed resolvent at most1/(U-|g|L). The Riesz projection

 Pi(g)=(1/(2 pi i)) integral_(|z|=U) (z-H(g))^-1 dz

is analytic and has fixed rank. Resolvent identity gives

 ||Pi(g)-P|| <= |g|L/(U-|g|L) <=1/3.

On the P carrier let A(g)=P Pi(g) P and B(g)=P H(g) Pi(g) P. Thus ||A-I_P||<=1/3 and the principal binomial A^-1/2 is analytic, with norm at mostsqrt(3/2). The exact compressed contour identity H Pi=(1/(2 pi i)) integral z(z-H)^-1 dz bounds ||B||<=U²/(U-|g|L)<=4U/3. Consequently

 K_can(g)=A(g)^-1/2 B(g) A(g)^-1/2

is analytic for |g|<=r and ||K_can(g)||<=2U there. For real g, Pi is orthogonal and Pi P A^-1/2 is an isometry with positive P overlap. This is precisely the canonical direct-rotation column. Therefore K_can is the actual Hermitian canonical effective Hamiltonian for the whole finite ice-descended cluster. Complex g is only an analytic bounding device; no physical nonunitary dynamics is asserted.

The global bit parity F=product_e Z_e conjugates H(g) to H(-g) and is scalar on ice (every ice state has3N/2 occupied edges). Hence A(-g)=A(g), B(-g)=B(g), and K_can(-g)=K_can(g). This supplies evenness of the complete canonical operator, not just its diagonal. K_can(0)=0.

## Sixth-order truncation

Let K_6(g) contain the exact degree2,4,6 Taylor coefficients in this canonical convention. Cauchy's coefficient bound and evenness give, for |g|<r,

 ||K_can(g)-K_6(g)|| <= 2U (|g|/r)^8 / [1-(|g|/r)^2].

In particular, for a=|g|L<=U/8,

 ||K_can-K_6|| <= (2^19/3) a^8/U^7.

The constant is coarse. The volume dependence is explicit in L, and this statement does not provide a volume-uniform isolated band or useful coupling threshold. It is a norm remainder for the canonical operator, separate from the earlier one-sided fourth-order eigenvalue bound.

## A sufficient sign window for the supplied uniform model

For uniform magnitude lambda>0 write epsilon=|g|lambda/U and E=|edges|=3N, so a=UEepsilon. In the legal four-transition witness, three C4 entries of K_6 have coefficient U[epsilon^4/2-(43/6)epsilon^6] times the native B phase. The closing C6 entry has coefficient -(3/8)Uepsilon^6 times its B phase. Distinct transition supports ensure no other C4/C6 term contributes to these entries.

For a strict sufficient window impose

 0<epsilon<min[1/(8E), sqrt(3/86), 3/(2^(23/2) E^4)].

The second bound leaves each C4 magnitude greater than Uepsilon^4/4. The last bound makes the global remainder smaller than (3/16)Uepsilon^6, half the magnitude of the C6 entry; it also is smaller than the retained C4 margin. Therefore all four nonzero signs survive in the exact finite-volume canonical Hamiltonian. The negative closed product obstructs making every entry real nonpositive by diagonal phases in this explicit sufficient window.

This is an extremely conservative existence bound, not evidence of a practical sign threshold, thermodynamic phase or hardness of every simulation method. Arbitrary nondiagonal basis changes are outside the obstruction. The complete H6 coefficients and delivered legal sign witness are separate prerequisites; the analytic norm proof itself does not determine them.
