# Independent review of the quasi-local star vacuum representative

Disposition: PASS within the explicitly imported uniform wrong-flux stiffness domain and the canonical antiperiodic cubic grids for the final inverse-frequency conclusion. No physical numerical run was performed. This is not an all-twist theorem and gives no node value or interacting phase conclusion.

Source read completely: `native-weak-electric-uniform-local-stability-stretch/QUASILOCAL_VERTEX_LEMMA.md`, SHA c892cdcd2a9c83c26afa19b3305a622188cc1cba082c17cc8b332ac72d7069c6. Also read its complete STAR_RETURN_AND_RESUMMATION.md and DERIVATION.md to identify the operator and the stated antiperiodic/zero-mode exclusions. Reviewer participated in the separate finite-L6 vertex implementation and canonical packaging; this analytic review does not reuse a numerical form-factor assumption.

## Filter and exact vector identities

The proposed odd smooth inverse filter is valid. Its tail is -1/x; subtracting -x/(1+x²), with a fixed scale if needed, leaves an L1 function because the difference is O(x^-3). The rational summand has a bounded, exponentially decreasing Fourier transform on either half-line (a jump at t=0 is harmless). For every n≥1, f^(n) is L1, and f tends to zero at both ends. Distributional integration by parts therefore yields |w(t)|≤C_n |t|^-n away from zero. The subtraction supplies boundedness near zero. Choosing n>p+1 proves every required weighted L1 moment. No finite-volume high-energy cutoff or exchange with an unbounded spectral interval is needed.

Given H_A-E0≥δ>0 on the active space actually used, functional calculus makes f(H_A-E0)=(E0-H_A)^-1. The phase calculation is exact:

    U_C(t) τ_t(X) Ω = e^(-it H_C) X e^(it H) Ω
                     = e^(-it(H_C-E0)) X Ω.

Thus the two-filter formula is the ordered second resolvent, not a replacement by a stationary free inverse. The90 ordered disjoint-pair terms and electric factor1/8 are retained. Even cocycles times γ_v give an odd bounded Y_v. The norm bound (90/8)M0² follows directly from unitarity. Y_vΩ=χ_v does not imply equality of the two operators on excited inputs; the source correctly distinguishes these statements.

## Uniform spatial tail

A concrete implementation of the locality argument uses a ball-truncated Hermitian generator for each cocycle. The Duhamel difference of two unitary evolutions is at most the integral of the generator difference; it does not acquire an exponential in ||B|| times the volume. Finite-range one-particle hopping bounds yield the usual exponentially small spatial tail at times below a fixed multiple of the radius. Even local quadratic B and the odd center Majorana have fixed support and fixed coefficient count. Applying τ_t to the first cocycle requires a light-cone budget proportional to |s|+|t|, which is exactly the split used in the proof.

On |s|+|t|≤cr, choose c below the propagation constant divided into μ; polynomial time factors then multiply an exponentially decreasing r bound. On the complement, integrate against |w(s)w(t)| and use arbitrarily high moments. This gives C_p(1+r)^-p for every fixed p. Constants depend on the hopping scale, stiffness/filter scale, local coordination and p, not torus volume. CAR locality must be graded for the odd factor; the proof uses precisely that convention. Twisted boundary signs do not increase local hopping norms. They cannot, however, manufacture a missing spectral separation relative to a chosen reference energy.

## Gaussian extraction checked directly

For a product of an odd number of distinct Majoranas, {γ_j,Y}/2 is zero when j is absent, and is the signed product with γ_j removed when j is present. Its Gaussian expectation is the sum of all Wick pairings of the remaining legs. The one-particle term of YΩ is obtained by choosing the surviving leg and pairing every other leg, with exactly the same sign. Therefore

    P1 YΩ = P1 (Σ_j (1/2)⟨{γ_j,Y}⟩ γ_j)Ω.

The right side already lies in the one-particle space. This derivation handles complex coefficients and non-Hermitian Y; it does not require c_j to be unique. Repeated Majoranas reduce by CAR first. Local operator algebras are spanned by these monomials, so linearity proves the finite-support statement. Also |c_j|≤||Y||, and graded locality sets every exterior coefficient to zero.

For dyadic approximants, use Y_0 plus differences Y_n-Y_(n-1). Each difference is supported on a ball of radius2^n and has norm O(2^-np); its coefficient l1 norm is O(2^n(3-p)). This is summable for p>3. The telescoping operators converge in norm, and their one-particle images converge by the bounded projection P1. Hence the resulting l1 coefficient series really represents P1χ, with a uniform bound. It is not merely a sequence of unrelated finite-volume estimates.

Magnetic covariance may be preserved by choosing the same ball construction at every vertex and transporting it with the exact magnetic symmetry. Equivalently one transports the obtained coefficient family. A fixed finite magnetic cell changes constants only. The resulting symbol is uniformly bounded without assuming continuity at a node, nonzero limits or a particular sign.

## Infrared conclusion and exact scope limits

On the fixed antiperiodic cubic grids, the distance from any conical zero is at least c/L. A shell with index j has O((j+1)²) points, while inverse squared frequency is O(L²/(j+1)²). After the L^-3 normalization, O(L) shells give a uniform bound. The finite complement contributes another uniform constant. Thus the bounded form factor supplies an l2 row bound for the one-particle singleton kernel. If coefficients are complex, one may use ||Σ t_j β_j||≤√2||t||2 instead of the equality available for real coefficients; either suffices for the asserted boundedness. No l1 kernel estimate follows.

The first portions of the lemma require a pure Gaussian vacuum and the imported full active wrong-pair bound relative to that vacuum's E0. They are not licensed for an arbitrary correlated mixture of zero-mode vacua, or an arbitrary nonminimizing winding reference whose energy exceeds the E0 in the stiffness theorem. For zero-mode-free canonical antiperiodic grids these concerns are absent. The final inverse-frequency assertion excludes grids containing exact zero modes unless a separately stated projection and denominator treatment is supplied. The current surrounding text makes this exclusion explicit; any canonical port should repeat it in the theorem domain rather than abbreviating it to “all twists.”

Finally, the proof constructs a quasi-local vacuum-creating representative, not a quasi-local full effective vertex or a controlled interacting reference. The one-particle kernel bound leaves higher odd sectors, mixed returns, operator-valued connected cancellations and all-order expansion control unresolved. The source's final paragraph correctly retains all these obligations. No correction to its mathematical argument is requested.
