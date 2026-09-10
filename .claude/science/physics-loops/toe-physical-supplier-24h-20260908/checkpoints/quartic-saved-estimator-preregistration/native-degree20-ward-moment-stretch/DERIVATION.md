# Degree-(2,0) also closes on c,nu,omega5

SOURCE ONLY, unreviewed, h=1. No native moments or accepted scalar values evaluated. This changes the first polynomial, so the all-q scheduling screen for fixed degree-one p does not apply. It makes no claim that the resulting error gate will close.

Use the reviewed six vectors a=e0,d=d_A,k=Ka,v=Kd,z=K²a,w=K²d and their dot/covariance table from degree11. Define local Clifford polynomials representing D^n Omega:

 O0=1,
 O1=B=i gamma(a)gamma(d),
 O2=2-gamma(k)gamma(d)-gamma(a)gamma(v),
 O3=-2B+2i gamma(a)gamma(k)+i gamma(d)gamma(v)
       -i gamma(z)gamma(d)-2i gamma(k)gamma(v)-i gamma(a)gamma(w). (1)

All O0..O3 are at most quadratic. Their displayed orders matter; O2 is NOT Hermitian as a local operator, although O2 Omega=D²Omega. The recursion is D O Omega=([H0,O]+BO)Omega. In deriving O3, gamma(d)gamma(k)gamma(d)=4gamma(d)-2gamma(k), using d·k=2 and||d||²=2. No arbitrary quartic term is discarded.

The required vacuum moments m0..m6 can therefore be evaluated by

 m0=<O0,O0>, m1=<O0,O1>, m2=<O1,O1>, m3=<O1,O2>,
 m4=<O2,O2>, m5=<O2,O3>, m6=<O3,O3>.                           (2)

Wick words in(2) have length at most4. All table entries depend only on c,nu,omega5 and the fixed integer even moments, so no mu7 or new spatial covariance is needed for these moments.

A residual-optimal quadratic p(x)=p0+p1x+p2x² solves the3x3 system H_ij=m_(i+j+2), b_i=m_(i+1), i,j=0..2. The alternative inverse-variational choice uses H_ij=m_(i+j+1),b_i=m_i. Positivity/nonsingularity must be enclosed. Any rational selected coefficients remain admissible when the actual residual

 r²=m0-2 sum_i p_i m_(i+1)+sum_ij p_i p_j m_(i+j+2)

is certified afterward. Original covariance and coefficient correlations are retained by evaluating these finite expressions with the authenticated scalar intervals.

Let O=p0 O0+p1 O1+p2 O2, J=2i gamma(d), M=[D,J]=-2gamma(v)-8gamma(a). Then

 b=J O Omega,
 Db={J(p0 O1+p1 O2+p2 O3)+M(p0 O0+p1 O1+p2 O2)}Omega.          (3)

Each is at most cubic and uses the SAME six vectors. Thus s0=<b,b>,s1=<b,Db>,s2=<Db,Db> need Wick words at most6 and again only c,nu,omega5. A constant q selected as s1/s2 has residual t²=s0-2q s1+q²s2. The same rigorous e858 gap error then applies, but now with the new first-polynomial residual E. This is the immediate alternative if the saved all-q screen excludes the degree-one p family.

## Cross-pair nominal needs no new spatial scalar

For disjoint C,A use white vectors(a,v_A,v_C) and black vectors(d_A,d_C,k). White dot Gram is
 [[1,-2,-2],[-2,L2_A,ell],[-2,ell,L2_C]],
black dot Gram is
 [[2,0,2],[0,2,2],[2,2,6]],
with L2=12(P),14(O) and ell=number of opposite neighbor pairs split across A,C. White-to-black kappa is
 [[-c,-c,-3c],[ed_A,e_CA,nu/3],[e_CA,ed_C,nu/3]],
where ed_P=6c,ed_O=nu/3,e_CA=ell*(nu/6-3c). Reverse covariance is negative transpose, same-color covariance zero. The new cross dot <v_A,v_C>=ell follows from the two-step K² kernel and the opposite-pair self value14=12+2. This is a native geometric identity, not a consequence of generic Clifford algebra alone.

The exact nominal ordered edge is

 Re <O_C^* O_A> + q_A Re <O_C^* gamma(a) J_A O_A>.             (4)

Wick length is at most6. In particular replacing O_C^* by O_C would be WRONG at degree2 because O2 is not Hermitian as a local representative. Formula(4), summed over the same90 ordered edges/five orbits, requires only c,nu. omega5 enters the residual moments and selected coefficients through(2),(3), not a new cross-space supplier.

## Cost and limits

Two classes and two fixed first choices need3x3 interval-certified candidate solves, seven vacuum moments with at most4 fields, three inner-source moments with at most6 fields, and90 nominal edge contractions. Literal expansion has fixed short lists, so a bounded cached Wick implementation is feasible in principle without a lattice-sized matrix. No native timing or precision sufficiency is asserted. The current32768-bit exact rational cap may require dyadic coefficient rounding (with subsequent residual recertification, which remains valid for any rational p) to prevent denominator growth. That implementation choice must be frozen/reviewed before an actual gate run.

Degree-(2,1) is not asserted to close on this same scalar family: D²b reaches additional K powers and may require a seventh absolute moment. It is unnecessary to assume that extension before testing the cheaper changed-p candidate.
