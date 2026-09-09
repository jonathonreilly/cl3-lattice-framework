---
claim_id: non_abelian_gauss_law_no_record_pattern_solutions_plaquette
claim_type: bounded_theorem
claim_scope: "Conditional on the declared four-corner cycle, eight JW modes, four one-rishon four-state links, fixed occupation basis and displayed G,Q,H: exact finite gauge algebra and zero of 65536 basis patterns in the Gauss kernel; 544-pattern Cartan hull and singlet multiplicity 82; a full corner-projector PPT obstruction across the specified matter/link partition; centre parity is necessary but not sufficient for a singlet; numerical supplied-H spectra. Fixed-basis joint probabilities do not determine Gauss membership. No physical Record, formation, confinement or gauge realization is derived."
upstream_dependencies: []
runner: scripts/non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.py
---

# A non-abelian Gauss law has no record-pattern solutions on the declared plaquette

**Date:** 2026-09-03; corrected 2026-09-08.
**Type:** bounded_theorem
**Status:** conditional-support for the supplied finite model; independent audit unset.
**Primary runner:** [non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.py](../scripts/non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.py)
**Runner cache:** [actual execution receipt](../logs/runner-cache/non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.txt)

Conditional on the declared four-corner cycle, eight JW modes, four one-rishon four-state links, fixed occupation basis and displayed G,Q,H: exact finite gauge algebra and zero of 65536 basis patterns in the Gauss kernel; 544-pattern Cartan hull and singlet multiplicity 82; a full corner-projector PPT obstruction across the specified matter/link partition; centre parity is necessary but not sufficient for a singlet; numerical supplied-H spectra. Fixed-basis joint probabilities do not determine Gauss membership. No physical Record, formation, confinement or gauge realization is derived.

## Supplied model and authority boundary

These are conditional finite matrix statements. A record pattern here means a vector of a **supplied joint occupation basis**. The joint tensor-product quantum carrier, its encoding into 16 binary labels, state-to-probability rule `p_r = <r|rho|r>` (or `|psi_r|^2`), and restriction of observables to a specified algebra are explicit model choices. They are not derived physical readout or formation rules.

The [current framework memo](MINIMAL_AXIOMS_2026-06-29.md) governs the interpretation boundary: Record supplies content-determined readout, but does not supply this Fock encoding, Born weights, physical gauge realization, gauge-invariant measurement restriction or formation law. Its bytes and this note's bytes are pinned by the standalone primary runner. No new axiom, primitive, audit status or physical identification is supplied.

Context, not proof premises: `QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md` concerns a supplied **unitary map C2 -> C2**. The four-state, nilpotent quantum link below is independently declared; only the Lie-algebra shape is shared. The current `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md` establishes conditional reconstruction of a supplied one-corner relation on occurring prefixes and gives global failure controls. It supplies no axiom-level formation odds or any-order global formation theorem. `NATIVE_HOLONOMY_PLAQUETTE_CENTER_FLUX_NO_GO_NOTE_2026-05-23.md` concerns native unitary hops; it is not a premise about the designed nilpotent links here. The old `RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md` is historical proposal context, not adopted Record authority. `archive/notes/docs/COLOR_DERIVATION_CAMPAIGN_20260706_ASSEMBLY_AND_HONEST_REBOUNDING_META_NOTE_2026-07-06.md` is archived navigation, with no premise weight.

## Definitions

Four corners `v=0,1,2,3` form a cycle, with links `e_k=(k,k+1 mod 4)`. Each corner has two fermion modes `alpha=0,1`, Jordan-Wigner index `2v+alpha` with mode zero leftmost. Each link has basis `|i,0>,|i,1>,|j,0>,|j,1>`, a supplied orientation-bit times colour-bit factorization. This is a four-dimensional factor, not one framework qubit site. The total carrier is `H=(C4)^4_matter tensor (C4)^4_link`, dimension `65536=2^16`.

