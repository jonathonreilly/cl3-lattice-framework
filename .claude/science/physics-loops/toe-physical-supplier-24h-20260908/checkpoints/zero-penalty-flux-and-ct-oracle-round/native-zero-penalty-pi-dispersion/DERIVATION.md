# Finite π-flux endpoint dispersion with canonical seams

## Domain and source

Use the full native Gauss dictionary and U=0 endpoint proved in native-zero-penalty-endpoint/DERIVATION.md, not the low-charge U1 dictionary. Coordinates r=(r0,r1,r2) label a rectangular torus with even extents La>=4, ordered lexicographically. Every positive-axis edge is an unordered edge in the native Hamiltonian with its generator canonically oriented from smaller to larger index. Set t=g lambda, with a common real lambda. We assume t!=0 except in the explicitly trivial limit. The supplied link-X representative is

xi_a(r)=(-1)^(sum_{b<a} r_b),

optionally multiplied by tau_a in {+1,-1} on the a seam r_a=La-1. Elementary plaquette Wilson products are -1. Straight winding products are tau_a: the alternating earlier-coordinate factor appears an even number of times. These are specified flux sectors, not a proof that any sector minimizes energy.

## Why canonical seams matter

The real antisymmetric Majorana matrix has K_ij=-2t xi_ij for i<j. Along a positive-axis nonseam edge, its row r, column r+e_a entry is -2t xi_a(r). On the seam the positive-axis orientation is reversed relative to canonical order, so that entry is +2t xi_a(r). This sign cannot be discarded while retaining the same supplied xi.

Define T_a on functions by (T_a f)(r)=f(r+e_a), with boundary multiplier beta_a=-tau_a when the shift wraps. Let eta_a(r)=(-1)^(sum_{b<a}r_b). The exact matrix identity is

K=-2t sum_a D_a,   D_a=eta_a(T_a-T_a^dagger).

eta_a commutes with T_a. For b<a, eta_a anticommutes with T_b and T_b^dagger, including the seam because L_b is even. Thus D_a D_b+D_b D_a=0 for a!=b. Also D_a^2=T_a^2+(T_a^dagger)^2-2I. Consequently

(iK)^2=4t^2 sum_a [2I-T_a^2-(T_a^dagger)^2].

This is an exact finite matrix identity, without a continuum approximation.

## Fourier blocks and multiplicities

Allowed momenta are k_a=2 pi(n_a+alpha_a)/La, n_a=0,...,La-1, where alpha_a=1/2 for tau_a=+1 and alpha_a=0 for tau_a=-1. The squared eigenvalues are

omega(k)^2=16t^2 sum_a sin^2(k_a).

The square identity alone does not assign the signs or their multiplicities. For that, group the four Fourier momenta (kx+s0 pi,ky+s1 pi,kz), s0,s1 in {0,1}. Choose kx and ky with n in the first half of their ranges and kz in its whole range. In this four-dimensional block,

iK=4t [sin(kx) Z_0 + sin(ky) X_0 Z_1 + sin(kz) X_0 X_1].

The three displayed real Hermitian Pauli matrices square to I and anticommute. Their linear combination has trace zero and square (sum sin^2 k)I. Hence every nonzero block has eigenvalues +4|t|sqrt(sum sin^2 k) and -4|t|sqrt(sum sin^2 k), each twice. A zero block has four zero eigenvalues. This constructs all N=L0 L1 L2 eigenvalues and fixes the frequency convention. Equal frequencies from different blocks retain their separate multiplicities.

For the requested untwisted Wilson representative tau=(+,+,+), every coordinate has antiperiodic momenta. For even La none has sin k_a=0. K therefore has full rank N and no active zero Majoranas. This is true for La=4 as well as larger even extents.

For any twist with at least one tau_a=+1, there are still no active zeros. Only tau=(-,-,-) makes every coordinate periodic. Then exactly the eight momenta k_a in {0,pi} have zero squared eigenvalue, giving nullity eight and rank N-8. In the four-block construction these are two zero blocks, not eight independently signed positive frequencies. At t=0 all N active Majoranas are zero regardless of twist.

A complex diagonal change of one-particle basis f(r)->i^(sum_a r_a) f(r) can express the same answer using cosine dispersion. Its boundary multiplier changes by i^La=(-1)^(La/2); thus the resulting boundary condition is (-1)^(La/2+1) tau_a. Using cosine with unchanged boundary twists would give incorrect finite-volume zero modes. This one-particle basis change is only an alternative spectral calculation, not an additional real Majorana gauge transformation.

## Physical fixed-flux energies

The parent exact gauge quotient identifies each flux sector with the even N-mode Fock space, dimension 2^(N-1). If rank K=2r, its energies are sum_{j=1}^r omega_j(n_j-1/2), and each active occupation pattern has physical multiplicity 2^(N-r-1). The N spectator Majoranas together with active zeros supply this count; individual odd spectators are not asserted to be physical operators.

For tau=(+,+,+), r=N/2, so each pattern and the ground energy have multiplicity 2^(N/2-1). For tau=(-,-,-), r=N/2-4 and the ground/pattern multiplicity is 2^(N/2+3). Other twists have the full-rank multiplicity. Accidental equality of excited pattern energies adds multiplicities. The sector ground energy can be written exactly as

E0(tau)=-|t| sum_{all allowed k} sqrt(sum_a sin^2 k_a).

Zero momenta contribute zero, so this expression covers all twists. It is a finite sum for specified sectors; no minimization among all exponentially many flux sectors has been performed. The full native carrier still has 2^E states after summing all sectors, as proved by the parent dictionary; the eight sectors here are only the π-plaquette family with different winding twists.

## Exact controls and limits

The prospective checker independently constructs sorted-edge K on 4x4x4 and 4x4x6, for all eight twists. It verifies the literal D identity, all three pair anticommutators, the squared finite-difference identity, and ranks by exact Fraction elimination. Ninety-seven predicates pass. A direct seam-omission adverse comparison changes nullity from zero to eight, so the seam issue is discriminating. This is a direct alternative, not a subprocess mutation campaign. No floating diagonalization is used.

The result solves the finite dispersion in these supplied backgrounds only. It does not show cubic flux optimality, a three-dimensional phase, Lorentz symmetry, a physical species count, or integrability at nonzero U. No flux-phase theorem is imported.
