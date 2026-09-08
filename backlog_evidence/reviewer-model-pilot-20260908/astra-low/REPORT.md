# Independent blind science review — astra-low

UTC start: 2026-09-08 14:31:41 UTC. UTC end: 2026-09-08T14:36:23.903436+00:00.
Frozen original tree: `311884f5b5516ba1dac437e7b75db2533a41c71e`; context base: `8257bddfc97ab763d208b43e9bdc8677fe89b1e8`.

Disposition: preserve the finite algebraic results, but correct the stronger interpretations before reuse. Four actionable findings follow; no formal audit status is assigned.

## F1 [P1] The 82 rank-one commuting projectors separate every physical state, losing nothing.

Location: `docs/THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:110`.

A complete commuting set separates its 82 joint eigenvectors, not all states in their 82-dimensional span. For two labels |a>, |b>, the orthogonal physical states (|a>+|b>)/sqrt(2) and (|a>-|b>)/sqrt(2) have identical probabilities for every element of R intersection I. The gauge-invariant operator |a><b|+|b><a|, extended by zero outside the Gauss sector, distinguishes them with expectations +1 and -1. controls.json reproduces the two-dimensional calculation. The rank-one/projector gate at runner lines 485-498 cannot detect this loss of coherence.

Correction: Preserve the complete commuting set result; replace all-state resolution and lossless language (also introduction, corollary, C7 output and review record) with separation of 82 joint eigenstates / recovery of their populations. Explicitly state that relative phases and general density matrices are not resolved.

## F2 [P1] D and the Gauss projector fail to commute, hence there is no canonical readable part or projection onto R intersection I.

Location: `docs/THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:106`.

Failure of D to preserve I is valid, but does not rule out a canonical conditional expectation onto A=R intersection I. With the already-computed component projectors P_c, E_A(M)=sum_c tr(P_c M)/tr(P_c) P_c is the unique Hilbert-Schmidt orthogonal projection onto A, trace-preserving, unital and completely positive. It is defined from exactly the existing matrix algebra and component partition, fixes A and discards other information. A small component example in controls.json verifies idempotence and trace preservation. Also Pi in the proof is an operator-space projection onto the commutant (e.g. Haar twirling), not the defined Hilbert-space Gauss projector P_G: P_G C_0 P_G=0, not C_0. Runner C3 tests only the previously established nonmembership and does not implement either projection.

Correction: Define Haar twirling Pi separately from P_G. Retain D(I) not subset I and the noncommutation of D with Pi; remove the impossibility of canonical projection. Give E_A explicitly, or restrict the negative claim to D alone and note that selecting a physical measurement interpretation remains additional work.

## F3 [P2] The contrast is caused by non-abelian structure alone; an abelian group stabilises the record basis up to phase.

Location: `docs/THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:126`.

Abelianity permits a simultaneous eigenbasis; it does not align that basis with the declared records. On this very carrier, the four generators G_v^1 commute across corners and generate an abelian subgroup, but their off-diagonal support has exactly the same connected components as the union of G_v^{1,2}: each elementary matter/link colour flip has nonzero real G^1 coefficient and the same support in G^2. Thus the readable commutant is still 1296-dimensional for this abelian control, with the record basis and carrier unchanged. The simpler single-qubit abelian generator X gives diagonal commutant dimension one; controls.json verifies [Z,X] has maximum magnitude 2.

Correction: Keep the exact Q_v control. Attribute its readability to the Q_v representation being record-diagonal, and remove the claim that commutativity alone makes every record value physical. Include the G_v^1 abelian control or expressly limit the comparison to the declared Q_v embedding.

## F4 [P2] The declared open-string state has reproducible fixed support counts and numerical matter readouts.

Location: `scripts/record_readable_gauge_invariant_algebra_colour_blind_check_2026_09_03.py:516`.

psi_p is chosen as column zero of an eigensolver basis for a 94-dimensional degenerate kernel. That vector is not uniquely specified by the mathematical construction and may change under admissible rotations within the kernel or LAPACK versions. Nonetheless D4, D5 and D7 require supports (174,174,348), exactly 23 occupied classes and readouts 0.793369885/0.606802758. A valid alternative highest-weight state fixes every link orientation to i; sets n_f0=0; and puts matter/rishon singlets at corners 1,2,3 with the corner-0 rishon up. It is j=1/2 only at corner 0, has Q0=1 and rho0^3=0, one readable class and 8 fine patterns, while retaining TV=1 between partners and complete gauge-invariant colour blindness. The originals pass on this environment; this is a portability/definition defect, not an observed runtime or symmetry failure.

