---
claim_id: native_stronger_ward_estimators_note_2026-09-10
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
proposal_allowed: false
bare_retained_allowed: false
---

# Trial-norm and spectral-residual certificates for the native Ward scalar

Claim type: bounded_theorem

Status: conditional-support; canonical assembly pending. This note extends the finite-moment hierarchy in PR8079 within the same supplied infinite native model. The completed quadratic-first-polynomial and posterior trial-norm calculations are all inconclusive. The spectral-residual theorem and runtime are source-reviewed; the accepted calculation also leaves both fixed choices inconclusive. None of these results establishes the sign or nonvanishing of alpha.

## Common premises and unchanged nominal

Use the original Gaussian reference, D_A=H0+B_A≥δ=h/4, R_A=−D_A⁻¹, g=γ0, J_A=2iγ(d_A) and J_A*J_A=j²I with j=2√2h. The fifteen two-link channels carry the disjoint-pair adjacency T of norm6. The original Ward formula is

    8α=Re(<x,Tx>−<x,Tg v>),
    x_A=R_AΩ,  v_A=R_A J_A R_AΩ.

Trial vectors are xhat_A=−p_A(D_A)Ω and vhat_A=q_A(D_A)J_Ap_A(D_A)Ω. Certified bounds E≥||x−xhat|| and F≥||v−vhat|| lead to an interval around the unchanged signed nominal. The bounds X=√15/δ and V=j√15/δ² apply to the exact vectors. No impurity-vacuum replacement, independent-residual assumption, physical-state selection, or finite-volume threshold is used.

## A posterior error bound

Let a≥||xhat|| and b≥||vhat||, and set chi=min(X,a+E), psi=min(V,b+F). Then

    |8α−What| ≤6[E(a+chi)+min(Eb+chi F,E psi+aF)].             (1)

For the quadratic term, self-adjointness of T gives the real polarization identity with x−xhat and x+xhat. Its absolute value is at most6E(a+chi). Splitting the mixed difference first around vhat and then around v gives bounds6(Eb+chi F) and6(Epsi+aF); either is valid, so their minimum is valid. The expression is monotone in every nonnegative upper-bound input. Outward upper substitutions therefore retain containment.

For constant q_A, the exact source norm s0_A=||J_Ap_A(D_A)Ω||² gives

    a²=(12s0_P+3s0_O)/(8h²),
    b²=12q_P²s0_P+3q_O²s0_O.

These quantities can be recovered from authenticated saved certificates without redoing their native moment calculations. Formula(1) changes the estimator, so the fixed-estimator all-q exclusion in8079 does not exclude this route. The completed applications to both original degree-one and degree-two first-polynomial choices remain INDETERMINATE_SIGN.

## Quadratic first-polynomial closure

At h=1 let a=e0, d=d_A, k=Ka, v=Kd, z=K²a and w=K²d in the established CAR convention. Local Clifford representatives satisfy O_iΩ=D_A^iΩ for i≤3:

    O0=1,
    O1=iγ(a)γ(d),
    O2=2−γ(k)γ(d)−γ(a)γ(v),
    O3=−2O1+2iγ(a)γ(k)+iγ(d)γ(v)−iγ(z)γ(d)
       −2iγ(k)γ(v)−iγ(a)γ(w).

O2 is not assumed Hermitian as a local polynomial. Moments are formed with actual reversed words and conjugated coefficients, e.g. m4=<O2Ω,O2Ω>, m5=<O2Ω,O3Ω>, m6=||O3Ω||². For J=2iγ(d), the commutator is [D_A,J]=−2γ(v)−8γ(a). Thus b=Jp(D)Ω and Db are explicit local Clifford vectors for quadratic p. The fixed six-vector covariance table reduces their required contractions to the same c=μ/3, ν and ω5 suppliers in8079. The full signed table, orbit contractions and domain argument are preserved as an exact imported proof, not replaced by tests or a scalar-fit assumption.

The completed degree-(2,0) protocol selected two predefined polynomials, recertified their residuals, and retained the full ninety ordered terms. Both outcomes remain inconclusive. The later posterior protocol held each p/q and nominal fixed and changed only its error estimate; both later outcomes are also inconclusive.

## Spectral residual majorants

For any self-adjoint H≥δ>0 and r∈DomH, define rho_j=<r,H^j r>, with rho2=||Hr||². For tau>0 put

    A=(tau+2δ)/(δ²tau³),
    Q_tau(λ)=(3tau−2λ)/tau³+A(λ−tau)².

