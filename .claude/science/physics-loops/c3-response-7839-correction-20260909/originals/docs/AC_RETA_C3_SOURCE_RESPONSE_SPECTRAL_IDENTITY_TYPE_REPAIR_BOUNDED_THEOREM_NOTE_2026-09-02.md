---
claim_id: ac_reta_c3_source_response_spectral_identity_type_repair_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "On the finite C3 regular carrier, complex conjugation and projection idempotence uniquely select the nonzero K-even invariant projector that kills the singlet, namely the rank-two doublet projector. For the full positive K-even C3-equivariant family A=a_s P_s+a_d P_d, the formal determinant D_A(j)=det(A+jP_d) has derivative Tr(A^-1 P_d)=2/a_d. The stipulated campaign response h=(1/3)tau(A^-1 P_d)=Tr(A^-1 P_d)/9 is 2/(9a_d), so h=2/9 occurs exactly at a_d=1; neither that action scale nor the extra orbit-density factor is physically selected. A genuine C3 conjugation average of the invariant operator returns the operator and contributes no extra factor. Under one explicitly stated lens quotient/operator/orientation convention, the local cyclic fixed-point density equals the magnitude of the raw odd-signature eta invariant at 2/9 uniquely for nontrivial p=3; reduced eta instead includes h_B=1 and equals 11/18 or 7/18 according to sign. This is an arithmetic coincidence, not a physical carrier, partition-function, or phase theorem. A flat character on an order-three torsion generator cannot have holonomy 2/9; only that flat shortcut is excluded. No physical carrier, statistics/measure, action normalization, density-to-angle identity, obligation retirement, axiom edit, or audit verdict is supplied."
upstream_dependencies:
  - minimal_axioms
runner: scripts/reta_c3_source_response_spectral_identity_2026_09_02.py
---

# R--eta C3 Source Response: Finite Arithmetic and Carrier-Type Repair

**Date:** 2026-09-02
**Type:** bounded theorem plus partial-narrowing prior-route repair
**Target:** `ac_reta_hclass_hunit_readout_derivation_obligation`
**Primary runner:**
[`scripts/reta_c3_source_response_spectral_identity_2026_09_02.py`](../scripts/reta_c3_source_response_spectral_identity_2026_09_02.py)

**Independent checker:**
[`scripts/reta_c3_source_response_independent_check_2026_09_02.py`](../scripts/reta_c3_source_response_independent_check_2026_09_02.py)

**Pinned caches:**
[`primary`](../logs/runner-cache/reta_c3_source_response_spectral_identity_2026_09_02.txt),
[`independent`](../logs/runner-cache/reta_c3_source_response_independent_check_2026_09_02.txt), and
[`mutations`](../logs/runner-cache/reta_c3_source_response_mutation_check_2026_09_02.txt).

## Result up front

This campaign finds one exact finite algebraic atom, one arithmetic
coincidence, and several remaining physical walls.  It does not find a
physical bridge.

First, on the finite `C3` regular carrier, the algebraic source class is much
tighter than the old free-functional language suggested.  Let `P_s` be the
singlet projector and `P_d` the rank-two conjugate-doublet projector.  Among
all `C3`-invariant projections fixed by complex conjugation, the unique
nonzero projection that vanishes on the singlet is `P_d`.  Thus if a physical
Record/source theorem establishes that the charged-lepton readout is a
repeatable invariant event, is `K`-even, and ignores the singlet, the source
projector itself has no continuous normalization freedom: idempotence fixes
the nonzero coefficient to one.

Second, the action still carries the decisive free scale.  Every positive
`K`-even `C3`-equivariant quadratic action has the form

```text
A = a_s P_s + a_d P_d,       a_s>0, a_d>0.
```

Define only the formal finite determinant functional

```text
D_A(j) = det(A+jP_d),
tau(X) = Tr(X)/3,
h_A = (1/3) tau(A^-1 P_d) = Tr(A^-1 P_d)/9 = 2/(9 a_d),
Phi_A = 3 h_A = 2/(3 a_d).
```

The first `1/3` is a **stipulated orbit-density normalization** for this
campaign.  It is not produced by group averaging.  The genuine conjugation
average of the invariant operator is

