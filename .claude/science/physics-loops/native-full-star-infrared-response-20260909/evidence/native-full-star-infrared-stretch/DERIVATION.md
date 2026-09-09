# Full odd-star infrared response — candidate derivation

Status: provisional conditional-support, not independently reviewed. Started 2026-09-09 after PR8063. This is an analytic stretch on the full singleton star response, not a new numerical run or the full sixth-order effective Hamiltonian.

## Contract and source

Use the exact supplied domain of PR8063, head aea1602ec35a045e5b06be563acef0c28dadcbd4, and its parent PR8062, head df8112d1642bec7aaaacd380036087b03cdb0173: canonical pure Gaussian active vacuum, pi gauge, cubic antiperiodic L=4M, M>=32, nonzero hopping t, positive uniform wrong-pair stiffness relative to the same vacuum reference energy. H_L means H_pi,L-E0,L >=0, not the wrong-flux Hamiltonian. H is its gapless infinite Gaussian GNS generator. Magnetic cell size is fixed. No empirical or fitted input, extra axiom, active spectral gap, finite-L6-to-infinite-volume positivity, or full effective-operator locality is allowed.

The previous theorem supplies odd Y_L,v with chi_L,v=Y_L,v Omega_L equal to the actual third-order double-resolvent star transition, uniform norm bounds and odd ball approximants with errors C_p(1+r)^(-p) for every p. The family converges locally in operator norm followed by uniform tails, and the vacuum states converge locally. The extracted Majorana coefficient family c_L,vj has uniformly rapid tails and converges in every weighted l1 norm. These premises are conditional source theorems, not formal audit grades.

Target: prove infrared control and a thermodynamic limit of the FULL chi response, including its higher odd quasiparticle component. Existing PR8062 proves an inverse-kernel row l2 estimate only for P1 chi. A proof here would remove the one-particle restriction for the singleton-star response. It would not identify other sixth-order histories, prove an interacting phase, or establish a nonzero infinite-volume nonlinear weight.

## 1. A local odd operator cannot concentrate arbitrary mass at zero energy

Diagonalize the finite canonical positive quadratic excitation Hamiltonian:

 H_L = sum_lambda omega_lambda a_lambda^* a_lambda,
 {a_lambda,a_mu^*}=delta_lambda, a_lambda Omega_L=0.

The Bloch label lambda=(k,b) uses a fixed number of bands b per magnetic cell. Frequencies are the stated 4|t| sqrt(sum_i sin^2 k_i), with the appropriate fixed-cell multiplicity/folding. Fourier normalization and the normalized internal eigenvectors give

 a_lambda = sum_j u_lambda,j gamma_j,
 |u_lambda,j| <= C_B / sqrt(Ncell),

with C_B independent of L,k,b. One may take a conservative fixed cell-dependent C_B; no smooth eigenvector gauge or node value is required. This follows by composing the unitary cell Fourier transform with a normalized finite-dimensional Bloch eigenvector and the fixed Majorana-to-annihilation normalization.

Let D be any odd operator supported on m real Majorana sites, not assumed Hermitian. Graded CAR locality gives {gamma_j,D}=0 outside its support. Since a_lambda kills the vacuum,

 a_lambda D Omega_L = {a_lambda,D} Omega_L,
 ||a_lambda D Omega_L|| <= 2 C_B m ||D|| / sqrt(Ncell).             (1)

There is no assumption that D creates only one particle. The local CAR algebra contains operators of all degrees up to its support size.

On the full excitation Fock basis define P_epsilon=1_(0,epsilon](H_L) and Q_epsilon=sum_(omega_lambda<=epsilon) a_lambda^* a_lambda. Then

 P_epsilon <= Q_epsilon.                                          (2)

Indeed, a nonvacuum occupied configuration of total energy at most epsilon contains at least one mode, every occupied mode has frequency at most epsilon, and Q_epsilon is a nonnegative integer on all configurations. Both sides are diagonal in that same occupation basis. Odd D Omega_L has no vacuum component. Therefore (1)-(2) imply

 ||P_epsilon D Omega_L||^2 <= 4 C_B^2 m^2 ||D||^2 S_L(epsilon),
 S_L(epsilon) = Ncell^(-1) # {lambda: omega_lambda<=epsilon}.        (3)

The conical canonical dispersion and half-shifted grids give a constant C_D such that

 S_L(epsilon) <= C_D epsilon^3                                    (4)

