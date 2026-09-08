# Interpreting the third-order vertex without assuming its weights

Status: independently derived finite-L4 interpretation and exact symmetry classification. No computed vertex weights were read. No physical solve, spectrum or stochastic simulation. The fixed canonical frame, Hamiltonian and third-order Feshbach operator O_v(E0) are supplied reviewed inputs.

## 1. What a particle weight does and does not say

Set chi_v=O_v(E0)|Omega>, with odd active parity. On L4 its one-star invariant space has six complex modes, so chi_v=chi_v,1+chi_v,3+chi_v,5. The exact weights w_n=||chi_v,n||² are nonnegative. A positive w_3+w_5 disproves equality of this vacuum transition to ANY linear active Majorana operator in the declared vacuum/frame. Indeed a linear Majorana applied to the vacuum has exactly one quasiparticle. Its best possible vacuum-state approximation has squared error w_3+w_5. If the higher weights vanish, only the vacuum transition is linear: an operator may annihilate the vacuum and act nonlinearly on excited states. Zero weights therefore do not prove the entire O_v is quadratic/linear or justify dropping other sixth-order histories.

## 2. Magnetic symmetry fixes the L4 one-particle shape

The reviewed magnetic lift acts gamma_i -> g_i gamma_f(i), beta_i -> g_i beta_f(i), preserves H0 and its vacuum, and sends the90-term definition O_v to g_v O_f(v). Let

    Z_iv=<Omega|gamma_i O_v|Omega>.

It is an invariant ordered64x64 matrix, with no antisymmetry assumption. The exact finite signed-orbit calculation in this packet acts on all4096 ordered entries using the eight reviewed generator permutations/gauges. It finds dimension two: the diagonal64-entry orbit and the nearest-neighbor384-entry orbit survive; every other orbit is forced zero. Since I and the nonzero K both obey the constraints and are independent, they span this commutant over the complex numbers. This reuses the physical lift authority; the new unrestricted ordered-matrix constraint computation is independent of the earlier antisymmetric-only census.

Let J=K/omega, omega=sqrt24|t|. With the supplied empty-mode convention the vacuum covariance is C=I+iJ and J C=-i C. Since only the one-particle part contributes to Z, JZ=-iZ. Together with the two-dimensional commutant, this gives

    Z=alpha(I+iJ),    chi_v,1=alpha gamma_v|Omega>.

The equality of states follows because the gamma_i|Omega> span the entire one-particle space. In the real bipartite Fock frame, v=0 lies on the black sublattice, gamma_0 is real, all pair-defect Hamiltonians and resolvents are real, and O_0 and chi_0 are real. Therefore alpha=<Omega|gamma_0 chi_0> is real. Magnetic translations make the same alpha apply to every v. In particular w_1=alpha², but a weight alone loses the sign of alpha; the signed overlap should be reported.

This conclusion is specific to the checked L4 magnetic representation and flat canonical covariance. It is not a proof of a momentum-independent L6 vertex. The finite exact group computation ran in0.03 seconds external with no matrix diagonalization or physical coefficient data.

## 3. Correct quadratic normalization and its limited implication

The one-particle vacuum-matched vertex is

    V_3,lin = -i alpha sum_v gamma_v beta_v.

In the convention H=(i/4)Gamma^T K_total Gamma, a cross block contributes(i/2)sum K_gamma,beta gamma beta. Thus its cross block is -2 alpha u³ I, not -alpha u³ I. The ideal diagnostic matrix is

    K_total = [[K, -2 alpha u³ I],[2 alpha u³ I,0]].

If this were the entire Hamiltonian to the required order, its small branch would be4 alpha² u^6/omega at fixed omega, and2|alpha| |u|³ at an active zero. These factors follow from the quadratic block convention. They do not turn the actual vertex into that model.

