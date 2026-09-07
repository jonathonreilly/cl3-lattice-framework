# Curved covariance — bounded held-source checkpoint

**Disposition: HELD. Standalone finite-matrix salvage is identifiable, but no existing seven-PR packet or extracted replacement has a final source PASS.** Review remains queued, not closed. Root reprioritized the new admissibility successor #8003 after this dependency/salvage checkpoint. No source edits, benchmark imports, production runs, audit runs or applied statuses were performed.

Frozen raw head `774374271180405d5c2522010511adbd2c906236`, tree `feb25916c46f1b83243017c8ca54543a668de306`; original authority main `2d0f551dcd8bd444daee85b97811cda53da0661e`. Current main subsequently advanced to `a8f84aaad75fdcb790ba6ba094e4275e237d9a5a` by the separately reviewed admissibility unit. This checkpoint is not a current-main integration verdict. The original 78 selected authored paths and seven constituent heads/bases/original deltas were frozen before reviewer artifacts; all 78 working source hashes were rechecked unchanged. Original deltas and their hashes, including excluded generated/nonselected paths, are in `frozen_source_inventory.json` and `checkpoint_constituent_dispositions.json`.

## Reserved dependency boundary

Static local-import closure from the seven runners reaches **52 modules / 91,107 source lines**. Of these, 45 are outside the selected 78-path unit and absent on the frozen current main. This is static reachability, not a claim that all 91,107 lines execute or prove current claims. Exact module hashes, local imports and declared input paths are pinned in `dependency_closure_initial.json`. There are 152 unique declared input paths across the closure; these are not all verified scientific premises.

