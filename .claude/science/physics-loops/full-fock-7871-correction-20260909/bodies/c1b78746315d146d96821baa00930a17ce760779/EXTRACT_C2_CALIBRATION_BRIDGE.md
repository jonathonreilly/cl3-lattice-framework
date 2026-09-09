# Track C cycle-2 extraction — repeated-apparatus calibration bridge

Date: 2026-07-29

Status: bounded extraction from `EXTRACT_W6_GROUNDING.md`, the frozen Cycle-744 interface/port, and the landed Cycle-317 surface only. This document specifies a comparison cycle; it does not derive occurrence, calibrate a weight, or select a Born law.

Source keys: `W6` = `EXTRACT_W6_GROUNDING.md`; `C744` = `scripts/frontier_cycle744_weight_receiver_sharpening_2026_07_28.py`; `B317` = `scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py`.

## 1. Operational meaning of “repeated apparatus”

### What Cycle 317 actually supplies

A complete execution of `B317.main()` is **not one apparatus trial**. It is a closed, argument-free verification run which constructs fixtures, derives several effect menus, and checks them. It has no supplied per-trial feed, no sampling call, and no callable that returns a realized outcome. Its own boundary is explicit: pointer labels are not occurrences or Records, conditional Born weights are not frequencies, and its semantic result has `occurrence = None` and `frequency_calibration = None` (`B317:14-15, 844-862`).

The landed call chain that produces **outcome effects/slots**, rather than outcome occurrences, is:

1. `physical_subcode_controls()` calls `physical_fixture(length)` for `length in (3, 6)` and returns the fixture map (`B317:141-247`).
2. `contact_trine_controls(fixtures[3])` constructs three projectors with `projector_bloch`, constructs Kraus blocks, calls `stack_isometry`, calls `derived_effects`, and returns `(kraus, effects)` for a three-effect menu (`B317:248-357`). `physical_isometry` and `menu_metrics` certify the apparatus and menu; neither selects an outcome.
3. `binary_and_ternary_threshold_controls(trine_effects)` uses `derived_effects` on a further fixed ternary menu and evaluates `nonlinear_binary_weight` as a counterfunctional. It returns no outcome (`B317:358-408`).
4. `mixed_projective_forcing_basis_controls(fixtures[3])` uses `projector_bloch`, `split_projector_isometry`, `merge_isometry`, `stack_isometry`, and `derived_effects` to construct the landed ray-split, axis-merge, and representation menus (`B317:409-650`). Its local `born_weight(effect) = Tr(sigma effect)` evaluates a **held candidate** on already constructed effects; it is explicitly “candidate consistency only” (`B317:599-634`).
5. `physical_locality_and_covariance_controls` and `deletion_domain_and_semantic_controls` test the constructed apparatus. They produce no per-trial outcome (`B317:651-865`).

Thus `derived_effects(isometry, groups)` is the exact landed producer of menu effects, while `contact_trine_controls` and `mixed_projective_forcing_basis_controls` are the landed menu-producing wrappers. There is **no landed per-run outcome producer**.

### The only honest build-now run convention

For a comparison-only cycle, define one “run” as one supplied Cycle-744 `RecordRow` of kind `declared_apparatus_test_row`, under one fixed `MenuProgramIdentity`, one fixed ordered effect list, and one `complete-exclusive-common-exposure` declaration. The row asserts exactly one `outcome_index/effect_id` for one declared complete-exclusive presentation. This is a **test-data convention**, not a derivation that the row is a physical occurrence or Record.

Do not define a run as “one evaluation of the Cycle-317 script on one feed”: Cycle 317 has no such feed port and returns no selected outcome. The apparatus/menu may be anchored to a Cycle-317-derived menu, but the row-to-apparatus link remains supplied.

The currently frozen Cycle-744 family has two corpus/profile members,

```text
landed-profile       counts = (1, 2, 3, 4), M = 10
counterfactual-shift counts = (2, 2, 3, 3), M = 10
```

not ten calls to a Cycle-317 outcome routine (`C744:212-217, 768-811`). Across those profiles, the declared profile/exposure identifiers, row identifiers and provenance, and outcome multiplicities vary. The menu id, program id, ordered effect ids, common-exposure protocol, per-effect eligibility, coarse-graining metadata, and singleton same-effect classes remain fixed.

