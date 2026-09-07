# U(1) Representation-Positive Registration Kernels Force a Positive Maxwell Germ

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source note sets no audit
verdict, changes no TOE score, and claims no obligation retirement.
**Continuum parent:**
[`COMPACT_U1_QUADRATIC_BASIN_SOURCE_FREE_MAXWELL_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-09-03.md`](COMPACT_U1_QUADRATIC_BASIN_SOURCE_FREE_MAXWELL_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Historical registration context (not a premise edge):**
`archive/notes/docs/GAUGE_LINK_CENTRAL_REGISTRATION_INDUCED_BI_INVARIANT_STEP_KERNEL_THEOREM_NOTE_2026-07-02.md`.
That archived construction supplied a position-classical registration
condition. The finite U(1) Lueders/Fourier formula used here is derived below;
no archival grade or conclusion is imported.
**Current axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Runner:**
[`scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py`](../scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.txt`](../logs/runner-cache/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.txt)

## Claim scope

Let a supplied compact `U(1)` relative-phase transition density, normalized
against mass-one Haar measure, have representation-positive Fourier data

```text
K(theta) = 1 + 2 sum_(n>=1) a_n cos(n theta),
a_n >= 0,                         sum n^4 a_n < infinity.
```

Assume that the kernel is nonconstant. Then the identity is a global maximum
of `K`, and the normalized negative-log potential

```text
V(theta) = -log[K(theta)/K(0)]
```

is finite, even, and `C^4` on a neighborhood of the identity, with

```text
V(0)=0,
V''(0)=kappa
      = 2 sum_(n>=1) n^2 a_n / [1+2 sum_(n>=1) a_n]
      > 0.
```

Thus representation positivity plus nontrivial neighbor dependence fixes the
previously open sign and nondegeneracy of the local quadratic germ. It does
not select the full finite-angle action or the value of `kappa`.

For a finite `U(1)` Peter-Weyl mode set, a supplied positive Lueders central
registration channel induces exactly such nonnegative Fourier data. In the
three-mode carrier `{-1,0,1}`, any supplied two-outcome positive Lueders
registration is necessarily nonconstant. Its induced negative-log kernel
therefore has `kappa>0`. The sharp two-outcome partitions give explicit
curvatures `2/5` or `8/5`; this is a conditional exhibit, not a claim that the
Qubit or Record axiom makes the readout binary.

If one additionally supplies the same local kernel as an isotropic factor on
all temporal and spatial plaquette orientations, the continuum parent applies:
the smooth zero-monopole branch has the source-free Maxwell action and
equations, an exact gauge null, and two transverse local modes. A temporal
registration kernel by itself supplies only the electric/temporal quadratic
block. It has no magnetic restoring block and is not Maxwell.

The theorem therefore closes a real sign bridge but not the whole physics
bridge. The remaining load-bearing input is an orientation-complete local
gauge action, together with the still-open physical identification, charged
source coupling, normalization, and Record-readable observable dictionary.

## 1. Fourier theorem

Absolute convergence of `sum n^4 a_n` permits four termwise derivatives and
makes `K` continuous. For every angle,

```text
K(0)-K(theta)
  = 2 sum_(n>=1) a_n [1-cos(n theta)]
  >= 0.
```

Hence the identity is a global maximum. Since
`K(0)=1+2 sum a_n>=1`, continuity gives a neighborhood on which `K>0`, even
if the kernel has zeros elsewhere. The logarithm is therefore finite and
`C^4` locally. Evenness gives `V'(0)=V'''(0)=0`, while direct differentiation
gives

```text
K'(0)=0,
K''(0)=-2 sum n^2 a_n,
V''(0)=-K''(0)/K(0).
```

Nonconstancy is equivalent to at least one `a_n>0`, so the last expression is
strictly positive. This proves the universal statement. The runner's finite
families and deterministic random families test the formulas and mutations;
they are not used in place of the analytic quantifier.

The negative-log potential can have hard barriers where `K=0` away from the
identity. That does not violate the continuum parent's widened hypothesis,
which requires finiteness and `C^4` only near the flat point.

## 2. Positive Lueders registration supplies the coefficient sign

Let `M` be a finite set of integer `U(1)` representation labels. Supply
positive central Kraus blocks

```text
K_j = sum_(n in M) sqrt[m_j(n)] P_n,
m_j(n)>=0,                  sum_j m_j(n)=1.
```

On the registration parent's supplied position-classical transition surface,
the relative-phase density is

```text
T(theta)
 = (1/|M|) sum_j |sum_(n in M) sqrt[m_j(n)] exp(i n theta)|^2.
```

Its Fourier coefficient at difference `q` is

```text
a_q
 = (1/|M|) sum_j sum_(n,n+q in M)
     sqrt[m_j(n+q)m_j(n)]
 >= 0.
```

Trace preservation gives constant coefficient one. Thus positive Lueders
central registration supplies normalization, inversion symmetry, and
representation positivity rather than assuming their signs independently.
The positivity of the square-root coefficients is load-bearing: the
registration parent gives exact central-scalar counterexamples with negative
representation coefficients outside this subclass.

For `M={-1,0,1}`, suppose there are exactly two Lueders outcomes. Every one of
the three mode columns has positive weight in at least one outcome. If neither
outcome overlapped two distinct modes, the two outcome supports could cover at
most two mode columns. Therefore some row overlaps two modes, at least one
`a_q` is positive, and `kappa>0`.

The three sharp nontrivial partitions reduce, up to reflection, to

```text
T_1(theta)=1+(2/3)cos(theta),       kappa_1=2/5,
T_2(theta)=1+(2/3)cos(2 theta),     kappa_2=8/5.
```

Resolving all three modes separately gives `T(theta)=1` and `kappa=0`. This
control shows that record formation or sharper resolution does not by itself
force a Maxwell germ. What does the work is nonconstant overlap together with
positive representation data.

## 3. Exact relation to Admissibility variation

The current Admissibility axiom states that the local distribution is
determined by and varies with nearest-neighbor conditions, but it does not
give its functional form or values. On the additional shifted-convolution
ansatz

```text
p(theta | phi) = K(theta-phi),
```

where `phi` is a neighboring compact phase condition, the axiom's variation
clause has a precise local realization:

```text
the conditional family changes for some neighboring conditions
iff K is nonconstant.
```

The qualifier “for some” matters. A kernel containing only harmonic `q>1`
has a smaller period and need not distinguish every pair of conditions. The
axiom requires genuine variation, not an injective encoding of every
neighbor condition.

This equivalence does not derive the shifted-convolution ansatz, compact
`U(1)` carrier, Lueders instrument, or mode content from the axioms. It says
that once those bounded ingredients are supplied, Admissibility's required
variation excludes exactly the constant, zero-curvature member of the
representation-positive class.

## 4. From transition probabilities to a local action germ

For supplied conditionally factorized transition factors, ordinary probability
multiplication gives

```text
P[path] = product_p K(theta_p),
-log[P[path]/K(0)^N] = sum_p V(theta_p).
```

Thus the negative-log transfer weight is additive over the supplied factors.
No separate finite additivity premise is imported from Record, and no global
joint law is inferred merely from arbitrary local full conditionals. The
factorized transfer interpretation is an explicit premise of this step.

Since the Fourier theorem gives a positive local curvature, the resulting
potential lies in the continuum parent's quadratic basin. Under smooth
principal-branch refinement,

```text
sum_p V(theta_p)
  -> (kappa/4) integral F_mu_nu F_mu_nu d^4x,
delta S=0
  -> partial_nu F_nu_rho=0.
```

After division by `kappa`, distinct representation-positive kernels converge
to the same source-free equation. Their values of `kappa` remain distinct
microscopic normalization data, relevant when sources, coupling constants,
or quantum fluctuation weights are introduced.

## 5. Temporal kernel versus Maxwell completion

A link transition from one time layer to the next naturally produces
temporal plaquette factors. Write their quadratic coefficient as `kappa_t`
and the spatial plaquette coefficient as `kappa_s`. At momentum `q`, the
quadratic kernel is the continuum parent's block

```text
K_00 = kappa_t P,
K_0i = -kappa_t q_0 q_i,
K_ij = kappa_t q_0^2 delta_ij
       + kappa_s(P delta_ij-q_i q_j).
```

With `kappa_s=0`, Schur reduction leaves no transverse magnetic restoring
term. On a purely spatial nonzero momentum, the full matrix has rank one,
whereas the isotropic `kappa_s=kappa_t>0` completion has rank three before
removing the gauge null and rank two in the physical spatial quotient.

Consequently:

- positive registration derives `kappa_t>0` for the stated temporal
  mechanism;
- it does not derive `kappa_s>0` or `kappa_s=kappa_t`;
- placing the same `V` on every plaquette orientation supplies an explicit
  completion and then yields source-free Maxwell; and
- unequal positive completion changes the infrared cone by
  `sqrt(kappa_s/kappa_t)`.

The spatial cubic lattice symmetries can relate spatial orientations after a
spatial action surface is present. They do not exchange space with Record
time. The approved kinetic-isotropy primitive concerns a kinetic graining
form and is not silently extended here into gauge-action isotropy.

## 6. Axiom and premise ledger

The current four axioms supply only the following pieces used at axiom scope:

- Lattice: the homogeneous nearest-neighbor `Z^3` spatial carrier and proper
  cubic covariance;
- Qubit: the one-site possibility domain with full algebra `M_2(C)`;
- Admissibility: a neighbor-conditioned local probability distribution that
  genuinely varies with neighbor conditions; and
- Record: records form, lock one supported possibility, persist, and alone
  are readable.

They do not supply a compact `U(1)` link variable, a Peter-Weyl carrier, a
central positive Lueders instrument, position-classicality between steps, a
factorized transfer law, a formation location/rate, a four-dimensional
plaquette action, or an electromagnetic interpretation. Record formation in
general is axiom content; repeated occurrence of this particular link
registration mechanism is not.

The bounded dependency stack is therefore:

```text
supplied compact U(1) link carrier
 + supplied positive central Lueders registration
 + supplied position-classical transition reading
 + Admissibility-compatible nonconstant shifted kernel
 -> positive temporal negative-log germ

positive temporal germ
 + supplied local spatial plaquette completion with equal curvature
 -> source-free Maxwell on the smooth zero-monopole branch.
```

This is narrower and more informative than supplying a Wilson action from the
start: the detailed temporal potential and its sign are now consequences of
the registration class. It remains conditional at the points listed above.

## 7. Executable evidence and controls

The runner reports `TOTAL: PASS=30 FAIL=0`. It checks:

- normalization, evenness, periodicity, the identity maximum, closed
  curvature, and negative-log derivatives for three explicit positive
  Fourier families;
- the analytic inequalities on 32 deterministic eight-harmonic families;
- reconstruction of three positive Lueders channels from their Kraus weights,
  nonnegative Fourier autocorrelations, and the two sharp curvature values;
- full-resolution, constant-kernel, and negative-character controls;
- exact variation of shifted conditionals and additivity of factorized
  negative-log transition weights;
- second-order action and Euler-operator refinement for three distinct
  microscopic kernels, including convergence after curvature normalization;
- the inherited exact zero-monopole cube identity;
- every nonzero Fourier momentum on `L=3,4,5` for the orientation-completed
  Hessian, gauge null, and two-mode quotient; and
- temporal-only and anisotropic spatial-completion controls.

The runner's finite families falsify implementation and scope errors. The
general Fourier theorem and support-count argument provide the universal
claims.

## No-Go Discipline Gate

The positive theorem contains one important negative boundary: a temporal
registration kernel alone is not a Maxwell field. The following N1-N8 gate
limits that statement to the exhibited missing magnetic block; it is not a
no-go against other spatial-completion mechanisms.

### N1 — Alternative routes and same-cycle evidence

These attempts were checked analytically or by the paired runners in this
47-path review unit. Positive and partial constructions remain positive or
partial; none is recast as a failed route to satisfy a count. Named check
labels, rather than old ordinal numbers, identify the evidence. Cross-note
comparisons below are scope tests, not extra premises of this note.

| Route | Actual attempt and evidence | Result within the stated scope |
|---|---|---|
| Fourier germ | **ATTEMPTED:** Sum nonnegative character data with the stated fourth-moment bound (§1 and curvature/maximum checks). | The nonconstant supplied kernel has a stable germ. |
| Registration channel | **ATTEMPTED:** Calculate the finite positive Lueders Kraus autocorrelation (§2 and mode-by-mode Kraus checks). | This specified channel realizes the sign condition; the channel is supplied. |
| Fully resolved registration | **ATTEMPTED:** Resolve all three modes (full-resolution check). | This particular channel becomes constant; records alone do not force curvature. |
| Probabilistic sign counterexample | **ATTEMPTED:** Keep a positive density with a negative character coefficient (negative-character check). | Its identity is unstable; positivity of probability alone is insufficient. |
| Temporal transition only | **ATTEMPTED:** Assemble the temporal-only quadratic block (temporal-only check). | It lacks two magnetic restoring directions at spatial momentum. |
| Spatial completion | **ATTEMPTED:** Supply all plaquette orientations and inspect the Hessian and Gauss quotient. | The conditional Maxwell completion works. |
| Anisotropic completion | **ATTEMPTED:** Give spatial and temporal germs unequal positive curvature (last control block). | The cone changes; their equality remains supplied. |

Recentered kernels and other backgrounds remain live. No claim excludes
registration channels beyond the finite construction or derives the physical
position-classical interpretation from its algebra.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: compact-link realization.
- W2: positive central registration when using that construction.
- W3: nonconstant kernel.
- W4: position-classical transition interpretation.
- W5: joint factorization.
- W6: spatial magnetic completion.
- W7: time-space gauge normalization.
- W8: physical U(1) identification.
- W9: charged coupling.

| Pair | First closure implies second? | Second closure implies first? | Independence established? |
|---|---|---|---|
| W1, W2 | unresolved | unresolved | no |
| W1, W3 | unresolved | unresolved | no |
| W1, W4 | unresolved | unresolved | no |
| W1, W5 | unresolved | unresolved | no |
| W1, W6 | unresolved | unresolved | no |
| W1, W7 | unresolved | unresolved | no |
| W1, W8 | unresolved | unresolved | no |
| W1, W9 | unresolved | unresolved | no |
| W2, W3 | unresolved | unresolved | no |
| W2, W4 | unresolved | unresolved | no |
| W2, W5 | unresolved | unresolved | no |
| W2, W6 | unresolved | unresolved | no |
| W2, W7 | unresolved | unresolved | no |
| W2, W8 | unresolved | unresolved | no |
| W2, W9 | unresolved | unresolved | no |
| W3, W4 | unresolved | unresolved | no |
| W3, W5 | unresolved | unresolved | no |
| W3, W6 | unresolved | unresolved | no |
| W3, W7 | unresolved | unresolved | no |
| W3, W8 | unresolved | unresolved | no |
| W3, W9 | unresolved | unresolved | no |
| W4, W5 | unresolved | unresolved | no |
| W4, W6 | unresolved | unresolved | no |
| W4, W7 | unresolved | unresolved | no |
| W4, W8 | unresolved | unresolved | no |
| W4, W9 | unresolved | unresolved | no |
| W5, W6 | unresolved | unresolved | no |
| W5, W7 | unresolved | unresolved | no |
| W5, W8 | unresolved | unresolved | no |
| W5, W9 | unresolved | unresolved | no |
| W6, W7 | unresolved | unresolved | no |
| W6, W8 | unresolved | unresolved | no |
| W6, W9 | unresolved | unresolved | no |
| W7, W8 | unresolved | unresolved | no |
| W7, W9 | unresolved | unresolved | no |
| W8, W9 | unresolved | unresolved | no |

### N3 — Hidden-wall scan

The supplied structures are named explicitly: finite or summably truncated
representation content, positive square-root Kraus coefficients, a shifted
convolution law, and a negative-log transfer interpretation. The
four-dimensional carrier and all-orientation plaquette completion enter only
in the Maxwell corollary. No Hamiltonian, spacetime symmetry, Born selector,
binary capacity, spatial action, physical photon dictionary, or formation
rate is attributed to the minimal axioms.

### N4 — Residual matching

The registration parent left occurrence, position-classicality, rate,
continuum, and Wilson/action-surface selection open. This note uses its
conditional positive-kernel theorem and closes only the downstream local-sign
calculation. The continuum parent left realization of a positive isotropic
quadratic basin open. This note supplies the positive temporal germ under a
specific registration mechanism while leaving the spatial/orientation part
open. Neither parent's wider residual is relabeled as closed.

### N5 — Rhetoric and resolution audit

“Temporal registration alone is not Maxwell” means that the displayed
temporal-only quadratic block lacks magnetic transverse stiffness. It does
not mean that Record, Admissibility, a spatial cell law, a larger composite,
or an effective-action mechanism can never supply that stiffness. The cached
runner prints the required five-resolution certificate:

```text
per_element: each U1 character coefficient and each three-mode Lueders Kraus weight is checked in the induced kernel
per_site: shifted neighbor-conditioned densities and additive negative-log transition factors are checked explicitly
per_mode: every nonzero Fourier momentum on L=3,4,5 is checked after the orientation-completed quadratic germ
per_block: temporal-only, isotropic-completed, anisotropic, constant, and negative-character blocks are contrasted
lattice_wide: fixed-volume action/operator refinements and zero-monopole cube identities run on periodic four-lattices
```

### N6 — Partial-closure paths and primitive check

The current axiom text was reread directly. Admissibility supplies a varying
nearest-neighbor probability distribution but no transfer operator or action;
Record supplies formation and fixed readable outcomes but no formation rule,
site, rate, or link update. The kinetic-isotropy primitive does not state a
gauge Hessian, the scale primitive supplies units only, and the realized-state
slot supplies no spatial plaquette factor. None derives orientation completion.

Live partial-closure routes remain: construct the spatial factor from the
cell/corner Admissibility law; derive the same kernel on all orientations from
a stronger spacetime mechanism; or retain anisotropy and show an infrared
fixed point equalizes it. This theorem makes any of those routes sufficient
without exact Wilson selection.

### N7 — Steelman

The strongest objection is that the induced `T(g|h)` may be only a readout
overlap kernel, not a physical update law. Even if it is a genuine temporal
transition, multiplying its factors may not define the framework's compatible
global probability law, and it supplies no spatial magnetic energy. This
objection blocks promotion to a derived Maxwell theory. It does not defeat the
Fourier theorem or the conditional statement: if that positive convolutional
kernel is the local transfer factor, its negative-log germ has the forced
positive sign.

### N8 — Cross-cycle echo

Earlier gauge work distinguished kinematic covariance from a dynamical step
measure and distinguished positive Lueders registration from general central
channels. The current theorem preserves both separations. Earlier
action-selection work distinguished Wilson, heat-kernel, and other
finite-angle laws; the quadratic-basin parent proved that their detailed shape
is unnecessary for smooth source-free Maxwell. This note composes those two
surfaces only at their shared local germ and does not revive a heat-kernel,
binary-capacity, or Wilson-selection claim.

**Gate result:** PASS for the scoped temporal-only boundary. The missing
magnetic block is exhibited, independent completion routes remain live, and
no permanent spatial-completion no-go is asserted.

## Falsifiers

The claim fails if any of the following occurs within its stated scope:

- a normalized nonconstant `U(1)` kernel with nonnegative character
  coefficients and finite fourth moment has `V''(0)<=0`;
- a positive Lueders central channel produces a negative Fourier
  autocorrelation coefficient;
- a two-outcome positive Lueders channel on all three modes has no overlapping
  mode pair and therefore zero second moment;
- the sharp partitions do not give the displayed kernels and curvatures;
- exact negative-log forces fail to converge to the curvature-normalized
  Maxwell operator on smooth refinement;
- the orientation-completed Hessian loses its gauge null or fails to leave two
  transverse modes; or
- the temporal-only control already contains the two spatial magnetic
  restoring directions claimed to be missing.

## Verification

Run:

```text
python3 scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=30 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A selected framework-derived electromagnetic law and physical field/readout bridge remain open; the eventual physical consumer is not yet established."
source_of_blocker_text: "review_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Use the conditional result with its stated inputs; establish the missing physical consumer and selection bridge before claiming framework closure."
conditional_surface_status: "Supplied compact phase kernel and nonnegative Fourier data; the finite Lueders construction and spatial completion have their stated conditions."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The written derivation establishes only the declared conditional mathematical claim; finite checks and source review grant no retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original September 2–3 source and receipts are preserved at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. This revision supplies current
source status, explicit timeout/input-bound evidence and written boundary
checks. The conditional scope is stated in the status record above.
Independent source confirmation and current-main integration validation are
separate; no audit verdict or effective retained status is asserted.
