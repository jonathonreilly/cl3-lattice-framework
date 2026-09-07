# Independent cold check of analytic Perron sign route

PASS for the written NEGATIVE_SIGN_PROOF.md and sign_certificate.py. I first independently derived the estimates from the communicated formulas, then read the completed proof and certificate. The written proof includes the necessary bounded-truncation justification. No numerical Nystrom observation is used in this review.

Let X=S M_sqrt(W), so T0=XX* and B=X*X=M_sqrt(W)e^L M_sqrt(W). If T0 phi=mu phi with ||phi||=1, then u=mu^-1/2 X*phi is normalized and Bu=mu u. Consequently |u|²=W|Sphi|²/mu, and d0/mu=<u,Ru>, R=Q(Q-7)/4. This links the kernel argument to the actual insertion coefficient, not a trial-state expectation.

## Positivity and unbounded weight

B is positive trace class and B>=mu|u><u|. Let g=(R+1)+ and first use g_N=min(g,N). Congruence by bounded M_sqrt(g_N), followed by trace monotonicity, gives

    mu <u,g_Nu> <= Tr(M_sqrt(g_N) B M_sqrt(g_N)).

The right side equals integral g_N W s_1^C(x,x)dx, by the positive heat-kernel/HS factorization. As N increases, monotone convergence gives the same inequality for g; finiteness follows from gW's polynomial-Gaussian envelope and the free diagonal bound s_1^C<=sqrt(3)/(2pi). One must not simply treat unbounded M_gB as a bounded operator without this argument. Since R<=-1+g, the result is

    d0/mu <= -1+J/mu,
    J <= sqrt(3)/(2pi) integral_C g(Q)W.

## Independent radial normalization

Use u=√3(x+y)/2,v=(x-y)/2 and polar u=√q cosθ,v=√q sinθ. The chamber is -pi/6<θ<pi/6, Q=q, dxdy=dq dθ/√3 and H=q^(3/2)cos(3θ)/(3√3). Therefore

    integral_C H F(Q)= (2/27) integral_0∞ q^(3/2)F(q)dq,
    integral_C H²e^-aQ=pi/(27√3) a^-4.

These factors were recomputed directly, not assumed from the new certificate. The trace prefactor is thus sqrt(3)/(27pi).

## Tail split

The pointwise inequality

    g(q) <= (1-3q/2)+ + [q(q-6)/4]1_(q>=6)

holds by checking0<=q<=2/3,2/3<=q<=6,q>=6. In the middle interval R+1<=0 by convexity and its negative endpoint values. After discarding e^-q<=1, the low integral is bounded by(4/35)(2/3)^(5/2)<1/24; this inequality is verified by squaring positive rationals.

For q=6+s, concavity sqrt(6+s)<=sqrt6(1+s/12) bounds the high integral by20sqrt6 e^-6. The polynomial moments are36+30+12+2=80 before its prefactor1/4. A19-term positive Taylor lower sum already proves e6>400; sqrt6<5/2 then gives a strict bound1/8. Consequently J<sqrt3/(27pi)*(1/6)<7/1944, using sqrt3<7/4 and pi>3.

## Rayleigh lower bound and sign

The exact Dirichlet heat solution is

    e^(tL)W=(1+t)^-4 H exp[-Q/(1+t)].

Independent symbolic differentiation checks the PDE and initial value. It vanishes on the chamber boundary, remains L² with the required smoothness, and uniqueness of the Dirichlet heat solution identifies it; no trial eigenfunction assumption occurs. At t=1, e^L W=Hexp(-Q/2)/16.

The normalized trial sqrtW gives

    mu >= <W,e^L W>/integral W
        =2sqrt(pi)/(243sqrt3) >2/243,

because integral W=sqrt(pi)/18 and the H² integral above at a=3/2 has the stated normalization. Combining this LOWER bound with the positive trace UPPER bound yields

    d0/mu < -1+(7/1944)/(2/243) = -9/16.

The direction of each bound is correct. It follows that d0 is strictly negative. This does not identify the Perron vector with sqrtW, determine d0 exactly, or give an excited-eigenvalue/physical-gap sign. It sharpens the previously undetermined top exact-versus-discrete-saddle difference coefficient only.

Independent symbolic/rational checks are in check.py and result.json. The previous dilation identity remains compatible with this conclusion; its failure to close a variance bound was not a no-go.

The absolute consequence d0<-1/216 is correct: multiply d0/mu<-9/16 by mu>2/243 with the negative-sign direction accounted for. The lower bound -49/16 is strict because an L² density cannot be supported on a measure-zero ellipse. Eventual top ordering follows from the established negative asymptotic coefficient, but no explicit finite-beta onset is supplied or claimed.

Reviewed artifact hashes:

- NEGATIVE_SIGN_PROOF.md: 9d9997c41bc5f99b76a0f2274a0c7f0d7836c83ca261099a5fc2080c3bbc3629
- sign_certificate.py: 952bb4eb3b92f1577b9991f9795389de597af1ab893149a264b7855e315f5193
- sign-certificate.json: 77052e2af6beed70fb583a077d516a1db1795a331de11d4a412bad39a871eef8
