# Independent blind science review — PRs #7908 and #7914

Reviewer arm: `sol-xhigh`  
UTC start: `2026-09-08T14:37:19Z`  
UTC end: `2026-09-08T15:03:29Z`  
Frozen original six-source tree: `311884f5b5516ba1dac437e7b75db2533a41c71e`  
Pinned repository context: `8257bddfc97ab763d208b43e9bdc8677fe89b1e8`

## Disposition

Neither packet is ready to land in its present form.

- **PR #7908:** preserve the declared finite-plaquette algebra, the exact computational-record-basis census `0/65536`, the exact character count `dim H_G = 82`, and the bounded numerical spectra. The claimed consequence for the framework's Record/Admissibility mechanism is not established and conflicts with the pinned abelian companion's corrected boundary. Disposition: **support-only demotion plus narrow source correction**.
- **PR #7914:** preserve the exact finite-algebra result for the declared pair `R` (record-basis diagonal operators) and `I` (the gauge commutant): `dim(R ∩ I)=1296`, its component description, its abelian generators, and its rank-one restrictions to the singlet sector. The identifications with all physically available readouts, full state resolution, non-existence of a canonical projection, generic abelian/non-abelian behavior, and “confinement at the level of registration” outrun the proof. Disposition: **support-only demotion; some claims need new science or explicit additional premises**.

Both original runners completed successfully and reproduced their caches (`PASS=25 FAIL=0` and `PASS=27 FAIL=0`). Passing runners do not cure the semantic and proof defects below.

## Findings

### F1 — Major — The Record axiom does not make every diagonal operator an available readout

**Locations:** `THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:65-71, 87-94, 102, 136-146, 152-154, 198-204`.

The note defines `R` as the full diagonal algebra and immediately identifies it with “THE RECORD-READABLE ALGEBRA,” then treats `R ∩ I` as everything records can register under the Record axiom. The pinned axiom says only that a readout value is determined by record content and that unrecorded sites are unreadable (`MINIMAL_AXIOMS_2026-06-29.md:75-90`). This is a necessary condition on an actual readout. It does not assert the converse that every function of the complete record pattern is an available physical readout. The same axiom memo keeps readout-context selection and physical-observable identification outside the axioms (`:132-151, 173-190`).

The cited record-map proposal cannot silently fill the gap: it is explicitly an unaudited proposal based on the superseded 2026-06-05 Record wording and requires a supplied central-sector decomposition and named partition predicate (`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md:3-9, 22-45, 60-113`). The reviewed note calls that pointer non-load-bearing and supplies neither an adopted sufficiency principle nor a physical readout context for the singleton record basis.

The exact algebraic calculation remains valid if `R` is called the **declared record-diagonal candidate algebra**. Claims about all registrable content and kinematic confinement require an explicit additional premise and a justified readout context; otherwise demote those interpretations to open/conditional language.

### F2 — Major — PR #7908 relies on a formation-law reading that its pinned abelian comparator expressly disclaims

**Locations:** `A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md:20-28, 92-96, 182-197, 231-250, 327-329`.

The note says the abelian companion established site-level forcing “in any formation order” and uses `0` raw Gauss-invariant patterns to conclude that the non-abelian sector is unreachable through the Record axiom's readable content. At the pinned base, the companion instead defines its one-corner calculation as a set-theoretic projection and says it does **not** supply probabilities, global compatibility, the fixed fine-site nearest-neighbor rule, covariance, or a physical Record formation process (`THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md:94, 163-169`). Its claim scope and status are explicitly conditional-support.

Therefore `0` versus `1312` establishes a sharp finite comparison between two declared diagonal/kernel conditions; it does not establish a difference between physically implemented support mechanisms. The corollary that the “strong sector is not reachable” from Record is unsupported. Retain “no computational record-basis vector lies in the declared joint Gauss kernel,” remove the formation/reachability conclusion, and list the physical local-law/readout bridge as open. The note is also not self-contained in the sense claimed at lines 327-329 once this interpretive comparator is used load-bearingly.

### F3 — Major — A complete rank-one commuting measurement does not resolve every physical state

**Locations:** `THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:22, 104-110, 136-146, 154, 202-204`; `record_readable_gauge_invariant_algebra_colour_blind_check_2026_09_03.py:484-498`.

