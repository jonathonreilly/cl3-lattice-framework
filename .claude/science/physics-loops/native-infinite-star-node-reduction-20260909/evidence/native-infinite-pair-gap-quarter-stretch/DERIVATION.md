# Retaining the positive logarithmic contributions improves the infinite gap to h/4

Provisional extension of the reviewed native infinite pair-gap proof, with exactly the same determinant formulas and A(0)<=17/(60h²). No improved return-probability estimate or physical spectrum is needed. Put h=1 below and restore linear h scaling at the end. The earlier h/6 theorem is preserved; this strengthens only its infinite lower bound.

For opposite pairs, d_O=1-g with g=(8/9)(1-z)^2 and 1-z>=6/(s²+7). Therefore g>=32/(s²+7)^2, and -log(1-g)>=g+g²/2. Standard elementary rational integrals give

 DeltaE_O >= [4/7+40/343]/sqrt7 > (3/8)[4/7+40/343] >1/4.

The integrals used are int_0^infty ds/(s²+a²)^2=pi/(4a³) and int_0^infty ds/(s²+a²)^4=5pi/(32a^7). The prefactor is1/(2pi), with no extra parity factor. sqrt7<8/3 justifies the rational replacement. These integral identities follow by s=a tan(theta) and the elementary cosine-power recursion.

For perpendicular pairs the old exact lower contribution from0<=s<=1 is c0>0.1869996. On s>=1, the previously proved upper determinant bound yields

 -log d_P(s) >=1-d_P(s) >= (24-8/s²)/(s²+7)^2 =g_P(s)>=0.

For j=16,...,319 let a=j/16,b=(j+1)/16. On[a,b], the numerator is at least24-8/a² and the denominator at most(b²+7)^2. Thus

 c_tail=(7/44) sum_j (1/16)(24-8/a²)/(b²+7)^2

is an exact rational lower bound for the contribution over1<=s<=20. Direct rational arithmetic gives c0+c_tail>1/4. All omitted contributions beyond20 are nonnegative by the parent proof. Monotonicity of g_P itself is not assumed.

The unchanged finite-to-GNS passage therefore proves the stronger INFINITE operator inequality D_A>=h/4 for both pair classes. No explicit finite-L threshold or impurity ground vector is inferred. In the previously reviewed90word Laplace tail expression, choosing delta=h/4, beta<3h and T=100/h gives a tail below10^-6/h² by a fixed exact Taylor lower bound for exp25.

This refinement improves a calculation budget. It does not evaluate alpha, remove spatial/covariance/quadrature errors or prove a bulk interacting phase. Supporting controls are rational bounds only, not physical numerical data.
