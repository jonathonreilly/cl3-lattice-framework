---
claim_id: admissibility_exterior_character_jr_r3_q2_adjacent_product_cubic_response_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_ADJACENT_PRODUCT_CUBIC_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
title: Exact r=3, q=2 adjacent-product cubic response on the two-cell ladder
claim_scope: "For the defining-vector character and the six nonempty proper three-plaquette histories, compute exactly the first possible cubic adjacent-product response on the finite two-cell 19-link ladder. Prove the lower orders vanish, prove that physical conditional-Haar Q annihilates all six histories, reconstruct all 48 temporal half-histories with original-link Brauer integration, and sum them to one closed polynomial in the supplied formal spin multipliers. This is one conditional finite-carrier response entry, not a full transfer, a positivity or minimal-memory theorem, arbitrary r or q, physical time, continuum dynamics, gravity, or a theory of everything."
depends_on:
  - admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_q4_o10_temporal_cup_bridge_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_bounded_theorem_note_2026-08-29: "supplies the defining-vector character convention, proper-subset inclusion-exclusion carrier, conditional-Haar map, and outer cubic response normalization"
  admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_bounded_theorem_note_2026-08-29: "supplies the adjacent-product cell geometry and the exact central-projector insertion convention"
  admissibility_exterior_character_jr_r2_q4_o10_temporal_cup_bridge_bounded_theorem_note_2026-08-29: "supplies reviewed exact original-link Brauer and temporal helper implementations; no q=4 response value is imported"
  admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28: "supplies the formal central spin multipliers; this note does not derive them from an exterior one-parameter semigroup"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r3_q2_adjacent_product_cubic_response_2026_08_29.py
independent_checker: null
date: 2026-08-29
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_bounded_theorem_note_2026-08-29
target_blocker_text: "compute the first exact higher-r adjacent-product response after the physical conditional-Haar subtraction"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
proposal_allowed: false
proposal_allowed_reason: "The temporal multipliers and outer response coefficient remain supplied formal inputs, and only one finite r=3, q=2 entry is proved."
axiom_policy: "framework boundary only; no axiom or approved primitive is edited"
next_trace_action: "Construct the complete six-history Gram carrier, or extend the same exact original-link method to a second independent q or r, before making any transfer or memory claim."
conditional_surface_status: "exact finite-carrier r=3, q=2 cubic adjacent-product response after physical conditional-Haar subtraction on the supplied formal multiplier family"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the lower-order vanishing, six physical-Q annihilations, 48 half-history identities, and closed cubic response are exact on the disclosed finite carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Exact `r=3`, `q=2` adjacent-product cubic response — bounded theorem

**Type:** `bounded_theorem`

**Status:** `proposed_retained`. The actual current surface is
`conditional-support`: the theorem is one exact finite-carrier response entry
conditional on the supplied formal temporal multipliers and outer response
coefficient. It does not promote either input to a derived physical law, and
the independent audit lane alone determines effective status.

## Authorities and imported inputs

- The [arbitrary-`r` scalar-fused vector transfer note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_ARBITRARY_R_SCALAR_FUSED_VECTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-29.md)
  supplies the defining-vector character convention, proper-subset carrier,
  conditional-Haar map, and outer cubic response normalization.
- The [`r=2` adjacent-product vector response note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md)
  supplies the two-cell geometry, central-projector insertion convention, and
  the original-link representation-label diagonality used in the physical-`Q`
  step.
- The [`q=4` O10 temporal cup-bridge note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_TEMPORAL_CUP_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-29.md)
  supplies the exact original-link Brauer and temporal helper implementations;
  no `q=4` response value is imported.
- The [time-refinement multiplier note](ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md)
  supplies the formal central spin multipliers. This note does not derive them
  from an exterior one-parameter semigroup.
- The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are a framework boundary
  only. No axiom or approved primitive is edited or added.

These parent notes are open conditional dependencies on the stacked review
surface, not effective retained authority. Compact-group Haar integration,
Peter--Weyl orthogonality, and Brauer Gram inversion are standard mathematical
machinery; the load-bearing new calculation is their exact assembly on the
declared finite carrier.

## Exact target and obligation graph

**Target.** Compute the first nonzero `r=3`, `q=2` adjacent-product cubic
`Y`-to-`Z` response after the supplied physical conditional-Haar subtraction,
for all six proper action partitions and all 48 temporal half-histories on the
original 19-link ladder.

The proof obligations are:

1. show orders zero through two vanish and identify the complete cubic action
   channel — proved here by the exclusive-rail Haar/Peter--Weyl argument;
2. enumerate the six proper action partitions and 48 half-action histories —
   proved here by complement enumeration;
3. show physical `Q=JJ^*`, rather than the static cup projector, annihilates
   the six proper histories after crossing — the conditional-Haar zero means
   are proved here, while preservation through crossing imports the linked
   parent-stack label diagonality and `[C,Q]=0`;
