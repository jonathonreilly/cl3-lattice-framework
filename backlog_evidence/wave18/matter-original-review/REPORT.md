# Original #7888/#7890 independent source review

FINAL VERDICT: CHANGES REQUESTED — nine P2 findings and two P3 precision corrections. The selected finite source is tractable and useful; the blockers are concrete proof, interpretation, scope and cache-binding defects. No reserved scientific dependency was needed, no source was corrected by this reviewer, and no formal audit grade was applied.

## Frozen unit and preservation

| PR | Frozen/live head | Actual authored base | Original scope |
|---|---|---|---|
|7888|c959360c78da807c17f2a1bd0d1887d20a432841|36fe57a7a784df31bc2178c4b94dfc7caaa5d094|329-line note,637-line runner,61-line cache|
|7890|f2e000568813e4b23b84246e6eeb81793d09676f|36fe57a7a784df31bc2178c4b94dfc7caaa5d094|329-line note,746-line runner,62-line cache|

Review main:4369a77fc1dcd37fbc1fe2102afba21b9e4bd406. Isolated worktree:/Users/jonreilly/Projects/Physics-worktrees/review-backlog-matter-7888-7890-20260908. The exact six-path overlay tree is72c7d519e7e9f8c34074f73f4c4a29a9022eb81a; exact-original-overlay.patch SHA2568daae5ab0abf641096695b283b900e7ee6ddbbac659f0413761c6f6e6d1cbdc6. No deletions or nominal/inherited authored omissions exist: each original has exactly these three additions against its verified base, all absent from main. FULL_PATH_DISPOSITIONS maps30,003 path rows, preserving all28,711 current-main paths exactly and excluding1,286 raw inherited branch-only paths. The original branches and exact original-source copies preserve all six bodies; both live heads were checked at preparation and freeze. The inherited raw trees are not accepted or imported. Both original heads are direct children of36fe57a7. The current-main merge-base query exits1 in the visible shallow graph; no missing ancestry is treated as an empty delta. Authored scope uses the actual immediate parent, and main preservation uses direct complete mode/blob comparisons.

The complete six bodies and both full PR bodies were read. Runtime source is standalone stdlib/NumPy, plus SymPy in7888; no imported repository science helper, dynamic code loader, file input or child scientific executable exists. Current memo and the quoted kinetic/corner clauses were checked and hash-bound; the kinetic gate's unneeded full parent proof is not enrolled. Contextual7844/7874/7879/7834 campaigns, physical role/Record/formation claims and reserved6379/6858/6859 remain unaccepted. The notes may retain their own explicit conditional finite objects without importing a tower. All source/claim/premise/read dispositions are in their separate machine-readable maps.

## Actual execution and adversarial evidence

Both originals ran exactly once through current runner_cache.execute_runner with actual pre/post execution identity and an additional whole selected/quoted-context identity guard. Real cache and live-log destinations were external; original canonical caches were untouched. BLAS/OMP threads were1, each declared/effective cap120seconds, outer watchdog135seconds and process-tree RSS cap6GiB. No timeout, kill, source movement or scientific failure occurred.

| Original | Actual result | Runner elapsed | Maximum process-tree RSS | External actual cache SHA256 |
|---|---|---|---|---|
|7888|18 PASS,0 FAIL;exit0|4.411s|1,647,280,128bytes|5189364939ca1b8610f1b85ca79f5739127aacdfd4065b4558db2d0151d9a887|
|7890|28 PASS,0 FAIL;exit0|2.061s|1,125,531,648bytes|f2b05405ed78c9d756a7fd40864dc0da99c6376ba200e19ff4b248f759b88059|

All stdout/stderr, full live output, environment, command, result, elapsed/resource and cache guard receipts are in original-execution/. The returned PASS counts describe the actual original predicates, not acceptance of all prose. The full new cache bodies were read against their source. Neither original writes independent data files; its raw numeric tables/shells/spectra/fits are preserved in stdout and original source. No parent simulator or second whole baseline ran.

