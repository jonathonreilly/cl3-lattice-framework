---
claim_id: native_finite_moment_ward_note_2026-09-10
claim_type: bounded_theorem
claim_scope: "Finite-moment Ward error bounds, exclusion of two fixed first-polynomial certificate families, and a certified fifth half-moment supplier in the supplied native model."
upstream_dependencies:
  - native_ward_direct_overlap_note_2026-09-10
  - native_finite_excitation_ward_note_2026-09-09
runner: scripts/native_finite_moment_ward_2026_09_10.py
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
bare_retained_allowed: false
---

# Finite moments for the native Ward scalar

Claim type: bounded_theorem

**Status: conditional-support; canonical proof review PASS; affected runner review pending.** Two completed degree-(1,0) certificates are inconclusive. A separate saved-data certificate proves that increasing the second polynomial alone cannot make either fixed first-polynomial certificate pass its unchanged error test. A new positive-integral certificate supplies the fifth half-moment needed by a different, higher-first-degree route. None of these statements determines the sign or nonvanishing of the physical node scalar.

Use the original supplied infinite Gaussian reference, CAR and normalization of the [direct overlap note](NATIVE_WARD_DIRECT_OVERLAP_NOTE_2026-09-10.md) and [bounded Ward theorem](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md). In particular D_A=H0+B_A≥δ=h/4, R_A=−D_A⁻¹, g=γ0 and J_A=2iγ(d_A), with J_A*J_A=8h²I. There are fifteen two-link defects and ninety ordered disjoint pairs. The disjoint-pair adjacency T has norm6. The exact identity is

    8α = <x,Tx> − Re<x,Tg v>,
    x_A=R_AΩ,   v_A=R_A J_A R_AΩ.

The reference constant c=<B_A>=μ/3 is not the impurity ground-energy shift. All local formulas below use h=1; restoring units gives α in h⁻².

## A computable residual certificate

Choose real polynomials p_A and q_A. Put uhat_A=p_A(D_A)Ω, xhat_A=−uhat_A, b_A=J_A uhat_A and vhat_A=q_A(D_A)b_A. Define certified nonnegative residual bounds

    r_A ≥ ||(1−D_A p_A(D_A))Ω||,
    t_A ≥ ||b_A−D_A vhat_A||,
    e_A=r_A/δ,   f_A=(j e_A+t_A)/δ,   j=2√2h.

Coercivity gives ||x−xhat||≤E=||e|| and ||v−vhat||≤F=||f||. Also ||x||≤X=√15/δ and ||v||≤V=j√15/δ². Expanding the two quadratic expressions, using ||T||=6 and ||g||=1, proves

    |8α−What| ≤ 6[E(2X+E)+EV+(X+E)F],
    What=<xhat,T xhat>−Re<xhat,Tg vhat>.

This retains the original boundary sources. It makes no impurity-vacuum replacement. A strict sign conclusion requires the entire nominal interval to exceed the certified error interval in magnitude.

Finite polynomial residuals reduce to finite vacuum moments and Wick contractions. The complete local derivations, including domain and convergence premises, are preserved in the packet's HIERARCHY.md and DEGREE10.md. For degree-one p, the vacuum moments m0 through m4 are respectively

    P: 1, c, 2, 10c, 20+36c²−2cν/3,
    O: 1, c, 2, 4c+ν/3, 22+4cν/3.

The two fixed choices solve either the residual normal equations (m2 m3; m3 m4)p=(m1,m2), or the variational equations (m1 m2; m2 m3)p=(m0,m1). The actual interval residuals are checked afterward. There is no fitted choice based on the eventual sign.

## Why a higher second degree does not repair the two completed tests

Fix one tested p family and let a=||xhat||. Since J_A*J_A=j²I, ||b||=ja exactly. For any domain vector vhat, let T_res bound ||b−D vhat||. Then ||vhat||≤(ja+T_res)/δ and

    |What| ≤ 6[a²(1+j/δ)+a T_res/δ].

