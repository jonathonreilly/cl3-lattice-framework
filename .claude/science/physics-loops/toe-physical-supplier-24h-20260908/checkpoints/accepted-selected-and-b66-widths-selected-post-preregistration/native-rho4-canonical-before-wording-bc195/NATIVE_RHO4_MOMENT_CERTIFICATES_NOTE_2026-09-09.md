---
claim_id: native_rho4_moment_certificates_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied infinite native Gaussian dispersion and authenticated scalar catalog: completed rho4/40-term cminus, mu and nu interval certificates, with independent full saved-node reconciliation."
upstream_dependencies:
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
  - native_certified_local_green_scalars_note_2026-09-09
runner: scripts/native_rho4_moment_certificates_2026_09_09.py
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
bare_retained_allowed: false
---

# Three certified native moments from an unchanged Green catalog

**Claim type: bounded_theorem.** Under the supplied [native dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md), normalized torus measure and authenticated interval-input premises below, the exact saved intervals contain cminus=E[X^(-1/2)], mu=E[sqrt(X)] and nu=E[X^(3/2)]. The completed new cminus and mu intervals each have full width below 2e-28. The nu interval has full width below 2e-19. Each is also independently reconciled against all 1742 saved quadrature-node contributions. These are supplied-model scalar bounds, not a physical selection of that model.

Original source reviews passed. This canonical assembly awaits independent source review and root integration; integration and formal audit are **NOT RUN**. This note does not rerun an integral or saved-node checker. Its [compact runner](../scripts/native_rho4_moment_certificates_2026_09_09.py) checks saved endpoints, acceptance bindings and supporting exact identities. Hash checks and finite controls alone do not prove containment: the analytic argument, input enclosures and authenticated completed implementations are load-bearing.

## Model, inputs and exact result

Work first at h=1, X=4 sum sin²(k_a)=6-2 sum cos(theta_a), with normalized independent phases. Then 0<=X<=12, E X=6 and E X²=42. The theta formulation absorbs the covering multiplicity; it does not multiply a torus expectation by eight. The [prior scalar note](NATIVE_CERTIFIED_LOCAL_GREEN_SCALARS_NOTE_2026-09-09.md) fixes A(t)=E[(X+t²)^(-1)] and the mathematical elliptic identity used by the accepted A oracle. That imported identity remains an explicit mathematical premise; no new elliptic evaluation or new A/root/weight oracle was made in these three contractions.

The fixed catalog has 67 panels [a,2a], a=2^j, j=-64,...,2, and 26 Gauss nodes per panel. Accepted interval root brackets and positive mapped weights enclose the exact Gauss rule. The successful repaired input contract uses mapped-weight width<=1e-38, total upper weight<=9, node width<=2^-140 and A endpoint width<=1e-30. Endpoint monotonicity yields an A-at-node interval; its width is checked, not inferred from a bit label. The older failed tighter mapped-weight assumption is not used. A0=E[1/X]<=17/60 is an explicit inherited analytic bound. All physical scalar inputs are the same authenticated catalog; no old cache midpoint is silently recentered.

Authoritative rational endpoints are the three rows in the [local scalar records](../.claude/science/physics-loops/native-rho4-moment-certificates-20260909/verification/SCALARS.json), mapped to byte-identical original RESULT files by the recovery manifest. Readable comparisons, checked as exact rational inequalities by the runner, are:

* 0.4553440516444301 < cminus < 0.4553440516444302; full width < 8e-31.
* 2.387 <= mu <= 2.389; full width < 3e-30.
* 15.645 <= nu <= 15.647; full width < 2e-29.

The nu bound exceeds its preregistered precision target; no target was changed after inspection. These coarse decimal displays are not substituted into downstream calculations. For X_h=h²X, cminus_h=h^-1 cminus, mu_h=h mu, nu_h=h³ nu. None of these results alone establishes a Gram frame, small leakage, propagation accuracy or a value/sign of node alpha.

## Positive identities and endpoint regularity

For x>0, integral_0^infinity dt/(x+t²)=pi/(2sqrt(x)). Nonnegative Tonelli integration gives

    cminus=(2/pi) integral A(t) dt,
    mu=(2/pi) integral [1-t²A(t)] dt,
    nu=(2/pi) integral [6-t²+t⁴A(t)] dt.

The integrands are respectively E[1/(X+t²)], E[X/(X+t²)] and E[X²/(X+t²)]. The last polynomial follows exact division, not an asymptotic fit. The zero of X has measure zero; local quadratic dispersion in three dimensions makes E[X^-1] finite and therefore also E[X^-1/2] finite. Finite positive moments are immediate from X<=12.

For the sharper low cminus bound one needs -A'(t)<=3 for 0<t<=1. Here is a direct estimate independent of elliptic differentiation. Set x_a=2sin(theta_a/2); then X=|x|² and density f(x)=(2pi)^-3 product(1-x_a²/4)^-1/2 on [-2,2]^3. On |x|<=1, 0<=f-f0<=f0|x|²/6: product(1-x_a²/4)>=1-|x|²/4 and the convex secant coefficient 2/sqrt(3)-1<=1/6. For -A'=2t integral f/(|x|²+t²)², the constant-density ball term is at most 1/(4pi), the density correction at most t/(6pi²), and the exterior term at most 2t. Thus -A'<=1/(4pi)+1/(6pi²)+2<3. For t>=1, the simpler 2/t³<=2 suffices. Differentiation for t>0 is dominated locally. This justifies the low endpoint estimate without differentiating an unspecified remainder.

