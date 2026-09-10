# A posterior Ward error certificate from computed trial-state norms

Status: exact-support, source-only proof candidate. This changes the residual error estimator; it does not determine alpha and is outside the fixed-estimator all-q exclusion. No accepted scalar or event arrays have been evaluated for this bound.

Use the same supplied native model, Gaussian reference, gap delta=h/4, direct sum of15 pair channels, Kneser adjacency T with norm6, and diagonal unitary g as the finite-moment Ward hierarchy. Write the exact coefficient as

 8 alpha = Re(<x,T x> - <x,T g v>).

Let xhat and vhat be the already defined polynomial trial vectors, with ||x-xhat|| <= E and ||v-vhat|| <= F. Let a=||xhat|| and b=||vhat||. Existing global bounds are ||x||<=X=sqrt15/delta and ||v||<=V=j sqrt15/delta². Define

 chi=min(X,a+E), psi=min(V,b+F).

Both bound the corresponding exact norms. The quadratic term obeys, by polarization and self-adjointness,

 |Re(<x,T x>-<xhat,T xhat>)| <= 6 E(a+chi).

Indeed its difference is the real part of <x-xhat,T(x+xhat)>. For the mixed term there are two decompositions:

 <x,Tgv>-<xhat,Tgvhat>
 = <x-xhat,Tgvhat> + <x,Tg(v-vhat)>
 = <x-xhat,Tgv> + <xhat,Tg(v-vhat)>.

Their respective bounds are6(E b+chi F) and6(E psi+a F). Thus

 |8 alpha - What| <=
 6 [ E(a+chi) + min(E b+chi F, E psi+a F) ].        (P)

This is valid without independence of the two residuals, without a norm bound on the unbounded polynomial q(D), and without replacing a signed interval by a central estimate. An even simpler valid bound drops the global estimates:

 6 [ E(2a+E+b) + (a+E)F ].                        (P0)

For interval certification, use outward upper bounds aU,bU,EU,FU,XU,VU. Set chiU=min(XU,aU+EU) and psiU=min(VU,bU+FU). Every term in(P) is increasing in its nonnegative inputs, so substituting those bounds gives a valid upper error. The accepted nominal interval must be expanded by that error before division by8. A strict sign gate requires the resulting lower endpoint>0 or upper endpoint<0.

## Available trial norms for constant second polynomial

For all already considered degree-(p,0) trials, vhat_A=q_A J_A p_A(D_A)Omega. The source norm s0_A=||J_A p_A(D_A)Omega||² was already recorded. Since J_A*J_A=8h²I,

 a²=(12 s0_P+3 s0_O)/(8h²),
 b²=12 q_P² s0_P+3 q_O² s0_O.

Therefore(P) needs no new native moment or oracle for the degree-(1,0) or degree-(2,0) protocols. A NEW bounded saved-data protocol must authenticate original result/events/root and extract these particular fields before evaluating the new estimator. It must not rerun the original moment/Wick calculations. The degree20 protocol still uses its originally frozen error estimator; this proposal does not alter an already preregistered calculation.

## Narrow trace

The downstream consumer is the full coefficient sign gate. This can reduce conservative uncertainty using norms of the actual trial vectors. There is no proof that it is numerically sufficient at any given degree. The completed all-q screen excludes improving q alone under the older estimator, and does not exclude(P). Native model selection, alpha's sign, and independent integration/audit remain open.
