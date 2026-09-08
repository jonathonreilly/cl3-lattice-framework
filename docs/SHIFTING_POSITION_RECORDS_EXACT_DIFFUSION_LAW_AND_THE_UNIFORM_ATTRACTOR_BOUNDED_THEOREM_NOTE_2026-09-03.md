---
claim_id: shifting_position_records_exact_diffusion_uniform_attractor
claim_type: bounded_theorem
claim_scope: "For the declared even pi-flux tori (L=32 one particle, L=16 comparison, L=6 two particles) and cube edge-qubit carrier (ambient N=2 dimension 896, selected +loop code dimension 28), retain formal-complement census, frozen-generator pinning, translation-covariant group increments and a centered additive-lift variance law, local 6*tau^2-8*tau^4 expansion, exact Bernoulli age identity, finite adjacent-detuning leakage and coarse measurement marginals. Torus position variance is bounded. The four-time quadratic fit and fitted-tail renewal outputs are uncontrolled diagnostics, not Drude or physical long-time limits. I/896 is a fixed point but not a unique attractor; all numerical rows have their sampled domains. No formation, physical CoM, arbitrary-strength confinement or framework tick is established."
upstream_dependencies: []
runner: scripts/shifting_position_records_exact_diffusion_law_check_2026_09_03.py
---

# Supplied position ticks: finite torus kernels, additive lifts and code-sector marginals

**Date:** 2026-09-03; source correction 2026-09-08.
**Type:** bounded_theorem. **Status:** conditional finite mathematical source; independent final source confirmation pending. Audit status remains unset.
**Primary runner:** [shifting_position_records_exact_diffusion_law_check_2026_09_03.py](../scripts/shifting_position_records_exact_diffusion_law_check_2026_09_03.py).
**Runner cache:** [actual canonical execution](../logs/runner-cache/shifting_position_records_exact_diffusion_law_check_2026_09_03.txt).

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional finite algebra, exhaustive finite certificates and explicitly bounded numerical diagnostics; no physical formation theorem or uncontrolled asymptotic promotion."
trace_class: frontier_discovery
artifact_role: theorem
next_trace_action: "Original independent reviewer confirms corrected source and actual inputs; coordinator owns integrated validation and any landing. Formal audit is deferred by owner until a solid TOE."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and current authority

The [current minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) is the governing
boundary, not a supplier of this model. Its Record clause makes records permanent
and fixes one local possibility at one site; its Admissibility reading distinguishes
support from a probability-selection or formation rule. A parity occupation on a
coarse corner is not a fine-site Record. Ordinary tensor/Fock composition, the
edge-qubit encoding, pi-flux hopping, chosen preparation, time, probabilities and
measurement/postselection are **supplied conditional hypotheses**. Their physical
realization is not derived here. Repeated changed values and joint configuration
conditioning are counterfactual models, with no embedding into permanent fine-site
Record formation or a nearest-neighbor physical instrument established.

The dated owner proposal about moving records is historical motivation. No axiom
change follows from interpreting that proposal. Historical references #7858,
#7876, #7879 and #7834 are not accepted parents or theorem suppliers; all needed
finite operators and conventions are redeclared below and in this runner. No
reserved source, ledger grade or parent campaign is imported. The runner reads
this final note and the actual current memo as declared, hash-pinned inputs.
Its mathematical runtime otherwise uses only NumPy/SciPy and standard Python.
There is no local runtime helper and no mutual note/cache fingerprint.

## Supplied objects and six protocols

On the cube graph there are eight corners, twelve edge qubits and six faces.
For i<j, use the superfast Pauli presentation
`A_ij = X_ij prod Z(previous edges at i and j)`, `A_ji=-A_ij`,
`B_v=prod_(e incident v) Z_e`, `T_ij=(i/2) A_ij(B_i-B_j)` and `H=sum T_ij`.
The parity dictionary is `n_v=(1-B_v)/2`. Every `y in F2^12` specifies twelve
edge values; `|y|` counts minus values, not the number of formed Records.
The ambient `N=sum n_v=2` carrier has dimension `896=28*32`. Five independent
commuting face-loop stabilizers select the all-plus code; its N=2 subspace has
rank 28. The runner's `slater(0,4)`, gauge-matched and lifted into that code,
has energy -4 and is a ground vector **within that code**. It is not an ambient
896-dimensional ground vector. Its parity marginal is 1/16 on sixteen pairs
and zero on twelve pairs sharing an x-face. These are chosen-state zeros.

