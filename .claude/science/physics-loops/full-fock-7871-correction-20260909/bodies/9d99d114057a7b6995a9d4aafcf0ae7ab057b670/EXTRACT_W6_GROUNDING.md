# Track C grounding — W6 Born weight-receiver bridge

Date: 2026-07-29

Status: bounded extraction from the five authorized surfaces only; no claim is made about the scope of sources outside that set.

## Source keys

- `F729` — `/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-cleanup-local-worktrees-5f598b/69c3b549-2cbd-469d-b08a-a04a7c8896f8/scratchpad/refs/ref_cycle729_born_surface_feed.py`
- `N729` — `/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-cleanup-local-worktrees-5f598b/69c3b549-2cbd-469d-b08a-a04a7c8896f8/scratchpad/refs/ref_CYCLE729_NOTE.md`
- `B317` — `scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py`
- `R317` — `scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py`
- `H728` — `scripts/frontier_born_acceptance_harness_2026_07_28.py`

## 1. Frozen 729 inventory and the zero-receiver result

`F729` does not hand-maintain a second notion of “signature”: it obtains the live parameter names with `inspect.signature(...).parameters` (`F729:296-300`), compares the result for exact equality with the frozen inventory (`F729:649-674`), and freezes the following twenty entries verbatim (`F729:76-97`):

```python
FROZEN_PORT_INVENTORY = {
    "basis": ("dimension", "index"),
    "binary_and_ternary_threshold_controls": ("trine_effects",),
    "check": ("label", "condition", "detail"),
    "contact_trine_controls": ("fixture",),
    "deletion_domain_and_semantic_controls": ("fixture", "forcing_kraus"),
    "derived_effects": ("isometry", "groups"),
    "main": (),
    "menu_metrics": ("effects",),
    "merge_isometry": ("weighted_projectors", "contact"),
    "mixed_projective_forcing_basis_controls": ("fixture",),
    "nonlinear_binary_weight": ("effect",),
    "normalized": ("path",),
    "note_contract": (),
    "physical_fixture": ("length",),
    "physical_isometry": ("two_ray_encoding", "kraus"),
    "physical_locality_and_covariance_controls": ("fixtures", "route_kraus"),
    "physical_subcode_controls": (),
    "projector_bloch": ("vector",),
    "split_projector_isometry": ("projector", "splits", "contact"),
    "stack_isometry": ("kraus",),
}
```

Thus the accepted quantities are exactly the parameter tuples shown: dimensions/indices; effects; labels/conditions/details; physical fixtures; Kraus families; isometries and pointer groups; projective components and contact; paths and lengths; two-ray encodings; Bloch vectors; and split coefficients. Empty tuples accept no quantity.

The two genuine census-facing apparatus ports are especially sharp:

- `projector_bloch(vector)` accepts one unit three-vector and rejects every other shape or norm (`B317:119-123`). In the 729 feed, three census field-one counts are L2-normalized exactly once and supplied as that apparatus direction (`F729:405-442`).
- `merge_isometry(weighted_projectors, contact)` accepts one to four `(coefficient, rank-one projector)` components; coefficients must be nonnegative and total at most one (`B317:422-452`). The 729 feed divides four base-stage handoff counts by their total and explicitly labels the result `"supplied apparatus coefficients"` and `"explicitly_not": "Born weights w(E)"` (`F729:473-520`).

The apparent exceptions are not receivers:

- `nonlinear_binary_weight(effect)` takes an already supplied/derived effect, uses a fixed `sigma0`, and returns a hard-coded counterfunctional (`B317:358-361`). The frozen boundary says verbatim: `"hard-coded counterfunctional of one supplied effect; not a configurable numerical-weight or census receiver"` (`F729:679-682`).
- `merge_isometry(weighted_projectors, contact)` contains the word “weighted” inside a compound parameter, but the frozen boundary says verbatim: `"weighted_projectors receives apparatus coefficients only"` (`F729:683-685`).

The receiver census checks parameter names for `calibration`, `count`, `epoch`, `exposure`, `frequenc`, `occurrence`, `record`, `row`, and `sampling` (`F729:98-108,649-665`). It finds none. Its verdict is verbatim:

> `"FROZEN FINDING no_census_weight_receiver matches all 20 live signatures and finds no count/frequency/exposure/Record-row port"` (`F729:687-693`).

That is a bounded signature result, not a universal no-go: all twenty live signatures match the extract, and none accepts the raw material from which an occurrence-driven weight could be derived.

## 2. Where `w(E)` currently lives, and the missing receiver contract

There is no supplied weight table and no top-level configurable `w` port. The landed positive candidate lives only inside a control as a **held per-effect function**:

```python
# A trace-form candidate satisfies every compiled normalization,
# refinement, and same-effect identity.  This is a consistency check,
# not a derivation or selection of the weight functional.
bloch = np.asarray((0.21, -0.32, 0.41), dtype=float)
sigma = (I2 + bloch[0] * X + bloch[1] * Y + bloch[2] * Z) / 2

def born_weight(effect: np.ndarray) -> float:
    return float(np.trace(sigma @ effect).real)
```

