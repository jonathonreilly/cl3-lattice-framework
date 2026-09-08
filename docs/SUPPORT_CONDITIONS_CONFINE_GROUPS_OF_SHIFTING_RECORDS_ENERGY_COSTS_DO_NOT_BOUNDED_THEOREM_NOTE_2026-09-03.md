---
claim_id: support_conditions_confine_shifting_record_groups
claim_type: bounded_theorem
claim_scope: "For connected starting polycubes with n<=6 and their complete reachable closure under single-site companion-preserving moves, prove the exact centroid coboundary certificate; no isolated sites does not forbid splitting or preserve original companions. Retain finite simultaneous-isometry census with complete10case160assignment70translation checks, separate explicit probability laws, fixed parity cosets versus N=2 union, and L=6,8 globally postselected adjacent-pair kernels. The Poisson rate measures the defined modulo-sum additive proxy, not physical CoM. Finite g=32 comparison is not all-strength impossibility. No permanent fine-site Record formation, arbitrary-n transport classification or unselected parent acceptance."
upstream_dependencies: []
runner: scripts/support_conditions_confine_groups_of_shifting_records_check_2026_09_03.py
---

# Supplied support restrictions: finite centroid certificates and conditional pair kernels

**Date:** 2026-09-03; source correction 2026-09-08.
**Type:** bounded_theorem. **Status:** conditional finite mathematical source; independent final source confirmation pending. Audit status remains unset.
**Primary runner:** [support_conditions_confine_groups_of_shifting_records_check_2026_09_03.py](../scripts/support_conditions_confine_groups_of_shifting_records_check_2026_09_03.py).
**Runner cache:** [actual canonical execution](../logs/runner-cache/support_conditions_confine_groups_of_shifting_records_check_2026_09_03.txt).

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional finite algebra, exhaustive finite certificates and explicitly bounded numerical diagnostics; no physical formation theorem or uncontrolled asymptotic promotion."
trace_class: frontier_discovery
artifact_role: theorem
next_trace_action: "Original independent reviewer confirms corrected source and actual inputs; coordinator owns integrated validation and any landing. Formal audit is deferred by owner until a solid TOE."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and current authority

The [current minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) is the governing
boundary, not a supplier of this model. Its Record clause makes records permanent
and fixes one local possibility at one site; its Admissibility reading distinguishes
support from a probability-selection or formation rule. A parity occupation on a
coarse corner is not a fine-site Record. Ordinary tensor/Fock composition, the
edge-qubit encoding, pi-flux hopping, chosen preparation, time, probabilities and
measurement/postselection are **supplied conditional hypotheses**. Their physical
realization is not derived here. Repeated changed values and joint configuration
conditioning are counterfactual models, with no embedding into permanent fine-site
Record formation or a nearest-neighbor physical instrument established.

The dated owner proposal about moving records is historical motivation. No axiom
change follows from interpreting that proposal. Historical references #7858,
#7876, #7879 and #7834 are not accepted parents or theorem suppliers; all needed
finite operators and conventions are redeclared below and in this runner. No
reserved source, ledger grade or parent campaign is imported. The runner reads
this final note and the actual current memo as declared, hash-pinned inputs.
Its mathematical runtime otherwise uses only NumPy/SciPy and standard Python.
There is no local runtime helper and no mutual note/cache fingerprint.

## Conditions, laws and observables

A configuration is a finite set S of distinct occupied Z³ sites. A fixed
polycube is a connected configuration modulo translation. The enumerated
reachable domain starts from **all connected fixed polycubes of a specified
size n<=6**, then closes under every admissible move, again modulo translation.
It is not all configurations of arbitrary size. Each coordinate of the physical
centroid is `sum(x in S)/n`.

C_comp requires each occupied site to have at least one occupied nearest
neighbor. It forbids isolated singletons, not changes of companion or separation
into components of size≥2. C_rig preserves every currently adjacent labelled
pair; its stronger isometry version preserves every pairwise distance. These
are examples, with no assertion of weakest/strongest possible law.

