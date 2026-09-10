---
claim_id: admissibility_dirac_kahler_global_dressing_involution_positivity_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "For a chosen d=2 antiperiodic Z8_t x Z4_x finite operator built inline, the displayed 512-real dressing ansatz with spatial blocks in span{I_4,D_x,C+C^T,C-C^T} has a 132-dimensional reflection-real, Gram-Hermitian linear space at c=5/13 and c=3/5. Its 64-real anti-diagonal restriction is one-dimensional and has exactly the two involutions +/-A_star, whose 16x16 Grams have inertia (8,8,0) at both fixtures. Separately, only at c=5/13, the K_A=I_16 equations have rank 184 and a 72-dimensional real fiber containing a pinned non-involution. No action-derived seam selector, full joint involution-positivity classification, transporter, or physical positivity theorem is claimed."
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
target_blocker_text: "A transition-compatible common differential/range-invariance lemma, the actual ADM/history transporter, reflection positivity, joint gravity, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Derive an action-selected seam operator before testing whether any finite dressing can enter an ADM/history transporter or reflection-positivity construction."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact rational finite-matrix identities and a one-variable restricted classification on the declared chosen d=2 carrier; no physical selector or size-uniform theorem"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite Global Dressing, Involution, And Positivity Certificates

**Date:** 2026-08-15

**Campaign block:** 109

**Type:** `bounded_theorem`
**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py`](../scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py)

## 1. Result and boundary

The runner constructs a chosen finite operator on `Z8_t x Z4_x`. It uses one
fine Grassmann mode per site, mass `m=9/20`, unit volume, antiperiodic time
closure, link-centered reflection `theta(t)=-1-t`, and the step-shear profile

```text
(-c,-c,-c,0,c,c,c,0).
```

The two displayed exact fixtures are `c=5/13` and `c=3/5`. These rational
choices make a finite algebraic test. An action-derived physical seam
selection is not supplied. In particular, the calculation does not select
this `Q`, shear profile, dressing, or seam from the microscopic action.

Each `4 x 4` spatial block belongs to the complex span of `I_4`, `D_x`,
`C+C^T`, and `C-C^T`, where

\[
 D_x=\operatorname{diag}(1,-1,1,-1)
\]

and `C` is the four-cycle shift. `D_x` is not circulant. The complete
displayed class is therefore a four-structure spatial ansatz, rather than a
class of spatial-circulant blocks. With 64 time-slice blocks, four structures,
and real and imaginary coefficients, it has 512 real coordinates.

For each fixture, reflection reality has rank 256. Hermiticity of the
`16 x 16` dressed two-history Gram adds rank 124 on the reality-fixed
coordinates. The stacked rank is 380 and the resulting linear space has
dimension

\[
 512-380=132.                                           \tag{1}
\]

This is a statement about each displayed finite fixture. It is not an
action-selection theorem, a curved reflection-positivity theorem, or a
continuum result.

## 2. Exact finite certificates

Let `P` be the 32-dimensional reflection permutation, `G_c=Q_c^{-1}` the
propagator of the chosen finite operator, and `S_+` the embedding of the
sixteen positive-time sites. The runner uses the target-arm convention

\[
 \mathcal K_A(c)=\overline{S_+^T A G_c P S_+}.           \tag{2}
\]

It checks the following facts with exact SymPy arithmetic.

1. At both fixtures, the reflection-real and Gram-Hermitian dressing space
   has dimension 132.
2. The undressed choice `A=I_32` is reflection-real but fails Gram
   Hermiticity at the primary fixture `c=5/13`. The maximum exact defect is
   the pinned nonzero rational stored as `UNDRESSED_DEFECT` in the runner.
3. The anti-diagonal dressing

   \[
   (A_\star)_{i,7-i}=s_iD_x,
   \qquad s=(1,-1,1,-1,-1,1,-1,1),             \tag{3}
   \]

   is reflection-real, Gram-Hermitian, and satisfies `A_star^2=I_32`; it is
   therefore an exact involution in the displayed finite class.
4. Within the 64-real anti-diagonal support, the stacked reality and
   Hermiticity equations have rank 63 at both fixtures. Their kernel is the
   line `lambda A_star`. The involution equations reduce to

   \[
   \lambda^2-1=0,                               \tag{4}
   \]

   so the only involutions in this restricted class are `+A_star` and
   `-A_star`.
5. The `16 x 16` Grams of both signs have exact inertia `(8,8,0)` at both
   fixtures. Thus this restricted anti-diagonal involution class is disjoint
   from positive semidefinite Grams.

The positivity calculation is separate. The positive-fiber calculation is
executed only at `c=5/13`. For the equation

\[
 \mathcal K_A(5/13)=I_{16},                             \tag{5}
\]

the real map has rank 184 in 256 real parameters, the augmented rank is also
184, and the solution fiber has dimension 72. The runner checks one pinned
exact representative. Its Gram is `I_16`, while

\[
 \operatorname{rank}(A^2-I_{32})=32,                    \tag{6}
\]

so that representative is not an involution. No positive-fiber result is
executed for `c=3/5`.

The exact `A_star` has zero central `{0,1}`-time block and is therefore
window-invisible in the displayed sense. At the primary fixture, the
associated 32-coordinate homogeneous central-window system has rank 24 and
contains the zero solution. This finite window check is not a locality or
transporter theorem.

## 3. Claims removed from the live surface

Historical prose described a 37-dimensional subspace, large pair scans, and
gamma extensions. Those computations were not executed by this runner. The
reported 666/8,646 pair counts and any gamma-extended classification are
recovery history only and carry no current scientific claim.

The live calculation does execute a four-pair reduction inside the single
anti-diagonal line in equation (4). That small reduction must not be confused
with the historical pair scans.

The full 132-dimensional involution-positivity variety remains open. The
runner does not establish whether another involution, including a mixed
spatial-structure involution, has a positive Gram. It also does not derive a
physical seam operator from the action.

## 4. Authority and actual runtime inputs

The scientific context is the current corrected supplier
[Dirac–Kähler shifted origins, frame gauge, and overlap Hodge](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
That note supplies a positive overlap-Hodge construction and explicitly
leaves the actual ADM/history transporter and reflection positivity
unexecuted. It does not supply the seam selector used here. The present
runner rebuilds its chosen finite matrices inline.

The literal `AUDIT_INPUT_PATHS` closure is:

1. this theorem note;
2. [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md);
3. [`docs/audit/data/axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json);
4. the corrected supplier note linked above.