This is verbatim from `B317:599-606`. It is evaluated effect by effect and checked for menu normalization, refinement, merge, and same-effect consistency (`B317:608-634`). The surface itself says this is “candidate consistency only” and that effect functionality and eligibility are not derived (`B317:632-634`). Logical status therefore remains **supplied/held hypothesis**, even though each scalar is numerically computed from the fixed `sigma` and an effect. The separate `nonlinear_binary_weight(effect)` is an intentionally non-Born counterexample, not the selected `w(E)` (`B317:358-405`).

The frozen finding states the missing source directly:

> `"The numerical map w(E) requires an occurrence/Record/sampling/calibration bridge absent from this surface. Census counts, normalized counts, projector directions, and merge fractions do not select it."` (`F729:704-710`)

A lawful proposed receiver from occurrence/Record data would therefore need the following contract. This is a W6 design requirement, not a claim that it is landed:

```text
receiver(
  menu/program identity,
  ordered eligible effect identities E[0:N],
  typed Records R[0:M],
  exposure/sampling declaration,
  coarse-graining and same-effect identity metadata
) -> empirical comparators or calibrated w[0:N]
```

- **Shape:** for one exhaustive, mutually exclusive `N`-outcome menu, the raw numerical sufficient statistic is an `N`-vector of occurrence counts `n_i`, together with a trial/exposure total `M` and Record provenance/typing. If trials have unequal eligibility or exposure, per-effect exposure data are additionally required; a bare `N`-vector is then insufficient.
- **Units:** `n_i` and `M` are integer occurrences/trials; `f_i = n_i/M` is dimensionless. An exposure-corrected rate has inverse-exposure units until a declared calibration removes those units. Apparatus split/merge coefficients are already dimensionless but are not outcome data.
- **Normalization:** for a complete exclusive menu with common exposure, `n_i >= 0`, `sum_i n_i = M`, hence `f` lies in the simplex `Δ^(N-1)` and `sum_i f_i = 1`. Coarse-graining must add component counts, and repeated presentations of the same effect must meet an explicit cross-program identity/calibration rule. Those are precisely the missing occurrence, Record typing, sampling/exposure, and calibration layers listed at `F729:696-708`.
- **Firewall-preserving output:** the least committal receiver returns empirical `f_i` and residuals against a separately held `w(E_i)` comparator. It does **not** call those frequencies Born weights. A stronger calibration bridge may derive `w_i`, but only after the occurrence/Record and exposure domain is independently justified.

## 3. Born firewalls, verbatim

The governing declarations forbid the following semantic promotions:

> `"No census quantity is interpreted as an outcome weight, occurrence, Record, frequency, calibration, eligibility declaration, or selected Born law."` (`F729:4-8`)

> `"supplied apparatus direction derived from declared census projection"` / `"explicitly_not": "a derived menu selection"` (`F729:425-442`)

> `"supplied apparatus coefficients"` / `"explicitly_not": "Born weights w(E)"` (`F729:501-520`)

> `"The instrument remains a conditional quantum apparatus. Pointer labels are not occurrences or Records, and conditional Born weights are not frequencies."` (`B317:14-15`)

The landed note contract also requires the literal boundaries `"pointer labels are not records"`, `"dephasing is not occurrence"`, `"conditional born weights are not frequencies"`, `"actual member remains open"`, `"global additivity remains open"`, and `"calibration remains open"` (`B317:68-104`). The executable semantic firewall records `effect_functional_weight: "conditional hypothesis"` while `occurrence`, `actual_member`, `Record_formation`, `permanence_application`, and `frequency_calibration` are all `None` (`B317:844-862`).

The standing harness has an exact input schema containing only a probe id, `kind: "bloch_projector"`, and a three-scalar direction (`H728:4-10`), and declares:

> `"Frozen feeds are supplied apparatus data. This harness selects no Born law, weight map, probability content, occurrence, or Record."` (`H728:12-16`)

Its final firewall correspondingly freezes `selects_born_law`, `selects_probability_content`, and `selects_weight_map` all false (`H728:929-935`). The release gate adds: `"Do not claim G2, literal arbitrary-finite X1, a selected weight law"` and explicitly blocks the broad Born/Record no-go/minimum-content release (`R317:357-365`).

Consequently census data may never be relabeled as outcomes, Records, frequencies, calibration, eligibility, or `w(E)` merely because they have a count-like or normalized shape.

## 4. Landed occurrence/Record assets that are weight-shaped

What is actually derived is narrower than an occurrence law:

