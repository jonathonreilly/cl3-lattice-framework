# Low-energy operator extension of the inverse-filter construction

Status: new conditional derivation, not yet independently reviewed. No numerical execution. All energies below are measured relative to the same canonical free vacuum E0. This is not an identification of a vacuum creator with the full unrestricted resolvent operator.

Assume H>=0 is the free active Hamiltonian and H_F=H+B_F>=Delta_F>0 in a fixed wrong-flux sector, with B_F a bounded local quadratic perturbation. The gap is on the full active Fock space, both parities. Let P_eta=1_[0,eta](H), with eta<Delta_F. The already supplied local dynamics and cocycle estimates apply uniformly in volume.

Choose a real smooth function f equal to 1/x on x>=Delta_F-eta and smoothly regularized below that positive threshold, with inverse Fourier kernel w having all polynomial absolute moments. Define

 Y_F(A)= integral w(t) exp(it H_F) A exp(-it H) dt

for a local or rapidly quasi-local operator A. Fourier conventions are chosen so integral w(t)exp(it x)dt=f(x). The cocycle exp(it H_F)exp(-it H), combined with free local dynamics of A, makes Y_F(A) rapidly quasi-local, with uniform norm and tail constants depending on Delta_F-eta and the supports/norms, not volume. Its parity is that of A. The integral is norm convergent. This uses the same inverse filter as the vacuum construction but a different spectral argument.

In finite volume the exact identity is

 (H_F Y_F(A)-Y_F(A) H)P_eta=A P_eta.                 (1)

Indeed, between eigenvectors of H_F of energy lambda and H of energy e<=eta, the left side is (lambda-e)f(lambda-e)A_lambda,e=A_lambda,e since lambda-e>=Delta_F-eta. In particular

 Y_F(A)|e>=(H_F-e)^(-1)A|e>, e<=eta.              (2)

For a superposition, (1), not a single scalar resolvent formula, is the correct statement. The bounded quasi-local operator is defined on the entire Hilbert space; only its exact inverse interpretation is restricted to P_eta. There is no claim of a global inverse Liouvillian: high active input energies can resonate with wrong-flux outputs.

For two wrong sectors A,C with gaps exceeding eta, define Y_A=Y_A(I) and Z_CA=Y_C(gamma_v Y_A). Products and inverse-filter maps preserve rapid quasi-locality. Then for each free input eigenstate e<=eta,

 Z_CA|e>=(H_C-e)^(-1) gamma_v (H_A-e)^(-1)|e>.

Thus the finite sum over the actual disjoint-pair star paths has a bounded quasi-local representative agreeing with the energy-relative double inverse on ALL input eigenstates in this window, not just the vacuum. Native prefactors and flux/gauge transports must be included exactly as in the supplied star formula; this lemma does not alter them. Uniform bounds follow from the filter's L1 norm and the CAR norm of gamma_v. Constants worsen as eta approaches the wrong-sector gap.

This supplies an operator-level extension, but does not close fixed-U stability. The window is a bound on TOTAL free excitation energy. A perturbed many-body ground state can have extensive free excitation energy even when its density is O(U^2). No supplied theorem puts that state in P_eta with a volume-uniform error. Replacing P_eta by a bound on local energy requires a new localization estimate; applying (1) without P_eta is false in general. In a thermodynamic representation (1) needs a specified common operator/form core and spectral double-integral justification; the present exact argument is finite-volume, with uniform local operator bounds.

The useful next target is therefore a local-energy version of (1), with errors controlled by local energy density and summable distant influence, or a dressed interacting reference for which the relative flux gap survives. Neither is assumed here.
