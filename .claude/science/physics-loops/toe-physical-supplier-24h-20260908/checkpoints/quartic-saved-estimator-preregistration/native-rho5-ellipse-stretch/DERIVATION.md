# A wider analytic ellipse for the same native integral rules

Status: source-only conditional support, independent review pending. This is a new analytic error certificate design, not a new physical integration or a relabeling of any completed rho4 protocol. No catalog, pole list, matrix, saved node or scalar interval was loaded. Its prospective consumer is an independently bound refinement of the accepted rho4 moment/B certificates, using their same centers and separately preserved low/high/input/rounding errors.

## 1. Positive real part is enough; Re(z²)>0 is not necessary

On a panel [a,2a], take the Bernstein ellipse rho=5:

    z/a = c + A cos(theta) + i B sin(theta),
    c=3/2, A=13/10, B=6/5.

The closed ellipse has Re(z)>=a/5>0. Put x=c+A cos(theta), y=B sin(theta), d=c²-A²=14/25. The identity

    x²-d sin²(theta)=(A+c cos(theta))² >=0

gives y²/x²<=B²/d=18/7. Therefore Re(z²)/|z²| >= -11/25. The same cone bound holds in the entire closed ellipse by convexity (x>0, |y|<=sqrt(18/7)x). For every X>=0 and w=z²,

    |X+w|² >= X²+|w|²-(22/25)X|w|
              =(|w|-(11/25)X)²+(504/625)X²
              >=(16/25)X².

Thus |X/(X+z²)|<=5/4 when X>0. This relaxed resolvent majorant permits rho5 even where Re(z²)<0. There is no pole in the ellipse because Re(z)>0 excludes z=+/-i sqrt(X). At X=0 the integrable majorants below are interpreted almost everywhere. On compact subsets, holomorphic dominated integration uses these majorants; no unproved contour continuation is imported.

## 2. Uniform integrand bounds

Assume the same supplied native measure, 0<=X<=12, E X=6, A0=E[1/X]<=17/60 and -A'(s)<=3. The latter bound has the explicit density proof in the completed moment source packet; it is not a numerical derivative premise.

For A(z), Q_mu(z)=E[X/(X+z²)], and Q_nu(z)=E[X²/(X+z²)], the uniform ellipse bounds are respectively

    M_c=17/48, M_mu=5/4, M_nu=15/2.

For each fixed real positive s, the B integrands are

    G_s(z)=E[X/((X+s²)(X+z²))],
    H_s(z)=2s E[X/((X+s²)²(X+z²))].

Their bounds are M_G<=5A(s)/4<=17/48 and M_H<=-5A'(s)/4<=15/4. The sign convention remains H=-partial_s G, with the final Bprime equal to minus the integrated H factor. This proof changes neither the divided-difference centers nor their near-coincidence/input error budgets.

## 3. Gauss26 error on all 67 panels

The existing Chebyshev argument for a length-a panel gives absolute Gauss26 error at most

    4a M rho^-52/(1-rho^-1).

It uses exactness through degree51 and positivity/total mass of the exact rule. Sum of panel lengths a is below8, so rho5 gives an absolute radius below40 M 5^-52. Safe rational radii are

    R_c = (85/6) 5^-52,
    R_mu = 50 5^-52,
    R_nu = 300 5^-52,
    R_G = (85/6) 5^-52,
    R_H = 150 5^-52.

Compared with the corresponding rho4 moment radii and the prior common B/H radius128*4^-52, the moment/H analytic radius ratio is (64/75)(5/4)^52, greater than90000. The separate B radius improves still more because its own integrand bound is smaller than the old common H bound. This is a ratio of one analytic error component, not a claim that any final interval or downstream physical error improves by that factor.

## 4. Honest reuse boundary

A future new certificate may retain the exact completed node centers, authenticated scalar input boxes and low/high tails, replacing only the analytic quadrature radius after separately binding this proof. It must reconstruct the final interval from the preserved component decomposition, keep every input/node/low/high/rounding/pi contribution unchanged, and enforce a newly frozen actual-width target. It may not multiply an old final width by the analytic improvement ratio or shrink an old cache radius around an unrelated midpoint. Raw A truth remains inherited.

For B, the accepted width ledger contains a common old quadrature term. Recover pre-factor radii as the exact saved node sum plus low/high/rem/rounding terms and insert R_G/R_H separately; do not infer them by floating subtraction from a final display. Reuse centers only when their product-coefficient midpoint choice, tail remainder centering and rounding budget match the accepted new center protocol. The original rho4 targets and outcomes remain immutable.

Large-s high-tail input amplification, small-s low error, raw input precision and coefficient conditioning can dominate after this change. No actual refined interval, Gram, leakage, propagation or alpha result is supplied here. A resource contract, independent source review, exact remote preregistration and a separate saved-component reconciliation remain required before any new numerical certificate.