INDEPENDENT_CONTROLS records49 bounded controls, including an independent finite adjacency/SVD construction, the actual Pauli and two-state commutator witnesses, exact positive-m concavity-inference counterexample, flavor degeneracies, explicit Slater/Born joint law and a correlated alternative, actual E2 predicate weakness, and real semantic-source changes. Three full mutated source files are retained; independent local identities reject their altered KS sign, Bloch sine sign and mass coefficient. These are explicitly focused source controls, not claimed full mutant-campaign runs. The small original F1 block was also run independently: its antiperiodic off-axis corruption passes, demonstrating incomplete coverage. SCOPE_CONTROLS adds four source-bound constructions/scaling statements, including uniform half-filled periodic zero-mode extension and actual edge-Z readout noncommutation.

Both actual note-derived graph and packet APIs return the correct primary, no helpers, recognized bounded_theorem type and no current science citation edges. Actual forensic source checks return no source-shape issue. This does not cure missing inputs: six actual own-note/memo/gate drifts leave the corresponding genuine cache fresh and cache-first --check-only exit0. Both actual runner-source drifts correctly produce sha_mismatch and exit1. These failures are preserved; no cache was fabricated or restamped.

## Actionable findings

### F1 [P2] Hermitian hop is not an eigenoperator of the mass commutator

`docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:128`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:134`; `scripts/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.py:349`.

For m=1 the actual A4 predicate passes, but [Hm,T]-2T and [Hm,T]+2T are both nonzero. [Hm,T]=m(eps_j-eps_i)T Bj rotates the Hermitian hop. The stated inference from TBi=-TBj does not make Bj scalar. A nonzero Hermitian T cannot be an eigenoperator of commutation with Hermitian H at a nonzero real eigenvalue. The never-zero assertion also requires m != 0.

Correction: Preserve the exact commutator; state the eigenoperator property for T(I+b Bj)/2, or ad(Hm)^2 T=4m²T. Test that property and distinguish the Hermitian hop. Correct T1/frontmatter/executable block/A4 caption and preserve m=0.

### F2 [P2] Spectrum proof uses the wrong fixed-mass intertwiner

`docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:160`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:167`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:254`.

Eps H(m) Eps=-H(-m), not -H(m). The independent m=.7 control gives residual1.4 for the claimed fixed-mass chiral symmetry. Squaring alone gives absolute eigenvalues, not equal sign multiplicities on arbitrary bipartite graphs. On the declared even tori the useful sign-paired spectrum is correct by balanced bipartite block SVD.

Correction: Give the short balanced-bipartite SVD proof on the actual domain. State gap2|m| (or explicitly m>=0), distinguish a grid containing the node from a finite torus with positive massless gap, and preserve all original spectra/tests. Do not extend half-positive multiplicity to an unbalanced open graph.

### F3 [P2] Finite two-sector comparisons and fourth moments do not prove every-mass minimization

`docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:222`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:225`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:231`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:257`; `scripts/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.py:26`.

The runner compares the uniform KS and plain sectors only: masses{0,.5,1,2,4} on4³/6³ with eight twists each; six masses on a200³ quadrature. It neither enumerates all allowed flux assignments nor proves ordering for all m or a thermodynamic error bound. The proposed general concavity inference is false. At m=1/4, X_A={0,2} with weights1/2 has mean1 and second moment2; X_B={1/2,5} with weights8/9,1/9 has mean1 and second moment3. Nevertheless E sqrt(X_A+m²)=(1+sqrt33)/8 <11/12=E sqrt(X_B+m²), reversing the asserted sea-energy ordering. This refutes the inference, not the actual KS/plain ordering.

Correction: Retain every finite value, twist minimization, moment42/90 and sampled quadrature result. Label the compared two sectors and finite masses explicitly everywhere including G3/header/summary/PR scope. Remove the universal/global conclusion and variance proof; keep -3/m³ as numerical comparison unless a separate bounded Taylor derivation is supplied. No new all-sector campaign is necessary.

### F4 [P2] A one-body projector and diagonal Pauli parity do not derive the joint Record law

`docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:233`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:243`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:131`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:218`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:252`; `scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py:605`.

The actual E2 expression is max(-P²)<=0 and passes on a nonprojector. It checks an algebraic determinant inequality, not a joint Record law or full negative association of arbitrary increasing disjoint events. A Slater state plus joint occupation measurement and Born rule gives the useful distinct-site covariance -|P_uv|². The diagonal duplicate u=v needs n_v²=n_v, not the two-distinct-index determinant. Hence a kernel amplitude r^-3 corresponds to occupation covariance r^-6; exp(-r/xi) corresponds to covariance lengthxi/2. In the actual Pauli source a single edge Z can anticommute with a face stabilizer although the full six-edge parity commutes. An individually readable permanent edge-record instrument is not obtained merely by saying diagonal/readable.