```text
P_i=diag(1,1,0,0), P_j=diag(0,0,1,1), P_i+P_j=I
U_e^{ab}=-|j,b><i,a|, U^{ab}U^{cd}=0
sum_ab (U^{ab dagger}U^{ab}+U^{ab}U^{ab dagger})=2 I
E^a_{e,s}=P_s (I2 tensor tau^a/2), s=i,j
rho_v^a=sum_pq psi_vp dagger (tau^a_pq/2) psi_vq
n_v^f=sum_a psi_va dagger psi_va; n_v^r=sum_{e at v} P_{e,v}
G_v^a=rho_v^a+sum_{e at v} E^a_{e,v}; Q_v=n_v^f+n_v^r
H_hop=-t sum_e eta_e sum_ab [psi_ia dagger psi_jb U_e^{ab}+h.c.]
eta=(1,1,-1,-1); t and g are supplied real coefficients; numerical fixture t=1
R={diagonal operators in the declared occupation basis}
I={M:[M,G_v^a]=0 for all v,a}; A=R intersection I
P_G=orthogonal projector onto the joint kernel of all twelve G_v^a
```

The word colour denotes the supplied SU(2) index. No SU(3), Standard Model identification, physical confinement, mass gap, larger block or continuum limit follows. Static operator kernels, classical joint supports, formation processes and physical readout are separate questions.

## T1 — construction and holonomy (A1–A3)

The eight JW annihilators satisfy the canonical anticommutators. Each link factorizes as declared, has commuting end su(2) actions and satisfies the truncated U identities above. `H_hop` is Hermitian with `131072` nonzeros. The loop product `U_p^{ad}=sum_bcx U_01^{ab} U_12^{bc} U_23^{cx} U_30^{xd}` has `32` nonzero entries; subtracting half its colour trace leaves `48`. This is an operator-valued loop on the designed link, not a group-valued unitary connection or a physical gauge field derivation.

These checks use exact dyadic entries and bounded finite sparse sums. A dyadic input alone would not prove all subsequent floating-point work exact; numerical eigensystems and tolerances are distinguished below.

## T2 — gauge algebra (B1–B6)

Sparse exact identities on the full carrier give `[G_v^a,H_hop]=0` for 12 pairs, `[Q_v,H_hop]=0` for 4 corners, `[G_v^a,G_v^b]=i epsilon_abc G_v^c` for 36 ordered same-corner pairs, cross-corner commutation for 108 pairs, and central `[Q_v,G_w^a]=0` for 48 pairs. Thus the supplied representation has `u(2)=su(2)+u(1)` at each corner. `max|[G_v^1,G_v^2]|=1.5`; each `G_v^3` is nonzero. Gauge invariance here means this matrix commutation property.

## T3 — basis census, singlet sector and local partition (C1–C2, D1–D6, E1–E2)

`G_v^3` and `Q_v` are diagonal; each of the two transverse families has `393216` off-diagonal entries summed over corners. Exactly 544 patterns have all `G_v^3=0`, and all 544 have even `Q_v`. **Zero** patterns lie in the full Gauss kernel. The runner checks the Cartan diagonals and `sum_v ||G_v^+|r>||^2` by exact equality over all 65536 patterns.

An independent identity explains the zero census without a search argument. For a product pattern r, transverse actions on different occupied factors give orthogonal output patterns, so

```text
sum_va ||G_v^a |r>||^2 = (4 + number of singly occupied matter corners)/2
                          + sum_v (G_v^3 diagonal at r)^2 >= 2.
```

The four rishons each contribute one transverse spin-half term; singly occupied matter corners contribute the others. The Cartan term includes its cross terms. This exact bound is checked against the actual generator Casimir diagonals.

Numerical diagonalization of the 544-dimensional raising-Gram cut at tolerance `1e-9` gives singlet dimension 82 and nonzero gap 2. Exact integer character arithmetic independently gives 82: if M(p) is the singlet multiplicity in p doublets, `c(p)=2M(p)+M(p+1)=[2,1,2,2,4,5]`; sum the product of c at the four corners over 16 link-orientation assignments. This is the integral of `prod_v(2+chi_v) prod_e(chi_i+chi_j)`.

