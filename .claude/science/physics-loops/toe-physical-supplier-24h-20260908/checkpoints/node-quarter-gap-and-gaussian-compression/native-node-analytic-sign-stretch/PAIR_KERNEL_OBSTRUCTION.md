# What positive inverses and cubic symmetry do not prove

Let the15 pair labels be the two-element subsets A of six star legs. The90-word sum uses adjacency T_CA=1 exactly when A and C are disjoint. For each leg i define u_i(A)=1_(i in A)-1/3. Direct counting gives Tu_i=-3u_i: when i belongs to A, no disjoint C contains it and the sum is -2; otherwise three of the six disjoint C contain it and the sum is1. Thus the disjoint-pair form is indefinite, notwithstanding its nonnegative individual entries. Its constant vector has eigenvalue6. In particular a Gram-matrix argument is insufficient.

A concrete fully permutation-covariant positive-resolvent counterexample is available without any physical computation. Let v_A in R6 be the incidence vector of A minus(1/3) times the all-one vector, and let Omega=(1,0) in R plus R6. For c>0 define

 P_A = [[1, c v_A^T], [c v_A, I+c² v_A v_A^T]].

The Schur complement is I, so every P_A is strictly positive. Every coordinate permutation carries P_A to P_(permuted A), while fixing Omega. D_A=P_A^-1 is therefore another strictly positive, fully permutation-covariant family. Both P_A-I and D_A-I have rank at most2. Yet P_A Omega=(1,c v_A), and v_C dot v_A=-2/3 for disjoint pairs, hence

 sum_(A,C disjoint) <Omega,P_C P_A Omega> =90-60c².

At c=2 this is -150. Adding a separate zero-energy fermion with gamma acting only on that factor makes the corresponding one-particle coefficient of sum R_C gamma R_A equal this same scalar, with R_A=-P_A. This is only an abstract operator counterexample: its D_A are NOT asserted to be the actual native quadratic star Hamiltonians, and the spectator zero mode is not the prescribed infinite Dirac construction. It disproves a proposed lemma based solely on positive inverses, rank-two operator differences, permutation symmetry and a center insertion. It does not disprove native positivity.

The native pair-family vectors may have components in the negative standard representation; symmetry alone does not remove them. A positive proof must use an additional native identity controlling those components or the gamma-center insertion, rather than discarding them by a scalar orbit average.