Correction: Keep projector identities and the declared Pauli observable, and explicitly condition probabilistic statements on a supplied Slater/Born occupation readout (or keep purely algebraic kernel statements). Limit E2 to distinct-site pairwise covariance unless an independent full negative-association theorem is actually supplied. Add a small actual joint-law control and preserve correlated same-marginal alternative. Distinguish kernel and connected occupation correlation decay. State the coarse role/encoding/readout/formation bridge is supplied or unproved; do not derive it from the current axioms or import a parent tower.

### F5 [P2] Mass-sign relabeling is not indistinguishability at a fixed labeled readout

`docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:240`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:245`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:259`.

The correct theorem itself gives <n_v>(-m)=1-<n_v>(m). On the actual4³ antiperiodic matrix at m=.7 the fixed-site means differ by more than.25 while spectra agree. The sign can be conventional only when the sublattice naming and observable/state identification are transformed consistently. Equal spectra alone do not erase the fixed-label observable difference.

Correction: Retain the particle-hole/conjugation identity and supplied sign. Qualify convention as an equivalence under explicit relabeling/readout transformation, and retain fixed-label distinguishability as a control. Remove unconditional nothing measurable and only magnitude is content.

### F6 [P2] Four tastes and kinetic taste splitting contradict the actual flavor census

`docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:187`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:255`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:162`.

The paired census is8=2spin×2chirality×2flavor, so each positive/negative band is fourfold from spin×flavor, not four physical tastes. The matrix W_a fails to commute with a chosen flavor generator, but H(q)^2=E(q)^2 I leaves the bands exactly fourfold even with those artifacts. Noncommutation/mixing is not an energy taste splitting.

Correction: Use two Dirac flavors/tastes consistently; distinguish spin and chirality from flavor. Retain chirality-odd flavor-singlet mass and O(p²) flavor mixing, and remove unsupported kinetic spectral splitting. Preserve the concrete degeneracy and Clifford controls.

### F7 [P2] Kernel theorem scope exceeds the sampled kernel checks and omits contact exceptions

`docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:210`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:211`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:301`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:208`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:211`; `scripts/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.py:626`; `scripts/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.py:634`.

The zero-odd-component rule has the explicit contact P_vv=1/2 exception. The288³ Fourier values and stride shells test finite samples, not an infinite-distance lattice limit or the identity of a historical0.21 result. The massive branch point gives a useful analytic comparison, but192²×2048 periodic quadrature and chosen fits do not prove every-m exponential asymptotics, exact lack of image effects or finite-range disappearance. F1 checks128 selected entries of one periodic source column and only7 antiperiodic axis magnitudes, not every projector entry. A real off-axis antiperiodic kernel output corruption survives the exact F1 predicate.

Correction: Preserve grids/windows/fit values/analytic branch point and the positive finite comparisons. Clearly distinguish conjectured/derived continuum comparison from checked finite lattice data and avoid a new asymptotic proof unless actually supplied. Correct contact scope, finite versus asymptotic/zero wording, image qualification, and F1 coverage label or add a bounded complete declared-column control. Do not claim full matrix validation or treat the historic0.21 as proven identical without its actual source.

### F8 [P3] Quartic uniqueness and velocity wording need their coordinate qualifications

`docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:186`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:187`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:199`; `scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py:416`.

Cubic quartic invariants span sum p_a^4 and |p|^4, two independent functions. Only the anisotropic class modulo the isotropic quartic is one-dimensional. E/|p| is explicitly phase velocity; its correction -p²/24 differs from group velocity -p²/8 along an axis. p is the2³ cell phase, so k=p/2 is coarse-site momentum, with limiting speed2 in supplied unit hopping/time. The gate antihermitian D has coefficient1/2; a site phase gives G(-iD)G†=M/2, not an absolute physical speed.

Correction: Qualify unique anisotropic quartic modulo isotropic quartic; retain -1/12 for this hop. State phase/group and cell/coarse momentum conventions, unit hopping and absence of a physical clock/boost-covariant dynamics. Existing explicit no-boost theorem boundary should remain.

