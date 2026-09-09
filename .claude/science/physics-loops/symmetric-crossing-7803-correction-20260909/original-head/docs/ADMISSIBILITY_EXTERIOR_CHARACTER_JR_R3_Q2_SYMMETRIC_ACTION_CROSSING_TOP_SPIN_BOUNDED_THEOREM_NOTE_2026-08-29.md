---
claim_id: admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SYMMETRIC_ACTION_CROSSING_TOP_SPIN_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
title: Exact symmetric action/crossing highest-spin coefficients on the r=3, q=2 physical-Q local carrier
claim_scope: "For each of the three fine-plaquette placements in the supplied r=3, q=2 two-cell original-link geometry, derive the unique highest-spin coefficient of the complete two-order local response B C_c+C B after transport to the physical residual packet. For the two placements disjoint from the neighboring eight-link loop, the one-layer coefficient is r_1^8(r_n^4+r_(n+1)^4). For the boundary placement sharing h3, the top-coupled coefficient is r_1^7(r_n^3 r_(n+1)+r_(n+1)^3 r_(n+2)). Both terms strictly reinforce for the supplied finite-positive multiplier family. The corresponding pure-placement all-layer products are exact formal selected-packet coefficients. Mixed-placement words, powers of the actual coarse-to-residual response, the full action exponential, invariant closure, and global minimal memory are not classified."
depends_on:
  - admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_no_go_note_2026-08-29
  - admissibility_exterior_character_jr_r3_q2_adjacent_product_cubic_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_no_go_note_2026-08-29: "supplies the selected ordered disjoint top branch whose cancellation in the complete two-order response is tested here"
  admissibility_exterior_character_jr_r3_q2_adjacent_product_cubic_response_bounded_theorem_note_2026-08-29: "supplies the three plaquette loops, neighboring merged loop, physical proper-subset conditional-Haar statement, and original-link geometry"
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "supplies the exact B C_c+C B response, physical J3/Q, C J3=J3 C_c, and [C,Q]=0"
  admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28: "supplies the normalized O(3) central multipliers and their strict positivity at finite positive exterior coupling"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
actual_current_surface_status: conditional-support
conditional_surface_status: "exact complete-two-order highest-spin reinforcement on each fixed local action placement of the supplied physical-J3/Q stack"
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_no_go_note_2026-08-29
target_blocker_text: "test the complete symmetric BC_c+CB branch and multiple action placements for cancellation or reinforcement of the unique top-spin branch"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
proposal_allowed: false
proposal_allowed_reason: "The exact coefficient theorem imports the supplied action, crossing, physical J3/Q, and open stacked parent results; it does not classify mixed placement words or a physical invariant carrier."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
axiom_or_primitive_edits: 0
runner: scripts/admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_independent_2026_08_29.py
date: 2026-08-29
claim_type_reason: "exact O(3) fusion, conditional Haar, original-link representation census, and the parent plus-sign identity determine the unique highest-spin coefficient on three fixed placements"
next_trace_action: "Enumerate mixed-placement top channels of the summed action and determine which remain distinct after physical conditional Haar; keep the response-domain and full-exponential boundaries explicit."
---

# The two action/crossing orders reinforce the local highest-spin branch

**Status:** `conditional-support`

**Type:** `bounded_theorem`

**Actual current surface:** `conditional-support`. The coefficient calculation
is exact on the supplied action/crossing/physical-`J_3/Q` stack. Its parent
results are open dependencies, and only the independent audit lane may assign
an effective status.

## Exact target

**Target claim.** For each fixed fine-plaquette placement in the supplied
`r=3, q=2` two-cell geometry, compute the unique highest-spin coefficient of
both terms in the parent response `B C_c+C B`, with physical conditional-Haar
`Q` and one central multiplier per original link representation, and decide
whether those two coefficients cancel or add.

The answer is addition. On both disjoint placements the coefficient from spin
`n` to spin `n+1` is

```text
s_n^D=r_1^8(r_n^4+r_(n+1)^4).                     (1)
```

On the boundary placement sharing the rung `h3` with the neighboring merged
loop, the coupled coefficient is

```text
s_n^S=r_1^7[r_n^3 r_(n+1)+r_(n+1)^3 r_(n+2)].    (2)
```

The normalized multipliers supplied for every finite positive exterior
coupling are strictly positive. Therefore the two orders reinforce at every
finite layer on all three fixed placements. The result does not widen the
ordered Block247 carrier conclusion beyond the domains proved below.

## Obligation graph