for all epsilon>0 and all allowed L. To see the finite-grid uniformity, near each of finitely many nodes sin distance >=(2/pi) distance on its nearest-node cube. The mode count in radius O(epsilon/|t|) is at most a constant times (L epsilon/|t|+1)^3. The AP grid has omega_min >= c |t|/L: below that the count is zero; otherwise the +1 is absorbed in L epsilon/|t|. Dividing by Ncell proportional to L^3 proves (4). Outside fixed node cubes the frequencies are bounded below; enlarge the same constant to cover all epsilon. The fixed band multiplicity only changes C_D. An exact-zero grid or a flat zero band would invalidate this step.

## 2. Rapid quasi-locality extends the bound to the full star vector

For any uniformly rapidly quasi-local odd family Y_L,v, take odd approximants at dyadic radii r_n=2^n and telescope:

 D_L,0=Y_L,v,1; D_L,n=Y_L,v,2^n-Y_L,v,2^(n-1).

On each finite torus the sequence eventually becomes the exact whole-torus operator; equivalently append its final tail as a whole-torus shell. Volume growth gives m_L,n<=C_V(1+2^n)^3, while ||D_L,n||<=C_p' 2^(-np) for every fixed p. Hence

 K_Y = sup_L 2 C_B sum_n m_L,n ||D_L,n|| < infinity,               (5)

using any p>3. These are actual bounds on local operators, not a potentially ill-conditioned expansion in Wick monomials. Triangle inequality applied to (3) gives

 mu_L,Y((0,epsilon]) := ||P_epsilon Y_L,v Omega_L||^2
                      <= K_Y^2 C_D epsilon^3.                    (6)

Also ||Y_L,v Omega_L||<=C0. Every odd sector is included. No independent-particle approximation to chi has entered.

As a second occupation-basis check, for s>0 and every nonempty occupied configuration,

 (sum_occupied omega)^(-s) <= sum_occupied omega^(-s).

Thus inverse-energy moments can also be bounded by sum_lambda omega_lambda^(-s)||a_lambda D Omega||^2 for each local D. The spectral-count proof above provides the more useful uniform small-energy tail and avoids a separate singular lattice sum for each s.

## 3. Inverse-energy domains and uniform integrability

For any 0<s<3, Stieltjes integration using F(epsilon)<=C_Y epsilon^3, C_Y=K_Y^2 C_D, gives

 integral_(0,epsilon] E^(-s) dmu_L,Y(E)
 <= [3 C_Y/(3-s)] epsilon^(3-s).                                 (7)

The E=0 boundary term vanishes by the same cubic bound. Above any fixed E_*>0 the inverse moment is bounded by E_*^(-s) C0^2. In particular

 sup_L ||H_L^(-1) chi_L,v||^2 < infinity,
 sup_L <chi_L,v,H_L^(-1)chi_L,v> < infinity.                        (8)

More generally chi lies in Dom H_L^(-q) with uniform norm for every 0<q<3/2. Fractional inverses refer to the nonvacuum sector; oddness removes the zero vacuum. The endpoint q=3/2 is not supplied. No nonzero node value or sharp threshold claim is made.

## 4. Thermodynamic spectral and inverse-response limits

Let mu_L,Y be the positive spectral measure of chi_L,v. For each fixed real time t,

 integral exp(-itE) dmu_L,Y(E)
 = omega_L(Y_L,v^* tau_L,t(Y_L,v))
 -> omega(Y_v^* tau_t(Y_v)).                                     (9)

The reference energy cancels since H_L Omega_L=0. Replace Y by fixed-ball approximants, use compact-time local dynamics and local-state convergence, and then send their uniform tails to zero. The right side is the characteristic function of the GNS spectral measure mu_Y of Y_v Omega, continuous at zero.

For an elementary tightness argument, the quadratic finite-range generator obeys ||[H_L,D]||<=C_H m ||D|| for a local operator D on m sites. Equation (5) therefore gives a uniform bound on ||H_L Y_L,v Omega_L||. The dyadic commutator series is norm convergent and its closed derivation limit is [H_L,Y_L,v]; the same construction works in infinite volume. Thus the spectral measures have uniformly bounded second energy moments. Smooth compactly supported functional calculus follows from (9) by Fourier inversion and dominated convergence; the moment bound supplies tightness and approximation by continuous compactly supported functions. This proves weak convergence of the finite positive measures, with their total masses also convergent.

The cubic bound passes to the limiting measure (use open low-energy intervals and then monotone endpoints). There is no zero-energy atom on the odd Fock subspace: the one-particle multiplier is positive almost everywhere, and each positive-particle-number sum has no zero kernel. Alternatively the continuous cutoff version of (6) directly excludes such an atom. Therefore (7) holds in the limit, and uniform low-energy integrability plus weak convergence implies

 integral E^(-s) dmu_L,Y -> integral E^(-s) dmu_Y,  0<s<3.           (10)

