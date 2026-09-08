# Local prethermal applicability for the full native soft-penalty model

## Result of the bounded primary-source check

There is a directly applicable published extension of the strong-field theorem; the overlapping stars are not an unresolved onsite assumption. Under the supplied full-carrier Hamiltonian and uniformly bounded edge couplings, one can obtain a volume-independent quasi-local normal form with approximately conserved **dressed D**, plus local-dynamics control for quasi-exponentially long times. This does not yet give the same long-time accuracy for the fourth-order ring Hamiltonian alone.

Three primary papers were inspected, with downloaded PDF/text hashes in SOURCE_RECEIPTS.json. No many-body computation or new stochastic run was performed.

## Exact native hypothesis map (independent derivation)

Let H=UD+V, D=sum_v Q_v², V=g sum_e lambda_e A_e and gamma=|g|sup_e|lambda_e|. Work on finite even cubic tori, full edge-qubit carrier, no low projection. Every Q_v² is diagonal, finite-range, bounded by9 and integer-valued. All commute. D is nonnegative and integer; on the closed bipartite graph it is in fact even by global signed neutrality. None of these facts require the terms to act on independent sites.

For edge e=(i,j), A_e contains X only on e, and Z factors on ordered incident edges. It commutes with Q_v² for every v other than i,j. Its support is contained in S_e=star(i) union star(j), which contains11 physical edges. Crucially, it is **strongly supported** there: every charge-star term not entirely contained in S_e commutes with A_e. The same remains true after conjugating by exp(itD), since all charge-star terms commute. For strongly supported A_Z,B_W, their commutator is strongly supported on Z union W and vanishes for disjoint supports. These are the needed local-algebra properties, not a claim that Q_v² is onsite.

A convenient match to the theorem's cubic-site tensor product stores the three positive-direction edge qubits at their tail vertex, giving local dimension8. Each S_e is contained in at most8 connected cubic cells. A given physical edge belongs to at most11 such S_e; a cell has three edges. Hence the explicit strong-potential bound

j_kappa := 33 gamma exp(8 kappa)

bounds the interaction norm sup_cell sum_{S containing cell} exp(kappa|S|)||V_S||. It is deliberately conservative, independent of volume. Periodic identifications do not increase the count. The standard finite-range commutator/Lieb-Robinson estimates use the torus graph metric and the same uniform degree/growth bounds.

## Published theorem actually used

**Abanin, De Roeck, Ho, Huveneers**, “A rigorous theory of many-body prethermalization for periodically driven and closed quantum systems,” CMP354,809–827 (2017), [primary](https://arxiv.org/abs/1509.05386). Read Sec2.1–2.4,3.1–3.3,5.4. The static theorem as written assumes onsite integer N_x; it cannot be cited directly without the next extension. Its normal form is YHY†=UN+K+E with [K,N]=0 and quasi-exponentially small remainder in a potential norm. Its local-observable and dressed-density conclusions are volume-independent, not global spectral-band claims. Floquet Theorem2.3 instead controls stroboscopic local dynamics with a polynomial-in-time prefactor. The proof's support-preserving averaging step is the precise place where the onsite condition matters.

**Else, Fendley, Kemp, Nayak**, “Prethermal strong zero modes and topological qubits,” PRX7,041062 (2017), [primary](https://arxiv.org/abs/1704.08703), [DOI](https://doi.org/10.1103/PhysRevX.7.041062). Read the theorem discussion and complete Appendix A. Appendix A explicitly replaces ordinary support by strong support to extend ADHH to finite-range commuting number terms. Averaging preserves this support and its commutator algebra, so the original proof carries over. Our preceding construction verifies those conditions. Their topological zero-mode conclusions are irrelevant here and are not imported. The sign convention −JN versus+UD is harmless by taking their N=−D; integer spectrum and locality are unchanged.

**Kuwahara, Mori, Saito**, “Floquet-Magnus theory and generic transient dynamics in periodically driven many-body quantum systems,” Annals of Physics367,96–124 (2016), [primary](https://arxiv.org/abs/1508.05797). Read few-body/local-strength definitions and Theorem2. It provides an alternative rotating-frame route using finite-range interactions and Lieb-Robinson bounds. Its local reduced-state estimate concerns a truncated Floquet Hamiltonian. It does not on its own identify that Hamiltonian with a D-conserving normal form or the fourth-order ice ring operator.

## Concrete conservative candidate bound

Use the static theorem with N=D, frequency U (there is no need to exploit the factor-two period improvement). Decompose V=Vbar+Voff by averaging under exp(itD). Strong support gives ||Vbar||_kappa<=j_kappa and ||Voff||_kappa<=2j_kappa. It is sufficient to impose

U >= 18 pi j_kappa/kappa,
nu0 := 270 pi j_kappa/kappa², with U/nu0>=1,
nstar := floor[(U/nu0)/(1+log(U/nu0))³]−2 >=1.

The imported theorem/extension then supplies a quasi-local Y and K,E with

Y H Y† = U D + K + E,
[K,D]=0,
||E||_{kappa/(1+log(nstar+1))} <= 2 j_kappa (2/3)^nstar.

Constants in dressing and observable estimates are inherited theorem constants; this note does not invent numerical values for them. In dimension3, the dressed-frame local-observable error can be bounded in the form C_O exp(−r nstar)(t+t_O)^4, for fixed r<log(3/2), with constants independent of total volume. The laboratory observable must be conjugated by Y; omitting that dressing leaves a local perturbative correction of order gamma/U after fixing dimensionless geometry/norm parameters. The approximately conserved quantity is Y† D Y. Its change per volume has a bound of order gamma t exp(−c nstar), with geometry/theorem constants; it is not an exponentially precise conservation statement for bare D.

This is a candidate theorem instantiation with explicit sufficient scale definitions and published, unspecified constants for the consequences. A canonical theorem should state the norm convention and carry the strong-support extension as an explicit mathematical import.

## Rotating frame, and why it is not the whole answer

Independently, V_I(t)=exp(iUDt)V exp(−iUDt) remains on the same11-edge supports with unchanged term norms. For bit x_e and external incident counts r_i,r_j in0..5, an edge flip changes D by2(1−2x_e)(r_i+r_j−5). Thus V_I is periodic with T=pi/U. Since exp(−iUDT)=I, laboratory and rotating-frame propagators agree stroboscopically. The ordinary high-frequency theorem therefore applies without overlapping-charge concerns. Between periods retain the explicit large-field rotation and the periodic micromotion/kick; do not silently compare undressed observables.

The Fourier average conserves D, but a generic stroboscopic Floquet gauge can contain non-D-conserving higher terms. Static strong-support normal form is the route that supplies exact [K,D]=0 and dressed-D prethermal conservation; periodicity alone does not prove it.

## Remaining mechanism obligation

The effective K is quasi-local and high-order, not just the fourth-order ring term. To turn this result into a controlled local ring-only approximation, derive a local interaction-norm truncation remainder and match the normal-form gauge to the already fixed canonical ice coefficient, while dressing initial states and observables consistently. An anticipated polynomial truncation error such as C gamma^6/U^5 is NOT proved here. Even if proved, it would limit ring-only times independently of the exponentially small optimal-normal-form remainder. Bare ice initialization differs from dressed ice, and small charge density does not bound the volume-independent probability of any defect anywhere.

No global ice band remains isolated at fixed gamma/U in arbitrary volume; the previous global-norm spectral theorem stays separate. No full no-double U1 mapping, thermodynamic phase, physical temperature/preparation law, or selected coupling follows. This is a viable local-error route with an existing overlap-compatible theorem, not a new general prethermal theorem.