On an even `Z_L^3` torus use unit spacing, unit hopping, coordination six and
`eta(v,0)=1`, `eta(v,1)=(-1)^v_x`, `eta(v,2)=(-1)^(v_x+v_y)`.
The two-particle generator uses the declared site-ordered fermionic sign.

- M0: unitary free evolution of a basis delta under H, for supplied duration t.
- M1: delete the six bonds incident to the chosen delta's site; evolve under H_R.
- M2: after each duration tau, measure the one-particle position and reset to the
  observed basis delta. This is a supplied repeatable position measurement.
- M3: independently make that measurement with Bernoulli probability p each tick.
- M4: two particles with `H=-sum eta(c†c+h.c.)+g sum_adj n n`, measured each tick.
  **Positive g raises adjacent configurations**: it is adjacent detuning, not a
  positive cost of separation. No positivity on every separated outcome is assumed.
- M5: on the cube apply `rho -> mask(U rho U†)`, masking between the 28 parity
  outcomes. This is a coarse measurement, not twelve local-Z registrations.

## T1 / A: formal complements and actual hops

For every 4096 bit pattern and twelve edges (49,152 cases), the **formal X
complement** `y -> y XOR e` flips just the two endpoint parities. Its minus-bit
weight changes by ±1 (24,576 each). Parity occupation number is conserved exactly
when one endpoint is occupied; otherwise it changes by ±2 (24,576 cases each).
This is exact integer enumeration. In the actual T_ij, the difference B_i-B_j
annihilates equal endpoint parities. Thus only the exclusion-conditioned half
of the formal census is a nonzero hop. In particular the all-zero pattern has
no hopping amplitude. Neither a formal complement nor this matrix identity
licenses changing a permanent fine-site Record's content.

## T2 / B: finite free spread and exact pinning

The original minimal-image, **centered torus variance** on L=32 is
`0.0592, 0.3453, 1.0890, 2.1365, 5.8574, 12.0704, 32.2419, 125.5190`
at `t=.1,.25,.5,1,2,3,5,10`; the displayed sqrt(variance)/t goes 2.4332 to
1.1204. These finite-time rows do not prove ballistic asymptotics. L=16 and
L=32 differences at `.1,.5,1` are `1.4e-17,4.1e-13,1.7e-8`, passing a 1e-7
comparison; they do not prove volume independence throughout an interval.
For M1, H_R e_v=0 exactly after the six bonds are removed, so the exponential
fixes e_v at every time. Numerical t=.5,1,5,20,100 rows give zero leakage and
variance. This is a frozen supplied generator, not physical Record formation.

## T3 / C: torus position and a separately defined additive lift

Let r be the increment in the finite group Z_L^3. Choose its coordinate
representative `a(r)` in `(-L/2,L/2]`: at the antipodal tie choose **+L/2**,
as the actual `minimal` function does. Put `mu_tau=E a(r)` and
`m2(tau)=E|a(r)-mu_tau|²` (the runner already subtracts that mean).
The tie can give nonzero mu even though the group law is inversion symmetric.
There is no assumption of exactly zero representative drift.

Translation covariance holds for all even L: translating by t changes the
staggered signs by the diagonal gauge
`G_t(v)=(-1)^(t_x*v_y+(t_x+t_y)*v_z)`; even periods make it well-defined.
Probabilities are unchanged. Real symmetric H makes U symmetric, so covariance
also gives inversion symmetry **in the finite group**. Each M2 reset therefore
supplies independent identically distributed group increments. Define a new
real observable `S_n=sum_(j=1)^n [a(r_j)-mu_tau]`. Independence gives exactly
`E|S_n|²=n*m2(tau)` and `D_lift=m2/(6*tau)`. This is a centered additive lift;
it is not the displacement of the finite torus position after n ticks.

The historical FFT check agrees within 1e-11 for the 17 screened (tau,n) rows
with wrap mass below 1e-14; it does not establish exact unwrapped behavior.
At tau=.5,n=2000 the actual torus variance is about 255.7497 while n*m2 is
2177.9896. Every torus variance is at most `3*(L/2)^2=768` at L=32.
The original D_lift table is
`0.0987,0.2302,0.3630,0.3860,0.3561,0.3479,0.4881,0.6706,1.0747`
at `tau=.1,.25,.5,.7,1,1.2,2,3,5` (acceptance error <1e-4 for these rounded
values). This definition preserves the numbers without assigning a physical lift.