At high energy E^(-s) is bounded and vanishes; near zero (7) controls the omitted part uniformly. In particular the full singleton susceptibility and squared inverse-vector norm have finite thermodynamic limits. These are scalar/matrix-element limits across the prescribed local identifications, not a global isometric embedding of finite periodic Fock spaces.

Polarization with Y_v+zY_w, z in {1,-1,i,-i}, yields convergence of fixed-position cross matrix elements <chi_L,v,H_L^(-1)chi_L,w>. The same local proof applies to a fixed union of two centers.

## 5. Isolating the higher odd contribution without nonlocal number-projector assumptions

Define L_L,v=sum_j c_L,vj gamma_j using the actual Gaussian extraction coefficients in PR8063, and Z_L,v=Y_L,v-L_L,v. Weighted l1 bounds supply uniformly rapid odd ball approximants to L, and its weighted coefficient convergence supplies the same local thermodynamic limit. On the vacuum,

 L_L,v Omega_L=P1 chi_L,v,
 Z_L,v Omega_L=P_(>=3) chi_L,v.

The infinite identity holds by the parent's Gaussian extraction theorem. Thus Z satisfies all hypotheses in sections 1-4. Consequently the higher odd weight ||Z_L,v Omega_L||^2 and its inverse-energy moments for 0<s<3 converge to finite nonnegative limits. H commutes with quasiparticle number, so the full scalar susceptibility is the sum of its one-particle and higher odd parts, without cross terms. This argument does not require independently asserting convergence of nonlocal finite-volume number projections.

A positive value at L6 does not bound the limit from below, especially since L6 is outside the uniform L=4M,M>=32 domain. This theorem establishes existence/control, not positivity, of the infinite higher odd response.

## 6. Full singleton inverse-kernel row bound from graded locality

Let v range over all translates and finitely many internal sites of the magnetic cell. Uniform rapid odd quasi-locality implies

 ||{Y_L,v^*,Y_L,w}|| <= g_L(v,w),
 sup_(L,v) sum_w g_L(v,w) <= G < infinity.                         (11)

For large d(v,w), choose disjoint ball approximants of radii less than d/3; their graded anticommutator is zero. Expanding the error bounds the left side by a constant times C_p(1+d)^(-p), with p>3. At small distances use 2C0^2. Periodic volume growth and finitely many internal types give the uniform summable bound, including seam/twist signs.

For any finitely supported coefficients a, A=sum_v a_v Y_L,v obeys

 ||A Omega_L||^2 <= ||A||^2 <= ||{A^*,A}||
 <= sum_vw |a_v||a_w|g_L(v,w) <= G sum_v|a_v|^2.                   (12)

Hence V_L:e_v -> chi_L,v extends to a bounded map from site l2 to active Fock space, norm <=sqrt(G); the same holds in infinite volume. This does not assume exponential vacuum clustering or an active gap. Graded locality controls the anticommutator even when ordinary vacuum correlations are long ranged.

Define the FULL singleton kernel

 T_L,vw=<chi_L,v,H_L^(-1)chi_L,w>.

It is Hermitian and positive as a form on finite site sequences. By (8) and (12), the conjugated row is V_L^* H_L^(-1)chi_L,v, so

 sum_w |T_L,vw|^2 <= G ||H_L^(-1)chi_L,v||^2 <= C_T.              (13)

The infinite kernel has the same bound, and each fixed entry converges by (10). The argument also applies to the higher odd Z family. It proves a full response row l2 bound, not row l1, bounded global convolution-operator norm, strong l2 convergence of finite rows, or locality of every sixth-order term.

For real spectator coefficients CAR gives ||sum a_w beta_w||=||a||2; for complex coefficients it gives the safe bound sqrt(2)||a||2. Thus (13) bounds the corresponding singleton spectator linear fields and local commutators of their self-adjoint quadratic realification, exactly as in the one-particle parent but now including all active odd intermediate sectors. The full physical sixth-order effective Hamiltonian may contain other histories and cancellations; it is not identified here.

## Decisive checks planned, not yet run

1. Exact finite Fock occupation inequalities including all odd sectors, and an explicit non-Hermitian local CAR creator, with a mutation that incorrectly replaces total-energy projection by one-particle projection.
2. Exact spectral-tail summation and endpoint distinction on a discrete conical toy spectrum; no toy result advertised as the native infinite theorem.
3. Overlapping odd CAR creators: compare their Gram matrix with the operator anticommutator bound; demonstrate that individual-vector inverse bounds alone do not give a row bound absent the bounded translate map.

Review should challenge (1)-(2), finite-grid uniformity, dyadic support counting, spectral-measure passage, use of oddness and the graded Bessel estimate. The desired conclusion is not a review premise.