The numerical projector `P=VV dagger` has trace 82, is Hermitian and idempotent within `1e-9`, annihilates the actual twelve generators, and has maximum diagonal and off-diagonal magnitude `1/4`. Its support hull is exactly the 544-pattern Cartan cut. This hull means precisely the coordinates that can have nonzero weight in a singlet. It does **not** characterize singlet membership: an actual normalized projector-column singlet and a single-bit phase flip have identical **complete** fixed-basis joint probabilities, while the latter has nonzero Gauss residual. Classical record correlations therefore do not recover the missing phase information.

For the local obstruction distinguish two carriers. The auxiliary corner is `C4_matter tensor C4_link` with `G=rho+E_i` and kernel rank 5. With one matter quantum and a rishon at that end the unique normalized kernel vector is the antisymmetric colour singlet, Schmidt spectrum `(1/sqrt(2),1/sqrt(2))`. Its actual annihilation by each G and relative phase up to global phase are checked. Entanglement of this one vector alone would not rule out a product basis of the entire rank-five subspace.

The **full** auxiliary kernel projector is the direct sum of identity on the four empty/doubly-occupied-matter, absent-rishon states and the rank-one occupied singlet projector. Its partial transpose across matter versus link has exact spectrum `{-1/2:1, 1/2:3, 1:4, 0:8}`: the singlet term contributes the negative eigenvalue and three `1/2` eigenvalues, and the disjoint spectator sector contributes four ones. A positive projector diagonal in a product basis is a sum of positive product rank-one operators; its partial transpose is positive. Hence this full projector has no such product-basis diagonalization.

The actual plaquette corner is `C4_matter tensor C4_outgoing tensor C4_incoming`, dimension 64, with `G=rho+E_i(outgoing)+E_j(incoming)`. The auxiliary local matter basis uses the explicit permutation `[0,2,1,3]` relative to the global two-mode JW basis. It changes coordinates only. The local-to-global restriction is checked for all three generators. The actual corner kernel has rank 14. Compressing the incoming link to its **i** orientation (rishon absent from this corner) gives exactly `P16 tensor I2` in this local basis. Such local compression preserves separability across matter versus both links, so the actual corner projector also lacks a product-basis diagonalization across that partition. Arbitrary entangling encodings and a derived physical site/readout realization remain outside this statement.

On the same supplied carrier and aligned basis the separate abelian condition `Q_v=q0` has counts `{0:0,1:32,2:1312,3:32,4:0}`. These are finite joint relations, not formation laws.

## T4 — invariant diagonal content (C3–C5)

The corner Gauss Casimirs have 98304 off-diagonal entries in total. The matter-only Casimir is diagonal and equals `(3/4)n_v(2-n_v)` exactly. Centre parity is `(-1)^Q_v`; all four are even on 4096 patterns. It records half-integer versus integer total spin, not singlet versus every nonzero charge. Matter occupation, matter Casimirs and link-end data also give invariant diagonal content. Patterns 16125 and 16384 have identical four centre parities but different corner-zero occupations. An actual local j=1 state has Casimir 2 and even centre, furnishing an integer-spin countercontrol.

The frame-aligned `G_v^3` is diagonal but not invariant. A raw pattern can carry such frame-dependent information; restricting to gauge-invariant observables is an additional supplied requirement. No assertion that centre parity is the only frame-free content survives.

## T5 — supplied-H spectra (F1–F3)

Exactly `sum_e,s,a (E^a_{e,s})^2=3I`, since each of four one-rishon links contributes 3/4. Therefore this term shifts every energy by `3g^2/2`. In the 82-dimensional singlet sector at t=1, numerical diagonalization at `1e-10` gives ground energy `-5.830951894845`, consistent with `-sqrt(34)`, and a 40-fold numerical zero. The runner checks every sorted eigenvalue against its reflected partner. This is numerical agreement, not an exact minimal-polynomial proof of the radical.

The separately declared one-sided term `sum_e,a (E^a_{e,i})^2` is nonconstant and commutes with all twelve G exactly. It breaks link reversal and gives numerical ground energy `-5.126268164739` at g^2=1. No principle selects this variant or its coefficients.

## Proof obligations and remaining scope

Construction supplies the matrices; exact algebra establishes their symmetry; the Cartan/raising kernel and independent character count establish the singlet dimension; its actual projector supplies the hull and the restricted spectra. The local PPT argument concerns the specified tensor partition. None of these steps supplies physical role assignment, a measurement instrument, formation odds or dynamical confinement. Larger blocks, different representations and entangling readout protocols remain separate questions.

