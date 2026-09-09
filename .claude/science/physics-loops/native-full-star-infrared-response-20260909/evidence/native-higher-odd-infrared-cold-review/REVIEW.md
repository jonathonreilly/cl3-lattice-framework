# Independent challenge of the higher-odd soft tail

PASS. Reviewed complete HIGHER_ODD_SOFT_TAIL.md SHA5adfb8e39dde484cdc1ddde64dc4cc464eb29e5c6bf2859b91240da89b0d5483, complete full-star infrared DERIVATION.md SHA58b7617ddd948491a69493c8aee09174d72ab2c85060dc04d844d6a2b022694c, and the thermodynamic parent's weighted coefficient-tail/convergence and GNS-generator sections. I reuse my independent72a29 review of the quasi-local creator/filter. I did not author the new factorial-soft-number argument. No numerical or physical run was performed.

## Decisive occupation inequality

Let Q_e count occupied modes with omega≤e. On an occupation basis vector of total energy in(0,e] and at least three particles, all occupied modes are soft, so Q_e≥3 and binomial(Q_e,3)≥1. On every other vector the desired left side is zero. Thus P_(0,e](H)P_>=3≤Q_e(Q_e−1)(Q_e−2)/6 is a positive diagonal inequality on the whole Fock basis. Hard occupied modes outside the energy window do not invalidate it; the right side may then be positive while the left is zero. Distinct ordered triples give exactly the factorial moment, not its square or an independence approximation:

    <xi,Q_e(Q_e−1)(Q_e−2)xi>
      = Σ_(i,j,k distinct soft) ||a_k a_j a_i xi||².

The factor1/6 is therefore correct. Exact-zero grids remain excluded by the imported antiperiodic domain and finite-grid counting bound.

## Local triple extraction

Define the graded commutator of an odd a with parity-homogeneous D by [a,D]_g=aD−(−1)^parity(D)Da. Since aΩ=0, applying three annihilators gives [a_k,[a_j,[a_i,D]_g]_g]_g Ω. The parities alternate odd→even→odd→even, hence the bracket types are anticommutator, commutator, anticommutator. Each resulting operator remains in the original local CAR algebra. In particular its exterior graded bracket with a Majorana vanishes; no support is added by using a delocalized annihilator.

The coefficient estimate |u_lj|≤C_B/sqrt(Ncell) and triangle inequality give operator norm≤2C_B m/sqrt(Ncell) times the prior norm at each step. Iteration gives the claimed m³/Ncell^(3/2) estimate. This does not require D to be Hermitian, a Wick-monomial expansion, orthogonality of different triple amplitudes, or smooth choices of Bloch eigenvectors. Repeated indices vanish by CAR; bounding their omitted count by the cube of the total soft-mode count is safe.

## Shell summation and actual subtraction

For the actual Z=Y−L, the thermodynamic parent supplies rapid weighted-l1 tails for L, so Z has uniform odd local approximants of arbitrarily high inverse-power accuracy. A shell of radius2^n has m_n=O(2^(3n)) and norm O(2^(-np)). The triple extraction constant sums m_n³||D_n||, so p>9 suffices. No fixed-volume support factor survives. The final whole-torus shell has volume O(L³) but norm O(L^-p), so it satisfies the same estimate when p>9.

The cancellation of the one-particle component is required only for the full vector ZΩ. It need not hold shell by shell, and the proof does not incorrectly assume it there. The factorial inequality is applied before the shellwise bound. Individual shells with one-particle components contribute zero to their triple annihilation, which is consistent with the estimate. Thus the argument genuinely improves the cubic generic-odd bound rather than merely relabeling it.

Combining S_e/Ncell≤C_D e³ with the triple bound gives mu_Z((0,e])≤K3² C_D³ e^9/6. Constants remain dependent on hopping/stiffness/locality data, with no explicit small numerical value claimed.

## Inverse moments and limit

With F(e)≤C e^9 and no zero atom, integration by parts yields

    integral_(0,e] E^-s dmu ≤ C e^(9-s)+sC integral_0^e x^(8-s)dx
                           =9C e^(9-s)/(9-s), 0<s<9.

For vector powers the squared norm uses s=2q, giving q<9/2, not q<9. The endpoints are not established or asserted divergent. Local spectral convergence from the full-odd parent, finite total mass, this uniform small-energy bound, and the bounded vanishing high-energy integrand give convergence of inverse moments. The limiting odd Fock space has no zero-energy kernel because its positive excitation multiplier is positive almost everywhere; this is an imported domain fact, not a consequence of a bound on the open interval(0,e] alone. The proof retains the required parent rather than forgetting that atom issue.

The r-particle generalization has the same conditional logic: one must first construct a uniformly quasi-local creator with the full vacuum image in N≥r. It does not prove that an arbitrary nonlocal number projection preserves quasi-locality. For r=3 the actual linear subtraction supplies the needed creator.

## Scope

This is an actual higher-odd singleton vacuum-response improvement under the same canonical Gaussian, antiperiodic, uniform-stiffness premises. It gives no infinite-volume nonzero higher-odd weight from L6, no control of mixed histories or excited-state operator action, and no interacting fixed-U resummation. No mathematical repair is requested before canonical integration.