| Obligation | Disposition | Evidence |
|---|---|---|
| identify the two typed operator orders and their relative sign | imported exactly | parent equation `(34b)` |
| transport the coarse crossing without changing operator order | imported exactly | `C J_3=J_3 C_c` and `[C,Q]=0` |
| apply physical `Q`, rather than a static tensor projector | proved on the selected top channel from the parent proper-subset Haar result and exclusive-path orthogonality | equations (5)--(6) below |
| reconstruct the original-link multiplicities | proved here | equations (7)--(10) and both runners |
| prove top fusion multiplicity one | proved here | exact `O(3)` character product and independent maximal-torus extraction |
| decide the relative sign of the two top paths | proved here | equations (11)--(14) |
| exclude cancellation on the supplied multiplier domain | proved here | strict positivity in equation (15) |
| classify mixed plaquette words and the full physical response carrier | not part of this target | strongest missing lemma stated below |

The graph is acyclic: the top coefficient is derived from the parent operator
identity, the independently reconstructed link labels, and ordinary compact-
group representation algebra. No step assumes the target coefficient.

## Imported stack and counterfactuals

The calculation imports, without editing:

1. the exact finite-step response
   `L_epsilon=-(epsilon/2)(B C_c,epsilon+C_epsilon B)` and the typed maps from
   the [parent semigroup-defect note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md);
2. the three fine plaquettes, the neighboring merged loop, and the proper-
   subset conditional-Haar mechanism from the
   [adjacent-product note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_ADJACENT_PRODUCT_CUBIC_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md);
3. the selected defining-vector tower and its parity convention from the
   [ordered action/crossing note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_PHYSICAL_Q_ACTION_CROSSING_TOWER_NO_GO_NOTE_2026-08-29.md);
4. the normalized multiplier family and strict finite-positive-coupling
   boundary from the
   [time-refinement note](ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md); and
5. the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) as a boundary on what is
   framework-native.

| Imported item | Role | Provenance | If changed |
|---|---|---|---|
| plus sign in `B C_c+C B` | fixes interference of the two orders | parent equation `(34b)` | a relative minus sign would define a different response and cancels at identity crossing |
| physical `J_3/Q` | removes the conditional coarse component | parent construction | another projector need not preserve the top branch |
| linkwise central `C` | assigns one multiplier to each original-link irrep | supplied time-refinement family | a noncentral or non-linkwise map invalidates the census formulas |
| finite-positive multipliers | gives strict reinforcement | supplied positive character expansion | zeros or signed multipliers reach the cancellation loci in equations (16)--(17) |
| defining-vector action component | supplies spin-one fusion | parent action Fourier component | a different action irrep changes the top increment and coefficient |
| three local action amplitudes | multiply placement contributions | parent `V_f` | their numerical specialization is not needed for the normalized coefficient |

No observed value, fit, sample rank, literature constant, new axiom, or proposed
primitive enters the proof. No axiom or approved primitive is edited.

## Typed transport of the symmetric response

Let `R=I-Q`, let `M_i` multiply by the defining-vector character on plaquette
`p_i`, and put

```text
A_i=R M_i.                                          (3)
```

If `alpha_i` denotes the coefficient of that character in the supplied local
action, then the corresponding parent term is

```text
B_i=alpha_i A_i J_3.
```

The parent relations `C J_3=J_3 C_c` and `[C,Q]=0` give, with operators acting
right to left,

```text
B_i C_c+C B_i
 =alpha_i(A_i C+C A_i)J_3.                         (4)
```

Thus the complete two-order fine-packet core is
`S_i=A_i C+C A_i`. The common physical scalar is
`-epsilon alpha_i/2`; it multiplies both order contributions and cannot change
their relative sign. Equation (4) is a transport identity on `Ran J_3`, not an
assertion that the actual coarse-to-residual map can be composed with itself.

## Physical conditional Haar

Write

```text
rho_n=(n,(-1)^n),       V=rho_1.
```

Below, `r_n` abbreviates the supplied multiplier `r_(n,(-1)^n)`. For
positive spin the supplied exterior family is parity-independent; all labels
are nevertheless retained in the representation argument. Reversing a link
orientation dualizes a real `O(3)` irrep and does not change its multiplier.

At fixed coarse deltas, each individual first-cell plaquette variable has Haar
marginal under physical `J_3`. Hence for every nontrivial `rho_n`,

```text
E[chi_(rho_n)(p_i) | coarse]=0.                    (5)
```

The coarse first-cell loop is
`C0=(u0,u1,u2,h3,v2^-1,v1^-1,v0^-1,h0^-1)` and contains neither internal rung
`h1` nor `h2`. Every fixed plaquette top network carries `rho_n` on at least
one of those internal rungs: `p0` carries it on `h1`, `p1` on `h1,h2`, and
`p2` on `h2`. This linkwise representation is nontrivial while every
`Ran J_3` coarse function is trivial there. Exact Peter--Weyl orthogonality
therefore gives zero coarse projection channel by channel, including for the
`p2/C1` shared-rung decomposition. After multiplication by `V`, the top output
is `rho_(n+1)` on the same internal rung, so

