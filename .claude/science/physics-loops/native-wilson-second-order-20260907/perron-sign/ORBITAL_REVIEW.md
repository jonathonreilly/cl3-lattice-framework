# Independent negative Perron sign proof review

Verdict: PASS. Reviewed native `perron-sign/NEGATIVE_SIGN_PROOF.md` and scalar certificate, after independently recording the radial normalization and positive-operator strategy in INDEPENDENT_PRECHECK.md. No Nyström JSON or eigenvector was used. The draft itself quotes a diagnostic value; that sentence plays no part in this review.

## Independently recomputed analytic steps

The metric Q transformation has Jacobian 2/sqrt(3), wedge angle pi/3, and H=r³ sin(3theta)/(3sqrt(3)). Angular integrals are integral sin(3theta)=2/3 and integral sin²(3theta)=pi/6. With q=r² these give exactly integral H F(Q)=(2/27) integral q^(3/2)F(q), integral H exp(-aQ)=sqrt(pi)/(18a^(5/2)), and integral H² exp(-aQ)=pi/(27sqrt(3)a^4). The heat diagonal sqrt(3)/(2pi) follows from det diffusion matrix=1/12. Killed heat is bounded by free heat. Thus the trace prefactor sqrt(3)/(27pi) is correct; no plane-versus-chamber factor is missing.

The pointwise bound on g is valid in each of the three intervals. On [0,2/3], the difference from 1-3q/2 is q(q-1)/4<=0. On [2/3,6], the convex quadratic is negative at both endpoints. Above6, the difference from q(q-6)/4 is 1-q/4<=0. Although g actually turns positive only above the larger irrational root, using6 is an honest upper estimate.

The low integral after dropping exp(-q) is (4/35)(2/3)^(5/2)<1/24. Above6 the square-root tangent inequality gives the polynomial 36s+15s²+2s³+s^4/12, whose exponential integral is80. Therefore the high contribution is <=20sqrt(6)e^-6<1/8 from sqrt(6)<5/2 and the positive Taylor lower bound e^6>400. Combining with sqrt(3)<7/4 and pi>3 gives J<7/1944. These constants were independently checked using exact Fractions in check.py; no native module was imported.

For the heat trial, LQ=1, the quadratic diffusion form of grad Q is Q, LH=0, and homogeneity gives the cross term 3H. Hence L[H exp(-aQ)]=(a²Q-4a)H exp(-aQ), which verifies (1+t)^-4 H exp[-Q/(1+t)]. The displayed function has the required Dirichlet wall values and Gaussian decay; odd Weyl extension or heat uniqueness identifies it with the semigroup. The Rayleigh quotient is (1/16)[pi/(27sqrt(3))](2/3)^4/[sqrt(pi)/18]=2sqrt(pi)/(243sqrt(3))>2/243. This is a lower bound for mu, not a substitution for its eigenvector.

For the actual normalized Perron vector u, B>=mu|u><u| follows from positive spectral decomposition. Bounded truncations g_n justify the trace inequality, and the derived finite trace allows monotone convergence. This also supplies the required positive moment integrability; R is bounded below. Thus r<=-1+J/mu<-9/16. Its strict lower bound -49/16 follows because the equality ellipse has zero two-dimensional Lebesgue measure and a normalized L² function cannot be supported there. Multiplication by the positive mu lower bound gives d0<-1/216 with the correct inequality orientation.

## Scope

The proof is analytic and does not require a numerical spectral-gap estimate, eigenvector enclosure, or quadrature. It uses the previously established Perron existence/normalization and the exact Dirichlet heat operator. The eventual top-to-top ordering is conditional on the previously proved operator/Perron limit and has no certified finite-beta onset. It does not determine an excited ratio, full fixed-heat expansion, or physical mass gap. The negative top matrix element is fully compatible with the previously proved indefinite correction operator.

No corrections required. The elementary exact script supports arithmetic only; the continuum heat/trace argument remains a source proof, not something certified by the seven arithmetic assertions.
