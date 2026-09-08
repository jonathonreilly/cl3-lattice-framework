# Conditional explicit constants, independent check

No density data are accepted by this calculation. Assume the limiting dimensionless dissemination coefficient delta_inf=min_q 8(e_q-e_pi)/m(q) is at least 3/50. This differs from the unweighted density minimum d_*.

Each comparison loses at most E_M+log(2)/(beta*h), where E_M=3*pi^2/(8*M^2). Since 8/m<=4, delta_beta,L/h >= delta_inf-4*E_M-4*log(2)/(beta*h). At M>=32 and beta*h>=200, pi^2<10 and log(2)<7/10 give lower bound 4013/128000>3/100. The native coefficient is delta_beta,L/8, hence kappa>=3*h/800. This is an explicit large-volume bound, separate from the existential inclusion of smaller sizes.

For beta*h>=14000, 2*beta*kappa>=105. Since B=N/8>=1, 2^(11+1/B)<=4096, so p<=31*4096*exp(-105). It suffices that exp(105)>48^24*31*4096, because then 36*p^(1/24)<36/48=3/4. The exact rational Taylor sum through degree 200 verifies this strict inequality; omitted terms are positive. Thus the existing connected-set bound is <=min(1,4*(3/4)^ell). This is unconditioned and excludes any assertion about pure winding changes.

The elementary constants require no libm: pi<22/7 implies pi^2<10, and the degree-four Taylor lower bound of exp(7/10) exceeds 2, implying log(2)<7/10. No floating point calculation is load-bearing.