The local small-time result is stronger than the old extrapolation:
`m2(tau)=6*tau²-8*tau⁴+O(tau⁶)` and
`D_lift=tau-(4/3)*tau³+O(tau⁵)` for the declared L=32 lattice.
For an origin delta let f_k=H^k delta. The amplitude terms through k=3 are
`-i*tau*f1 - tau²*f2/2 + i*tau³*f3/6` in addition to f0.
Consequently the weighted second-moment coefficients are
`sum |r|² f1(r)²=6` and
`sum |r|² [f2(r)²/4-f1(r)*f3(r)/3]=-8`.
Enumerating signed nearest-neighbor walks with exact integers/Fractions gives
enumerated endpoint counts 1,6,19,44 (including endpoints whose signed sums cancel to zero). No path of length at most three wraps L=32, and the
mean-squared centering correction starts beyond this order. Evenness in time
removes odd powers. The direct tau=.005 estimate 7.99984 is retained as a
1e-3 numerical crosscheck, not the proof of the coefficient.

The original quadratic least-squares fit to the four times 3,4,5,6 has leading
coefficient 1.2437. It has three fitted coefficients, **no tail error bound**,
and establishes no Drude limit. At fixed L, bounded m2 implies
`m2(tau)/tau² -> 0` and `D_lift(tau) -> 0` as tau grows. An infinite-volume-first
limit is unproved here. The sampled shoulder maximum .3860 at .7 and minimum
.3474 at1.15 are just the two finite scan extrema, not global extrema.

## T4 / D: exact renewal accounting and uncontrolled tail diagnostic

For independent Bernoulli ticks, age a at tick n has weights
`P_n(a)=p*(1-p)^a` for a<n and `(1-p)^n` for a=n. Induction proves this for
all n; the original Fraction and 2^n-history checks for p=1/5,n<=12 remain.
For a **segment-wise centered lift**, subtract the duration-dependent mean
from each completed and unfinished segment. Conditional independent segment
variances then give `E[V_n]+sum_a P_n(a)*m2(a*tau)`. This is the exact identity
being numerically compared (residual <1e-12); it is not the torus variance or
an uncentered physical path when means depend on duration.

For this precisely defined lift, renewal-reward accounting gives, at p>0,
`D_renewal=(p/(6*tau))*sum_(k>=1) p*(1-p)^(k-1)*m2(k*tau)`.
Since each m2<=768, `D_renewal<=128*p/tau`; it tends to zero as p→0 at fixed
L=32,tau. The finite torus position itself remains bounded for all protocols.

The historical implementation replaces m2(s) for **s>6** by the fitted
quadratic `c2*s²+c1*s+c0`, and truncates its sum at k<int(240/p).
Its numbers `0.3630,0.9942,4.0735,3.9700,16.1936` at
`(.5,1),(.5,.2),(.5,.05),(1,.1),(2,.05)` are retained as **uncontrolled
fitted-tail diagnostics**, not actual finite-torus D_renewal. The corresponding
quadratic-leading-term proxy is `0.1036,0.9328,4.0421,3.9385,16.1685`.
The three tau/p=10 diagnostic cases give `4.0735,3.9700,3.7625` (8.3% spread).
Neither their apparent 1/p scaling nor the shared mean duration proves a
physical crossover or a limiting law. The actual acceptance bounds are 2%
and 9% comparisons, not 1e-6 accuracy. A new independent rational normal-equation
reconstruction from the four computed samples checks all three coefficients
and the **actual extrapolator**; flipping its constant must fail. This validates
which diagnostic was computed, without validating the extrapolation as physics.

## T5 / E: finite adjacent-detuning leakage and a modulo-sum proxy

On L=6 there are 23,220 two-particle configurations and 111 relative classes
modulo translation/inversion. The gauge covariance and exchange convention
make the relative partition lumpable; probability sums over each class give
its transition row. Rows sum to one within 1e-9. Uniform configurations induce
class probabilities proportional to class sizes, with adjacency .0279 and mean
distance4.5209. This is a reference, not a proof of mixing from row stochasticity.
At tau=.5 the five computed adjacent-detuning strengths g=0,4,8,16,32 give
first→40th-tick adjacency probabilities
`.3092→.0279, .4588→.0279, .7368→.0279, .9285→.0766, .9783→.4235`;
tick40 mean distances are `4.5209,4.5209,4.5208,4.3187,3.0338`.
Each sampled case leaks out of adjacency. This is neither an all-g theorem nor
a test of arbitrary energy penalties. Finite irreducible chains are recurrent,
not transient. Some separated amplitudes are exactly zero, so positive leakage
does not mean every separated configuration has positive weight.

