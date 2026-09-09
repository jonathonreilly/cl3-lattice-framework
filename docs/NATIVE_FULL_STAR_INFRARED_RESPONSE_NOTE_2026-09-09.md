---
claim_id: native_full_star_infrared_response_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied canonical Gaussian reference and uniformly quasi-local native star creator: full odd cubic and higher-odd nine-power spectral bounds, inverse moments and thermodynamic susceptibility, including higher odd sectors, full singleton-kernel row l2 control and an absolutely summable higher-odd channel."
upstream_dependencies:
  - native_star_thermodynamic_limit_note_2026-09-09
  - native_uniform_quasilocal_star_vertex_note_2026-09-09
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
runner: scripts/native_full_star_infrared_response_2026_09_09.py
---

# Full odd-star infrared response and thermodynamic susceptibility

**Status:** conditional-support; trace class upstream_support. This theorem controls the full singleton-star response in the supplied Gaussian reference. It does not identify the full sixth-order effective Hamiltonian or prove an interacting phase.

Use the [thermodynamic star construction](NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md), [uniform quasi-local creator](NATIVE_UNIFORM_QUASILOCAL_STAR_VERTEX_NOTE_2026-09-09.md), and [canonical dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md).

The full response has a uniform cubic low-energy spectral bound. After the actual one-particle part is removed, the bound improves to ninth power and the higher-odd singleton kernel has absolutely summable spatial rows, converging in l1 as the volume grows. The one-particle channel and other mixed histories retain their separate obligations.

## Contract and source

Use the exact supplied domain of PR8063, head aea1602ec35a045e5b06be563acef0c28dadcbd4, and its parent PR8062, head df8112d1642bec7aaaacd380036087b03cdb0173: canonical pure Gaussian active vacuum, pi gauge, cubic antiperiodic L=4M, M>=32, nonzero hopping t, positive uniform wrong-pair stiffness relative to the same vacuum reference energy. H_L means H_pi,L-E0,L >=0, not the wrong-flux Hamiltonian. H is its gapless infinite Gaussian GNS generator. Magnetic cell size is fixed. No empirical or fitted input, extra axiom, active spectral gap, finite-L6-to-infinite-volume positivity, or full effective-operator locality is allowed.

The previous theorem supplies odd Y_L,v with chi_L,v=Y_L,v Omega_L equal to the actual third-order double-resolvent star transition, uniform norm bounds and odd ball approximants with errors C_p(1+r)^(-p) for every p. The family converges locally in operator norm followed by uniform tails, and the vacuum states converge locally. The extracted Majorana coefficient family c_L,vj has uniformly rapid tails and converges in every weighted l1 norm. These premises are conditional source theorems, not formal audit grades.

The result proves infrared control and a thermodynamic limit of the full chi response, including its higher odd quasiparticle component. The parent proves an inverse-kernel row l2 estimate only for P1 chi. Here that restriction is removed for the singleton-star response. Other sixth-order histories, an interacting phase, and positivity of the infinite-volume nonlinear weight remain open.

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

## 6. Stronger nine-power tail for the higher odd component

For the actual Z family constructed in section 5, the cubic bound strengthens to a nine-power bound.

Write N_epsilon=sum_{omega_l<=epsilon} a_l* a_l. On occupation vectors with particle number>=3 and total energy in(0,epsilon], every occupied mode is soft. Thus

 1_(0,epsilon](H) P_(>=3) <= N_epsilon(N_epsilon-1)(N_epsilon-2)/6.

This remains a diagonal positive operator inequality on the entire Fock basis, with the left side understood to include P_(>=3). Consequently, using CAR,

 ||1_(0,epsilon](H) Z Omega||²
 <= (1/6) sum_{i,j,k soft, distinct} ||a_k a_j a_i Z Omega||².

