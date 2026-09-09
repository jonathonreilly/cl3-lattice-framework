---
claim_id: admissibility_d4_frozen_h2_common_action_source_image_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "Nonmembership of the supplied H2 coefficient/source in the frozen 64-mask affine H1 decoder image; no larger-domain or physical impossibility."
claim_type_reason: "Exact finite conditional algebra; scientific assumptions and physical supplier boundaries are explicit."
---

# The frozen H1 source law has no H2 member, and the missing direction is exact

**Date:** 2026-08-29; corrected 2026-09-09

**Type:** bounded_theorem

**Standing:** conditional finite mathematics; formal audit deferred.

Nonmembership of the supplied H2 coefficient/source in the frozen 64-mask affine H1 decoder image; no larger-domain or physical impossibility.

## Primary verification

Primary runner: [`admissibility_d4_frozen_h2_common_action_source_image_2026_08_29.py`](../scripts/admissibility_d4_frozen_h2_common_action_source_image_2026_08_29.py).

Independent checker: [`independent_admissibility_d4_frozen_h2_common_action_source_image_2026_08_29.py`](../scripts/independent_admissibility_d4_frozen_h2_common_action_source_image_2026_08_29.py).

The current [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the named
framework ontology, not the specific encoder, probabilities, CPTP preparation
or complete-density Record representation used here. These remain conditional.

## Current premises and historical custody

The finite definitions below are supplied mathematical inputs. The dated
[recovery inventory](../.claude/science/physics-loops/eta-spin2-correction-20260909/RECOVERY.json) preserves every original endpoint,
changed version and actual historical helper input. Historical preregistration,
Git ancestry, old main hashes, source compilations, printed mutation counts and
cache scores are not present-day proof or input guards. The original notes and
all their arguments remain recoverable; only the scoped assertions below are
active. The five companion notes share the explicit finite models; no broader
parent campaign, axiom-level physical selector or reservation is accepted.

[Correction and claim disposition](../.claude/science/physics-loops/eta-spin2-correction-20260909/HISTORY.md) explains the source split.

The proper cubic group is all signed permutation matrices of determinant one,
sorted lexicographically by their nine entries. Its six directions are
`(-x,+x,-y,+y,-z,+z)`. On six bits use the unique GF(2) affine cocycle class
with a 24-point orbit from the explicitly implemented finite cocycle quotient.
The selected representative is the original row-reduction convention. The action
is `A(g,m)=permute(m,g) XOR t_g`; this is a supplied code action, not a derived
physical rotation on arbitrary Bloch vectors. On the orbit of mask 5 the shear
is the cubic transport of `(0,1/sqrt(2),-1)`; on all other masks it is zero.
This defines every row of the 64-mask decoder without a parent controller.

The normalized symmetric four-tensor basis is ordered
`(33,00,11,22,03,13,23,01,02,12)`, with off-diagonal entries `1/sqrt(2)`.
For each supplied transfer, impose zero trace and annihilation of
`(2 sin(q0/2),2 sin(q1/2),2 sin(q2/2))`, take the exact SymPy nullspace in that
basis, and select its second column. H1 uses incoming
`(pi/6,pi/3,0,pi/6)` and transfer `(pi/3,pi/2,0,0)`; H2 uses incoming
`(pi/4,pi/6,pi/3,pi/6)` and transfer `(pi/6,pi/3,pi/2,0)`.

## Exact H2 coefficient

In the upstream symmetric `PAIRS4` order

```text
(33,00,11,22,03,13,23,01,02,12),
```

the two independent reconstructions give

```text
h_H2 = (
  0,
  (sqrt(3)+3)/4,
  -(sqrt(3)+1)/4,
  -1/2,
  0, 0, 0,
  -sqrt(3)/2,
  0,
  1
).                                                        (1)
```

Thus its exact nonzero slots are

```text
(1,2,3,7,9).                                              (2)
```

The frozen H1 decoder writes only slots `(7,9,8)` according to

```text
J_H1(s_x,s_y,s_z)
  = sqrt(2) s_x e_7 + sqrt(2) s_y e_9 + sqrt(2) s_z e_8.  (3)
```

Projecting (1) onto that normalization gives the H2 shear

```text
s_H2 = (-sqrt(6)/4, sqrt(2)/2, 0).                        (4)
```

But (1) also has nonzero diagonal spatial slots `(1,2,3)`.  If `B_H1` is the
ten-by-three matrix in (3), exact rank gives

```text
rank(B_H1) = 3,
rank([B_H1 | h_H2]) = 4.                                  (5)
```

Therefore the H2 coefficient is not in the frozen H1 source domain.

## Exhaustive eta decoder test

The primary runner reconstructs the supplied affine table, forms its unique Boolean ANF, and evaluates that ANF for all 64 six-bit conditions.
Twenty-four inputs form the active proper-cubic H1 orbit and forty have the
frozen zero extension.  None equals (4):

```text
{eta in {0,...,63}: s(eta)=s_H2} = empty.                 (6)
```

Masks 17 and 33 are closest only in the discrete sense that each leaves one
nonzero shear coordinate.  Their residuals are, respectively,

```text
(1+sqrt(6)/4, 0, 0),
(-1+sqrt(6)/4, 0, 0).                                     (7)
```

Neither is zero.  No tolerance, fitted scalar, support match, alternative
column, or H2-specific decoder is admitted.

The independent checker does not import the Block-03 decoder table.  It
rebuilds the 24 active shears from the base shear
`(0,1/sqrt(2),-1)` and the proper-cubic representation, appends the forty
declared inactive zeros, and obtains the same empty image intersection.

## Complete cubic and reflection orbit

The full signed cubic group contains 48 spatial matrices: 24 proper
rotations and 24 reflected transforms.  For each `R`, the runner constructs
the exact ten-dimensional symmetric-tensor representation `T(R)` and checks

```text
rank(T(R) B_H1) = 3,
rank([T(R) B_H1 | T(R) h_H2]) = 4.                       (12)
```

All 48 cases pass.  A basis change or orientation reversal therefore cannot
turn H2 into a member.  This orbit statement uses only invertible transport;
it does not assert that the fixed H2 momentum is itself invariant under the
group.

## What the verdict means

The exact preregistered verdict is:

```text
NO-MEMBER
```

It means no member of the already-frozen H1 action/ANF/rank-three-source
family realizes H2.  It does not mean:

- no local source law can realize H1 and H2;
- the M4 carrier or Record instrument fails on a lawful H2 state;
- diagonal tensor components require a new axiom;
- gravity, quantum probabilities, or Records are impossible; or
- the minimal-axiom program is inconsistent.

The earliest failing object is the candidate source representation.  It is
therefore premature to blame the carrier, probability family, ordered
history, or axioms.  The current axioms allow other local quantum-state
alternatives and do not prescribe the rejected three-coordinate decoder.

## Positive repair now exposed

Equation (5) identifies a small constructive target.  Search, before opening
either fixture, for a proper-cubic local source representation `J_common`
whose image contains the H1 three-space and the new H2 direction.  The
minimal data rank is at least four.  A successful candidate must:

1. be derived from one local action or condition representation rather than
   a fixture-name switch;
2. reproduce both exact TT coefficient/source pairs with one normalization;
3. preserve the literal forward and actual-reverse conventions;
4. generate its condition input locally without importing momenta or a
   post-hoc lookup table; and
5. only then pass the existing M4 carrier, CP/TP instrument, Record, and
   generated-history gates.

This route is more informative than adding another H1 history event now:
without a common H1+H2 source law, additional H1-only recurrence cannot
establish a physical common law.  It is also more immediate than polishing
the supplied fixed-`q=3` gravity carrier, whose action selection, clock, and
Record coupling remain open.

## Source composition and injectivity proof

The source-only exterior model uses the sixteen subset states of four fermion
modes, creation operators C_i, occupation N_i=C_i C_i^T, mass m=2/7,
D(p)=sum sin(p_i) C_i, and centered Hodge vertices
`H_ii=cos(p_i+q_i/2)^2 (I/2-N_i)` and
`H_ij=-cos(p_i+q_i/2)cos(p_j+q_j/2)(C_i C_j^T+C_j C_i^T)/sqrt(2)`.
Its exact action vertex is `V_A=m H_A+i(H_A D(p)+D(p+q)^T H_A)`.
A coefficient c denotes `sum c_A V_A`; equality of decoded coefficients and
momenta therefore gives equality of every source entry and phase, without an
additional numerical acceptance assumption.

At zero momenta the ten occupation/hopping H_A are independent: the four
occupation columns are independent diagonal functions on all subsets, while
the six hopping columns have different unordered pairs of off-diagonal
transitions. Nonzero mass preserves rank ten, which proves injectivity of the
universal Laurent map from this one evaluation witness. Restriction to the
five-dimensional STF module therefore has rank five. Literal reverse is the
invertible substitution `(p,q)->(p+q,-q)` (or exponent `(a,b)->(a,a-b)`), so the
same rank statement holds in the actual reverse convention, not a substituted
adjoint. At the supplied H2 point all four centered cosines are nonzero;
the even-degree part m H_A is injective, while the differential part changes
degree parity and cannot cancel it. Thus coefficient nonmembership also holds
at that fixed point. Transfer time is zero, so the historical full-carrier
modulation reduces to I24, preserving these ranks upon tensor product.

The old full Laurent report (195 target terms, nearest-mask residual 155 powers
and 1,212 entries) is preserved as historical computation. Fresh checks use the
exact injectivity argument and actual 64-row decoder; they do not restamp or
claim to replay those larger enumerations. The earlier physical Schur, transport,
clock, formation and history constructions are not premises of this source map.

## Current evidence and limits

The primary and registered checker bind their own note and the complete actual
source-helper closure by current SHA-256. Their terminal result fails closed.
The canonical cache contains a fresh bounded execution of the named predicates.
Each checker includes actual changed operands and applies its unchanged baseline
predicate; the old label-only mutation totals are withdrawn as rejection evidence.
Historical successes are neither erased nor converted into fresh runs. There is
no physical instrument selection, global causal-preparation no-go, new axiom,
obligation retirement, retained grade, audit verdict or TOE percentage claim.

## No-Go Discipline Gate

### N1 — Actual alternatives and quantifiers

The finite source nonmembership leaves larger coefficient images open. The
six-bit capacity theorem leaves a larger input domain or supplied quantum
conditions open. The nondisturbance theorem allows a consumable relay, orthogonal
classical data, approximate channels, external programs or direct reuse when
its full quantum-product preservation/separate-output hypotheses are relaxed.
These are actual scope alternatives, not five newly rejected campaigns.

### N2 — Relations among conditions

The assumptions in each theorem are jointly explicit. No claim of pairwise
independence among physical encoding, preparation, covariance and readout is
made; their implications are unresolved. Code-action covariance is not the
same assertion as physical whole-stencil covariance.

### N3 — Supplied inputs

The affine code action, H1/H2 target columns, Bloch preparations, fixed output
menu, conditional law, CPTP domain and complete product-state preservation are
supplied mathematical definitions or hypotheses. No missing framework supplier
is hidden by the words registered, native, physical or by construction.

### N4 — Exact residual

The current finite source result concerns one decoder image, the orbit result
one affine action, and the channel theorem one full-density preservation target.
The B6 enlarged-register construction does not close any physical encoding or
readout residual here. No earlier compiler or audit verdict is borrowed.

### N5 — Resolution

Element and finite-block identities are explicit in the proofs and named fresh
checks. Six-site states are supplied conditions. No spatial dynamics, universal
mode census, whole-lattice preparation or infinite history is executed or closed.

### N6 — Partial constructive route

A common five-dimensional source module and the supplied joint nine-coordinate
carrier are positive finite constructions. A physical realization may use a
reframed encoding or classical readout; the current theorem does not require a
new axiom or declare those routes absent.

### N7 — Strong counterargument

A larger encoded classical register or consumed quantum substrate could carry
the required data without preserving a separate copy of every noncommuting old
product state. Such a construction would escape the narrow domain; it still
must provide an actual physical local encoding and readout, rather than only
code labels. No universal impossibility follows from this conditional theorem.

### N8 — Lineage check

Earlier B3/B6 lineage and front protocols motivated these questions. Their
corrected scope preserves supplied finite algebra while leaving physical M2
encoding/readout open and the proposed whole-stencil covariance false. That distinction is propagated
here; similar historical boundary labels have no independent authority.

This is written scope analysis, not an author-issued audit or packet PASS.