K1 proposes one occupied member's nearest-neighbor move to an empty site and
keeps configurations satisfying the chosen condition. For an optional stochastic
K1 law use uniform admissible moves, and **stay** if none exists. The integer
support and centroid results do not depend on these weights. A singleton is
outside the C_comp state domain; the stay convention does not make it admissible.

KS enumerates simultaneous assignments of neighbor steps or stay to all labelled
members, with no collision. STRICT forbids entering a site occupied in the old
configuration unless staying there; PERMISSIVE permits entering a site vacated
in the same tick. These support sets do **not** select transition probabilities.
For the numerical `free-directions/6` transport formula only, supply a separate
**translation-only protocol**: choose one of the six unit translations uniformly,
accept if allowed, otherwise stay. This is not uniform sampling of all KS
assignments or uniform sampling of nonstay allowed translations.

KT uses two ordinary fermions with the self-contained site-ordered exchange
sign and unit pi-flux nearest-neighbor hopping on even L=6 or8 tori.
`eta(v,0)=1`, `eta(v,1)=(-1)^v_x`, `eta(v,2)=(-1)^(v_x+v_y)`.
After supplied duration tau, square the propagated amplitudes, discard every
nonadjacent configuration and normalize by the strictly positive success mass.
This is **global outcome postselection**, not a local physical formation law.
It maintains adjacency by definition only when the normalizer is positive.
The actual sampled normalizers and row sums are checked. Failed postselection
has no tick in this conditional protocol; no physical retry law is inferred.

For KT define `s=(x+y) mod L`, and for a transition set
`d=minimal(s'-s mod L)/2` with `minimal` in `(-L/2,L/2]` and positive ties.
The computed additive observable sums these d increments and centers its
stationary drift. It is a **modulo-sum proxy**, not a physical CoM lift:
L=6 {0,1}→{3,4} has displacement3 but proxy0. This transition has positive
conditional weight. Finite wrap/drift effects are part of the observable, not
proof they are absent. D1 is the centered single-particle minimal-image lift
variance/(6*tau) on the same finite torus. The ratio does not compare true CoM
and one-particle physical diffusion constants.

## T1 / A: bipartite adjacency

Coordinate-sum parity proves bipartiteness of Z³ and an even torus. If x,y are
neighbors, N(x),N(y) are disjoint: members of these sets have opposite colors.
Thus a single move loses all of the moving member's previous companions;
a newly found companion can still satisfy C_comp. The L=6 census checks1296
oriented bonds and6480 ordered neighbor pairs exactly, with no triangles or
surviving previous companions. This local lemma is independent of tick weights.

## T2 / B: the complete n<=6 centroid certificate

Fixed polycube counts at n=1..6 are `1,3,15,86,534,3481`.
For n=2..6, reachable translation classes number `3,15,86,990,11851`,
with `0,24,192,3372,52320` directed admissible moves. The dimer, straight
trimer, straight4 and square are frozen; bent trimer2, L1, T4, S2, skew2,
tripod6 count their available one-site moves. Occupation number stays n and
no reachable state has an isolated site. A connected group with n<=4 cannot
split by one move (components would each need≥2 and the moved site would
be isolated in a new separate component). At n=5 the complete census has336
splitting moves. The configuration
`{(0,0,0),(1,0,0),(2,0,0),(3,0,0),(3,1,0)}` has a2+3 split;
merges equal splits (336 at n5,4440 at n6). This is not preservation of
connectedness or original partners.

