---
claim_id: admissibility_d4_record_past_nondisturbing_causal_preparation_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "A CPTP extension preserving the complete supplied product density on an open nine-parameter quantum family has a constant complementary output; physical Record encoding and readout remain open."
claim_type_reason: "Exact finite conditional algebra; scientific assumptions and physical supplier boundaries are explicit."
---

# A permanent noncommuting Record shell cannot also program a fresh copy of itself

**Date:** 2026-08-29; corrected 2026-09-09

**Type:** bounded_theorem

**Standing:** conditional finite mathematics; formal audit deferred.

A CPTP extension preserving the complete supplied product density on an open nine-parameter quantum family has a constant complementary output; physical Record encoding and readout remain open.

## Primary verification

Primary runner: [`admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.py`](../scripts/admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.py).

Independent checker: [`independent_admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.py`](../scripts/independent_admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.py).

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

Current conditional predecessor: [ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29](ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md).

The full old product density is the hypothesis, not merely nine moment
statistics. The new target is a separate quantum output. The earlier B6
construction is a supplied enlarged finite tape/register protocol; its physical
one-site M2 encoding and readout bridge remain open and its proposed whole
geometric stencil covariance fails. It is not a framework-native physical
counterexample to this theorem. This note relies only on the explicit channel
and product-family assumptions below, not on B6 or old audit status.

## Exact channel target

Write the Block-10 parameters as

\[
 \theta=(q_0,q_1,q_2,q_3,q_4,u_x,u_y,u_z,s)
\]

and let

\[
 v_n(\theta)=-\frac12Q(\theta)n
 +\frac18\left(sn+u\mathbin{\times}n\right),\qquad
 \rho_n(\theta)=\frac12(I+v_n\cdot\sigma).
 \tag{1}
\]

Opposite directions are antipodal:

\[
 v_{-n}(\theta)=-v_n(\theta).                           \tag{2}
\]

The old six-site Record program is the product state

\[
 R(\theta)=\bigotimes_{n=\pm e_i}\rho_n(\theta)
 \quad\hbox{on}\quad H_R=(\mathbb C^2)^{\otimes6}.     \tag{3}
\]

The open box around `theta=0` lies strictly inside all six Bloch balls.  At
zero, `R(0)=I_64/64`.

The tested class contains every CPTP map

\[
 \Gamma:B(H_R)\longrightarrow B(H_R\otimes H_C)        \tag{4}
\]

with arbitrary fixed ancillas and arbitrary old/new correlations, subject to

\[
 \operatorname{Tr}_{C}\Gamma(R(\theta))=R(\theta)       \tag{5}
\]

for every `theta` in the open box.  Equation (5) is the candidate **complete
quantum prefix-safety** reading.  The desired new condition shell must have
nonconstant `A1+T1+E+T2` response of rank nine.  It need not be a product
state for the theorem; only its six condition marginals and decoder response
matter.

Locality and cubic covariance are not needed to obtain the obstruction.  Thus
the theorem covers every strict-radius-one, translation/proper-cubic-covariant
subclass satisfying (3)--(5), but it does not cover other Record semantics.

## The nine tangents generate the full old-shell algebra

It is enough to use the three positive-direction vectors.  Their exact
Jacobian is

\[
 J_+=\frac{\partial(v_{+e_1},v_{+e_2},v_{+e_3})}
 {\partial\theta},\qquad
 \operatorname{rank}J_+=9,\qquad
 \det J_+=\frac{3}{16384}.                              \tag{6}
\]

Differentiating (3) at zero and using (2) gives, after the invertible change
of coordinates (6), the nine operators

\[
 D_{i,a}=\sigma_a^{(+e_i)}-\sigma_a^{(-e_i)},
 \qquad i=1,2,3,\quad a=x,y,z.                          \tag{7}
\]

For one opposite pair, put `D_a=sigma_a tensor I-I tensor sigma_a`.  Exact
commutators give

\[
 \frac{[D_x,D_y]}{2i}=Z\otimes I+I\otimes Z             \tag{8}
\]

and the two cyclic analogues.  Adding and subtracting the corresponding
`D_a` recovers every `sigma_a tensor I` and every `I tensor sigma_a`.
Therefore one pair generates `M4`.  The independent checker reaches the same
conclusion without using (8): it solves the generic `4x4` commutant of the
three differences, finds exact coefficient rank 15 and a one-dimensional
scalar commutant, and hence obtains the full irreducible `M4` algebra.

The three disjoint pairs generate

\[
 M_4\otimes M_4\otimes M_4=M_{64},
 \qquad \dim M_{64}=4096.                               \tag{9}
\]

## Prefix safety forces the identity marginal

Define the old-shell marginal channel

\[
 N=\operatorname{Tr}_{C}\circ\Gamma.                    \tag{10}
\]