```text
(1/3) sum_k C^k (A^-1 P_d) C^-k = A^-1 P_d.
```

The normalized trace then gives `2/(3a_d)`; the separately stipulated
orbit-density factor gives `2/(9a_d)`.  Keeping these operations typed in this
order repairs the previous scalar-`tau` error.

The desired values `h_A=2/9` and `Phi_A=2/3` occur exactly at `a_d=1`.
`C3`, `K`, positivity, determinant normalization alone, and trace
normalization alone do not select that member.  Source idempotence fixes the
source coefficient but not the action eigenvalue.  This is the shortest
remaining finite source/action atom.

Third, there is an exact arithmetic fact at order three.  The cyclic
fixed-point density used by this route and the magnitude of the raw
odd-signature eta invariant under the convention stated below are different
functions of `p`, but they meet uniquely at the nontrivial order `p=3`:

```text
F_p = (p^2-1)/(12p),
E_p = (p-1)(p-2)/(3p),
E_p-F_p = (p-1)(p-3)/(4p),
F_3=E_3=2/9.
```

This is an exact arithmetic coincidence for the stated quotient/operator
convention.  It does not put the two quantities on a common carrier, and it
does not identify the charged-lepton carrier with the odd-signature operator.

Finally, the older Cheeger--Simons shortcut contains an exact type error.  A
flat character on a torsion generator `g` of order three must obey
`3 chi(g)=0 mod 1`, so its values are `0,1/3,2/3`.  The value `2/9` obeys
`3(2/9)=2/3 != 0 mod 1` and cannot be that flat holonomy.  The global eta
invariant may still have raw magnitude `2/9`; it is not thereby a flat
character on the `Z3` generator.  A non-flat replacement would require
curvature and characteristic-class data, none of which is constructed here.
Eta, non-flat differential-cohomology, and physical source/action routes
remain live.

The physical carrier remains open.  Record supplies no source or action.
Open PRs are comparators only.  The obligation remains open.
TOE percentage movement: `0`.

## Machine status and trace

```yaml
actual_current_surface_status: partial-narrowing
no_go_discipline_gate: FAIL
negative_disposition: partial-attempt-with-named-live-routes
target_claim_type: bounded_theorem
trace_class: direct_source_action_eta_readout_classification
target_claim_id: ac_reta_hclass_hunit_readout_derivation_obligation
reachability_to_target: direct
obligation_retirement: 0
toe_percentage_movement: 0
axiom_amendment: none
audit_status: unset
gravity_paths_touched: 0
review_loop_used: false
```

## Exact finite carrier classification

Let

```text
C = [[0,0,1],[1,0,0],[0,1,0]],
omega = exp(2 pi i/3),
P_r = (1/3) sum_(k=0)^2 omega^(-rk) C^k.
```

The three `P_r` are mutually orthogonal Hermitian rank-one projectors and sum
to the identity.  The commutant of `C` in `M_3(C)` has complex dimension
three.  Its Hermitian part has the real basis

```text
I,  C+C^T,  i(C-C^T).
```

Entrywise complex conjugation fixes the first two basis elements and negates
the third.  Equivalently it fixes `P_0` and swaps `P_1,P_2`.  The complete
list of invariant `K`-even projections is therefore

```text
0, P_s=P_0, P_d=P_1+P_2, I.
```

Only `P_d` is nonzero and annihilates the singlet.  If a source is restricted
to `cP_d`, projection idempotence gives `c^2=c`; the nonzero source has
`c=1`.  This is a positive uniqueness theorem for the finite source class.
It is conditional on projection/event typing and is not a physical readout
identification.

## Full invariant formal-determinant response

Every positive `K`-even invariant action is diagonal on the two real isotypes:

```text
A=a_s P_s+a_d P_d.
```

Since `P_d` has rank two, define the formal finite determinant functional

```text
D_A(j)=det(A+jP_d)=a_s(a_d+j)^2,
d/dj log D_A(j)|_0=Tr(A^-1 P_d)=2/a_d.
```

The well-typed campaign definition is

```text
tau(A^-1 P_d) = Tr(A^-1 P_d)/3 = 2/(3a_d),
h_A = (1/3) tau(A^-1 P_d) = 2/(9a_d).
```

