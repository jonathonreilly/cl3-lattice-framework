---
claim_id: matter_above_the_half_filled_sea_odd_and_even_densities_and_the_vacuum_question_conditional_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite real Slater, chiral, source-response and imposed-label calculations on the named tori. Fixed-number neutrality, physical readout, field zero-mode projection and even carrier parity remain distinct. Finite fits and conditional span obstructions do not prove a physical gravity or APS theorem."
upstream_dependencies: [minimal_axioms, gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11]
---
# Matter above a selected half-filled sea: number and energy source comparisons

**Date:** 2026-09-03; source correction 2026-09-08.
**Claim type:** bounded_theorem
**Status:** conditional source for independent review; no applied audit verdict.
**Primary runner:** [`scripts/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.py`](../scripts/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.py)
**Cached output:** [`logs/runner-cache/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.txt`](../logs/runner-cache/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.txt)
**Correction history:** [original bodies and the two #7881 revisions](../.claude/science/review-fixes/vacuum-energy-7879-7881-7885-20260908/REVIEW_CORRECTION.md).

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are the interpretation boundary. They do not supply the Hamiltonian, its vacuum, a Born/instrument law, an energy readout, a formation rule or a physical clock. The models below are stated mathematical choices. Historical parent quotations and audit/landing language are preserved in the dated history, with no new acceptance of those parent campaigns.

## Setting and used premises

The coarse graph is the torus of side L=4,6,8. At site v the forward hopping signs are eta_x=1, eta_y=(-1)^v_x, eta_z=(-1)^(v_x+v_y); each twist bit reverses bonds crossing that coordinate cut. The real symmetric matrix M has these nearest-neighbour entries, with hop t=1. The selected twist minimizes the sum of the lowest V/2 one-particle eigenvalues among eight twists of the supplied staggered sign field. This is a free g=0 energy sum, not an interacting spectrum or a proof of physical vacuum selection.

The source uses real occupied/empty orbitals and their real Slater projector P. For a real particle-hole change D=P'-P, define number deviation rho_v=D_vv and local row energy e_v=sum_w M_vw D_vw, so sum e=Tr(MD). This real-state restriction matters: complex orbitals can give a complex unsymmetrized row. A Hermitian local convention would require explicitly taking Re((MD)_vv); that different domain is not silently substituted in the original tables.

The edge-carrier parity dictionary is B_v=product of incident Z_e and n_v=(1-B_v)/2. Product_v B_v=I requires even N in that carrier. Definite edge-Z records, the Born expectations of a supplied coherent state, and offdiagonal hopping energy are different objects. Two states can have identical Z probabilities and energies +1 and -1 for an offdiagonal 2-by-2 hopping matrix. No physical energy-readout map is derived here.

For response we explicitly supply the finite cubic Laplacian H=-Delta, P0 removal of the constant mode, and G=H^+ with Fourier multiplier [6-2 sum cos(k_a)]^-1 away from k=0. We use only the quadratic action and zero-mode convention restated in the [current weak-field bridge](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md); its Born-density uniqueness, Green asymptotics and physical source/test-body interpretation are not inherited. This packet reconstructs the finite FFT operator. Historical coefficient/window rows are comparisons, not a newly proved infinite-distance normalization.

## Theorem 1 — the chosen sea (A1–A5)

At the selected twists the half-filled energies on L=4,6,8 are -78.383672, -258.857540, -611.811768. At L=4, M^2=6I is an integer identity and E_sea/V=-sqrt(6)/2. The finite gaps are 2sqrt(6), 2sqrt(3), 2sqrt(6-3sqrt(2)). The stated Bloch formula has a gapless point as its momentum grid becomes dense; the three finite gaps alone are not a physical Lorentz or continuum theorem.

For invertible bipartite M, Gamma M Gamma=-M implies Gamma P Gamma=I-P for the negative projector, hence P_vv=1/2. The runner checks this on each named torus. N=32,108,256 is even; that arithmetic neither makes a matter state neutral relative to the sea nor imposes the response-field projection P0.

## Theorem 2 — selected fixed-number pairs (B1–B5, R1/R3)

For orthogonal normalized h in the occupied space and p in the empty space, P'=P-|h><h|+|p><p| remains a projector of rank V/2. Therefore sum rho=0 for this preparation and sum e=E_exc. The band-edge pair has energy 2.651309 on L=8; the original real Gaussian projections at separations 1 through 4 retain their energy, negative-part and absolute-count data. The local energy need not be positive, and sum|rho| is not a two-particle counter.

Even parity permits charged alternatives: adding two empty orbitals produces another projector with even total N and delta N=+2. The actual R1 control constructs it. The original zero-total family is retained, but no claim that all matter must occur in neutral particle-hole pairs remains. Field P0 can be applied to either source and does not select a fermionic N sector. R3 gives a concrete complex-row witness explaining the stated real-source restriction.

## Theorem 3 — finite conjugation (C1–C2)

On this real chiral carrier, P' maps to Gamma(I-P')Gamma. Its number deviation changes sign and its row energy is unchanged. Every reversed link enters a face or an even-length Wilson loop an even number of times, so those bulk products stay fixed. These are finite operator identities. They do not construct an APS boundary operator or determine an independently supplied orientation label.

