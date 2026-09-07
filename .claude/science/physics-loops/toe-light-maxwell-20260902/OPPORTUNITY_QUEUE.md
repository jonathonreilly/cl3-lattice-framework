# Opportunity queue

| Rank | Non-fermion opportunity | Positive probability | Missing imports | Runner availability | Landability | Blast radius | Decision |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | compact `U(1)` Wilson to source-free Maxwell | high | 2 | high | **fails V1/V3 for TOE promotion** | conditional Lane 8A verification only | recovered 30/30 in draft PR #7840 |
| 2 | analytic positive plaquette-potential Maxwell universality | medium-high | 2 | high | low after Block 53 value check | reduces action-form dependence but remains supplied-action math | defer |
| 3 | full pure-gauge `beta=6` versus `beta=24` same-slot decision | medium | 1 | medium | pending fresh gate | very high downstream dependency count | **promote to next block** |
| 4 | local conservation to linear hydrodynamic sound | medium | dynamics law | medium | medium-low | broad bosonic lane | reserve |

## Promotion value gate — post-execution decision

- **V1 — FAIL for a promotion PR.** Lane 8A states a frontier target, but this
  is not a specific parent-row `verdict_rationale` obstruction. The candidate
  does not retire the action-selection or physical-observable import.
- **V2.** At main commit `36fe57a7a...`, statement searches across `docs/`,
  scripts, audit obligations, and open PR titles found scattered scalar-wave,
  polarization-count, Wilson-positivity, compact-monopole, and connection
  pieces, but no matching complete theorem. PR #7814's one-file summary is the
  closest open work; it reports an induced coefficient but does not ship the
  proof artifacts or the chain targeted here.
- **V3 — FAIL.** Once the compact Wilson action is supplied, the audit lane can
  complete the result with standard cochain calculus, Taylor bounds, a Schur
  complement, and Gauss reduction. Framework-retained primitives are not
  necessary to the derivation.
- **V4 — insufficient for promotion.** The common-carrier composition and its
  compact-sector controls are careful and the runner passed 30/30, but the
  marginal theorem is still the standard continuum behavior of a supplied
  Wilson action.
- **V5.** The closest main artifacts separately address scalar radiation,
  abstract rank counting, or Wilson positivity. The proposed composition is
  not a relabeling of those objects. This answer must be rechecked immediately
  before PR creation.

Historical decision: the first theorem/note/runner payload was deliberately
discarded. Current owner policy overrides that preservation decision. The
source is reconstructed in draft PR #7840. This remains a portfolio result,
not a physics refutation or TOE promotion: conditional Maxwell recovery is
sound, but it cannot close the physical lane until the framework supplies the
action and physical-field bridge.
