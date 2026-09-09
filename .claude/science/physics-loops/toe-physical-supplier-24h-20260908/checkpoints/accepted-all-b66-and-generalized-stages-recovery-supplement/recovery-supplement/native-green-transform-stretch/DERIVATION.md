# Positive one-dimensional transform for the native B function

No physical quadrature is executed. Let X=4h² sum_a sin²(k_a), with0<=X<=12h², A(s)=E[(X+s²)^-1], and B(s)=E[sqrt(X)/(X+s²)], s>0. The actual Dirac distribution has no atom at0 and finite A(0).

## Positive transform and exact scalar input

Define G_s(t)=E[X/((X+s²)(X+t²))]. Tonelli and integral_0^infinity dt/(X+t²)=pi/(2sqrt X) give

 B(s)=(2/pi) integral_0^infinity G_s(t)dt.       (1)

The integrand is nonnegative and decreasing in t. It uses only A:

 G_s(t)=[t² A(t)-s² A(s)]/(t²-s²), t!=s;
 G_s(s)=A(s)+(s/2)A'(s).                        (2)

The apparent singularity is removable. Independent interval values in the numerator can suffer cancellation near t=s; a future implementation must either use the derivative or a joint enclosure, not silently lose significance. In squared parameter z, derivative of z E[1/(X+z)] is E[X/(X+z)²]>=0, giving an alternative divided-difference enclosure as the average of this positive derivative between s² and t². This derivative is exactly the A/A' combination already available from the2D reduction.

Low and high tails obey

 integral_0^epsilon G_s(t)dt <=epsilon A(s),
 integral_T^infinity G_s(t)dt <=[1-s²A(s)]/T <=1/T.

These bounds alone would require a large high cutoff. A native compact-spectrum expansion removes that cost.

## High tail with geometric convergence and exact moments

For T²>12h² expand1/(X+t²) in powers of X/t² and integrate each term:

 integral_T^infinity G_s(t)dt
 =sum_(n=0..m-1) (-1)^n C_n(s)/[(2n+1)T^(2n+1)] + remainder,
 C_n(s)=E[X^(n+1)/(X+s²)]>=0.

The remainder has sign(-1)^m and magnitude at most

 (12h²)^m /[(2m+1)T^(2m+1)],                   (3)

since X/(X+s²)<=1. Coefficients need only A(s) and polynomial moments: C0=1-s²A(s), Cn=E[X^n]-s² C_(n-1). Their true values are positive, but interval recurrence errors must be retained. The moments are explicit rational multiples of h^(2n): E sin^(2j)k=binom(2j,j)/4^j and the three independent coordinates are combined by the multinomial formula. Choosing T²=48h² gives ratio1/4 in(3); m grows logarithmically with requested accuracy. No Bessel or elliptic evaluation is required.

## Middle interval quadrature with a quantitative analytic bound

G_s is analytic for Re t>0. For a disk |z-c|<=c/2, factor X+z²=(sqrt X+iz)(sqrt X-iz). Each factor has modulus at least Re z>=c/2, so |X+z²|>=c²/4. Therefore

 |G_s(z)| <=4 E[X/(X+s²)]/c² <=4/c².

There is also the bound |X+z²|>=X/2 on this disk: writing z=u+iv, |v|<=c/2 and u>=c/2 gives |v|<=u; then |X+z²|²=(X+u²-v²)²+4u²v²>=X². In fact the stronger bound |X+z²|>=X holds because u²-v²>=0. Thus |G_s(z)|<=A(s). A safe envelope is M(c)=min(A(s),4/c²). The circular disk indeed has |Im z|<=Re z, since its radius c/2 is smaller than the distance c/sqrt2 to either line Im z=+/-Re z.

For a dyadic interval [a,2a], center c=3a/2, the Bernstein ellipse rho=5/2 lies inside this disk: maximum displacement29a/40<c/2. A p-node positive Gauss rule has error at most

 (20/3) a M(3a/2) (4/25)^p.                    (4)

This follows from the Chebyshev contour tail of degree2p-1 and the positivity/total weight of the rule, exactly as in the reviewed projector quadrature. Summing dyadic intervals is finite with explicit endpoints. Hence the middle discretization requires O(log(1/epsilon)) intervals and O(log(1/epsilon)) nodes per interval, while the high tail uses logarithmically many exact moments. This is a certified O(log²) SCALAR CALL count; the accuracy/cost of each2D A call remains separate.

## What this does and does not improve

This replaces the3D B box integration by one-dimensional positive quadrature plus the already2D A oracle, with explicit low tail, analytic middle error and rapidly convergent compact-spectrum high tail. It is computationally meaningful only if A and its divided differences can be enclosed sufficiently sharply and cheaply; near-node and near-coincident cancellation may otherwise dominate. The same transform differentiated in s gives B'(s)=-(4s/pi) integral E[X/((X+s²)²(X+t²))]dt, again a positive magnitude with analogous bounds and A-derivative inputs. No actual costs, scalar Green values, Gram spectra or physical matrices are claimed here.