4. evaluate every original-link Haar contraction and reduce the temporal sum —
   proved here and checked by the primary exact runner plus an independent
   dense-moment reconstruction;
5. preserve the cubic `1/3!` and half-action normalization — proved by the
   explicit expansion below and checked at the identity control.

The strongest missing lemma is an arbitrary-`r`, arbitrary-`q` transfer or a
complete physical history Gram theorem. It is not needed for the bounded
target above and remains open.

## Result

Let the first coarse cell contain fine plaquettes `p0,p1,p2`, with independent
fine-link actions `a0,a1,a2`, and define

```text
delta0 = W2 W1 W0,
delta1 = W5 W4 W3,
Y      = chi_V(delta1),
Z      = chi_V(delta0) chi_V(delta1).
```

For the defining vector `V` of `O(3)`, the first possibly nonzero normalized
adjacent-product coefficient is

```text
(1/3!) <Y, partial_lambda^3 D_epsilon(0) Z>.
```

Writing the supplied even-spin temporal weights as

```text
x_0=1, x_1=t, x_2=u,
M1 = 1 + 3t + 5u,
M2 = 1 + 3t^2 + 5u^2,
```

define

```text
L1 = t^18 + 3t^20 + 9t^22 + 2t^24 + 8t^26 + t^28,
L2 = t^20 + 2t^22 + 6t^24 + t^26 + 2t^28,
L0 = 2t^20 + 3t^22 + 2t^24 + 4t^26 + t^28.
```

The exact half-history sum and cubic response are

```text
S(t,u) = M1 L1/81 + M2 L2/81 + L0/9,

R3,2 = (epsilon c_V^(n)/2)^3 a0 a1 a2 S(t,u)
     = epsilon^3 (c_V^(n))^3 a0 a1 a2
       [M1 L1 + M2 L2 + 9L0]/8/81.
```

Thus the response stripped only of
`epsilon^3 (c_V^(n))^3 a0 a1 a2` is `S/8`. At the identity crossing
`t=u=1`, this equals `2/3` exactly. At the disclosed rational sample

```text
t=3/10, u=2/5,
S/8 = 8762819875140884481
      / 2000000000000000000000000000000,
```

whose residues over `F_1009`, `F_1013`, and `F_1019` are respectively
`(83,121,659)`.

## Lower-order vanishing and six histories

Each of the three fine plaquettes contributes one defining-vector occurrence
from `C0` on the `Z` side and a trivial label on the `Y` side. Its exclusive
`u_i/v_i` rail can be paired only by an action insertion on that same `p_i`.
At derivative order zero, one, or two, at least one exclusive rail is therefore
unmatched and its Haar integral vanishes. At order three, a surviving placement
must put exactly one insertion on every `p_i`; Peter--Weyl orthogonality on each
exclusive rail then forces the inserted exterior-action irrep `sigma_i` to be
the defining vector `V`. Thus all repeated placements and all non-`V` supplied
action irreps vanish. Equivalently within the selected vector channel, for
every weak composition `(n0,n1,n2)` below order three, not all three values
`1+ni` are even. The order-three survivor is therefore complete and
multilinear in `a0 a1 a2`, with coefficient `(c_V^(n))^3`; it is not merely a
preselected-`V` subcalculation.

The surviving inclusion-exclusion histories are the six nonempty proper
subsets

```text
X in {{0},{1},{2},{0,1},{0,2},{1,2}},
```

with the left trace `p_X C1` and right trace `p_(X^c) C0 C1`. Splitting the
three selected actions between the two temporal halves gives
`sum_X 2^|X| 2^(3-|X|)=48` half-history pairs.

## Physical conditional-Haar `Q`

This step uses the physical conditional-Haar `Q` (namely `Q=JJ^*`); it is not the static `h_3` cup
projector. Fix `delta0` and choose `W0,W1` as independent Haar
variables, so

```text
W2 = delta0 W0^(-1) W1^(-1).
```

Every proper fine-plaquette product has zero conditional defining-vector
character mean. Explicit integration witnesses are

```text
X={0}:     integrate W0,
X={1}:     integrate W1,
X={2}:     integrate W0 inside W2,
X={0,1}:   factor the W0 first moment,
X={0,2}:   integrate W1 inside W2,
X={1,2}:   integrate W0 inside W2.
```

The second-cell factor is a spectator in this conditional integral. Preservation
through temporal crossing is a supplied parent-stack fact, not a consequence of
symmetry alone: Blocks232/236 supply original-link representation-label
diagonality and `[C,Q]=0`. Those inputs keep the six proper mixed-label rows in
`ker Q` after crossing. Therefore the physical `(I-Q)` leaves the calculated raw
`1/9` overlap unchanged. This proves the action of `Q` on this particular
history span; it does not identify `Q` with a local cup or prove its action on
an arbitrary history space.

