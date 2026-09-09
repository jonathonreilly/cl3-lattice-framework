---
claim_id: ac_occupancy_grain_support_typed_formal_target_repair_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "Exact projective support theorem distinguishing global determinant-power doubling from sector-local occupancy duplication; current-epoch audit of the AC occupancy-grain closure wording; reconciliation with open PR #7340 at prior-art status; and a conditional Record-odds discriminator. No physical carrier, action, measure, event partition, probability law, charged-lepton value, axiom update, audit verdict, or obligation retirement is derived."
upstream_dependencies: []
runner: scripts/ac_occupancy_grain_support_typed_target_repair_2026_09_02.py
---

# AC Occupancy Grain: Support-Typed Formal-Target Repair

**Date:** 2026-09-02
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded target-integrity support
**Audit-status authority:** independent audit lane only.  This source sets no
audit verdict and predicts none.
**Primary runner:**
[`scripts/ac_occupancy_grain_support_typed_target_repair_2026_09_02.py`](../scripts/ac_occupancy_grain_support_typed_target_repair_2026_09_02.py)
**Independent runner:**
[`scripts/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.py`](../scripts/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.py)
**Primary cache:**
[`logs/runner-cache/ac_occupancy_grain_support_typed_target_repair_2026_09_02.txt`](../logs/runner-cache/ac_occupancy_grain_support_typed_target_repair_2026_09_02.txt)
**Independent cache:**
[`logs/runner-cache/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.txt`](../logs/runner-cache/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.txt)

## Result up front

The registered AC occupancy-grain obligation has the right physical question
in its Exact target: does the charged-lepton matter action count the conjugate
doublet as one K/CPT orbit or as its separate channels?  Its Closure criterion
then abbreviates that question as

```text
det_C / holomorphic count-once
versus
|det_C|^2 / realified count-twice.
```

That abbreviation is under-typed.  Two distinct operations fit it:

1. **Global full-carrier squaring** multiplies every sector exponent by the
   same number.  It leaves every projective singlet/doublet ratio unchanged.
2. **Doublet-sector-local duplication with the singlet held fixed** adds
   support only in the doublet sector.  It changes the relative occupancy
   grain and may change the conditional Koide dial.

The exact criterion is support-sensitive.  If the current support vector is
`nu=(nu_s,nu_d)` and a new carrier/copy contributes `q=(q_s,q_d)`, then under
the explicitly conditional balance map

```text
r(nu)=nu_d/(2 nu_s)
```

one has

```text
r(nu+q)-r(nu)
 = (nu_s q_d-nu_d q_s)/(2 nu_s(nu_s+q_s)).
```

The candidate `r` changes exactly when the added support is not proportional
to the old support.  This is a projective algebra theorem, not a derivation of
the balance map or of a physical support vector.

Open PR #7340 is consistent with this theorem.  Its exponent-two result is a
`c`/doublet-sector factor after the `k=0` singlet fiber is divided out.  It is
therefore a sector-local `(1,1)->(1,2)` support move, not global determinant
squaring.  The PR itself leaves the physical carrier, sector identification,
singlet calibration, and slot-to-`r` bridge supplied or proposed.  It remains
prior art, not current premise authority.

The obligation remains open.  The current four axioms and three
approved primitives declare none of the needed physical carrier, action,
measure, K/CPT event partition, sector factorization, or relative-support
bridge.  In particular, the approved realized-state primitive classifies a
charged-lepton sector weight pattern such as `r` as registered state data,
never as a value forced merely by having a realized-state slot.  No axiom
amendment follows from the algebra.

## Exact support theorem

### 1. The physical comparison object

Let `nu_s>0` and `nu_d>0` denote the induced physical weights, determinant
degrees, or independent-cell multiplicities of the singlet and doublet only
after a theorem has typed those numbers on the physical matter measure.
Their common scale is irrelevant to the candidate endpoint.  The comparison
object is the ray

```text
[nu_s:nu_d].
```

The familiar charged-lepton balance arithmetic uses

