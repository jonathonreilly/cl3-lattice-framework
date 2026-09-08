# FiniteL4 magnetic space-group reduction of the sixth operator

Research proof, awaiting independent review. Inputs: supplied uniform full CAR/Z2 native dictionary, actualL4 unique minimizing flux orbit and isolated full-rank active vacuum; canonical electric correction scalar through5; sixth correction scalar plus opposite-sublattice spectator bilinears. No coefficient is evaluated here. An exact finite signed-orbit certificate below is load-bearing only on64 vertices.

## Lift graph automorphisms to the full physical Hamiltonian

In canonical vertex order i<j the full native hopping is -it gamma_i gamma_j X_{ij}, and D is the degree-centered square in link Z. For any cubic graph automorphism f define kappa_e=+1 if f(i)<f(j) and -1 otherwise. A unitary permutes the complex matter modes c_i to c_{f(i)}, permutes link qubits e to f(e), and conjugates each image link by Z when kappa_e=-1. Thus X_e maps to kappa_e X_{f(e)}, while Z_e merely permutes. The two orientation signs cancel in the hopping term. Uniform t sum A and uD are invariant. Matter parity and vertex Gauss operators permute, so this is a unitary on the physical even-Gauss carrier, not an arbitrary change of Hamiltonian or a symmetry only of its spectrum.

The unique minimizing flux orbit must be preserved by every such symmetry. Fix the pi representative xi and its canonical skew matrix K_ij=-2xi_ij for i<j. For each selected f solve signs g_i such that

K_{f(i),f(j)}=g_i g_j K_{ij}.

After the unitary, the representative on image edge f(e) has sign kappa_e xi_e. The gauge transformation at image vertex f(i) with sign g_i restores xi, since g_i g_j kappa_e xi_e=xi_{f(e)}. In the fixed-representative physical Fock description the induced transformation is therefore c_i -> g_i c_{f(i)}, so both active and spectator Majoranas transform by the SAME signed permutation O. The gauge correction here is the Gauss identification between representatives; it is not a new physical perturbation. A global ambiguity g->-g has no effect on bilinears.

The equation above is precisely invariance of the active quadratic form under O. Its simple active vacuum is preserved up to phase. The full physical unitary preserves total matter parity; the resulting action on the allowed spectator-parity space is well-defined. Equivalently an orthogonal O commuting with the full-rank complex structure lies in its unitary subgroup and has real determinant+1, so it does not flip active or spectator parity individually. No projection onto the wrong parity sector is introduced.

## Canonical effective covariance

The full unitary commutes with H(u)=H0+uD, hence with the isolated contour projector Pi(u) and its u=0 projector P. It commutes with P Pi P, its positive inverse square root and P H Pi P. Consequently the positive-overlap canonical Hamiltonian commutes with the induced spectator representation at every order. At order6 write

K6=cI+sum_{i<j} b_ij (i bar_gamma_i bar_gamma_j),

with real b_ij and antisymmetric extension b_ji=-b_ij. Same-sublattice entries vanish by the separately proved active-reality/Hermiticity selection rule. Covariance imposes

b_{f(i),f(j)}=g_i g_j b_{ij},

with the orientation sign when an image pair is re-sorted. Thus a signed pair-orbit cycle with net minus sign forces its entire orbit coefficient to zero. Distinct bilinears remain linearly independent in the fixed spectator parity space atN64, so these are genuine coefficient constraints.

## Exact finite signed-orbit certificate

check.py constructs the actual64x64 integer K and eight generators: three unit coordinate translations, three coordinate reflections r_a->-r_a, and adjacent coordinate swaps(0,1),(1,2). Each generator's signs are solved from the graph starting g_0=1 and checked on EVERY matrix entry. The complete generator permutations and signs are saved. All1024 opposite-sublattice unordered pairs are propagated through their exact signed orbits; any inconsistent sign cycle is recorded as a forced-zero orbit. This is a finite linear constraint calculation, not an eigensolver, sampling result or extrapolation to larger tori.

5657 exact predicates give four pair orbits:

-192 nearest-neighbor pairs: one free coefficient;
-384 distance3 pairs of displacement type(2,1,0): forced zero;
-256 distance3 pairs of type(1,1,1): forced zero;
-192 distance5 pairs of type(2,2,1): forced zero.

The invariant real antisymmetric opposite-color matrix space has dimension1. The nonzero K itself lies in that space, so b is proportional to K. Therefore a separately certified coefficient of the ordered pair(0,16) determines the entire nonscalar sixth-order operator on this finite uniformL4 endpoint, assuming the reviewed inputs and the lift above. If that coefficient vanishes, symmetry alone cannot establish a nonzero higher-order splitting. No nonzero value is assumed.

This special finite symmetry result does not assert the same one-dimensional space on larger or anisotropic tori, nonuniform couplings or altered boundary sectors. It does not select the Hamiltonian, establish a nonzero-penalty phase, or prove that a formal leading coefficient dominates at a stated finite radius. The checker production remains scoped to its single adjacent coefficient until this bridge is independently reviewed.
