# Mobile low-charge stability: an improved four-hop bound

Root supplied the six-hop candidate. The same conditional theorem holds with the sharper coefficient four. Fix the full native edge-qubit carrier on a finite even periodic cubic graph with each extent at least4, relaxed fixed magnetic-cycle constraints, and the supplied low-charge subspace |G_v|<=1. Use G_v=sum incident n_e-3, Q_v=epsilon_v G_v, D=sum_v Q_v², and one hopping term per UNDIRECTED edge. The supplied real Hamiltonian is

H=J sum_p F_p(I-S_p)+U D+t T_low,
T_low=sum_{undirected e} P_low T_e P_low,
J>=0,U>0,t real.

Native order-dependent Pauli phases and the common-carrier dictionary are retained. These are still supplied gates, domain and coefficients; the statement is not an axiom-selected physical mass or dynamics.

## Conservation and allowed amplitudes

Every gated ring preserves each integer G_v and therefore D. F_p commutes with the native Hermitian cycle involution S_p, so F_p(I-S_p)>=0. This follows directly from their commuting projector/involution algebra, or from the phase-correct W image F_p(I-X_p). Relaxing the fixed-cycle code does not remove the phases from arbitrary native state vectors.

For a nonzero native hopping column, B_i differs from B_j. On the low-charge domain B_v=-(-1)^G_v, so exactly one endpoint is charged and one neutral. If the source has G=s=+1 or-1 and the target G=0, the common edge toggle changes both by delta=1-2n_e. Remaining in the low-charge domain forces delta=-s. The final G pair is0,-s. Bipartite epsilon changes sign across the edge, so the same signed Q moves to the target. Thus positive and negative defect counts, and hence D, are conserved. Each permitted matrix element has magnitude one: T_e=(i/2)A_e(B_i-B_j), with |B_i-B_j|=2 and native A amplitude of unit modulus. The reverse column has the complex-conjugate amplitude. No replacement by an unsigned Hamiltonian is made.

## Four choices per charged source

A source with G=+1 has four occupied incident bits, and only these four can be flipped because delta must be-1. A source with G=-1 has two occupied bits, hence four vacant bits; only those can be flipped because delta must be+1. Requiring a neutral target can only reduce the count. Therefore any configuration with D charges has at most4D permitted undirected-edge hops. Each permitted edge is counted exactly once, at its unique charged endpoint; there is no extra orientation factor. Distinct physical edges flip distinct bits, so they lead to distinct configurations on this simple cubic graph. The degree-six bound6D is valid but unnecessarily loose.

For the Hermitian block T_D on the fixed-D subspace, the absolute row and column sums are at most4D. Equivalently, bounding each unordered off-diagonal contribution by |z_x|²+|z_y|² gives |<z,T_D z>|<=4D||z||². Hence ||T_D||<=4D. Combining blocks and ring positivity proves the operator inequality

H >= (U-4|t|) D.

The row-capacity coefficient is attained by an actual D2 configuration below; this establishes sharpness of the simple counting bound, not of the operator norm or stability threshold. Native phases may prevent spectral saturation. No stronger spectral optimality is asserted.

## Vacuum ground states and charged-sector bounds

On ice, G=Q=0 and every B_v=-1, so every native T_e vanishes. A phase-correct uniform vector in any nonempty ice ring component is annihilated by all F_p(I-S_p). Thus it remains an exact zero-energy vector for all t. If U>=4|t| the operator lower bound is nonnegative, so these are exact ground states. This does not assert their uniqueness; frozen ring components are allowed. At equality additional charged zero states are not excluded. Below the threshold the bound is inconclusive, not an instability proof.

Global neutrality sum Q=0 on the closed bipartite torus and Q in{-1,0,1} imply D is even. Every nonzero charged block has D>=2. For U>4|t|,

inf spec(H restricted D>0)-E0 >=2(U-4|t|).

In particular the D2 block has this lower bound. This is a charged-sector gap above the neutral ground energy, not a gap to neutral excitations and not a proof that the lowest charged eigenstate necessarily lies in D2 rather than a higher-D block.

For any ordered pair of distinct vertices, the previously proved directed-path support construction supplies a nonempty fixed signed-charge vector with that pair. Let phi be its phase-correct uniform ring-component state. Its ring energy is zero and D=2. Every permitted single hop changes the charge-position vector, so it maps phi's support to an orthogonal fixed-charge-position subspace. Therefore <phi,T_low phi>=0, even with all native phases. This yields the variational upper bound

inf spec(H restricted D2)<=2U.

When t!=0, positions are not conserved and this trial state is not generally an eigenstate. The combined rigorous statement is2(U-4|t|)<=E_D2<=2U in the strict stability region, plus the all-charged lower bound. It is not a fixed-position spectral comparison under mobile dynamics. At t=0 it reduces to the earlier exact static sector result.

## Exact bounded controls and limits

Before computation the four-choice refinement was preregistered. Thirty local degree-two/degree-four bit patterns each have exactly four allowed source bits, assuming neutral targets. An actual L4 ice seed has all degrees3 and no hopping. Toggle the two edges on the directed electric path (0,0,0)->(3,0,0)->(2,0,0). It yields charges-1,+1 at its endpoints and exactly eight permitted hops, attaining4D. Bounded depth neighborhoods of this configuration test the actual native ordered-star Pauli phases, reverse Hermitian amplitudes, signed charge preservation and row bound. They are not a complete charged-sector census or a spectral diagonalization. Source/raw counts disclose repeated depth neighborhoods.

No charge mobility, deconfined quasiparticle, nonconfinement at nonzero t, gauge-field gap, photon, continuum limit, or physical mass is proved. The sign and sector bounds are finite operator statements for the supplied Hamiltonian and low-charge domain. Changing coordination, including parallel-edge graphs, allowing |G|>1, dropping the low-charge projection, using negative J, or retaining the original fixed-cycle state constraint requires another analysis.
