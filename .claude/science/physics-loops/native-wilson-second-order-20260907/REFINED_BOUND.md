# Analytic refinement: C=29 for beta>=2048

New estimate under REFINEMENT_PREREGISTRATION.md; original large-constant proof is preserved. Same exact native integrals, normalization, frozen W2 and Omega. No constants fitted to quadrature. This provisional refinement proves

|v_beta(p)−W(x_p)−W2(x_p)/beta| <=29/beta², beta>=2048.

It is ready for independent review. It grants no full-operator/spectral result. Although the bound becomes numerically useful, the mathematical claim is still only the exact multiplier expansion.

## Low frequencies

Replace the old low region by a<=beta/2. It still lies inside the scaled torus, and squared sine arguments sum to3a/(2beta)<=3/4, so all factors used in the product comparison are positive. The original bounds remain valid:

|B−(1−a/(4beta))|<=a²/(20beta²),
|B²−(1−a/(2beta))|<=a²/(5beta²).

For the second, the enlarged cutoff gives coefficient1/16+1/10+1/80+1/1600<1/5. The exact fourth-power identity supplies the sharper cosine estimate |b−u|<=a³/(810beta²), with0<=b<=u=a²/(36beta). Now u<=a/72, so damping is exp(−alpha a), alpha=23/72.

The exact low remainder factors, after multiplying by beta², are at most exp(−alpha a) times

PN=a²/20+(23/2592)a³+a^4/2592,
PD=a²/5+(29/1620)a³+a^4/2592.

These coefficients follow the same product expansion as the original proof: numerator cubic1/810+1/1440+1/144=23/2592; denominator1/810+1/360+1/72=29/1620.

Retain Fourier prefactors. For numerator use |Delta|<=3a^(3/2), polar Jacobian2pi/sqrt3, obtaining coefficient sqrt3/(2pi) times radial integrals. Gamma(n+1/2)=sqrt(pi)*(2n)!/(4^n n!). Since sqrt3/(2sqrt(pi))<1/2 and alpha^-1/2<2, a fully rational sufficient low constant is

CN_low <= sum_(c,n) c [(2n)!/(4^n n!)] alpha^-n <170,
(c,n)=(1/20,4),(23/2592,5),(1/2592,6).

For denominator use the EXACT angular identity

integral Delta² exp(−alpha a) dz=8pi sqrt3 alpha^-4.

Its m-th radial moment is that expression times(4)_m alpha^-m. With denominator prefactor1/(24pi²), sqrt3/(3pi)<1/5, hence

CD_low <=(1/5)[(1/5)*20 alpha^-6+(29/1620)*120 alpha^-7+(1/2592)*840 alpha^-8] <2617.

Both rational inequalities are checked exactly in the companion certificate; their approximate values169.2583 and2616.294 are not inputs.

## Exact high tail

Keep the global source bound beta psi>=a/24. On a>=beta/2>=1024, |Delta|<=3a^(3/2)<=3a². The numerator prefactor and polar Jacobian give sqrt3/(2pi)<1/3. The denominator's exact angular radial density gives sqrt3/(18pi)<1/30. Therefore beta² times the exact high tails are bounded by

(beta²/3)24³*2!*exp(−t)(1+t+t²/2),
(beta²/30)24^4*3!*exp(−t)(1+t+t²/2+t³/6),
t=beta/48.

Each summand is a positive constant times beta^j exp(−beta/48), with j<=5, and is decreasing for beta>=2048>240. At beta2048, t=128/3. The exact positive exponential-series lower bound exp(128/3)>10^18 gives respective bounds below0.000037 and0.003869. No pointwise oscillatory cancellation is needed for these tail estimates.

## Gaussian approximation high tails

Here beta<=2a. Retaining the leading+first coefficient and using |Delta|<=3a² gives beta² times the numerator approximation tail at most

(1/3) integral_1024^infinity [(9/2)a^4+a^5/18]exp(−a/3)da.

For the denominator it is at most

(1/30) integral_1024^infinity [5a^5+a^6/18]exp(−a/3)da.

Use exp(−a/3)<=exp(−1024/6)exp(−a/6), the exact series bound exp(512/3)>10^60, and full moments m!6^(m+1). Each resulting rational upper bound is less than1/1000. This includes Gaussian integration outside the scaled torus. Thus, after adding exact and approximation tails,

|N−D0[W+(W2−W)/beta]|<=171/beta²,
|D−D0(1−1/beta)|<=2618/beta².

## Global multiplier bounds and denominator

On the positive chamber,

Q³−27H²=(x−y)²(x+2y)²(2x+y)²/4>=0.

Consequently H<=Q^(3/2)/(3sqrt3). Maximizing q^r exp(−q) for q>=0 at q=r and checking positive exponential sums yields

W<1/12 from exp(3)>18,
QW<1/6 from exp(5)>36(5/2)^5/27,
Q²W<1/2 from exp(7)>4(7/2)^7/27.

Hence |W2|<=3W+(7/4)QW+(1/4)Q²W<2/3. These are global absolute bounds, so certainly apply on the preregistered Omega. D0=27sqrt3/pi>14 (use sqrt3>5/3 and pi<22/7). For beta>=2048,

D/D0 >=1−1/2048−2618/(14*2048²)>999/1000.

The exact ratio subtraction from the original proof now gives a sufficient coefficient

(1000/999)[171/14+2/3+(2618/14)(1/12+(2/3)/2048)]
 =76675625/2685312 <29.

Thus the proposed refined bound follows. Every numeric constant in this note is fixed by algebra, a monotone tail bound, a positive series inequality or a rational ceiling. Existing quadrature is only a separate falsifier and was not used to set these constants.
