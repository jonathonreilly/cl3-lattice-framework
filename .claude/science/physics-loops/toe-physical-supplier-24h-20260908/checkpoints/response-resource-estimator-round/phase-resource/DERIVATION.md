# Phase-resource price of heralded native Gibbs preparation

## Result and scope

Conditional finite resource estimate, not a new physical law or a new general imaginarity monotone. Arbitrarily small TOTAL phase resource cannot prepare a fixed nonreal native Gibbs target at appreciable success, even with adaptive postselection. Merely making each pulse weak does not ensure small total resource: many weak pulses can accumulate a finite angle. Failure probabilities are included throughout.

Fix the physical edge-Z basis and the real native code from boundary-preparation/DERIVATION.md. Native real-coefficient hoppings generate real unitaries in this basis; edge-Z Record Kraus maps are real. Permit any finite real instrument, larger than this native subset, plus specified phase pulses exp(−i theta D) with D real Hermitian. Real product/mixed ready states and real ancillary supply are required. Nonreal initial resources would have to be charged separately. Histories are classical adaptive flags, never coherently recombined after being declared outcomes. All preparation, Born instrument, controls, h,beta, roles and event formation remain conditional inputs.

For each pulse define the mathematical centered angle cost

    gamma=|theta|[lambda_max(D)−lambda_min(D)]/2.

For occupation-difference D=ni−nj on the full native code, gamma=|theta|. This is an angle/norm budget, not work, heat, energy, duration, or an axiom-derived resource law. Known real factors can be factored out before accounting; for example exp(i pi(ni−nj)) is already real. The unoptimized cost is still a valid upper bound.

Organize a finite adaptive tree into pulse layers, padding branches with identity. Let gamma_l be the maximum cost among branches at layerl, and Θ=sum_l gamma_l. This definition is deliberate: it is NOT the probability-weighted mean cost or automatically the maximum path sum if different branches have their expensive pulses in different layers.

For a designated successful normalized target tau,

    p_success I_g(tau) ≤ sin²(min(Θ,pi/4)).                         (1)

Here I_g is the standard convex-roof geometric imaginarity. For actual native kinetic Gibbs targets on a real invariant code of dimensiond,

    tau_beta=P exp(−beta H)/Z_beta,   conjugate(H)=−H,
    I_g(tau_beta)=(1−d/Z_beta)/2.                                 (2)

For beta>0 and nonzero H, the denominator is positive, and(1) bounds success explicitly. For beta0 it is zero and(1) is vacuous, as it must be. Eq(2) uses the source's fixed empty-vacuum Hamiltonian zero, not an arbitrary scalar-shifted partition function.

## Primary literature and novelty boundary

Read Wu et al., Resource theory of imaginarity: Quantification and state conversion, Phys.Rev.A103,032401(2021), https://arxiv.org/html/2103.01805 (primary full text), sectionIV.1 Propositions3/4, sectionIV.2 Proposition5, and sectionV.1 Theorem1. The pure-state geometric formula, strong monotonicity, trace-norm robustness and optimal pure-state stochastic conversion are established prior art. Their methods do not select a native physical phase source. The contribution attempted here is applying a finite phase-pulse budget to the actual native Gibbs target and its parity-extended code, with explicit adaptive-cost semantics and actual preparation-circuit comparisons. No claim of a novel general resource theory is made.

## Derivation of the quadratic phase-budget bound

For a pure vector psi, choose its global phase so its real and imaginary parts are orthogonal with norms cos(alpha),sin(alpha), alpha∈[0,pi/4]. Its maximal squared overlap with a real vector is cos²(alpha), hence I_g(psi)=sin²(alpha)=(1−|psi^T psi|)/2. The mixed-state definition is the convex roof over pure ensembles. Under a real Kraus instrument this quantity is nonincreasing on average; a direct pure-state proof chooses the normalized real part of each Kraus output as a candidate real comparison vector, sums their squared norms, and then extends by convexity. This is the known strong-monotonicity fact, not a claim established by numeric sampling.

Purify the real input using a real purification. Dilate all real instruments with real isometries and keep every outcome/environment flag; real isometries extend to orthogonal unitaries in finite dimension if needed. Controlled adaptive real operations remain real. A branch-dependent scalar phase removed in centering D does not alter any final classical conditional state because the histories are not coherently recombined.

Compare this purified circuit to the circuit with every centered phase pulse replaced by identity. The latter produces a real vector. A unitary with centered generator norm giving angle gamma moves every vector by Fubini–Study angle at most gamma: for gamma≤pi/2, its expectation lies in the convex hull of an arc with real part at least cos(gamma); for larger gamma the bound is trivial. A hybrid replacement and triangle inequality give final angular distance at mostΘ to a real vector. Therefore I_g(global output)≤sin²Θ forΘ≤pi/4, and the universal bound I_g≤1/2 handles largerΘ.

Measuring/tracing the retained real flags is a real operation. Strong monotonicity and convexity give sum_h p_h I_g(tau_h)≤I_g(global output). Grouping all successful branches and retaining all failure weights proves(1). Even if the successful branches carry different states, it bounds their average successful density via convexity. A single rare success cannot omit its factorp.

The proof remains a bound for the more restrictive native hopping/Record class because it allows a superset of real operations. It does not show all these real dilations are physically supplied or strictly nearest-neighbor native gates.

## Native target-specific evaluation

