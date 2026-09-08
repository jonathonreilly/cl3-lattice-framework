# Conditional finite-temperature defect stiffness

Status: independently derived, pending review. No spectral or stochastic computation. The uniform U=0 Hamiltonian, native constrained dictionary, finite-temperature reflection theorem, and hypothetical positive ground-density certificate are supplied premises. No nonzero-U phase statement.

## Exact parity and partition factors

Let N be even, with N/2 active complex modes and N/2 spectator modes. In a fixed link-flux orbit the physical total parity is fixed even. For every active occupation, exactly 2^(N/2-1) spectator occupations supply the required parity. Thus, including active zero modes,

    Z_native = 2^(N/2-1) Z_active,
    Z_aux = Z_active^2,
    Z_native^2 = 2^(N-2) Z_aux.

Here Z_active is its unrestricted trace. The auxiliary number-conserving N-mode spectrum doubles the active Majorana spectrum, so its paired-frequency product is precisely the square. Spectator parity is not imposed a second time on the active or auxiliary trace. Consequently every fixed-orbit native free-energy difference is half its auxiliary counterpart. Summing these sector weights is the full native Gibbs partition function; maximizing one weight does not eliminate the other sectors.

## Thermal and finite-size density errors

Use unit hopping in the 64-site Bloch matrices; physical hopping h=2|g lambda| multiplies energies and changes inverse temperature to beta h. Below energies and beta are physical unless h is explicitly shown. For any N-site auxiliary one-particle matrix,

    -N log(2)/beta <= F_aux-E_aux <= 0.

This follows term by term from log(1+exp(-beta|epsilon|)). Thus a difference of two auxiliary densities loses at most log(2)/beta, not twice that amount.

Suppose all noncanonical disseminated infinite-volume ground-density differences are at least d0>0 in physical units. On a rectangular period-four torus with M_a=L_a/4 momentum points per axis, the reviewed shift-uniform semiconvex bound gives

    d_beta,L(q) >= d0 - h*pi^2/8 sum_a M_a^(-2) - log(2)/beta.       (1)

This includes all eight winding twists. It is a bound on the finite-temperature comparison list, not an evaluation of d0.

The same quadrature constant holds directly at finite temperature. Replace Tr|H| by f_beta(H)=Tr[(2/beta)log(2cosh(beta H/2))]. This is convex as a spectral trace functional and is 1-Lipschitz in nuclear norm: its scalar derivative is tanh(beta x/2), bounded by one. The original midpoint-convexity argument therefore applies unchanged to the matrix second derivative, whose nuclear norm is 32 at unit hopping. Dividing by 128 gives semiconvex constant 1/4. No spectral gap or smooth eigenvectors are required.

For cubic M and 3h*pi^2/(8M^2)<=d0/4, beta>=4log(2)/d0, (1) is at least d0/2. The finite number of smaller cubic sizes can also be included existentially: their strictly positive ground comparison gaps follow from the separately proved finite all-even isolation theorem; choose beta large enough that their density gaps survive the same thermal bound. This supplies an all-cubic-size positive coefficient conditional on d0, but no explicit small-size constant without further certificates. It does not cover arbitrary aspect ratios with a permanently small side by this argument.

## Dissemination at finite beta

Macris–Nachtergaele, cond-mat/9604043, Section 2 Remark (a), explicitly replaces ground energy in the reflection lemma by minus log of the full Fock trace. Dividing by beta gives

    F_beta(s) >= [F_beta(s_+)+F_beta(s_-)]/2.

Its graph, coupling and trace assumptions are those already checked for the supplied auxiliary problem. The existing disjoint-cube proof uses only this inequality and finite minimization: replace every energy by F_beta. The longest-run minimizer argument and the secondary minimization of bad crossing faces are unchanged. Therefore Phi_beta,L(q) is the minimum over the eight windings of the same compatible periodic cube pattern.

Set B=N/8 and

    delta_beta,L = min_(m(q)>0) [Phi_beta,L(q)-F_beta,pi]/[B m(q)].

All 32 labels and their Bianchi-compatible link tilings remain as in the geometry proof. Averaging over eight cube partitions counts each defective face twice, giving

    F_native(s)-F_native(pi) >= delta_beta,L k(s)/8.                (2)

If (1) is at least d0/2, m(q)<=6 implies delta_beta,L>=2d0/3. Thus the native coefficient in (2) is at least d0/12. This is a low-temperature local-defect free-energy cost, uniform on the specified large cubic volumes, conditional on the not-yet-established density certificate. Pure winding changes have k=0.

## What this proves about the Gibbs distribution

There is a useful global probability consequence without claiming a Peierls theorem. Suppose (2) holds with a uniform coefficient kappa>0. An allowed elementary-face assignment determines at most eight link gauge orbits, one per winding. There are 3N faces. Bounding allowed assignments by all binary assignments is an overcount and hence safe. Since the full partition is at least Z_pi,

    Prob(k>=1) <= min(1,8[(1+exp(-beta kappa))^(3N)-1]).

This bound is volume-growing. It does not prove probability one of the canonical orbit at a fixed positive temperature. More usefully, for 0<s<beta kappa,

    E exp(s k) <= 8(1+exp(-(beta kappa-s)))^(3N),
    E k/N <= [log(8)/N+3log(1+exp(-(beta kappa-s)))]/s.

The second statement is Jensen's inequality. Taking s=beta kappa/2 gives a low-temperature bound on mean defect density, including a finite-size term. These conclusions include Bianchi constraints by overcounting; they do not require independent defects. They are not estimates for a specified contour conditioned on its exterior.

A genuine conditional Peierls/chessboard event estimate still needs either a local repair map with a conditional free-energy comparison or a proved reflection-positive annealed native measure with its event inequality. The identity Z_native proportional sqrt(Z_aux) is an identity of weights, and does not by itself establish positivity of an annealed reflection kernel. Entrywise square roots do not in general preserve positive semidefiniteness. No such extra measure theorem is asserted here. A global comparison with one reference orbit cannot simply be subtracted between two arbitrary exterior-conditioned configurations.

## Source coverage and next obligation

Read in full the local flux-selection DERIVATION, the compatible 3D dissemination DERIVATION, and the semiconvex quadrature DERIVATION. The first two are reused source proofs, not newly independent derivations of their zero-temperature statements. Directly checked the primary paper's assumptions, reflection setup and finite-temperature Remark (a): https://arxiv.org/html/cond-mat/9604043 . Its finite-temperature reflection result is load-bearing; the present parity, softabs, dissemination substitution and counting consequences are the new derivation. No third-party text is archived.

The next decisive input is the five positive infinite-volume density certificates with physical normalization. Once available, (1) prices a temperature/size regime immediately. A conditional contour theorem is a distinct later obligation; neither it nor a physical phase is needed for the free-energy statement above.