For a directed quotient edge `(S,x,y,c)` with `c=canon(S-{x}+{y})`, the **physical
increment** is `(y-x)/n`, not the difference of centroids of the separately
recentered shapes. Breadth-first rational potential assignment gives
`Phi(c)-Phi(S)=(y-x)/n`; checking every outgoing edge certifies zero residual
on24/192/3372/52320 edges for n3/4/5/6, across6/13/34/40 components.
The closure includes all successors and every reverse edge is admissible.
Along any actual path, increments telescope into Phi(final)-Phi(initial).
Within each finite component this bounds the centroid coordinate range by
`1/3,1/2,4/5,4/3` lattice units, respectively. Hence centered centroid variance
is bounded and its long-time variance/(6*ticks) limit is zero, for **this complete
n<=6 reachable domain**, for any law supported on these edges/stays.
This is a centroid bound, not a whole-group bounding box: a frozen straight
six-site group already spans5 sites. The special bent-trimer lab orbit has
four configurations in one fixed unit square. Arbitrary-n mobility remains open.

## T3 / C: rigid support and separately supplied weights

Under C_rig no one-site move is allowed for any of the104 connected groups
of sizes2,3,4. T1 gives the general obstruction for moving a member that
currently has a companion while preserving each old adjacency.
In the eight declared STRICT simultaneous cases, all admitted assignments
are translations/stay; free directions are `4,4,2,2,4,2,2,0` for
`dimer,straight trimer,bent trimer,square,straight4,L,T,tripod`.
This is a named finite census, not all groups.

For the ten declared PERMISSIVE isometry cases
`dimer,straight trimer,bent trimer,square,straight4,L,T,S,skew,tripod`,
there are160 labelled admissible assignments and70 pure translations/stays,
seven per case. Every actual image is congruent under the48 cubic isometries
and translations. The strengthened actual C3 verifies the complete named case
set, per-case counts, totals and congruence; deleting eight cases must fail.
No claim is made that every abstract rotation is feasible in a single tick.

Under the **six equally probable translation proposals with rejected stay**
protocol, opposite allowed directions cancel drift, and E|step|² equals
free-directions/6. Relative to free six-direction D1=1/6 per tick,
PERMISSIVE gives1 and STRICT gives2/3 for a dimer,1/3 for a bent trimer,
0 for a2x2x2 block. For a fixed shape, the allowed direction set is unchanged
by translations. A different normalization changes the result:
uniform all16 admissible labelled dimer isometries gives exact ratio5/8;
uniform seven translations including stay gives6/7; six nonstay translations
 gives1; stay-only gives0. For the uniform dimer-isometry law, reflection symmetry gives zero conditional centroid drift in each orientation; cubic covariance keeps the trace second moment5/8 in every orientation, so martingale increments give the same asymptotic variance rate. Uniform allowed nonstay STRICT translations also
gives1 when at least one exists. These are explicit probability-law witnesses,
not independent physical route eliminations. The support alone fixes none of them.

## T4 / D: fixed parity cosets and the N=2 union

On the cube, `n_v(y)=popcount(y intersect star(v)) mod2`. A fixed parity sector
specifies **every B_v**. The4096 patterns form128 sectors of32: the incidence
matrix has rank7, and its kernel (cycle space) has dimension12-8+1=5.
The32 preserving complement masks have weights `{0:1,4:6,6:16,8:9}` and are
exactly the XOR span of the six face cycles. These preserve every fixed coset,
not just vacuum. No single-edge complement preserves any fixed parity sector.
All24 adjacent two-edge complements leave vacuum and create two odd corners.

The separate union of all28 sectors having N=2 admits single complements
incident to exactly one odd corner:4 hops for adjacent odd corners and6
for distance2 or3. The additional formal complement of the edge joining
adjacent odd corners annihilates the pair into N=0, **outside this union**.
For the actual number-conserving hopping
`T_ij=(i/2)A_ij(B_i-B_j)`, that equal-parity annihilation complement has zero
amplitude. Formal complement masks are algebraic support operations, not
proof of dynamic availability. The nonzero hop flips one edge value and moves
one odd corner between fixed cosets; it does not translate a star of Records.
Every full bit pattern specifies all twelve edge values. Occupation, minus-bit
count, readout content and formed fine-site Records must not be identified.