```text
E_s=3a^2,
E_d=6|b|^2,
r=|b|^2/a^2.
```

If, and only if as an explicit premise, the physical balance law identifies
`E_s:E_d=nu_s:nu_d`, then

```text
r(nu)=nu_d/(2 nu_s),
Q=(1+2r)/3=(nu_s+nu_d)/(3 nu_s).
```

Consequently `(1,1)` gives the candidate endpoint `r=1/2`, `Q=2/3`, while
`(1,2)` gives `r=1`, `Q=1`.  The arithmetic does not supply the balance law.

### 2. Necessary and sufficient support condition

For an added support vector `q=(q_s,q_d)`, direct subtraction gives

```text
(nu_d+q_d)/(2(nu_s+q_s))-nu_d/(2nu_s)
 = (nu_s q_d-nu_d q_s)/(2nu_s(nu_s+q_s)).
```

On the positive domain, the denominator is nonzero.  Therefore

```text
r(nu+q) != r(nu)
iff
nu_s q_d-nu_d q_s != 0.
```

This is equivalently the statement that `q` is not proportional to `nu`.
It is necessary and sufficient for changing the projective support ratio.  It
is not sufficient for physical selection: the carrier, action, measure,
factorization, and balance map still require physical derivation.

### 3. The two operations that must not be conflated

On a K-real three-channel spectral surface write

```text
D=lambda_s lambda_+ lambda_-
 =lambda_s |lambda_+|^2.
```

In channel-degree coordinates,

```text
deg(D)=(1,2),
deg(D conjugate(D))=(2,4).
```

In aggregated singlet/doublet-factor coordinates the same global operation is
`(1,1)->(2,2)`.  Both descriptions multiply the whole vector by two.  The
projective ratio is unchanged.

By contrast, a physical measure with one singlet cell and one doublet orbit
cell has `(nu_s,nu_d)=(1,1)`.  Adding an independently physical second
doublet/channel cell while leaving the singlet factor fixed gives `(1,2)`.
Here `q=(0,1)`, so the support determinant is nonzero and the ratio changes.

Thus determinant power is informative for this lane only after its **sector
support** has been derived.  The bare words first power and second power do not
specify that support.

## Realification and fermion typing

For a complex matrix `K=X+iY`, ordinary realification obeys

```text
R(K)=[[X,-Y],[Y,X]],
det_R R(K)=det_C K det_C conjugate(K)=|det_C K|^2.
```

This operation doubles the entire complex carrier.  It must not be silently
applied only to a selected sector.

For one complex Grassmann Gaussian, the skew kernel

```text
A_K=[[0,K],[-K^T,0]]
```

has `Pf(A_K)=(-1)^(n(n-1)/2) det_C K`.  An invertible coordinate change acts
by congruence on `A_K`; its Pfaffian determinant factor cancels the inverse
Berezin Jacobian.  Rewriting one complex field in Majorana-paired coordinates
therefore preserves determinant power one.  The second power in this finite
construction appears only after an independently integrated conjugate block is
adjoined.

The generation algebra `R direct-sum C` has real dimension three and is not
the ordinary realification of a complex vector space.  A physical mixed
real/complex polarization may still be supplied, but it must state which
sector is real, which is complex, which fields are independent, and which
measure is integrated.  The word realified is not a substitute for those
facts.

## Reconciliation with the latest relevant PRs

Open PR heads are novelty comparators only:

