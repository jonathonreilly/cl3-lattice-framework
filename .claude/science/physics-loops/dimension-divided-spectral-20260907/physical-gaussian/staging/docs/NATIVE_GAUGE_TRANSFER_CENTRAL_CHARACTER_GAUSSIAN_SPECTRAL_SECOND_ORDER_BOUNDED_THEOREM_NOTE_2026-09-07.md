---
claim_id: native_gauge_transfer_central_character_gaussian_spectral_second_order_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional central-character one-link result; no multi-link spatial transfer identification."
upstream_dependencies:
  - native_gauge_transfer_dimension_divided_wilson_second_order_bounded_theorem_note_2026-09-07
  - native_gauge_transfer_killed_heat_second_order_kernel_bounded_theorem_note_2026-09-07
  - native_gauge_transfer_full_top_second_order_bounded_theorem_note_2026-09-07
runner: scripts/native_gauge_transfer_central_character_gaussian_spectral_second_order_2026_09_07.py
---

**Type:** bounded_theorem
**Status:** proposed_retained

Actual current-surface status is conditional-support; independent audit is unset.

~~~yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
target_claim_type: bounded_theorem
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Audit the stated one-link theorem and its declared analytic premises."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

# Exact Gaussian chamber spectrum and dimension-divided branch corrections

The searched Wilson campaign gauge notes contain no Mehler or matching dimension-divided Gaussian-sandwich spectral result. This is a scoped repository search finding. The already known Schur normalization is not reproved as a new physical bridge.

For the supplied CENTRAL-CHARACTER sandwich with dimension-divided multiplier, the continuum operator is G0=S M_w S, w=e^-Q. It differs from the native H-weighted Perron operator. Its spectrum and the first two large-beta branch corrections can be computed exactly. All discrete asymptotic statements below depend on the reviewed global divided multiplier, reflected heat and quadrature lemmas; no multi-link spatial compression is identified.

## Gaussian kernel and exact spectral normalization

Use Euclidean coordinates u=√3(x+y)/2,v=(x-y)/2. Then Q=u²+v², L=Delta/4 and dxdy=(2/√3)dudv. The unitary change of measure converts the free time-one heat prefactor sqrt3/(2pi) into1/pi. The positive spectrum-equivalent carrier

    B=M_sqrtw exp(L)M_sqrtw

therefore has the six-reflection restriction of the full-plane kernel

    pi^-1 exp[-(3/2)(|r|²+|s|²)+2r·s].

Let omega=√5 and theta=(3-√5)/2. In one dimension, apply the kernel pi^-1/2 exp[-3(x²+y²)/2+2xy] to the Hermite generating function exp[-omega y²/2+2√omega yz-z²]. Completing the Gaussian square gives

    √theta exp[-omega x²/2+2√omega x(theta z)-(theta z)²].

The identities theta^-1=(3+√5)/2 and omega theta=1-theta² verify every coefficient. Thus the Hermite degree n has eigenvalue theta^(n+1/2). Taking products in two dimensions gives eigenvalue theta^(N+1) for total oscillator degree N; completeness is the ordinary complete Hermite basis, not a fitted Gaussian ansatz.

The chamber is an angle-pi/3 wedge. Odd Weyl extension is an isometry after its factor1/√6 and identifies the killed kernel with the anti-invariant full-plane sector. There is no additional factor6 in its eigenvalues. Dirichlet angular modes have angular momentum3k,k>=1; radial Laguerre index n>=0 adds2n to the degree. Therefore the exact spectrum is

    theta^(3k+2n+1), k>=1,n>=0,

with multiplicities from equal degrees, equivalently degrees3+2a+3b,a,b>=0. The leading degree3 and next degree5 are each simple; degree4 is absent. Hence

    mu0=theta4,   mu1=theta6,   mu1/mu0=theta².

This is the spectrum of the Gaussian DIRICHLET SANDWICH, not of bare normalized group convolution on its full Peter–Weyl space.

## Actual first two eigenfunctions

Up to normalization, the B eigenvectors are

    u0=H exp(-omega Q/2),
    u1=H(4-omega Q)exp(-omega Q/2).

The second is the degree5 radial Laguerre mode, not a trial excitation. With X=S M_sqrtw, G0=XX* and B=X*X, the normalized G0 eigenvectors satisfy phi_i=Xu_i/sqrt(mu_i). The exact harmonic-Gaussian heat formula and its derivative in its Gaussian parameter give

    phi0 proportional H exp(-aQ),
    phi1 proportional H(4-2aQ)exp(-aQ),   a=2/√5.

In particular phi1 is proportional H(√5-Q)exp(-2Q/√5). Their normalization and orthogonality use the radial density H²dxdy proportional q³dq, with exponential rates omega for u and2a for phi. The checked mapping includes the coefficient change in the excited radial polynomial.

