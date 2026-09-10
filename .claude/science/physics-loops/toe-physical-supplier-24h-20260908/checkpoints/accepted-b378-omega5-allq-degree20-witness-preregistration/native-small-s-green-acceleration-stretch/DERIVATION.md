# Uniform small-s acceleration through a checked mathematical bridge

## Imported identity and normalization

Read Guttmann, arXiv1004.1435, section1.2 page5, simple-cubic formula and its defining integral; reference33 identifies Joyce1998 J.Phys.A31,5105–5115. Source: https://arxiv.org/pdf/1004.1435 . This is an explicitly imported lattice-Green-function identity, not a new native physics derivation. With P(z)=E[1-z(sum cos k)/3]^-1, the paper gives

 P(z)=((1-9xi^4)/((1-xi)^3(1+3xi))) [2K(k)/pi]^2,
 k²=16xi³/((1-xi)^3(1+3xi)),
 xi=sqrt(1-sqrt(1-z²/9))/sqrt(1+sqrt(1-z²)).

Use positive roots for0<=z<=1. K is the complete elliptic integral with modulus k; below m=k² is the series parameter. The source formula is the load-bearing mathematical bridge. No numerical value from the paper is imported.

## Native substitution and stable algebra (derived here)

The actual scalar oracle has q=s²+6 and z=6/q, so A(s)=P(z)/q. This follows directly by folding the actual dispersion X=6-2sum cos(2k). For s>=0 rewrite the radical parameter as

 xi²=4/[(q+sqrt(q²-4))(q+s sqrt(s²+12))].        (1)

This rationalization removes cancellation in1-sqrt(1-z²/9) and in1-z² near the node. The second radical is s sqrt(s²+12), not an independently subtracted near-equal number. At s0 equation(1) is finite; the positive one-sided branch is explicit.

For every s>=0, xi²<=1-sqrt(8/9)<1/16. The latter strict inequality is the exact rational comparison8/9>(15/16)². Therefore0<=xi<1/4, d=(1-xi)^3(1+3xi)>=27/64, and

 0<=m=16xi³/d<16/27<1.

The normalized elliptic factor has a positive binomial series derived by integrating the binomial expansion of(1-m sin²theta)^-1/2:

 C(m)=2K(sqrt m)/pi=sum_(n>=0)[binom(2n,n)/4^n]^2 m^n.

Every coefficient is at most1, so retaining N terms has remainder at most m^N/(1-m), uniformly at most(16/27)^N/(1-16/27). All operations are rational interval arithmetic and integer square roots; pi cancels from the normalized series entirely. N depends logarithmically on accuracy and does NOT grow as s approaches0.

If C lies in[S,S+r], square it monotonically. The prefactor (1-9xi^4)/d is positive and at most64/27, and1/q<=1/6. Thus the series-tail contribution to A is at most(32/81)(2S r+r²). Parameter/radical errors must be added by actual interval evaluation; this is not a full floating error certificate. It gives an explicit uniform alternative to the return series whose ratio approaches1 at smalls.

## A0 subtraction, derivatives and B

A0 need not be separately subtracted: equation(1) and the uniformly convergent C series evaluate A(s) directly at arbitrarily small positive s and at0. Computing A0-A(s) by subtracting separate enclosures may still lose relative accuracy. A joint derivative/Taylor enclosure in s, using (1), avoids this: all denominators in (1) stay positive, sqrt(s²+12) stays away from0, and the right-hand expression is one-sided analytic near0. It reflects the physical linear cusp under even extension in s, rather than incorrectly assuming an analytic function of s² there.

Derivatives of C have explicit tails, e.g. sum_(n>=N)n m^(n-1)<=N m^(N-1)/(1-m)+m^N/(1-m)². Chain-rule interval evaluation can therefore certify A' jointly. For the B-transform divided difference, use a shared expression or interval derivative for zA(sqrt z) near coincident parameters; independent high-precision A evaluations alone are not a relative-error guarantee.

## Certification and scope

Next implement the rationalized formula and positive C series with outward roots; independently check the imported modulus/parameter convention against exact return-series coefficients or overlapping certified A intervals before any downstream physical use. A rigorous source-based implementation must bind this mathematical import and independently validate its transcription; the present work does not reprove Joyce's identity. No physical evaluation or new pilot has occurred. Existing A0<=17/60 remains the campaign's established bound until a new certified calculation is reviewed. The model/reference are still supplied, and no alpha sign or value follows from an efficient A oracle.