The same reported error satisfies F≥T_res/δ. Set C=E(2X+E+V). Because a≤X+E, subtraction yields

    |What|−Error ≤ 6[a²(1+j/δ)−C].

Thus C≥a²(1+j/δ) excludes both strict sign gates for every second polynomial, with this fixed p and this error estimator. Equality also excludes a strict gate. This is a quantified certificate-family limitation, not a physical no-go.

The saved source norms give a²=(12s0P+3s0O)/8 at h=1. The separate screen uses lower endpoints for C and upper endpoints for a²(1+8√2). Both completed fixed modes satisfy that sufficient inequality. The original degree-(1,0) run itself remained INDETERMINATE_SIGN; the subsequent screen, using only saved E and s0 intervals, returned CERTIFICATE_FAMILY_EXCLUDED for both modes. Neither completed calculation was replayed in this package.

## The new fifth half-moment supplier

Write X=6−2Σcosθ in the canonical dispersion, A(t)=E[(X+t²)⁻¹], M1=6, M2=42, and ω5=E[X^(5/2)]. Tonelli and polynomial division give

    ω5=(2/π)∫₀∞Q5(t)dt,
    Q5(t)=E[X³/(X+t²)]=42−6t²+t⁴−t⁶A(t).

The existing catalog has1742 Gauss nodes and3484 endpoint oracle evaluations, each returning A and A′. No new oracle was called for ω5. On a dyadic panel[a,2a], the rho4 ellipse is z/a=3/2+(17/16)cosθ+i(15/16)sinθ. Since (3/2)²−(17/16)²−(15/16)²=31/128>0, Re z>|Im z| and Re z²>0. Therefore |Q5(z)|≤EX²=42, with analytic domination. Degree51 exactness of Gauss26 and the Chebyshev tail bound give panel radius (16/3)a M4⁻⁵². Summing the67 panels from2⁻⁶⁴ to8 gives radius below1792·4⁻⁵²; the implemented certificate conservatively uses1904·4⁻⁵².

At ε=2⁻⁶⁴, L=42ε−2ε³+ε⁵/5 and the low integral lies in [L−(17/60)ε⁷/7,L]. The correction has negative sign. At t≥8, forty terms give

    Σ(n=0..39)(−1)^n M(n+3)/[(2n+1)8^(2n+1)],

with nonnegative remainder at most M43/(81·8⁸¹). Exact phase multinomials provide those integer moments; directed input and arithmetic intervals, Machin π bounds, and all low/middle/high pieces remain separate in the saved output. The accepted full width is below the predefined10⁻²⁴ target. The root's saved reconciliation covers all1742 node and tail arithmetic steps; this package reuses that certificate rather than replaying it.

This supplier enables different first-polynomial routes. For example the reviewed degree-(2,0) algebra uses O_iΩ=D^iΩ through i=3, with O2 generally not Hermitian as a local polynomial. Moments must use O_i*O_j with actual reversed words and conjugated coefficients. The required sixth vacuum moment and cubic-source contractions close on c,ν,ω5. That is a source theorem and prospective implementation boundary; no higher-degree numerical outcome is claimed here.

## Evidence and remaining work

The packet copies exact original results, receipts, proof sources and an original-to-local hash map. Original NOT_EXECUTED wording in historical derivations records their prelaunch status; current execution claims derive only from the separately copied accepted receipts. The compact runner checks identity controls and preserved result structure only. It does not invoke a native solver, oracle, catalog integrand, or saved full-node reconstruction.

Independent constituent checks do not replace independent review of this assembled note. Parent canonical proof review is PASS on the conditional scope. Affected runner review, full integration pipeline, changed-audit readiness, citation graph and formal audit remain unrun or pending. The full α remains open. The appropriate next test changes the first polynomial or proves a sharper state-dependent error estimate; rerunning the excluded fixed-p family is not justified by a higher second degree alone.