### F9 [P3] Periodic zero modes prevent a unique filling, not a half-filled projector

`docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:314`.

The rank252 strict-negative projector is correctly reported. But zero modes do not prevent an exactly half-filled projector: on4³ periodic, four Walsh combinations of the eight explicit q=pi zero modes give rank32, P²=P and every diagonal1/2. The identical cell construction extends to8³. The issue is a supplied occupation choice, not impossibility.

Correction: Replace prevent that by do not uniquely select it, retain the strict-negative original result and unchosen filling boundary. A small explicit zero-mode filling control suffices; do not change the original selected strict-negative convention silently.

### F10 [P2] Successful caches omit all note and quoted-source input identity

`scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py:57`; `scripts/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.py:46`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:2`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:2`.

Neither runner declares AUDIT_INPUT_PATHS. The actual successful caches remain fresh and cached_runner_output --check-only exits0 after an own-note, current memo or quoted kinetic-gate byte drift; runner-source drift properly gives sha_mismatch/exit1. Both actual consumers resolve the filename-derived primary and zero helpers, but the two frontmatter claim_id aliases differ from the canonical actual IDs. Current type hints are correctly recognized.

Correction: Before one final run per changed runner, freeze/pin its own final note and exact actually retained quoted premise/context surfaces; guard quotation identity where promised. Align current IDs with real filename-derived IDs, preserving old aliases explicitly as provenance. Keep zero helper registries unless a real helper is introduced. Test both actual note-derived APIs, source guards, and actual cache-first drift rejection. Use real final caches and preserve the original receipts, including these baseline receipts.

### F11 [P2] Historical parent readings are endorsed despite declared non-load-bearing status

`docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:162`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:215`; `docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:311`; `docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md:63`.

The note labels parent7844 non-load-bearing yet says every multiplicity/spectrum/representation stands, and treats its historical0.21 as established finite-distance content. This unit rederives the Clifford/census objects but does not reprove the parent full2A1+2T1/campaign/physical encoding claims. Standard methodology naming likewise does not establish a physical Record/BKS equivalence or the parent role-pattern law. These need not become source premises to preserve the current finite work.

Correction: Keep exact attributed historical quotes and local redeclared results; qualify all other parent claims/results as historical, unverified/unaccepted by this unit. Make no full parent acceptance and add no arbitrary graph enrollment. If any specific parent theorem is retained as load-bearing, explicitly scope/read/bind it before acceptance; otherwise retain the standalone conditional construction.

## Review lenses and repair boundary

Proof and independent mathematics: PROOF_REVIEW.md derives the useful finite cell/census/dispersion, balanced spectrum, commutator alternatives, projector identities and conditional readout boundary. Every original T1–T5 and T1–T8 has a specific CLAIM_DISPOSITIONS row; none is silently dropped. The input/import lens found no required reserved or obsolete-premise supplier. Current four axioms are quoted context, not a license for global formation, a physical clock, a Slater/Born joint law, or a full parent campaign. No observation or numerical target was imported into the runner from an external data file.

The scope/no-go lens is applicable to the stated finite absence of chirality/splitting and explanatory exclusions, not to a new global no-go result. Finite vector-like census is supported; chiral projections, interactions, other mass terms, nonuniform flux sectors, zero-mode fillings, different instruments and physical role/time completions remain alternatives. No independent-wall count or blanket impossibility result is warranted. The label lens finds broad every-mass/limit/negative-association/readable claims exceeding actual checks. The governance lens requires actual final source/input identity and complete filename-derived consumer binding, not a formal audit or a fabricated historical receipt.

Preserve all six originals and their genuine historical and present baseline results. A separate author should narrowly correct the two notes, corresponding source predicates/labels and final input declarations/caches, adding explicit historical provenance outside active science discovery if needed. Freeze all final prose/inputs before one genuine final run per affected runner. No broad parent campaign or large rerun is required for the repairs specified here. Root owns any final integration, graph, gates or PR actions; this original reviewer remains available for one combined affected-source/input/manifest confirmation.

Three review-harness failures are retained: initial two-state residual expected2 instead of4, a relative-path dependency API call, and a wrong forensic-tool directory during receipt preparation. They caused no original baseline repetition or scientific-source change. No failed original scientific run was suppressed. No formal audit, retained-grade application, main change or GitHub mutation occurred.
