# Soft annihilator limit and an exponential imaginary-time node tail

This derivation avoids spatial cutoff commutators with the free Hamiltonian. For a cutoff q_R, ||Kq_R|| need not vanish; that route is not used. The generalized zero-mode notation at the end is shorthand for a bounded expression obtained from finite normalized annihilators.

## Finite exact identity with its normalization

On a finite antiperiodic canonical torus, take a normalized active annihilator a_L at positive frequency omega_L, with a_L Omega_L=0 and [a_L,H_L]=omega_L a_L. If there are n_cell magnetic cells, rescale it to tilde a_L=sqrt(n_cell/2) a_L. With the convention {gamma_i,gamma_j}=2delta_ij, its local anticommutator coefficients are phi_L(R,s)={tilde a_L,gamma_(R,s)}=exp(ik_L dot R)u_L(s), for a unit cell spinor u_L (complex conjugation may be absorbed into its definition). The rescaled operator norm grows; no norm bound on that operator is used.

Let R_A(E)=(E-H_A)^(-1), L_A(phi)=[tilde a_L,B_A]. Exact multiplication gives

 tilde a_L R_A(E)
 =R_A(E-omega_L) tilde a_L
   +R_A(E-omega_L)L_A(phi_L)R_A(E).            (1)

The shift is E MINUS omega_L. L_A(phi_L) is a linear Majorana operator supported on the fixed pair and center; its coefficients are bounded independently of volume. Applying(1) twice and using tilde a_L Omega_L=0 yields

 <tilde a_L R_C(E0) gamma_v R_A(E0)>
 =phi_L(v)<R_C(E0-omega_L)R_A(E0)>
 +<R_C(E0-omega_L)L_C(phi_L)R_C(E0)gamma_v R_A(E0)>
 -<R_C(E0-omega_L)gamma_v R_A(E0-omega_L)L_A(phi_L)R_A(E0)>. (2)

All brackets have the original vacuum on both sides. No vacuum commutation of a defect inverse is assumed.

## Taking the limit without an unbounded Q

Take momenta approaching the folded Dirac node along a direction, with omega_L->0 and u_L->u in the appropriate annihilation-band directional subspace. Each shifted inverse differs from its unshifted inverse by at most omega_L/delta^2. The three right-hand terms consist only of uniformly bounded inverses and fixed-local linear operators. Their finite-to-infinite vacuum matrix elements converge: use the same inverse filter/cocycle argument as the parent, now for at most three inverses and finitely many local insertions. The scalar Fourier kernel acquires only exp(-i omega_L t), so dominated convergence applies. Thus the limit of(2) is a direction-independent LINEAR functional of u obtained by setting the shift to zero and replacing local phi by its periodic zero-momentum cell values.

The thermodynamic smooth coefficient matrix independently identifies the left side with the limiting one-particle form factor evaluated against u. Opposite rays have complementary directional band subspaces. Hence the limiting linear identity holds on their combined full cell space, not just one chosen band. It can therefore be evaluated at u=e_0, although that real cell vector itself is not an annihilation-band vector. This is a linear extension of identities on complementary subspaces, not an assertion that a generalized Hermitian zero mode annihilates the vacuum.

By the signed little-group theorem the node matrix is alpha I. Put q_j=1 on2Z^3 and zero otherwise, merely to label u=e_0. Then q_v=1 and q is zero on the pair's two neighboring sites. Define the bounded local odd operator J_A by substituting these coefficients into twice L_A(phi). Equivalently J_A is the formal algebraic [gamma(q),B_A], but no gamma(q) operator is formed. If B_A=(i/2)gamma_v gamma(d_A), then J_A=i gamma(d_A), ||J_A||=beta=4sqrt(2)|t_hop|. The exact scalar identity is

 alpha=(1/8)sum_{A,C disjoint} < R_C R_A
       +(1/2)R_C J_C R_C gamma_v R_A
       -(1/2)R_C gamma_v R_A J_A R_A >.           (3)

Every term in(3) is an ordinary bounded operator in the infinite Gaussian GNS representation. The factors1/2 come from extending the annihilator local anticommutators phi=q rather than {gamma(q),gamma_j}=2q_j. This is the rigorously defined version of the formal half-anticommutator expression.

## Imaginary-time representation and tail

Write D_A=H_A-E0>=delta and E_A(s)=exp(-sD_A). Define bounded odd insertion integrals

 Z_A(s)=-integral_0^s E_A(s-r) J_A E_A(r) dr.

Then ||E_A(s)||<=exp(-delta s) and ||Z_A(s)||<=beta s exp(-delta s). Expanding the three negative inverses in(3), or directly using their Laplace transforms, gives

 alpha=(1/8)sum_{A,C disjoint} integral_0^infinity dt ds
 < E_C(t) E_A(s)
       +(1/2)Z_C(t) gamma_v E_A(s)
       -(1/2)E_C(t) gamma_v Z_A(s) >.             (4)

The sign of Z is negative, and two integrations of E produce the two positive inverse signs. In particular the correction terms in(4) match the three-resolvent signs in(3). The integrand obeys

 |F_CA(t,s)| <= exp[-delta(t+s)] [1+(beta/2)(t+s)].

This gives the explicit complete90-word error when either time exceeds T:

 error_tail <= (90/8) exp(-delta T)
 [2/delta^2 + beta T/delta^2 + 2beta/delta^3].     (5)

The bound contains no generalized-Q norm, finite volume, oscillatory inverse-filter moment or active gap. It does retain the supplied wrong-flux gap. The internal insertion integral in Z is a derivative of a Gaussian product and can be evaluated through Gaussian insertion formulas, or retained as a third integration variable. A numerical implementation must preserve its sign and error; (5) is not a claim that those point evaluations are free.

## Concrete conservative scale

In units h=2|t_hop|=1, delta=3483/102400 and beta=2sqrt2<3. Taking T=1024 makes(5) smaller than10^-6 in the units of alpha. This statement is certified by the accompanying exact rational lower Taylor bound for exp(delta T); it is a tail budget only. Such a large time can make imaginary-time Gaussian conditioning expensive, so it does not establish practical feasibility. A first pilot should measure a fixed short-time overlap/derivative kernel before any full square integral; replacing the true gap by an observed larger one would require its own certificate.

Alpha remains unevaluated. Equations(3)-(5) provide a native, explicitly bounded scalar target and a route to exponential tails. They do not establish alpha nonzero, discard multiparticle transitions, or identify a bulk interacting phase.
