# Spatial Wilson-loop suppression from a uniform marked expansion

2026-09-07. Conditional mathematical result for the supplied compact Hamiltonian. Root supplied the proposed marked-polymer route before the prospective contract; the detailed weighted pinned-cluster argument below was developed in this lane. This is an explicit mathematical import, not an axiom derivation or a new general cluster-expansion theorem. The primary worker's selection proof and root's completed derivation have not been read before freezing this file.

## Model and precise boundary family

Use cubic periodic volumes with three outgoing SU(3) link spaces per cell. The electric operator is K_e=−3Δ_e/(2a), with all-label energies [p²+pq+q²+3p+3q]/a. Thus its constant vacuum is unique and its first positive energy is 4/a. Put r_f=Re Tr(U_f)/3, H=ΣK_e+vΣ_f(1−r_f), and u=av. The parameter a is the supplied kinetic/temporal-scaling parameter, not a spatial lattice spacing.

For a contractible R×S planar rectangle C, W_C=Tr(U_C)/3 has norm at most one. Write A=RS and P=2(R+S). Take torus side lengths sufficiently large, for example all at least 2max(R,S)+2; more generally the necessary projected condition is A≤L_xL_y/2. The theorem concerns these finite periodic ground states and their selected thermodynamic limit. It does not silently identify different boundary-selected infinite states.

There exist constants u_0>0 and C_0≥1, depending only on the fixed interaction geometry and the imported expansion, such that

|ω_u(W_C)| ≤ C_0^P (|u|/u_0)^A,  0≤u<u_0.

In particular, for 0≤u<u_0/C_0^4, the right side is at most [C_0^4 u/u_0]^A. The constants are not computed numerically. This is a spatial-loop upper bound, not a lower bound, a temporal-loop/static-charge confinement theorem, or a continuum limit.

## Exact applicability of the external expansion

The load-bearing source is Yarotsky, arXiv:math-ph/0412040, Theorem 1 and Section 2 (especially the ordinary polymer bound/count and the marked-insertion argument on printed pages 10–11): https://arxiv.org/pdf/math-ph/0412040 . Infinite-dimensional local spaces and unbounded classical local Hamiltonians are explicitly allowed. The paper treats periodic translation-invariant finite volumes. Its weak-star analyticity statement alone is NOT used as the needed support-dependent bound.

To match its block-vacuum hypothesis rather than merely its terminology, set h_x=(a/4)Σ_{i=1}^3K_(x,i), Λ_0={0,e_1,e_2,e_3}, and tilde h_x=Σ_{y∈x+Λ_0}h_y. Each tilde h_x is classical in a product Peter–Weyl basis, has a unique whole-block vacuum, and gap at least one. On a periodic volume Σ tilde h_x=4Σh_x. The perturbation tilde φ_x(z)=−zΣ_{i<j}r_(x,ij) has norm at most 3|z|. Hence Σ tilde h_x+Σ tilde φ_x(u)=aH−3u|Λ|. It has exactly the desired ground vector. Choose the source's relative-bound parameter small and fixed and then |z| small; bounded perturbations satisfy its form bound. No finite-dimensional truncation is needed.

The source gives ordinary activities bounded by ε^{|γ|}, with ε made arbitrarily small by its time-step and perturbation choices; the number of support/decorated polymers of size n through one point is at most c^n. For a bounded insertion O supported on S it gives marked activity bound ||O|| ε^{|γ_O|−|S|}. These norm estimates extend to complex bounded local couplings by the same sectorial-semigroup estimates and holomorphic bounded perturbation expansion used in Section 2. They are not estimates of a conjugated complex ground vector.

For W_C choose S to be ALL perimeter vertices viewed as outgoing cells, including the otherwise unused corner. This set is connected and |S|=P. Inserting this connected set into the marked support makes the same bounded-degree animal count applicable: after enlarging the geometry constant c, marked supports of size n≥P containing S number at most c^n. Internal Hilbert-space matrix indices are controlled by operator norms, not counted as finitely many spin colors.

## Uniform complex bound and zero-free normalization

For clarity the pinned-cluster estimate is an additional explicit standard mathematical import: the Kotecký–Preiss criterion in Fernández–Procacci, arXiv:math-ph/0605041, equations (2.7), (2.15), https://arxiv.org/pdf/math-ph/0605041 . If Σ_{γ incompatible γ_0}ρ_γ e^{a_γ}≤a_{γ_0}, the absolute pinned cluster sum is at most e^{a_{γ_0}}. The distinguished root may have zero activity; its pinned sum depends only on the ordinary activities.

Choose q=ceε≤1/4. Apply the criterion to weighted ordinary majorants ρ_γ=ε^{|γ|}e^{|γ|/2}, a_γ=|γ|/2. Overcounting incompatibility by a point in γ_0 gives