## Why the same Gauss nodes support a stronger rho=4 bound

The Bernstein ellipse for [a,2a] at rho=4 is

    z/a=3/2+(17/16)cos(theta)+i(15/16)sin(theta).

Its real part u satisfies u-|v|>=3/2-sqrt(514)/16>0, since 9/4-514/256=31/128>0. The interior also lies in this convex cone. Hence Re z²>0 and |X+z²|>=X. Holomorphic dominated integration on compact subsets gives uniform bounds M=A0<=17/60 for A(z), M=1 for E[X/(X+z²)], and M=6 for E[X²/(X+z²)]. The A bound uses the integrable majorant 1/X; the measure-zero node causes no complex singularity on these contours.

An analytic function bounded by M on the ellipse has Chebyshev coefficients |c_k|<=2M rho^-k. The degree-51 truncation error is <=2M rho^-52/(1-rho^-1). Both integration on a length-a panel and the positive Gauss26 functional have norm a and agree on degree<=51. Their difference is at most 4aM rho^-52/(1-rho^-1). Summing a<8 at rho=4 gives the following absolute quadrature radii:

    R_c=(544/45)4^-52, R_mu=(128/3)4^-52, R_nu=256*4^-52.

These apply to the exact rule. Interval node/weight uncertainty and arithmetic are separately enclosed; they are not absorbed into this analytic radius. Reusing an old rule does not require reusing its older, weaker ellipse error estimate. The new certificate protocols also change the tail order and cminus low interval; they do not relabel an unchanged earlier run.

## Low intervals and exactly forty high terms

Let eps=2^-64. For nu, exact subtraction gives

    6eps-eps³/3 <= integral_0^eps Q_nu
       <=6eps-eps³/3+(17/60)eps^5/5.

For mu the low interval is [eps-(17/60)eps³/3,eps]. Let [t_lo,t_hi] be the authenticated first Gauss node, eps<t_lo<t_hi<2eps, and [a_lo,a_hi] its enclosing A interval. Monotonicity gives A(t)>=a_lo for t<=eps, while the derivative estimate gives A0<=a_hi+3t_hi. Thus the new cminus low interval is [eps*a_lo,eps*(a_hi+3t_hi)]. This is a bound from an existing node, not a new A0 oracle or extrapolated value.

For t>=8 use the finite geometric identity with exactly40 terms. If the numerator is X^q, q=0,1,2, then

    X^q/(X+t²)=sum_(n=0)^39 (-1)^n X^(n+q)/t^(2n+2)
                      + X^(40+q)/(t^80(X+t²)).

The remainder is nonnegative because40 is even. Its integrated upper bound is 12^(40+q)/(81*8^81). The high partial is sum (-1)^n M_(n+q)/[(2n+1)8^(2n+1)]. Native moments are exact integers:

    M_k=sum_(a+b+c=k) k!/(a!b!c!) binom(2a,a)binom(2b,b)binom(2c,c).

This follows independence of the three variables 4sin²(theta/2), whose nth moments are binom(2n,n). cminus uses M0..M39, mu uses M1..M40 and nu uses M2..M41. M42 is not numerically required: X<=12 bounds its positive remainder. This specifies the actual normalization and remainder sign independently of an oracle.

## Directed arithmetic and completed execution

The copied producer sources evaluate each mapped-node contribution with outward192-bit arithmetic, save all67 panel cumulatives and tail data before final target gates, then add the signed quadrature radius and low/high intervals. Exact directed Machin bounds pi=16atan(1/5)-4atan(1/239), with32 and10 terms and alternating remainders, enclose multiplication by2/pi. Negative-term subtraction is outward. The independent saved checkers use Fraction/divmod and an alternative binomial convolution for moments, reconstructing all1742 node contributions rather than only comparing summaries.

For nu the predata middle width bound uses t<=8, |dQ/dA|<=4096, |dQ/dt|<600 when A is held independent, total upper weights<=9 and the actual node/A widths; its checked middle gate is2e-25. The two-moment targets were conditional on their actual propagated widths and are now accepted. Original arithmetic and full-node postchecks, not a nominal precision label, establish all three actual gates.

The nu attempt completed once in2.25 external seconds and its full-node reconciliation in2.11 seconds. The new dual-moment attempt completed once in2.09 seconds and its full-node reconciliation in2.43 seconds. Original receipts with then-pending post/external flags are retained unchanged beside the later explicit acceptances. Zero new oracles means no new Green/node/weight evaluation; the original contractions were genuine new numerical integrations, not free symbolic deductions. This canonical runner performs neither integration nor a full-node replay.

## Source closure, recovery and remaining scope

The [recovery manifest](../.claude/science/physics-loops/native-rho4-moment-certificates-20260909/verification/RECOVERY_MANIFEST.json) pins exact producer/checker arithmetic sources, reviews, results and accepted receipts. Checkpoints65–69 at the pinned remote commit retain full runtime/input/catalog and failure histories. The compact local bundle omits large raw catalogs and installed runtimes deliberately; it is sufficient for the stated compact identity/binding verifier, not a standalone full scientific replay. Reconstructing that larger replay requires the exact recovery paths and a separate execution contract.

Source review PASS is not integration PASS or an audit verdict. The canonical source is conditional on the stated native model and authenticated imported A catalog. The new intervals may support later covariance calculations, but an old cache centered at older scalar midpoints cannot obtain their precision merely by shrinking its radius. Such reuse needs explicit midpoint correction or rebuilding. This note supplies no such downstream claim.
