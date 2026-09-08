# Exact finite L4 flux isolation and the spectator corollary

Root supplied the proposed constant-square and quantitative Jensen route. The following derivation and integer checks were completed independently of any new author proof. Domain: the actual simple 4x4x4 periodic cubic graph, N=64, uniform real t=g lambda !=0, full native carrier, H0=t sum_e A_e. The full Gauss/CAR fixed-flux dictionary remains an input. This is an exact finite endpoint theorem, not a phase or a volume-uniform assertion.

## Constant square and its equality characterization

In a flux representative xi, set h=iK, K_ij=-2t xi_ij for i<j. The native ground energy in that sector is

E(xi)=-(1/4) Tr sqrt(h^2).

Every row of h has six entries of modulus 2|t|. Thus A=h^2 has A_ii=24t^2 and Tr A=24Nt^2. The row-sum bound gives ||h||<=12|t|, so every eigenvalue of A lies in [0,144t^2].

On the L4 graph any two distinct vertices joined by a two-step walk have EXACTLY two intermediate vertices. For displacement along two different axes these two paths bound an elementary square. For displacement two units along one axis, they are the two halves of a straight winding four-cycle. These exhaust the possibilities. There are no other off-diagonal A entries. The two path amplitudes each have modulus 4t^2. Their ratio is the hopping holonomy of their closed four-cycle. Consequently they cancel if and only if that hopping holonomy is -1.

Hence A=24t^2 I if and only if all elementary square and all straight winding hopping holonomies are -1. These cycles generate the integral cycle space of the torus, so their flux values determine the U(1) gauge orbit; within the sign-valued family they also determine exactly one Z2 gauge orbit. One can see the latter directly by fixing a spanning tree: trivial holonomy of the ratio of two assignments fixes every remaining chord sign.

The representative xi_(r,a)=(-1)^(sum_{b<a}r_b) exists periodically. Its native square holonomies are -1 and its straight winding holonomies are +1. In passing to h, the vertex-order orientation factor is +1 around a square and -1 around a straight winding; the factor (-i)^4 is +1. Thus every one of the corresponding hopping holonomies is -1, including seam squares and all three winding directions. The required constant square is attained. This proof does not import a flux-optimization theorem.

## Strict minimizer and an explicit separation

Scalar concavity gives

Tr sqrt(A) <= N sqrt(24)|t|,

with equality only if all eigenvalues equal 24t^2. For Hermitian A this means A=24t^2 I. Therefore the specified orbit is the unique minimizing magnetic flux orbit, and its ground energy is -N sqrt(24)|t|/4. This is uniqueness of the orbit, not of the many-body ground vector.

For a wrong sign-valued flux orbit, at least one off-diagonal A_ij is nonzero. Its two path contributions are equal instead of cancelling, so A_ij is +8t^2 or -8t^2. Hermiticity gives the symmetric entry as well. Therefore

sum_j (lambda_j(A)-24t^2)^2 = Tr(A-24t^2 I)^2 >= 128t^4.

For f(x)=sqrt(x) on (0,M], f''(x)<=-1/(4M^(3/2)). The tangent bound at mu=24t^2, extended continuously to x=0, is

sqrt(x) <= sqrt(mu)+(x-mu)/(2sqrt(mu))-(x-mu)^2/(8M^(3/2)).

Set M=144t^2 and sum; the linear term vanishes. The trace slack is at least

128t^4/[8(144t^2)^(3/2)] = |t|/108.

Multiplying by the native energy factor 1/4 proves every other flux-sector ground energy is at least |t|/432 above the minimizing sector ground. This is a conservative bound, not the exact sector gap.

In the minimizing orbit all positive active frequencies equal sqrt(24)|t|. K is full rank, and the active vacuum is unique. The spectator constraint allows each active occupation pattern with its corresponding spectator parity, so the first active excitation has energy sqrt(24)|t|. Thus the FULL H0 ground eigenspace is isolated by a gap at least |t|/432, is contained in the single minimizing flux orbit, and has dimension 2^(N/2-1)=2^31. Every state outside that eigenspace belongs either to an excited active pattern in that orbit or to another flux orbit, both already bounded.

## Consequence for small electric penalty

The hypotheses of the previously frozen spectator-selection theorem b1561c3326a62a6a9d045c0380e93bd3eff5c7f22b1bef63238c4ef46487d9b1 now hold for this actual finite uniform L4 model. Therefore the positive-overlap canonical effective Hamiltonian on this 2^31-dimensional unperturbed ground eigenspace, for H0+uD, is scalar through order five in u. This uses the proved small-cut and incident-pair selection argument; it does not compute the first surviving coefficient. Sixth order is only the first support-allowed order. Finite isolation ensures analytic perturbation theory near zero, but no explicit radius or splitting coefficient is asserted here.

At t=0 this argument does not apply. No result for larger tori, inhomogeneous magnitudes, nonzero-u ground-state phase, thermodynamic flux gap or preparation follows. In particular the uniqueness above does not remove the exact spectator ground degeneracy at u=0.

## Finite controls and limits

check.py has no author imports or eigensolver. It constructs the actual 64x64 integer square matrix at t=1, confirms the constant square and all 240 basic-cycle phases, and checks all coordinate-pair path multiplicities. Four single-edge mutations and three winding-only twists yield nonzero square entries and the variance floor. The winding twists preserve every plaquette phase and demonstrate why plaquettes alone would be insufficient. Exact rational arithmetic checks the 1/108 and 1/432 factors. 5091 predicates passed in 0.134 seconds with 16.234375MiB reported RSS. These controls support the literal finite geometry; the all-flux conclusion follows from the two-path/equality proof, not an unperformed enumeration of 2^129 flux sectors.