All three reserved runners are reached: Block 105 shifted-origin/frame-gauge/Hodge overlap (#6379), Block 142 carrier reflection (#6858), and Block 143 staggered Hermitian pairing (#6859). The latter two arise through the long Block 201 → generator-trilemma chain. Shortest static paths are recorded in `reserved_dependency_paths.json`. Reading a descendant or including it in an inventory does not authorize these sources.

The direct, demonstrably load-bearing Block 105 usages are narrower than that large graph:

- Block 213 runner lines 1456–1469 invokes `shear_hodge`, `onsite_hodge`, `overlap_field`, and `overlap_hodge`, using the reserved source's nonuniform shears/extents. This is the claimed exact assembler-fidelity test, not merely an unused import.
- Block 211 runner lines 147–148 binds `LANDED_SHEAR_HODGE = b128.block105.shear_hodge`. Block 213 then uses that callable for face/Hodge identification, reconstruction and controls (e.g. lines 1240, 1449, 1471, 1817, 1855).
- Block 201 directly calls `b128.block105.shear_hodge` at lines 620, 871, 1078 and 1220. Block 213 imports its lane/grading/fork source claims, and later runners inherit the same construction chain.

Consequently the statements identifying the explicit cell/rule matrices with the inherited Hodge, nonuniform onsite/overlap assemblers, shadow/covariant-rule helpers, and their current-framework origin remain **deferred with original raw-source recovery provenance**. Their benchmark receipts cannot establish an authorized standalone source boundary. All seven canonical runners are held: their authority and construction gates intertwine these claims. Do not copy a reserved function into a fresh helper or silently label it an arbitrary hypothesis. A new supplied-matrix theorem must state that premise explicitly and omit inherited assembler-identity claims.

The current cache/authority contracts also need eventual review: declarations differ from transitive actual inputs; Block 213's authority reads include axioms/registry outside its declared list; later descendants omit some transitively imported older helpers. Several original gates pin a historical `origin/main` and raw-parent ancestry. Their historical PASS receipts are provenance, not current-main scientific validation. No fresh large benchmark was run because it could not lift the reservation.

## Smallest honest standalone source candidate

The smallest identifiable unit is **Block 213 N2's three-dimensional determinant lemma for a supplied degree-block matrix and an explicitly defined exterior differential**, without any lattice/curvature/gravity identification:

1. Define the eight-dimensional exterior basis by lexicographic bit triples `(t,x,y)` and let `D(k)` wedge by `k`, using insertion parity. Define a symmetric supplied `H = diag(D0,D1,D2,D3)` by form degree, with degree-one coordinates `(t,x,y)` and degree-two complementary coordinates `(xy,ty,tx)`.
2. For `M = H D + D^T H`, take the even–odd block in exactly the note's corner order. With `E = diag(1,-1,1)`, prove `det B = D3 (k^T D1 k)(k^T E adj(D2) E k)`. No positivity or inverse is required for this polynomial identity; invertibility/positivity must be added separately for pencil/metric readings.
3. State only a determinant factorization of supplied finite matrices. It supplies neither a selected cell, an Admissibility law, Lorentzian metric, physical gravity, nor a uniqueness result for competing constructions.

A reviewer-owned construction importing **no repository module** verified this identity in all 17 formal variables (six entries each in symmetric D1 and D2, D0, D3 and three momenta). `symbolic_onsite_det.json` records exact zero residual. An independent asymmetric positive-definite example and three actual semantic mutations are in `independent_matrix_checkpoint.py` / `.json`; changing an exterior insertion sign, the congruence sign, or the complementary signature each breaks the corresponding identity.

The next small possible extension is Block 214's **general D07 congruence and Schur shift**, and its **4×4 parity-block determinant sufficiency** when `D16 = D34 = -D25`. The congruence survives the counterexample below. The branch-rescaling conclusion must be narrowed first. This extension has not received a complete proof/source/label review. Block 218's finite Bloch-point argument offers a later explicitly supplied phase/differential theorem, but its full source and quantifiers remain unreviewed. No extraction has been authored or approved for landing; even the smallest candidate still needs a complete clean source contract, proof, independent focused runner, import/negative-scope/label/governance review and exact-source confirmation.

## Concrete findings to carry into any salvage

**P2 — Block 214 note lines 232–234: general D07 congruence does not imply a single zero-form branch rescaling off the star line.** The note says `D07` acts only by replacing `k^T D1 k/D0` with `k^T D1 k/(D0-D07²/D3)` at general symbolic moduli and other parameters. Take the positive-definite flat-family matrix `H = I8 + (E07+E70)/4 + (E16+E61)/3`, with `k=(1,2,3)`. The claimed branch is `224/15`, but for `L=(H^-1 M)^2`, `det(L-(224/15)I)=528724036/455625`, nonzero. The exact characteristic polynomial is `(8λ²-238λ+1719)²(15λ²-434λ+3056)²/14400`. Both displayed D07 congruences hold in this example. Fix: retain the general congruence/Schur shift and restrict the branch-only conclusion to the degree-diagonal/star-line hypotheses actually proved; do not propagate it as a general off-line branch identity. This does not refute the separately stated star-line witness formulas.

**P2 — Block 214 note line 251: the arbitrary-square-block lemma omits its dimension parity sign.** For square `n×n B`, the determinant is `(-1)^n det(B)^2` when either diagonal block is zero. The source's actual `n=4` case is correct. A one-dimensional counterexample is `det[[2,3],[3,0]]=-9`. Fix the general formula or say explicitly `B is 4×4`.

**P2 — Block 216 note line 344: “four distinct branch constants” contradicts the preceding table and its stated degenerate transverse pair.** The displayed values are `1,128/99,16/11,16/11` at the first witness. Fix to four branches with the transverse pair degenerate, and state distinct-value claims only at checked/derived parameter ranges.

These are source findings, not a complete findings list. No claim is made that the unread remainder is clean.

## Coverage and recovery ledger

All 78 selected paths are **deferred**, preserving their exact raw hashes: seven scientific notes, seven paired runners, seven cached result files, and 57 planning/review/provenance files. Original generated/nonselected deltas remain excluded from landing, with original hashes retained. No historical reviewer PASS has been adopted. The path-level map is complete for the held disposition; a final inherited-claim/content disposition map is not complete.

- **#7981 / Block 213:** source note N0–N4 through line 380 read; N2 general onsite determinant independently rederived. Runner introduction/authority through line 525, rule/matrix definitions 802–958 and 1088–1177, and construction 1408–1480 read. Remaining proof/census/spectra/import/no-go/history material and numerical families not fully reviewed. Bench/Hodge/shadow identifications deferred; determinant-only candidate identified.
- **#7988 / Block 214:** note principal parity/D07/union discussion lines 172–262 read; runner introduction 1–100 and construction 383–433 read. General D07 overclaim and block-determinant sign found. Remaining locus/spectrum/registration proofs and current source gates not reviewed. Congruence/sufficiency candidates identified; full claim package deferred.
- **#7992 / Block 215:** import/metadata/outline scanned. Covariance action, subgroup census, strict-versus-twisted identification and no-go gates not fully read or recomputed. All claims deferred; no independent covariance or physical interpretation verdict.
- **#7993 / Block 216:** note through line 380 read; statement/table inconsistency identified. Remaining interpretations, imports, N1–N8, claim register and runner mathematics not fully reviewed. Census, necessity-at-witnesses and symbol claims remain deferred; sufficiency remains a possible arbitrary-cell theorem after full proof review.
- **#7994 / Block 217:** imports/metadata/outline scanned only. Overlap assembly, covariance and one-direction bench claims deferred without math verdict.
- **#7995 / Block 218:** note N2 lines 199–255 read, plus imports/metadata/outline scan. The finite-point proof appears potentially separable if differential, phase, invertibility and momenta are explicitly supplied. Remainder and runner unreviewed; no theorem confirmation.
- **#7997 / Block 219:** imports/metadata/outline scanned only. Three-direction benchmark and full-metric-read-off claims deferred without math verdict.

The seven original heads/bases and their complete original file deltas are frozen in the inventory. Each constituent row points to final raw hashes or explicit exclusion/recovery. The 45 dependency modules' source is **not** substantively reviewed merely because AST imports and hashes were scanned. The 57 planning/provenance files have not all been read in full. Cached stdout has not been freshly reproduced. The full no-go N1–N8, theorem/proof obligations, physics boundary, import, label, governance and audit-compatibility lenses therefore remain incomplete for this unit. Source review has made decisive progress on the import boundary and selected matrix claims; it has not reached a final packet PASS.

Recovery should resume from this checkpoint in the same reviewer session, first choosing whether to author the minimal supplied-matrix unit or keep the full packet held. Reserved content remains excluded unless the owner explicitly changes the reservation. Root alone owns any subsequent source edits, current-main integration and mechanical pipeline. Formal audit remains deferred.
