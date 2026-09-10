---
claim_id: admissibility_dirac_kahler_carrier_reflection_blocker_bounded_theorem_note_2026-08-19
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md
claim_type: bounded_theorem
claim_scope: "For the displayed 4 by 4 quotient, Block 105 staircase Hodge carrier, primary connection fixture s_x=3/5 and s_t=4/5, four origins, and symbolic real mass, all sixteen dressed actions have Hermitian part m H_q and H_q is positive definite. The displayed H_q has no preserver in the enumerated 256 signed lattice reflections. For the named half-carrier compression, a symbolic two by two minor excludes PSD whenever m is nonzero. The inertia census is only at m=2/7, the zero-mass inertia is one named corner, and the all-zero undressed action is an explicit PSD counterexample. Three carrier controls and two weight assignments are finite controls. No general relation between global Hodge invariance and compressed Hermiticity, all-carrier or all-weight result, zero-mass no-PSD theorem, reflection-positivity result, or OS no-go is claimed."
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
artifact_role: theorem
claim_type_reason: "The exact matrix equalities, finite reflection enumeration, symbolic minor, and named fixture counts are theorem-level statements on the declared finite fixture; the untested involution and carrier classes keep the result bounded."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Carrier Reflection Certificates On The Displayed Fixture

**Date:** 2026-08-19

**Campaign block:** 142

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. This note adopts no premise and changes no
axiom or retained claim.

**TOE accounting:** zero obligation retirement. No axiom amendment is
justified. No TOE percentage moves. The retained-positive end-to-end theory
count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py`](../scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py)

**Construction source:**
[Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
supplies the reviewed Hodge fixture. The current premise boundary is
[Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md); this note does not add to it.

## 1. Corrected Result

The runner rebuilds one exact finite system:

\[
 L_x=4,\qquad T_{\rm physical}=4,\qquad T_{\rm cover}=8,
 \qquad {\cal O}=\mathbb Z_2^2,
 \qquad s_x=\frac35,\quad s_t=\frac45.                  \tag{1}
\]

It uses the Block 105 staircase overlap-Hodge carrier, symbolic real mass
`m`, and primary weights `x=(0,0,1/2,-1/3)`. On this fixture all sixteen
dressed edge actions satisfy

\[
 Q_{ij}+Q_{ij}^{\dagger}=2mH_q.                          \tag{2}
\]

Equivalently, the executable certificate uses the plain-text identity
`Q_ij + Q_ij^dagger = 2 m H_q`. The real symmetric `H_q` has inertia
`(16,0,0)`, and all sixteen leading principal minors are positive. The
atlas-global mass form is positive definite for `m>0`.

The four displayed chart actions have a two-dimensional difference span and
the exact sum rule

\[
 \dim\operatorname{span}\{Q_i-Q_{(0,0)}\}=2,
 \qquad Q_{(0,0)}+Q_{(0,1)}=Q_{(1,0)}+Q_{(1,1)}.          \tag{3}
\]

This rules out representing all three chart differences by one
common scalar multiple of a single generator on this fixture.

For the displayed `H_q`, exact backtracking finds **only the identity**
among all site permutations preserving `|H_q|` entrywise. The runner also
enumerates the 256 signed lattice reflections
`(t,x) -> (b-t,a-x)`, including sign twists. All descend through the
antiperiodic quotient and zero preserve `H_q`. Thus **no signed lattice
reflection** in that enumerated family preserves this displayed Hodge form.
This finite-family result does not classify general metric-adapted
involutions.

## 2. Compressed Hermiticity Is Separate

The historical draft treated global Hodge invariance as necessary for the
Hermiticity of the compressed pairing. That implication is false. If
`theta=theta^dagger` and `Delta^dagger=-Delta`, then

\[
 \operatorname{herm}(\theta\Delta)
   =\frac{\theta\Delta-\Delta\theta}{2}.                  \tag{4}
\]

In plain text, `herm(theta Delta)=(theta Delta-Delta theta)/2`.
Compression can remove or retain different parts of the global defect.
Global Hodge invariance is not necessary for a particular compressed matrix
to be Hermitian.

The runner records **three fixture controls**:

1. A shear-free overlap carrier, whose volume profile remains nonconstant,
   gives 16 Hermitian compressed pairings while the named `theta` is not a
   global Hodge symmetry.
2. A constant carrier gives an exact global Hodge symmetry and 1 Hermitian
   compressed pairing out of 16 at the fixed nonzero connection fixture.
3. The staircase carrier gives 0 Hermitian compressed pairings out of 16 and
   has no global `theta`-Hodge symmetry.

These values distinguish the two properties. They do not prove a general
shear or nonconstancy law, and the runner does not infer compressed
Hermiticity from global invariance or its failure.

## 3. The Valid Nonzero-Mass Minor

For the named half-carrier compression, set

\[
 B_{ij}=[\theta Q_{ij}]_{++},\qquad
 A_{ij}=\frac{B_{ij}+B_{ij}^{\dagger}}2.                 \tag{5}
\]

For every left chart in the symbolic `m,w,s_x,s_t` calculation,

\[
 A[1,1]=0,\qquad A[1,2]=-\frac{19m}{160},                \tag{6}
\]

so the corresponding principal minor is

\[
 \det A[\{1,2\},\{1,2\}]
   =-\frac{361m^2}{25600}.                               \tag{7}
\]

Equation (7) **excludes positive semidefiniteness whenever m is nonzero**.
This is the all-parameter statement supplied by the symbolic calculation.
In the runner's plain-text indexing, `A[1,2]=-19m/160`.

The following counts have narrower scopes:

- At fixture mass `m=2/7`, the sixteen primary-weight edges have inertia
  census exactly `{(2,0,6),(4,0,4),(6,0,2)}`; none is PSD.
- The result `(0,4,4)` is **only at m=0, s_t=0, s_x=3/5** for the named
  `(0,0)` chart compression.
- With `m=s_x=s_t=0`, the undressed `(0,0)` self-edge action is zero. Its
  compression is the **zero positive-semidefinite counterexample**. This
  all-zero parameter action shows why (7) cannot become a generic zero-mass
  no-PSD claim.

The exact inertia implementation counts repeated eigenvalues with their
multiplicities. Its local controls include

\[
 \operatorname{inertia}\operatorname{diag}(1,1,-2,-2,0)=(2,1,2),
 \qquad \operatorname{inertia}(0_{5\times5})=(0,5,0).    \tag{8}
\]

It verifies Hermiticity, rational characteristic-polynomial coefficients,
zero-root multiplicity against matrix nullity, and that all counts sum to the
matrix dimension.

## 4. Weight And Parent Scope

The alternative weights `x'=(0,7/3,-5/11,2)` reproduce (6), the symbolic
anti-Hermitian rank reported by the primary calculation, and the `m=2/7`
inertia census. These are **two tested weight assignments**. They do not
establish an all-weight result. The four self-edge dressings vanish for both
assignments because each uses `x_i-x_i=0`.

