# Independent shifted-moment interpretation check

For a positive normalized spectral measure on ω>0, a=Eω and rα=E(ω+α)^−1, define bα=1/rα and cα=sqrt((a+α)/rα). Cα=(a+α)rα≥1 by Cauchy–Schwarz. With x=(ω+α)/cα, E(x+x^−1−2)=2(sqrt(Cα)−1). Thus mass outside [cα/r,cα*r] in the SHIFTED variableω+α is at most2(sqrt(Cα)−1)/(r+r^−1−2). In physical energy this interval is[cα/r−α,cα*r−α], intersected withω>0. It need not be narrow, positive at its lower endpoint, or centered at a genuine pole. cα is a shifted geometric center, not a physical excitation energy.

For fixed finite spectral support, Cα=1+Var(ω)/α²+O(α^−3), so Cα→1 automatically asα→∞. A fixed multiplicative band inω+α then has physical width cα(r−1/r)=O(α), growing rather than narrowing. For example ν=(δ1+δ9)/2 has two separated equal-weight levels forever, while Cα=(α+5)/2*[1/(α+1)+1/(α+9)]→1. This is an exact adverse interpretation example, not an ice-model spectrum. Any claimed physical-pole concentration must translate the interval back toω and report its absolute width and lower endpoint.

The geometric-lag identity in the reviewed draft has the correct coefficient: withq=M/(M+α), E[P^K]=(1−q)(I−qP)^−1=α(H+α)^−1. Divide endpoint product byαS. Discarding K>Kmax as ZERO leaves omitted normalized absolute contribution≤q^(Kmax+1)/α by stationary Cauchy–Schwarz; clippingK would instead add endpoint mass and change the target. This bound concerns the exact stationary normalized expectation, not a random empirical denominator. A ratio estimate and its finite-chain uncertainty require separate reporting.

Elementary P is essential: P^M generally changes the resolvent. Independent RNG namespaces must separate geometric K, endpoint trajectory and advancing origin chain, including truncation branches. Stationarity is a sampling premise after a finite burn, not established by correct elementary transitions or passing two burn comparisons. No reviewed statement yet supplies uniform mixing or zero-regulator tail control.

Read full DERIVATION and L4_PROPOSAL. These formulas/scope are sound. Actual pilot code review pending its freeze; this memo does not certify forthcoming implementation or production.