In particular a nonzero alpha proves an allowed, nonzero one-particle vacuum transition at this order. It does not determine the full sixth spectator coefficient: the singleton-middle multiparticle channels and648 mixed-middle orders remain. Nor does an inverse-gap bound prove infrared divergence: alpha and momentum-dependent numerators can vanish or scale with the gap.

## 4. Multiparticle channels can be moved by dressing

Positive higher weights are not a basis-independent obstruction to an effective low-energy theory. In a fixed finite system, an even, generally non-Gaussian near-identity unitary can remove the vacuum-to-multiparticle part at order u³. If V_3 denotes that even active/spectator vertex, choose anti-Hermitian S with

    S_a0=(V_3)_a0/(E_a-E0), S_0a=-conjugate(S_a0)

for the multiparticle active states a and the spectator indices, setting other entries to zero. Then [S,H0]_a0=-(V_3)_a0, so exp(u³ S) cancels that coupling at this order. On L4 these denominators are at least3omega. This construction is only for this finite vacuum/multiparticle offdiagonal component; it is not a resonant all-active SW block or a volume-uniform local dressing theorem.

The eliminated coupling returns in sixth-order energy/operator terms, and observables/states must be transformed. A genuinely non-Gaussian dressing is outside a claim that the original canonical active Majoranas themselves have an exactly quadratic vertex. Under a Gaussian change of variables that simultaneously transports H0 and its vacuum, the particle-sector statement is covariant; simply relabeling modes cannot erase a positive transported multiparticle norm. More general field redefinitions may move that weight and must be declared and priced. Thus the honest distinction is fixed-frame nonlinearity versus an invariant obstruction to every dressed description; only the first follows from w_3+w_5>0.

## 5. Weights alone do not give the multiparticle spectator kernel

The singleton-middle contribution contains cross Gram matrices

    G_n(v,w)=<chi_v,n|chi_w,n>,

weighted by negative1/(n omega) on flat L4. Each G_n is a positive Hermitian magnetic-invariant matrix, hence G_n=a_n I+i b_n J with real a_n,b_n and |b_n|<=a_n. Its diagonal fixes a_n=w_n. For n=1 the covariance forces b_1=a_1=alpha². For n=3,5 the weights do not fix b_n: symmetry and positivity alone allow b_n=0 even with positive w_n. Therefore a higher-particle norm neither establishes nor evaluates its offsite spectator hopping contribution. At nonflat L6 the many-particle denominator is no longer n omega, so even unweighted offsite Gram matrices are insufficient.

The lowest-cost decisive next finite test, after the already frozen30-solve chi_0 calculation, is: report signed alpha and all exact w_n; verify the one-particle shape; then compute one nearest-neighbor G_3,G_5 by embedding the two local six-mode states into the reviewed common ten-mode L4 invariant space. Because both local spaces are J-invariant, this is a number-preserving change of creation basis with wedge/determinant amplitudes, not new physical resolvent solves. It still needs exact frame/phase/metric controls and a frozen cost before execution. That one overlap fixes each invariant G_n on L4; it does not supply the mixed-middle term.

For L6, the useful route is first the exact one-star Krylov dimension and Gaussian representation of chi_v, then certified one-/multiparticle or spectral-weight bounds using actual prefix gaps. The30-application grouped formula reduces work for the singleton channel but cannot replace the five-resolvent mixed-prefix calculation. Existing nonadjacent rank-four gap census is the appropriate independent prerequisite for the latter. No L6 numerical cost, weight or vanishing claim is inferred here.

## Provenance and finite control

The source-bound generator receipt is native-sixth-magnetic-symmetry-root/RESULT.json. COMMUTANT.json retains every ordered-entry orbit and its sign assignment, including forced-zero contradictions; no eigenvalue or vertex weight is an input. The third-order definition and72/648 boundary are reused from native-third-order-hybridization/DERIVATION.md410b2f91 and native-l6-sixth-factorization. All numerical weight interpretations above were fixed before any such weight was seen.
