# Track D grounding — W7 gravity response program

Date: 2026-07-29  
Worker type: bounded extraction; no runner executed  
Target supplied by the task: W7 = “source/gravity meaning, reciprocal response, and a no-refit prediction attachment”

## Authorized-source status

- `scripts/frontier_source_acceptance_harness_2026_07_28.py` is absent or unreadable on this branch and was skipped. Consequently, no acceptance-set details are attributed to that file below.
- The Cycle-320, Cycle-322, and Cycle-294 Python surfaces were read.
- `docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md` was readable and was read.
- The quoted W7 wording comes from the task. The 719 wall table was not among the authorized files and was not read.

## 1. RESPONSE structure already landed, and the remaining RESPONSE LAW

### Cycle 320: local one-carrier recoil with recurrent physical transport

Cycle 320 derives a source-side recoil structure, not a gravity response law.
Its retained source channel is
`E_d <-> G_reverse(d),F_d,A_d`; it conserves `Q` and the dimensionless
unit-weight sum `P_matter + P_mediator + P_aux` at operator level
(`scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:2-10`).
For all six directions, the executable response rows separately calculate
`matter_recoil`, `mediator_flux`, and `auxiliary_flux`, and require their
unit-weight balance residual to vanish while the matter recoil remains nonzero
(`scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:775-841`).

The result is more than a bare local vertex:

- it has an exact logical/physical intertwiner through ambient lattice sizes
  `L=3,4,6`, with `L=6` held out
  (`scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:41-45`,
  `scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:878-916`);
- it derives emission, physical transport, conjugate absorption, and
  source/tag/auxiliary catch-up, including the fixed analytic
  `sin(angle)^2` emitted-weight check
  (`scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:919-1031`);
- adjacent translated source blocks commute without leakage, the update is
  covariant under all 24 proper-cubic frames and all 27 `L=3` translations,
  and the implementation has bounded 40-M2-per-cell support through held
  `L=6`
  (`scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:1082-1163`).

Its scope remains one matter carrier with
`Q=N_source+N_field=1`. The inventory itself leaves simultaneous carriers,
contact, two sources, and physical calibration open
(`scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:1285-1296`).
Thus Cycle 320 supplies a local and recurrent *recoil/flux ledger*, plus a
test-style held-out size, but not a physical gravity observable or a
gravity-calibrated prediction.

### Cycle 322: two-source reciprocity on one physical edge

Cycle 322 places two coefficient-two endpoint source vertices on the complete
`M64 x M64` two-cell physical edge code. Its declared source/mediator sector is
global `Q=1`: either reservoir `R_A`, reservoir `R_B`, or one directional
mediator
(`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:2-8`,
`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:38-46`).
Each endpoint separately has a proper-cubic unitary, preserves local matter
number and `Q`, and balances a coefficient-two vector ledger with nonzero
matter recoil
(`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:523-575`).
The full-Fock extension is already essential here: the naive one-one
carried-source product is not closed under the Cycle-315 FSWAP, whereas the
full-Fock source extension is used
(`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:579-633`).

The actual reciprocal-response object is a `2 x 2` reservoir occupation
matrix. Starting from a supplied symmetric one-one matter state, the code
places the input in one of the two reservoirs, advances exactly two updates,
and reads the final reservoir weights
(`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:771-799`).
Across ambient `L=3,4,6` (held `L=6`), it derives:

- nonzero off-diagonal transfer;
- equality of the two off-diagonal entries;
- equality of the diagonal entries;
- norm preservation; and
- loss or differentiation of the response under receiver, stream, and
  source-exchange deletion controls
  (`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:802-851`).

The response is therefore reciprocal at the scope of **two source endpoints,
one Cycle-315 edge, global `Q=1`, and two update depths**. The ambient volume
varies and the family is translation/cubic covariant with bounded support, but
the number and topology of sources do not: multi-edge recurrence, global
`Q=2`, the Cycle-320 unit-weight full-Fock lift, alternate mediators, and
energy/stress/metric remain open
(`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:911-978`,
`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:1046-1057`).

### Exact missing law