`_declared_rows(profile, counts)` manufactures one row per declared multiplicity. `receive_occurrence_records(...)` then validates those supplied rows and increments `counts[row.outcome_index]` once per row. Its census counts declared rows assigned to each ordered effect slot; it checks `sum(counts) = M` and derives the exact `Fraction` simplex `f_i = n_i/M` (`C744:293-429, 768-934`). It does not observe Cycle 317 and it does not generate occurrences.

## 2. Calibration-map candidate and the honest line

The landed flow is:

```text
declared profile/counts
  -> _declared_rows
  -> supplied typed test rows + supplied exposure/provenance
  -> receive_occurrence_records
  -> derived count vector n, exact simplex f, coarse counts
                                                [DATA]

supplied effects + frozen held sigma
  -> _held_landed_candidate_values
  -> held candidate w_hold(E) = Tr(sigma E)      [HELD WEIGHT CANDIDATE]

(f, w_hold, declared tolerance T)
  -> compare_empirical_to_landed
  -> residuals and agreement/disagreement         [COMPARISON]
```

For the existing port, `compare_empirical_to_landed` defaults to `T = 1.0e-12` and returns a `ComparatorRow` per effect; it never writes a weight (`C744:431-463`). The frozen example compares the exact simplexes `(1/10,2/10,3/10,4/10)` and `(2/10,2/10,3/10,3/10)` with separately held values `(0.1,0.2,0.3,0.4)`. It obtains four agreements in the first profile and two agreements/two disagreements in the second (`C744:936-1011`).

One additional boundary matters: the Cycle-744 example directly supplies the scalar effects `(0.1 I, 0.2 I, 0.3 I, 0.4 I)`. It does not obtain those four effects by calling a Cycle-317 menu constructor (`C744:949-965`). Therefore the frozen example is a port test against legal qubit effects, not yet a repeated use of a Cycle-317 physical apparatus. A first comparison cycle must freeze an effect tuple returned by the landed Cycle-317 call chain if it wants the narrower “Cycle-317 apparatus” label.

The flow stops being data and becomes a **weight claim** at the first semantic promotion that:

- identifies `f_i` with `w(E_i)`, returns it through a calibration/weight field, or uses it downstream as the effect functional;
- selects the fixed `sigma`, the trace form, or the Born law because declared profiles agree with it;
- calls `_declared_rows` output a derived physical occurrence/Record corpus; or
- turns finite agreement, even exact agreement, into a derivation of a limit law.

A bounded cycle may derive and certify only:

- the count vector and exact simplex of the **declared** run family;
- exposure, provenance, slot, coarse-graining, and same-effect schema consistency;
- residuals and “agreement/disagreement to declared tolerance `T`” against the separately held `w_hold(E)`; and
- counterfactual sensitivity: changing valid declared rows changes `n` and `f`, while the held candidate is unchanged.

It may not call that simplex calibrated weights. Calibration and occurrence remain absent in `honest_boundary()` (`calibration_map = False`, `selected_occurrence_law = False`, `port_is_comparator_only = True`, `w6_closed = False`; `C744:1114-1132`).

The occurrence-derivation dependency is **Track A’s scope resolution of the named `record_outcome_orbit_occupancy` no-go, followed by a lawful actual-member/occurrence → typed-Record formation source**. The run family must come from that derived occurrence/Record mechanism, with exposure/sampling provenance, rather than from `DECLARED_APPARATUS_DATA_FAMILY` or `_declared_rows`. Until then, the bridge is a declared-data comparator.

## 3. Convergence: testable comparison, not derived law

The landed numerical interfaces are sufficient to test a finite, declared convergence-like comparison:

```text
for declared corpus k with M_k rows:
    f^(k) = receive_occurrence_records(...).simplex
    r^(k) = f^(k) - w_hold
    report ||r^(k)|| and whether it meets predeclared T_k
```

They are not sufficient to derive or certify the law-like statement
`f_i -> Tr(sigma E_i)` as `M -> infinity`. There is no landed occurrence generator, no derived run-family measure, and no theorem connecting repeated physical trials to the declared rows. A finite bounded cycle can report that residuals for a declared sequence decrease, fail to decrease, or meet a finite tail criterion. It must label that result “finite declared-family comparison,” not “convergence proved,” “Born law selected,” or “frequency calibration.”

Honest certificate keys would be:

