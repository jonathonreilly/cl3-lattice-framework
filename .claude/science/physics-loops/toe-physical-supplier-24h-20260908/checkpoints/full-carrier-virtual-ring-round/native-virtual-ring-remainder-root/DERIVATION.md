# Explicit finite-volume fourth-order spectral approximation bound

Use the supplied finite native low-charge model H(g)=UD+gV, V=sum_e lambda_e P_low A_e P_low, real lambda_e and real g, U>0, on the connected even cubic tori with extents at least four. P projects onto all ice states and Q=I-P; signed vertex charges are still Q_v. Put B=sum_e|lambda_e|, a=|g|B, d=2U, and assume a<=U/4=d/8. The a=0 case is exact and may be separated below.

The fourth-order Hermitian coefficient H4 is the independently derived native ring plus scalar in the parent research proofs. Let C=sum lambda_e^2, c=g^2 C and

    K4 = -c/d P + g^4 H4,
    H4 = -P V R V R V R V P + C^2/d^3 P,
    R=Q(UD)^-1 Q.

Claim: for every eigenvalue E in the low-energy cluster of H(g) descending from the ice subspace,

    dist(E, spectrum(K4)) <= a^6/U^5.

This is a finite-volume, one-sided spectral-distance bound; it does not assert eigenvector error, individual multiplicity matching, a thermodynamic expansion, a selected physical coupling or a useful extensive-volume convergence regime. B scales with the number of edges for uniform nonzero couplings.

## Isolation and energy size

The unperturbed Q spectrum is at least d. Since ||gV||<=a, Weyl inequalities put exactly dim(P) eigenvalues in [-a,a] and all others above d-a. The min-max principle applied to the P trial space gives E<=0 for every member of the low cluster, because PHP=0. For each such E the Q block of H(g)-E is positive, at least d-a. Its eigenvector has nonzero P component p, and the exact Schur equation gives

    E p = -g^2 P V Q [Q(H0+gV-E)Q]^-1 Q V P p.

Consequently |E|<=e:=a^2/(d-a), sharper than the Weyl estimate. This uses neither stationarity nor a probabilistic approximation.

## Expansion with parity retained

All ice strings contain exactly 3|vertices|/2 occupied edges. The parity operator (-1)^(sum x_e) commutes with H0,R,P,Q and anticommutes with V. Every P-to-P word with an odd number of V factors is therefore zero, even when resolvent powers or Q projections intervene.

Expand the Q inverse around H0 using K=R^(1/2)(gQVQ-EQ)R^(1/2). Its norm is at most k=(a+e)/d=a/(d-a)<=1/7. The zeroth and first retained terms give -c/d P - E c/d^2 P. The two-V term inside the inverse gives -g^4 A4, where A4=P V R V R V R V P. Odd-V terms vanish. All other terms are bounded, before normalizing the P equation, by

    Rerr <= a^2 e^2/d^3
            + a^2(3a^2 e+e^3)/d^4
            + (a^2/d) k^4/(1-k).

The first summand is the two-E term in inverse order two. The second retains the three mixed placements of two gV factors and one E, plus three E factors, in inverse order three. The inverse tail beginning at order four is the last summand. Terms with one or three gV factors are exactly zero, not bounded as lower-order errors. This estimate uses ||R||<=1/d and submultiplicativity, so does not assume commuting perturbations.

Thus

    (1+h) E p = [-c/d P - g^4 A4 + remainder] p,
    h=c/d^2 >=0, ||remainder||<=Rerr.

The scalar denominator is exact at this retained order. The difference between (-c/d P-g^4 A4)/(1+h) and K4 is

    [h g^4 A4 - (c h^2/d)P]/(1+h),

whose norm is at most 2a^6/d^5, since ||g^4 A4||<=a^4/d^3 and c<=a^2. Therefore the normalized residual of the Hermitian operator K4 on p has norm at most Rerr+2a^6/d^5. The spectral theorem bounds dist(E,spectrum(K4)) by this residual divided by ||p||; all preceding operator estimates already multiply ||p||.

## Explicit constant

Writing r=a/d<=1/8, divide Rerr+2a^6/d^5 by a^6/d^5. The result is bounded by

    1/(1-r)^2 + 3/(1-r) + r^2/(1-r)^3
      + 1/[(1-r)^3(1-2r)] + 2.

Each term increases on [0,1/8]. At r=1/8 the sum is 64/49+24/7+8/343+2048/1029+2, which is less than9. Hence the distance is at most9a^6/d^5=9a^6/(32U^5), and the simpler stated a^6/U^5 bound follows. The constants are deliberately conservative. This argument controls eigenvalue distance to the actual fourth-order native operator, including its winding four-cycles at extent four, not an RK Hamiltonian with an added flippability potential.