The exact factorization

    Q_tau(λ)−λ⁻²
      =(λ−δ)(λ−tau)²[(tau+2δ)λ+δtau]/(δ²tau³λ²)

is nonnegative for every λ≥δ. Spectral calculus gives

    ||H⁻¹r||²≤A rho2+B rho1+C rho0,
    B=−2/tau³−2tau A,  C=3/tau²+tau²A.                       (2)

Only finite rho2 is needed; H need not be bounded above. B is negative, so a certified upper evaluation uses the lower rho1 endpoint. A negative certified upper bound contradicts the premises and must be refused, not clipped into a successful norm certificate.

For fixed degree-one p=p0+p1D, the first residual r=(1−Dp(D))Ω has coefficients(1,−p0,−p1). Its three moments are

    rho_j=Σ(i,k=0..2)c_i c_k m_(i+k+j), j=0,1,2.

The maximum vacuum moment is m6. For b=Jp(D)Ω and constant q, the inner residual t=(1−qD)b has

    xi_j=s_j−2q s_(j+1)+q²s_(j+2), j=0,1,2,

requiring s0 through s4. The established degree-one source closure supplies b,Db,D²b on the same six vectors, so no new spatial covariance or seventh half-moment is introduced. These finite local vectors meet the required domains.

Let u_A and v_A bound the inverse norms of these first and inner residuals using(2). The inner trial error still obeys

    ||D_A⁻¹J_A D_A⁻¹Ω−q_AJ_Ap_A(D_A)Ω||
      ≤(j/δ)u_A+v_A.

The operator gap remains in the first term. It is not silently replaced by a known local residual. Consequently E_new²=Σu_A² and F_new²=Σ[(j/δ)u_A+v_A]² can be used in(1) without changing the original nominal.

## One bounded parameter proposal

Writing z=1/tau turns the right side of(2) into rho0/δ²+B0 z+C0 z²+D0 z³, where

    B0=2rho0/δ−2rho1/δ²,
    C0=3rho0−4rho1/δ+rho2/δ²,
    D0=2rho2/δ−2rho1.

For exact physical moments B0≤0 and D0≥0. The degenerate case is a measure supported atδ, where every tau gives the exact gap bound. Otherwise B0<0,D0>0 and the unique positive critical point is the global minimum. Its parameter is

    tau*=(sqrt(C0²−3D0B0)+C0)/(−B0).

For C0<0 the equivalent expression3D0/(sqrt(C0²−3D0B0)−C0) avoids cancellation. The derivative at z=1/δ equals(8/δ³)∫(λ−δ)²dμ>0, so tau*>δ.

The runtime does not certify that its midpoint proposal is this exact optimum. It computes one bounded dyadic proposal, clamps/rounds it by the frozen rule, and reevaluates it with the original intervals. Inconsistent or oversized midpoint proposals fall back to the already present tau1. The original fixed tau set{1,2,4,8,16} and gap bound remain. No extra search or moment acquisition occurs; no numerical improvement follows merely from this rule.

## Prospective spectral computation and status boundary

The spectral runtime reuses m0..m6 from the completed degree20 event records and s0..s2,p/q/nominal from the completed degree10 records. It checks exact scalar-family identity and repeated vacuum-moment copies. Only s3 and s4 are newly evaluated, for each original class/mode. All moment contractions, candidate bounds, refusals and selected error components are retained before gates. The fixed30-second/384MiB contract is a resource ceiling, not a prediction of sign closure.

Spectral execution status: ACCEPTED, BOTH INDETERMINATE_SIGN. The exact source and review hashes are in the packet inventory; the completed receipts stay separate from preserved preactivation runtime metadata. Canonical review, integration, citation graph, changed-audit readiness and formal audit remain separate obligations. The full native alpha remains open.

## Accepted spectral outcome

The new spectral estimator completed once under its 30-second contract, in 1.87 seconds externally with a sampled whole-tree peak of 122,683,392 bytes. Both fixed polynomial choices remain INDETERMINATE_SIGN. The reported residual-mode error bound is approximately 6243.67 and the variational-mode bound approximately 6511.72. These are estimator improvements, not a sign certificate. The root checked the residual-majorant and posterior arithmetic while explicitly inheriting the new s3/s4 Wick identities; the compact supporting checker validates that exact receipt boundary without replaying the 588-event computation.