Σ_{γ incompatible γ_0}ρ_γ e^{a_γ} ≤ |γ_0|Σ_{n≥1}q^n ≤ |γ_0|/3 ≤ a_{γ_0}.

Thus the pinned sum is at most e^{|γ_0|/2}. Multiplying the marked root weight by e^{|γ_0|/2} as well controls an exponential weight in the TOTAL cluster size. Summing roots of size n≥P gives

Σ absolute marked clusters × e^{total size/2}
 ≤ ||O|| ε^(−P)Σ_{n≥P}(ceε)^n
 = ||O||(ce)^P/(1−q) ≤ ||O||(2ce)^P.

Set C_0=2ce, enlarged to at least one. This also gives an exponentially small tail in total cluster size. It supplies normal convergence uniformly in volume and imaginary-time extent, and the local thermodynamic/time limits uniformly on compact complex disks. Large wrapping or distant-boundary clusters are included in that tail, rather than ignored.

The finite-time complex expression is the fixed-vacuum quotient

<Ω_0,e^(−Nt_0 H(z)) O e^(−Nt_0 H(z))Ω_0> / <Ω_0,e^(−2Nt_0 H(z))Ω_0>.

Both semigroups use the SAME z; no adjoint or conjugated z occurs. The ordinary cluster expansion exponentiates the logarithm of the denominator and establishes its nonvanishing on the common disk. Introducing I+λO at the middle and differentiating log at λ=0 selects exactly one marked root. This explains both cancellation of vacuum clusters and the pinned estimate; one does not assume that the marked activity itself is small. For real u the time limit is the unique ground expectation. For complex z the normally convergent marked sum defines its holomorphic continuation and agrees with its finite-volume analytic ground germ near zero. Uniform complex spectral isolation on the entire disk is not needed or asserted.

## All-order center selection, including repeated insertions

Each independent link-center action U_e→ζU_e, ζ³=1, commutes with K, fixes the electric vacuum, and is compatible with Gauss invariance. Split each r_f into its fundamental and antifundamental characters. Every perturbation insertion carries ±∂f as an F_3 edge chain. An order-n term with W_C can survive only if C+Σ_{j=1}^n σ_j∂f_j=0 over F_3. Repeated plaquettes and opposite orientations are allowed.

This follows directly in the finite-time bounded-perturbation Dyson integrals: the free semigroups commute with the center actions, so a nonneutral vacuum matrix element is zero. It avoids taking traces of individual non-trace-class resolvent products. The denominator has nonzero constant coefficient; therefore division cannot introduce coefficients below the numerator's vanishing order. Uniform complex convergence passes these vanishing derivatives to the ground and thermodynamic limits.

Project chains onto the rectangle's coordinate plane: horizontal faces map to their unit cells, vertical faces to zero. This is a chain map. On the infinite plane a finite 2-chain with prescribed rectangle boundary is unique, because a boundary-free finite chain has equal adjacent coefficients and hence is zero. It has A nonzero cells. Each such cell requires at least one actual horizontal plaquette insertion; hence n≥A even if the chosen faces leave the plane.

On a periodic plane the kernel consists of constant sheets. The three possible projected fillings have support sizes A, L_xL_y−A, L_xL_y. Thus n≥min(A,L_xL_y−A), and the stated half-area restriction gives n≥A. The restriction is substantive: on a 4×4 torus a 3×3 rectangle has a seven-face complementary filling.

## Completion of the estimate

The holomorphic expectation F_C(z) is bounded by C_0^P on |z|<u_0 and has a zero of order at least A at zero. The higher-order Schwarz lemma, applied after division by C_0^P and rescaling the disk, gives |F_C(u)|≤C_0^P(|u|/u_0)^A. No geometric-series denominator is needed. Since P≤4A for positive integer side lengths, the additional smallness u<u_0/C_0^4 gives the stated pure area bound.

The hard imported input is the uniform complex marked expansion, including its norm estimate and ordinary support counting. Finite selection checks alone would not establish the theorem: analytic functions sin(Nz)^A are bounded on the real axis with the same vanishing order but have no uniform complex bound as N grows.

## Finite controls and provenance

The preregistered check.py verifies 19 exact finite identities/controls on the actual 192 oriented positive faces of a 4³ torus, projected boundary rank 15, all three affine fillings for four frozen rectangles, actual lifted boundaries, the adverse complement, repeated triple charge cancellation, and insufficiency of total flux alone. It uses 17.875 MiB and 0.0017 seconds in the preserved run. These are chain/arithmetic checks, not proofs of the external polymer estimates, and do not select u_0 or C_0. Original preregistration and raw JSON are retained. This derivation was frozen before reading the other lanes' completed proofs; root's proposed route and later scheduling messages were available and are credited.
