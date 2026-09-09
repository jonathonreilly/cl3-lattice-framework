---
claim_id: admissibility_d4_quantum_direction_corner_common_source_owner_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "A conditional fourteen-outcome probability law on six supplied Bloch vectors has a rank-five STF moment; fixed pure outcome states differ from auxiliary three-neighbor mixtures."
claim_type_reason: "Exact finite conditional algebra; scientific assumptions and physical supplier boundaries are explicit."
---

# Quantum Direction/Corner Common-Source Law And Ownership Boundary

**Date:** 2026-08-29; corrected 2026-09-09

**Type:** bounded_theorem

**Standing:** conditional finite mathematics; formal audit deferred.

A conditional fourteen-outcome probability law on six supplied Bloch vectors has a rank-five STF moment; fixed pure outcome states differ from auxiliary three-neighbor mixtures.

## Primary verification

Primary runner: [`admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.py`](../scripts/admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.py).

Independent checker: [`independent_admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.py`](../scripts/independent_admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.py).

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

Current conditional predecessor: [ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29](ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md).

**Two different corner objects.** The fourteen fixed output possibilities have
Bloch vectors `±e_i` and `c/sqrt(3)` and hence are pure states. Separately,
`b_c=(v_(c_x e_x)+v_(c_y e_y)+v_(c_z e_z))/3` is an input-dependent auxiliary
mixture. At Q=0 (and u=s=0 for the joint preparation), every such mixture is
I/2 while each fixed corner output stays pure. Mixture positivity neither
identifies it with an output state nor constructs a readable Record instrument.
All probabilities below are conditional on an opportunity; no formation rate
is inferred. Address/Bloch covariance refers to simultaneous mathematical
rotation of these supplied inputs, not a derived physical stencil.

## 2. Frozen Local Distribution

Let

```text
D = {+e_x,-e_x,+e_y,-e_y,+e_z,-e_z}
```

and write each neighboring Record content as

\[
 \rho_n={I+v_n\cdot\sigma\over2},\qquad \|v_n\|\leq1.       \tag{1}
\]

Define

\[
 S(v)=\operatorname{STF}\!\left[
 {1\over4}\sum_{n\in D}(nv_n^T+v_nn^T)\right].              \tag{2}
\]

For `tau=1/24`, the six axis probabilities are

\[
 p_{\pm e_i}={1\over12}+{\tau\over2}S_{ii},                  \tag{3}
\]

and the eight corner probabilities are

\[
 p_c={1\over16}+{3\tau\over8}
 (S_{xy}c_xc_y+S_{yz}c_yc_z+S_{xz}c_xc_z),                  \tag{4}
\]

where `c in {+/-1}^3`.  The associated qubit possibilities have Bloch
directions `+/-e_i` and `c/sqrt(3)`.

For arbitrary six Bloch balls, exact coefficient bounds give

\[
 |S_{ii}|\leq{4\over3},\qquad |S_{ij}|\leq1.                 \tag{5}
\]

Consequently every axis probability is at least `1/18`, every corner
probability is at least `1/64`, and their exact sum is one.  No target fixture
is used in this proof.

Let

\[
 M(p)=\operatorname{STF}\!\left[
 \sum_{n\in D}p_nnn^T+\sum_c p_c{cc^T\over3}\right].        \tag{6}
\]

Direct symbolic cancellation gives

\[
 M(p)=\tau S(v).                                               \tag{7}
\]

Both the map from the 18 neighbor Bloch coordinates to `S` and the map from
the five `S` coordinates to the fourteen probabilities have rank five.

## 3. Direction/Corner Preparation Witness

For a trace-free spatial tensor `Q`, the preregistered positive-control
preparation is

\[
 v_n(Q)=-{3\over4}Qn.                                         \tag{8}
\]

It is used only to test reachability.  The supplied conditional law (2)--(4) receives the
six `rho_n`; it never receives `Q`, H1/H2, a TT coefficient, momentum, or an
orbit label.

For a sign triple `c`, select the three neighbors `c_i e_i` and take their
equal mixture.  Its Bloch vector is

\[
 b_c={v_{c_xe_x}+v_{c_ye_y}+v_{c_ze_z}\over3}
     =-{Qc\over4}.                                             \tag{9}
\]

