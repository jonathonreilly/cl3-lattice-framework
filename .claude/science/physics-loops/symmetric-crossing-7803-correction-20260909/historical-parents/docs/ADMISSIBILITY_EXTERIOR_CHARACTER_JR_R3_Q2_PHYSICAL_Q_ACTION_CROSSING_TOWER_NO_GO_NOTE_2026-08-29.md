---
claim_id: admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_no_go_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_PHYSICAL_Q_ACTION_CROSSING_TOWER_NO_GO_NOTE_2026-08-29.md
claim_type: no_go
title: Exact unbounded selected physical-Q action/crossing tower on the r=3, q=2 fiber
claim_scope: "On the selected disjoint p0/C1 fiber of the supplied r=3, q=2 original-link ladder, iterate exactly one defining-vector action insertion, physical conditional-Haar subtraction, and then the supplied central crossing. Derive the complete spin-by-spin recurrence, prove that layer n has a unique nonzero spin-n top coefficient for every finite positive exterior crossing, and therefore prove that no finite-dimensional linear invariant carrier containing this selected orbit can close under that ordered operator. Separately prove that crossing alone preserves Peter--Weyl support and obeys a finite spectral recurrence on every fixed finite packet. This is a selected local linear-carrier no-go conditional on the supplied action, crossing, J3/Q, nonzero multiplier family, and operator order; it is not the full symmetric step, the full action exponential, a global minimal-memory theorem, physical dynamics, gravity, or TOE closure."
depends_on:
  - admissibility_exterior_character_jr_r3_q2_second_crossing_action_leakage_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r3_q2_second_crossing_action_leakage_bounded_theorem_note_2026-08-29: "supplies the selected p0/C1 seed, the action-then-physical-Q-then-crossing branch, and the distinction between temporal multiplicity leakage and new Peter--Weyl content"
  admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28: "supplies the normalized O(3) central multiplier family and strict nonzero finite-positive-coupling boundary"
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "supplies physical J3/Q, linkwise central crossing, representation-label preservation, and [C,Q]=0"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
actual_current_surface_status: conditional-support
conditional_surface_status: "exact selected unbounded linear action/crossing tower on the supplied r=3, q=2 physical-J3/Q stack"
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: admissibility_exterior_character_jr_r3_q2_second_crossing_action_leakage_bounded_theorem_note_2026-08-29
target_blocker_text: "construct the wider crossing/action closure tower or a finite recurrence, preserving physical Q and the distinction between multiplicity leakage and new Peter--Weyl content"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
proposal_allowed: false
proposal_allowed_reason: "The exact no-go is conditional on a supplied selected operator branch and open stacked dependencies; it does not classify the full symmetric action step, all action placements, all coarse words, or global minimal memory."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
axiom_or_primitive_edits: 0
runner: scripts/admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_independent_2026_08_29.py
date: 2026-08-29
claim_type_reason: "the physical conditional-Haar subtraction, O(3) fusion recurrence, central-crossing eigenvalues, universal top-spin induction, and fixed-packet crossing recurrence give an exact negative result for one explicitly ordered selected linear carrier"
next_trace_action: "Test the complete symmetric BC_c+CB branch and multiple action placements for cancellation or reinforce the selected no-go into a full action-kernel invariant-carrier theorem; keep nonlinear or indexed recurrence memory and global minimal memory open."
---

# The selected physical-`Q` action/crossing tower has no finite-dimensional linear closure

**Type:** `no_go`

**Actual current surface:** `conditional-support`. The theorem is exact on the
supplied action, crossing, and physical-`J_3/Q` stack. The crossing and action
are not derived from the minimal axioms, and the open stacked dependencies are
not reclassified here. Only the independent audit lane may set effective
status.

## Result in plain language

Block246 found one new even-spin direction after adding a defining-vector
character and applying physical `Q`. That leakage does not stop at spin two.
On the same selected fine plaquette, every next action layer creates a new top
spin. Physical `Q` removes only the trivial character. The supplied central
crossing rescales the surviving irreps but does not change their labels. At
every finite positive exterior crossing its multipliers are nonzero, so the
new top spin survives.