The correction `Delta*` is `s_t`-only and vanishes at `s_t=0`. The
displayed `H_q`, the finite-family reflection certificate, and (7) are
independent of `s_t`, so that bounded nonzero-mass certificate **does not
collapse at s_t = 0**. The separate zero-mass statement remains limited to
the single corner above.

**Historical parent counts are not executed** by this runner. The original
twenty-six-file input surface, including every transitive helper body, remains
byte-for-byte recoverable under
`.claude/science/physics-loops/released-reflection-recovery-20260910/original/`.
The new helper extracts only the definitions used here and identifies each
source commit, blob, AST node, and line interval. The reviewed Block 105
module is imported intact.

## 5. Executable Checks

The original check IDs are preserved with corrected meanings:

- **A-authority:** the literal audit-input tuple is complete, every non-self
  filesystem input is SHA-256 bound, and no moving `origin/main` or ancestry
  condition is used.
- **B-atlas-global-quadratic-form:** (2), positive definiteness of the
  displayed `H_q`, the affine correction, and (3).
- **C-reflection-blocker:** the absolute-profile backtracking and finite
  256-member signed-reflection enumeration.
- **D-decoupled-cause-controls:** the three controls in Section 2; the
  historical ID is retained, while no general causal implication is claimed.
- **E-non-positivity-certificate:** the nonzero-mass minor, separately scoped
  fixture counts, zero-action counterexample, and two inertia controls.
- **F-weight-freedom:** the historical ID is retained for the two-weight
  control; it is not an all-weight theorem.
- **G-rider-break:** `s_t`-independence of the finite reflection result and
  nonzero-mass minor, with the zero-mass scope kept narrow.