Neither landed response answers the source ledger with a derived
field/deformation/metric variable and a dynamical or constraint equation for
that variable. Cycle 320 derives dimensionless recoil/flux balance; Cycle 322
derives finite reservoir-occupation transfer. Neither derives:

1. a physical source map (for example, from the finite ledger to a
   gravity-source quantity);
2. a field/metric-side response carrier and update or constraint;
3. the physical calibration/units identifying that response as gravity; or
4. a fixed-parameter observable prediction tested out of sample without a
   response-side refit.

The existing held-size checks are valuable anti-refit *test structure*, but
their checked outputs are still source-sector occupation/recoil quantities.
They are not yet W7's physical no-refit gravity prediction attachment.

## 2. Cycle 294 bridge tournament

The Cycle-294 synthesis keeps three routes independent:

- Route A: direct gatewise matter/mediator current ledger;
- Route B: local-M2 mass-scalar deformation response;
- Route C: bounded direct-current search
  (`scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:27-47`).

It checks that all three independent runners passed their reviewed totals, but
also that they have no common code/update and “do not silently form one law”
(`scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:111-165`).
The synthesis contract additionally requires “not one combined law,”
“externally supplied additive,” “not the autonomous hard-core vertex
history,” “no shared obstruction,” and “no axiom pressure”
(`scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:70-108`).
The bridge-tournament conclusion is therefore **non-closure**: three passing,
useful source/deformation/current surfaces do not compose a source-to-gravity
law, and their failure to compose does not establish a common no-go theorem.

There are two precise senses of “strongest” on the authorized executable
surface:

- **Strongest named gravity-facing route:** Route B, because it is the only
  named route whose surface is explicitly a mass-scalar *deformation
  response*, and the synthesis contract names a “physical local deformation
  layer”
  (`scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:35-39`,
  `scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:75-84`).
  This is a relevance classification, not a tournament-certified winner.
- **Strongest exact synthesis identity:** the selected additive port-kernel
  comparator. On a supplied zero-mean periodic `rho`, it gives exactly
  `-rho/2` across sides 3, 5, 7, and 9
  (`scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:174-198`).
  The same lines explicitly say this is not the autonomous vertex history.

The file does not literally rank A/B/C or contain a future-cycle label named
“next.” What it actually performs next is the selected port-kernel comparison.
The forced scientific next step is consequently an autonomous or explicitly
conditional **response-side law test**: preserve the independently derived
source structure, declare any candidate field/deformation response as supplied,
and test whether one fixed candidate survives covariance, reciprocity,
deletions, held sizes, and no-refit prediction checks. It may not promote the
conditional comparator into autonomous gravity content; Cycle 294 says its
runner “does not splice routes, name occupation probability energy, or promote
a selected source-port residual to an autonomous-law obstruction”
(`scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:2-8`).

## 3. `C_source` firewall — verbatim operative declarations

The authorized scripts do not expose a standalone prose definition assigned
to a Python constant named `C_source`; Cycle 294 instead requires that token in
its synthesis note contract
(`scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:95-105`).
The surfaces' own operative prohibitions are:

> “No physical momentum, work, energy, stress, or gravity meaning is assigned.”

— `scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:9-10`

> “dimensionless direction/flux only; not physical momentum, work, energy, stress, gravity, or metric”

— `scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py:1296`

> “The result is a bounded common-code response/reciprocity proxy, not physical energy, stress, gravity, metric, or time.”

— `scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:7-8`

> “finite occupation response only; not energy, stress, gravity, metric, force, or time”

— `scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:1057`

> “does not splice routes, name occupation probability energy, or promote a selected source-port residual to an autonomous-law obstruction.”

— `scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:4-7`

Cycle 294 also tests the three route declarations verbatim as
“probability/configuration current, not energy,” “not physical energy,” and
“nothing here calls it physical energy or stress”
(`scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py:166-170`).

Therefore the only lawful response-law cycle has this shape:

1. retain the source/recoil/reciprocity results as derived mathematical
   structure;
2. declare any response carrier, kernel, calibration, or field/metric
   interpretation as a supplied candidate unless independently derived;
3. derive consequences, symmetries, consistency conditions, deletion
   signatures, and held-out predictions from that declared candidate; and
