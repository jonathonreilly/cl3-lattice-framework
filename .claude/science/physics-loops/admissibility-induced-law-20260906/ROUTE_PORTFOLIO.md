# Route portfolio — admissibility-induced-law-20260906

## Prior-art sweep (workflow step 2), searched commit origin/main 341511a74e381be959777b1cb68ceb2dd217c890 (2026-09-06)

Commands run (worktree at the same tip):

```bash
git fetch origin main:refs/remotes/origin/main
git grep -n -iE "formation order|order of formation|sequential(ly)? form" origin/main -- 'docs/*.md'
git grep -n -iE "static law|Gibbs (measure|law|specification|potential)|Markov random field|Hammersley" origin/main -- 'docs/*.md'
git grep -n -iE "Brook|full conditional|local characteristic|compatib.*conditional|conditional.*compatib" origin/main -- 'docs/*.md'
git grep -n -iE "product over (the )?neighbo|neighbo.*product form" origin/main -- 'docs/*.md'
git grep -n -iE "normali[sz]er.*neighbo|neighbo.*normali[sz]er" origin/main -- 'docs/*.md'
git grep -n -iE "order[- ]independen|order[- ]dependen" origin/main -- 'docs/*.md'
git grep -l -iE "hammersley|markov random field|formation order|Brook" origin/main -- 'docs/audit/data/ledger/*.json' docs/audit/data/derivation_obligations.json
git ls-tree -r --name-only origin/main -- docs/ | grep -iE "FORMATION_(ORDER|LAW)|GIBBS|MARKOV|SEQUENTIAL|STATIC_LAW|NEIGHBOR_RULE|ADMISSIBILITY_RULE"
grep -rli -e "hammersley" -e "markov random field" docs archive .claude/science
```

Hits and classification (each read at its own text):

| Hit | Classification | What it establishes / why it is not this block |
|---|---|---|
| `docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md` (unaudited; candidate-retained-grade in its own status field) | MATCHING PRIOR ART for the static half, binary menu | Brook square-curl compatibility of strictly positive binary full conditionals, uniqueness by path integration, the cubic count-only classification to geometric odds and an Ising-type finite action. Its scope boundary excludes "stochastic update dynamics" and "Record formation". This block LINKS it as upstream, re-proves the static half for the six-state menu (general finite-menu Brook lemma + pair form on triangle-free graphs + positivity necessity), and adds the formation law, which that note does not define. |
| `docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md` | context-only | An append-only cellular relation witness (majority menu; one record per step; permanence) and a rule-space census; states that the rule supplies conditional odds for the forming record and not the formation site/rate. No static law, no formation law as a probability law, no comparison. |
| `docs/R_HALF_OPEN_BACKLOG_FORMATION_LAW_PROBE_BATCH_EXACT_SUPPORT_NOTE_2026-07-13.md` | context-only | Formation-weight probes across epochs (`w=1/3`, `w=1/2`); marginals differ between complete record environments. Different object (formation weights across epochs), no static-vs-formation theorem. |
| `docs/RECORD_MARKOV_GENERATOR_PREMISE_CLASSIFIER_2026-06-06.md`, `docs/RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md` | context-only | Continuous-time generator embeddability premises for two-state record dynamics. Not a nearest-neighbor rule's joint law. |
| `docs/ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md` (order-independent partial-map union) | context-only | Set-theoretic order independence of compatible partial-map unions; explicitly "not physical commutation of formation". |
| `docs/work_history/repo/review_feedback/LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md:505` | context-only | Counts transcripts if formation order is certified; no law. |
| `archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md` RESULT 136 (+ `opus_t210-213.py`), archived, never refereed, floating point | REFERENCE (archive tier, no authority) | The static reading of the rule as a full conditional; Hammersley–Clifford as a quoted step; the sum rule's compatibility failure in floats; the normalizer-constancy argument. This block re-proves the finite statements exactly, names the reading, and adds the formation law. |
| `archive/notes/docs/work_history/repo/review_feedback/EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md` | context-only (archived) | Law-type vs law-value taxonomy; no theorem on the two laws. |
| ledger shards / `derivation_obligations.json` | no hits for hammersley / markov random field / formation order / Brook | — |

Target state after the matched-hit review: **open**. The static half is a generalization of a landed binary theorem (cited as upstream); the formation law and its exact relation to the static law are not on `origin/main` or in the archive.

## Artifact routes for this block

| Route | Artifact type | Status |
|---|---|---|
| Exact finite theorems T1/T2 on declared windows and menu, native proofs, exact runner, one note | theorem note + runner certificate | active (block 01) |
| The five attempted coincidence routes as exact computations (family G) | runner certificate + N-gate section | active (block 01) |
| Infinite-volume (DLR) existence/uniqueness of the static specification | open; not this block | queued (OPPORTUNITY_QUEUE.md) |
| The Gaussian (gravity-lane) instance of the static/formation distinction on the lane's own fixture | open; not this block | queued |

## Block 02 prior-art sweep, searched commit origin/main 341511a74e (2026-09-06, after block 01)