Correction: Declare a deterministic state independently of eigensolver basis, for example project a fixed vector into the kernel and normalize with a nonzero check, or use the explicit product of singlets. Regenerate state-specific numbers. Gate invariant properties separately from optional historical vector-dependent values.

## Valid results and proof checks

Both original runners were executed exactly once, unmodified, with a 150-second wall cap, single-thread BLAS environment, sampled 2-GiB RSS enforcement and captured stdout/stderr. Both completed normally: the first reports PASS=25 FAIL=0, the second PASS=27 FAIL=0. Actual elapsed times were approximately 0.981 and 1.487 seconds; peak sampled RSS was 231129088 and 276561920 bytes. This agrees with the supplied historical caches on pass/fail outcomes. `timings.json` and the raw output files preserve actual evidence; no timeout is interpreted as a scientific failure.

The construction implements the declared finite quantum-link model. The local matter bilinears and link-end spin generators give the stated Lie algebra; the hopping contraction conserves each gauge generator and Q. The direct zero-pattern census is discriminating: each record product has an occupied link spin whose raising/lowering action produces an orthogonal flipped pattern, so a product record cannot be annihilated by all generators. A computational basis change by a gauge rotation cannot fix that. The independent control counts occupation/orientation classes and couples spins by integer recursion, reproducing 1296 classes, 82 singlets, 94 doublets, 193 irreps and commutant dimension 356306 without the runners' character-polynomial pipeline.

The 16-dimensional local kernel contains other product states, so merely exhibiting one entangled vector is not generally enough to exclude a product-basis diagonal projector. Here the stronger conclusion can be rescued: the complete rank-five kernel projector is the singlet projector on the occupied/matter-single block plus the four empty-or-double-matter/unoccupied-link product projectors. Its partial transpose has eigenvalue -1/2 (`controls.json`). A projector diagonal in any product basis is separable and has positive partial transpose. Thus this particular full corner kernel cannot be product-basis diagonal. This closes the local proof gap without calling the bounded result false. It does not promote the finite result into an axiom-level or general nonabelian no-go.

The component-constant diagonal commutant reduction is exact and sound, including its frame invariance under gauge conjugation. Colour-rotation blindness follows for every operator in I by commutation, independently of the chosen numerical vector. The tensor singlet-block selection rule is also valid; the tested matter spin-half quadrupole is identically zero, so that particular check adds no nonzero rank-two evidence. The electric constant and bounded spectra are supported by the original run; no independent exact spectral derivation was performed.

## Precision and scope cautions

The first note calls the eigensolver calculation “exact linear algebra” (line 164 and claim scope), while its proof and runner correctly label it numerical. Keep 82 as the exact independently certified multiplicity, but relabel the diagonalization, projector extrema/hull and Schmidt computations consistently. I do not treat this as a false multiplicity claim.

The declared record algebra is an explicit chosen context. The pinned minimal axioms do not themselves supply measurement basis selection or Born weights, and the older record-map proposal is explicitly context-dependent. The notes generally disclose the designed roles and basis. Their finite conclusions should retain those disclosures; they do not establish confinement or a modification of Record. “Kinematic confinement” is interpretation, not an extra mathematical conclusion of the commutant calculation.

## Coverage and limits

All six packet source bodies were read; their SHA256 hashes and equality with the original tree are in `coverage.json`. Every runner group was inspected for code/prose agreement. The installed reviewer skill was examined, then the pinned-base skill and its proof-governance reference were used; no delegation, landing, external write, source modification or formal audit was performed. `AGENTS.md` at the pinned base points to a moving instruction branch; that branch was not read because this comparison explicitly restricts context to the pinned base. No sibling reports or author corrections were accessed.

The non-load-bearing U(1) companion, quantum-link reference, native holonomy note and colour campaign note were not independently reviewed. Their broader claims are not certified here. No full ledger audit, external literature survey, larger block or SU(3) calculation was performed. The arbitrary-eigenvector finding is a mathematical reproducibility issue; a second-platform failure was not observed. All controls are small, finite checks and do not establish physical realizability under the framework axioms.

`controls.py` / `controls.json` contain focused independent controls (about 0.017 seconds). `run_originals.py` documents resource enforcement and original commands. Read-only shell/context queries each completed in less than one second according to tool timing; only original-run and control scientific timings are persisted separately. This report and FINDINGS.json are sealed for parent adjudication.