| PR | Pinned head | Relevant content | Why it does not close this obligation |
|---|---|---|---|
| #7334 | `412c30cfc6e7eb8d649c34ad703d140b217f8ac1` | normalized Gaussian source functional, Wick tower, one-copy/doubled distinction | source/reflection event selector and physical sewing remain open |
| #7337 | `a1c71f03e7474eb91aafce8958a1a02cb1e24930` | one-orbit module map and multiplicity residue | physical star-algebra map, observable preservation, Record identity, and fiber theorem remain open |
| #7340 | `b2664db3fc277983cf657fc6ad47db860b7a49fe` | `c`-sector factor has two cells; `Fix(-Theta o X_0)` has one | field reality choice is proposed; flavor bridge and slot map are imported |
| #7829 | `551dfd9f317a36db050dffa0d717764f9af9f291` | graded composition candidate | selects no Hamiltonian, action, state, or measure |
| #7830 | `f8581d80efdd0856aa1a64078a48931a763765e9` | conditional even-algebra Born form | selects no weight values or physical state |
| #7831 | `ff8573cf054125db0dd0fcf07dba131280b6b736` | conditional one-site Lüders cell | supplies no formation rule or action |
| #7832 | `9301c509842ea4835def91ad50f41bfd4f80ab1c` | conditional hopping-response relocation | leaves a six-dimensional response family and no selected dynamics |

The exact #7340 reconciliation is

```text
F_c=det(record slice)/det(k=0 singlet fiber)=u^2.
```

The singlet fiber has already been removed.  Reading `u^2` as two doublet
cells relative to an external one-cell singlet is a sector-local support move.
It can feed the conditional slot arithmetic.  It is not the global map
`D->D conjugate(D)`, and its exact finite-fixture identity alone does not prove
the physical sector map or the energy/readout bridge.

## Current premise-epoch boundary

Current Record says that records form, a present record locks exactly one
admissible local possibility, at most one permanent record occupies a site,
only records are readable, and readout depends on content.  It does not identify
one local possibility with a K/CPT orbit, a Grassmann copy, a determinant
factor, or a charged-lepton sector.

The 2026-08-13 owner-approved reset removed the named scalar collection
functional `I`, finite additivity, and `I(empty)=0`.  Several July route notes
quote that retired sentence as Record content.  Their wider nonselection
conclusions may survive, but their Record-derived affine/stationarity steps
cannot be imported into a current-epoch closure without fresh review.  This
strengthens the need for a physical event/action bridge; it does not justify
restoring the removed sentence or editing an axiom.