```yaml
comparison_kind: finite_declared_census_vs_held_trace_candidate
apparatus_surface: cycle317
apparatus_call_chain: [...]
apparatus_execution_is_one_trial: false
menu_id: ...
program_id: ...
ordered_effect_ids: [...]
effect_origin: landed_cycle317_derived_effects
run_row_kind: declared_apparatus_test_row
run_family_origin: declared_not_occurrence_derived
sampling_protocol: complete-exclusive-common-exposure
record_provenance: [...]
exposure_provenance: ...
M_sequence: [...]
counts_by_M: [...]
simplex_by_M_exact: [...]
held_candidate_origin: fixed_sigma_trace_candidate
held_candidate_values: [...]
tolerance_by_M: [...]
residuals_by_M: [...]
residual_norm_by_M: [...]
finite_tail_comparison_verdict: agreement_or_disagreement
coarse_graining_additivity: pass_or_fail
counterfactual_record_sensitivity: pass_or_fail
malformed_intakes_refused: [...]
selected_occurrence_law: false
calibration_map_supplied: false
simplex_promoted_to_weight: false
born_law_selected: false
asymptotic_convergence_claimed: false
w6_closed: false
track_a_dependency: record_outcome_orbit_occupancy_scope_and_occurrence_record_formation
```

The comparison tolerance must be declared as comparison metadata. `1.0e-12` is the present Cycle-744 comparator default; Cycle 317’s separate apparatus-control tolerance is `5.0e-11` and must not silently substitute for it (`C744:431-439`; `B317:39`).

## 4. First-cycle scope, certificates, and verdict

### Buildable first comparison cycle

Keep the cycle narrow:

1. Freeze exactly one existing Cycle-317 effect menu and its call chain, preferably the already returned contact-trine tuple from `physical_subcode_controls()` → `contact_trine_controls(fixtures[3])` → `derived_effects`.
2. Assign ordered effect ids without claiming that the labels occur.
3. Supply two or more typed declared corpora at declared totals `M_k`, under one fixed menu/program and common-exposure schema.
4. Pass each corpus through `receive_occurrence_records`.
5. compute the separately held fixed-`sigma` trace candidate on the frozen effects;
6. call `compare_empirical_to_landed` with an explicit tolerance schedule; and
7. report only finite residual/comparison results and the open Track A dependency.

No new sampler, state law, stochastic dynamics, actual-member rule, Record formation, or calibration theorem belongs in this comparison cycle.

### Required certificates

- **C1 — landed apparatus/menu origin:** exact Cycle-317 callable chain, ordered effect count, normalization/positivity diagnostics, and explicit `per_run_outcome_callable: None`.
- **C2 — declared-run schema:** unique typed rows, matching menu/program/effect slot/exposure, common exposure, nonempty provenance, and `run_family_origin: declared`.
- **C3 — exact census/simplex:** integer `n_i >= 0`, `sum n_i = M`, exact `Fraction` values, and simplex sum exactly one.
- **C4 — coarse/same-effect bookkeeping:** coarse counts add component counts and declared same-effect classes partition the effect ids.
- **C5 — held-candidate separation:** fixed `sigma`, per-effect `Tr(sigma E)`, candidate values stored separately from empirical values, and no candidate selection from the census.
- **C6 — finite comparison/convergence dashboard:** `M_k`, counts, exact simplexes, residual vectors/norms, declared `T_k`, and finite-tail agreement/disagreement only.
- **C7 — counterfactual sensitivity:** changing a valid declared corpus changes the empirical output; holding the effects and `sigma` fixed leaves the candidate unchanged.
- **C8 — lawful-domain refusals:** duplicate ids, untyped rows, slot/effect mismatch, inconsistent exposure, and missing provenance are rejected.
- **C9 — semantic/write firewall:** no empirical-to-weight assignment, no Cycle-317 module write, no calibration output, no selected occurrence law, no asymptotic claim, and `w6_closed = false`.
- **C10 — Track A gate:** name `record_outcome_orbit_occupancy` scope resolution and derived actual-member/occurrence → typed-Record formation as unmet.

### Feasibility verdict

**Buildable now:** a bounded, comparison-only cycle using a genuinely Cycle-317-derived effect menu, declared typed run corpora, the Cycle-744 exact simplex port, and residuals against the separately held trace candidate.

**Not buildable from the landed surfaces:** a repeated-apparatus occurrence law, a physical Record corpus, a calibration map from frequencies to `w(E)`, selection of `Tr(sigma E)`, or a derived asymptotic convergence law. Those require the Track A occurrence/Record dependency. The comparison cycle is useful infrastructure but does not close W6.