The runner supports a maximal abelian algebra on the 82-dimensional singlet sector: 82 mutually orthogonal rank-one projectors. The note then says these projectors “separate every physical state from every other, losing nothing.” This is false for arbitrary rays or density matrices. An orthonormal-basis measurement fixes 82 diagonal probabilities but discards off-diagonal coherence.

A two-dimensional counterexample is decisive: `(|0>+|1>)/sqrt(2)` and `(|0>+i|1>)/sqrt(2)` give the same probabilities `(1/2,1/2)` for the complete commuting rank-one projectors `{|0><0|,|1><1|}` but are distinct rays (overlap squared `1/2`). Replace the claim with “the 82 projectors distinguish the 82 one-dimensional joint eigenspaces/basis rays.” Any claim of arbitrary-state resolution needs an informationally complete noncommuting observable set or an explicit superselection premise removing all coherences.

### F4 — Major — The “Gauss projector” is undefined as a map, its runner gate is non-discriminating, and non-canonicity does not follow

**Locations:** `THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:77-94, 104-108, 136-143, 162-177`; `record_readable_gauge_invariant_algebra_colour_blind_check_2026_09_03.py:424-446`.

The definitions introduce the Hilbert-space projector `P_G`, but the theorem and runner suddenly use an operator-map `Pi` with `Pi(C_0)=C_0` and call it “the Gauss projector.” `P_G C_0 P_G=0`, so `Pi` cannot be the declared `P_G` sandwich map. If `Pi` means gauge twirling/conditional expectation onto `I`, it must be defined.

The C3 pass condition constructs no `Pi` and tests only `(not dc_in_I) and in_I_exact(CAS0)`, facts already established in C2. It therefore cannot discriminate a wrong implementation or definition of `Pi`. C2 validly proves that the specific dephasing `D` does not preserve `I`. It does not prove that no canonical readable projection exists. Given the already computed component projectors `P_c`, the normalized-trace Hilbert-Schmidt projection

`E(M) = sum_c Tr(P_c M)/rank(P_c) P_c`

is a canonical conditional expectation onto the finite-dimensional algebra `R ∩ I` once the standard matrix trace is part of the declared setup. Define the intended `Pi`, directly test the two compositions on a witness, and narrow the conclusion to “the chosen record dephasing `D` is not gauge-compatible.” Delete the categorical non-existence claim unless “canonical” is formally defined with stronger requirements and ruled out.

### F5 — Moderate — Twenty-eight examples do not prove the universal tensor-operator statement

**Locations:** `THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:104-108, 168-179`; `record_readable_gauge_invariant_algebra_colour_blind_check_2026_09_03.py:459-476`.

The source claims “Every rank >= 1 tensor operator has a zero Gauss-sector block.” The runner checks 28 selected operators. This is not an exhaustive set or a proof of the universal quantifier, and “rank” is not defined precisely enough to exclude reducible operators containing a scalar component.

The intended Wigner-Eckart statement is standard and likely true for irreducible, nontrivial `SU(2)^4` tensor operators between joint singlets, but that theorem is load-bearing despite the note's assertion that no imported scientific authority enters. Either state “all 28 tested operators” or define the transformation law and prove the general selection rule (for example by gauge averaging) before retaining the universal claim.

### F6 — Moderate — The U(1) control does not isolate non-abelianity in general

**Locations:** `THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:120-126, 136-146`; `record_readable_gauge_invariant_algebra_colour_blind_check_2026_09_03.py:604-614`.

The exact control proves only that this particular `u(1)` summand, generated by diagonal charges `Q_v`, stabilizes the chosen record basis, so `R ∩ I = R`. The attached general sentence “An abelian group stabilises the record basis up to phase” is false. On one qubit, the abelian group `U(theta)=exp(-i theta X)` mixes the declared `Z` record basis and the diagonal algebra's commutant with `X` has dimension 1, not 2.

Likewise, a non-abelian representation may act diagonally through an abelian quotient or trivially on a chosen sector. Restrict the causal statement to the declared representations: the off-diagonal support of the chosen `SU(2)` generators reduces the intersection, while the chosen diagonal `Q_v` action does not.

### F7 — Moderate — Schmidt rank of one surviving vector is not the stated proof about the whole corner condition

**Locations:** `A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md:159-180, 182-197, 231-246, 295-305`; `non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.py:462-499`.

