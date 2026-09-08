# Independent finite-temperature cold review

PASS for the stated conditional finite-temperature stiffness and native annealed joint-event results. Source hashes: stiffness b8c272d9f4c70152451d73a4cd645401574b3878175683938d3815ada61bcd29; chessboard918d3aae1487e825151478a9b2765fa48e82508a395c10a50fe7315760c7b561. Complete proofs, actual2452-case checker and its report were read. No density certificate, thermal scan, phase or supplied-model selection is granted by this review.

## Trace and free-energy accounting

A fixed native orbit has N/2 active and N/2 spectator complex modes, with only their total parity fixed. Every active occupation has exactly2^(N/2-1) compatible spectator occupations, including when active modes have zero energy. Thus Z_native=2^(N/2-1)Z_active and the unrestricted auxiliary paired-frequency product is Z_active². The fixed-orbit native free-energy difference is exactly half the auxiliary difference; imposing another active parity restriction would be wrong.

Each auxiliary density thermal correction lies in[-log2/beta,0]. The difference of two corrections therefore loses at most log2/beta, rather than twice that. The physical hopping factor in the finite-grid term is correctly h. The soft absolute-value spectral trace is convex with dual derivative norm at most1, giving the same unit-hopping semiconvex constant. The stated d0/2 regime, delta>=2d0/3 and native coefficient d0/12 have the correct factors. Extending to finitely many smaller cubes requires the separately supplied strict ground comparison and a sufficiently large beta; it does not produce an explicit small-size constant.

The primary Macris–Nachtergaele paper was checked directly at Theorem1.4, Section2's reflection/gauge reconstruction and Remark(a). Its finite-temperature remark extends both the reflection lemma and the optimization proof to the full trace. Thus the canonical reference remains a minimizing fixed-orbit free energy; this is not inferred merely from its ground-energy minimum. This external reflection theorem remains an explicit mathematical import. See https://arxiv.org/html/cond-mat/9604043 .

The global moment-generating/mean-density inequalities safely overcount at most eight winding orbits per face assignment. Their growing-volume bound is not an exterior-conditioned event estimate. The first packet correctly leaves that separate obligation open; the second supplies a new argument for the annealed measure rather than taking an entrywise square root of a positive kernel.

## Native reflection kernel

On the declared cuts both opposite boundaries form a matching, because half width is at least two. Choosing one endpoint gauge per crossing edge fixes every cross sign independently; for each of the2^c crossing assignments this is a bijection on internal link assignments. Half-internal gauge-invariant events are preserved. Gauge-orbit size is the uniform2^(N-1), so these multiplicities cancel in normalized probabilities. This does not fix or omit winding sectors.

Each half has an even number of Majoranas. With gamma_L=alpha tensor I and gamma_R=P_L tensor conjugate(alpha), the cross Hamiltonian convention -it gamma_L gamma_R produces the exponential factor+i alpha P_L tensor conjugate(alpha). Right reflected internal hopping must have the conjugated coefficient; this returns canonical crossing face flux, consistent with the magnetic reflection convention. Arbitrary half fields on the two sides are then independently indexed l,r in the same reflected coordinate system.

At every finite Trotter depth the cross matching expands with positive real cosh/sinh coefficients. Moving the m left parity strings across the odd insertions gives(-1)^(m(m-1)/2). Odd histories have zero left trace because the final word is parity odd. For m=2k, i^m times that sign is exactly+1. The remaining right trace is the conjugate of the SAME ordered left word evaluated at r; complex conjugation does not reverse multiplication order. Hence each history contributes a positive-weight rank-one Gram kernel. Summing histories and taking the finite-dimensional Trotter limit preserves positivity. No active gap or zero-mode exclusion is needed. The constant spectator factor preserves this kernel positivity.

This is enough for normalized event Cauchy–Schwarz after the internal sums, with the same full partition denominator on both reflected events. Gauge-invariant cube events fit the half-support requirement. The proof is stronger than a pointwise inequality on individual weights.

## Chessboard, entropy and connected sets

Every assignment of disjoint internal cube labels, including wildcards, has positive probability in the finite Gibbs measure. Negative logarithms are therefore finite. The commuting rho twist converts reflections to the ordinary finite-alphabet reflection operation; the previously proved longest-run lemma applies to even block counts without a power-of-two restriction. Wildcard dissemination has probability1.

The full cycle rank is E-N+1=2N+1=16B+1. Five independent internal cycles per disjoint cube impose5B independent constraints, leaving exactly11B+1 free orbit bits. This counts all crossings and windings, rather than using only the cube labels as the measure space. Combining this entropy with m(q)>=2 and the31-label union gives the displayed p^k. If the untruncated p is above1, replacing it by1 is simply the trivial probability bound.

Each prescribed face lies internally in two of eight partitions, so a fixed partition contains at least m/4 chosen faces. Since a cube contains at most six faces, at least m/24 cubes must be bad. Selecting that partition from the prescribed set before the random field is sampled is essential and is satisfied. The p^(m/24) inequality is safe; integer ceilings can only strengthen it.

A connected m-edge set containing a fixed dual vertex has a deterministic Euler traversal after doubling every edge, of length2m. The six-valued step word reconstructs its edge set, so the injection into at most6^(2m) words proves the36^m bound, also on the finite torus. Summing the prescribed-edge event bounds yields the stated tail when36*p^(1/24)<1. This is unconditioned and includes winding components with defects; it says nothing about defect-free pure winding sectors, DLR uniqueness, particle confinement or a physical phase.

## Independent controls and failures retained

The independent checker uses abstract Clifford bitmask algebra with SIX Majoranas per half, not the author's dense one/two-mode matrices.288 fixed histories through eight crossing insertions verify the trace sign identity. Removing i, removing the parity string, or dropping right conjugation each gives64 actual mismatches. This is finite algebraic evidence; the all-beta result is the analytical Trotter argument.

The first independently chosen history schedule had no useful simultaneous nonzero traces, so none of its adverse variants discriminated. Its source and failure record are preserved. The corrected deterministic fixture explicitly closes both even histories before evaluating the unchanged identity; no theorem or acceptance constant was altered. The author's two platform-limit failures likewise remain disclosed and are not counted as successful controls. No exponential, eigensolver, stochastic or thermal-production run was performed.
