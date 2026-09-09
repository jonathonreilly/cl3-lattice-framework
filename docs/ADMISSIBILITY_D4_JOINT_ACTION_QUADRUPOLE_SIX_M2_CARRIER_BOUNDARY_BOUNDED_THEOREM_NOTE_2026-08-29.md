---
claim_id: admissibility_d4_joint_action_quadrupole_six_m2_carrier_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "A supplied linear six-qubit preparation and decoder carries scalar/vector/STF coordinates of ranks 1+3+5 with a strict 512-vertex box; no physical preparation or event rate selected."
claim_type_reason: "Exact finite conditional algebra; scientific assumptions and physical supplier boundaries are explicit."
---

# Joint Action/Quadrupole Six-`M2` Carrier Boundary

**Date:** 2026-08-29; corrected 2026-09-09

**Type:** bounded_theorem

**Standing:** conditional finite mathematics; formal audit deferred.

A supplied linear six-qubit preparation and decoder carries scalar/vector/STF coordinates of ranks 1+3+5 with a strict 512-vertex box; no physical preparation or event rate selected.

## Primary verification

Primary runner: [`admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py`](../scripts/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py).

Independent checker: [`independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py`](../scripts/independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py).

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

Current conditional predecessor: [ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29](ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md).

**Two different corner objects.** The fourteen fixed output possibilities have
Bloch vectors `±e_i` and `c/sqrt(3)` and hence are pure states. Separately,
`b_c=(v_(c_x e_x)+v_(c_y e_y)+v_(c_z e_z))/3` is an input-dependent auxiliary
mixture. At Q=0 (and u=s=0 for the joint preparation), every such mixture is
I/2 while each fixed corner output stays pure. Mixture positivity neither
identifies it with an output state nor constructs a readable Record instrument.
All probabilities below are conditional on an opportunity; no formation rate
is inferred. Address/Bloch covariance refers to simultaneous mathematical
rotation of these supplied inputs, not a derived physical stencil.

## 1. Result up front

The action information and the common spin-two geometry can coexist in the
same six neighboring qubit conditions.  They do not merely fit by a dimension
count: one frozen positive preparation, one exact decoder, and the unchanged
Block-09 probability rule pass H1, held-out H2, every proper-cubic frame, and
an open nine-parameter neighborhood.

For the six signed spatial directions `n`, let `Q` be a real symmetric
trace-free `3x3` tensor.  Normalize the four local action coordinates as

\[
 u=(p_0,p_1,p_2)/\pi,\qquad s=p_3/\pi .
\]

The preregistered Bloch vectors are

\[
 v_n(Q,u,s)=-\frac12Qn+\frac18\left(sn+u\mathbin{\times}n\right).
 \tag{1}
\]

Each neighbor condition is the ordinary qubit state

\[
 \rho_n=\frac12(I+v_n\cdot\sigma).
\]

Define the odd-shell matrix

\[
 F(v)=\frac12\sum_{n=\pm e_i}v_n n^T .                 \tag{2}
\]

Then exactly

\[
 F=-\frac12Q+\frac18\left(sI+[u]_\times\right),       \tag{3}
\]

so its three irreducible pieces decode independently:

\[
 Q=-2\,\operatorname{STF}(\operatorname{sym}F),\qquad
 s=\frac83\operatorname{tr}F,\qquad
 u=8\,\operatorname{axial}(\operatorname{skew}F).     \tag{4}
\]

The ranks are `1+3+5=9`: scalar time action, spatial action vector, and the
`E+T2` quadrupole.  The remaining nine even-shell coordinates are unused by
this construction.

The registered outcome is **`JOINT-CARRIER`**.  This closes the existence of
the same-shell action-state solder at the condition-content level.  It does
not yet say why the causal dynamics prepares (1), why Nature selects these
gains, or how an outcome becomes a readable permanent Record.

## 3. Why the joint carrier is exact

Equation (2) is the natural matrix made from the signed spatial address and
the Bloch-vector content.  Under a proper cubic rotation `R`,

\[
 F\longmapsto RFR^T.
\]

Every real `3x3` matrix decomposes uniquely as

\[
 \mathbb R^{3\times3}
 =\underbrace{A_1}_{\text{trace}}
 \oplus\underbrace{T_1}_{\text{antisymmetric}}
 \oplus\underbrace{(E\oplus T_2)}_{\text{symmetric trace-free}} .
 \tag{5}
\]

The primary Jacobians have ranks `1`, `3`, and `5`; their stacked rank is
`9`.  The preparation Jacobian also has rank `9`, and composing preparation
with decoding gives the exact nine-dimensional identity.  All identities
intertwine in all 24 frames, including the handed cross-product term.  Proper
rotations are essential here; no reflection or chirality claim is made.

This is more than the Block-08 module-capacity result.  Block 08 found the
five-dimensional common representation.  Equations (1)--(5) supply one
strictly positive quantum carrier that simultaneously owns that representation
and the four action coordinates.

## 4. The probability law is unchanged

Block 09 uses only

\[
 S(v)=\operatorname{STF}(\operatorname{sym}F(v)).
\]

The scalar and antisymmetric action terms vanish identically under this
projection.  Consequently

\[
 S=-\frac12Q                                             \tag{6}
\]