Equation (9) defines an auxiliary mixture, not the fixed outcome state with Bloch vector `c/sqrt(3)`, and introduces no diagonal lattice site.  Since it is a convex mixture of three
actual neighbor contents, it is a mathematical qubit state whenever those contents
are.

Equations (2), (7), and (8) give

\[
 S=-{3\over4}Q,\qquad M=-{Q\over32},\qquad Q_{\rm source}=-32M=Q. \tag{10}
\]

The factors in (10) were frozen in the preregistration before target
execution.

## 4. Exact H1 And H2 Tests

The spatial tensor uses the action's normalized symmetric basis: diagonal
slots have unit matrix entries and off-diagonal coefficient slots multiply
matrices with entries `1/sqrt(2)`.

For H1, the supplied tensor is

\[
 Q_{H1}=\begin{pmatrix}
 0&0&-1\\
 0&0&1/\sqrt2\\
 -1&1/\sqrt2&0
 \end{pmatrix}.                                                 \tag{11}
\]

The maximum squared neighbor Bloch norm under (8) is `27/32`; the maximum
composite-corner norm is `(3+sqrt(2))/16`.

For H2,

\[
 Q_{H2}=\begin{pmatrix}
 (3+\sqrt3)/4&-\sqrt6/4&0\\
 -\sqrt6/4&-(1+\sqrt3)/4&1/\sqrt2\\
 0&1/\sqrt2&-1/2
 \end{pmatrix}.                                                 \tag{12}
\]

The maximum squared neighbor norm is
`(81+27 sqrt(3))/128`, strictly below one.  The maximum composite-corner norm
is `3 sqrt(2)/64 + sqrt(3)/16 + 3/16`, also strictly below one.

For both tensors:

- all six neighbor states and all eight composite mixtures are positive;
- all fourteen probabilities are positive and normalized;
- (10) returns every normalized tensor coefficient exactly;
- the target orbit has 24 elements and the same law works in every frame;
- no scalar `A1` trace is introduced.

## 5. Native Forward And Actual-Reverse Source

Let `F` and `F_reverse` be the frozen native maps from the ten normalized
symmetric coefficients to the full action source.  Their full ranks are ten.
On the common trace-free module, both ranks are five.

Substituting the source moment (10) gives the exact H1 and H2 forward sources
and the exact literal actual reverses.  The reverse uses the inherited
literal `(p,q)->(p+q,-q)` map, not an adjoint surrogate.  One common spatial
moment therefore supplies the complete coefficient input to both orientations.

This is an algebraic composition with the native action map.  It does not by
itself prove that the action's phase and temporal factors occupy the same six
physical Record contents.

## 6. Symbolic Open-Family Holdout

After freezing all coefficients, the runner evaluates

\[
 Q(a,b,d,e,f)=\begin{pmatrix}
 a&d&e\\ d&b&f\\ e&f&-a-b
 \end{pmatrix}.                                                 \tag{13}
\]

Symbolically, not at selected samples,

\[
 -32M(p(v(Q)))=Q                                                \tag{14}
\]

with Jacobian rank five.  On the full rational box

```text
|a|,|b|,|d|,|e|,|f| <= 1/4,
```

the maximum squared neighbor norm is `27/128` and the maximum composite-corner
norm is `9/128`. The original deterministic rational interior sample is
preserved historical evidence; the current proof uses the symbolic identity
and all 32 box vertices, without replaying that sample.

This open-family identity is why the positive result is not an H1/H2 lookup
or interpolation.

## 7. Law Statistic Versus Realized Record

Equations (3)--(4) are the **law-level distribution**.  A forming Record locks
one of its supported one-site possibilities.  The tensor (6) is a statistic
of that distribution, **not the realized one-Record outcome**.  Across
repeated comparable Records, frequencies can in principle infer the
probabilities and hence the moment; one individual outcome does not equal the
five-component tensor.

This separation matches the minimal Admissibility/Record wording.  It does
not supply formation site, rate, a realized draw mechanism, or an operational
tomography protocol.

## Exact downstream equality and scope

Source equality follows by substitution into the explicit linear exterior
model in the [fixed-source note](ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md).
The corrected entrypoints test exact reconstructed coefficients/coordinates;
complete action phases and forward/reverse vertices then agree as functions
of those identical arguments. This is conditional composition, not a fresh
rerun of the historical Schur or physical compiler. Rotation identities and
the full original finite box remain checked. Convexity bounds on squared
norms extend the finite vertex maxima to the whole supplied parameter box.

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
