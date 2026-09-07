# Cold adversarial review of refined Wilson bound

PASS: all reviewed inequalities support C=29 for beta>=2048, conditional on the same exact parent Fourier identity and frozen W2 already independently checked. No orbital source, certificate or repository file was edited. This is an independent proof check, not execution of the author's certificate as evidence.

## Enlarged low region

On a<=beta/2, z_i²<=4a/3<=2beta/3, so the ellipsoid lies inside the scaled torus. The sinc arguments satisfy sum t_j²<=3/4 and individually t_j²<=a/beta<=1/2. Both sinc and quadratic approximants remain in[0,1]. The original product comparison therefore still gives |r|<=a²/(20beta²). For B², v²+2|r|+2v|r|+r² has coefficient at most1/16+1/10+1/80+1/1600<1/5 after factoring a²/beta²; the enlarged cutoff is fully accounted for.

The cosine sixth remainder1/810 follows from the exact fourth-power identity, as in the prior review. With u=a²/(36beta)<=a/72, e^(-a/3+u)<=e^(-23a/72). Expanding e^bB and e^bB² gives respectively cubic coefficients1/810+1/1440+1/144=23/2592 and1/810+1/360+1/72=29/1620. These use the new a/beta<=1/2 rather than reusing the old1/16 reduction. Quartic coefficient1/2592 and quadratic coefficients1/20,1/5 are correct.

## Exact prefactors and low constants

Numerator prefactor times polar Jacobian times |Delta| bound is sqrt(3)/(2pi). Integrating a^(3/2)PN introduces Gamma(n+1/2) with n=4,5,6. After extracting sqrt(pi), sqrt(3)/(2sqrt(pi))<1/2 and alpha^(-1/2)<2 make their product strictly below1. Thus the rational gamma-ratio sum is a valid upper bound, not a missing square-root power. Independently obtained CN_low=25056301536/148035889<170.

For the denominator, the angular identity has normalization integral Delta²e^-alpha a=8pi sqrt(3)alpha^-4. Its differentiated moments are rising factorials(4)_m, giving20,120,840. The1/(24pi²) prefactor leaves sqrt(3)/(3pi)<1/5. Independently obtained CD_low=204884558217216/78310985281<2617. These constants agree with the certificate but were recomputed using a different recurrence for half-integer gamma factors.

## Exact and approximate high tails

For a>=beta/2>=1024, replacing a^(3/2) by a² is valid. Numerator radial prefactor sqrt(3)/(2pi)<1/3 and denominator angular density sqrt(3)/(18pi)<1/30 are both safe. The gamma-tail expressions retain the correct24 powers/factorials and the threshold t=beta/48. Their summands have powers beta^j,j<=5, so each derivative has sign j/beta-1/48<0 throughout beta>=2048. Evaluating only the endpoint is therefore justified.

Independently bounded e^(128/3)>10^18 with a60-term positive Taylor lower sum, rather than the author's150 terms. This reproduces exact-tail bounds below37/10^6 and3869/10^6. No numerical exponential approximation enters the certificate.

For Gaussian approximation tails, beta²<=4a² and beta<=2a give numerator polynomial(9/2)a^4+a^5/18 and denominator5a^5+a^6/18 after including radial powers. Extending the lower integration limit to1024 is conservative. Splitting e^-a/3<=e^-1024/6 e^-a/6 and extending remaining moments to0 is valid. An independent180-term positive Taylor lower sum proves e^(512/3)>10^60 (the author's500 terms are also sufficient). The resulting rational integrals are each below1/1000, and combined low+both tails lie below171 and2618. Approximation tails outside the torus are included; no unstated local-CLT replacement is used.

## Denominator and ratio cross-check

D0>14 follows from sqrt(3)>5/3 and pi<22/7. The worst endpoint1-1/2048-2618/(14*2048²)>999/1000 is correct and improves thereafter. With the independently reviewed coefficient/normalization, the ratio identity remains unchanged. Recomputed coefficient76675625/2685312<29. The separate global W/W2 estimates also have the right squaring/exponential thresholds; this review does not rely on a numerical optimum or quadrature to establish them.

No actionable defect found. The theorem is an absolute multiplier expansion with the declared conditional identity and domain, not a full operator, spectral-gap or physical-theory result. No radius/error lower bound or apparatus conclusion is implicated.

Reviewed hashes:

- REFINED_BOUND.md: 497aa10ffed66c77cd8a5011eb27b880713ab49e65f71b51562818a73f47c415
- refined_certificate.py: 7e36ba8b47d64215c362d37f87c203a5a8bdede18361c21ad604e787e31194a1
- refined_certificate.json: edcff23d3ce41fb69e8af5ff006f955ce2e3265dee31c62ac00f19ee79d40725

Independent exact recalculation is in independent_check.py and result.json; it does not import the orbital certificate.
