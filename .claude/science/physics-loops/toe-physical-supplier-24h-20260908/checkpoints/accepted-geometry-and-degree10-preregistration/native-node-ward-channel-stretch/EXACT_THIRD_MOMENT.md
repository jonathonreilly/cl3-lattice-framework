# Optional stronger direct-term theorem from an exact third moment

Source-only successor; the earlier frozen direct bound>3/h² is unchanged. No native moment values evaluated. The full Ward correction is still retained and alpha remains open.

For real orthogonal Majorana vectors a,d with ||a||=1, write B=i gamma(a)gamma(d), c=<B>, mu_a=<gamma(a)Omega,H0 gamma(a)Omega>. With H0=(i/4)gamma^T K0 gamma and one-particle h0=iK0, direct CAR gives

 <B Omega,H0 B Omega>=||d||² mu_a+<d,|h0|d>+2(a^T K0 d)c.       (1)

Indeed [H0,gamma(a)]=i gamma(K0 a), and conjugating the two linear commutator terms by gamma(d)gamma(a) gives the two individual energy expectations plus the displayed covariance term. The sign can be checked on a single occupied quadratic bond: gamma(a)gamma(d) then acts as a scalar on its ground vacuum, and the two energy terms cancel against2K_ad c. This check prevents a spurious positive sign on that correction.

For the actual pair perturbation B_A=i gamma0 gamma(d_A), d_A is the negative signed free center-row contribution on the selected two edges. Therefore ||d_A||²=2h² and e0^T K0 d_A=-2h². The same local spectral measures used in the pair resolvent give

 <d_P,|h0|d_P>=2h² mu,
 <d_O,|h0|d_O>=nu/3,

where mu=<e0,|h0|e0>, nu=<e0,|h0|³e0>. For O the normalized neighbor spectral measure is X/6 times the center measure; for P it is the center measure. Here X=|h0|²/h² and EX=6. Thus, using c=mu/3 and B_A²=2h²I,

 <D_P³>=10h²c,
 <D_O³>=4h²c+nu/3.                                           (2)

These follow from <D³>=<B Omega,H0 B Omega>+2h²c; no impurity-vacuum expectation is substituted.

In h=1 units the exact elementary dispersion moments are EX=6 and EX²=42. Holder/Cauchy imply

 mu>= (EX)^(3/2)/(EX²)^(1/2)=6/sqrt7,
 nu<=sqrt(EX*EX²)=6sqrt7<16.

The first follows from EX<= (E sqrtX)^(2/3)(EX²)^(1/3), not a reversed concavity inequality. Consequently3/4<c<49/60, and (2) gives the uniform bound <D³><43/5. No attained scalar enclosure was read to obtain it.

Repeat the inverse-moment proof with M=43/5 replacing26. Its2x2 moment majorant is positive definite throughout c in[3/4,49/60]. The function

 f_M(c)=(M-4c+c³)/(Mc-4)

has derivative numerator2M c³-12c²+16-M²<0 on that interval. Hence m_A=<D_A^-1> is bounded below by

 m1=1269649/653040.

The unchanged variance/Kneser argument yields

 sum_disjoint<R_C R_A> >=135m1²-180m1
 =506499805921/3158972160 >160                                (3)

in h=1 units, and >160/h² after scaling. This is a stronger direct-term theorem pending independent review. It still does not control the full signed Ward boundary sum or determine alpha.
