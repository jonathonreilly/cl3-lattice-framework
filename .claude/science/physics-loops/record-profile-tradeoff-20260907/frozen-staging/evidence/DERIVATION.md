# Sharp registration-overlap stiffness at fixed collision concentration

This is a conditional mathematical profile theorem, not a dynamical selector. The corrected source defines r=C(0)=∫p² and κ=∫|p'|²/r, with mass-one Haar dtheta/(2pi), p≥0, ∫p=1 and p∈H²(U1). The current axioms do not fix r or require minimization. We fix r as an additional measurable statistic and characterize the sharp lower envelope, without assigning that variational law to physics.

## Theorem

For r>1, the minimum over these profiles is

κ_min(r)=(r−1)/r for1<r≤3/2,

κ_min(r)=4r²/27 forr≥3/2.

For1<r≤3/2 all minimizers, up to angular translation, are

p(theta)=1+sqrt[2(r−1)] cos(theta).

Forr≥3/2 all minimizers, up to translation, are

p(theta)=k[1+cos(k theta)] for |theta|≤pi/k, and0 otherwise,

where k=2r/3 and theta is the representative angular distance in[-pi,pi]. At r=3/2 the formulas coincide. At r=1 only p=1 is admissible and κ=0; this uniform case is excluded by genuine variation in the supplied shift-family construction.

## Existence and rearrangement

First minimize E=∫|p'|² at fixed ∫p=1 and∫p²=r in H¹. The displayed profiles provide feasible functions at every r≥1, so the infimum is finite. A minimizing sequence is bounded in H¹; weak H¹ compactness and strong uniform/L² compactness on the circle preserve positivity, mass and r. Lower semicontinuity gives a minimizer.

Circular symmetric decreasing rearrangement preserves the distribution of p and hence both constraints, and does not increase E. The one-dimensional reason is explicit. At almost every regular level t, let m(t) be superlevel length and let a_j be the nonzero boundary slopes. Coarea gives -m'(t)=Σ1/|a_j| and the energy density Σ|a_j|. A proper nonempty superlevel set has at least two endpoints; Cauchy–Schwarz gives Σ|a_j|≥4/[-m'(t)]. A centered interval with equal endpoint slopes achieves equality. Integrate over levels, and extend to H¹ by smooth approximation/lower semicontinuity. Thus some minimizer is even and nonincreasing on[0,pi], with a single positive interval (or full support).

## Euler equation and obstacle boundary

On the positive interval, variations compactly supported there satisfy the two equality constraints. Since r>1, the functions1 andp are independent on a suitable positive open set. Lagrange multipliers therefore give

-p''=lambda p+mu

there, with harmless normalization absorbed into the multipliers. The profile is smooth in the positive region. Symmetry gives p'(0)=0. The positivity constraint yields the distributional variational inequality

-p''−lambda p−mu≥0

on the zero region/boundary: take any nonnegative exterior perturbation and correct its mass and L² changes using two independent interior variations. The first-order inequality then has precisely this sign.

If the support ends at ell<pi, continuity gives p(ell)=0. The one-sided interior derivative exists from the ODE. A negative derivative at ell followed by the zero exterior derivative would make p'' carry a positive delta, so the displayed nonnegative distribution would carry a negative delta. That is impossible. Hence p'(ell)=0 (smooth fit). The same derivative condition holds at ell=pi by even periodicity, including a possible isolated zero there.

A nonconstant monotone solution with p'(0)=p'(ell)=0 forces lambda>0. For lambda≤0, the affine/hyperbolic solutions with derivative0 at0 cannot have a second zero of the first derivative unless constant. For lambda>0 the derivative is a sine; monotonicity forces sqrt(lambda)ell=pi rather than a higher multiple. If the support is proper, the zero boundary value gives exactly A[1+cos(pi theta/ell)]. Normalization gives A=pi/ell=k; its squared norm gives r=3k/2. Proper support requires k≥1, hence r≥3/2.

For full positive support, periodicity and monotonicity give p=1+A cos(theta); normalization fixes the constant term and the squared norm gives A²=2(r−1). Nonnegativity requires A≤1, hence r≤3/2. The constant solution would have r=1 and is not in the r>1 problem.

This exhausts the rearranged minimizers. The equality case in the coarea inequality forces two boundary points and equal slopes at almost every nontrivial level. Equal slopes make the midpoint of the two endpoints independent of level. Positive plateaux are excluded by the ODE unless the profile is constant. Thus any minimizer is a translate of the same symmetric profile; there is no additional multi-bump equality family.

## Exact values and H² admissibility

For the harmonic branch E=A²/2=r−1. For the supported branch,

∫p=1, ∫p²=3k/2, E=k³/2,

so E/r=k²/3=4r²/27. The supported profile and its first derivative match0 at the support endpoints. Its weak second derivative is the bounded piecewise function -k³cos(k theta) inside and0 outside; no delta occurs. Hence it belongs to H², as required by the corrected overlap source. The H¹ minimum is attained within H² and therefore is also the H² minimum.

The two lower-envelope branches have equal value1/3 and equal first derivative4/9 at r=3/2; the transition is not an artificial discontinuity. The first-harmonic formula beyond r=3/2 becomes negative and is infeasible. Multiple separated bumps lose the coarea equality and cannot improve the result.

## Scientific scope and failed selector

The current MINIMAL_AXIOMS_2026-06-29.md Admissibility and Record sections specify a neighbor-dependent distribution and durable readable realization, not a concentration, entropy principle or minimization rule. REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md explicitly supplies no normalization or state-selection law. SCALE_REFERENCE and KINETIC_ISOTROPY supply no dimensionless coupling. Thus neither the fixed r nor minimizing E is an already-axiomatized selector. This theorem cannot select a physical profile or stiffness without TWO additional bridges: a fixed concentration datum/law and a variational extremality law.

The new content is the exact sharp profile tradeoff, including a positivity-obstacle transition and admissible compact support. It strengthens the existing functional κ=||p'||²/||p||² by relating it sharply to another statistic of the SAME actual profile. Under the source's supplied repeatable ensemble protocol, r is inferable from overlap data; that makes the conditional theorem operationally testable, not primitive-derived physics.

The next concrete route is to test any independently supplied microscopic registration dynamics for a Lyapunov functional whose constrained stationary profiles are exactly these minimizers. No such law was found in the inspected current axioms. One must derive its conservation of r and monotonicity of E, rather than stipulate a gradient flow after seeing the desired profiles. The arbitrary positive-T conditional compiler alone cannot supply that law.