There is no imported scientific helper runner in Block 109. Standard Python
and SymPy packages are environment dependencies. The runner binds the three
external repository inputs by SHA-256 and uses this note as the claim surface.
Historical Block 103--108 files and the released caches are not live runtime
inputs.

## 5. No-go discipline for the restricted negative claim

The only negative theorem here is the anti-diagonal result in Section 2. The
following packet stress-tests that bounded statement.

**N1 — alternative-route enumeration.** Five distinct routes are visible in
the executed calculation: enlarge the anti-diagonal linear kernel; seek
additional roots of its involution ideal; reverse the sign of `A_star`; use
the exact positive fiber outside that line; or leave the anti-diagonal
support and solve the full 132-dimensional variety. The first three are
closed only in the declared anti-diagonal class. The last two remain live.

**N2 — wall-independence audit.** `W1` is the rank-63 linear restriction,
`W2` is the polynomial equation `lambda^2-1`, and `W3` is the exact Gram
inertia `(8,8,0)` for both roots. These walls are sequential rather than
independent: `W2` is evaluated on the `W1` line, and `W3` is evaluated on the
`W2` roots. The negative conclusion uses the whole chain and claims no extra
confidence from treating the walls as independent.

**N3 — hidden-wall scan.** The proof assumes the chosen torus, boundary
condition, reflection, step profile, two rational fixtures, positive-time
span, target-arm Gram convention, and four-structure block ansatz. It does
not assume or prove locality, modular selection, action derivation, curved
transport, gravity compatibility, or persistence with lattice size.

**N4 — residual matching.** The exact positive fiber is outside the
anti-diagonal involution set and its pinned member fails involution by full
rank. It is evidence that positivity equations are feasible at one fixture;
it is not evidence that the joint variety is empty or nonempty.

**N5 — resolution audit.**

- `per_element:` exact matrix identities and rational equations are checked.
- `per_site:` the chosen one-mode-per-site `Z8_t x Z4_x` carrier is checked.
- `per_mode:` both shear fixtures enter the 132-dimensional and
  anti-diagonal certificates; the positive fiber enters only at `c=5/13`.
- `per_block:` all eight anti-diagonal blocks of `A_star` are checked.
- `lattice_wide:` not executed; no size-uniform theorem is claimed.

**N6 — partial-closure path scan.** The exact remaining routes are the full
mixed-structure involution equations, an action-derived selector, and a
transport-compatible positivity construction. This note advances none of
them beyond the finite certificates stated above.

**N7 — steelman.** A candidate outside the anti-diagonal support could mix the
132 linear directions so that `A^2=I_32` and the Gram is positive. The
positive fiber shows that Gram positivity itself is not inconsistent at the
primary fixture. The present negative theorem has no force against that
candidate.

**N8 — cross-cycle echo.** No prior historical no-go is imported as proof.
The old Block 103--108 ancestry and its absent files are archived provenance.
Only the equations re-executed by the current runner support this claim.

## 6. Disposition

This is a bounded finite certificate. It is not a transporter impossibility.
No axiom amendment is justified. The actual ADM/history transporter remains
open, the gravity constraint quotient remains unexecuted, and formal audit
and retention remain outside this authoring unit.