The runner finds one maximally entangled vector in the fixed `n_f=1`, occupied-end sector and infers that no single-site product basis can turn the full five-dimensional corner singlet condition into a record-value condition. Schmidt rank is invariant for that vector, but a coordinate constraint subspace may contain entangled vectors: the Bell state belongs to the record-value subspace `span{|00>,|11>}`. Thus the stated inference does not by itself prove the subspace claim, particularly when an arbitrary local basis change may mix the number/orientation sectors used to isolate the one-dimensional block. The E2 pass predicate also checks only the two Schmidt values and reduced density matrix; it never compares the vector's components with the specific signed Bell vector printed in the claim.

A separate focused control indicates the desired conclusion is salvageable. For the full declared rank-5 corner singlet projector, the commutator map with a general traceless one-qubit observable has nullity zero on matter factors 0 and 1 and on link-colour factor 3 (singular values respectively `[sqrt(10),sqrt(10),sqrt(2)]`, the same, and `[sqrt(2),sqrt(2),sqrt(2)]`). A projector diagonal in a product basis would commute with a nontrivial local axis on every factor. Replace the Schmidt-only inference with that full-projector local-commutant proof and an exact certificate; until then classify this as a missing proof, not a false conclusion.

### F8 — Moderate — Several exact equality phrasings are backed only by floating-point diagonalization

**Locations:** `A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md:1-4, 159-180, 216-226, 276-293`; `non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.py:404-453, 515-540`.

The frontmatter groups the singlet projector's extrema/hull with `[exact]` claims and calls the 82-dimensional result “exact linear algebra,” while the runner uses `numpy.linalg.eigh`, tolerance cuts, and floating projectors. The dimension 82 has a genuinely exact independent character calculation, but `max off-diagonal = 0.25`, exact hull statements, spectrum symmetry/zero multiplicity, and especially `E_0 = -sqrt(34)` are only numerical checks. Comparing a floating eigenvalue to `sqrt(34)` within `1e-10` does not prove the radical equality. The D5 pass predicate prints `max_diag = 0.25` but only checks `max_diag < 1 - 1e-6`, so that displayed value is not even protected by its named gate.

Align the machine scope with the body’s numerical labels, use `≈` for the energy, and avoid propagating `E_0(g) = -sqrt(34)+(3/2)g^2` as exact. If exact identities matter, supply a rational/symbolic invariant-subspace certificate or exact characteristic/minimal-polynomial and ordering proof.

## Preserved finite results

The following results survived line-by-line review within their declared finite model:

- The one-rishon four-dimensional link representation, the local `su(2)` commutators, central `Q_v`, and exact commutation of the declared hop with all local generators.
- No one of the 65,536 declared computational record-basis vectors is in the joint `SU(2)^4` Gauss kernel. An independent representation argument supports this: every link contributes a doublet at one endpoint, and any corner carrying active doublets requires a nontrivial singlet superposition; all four links cannot have their occupied endpoints absent simultaneously.
- The singlet multiplicity 82 and open-string multiplicity 94 are independently supported by exact character arithmetic; the floating Gram spectra show a large gap of 2.
- For the declared record basis, `R ∩ I` is the component-constant algebra with 1,296 atoms, equivalently functions of matter occupations and link orientations, and is generated by the stated `Q_v` and end-Casimir data.
- The restriction of those atoms to the singlet sector yields 82 rank-one orthogonal projectors. This is a maximal commuting projective measurement, with the state-resolution limitation in F3.
- The raw record distributions for the selected open-string colour partners are disjoint, while exact commutation of the component projectors with the gauge group makes their coarse probabilities invariant under all gauge rotations. The finite angle scan is a numerical illustration, not the reason for the general invariance.
- The symmetric electric term is exactly the scalar 3 on the chosen one-rishon carrier. The quoted energies and projector extrema remain bounded numerical observations.

## Runtime and limits

The cached runner hashes match the packet scripts. Both fresh runs used `/opt/homebrew/opt/python@3.13/bin/python3.13`, single-thread BLAS environment variables, and an inherited 150-second alarm.

The first run's attempted native `ulimit -v 2097152` failed on this macOS host (`setrlimit failed: invalid argument`), so a 2 GiB RSS ceiling was not enforceable for that already-consumed one allowed run; it finished in 0.90 s. The second used an external RSS monitor and peaked at 299,368,448 bytes, safely below 2 GiB, finishing in 1.61 s. This limitation is operational and does not change the mathematical findings, but it is an explicit protocol deviation for the first run.

Full read coverage, hashes, unreviewed material, command timings, and captured outputs are recorded in the companion artifacts in this directory.