This gives an exact unbounded tower on one selected local fiber. No
finite-dimensional linear invariant carrier containing that orbit can close
under the ordered action/`Q`/crossing operator. The statement is narrower than
a global memory theorem. A nonlinear rule, an indexed recurrence, a quotient
that does not contain this selected orbit, or cancellation in the complete
symmetric action response is not excluded.

The same calculation also separates the two Block246 mechanisms. Crossing
alone keeps a fixed Peter--Weyl packet fixed and obeys a finite spectral
recurrence. It may resolve temporal multiplicities inside that packet, but
temporal multiplicity leakage is not new Peter--Weyl content. The unbounded
labels come from repeated defining-vector action after physical `Q`.

## Imported stack and exact operator order

The construction imports without modification:

1. the [Block246 selected action residual and crossing branch](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SECOND_CROSSING_ACTION_LEAKAGE_BOUNDED_THEOREM_NOTE_2026-08-29.md);
2. the supplied physical conditional-Haar isometry `J_3`, `Q=J_3J_3^*`,
   linkwise central crossing, and `[C,Q]=0` from the
   [parent semigroup-defect note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md);
3. the linkwise central crossing with normalized `O(3)` multipliers
   `r_(ell,p)`;
4. the defining-vector exterior character `chi_V`; and
5. the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) as a framework
   boundary only.

No axiom or approved primitive is edited. The load-bearing new work is the
all-layer recurrence and induction below.

Operator order matters. Put

```text
A=(I-Q) M_(chi_V(p0)),
K=C A=C(I-Q)M_(chi_V(p0)).                           (1)
```

This is exactly the Block246 branch: add the action character, perform the
physical conditional-Haar subtraction, and then apply the supplied central
crossing. It is not replaced by `AC`, and it is not called the complete
symmetric `BC_c+CB` response from the parent finite-step identity. The runner
checks that `CA` and `AC` differ at a generic exact rational sample.

## Physical conditional Haar on the selected fiber

Let `p0` be the first fine plaquette of the first blocking cell and let `C1`
be the disjoint merged defining-vector loop over plaquettes three through
five. The latter has eight original links. At fixed coarse deltas, take the
two independent first-cell fiber variables Haar and solve the third from
`delta0`. The `C1` character is a spectator. Define

```text
e_(ell,p)=chi_(ell,p)(p0) chi_V(C1),                 (2)
```

where `ell` is spin and `p` is inversion parity. Exact character
orthogonality gives

```text
Q e_(ell,p)=1_((ell,p)=(0,+)) chi_V(C1).            (3)
```

Thus physical `(I-Q)` removes exactly the trivial `p0` character. In
particular, the odd spin-zero determinant character `(0,-)` is not removed.
Equation (3) is physical conditional-Haar `Q`, not a static cup projector.

The Block246 seed and first new layer are

```text
f_1=e_(1,-),
A f_1=e_(1,+)+e_(2,+).                              (4)
```

Equation (4) is the earlier residual
`[chi_V(p0)^2-1]chi_V(C1)`.

## Exact action recurrence

Multiplication by the defining-vector character obeys the `O(3)` rule

```text
(1,-) tensor (0,p)=(1,-p),
(1,-) tensor (ell,p)
  =(ell-1,-p)+(ell,-p)+(ell+1,-p),  ell>=1.          (5)
```

Every layer has one inversion parity `p_n=(-1)^n`. Write the coefficients
before layer `n+1` as `a_(n,ell)`. Define the pre-crossing action coefficients

```text
b_(n+1,0)=a_(n,1),
b_(n+1,ell)=a_(n,ell-1)+a_(n,ell)+a_(n,ell+1),
                                                     ell>=1,              (6)
```

with absent coefficients zero. When `p_(n+1)=+`, physical `Q` sets
`b_(n+1,0)=0`; when `p_(n+1)=-`, that coefficient is the determinant channel
and remains.

The first four layers at the identity crossing are therefore

```text
f_1 = e_(1,-),
f_2 = e_(1,+)+e_(2,+),
f_3 = e_(0,-)+2e_(1,-)+2e_(2,-)+e_(3,-),
f_4 = 5e_(1,+)+5e_(2,+)+3e_(3,+)+e_(4,+).          (7)
```

