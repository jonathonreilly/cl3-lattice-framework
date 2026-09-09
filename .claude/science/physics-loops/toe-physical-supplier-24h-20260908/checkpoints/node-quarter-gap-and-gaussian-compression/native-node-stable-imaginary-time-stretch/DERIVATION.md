# Stable normalized imaginary-time states and the remaining overlap problem

This is a new algorithmic derivation, not a physical calculation or an accepted long-time native kernel. The infinite h/4 refinement may supply a tail cutoff in future work; no finite fixture below uses that bound.

## 1. Normalized Gaussian evolution removes exponential overflow

Use h_A=iK_A and covariance Gamma_ij=(i/2)<[gamma_i,gamma_j]>. For a pure state define the occupied Nambu projector P=(I+iGamma)/2. Starting at the reference negative-frequency projector P0, the normalized state exp[-tau(H_A-E0)]Omega/||...|| satisfies

 dP/dtau=-h_A P-P h_A+2P h_A P,
 dGamma/dtau=-K_A-Gamma K_A Gamma.                         (1)

A stable finite-bath representation is P=Q Q^dagger with orthonormal columns. Advance exp(-Delta h_A)Q and take a thin QR, with a fixed bounded Delta||h_A||. This never forms exp(-tau h_A) at a large tau. It preserves the projector geometry; a numerical ODE/QR error certificate remains necessary.

Track log n_A(tau), not the exponentially small norm n_A. The exact derivative is -<H_A-E0>. It need not be computed by subtracting two extensive energies. Let h0,+ be the positive part of the reference one-particle matrix. Particle-hole symmetry gives

 <H_A-E0>=Tr(h0,+ P)+(1/2)Tr((h_A-h0)P).                  (2)

The first term is the nonnegative squared Frobenius norm ||sqrt(h0,+)Q||_F^2. The second is finite rank and uses only the impurity's local correlations. Equation (2) cancels E0 algebraically before floating arithmetic. It does not subtract two volume-size log determinants.

For an actual fixed impurity, energy decreases along normalized imaginary time: d<D_A>/dtau=-2 Var(D_A). Initially <D_A>=<B_A> and ||B_A||<=beta/2. Thus the free excitation energy stays at most beta, whenever the evolution starts in the reference vacuum. This is a volume-independent energy bound, not a bound on the number of soft excitations or a low-rank approximation theorem.

The target overlap separates as

 <Omega|E_C(t)E_A(s)|Omega>=n_C(t)n_A(s)<phi_C(t),phi_A(s)>.

The norms can be stored logarithmically. The normalized overlap has modulus at most one and must retain its complex phase/sign. Fixed J insertions can similarly be evaluated as unnormalized Gaussian transition minors, without dividing by this overlap.

## 2. Phase tracking is a real obligation

A single imaginary-time state has positive reference overlap <Omega|exp(-tau D_A)|Omega>, fixing its phase. Two such normalized states need not have positive mutual overlap.

A decisive two-mode even-CAR example uses H_+=sigma_z+sigma_x and H_-=sigma_z-sigma_x on the even sector, with any common positive scalar added to make D_+/- positive. For r=sqrt(2), choose cosh(rt)=5/3 and sinh(rt)=4/3. Both evolved vectors have positive first component (5-2sqrt(2))/3, but their unshifted mutual overlap is

 (25-20sqrt(2))/9<0, since 625<800.

Hence taking a positive square root of the determinant overlap fails even for two positive semigroups. This is a non-native counterexample to that proposed numerical shortcut, not a claim about the native kernel's sign.

There is a phase-preserving unitary representation of the normalized path. Define the real skew transport generator

 A(tau)=-(1/2) dotGamma(tau) Gamma(tau).

Then dotGamma=[A,Gamma]. Its quadratic Spin lift has zero expectation because Tr(A Gamma)=0. It therefore transports the pure Gaussian state in the same zero-Berry-phase gauge as normalized imaginary time. This gives an exact bounded orthogonal path, rather than an exponentially growing Bogoliubov matrix. A discretized implementation must track the Spin lift, not just its SO endpoint. The reviewed real-time ordered Pfaffian formula can evaluate a product of these short lifts with its explicit cosine signs. Compressing many lifts to one endpoint without losing the sheet requires a chart/lift algorithm, still to be implemented and priced.

## 3. Finite-rank time-kernel route to the infinite bath

There is an alternative to retaining every spatial mode. On the finite star support the free imaginary-time ordered contraction is

 G(tau)=2 exp(-tau h0) P_+ for tau>0,
 G(tau)=-2 exp(-tau h0) P_- for tau<0.

These contractions decay in the correct spectral half-space; no exponentially growing bare interaction-picture field is evaluated. A piecewise impurity history is supported on at most the center and four neighbors. Dyson/Wick expansion therefore produces a time-domain Gaussian determinant/Pfaffian problem on that fixed spatial support, rather than on the whole bath.

The candidate determinant kernel is A(tau,sigma)=(i/2)G(tau-sigma) DeltaK(sigma). The linear term is exactly minus the integrated reference impurity expectation. Its continuous kernel has a time-ordering jump: Hilbert-Schmidt regularity does NOT by itself justify an ordinary trace-class Fredholm determinant. One must define the contact term and regularized determinant (or Fredholm Pfaffian) consistently with the finite ordered Dyson limit. A formal det_2 expression is not yet a certified implementation. Two insertions should use minors, not a transition inverse at a zero overlap.

This route could use certified positive matrix-valued spectral quadrature for the local bath contractions, then a rational/finite-bath representation. It avoids a spatial cube and extensive energy subtraction. However the generic Hilbert-Schmidt determinant perturbation bound grows exponentially with its norm and is too pessimistic at time 100/h. A useful implementation needs structure-specific coercivity or a stable factorization/error analysis. No feasibility claim is based on writing the determinant formally.

## 4. Actual bounded synthetic control

The companion code uses a non-native two-mode quadratic Hamiltonian and checks normalized QR/Riccati covariance plus log norm from (2), against an independent dense Fock spectral calculation at times 0, 1/4, 10 and 100. It also checks the exact sign inequality above. This test is about normalization and numerical scale, not the full Spin overlap algorithm or a native bath. There are no physical matrices or production actions.