```text
A_i : top(rho_n) -> top(rho_(n+1)) + lower spins,  (6)
```

with unit top coefficient. Physical `Q` here is conditional Haar and is not a static cup projector.

The scalar subtraction affects lower branches when the trivial irrep occurs;
it never removes the displayed positive-spin top output. This conclusion uses
the actual conditional-Haar projector and the supplied proper-subset geometry,
not a static cup-image analogy.

## Original-link reconstruction

The three fine plaquettes and the neighboring merged loop are

```text
p_i=(u_i,h_(i+1),v_i^-1,h_i^-1),                  (7)
C1 =(u_3,u_4,u_5,h_6,v_5^-1,v_4^-1,v_3^-1,h_3^-1). (8)
```

Therefore `p0` and `p1` are disjoint from `C1`. A spin-`n` plaquette character
times the `C1` vector character has four links labelled `rho_n` and eight
links labelled `V`, so its crossing eigenvalue is

```text
d_n^D=r_n^4 r_1^8.                                 (9)
```

The boundary plaquette `p2` shares exactly `h3` with opposite orientation.
On the unique highest-coupled channel, the three exclusive `p2` links carry
`rho_n`, the seven exclusive `C1` links carry `V`, and `h3` carries
`rho_(n+1)`. Thus

```text
d_n^S=r_n^3 r_1^7 r_(n+1).                        (10)
```

The shared rung is counted once in equation (10), in its coupled
representation. Treating the two loops as independent would incorrectly give
`r_n^4 r_1^8`; multiplying that by an extra shared factor would double count
the same original link.

The independent checker derives (10) from oriented links rather than from the
displayed powers. On a common maximal torus, choose weight `n` on `p2` and
weight `-1` on the oppositely oriented `C1` loop. The shared exponent is then
`n+1`, while every exclusive exponent saturates the labels above. The
conjugate monomial gives the opposite exponents. Both have coefficient one,
and multiplying by the action vector produces the unique shared exponent
`n+2`. This also establishes the unit top-fusion coefficient without importing
the primary formula.

## Both operator orders

Let `g_n^i` denote the selected top network for placement `i`; on a disjoint
placement it is the product character itself, while on `p2` it is the top
shared-rung component. Normalize the latter so that its two conjugate
saturated maximal-torus monomials have coefficient one, matching the character-
product normalization used above. With this convention the unique top fusion
coefficient is exactly one. Centrality gives

```text
C g_n^i=d_n^i g_n^i.                               (11)
```

The crossing-first contribution is

```text
A_i C g_n^i=d_n^i g_(n+1)^i+lower,                 (12)
```

and the action-first contribution is

```text
C A_i g_n^i=d_(n+1)^i g_(n+1)^i+lower.            (13)
```

They land on the same uniquely labelled top network. Because equation (4)
contains a plus sign,

```text
S_i g_n^i=(d_n^i+d_(n+1)^i)g_(n+1)^i+lower.       (14)
```

Substituting (9) and (10) gives equations (1) and (2). For every multiplier in
the supplied finite-positive family,

```text
s_n^D>0,       s_n^S>0.                            (15)
```

Hence the unique top branch used by the ordered calculation survives the
complete two-order local response on each fixed placement. It is reinforced,
not canceled.

## Exact cancellation loci and endpoints

The calculation also identifies where the conclusion stops. For real
multipliers and `r_1` nonzero,

```text
s_n^D=0  iff  r_n=r_(n+1)=0.                       (16)
```

The shared placement has the wider algebraic locus

```text
s_n^S=0  iff
r_(n+1)[r_n^3+r_(n+1)^2 r_(n+2)]=0.               (17)
```

Thus signed nonphysical multipliers can cancel a shared-placement layer. For
example, `r_n=r_(n+1)=1` and `r_(n+2)=-1` makes (17) vanish exactly. The
signed cancellation control lies outside the supplied positive multiplier domain.
At identity crossing every `d_n` is one and each symmetric factor is exactly
two. At the Haar endpoint the relevant nontrivial multipliers vanish, and at
`r_1=0` the vector spectator kills all three placement factors.

These are parameter boundaries of the coefficient formula. They are not
evidence for cancellation at a finite positive supplied crossing.

## Pure-placement all-layer coefficient

For the normalized selected fine-packet extension, start with `g_1^i` and
apply `S_i` repeatedly. The spin-`N` coefficient is

```text
T_N^D=product_(j=1)^(N-1) r_1^8(r_j^4+r_(j+1)^4),             (18)

T_N^S=product_(j=1)^(N-1)
      r_1^7[r_j^3 r_(j+1)+r_(j+1)^3 r_(j+2)].                 (19)
```

