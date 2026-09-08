# Operational partition normalization on a fixed native carrier

## Decision

A concrete conditional implementation gap can be retired: the source-dependent spectral prefactor of the earlier heralded Gibbs circuit can be replaced by one source-independent prefactor, using extra actual native leaf instruments with all outcomes retained. This is useful for interpreting success odds as a partition ratio. It does NOT retire the physical source/action supplier. The experiment is explicitly a source-reprogrammed preparation, not a perturbation applied to a fixed preparation apparatus. No new science PR or action-selection theorem is proposed here.

Read current main weak-field source-response, corrected self-consistency/Poisson and Gate-B interface in the immediately preceding source-action review; read full phase-preparation and source-action artifacts in this same session. Prior-overlap account is the source-priority map, prior action-measure distinction between selected trace and supplied measure, source-action neutral nonreciprocity, and phase-preparation's existing programmable Gaussian filter. Those already exclude counting a determinant identity or an arbitrary logarithm as physical selection. No exhaustive corpus novelty claim is made.

## General finite construction

Fix m matter-path sites, TWO sacrificial leaves per site, and one inert parity reservoir attached to the first matter site. Embed leaves at virtual +/-y, path along x and reservoir at +z. There are3m physical edge midpoint M2 factors, maximum degree4, no cycles, and no old Record restoration. The enlarged graph is fixed across all sources. This adds m leaf qubits relative to the earlier2m-qubit graph; it is not a same-dimension implementation on that old graph.

Supply finite beta>=0 and a compact real symmetric one-particle family h(s) whose spectral radius is bounded by a fixed B. Onsite occupation terms are explicitly additional source Hamiltonian terms here, not inferred from the earlier hopping-only target. Diagonalize with an SO(m) basis using the previously proved adjacent current/difference-phase compilation. Source-dependent eigenvectors, angles and eigenvalues are input to this program.

In the eigenmode frame prepare one leaf empty and one filled. With eigenvalue epsilon, use vacant-leaf survival r_plus=exp[-beta(B+epsilon)/2] and filled-leaf survival r_minus=exp[-beta B/2]. Both lie in[0,1]. The actual two successful native Record contractions multiply to

r_plus^n r_minus^(1-n) = exp[-beta B/2] exp[-beta epsilon n/2].

Even pair operations involving other matter/leaf modes commute. For the two leaves on the same mode, the success contractions are diagonal functions of that occupation, so their successful product is exactly the expression above; full pulse commutation is not assumed. Completing every leaf measurement and summing all4^m histories gives identity on the ready sector. Subsequent pulses preserve old leaf Records. A failed leaf is not reset.

After rotating back, K_s=c exp[-beta H(s)/2], c=exp[-beta mB/2], on every ready input. The remaining m physical bits are maximally mixed, the2m prescribed leaf bits are product-sharp, and the reservoir supplies compatible parity. The binary tree incidence bijection gives every matter occupation exactly once. Therefore the matter ready functional is I/2^m and

p(s)=c² Z(s)/2^m.

No signed-spectrum prefactor remains. The construction is intentionally not resource optimal.

## Actual finite probe

PREREGISTRATION.md was written before execution. A literal64-dimensional physical Pauli implementation uses edges01,02,04,06,13,15, with vacant leaves2,3 and filled leaves4,5. Native A/B/T are built from endpoint neighbor order; ready rank4 is verified. Target H(s)=T01+s(n0−n1), s∈[-1,1], beta=log2, B2. Fixed evaluated sources0,+3/4,-3/4 have genuinely noncommuting source and hopping. All controls and physical graph are the same family across s; amplitudes/diagonalizer are reprogrammed.

For all three sources the full successful matrix equals .25 exp[-beta H(s)/2]P, and all16 outcome effects sum to P. Earlier leaf Records commute with later pulses and the final rotation. The success law is Z(s)/64. Results:

- s0: p=.0703125, <n0−n1>=0.
- s+.75: p=.07498222558800469, <n0−n1>=-.24480376937138731.
- s−.75: same p, opposite expectation.

Eighty-seven actual residual assertions include the additional fixed finite-difference source evaluations; they are not87 independent fixtures. Runtime below one second,55.27MiB, one BLAS thread,180second/384MiB cap. Floating full matrices are not interval-certified. All inputs and unfiltered output are retained.

## What the success derivative measures

Since c is constant, ordinary finite-dimensional Duhamel differentiation and cyclic trace give

partial_s log p(s)=partial_s log Z(s)=−beta <partial_s H(s)>_Gibbs.

No commutation of source and hopping is needed. For multiple linearly coupled occupation sources the Hessian is the symmetric Duhamel covariance, not generally the elementary equal-time covariance. This is conditional Gibbs calculus, not a derived Poisson inverse or native action. In the probe the target derivative at+.75 is .1696850425302242; centered steps1e-4 and5e-5 give .16968504246817062 and .1696850425103591. These fixed numerical checks are not a derivative-error theorem.

The old one-leaf normalized circuit has c(s)²=exp[-beta sqrt(1+s²)] for this dimer. Its log-success derivative at+.75 would instead subtract beta*.6, changing the response and even its sign. Thus ignoring the old prefactor is a substantive observable mismatch. Removing the additional constant-normalizing attenuation does not leave the same measured partition response.

## Physical residual and stop criterion

This is a source-programmed family of complete instruments, not the source-action impulse experiment K_z(s)=Q_z V exp(i s.n) with fixed V and fixed prepared rho. Their responses can disagree without contradiction. In particular the nonreciprocal impulse example is not repaired into reciprocity merely by choosing the thermal program.

What was concretely removed is the need to infer Z(s) using a source-dependent success-normalization correction. What remains supplied is h(s), its identification with a physical source, beta, ready states, spectral processing, phase/hopping control, outcome probabilities, event schedule, fresh leaf capacity and energy/work implementation. Measuring p(s) therefore verifies that supplied program; it does not select the program or its scalar free energy as a physical action.

The next load-bearing clause would identify a naturally fixed source-coupled preparation/relaxation mechanism whose invariant state is this Gibbs family, and show that its measured source/readout is the same operator governing propagation. Without that clause, further programmable partition variants are writer churn. The present bounded matrix repair is worth retaining as support, but does not justify elevating this route above native formation/preparation selection or claiming gravity progress.