## Conditional discrete asymptotic transfer

Let A_beta^conv=e^-beta T_beta^conv=P_beta M_(c_p/(d_p c0))P_beta be the supplied central-character one-link sandwich, with P_beta=exp[(beta/2)(J-I)]. There is no extra beta^-3/2 here. The global dimension-divided theorem gives

    c_p/(d_p c0)=w(x_p)+h²P2(Q(x_p))w(x_p)+O(h4)

uniformly over actual labels. Its operator remainder remains O(h4) after the two contraction factors. The exact weighted time-one heat expansion gives the heat-only correction L²/4 in the spectrum-equivalent sqrtw carrier.

The sampled continuum B has eigenvalue quadrature error O(h4) on both displayed branches. Indeed its eigenvector quadrature integrand is sqrtw(x)s_1(x,y)w(y)psi_i(y), psi_i=Sphi_i/sqrt(mu_i). The heat factor and psi_i each vanish linearly at each wall, so the product vanishes quadratically and its first normal derivative is zero. All derivatives have Gaussian envelopes. The same is true of u_i². The previous tensor Euler–Maclaurin/quasimode proof therefore applies even though w itself does not vanish at a wall. The full correction converges qualitatively in weighted Hilbert–Schmidt norm. Simplicity and isolation of BOTH mu0 and mu1 justify first-order branch perturbation; no generic excited-branch simplicity is assumed.

Consequently, for i=0,1,

    lambda_i(A_beta^conv)=mu_i[1+k_i/beta+o(beta^-1)],
    k_i=<u_i,P2(Q)u_i>+||Lphi_i||²/4.

Here u_i,phi_i are normalized actual eigenvectors. Unlike the native shifted-saddle comparison, no separate exp(3/beta) is inserted: its3 is already in P2. No second-order step-function operator expansion or O(beta^-2) spectral remainder is claimed.

## Exact branch moments and coefficients

For u0, Q has gamma shape4 and rate√5: EQ=4/√5, EQ²=4. For u1, the same density is weighted by(4-√5Q)² and normalized; direct gamma moments give EQ=6/√5, EQ²=10. Hence

    <u0,P2u0>=4-7/√5,
    <u1,P2u1>=11/2-21/(2√5).

For H F(Q), L[H F]=H[QF''+4F']. Applying this to the two actual phi_i and integrating their squared derivatives gives

    ||Lphi0||²=4,   ||Lphi1||²=10.

Thus the exact full relative corrections are

    k0=5-7/√5,
    k1=8-21/(2√5).

The first/top ratio therefore has

    lambda1/lambda0=theta²[1+(3-7/(2√5))/beta+o(beta^-1)].

Its relative correction is strictly positive; equivalently the top/first logarithmic separation has first correction -3+7/(2√5). These conclusions concern these independently isolated Gaussian branches of the correctly normalized supplied central-character model only. They do not import the native H-weighted coefficient or establish a physical multi-link mass gap.

## Checks and remaining scope

The symbolic certificate checks Gaussian generating-function exponents, the finite low-degree angular/radial census, eigenfunction heat mapping, orthogonality, exact gamma moments, generator norms and ratio coefficient. The analytic completeness/odd-extension and discrete weighted/quadrature arguments are given above, not inferred from that finite census. No numerical Perron fit or assumed trial ground state is used. There is no explicit beta onset, certified finite-beta spectral value, full fixed-embedding operator expansion, or multi-link spatial transfer identification.
## Declared proof inputs and certificate

The exact native Fourier/reflection identity is the [September 2 reflection theorem](NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md). The actual Schur-normalized one-link coefficient is supplied by [Wilson SU(3) kernel positivity](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md), with the earlier [character-diagonal equivalence](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md). These are imported model identities, not a newly established multi-link bridge.

The uniform multiplier premise is the [dimension-divided theorem](NATIVE_GAUGE_TRANSFER_DIMENSION_DIVIDED_WILSON_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-07.md). The heat premise is the [killed heat kernel theorem](NATIVE_GAUGE_TRANSFER_KILLED_HEAT_SECOND_ORDER_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-07.md). The tensor Euler–Maclaurin, quasimode and isolated-branch argument is the [full-top theorem](NATIVE_GAUGE_TRANSFER_FULL_TOP_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-07.md), applied here to the explicitly displayed smooth Gaussian eigenfunctions and quadratic wall zeros.

The standalone [exact certificate](../scripts/native_gauge_transfer_central_character_gaussian_spectral_second_order_2026_09_07.py) performs 19 substantive assertions. It has no external input files, runs under 180 seconds and 180 MiB, and emits pure JSON with `--json`. Its finite symbolic checks support the analytic proof; they do not replace completeness, asymptotic estimates, or establish a finite-beta onset. In particular no beta=6 conclusion is asserted.
