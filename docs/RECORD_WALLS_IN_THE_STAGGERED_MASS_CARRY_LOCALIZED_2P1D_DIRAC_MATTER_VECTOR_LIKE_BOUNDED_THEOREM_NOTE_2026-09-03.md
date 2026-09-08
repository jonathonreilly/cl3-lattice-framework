---
claim_id: record_walls_in_the_staggered_mass_carry_localized_2p1d_dirac_matter_vector_like_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied one-particle staggered hopping on coarse 2Z^3 and named finite slabs: retain the stacking-fault/Pauli/squared-dispersion identities, sharp cutoff counts, selected wall projections, original localization fits and small resolved levels, paired finite taste coefficients and a massive dispersing line band. Cell momentum spans two coarse sites. Wall-energy decay differs from the zero-energy kernel. No exact generic zero, wall-swap proof, physical chirality/anomaly or Record-readout supplier follows."
upstream_dependencies: [minimal_axioms]
runner: scripts/record_walls_staggered_mass_localized_2p1d_matter_check_2026_09_03.py
---

# Supplied staggered mass walls: finite localized bands and projection limits

**Date:** 2026-09-03; source correction 2026-09-08
**Type:** bounded_theorem
**Audit:** unset; formal audit remains deferred by the owner.
**Status:** conditional finite-model source; no retained grade is asserted.
**Primary runner:** [record_walls_staggered_mass_localized_2p1d_matter_check_2026_09_03.py](../scripts/record_walls_staggered_mass_localized_2p1d_matter_check_2026_09_03.py)
**Runner cache:** [current source/input-bound execution](../logs/runner-cache/record_walls_staggered_mass_localized_2p1d_matter_check_2026_09_03.txt)
**Correction history:** [original claims and original cache bodies, preserved verbatim](../.claude/science/review-fixes/walls-7896-7909/REVIEW_CORRIGENDUM_2026-09-08.md).
The dated history is provenance, not an active premise or fresh receipt. The canonical cache describes its own exact source and input hashes; no old output is restamped.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional finite operator identities and explicitly bounded numerical spectra; physical suppliers remain open."
trace_class: frontier_discovery
target_claim_id: record_walls_in_the_staggered_mass_carry_localized_2p1d_dirac_matter_vector_like_bounded_theorem_note_2026-09-03
artifact_role: theorem
next_trace_action: "Independent source review of the corrected finite claims and genuine execution evidence; formal audit remains deferred."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting and authority