Equation (5) fixes `R(0)=I/64`, so `N` is unital as well as trace preserving.
It also fixes every derivative (7).

For a unital completely positive map, the Schwarz inequality gives

\[
 N(X^\dagger X)\succeq N(X)^\dagger N(X).               \tag{11}
\]

If `N(X)=X`, trace preservation makes the two sides of (11) have equal trace.
Their positive difference is therefore zero, putting `X` in the
multiplicative domain of `N`.  Products and adjoints of fixed operators are
fixed.  The fixed set is consequently a star algebra containing all nine
operators (7), so (9) forces

\[
 N=\operatorname{id}_{64}.                              \tag{12}
\]

This step is exhaustive over channels; it is not a search over a selected
Kraus ansatz.

## A rank-one Choi marginal has a constant complement

Take the Choi matrix of (4).  Tracing out `H_C` gives the identity-channel
Choi matrix

\[
 \operatorname{Tr}_{C}J(\Gamma)=J(\operatorname{id}_{64})
 =|\Omega\rangle\langle\Omega|,                         \tag{13}
\]

which has rank one and trace 64.  A positive operator with a rank-one
marginal factors across that marginal.  To see the load-bearing step directly,
decompose the first factor into the support of `|Omega>` and its orthogonal
complement.  The complement-complement block is positive and has trace zero,
so it vanishes.  Positivity of every `2x2` principal block then kills the
off-diagonal block: a scalar representative has determinant `-|beta|^2`.
Thus

\[
 J(\Gamma)=J(\operatorname{id}_{64})\otimes\tau_C,
 \qquad
 \Gamma(A)=A\otimes\tau_C                              \tag{14}
\]

for one fixed state `tau_C`.

Every new-shell marginal is independent of `theta`.  Its parameter Jacobian
has rank zero, contradicting the required rank nine.  This proves `EMPTY` for
(3)--(5) together with the required nonconstant new target. Conditions (3)--(5)
alone admit the constant-output extension (14). For the required variable-target
class, the Kraus/Stinespring gauge
quotient is empty; there is no hidden unique-versus-plural selection inside
this class.

## Positive and relaxed-premise controls

### Consumable live conditions

Relabeling or SWAP-moving the old six-qubit state into a new shell is a unitary
channel.  It is trace preserving, uses only the past shell, has target
Jacobian rank nine, and preserves every H1/H2/cubic/law check.  It consumes or
moves the input instead of returning the old shell unchanged.  This is the
explicit consumable live-condition relay left open by the theorem.

### Orthogonal Record atoms

For the commuting program menu `|0>,|1>`, CNOT obeys

\[
 |b\rangle|0\rangle\longmapsto |b\rangle|b\rangle,
 \qquad b=0,1,                                          \tag{15}
\]

and leaves the old label intact. The primary checks CNOT unitarity and (15);
the checker uses its copy isometry to compare unchanged classical and disturbed
coherent marginals.
This is a real classical Record-copy route.  Six binary orthogonal labels do
not parameterize the exact nine-dimensional continuum (1), but a different
Record/readout representation or larger block could use the mechanism.

### Approximate quantum copying

Let `P_sym=(I+SWAP)/2`.  The channel

\[
 C(\rho)=\frac23P_{\rm sym}(\rho\otimes I)P_{\rm sym}   \tag{16}
\]

has an exact two-Kraus form, is trace preserving, and gives both output
marginals Bloch shrink `2/3`.  It consumes/disturbs the original program and
does not reproduce the frozen gains, so it fails (5) and the exact target.
It nevertheless proves that approximate/statistical propagation is a
separate live route.

### Supplied external program and direct reuse

If an extra `theta`-dependent shell is supplied, a SWAP can install it while
leaving (3) untouched.  That is an external state-dependent program, not a
fixed channel whose only varying input is the old Record shell.  Likewise a
single event can use existing Records directly as its neighboring conditions
without preparing a new copy.  Source/Eta Block 04 showed that the exact
all-six-Record ready-set realization fills surrounded holes but is cleanup-only;
it does not generate an adjacent front.  Neither route is closed here.

## Even-shell and physical boundaries

Adding the same three-vector to both members of each opposite pair leaves
the odd decoder unchanged. The full 18-dimensional shell still has the same
nonconstant rank-nine required target, so this addition does not evade the
constant-complement conclusion. A consumable identity/SWAP relay, an orthogonal
classical copy, an approximate clone, external preparation, and direct reuse
relax different stated hypotheses. None supplies the missing physical encoding,
readout, event attachment, endogenous formation site/rate or generated history.
The finite B6 register construction is another conditional route only; its
whole-stencil geometric covariance is not established and in the proposed form
is false. No relation among those physical obligations is asserted independent.

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
