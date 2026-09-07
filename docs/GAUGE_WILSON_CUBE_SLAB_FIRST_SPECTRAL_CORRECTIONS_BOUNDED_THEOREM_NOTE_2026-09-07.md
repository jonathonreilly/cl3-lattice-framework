---
claim_id: gauge_wilson_cube_slab_first_spectral_corrections_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/gauge_wilson_cube_slab_first_spectral_corrections_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_cube_slab_exact_covariance_central_gaussian_spectrum_bounded_theorem_note_2026-09-07
  - gauge_wilson_cube_slab_two_source_cubic_cancellation_rate_bounded_theorem_note_2026-09-07
claim_scope: "Exact first relative corrections of the first two central eigenbranches of the supplied finite SU3 cube slab under weak-coupling dilation; no finite onset or physical gap identification."
---

# Actual cube slab: first two spectral corrections

**Type:** bounded_theorem

For the supplied finite SU(3) cube slab A_beta=D_beta/D_00, the first two central eigenvalues have

    beta^-4 ell_j(A_beta)=lambda_j[1+k_j/beta+o(beta^-1)], j=0,1,
    lambda_1/lambda_0=theta²,
    theta=(32-3sqrt(55))/23,
    k0=126839623/20482880+27961081 sqrt(55)/27931200,
    k1=137812123/20482880+27961081 sqrt(55)/18620800.

Consequently ell_1/ell_0=theta²[1+delta/beta+o(beta^-1)], where delta=49875/93104+27961081 sqrt(55)/55862400 is strictly positive. These are actual finite-slab asymptotic coefficients, computed without an eigenvalue fit.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