The approved primitives add units, kinetic isotropy, and a pointwise realized
state slot at their declared scopes.  They add no charged-lepton matter action,
functional measure, K/CPT partition, field reality condition, event codec,
or support-to-energy map.  This inventory was checked against the canonical
[`axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json) registry and
each registered primitive's current source, rather than inferred from older
framework prose.

## Conditional Record-only discriminator

A future supplied writer can distinguish a single factor from its square
without an absolute rate.  Let a controlled positive source `x` produce a
binary final-Record law

```text
p_n(1|x)=x^n/(1+x^n),
p_n(0|x)=1/(1+x^n).
```

Then final Record odds are `O_n(x)=x^n`.  Comparing two controlled source
settings gives

```text
O_n(4)/O_n(2)=2^n,
```

which is `2` for one copy and `4` for two.  Common normalization and a common
formation-rate scale cancel.

This is a conditional operational falsifier, not a law derived from Record.
It requires repeated trials, a controlled physical source, a common event
codec, eligibility calibration, and an action-to-Admissibility probability
bridge.  It distinguishes power support; it does not by itself identify the
charged-lepton sector or select the Koide balance map.

## Proposed corrected target

The following is decision-memo wording only.  It does not edit the canonical
obligation or registry:

> Derive the physical charged-lepton carrier, action, measure, and K/CPT
> action; prove a presentation-independent factorization
> `Z_phys=Z_s F_d^n Z_rest` in which the singlet factor and normalization are
> held fixed; and derive whether `n=1` (one K/CPT-orbit cell) or `n=2` (two
> independently physical channel cells).  Track any global conjugate copy
> separately: it changes the relative occupancy grain only when its support is
> anisotropic between the singlet and doublet sectors.  Do not insert the
> desired charged-lepton value or readout dictionary.

This wording keeps the obligation's original physical target and makes its
closure test necessary and sufficient at the support level.  A retained-grade
physical theorem and independent audit would still be needed to retire it.

## No-go discipline gate

**Result:** `PASS` for the narrow current-authority and global-common-power
boundary below.  It would be `FAIL` for a universal no-go.  The positive
physical-action, carrier, event, writer, and owner-governance routes remain
open.  This is therefore a `partial-narrowing`, not a claim that the target can
never be closed.

## N1 — Alternative route enumeration

The families are normalized by `(primary object, mechanism, terminal
obligation)`, not by agent, wording, or artifact.  `ATTEMPTED` means the family
was exercised or authority-checked in this cycle; none is presented as ruled
out by an unaudited historical note.

| Family and normalized route class | Primary object / mechanism / terminal obligation | Honesty | Current-cycle result and authority |
|---|---|---|---|
| `F1` dynamical-or-effective-action | complex CAR carrier / Berezin integration and independent-field content / derive the physical charged-lepton action and measure | **ATTEMPTED** | The runner proves the one-copy Pfaffian and independently doubled alternatives, but current Admissibility explicitly selects no dynamics or action ([minimal axioms, lines 116-130](MINIMAL_AXIOMS_2026-06-29.md)); route remains open. |
| `F2` alternate-carrier-or-sector | K-orbit quotient versus channel atoms / induced quotient or pushforward measure / derive which physical event partition the action realizes | **ATTEMPTED** | The exact orbit census gives both candidate grains; current Record explicitly leaves K/CPT orbit structure downstream ([minimal axioms, lines 163-171](MINIMAL_AXIOMS_2026-06-29.md)); route remains open. |
| `F3` symmetry-or-representation | real, complex, or Majorana carrier / star-compatible reality constraint and Pfaffian orientation / derive the physical polarization and its sector support | **ATTEMPTED** | Exact realification and Pfaffian congruence checks separate coordinate rewriting from an independent copy, while the only pinned fork states `POLARIZATION-SELECT` as conditional ([fork note, lines 44-52](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)); route remains open. |
| `F4` algebraic-rearrangement | determinant support ray / projective-degree invariant / select the relative occupancy grain from determinant power alone | **ATTEMPTED** | The exact support identity proves global `(1,2)->(2,4)` scaling is projectively neutral; only anisotropic support can move the ratio.  This family fails as a stand-alone selector but remains usable after `F1` or `F2` supplies physical typing. |
| `F5` alternate-observable-or-readout | repeated final Records / common-menu odds exponent / operationally discriminate one physical factor from two | **ATTEMPTED** | The exact odds ratio distinguishes exponents one and two, but Record supplies neither a writer nor action-to-probability bridge ([minimal axioms, lines 75-84 and 116-130](MINIMAL_AXIOMS_2026-06-29.md)); route remains open. |
| `F6` dependency-or-registry-reclassification | foundation registry / explicit owner approval / register a narrow physical premise if derivation fails | **ATTEMPTED** | The canonical registry contains only the four axioms plus scale, kinetic-isotropy, and realized-state primitives; none declares this selector ([registry](audit/data/axiom_premise_nodes.json)).  This is a live governance route, not a derivation and not permission for a silent import. |

These six families differ in primary object, load-bearing mechanism, or
terminal obligation.  The one narrow route actually closed is `F4` as a
stand-alone global-power selector; the five positive routes are preserved.

## N2 — Wall-independence audit

After collapsing carrier, selected action, independent-field content, and
functional measure into one construction obligation `W_AM`, the physical wall
set is:

- `W_AM`: construct the physical carrier/action/measure;
- `W_E`: derive its singlet/doublet/K event factorization;
- `W_K`: derive the support-to-energy or physical readout map;
- `W_P`: for the operational route, derive source/action weights to the
  Admissibility probability law;
- `W_R`: for the operational route, construct repeated-Record eligibility,
  context, and a common event codec.

Pairwise implication was checked explicitly:

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| `W_AM`, `W_E` | no | no | yes |
| `W_AM`, `W_K` | no | no | yes |
| `W_AM`, `W_P` | no | no | yes |
| `W_AM`, `W_R` | no | no | yes |
| `W_E`, `W_K` | no | no | yes |
| `W_E`, `W_P` | no | no | yes |
| `W_E`, `W_R` | no | no | yes |
| `W_K`, `W_P` | no | no | yes |
| `W_K`, `W_R` | no | no | yes |
| `W_P`, `W_R` | no | no | yes |

Independent audit/retention is a publication gate, not a sixth physical wall.
A single theorem may of course discharge several rows at once, but no row
follows logically from another as currently defined.

## N3 — Hidden-wall scan

Outside the checklist's own quoted scan vocabulary, the required phrase scan
found `registered` and `canonical`.  Every occurrence is classified here:

| Occurrence | Classification |
|---|---|
| registered AC obligation | cited authority identity: the canonical obligation source and live ledger row |
| registered state data | cited authority: `realized_state_primitive`, which explicitly gives the classification |
| registered primitive sources | cited authority: `axiom_premise_nodes.json` and each `current_path` source |
| owner-approved route becoming registered | explicit future governance route, not a premise used by this theorem |
| canonical obligation / registry / ledger metadata | cited identity of the current governed source, never a claim that the physical construction is unique |
| quoted N3 scan phrases in this section | non-load-bearing audit vocabulary recorded solely to make the scan reproducible |

No substantive occurrence of `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, or `standard QFT` occurs outside that audit list.
Separate explicit conditions remain
coordinate choice, determinant phase, singular kernels, Berezin orientation,
branch cuts, K-real restriction, field-copy independence, source
normalization, event calibration, current axiom epoch, open-PR status, and the
energy-balance dictionary.  The displayed theorem is only on positive support
rays; physical use of those rays is open.

## N4 — Residual matching

The exact residual is:

```text
derive Z_phys=Z_s F_d^n Z_rest and the physical event/energy map,
with n fixed as one or two and the singlet normalization held fixed.
```

No unaudited historical note or open PR is used as negative authority:

| Cited witness and locator | Witness residual | This note's residual | Match? / treatment |
|---|---|---|---|
| [canonical obligation, lines 9-24](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md) | derive physical action/measure and select orbit versus channels | same target, with sector support made explicit | **yes** — target authority, not proof |
| [minimal axioms, lines 116-130 and 163-171](MINIMAL_AXIOMS_2026-06-29.md) | dynamics/action and K/CPT structures are downstream | current-authority nonsupply only | **yes** — approved premise authority |
| [determinant-support note, lines 71-101](ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md) | first versus second determinant powers; physical identification open | global power versus relative sector support | **partial** — unaudited prior art, dropped as authority |
| [Pfaffian note, lines 67-106](ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md) | ordinary realification versus doubled Grassmann carrier | independent physical copy and sector support | **partial** — unaudited prior art, dropped as authority |
| [fork note, lines 44-73](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md) | supplied polarization chooses conditional counting horn | derive polarization/action physically | **partial** — unaudited prior art, dropped as authority |
| open PR #7340 at pinned head | sector-local two-cell versus one-cell finite fixture | physical carrier/action/factorization and readout map | **no** as closure witness — positive comparator only |

After the drops, the bounded current-authority statement rests only on the
approved foundation inventory and this cycle's exact algebra.  The historical
surfaces establish search history, not retained support.

## N5 — Rhetoric audit

The cached primary stdout contains substantive `per_element:`, `per_site:`,
`per_mode:`, `per_block:`, and `lattice_wide:` execution-certificate lines.
The runner exercises the finite support elements and matrix block, and marks
site-, mode-, and lattice-wide scopes checked but not executed because no such
physical action is supplied.  Accordingly the note makes no lattice-wide or
all-future no-go, no metaphysical impossibility claim, and no claim that a
physical selector is forced.  Biconditional words apply only to the exact
positive-ray support identity; prescriptive words in the corrected target are
contract language, not a derived physical law.

## N6 — Partial-closure path scan

The primitive registry check confirms that scale, kinetic isotropy, and the
realized-state slot are approved and must not be counted as walls.  It also
confirms that none supplies a mass ratio, selector, source/action, event codec,
or measure.  The prior labeling-only escape used in the staggered species-map
campaign does not transfer: naming two factors cannot decide whether the
physical path integral contains one independent field or two.  The
realized-state primitive can classify a chosen `r` as state data, but that does
not derive the physical multiplicity requested by this obligation.

Preserved partial closures are the exact determinant and Pfaffian identities,
coordinate invariance of one complex Gaussian, K-orbit census, anisotropic-
support iff criterion, #7340's conditional sector-local factor, current-
premise reset, and conditional odds-exponent discriminator.  Any explicit
future action import should be followed by a bounded theorem and an
import-retirement audit; it must not be silently promoted to an axiom.

## N7 — Steelman

A hostile reviewer can break any broader no-go with a concrete sector-local
construction: let the physical charged-lepton carrier decompose as a real
singlet plus a complex K-paired doublet, derive a star-preserving inclusion of
that carrier into the lattice CAR algebra, show that the induced Berezin
measure factors as `Z_s F_d^2 Z_rest`, and prove that the Record event quotient
pushes the two independent doublet cells onto the charged-lepton readout while
leaving `Z_s` fixed.  That would turn `det_C K` versus `|det_C K|^2` into valid
sector-local shorthand and make #7340 a useful finite lemma.  The terminal
obligation is the observable-preserving carrier/action/measure pushforward,
not another determinant identity.  This concrete route is unclosed, so the
present result is deliberately demoted to partial narrowing.

## N8 — Cross-cycle echo

| Similar prior wall | Later state / retirement mechanism | Transfer test here |
|---|---|---|
| staggered species labeling | a naming convention can close label assignment without new physics | does **not** close independent-field multiplicity; retained only as a warning not to call every convention an axiom |
| observable-principle structural reframe | renaming `log Z` as a cumulant convention did not remove the physical-identification step | directly analogous: calling a factor `realified` does not derive its physical carrier |
| June power-not-count and July determinant/Pfaffian routes | current ledger status is unaudited after premise-epoch invalidation | core algebra is rerun here; no old negative verdict is inherited |
| August 13 Record reset | removed scalar additivity by owner-approved axiom revision | old affine/stationarity arguments require fresh review; the removed clause is not silently restored |
| approved-primitive registration pattern | owner approval plus registry update can turn a supplied structural input into a chain-satisfying premise | available only if the owner chooses a genuinely narrow clause; no amendment is recommended by this algebra alone |

The marginal contribution is therefore narrow but real: current-epoch exact
verification, the support-increment theorem, explicit #7340 reconciliation,
and a corrected positive target.  It is not advertised as a new determinant
discovery or as direct TOE-lane movement.

## Value gate and TOE accounting

| Gate | Result |
|---|---|
| V1: retire the registered obligation | **FAIL** — physical carrier/action/measure/event chain absent |
| V2: material novelty | **NARROW ONLY** — #7340 reconciliation and current-epoch packaging; core theorem is prior art |
| V3: not synthesizable from current content | **FAIL** for the algebra; physical selector remains unsupplied |
| V4: carrier/lattice-wide physical theorem | **FAIL** — no physical intertwiner or measure pushforward |
| V5: structurally distinct from prior art | **FAIL** for closure; exact support typing is a repair checkpoint |

PR disposition: `BACKLOG_NO_PR`.

Obligation retirement: `0`.

TOE percentage movement: `0`.

Retained-positive end-to-end theory count change: `0`.

Axiom amendment: `none`.

This is meaningful program progress because it prevents a critical false
discharge across a live graph with sixteen direct consumers and one hundred
eight transitive descendants.  It is not direct TOE-lane progress.

Open PRs are prior-art comparators only.

## Verification

Run:

```bash
python3 scripts/ac_occupancy_grain_support_typed_target_repair_2026_09_02.py
python3 scripts/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.py
```

The primary runner checks source hashes, the complete approved-primitive
registry, exact orbit and support algebra, realification/Pfaffian typing, the
conditional odds discriminator, canonical live-ledger blast-radius metadata,
current premise wording, N5 resolution, and governance boundaries.  The
independent runner uses separate exact implementations.
