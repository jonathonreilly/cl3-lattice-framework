# Explicit provisional second-order Wilson multiplier bound

Independent constructive derivation after PREREGISTRATION.md. Constants are deliberately loose, derived without numerical fitting. This is ready for cold coefficient/bound review, not a retained verdict. Exact recurrence/Fourier identity is the supplied parent premise. No operator-spectrum, gap or physical-theory conclusion.

## Statement

On Omega=[1/4,2]^2, for x=(p+rho)/sqrt(beta), p in N0², rho=(1,1), define v_beta=beta^-3/2 c_p(beta)/c_0(beta) using the exact native reflection integrals. Let W=H exp(-Q), H=xy(x+y)/2, Q=x²+xy+y². The frozen coefficient is

W2=(3−7Q/4+Q²/4)W.

The following explicit sufficient constants result from the estimates below:

beta0=272104869,
C=4738711459316761536.

For every real beta>=beta0 and every such grid point in Omega,

|v_beta(p)−W(x)−W2(x)/beta| <= C/beta².

The huge beta0 is an analytic sufficiency threshold, not a physical parameter choice or an observed onset. Improving constants is optional; the present goal is a correct second-order coefficient and explicit absolute rate.

## Scaled integrals and coefficients

Put a=z1²−z1z2+z2², Delta=(2z1−z2)(z1−2z2)(z1+z2), and B_beta=product_j sinc(l_j/(2sqrt(beta))), where l=(2z1−z2,z1−2z2,z1+z2). On the scaled torus T_beta=[−pi sqrt(beta),pi sqrt(beta)]²,

N_beta(x)=(2pi)^-2 integral_Tbeta exp(−beta psi(z/sqrt(beta))) exp(−iz.x) iDelta B_beta dz,
D_beta=[6(2pi)^2]^-1 integral_Tbeta exp(−beta psi(z/sqrt(beta))) Delta² B_beta² dz.

Exactly v_beta=N_beta/D_beta. The beta powers are beta^(5/2)e^-beta c_p in N and beta^4 e^-beta c_0 in D. Fourier signs follow the parent exactly.

Let D0=27sqrt(3)/pi>1. Leading transforms give N0=D0 W. The order1/beta numerator factor is a²/36−a/4; denominator factor is a²/36−a/2. Since a Fourier multiplication corresponds to−3L,

N1=D0[(L²/4)+(3L/4)]W=D0(W2−W).

For the denominator, the radial density e^(-a/3)Delta² has a moments12 and180. Hence D1/D0=180/36−12/2=−1. The identities LW=(Q−4)W and L²W=(Q²−10Q+20)W establish the frozen W2. All four polynomial/differential identities used here were independently checked symbolically during intake; the estimates below do not use a fitted coefficient.

## Low-frequency absolute remainder

Use the ellipsoid a<=beta/16, which lies inside T_beta. Let u=a²/(36beta), b=a/3−beta psi(z/sqrt(beta)), and v=a/(4beta). Taylor inequalities give

0<=b<=u, |b−u|<=a³/(90beta²).

Indeed sum of fourth powers z1^4+z2^4+(z1−z2)^4=2a², and the sixth-order cosine remainder is bounded by sum sixth powers/(2160beta²); each squared linear form is at most4a/3. The1/90 bound is generously larger than the resulting1/810.

Since sum l_j²=6a and |sinc(t)−(1−t²/6)|<=t^4/120,

|B_beta−(1−v)|<=a²/(20beta²), |B_beta|<=1,
|B_beta²−(1−2v)|<=a²/(5beta²).

For the first estimate, compare the product of sinc factors with product(1−t_j²/6), using factors in[0,1], then bound pair cross terms by(sum t_j²)²/72. The total is at most(sum t_j²)²/45=a²/(20beta²). For the squared estimate, write B=1−v+r and use a/beta<=1/16; v²+2|r|+2v|r|+r² <a²/(5beta²).

Also |exp(b)−1−u|<=exp(u)[a^4/2592+a³/90]/beta². Since u<=a/576, exp(−a/3+u)<=exp(−a/4). Multiplying the preceding estimates yields, for either the numerator B or denominator B² factor, absolute integrand-factor remainder at most

beta^-2 exp(−a/4)(a²+a³+a^4).

For example the numerator bound before enlargement has a²/20+a³(1/90+1/11520+1/144)+a^4/2592; the denominator has a²/5+a³(1/90+1/2880+1/72)+a^4/2592. Both are below the displayed polynomial. Multiply by |Delta| or Delta² respectively, and by their constant Fourier prefactors.

## High-frequency remainder without an unproved local-CLT tail

For all k in[−pi,pi]²,

psi(k)>=(2/(3pi²))(k1²+k2²)>=4a(k)/(9pi²)>=a(k)/24.

The first inequality uses only1−cos t>=2t²/pi² on[−pi,pi] and discards the third nonnegative cosine term. Thus the scaled exact integrand is bounded by exp(−a/24)|Delta| or exp(−a/24)Delta² everywhere, because |B_beta|<=1 globally.

Outside a<=beta/16, beta<=16a. Multiplying the exact tail plus the leading/first-order Gaussian approximation tails by beta² bounds their combined factor by

exp(−a/24)(516a²+a³) for the numerator,
exp(−a/24)(520a²+a³) for the denominator.

This includes the Gaussian region outside T_beta: integrate the approximation tail over the whole plane, whereas the exact tail only exists in T_beta. Combining low and high bounds is safely dominated by

exp(−a/24)(600a²+3a³+a^4).

No asymptotic tail replacement or fitted cutoff is used.

## Explicit remainder constants

Use |Delta|<=3a^(3/2), Delta²<=8a³, and

integral_R² f(a) dz=(2pi/sqrt3) integral_0^infinity f(a) da <4 integral_0^infinity f(a) da.

Both Fourier prefactors are less than1; discarding them enlarges the bounds. Since a^(3/2)<=1+a² and integral a^m exp(−a/24)da=m!24^(m+1), define

CN=12{600[2!24³+4!24⁵]+3[3!24⁴+5!24⁶]+[4!24⁵+6!24⁷]}
  =41831183351808,
CD=32{600*5!24⁶+3*6!24⁷+7!24⁸}
  =18510264831836160.

We obtain globally in x (before restricting the final ratio bounds),

|N_beta−D0[W+(W2−W)/beta]|<=CN/beta²,
|D_beta−D0(1−1/beta)|<=CD/beta².

These inequalities hold at least for beta>=1 with the above decomposition. They are absolute bounds; cancellation is retained in the coefficient derivation, not thrown away before extracting it.

## Positive denominator and ratio

Choose beta0=1+floor(sqrt(4CD))=272104869. Then beta>=beta0 implies beta>=4 and CD/beta²<=1/4<D0/4. Hence D_beta>=D0/2>0.

On Omega, H<=8 and Q<=12, so |W|<=8 and |W2|<=480. Write N=D0[W+(W2−W)/beta]+rN and D=D0(1−1/beta)+rD. Subtracting D[W+W2/beta] from N gives exactly

rN+D0 W2/beta²−rD[W+W2/beta].

Using beta>=4, |W+W2/beta|<=128 and D>=D0/2, D0>1,

|N/D−W−W2/beta|
 <=[2CN+960+256CD]/beta²
 =4738711459316761536/beta².

This completes the provisional explicit bound. The remaining obligation is independent cold verification of the exact Fourier coefficient normalization, scalar inequalities and arithmetic, not a missing numerical eigenfunction or an assumed boundary spectral expansion.