The [exact covariance and central spectrum parent](GAUGE_WILSON_CUBE_SLAB_EXACT_COVARIANCE_CENTRAL_GAUSSIAN_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the original 32 links, 16 vertices, two omitted source faces, 22 retained weights, central Haar normalization and isolated eigenbranches. The [two-source cancellation parent](GAUGE_WILSON_CUBE_SLAB_TWO_SOURCE_CUBIC_CANCELLATION_RATE_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the whole-kernel first-order cancellation and chart estimates. Its structural input is the [nonlinear dilated-kernel theorem](GAUGE_WILSON_CUBE_SLAB_NONLINEAR_SADDLE_DILATED_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-07.md). None of these supplied Wilson/Gibbs/central-compression premises is derived from minimal Record axioms here.

The [primary exact runner](../scripts/gauge_wilson_cube_slab_first_spectral_corrections_2026_09_07.py) reconstructs a distinct adapted tree, all face words and explicit color matrices, then computes both branches with scalar covariance derivatives. It performs 23 actual assertions. The [independent ground helper](../scripts/gauge_wilson_cube_slab_first_ground_correction_independent_check_2026_09_07.py) uses the other adapted tree and rational-field implementation, with seven assertions including its positive resource guard. Both are self-contained; neither consumes saved result JSON. Supporting frozen matrix-word tests and the orbital independent derivative computation remain in the evidence packet. Different per-tree Taylor pieces agree only after assembling the gauge-invariant normalized coefficient.

## Third-derivative estimate and spectral justification

Write epsilon=beta^-1/2. Use nested, star-shaped product exponential-coordinate balls and a smooth cutoff equal to one on the smaller ball. Flatness and the positive Hessian imply E(X)>=c|X|² there; the compact complement has a positive action gap. The Hessian integral formula gives

    E(epsilon z)/epsilon² = integral_0^1 (1-t) D²E(t epsilon z)[z,z] dt.

Its r-th epsilon derivative for r<=3 is bounded by C_r |z|^(r+2), since the action has bounded derivatives through order five on the larger ball. At every intermediate epsilon for which the cutoff is nonzero the exponential is bounded by exp(-c|z|²). The product rule for exp[-E(epsilon z)/epsilon²] therefore bounds its third derivative by a fixed polynomial of degree at most nine times this Gaussian. Derivatives of the smooth cutoff and Haar factors contribute further fixed polynomial factors. On their support the same quadratic estimate holds; cutoff boundaries can equivalently be isolated as exponentially small chart tails. Taylor's integral remainder then gives O(epsilon³) in the full Gaussian-weighted integrable norm, and after integrating the 120 nuisance coordinates also in the two-source weighted L2 norm. The derivatives at zero are the actual ordered action polynomials E3,E4 and Haar quadratic coefficient. Integration of a polynomial times a joint positive Gaussian leaves a polynomial-Gaussian source envelope. Off-chart terms, even after normalization and dilation powers of beta, are exponentially small.

The positive partition normalization has the same expansion; its leading value is nonzero. Source square-root Jacobians are smooth and positive on the chart. Division preserves the L2 expansion. Independent angular averaging is a contraction. The cancellation parent makes the entire epsilon marginal zero, including arbitrary fixed source vectors. Thus the common-space central operators obey K_beta=K0+epsilon² K2+O(epsilon³) in Hilbert-Schmidt, hence operator norm. The actual finite-group operator and its chart compression differ by an exponentially small term under the parent estimates.

For each simple isolated branch, norm perturbation and its spectral gap give a normalized eigenvector phi_epsilon=phi+O(epsilon²), with the phase fixed by positive overlap. Taking the eigenvalue equation against phi yields lambda_epsilon=lambda+epsilon²<phi,K2 phi>+o(epsilon²). A would-be first-order resolvent correction is absent because the entire epsilon operator is zero; vanishing only its diagonal expectation would not suffice. The two relevant central Mehler branches are simple by the invariant-polynomial degree classification in the spectrum parent.


# Independent adapted-tree reproduction of the first actual ground correction

This calculation was preregistered and executed before reading native's correction coefficients. It uses a different adapted spanning tree and independently expands the22 ordered face words. The exact agreement is a nontrivial gauge-coordinate control, not a repeated evaluation of the same source.

## Distinct adapted gauge and local fields

The tree is [0,20,1,4,23,5,31,30,29,27,26,19,18,11,9] in the frozen lex-vertex/axis edge enumeration. It contains three edges of each source square, omitting the x edge at y1 rather than native's y edge at x0. Reverse-edge greedy extension completes the tree. Both source loops are literal chord variables up to inverse signs; the two ground functions and source Haar terms are invariant under inversion and conjugation. Changing the adapted tree can align color frames differently, but it does not change these actual central source integrals.

Let H=B^TWB and use Tr(TaTb)=delta_ab. Expanding the actual Wilson action gives E2=z^THz/6 per color, E3 and E4 from ordered matrix products, not commuting holonomies. The partition covariance is G0=3H^-1. The normalized limiting ground function is proportional to exp[-omega TrX²/2], omega=sqrt55/90. Its two source factors add omega times the source-coordinate projector to the precision, giving Gg=(H/3+omega Psource)^-1. Exact inversion and the unchanged2-source covariance are checked independently.

## Independent color and word calculation

Using explicit trace-orthonormal Gell-Mann matrices, define F_abc=ImTr(TaTbTc). The matrix calculation gives sumF²=12. It also gives the three fourth trace contractions64/3,-8/3,64/3. Consequently

    E Tr(Xe Xf Xg Xh)
      =(64/3)(Gef Ggh+Geh Gfg)−(8/3)Geg Gfh.

For each face, enumerate every degree-four composition among its ordered exponential factors. Its coefficient is minus the face weight divided by3, multiplied by orientation signs and inverse exponential factorials. These are kept per face and per ordered word. The middle Wick contraction is negative and cannot be dropped as an Abelian simplification.

Every ordered three-distinct-factor choice contributes -weight/3 times its sign to F(Xe,Xf,Xg). Sorting the edge triple contributes the corresponding alternating parity. Repeated-factor cubic real traces vanish. If q_I are these coefficients, then

    E E3² =12 sum_(I,J) q_I q_J det G[I,J].

Within-triple Wick contractions vanish against F. The six cross-pairings give the determinant with their alternating signs. All cross-face terms are retained; the raw22-by22 face-pair matrix is part of result.json. This convention is independently related to native's f' by F=f'/2, so12 corresponds to48/4 rather than a conflicting color normalization.

## Haar and kernel normalization

The local Haar Jacobian satisfies

    log(j(X)/j0)=−sum_(positive roots) alpha(X)²/12+O(|X|4)
               =−TrX²/4+O(|X|4).

For a traceless diagonal X, sum_(i<j)(lambda_i−lambda_j)²=3sum_i lambda_i², establishing the coefficient. Since ETrXe²=8Gee, the product Haar insertion is−2TrG. The source-kernel local unitary contributes reciprocal square roots of its two source Haar densities; their second-order insertion is +(TrXu²+TrXv²)/8, whose expectation is Guu+Gvv. Omitting it would compute a different, non-unitarily normalized matrix element.

Thus, with R=E3²/2−E4,

    Z1=E_G0 R−2TrG0,
    Ng1=E_Gg R−2TrGg+Gg_uu+Gg_vv,
    k0=Ng1−Z1.

The ground Gaussian integral is normalized when taking these expectations: its leading factor cancels against the actual Gaussian ground eigenvalue. In the one-group control, G=3 gives E E4=−5 and Haar=−6, hence Z1=−1. This control independently fixes both action and Haar conventions.

## Analytic interface, including the missing-resolvent issue

The separately reviewed two-source cancellation theorem makes the WHOLE first epsilon kernel coefficient vanish, not just its ground expectation. This matters: otherwise a second-order eigenvalue correction could contain a first-order-kernel resolvent contribution even when the first ground expectation vanishes.

With epsilon=beta^-1/2, the Hessian-integral Taylor representation of E(epsilon z)/epsilon² can be differentiated three times on a small star-shaped chart. Bounded fifth action derivatives and third cutoff/Haar derivatives give a fixed polynomial times Gaussian bound for the third epsilon derivative. Taylor expansion through epsilon² is therefore valid in weighted marginal L2 with remainder O(epsilon³); compact complements are exponentially negligible. Dividing by the partition and source square-root densities preserves this expansion. It yields K_beta=K0+beta^-1 K2+o(beta^-1) in operator norm as well as Hilbert-Schmidt norm.

The ground is simple and isolated, so its eigenvalue correction is the Rayleigh insertion <phi,K2phi>, with no first-order-kernel term. The same exponentially small off-chart estimate transfers this coefficient to the actual finite supplied group operator. Therefore

    beta^-4 ell0(A_beta)=lambda0[1+k0/beta+o(beta^-1)].

This is a coordinate-dilated statement; no fixed-group operator expansion or finite-beta onset is implied.

## Frozen result and distinct-tree agreement

The independent results are

    Z1=1444313/38720,
    Ng1=1012365/23276+(27961081/27931200)sqrt55,
    k0=126839623/20482880+(27961081/27931200)sqrt55 >0.

Both rational coefficients of k0 are positive. The result is not inferred from a numerical eigenvalue fit.

Our partition components are

    E E3²=4401207/3520,
    E E4=24786923/77440,
    Haar=−29457/110.

Native's different tree instead gives1439937/880,19686973/38720,−1362/5 respectively. These DIFFER individually, while their normalized sum agrees exactly. Ground bulk and source-half correction likewise combine to the identical coefficient. This is expected: coordinate-dependent Taylor pieces need not be gauge invariant separately, but the actual normalized central integral is.

The independent source and raw receipt were frozen before reading native's result. All matrices, per-face quartics, cross-face cubic covariance, mutations and full exact field values remain in result.json. Dropping cross-face covariance, the middle noncommuting quartic pairing, Haar or the active source half-density has a recorded nonzero effect. The partition source-half term is correctly inactive, not counted as a failed mutation. That ground-only calculation by itself supplies no ratio correction; the separate radial insertion below supplies it. Neither calculation claims physical coupling selection, a thermodynamic result or numerical accuracy at beta=6.

# Independent alternative-tree first excited correction

The preregistration and result hashes record the order of this calculation. Candidate numbers had already arrived unsolicited in an agent message; this is an independent implementation and gauge-tree check, not a blind-to-values experiment. Neither the orbital jet source nor its result was read before this result froze. The sole computational input is our previously frozen alternative-tree ground raw data, including independently derived SU(3) color traces and ordered face words.

Let Q(X)=Tr X², omega=sqrt(55)/90 and theta=(32-3sqrt(55))/23. The limiting eight-dimensional Mehler ground is phi0 proportional to exp(-omega Q/2). Its first nonconstant conjugation-invariant eigenfunction is phi1=(4-omega Q)phi0. Under phi0², omega Q has mean4 and variance4; thus this state is orthogonal to the ground, has four times its squared norm, and is the sole invariant degree-two branch. Its eigenvalue is lambda0 theta².

With two source penalties a,b, define G=(H/3+2aP_u+2bP_v)^-1 and Gamma the unnormalized 136-dimensional Gaussian integral. There are eight independent color coordinates. Consequently logGamma_a=-8Guu, logGamma_b=-8Gvv, logGamma_ab=16Guv². Direct differentiation of the inverse gives Ga=-2GPuG, Gb=-2GPvG and Gab=4(GPuGPvG+GPvGPuG).

The polynomial entering the normalized source kernel is K=E_G(E3²/2-E4)-2TrG+Guu+Gvv. The last two entries restore the source half-Haar densities; omitting them before differentiation changes the excited answer. In the program K is assembled into actual scalar monomials of symmetric covariance entries. The cubic variance is expanded into the six permutations of each determinant, quartic words into the three independently computed color pairings. Every monomial is differentiated by the elementary product rule, retaining both distinct-factor mixed terms and each same-factor Gab term. This differs from the orbital four-component jet implementation. The exact inverse derivative equations and a separately symbolic two-by-two source covariance calculation validate these derivatives.

At a=b=omega/2 write la=logGamma_a, lb=logGamma_b and lab=logGamma_ab. The two radial insertions act by D=(4+omega partial_a)(4+omega partial_b). Thus

    d=D Gamma/Gamma=16+4omega(la+lb)+omega²(la lb+lab)=4theta²,
    D(Gamma K)/Gamma=d K+(4omega+omega² lb)Ka
                           +(4omega+omega² la)Kb+omega² Kab.

The partition coefficient is independent of a,b. It follows that k1=D(Gamma K)/(D Gamma)-Z1, while k0=K-Z1. Exact arithmetic on the alternative tree gives

    k0 = 126839623/20482880 + 27961081 sqrt(55)/27931200,
    k1 = 137812123/20482880 + 27961081 sqrt(55)/18620800,
    k1-k0 = 49875/93104 + 27961081 sqrt(55)/55862400 > 0.

All coefficients, 17-by-17 covariance derivatives, monomials and Gaussian normalization derivatives are retained in result.json. The existing ground coefficient is reproduced exactly, rather than inserted as an expectation. Ten actual named controls pass in 4.18 seconds at 65.69 MiB.

For the actual spectral conclusion, use the separately reviewed common Hilbert-Schmidt kernel expansion through epsilon², with epsilon=beta^-1/2. Its whole epsilon coefficient vanishes. Hence the usual first perturbation of each isolated simple eigenbranch at order epsilon² is its diagonal matrix element; there is no resolvent term made from an epsilon-order perturbation. The limiting invariant ground and degree-two branches are simple and separated. Therefore the actual first/top ratio has expansion theta²[1+(k1-k0)/beta+o(beta^-1)]. The positive coefficient gives eventual approach from above at this asymptotic order; it supplies neither monotonicity, an explicit onset, beta=6 accuracy, nor a physical gap identification. This argument relies on whole-kernel cancellation, not merely a zero ground expectation.

After freezing these raw data, the orbital derivation and actual result were opened. Their independently differentiated coefficients agree exactly despite the different adapted spanning tree and differing intermediate Wick pieces. The comparison receipt binds both raw files and checks symbolic equality of k0, k1 and the relative difference.


## Scope and evidence protocol

The exact matrix calculations certify the finite algebra, not the infinite-dimensional analytic estimates by sampling. The latter are proved above and in the explicit parents. Native code, Wilson action, group Haar measure, marked central source map, finite geometry and weak-coupling limit remain fixed supplied model premises. No dynamical Record-formation law, coupling selection, full interacting theory, thermodynamic limit or physical mass-gap identification follows. The positive delta gives an eventual asymptotic approach from above, with no monotonicity, explicit threshold or beta=6 accuracy assertion.

Negative-language controls: N1 fixes the original finite source map; N2 keeps the two marked faces and all 22 weights; N3 forbids a commuting-holonomy replacement; N4 retains all cross-face cubic correlations; N5 reports actual per-element, per-mode, per-block and finite-lattice counts; N6 binds the source half-Haar normalization; N7 distinguishes whole-kernel cancellation from a ground-only cancellation; N8 preserves failed controls and the candidate-values disclosure. These are scope checks, not a universal impossibility theorem.
