---
claim_id: energy_product_and_test_body_law_above_the_half_filled_sea_conditional_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional real Slater preparations and finite FFT response arithmetic. The actual joint density differs from the classical source sum; on-shell action and extended-source force identities are exact within their supplied model, while finite point-source ratios are diagnostics. No physical test-body law is derived."
upstream_dependencies: [minimal_axioms, gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11]
---
# Two-pair sources, a quadratic response and the point-source approximation

**Date:** 2026-09-03; source correction 2026-09-08.
**Claim type:** bounded_theorem
**Status:** conditional source for independent review; no applied audit verdict.
**Primary runner:** [`scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py`](../scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py)
**Cached output:** [`logs/runner-cache/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.txt`](../logs/runner-cache/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.txt)
**Correction history:** [original bodies and the two #7881 revisions](../.claude/science/review-fixes/vacuum-energy-7879-7881-7885-20260908/REVIEW_CORRECTION.md).

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are the interpretation boundary. They do not supply the Hamiltonian, its vacuum, a Born/instrument law, an energy readout, a formation rule or a physical clock. The models below are stated mathematical choices. Historical parent quotations and audit/landing language are preserved in the dated history, with no new acceptance of those parent campaigns.

## Setting and used premises

Use the real L=8 staggered hopping matrix with twist (1,1,1), defined by eta_x=1, eta_y=(-1)^x, eta_z=(-1)^(x+y), and the negative-energy projector P of rank256. Its energy is -611.811768, gap 2sqrt(6-3sqrt(2))=2.651309 and diagonal 1/2. These are independently reconstructed finite definitions; no parent supplier campaign is loaded.

For two real particle-hole pairs, orthonormalize the two hole and particle spans separately and form P''=P-Q_h+Q_p. Define e_joint as the actual real row energy of P''-P. Define e1,e2 from the two separately prepared one-pair projectors. In general e_joint is not e1+e2. The separately supplied classical response source is s=e1+e2 (after the stated unwrapping/placement when using a larger response box). Keep all three objects distinct.

Supply H=-Delta on the periodic response box, G=H^+ off its constant mode, and A[phi;s]=<phi,Hphi>/2-<P0s,phi>. Only this action, zero-mode and test-source sign convention are used from the [current weak-field bridge](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md). The action's physical identification, its density-readout uniqueness and its imported infinite-distance theorem are not accepted by this unit. Here H and G are explicitly reconstructed, and all source units and placements are chosen.

The local row-energy formula is used for real states. Fixed-number preparation, even carrier parity and P0 mean subtraction are separate restrictions. Z-record probabilities do not determine offdiagonal energy; preparation and an energy readout require additional suppliers. The current memo derives none of those choices.

## Theorem 1 — two real Slater pairs (A1–A6, R1)

On the eight original cases d_pair=1,2 and D=(2,0,0),(3,0,0),(4,0,0),(3,3,0), P'' is a rank256 projector to the stated tolerance and has zero number deviation by construction. Single-pair energies, overlaps, normalization and all original data remain unchanged. At d_pair=1 the particle overlaps are 0.37/0.15/0.044/0.014 and hole overlaps 0.38/0.021/0.0013/0.0036. Relative joint-energy additivity defects are -2.1e-2/-2.3e-3/-2.7e-4/-5.8e-5. These are measured finite points, not a monotone theorem for arbitrary displacement.

The joint local-density defects 0.21/0.024/0.0027 are real and retained. R1 uses the actual same L=8 box at D=(2,0,0),d_pair=1: max|e_joint-e1-e2|=0.210861615 approximately. In that same Poisson box, substituting the actual joint source into the classical cross identity gives a residual about -0.284741566, while the classical-sum residual is at floating-point zero. Thus the distinction is tested on actual operands, not just renamed.

## Theorem 2 — classical-sum response (B1–B6)

Let B(e1,e2)=<e1,G P0 e2>. The PSD property of G makes Q(s)=<s,G P0 s> nonnegative for real s; it does not make every cross pairing B positive. Symmetry alone gives Q(e1+e2)-Q(e1)-Q(e2)=2B(e1,e2). This identity is exact for the classical sum and is verified on all sixteen response rows. It is not a formula for Q(e_joint).

The finite point control 4pi rG at r=Lb/4 is 0.3307/0.3275 for Lb=32/64. On Lb=64,d_pair=1 the B/(E1 E2 G(D)) ratios are 0.8517/0.9043/0.9650/0.9540. Other original box/separation rows remain unchanged. Dipole/quadrupole corrections give 0.9380/0.9146/0.9773/0.9576 on the same cases; those few residual comparisons do not certify an asymptotic expansion error.

For two rigid copies of one profile in Lb=64 the ratios are 0.9462/0.9736/0.9938/0.9986 at D=3/4/8/16. These are classical placed arrays, not a rebuilt joint Slater determinant. The approach toward one at these points is a finite diagnostic.

## Theorem 3 — extended versus point response (C1–C5)

Define F_num=-D_x B for rigidly translating the second extended source by the same central difference. The point approximation is F_pred=-E2 D_x phi1 at its chosen centroid. Their original x-component ratios are 0.8271/0.9719 and 0.8568/0.9209, with angles 5.7/6.5/1.9/0.1 degrees. The nonzero angles mean the vectors are not identical.

For rigid copies at D=3/4/6/8/10/16 the x ratios are 0.8981/0.9854/0.9982/0.9992/0.9997/1.0000. The retained coefficient is 4pi D^2 F_num,x/(E1 E2), not the vector norm: 0.9711/1.0398/1.0216/1.0060/0.9924/0.9260. The original quoted point rows 1.0194/1.0064/1.0009/0.9963 are historical comparisons at their own distances. No physical inverse-square error bound is established.

The old seed-rebuild residuals 0.396 and 0.00210 compare naive and KS-bulk-only maps. The latter misses the twist seam; this is an incomplete-map diagnostic, not a no-go for torus covariance. R2 solves the full actual edge-gauge map and binds all directed edges and the translated real density. Rebuilding a different profile, rigidly translating an array and covariantly carrying a state remain different operations.

## Theorem 3b — action sign and actual operands (H1–H3)

On P0, stationarity gives Hphi=P0s, so A*=-Q(s)/2. For the classical sum, its two-source cross term is -B(e1,e2), reading -0.522027 at D=(4,0,0). If this A* is chosen as the interaction energy U, the exact extended-source force is F_U=-D_x U=D_x B. By translation invariance it is the convolution of the translated second source with the central difference of phi1. It equals -F_num; this is the useful sign/action correction in original revision af1af53, preserved together with c7ca994.

For the original rigid copies H2 retains the inward x signs -2.808e-1 through -9.413e-3 and the 4e-16 sign residual. The point expression F_point=-E2 D_x Phi_N, Phi_N=-phi1, is a separate approximation. H3 now compares the actual FU and FN arrays and records their nonzero finite discrepancy, while separately checking the exact extended convolution against FU. The former zero residual compared a point expression with its own negation; that failed claim is preserved as history. The discrepancy is not repaired by loosening an equality tolerance.

This proves a conditional finite action identity and the sign on these fixtures. Selecting U=A*, treating e as a physical source and coupling an actual test body remain separate assumptions.

## Theorem 4 — energy and count choices (D1–D4)

At fixed D=4 the original band filter changes both energy and spatial profile. E_exc takes 3.8766/4.5998/5.3655/5.8591/6.0461; the endpoint factor is about1.56, not4. The energy product changes by2.425 and the chosen bilinear response by2.525, giving ratio of ratios1.041. This is not a pure rescaling at fixed shape.

The independently supplied two-delta count source has I=2 per source and B=0.0655525 in every filter row. It is deliberately held constant. Zero number deviation in the selected fixed-N Slater family does not remove charged even alternatives. The historical empty-vacuum source interpretation is retained as attribution in the correction record, not asserted proved here. These source choices cannot be attributed solely to a vacuum choice.

## Units and corollary

All calculations set hop t=1 and use explicit coarse-grid coordinates and response-box conventions. E_exc/t is dimensionless. G's coordinate normalization and any physical coupling must be supplied before identifying a dimensional interaction energy. No factor-two coarse/fine embedding, physical G_Newton, mass readout or absolute length is derived. The useful surviving result is a finite controlled comparison of distinct mathematical sources and force operands.

## Source and evidence boundary

The original numerical fixtures, seeds, windows and old check identities are retained. Exact original note/cache bodies and source Git blobs remain recoverable from the correction history; the current cache must come from an actual run after the final source and input freeze. A fresh cache binds a computation to source; it does not certify a physical interpretation. Each standalone runner declares and checks its own note, the governing memo and only the explicitly used current interpretation surface. No local computational helper or parent campaign is loaded.

## No-Go Discipline Gate

N1: This is a corrected partial comparison, not a complete physical no-go. The concrete routes and positive alternatives are identified in the theorem sections and actual check groups. Numerical variations within one model are not independent routes. No five-family procedural certificate or exhaustive route search is asserted by this source correction.

N2: No independent-wall count is made. The supplied Hamiltonian/preparation/readout/response choices form an input inventory, not demonstrated independent obstructions. For the input inventory H (law), P (preparation), R (readout), S (response/action choice), C (physical clock/formation interpretation), both directions in every pair are unresolved:

| Pair | First implies second | Second implies first | Independent? |
|---|---|---|---|
| H/P | unresolved | unresolved | unestablished |
| H/R | unresolved | unresolved | unestablished |
| H/S | unresolved | unresolved | unestablished |
| H/C | unresolved | unresolved | unestablished |
| P/R | unresolved | unresolved | unestablished |
| P/S | unresolved | unresolved | unestablished |
| P/C | unresolved | unresolved | unestablished |
| R/S | unresolved | unresolved | unestablished |
| R/C | unresolved | unresolved | unestablished |
| S/C | unresolved | unresolved | unestablished |

This table asserts no wall count; these bundles name actual inputs, not an independence theorem.

N3: The source explicitly separates conditional matrix/probability definitions, the selected particle-number domain, a classical response source, force convention and finite coordinate units. None becomes an axiom by being used in a runner.

N4: Every negative conclusion uses the named actual operands. A fixed-number counterexample does not close all even-parity preparations; a two-vector span does not close an APS boundary problem; a finite point/extended discrepancy does not close a different response mechanism. Historical references have no unmatched residual weight.

N5: Scalar/edge/one-mode and named finite-block statements have the stated exact or numerical support. No unexecuted lattice-wide physical law, asymptotic error bound or continuum formation statement is claimed. The runner prints the corresponding resolution boundaries.

N6: The positive alternatives include changing a supplied preparation/readout, retaining an explicit imported response, or using the exact extended-source or restricted-domain formulation. Naming one does not require or ratify a new primitive; no statement here says a new axiom is necessary.

N7: The strongest challenge is to construct the missing physical preparation and local measurement/formation map, or a different response operator, and show that it realizes an allowed alternative. That terminal obligation is open. The finite failures of particular operands cannot rule it out.

N8: The two original #7881 revisions already show why a source/action convention can change a conclusion while preserving measured magnitudes. The present seam-aware covariance and exact domain corrections likewise replace broad failure rhetoric by a correct finite statement. Neither mechanism proves the remaining physical interpretation. Formal audit is deferred; the next step is independent source confirmation and the coordinator's authorized mechanical gates.