The third line is an operator-order control. If physical `Q` were delayed
until after both new action insertions, the result would instead be the
one-shot residual of `chi_V^3`, which differs from `f_3` by `e_(1,-)`.

## Exact supplied crossing recurrence

On the basis (2), original-link central convolution is diagonal. The four
`p0` edges carry `(ell,p)`, while the eight disjoint `C1` edges carry the
defining-vector irrep. Hence

```text
C e_(ell,p)=c_(ell,p)e_(ell,p),
c_(ell,p)=r_(ell,p)^4 r_V^8.                        (8)
```

For `ell=0,p=-`, `r_(0,-)=r_det`. The trivial `p0` value would be one, but
that component is removed by (3). For `ell>=1`, the supplied exterior family
has parity-independent multipliers. The parent exact character expansion
proves that all these multipliers are strictly nonzero at every finite
positive exterior coupling. Therefore the ordered recurrence is

```text
a_(n+1,ell)=c_(ell,p_(n+1)) b_(n+1,ell).            (9)
```

Equations (3), (5), (6), (8), and (9) reconstruct every layer without a cup
projection or sampled Gram-rank inference.

## Unbounded top-spin theorem

**Theorem.** At every layer `n>=1`, the coefficient of `e_(n,(-1)^n)` is

```text
a_(n,n)
 = r_V^[8(n-1)] product_(j=2)^n r_(j,(-1)^j)^4.    (10)
```

It is nonzero whenever the displayed supplied multipliers are nonzero.

**Proof.** The seed has `a_(1,1)=1`. Suppose layer `n` has maximum spin `n`
with the coefficient in (10). In (5), only its top summand can produce spin
`n+1`, and that summand has Clebsch--Gordan multiplicity one. Physical `Q`
acts only on `(0,+)` and cannot remove it. Equation (8) then multiplies the
new top summand by `r_(n+1,(-1)^(n+1))^4 r_V^8`. This gives (10) at layer
`n+1`. No spin larger than `n+1` can occur by (5). Induction proves the
claim. QED.

The top-spin labels in successive layers are distinct. For every `N`, the
coefficient matrix of `f_1,...,f_N` contains a triangular `N by N` minor with
diagonal entries (10). Its determinant is nonzero. Thus every finite prefix
has rank `N`, and no finite-dimensional linear subspace containing the seed
can be invariant under `K`.

This is a universal conditional theorem, not a sampled generic-rank claim.
Sample-wise Block246 ranks are not used as universal generic ranks. The exact
rational and finite-field tables in the runner only hostile-test the
implementation of (6)--(10).

## Crossing-only finite recurrence and invariant decomposition

The action conclusion does not apply to crossing by itself. Let `S` be any
fixed finite Peter--Weyl support and let `Lambda_S` be the distinct values of
`c_(ell,p)` on it. Equation (8) gives the exact annihilating polynomial

```text
P_S(C)=product_(lambda in Lambda_S)(C-lambda I)=0
                                                     on span S.           (11)
```

Consequently every crossing-only orbit on `S` obeys a finite recurrence of
order at most `|S|`, and crossing creates no new Peter--Weyl irrep. On a
fixed original-link tensor packet, partial central selections can resolve a
larger multiplicity algebra, as Block246 observed, but that algebra is still
inside the finite tensor product. The checked quotient dimension 43 remains
a sample-wise lower bound for the selected Block245 union, not a count of new
irreps and not a universal generic equality.

Equations (10)--(11) are the requested invariant separation:

| mechanism | Peter--Weyl labels | invariant conclusion |
|---|---|---|
| crossing on fixed finite support | unchanged | finite spectral recurrence |
| Block246 partial-crossing histories | fixed tensor-product labels, enlarged multiplicities | selected rank-29 span not invariant; exact full multiplicity closure still open |
| successive defining-vector action, physical `Q`, then crossing | new top spin at every layer | no finite-dimensional selected linear invariant carrier |

## Endpoint and hostile controls

- **Identity crossing.** Setting every multiplier to one gives (7) and leaves
  the top coefficient equal to one. The action/`Q` tower is still unbounded.
- **Haar endpoint.** Every nontrivial central multiplier vanishes. The first
  crossed residual and every descendant vanish. This singular endpoint is not
  used to claim nonclosure.
