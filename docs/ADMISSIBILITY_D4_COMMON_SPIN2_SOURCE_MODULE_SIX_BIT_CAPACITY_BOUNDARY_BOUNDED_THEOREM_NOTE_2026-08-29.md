---
claim_id: admissibility_d4_common_spin2_source_module_six_bit_capacity_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "The supplied cubic tensor module has E plus T2 dimension five; the specified affine six-bit domain has only one free orbit, so cannot cover both disjoint free target orbits."
claim_type_reason: "Exact finite conditional algebra; scientific assumptions and physical supplier boundaries are explicit."
---

# H1 and H2 share one five-dimensional spin-two source module, but six condition bits supply only one generic orbit

**Date:** 2026-08-29; corrected 2026-09-09

**Type:** bounded_theorem

**Standing:** conditional finite mathematics; formal audit deferred.

The supplied cubic tensor module has E plus T2 dimension five; the specified affine six-bit domain has only one free orbit, so cannot cover both disjoint free target orbits.

## Primary verification

Primary runner: [`admissibility_d4_common_spin2_source_module_2026_08_29.py`](../scripts/admissibility_d4_common_spin2_source_module_2026_08_29.py).

Independent checker: [`independent_admissibility_d4_common_spin2_source_module_2026_08_29.py`](../scripts/independent_admissibility_d4_common_spin2_source_module_2026_08_29.py).

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

## Exact common module

Use the upstream ten-component symmetric basis and restrict to the six purely
spatial slots `(1,2,3,7,8,9)`.  Define

```text
A1 = span{(1,1,1) on slots (1,2,3)},
E  = span{(1,-1,0),(1,1,-2) on slots (1,2,3)},
T2 = span{e_7,e_8,e_9}.                                 (1)
```

The H1 coefficient lies in `T2` and has proper-cubic cyclic-span rank three.
The H2 diagonal coefficients obey

```text
(sqrt(3)+3)/4 -(sqrt(3)+1)/4 - 1/2 = 0,                (2)
```

so H2 has no `A1` trace.  Its diagonal projection spans `E` with rank two,
and its off-diagonal projection spans `T2` with rank three.  Exact cyclic
spans give

```text
dim <G H1>              = 3,
dim <G H2>              = 5,
dim (<G H1> + <G H2>)   = 5,
dim (<G H1> intersect <G H2>) = 3.                     (3)
```

Therefore the unique smallest invariant subspace containing both complete
orbits is

```text
V_common = E direct-sum T2,       dim V_common = 5.     (4)
```

It is the trace-free spatial symmetric or spin-two module restricted to the
proper cubic group.  The phrase “spin two” identifies this representation;
it does not assert a continuum graviton or gravity closure.

## Exact cubic characters

The 24 signed proper-cubic matrices split into five conjugacy signatures.  In
the table, the signature is `(order, spatial trace, nonzero diagonal count)`.

| signature | count | chi_E | chi_T2 | chi_common |
|---|---:|---:|---:|---:|
| `(1,3,3)` | 1 | 2 | 3 | 5 |
| `(2,-1,1)` | 6 | 0 | 1 | 1 |
| `(2,-1,3)` | 3 | 2 | -1 | 1 |
| `(3,0,0)` | 8 | -1 | 0 | -1 |
| `(4,1,1)` | 6 | 0 | -1 | -1 |

The primary obtains these representations from exact tensor conjugation, not
from a named character table; the checker independently checks the orbit spans.  The dimensions and distinct characters rule
out a four-dimensional invariant common subspace and a hidden scalar repair.

## Complete 64-mask affine-action census

The frozen nontrivial affine proper-cubic action splits all 64 masks into:

| canonical representative | orbit size | stabilizer size | dim `V_common^H` | complement |
|---:|---:|---:|---:|---:|
| 0 | 6 | 4 | 2 | self |
| 1 | 6 | 4 | 2 | orbit 7 |
| 4 | 12 | 2 | 3 | self |
| 5 | 24 | 1 | 5 | self |
| 7 | 6 | 4 | 2 | orbit 1 |
| 12 | 2 | 12 | 0 | self |
| 21 | 4 | 6 | 1 | orbit 22 |
| 22 | 4 | 6 | 1 | orbit 21 |

The sizes sum to 64.  For an orbit `G/H`, an equivariant map into
`V_common` is determined by one seed in the fixed subspace `V_common^H`.
Summing the displayed fixed dimensions gives an exact 16-dimensional vector
space of equivariant functions on the full mask set.  The self-complement
even/odd dimensions are respectively `(1,1)`, `(1,2)`, `(3,2)`, and `(0,0)`
for representatives `0,4,5,12`; paired orbits are carried into each other.
This exhausts both parity choices without selecting one.

## Why sixteen equivariant degrees of freedom are still insufficient

The target is not merely a nonzero equivariant function.  It must contain the
complete H1 and H2 source orbits.  Both exact vectors have trivial cubic
stabilizer:

```text
|Stab(H1)| = |Stab(H2)| = 1,
|G H1| = |G H2| = 24.                                   (6)
```

They are distinct orbits because H1 has no `E` projection while H2 has a
rank-two `E` projection.  If an equivariant map sends a domain point with
stabilizer `H` to a target with stabilizer `K`, then necessarily `H` is a
subgroup of `K`.  For either generic target, `K` is trivial, so its preimage
must lie in a free domain orbit.

The census has exactly one free orbit, representative 5.  That is the frozen
H1 active orbit.  Hence:

```text
number of free domain orbits required = 2,
number of free six-bit affine orbits  = 1.               (7)
```

No deterministic equivariant map from this 64-mask `G`-set can contain both
target orbits.  This remains true even if the forty inactive zeros are allowed
to change: none of their seven orbits is free.  Preserving the complete H1
map makes a strict extension impossible immediately; allowing an explicit
replacement while preserving only the H1 active orbit still cannot place H2.
Fixture-name switching would create two maps, not one local decoder, and is
excluded by registration.

## Adjudication and physical meaning

The registered outcome is

```text
MODULE-ONLY.
```

The common five-component source representation is exact and positive.  The
frozen six-bit deterministic condition action is one generic-orbit short.
Physical local ownership is not proved: neither the six-bit map nor this note
derives how local quantum conditions prepare an H1-versus-H2 sector.

This identifies a high-leverage next target.  A second physically owned free
orbit remains open.  Candidate realizations include an additional invariant
binary sector, a two-cell distributed condition, or a quantum local variable
built from direction comparisons and corner weights.  Any such repair must
derive its value from neighboring quantum conditions; an H1/H2 label is not a
physical bit.  The next campaign must preregister and compare those owners
before constructing a common decoder.

In the exact controlled wording used by the runners, a second physically owned free orbit remains open, and physical local ownership is not proved.

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