For a local parity-homogeneous D supported on m real Majoranas, move each annihilator through D using the GRADED commutator. Since annihilators kill Omega, the triple action equals a triple nested graded commutator applied to Omega. Each commutator flips parity, remains supported on D's sites, and has norm at most (2 C_B m/sqrt(Ncell)) times the preceding operator norm. The commutator types alternate anticommutator/ordinary commutator/anticommutator for initially odd D. Therefore

 ||a_k a_j a_i D Omega|| <= (2 C_B m)^3 ||D|| / Ncell^(3/2).

Decompose the uniformly quasi-local Z into odd dyadic shells D_n of support m_n=O(2^(3n)). The constant

 K_3=sum_n (2 C_B m_n)^3 ||D_n||

is uniform using any tail exponent p>9. Triangle inequality bounds every triple action of Z by K_3/Ncell^(3/2). The conical mode count #soft/Ncell<=C_D epsilon³ then gives

 mu_Z((0,epsilon]) <= K_3² C_D³ epsilon^9 /6.

No independence assumption on the three created particles enters. Shells individually need not have zero one-particle vacuum component: the number>=3 condition is used only for the FULL Z vector before shellwise bounds on triple annihilation. This avoids an invalid per-shell number assumption.

Stieltjes integration yields inverse moments for0<s<9 and inverse-vector powers q<9/2, with uniform low-energy remainder9C/(9-s) epsilon^(9-s). Section 4 local spectral convergence then gives the corresponding thermodynamic inverse moments. This is strictly stronger than merely reapplying the generic cubic tail to Z.

The argument generalizes to any uniformly quasi-local parity-homogeneous creator whose vacuum image has particle number at least r: factorial soft-number moment of order r, nested graded commutators, and p>3r give epsilon^(3r). It does NOT claim the required subtraction creator exists for every r without a separate construction. For r=3, existence is already supplied by linear subtraction.


The stronger bound controls the higher odd vacuum transition; mixed-flux histories, the interacting reference and the all-coupling relative susceptibility remain open.

## 7. Full singleton inverse-kernel row bound from graded locality

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

## 8. Absolutely summable higher-odd singleton channel

### A one-sided inverse filter whose adjoint kills the vacuum

Choose real smooth theta with0<=theta<=1, theta(x)=0 for x<=1/2 and theta(x)=1 for x>=1. Let f(x)=theta(x)/x, defining it as0 near zero and on negative x. Then f and every derivative belong to L2(R). Plancherel plus Cauchy-Schwarz, with sufficiently many polynomial time weights, gives an inverse Fourier kernel w with every weighted L1 moment finite. This argument does NOT require w bounded at t=0; the one-sided1/x tail can give a logarithmic singularity there, which is integrable.

With energy measured in the fixed hopping unit, for 0<epsilon<=1 set f_epsilon(x)=epsilon^-1 f(x/epsilon)=theta(x/epsilon)/x and w_epsilon(t)=w(epsilon t), in the same Fourier convention f(x)=integral w(t)e^-itx dt. Hence

 integral |t|^p |w_epsilon(t)|dt = epsilon^(-p-1) M_p.

Define the bounded odd quasi-local operator X_epsilon,w=integral w_epsilon(t) tau_t(Z_w)dt. Since H Omega=0,

 X_epsilon,w Omega=f_epsilon(H) Z_w Omega,
 X_epsilon,w* Omega=f_epsilon(-H) Z_w* Omega=0.

The second identity is crucial and uses the positive generator, real filter and negative-frequency support exclusion, not Hermiticity of Z. Therefore for every v,

 <Z_v Omega,X_epsilon,w Omega>=omega({Z_v*,X_epsilon,w}).

The reversed product has zero vacuum expectation because X_epsilon,w* Omega=0. An ordinary arbitrary inverse approximation would not permit this replacement by a graded anticommutator.

### Two errors: infrared vector tail and spatial operator tail

The higher-odd spectral bound mu_Z(0,e]<=C e^9 gives

 ||(H^-1-f_epsilon(H))Z_w Omega||
 <= [integral_(0,epsilon] E^-2 dmu_Z]^(1/2)
 <= sqrt(9C/7) epsilon^(7/2).

Thus replacing T^Z_vw by the filtered correlation costs at most a uniform constant times epsilon^(7/2).