- **`t_V=0` with higher spins live.** The spectator factor `r_V^8` in (8)
  kills the whole selected tower. Higher `p0` spins cannot revive a killed
  `C1` vector rail.
- **Order reversal.** `CA f_1` has spin-one and spin-two coefficients
  `c_(1,+),c_(2,+)`, while `AC f_1` gives the same pre-crossing coefficient
  to both. They differ generically.
- **Identity action.** Replacing multiplication by `chi_V` with the identity
  cannot raise the maximum spin and fails the layer-two certificate.
- **Held-out arithmetic.** Two positive rational samples, one unrelated
  signed sample, three prime fields, and held-out `F_10007` reproduce full
  layer rank through layer eight. These checks verify code, not theorem
  quantifiers.
- **Independent implementation.** The companion imports no primary code. It
  multiplies Laurent characters on the `SO(3)` maximal torus, greedily
  decomposes them, tracks inversion parity separately, removes only the
  physical trivial character, and reproduces the recurrence and order
  control.

## Claim boundaries

Proved on the declared conditional stack:

- the exact all-layer recurrence for the selected `p0/C1` fiber;
- a genuinely new Peter--Weyl spin at every nonzero finite action/crossing
  layer;
- unbounded dimension of the selected linear Krylov carrier;
- a finite spectral recurrence for crossing alone on fixed finite support;
- the identity, Haar, `t_V=0`, operator-order, delayed-`Q`, held-out-field,
  and independent-reconstruction controls.

Not proved:

- invariance or non-invariance of the complete symmetric `BC_c+CB` response;
- absence of cancellations after summing all action placements or the full
  action exponential;
- an exact universal rank for the Block246 twice-crossed union;
- a globally minimal history memory, nonlinear memory, indexed recurrence,
  or automaton-state lower bound;
- arbitrary blocking width or arbitrary coarse word;
- physical time, continuum or Lorentzian dynamics, metric/source structure,
  gravity, phenomenology, or a theory of everything.

The local/selected carrier result constrains any finite-dimensional linear
global carrier that is required to contain this exact selected orbit. Global
minimal memory remains open because a different representation of the full
kernel need not be that carrier.

## No-Go Discipline Gate

The negative sentence is deliberately narrow: under the ordered operator (1)
and nonzero supplied finite-step multipliers, no finite-dimensional linear
invariant carrier containing the selected `p0/C1` seed exists. It does not say
that every full response, memory representation, or action convention is
unbounded.

### N1 — alternative attacks

The following five normalized attack families were attempted. Each attacks a
different load-bearing part of the selected theorem rather than counting a
second implementation as a new route.

