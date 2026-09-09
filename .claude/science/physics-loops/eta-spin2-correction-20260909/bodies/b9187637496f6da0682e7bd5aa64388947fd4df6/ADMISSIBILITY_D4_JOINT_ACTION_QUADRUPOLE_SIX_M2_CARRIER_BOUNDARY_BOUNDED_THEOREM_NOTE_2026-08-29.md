---
claim_id: admissibility_d4_joint_action_quadrupole_six_m2_carrier_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "One fixed proper-cubic-covariant preparation of the same six neighboring M2 Record contents carries a normalized local action covector in the scalar-plus-antisymmetric pieces of its odd-shell matrix and the full E+T2 quadrupole in its symmetric trace-free piece. The three sectors have exact ranks 1+3+5=9 and zero mutual leakage. With preregistered gains -1/2 and 1/8, all H1 and held-out H2 incoming/outgoing shells, their composite-corner mixtures, and all 24 proper-cubic images are strictly positive. Decoding those shells reproduces the exact H1/H2 action phases, centered forward vertices, literal actual-reverse vertices, and native common quadrupole sources. A symbolic nine-parameter family is exact and all 512 vertices of the registered box remain strict. This constructs the action-state solder at the condition-content level but does not derive causal preparation, instrument selection, readable/permanent Record attachment, formation/history, gravity, an axiom amendment, obligation retirement, retained status, or TOE percentage movement."
claim_type_reason: "The decomposition, ranks, positivity bounds, cubic intertwining, action phases, source vertices, common moments, target checks, and 512-vertex neighborhood are finite exact calculations. Standing remains bounded because the preparation gains are constructed rather than dynamically selected, and no causal channel or permanent-Record formation process is supplied."
parent_commit: ac1473f94fd5df2647bda77b22a191987f4aa05f
preregistration_commit: 67accddd65f15396fb810237147ba6902c94a9bc
origin_main: 004f64e1c87dad696b282cf2b526f3e7312dc82d
minimal_axioms_blob: bc23300becfe4e4db57153c0e94cfcdf2338da71
verdict: JOINT-CARRIER
condition_level_action_state_solder: true
causal_preparation: false
permanent_record_attachment: false
obligation_retirement: 0
toe_percentage_movement: 0
---

# Joint Action/Quadrupole Six-`M2` Carrier Boundary

**Date:** 2026-08-29

**Campaign block:** Source/Eta 10

**Type:** `bounded_theorem`

**Standing:** author-side bounded theorem; audit status unset

Primary runner:
[`admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py`](../scripts/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py).

Independent checker:
[`independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py`](../scripts/independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py).

Frozen upstream probability law:
[`ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md`](ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md).

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

## 2. Frozen authority and prospective discipline

The immutable goal and falsifiers were committed at `67accddd65` and pushed
before target execution.  They froze:

- the parent Block-09 delivery and its positive fourteen-possibility law;
- the gains `-1/2` and `1/8`;
- the matrix decoder (2)--(4);
- H1 and held-out H2, forward and literal actual reverse;
- all 24 proper-cubic frames;
- the nine-parameter box `|parameter| <= 1/4`;
- the three registered outcomes and the no-TOE scope.

No gain was searched or refitted after seeing H1 or H2.  Candidate Block 208
is used only as immutable prior evidence that exact endpoint phase statistics
reconstruct H1 while its action-to-`M2` state solder remained open.

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

Thus adding the action carrier cannot alter the Record-formation
probabilities used for the geometry source.  The source gain changed from the
Block-09 preparation witness only because (1) deliberately leaves additional
Bloch-ball headroom; the probability law itself did not change.

## 5. Exact H1 and held-out H2 results

For each target, the runner constructs separate incoming and outgoing shells
from the frozen action points and the same target quadrupole.  It decodes the
four phases only from those six local contents.  It then reconstructs the
existing centered action vertices and literal actual reverse without a
momentum, fixture, or target label.

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

## 9. Axiom and TOE decision

No minimal-axiom edit is justified by this result.  We found one positive
joint carrier rather than two physically complete competing laws or an empty
admissible class.  The axiom already permits one fixed covariant local
distribution; this block makes that route more concrete.

No formal retained obligation is retired because causal preparation,
law/instrument selection, and permanent Record attachment are still missing.
The TOE lane percentages therefore remain unchanged even though route
confidence and the physical frontier have advanced materially.

```text
obligation retirement: 0
TOE percentage movement: 0
```

## 10. Highest-leverage next experiment

The odd shell uses only nine of the six qubits' eighteen Bloch coordinates.
The complementary even-shell kernel is also nine-dimensional.  The next
campaign should test whether a fixed radius-one CPTP causal update can:

1. prepare the joint odd-shell carrier from prior neighboring Records;
2. use the even-shell sector or a strict past relay as a readable pointer;
3. reproduce the same fourteen outcome rates without same-event feedback;
4. write one orthogonal, repeatable, permanent Record outcome; and
5. preserve H1 and held-out H2 forward/actual-reverse sources.

A positive result would move the program from a condition-level local law to
an actual event/update law.  An empty result would identify the exact missing
preparation or pointer primitive and provide a serious axiom-decision input.
