# Uniform reference chart for the normalized imaginary-time state

Supplement to frozen b6ce4a68; no new physical computation. Let D_A=H0+B_A be the actual active quadratic impurity Hamiltonian in the reference Fock representation. The main proof constructs its negative-band quasifree vacuum Omega_A with positive amplitude a=<Omega0,Omega_A>>exp(-7569/349).

First justify calling this a ground vector. The trace-class covariance change and bounded one-particle h0 give finite reference excitation energy. The represented Gaussian state is pure and invariant under the h_A CAR dynamics. Equivalently, in its annihilator representation the quadratic generator is the second quantization of the positive quasiparticle energies plus a scalar E_A. This identity follows on finite excitation vectors from the CAR commutators; the generators differ only by a scalar, fixed by the vacuum expectation. The bounded local perturbation defines the same self-adjoint generator. Thus D_A-E_A>=0 and (D_A-E_A)Omega_A=0. No positive quasiparticle gap is assumed. Zero one-particle eigenvectors are absent by the main proof, so there is no additional zero-energy Fock excitation. These statements concern this active quadratic impurity, not other flux sectors or an interacting electric Hamiltonian.

For tau>=0 set psi_tau=e^(-tau D_A)Omega0/||e^(-tau D_A)Omega0||. Write the spectral probability measure of D_A-E_A in Omega0 as mu; it is supported on[0,infinity) and has an atom of weight at least a² at0. With

 M1=integral e^(-tau x)dmu, M2=integral e^(-2tau x)dmu,

we have M2<=M1<=1 and M1>=a². The energy-shift scalar cancels on normalization. Therefore

 <Omega0,psi_tau>=M1/sqrt(M2)>=sqrt(M1)>=a>exp(-7569/349).       (1)

The amplitude is real positive, fixing the state phase directly, without choosing a square-root sign from a determinant. This is uniform for all tau, even though there is no active bulk gap. The bound remains valid at tau0; no differentiation of a generalized zero-energy vector is involved.

Quadratic imaginary-time evolution of a pure Gaussian vector remains Gaussian when normalized. This can be obtained from finite quadratic CAR approximants and their strong semigroup limit; (1) prevents disappearance of the reference component. Thus every psi_tau has a reference Thouless chart. In canonical paired singular modes, its reference amplitude is product_j cos(phi_j). Each factor is at most1, so (1) implies cos(phi_j)>=a individually. The chart matrix consequently obeys the explicit, very coarse uniform bound

 ||Z_tau||<=sqrt(a^-2-1)<sqrt(exp(15138/349)-1).                (2)

This does NOT assert that the sharper stationary bound ||Z_A||<1 propagates along the whole imaginary-time path. Equation(2) can be numerically poorly conditioned; it removes a literal reference-chart zero, not the need for stable certified arithmetic or useful compression.

A common positive reference anchor fixes the phase of each normalized impurity state. It does not force overlap between two different such states to be positive or nonzero. Mixed-impurity insertion kernels may still change sign or vanish. No physical kernel, overlap or node scalar has been computed by this supplement.