1. **Fusion-cancellation attack — `ATTEMPTED`.** This route asks whether two
   parents or a lower-spin contribution can cancel the new spin-`n` term. It
   fails because the exact `O(3)` fusion rule gives that top term a unique
   multiplicity-one parent, as proved in [equations (5)--(10) of this
   note](#unbounded-top-spin-theorem).
2. **Original-link power-census attack — `ATTEMPTED`.** This route asks whether
   overlap or miscounting changes the four `p0` and eight disjoint `C1` powers.
   It fails under the explicit disjoint sets reconstructed by the
   [independent census checker](../scripts/admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_independent_2026_08_29.py),
   which is compared coefficient-by-coefficient with the [primary
   recurrence](../scripts/admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_2026_08_29.py).
3. **Physical-`Q` removal attack — `ATTEMPTED`.** This route asks whether
   conditional Haar can remove the determinant channel or a positive-spin top
   term. It fails because the supplied fixed-`delta0` conditional-Haar theorem
   removes only `(0,+)`, as stated in the [parent conditional-Haar
   reduction](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md),
   and the exact identity layers retain `(0,-)`.
4. **Fixed-support recurrence attack — `ATTEMPTED`.** This route asks whether
   the crossing-only annihilating polynomial can close the full selected
   orbit. It fails because that polynomial acts on a fixed finite
   Peter--Weyl packet, whereas defining-vector multiplication raises the
   maximum spin at every layer; the positive crossing-only statement is
   equation (11), not a recurrence for `K`.
5. **Singular-endpoint attack — `ATTEMPTED`.** This route sets the supplied
   crossing to Haar or kills the disjoint spectator multiplier. It does close
   the tower, and the [primary endpoint checks](../scripts/admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_2026_08_29.py)
   reproduce that collapse. It fails as a counterexample to the stated theorem
   because the theorem explicitly assumes nonzero finite-positive multipliers;
   the singular endpoints remain named boundary cases rather than being hidden.

The full symmetric response and alternative global memory representations are
not among the five closed attacks, and no broader no-go is asserted.

### N2 — independence of supplied conditions

The conditional result has three supplied conditions: `W1`, the physical
`J_3/Q` fiber and selected seed; `W2`, the defining-vector action and ordered
branch; and `W3`, the central multiplier family with nonzero finite-step
channels.

| pair | closing first closes second? | closing second closes first? | independent here? |
|---|---|---|---|
| `W1,W2` | no | no | yes |
| `W1,W3` | no | no | yes |
| `W2,W3` | no | no | yes |

The nonzero-multiplier qualification is part of `W3`, not a fourth wall.

### N3 — hidden-condition scan

“Selected fiber,” “ordered branch,” “physical conditional-Haar,” and
“nonzero finite-step multipliers” state the load-bearing conditions. No
observed value, fitted selector, empirical constant, static cup, background
clock, or unregistered primitive enters the proof. The rational samples are
code controls only.

### N4 — residual matching

| cited surface | residual there | residual here | match? |
|---|---|---|---:|
| [Block246 action leakage](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SECOND_CROSSING_ACTION_LEAKAGE_BOUNDED_THEOREM_NOTE_2026-08-29.md) | construct the wider action/crossing closure or recurrence after the first even-spin residual | iterate the same selected physical-`Q` action/crossing branch exactly | yes |
| [time-refinement multiplier theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md) | finite positive exterior multipliers are nonzero but do not share an exact semigroup clock | use only channel nonvanishing in (10), not a semigroup law | yes |
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | framework boundary with no supplied dynamics | axiom/primitive non-edit boundary only | yes; not evidence for `K` |

### N5 — rhetoric resolution

“No finite-dimensional selected linear invariant carrier” means exactly the
triangular-rank statement following (10).

- `per_element`: every irrep coefficient in the displayed recurrence is
  constructed and checked through layer eight;
- `per_block`: the selected disjoint `p0/C1` physical-`J_3` fiber is the
  complete block used by the theorem;
- `per_site`: no physical site evolution law is constructed;
- `per_mode`: no continuum or lattice momentum mode is constructed;
- `lattice_wide`: no full lattice transfer or global minimal-memory theorem is
  made.

The primary runner emits the same five-resolution certificate.

### N6 — partial closure and primitive scan

Crossing-only closure is explicitly retained as the positive recurrence (11).
The no-go requires no new axiom. A full symmetric cancellation, multiple
placement quotient, nonlinear recurrence, or indexed carrier can still alter
the wider memory question. Those are next calculations, not assumed walls.

### N7 — steelman

The strongest objection is that repeated conditional subtraction could remove
the new high-spin component, or that crossing could kill it even away from the
Haar endpoint. Equation (3) shows that `Q` sees only `(0,+)`. Equation (5)
gives the high-spin summand a unique parent and coefficient one. Equation (8)
shows that crossing only multiplies it, and the imported finite-positive-step
theorem makes that multiplier nonzero. This defeats the objection on the
selected branch. It does not defeat possible cancellation between the two
orders in the complete symmetric response, so that route remains open.

### N8 — cross-cycle echo

Block245 left invariant closure open. Block246 falsified only its rank-29
carrier and separated sample-wise temporal multiplicity leakage from one new
even-spin direction. The present theorem does not echo the earlier static-cup
wall or promote rank 72. It resolves the next selected action-tower question
by an all-layer recurrence, while preserving the full symmetric step and
global memory as open routes.

**Gate result: PASS for the selected ordered finite-dimensional linear-carrier
no-go.** The packet would fail for a claim about the complete action kernel,
all operator orders, global minimal memory, arbitrary `r/q`, physical
dynamics, gravity, or TOE closure; none of those claims is shipped.
