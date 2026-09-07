# Root derivation and controls

## Nonstationary input

Write H_j for the matter Hamiltonian after event j, D_j=exp(-i d_j H_(j-1))
and U_j=D_j...D_1. Each of the five nonbridge instruments is an isometry
of the surviving CAR representation, with an independent orthogonal Record
flag of amplitude 1/sqrt(2). This reduces the conditional matter calculation
to U_j; it does not make physical branch vectors equal.

The shared battery lift of a map W from H_in to H_out is
sum_(a,b) P_out(b) W P_in(a) tensor T_(a-b). In its Fourier fiber it is
exp(-i tau H_out) W exp(i tau H_in). Adjacent conjugations cancel in the
product when the SAME battery is used. Thus the post-event prefix fiber is
V_j(tau)=exp(-i tau H_j) U_j exp(i tau H_0). Before event j, after the
dwell, replace H_j by H_(j-1). In particular the first pre-event fiber is
D_1 independently of tau. This is an important control for timing.

For a pure input psi, x_(a,b)=P_out(b) U P_0(a) psi and u_(a,b)=a-b give
the exact joint state sum x_(a,b) tensor T_u beta. Its reduced density is
sum_(a,b,a',b') x_(a,b)x_(a',b')^dag K(u-u'). This includes the input's
off-diagonal energy coherences. Deleting them would be a different state.

## Sine packet and energy operator

For beta(E)=sqrt(2/w)sin(pi(E-E0)/w) on [E0,E0+w], zero elsewhere,
translation is (T_u beta)(E)=beta(E-u). The overlap of two translates has
the exact formula, with x=|u-v|/w,

K(u-v)=(1-x)cos(pi x)+sin(pi x)/pi for x<1, and zero for x>=1.

This follows by integrating 2sin(A)sin(B)=cos(A-B)-cos(A+B) over the
intersection of the shifted supports. At x=0 it is1; at x=1 it is0.

The product beta(E-u) beta(E-v) is symmetric about
m=E0+w/2+(u+v)/2. Its energy-weighted odd part integrates to zero, hence

<T_v beta|E_B|T_u beta> = m K(u-v).

Use this matrix element directly for battery energy. Only AFTER evaluating
it compare E_matter+E_battery to the initial total. Defining the battery
energy as the compensating difference would be the scalar bookkeeping
we are testing beyond.

Root numerical control used adaptive direct integration on the exact
overlap intervals for shifts (0,0),(.3,0),(0,-.5),(.3,-.5),(2,2.25),
(-.7,.6),(-2.25,-2) at E0=24,w=1. Maximum overlap disagreement2.45e-15;
maximum energy-moment disagreement6.04e-14. These are diagnostic arithmetic
checks, not rigorous quadrature certificates. The displayed integral proof
is the analytic justification.

## Cap, dimensions and conservation

The parent operator bound ||H_j||<=L*t=12 holds for all prefixes. Initial
battery support[24,25] and matter support[-12,12] give total support[12,37].
The spectral lift conserves total energy term by term: b+(E+a-b)=E+a.
Every reachable battery energy therefore lies in[0,49]. These are spectral
support bounds, not conclusions inferred from its mean. A bounded continuous
energy interval is still an infinite-dimensional battery.

The native Record support and fixed N subspace survive every spectral
projector because the conditional Hamiltonians preserve the appropriate
code/Record sector and N. Prefix flags have equal weights2^(-j) on this
nonbridge-only fixed schedule. The phase pulse has zero particle-number
commutator but generally nonzero H_0 commutator.

## Physical locality left open

The exact spectral lift is defined using eigenprojectors of the connected
matter Hamiltonian. Neither local edge projectors nor bounded support of h_e
proves that this lift is an operation of the physical nearest-neighbor rule.
The numerical test is a conditional apparatus/transport join. Spatial
apparatus realization and autonomous formation remain separate targets.