## No-Go Discipline Gate

N1 — Actual route families and scope: (i) ATTEMPTED fixed-basis matrix/graph constraints, with complete finite support checks; (ii) ATTEMPTED full local-kernel separability/PPT test, whose obstruction is limited to the matter/link partition; (iii) ATTEMPTED quantum-superposition and phase information, which survives and defeats broader classical-tomography or membership claims; (iv) ATTEMPTED changing the readout map, for which the component-mean conditional expectation succeeds; (v) ATTEMPTED changing the gauge representation, for which the aligned Q control succeeds and an unaligned abelian control defeats a universal contrast. These are real contrasting routes across this two-note correction, not five failures or five independent proofs of each negative subclaim. The current five-closed-family packet requirement is **not claimed satisfied** for each narrow negative theorem. Any resulting submission limitation remains distinct from finite mathematical validity; no packet PASS or exhaustive physics no-go is asserted.

N2 — No independent-wall count is claimed. Fixed basis, tensor partition, representation and quantum interpretation are supplied premises with interactions, not proved independent obstructions. A changed basis can change both the graph algebra and accessible statistics.

N3 — Hidden-premise scan: the joint quantum carrier, Born comparison, gauge-invariant observable restriction, basis and trace convention are now explicit. “Canonical” qualifies the mathematical trace expectation only. Historical framework/campaign references grant no additional premises.

N4 — No prior no-go is used as proof. The native-hop scalar-holonomy residual differs from the designed nilpotent-link calculation; the unitary-connection carrier differs from the four-state quantum link; and the U(1) one-corner reconstruction result does not prove global formation. These mismatched authority readings are removed.

N5 — Resolution: actual generator entries and all 65536 fixed-basis patterns are tested; local 16/64-dimensional corner partitions and one full plaquette are the domains. The quantum-state witnesses compare complete joint probabilities, not just marginals. No lattice-wide, SU(3), arbitrary-readout or continuum impossibility is tested or implied. Exact integer/dyadic claims and tolerance-based eigensystems are separated.

N6 — Partial closure: the 1296-dimensional invariant diagonal algebra,82 singlet basis populations and a CP trace expectation are useful surviving constructions. Quantum states and altered readout contexts are legitimate alternative domains. No new axiom is declared necessary.

N7 — Steelman: a gauge-invariant quantum state exists even though no coordinate pattern is itself a singlet; an entangling encoding or additional readout protocol could expose its coherences. To claim physical impossibility one would have to rule out those realizations under actual framework premises. That obligation is unclosed and excluded here. It does not refute the finite fixed-basis census or partition-specific projector proof.

N8 — Cross-cycle comparison: the current corrected U(1) note separates local conditional projections from global formation, and the archived colour campaign has no active premise authority. The historical no-canonical-projection and complete-state-separation assertions in these original notes are themselves retired by explicit mathematical counterexamples. They cannot be reused as evidence against the surviving alternatives.

## Source preservation and execution

All original check IDs remain in the primary runner (25 original checks). Corrections strengthen predicates and add named controls; no original successful check output is rewritten as if it had tested the new statements. The [original note](../.claude/science/physics-loops/nonabelian-correction-20260908/original/docs/A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md), [original runner](../.claude/science/physics-loops/nonabelian-correction-20260908/original/scripts/non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.py) and [complete original cache](../.claude/science/physics-loops/nonabelian-correction-20260908/original/logs/runner-cache/non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.txt) are exact historical bytes from tree `311884f5b5516ba1dac437e7b75db2533a41c71e`. They contain superseded claims and numerical fixtures, not current authority. The [correction record](../.claude/science/physics-loops/nonabelian-correction-20260908/CORRECTION_RECORD.md) maps finding dispositions.

The primary is standalone; it imports no parent science runner. Its actual own-note/current-memo inputs are declared and hash-guarded. Final execution evidence belongs in the linked cache, with command, source and input identity; this note does not prewrite a new PASS total. Source review and combined integration validation remain separate from independent formal audit, which is deferred under the owner's campaign direction.