The second line's `1/3` is a stipulated orbit-density factor.  It is not the
result of conjugation averaging: because `A^-1 P_d` commutes with `C`, its
true `C3` conjugation average is itself.  Neither the stipulated factor nor
its physical use is derived by this packet.

`D_A` is also not yet a physical partition function.  Gaussian integration
gives different determinant powers for a real boson, complex boson, and
complex Grassmann field: respectively `det(A)^(-1/2)`, `det(A)^(-1)`, and
`det(A)`.  No graded carrier, measure, statistics, source units, or physical
action is constructed here.  The displayed derivative therefore remains a
formal finite determinant response; the Grassmann typing needed for the
positive determinant power is a future construction, not an inference.

The following exact countercontrols preserve positivity and `C3/K` symmetry:

- `a_d=2, a_s=1/4` has `det A=1` but gives `h=1/9`;
- `a_d=1/2, a_s=2` has `Tr A=3` but gives `h=4/9`;
- `P_d -> cP_d` scales `h` by `c` unless projection idempotence is imposed;
- `a_d -> lambda a_d` scales `h` by `1/lambda` even after source
  idempotence.

Imposing both `det A=1` and `Tr A=3` does select the identity action inside
this two-parameter positive family because

```text
2 a_d^3 - 3 a_d^2 + 1 = (a_d-1)^2(2a_d+1).
```

That is a concrete positive reopening condition.  Neither normalization,
nor their conjunction as physical action conditions, is supplied by the
current framework foundation.

## The order-three local/global spectral identity

For `zeta_p=exp(2 pi i/p)`, set

```text
F_p=(1/p) sum_(k=1)^(p-1)
    1/((zeta_p^k-1)(zeta_p^(-k)-1)).
```

Write `q_p(x)=1+x+...+x^(p-1)`.  Logarithmic derivatives at `x=1` give

```text
sum 1/(1-zeta_p^k) = (p-1)/2,
sum 1/(1-zeta_p^k)^2 = (p-1)(5-p)/12.
```

Because

```text
1/((zeta-1)(zeta^-1-1))
 = 1/(1-zeta) - 1/(1-zeta)^2,
```

one obtains `F_p=(p^2-1)/(12p)`.

Fix the convention before comparing numbers.  Let `S^3` be the unit sphere in
`C^2`, let `zeta_p=exp(2 pi i/p)`, and define `L(p,1)` by the free quotient

```text
(z_1,z_2) -> (zeta_p z_1,zeta_p z_2).
```

Use the round quotient metric and the boundary orientation induced from the
unit ball with its standard complex orientation.  On even forms use the APS
odd-signature operator

```text
B(phi)=(-1)^(r+1)(*d-d*)phi,    degree(phi)=2r,
```

where the second `d*` means `d` followed by Hodge star, not the
codifferential.  Replacing `B` by `-B` or reversing orientation reverses raw
eta.  The convention-independent statement used here is therefore the
magnitude

```text
E_p=|eta_B(0)|
   =(1/p) sum_(k=1)^(p-1) cot(pi k/p)^2.
```

Using `cot^2=csc^2-1` and the same root identity gives
`E_p=(p-1)(p-2)/(3p)`.  Their difference factors as above, so the only
integer equality is `p=1` or `p=3`; `p=3` is the unique nontrivial cyclic
case.  The weight pair `(1,-1)` instead gives the cotangent product with the
opposite sign and represents the orientation-reversed `L(p,-1)` convention;
it must not be silently conflated with `(1,1)`.

This equality concerns **raw** eta magnitude.  For the standard odd-signature
operator on a lens-space rational homology sphere,

```text
h_B=dim ker(B)=b_0+b_2=1,
bar_eta=(eta_B(0)+h_B)/2.
```

Consequently raw eta `+2/9` gives `bar_eta=11/18`, while raw eta `-2/9`
gives `bar_eta=7/18`: the reduced eta values are 11/18 or 7/18, not `2/9`.
Any determinant or boundary-phase construction must specify whether it uses
raw eta, reduced eta, or another kernel-subtracted convention.