A purely imaginary Hermitian H is i times a real antisymmetric matrix. A real orthogonal change of basis decomposes it into2×2 energy pairs(+E,−E), plus zero modes. Its Gibbs density splits into orthogonal REAL blocks. On a normalized two-dimensional block the Bloch vector lies alongY with length y=tanh(beta E).

For such a qubit, convex-roof geometric imaginarity is g(y)=(1−sqrt(1−y²))/2. The lower bound follows from convexity of g and the fixed averaged imaginary Bloch coordinate; the upper bound is attained by two pure states with that same y and opposite real z coordinates. Measuring the real block flag gives a lower bound on the full I_g, and assembling the block ensembles gives the matching upper bound. Thus each positiveE pair contributes(cosh(beta E)−1)/Z. Summing pairs and zeros yields(2). This derives the needed mixed-state value for this actual target rather than assuming a general mixed-state formula.

The exact native dimer target in phase-preparation has r3/5, beta=2log(5/3), d4, Z=2+2cosh(beta). Therefore

    I_g=32/289,
    p_actual=289/625,
    p_actual I_g=32/625.

Any circuit in the stated class achieving that state at that success rate must have

    Θ ≥ arcsin(4sqrt2/25).

The existing dimer sequence uses two difference phases of magnitudepi/4 and has unoptimized budgetpi/2. The lower bound is not claimed tight for native gates or for that circuit.

For the independently reviewed m4 path family, d16 and Z=product_j(1+exp(−beta epsilon_j)). Exact occupation enumeration and the real-block expression agree. Current numerical support gives:

|couplings|beta|I_g|actual success|necessary Θ at that success|
|---|---:|---:|---:|---:|
|1,2,3|0.7|0.3767192303655|0.1772221047328|0.2613503921442|
|1,2,3|2|0.4992678766804|0.0891123361036|0.2125249629469|
|2,1,2|0.7|0.3159940564931|0.1515963476223|0.2206549953499|
|2,1,2|2|0.4980979197171|0.0689377520488|0.1863817010485|

Angles are dimensionless mathematical radians. At Θ0.01, for example, the first target has p≤sin²(.01)/0.376719...≈0.0002655; native postselection cannot keep its original≈0.177 success while the total phase resource tends to zero. The current six-Givens implementation has a much larger naive phase budget; this calculation does not optimize it or assert saturation. beta0 rows are explicitly retained as zero-denominator/vacuous cases.

## Expected-cost alternative and approximate outputs

Let R(rho)=||rho−conjugate(rho)||_1/2, the known robustness of imaginarity. Flagging a real instrument and using trace-norm contraction proves strong monotonicity of R directly. A pulse of centered costgamma increases R by at most sin(min(2gamma,pi/2)): compare U rho* U† to U* rho* U^T by triangle inequality; the relative unitary has spectral arc halfwidth2gamma. At a node reached with probabilityw, this increase is weighted byw. Thus

    p_success R(tau) ≤ B,
    B=sum_nodes w_node sin(min(2gamma_node,pi/2)).                 (3)

For an actual success state sigma within ordinary trace distance epsilon of tau, R(sigma)≥max(0,R(tau)−2epsilon). Eq(3) remains useful with that lower bound. A quadratic-budget approximate variant follows from the general inequality I_g(sigma)≥g(R(sigma)), where g(y)=(1−sqrt(1−y²))/2: use convexity ofR and concavity of2sqrt(x(1−x)) on pure-state ensembles. Thus replace I_g(tau) in(1) by g(max(0,R(tau)−2epsilon)). This weaker approximate form requires no claim of continuity of an uncomputed convex roof.

The quadratic bound cannot use expectedΘ in place of the layerwise worst-branch budget. A real coin selects a strongpi/4 phase branch with probabilityη and otherwise does nothing. It can output a maximally imaginary pure state on that branch, so weighted I_g=η/2, whereas(mean gamma)²=η²pi²/16. This violates the proposed mean-square bound for smallη. The exact η1/100 adverse is recorded. It does not violate(1), which charges the layer's maximum, or(3), which is linear in probability-weighted cost.

## Exact small-case calibration and evidence

The known optimal pure conversion from psi=(sqrt24/5,i/5) to phi=(4/5,3i/5) has p=1/9. A real success filter diag(2/(3sqrt6),1) maps psi tophi/3; failure filter diag(sqrt(25/27),0) completes the instrument and leaves a real failure state. Its success-weighted I_g equals the input1/25. This saturates the standard pure-state resource ratio but is NOT claimed an optimal native implementation or a new theorem. Removingp gives the false inequality9/25≤1/25, an explicit bad-postselection control.

check.py executes28 checks: direct physical dimer rho·rho* identity; exact target and weighted geometric values; complete real pure conversion; missing-success-weight and mean-cost-square adverse controls; independently enumerated16-state path energies/partitions and real spectral-block I_g at all6 frozen cells; robustness consistency and wrong-dimension rejection. It copies the exact dimer source into this scratch directory before execution because that source writes adjacent output. The dimer's49 original checks are rerun dependencies, not added to this28 count. No new numeric fit, empirical frequency, or claimed exhaustive control classification.

## Scientific disposition

This provides a quantitative native-target robustness statement under a finite apparatus class: vanishing total phase cannot be rescued at fixed success by arbitrarily aggressive heralding. Individual weak pulses remain a valid route if their number supplies a nonvanishing total resource. The result leaves the actual phase mechanism, state supply, physical work, action/beta and primitive Record calibration unselected. It supports the same preparation milestone and does not motivate a separate generic resource-theory PR.