The [current minimal memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the ontology boundary. Physical sites are points of nearest-neighbour `Z^3`; their one-site algebra is `M_2(C)`. A site has **zero or one** permanent record. A present record locks an admissible possibility, and its readable value depends on record content. Neither a Hamiltonian, Born occupation/readout instrument, formation rule, time metric nor physical coarse hopping follows from that memo.

The [kinetic-clause comparison](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md) is used only for its displayed Kawamoto–Smit convention; its wider forcing/statistics claims are not premises here. In its declared kinetic class it writes `D=(1/2) sum eta_mu(x)(chibar_(x+mu) chi_x-chibar_x chi_(x+mu))`, with signs `eta_1=1`, `eta_2=(-1)^x1`, `eta_3=(-1)^(x1+x2)`. Here those signs and a different explicitly defined Hermitian one-particle hopping are supplied on the coarse graph. A coarse bond spans two fine sites; the effective interaction realizing it from fine nearest-neighbour physics is absent. The old #7890/#7888/#7894/#7892/#7844/#7834 pointers remain historical comparisons, not unreviewed proof suppliers.

Every matrix, boundary, mass, normalization and projection below is stipulated. Ordinary composition is used. These are one-particle calculations; no physical many-body sea, fermion measure, anomaly response or formation process is constructed. Model hypotheses are adopted conditionally; no axiom or approved primitive is adopted or changed.

## Definitions and proof dependencies

A coarse vertex `v` occupies fine position `2v`. With `eta=(1,(-1)^v1,(-1)^(v1+v2))`, set `H[w,v]=eta_a(v)` on `w=v+e_a` and its Hermitian conjugate (the supplied `t=-1` convention), and add `m(v1) eps_v` on the diagonal, `eps_v=(-1)^(v1+v2+v3)`. One fermionic coordinate per coarse vertex is supplied; no local physical encoding is derived here.

The sharp torus profile is `+m` for `x<Lx/2`, `-m` otherwise. The resolved profile is exactly the runner's product
`m tanh((Lx/2-.5-x)/w) tanh((x+.5)/w) tanh((Lx-.5-x)/w)`.
Its interpolant crosses zero between sites; no sampled zero is implied. The transverse `1x2x2` cell gives a `4Lx` matrix. Its Bloch phase crosses **two coarse sites**: `q=2 k_coarse=4 k_fine`. Velocity 1 in cell units is 2 coarse or 4 fine sites per supplied time unit. No physical time calibration is furnished.

The cell operators are `Gamma=(YII,ZYI,ZZY)`, `Eps=ZZZ`, `X=i Gamma1 Gamma2 Gamma3=-YXY`, `W=i Gamma1 Eps=-XZZ`, and `M2D=Gamma1 X=i Gamma2 Gamma3`. The taste commutant is spanned by `I` and `F=(IYX,YXI,YZX)`.

The finite definitions imply the algebra below. Spectral counts, selected-subspace projections, fits and densities then use the actual matrices. No parent campaign supplies an uncomputed step. Original groups A–E and all 22 original check IDs remain; added Q controls bind the corrected distinctions.

## T1 — stacking fault and exact cell algebra (A1–A6)

`eps_(v+ex)=-eps_v`: the sharp half-space mass reversal equals a one-coarse-site translation of the alternating diagonal on that half. Its sampled mass magnitude remains `m`. This is a conditional diagonal identity, not a formation mechanism.

`{Gamma_a,Gamma_b}=2 delta_ab I`, `{Gamma_a,Eps}=0`; X commutes with all three Gammas and anticommutes with Eps. W is Hermitian, squares to I, anticommutes with Gamma1, Eps and X, and commutes with Gamma2 and Gamma3. Direct Pauli multiplication gives these identities; all distinct-generator numerical residuals are zero. Enumeration of the 64 Pauli words gives the four-dimensional commutant just stated. Commutation alone does not determine a projected wall spectrum.

The transverse-block/direct-torus spectra agree within `1.6e-14` at L=4,6 and m=0,.5,1. At uniform mass the magnetic-cell dispersion is `E(q)^2=6+2 sum cos(q_a)+m^2`, each sign fourfold, checked within `2.8e-14` at L=4,6,8 and m=0,.5,2. The 8^3 periodic gap agrees with 2m within `9.4e-15`. These residuals are historical measured precisions; final cache residuals govern its own run.

For arbitrary supplied x profiles, transverse hopping anticommutes with the remaining terms. Thus
`H(qY,qZ)^2=H(pi,pi)^2+[4cos²(qY/2)+4cos²(qZ/2)]I`.
The two-site hopping has squared magnitude `|1+exp(iq)|²`; staggered signs cancel cross terms. The runner checks this identity directly on an independently chosen nonuniform profile. Near the node the coefficient of cell momentum is 1, with the coarse/fine conversions above.

## T2 — named counts, selected spaces, density and fits (B1–B6)

The 8x8 transverse scan at Lx32,m1 has minimum 0.414214 at (pi,pi), versus 0.870264 at the other scanned points. It is a finite grid result. For **sharp** profiles at Lx32,64 and m=.5,1,2, the complete numerical cutoff `|E|<.9m` contains eight states, split 4+4 by the half-slab indicator (worst separation .0208/.9792). In the open sharp slab the **ten lowest absolute-energy states** are classified by density in the eight-plane central window: four wall states (two at each sign), other tested states near |E|~m (1.004258 at L64,m1). This classification does not count all possible surface excitations.

`split_walls` selects the eight lowest absolute-energy states also for resolved profiles. Properties of its four-dimensional wall spaces do not constitute a full resolved in-gap census. A complete `|E|<m` count at L64,w4 gives **24** states for m1 and **72** for m2. Preserve that difference from the sharp result.

| m | Sharp amplitude-length fit | Resolved w4 fit | Zero-energy bulk kernel 2/acosh(1+m²/2) | Resolved relative difference |
|---:|---:|---:|---:|---:|
| .5 | 4.1562 | 4.1632 | 4.0410 | +3.03% |
| 1 | 2.2692 | 2.1353 | 2.0781 | +2.75% |
| 2 | 1.3854 | 1.1602 | 1.1346 | +2.26% |

The fit uses `log n(x)` for `4.5<=|x-31.5|<=14.5` and amplitude convention `xi=-2/slope`. These are distinct lengths: the uniform far-tail equation at energy E gives `E²=m²+2-2cosh(kappa)`, hence `xi(E)=2/acosh(1+(m²-E²)/2)`. At the sharp fitted E=sqrt(1+m²)-1 this is `2/asinh(m)`, matching the listed sharp fits. It differs from the zero-energy kernel by 2.85%,9.20%,22.10%; no exact common sea/wall scale is inferred from the finite resolved comparison.

Density within 4.5 coarse sites is sharp/resolved 91.9/85.2% at m.5, 99.1/96.9% at m1 and 100.0/99.8% at m2. For m1 the sharp pair-flat ratios n30/n29=1.0000 and n31/n30=5.828 contrast with resolved 1.629 and 1.304. These are normalized one-particle densities, not an implemented Record readout.

The fit of `E²-E0²` versus p² at p=.02,.04,.06,.08 along each transverse axis and diagonal gives .9997 for m=.5,1,2, both profiles. It is the small-cell-momentum coefficient with finite truncation; a massive band is not an exactly gapless cone. The squared-dispersion identity supplies the exact conditional relation; a physical Lorentz/time conclusion is absent.

## T3 — sharp fit and nonzero resolved levels (C1–C2)

| m | Sharp E at both Lx32,64 to six decimals | Resolved w4 | Resolved w8 |
|---:|---:|---:|---:|
| .25 | .030776 | 2.7e-8 | 4.2e-10 |
| .5 | .118034 | 5.2e-7 | 6.5e-12 |
| 1 | .414214 | 2.1e-5 | 5.0e-10 |
| 2 | 1.236068 | 1.2e-3 | 1.0e-6 |

The sharp values agree with the **fit** sqrt(1+m²)-1 and lie below m. Agreement between two lengths is finite-size evidence, not proof excluding every hybridization correction. Resolved profiles produce small finite levels, not exact zeros. At L64,m1,w4 the minimum is 2.132099e-5 while min sampled |m(x)|=.124352944; the smooth zero lies between planes. No exact gapless theorem or unique physical profile follows.

## T4 — direct projections and paired finite taste coefficients (D1–D4)

For the selected four-dimensional wall spaces at L64,m=.5,1,2, sharp and resolved w4, the directly computed compression of X has norm below 1e-12 (historical worst 1.4e-15). This is **not** a consequence of `{W,X}=0` alone. For the actual sharp m1 selection W leaks from one wall space with norm .70710678; X has norm .9999999997 outside both light spaces and only 2.4029e-5 between them. X does not swap the selected walls. A state of the exact cell algebra has both <W> and <X>=1/sqrt2 despite the zero anticommutator. The original purported proof is withdrawn.

The W compressions are constant to the stated tolerances and opposite between the two selected walls: sharp magnitudes .894427,.707107,.447214, resolved .989451,.974387,.939317. The sharp 1/sqrt(1+m²) expression is a fit; these noninteger expectation values are not a quantized index.

For the **sharp** L64 fixtures only, projection onto M2D and M2D F_b reconstructs the wall Hamiltonian within 1e-12 (historical 3.1e-15), with singlet coefficient below 1e-12 (historical 5.1e-20), |n| matching E_w to 1e-6 and n reversed between walls. Traceless F_b alone would not establish equal position densities. The runner checks the summed coarse-x-plane projector Pi_x = sum_(a,b) |x,a,b><x,a,b|: its compression is scalar on each selected sharp wall space, so normalized states there share the same x-plane marginal after summing the four transverse-cell coordinates. This is not equality at each individual vertex: a single coordinate projector compresses to rank at most one and cannot be a nonzero scalar on the four-dimensional wall space. This is finite paired taste structure; no regulator, sea, fermion measure or background-response calculation establishes a physical parity anomaly or its cancellation.

## T5 — massive dispersing line band (E1–E4)

Define the sampled step s_L(x)=+1 for 0<=x<L/2 and s_L(x)=-1 for L/2<=x<L. The supplied field is exactly m(x,y)=s_L(x)s_L(y), with amplitude 1 including the integer interface sites, on L=24,32 tori and a two-site z cell. At kz=pi the lowest eight absolute-energy states are degenerate to 1e-6 with minimum .317837 at both lengths (historical difference 2.2e-16), below the sharp single-wall .414214 and bulk 1. The field itself and the quoted numerical minimum are now checked; multiplying the actual field by 1.05 must fail.

The old dispersion rows remain .327745 at dk=.08 and .355761 at .16, equal at pi±dk within 1e-9. Squaring gives `H(kz)^2=H(pi)^2+4cos²(kz/2)I`, hence the positive low branch `E(pi+dk)=sqrt(E0²+4sin²(dk/2))`. Its derivative is `sin(dk)/E`, nonzero and opposite at ±.08 (about ±.24383155). Evenness sets the derivative to zero only at the minimum; the band disperses. No complete absence-of-movers or chiral-wire theorem follows.

For the resolved w3 crossing, the two measured minima are 6.5e-5 at the node and .099958 at dk=.1. Those two numbers do not classify every resolved plane or line mode. The sharp selected density is enhanced 11.2-fold within 1.5 coarse sites of the four intersection lines at L32: 17.5% on 16 of 1024 cells. Two-size agreement and density concentration retain their finite numerical scope.

## Interpretation, negative scope and executable obligations

T1–T5 are the conditional claims just stated, corresponding to original A1–E4 and the added Q controls. Their original numerical payload is also retained verbatim in the dated history. The final cache contains every old check ID with corrected labels plus the additional substantive checks; no historical PASS is used as current evidence.

A mass-sign pattern and one-particle density could be connected to records only by a separately supplied occupation/readout instrument and coarse-to-fine realization. No formation site/rate, physical clock or equation selecting the mass profile is furnished. There is no physical chiral/anomaly exclusion beyond these selected matrices and diagnostics.

N1: executed families are cell/torus algebra, sharp finite slabs, selected resolved slabs, wall projections and line fixtures; alternatives include other orientations, larger sizes/other cells, interactions, different carriers, many-body measures, and three-wall defects. They are live alternatives, not independently closed routes. N2: supplied data and projection choices overlap; no independent-wall count is asserted. N3: Hilbert space, coarse bonds, boundaries, profiles, cutoffs and time/readout are explicit hypotheses. N4: fits/residuals and finite small levels are separated from exact identities. N5: the wall-swap, anomaly and no-motion conclusions are withdrawn. N6: the positive finite algebra/localization/paired coefficients survive. N7: small selected levels and weak overlap remain useful without exact zero or physical identification. N8: historical parent repetitions supply context only, no additional authority.

No new axiom, primitive or audit verdict is applied. Formal audit remains deferred. The runner cap remains 120 seconds; no parent campaign, new production protocol or anomaly calculation is included.
