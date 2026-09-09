# Thermodynamic limit of the quasi-local star vacuum creator

Domain: the supplied cubic model, canonical pi background, pure active Gaussian vacuum and antiperiodic tori L=4M, M>=32, with uniform full-active wrong-pair inequality H_{L,A}-E_{0,L}>=delta=6kappa>0. The quasi-local construction is the reviewed canonical note NATIVE_UNIFORM_QUASILOCAL_STAR_VERTEX_NOTE_2026-09-09.md, source b91828c58b110e984c6c033b3ba5b464f1bcb7dcb569262f054d5e5384df0eb7. No new computation or phase assumption is used.

## 1. Common local algebra and Gaussian state

Fix the star at the origin and embed increasing centered coordinate boxes in the infinite cubic CAR algebra. Choose the canonical pi gauge on each fixed box identically; finite-torus seam signs occur outside that box for sufficiently large L. This is a local identification, not an embedding of the entire periodic bond algebra preserving its wrap bonds. A fixed magnetic cell accounts for the staggering.

The finite pure active Gaussian covariance is a discrete Fourier sum of the bounded spectral projector of the canonical one-particle symbol. Away from its finitely many conical zeros that projector is continuous. The nodal set has measure zero, and each matrix entry is bounded. The antiperiodic Riemann sums therefore converge to the Brillouin-zone integral for every fixed pair of sites. One direct proof removes small fixed neighborhoods of the nodes, uses ordinary uniform Riemann convergence on the complement, and bounds the removed sums by their bounded integrand times their asymptotic grid density. Sending the neighborhood volume to zero finishes the limit. No point value at a node is required.

Wick's rule gives convergence of every fixed local polynomial expectation, hence of the local states to the infinite pure quasifree vacuum state omega. Purity follows from the limiting covariance being a projection almost everywhere, not from a finite-volume many-body gap. Write its GNS vacuum as Omega.

## 2. Local dynamics and the exact creator

Finite-range uniformly bounded quadratic interactions define infinite CAR dynamics tau_t. The one-particle hopping-path expansion, or its graded local commutator version, shows that finite-volume evolutions of each fixed local observable converge in norm uniformly on compact time intervals. Wrap-dependent paths must travel to the distant seam, and their exponential-series tail vanishes. The same Duhamel estimate applies to the local perturbation cocycles U_{L,A}(t) and gives their norm limit U_A(t). Local generators and time directions are those in the parent: U_A(t)=exp[-it(H+B_A)]exp(itH) in the GNS implementation.

Use exactly the same smooth inverse filter f and Fourier kernel w at every L, with all weighted L1 moments finite and f(x)=-1/x on x>=delta. Define the infinite quasi-local element

 Y_v=(1/8) sum_{A,C disjoint} integral ds dt w(s)w(t)
                 U_C(t) tau_t(gamma_v U_A(s)).

The Bochner integrals converge in norm, since the factors are unitary apart from the norm-one Majorana and w is integrable. For a fixed time box, compact-time local convergence proves convergence of its integral. The complement is uniformly bounded by the L1 tails of w. Combined with the parent's uniform spatial tails, this proves convergence of the finite creators in the following precise local-algebra sense: embed their ball-truncated versions on each fixed ball, take L to infinity there, and then let the ball grow; the omitted operator norms vanish uniformly in L. It does not claim an isometric global embedding of every finite periodic algebra.

The same construction yields odd ball approximants with error C_p(1+r)^(-p) for every p, independent of L and valid for the infinite limit. Norms remain bounded by (90/8)M_0^2. This is an operator-norm statement about the vacuum creator, not about the original global resolvent operator on arbitrary excited states.

## 3. Weighted coefficient convergence and the Fourier distinction

Set c_{L,vj}=omega_L({gamma_j,Y_{L,v}})/2 and c_{vj}=omega({gamma_j,Y_v})/2. For each fixed j these converge: first replace Y by a fixed-ball approximant using uniform norm control, then use finite-local state and operator convergence. Gaussian extraction gives P1 Y_v Omega=sum_j c_{vj} gamma_j Omega, by norm convergence from finite local polynomials.

If j is outside a ball of radius r, graded locality makes its anticommutator with the odd ball approximant vanish. Therefore |c_{L,vj}| and |c_{vj}| are bounded by C_p(1+distance(v,j))^(-p), for every p, uniformly. Represent finite sites in the centered fundamental box and extend coefficients by zero outside. For any fixed integer q>=0, choosing p>q+3 and using local pointwise convergence plus the summable common tail yields

 sum_j (1+|j-v|)^q |c_{L,vj}-c_{vj}| -> 0.

The finite-cell coefficient Fourier polynomials thus converge uniformly with every fixed number of derivatives to a smooth periodic coefficient symbol c_v(k). This does NOT prove smoothness of individual band amplitudes or of P_+(k)c_v(k) at a Dirac node. The spectral projector is direction-dependent there and an eigenvector gauge may be singular. The smooth object proved here is the Majorana coefficient symbol, before band projection. No nonzero node value or nodal zero is established.

## 4. Optional GNS resolvent identification is justified here

In the Gaussian Fock representation the positive active generator H is the second quantization of the bounded positive excitation dispersion, with H Omega=0. Local CAR polynomials applied to Omega form a dense core: each such vector has finite quasiparticle number and hence is an entire analytic vector for H, and local one-particle wavefunctions span a dense one-particle subspace. Local even quadratic B_A is bounded and self-adjoint, so the same set is a core for H+B_A.

For a fixed local polynomial X, the finite quadratic form identity is

 <X Omega_L,(H_{L,A}-E_{0,L})X Omega_L>
 = omega_L(X^*[H_L,X])+omega_L(X^* B_A X).

The commutator is a fixed finite-local polynomial, because only interactions meeting X contribute. The finite wrong-pair inequality bounds this expression below by delta omega_L(X^*X). Local state convergence passes it to the infinite limit. The core and bounded-perturbation facts then imply H+B_A>=delta I as a self-adjoint quadratic-form inequality on the full GNS active Fock space. This is a wrong-flux impurity gap relative to the original vacuum energy zero; H itself remains gapless.

Consequently R_A=-(H+B_A)^(-1)=f(H+B_A) exists with norm at most1/delta. Functional calculus and the cocycle identity reproduce both filtered inverses exactly, and

 Y_v Omega=(1/8)sum_{A,C disjoint} R_C gamma_v R_A Omega.

Thus the infinite vacuum transition has an exact double-resolvent meaning, not merely a formal local limit. This construction stays in the canonical Gaussian GNS representation. It does not assert a global tensor identification of inequivalent flux representations, or an all-active gap between unbounded excited spectra.

## Boundary

The result supplies a thermodynamic quasi-local creator and smooth coefficient-symbol limit under the same supplied uniform stiffness. It does not transfer finite-L6 nonlinearity to infinite volume, determine a Dirac-node value, identify the full sixth-order effective Hamiltonian, or prove an interacting phase/local joint-defect theorem. No numerical calculation was performed. Uniform inverse-kernel row l2 bounds remain available from the parent; convergence of more singular interacting quantities requires its own argument.