## T5 / E: finite postselected pair and finite energetic comparison

KT removes22,572/129,280 nonadjacent configurations from23,220/130,816 on
L=6/8, leaving648/1536 adjacent configurations. Real staggered translation
gauge and exchange covariance justify lumping by relative axis; sampled
entrywise covariance is checked within1e-9. In each of the four (L,tau) cases
L=6,8 and tau=.5,1 the success mass is positive, so normalized ticks remain
adjacent. The original success masses round to .31 and .28 on L6; the
orientation chain is row stochastic and has uniform stationary law to1e-9.
Axis-change probabilities are `.475,.476` at tau=.5 and `.079,.072` at1.
These rows are finite computations, not physical instruments or arbitrary tau claims.

The Poisson equation actually used is
`(I-P)h=MU-m`, `pi*h=0`, `m=pi*MU`.
For centered additive proxy increments, the corrected increment
`d+h(next)-h(current)-m` is a martingale difference. Its stationary mean square
gives the asymptotic **proxy** variance rate; bounded h makes the endpoint
correction irrelevant to that limit. The irreducible sampled orientation
chains have a well-defined solution, whose actual equation and normalization
are checked. This is more than a sum of conditional variances, but it does
not remove the half-period physical-centre alias.
The original ratios are `.5016,.5075` at tau=.5 and `.1058,.1453` at1
(rounded-target checks1e-3). There is no universal half-speed theorem.
Wrap mass reaches1.5e-2 and drift1.0e-2 under the positive-tie convention;
the latter is not exactly zero. The L8,tau=.5 joint assignment weights are
one member shifts .540, rigid translation .239, same sites .218, nonrigid .002
(rounded-target acceptance2e-3, normalization1e-9).

The separately recomputed L6,tau=.5,g=32 **positive adjacent detuning**
comparison has adjacency `.978,.957,.896,.804,.648,.424` at
1,2,5,10,20,40 ticks, versus the uniform-configuration reference .0279.
It leaks in this finite sample. It proves no all-strength/all-energy
impossibility, transience, arbitrary-time convergence or full separated support.
Global support conditioning can exclude separation by construction; this
logical fact does not derive the weights, success mechanism or physical law.

## Executable claim block and unresolved boundaries

```text
T1: bipartite local adjacency lemma, independently of probabilities.
T2: complete connected-start n<=6 closure; rational centroid certificate;
    no singleton does not imply connectedness or permanent companions.
T3: complete named simultaneous/isometry supports; transport ratios only under named laws.
T4: fixed parity cosets preserved by cycles; single hops move within the N=2 union.
T5: finite KT normalized kernels and centered modulo-sum Poisson proxy;
    finite g=32 leakage contrast only.
framework_formation_derived: false
formal_audit: deferred_by_owner
```

All original21 check identifiers and raw numerical outputs remain recoverable
in the original packet; genuine corrected caches bind current notes/runner/memo.
Exact integer/Fraction statements and finite floating comparisons are separated.
Transcendental propagation does not rule out special rational values; displayed
digits are not interval-certified error bounds. There is no sampling here.

Manual N1–N8 boundary: actual tested alternatives include companion one-site,
rigid one-site, simultaneous translations, isometry assignments and global
postselection, plus a finite energetic comparator. These are different targets
or protocols, not five failed routes to one universal no-go. No independence
count is established for locality, permanence, supplied probabilities and
formation. The n<=6 certificate is positive finite mathematics; larger groups,
other supports/instruments, actual physical lifts and Record formation remain
open. No procedural quota or structured no-go PASS is invented. Any unmet quota
is left pending, separately from the conditional proofs. The old claims that all
energy costs fail or every companion group has a small whole-group cage are
withdrawn. Historical marker/source campaigns are context only and unaccepted.
