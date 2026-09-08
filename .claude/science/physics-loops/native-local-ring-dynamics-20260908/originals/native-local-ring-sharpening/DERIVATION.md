# Sharper constants for the same finite local ring theorem

This separately frozen companion replaces only numerical majorants in proof761aaa6cc6a500a9a96ed66ddf6afce88cf05bb738b1550a4d6d6a5a375378fe. The exact generator, fourth-order ice identification, dressing requirements, finite-volume model and one-sided local dynamical scope are unchanged. The old proof and outputs remain untouched. No root completed sharpening proof was read.

## Homological majorant without commuting against all of D

Use the original construction F_n, S_n=Gamma F_n, K_n=P_D F_n. The exact identity [S_i,D]=-(F_i-P_DF_i) implies ||[S_i,D]||_0<=2f_i, on the original support of size11i. Thus the innermost D commutator need not be bounded by18 times an extensive local intersection estimate.

For ordered compositions c=(i_1,...,i_l), p_j=sum_{a<=j}i_a, define recursively

 f_n = sum_{l>=2,sum i=n} [2f_(i_1) product_{j=2}^l(22p_j s_(i_j))]/l!
       +11 sum_{l>=0,sum i=n-1} [product_{j=1}^l(22(1+p_j)s_(i_j))]/l!,
 s_n=4 f_n.

The empty second composition contributes11 when n=1. All indices on the right are less than n. The first factor uses the exact homological identity; the remaining factors are the already proved support-size commutator bound. Strong support ensures the D commutator has not acquired an extra star. Induction therefore proves these smaller bounds for the SAME coefficients, not a different normal-form gauge. Exact results through order5 are

 s1=44,
 s2=170368,
 s3=1690391296,
 s4=77185410486272/3,
 s5=508096152076812288.

## Radius retaining each degree

Set kappa=1/55. Then S_j support size<=11j gives

 ||S(x)||_kappa <= sum_{j=1}^5 exp(j/5)s_j |x|^j
                  <= sum_{j=1}^5 (5/4)^j s_j |x|^j =:p(|x|).

The rational exponential bound follows from exp(t)<=1/(1-t) for0<=t<1 and exp(j/5)=(exp(1/5))^j. Define rho as the largest point k/2^80 in[0,1] with p(rho)<=1/440. The strictly increasing polynomial allows exact rational binary search. There is no claim of a largest rational below its irrational root. The exact grid maximum is

 rho=2428608877045075437/75557863725914323419136
     approximately3.214237085705386e-5.

The unreduced grid numerator is38857742032721206992. The next grid point fails the bound, verified exactly. On |x|<=rho the old support55 Lie-series argument applies verbatim because110||S||_kappa<=1/4. No shrinking-weight commutator is used in this argument.

Also ||D||_kappa<=18exp(6/55)<=990/49 and ||V||_kappa<=11exp(1/5)<=55/4. Since rho<=1, choose

 M=2(990/49+55/4)=6655/98,
 C_R=2M/rho^6, approximately1.2316421235964582e29.

The exact remainder theorem becomes, for gamma/U<=rho/2,

 Y H Y†=UD+K+R,  [K,D]=0,
 ||R||_(1/55)<=C_R gamma^6/U^5,
 ||K||_(1/55)<=2M gamma/rho.

Thus the sufficient ratio is at most approximately1.607118542852693e-5. These decimal displays are descriptions of exact rational certificates, not certified practical accuracy thresholds. In particular the large C_R and local-dynamics constants still prevent a claim of useful simulation accuracy at the edge of this regime. The old radius was about1.47e-59; this improvement removes artificial coefficient and support-weight losses without changing the theorem.

## Explicit locality parameters after changing the weight

A positive weight is essential; we have not taken kappa to zero. For the edge-adjacency graph use

 F(r)=exp(-r/220)/(1+r)^4,
 C_0=(880/3)^4,
 C_F=9216.

These are sufficient constants for the locality argument. Connected support diameter is at most its size. Since sup_{m>=0}(1+m)^4 exp(-3m/220) <=(880/3)^4, the interaction F-norm is at most C_0||K||_(1/55).

To justify C_F uniformly, a line-graph sphere of radius r>=1 is covered by edges incident to vertices at cubic distance r-1 from one of the two endpoints of its central edge. The infinite cubic sphere has4k²+2 vertices for k>=1 and one for k=0; periodic shortest-distance shells have no more representatives. Multiplying by two endpoints and six incident edges bounds every shell by72(r+1)^2. Hence sup_x sum_y(1+dist(x,y))^-4<=144, and288 is a conservative bound. Splitting the convolution according to which distance is at least half the total gives C_F<=32*288=9216. The exponential triangle inequality supplies the remaining factor.

The commutator-chain exponential rate may be taken as a=2 C_F C_0||K||_(1/55). A corresponding spatial light-cone rate is220a, so a sufficient gamma-dependent rate in the polynomial local estimate is

 v=440 C_F C_0 (2M/rho) gamma.

Fixed-support prefactors remain those obtained by the capped light-cone shell sum; they are independent of volume, U and time. The error still has the form C_X C_R gamma^6/U^5 |t|(1+v|t|)^3. Rotating by UD preserves the strong supports of R and enlarges a generic local observable once by the commuting charge stars, so there is no U-speed inserted into v. Dressing is still required; no bare-ice or global-band statement is added.

## Verification scope

Twenty exact rational predicates verify the recursion, positive grid radius, failed next grid point, Lie threshold, exponential majorants and strict improvement over the old constants. The earlier40 exact native-matrix controls remain valid because the actual generator is unchanged; they were not rerun merely to inflate the count. No numerical time-evolution benchmark, fitted coupling, new phase assertion or canonical-file edit is part of this companion.