## Original-link reconstruction and normalization

Use the unreduced two-cell ladder

```text
p_i = u_i h_(i+1) v_i^(-1) h_i^(-1),
C0  = u0 u1 u2 h3 v2^(-1) v1^(-1) v0^(-1) h0^(-1),
C1  = u3 u4 u5 h6 v5^(-1) v4^(-1) v3^(-1) h3^(-1).
```

There are 19 original links: twelve `u/v` links and `h0,...,h6`. The merged
`C1` cancels `h4,h5`, so precisely 17 links are active. Every active link
except `h3` has defining-vector degree two, while `h3` has degree four. The
exact `O(3)` Haar moments are reconstructed from the reviewed Brauer
pairing/Gram factorization, not from a dense `3^16` tensor.

At identity, all six topology overlaps equal `1/9`; their prime residues are
`(897,788,453)`. On a degree-two link, selecting both occurrences on the same
trace side hits the invariant cup and contributes spin-zero weight `x_0=1`,
not `t^2`. After removing these cup pairs, the remaining degree-two selected
occurrences give the displayed power of `t`.

The degree-four junction `h3` has two endpoint types:

```text
2 in X:
  2 in the left half      -> t^e M2/81,
  2 not in the left half  -> t^(e+1) M1/81;

2 not in X:
  2 in the right half     -> t^(e+2)/9,
  2 not in the right half -> t^(e+1) M1/81.
```

Here `e` is the exact selected-occurrence census on the other 16 active
degree-two links, with two selected occurrences removed for each same-side
cup. The weights `1,3,5` in `M1,M2` are the ranks of the spin `0,1,2`
channels of the degree-four invariant moment. Summing the 48 cases yields
exactly `S(t,u)` above. The formal sample also varies unused odd/even labels
in the verifier to demonstrate that no undisclosed `d` or `v` dependence has
been introduced.

## Deterministic certificate and hostile controls

The runner imports the reviewed Block240 Brauer factors and Block243
finite-field central projectors, but independently rebuilds this Block244
network, half-history census, endpoint reduction, and closed polynomial. It
checks:

```text
6 topology/identity overlaps x 3 primes                 = 18,
48 disclosed temporal half-histories x 3 primes        = 144,
48 half-histories x 3 unrelated signed samples x 3     = 432,
total load-bearing all-link comparisons                 = 594.
```

The three signed samples vary `t,u,d,v` independently. Exact closed sums are
also compared to the direct all-link totals at all four samples; symbolic
checks certify the `2/3` identity limit and nontrivial `u` dependence. Hostile
mutations must reject: a corrupted link census, treating a same-side cup as
`t^2`, collapsing `M2` to `M1`, swapping the two endpoint types, permitting
lower-order leakage, dropping the cubic `1/8`, identifying physical `Q` with
the static cup, claiming a full transfer, and editing an axiom boundary.

The calculation is modular-exact, not floating-point evidence: all rational
denominators are inverted independently in three prime fields, and tensor
products are reduced modulo the active prime after each operation. The
disclosed final rational is additionally reconstructed in characteristic
zero.

## Boundaries

- No full transfer, transfer semigroup, Gram-positivity, or minimal-memory
  theorem is proved.
- No claim is made for arbitrary `r`, arbitrary `q`, arbitrary words, or the
  other entries of a six-history response matrix.
- No lower-order leakage is hidden: orders zero through two vanish by the
  explicit exclusive-rail parity gate.
- The temporal multipliers and `c_V^(n)` are imported formal data. They are
  not derived from exterior time, a continuum limit, or measured dynamics.
- No gravity, continuum, phenomenology, or theory-of-everything statement is
  inferred from this finite exact carrier.
- No axiom or approved primitive changes are made.

## Review record

An independent restricted-input refuter reconstructed the six raw overlaps by
an exact union-find `O(3)` Weingarten calculation, then rebuilt all 48 temporal
histories with dense second/fourth moments and spin-one Casimir projectors on a
separate implementation path. The independent checks matched the 48 histories
at two signed samples (`96/96`, maximum numerical discrepancy below
`1.1e-23`), reproduced the closed polynomial, identity limit, disclosed
rational and prime residues, and confirmed that independent variations of the
unused `d,v` inputs do not change the result. Two review findings were repaired:
the physical-`Q` crossing step is now explicitly conditional on the parent
label-diagonality/commutation input, and the cubic completeness argument now
includes the full action-irrep selection rather than only a preselected vector
channel. The resulting review-loop disposition is `CONDITIONAL` in the
proof-obligation vocabulary: the finite target closes on its stated supplied
parent inputs, while those inputs and every wider transfer/dynamics claim remain
outside this note.