- **H-note-scope:** the claim boundaries, firewalls, and exact N5 fence.

The proposed bounded producer cap is 120 seconds, with a separate 1 GiB
peak-RSS watcher on macOS. It does not use `RLIMIT_AS`.

## 6. Finding Dispositions

- **R142-1:** corrected. Global Hodge invariance and compressed Hermiticity
  are separated; (4) and the actual controls replace the false implication.
- **R142-2:** corrected. Authority is tied to literal, present filesystem
  inputs by SHA-256; moving refs, stale parents, and ancestry are absent.
- **R142-3:** corrected. Only the measured compression, minor, three carrier
  controls, two weights, and named fixture counts remain. Unexecuted parent
  propagator, gluing-tail, nilpotency, and curvature counts are not imported.
- **R142-4:** corrected. The negative minor is stated for `m != 0`, the
  `m=0` inertia is a narrow corner, and the all-zero PSD counterexample is
  explicit.

## 7. N1--N8 Stress Test And Wall W1

- **N1:** Metric-adapted involutions, other carriers, and completion terms
  remain open.
- **N2:** The finite signed-reflection enumeration and nonzero-mass minor are
  separate certificates.
- **N3:** The fixed atlas, staircase Hodge carrier, compression, shears, mass
  specializations, and two weights are explicit.
- **N4:** Equation (3) records only the displayed chart-difference span; it
  does not reproduce historical parent tail counts.
- **N5:** The resolution fence below states each quantifier.
- **N6:** The global mass form remains a positive finite result.
- **N7:** A metric-adapted involution outside the 256 signed maps could still
  supply the required geometry.
- **N8:** No result from the flat or parent lanes upgrades this fixture.

**W1.** On the displayed `H_q`, no member of the enumerated signed lattice
reflection family preserves the Hodge form. Metric-adapted involutions are
**not searched**. This is not an OS no-go and not a curved OS no-go.

## 8. Firewalls And Independence

The actual ADM/history transporter remains unexecuted. The gravity constraint
quotient remains unexecuted. Reflection positivity, the forced self-edge
decision, coboundary admissibility, the joint-lane program, Records,
retention, axiom amendment, obligation retirement, and TOE movement remain
outside the claim. These are hard firewalls.

The historical solve/check round had **cross-context** checking within one
model family. This disclosure supplies provenance only. It is not independent
audit authority, and this corrected source does not synthesize an audit
verdict.

## 9. Exact N5 Resolution Fence

```text
N5: per_element: on the displayed 4x4 quotient fixture the sixteen dressed edge actions obey Q_ij + Q_ij^dagger = 2 m H_q, and the extracted coboundary correction is anti-Hermitian and rank 16 at the primary connection fixture, while its symbolic expression is s_t-only and zero at s_t=0
per_site: the parameter-free H_q has 15 absolute-row fingerprints and only the identity preserves its absolute profile; the separately enumerated 256 signed lattice reflections all descend and none preserves H_q, which is a finite-family statement rather than a classification of metric-adapted involutions
per_mode: the shear-free, constant, and staircase carrier calculations are three fixture controls that distinguish compressed-pairing Hermiticity from global Hodge invariance; herm(theta Delta)=(theta Delta-Delta theta)/2 for skew Delta, so neither global invariance nor shear/nonconstancy is promoted to a general implication
per_block: for the specified compression the symbolic minor is -361 m^2/25600 and excludes positive semidefiniteness whenever m is nonzero; the three-inertia census is only at mass 2/7, the (0,4,4) result is only at m=0, s_t=0, s_x=3/5 for the named chart, and the all-zero parameter action gives an explicit zero positive-semidefinite counterexample
lattice_wide: the displayed chart tails span dimension two with the exact sum rule, and the alternative-weight calculation is one second control rather than an all-weight theorem; historical parent propagator, tail-rank, nilpotency, and curvature counts are archived but not executed by this runner
RESULT: the displayed fixture has positive-definite H_q and an exact global mass split, no preserver in the tested signed-reflection family, and a nonzero-mass negative-minor certificate for the named compression; no necessity of global Hodge symmetry, generic carrier law, zero-mass no-PSD theorem, OS theorem, or curved OS theorem follows
DECISION_CUT: metric-adapted involutions, other carriers, completions, the forced self-edges, coboundary admissibility, and the joint-lane program remain live; no premise or audit disposition is adopted here
TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero
```