The actual statistic is `d= minimal([(x'+y')-(x+y)] mod L)/2`, with positive
antipodal ties coordinatewise. This modulo-sum **proxy** aliases a physical
half-period translation: on L=6, {0,1}→{3,4} translates by3 but d=0.
The runner sums local conditional variances of d over40ticks and divides by
6*n*tau and its same-torus single-particle lift reference. The resulting .4910
at g=0 is not a proved full correlated asymptotic CoM diffusion ratio.
It has no blanket equality to1/2. The original 896-carrier cube rows at
(tau=.5,g=32) give `.9880,.9762,.9423,.8905,.6726` at ticks1,2,5,10,40
from the declared adjacent +code preparation; .4286 is a uniform-pair reference.
No new energy sign theorem or general confinement exclusion is claimed.

## T6 / F: coarse outcomes, conserved code sectors and fixed points

Masking the unitary conjugation equals explicit coarse-outcome tree enumeration
at two ticks (312 and5824 branches; acceptance <1e-14). From the chosen +code
preparation, mass on its twelve initially zero pairs at ticks1,2,5,8 is
`.2655,.3430,.4161,.4267` at tau=.5;
`.3101,.3638,.4228,.4280` at1;
`.2148,.3065,.4016,.4223` at2.
The first vector is compared with rounded targets to1e-3 and monotonicity is
checked at these rows. The sampled tick12/tick11 marginal L1 ratios are
`.5294,.4560,.6156` (acceptance5e-3). They are not a theorem of a fixed
geometric rate for all times or initial states. For the24 listed ticks, no
initially allowed pair exceeds1/16, so the elementary identity
`L1(q,initial marginal)=2*mass(initially zero pairs)` applies; it is not universal.

Unitality makes I/896 an exact fixed point with uniform28-outcome marginal;
the numerical map residual is <1e-15. It is **not a unique attractor**.
Every face loop S commutes with H and the coarse projectors. An involutory,
traceless Hermitian loop gives a distinct density `(I+S)/896` fixed by the map,
at trace distance1/2 from I/896. The chosen state has S expectation1, whereas
I/896 has0. The invariant rank28 projector Pc gives another fixed density
Pc/28 (trace distance31/32 from I/896), with the same uniform outcome marginal.
The exact code-to-two-fermion diagonal phase match is checked entrywise.
Walsh characters diagonalize single-particle cube hopping into
`-3,-1,-1,-1,1,1,1,3`; summing distinct occupied modes gives the code H
spectrum `{-4,-2,0,2,4}`, multiplicities `{3,6,10,6,3}`. Consequently,
at tau=pi its unitary is I exactly, so even outcome attraction cannot hold at
all tau. The raw896 minimum is approximately−4.828427, below the code minimum−4.
These are separate state/code/marginal claims. Masking preserves within-outcome
coherences; it is not a fine-site Z dephasing or a Record-formation theorem.

## Executable claim block and unresolved boundaries

```text
T1: 49152 formal complements; actual hopping nonzero only at opposite endpoint parities.
T2: finite M0 table; H_R delta=0 implies exact pinning for supplied M1.
T3: centered additive lift has variance n*m2; finite torus variance is bounded;
    local coefficients6,-8 exact; four-time quadratic fit has no long-time guarantee.
T4: exact Bernoulli age/centered-segment accounting; fitted-tail numbers are diagnostics.
T5: five finite g rows and finite local-variance proxy; no all-strength or CoM theorem.
T6: coarse tree/marginal data; I/896 fixed but nonunique; code and ambient separated.
framework_formation_derived: false
formal_audit: deferred_by_owner
```

The unchanged raw original tables and failed source controls are preserved in
the dated correction evidence identified outside docs. Current caches are genuine
executions of the corrected source, not restamped historical PASS receipts.
All original23 check identifiers remain. Numerical labels name actual predicate
bounds; floating evaluation is not an interval certificate. A transcendental
matrix exponential can have special rational entries, so transcendence alone
proves no irrationality. No observational constants are fitted; the disclosed
four-time fit is internal diagnostic data fitting.

Manual N1–N8 boundary: six real supplied protocols are compared; they are not
five failed routes to a universal theorem. Relationships among formation,
physical lift, probability selection and dynamics remain unresolved, not
independent walls. The old universal Drude, full-state attraction and all-strength
claims are withdrawn. The local coefficient and finite fixed-point/census proofs
survive. Support-conditioned alternatives, different instruments, actual lifts,
large-volume-first limits and framework formation remain open. No route quota,
wall-independence audit or structured no-go acceptance is asserted; any unmet
procedural quota remains pending. Formal audit/TOE scheduling in the historical
packet is superseded by the explicit current owner deferral.