## Theorem 4 — finite response protocols (D1–D6)

The original L=8 source arrays are unwrapped about their chosen centroids and zero-padded into boxes Lb=8,16,32,64. Their FFT responses and cubic-star diagnostics remain unchanged. A zero-total number source has no monopole and can have a leading dipole; it can also have higher multipoles. A nonzero energy-source sum gives the tested monopole-like comparison in the finite windows. Neither description says that the field contains nothing else.

The number-source decay uses an actual log-log polynomial fit. The energy-source comparison retains the original 0.3267 reference and 0.02 amplitude band as a criterion chosen for this computation. The historical window source's separate 0.02 statement concerned fitted exponents, not this amplitude tolerance. Fixed-distance rows 0.190/0.432/0.568 and the stated Richardson combination retain their original finite-box meaning. No discretization uncertainty or infinite-volume error bound follows from these finite fits. The original D6 positive nonlinear source comparisons retain their numbers in the same chosen band; that response resemblance does not turn nonlinear postprocessing into an operator readout.

## Theorem 5 — readout clauses and actual covariance (E1–E4, R2/R4)

The linear number candidate has zero total on the selected family and need not be positive. The real hopping-energy candidate is offdiagonal in the occupation basis. Absolute-value and positive-part replacements are nonlinear in the state: the original convex-mixture witness excludes a linear operator for that postprocessing. These failures concern these candidate maps and their stated clauses, not every physical energy or Record readout.

The old translation rows are retained as naive and KS-bulk-only diagnostics. The latter omits the twist seam; its nonzero residual is not an unavoidable torus obstruction. R4 constructs the complete gauge by solving the actual translated edge equations, checks all 3072 directed edges, and checks the translated real-state energy density. The physical placement/formation problem remains distinct from this finite positive covariance result.

## Theorem 6 — imposed two-component span (F1–F2)

If the two labels are stipulated to carry the even source vector (1,1), its scalar span has least-squares distance sqrt(2) from (1,-1). The runner retains that exact finite obstruction and the particle-to-hole grading identity. Bulk holonomy invariance supplies no map to an APS eta invariant, so chi_eta is not inferred to stay fixed. Odd readouts and boundary transport remain untested alternatives.

## Corollary and interfaces

The selected sea and empty state are useful conditional comparisons. An empty N=0 Fock state gives no kinetic preference between flux fields, but the supplied one-particle M can still have its Dirac dispersion. Changing only the vacuum does not supply a source functional, force law or physical mass. Hop units, coarse coordinates, the state, its readout and response are separately declared; no physical factor-of-two map, G_Newton or absolute scale is derived.

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