For R=distance(v,w) large, approximate Z_v by an odd operator in its R/4 ball. For |t|<=cR, with c a fixed inverse propagation velocity, tau_t(Z_w) has an odd R/4-ball approximant with error <=C_q R^-q for every fixed q. This follows by first truncating Z_w to a smaller fixed fraction of R, then applying the finite-range propagation bound; the exponential short-time leakage and original rapid tails are uniform in volume. Constants may depend on q, not epsilon,R,L.

Integrate those local approximants only for |t|<=cR. Their support is disjoint from the v approximant, so the graded anticommutator vanishes. The short-time error is at most C_q epsilon^-1 R^-q. The long-time part is bounded by norms and the filter moment:

 integral_(|t|>cR)|w_epsilon(t)|dt <= C_p epsilon^(-p-1) R^-p.

The v truncation error times ||X_epsilon,w||<=M0 epsilon^-1 has the same first form. Consequently

 |T^Z_vw| <= C epsilon^(7/2)+C_q epsilon^-1 R^-q
                         +C_p epsilon^(-p-1)R^-p.

Finite torus balls use their graph distance; at sufficiently large ball size they equal the whole algebra. The same constants and argument apply to the infinite limit.

### Explicit summable exponent and thermodynamic rows

Choose epsilon=R^(-7/8), p=q=32. The three powers are respectively

 R^(-49/16), R^(-249/8), R^(-25/8).

Thus |T^Z_vw|<=C'(1+R)^(-49/16), uniformly in volume. Since49/16>3, the row is l1 summable on the three-dimensional lattice. More generally any exponent below7/2 can be achieved by choosing epsilon=R^-a with a<1 sufficiently close to1 and sufficiently high filter moments.

Section 4 gives convergence of every fixed entry. The new common summable spatial majorant gives l1 convergence of centered zero-extended rows by dominated convergence. In a fixed magnetic cell, the corresponding Fourier coefficient symbols therefore converge uniformly. This does not claim an isometric embedding of finite periodic many-body spaces.

The higher-odd quadratic singleton channel now has an absolutely summable kernel, hence a bounded convolution operator by Schur's estimate. This is a statement about the defined response kernel (or its self-adjoint realification), not identification of the full native sixth-order Hamiltonian. For the one-particle component the generic cubic spectral tail supplies only powers below 1/2 through this filtering argument; it gives no summable bound for that component. Nonlinear higher-odd singleton returns can therefore be separated as a summable channel while the linear return still requires controlled resummation. Other mixed histories and the all-u relative-impurity susceptibility remain outside the result.

## Evidence and scope

The supporting runner executes 1217 exact-dyadic CAR, occupation and rational spectral controls on a four-mode toy. It includes a complex non-Hermitian creator with both one- and three-particle content, an explicit unitary mode basis, the full low-energy occupation inequality, inverse-moment bounds, dyadic tail sums, a graded Gram bound, the triple graded-commutator identity, factorial soft-number counting, the nine-power tail after exact one-particle subtraction, a one-sided spectral-filter fixture and the spatial exponent balance. Seven explicit counterexamples reject common invalid replacements: ordinary instead of graded locality, one-particle instead of full low-energy projection, endpoint integrability from cubic counting alone, a uniform row bound from individual inverse-vector norms alone, requiring each dyadic shell to have no one-particle part, endpoint integrability at inverse power nine, and annihilation of the vacuum by an arbitrary two-sided inverse filter. These are exhibited mathematical counterexamples, not claimed executions of mutated physical solvers. No native physical calculation was performed. The finite controls support inspection; the preceding proof establishes the infinite-volume assertions.

Original source and independent proof review are preserved in the branch packet. The finite L6 nonlinear calculation is not a premise and is not extrapolated. Constants are existence bounds from the stated conical dispersion and uniform quasi-locality, not numerical estimates. Preparation, the physical choice of Hamiltonian and Gaussian state, mixed histories, node values, and fixed-coupling interacting stability remain separate obligations.