for every `Q,u,s`, not merely at the targets.  The six axis and eight
composite-corner probabilities are exactly the same functions of `S` as in
Block 09.  They retain:

- exact normalization;
- the universal full-Bloch-domain axis floor `1/18`;
- the universal full-Bloch-domain corner floor `1/64`;
- rank-five `E+T2` response;
- no diagonal lattice-site input.

With `tau=1/24`, their trace-free second moment is

\[
 M=\tau S=-\frac1{48}Q,
 \qquad Q_{\rm source}=-48M=Q .                         \tag{7}
\]

Thus adding the action carrier cannot alter the conditional outcome
probabilities used for the geometry source.  The source gain changed from the
Block-09 preparation witness only because (1) deliberately leaves additional
Bloch-ball headroom; the probability law itself did not change.

## 5. Exact H1 and held-out H2 results

For each target, the runner constructs separate incoming and outgoing shells
from the frozen action points and the same target quadrupole.  It decodes the
four coordinates only from those six local contents. Equality of phases,
centered action vertices and literal actual reverse follows by substitution
into their stated functions of these exactly identical coordinates.

| test | H1 | held-out H2 |
|---|---:|---:|
| incoming action decode | exact | exact |
| outgoing action decode | exact | exact |
| transfer decode | exact | exact |
| both Clifford phase orientations | exact | exact |
| centered forward vertices | exact | exact |
| literal actual-reverse vertices | exact | exact |
| native common quadrupole source | exact | exact |
| proper-cubic frames | `24/24` | `24/24` |
| strict neighbor positivity | yes | yes |
| strict composite-corner positivity | yes | yes |

The strongest exact norm bounds observed are

\[
\begin{aligned}
 \max\|v_n\|^2_{H1}
 &=\frac{1139}{2304}+\frac{\sqrt2}{32},\\
 \max\|v_n\|^2_{H2}
 &=\frac{647}{2304}+\frac{5\sqrt6+17\sqrt3}{192},
\end{aligned}
\]

both far below one.  The corresponding corner-mixture maxima are

\[
 \frac{1793}{20736}+\frac{\sqrt2}{36}
\]

for H1 and

\[
 \frac{4483}{41472}+\frac{\sqrt6}{1152}
 +\frac{7\sqrt2}{216}+\frac{127\sqrt3}{3456}
\]

for H2.  These are convex mixtures of three nearest-neighbor conditions, not
states on diagonal corner sites.

H2 was frozen as the held-out target.  It contains the `E` doublet absent
from H1, so its success is the decisive check that this is a common
`A1+T1+E+T2` carrier rather than a disguised H1 fit.

## 6. Open-family test

Let

\[
 Q(a,b,d,e,f)=
 \begin{pmatrix}
 a&d&e\\ d&b&f\\ e&f&-a-b
 \end{pmatrix}
\]

and treat `(u_x,u_y,u_z,s)` as four more independent symbols.  The decoded
nine-vector is symbolically identical to the input nine-vector, and its
Jacobian has rank `9`.

Every one of the `2^9=512` vertices of

\[
 |a|,|b|,|d|,|e|,|f|,|u_x|,|u_y|,|u_z|,|s|\le\frac14
\]

was checked exactly.  The maxima are

\[
 \max\|v_n\|^2=\frac{131}{1024},\qquad
 \max\|v_{\rm corner}\|^2=\frac{395}{9216}.
\]

This gives substantial strict headroom and defeats the interpretation that
the result survives only on two isolated fixtures.

## 7. What is closed and what remains open

| seam | disposition |
|---|---|
| same six `M2` conditions carry action plus quadrupole | **closed constructively** |
| exact `A1+T1+E+T2` decomposition | **closed, rank 9** |
| action contamination of geometry probability | **absent identically** |
| H1 forward/actual reverse | **closed exactly** |
| held-out H2 forward/actual reverse | **closed exactly** |
| H1/H2 common native quadrupole source | **closed exactly** |
| target and open-family state positivity | **closed strictly** |
| action-state solder existence at condition-content level | **closed constructively** |
| uniqueness or dynamic selection of gains | **open** |
| causal preparation of the neighboring conditions | **open** |
| endpoint/relay branch attached to readable permanent Record | **open** |
| formation rate, realized history, gravity coupling | **not executed** |

The phrase “action-state solder” must now be split carefully.  The earlier
existence question—can the action and geometry be encoded together in actual
positive `M2` contents?—has a positive answer.  The stronger causal question—
does the framework dynamics prepare this particular encoding before the event
whose probabilities it conditions?—is still unanswered.  In that precise
sense, **causal preparation remains open**.

## 8. Probability, possibility, and Record scope

The fourteen possibilities are alternatives of the quantum condition law.
Their probabilities are law-level statistics determined by the neighboring
conditions.  The tensor `M` in (7) is a statistic of that distribution, not
the outcome of one realized draw.

One realized Record supplies one axis or composite-corner outcome.  Repeated
comparable Records can estimate the distribution and therefore infer its
moment.  Nothing here claims that a single Record reveals all nine carrier
coordinates or that the overlapping qubit conditions are themselves a
readable classical register.

The construction also does not use a same-event post-state to set its own
probability.  The remaining campaign must supply a strictly causal-past
preparation or relay and a separate permanent pointer write.

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