```bash
git grep -l -iE "dobrushin" origin/main -- 'docs/*.md'                                  # 11 hits
git grep -l -iE "\bDLR\b|Dobrushin-Lanford-Ruelle" origin/main -- 'docs/*.md'          # 0
git grep -l -iE "transfer matrix.*strip|strip.*transfer matrix" origin/main -- 'docs/*.md'   # 0
git grep -l -iE "probabilistic cellular automat|PCA\b" origin/main -- 'docs/*.md'      # 0
git grep -l -iE "stationary (row|law|distribution).*(sweep|sequential)|sequential.*stationary" origin/main -- 'docs/*.md'   # 1
git grep -l -iE "uniqueness.*(Gibbs|infinite.volume)|infinite.volume.*unique" origin/main -- 'docs/*.md'   # 3
git grep -l -iE "specification.*(quasilocal|Feller|kernel)" origin/main -- 'docs/*.md' # 1
```

| Hit | Classification | Disposition |
|---|---|---|
| the six `WILSON_STAGGERED_*` notes of 2026-07-12 naming Dobrushin (e.g. `docs/WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md`) | context-only | Dobrushin-type contraction controls on the Wilson-staggered polymer/RG fibers — a different carrier, a different specification, no nearest-neighbor menu rule; relevant to block 03 (uniqueness) as prior use of the Dobrushin idea in-repo, not to block 02 |
| `docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md` | non-matching | the regex hit is incidental (seam packets); no sequential stationary row law |
| `docs/AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md`, `docs/GL_F_RECORD_VALUE_DICTIONARY_COMMUTING_LOCK_BOUNDED_THEOREM_NOTE_2026-09-01.md`, `docs/PRR_LOCAL_DERIVATION_FROM_JAYNES_MAX_ENTROPY_NARROW_THEOREM_NOTE_2026-05-22.md` | non-matching | KMS/Gibbs-state uniqueness in an operator-algebraic or max-entropy sense; not the menu rule's specification |
| `docs/work_history/repo/review_feedback/INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md` | context-only | a "specification" in the law-type sense of the 2026-07 tournament, not a DLR specification |

Target state after the matched-hit review: **open** — no note on `origin/main` states a DLR specification for the menu rule, an infinite-volume existence argument on the finite menu, a formation law on an infinite window, a row-sweep invariance theorem, or a transfer-matrix enclosure of a static strip statistic.

## Block 03 prior-art sweep, searched commit origin/main 341511a74e (2026-09-06, after block 02)

```bash
git grep -l -iE "dobrushin" origin/main -- 'docs/*.md'                                                     # 11
git grep -l -iE "uniqueness.*(Gibbs|specification|infinite.volume|static law)" origin/main -- 'docs/*.md'  # 2
git grep -l -iE "glauber|heat.bath dynamics|gibbs sampler" origin/main -- 'docs/*.md'                      # 0
git grep -l -iE "oscillation.*(lemma|bound)|interdependence" origin/main -- 'docs/*.md'                    # 7
git grep -l -iE "comparison theorem" origin/main -- 'docs/*.md'                                            # 3
git grep -l -iE "coupling.*(argument|proof|contraction)|path coupling|maximal coupling" origin/main -- 'docs/*.md'   # 26
git grep -l -iE "phase transition.*(menu|product rule)|(menu|product rule).*phase transition" origin/main -- 'docs/*.md'   # 0
```

| Hit | Classification | Disposition |
|---|---|---|
| `docs/WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md` (and five sibling `WILSON_STAGGERED_*` notes) | context-only; prior in-repo USE of the criterion | applies the one-site contraction criterion (`alpha < 1/2` on a constrained polymer fiber) on the Wilson-staggered carrier and quotes the theorem as authority ("Condition (0.4) now gives Dobrushin uniqueness and boundary comparison"); it does not re-prove it and it is not about the menu rule; cited once in the note's Prior art |
| `docs/AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md`, `docs/GL_F_RECORD_VALUE_DICTIONARY_COMMUTING_LOCK_BOUNDED_THEOREM_NOTE_2026-09-01.md` | non-matching | KMS/operator-algebraic uniqueness; a record-value dictionary lock; neither concerns the menu rule's specification |
| the `oscillation`/`interdependence` hits (`PMNS_*`, `SIGMA_MNU_*`, `SM_GSTAR_*`) | non-matching | neutrino/thermal contexts; the word coincidence only |
| the `comparison theorem` hits (`BEYOND_LATTICE_QCD_NOTE.md`, `QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`, `SYMMETRY_HEAD_TO_HEAD_NOTE.md`) | non-matching | QCD comparison tables, not the Gibbs-measure comparison theorem |
| the 26 `coupling` hits (e.g. `BBS_RG_BANACH_CONTRACTION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md`, `FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md`) | non-matching | "coupling" as a physical coupling constant or RG contraction; no coupling of Markov chains for a menu rule |

Target state after the matched-hit review: **open** — no note on `origin/main` computes the one-site interdependence coefficient of the menu rule, states its uniqueness region, or re-proves the criterion.
