---
claim_id: the_vacuum_question_is_one_coefficient_of_the_law_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional Pauli and finite free-Fock spectral comparisons, with unrestricted and even-N domains separated. Preserve cube and flat-torus certificates, finite two-uniform-family scans and the analytic small-J coefficient. No global physical vacuum selection or certified L224 limit error is claimed."
upstream_dependencies: [minimal_axioms]
---
# Occupancy costs in a supplied free lattice model

**Date:** 2026-09-03; source correction 2026-09-08.
**Claim type:** bounded_theorem
**Status:** conditional source for independent review; no applied audit verdict.
**Primary runner:** [`scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py`](../scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py)
**Cached output:** [`logs/runner-cache/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.txt`](../logs/runner-cache/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.txt)
**Correction history:** [original bodies and the two #7881 revisions](../.claude/science/review-fixes/vacuum-energy-7879-7881-7885-20260908/REVIEW_CORRECTION.md).

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are the interpretation boundary. They do not supply the Hamiltonian, its vacuum, a Born/instrument law, an energy readout, a formation rule or a physical clock. The models below are stated mathematical choices. Historical parent quotations and audit/landing language are preserved in the dated history, with no new acceptance of those parent campaigns.

## Setting and domains

For an oriented coarse graph, put one qubit on each edge. Define B_v as the product of incident Z operators and the usual explicitly reconstructed ordered-edge A_vw strings in the primary. Their supplied hopping term is T_vw=(i/2)A_vw(B_v-B_w). The added term is -J sum_v B_v. All statements concern this declared free model, not a derivation of its law or role typing from the current memo.

The exact carrier identity product_v B_v=I forces N=(V-sum_v B_v)/2 to be even. The separately constructed signed one-particle matrix M has ordered eigenvalues eps_j. At free coupling g=0 define E_N=sum_{j<=N} eps_j. This sum formula is not an interacting energy formula, and parity by itself is not a proof of a full code-to-Fock equivalence on every graph/sector.

Retain the original unrestricted functional W_all(J)=min_{N=0,...,V}(E_N+2JN). Define the constrained comparison W_even(J)=min_{N even}(E_N+2JN) separately. The latter enforces the necessary carrier parity; identifying every such state with a particular encoded sector remains conditional on its encoding. The original Wm tables evaluate W_all, with an eigensolver zero threshold1e-9 and the lowest-occupation tie representative. They are never relabeled as even-carrier tables. R1 explicitly tests both domains and their different cube threshold.

## Theorem 1 — occupancy algebra and dynamics (A1–A5, R2)

The exact Pauli checks establish B_v^2=I, pairwise B commutation, and [sum B,H_hop]=0 on each declared algebra fixture. Thus -J sum B=-JV+2JN and N is conserved. In a fixed-N sector this changes unitary evolution only by an overall phase. For any observable commuting with N the extra phase also cancels in its Heisenberg evolution.

It does not leave the channel unchanged on arbitrary even-parity states. The allowed superposition (|N=0>+|N=2>)/sqrt2 acquires relative phase exp(-4iJt); its pair-coherence expectation is cos(4Jt). R2 computes this counterexample. No physical restriction to N-diagonal readout or superselection is inferred from number conservation.

## Theorem 2 — J=0 spectra and geometry (B1–B5)

The four algebra fixtures are the open cube, the open3-by-3-by-3 block, the periodic3-by-3-by-3 graph, and the periodic4-by-4-by-4 graph. They are not all degree-six bipartite lattices. The cube has degree3; open3^3 has variable degree and V=27; periodic3^3 is nonbipartite. The spectral symmetry claim concerns the genuinely bipartite spectral fixtures only, not that odd periodic algebra test.

On a bipartite signed matrix, the spectrum is symmetric and the unrestricted minimum is reached after all strictly negative levels, with every zero-mode occupation also a minimizer. For odd V, V/2 is not an integer; floor/ceiling can tie. Carrier compatibility further intersects those occupations with even N. In the plain untwisted4^3 spectrum, the original unrestricted zero-mode interval is N=22 through42; its even subfamily is22,24,...,42.

The original cube exhaustion, uniform/twist spectra and random/structured searches remain as computed. In particular the cube staggered J=0 N=4 result and the flat4^3 N=32 construction are even and survive this correction. Claims over unenumerated sign fields are limited to the separate certificate below; sampled searches are not proofs of global selection.

## Theorem 3 — finite uniform-family comparisons (C1–C3, F1–F2)

The original tables compare plain and staggered uniform flux families and eight twists, using W_all and their stated tie convention. The finite4^3 crossing sqrt(3)/2 comes from the explicitly compared affine branches. The6^3 and8^3 crossings 0.849332 and0.867676 are numerical comparisons of those same families. They do not rule out nonuniform competitors.

Only the original L_B=224 Bloch quadrature is executed for the large-grid table. Its root is approximately0.8654029 and is compared arithmetically with the historical quoted0.8654003. The old claimed128/160/192/224 convergence sequence and +/-3e-6 uncertainty have no bound execution evidence here and are withdrawn. The original numerical tolerance around the quoted number remains a reference diagnostic, not a quadrature-error estimate. No additional grid is run to manufacture a limit.

At finite V each W is the minimum of finitely many affine functions. The chosen occupancy is piecewise constant, with tie sets at crossings. No continuously draining finite ground state or unique vacuum follows. A limiting integral is a different object, and neither it nor these two-family scans supplies a physical vacuum selector.

## Theorem 4 — emptying and the parity counterexample (C4–C5, F4, R1)

The original unrestricted one-particle endpoint thresholds remain identified: plain periodic band3, staggered band sqrt(3), open3^3 values3sqrt(2)/2 andsqrt(6)/2, and cube3/2. These are thresholds for W_all or the named continuous bands, not automatically for a finite even carrier.

For any ordered finite spectrum, the even emptying threshold is max over positive even N of -E_N/(2N), clipped below at0. At threshold N=0 may tie with positive N; above it the empty representative minimizes. R1 computes this quantity from the actual32 cube sign-sector representatives, whose gauge equivalence covers the4096 edge-sign assignments. Its maximum is (1+sqrt(2))/2, not3/2. The maximum over even N occurs at N=2 because the mean of the first N sorted levels is nondecreasing. Fixing seven spanning-tree edge signs to+1 by vertex signs leaves five free signs; those32 classes cover4096 fields. Exact characteristic polynomials give the following six classes (x is the one-particle eigenvalue):

| Count | Characteristic polynomial | Even emptying threshold |
|---|---|---|
| 1 | (x^2-3)^4 | sqrt(3)/2 |
| 1 | (x^2-9)(x^2-1)^3 | 1 |
| 3 | (x^2-1)^2(x^2-5)^2 | sqrt(5)/2 |
| 3 | (x^2-2x-1)^2(x^2+2x-1)^2 | (1+sqrt(2))/2 |
| 12 | (x^2-3)^2(x^2-2x-1)(x^2+2x-1) | (1+sqrt(2)+sqrt(3))/4 |
| 12 | (x^2-1)(x^3-x^2-5x+1)(x^3+x^2-5x-1) | less than19/16 |

For the last row, the two largest positive roots lie in(5/2,11/4) and(7/4,2), respectively, as follows from the cubic signs and root counts; their sum is less than19/4. Since19/16<(1+sqrt(2))/2, this row is not maximal. The actual R5 integer-polynomial census binds all32 represented sectors; this is a finite free-model argument, not a physical code-equivalence theorem. At J=1.4 the original plain Wm selects forbidden odd N=1 with W=-0.2, whereas the minimum over all cube sectors and even N is0. The actual even minimizer and threshold, not a raw eigenvalue bottom, are guarded.

The original all-minus versus two-flux crossing sqrt(3)-(1+sqrt(2))/2 is retained within its stated unrestricted branch comparison. Elsewhere an even-domain interpretation requires its own minimization and tie analysis; the old tables are not silently converted.

## Theorem 5 — a valid all-field lower bound (D1–D3)

On the periodic degree-six bipartite4^3 one-body graph, Tr(M^2)=6V and the negative half contributes3V to the squared spectrum. If m negative levels are occupied, Cauchy-Schwarz gives sum_occ|eps|<=sqrt(3Vm). For J>=0 a free minimizer need not occupy strictly positive levels. Therefore minimizing -sqrt(3Vm)+2Jm over real0<=m<=V/2 is a lower bound on the discrete unrestricted minimum and hence also on any restricted even-N minimum.

The relaxed value is -V sqrt(3/2)+JV for J<=sqrt(3/8), and -3V/(8J) above it; the stationary real occupation is3V/(16J^2). The relaxation is not generally an attainable integer/even occupation. The explicit flat spectrum M^2=6I at N=32 attains the first branch, so it is an actual even-N all-sign-field certificate on that interval, conditional on the declared one-body model. It does not certify the uniform-family transition near0.865.

## Theorem 6 — finite windows and the small-J integral (E1–E2, F3)

The original half-filling bisections range over only eight staggered twists. On4^3 their named windows end at4sqrt(6)-3-3sqrt(2)-sqrt(3)=0.823267 for twist optimization andsqrt(6)/2 for the fixed half-filling twist. These are W_all family comparisons with their original tie convention; they are not an all-sign-field phase window or a general even-domain result.

For the supplied gapless staggered Bloch integral, the negative band has half the site-normalized weight. Near its cone, the removed region has radius2J, giving (1/2)(4pi/3)(2J)^3/(2pi)^3=2J^3/(3pi^2), with higher-order correction O(J^5). This analytic coefficient is retained separately from the finite L224 samples. Tiny J can be below that grid's level spacing, and numerical zero levels affect the J=0 count. Those limitations prevent using the table as a certified continuum error bar.

## Corollary and interfaces

J changes an occupancy cost inside a supplied free model; it does not by itself select a unique framework vacuum. The Hamiltonian, encoded/one-body relation, allowed state/preparation, readout, response functional and physical units remain separate conditions. An empty N=0 state removes kinetic preference between sign fields but does not erase a supplied one-particle Dirac band. Fixed-number neutral pairs and charged even alternatives both remain available in their respective state domains. Historical assertions that one vacuum or one coefficient alone settles a physical gravity/formation question are retained only as provenance.

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
