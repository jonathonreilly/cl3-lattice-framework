# Conditional leading spectator spectrum on uniform L4

Assume the supplied full native Hamiltonian H(u)=H0+uD at the previously proved isolated uniform L4 endpoint, with t normalized as in K0²=-24I. Its entire ground space is a unique active vacuum tensored with the allowed spectator parity space. Assume the reviewed canonical coefficients through order five are scalar, the sixth coefficient is scalar plus bilinear, and the magnetic symmetry proof applies. Let c be the real coefficient of i beta_0 beta_16 in the sixth coefficient, and ASSUME c is nonzero. This note does not calculate or certify c.

Since K0_(0,16)=-2, the antisymmetric bilinear coefficient matrix b=aK0 has a=-c/2. Write the nonscalar sixth operator as Q=sum_(i<j) b_ij i beta_i beta_j. In the convention Q=(i/4) beta^T K_eff beta, K_eff=2b=-cK0. Thus all32 positive Majorana frequencies are omega=|c|sqrt24. This factor of two is essential; the pair coefficient b is not itself the standard skew Hamiltonian matrix.

## Physical parity, including the active vacuum

There are64 complex matter modes. With gamma_i=c_i+c_i† and beta_i=-i(c_i-c_i†), their total parity is product_i(-i gamma_i beta_i). Moving every beta to the right introduces (-1)^(64*63/2)=+1, while (-i)^64=1. Define active and spectator chirality by P_gamma=(-i)^32 product_i gamma_i and P_beta=(-i)^32 product_i beta_i. Both phases equal1, so exactly P_total=P_gamma P_beta. The physical Gauss carrier has P_total=+1, not independently chosen active or spectator parity.

Choose one real orthogonal frame putting K0 into32 canonical two-dimensional skew blocks. Use the SAME frame on gamma and beta. Each chirality changes by the determinant of that frame, so their product and the physical parity relation are unchanged. Let the active vacuum chirality in the original frame be s=±1. If -c>0, the spectator quadratic is a positive multiple of the active quadratic and its unique unconstrained vacuum has the SAME chirality s. If -c<0, every one of the32 block occupations is reversed, changing chirality by (-1)^32=+1. Hence for EITHER sign of nonzero c, the spectator vacuum still has chirality s. It is physically allowed because s*s=+1. This argument does not assume the active vacuum has parity+1 in the original ordering.

The allowed spectator excitations above that vacuum have even occupation count n=0,2,...,32. Their exact leading energies are omega(n-16), with multiplicity binomial(32,n). A scalar sixth coefficient shifts all these equally. The ground is unique, its nonscalar energy is -16omega, and the leading physical gap is2omega. The sum of these multiplicities is2^31, matching the original ground-space dimension. Odd-n states belong to the wrong total parity and cannot supply a smaller physical gap.

## Finite nonzero-penalty consequence

The finite64-site physical matrix has an isolated initial spectral cluster. Its canonical effective matrix is analytic in u for some neighborhood of zero, with the polar branch fixed by the positive overlap convention. Subtract its scalar Taylor polynomial through degree six and divide by u^6. The quotient extends analytically to u=0 and equals Q+O(u) in finite-dimensional operator norm. No thermodynamic bound is asserted.

Since Q has a unique physical ground separated by delta=2|c|sqrt24, continuity (or the elementary eigenvalue norm bound) gives a unique lowest eigenvalue of this cluster for every sufficiently small nonzero real u. Its first gap is

Gap(u)=2|c|sqrt24 u^6+O(|u|^7).

The other unperturbed spectral clusters remain separated by a positive constant for sufficiently small |u|, by finite-dimensional continuity and the original gap. Therefore this cluster's unique lowest state is also the full physical ground, and the displayed gap is the full physical gap near zero. This includes the physically intended positive u; negative u is only a finite analytic statement where the same isolated-cluster argument applies.

The binomial multiplicities are exact for the LEADING coefficient Q. At nonzero u, higher coefficients may split those excited multiplets at order seven or later. They are not asserted to be exact degeneracies of H(u). The ground uniqueness/gap conclusion is conditional on c≠0; if c=0 this proof gives no splitting at sixth order. No explicit radius, practical gap estimate, higher-volume phase, thermal concentration or selected coupling is obtained.