1. **Event-field counts and a unit direction.** Each of the two 2×2×2 legs has 24 event rows, 24 distinct identities, and five event-field one-counts, but the feed projects three combined counts into a positive L2-normalized Bloch direction (`F729:207-260,348-367,405-442`). The note prints `(certificate, actuality, law_domain) = (48,48,48)` and calls the normalized output a supplied apparatus direction (`N729:35-43`).
2. **Handoff multiplicities and simplex-shaped apparatus coefficients.** The four combined stage counts `(200,164,180,144)` are divided by `688`, producing a nonnegative sum-one tuple (`F729:473-540`; `N729:40-43`). This is weight-shaped but explicitly an apparatus coefficient tuple, not `w(E)`.
3. **Tick-identity multiplicities.** Across both legs the feed derives a `Counter` over `tick_identity`; there are 24 distinct identities and every identity has multiplicity two (`F729:566-635`). These are integer repetition multiplicities, not physical outcomes.
4. **An inherited object named `occurrence`.** `PhysicalFixture` has an `occurrence: dict`, obtained from `flagged_basis_and_encoding` and used to build exchange/frame representations (`B317:126-167,729-740`). The same executable nevertheless declares physical `occurrence: None` in its semantic firewall (`B317:844-862`). The field name therefore cannot be promoted into an actual-member occurrence source.

No authorized source derives an empirical outcome-frequency corpus, typed Records, exposure denominators, or a frequency-to-weight calibration. The release only names these as missing constructive directions: `occurrence-first numerical law` and `process-functional/global-history route` (`R317:25-35`), plus `actual member/Record law` and `certified repeated Record corpus` (`R317:323-331`).

**Track A scope dependency:** the task identifies an existing `record_outcome_orbit_occupancy` no-go. Its statement and scope are not in the five authorized files and were deliberately not read here. Track A must determine whether it forbids only the promotion of orbit occupancy to physical Record/weight, or a stronger receiver construction. Until that scope reading is supplied, orbit occupancy is not an available W6 source and the process/history route below remains gated.

## 5. Route candidates

| Route | Supplied → derived boundary | Counterfactual pass | Readiness |
|---|---|---|---|
| **A. Repeated-apparatus calibration bridge (top route)** | **Supplied:** unchanged derived-effect surface, menu/program identity, a lawful occurrence mechanism, typed Record corpus, sampling/exposure protocol, and calibration convention. **Derived:** `n_i`, `f_i`, then calibrated per-effect `w_i` if the calibration theorem warrants that identification. | Hold apparatus, effects, and menu fixed; replace the lawful Record corpus by one with different outcome ratios. The derived calibration output must change. Conversely, changing the hard-coded held `sigma` must not rewrite the empirical counts. Coarse-grained counts and weights must add. | **Needs mechanism.** It directly targets all four absent bridge elements at `F729:696-708`; none is landed. Scientifically strongest route. |
| **B. Occurrence-census comparator receiver** | **Supplied:** typed Records, exposure/eligibility domain, effect identities, and the separately held candidate `w(E)`. **Derived:** empirical simplex vector `f` and comparator residuals `f_i-w(E_i)`; **not** a selected weight law. | With `w(E)` and effects fixed, changing valid Record counts changes only the empirical comparator. Malformed typing, negative counts, inconsistent totals, or undeclared exposure must be rejected. | **Needs mechanism, but narrower than A.** The existing harness can inspire rejection/frozen-output infrastructure, but its present schema is direction-only and its firewall forbids weight synthesis (`H728:4-16,721-784`). |
| **C. Exact receiver-hole/no-go sharpening** | **Supplied:** an eligible exhaustive `N`-effect menu and the current twenty-port inventory. **Derived:** a proof that a raw receiver needs `N` count slots plus exposure/provenance, with `N-1` normalized numerical degrees after the sum rule; no weights are derived. | Construct two lawful hypothetical Record corpora with the same current apparatus direction and merge coefficients but different outcome count vectors. All current ports receive identical inputs, so any current-port-only claim must return the same answer; a Record-sensitive receiver must distinguish them. | **Buildable now as a bounded signature/dimension theorem.** Exact cross-program/global dimension still needs eligibility/effect-identity assumptions and cannot outrun the independent walls (`R317:158-172`). It sharpens W6 but does not close it. |
| **D. Record/process-functional or global-history receiver** | **Supplied:** a lawful actual-member/Record law or certified repeated Record corpus and a declared history functional. **Derived:** per-effect or history-conditioned comparator/weight values. | Hold local menu marginals fixed while changing lawful history/orbit organization. A genuinely history-sensitive output changes; a per-effect `w(E)` must not unless a declared history dependence is part of its domain. | **Likely blocked pending mechanism and Track A scope.** The release names the route and also keeps `W_occ`, `W_record`, and `W_global` as independent walls (`R317:25-35,158-172`). Do not use orbit occupancy until Track A resolves the named no-go's scope. |

Route A is the best W6-closing candidate because it makes weights derived from repeated, typed, exposed apparatus use while leaving the Cycle-317 effect surface unchanged. Route B is the safest infrastructure step because it can test Record-sensitive empirical comparators without claiming that frequency already is Born weight. Route C is immediately buildable and should specify exactly what A or B must add.

## 6. Stakes / minimal missing content

**W6 is missing one lawful occurrence → typed-Record → sampling/exposure → calibration map that is counterfactually sensitive to realized Records and yields, for every eligible effect menu, a normalized per-effect weight vector (or a comparator to it) without reinterpreting apparatus counts, pointer labels, dephasing, or unscoped orbit occupancy as outcomes.**

If routes A–D all fail for their stated reasons, that sentence—not another apparatus-direction feed, merge fraction, held `sigma`, or acceptance probe—is the minimal missing content.