The formula and convention are cross-checked against Atiyah, Patodi, and
Singer, [*Spectral asymmetry and Riemannian geometry II*](https://doi.org/10.1017/S0305004100051872).

## Exact Cheeger--Simons carrier repair

The prior source and runner say all three of the following:

1. the proposed flat value is `chi(g)=2/9 mod 1` on the `Z3` generator;
2. `3 chi(g)=2/3 != 0 mod 1`; and
3. the same assignment is nevertheless a valid flat differential character
   with well-defined generator holonomy.

Items 2 and 3 are incompatible.  A flat line-bundle holonomy factors through
`H_1` and is a group homomorphism.  Thus an order-three loop can map only to a
third root of unity.  In additive `R/Z` notation its values are
`0,1/3,2/3`, not `2/9`.

Degree labels differ by convention: loop holonomy is degree two in the modern
cohomological convention and degree one in the shifted original
Cheeger--Simons convention.  The repair does not depend on that label.  It
depends only on flatness and the torsion relation.  A non-flat character can
obey a curvature boundary relation, and higher-degree or eta-linked
differential-cohomology constructions are not excluded.

The mathematical definition is cross-checked against Cheeger and Simons,
[*Differential characters and geometric invariants*](https://doi.org/10.1007/BFb0075216).

## Why the spectral identity is not yet h-unit

An eta value and a physical phase require a specified conversion.  The maps

```text
h -> h,
h -> pi h/2,
h -> pi h,
h -> 2 pi h
```

send `2/9` respectively to `2/9`, `pi/9`, `2pi/9`, and `4pi/9`.
Exponentiating an `R/Z` value uses the last map.  A reduced-eta phase also
contains the additive `h_B=1` correction before any multiplicative
coefficient is applied.  Determinant and eta phases can therefore differ by
statistics, kernel, sign, and normalization conventions.  The local/global
raw-magnitude equality is arithmetic support only; it cannot silently supply
the identity coefficient required by h-unit.

## What moved

- The invariant source family collapses to one nonzero doublet projector once
  repeatable-event idempotence and singlet exclusion are supplied.
- The local `C3` fixed-point density has an exact arithmetic match with the
  raw `L(3,1)` odd-signature eta magnitude, and this equality uniquely selects
  nontrivial order three in the displayed cyclic formulas.
- The remaining finite source/action freedom is localized exactly to the
  physical doublet action scale `a_d` after source idempotence.
- The old flat `2/9` holonomy carrier is removed from the live route map at
  its exact invalid step.

## What did not move

- No physical charged-lepton carrier or odd-signature operator attachment is
  derived.
- No bosonic/Grassmann statistics, functional measure, or partition function
  is derived from the formal determinant.
- No action or measure is selected by the four axioms.
- No theorem identifies the geometric density, eta invariant, source
  response, and realized charged-lepton angle as the same physical readout.
- No identity phase coefficient is derived.
- No obligation, axiom, primitive, audit row, ledger row, or TOE score changes.

## Owner decision memo

No axiom edit is justified by this finite result.  The shortest positive
target is now:

> Derive a physical charged-lepton carrier/source-action map whose selected
> `C3` triplet carries the invariant event projector `P_d`, whose positive
> quadratic action fixes the doublet eigenvalue `a_d=1` by an independently
> physical normalization, and whose correctly typed Grassmann determinant or
> eta readout (including kernel correction) identifies the resulting
> `h=2/9` with the realized angle without an inserted coefficient.

Two particularly concrete reopening routes remain:

1. derive both unit determinant and normalized trace for the physical
   invariant action, which select `A=I` on this finite family; or
2. derive a charged-lepton odd-signature operator whose physical
   exponentiated determinant supplies the identity coefficient rather than a
   `pi`-bearing one.

If neither normalization nor an equivalent inhomogeneous condition follows
from physical construction, the owner-level issue is not the arithmetic
`2/9`; it is the missing source/action and phase-readout law.  This memo does
not recommend inserting `R--eta` into the minimal ontology merely to recover
the target number.

## N1 -- Alternative route enumeration

No current science row is treated as retained authority: the live audit epoch
has zero effective retained science rows.  The citations below are therefore
route evidence or comparators, never premise supply.

| route family | disposition here | concrete evidence | live reopen/closure condition |
|---|---|---|---|
| invariant projector plus repeatable-event idempotence | `ATTEMPTED / PARTIAL` | exact `C3/K` classification in this packet | derive the physical charged-lepton event/carrier typing |
| formal determinant response plus action normalization | `ATTEMPTED / PARTIAL` | this packet; the determinant/trace countermembers | construct one physical statistics/measure/action and derive `a_d=1` plus the orbit-density factor |
| raw lens-space odd-signature eta | `ATTEMPTED / ARITHMETIC ONLY` | the explicit quotient/operator convention above; APS formula | derive the physical operator attachment and state whether the phase uses raw or reduced eta |
| flat differential character on the order-three generator | `CLOSED AT THIS STEP ONLY` | exact torsion relation and the cited April source contradiction | none within the flat order-three character class; change curvature/type to reopen |
| non-flat or higher differential-cohomology carrier | `UNTESTED / LIVE` | Cheeger--Simons permits curvature-bearing characters | construct curvature, characteristic class, carrier map, and physical evaluation cycle |
| charged-lepton `C3` Grassmann carrier/source action | `UNTESTED / LIVE` | open PRs #7334/#7340 give conditional determinant and sector comparators | derive the unital observable-preserving carrier, Berezin measure, event quotient, units, and normalization |
| Record instrument/repeatability/readout route | `UNTESTED HERE / LIVE` | open PRs #7326/#7827 give selected-law patterns | derive rather than stipulate the charged-lepton attachment and repeatability condition |
| occurrence/tick, anomaly-inflow, or owner-governance route | `UNTESTED OR NON-SCIENCE` | July h-unit notes and the registered obligation | a physical clock/anomaly theorem, or an explicit owner action clearly labelled governance |

Because several materially different physical routes remain untested, the
no-go discipline gate is `FAIL`.  The negative result is demoted to
`partial-attempt-with-named-live-routes`.

## N2 -- Wall-independence audit

| wall pair | why the first does not close the second | reverse implication? |
|---|---|---|
| physical carrier / source projector | a carrier may admit many effects | no: `P_d` can be classified on an unphysical carrier |
| source projector / action normalization | idempotence fixes `c`, not `a_d` | no: `a_d=1` would not type `P_d` as the event |
| action normalization / statistics and measure | the same matrix has bosonic and Grassmann determinant powers | no |
| raw eta / reduced eta | `bar_eta` contains the additive `h_B=1` term | no |
| eta operator / density-to-angle unit | an operator can fix eta while leaving the physical coefficient free | no |
| Record readout / source-action map | content-determined readout supplies neither source nor action | no |
| bounded proof / audit retention | a correct proposed theorem is not an independent verdict | no |

The `p=3` equality collapses none of these pairs.  No two independently named
walls have been counted as one closure.

## N3 -- Hidden-wall scan

The source and runners scan the following hidden-wall vocabulary explicitly:

| phrase | actual hit and resolution |
|---|---|
| `no-go` | restricted to the discipline gate and the flat-character step; broad gate fails |
| `cannot` | only `2/9` as flat holonomy and the prohibition on silently supplying h-unit |
| `unique` | only the finite `P_d` classification and roots of the displayed cyclic equality |
| `forced` / `must` | no physical quantity is declared forced; `must` states closure/test requirements |
| `partition function` | explicitly denied until statistics and measure are constructed |
| `group average` | true conjugation average is distinguished from the stipulated orbit-density factor |
| `eta` | operator, quotient action, metric, orientation, raw/reduced convention, and kernel are separated |
| `Record` | checked against the current axiom: it supplies neither source, action, nor scalar additivity |
| open PR | comparator-only and never retained authority |

The mutation battery independently targets each of the type, orientation,
kernel, scaling, premise, and authority failures in this table.

## N4 -- Residual matching

| cited source | content used | residual after matching |
|---|---|---|
| `MINIMAL_AXIOMS_2026-06-29.md` | current four-axiom boundary | no carrier, source/action, measure, readout context, or coefficient |
| registered R--eta obligation | exact target wording | every physical clause remains open; retirement `0` |
| July h-class and angle-native notes | prior normalization and route boundaries | no h-unit or physical carrier |
| registrable-cycle normal form | finite holonomy presentation | no physical cycle/value selection |
| April Cheeger--Simons note and runner | exact legacy `2/9` flat assignment | assignment fails the torsion character law; non-flat route not constructed |
| April radian bridge note | coefficient ambiguity | identity coefficient remains open |
| APS lens formula | raw eta under a specified operator/orientation | no charged-lepton attachment; reduced eta differs |
| Cheeger--Simons definition | flat/non-flat typing | no curvature-bearing replacement supplied |
| open #7326/#7334/#7340/#7827 | conditional construction patterns | no retained physical selection or common charged-lepton carrier |

The residual still matches the registered obligation exactly: derive the
physical fixed-locus density class and identity-read it as the eta angle with
no extra normalization, clock, kernel, statistics, or transport factor.

## N5 -- Rhetoric audit

The executable certificate reports five resolutions:

- `per_element`: all three Fourier projectors, the source rescaling, and the
  three flat-character values are exact.
- `per_site`: the finite triplet is checked only conditionally and is not
  called the physical site carrier.
- `per_mode`: singlet and conjugate-doublet modes are classified exactly.
- `per_block`: every `C3/K` invariant quadratic and projection block is
  covered, including hostile scale changes.
- `lattice_wide`: not executed; there is no physical lattice action,
  charged-lepton attachment, or end-to-end Record process.

Cached stdout must contain these resolutions plus terminal totals before the
checkpoint is committed.  No global impossibility, all-future-route no-go, or
physical forcing claim is made.

## N6 -- Partial-closure path scan

The finite projector theorem, formal response formula, normalization
counterfamilies, raw arithmetic crossing, and flat-character correction
survive the demotion.  Joint determinant-and-trace normalization is a
sufficient algebraic path to `A=I` inside the family, but is not physical until
derived from one carrier/action/measure.  Non-flat differential cohomology,
an actual eta operator, a Grassmann determinant, and a Record-facing
inhomogeneous action remain live.  This is useful partial closure, not TOE
progress.

## N7 -- Steelman

The strongest actionable positive case combines existing open constructions
without treating them as authority: use #7334's formal source/action
derivative, #7340's sector factor, #7326's event/pushforward machinery, and
#7827's repeatability pattern on one newly derived charged-lepton Grassmann
carrier.  The experiment must construct a unital observable-preserving map,
pull back the actual Berezin action and measure, derive the physical event
quotient, and survive `O -> cO` and `a_d -> lambda a_d`.  A success must fix
`c=a_d=1` and the h-unit map without fitting `2/9`.  That live construction is
why a broad no-go cannot ship.

## N8 -- Cross-cycle echo

| earlier cycle | what survives or is retired | mechanism impact now |
|---|---|---|
| April eta/radian work | eta arithmetic and coefficient ambiguity survive; flat `2/9` generator holonomy is retired | requires correct operator and character typing |
| July h-class/h-unit split | survives in full | raw equality does not supply identity units |
| August axiom reset | scalar/additive Record content was removed | Record cannot normalize the formal determinant |
| Block51 target repair | global power arithmetic was shown not to settle relative physical grain | forbids counting presentation multiplicity as an event theorem |
| open #7829--#7833 | graded composition is unselected but has exact Record-statistics consequences | makes a physical Grassmann/composition choice part of the carrier theorem |

No earlier route was silently reopened under a new name, and no previous
narrow failure was upgraded to a universal wall.

**N1--N8 verdict:** `FAIL_for_broad_negative / DEMOTE_TO_PARTIAL_NARROWING`.
The packet may be kept as a checkpoint only; it is not an audit-ready no-go or
a positive physical bridge.

## Verification

```bash
python3 scripts/reta_c3_source_response_spectral_identity_2026_09_02.py
python3 scripts/reta_c3_source_response_independent_check_2026_09_02.py
python3 scripts/reta_c3_source_response_mutation_check_2026_09_02.py
```

The primary and independent runners must close with `FAIL=0`; every
preregistered mutation must be killed.  Independent audit remains a separate
lane.
