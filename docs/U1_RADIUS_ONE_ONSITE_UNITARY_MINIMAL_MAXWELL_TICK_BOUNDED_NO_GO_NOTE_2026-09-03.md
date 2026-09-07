---
claim_id: u1_radius_one_onsite_unitary_minimal_maxwell_tick_bounded_no_go_note_2026-09-03
claim_type: no_go
claim_scope: "For one complex scalar on each role-compiled physical edge and face, no vertex/cube/coin payload, a complete translation-covariant linear tick whose old-to-new support is self plus physical nearest neighbors and whose gauge-compatible off-diagonal blocks are the oriented curl cannot both propagate and preserve the raw onsite norm exactly. Unitarity forces both curl coefficients to zero, leaving momentum-independent onsite phases. Finite-depth, local-metric, enlarged-carrier, longer-range, nonlinear, observable-level, and interacting qubit routes remain open or positively exhibited."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - u1_minimal_physical_neighbor_conservative_gauge_dynamics_uniquely_maxwell_bounded_theorem_note_2026-09-03
  - u1_local_reversible_yee_leapfrog_tick_bounded_theorem_note_2026-09-03
runner: scripts/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.py
---

# Radius-One Onsite Unitarity Makes the Minimal Maxwell Tick Transport-Trivial

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** no_go
**Type:** bounded no-go
**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.
**Generator classification:**
[`U1_MINIMAL_PHYSICAL_NEIGHBOR_CONSERVATIVE_GAUGE_DYNAMICS_UNIQUELY_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_MINIMAL_PHYSICAL_NEIGHBOR_CONSERVATIVE_GAUGE_DYNAMICS_UNIQUELY_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Positive finite-depth sibling:**
[`U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Approved kinetic primitive:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
**Runner:**
[`scripts/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.py`](../scripts/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.txt`](../logs/runner-cache/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.txt)

## Result up front

Consider the strict reading of “one local tick” on the physical role lattice:

1. one complex electric scalar lives at each edge-role site and one complex
   magnetic scalar at each face-role site;
2. vertex and cube roles carry no tick payload;
3. one complete old-to-new linear map reads only the same site and its six
   physical nearest neighbors;
4. the map is translation-covariant and gauge/chain compatible;
5. the raw onsite norm `sum |E|^2+sum |B|^2` is preserved exactly; and
6. no sequential sublayers, hidden coin, enlarged unit cell, or longer-range
   same-role stream participates.

The role geometry has no edge-edge or face-face nearest-neighbor pair. Gauge
and chain compatibility make every non-onsite edge/face block a multiple of
the oriented curl. In coarse Fourier form the most general proper-cubic member
is therefore

```text
U(k) = [[u I, r C(k)^dag],
        [q C(k), v I     ]].
```

At zero momentum, `C(0)=0`. Unitarity gives

```text
|u|=|v|=1.
```

At any momentum for which `C(k)` is nonzero, the two diagonal column-norm
identities are

```text
|u|^2 I+|q|^2 C(k)^dag C(k)=I,
|v|^2 I+|r|^2 C(k) C(k)^dag=I.
```

The first terms already equal `I`, and the remaining terms are positive
semidefinite. Hence

```text
q=r=0.
```

Every exact raw-onsite-unitary tick in this declared class is consequently

```text
U(k)=diag(u I,v I),
```

a momentum-independent pair of onsite phases. It carries no propagation and
cannot have the Maxwell tangent. The argument also kills independent
orientation coefficients; proper cubic covariance is not needed for that
strengthening.

This is an exact obstruction to one narrow conjunction, not to local photon
dynamics. The immediately preceding source gives a three-layer local
reversible photon tick with a positive local field-energy metric. A
six-direction internal carrier gives strict radius-one cubic-unitary
transport. Cayley evolution gives exact raw unitarity with nonlocal support.
Those explicit escapes show that at least one of complete-map radius one, raw
onsite norm, or minimal edge/face payload must be relaxed.

The approved kinetic-isotropy primitive supplies `c_t=c_s` and says one tick
is one edge in form. It does not define “one edge in form” as this complete-map
radius-one onsite-unitary class, and it supplies no dynamics. This theorem
therefore identifies an interpretation boundary; it does not contradict or
amend the primitive.

## 1. Exact target contract

| Field | Contract |
|---|---|
| Target statement | Classify all complete radius-one raw-onsite-unitary linear ticks on the minimal physical edge/face payload after gauge/chain compatibility reduces the off-diagonal blocks to curl incidence. |
| Quantifiers/domain | Every momentum on the cubic Brillouin torus; complex coefficients; one scalar per edge/face role; translation covariance; physical nearest-neighbor support. |
| Allowed premises | The physical role incidence graph, `C d_0=0`, `d_2 C=0`, and elementary positive-semidefinite column norms. |
| Forbidden weakening | No inference about finite-depth circuits, extra carriers, longer range, nonlinear maps, compact interactions, observable evolution inside a larger unitary, or all qubit QCAs. |
| Required edge cases | `k=0`; nonzero rank-two curl; complex phases; independent orientation coefficients; raw-unitary but Gauss-breaking pair rotations. |
| Completion witness | Fourier block identity proving `q=r=0`, full-lattice exhibit, exhaustive coefficient control, and five-resolution receipt. |
| Outcomes not counting as closure | A finite momentum scan alone; failure of Euler alone; nonlocality of Cayley alone; or the older one-mode scalar CAR result. |

## 2. Why this is the general radius-one block in the declared class

On the doubled incidence role pattern, an edge site has two vertex and four
face neighbors; a face site has four edge and two cube neighbors. With no
vertex/cube tick payload, there is no dynamical same-role input one physical
step away. The only diagonal terms are onsite scalars.

For a face output, gauge invariance of the four neighboring edge inputs leaves
the oriented boundary stencil `(1,1,-1,-1)`, as classified in the generator
parent. For an edge output, preservation of electric Gauss gives the adjoint
co-curl stencil. Translation covariance gives the Fourier form

```text
U(k) = [[U_E, R(k)], [Q(k), U_B]],
U_E=u I,                  U_B=v I,
Q(k)=q C(k),              R(k)=r C(k)^dag.
```

Proper cubic covariance makes each displayed coefficient common across
orientations. The executable also drops that equality and tests independent
orientation weights. Positivity still forces every weight to zero because a
nonzero row of `diag(q_x,q_y,q_z)C(k)` adds positive norm to some input
column. It separately enumerates all 625 small reverse stencils around one
face and confirms that electric-Gauss preservation leaves only the co-curl.

## 3. The zero-mode saturation argument

The curl symbol is

```text
C(k) = [s(k)]_cross,
s_i(k)=2 sin(k_i/2),
```

up to harmless staggered phases. It vanishes at `k=0`. Therefore

```text
U(0)=diag(u I,v I).
```

Raw onsite unitarity at this one mode already saturates every input column:

```text
|u|^2=|v|^2=1.
```

For a general momentum, the electric-input diagonal block of `U^dag U` is

```text
|u|^2 I+|q|^2 C^dag C.
```

There is no negative interference term because onsite electric output and
face output occupy orthogonal raw coordinates. Since the first summand is
already `I`, unitarity requires

```text
|q|^2 C^dag C=0
```

for every momentum. Some momentum has rank-two `C`, so `q=0`. The magnetic
input columns give `r=0` identically. Cross-block unitarity conditions are no
longer needed.

The surviving `u` and `v` may be arbitrary complex phases. If the field map
is additionally required to be real, they reduce to signs. The identity-
connected real component is `u=v=+1`. None depends on momentum, so none
transports a field or supplies a photon phase.

## 4. Executed controls and explicit escapes

The runner separates six materially different mechanisms.

### 4.1 Exact coefficient census

It enumerates

```text
u,v in {1,-1,i,-i},
q,r in {0,1,-1,i,-i}
```

over zero momentum, three axial momenta, and one generic momentum. Exactly 16
of the 400 tuples are unitary, precisely the 16 pairs with `q=r=0`. It then
checks every nonzero mode on `L=3,4,5,7` for a transported coefficient pair;
all violate raw unitarity.

### 4.2 Full physical block

On the `162`-component side-six role lattice, a nonzero curl pair has only
radius-one support and nevertheless fails `U^dag U=I`. A phase-only survivor
is exactly unitary and exactly diagonal.

### 4.3 Euler

```text
I+h [[0,-C^T],[C,0]]
```

has the correct Maxwell tangent and complete-map radius one, but its norm
defect is `h^2 G^dag G`. This is one witness for dropping exact raw unitarity,
not proof of the theorem by itself.

### 4.4 Cayley

```text
(I+hG/2)(I-hG/2)^-1
```

is exactly raw-unitary on the finite block. Every tested row spreads beyond a
physical star, so it exits complete-map radius one.

### 4.5 Palindromic leapfrog

The positive sibling composes three physical-neighbor shears. It preserves a
positive local field-energy metric and both Gauss rows while carrying two
photon phases. Its complete map has radius three and its raw onsite norm is
not the conserved metric. It is the strongest direct counterexample to any
broader negative wording.

### 4.6 Pair rotation and enlarged carrier

A Givens rotation on one incident edge-face pair is exactly raw-unitary and
radius one. The runner supplies a Gauss-valid input that it sends outside the
Gauss sector. Thus local pair rotations evade the norm problem only by losing
the gauge constraint unless assembled by a more elaborate mechanism.

A separate six-direction carrier streams each internal direction one lattice
step. Its symbol is diagonal with entries `exp(i k dot d)` for
`d in {+/-e_x,+/-e_y,+/-e_z}`. It is exactly radius-one unitary and covaries
under all 24 proper cubic rotations by permuting the six directions. This is a
positive enlarged-payload escape; it is not yet a Maxwell/Gauss construction.

## 5. Approach-family registry

| Family | Object/formulation | Mechanism/invariant | Terminal obligation | Strength vs target | Status | Concrete evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| minimal Fourier block | `6 x 6` edge/face symbol | zero-mode norm saturation plus PSD curl norm | prove all curl coefficients vanish | target-equivalent | candidate-complete | exact algebra and 400-tuple census | a legal radius-one term outside the declared block form |
| finite-depth field update | three shear layers | local modified energy and palindromic inverse | preserve photon phases and Gauss | incomparable escape | candidate-complete | sibling 27/27 runner replayed | require raw onsite norm or one-layer radius |
| local pair circuit | incident Givens rotation | Euclidean orthogonality | preserve the Gauss kernel | weaker escape | blocked-local | explicit Gauss-valid counterexample | a gauge-preserving matching/product mechanism |
| rational unitary | Cayley transform | skew-generator functional calculus | retain finite physical support | weaker escape | blocked-local | exact unitary, dense finite block | finite Laurent factorization of the rational symbol |
| enlarged carrier QCA | six directed streams | permutation unitarity and cubic orbit | produce Maxwell/Gauss physical sector | incomparable escape | provisional | exact six-band radius-one cubic transport | a gauge-invariant photon encoding in the carrier |
| observable-in-larger-unitary | qubit QCA plus field observables | Heisenberg compression rather than raw field unitarity | close the observable algebra under a local unitary | unknown/comparable | unexplored | no construction imported | explicit `M2(C)` circuit and Maxwell observable sector |

## 6. Program consequence

The strict conjunction

```text
minimal E/B payload
+ complete-map physical radius one
+ gauge-compatible curl response
+ raw onsite unitarity
```

cannot carry light. This gives a useful decision tree rather than a broad
failure:

- accept a finite-depth local cycle, as the positive leapfrog source does;
- conserve a positive local field metric rather than the raw coordinate norm;
- enlarge the dynamical carrier or unit cell;
- realize E and B as observables inside a larger onsite-unitary qubit law; or
- allow longer-range complete-map support.

The first route is already positive. The fourth is the most faithful route if
raw qubit unitarity is treated as non-negotiable. It asks for a finite local
`M2(C)` update whose closed gauge-invariant observable sector has the photon
spectrum; it does not ask the six raw field coordinates themselves to be a
unitary one-particle basis.

No new axiom follows. In particular, the kinetic-isotropy primitive is an
approved premise supplying OS0 kinetic-form normalization, not a dynamics or
support-radius definition. The exact governance question is whether “one tick
is one edge in form” permits a finite-depth nearest-neighbor cycle or refers
only to the normalized regulator form. Silently strengthening it to the
obstructed conjunction would make a supplier choice look like axiom content.

## No-Go Discipline Gate

### N1 — Alternative route enumeration

Every row is a distinct approach family under the proof-search governance
tuple `(object, mechanism, terminal obligation)`.

| Honesty | Route class | Attack on the no-go | Same-cycle outcome and evidence |
|---|---|---|---|
| **ATTEMPTED** | `algebraic_rearrangement` | Solve the complete minimal Fourier block without assuming adjoint cancellation. | Zero-mode saturation and positive diagonal column norms force both curl coefficients to zero; checks 4-11. |
| **ATTEMPTED** | `dynamical_or_effective_action` | Replace the one-layer map by the palindromic Yee evolution. | Positive photon tick; it exits complete-map radius one and raw onsite norm; check 17 plus the replayed sibling runner. |
| **ATTEMPTED** | `symmetry_or_representation` | Give each curl orientation its own coefficient. | Axial basis momenta force all three edge-to-face and all three face-to-edge coefficients to zero independently; check 9. |
| **ATTEMPTED** | `alternate_carrier_or_sector` | Add six directed internal streams. | Positive strict radius-one cubic-unitary transport; it exits the one-scalar edge/face payload and has no Maxwell sector yet; check 19. |
| **ATTEMPTED** | `topology_or_global_structure` | Use a local unitary pair rotation and hope products preserve the constrained subspace. | One exact radius-one Givens gate sends an explicit Gauss-valid vector outside the Gauss sector; check 18. General gauge-preserving products remain open outside this single-pair route. |
| **ATTEMPTED** | `lattice_scale_or_limit` | Use Cayley functional calculus at finite step. | Exact raw unitarity survives, but the inverse produces support beyond the physical star on the named full block; check 16. |
| **ATTEMPTED** | `numerical_or_finite_case` | Search a finite complex coefficient grid and finite Brillouin zones. | All 400 coefficient tuples and every nonzero `L=3,4,5,7` mode agree with the algebra; checks 8 and 10. This supports but does not replace the proof. |

The open enlarged-carrier and observable-sector routes prevent any broader
no-go. They do not invalidate the target because the target forbids their
additional payload.

### N2 — Wall-independence audit

Use the collapsed escape set

```text
W1 = relax complete-map radius one to finite depth or longer range,
W2 = replace raw onsite norm with a positive local field metric,
W3 = enlarge the dynamical payload or unit cell,
W4 = realize E/B as observables inside a larger unitary,
W5 = relax exact Gauss-sector preservation.
```

`W4` is not collapsed into `W3`: an observable subalgebra may use the same
underlying one-qubit-per-site lattice while ceasing to identify raw E/B
coordinates with the unitary state vector.

| Pair | `Wi -> Wj`? | `Wj -> Wi`? | Independent? |
|---|---:|---:|---:|
| W1, W2 | no | no | yes |
| W1, W3 | no | no | yes |
| W1, W4 | no | no | yes |
| W1, W5 | no | no | yes |
| W2, W3 | no | no | yes |
| W2, W4 | no | no | yes |
| W2, W5 | no | no | yes |
| W3, W4 | no | no | yes |
| W3, W5 | no | no | yes |
| W4, W5 | no | no | yes |

The positive leapfrog closes W1 and W2 together, but that one construction
does not make the two logical relaxations imply each other.

### N3 — Hidden-wall scan

The load-bearing conditions are all in the six-item class declaration. “Raw
onsite norm” excludes a cross-site metric. “Complete map” excludes a sequence
whose individual layers are local but whose product reaches farther. “Minimal
payload” excludes vertex, cube, coin, or directed-stream channels. “Linear”
excludes compact nonlinear updates. Gauge/chain compatibility supplies the
curl form; it is not inferred from unitarity.

Searches for “we assume,” “as is standard,” “naturally,” “obviously,”
“standard QFT,” “bridge context,” and “the framework provides” return no
load-bearing hidden condition. “Approved” modifies the actual registered
kinetic primitive. “General” is always followed by “in the declared class.”

### N4 — Residual matching

| Cited surface | Its residual | Current residual | Match? | Use |
|---|---|---|---:|---|
| `docs/U1_MINIMAL_PHYSICAL_NEIGHBOR_CONSERVATIVE_GAUGE_DYNAMICS_UNIQUELY_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-03.md:327` | strictly radius-one exact unitary tick not constructed | classify the strict minimal radius-one raw-unitary block | yes | target motivation only |
| `docs/U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md:83` and `:462` | one-layer radius-one qubit unitary and paraunitary search remain | same narrow strict search | yes | direct positive steelman and target |
| `docs/SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md:37` and `:234` | one scalar cubic CAR stream is onsite; six directions escape | edge/face gauge curl block under raw norm | no | analogy only; not proof authority |
| `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:15` and `:25` | OS0 kinetic-form normalization; one tick one edge in form | algebraic support and unitarity of a candidate field map | no | interpretation boundary only |

No prior negative source is used to prove this theorem. The block proof is
self-contained. The two nonmatching citations are retained only as clearly
marked context and escape guidance.

### N5 — Rhetoric and resolution audit

The exact sentence is “the declared minimal radius-one raw-onsite-unitary
block has no transported member.” Its resolution census is:

| Resolution | Executed? | Evidence | Scope of negative |
|---|---:|---|---|
| per-element | yes | zero-mode onsite magnitude and positive curl-column norm | complex scalar coefficients in the block form |
| per-site | yes | every permitted off-diagonal entry is one physical edge-face incidence | role-compiled minimal payload only |
| per-mode | yes | algebra for every `k`; exhaustive `L=3,4,5,7` control | transported block violates raw unitarity at nonzero `k` |
| per-block | yes | 400 tuples, orientation variants, and five route controls | declared `6 x 6` Fourier family only |
| lattice-wide | yes | full `162 x 162` phase and transported maps | named periodic physical block |

No sentence extends the result to finite-depth circuits, enlarged carriers,
nonlinear dynamics, longer range, local energy metrics, or observable sectors.
The runner cache lands the same five-resolution certificate.

### N6 — Partial-closure paths and primitive check

The primitive registry and the current kinetic source were read directly.
`kinetic_isotropy_primitive` is approved and chain-satisfying. It supplies
`c_t=c_s`; it is neither a wall nor evidence for this no-go, and it does not
supply a dynamics selector or support-radius theorem.

Three partial-closure paths are already visible:

- the finite-depth sibling positively closes local reversible photon
  existence while relaxing W1 and W2;
- the six-direction stream positively closes strict radius-one cubic-unitary
  transport while relaxing W3; and
- treating E/B as observables of a larger unitary could close W4 without an
  axiom edit, but needs an explicit local qubit construction.

Clarifying that the kinetic primitive concerns OS0 form rather than complete
map support would be an interpretation/reframing, not new physics. This note
therefore makes no “new axiom required” claim.

### N7 — Steelman

A hostile reviewer should reject the raw-field premise as the wrong level of
description. Fundamental qubits may evolve by an exactly local unitary while
electric and magnetic fields are composite observables whose closed linear
expectation-value update is neither unitary nor radius one in the raw six-field
metric. The six-direction stream demonstrates that internal transport removes
the zero-mode saturation, and the finite-depth Yee map already supplies the
desired photon sector. The actionable counter-route is to construct a local
`M2(C)` circuit, identify a gauge-invariant E/B observable subspace, and prove
its two-phase Maxwell spectrum and Record readout. Until that terminal
obligation is attempted, this result cannot be promoted beyond its minimal
raw-coordinate class.

This steelman does not break the scoped block algebra; it is the next positive
compiler target and the reason the theorem is a bounded no-go rather than a
general obstruction.

### N8 — Cross-cycle echo

The July scalar cubic CAR/QCA source made a similar one-mode onsite-phase
statement and exhibited a six-direction escape. Its archived audit was later
invalidated for missing complete N1-N8 coverage. This note does not import
that result: it redoes the distinct gauge-field block algebra, executes the
six-direction escape, lands seven normalized N1 routes, and includes the five
resolution cache certificate.

The immediate prior cycle also retired a broader apparent wall: nonlocality
of the exact exponential did not prevent a finite-depth local reversible
photon tick. The same mechanism is therefore included as the primary
steelman, rather than being ignored while asserting a universal local no-go.

**Gate result:** PASS for the declared minimal raw-coordinate class. Seven
normalized routes were attempted, five independent escape dimensions were
audited, the strongest positive counter-routes remain explicit, and the
negative claim is not generalized beyond its exact block form.

## Falsifiers

The bounded theorem fails if any of the following occurs inside the declared
class:

- the physical radius-one role graph permits a dynamical same-role input;
- gauge/chain compatibility permits an off-diagonal stencil not represented
  by the declared curl blocks;
- raw unitarity at `k=0` does not fix both onsite magnitudes to one;
- a nonzero curl coefficient can cancel its positive contribution to the
  diagonal column norm;
- an independent orientation coefficient survives the three axial momenta;
- an exact coefficient tuple with nonzero `q` or `r` is unitary at every
  momentum; or
- a surviving phase-only block has momentum-dependent propagation.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=19 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "no-go"
target_claim_type: "no_go"
trace_class: "negative_route_pruning"
target_claim_id: null
target_blocker_text: "Whether a minimal radius-one raw-onsite-unitary curl tick can propagate."
source_of_blocker_text: "review_loop"
reachability_to_target: "prunes"
artifact_role: "no_go"
next_trace_action: "Keep the strict obstruction scoped and test enlarged payload or finite-depth gauge-preserving alternatives."
conditional_surface_status: "Complete-map radius one, one complex scalar per edge/face, linear translation-covariant curl blocks and exact raw onsite norm; enlarged or finite-depth routes are outside the obstruction."
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