Restoring the parent scalar for a pure placement multiplies (18) or (19) by
`(-epsilon alpha_i/2)^(N-1)`. The induction is exact because every action
raises spin by at most one and the displayed top summand has multiplicity one.
No lower branch can reach spin `N` at layer `N`.

If the local action is kept formal as `sum_i alpha_i M_i`, equations (18)--(19)
are the coefficients of the pure monomials `alpha_i^(N-1)`. That statement
does not enumerate mixed monomials or assert their numerical behavior after a
particular amplitude specialization.

## Scope locks

The exact result is the complete two-order coefficient on each fixed local
placement and its pure-placement selected extension.

Here “complete two-order” means that both parent orders are included for the
selected defining-vector action component. It does not mean that every Fourier
irrep in the full supplied action has been iterated.

Mixed-placement histories are not evaluated by this coefficient theorem.

The full action exponential is not evaluated by this coefficient theorem.

No invariant-closure statement is proposed.

No global minimal-memory statement is proposed.

No statement about arbitrary `r/q`, physical time evolution, continuum
dynamics, gravity, or TOE closure is proposed. The selected formal iteration
is not identified with powers of the actual coarse-to-residual `L_epsilon`.

## Strongest missing lemma and next falsifier

The strongest missing lemma is an exact recoupling classification for every
mixed word in `S=sum_i alpha_i S_i`, with physical `Q` applied at each typed
domain transition. Such a classification must determine whether histories
from different placements enter distinct spin-network sectors or the same
sector with signed recoupling coefficients. The next falsifier is the shortest
mixed word containing both a disjoint placement and `p2`; compute all channels
that reach its maximum external labels and compare their exact coefficients at
the supplied positive multipliers.

## Prior-art and approach record

The prior-art sweep was run after fetching `origin/main` at
`3cc632921c36aa90266c5c62e56816577ce59a0a`. It searched note titles and bodies
for combinations of `highest-spin`, `top-spin`, `symmetric`, `both orders`,
`action crossing`, `BC_c`, and cancellation language, and inspected the audit
derivation obligations. No matched hit on `origin/main` derived equations
(1)--(2) or classified the shared-rung placement. The open stacked parents are
dependencies, not effective retained authority.

The attempted approaches were:

1. **Disjoint character recurrence:** exact and used in the packet; it
   shows directly that the two ordered coefficients are `d_n^D` and
   `d_(n+1)^D`.
2. **Independent original-link census:** exact and retained; it reconstructs
   all loops and rejects altered `4/8` powers.
3. **Shared loop treated as disjoint:** rejected by the literal `h3`
   intersection and the coupled label `rho_(n+1)`.
4. **Shared rung counted twice:** rejected because central crossing acts once
   per original link; the torus monomial has one shared exponent.
5. **Maximal-torus highest monomial:** exact and retained; it independently
   establishes shared multiplicities `3/7/1` and top multiplicity one.
6. **Signed hostile cancellation:** exact as a counterfactual; it identifies
   the boundary (17) but lies outside the supplied positive domain.
7. **Sample-rank continuation:** not used; the universal coefficient follows
   from triangular representation labels rather than finite sampled rank.

## Verification and hostile falsifiers

The primary runner uses exact rational arithmetic. It constructs the full
disjoint `A C+C A` coefficient tables in two different ways, checks both
positive and signed samples, compares every placement to the independent
link-census oracle, tests identity/Haar/spectator-zero endpoints, and records
the exact signed shared-rung cancellation locus. The independent checker
imports no primary module and derives its labels from oriented loop incidence
and maximal-torus characters.

The mutation suite rejects: deleting either order; replacing the plus sign by
a minus sign; changing a disjoint plaquette power from four to three; changing
the spectator power from eight to seven; treating the shared placement as
disjoint; counting `h3` twice; changing the top fusion coefficient; replacing
physical `Q` by a static cup; and extending the claim to mixed placements, the
full exponential, invariant closure, global memory, the signed control as a
physical point, or an axiom edit.

The five-resolution lines in cached stdout are supplied as a conservative
rhetoric audit. This note advances a bounded positive coefficient theorem; it
does not propose a `no_go`, `stretch_attempt_negative`, or lattice-wide
negative result, so the N1--N8 negative-claim gate is not invoked.

## Review record

This result answers the Block247 symmetric-order falsifier without changing
the earlier ordered theorem. It replaces the provisional possibility of
two-order cancellation, on each fixed placement, with the exact reinforcement
formulas (1)--(2). The scope ends at fixed-placement top coefficients
and formal pure-placement monomials. The mixed-placement recoupling lemma and
the domain-correct physical carrier remain subsequent work. No audit verdict,
merge, PR creation, push, axiom edit, or primitive edit is part of this packet.