4. never relabel occupation, number/configuration current, or dimensionless
   direction/flux as energy, stress, force, gravity, or metric.

Cycle 693 supplies the relevant general proof discipline: deriving an additive
factorization does not derive the physical carrier
(`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:68-78`),
and even a canonical mathematical construction still needs a bridge identifying
it as the physical product
(`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:125-139`).
For W7, reciprocal response structure is analogous to that factorization:
derived structure narrows the missing content but does not supply gravity
meaning.

## 4. Candidate routes for raising the gravity-bridge column

| Candidate | Classification | First-cycle scope and pass condition | W7 value / firewall |
|---|---|---|---|
| **R1. Multi-source reciprocity extension** | `DERIVED_STRUCTURE`; direct continuation | Extend the one-edge two-reservoir construction to three source cells on a connected two-edge patch, initially retaining global `Q=1`. Derive a fixed-depth `3 x 3` occupation-response kernel; require off-diagonal reciprocity, cubic/translation covariance, bounded support, receiver/stream deletions, and an untouched held `L=6` check. | Raises reciprocal-response scope beyond two endpoints. It remains a finite occupation kernel and must carry the Cycle-322 firewall verbatim. |
| **R2. Response-comparison harness** | `COMPARATOR / ACCEPTANCE INFRASTRUCTURE`; strongest immediate W7-facing route | Freeze a public acceptance set before evaluation: common lawful source input, fixed candidate parameters, covariance/locality checks, reciprocity residual, deletion signatures, zero-mode/domain handling, and a held-size no-refit prediction. Compare Route-B-style local deformation, the Cycle-294 selected port kernel, and any other explicitly supplied response candidate without splicing them. | Directly targets the response-law and no-refit parts of W7 while keeping all candidate gravity content supplied. The July 28 harness is absent, so this is a proposed use of the task-specified acceptance-set pattern, not an extraction of that file's implementation. |
| **R3. Cycle-320 full-Fock two-source lift** | `ENABLING REPRESENTATION`; prerequisite, not a gravity bridge by itself | Put the Cycle-320 unit-weight auxiliary source on the Cycle-322 complete full-Fock two-endpoint seam; first retain global `Q=1`, prove closure under FSWAP/contact, exact unit-weight recoil at both endpoints, and the same `2 x 2` reciprocity/deletion controls. Defer global `Q=2` simultaneous emission to a later cycle. | Removes the mismatch between Cycle 320's physically balanced recoil and Cycle 322's full-Fock reciprocity. Cycle 322 explicitly lists the “Cycle320 unit-weight full-Fock lift” as open (`scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py:1046-1057`). It supplies no field/metric content. |
| **R4. Conditional field/deformation response theorem** | `CONDITIONAL_BRIDGE`; highest semantic leverage, highest firewall risk | Supply one response carrier and one kernel/update explicitly. On the landed source ledger, derive its Green/response reciprocity, cubic and translation covariance, locality/support or controlled nonlocality, source deletion, calibration dependence, and one fixed held-out observable. Compare against the exact conditional `-rho/2` port identity rather than calling that identity autonomous. | This is the only candidate that places an answering object on the field/deformation side. It raises W7 only conditionally until a separate retained theorem identifies the carrier, source map, calibration, and observable as physical gravity. |

Recommended ordering is **R2 → R3/R1 → R4**: freeze the response acceptance
contract first; remove the full-Fock/unit-weight representation gap and extend
reciprocity scope; then test a supplied field/deformation candidate without
refit. R2 is the strongest immediate programmatic route because it makes a
response law fail or survive on predeclared evidence, while R4 is the only
route capable of semantic closure if its physical identifications are later
independently grounded.

## 5. Stakes

**Minimal missing content if these routes fail:** W7 still lacks one
independently grounded field/metric response law mapping the already-derived
finite source/recoil ledger to a physically calibrated gravity response, plus
one fixed-parameter held-out observable prediction requiring no response-side
refit.

The negative verdict would not erase Cycles 320/322: their recoil,
intertwining, transport, covariance, and finite reciprocal occupation response
would remain derived. It would mean only that those source-side structures do
not determine gravity content.
